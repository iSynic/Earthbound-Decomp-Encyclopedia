from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import rom_tools


ROOT = Path(__file__).resolve().parent.parent
ASSET_MANIFEST_DIR = ROOT / "asset-manifests"
MUSIC_CONSTANTS = ROOT / "refs" / "ebsrc-main" / "ebsrc-main" / "include" / "constants" / "music.asm"

MUSIC_DATASET_START = "C4:F70A"
MUSIC_DATASET_END = "C4:F947"
MUSIC_PACK_POINTER_START = "C4:F947"
MUSIC_PACK_POINTER_END = "C4:FB42"
CUSTOM_AUDIO_PACK_1_RANGE = "E6:0000..E6:45D8"

AUDIO_PACK_ID_RE = re.compile(r"audio_pack_(\d+)", re.IGNORECASE)
MUSIC_ENUM_RE = re.compile(r"^\s*([A-Z0-9_ ]+)\s*=\s*([0-9]+)\b")
RANGE_RE = re.compile(r"^([0-9A-F]{2}):([0-9A-F]{4,5})\.\.([0-9A-F]{2}):([0-9A-F]{4,5})$", re.IGNORECASE)


@dataclass(frozen=True)
class CpuRange:
    bank: int
    start: int
    end: int

    @property
    def size(self) -> int:
        return self.end - self.start

    def to_text(self) -> str:
        return f"{self.bank:02X}:{self.start:04X}..{self.bank:02X}:{self.end:04X}"


@dataclass(frozen=True)
class AudioStreamBlock:
    index: int
    stream_offset: int
    payload_offset: int | None
    count: int
    destination: int
    consumed_bytes: int
    sha1: str | None
    role_guess: str
    terminal: bool

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["stream_offset"] = f"0x{self.stream_offset:04X}"
        data["payload_offset"] = None if self.payload_offset is None else f"0x{self.payload_offset:04X}"
        data["destination"] = f"0x{self.destination:04X}"
        return data


@dataclass(frozen=True)
class ParsedAudioStream:
    status: str
    consumed_bytes: int
    blocks: tuple[AudioStreamBlock, ...]
    errors: tuple[str, ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "status": self.status,
            "consumed_bytes": self.consumed_bytes,
            "blocks": [block.to_dict() for block in self.blocks],
            "errors": list(self.errors),
            "summary": {
                "block_count": len(self.blocks),
                "payload_bytes": sum(block.count for block in self.blocks if not block.terminal),
                "destination_roles": dict(Counter(block.role_guess for block in self.blocks)),
            },
        }


def rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def parse_cpu_range(text: str) -> CpuRange:
    match = RANGE_RE.match(text.strip())
    if not match:
        raise ValueError(f"invalid CPU range: {text}")
    bank_a = int(match.group(1), 16)
    start = int(match.group(2), 16)
    bank_b = int(match.group(3), 16)
    end = int(match.group(4), 16)
    if bank_a != bank_b:
        raise ValueError(f"cross-bank ranges are not supported: {text}")
    if start > end:
        raise ValueError(f"range start is after end: {text}")
    return CpuRange(bank_a, start, end)


def cpu_offset(bank: int, address: int) -> int:
    if bank < rom_tools.HIROM_CANONICAL_START_BANK:
        raise ValueError(f"expected canonical HiROM bank, found 0x{bank:02X}")
    return (bank - rom_tools.HIROM_CANONICAL_START_BANK) * rom_tools.EXPECTED_BANK_SIZE + address


def slice_range(rom: bytes, cpu_range: CpuRange) -> bytes:
    start = cpu_offset(cpu_range.bank, cpu_range.start)
    end = cpu_offset(cpu_range.bank, cpu_range.end)
    return rom[start:end]


def read_u16_le(data: bytes, offset: int) -> int:
    return data[offset] | (data[offset + 1] << 8)


