#!/usr/bin/env python3
"""Build ignored renderer input fixtures for EarthBound music tracks.

Fixtures are the bridge between contract parsing and a future renderer backend:
they include the cold-start APU RAM seed, the exact pack/block load transcript,
the post-load track command, and the still-missing SPC state fields.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import audio_pack_contracts
import build_audio_track_snapshot
import rom_tools


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONTRACT = ROOT / "manifests" / "audio-pack-contracts.json"
DEFAULT_FRONTIER = ROOT / "manifests" / "audio-spc-state-frontier.json"
DEFAULT_OUT = ROOT / "build" / "audio" / "renderer-fixtures"
DEFAULT_TRACKS = "1,2,46,47,48,83,95,105,121,133,157,160,161,162,163,168,175,186,187,191"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build renderer input fixtures for selected music tracks.")
    parser.add_argument(
        "--tracks",
        default=DEFAULT_TRACKS,
        help="Comma-separated track ids. Defaults to the 20-track representative audio corpus.",
    )
    parser.add_argument("--rom", help="Optional explicit EarthBound US ROM path.")
    parser.add_argument("--contract", default=str(DEFAULT_CONTRACT), help="Audio contract JSON path.")
    parser.add_argument("--frontier", default=str(DEFAULT_FRONTIER), help="SPC state frontier JSON path.")
    parser.add_argument("--out", default=str(DEFAULT_OUT), help="Ignored fixture output directory.")
    parser.add_argument(
        "--no-cold-start",
        action="store_true",
        help="Apply only the track row, without InitializeMusicSubsystem bootstrap.",
    )
    return parser.parse_args()


def parse_track_ids(text: str) -> list[int]:
    track_ids: list[int] = []
    for part in text.split(","):
        part = part.strip()
        if part:
            track_ids.append(int(part, 0))
    return track_ids


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sanitize_stem(track_id: int, name: str) -> str:
    stem = f"track-{track_id:03d}-{name.lower()}"
    return "".join(ch if ch.isalnum() or ch in "-_" else "_" for ch in stem)


def selected_load_order(track: dict[str, Any], *, use_cold_start: bool) -> list[dict[str, Any]]:
    if use_cold_start and track.get("cold_start_load_order"):
        return track["cold_start_load_order"]
    return track["load_order"]


def build_load_transcript(
    contract: dict[str, Any],
    rom: bytes,
    track: dict[str, Any],
    *,
    use_cold_start: bool,
) -> list[dict[str, Any]]:
    packs = {int(pack["pack_id"]): pack for pack in contract["audio_packs"]}
    transcript: list[dict[str, Any]] = []
    for order_index, load in enumerate(selected_load_order(track, use_cold_start=use_cold_start)):
        pack_id = int(load["pack_id"])
        pack = packs[pack_id]
        cpu_range = audio_pack_contracts.parse_cpu_range(pack["range"])
        data = audio_pack_contracts.slice_range(rom, cpu_range)
        parsed = audio_pack_contracts.parse_load_spc700_stream(data)
        if parsed.status != "ok":
            raise ValueError(f"AUDIO_PACK_{pack_id} parse status is {parsed.status}")

        block_records: list[dict[str, Any]] = []
        for block in parsed.blocks:
            block_record: dict[str, Any] = {
                "index": block.index,
                "stream_offset": f"0x{block.stream_offset:04X}",
                "terminal": block.terminal,
                "count": block.count,
                "destination": f"0x{block.destination:04X}",
                "role_guess": block.role_guess,
            }
            if block.payload_offset is not None:
                block_record["payload_offset"] = f"0x{block.payload_offset:04X}"
                block_record["payload_sha1"] = block.sha1
            block_records.append(block_record)

        transcript.append(
            {
                "order_index": order_index,
                "role": load["role"],
                "pack_id": pack_id,
                "asset_id": load.get("asset_id"),
                "rom_range": pack["range"],
                "rom_sha1": pack["sha1"],
                "stream_status": parsed.status,
                "blocks": block_records,
            }
        )
    transcript.append(
        {
            "order_index": len(transcript),
            "role": "post_load_track_start_command",
            "command": "write_apu_io0",
            "value": int(track["track_id"]),
            "value_hex": f"0x{int(track['track_id']) & 0xFF:02X}",
            "source": "CHANGE_MUSIC -> C0ABBD_SendApuPort0CommandByte",
        }
    )
    return transcript


def build_fixture(
    contract: dict[str, Any],
    frontier: dict[str, Any],
    rom: bytes,
    track_id: int,
    out_dir: Path,
    *,
    use_cold_start: bool,
) -> dict[str, Any]:
    track = build_audio_track_snapshot.require_track(contract, track_id)
    ram, applied = build_audio_track_snapshot.build_apu_ram_image(
        contract,
        rom,
        track,
        use_cold_start=use_cold_start,
    )
    stem = sanitize_stem(track_id, track["name"])
    ram_path = out_dir / f"{stem}.apu-ram.bin"
    fixture_path = out_dir / f"{stem}.renderer-fixture.json"
    ram_path.write_bytes(ram)
    transcript = build_load_transcript(contract, rom, track, use_cold_start=use_cold_start)

    fixture = {
        "schema": "earthbound-decomp.audio-renderer-fixture.v1",
        "track_id": track_id,
        "track_name": track["name"],
        "source_policy": contract["source_policy"],
        "load_mode": "cold_start" if use_cold_start else "track_row_only",
        "contract": "manifests/audio-pack-contracts.json",
        "state_frontier": "manifests/audio-spc-state-frontier.json",
        "apu_ram": {
            "path": str(ram_path),
            "size": len(ram),
            "sha1": hashlib.sha1(ram).hexdigest(),
            "status": "implemented",
        },
        "track_packs": track["packs"],
        "load_order": selected_load_order(track, use_cold_start=use_cold_start),
        "load_transcript": transcript,
        "applied_block_count": len(applied),
        "payload_block_count": sum(1 for block in applied if not block.get("terminal")),
        "spc_snapshot_status": frontier["status"],
        "missing_state": frontier["missing_state"],
        "renderer_gate": {
            "current": "diagnostic_apu_ram_seed",
            "next": "complete_spc_snapshot",
        },
    }
    fixture_path.write_text(json.dumps(fixture, indent=2) + "\n", encoding="utf-8")
    return {
        "track_id": track_id,
        "track_name": track["name"],
        "fixture_path": str(fixture_path),
        "apu_ram_path": str(ram_path),
        "apu_ram_sha1": fixture["apu_ram"]["sha1"],
        "load_mode": fixture["load_mode"],
        "load_transcript_steps": len(transcript),
    }


def main() -> int:
    args = parse_args()
    track_ids = parse_track_ids(args.tracks)
    if not track_ids:
        raise SystemExit("No track ids selected.")

    contract = load_json(Path(args.contract))
    frontier = load_json(Path(args.frontier))
    rom_path = rom_tools.find_rom(args.rom)
    rom = rom_tools.load_rom(rom_path)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    records = [
        build_fixture(
            contract,
            frontier,
            rom,
            track_id,
            out_dir,
            use_cold_start=not args.no_cold_start,
        )
        for track_id in track_ids
    ]
    manifest = {
        "schema": "earthbound-decomp.audio-renderer-fixture-index.v1",
        "source_policy": contract["source_policy"],
        "track_count": len(records),
        "fixtures": records,
        "status": "renderer_input_fixtures_ready_complete_spc_snapshot_not_yet_available",
    }
    index_path = out_dir / "audio-renderer-fixtures.json"
    index_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Built audio renderer fixtures: {len(records)} tracks -> {index_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
