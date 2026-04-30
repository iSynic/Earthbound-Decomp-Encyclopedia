#!/usr/bin/env python3
"""Build ignored bootstrap-only APU RAM seeds for the audio smoke corpus."""

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

import build_audio_snapshot_corpus
import build_audio_track_snapshot
import rom_tools


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONTRACT = ROOT / "manifests" / "audio-pack-contracts.json"
DEFAULT_OUT = ROOT / "build" / "audio" / "bootstrap-corpus"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build bootstrap-only APU RAM seeds for representative music tracks.")
    parser.add_argument(
        "--tracks",
        default=",".join(str(track_id) for track_id in build_audio_snapshot_corpus.DEFAULT_TRACKS),
        help="Comma-separated track ids. Defaults to the 20-track representative corpus.",
    )
    parser.add_argument("--rom", help="Optional explicit EarthBound US ROM path.")
    parser.add_argument("--contract", default=str(DEFAULT_CONTRACT), help="Audio contract JSON path.")
    parser.add_argument("--out", default=str(DEFAULT_OUT), help="Ignored corpus output directory.")
    return parser.parse_args()


def bootstrap_load_order(track: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        load
        for load in track.get("cold_start_load_order", [])
        if str(load.get("role")) == "initialize_music_subsystem_sequence_pack"
    ]


def main() -> int:
    args = parse_args()
    track_ids = build_audio_snapshot_corpus.parse_track_ids(args.tracks)
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
    block_role_usage: Counter[str] = Counter()

    for track_id in track_ids:
        track = build_audio_track_snapshot.require_track(contract, track_id)
        bootstrap_track = dict(track)
        bootstrap_track["load_order"] = bootstrap_load_order(track)
        ram, applied = build_audio_track_snapshot.build_apu_ram_image(
            contract,
            rom,
            bootstrap_track,
            use_cold_start=False,
        )
        stem = build_audio_snapshot_corpus.sanitize_stem(track_id, track["name"])
        ram_path = out_dir / f"{stem}.bootstrap-apu-ram.bin"
        report_path = out_dir / f"{stem}.bootstrap-apu-ram.json"
        ram_path.write_bytes(ram)
        load_order = bootstrap_track["load_order"]
        for load in load_order:
            pack_usage[int(load["pack_id"])] += 1
        for block in applied:
            if "role_guess" in block:
                block_role_usage[str(block["role_guess"])] += 1

        record = {
            "track_id": track_id,
            "track_name": track["name"],
            "ram_path": str(ram_path),
            "report_path": str(report_path),
            "ram_sha1": hashlib.sha1(ram).hexdigest(),
            "load_mode": "bootstrap_only",
            "load_order": load_order,
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
                    "load_mode": "bootstrap_only",
                    "applied_blocks": applied,
                    "spc_snapshot_status": "bootstrap_apu_ram_only_track_packs_not_loaded",
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
            "load_role_usage": {"initialize_music_subsystem_sequence_pack": len(records)},
            "apu_destination_role_usage": dict(block_role_usage),
        },
        "renderer_status": "bootstrap_only_seed_for_loader_apply_smoke; not final render output",
    }
    manifest_path = out_dir / "audio-bootstrap-snapshot-corpus.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(
        f"Built audio bootstrap snapshot corpus: {len(records)} tracks, "
        f"{len(pack_usage)} unique packs -> {manifest_path}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