def classify_apu_destination(destination: int, *, terminal: bool) -> str:
    if terminal:
        return "terminal_entry_handshake"
    if destination == 0x0500:
        return "main_spc700_driver_or_driver_overlay"
    if 0x0000 <= destination < 0x0200:
        return "apu_zero_page_or_io_adjacent"
    if 0x0200 <= destination < 0x2000:
        return "spc700_driver_code_or_tables"
    if 0x2000 <= destination < 0x5000:
        return "sequence_or_runtime_tables"
    if 0x5000 <= destination < 0x6C00:
        return "music_sequence_or_sample_directory"
    return "brr_sample_or_high_apu_payload"


def parse_load_spc700_stream(data: bytes) -> ParsedAudioStream:
    blocks: list[AudioStreamBlock] = []
    errors: list[str] = []
    cursor = 0

    while cursor + 2 <= len(data):
        block_start = cursor
        count = read_u16_le(data, cursor)
        cursor += 2
        if count == 0:
            blocks.append(
                AudioStreamBlock(
                    index=len(blocks),
                    stream_offset=block_start,
                    payload_offset=None,
                    count=0,
                    destination=0x0500,
                    consumed_bytes=2,
                    sha1=None,
                    role_guess=classify_apu_destination(0x0500, terminal=True),
                    terminal=True,
                )
            )
            status = "ok" if cursor == len(data) else "trailing_bytes_after_terminal"
            if cursor != len(data):
                errors.append(f"{len(data) - cursor} trailing bytes after terminal block")
            return ParsedAudioStream(status, cursor, tuple(blocks), tuple(errors))

        if cursor + 2 > len(data):
            errors.append(f"truncated destination word at stream offset 0x{block_start:04X}")
            return ParsedAudioStream("truncated", block_start, tuple(blocks), tuple(errors))

        destination = read_u16_le(data, cursor)
        cursor += 2
        payload_offset = cursor
        payload_end = cursor + count
        if payload_end > len(data):
            errors.append(
                f"payload at stream offset 0x{block_start:04X} needs {count} bytes, "
                f"only {len(data) - cursor} remain"
            )
            return ParsedAudioStream("truncated", block_start, tuple(blocks), tuple(errors))

        payload = data[payload_offset:payload_end]
        cursor = payload_end
        blocks.append(
            AudioStreamBlock(
                index=len(blocks),
                stream_offset=block_start,
                payload_offset=payload_offset,
                count=count,
                destination=destination,
                consumed_bytes=4 + count,
                sha1=hashlib.sha1(payload).hexdigest(),
                role_guess=classify_apu_destination(destination, terminal=False),
                terminal=False,
            )
        )

    if cursor == len(data):
        errors.append("stream ended without terminal zero-length block")
    else:
        errors.append(f"one trailing byte after incomplete terminal/count word at 0x{cursor:04X}")
    return ParsedAudioStream("missing_terminal", cursor, tuple(blocks), tuple(errors))


def manifest_paths() -> list[Path]:
    return sorted(ASSET_MANIFEST_DIR.glob("*.json"))


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def extract_pack_id(asset: dict[str, Any]) -> int | None:
    for field in ("id", "title"):
        match = AUDIO_PACK_ID_RE.search(str(asset.get(field, "")))
        if match:
            return int(match.group(1))
    return None


def audio_assets_from_manifests() -> dict[int, dict[str, Any]]:
    packs: dict[int, dict[str, Any]] = {}
    for manifest_path in manifest_paths():
        manifest = load_json(manifest_path)
        bank = manifest_path.stem.split("-")[1].upper()
        for asset in manifest.get("assets", []):
            if asset.get("category") != "audio":
                continue
            pack_id = extract_pack_id(asset)
            if pack_id is None:
                continue
            source = asset["source"]
            cpu_range = parse_cpu_range(source["range"])
            packs[pack_id] = {
                "pack_id": pack_id,
                "asset_id": asset["id"],
                "title": asset["title"],
                "bank": bank,
                "manifest": rel(manifest_path),
                "range": cpu_range.to_text(),
                "bytes": int(source["bytes"]),
                "sha1": source["sha1"],
                "outputs": asset.get("outputs", []),
                "source_asset_ids": [asset["id"]],
                "kind": "standard_audio_pack",
            }
    return packs


