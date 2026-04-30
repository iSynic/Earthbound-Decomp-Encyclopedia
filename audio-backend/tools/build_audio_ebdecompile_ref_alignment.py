#!/usr/bin/env python3
"""Align eb-decompile music references with this project's audio contracts."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import audio_pack_contracts
import rom_tools


DEFAULT_CONTRACT = ROOT / "manifests" / "audio-pack-contracts.json"
DEFAULT_MANIFEST = ROOT / "manifests" / "audio-ebdecompile-ref-alignment.json"
DEFAULT_NOTES = ROOT / "notes" / "audio-ebdecompile-ref-alignment.md"
EBCOMP_MUSIC_ROOT = ROOT / "refs" / "eb-decompile-4ef92" / "Music"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build eb-decompile audio reference alignment.")
    parser.add_argument("--contract", default=str(DEFAULT_CONTRACT), help="Audio pack contract JSON.")
    parser.add_argument("--rom", help="Optional explicit EarthBound US ROM path.")
    parser.add_argument("--output", default=str(DEFAULT_MANIFEST), help="Manifest output JSON.")
    parser.add_argument("--notes", default=str(DEFAULT_NOTES), help="Markdown note output.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_hex_int(text: str) -> int:
    return int(text, 16)


def read_u16_le(data: bytes, offset: int) -> int:
    return data[offset] | (data[offset + 1] << 8)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def parse_songs_yml(path: Path) -> dict[int, dict[str, str]]:
    entries: dict[int, dict[str, str]] = {}
    current_track: int | None = None
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("0x") and stripped.endswith(":"):
            current_track = int(stripped[:-1], 16)
            entries[current_track] = {}
            continue
        if current_track is None or ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        entries[current_track][key.strip()] = value.strip()
    return entries


def block_payload(rom: bytes, pack: dict[str, Any], block: dict[str, Any]) -> bytes:
    payload_offset = block.get("payload_offset")
    if payload_offset is None:
        return b""
    data = audio_pack_contracts.slice_range(rom, audio_pack_contracts.parse_cpu_range(pack["range"]))
    offset = parse_hex_int(payload_offset)
    return data[offset:offset + int(block["count"])]


def sequence_block_index(contract: dict[str, Any], rom: bytes) -> dict[tuple[str, int, int], list[dict[str, Any]]]:
    index: dict[tuple[str, int, int], list[dict[str, Any]]] = {}
    for pack in contract["audio_packs"]:
        for block in pack["stream"]["blocks"]:
            if block.get("terminal"):
                continue
            if block["role_guess"] not in {"sequence_or_runtime_tables", "music_sequence_or_sample_directory"}:
                continue
            payload = block_payload(rom, pack, block)
            key = (hashlib.sha1(payload).hexdigest(), int(block["count"]), parse_hex_int(block["destination"]))
            index.setdefault(key, []).append(
                {
                    "pack_id": int(pack["pack_id"]),
                    "pack_range": pack["range"],
                    "block_index": int(block["index"]),
                    "destination": block["destination"],
                    "bytes": int(block["count"]),
                    "payload_sha1": block["sha1"],
                }
            )
    return index


def ref_song_path(entry: dict[str, str]) -> Path | None:
    song_pack = entry.get("Song Pack")
    song_file = entry.get("Song File")
    if not song_pack or not song_file or song_pack == "in-engine":
        return None
    return EBCOMP_MUSIC_ROOT / "Packs" / song_pack[2:].upper().zfill(2) / song_file


def in_engine_candidates(entry: dict[str, str]) -> list[str]:
    song_file = entry.get("Song File")
    if not song_file:
        return []
    return [rel(path) for path in sorted((EBCOMP_MUSIC_ROOT / "Packs").glob(f"*/{song_file}"))]


def build_alignment(contract: dict[str, Any], rom: bytes) -> dict[str, Any]:
    songs_path = EBCOMP_MUSIC_ROOT / "songs.yml"
    songs = parse_songs_yml(songs_path)
    blocks_by_key = sequence_block_index(contract, rom)
    tracks = {int(track["track_id"]): track for track in contract["tracks"]}

    records: list[dict[str, Any]] = []
    direct_ref_count = 0
    direct_ref_payload_matches = 0
    contract_pack_matches = 0
    referenced_song_count = 0
    in_engine_count = 0

    for track_id in sorted(songs):
        entry = songs[track_id]
        contract_track = tracks.get(track_id)
        contract_sequence_pack = None
        if contract_track:
            contract_sequence_pack = contract_track.get("packs", {}).get("sequence_pack")

        record: dict[str, Any] = {
            "track_id": track_id,
            "track_name": None if contract_track is None else contract_track["name"],
            "contract_sequence_pack": contract_sequence_pack,
            "ebdecompile_song_pack": entry.get("Song Pack"),
            "ebdecompile_song_file": entry.get("Song File"),
            "song_to_reference": entry.get("Song to Reference"),
            "instrument_pack_1": entry.get("Instrument Pack 1"),
            "instrument_pack_2": entry.get("Instrument Pack 2"),
        }

        if entry.get("Song to Reference"):
            referenced_song_count += 1
            record["alignment_status"] = "song_references_another_track"
        elif entry.get("Song Pack") == "in-engine":
            in_engine_count += 1
            candidates = in_engine_candidates(entry)
            record["alignment_status"] = "in_engine_subsong_reference"
            record["candidate_ref_files"] = candidates
        else:
            path = ref_song_path(entry)
            direct_ref_count += 1
            if path is None:
                record["alignment_status"] = "missing_ref_path"
            elif not path.exists():
                record["alignment_status"] = "missing_ref_file"
                record["reference_song_path"] = rel(path)
            else:
                data = path.read_bytes()
                record["reference_song_path"] = rel(path)
                if len(data) < 4:
                    record["alignment_status"] = "ref_file_too_short"
                else:
                    declared_count = read_u16_le(data, 0)
                    declared_destination = read_u16_le(data, 2)
                    payload = data[4:]
                    payload_sha1 = hashlib.sha1(payload).hexdigest()
                    matches = blocks_by_key.get((payload_sha1, declared_count, declared_destination), [])
                    record["reference_bytes"] = len(data)
                    record["declared_count"] = declared_count
                    record["declared_destination"] = f"0x{declared_destination:04X}"
                    record["payload_sha1"] = payload_sha1
                    record["matching_contract_blocks"] = matches
                    if matches:
                        direct_ref_payload_matches += 1
                        record["alignment_status"] = "payload_matches_contract_sequence_block"
                        if contract_sequence_pack is not None and any(
                            match["pack_id"] == int(contract_sequence_pack) for match in matches
                        ):
                            contract_pack_matches += 1
                            record["contract_sequence_pack_matches_ref"] = True
                        else:
                            record["contract_sequence_pack_matches_ref"] = False
                    else:
                        record["alignment_status"] = "no_matching_contract_sequence_block"
        records.append(record)

    return {
        "schema": "earthbound-decomp.audio-ebdecompile-ref-alignment.v1",
        "source_policy": contract["source_policy"],
        "references": [
            "refs/eb-decompile-4ef92/Music/songs.yml",
            "refs/eb-decompile-4ef92/Music/Packs/*/*.ebm",
            "manifests/audio-pack-contracts.json",
        ],
        "summary": {
            "songs_yml_entries": len(songs),
            "direct_ref_song_files": direct_ref_count,
            "direct_ref_payload_matches": direct_ref_payload_matches,
            "contract_sequence_pack_matches": contract_pack_matches,
            "song_reference_entries": referenced_song_count,
            "in_engine_entries": in_engine_count,
            "alignment_status_counts": dict(
                sorted(
                    {
                        status: sum(1 for record in records if record.get("alignment_status") == status)
                        for status in {record.get("alignment_status") for record in records}
                    }.items()
                )
            ),
        },
        "records": records,
        "findings": [
            "Direct eb-decompile song files include a 4-byte load header followed by the sequence payload.",
            "Matching direct song files corroborate our LOAD_SPC700_DATA block extraction, destination, and payload hashing.",
            "In-engine songs are sub-song references inside pack 1 driver/runtime data rather than one file per top-level sequence pack, so they need a separate sub-song alignment pass.",
            "Song-to-reference entries intentionally reuse another track's song data and should be resolved before exact export planning treats them as independent sequences.",
        ],
        "next_work": [
            "resolve in-engine song files against pack 1's runtime sequence area",
            "use direct payload matches to seed future focused pack reports automatically",
            "feed song-to-reference reuse into exact-duration export planning",
        ],
    }


def render_markdown(data: dict[str, Any]) -> str:
    summary = data["summary"]
    rows = []
    for record in data["records"][:80]:
        rows.append(
            f"| `{record['track_id']}` | {record.get('track_name') or ''} | "
            f"`{record.get('contract_sequence_pack')}` | `{record.get('ebdecompile_song_pack')}` | "
            f"`{record.get('alignment_status')}` | `{record.get('reference_song_path', '')}` |"
        )
    return "\n".join(
        [
            "# Audio eb-decompile Reference Alignment",
            "",
            "Status: direct song-file payload alignment built; in-engine sub-song alignment remains separate work.",
            "",
            "## Summary",
            "",
            f"- songs.yml entries: `{summary['songs_yml_entries']}`",
            f"- direct ref song files: `{summary['direct_ref_song_files']}`",
            f"- direct ref payload matches: `{summary['direct_ref_payload_matches']}`",
            f"- contract sequence-pack matches: `{summary['contract_sequence_pack_matches']}`",
            f"- song-reference entries: `{summary['song_reference_entries']}`",
            f"- in-engine entries: `{summary['in_engine_entries']}`",
            f"- alignment statuses: `{summary['alignment_status_counts']}`",
            "",
            "## First 80 Tracks",
            "",
            "| Track | Name | Contract sequence pack | Ref song pack | Status | Ref file |",
            "| ---: | --- | ---: | --- | --- | --- |",
            *rows,
            "",
            "## Findings",
            "",
            *[f"- {finding}" for finding in data["findings"]],
            "",
            "## Next Work",
            "",
            *[f"- {item}" for item in data["next_work"]],
            "",
        ]
    )


def main() -> int:
    args = parse_args()
    contract = load_json(Path(args.contract))
    rom = rom_tools.load_rom(rom_tools.find_rom(args.rom))
    data = build_alignment(contract, rom)
    output = Path(args.output)
    notes = Path(args.notes)
    output.parent.mkdir(parents=True, exist_ok=True)
    notes.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    notes.write_text(render_markdown(data), encoding="utf-8")
    print(
        "Built eb-decompile audio reference alignment: "
        f"{data['summary']['direct_ref_payload_matches']} / "
        f"{data['summary']['direct_ref_song_files']} direct files match contract blocks"
    )
    print(f"Wrote {output}")
    print(f"Wrote {notes}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
