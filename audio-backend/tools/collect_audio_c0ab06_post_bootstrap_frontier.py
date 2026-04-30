#!/usr/bin/env python3
"""Collect C0:AB06 post-bootstrap game-driver reload frontier evidence."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import rom_tools
from collect_audio_c0ab06_real_ipl_frontier import DEFAULT_IPL, payload_region_metadata
from run_audio_c0ab06_loader_handshake_corpus import (
    DEFAULT_EXE,
    DEFAULT_LOADER_CONTRACT,
    DEFAULT_LOADER_FILE,
    DEFAULT_PACK_CONTRACT,
    expected_apu_ram_for_pack,
    expected_streams,
    load_json,
    pack_pointer_map,
    write_json,
)


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT = ROOT / "build" / "audio" / "c0ab06-post-bootstrap-frontier" / "c0ab06-post-bootstrap-frontier.json"
BOOTSTRAP_PACK_ID = 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Collect C0:AB06 post-bootstrap reload frontier evidence.")
    parser.add_argument("--rom", help="Optional explicit EarthBound US ROM path.")
    parser.add_argument("--exe", default=str(DEFAULT_EXE), help="Built C0:AB06 loader handshake executable.")
    parser.add_argument("--loader-file", default=str(DEFAULT_LOADER_FILE), help="C0:AB06 routine fixture.")
    parser.add_argument("--loader-contract", default=str(DEFAULT_LOADER_CONTRACT), help="C0:AB06 loader contract JSON.")
    parser.add_argument("--pack-contract", default=str(DEFAULT_PACK_CONTRACT), help="Audio pack contract JSON.")
    parser.add_argument("--ipl-file", default=str(DEFAULT_IPL), help="ares Super Famicom IPL ROM.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Ignored frontier JSON.")
    parser.add_argument("--limit", type=int, help="Optional unique-pack limit for debugging.")
    return parser.parse_args()


def run_post_bootstrap(
    exe: Path,
    loader_file: Path,
    rom_path: Path,
    ipl_file: Path,
    bootstrap: dict[str, Any],
    target: dict[str, Any],
    apu_ram_out: Path,
) -> dict[str, Any]:
    command = [
        str(exe),
        "--receiver",
        "ares_smp_ipl",
        "--bootstrap-bank",
        f"0x{int(bootstrap['bank']):02X}",
        "--bootstrap-address",
        f"0x{int(bootstrap['address']):04X}",
        "--stop-after-terminal",
        "--ipl-file",
        str(ipl_file),
        "--loader-file",
        str(loader_file),
        "--rom-file",
        str(rom_path),
        "--stream-bank",
        f"0x{int(target['bank']):02X}",
        "--stream-address",
        f"0x{int(target['address']):04X}",
        "--apu-ram-out",
        str(apu_ram_out),
    ]
    completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
    try:
        handshake = json.loads(completed.stdout)
    except json.JSONDecodeError as error:
        handshake = {
            "schema": "earthbound-decomp.c0ab06-loader-handshake.v1",
            "parse_error": str(error),
            "stdout": completed.stdout,
        }
    return {
        "pack_id": int(target["pack_id"]),
        "pointer": {
            "bank": f"0x{int(target['bank']):02X}",
            "address": f"0x{int(target['address']):04X}",
            "cpu": target.get("cpu"),
            "range": target.get("range"),
        },
        "returncode": completed.returncode,
        "stderr": completed.stderr.strip(),
        "handshake": handshake,
    }


def main() -> int:
    args = parse_args()
    exe = Path(args.exe)
    loader_file = Path(args.loader_file)
    ipl_file = Path(args.ipl_file)
    if not exe.exists():
        raise FileNotFoundError(f"missing C0:AB06 loader executable: {exe}")
    if not loader_file.exists():
        raise FileNotFoundError(f"missing C0:AB06 loader fixture: {loader_file}")
    if not ipl_file.exists():
        raise FileNotFoundError(f"missing SFC IPL ROM: {ipl_file}")

    rom_path = rom_tools.find_rom(args.rom)
    rom = rom_tools.load_rom(rom_path)
    loader_contract = load_json(Path(args.loader_contract))
    pack_contract = load_json(Path(args.pack_contract))
    pointer_by_pack = pack_pointer_map(pack_contract)
    occurrences, setup_errors = expected_streams(loader_contract, pointer_by_pack)
    bootstrap = pointer_by_pack.get(BOOTSTRAP_PACK_ID)
    if bootstrap is None:
        raise ValueError("bootstrap pack 1 is missing from the pack pointer table")

    unique_pack_ids = sorted({int(stream["pack_id"]) for stream in occurrences if int(stream["pack_id"]) != BOOTSTRAP_PACK_ID})
    if args.limit is not None:
        unique_pack_ids = unique_pack_ids[: args.limit]

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    records: list[dict[str, Any]] = []
    for pack_id in unique_pack_ids:
        pointer = pointer_by_pack[pack_id]
        expected = expected_apu_ram_for_pack(rom, pointer)
        apu_ram_out = output.parent / f"pack-{pack_id:03d}-post-bootstrap-apu-ram.bin"
        record = run_post_bootstrap(exe, loader_file, rom_path, ipl_file, bootstrap, pointer, apu_ram_out)
        record["expected_apu_ram"] = expected
        record["payload_regions"] = payload_region_metadata(apu_ram_out, expected) if apu_ram_out.exists() else None
        status = "ok" if record["returncode"] == 0 and (record["payload_regions"] or {}).get("payload_regions_match") else f"failed({record['returncode']})"
        print(f"- post-bootstrap pack {pack_id:03d} {pointer.get('cpu')}: {status}")
        records.append(record)

    payload_match_count = sum(1 for record in records if (record.get("payload_regions") or {}).get("payload_regions_match"))
    summary = {
        "schema": "earthbound-decomp.c0ab06-post-bootstrap-frontier.v1",
        "status": "real_ares_smp_driver_accepts_post_bootstrap_c0ab06_reloads",
        "source_policy": loader_contract.get("source_policy"),
        "remaining_shortcut": "Each target pack is tested in a fresh pack-1-bootstrap-then-target transaction; full CHANGE_MUSIC still needs to sequence the required multi-pack triplets in one continuous run.",
        "loader_contract": str(Path(args.loader_contract)),
        "pack_contract": str(Path(args.pack_contract)),
        "handshake_executable": str(exe),
        "loader_fixture": str(loader_file),
        "ipl_file": str(ipl_file),
        "bootstrap_pack": {
            "pack_id": BOOTSTRAP_PACK_ID,
            "pointer": {
                "bank": f"0x{int(bootstrap['bank']):02X}",
                "address": f"0x{int(bootstrap['address']):04X}",
                "cpu": bootstrap.get("cpu"),
                "range": bootstrap.get("range"),
            },
        },
        "unique_target_pack_count": len(unique_pack_ids),
        "executed_target_pack_count": len(records),
        "payload_region_match_count": payload_match_count,
        "mismatch_count": len(records) - payload_match_count + len(setup_errors),
        "setup_errors": setup_errors,
        "records": records,
    }
    write_json(output, summary)
    print(
        "C0:AB06 post-bootstrap frontier: "
        f"{payload_match_count} / {len(records)} target pack payload regions matched"
    )
    print(f"Wrote {output}")
    return 0 if summary["mismatch_count"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