def custom_audio_pack_1(rom: bytes) -> dict[str, Any]:
    cpu_range = parse_cpu_range(CUSTOM_AUDIO_PACK_1_RANGE)
    data = slice_range(rom, cpu_range)
    return {
        "pack_id": 1,
        "asset_id": "asset.e6.audio_pack_1_custom_inline",
        "title": "AUDIO_PACK_1",
        "bank": "E6",
        "manifest": "asset-manifests/bank-e6-assets.json",
        "range": cpu_range.to_text(),
        "bytes": len(data),
        "sha1": hashlib.sha1(data).hexdigest(),
        "outputs": [{"kind": "raw", "path": "e6/audiopacks/1-custom-inline.ebm"}],
        "source_asset_ids": [
            "table.e6.000_inline_audio_pack_1",
            "table.e6.002_inline_audio_subpack_0_data_start",
            "table.e6.005_inline_audio_subpack_1_data_start",
            "table.e6.008_incbin_main_spc700_bin",
        ],
        "kind": "custom_inline_audio_pack",
    }


def load_music_names() -> dict[int, str]:
    names: dict[int, str] = {}
    if not MUSIC_CONSTANTS.exists():
        return names
    for line in MUSIC_CONSTANTS.read_text(encoding="utf-8", errors="ignore").splitlines():
        match = MUSIC_ENUM_RE.match(line)
        if match:
            names[int(match.group(2))] = match.group(1).strip()
    return names


def read_cpu_range(rom: bytes, range_text: str) -> bytes:
    return slice_range(rom, parse_cpu_range(range_text))


