#!/usr/bin/env python3
"""Build a local APU RAM image seed for one EarthBound music track.

This is not a complete SPC snapshot yet. It applies the same audio-pack load
streams that CHANGE_MUSIC would request, producing the 64 KiB APU RAM image
that a future ares/snes_spc backend will combine with CPU/DSP register state.
Generated outputs are ROM-derived and must stay under ignored build/audio.
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
import rom_tools


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONTRACT = ROOT / "manifests" / "audio-pack-contracts.json"
DEFAULT_OUT = ROOT / "build" / "audio"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build an ignored APU RAM image seed for a music track.")
    parser.add_argument("track_id", type=int, help="Music track id, matching include/constants/music.asm.")
    parser.add_argument("--rom", help="Optional explicit EarthBound US ROM path.")
    parser.add_argument("--contract", default=str(DEFAULT_CONTRACT), help="Audio contract JSON path.")
    parser.add_argument("--out", default=str(DEFAULT_OUT), help="Ignored output directory.")
    parser.add_argument(
        "--no-cold-start",
        action="store_true",
        help="Apply only the track row, without InitializeMusicSubsystem bootstrap.",
    )
    return parser.parse_args()


def load_contract(path: Path) -> dict[str, Any]:
    if not path.exists():
        return audio_pack_contracts.build_audio_contract()
    return json.loads(path.read_text(encoding="utf-8"))


def require_track(contract: dict[str, Any], track_id: int) -> dict[str, Any]:
    for track in contract["tracks"]:
        if int(track["track_id"]) == track_id:
            return track
    raise ValueError(f"unknown track id {track_id}")


def build_apu_ram_image(
    contract: dict[str, Any],
    rom: bytes,
    track: dict[str, Any],
    *,
    use_cold_start: bool = True,
) -> tuple[bytes, list[dict[str, Any]]]:
    packs = {int(pack["pack_id"]): pack for pack in contract["audio_packs"]}
    ram = bytearray(0x10000)
    applied: list[dict[str, Any]] = []

    selected_load_order = track.get("cold_start_load_order") if use_cold_start else None
    if not selected_load_order:
        selected_load_order = track["load_order"]

    for load in selected_load_order:
        pack_id = int(load["pack_id"])
        pack = packs[pack_id]
        cpu_range = audio_pack_contracts.parse_cpu_range(pack["range"])
        data = audio_pack_contracts.slice_range(rom, cpu_range)
        parsed = audio_pack_contracts.parse_load_spc700_stream(data)
        if parsed.status != "ok":
            raise ValueError(f"AUDIO_PACK_{pack_id} parse status is {parsed.status}")

        for block in parsed.blocks:
            if block.terminal:
                applied.append(
                    {
                        "role": load["role"],
                        "pack_id": pack_id,
                        "terminal": True,
                        "stream_offset": f"0x{block.stream_offset:04X}",
                    }
                )
                continue
            assert block.payload_offset is not None
            destination_end = block.destination + block.count
            if destination_end > len(ram):
                raise ValueError(
                    f"AUDIO_PACK_{pack_id} block {block.index} writes past APU RAM: "
                    f"0x{block.destination:04X}+0x{block.count:04X}"
                )
            payload = data[block.payload_offset:block.payload_offset + block.count]
            ram[block.destination:destination_end] = payload
            applied.append(
                {
                    "role": load["role"],
                    "pack_id": pack_id,
                    "block": block.index,
                    "destination": f"0x{block.destination:04X}",
                    "bytes": block.count,
                    "payload_sha1": hashlib.sha1(payload).hexdigest(),
                    "role_guess": block.role_guess,
                }
            )

    return bytes(ram), applied


def main() -> int:
    args = parse_args()
    contract_path = Path(args.contract)
    contract = load_contract(contract_path)
    track = require_track(contract, args.track_id)

    rom_path = rom_tools.find_rom(args.rom)
    rom = rom_tools.load_rom(rom_path)
    ram, applied = build_apu_ram_image(contract, rom, track, use_cold_start=not args.no_cold_start)

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = f"track-{args.track_id:03d}-{track['name'].lower()}"
    stem = "".join(ch if ch.isalnum() or ch in "-_" else "_" for ch in stem)
    ram_path = out_dir / f"{stem}.apu-ram.bin"
    report_path = out_dir / f"{stem}.apu-ram.json"
    ram_path.write_bytes(ram)
    report_path.write_text(
        json.dumps(
            {
                "schema": "earthbound-decomp.audio-track-apu-ram-image.v1",
                "track_id": track["track_id"],
                "track_name": track["name"],
                "source_policy": contract["source_policy"],
                "contract": str(contract_path),
                "ram_sha1": hashlib.sha1(ram).hexdigest(),
                "load_mode": "cold_start" if not args.no_cold_start else "track_row_only",
                "applied_blocks": applied,
                "spc_snapshot_status": "apu_ram_only_registers_and_driver_start_not_finalized",
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"Built APU RAM seed for track {track['track_id']} {track['name']}")
    print(f"Wrote {ram_path}")
    print(f"Wrote {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
