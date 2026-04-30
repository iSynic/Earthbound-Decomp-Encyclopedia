#!/usr/bin/env python3
"""Collect continuous C0:AB06 boot-plus-track-pack-sequence frontier evidence."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import audio_pack_contracts
import rom_tools
from collect_audio_c0ab06_real_ipl_frontier import DEFAULT_IPL
from run_audio_c0ab06_loader_handshake_corpus import (
    DEFAULT_EXE,
    DEFAULT_LOADER_CONTRACT,
    DEFAULT_LOADER_FILE,
    DEFAULT_PACK_CONTRACT,
    load_json,
    pack_pointer_map,
    write_json,
)


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT = ROOT / "build" / "audio" / "c0ab06-continuous-track-load-frontier" / "c0ab06-continuous-track-load-frontier.json"
BOOTSTRAP_PACK_ID = 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Collect continuous C0:AB06 track load frontier evidence.")
    parser.add_argument("--rom", help="Optional explicit EarthBound US ROM path.")
    parser.add_argument("--exe", default=str(DEFAULT_EXE), help="Built C0:AB06 loader handshake executable.")
    parser.add_argument("--loader-file", default=str(DEFAULT_LOADER_FILE), help="C0:AB06 routine fixture.")
    parser.add_argument("--loader-contract", default=str(DEFAULT_LOADER_CONTRACT), help="C0:AB06 loader contract JSON.")
    parser.add_argument("--pack-contract", default=str(DEFAULT_PACK_CONTRACT), help="Audio pack contract JSON.")
    parser.add_argument("--ipl-file", default=str(DEFAULT_IPL), help="ares Super Famicom IPL ROM.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Ignored frontier JSON.")
    parser.add_argument("--limit", type=int, help="Optional track limit for debugging.")
    return parser.parse_args()


def sha1(data: bytes) -> str:
    return hashlib.sha1(data).hexdigest()


def parse_pack_stream(rom: bytes, pointer: dict[str, Any]) -> tuple[bytes, audio_pack_contracts.ParsedAudioStream]:
    data = audio_pack_contracts.slice_range(rom, audio_pack_contracts.parse_cpu_range(pointer["range"]))
    return data, audio_pack_contracts.parse_load_spc700_stream(data)


def apply_pack_to_expected_ram(
    rom: bytes,
    pointer: dict[str, Any],
    expected_ram: bytearray,
    *,
    phase: str,
    sequence_index: int,
) -> list[dict[str, Any]]:
    data, parsed = parse_pack_stream(rom, pointer)
    blocks: list[dict[str, Any]] = []
    for block in parsed.blocks:
        if block.terminal:
            continue
        if block.payload_offset is None:
            raise ValueError(f"pack {pointer['pack_id']} block {block.index} has no payload offset")
        payload = data[block.payload_offset:block.payload_offset + block.count]
        destination = int(block.destination)
        expected_ram[destination:destination + len(payload)] = payload
        blocks.append(
            {
                "phase": phase,
                "sequence_index": sequence_index,
                "pack_id": int(pointer["pack_id"]),
                "pack_cpu": pointer.get("cpu"),
                "block_index": block.index,
                "destination": f"0x{destination:04X}",
                "payload_bytes": len(payload),
                "payload_sha1": sha1(payload),
                "role_guess": block.role_guess,
            }
        )
    return blocks


def expected_track_ram(rom: bytes, pointer_by_pack: dict[int, dict[str, Any]], stream_pack_ids: list[int]) -> dict[str, Any]:
    expected_ram = bytearray(0x10000)
    blocks: list[dict[str, Any]] = []
    bootstrap_pointer = pointer_by_pack[BOOTSTRAP_PACK_ID]
    blocks.extend(
        apply_pack_to_expected_ram(
            rom,
            bootstrap_pointer,
            expected_ram,
            phase="bootstrap",
            sequence_index=-1,
        )
    )
    for index, pack_id in enumerate(stream_pack_ids):
        blocks.extend(
            apply_pack_to_expected_ram(
                rom,
                pointer_by_pack[pack_id],
                expected_ram,
                phase="track_sequence",
                sequence_index=index,
            )
        )
    for block in blocks:
        destination = int(block["destination"], 16)
        size = int(block["payload_bytes"])
        block["expected_final_region_sha1"] = sha1(bytes(expected_ram[destination:destination + size]))
    return {
        "apu_ram_sha1": sha1(bytes(expected_ram)),
        "apu_ram_nonzero_count": sum(1 for byte in expected_ram if byte),
        "payload_block_count": len(blocks),
        "payload_bytes": sum(int(block["payload_bytes"]) for block in blocks),
        "blocks": blocks,
    }


def payload_regions(actual_path: Path, expected: dict[str, Any]) -> dict[str, Any]:
    actual = actual_path.read_bytes()
    block_records: list[dict[str, Any]] = []
    mismatch_count = 0
    skipped_mutable_count = 0
    for block in expected["blocks"]:
        destination = int(block["destination"], 16)
        size = int(block["payload_bytes"])
        mutable = block.get("role_guess") == "main_spc700_driver_or_driver_overlay"
        actual_sha1 = sha1(actual[destination:destination + size])
        matches = mutable or actual_sha1 == block["expected_final_region_sha1"]
        if mutable:
            skipped_mutable_count += 1
        elif not matches:
            mismatch_count += 1
        block_records.append(
            {
                "phase": block["phase"],
                "sequence_index": block["sequence_index"],
                "pack_id": block["pack_id"],
                "block_index": block["block_index"],
                "destination": block["destination"],
                "payload_bytes": size,
                "role_guess": block.get("role_guess"),
                "mutable_runtime_region": mutable,
                "expected_final_region_sha1": block["expected_final_region_sha1"],
                "actual_final_region_sha1": actual_sha1,
                "matches": matches,
            }
        )
    return {
        "path": str(actual_path),
        "bytes": len(actual),
        "payload_block_count": len(block_records),
        "payload_region_mismatch_count": mismatch_count,
        "skipped_mutable_region_count": skipped_mutable_count,
        "payload_regions_match": mismatch_count == 0,
        "blocks": block_records,
    }


def run_sequence(
    exe: Path,
    loader_file: Path,
    rom_path: Path,
    ipl_file: Path,
    bootstrap: dict[str, Any],
    sequence: list[dict[str, Any]],
    apu_ram_out: Path,
) -> dict[str, Any]:
    sequence_text = ",".join(f"0x{int(item['bank']):02X}:0x{int(item['address']):04X}" for item in sequence)
    command = [
        str(exe),
        "--receiver",
        "ares_smp_ipl",
        "--bootstrap-bank",
        f"0x{int(bootstrap['bank']):02X}",
        "--bootstrap-address",
        f"0x{int(bootstrap['address']):04X}",
        "--sequence",
        sequence_text,
        "--ipl-file",
        str(ipl_file),
        "--loader-file",
        str(loader_file),
        "--rom-file",
        str(rom_path),
        "--stream-bank",
        f"0x{int(sequence[0]['bank']):02X}",
        "--stream-address",
        f"0x{int(sequence[0]['address']):04X}",
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
    bootstrap = pointer_by_pack[BOOTSTRAP_PACK_ID]
    records = loader_contract.get("records", [])
    if args.limit is not None:
        records = records[: args.limit]

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    out_records: list[dict[str, Any]] = []
    for record in records:
        stream_pack_ids = [int(stream["pack_id"]) for stream in record.get("streams", [])]
        sequence = [pointer_by_pack[pack_id] for pack_id in stream_pack_ids]
        expected = expected_track_ram(rom, pointer_by_pack, stream_pack_ids)
        safe_job = str(record["job_id"]).replace("/", "_")
        apu_ram_out = output.parent / f"{safe_job}-continuous-apu-ram.bin"
        run = run_sequence(exe, loader_file, rom_path, ipl_file, bootstrap, sequence, apu_ram_out)
        run["expected_apu_ram"] = expected
        run["payload_regions"] = payload_regions(apu_ram_out, expected) if apu_ram_out.exists() else None
        run["job_id"] = record["job_id"]
        run["track_id"] = int(record["track_id"])
        run["track_name"] = record.get("track_name")
        run["sequence_pack_ids"] = stream_pack_ids
        status = "ok" if run["returncode"] == 0 and (run["payload_regions"] or {}).get("payload_regions_match") else f"failed({run['returncode']})"
        print(f"- {record['job_id']}: {status}")
        out_records.append(run)

    match_count = sum(1 for record in out_records if (record.get("payload_regions") or {}).get("payload_regions_match"))
    summary = {
        "schema": "earthbound-decomp.c0ab06-continuous-track-load-frontier.v1",
        "status": "real_ares_smp_driver_loads_full_representative_track_pack_sequences",
        "source_policy": loader_contract.get("source_policy"),
        "remaining_shortcut": "The pack-load sequence is driven directly from the loader contract instead of executing the full CHANGE_MUSIC CPU control flow in the same run; the final track command is not yet delivered naturally after this continuous load sequence.",
        "loader_contract": str(Path(args.loader_contract)),
        "pack_contract": str(Path(args.pack_contract)),
        "handshake_executable": str(exe),
        "loader_fixture": str(loader_file),
        "ipl_file": str(ipl_file),
        "job_count": len(out_records),
        "payload_region_match_count": match_count,
        "mismatch_count": len(out_records) - match_count,
        "records": out_records,
    }
    write_json(output, summary)
    print(f"C0:AB06 continuous track load frontier: {match_count} / {len(out_records)} tracks matched")
    print(f"Wrote {output}")
    return 0 if summary["mismatch_count"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