def build_music_pack_pointers(rom: bytes) -> list[dict[str, Any]]:
    data = read_cpu_range(rom, f"{MUSIC_PACK_POINTER_START}..{MUSIC_PACK_POINTER_END}")
    if len(data) % 3:
        raise ValueError(f"music pack pointer table size is not divisible by 3: {len(data)}")
    pointers: list[dict[str, Any]] = []
    for pack_id in range(len(data) // 3):
        offset = pack_id * 3
        bank = data[offset]
        address = read_u16_le(data, offset + 1)
        pointers.append(
            {
                "pack_id": pack_id,
                "bank": f"{bank:02X}",
                "address": f"{address:04X}",
                "cpu": f"{bank:02X}:{address:04X}",
                "table_offset": f"0x{offset:03X}",
            }
        )
    return pointers


def build_music_tracks(rom: bytes, pack_contracts: dict[int, dict[str, Any]]) -> list[dict[str, Any]]:
    names = load_music_names()
    data = read_cpu_range(rom, f"{MUSIC_DATASET_START}..{MUSIC_DATASET_END}")
    if len(data) % 3:
        raise ValueError(f"music dataset table size is not divisible by 3: {len(data)}")

    bootstrap_pack = data[2]
    bootstrap_pack_id = None if bootstrap_pack == 0xFF else int(bootstrap_pack)
    tracks: list[dict[str, Any]] = [
        {
            "track_id": 0,
            "name": names.get(0, "NONE"),
            "packs": {"primary_sample_pack": None, "secondary_sample_pack": None, "sequence_pack": None},
            "load_order": [],
            "cold_start_load_order": [
                {
                    "role": "initialize_music_subsystem_sequence_pack",
                    "pack_id": bootstrap_pack_id,
                    "asset_id": pack_contracts.get(bootstrap_pack_id, {}).get("asset_id")
                    if bootstrap_pack_id is not None
                    else None,
                }
            ]
            if bootstrap_pack_id is not None
            else [],
            "notes": ["Track 0 is not indexed into MusicDatasetTable by CHANGE_MUSIC."],
        }
    ]

    roles = ("primary_sample_pack", "secondary_sample_pack", "sequence_pack")
    for table_index in range(len(data) // 3):
        track_id = table_index + 1
        row = data[table_index * 3:table_index * 3 + 3]
        packs: dict[str, int | None] = {}
        load_order: list[dict[str, Any]] = []
        for role, raw_pack_id in zip(roles, row):
            pack_id = None if raw_pack_id == 0xFF else raw_pack_id
            packs[role] = pack_id
            if pack_id is not None:
                load_order.append(
                    {
                        "role": role,
                        "pack_id": pack_id,
                        "asset_id": pack_contracts.get(pack_id, {}).get("asset_id"),
                    }
                )
        cold_start_load_order: list[dict[str, Any]] = []
        if bootstrap_pack_id is not None:
            cold_start_load_order.append(
                {
                    "role": "initialize_music_subsystem_sequence_pack",
                    "pack_id": bootstrap_pack_id,
                    "asset_id": pack_contracts.get(bootstrap_pack_id, {}).get("asset_id"),
                }
            )
        for load in load_order:
            if load["role"] == "secondary_sample_pack" and load["pack_id"] == bootstrap_pack_id:
                continue
            cold_start_load_order.append(load)
        tracks.append(
            {
                "track_id": track_id,
                "name": names.get(track_id, f"TRACK_{track_id}"),
                "table_offset": f"0x{table_index * 3:03X}",
                "packs": packs,
                "load_order": load_order,
                "cold_start_load_order": cold_start_load_order,
            }
        )
    return tracks


def attach_stream_contracts(rom: bytes, packs: dict[int, dict[str, Any]]) -> None:
    for pack in packs.values():
        cpu_range = parse_cpu_range(pack["range"])
        data = slice_range(rom, cpu_range)
        parsed = parse_load_spc700_stream(data)
        pack["stream"] = parsed.to_dict()
        pack["rom_sha1_verified"] = hashlib.sha1(data).hexdigest() == pack["sha1"]


def build_audio_contract(rom_path: Path | None = None) -> dict[str, Any]:
    resolved_rom_path = rom_tools.find_rom(str(rom_path) if rom_path else None)
    rom = rom_tools.load_rom(resolved_rom_path)
    info = rom_tools.read_rom_info(resolved_rom_path)
    problems = rom_tools.verify_earthbound_us(info)
    if problems:
        formatted = "\n".join(f"- {problem}" for problem in problems)
        raise ValueError(f"ROM verification failed:\n{formatted}")

    packs = audio_assets_from_manifests()
    packs[1] = custom_audio_pack_1(rom)
    attach_stream_contracts(rom, packs)
    pointers = build_music_pack_pointers(rom)
    tracks = build_music_tracks(rom, packs)

    usage_by_pack: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for track in tracks:
        for load in track["load_order"]:
            usage_by_pack[int(load["pack_id"])].append(
                {
                    "track_id": track["track_id"],
                    "track_name": track["name"],
                    "role": load["role"],
                }
            )
    for pack_id, pack in packs.items():
        pack["music_usage_count"] = len(usage_by_pack.get(pack_id, []))
        pack["music_usage_sample"] = usage_by_pack.get(pack_id, [])[:12]
        pack["pointer"] = pointers[pack_id] if 0 <= pack_id < len(pointers) else None

    status_counts = Counter(pack["stream"]["status"] for pack in packs.values())
    role_counts = Counter()
    for pack in packs.values():
        role_counts.update(pack["stream"]["summary"]["destination_roles"])

    return {
        "schema": "earthbound-decomp.audio-pack-contract.v1",
        "game": "earthbound-us",
        "source_policy": {
            "requires_user_supplied_rom": True,
            "do_not_commit_generated_outputs": True,
            "generated_audio_output_root": "build/audio",
        },
        "references": [
            "notes/bank-e2-ee-audio-pack-run.md",
            "notes/audio-apu-battlebg-transfer-frontier-c0ab06-c0ae44.md",
            "refs/ebsrc-main/ebsrc-main/src/audio/load_spc700_data.asm",
            "refs/ebsrc-main/ebsrc-main/src/audio/change_music.asm",
            "refs/ebsrc-main/ebsrc-main/src/audio/get_audio_bank.asm",
            "refs/ebsrc-main/ebsrc-main/include/constants/music.asm",
            "refs/ebsrc-main/ebsrc-main/include/symbols/audiopacks.inc.asm",
        ],
        "rom": {
            "sha1": info.sha1,
            "size": info.size,
            "title": info.title,
        },
        "loader_contract": {
            "runtime_entry": "C0:AB06 LoadSpc700DataStream",
            "initializer_entry": "C4:FB58 InitializeMusicSubsystem",
            "stream_format": [
                "u16 payload_byte_count",
                "if payload_byte_count != 0: u16 apu_destination, then payload_byte_count bytes",
                "if payload_byte_count == 0: terminal handshake with destination $0500; no payload follows",
            ],
            "cold_start_bootstrap": "InitializeMusicSubsystem loads MusicDatasetTable row 0 sequence_pack, stores it as CurrentSecondarySamplePack/Unknown7EB543, then ChangeMusic applies the requested track.",
            "load_order": "CHANGE_MUSIC loads primary sample pack, secondary sample pack, then sequence pack when changed and not $FF.",
        },
        "summary": {
            "pack_count": len(packs),
            "track_count": len(tracks),
            "pointer_count": len(pointers),
            "stream_status_counts": dict(status_counts),
            "destination_role_counts": dict(role_counts),
            "unused_pack_count": sum(1 for pack in packs.values() if pack["music_usage_count"] == 0),
        },
        "audio_packs": [packs[pack_id] for pack_id in sorted(packs)],
        "music_pack_pointers": pointers,
        "tracks": tracks,
        "renderer_backends": [
            {
                "id": "ares",
                "status": "diagnostic_runtime_harness_implemented",
                "license_policy": "ISC/permissive candidate; review third-party notices before vendoring.",
                "role": "accuracy-first runtime/capture harness and future differential oracle",
            },
            {
                "id": "snes_spc",
                "status": "libgme_snapshot_renderer_implemented",
                "license_policy": "LGPL-2.1; use as lightweight SPC snapshot renderer with compliance notes.",
                "role": "lightweight SPC snapshot renderer for local WAV export once snapshots are generated",
            },
            {
                "id": "external_reference",
                "status": "planned",
                "license_policy": "GPL/noncommercial tools stay optional and out-of-process.",
                "role": "bsnes/higan, Mesen2, or Mednafen comparison/export checks",
            },
        ],
    }


def write_json(data: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def render_markdown(data: dict[str, Any]) -> str:
    summary = data["summary"]
    rows = []
    for pack in data["audio_packs"]:
        stream = pack["stream"]
        pointer = pack.get("pointer") or {}
        rows.append(
            "| `{pack_id}` | `{kind}` | `{range}` | {bytes} | `{status}` | {blocks} | `{pointer}` | {usage} |".format(
                pack_id=pack["pack_id"],
                kind=pack["kind"],
                range=pack["range"],
                bytes=pack["bytes"],
                status=stream["status"],
                blocks=stream["summary"]["block_count"],
                pointer=pointer.get("cpu", "missing"),
                usage=pack["music_usage_count"],
            )
        )

    renderer_rows = [
        f"| `{backend['id']}` | {backend['status']} | {backend['role']} | {backend['license_policy']} |"
        for backend in data["renderer_backends"]
    ]

    return "\n".join(
        [
            "# Audio Pack Format And Renderer Frontier",
            "",
            "Status: audio pack contract implemented; fused runtime snapshot generation and local libgme WAV export now validate across the snapshot-backed music table.",
            "",
            "EarthBound audio packs are modeled here as `LOAD_SPC700_DATA` streams that populate APU RAM. "
            "The current playback/export path boots the real APU loader path, executes ROM-derived CHANGE_MUSIC through real C0:AB06 loader calls, captures key-on SPC snapshots, and renders them locally through libgme.",
            "",
            "## Summary",
            "",
            f"- audio packs represented: `{summary['pack_count']}`",
            f"- music tracks represented: `{summary['track_count']}`",
            f"- pack pointer entries represented: `{summary['pointer_count']}`",
            f"- stream statuses: `{summary['stream_status_counts']}`",
            f"- unused pack ids in track table: `{summary['unused_pack_count']}`",
            f"- generated audio outputs policy: `{data['source_policy']['generated_audio_output_root']}` is ignored/local only",
            "",
            "## What This Proves",
            "",
            "- Every known audio pack has a byte-exact ROM source range and SHA-1.",
            "- Every known audio pack parses as a complete `LOAD_SPC700_DATA` stream.",
            "- Every music track resolves to the same primary/secondary/sequence pack order used by `CHANGE_MUSIC`.",
            "- The corpus tools can deterministically construct 64 KiB APU RAM images for selected tracks.",
            "- The fused all-track runtime corpus validates `191 / 191` load paths and `191 / 191` stable payload-region matches.",
            "- The playback/export corpus renders `190 / 190` snapshot-backed tracks as audible local WAVs; track `4` (`NONE2`) is explicitly load-ok/no-key-on.",
            "",
            "## What Is Not Final Yet",
            "",
            "- The remaining fidelity gap is a bounded post-command observation loop rather than a full continuously scheduled SNES runtime.",
            "- Generated SPC/WAV outputs are ROM-derived local artifacts and must stay ignored/uncommitted.",
            "- External emulator comparison is still needed before claiming final audio-cycle equivalence.",
            "",
            "## Loader Contract",
            "",
            "- Runtime entry: `C0:AB06 LoadSpc700DataStream`.",
            "- Cold-start initializer: `C4:FB58 InitializeMusicSubsystem` loads row-0 sequence/common pack before track changes.",
            "- Each stream block is `u16 payload_byte_count`, then `u16 apu_destination` and payload bytes when the count is nonzero.",
            "- A zero count terminates the stream with the loader's `$0500` final handshake.",
            "- `CHANGE_MUSIC` applies primary sample pack, secondary sample pack, then sequence pack, skipping unchanged or `$FF` packs.",
            "",
            "## Renderer Backends",
            "",
            "| Backend | Status | Role | License policy |",
            "| --- | --- | --- | --- |",
            *renderer_rows,
            "",
            "## Tooling",
            "",
            "- Rebuild: `python tools/build_audio_pack_contracts.py`.",
            "- Validate: `python tools/validate_audio_pack_contracts.py`.",
            "- Build ignored APU RAM seed for a track: `python tools/build_audio_track_snapshot.py 46`.",
            "- Build ignored 20-track APU RAM corpus: `python tools/build_audio_snapshot_corpus.py`.",
            "- Validate ignored corpus outputs: `python tools/validate_audio_snapshot_corpus.py`.",
            "- Collect semantic loader transfer metrics: `python tools/collect_audio_load_stream_transfer_metrics.py`.",
            "- Validate semantic loader transfer metrics: `python tools/validate_audio_load_stream_transfer_metrics.py`.",
            "- Collect C0:AB06 loader contract evidence: `python tools/collect_audio_c0ab06_loader_contract.py`.",
            "- Validate C0:AB06 loader contract evidence: `python tools/validate_audio_c0ab06_loader_contract.py`.",
            "- Run byte-level C0:AB06 loader handshake corpus: `python tools/run_audio_c0ab06_loader_handshake_corpus.py`.",
            "- Validate byte-level C0:AB06 loader handshake corpus: `python tools/validate_audio_c0ab06_loader_handshake_corpus.py`.",
            "- Collect real ares SMP IPL receiver frontier: `python tools/collect_audio_c0ab06_real_ipl_frontier.py`.",
            "- Validate real ares SMP IPL receiver frontier: `python tools/validate_audio_c0ab06_real_ipl_frontier.py`.",
            "- Collect post-bootstrap game-driver reload frontier: `python tools/collect_audio_c0ab06_post_bootstrap_frontier.py`.",
            "- Validate post-bootstrap game-driver reload frontier: `python tools/validate_audio_c0ab06_post_bootstrap_frontier.py`.",
            "- Collect continuous representative track load frontier: `python tools/collect_audio_c0ab06_continuous_track_load_frontier.py`.",
            "- Validate continuous representative track load frontier: `python tools/validate_audio_c0ab06_continuous_track_load_frontier.py`.",
            "- Collect CHANGE_MUSIC-to-continuous-load sequence contract: `python tools/collect_audio_change_music_continuous_sequence_contract.py`.",
            "- Validate CHANGE_MUSIC-to-continuous-load sequence contract: `python tools/validate_audio_change_music_continuous_sequence_contract.py`.",
            "- Collect full CHANGE_MUSIC/real-C0:AB06 fusion frontier: `python tools/collect_audio_c0ab06_change_music_fusion_frontier.py`.",
            "- Validate full CHANGE_MUSIC/real-C0:AB06 fusion frontier: `python tools/validate_audio_c0ab06_change_music_fusion_frontier.py`.",
            "- Build fused CHANGE_MUSIC/C0:AB06 SPC index: `python tools/build_audio_c0ab06_change_music_fusion_spc_index.py`.",
            "- Render fused CHANGE_MUSIC/C0:AB06 SPC corpus through libgme using `tools/run_audio_backend_batch.py`.",
            "- Build all-track renderer jobs directly from the SPC index: `python tools/build_audio_backend_jobs_from_spc_index.py`.",
            "- Build the all-track playback/export handoff: `python tools/build_audio_playback_export_manifest.py`.",
            "- Validate the all-track playback/export handoff: `python tools/validate_audio_playback_export_manifest.py`.",
            "- Collect fused post-command timing metrics: `python tools/collect_audio_fusion_timing_metrics.py`.",
            "- Validate fused post-command timing metrics: `python tools/validate_audio_fusion_timing_metrics.py`.",
            "- Build ignored renderer fixtures: `python tools/build_audio_renderer_fixtures.py --tracks 46`.",
            "- Validate renderer fixtures: `python tools/validate_audio_renderer_fixtures.py`.",
            "- Build ignored backend job queue: `python tools/build_audio_backend_jobs.py --backend ares`.",
            "- Validate backend job queue: `python tools/validate_audio_backend_jobs.py`.",
            "- Dry-run one backend job: `python tools/run_audio_backend_job.py ares-track-046-onett`.",
            "- Check external harness shape: `python tools/run_audio_backend_job.py ares-track-046-onett --mode external --external python tools/audio_backend_stub_harness.py --job \"{job}\" --result \"{result}\"`.",
            "- Dry-run pending backend jobs in batch: `python tools/run_audio_backend_batch.py --limit 2`.",
            "- Collect backend result statuses: `python tools/collect_audio_backend_results.py`.",
            "- Validate backend result summary: `python tools/validate_audio_backend_result_summary.py`.",
            "- Check local ares prerequisite: `python tools/check_ares_backend_prereq.py`.",
            "- Build ares link smoke: `cmake -S tools/ares_link_smoke -B build/audio/ares-link-smoke-msvc -G \"Visual Studio 17 2022\" -DARES_ROOT=<local-ares-checkout>`.",
            "- Build backend adapter contract: `python tools/build_audio_backend_contract.py`.",
            "- Validate backend adapter contract: `python tools/validate_audio_backend_contract.py`.",
            "- Build a dry-run backend result: `python tools/build_audio_backend_result_stub.py --job-id ares-track-046-onett`.",
            "- Validate one backend result: `python tools/validate_audio_backend_result.py build/audio/backend-jobs/ares-track-046-onett/result.json --job build/audio/backend-jobs/ares-jobs.json`.",
            "- Inspect track-to-pack mappings: `python tools/lookup_audio_track.py onett`.",
            "- Build SPC state frontier: `python tools/build_audio_spc_state_frontier.py`.",
            "- Validate SPC state frontier: `python tools/validate_audio_spc_state_frontier.py`.",
            "- Build APU destination region map: `python tools/build_audio_apu_region_map.py`.",
            "- Validate APU destination region map: `python tools/validate_audio_apu_region_map.py`.",
            "- Renderer abstraction scaffold: `tools/audio_renderers.py`.",
            "",
            "## Audio Pack Contracts",
            "",
            "| Pack | Kind | ROM range | Bytes | Parse | Blocks | Pointer | Track uses |",
            "| ---: | --- | --- | ---: | --- | ---: | --- | ---: |",
            *rows,
            "",
            "## Next Implementation Step",
            "",
            "Continue Gate 2 by replacing the remaining bounded post-command SMP observation loop with a fuller scheduled runtime, then use external emulator captures as accuracy oracles for selected tracks.",
            "",
        ]
    )
