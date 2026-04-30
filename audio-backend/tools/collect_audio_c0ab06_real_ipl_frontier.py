#!/usr/bin/env python3
"""Collect C0:AB06 real ares SMP IPL receiver frontier evidence."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import rom_tools
from run_audio_c0ab06_loader_handshake_corpus import (
    DEFAULT_EXE,
    DEFAULT_LOADER_CONTRACT,
    DEFAULT_LOADER_FILE,
    DEFAULT_PACK_CONTRACT,
    apu_ram_metadata,
    expected_apu_ram_for_pack,
    expected_streams,
    load_json,
    pack_pointer_map,
    write_json,
)


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_IPL = (
    Path(os.environ["EARTHBOUND_ARES_ROOT"]) if "EARTHBOUND_ARES_ROOT" in os.environ else ROOT.parent / "ares-earthbound-audio-backend"
) / "ares" / "System" / "Super Famicom" / "ipl.rom"
DEFAULT_OUTPUT = ROOT / "build" / "audio" / "c0ab06-real-ipl-frontier" / "c0ab06-real-ipl-frontier.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Collect C0:AB06 real-IPL receiver frontier evidence.")
    parser.add_argument("--rom", help="Optional explicit EarthBound US ROM path.")
    parser.add_argument("--exe", default=str(DEFAULT_EXE), help="Built C0:AB06 loader handshake executable.")
    parser.add_argument("--loader-file", default=str(DEFAULT_LOADER_FILE), help="C0:AB06 routine fixture.")
    parser.add_argument("--loader-contract", default=str(DEFAULT_LOADER_CONTRACT), help="C0:AB06 loader contract JSON.")
    parser.add_argument("--pack-contract", default=str(DEFAULT_PACK_CONTRACT), help="Audio pack contract JSON.")
    parser.add_argument("--ipl-file", default=str(DEFAULT_IPL), help="ares Super Famicom IPL ROM.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Ignored frontier JSON.")
    parser.add_argument("--limit", type=int, help="Optional unique-pack limit for debugging.")
    return parser.parse_args()


def run_real_ipl(
    exe: Path,
    loader_file: Path,
    rom_path: Path,
    ipl_file: Path,
    pointer: dict[str, Any],
    apu_ram_out: Path,
    *,
    stop_after_terminal: bool,
) -> dict[str, Any]:
    command = [
        str(exe),
        "--receiver",
        "ares_smp_ipl",
        "--ipl-file",
        str(ipl_file),
        "--loader-file",
        str(loader_file),
        "--rom-file",
        str(rom_path),
        "--stream-bank",
        f"0x{int(pointer['bank']):02X}",
        "--stream-address",
        f"0x{int(pointer['address']):04X}",
        "--apu-ram-out",
        str(apu_ram_out),
    ]
    if stop_after_terminal:
        command.append("--stop-after-terminal")
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
        "pack_id": int(pointer["pack_id"]),
        "pointer": {
            "bank": f"0x{int(pointer['bank']):02X}",
            "address": f"0x{int(pointer['address']):04X}",
            "cpu": pointer.get("cpu"),
            "range": pointer.get("range"),
        },
        "returncode": completed.returncode,
        "stderr": completed.stderr.strip(),
        "handshake": handshake,
    }


def payload_region_metadata(actual_path: Path, expected: dict[str, Any]) -> dict[str, Any]:
    actual = actual_path.read_bytes()
    block_records: list[dict[str, Any]] = []
    mismatch_count = 0
    payload_mask = bytearray(0x10000)
    for block in expected.get("blocks", []):
        destination = int(str(block["destination"]), 16)
        size = int(block["payload_bytes"])
        for offset in range(destination, destination + size):
            payload_mask[offset] = 1
        actual_sha1 = __import__("hashlib").sha1(actual[destination:destination + size]).hexdigest()
        matches = actual_sha1 == block["final_region_sha1"]
        if not matches:
            mismatch_count += 1
        block_records.append(
            {
                "index": block["index"],
                "destination": block["destination"],
                "payload_bytes": size,
                "expected_final_region_sha1": block["final_region_sha1"],
                "actual_final_region_sha1": actual_sha1,
                "matches": matches,
            }
        )
    nonpayload_nonzero = [
        f"0x{index:04X}"
        for index, byte in enumerate(actual)
        if byte and not payload_mask[index]
    ]
    return {
        "path": str(actual_path),
        "bytes": len(actual),
        "payload_block_count": len(block_records),
        "payload_region_mismatch_count": mismatch_count,
        "payload_regions_match": mismatch_count == 0,
        "nonpayload_nonzero_count": len(nonpayload_nonzero),
        "nonpayload_nonzero_sample": nonpayload_nonzero[:16],
        "blocks": block_records,
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
    unique_pack_ids = sorted({int(stream["pack_id"]) for stream in occurrences})
    if args.limit is not None:
        unique_pack_ids = unique_pack_ids[: args.limit]

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    records: list[dict[str, Any]] = []
    for pack_id in unique_pack_ids:
        pointer = pointer_by_pack[pack_id]
        expected = expected_apu_ram_for_pack(rom, pointer)
        apu_ram_out = output.parent / f"pack-{pack_id:03d}-real-ipl-apu-ram.bin"
        record = run_real_ipl(
            exe,
            loader_file,
            rom_path,
            ipl_file,
            pointer,
            apu_ram_out,
            stop_after_terminal=True,
        )
        record["expected_apu_ram"] = expected
        record["payload_regions"] = payload_region_metadata(apu_ram_out, expected) if apu_ram_out.exists() else None
        status = "ok" if record["returncode"] == 0 and (record["payload_regions"] or {}).get("payload_regions_match") else f"failed({record['returncode']})"
        print(f"- real IPL pack {pack_id:03d} {pointer.get('cpu')}: {status}")
        records.append(record)

    bootstrap_pointer = pointer_by_pack.get(1)
    bootstrap_return: dict[str, Any] | None = None
    if bootstrap_pointer is not None:
        bootstrap_return_path = output.parent / "pack-001-real-ipl-bootstrap-return-apu-ram.bin"
        bootstrap_return = run_real_ipl(
            exe,
            loader_file,
            rom_path,
            ipl_file,
            bootstrap_pointer,
            bootstrap_return_path,
            stop_after_terminal=False,
        )
        bootstrap_return["fully_returned_to_cpu"] = (
            bootstrap_return.get("returncode") == 0
            and (bootstrap_return.get("handshake") or {}).get("final_pc") == "0x008004"
        )
        print(
            "- real IPL bootstrap return pack 001: "
            + ("ok" if bootstrap_return["fully_returned_to_cpu"] else f"failed({bootstrap_return.get('returncode')})")
        )

    payload_match_count = sum(1 for record in records if (record.get("payload_regions") or {}).get("payload_regions_match"))
    summary = {
        "schema": "earthbound-decomp.c0ab06-real-ipl-frontier.v1",
        "status": "real_ares_smp_ipl_receiver_executes_c0ab06_stream_payloads",
        "source_policy": loader_contract.get("source_policy"),
        "remaining_shortcut": "Each pack is loaded as an isolated IPL transaction; post-bootstrap game-driver re-entry for later packs still needs full runtime sequencing.",
        "loader_contract": str(Path(args.loader_contract)),
        "pack_contract": str(Path(args.pack_contract)),
        "handshake_executable": str(exe),
        "loader_fixture": str(loader_file),
        "ipl_file": str(ipl_file),
        "unique_pack_count": len(unique_pack_ids),
        "executed_unique_pack_count": len(records),
        "payload_region_match_count": payload_match_count,
        "mismatch_count": len(records) - payload_match_count + len(setup_errors),
        "setup_errors": setup_errors,
        "bootstrap_return": bootstrap_return,
        "records": records,
    }
    write_json(output, summary)
    print(
        "C0:AB06 real-IPL frontier: "
        f"{payload_match_count} / {len(records)} unique pack payload regions matched"
    )
    print(f"Wrote {output}")
    return 0 if summary["mismatch_count"] == 0 and (bootstrap_return or {}).get("fully_returned_to_cpu") else 1


if __name__ == "__main__":
    raise SystemExit(main())
