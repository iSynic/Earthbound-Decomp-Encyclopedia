#!/usr/bin/env python3
"""Build ignored APU RAM seeds for a representative audio-render test corpus."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import build_audio_track_snapshot
import rom_tools


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONTRACT = ROOT / "manifests" / "audio-pack-contracts.json"
DEFAULT_OUT = ROOT / "build" / "audio" / "corpus"
DEFAULT_TRACKS = [
    1,    # GAS_STATION: pack 1 driver/common path
    2,    # NAMING_SCREEN: setup/menu path
    46,   # ONETT: representative overworld track
    47,   # FOURSIDE
    48,   # SATURN_VALLEY
    83,   # SKY_RUNNER
    95,   # SMILES_AND_TEARS
    105,  # POKEY_MEANS_BUSINESS
    121,  # ONETT_INTRO
    133,  # HIDDEN_SONG
    157,  # ATTRACT_MODE
    160,  # SOUNDSTONE_RECORDING_GIANT_STEP
    161,  # SOUNDSTONE_RECORDING_LILLIPUT_STEPS
    162,  # SOUNDSTONE_RECORDING_MILKY_WELL
    163,  # SOUNDSTONE_BGM-adjacent coverage
    168,  # SOUNDSTONE_BGM
    175,  # TITLE_SCREEN
    186,  # GIYGAS_PHASE1
    187,  # GIVE_US_STRENGTH
    191,  # GIYGAS_WEAKENED
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build ignored APU RAM image seeds for representative music tracks."
    )
    parser.add_argument(
        "--tracks",
        default=",".join(str(track_id) for track_id in DEFAULT_TRACKS),
        help="Comma-separated track ids. Defaults to a 20-track representative corpus.",
    )
    parser.add_argument("--rom", help="Optional explicit EarthBound US ROM path.")
    parser.add_argument("--contract", default=str(DEFAULT_CONTRACT), help="Audio contract JSON path.")
    parser.add_argument("--out", default=str(DEFAULT_OUT), help="Ignored corpus output directory.")
    return parser.parse_args()


def parse_track_ids(text: str) -> list[int]:
    ids: list[int] = []
    for part in text.split(","):
        part = part.strip()
        if not part:
            continue
        ids.append(int(part, 0))
    return ids


def sanitize_stem(track_id: int, name: str) -> str:
    stem = f"track-{track_id:03d}-{name.lower()}"
    return "".join(ch if ch.isalnum() or ch in "-_" else "_" for ch in stem)


def main() -> int:
    args = parse_args()
    track_ids = parse_track_ids(args.tracks)
    if not track_ids:
        raise SystemExit("No track ids selected.")

    contract_path = Path(args.contract)
    contract = build_audio_track_snapshot.load_contract(contract_path)
    rom_path = rom_tools.find_rom(args.rom)
    rom = rom_tools.load_rom(rom_path)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    records: list[dict[str, Any]] = []
    pack_usage: Counter[int] = Counter()
    role_usage: Counter[str] = Counter()
    block_role_usage: Counter[str] = Counter()

    for track_id in track_ids:
        track = build_audio_track_snapshot.require_track(contract, track_id)
        ram, applied = build_audio_track_snapshot.build_apu_ram_image(contract, rom, track)
        stem = sanitize_stem(track_id, track["name"])
        ram_path = out_dir / f"{stem}.apu-ram.bin"
        report_path = out_dir / f"{stem}.apu-ram.json"
        ram_path.write_bytes(ram)
        cold_start_load_order = track["cold_start_load_order"]
        for load in cold_start_load_order:
            pack_usage[int(load["pack_id"])] += 1
            role_usage[str(load["role"])] += 1
        for block in applied:
            if "role_guess" in block:
                block_role_usage[str(block["role_guess"])] += 1

        record = {
            "track_id": track_id,
            "track_name": track["name"],
            "ram_path": str(ram_path),
            "report_path": str(report_path),
            "ram_sha1": hashlib.sha1(ram).hexdigest(),
            "load_mode": "cold_start",
            "load_order": cold_start_load_order,
            "applied_block_count": len(applied),
            "payload_block_count": sum(1 for block in applied if not block.get("terminal")),
        }
        report_path.write_text(
            json.dumps(
                {
                    "schema": "earthbound-decomp.audio-track-apu-ram-image.v1",
                    "track_id": track["track_id"],
                    "track_name": track["name"],
                    "source_policy": contract["source_policy"],
                    "contract": str(contract_path),
                    "ram_sha1": record["ram_sha1"],
                    "load_mode": "cold_start",
                    "applied_blocks": applied,
                    "spc_snapshot_status": "apu_ram_only_registers_and_driver_start_not_finalized",
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        records.append(record)

    manifest = {
        "schema": "earthbound-decomp.audio-snapshot-corpus.v1",
        "source_policy": contract["source_policy"],
        "contract": str(contract_path),
        "track_count": len(records),
        "tracks": records,
        "summary": {
            "unique_pack_count": len(pack_usage),
            "pack_usage": {str(pack_id): count for pack_id, count in sorted(pack_usage.items())},
            "load_role_usage": dict(role_usage),
            "apu_destination_role_usage": dict(block_role_usage),
        },
        "renderer_status": "ready_for_ares_or_snes_spc_backend; not final render output",
    }
    manifest_path = out_dir / "audio-snapshot-corpus.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(
        f"Built audio snapshot corpus: {len(records)} tracks, "
        f"{len(pack_usage)} unique packs -> {manifest_path}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
