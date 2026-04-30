#!/usr/bin/env python3
"""Run real C0:AB06 LOAD_SPC700_DATA bytes against selected audio streams."""

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

import rom_tools
import audio_pack_contracts


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_LOADER_CONTRACT = ROOT / "build" / "audio" / "c0ab06-loader" / "c0ab06-loader-contract.json"
DEFAULT_PACK_CONTRACT = ROOT / "manifests" / "audio-pack-contracts.json"
DEFAULT_OUT = ROOT / "build" / "audio" / "c0ab06-loader-handshake" / "c0ab06-loader-handshake-summary.json"
DEFAULT_EXE = (
    ROOT
    / "build"
    / "audio"
    / "ares-c0ab06-loader-handshake-msvc"
    / "RelWithDebInfo"
    / "earthbound_ares_c0ab06_loader_handshake.exe"
)
DEFAULT_LOADER_FILE = ROOT / "build" / "audio" / "cpu-routine-fixtures" / "c0-ab06-load-spc700-data-stream.bin"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the C0:AB06 loader handshake corpus.")
    parser.add_argument("--rom", help="Optional explicit EarthBound US ROM path.")
    parser.add_argument("--exe", default=str(DEFAULT_EXE), help="Built C0:AB06 loader handshake executable.")
    parser.add_argument("--loader-file", default=str(DEFAULT_LOADER_FILE), help="C0:AB06 routine fixture.")
    parser.add_argument("--loader-contract", default=str(DEFAULT_LOADER_CONTRACT), help="C0:AB06 loader contract JSON.")
    parser.add_argument("--pack-contract", default=str(DEFAULT_PACK_CONTRACT), help="Audio pack contract JSON.")
    parser.add_argument("--output", default=str(DEFAULT_OUT), help="Ignored corpus summary JSON.")
    parser.add_argument("--limit", type=int, help="Optional unique-pack limit for debugging.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def sha1(data: bytes) -> str:
    return hashlib.sha1(data).hexdigest()


def parse_hex_word(text: str) -> int:
    return int(str(text), 16)


def pack_pointer_map(pack_contract: dict[str, Any]) -> dict[int, dict[str, Any]]:
    packs: dict[int, dict[str, Any]] = {}
    for pack in pack_contract.get("audio_packs", []):
        pointer = pack.get("pointer") or {}
        if not pointer:
            continue
        packs[int(pack["pack_id"])] = {
            "pack_id": int(pack["pack_id"]),
            "bank": parse_hex_word(pointer["bank"]),
            "address": parse_hex_word(pointer["address"]),
            "cpu": pointer.get("cpu"),
            "range": pack.get("range"),
        }
    return packs


def expected_streams(loader_contract: dict[str, Any], pointer_by_pack: dict[int, dict[str, Any]]) -> tuple[list[dict[str, Any]], list[str]]:
    streams: list[dict[str, Any]] = []
    errors: list[str] = []
    seen: set[int] = set()
    for record in loader_contract.get("records", []):
        for stream in record.get("streams", []):
            pack_id = int(stream.get("pack_id", -1))
            pointer = pointer_by_pack.get(pack_id)
            if pointer is None:
                errors.append(f"{record.get('job_id')}: pack {pack_id} has no pointer")
                continue
            occurrence = {
                "job_id": record.get("job_id"),
                "track_id": record.get("track_id"),
                "track_name": record.get("track_name"),
                "pack_id": pack_id,
                "expected_payload_bytes": int(stream.get("payload_bytes", 0)),
                "expected_payload_block_count": int(stream.get("payload_block_count", 0)),
                "expected_terminal_block_count": int(stream.get("terminal_block_count", 0)),
                "pack_range": stream.get("pack_range"),
            }
            streams.append(occurrence)
            seen.add(pack_id)
    return streams, errors


def expected_apu_ram_for_pack(rom: bytes, pointer: dict[str, Any]) -> dict[str, Any]:
    pack_range = pointer.get("range")
    if not pack_range:
        raise ValueError(f"pack {pointer.get('pack_id')} has no ROM range")
    data = audio_pack_contracts.slice_range(rom, audio_pack_contracts.parse_cpu_range(pack_range))
    parsed = audio_pack_contracts.parse_load_spc700_stream(data)
    apu_ram = bytearray(0x10000)
    blocks: list[dict[str, Any]] = []
    for block in parsed.blocks:
        if block.terminal:
            continue
        if block.payload_offset is None:
            raise ValueError(f"pack {pointer.get('pack_id')} block {block.index} missing payload offset")
        payload = data[block.payload_offset:block.payload_offset + block.count]
        destination = int(block.destination)
        apu_ram[destination:destination + len(payload)] = payload
        blocks.append(
            {
                "index": block.index,
                "destination": f"0x{destination:04X}",
                "payload_bytes": len(payload),
                "payload_sha1": sha1(payload),
                "final_region_sha1": sha1(bytes(apu_ram[destination:destination + len(payload)])),
                "role_guess": block.role_guess,
            }
        )
    return {
        "parse_status": parsed.status,
        "consumed_bytes": parsed.consumed_bytes,
        "payload_block_count": len(blocks),
        "payload_bytes": sum(int(block["payload_bytes"]) for block in blocks),
        "apu_ram_sha1": sha1(bytes(apu_ram)),
        "apu_ram_nonzero_count": sum(1 for byte in apu_ram if byte),
        "blocks": blocks,
    }


def apu_ram_metadata(path: Path, expected: dict[str, Any]) -> dict[str, Any]:
    data = path.read_bytes()
    blocks: list[dict[str, Any]] = []
    for block in expected.get("blocks", []):
        destination = int(str(block["destination"]), 16)
        size = int(block["payload_bytes"])
        actual_region = data[destination:destination + size]
        actual_sha1 = sha1(actual_region)
        blocks.append(
            {
                "index": block["index"],
                "destination": block["destination"],
                "payload_bytes": size,
                "expected_final_region_sha1": block["final_region_sha1"],
                "actual_final_region_sha1": actual_sha1,
                "matches": actual_sha1 == block["final_region_sha1"],
            }
        )
    return {
        "path": str(path),
        "bytes": len(data),
        "sha1": sha1(data),
        "expected_sha1": expected["apu_ram_sha1"],
        "matches_expected": sha1(data) == expected["apu_ram_sha1"],
        "nonzero_count": sum(1 for byte in data if byte),
        "expected_nonzero_count": expected["apu_ram_nonzero_count"],
        "blocks": blocks,
        "block_mismatch_count": sum(1 for block in blocks if not block["matches"]),
    }


def run_handshake(
    exe: Path,
    loader_file: Path,
    rom_path: Path,
    pointer: dict[str, Any],
    apu_ram_out: Path,
    expected_apu_ram: dict[str, Any],
) -> dict[str, Any]:
    command = [
        str(exe),
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
    completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
    try:
        handshake = json.loads(completed.stdout)
    except json.JSONDecodeError as error:
        handshake = {
            "schema": "earthbound-decomp.c0ab06-loader-handshake.v1",
            "parse_error": str(error),
            "stdout": completed.stdout,
        }
    apu_ram = apu_ram_metadata(apu_ram_out, expected_apu_ram) if apu_ram_out.exists() else None
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
        "expected_apu_ram": expected_apu_ram,
        "apu_ram": apu_ram,
    }


def occurrence_match(occurrence: dict[str, Any], handshake_record: dict[str, Any]) -> tuple[bool, list[str]]:
    handshake = handshake_record.get("handshake") or {}
    reasons: list[str] = []
    if int(handshake_record.get("returncode", -1)) != 0:
        reasons.append(f"returncode {handshake_record.get('returncode')}")
    if not handshake.get("ok"):
        reasons.append("handshake did not report ok")
    if int(handshake.get("payload_bytes", -1)) != int(occurrence["expected_payload_bytes"]):
        reasons.append(
            "payload bytes "
            f"{handshake.get('payload_bytes')} != {occurrence['expected_payload_bytes']}"
        )
    if int(handshake.get("payload_writes", -1)) != int(occurrence["expected_payload_bytes"]):
        reasons.append(
            "payload writes "
            f"{handshake.get('payload_writes')} != {occurrence['expected_payload_bytes']}"
        )
    if int(handshake.get("block_start_tokens", -1)) != int(occurrence["expected_payload_block_count"]):
        reasons.append(
            "block tokens "
            f"{handshake.get('block_start_tokens')} != {occurrence['expected_payload_block_count']}"
        )
    if int(handshake.get("terminal_tokens", -1)) != int(occurrence["expected_terminal_block_count"]):
        reasons.append(
            "terminal tokens "
            f"{handshake.get('terminal_tokens')} != {occurrence['expected_terminal_block_count']}"
        )
    if handshake.get("final_pc") != "0x008004":
        reasons.append(f"final PC {handshake.get('final_pc')} != 0x008004")
    apu_ram = handshake_record.get("apu_ram") or {}
    if not apu_ram.get("matches_expected"):
        reasons.append("APU RAM dump does not match semantic reconstruction")
    if int(apu_ram.get("block_mismatch_count", -1)) != 0:
        reasons.append(f"APU RAM block mismatch count {apu_ram.get('block_mismatch_count')}")
    return not reasons, reasons


def main() -> int:
    args = parse_args()
    exe = Path(args.exe)
    loader_file = Path(args.loader_file)
    if not exe.exists():
        raise FileNotFoundError(f"missing C0:AB06 loader handshake executable: {exe}")
    if not loader_file.exists():
        raise FileNotFoundError(f"missing C0:AB06 loader fixture: {loader_file}")

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
    expected_apu_ram_by_pack = {
        pack_id: expected_apu_ram_for_pack(rom, pointer_by_pack[pack_id])
        for pack_id in unique_pack_ids
    }

    handshake_by_pack: dict[int, dict[str, Any]] = {}
    for pack_id in unique_pack_ids:
        pointer = pointer_by_pack[pack_id]
        apu_ram_out = output.parent / f"pack-{pack_id:03d}-apu-ram.bin"
        record = run_handshake(exe, loader_file, rom_path, pointer, apu_ram_out, expected_apu_ram_by_pack[pack_id])
        handshake_by_pack[pack_id] = record
        status = (
            "ok"
            if record["returncode"] == 0 and record["handshake"].get("ok") and (record.get("apu_ram") or {}).get("matches_expected")
            else f"failed({record['returncode']})"
        )
        print(f"- pack {pack_id:03d} {pointer.get('cpu')}: {status}")

    occurrence_records: list[dict[str, Any]] = []
    mismatch_records: list[dict[str, Any]] = []
    for occurrence in occurrences:
        pack_id = int(occurrence["pack_id"])
        handshake_record = handshake_by_pack.get(pack_id)
        if handshake_record is None:
            occurrence_record = {
                **occurrence,
                "matches_handshake": False,
                "mismatch_reasons": ["pack not executed because of --limit"],
            }
        else:
            matches, reasons = occurrence_match(occurrence, handshake_record)
            occurrence_record = {
                **occurrence,
                "matches_handshake": matches,
                "mismatch_reasons": reasons,
            }
        occurrence_records.append(occurrence_record)
        if not occurrence_record["matches_handshake"]:
            mismatch_records.append(occurrence_record)

    total_payload_bytes = sum(int(record.get("expected_payload_bytes", 0)) for record in occurrence_records)
    total_payload_blocks = sum(int(record.get("expected_payload_block_count", 0)) for record in occurrence_records)
    executed_payload_bytes = sum(
        int(record.get("handshake", {}).get("payload_bytes", 0))
        for record in handshake_by_pack.values()
    )
    executed_apu_ram_match_count = sum(
        1 for record in handshake_by_pack.values()
        if (record.get("apu_ram") or {}).get("matches_expected")
    )
    summary = {
        "schema": "earthbound-decomp.c0ab06-loader-handshake-corpus.v1",
        "source_policy": loader_contract.get("source_policy"),
        "status": "real_C0AB06_cpu_loader_executed_against_modeled_apuio_receiver",
        "remaining_shortcut": "APUIO receiver acknowledgements are modeled; this does not yet execute the real SPC-side receiver loop.",
        "loader_contract": str(Path(args.loader_contract)),
        "pack_contract": str(Path(args.pack_contract)),
        "handshake_executable": str(exe),
        "loader_fixture": str(loader_file),
        "unique_pack_count": len(unique_pack_ids),
        "executed_unique_pack_count": len(handshake_by_pack),
        "stream_occurrence_count": len(occurrence_records),
        "matched_occurrence_count": sum(1 for record in occurrence_records if record["matches_handshake"]),
        "executed_apu_ram_match_count": executed_apu_ram_match_count,
        "mismatch_count": len(mismatch_records) + len(setup_errors),
        "setup_errors": setup_errors,
        "totals": {
            "selected_payload_blocks": total_payload_blocks,
            "selected_payload_bytes": total_payload_bytes,
            "executed_unique_payload_bytes": executed_payload_bytes,
            "executed_unique_apu_ram_matches": executed_apu_ram_match_count,
        },
        "handshakes": [handshake_by_pack[pack_id] for pack_id in sorted(handshake_by_pack)],
        "occurrences": occurrence_records,
        "mismatches": mismatch_records,
    }
    write_json(output, summary)
    print(
        "C0:AB06 loader handshake corpus: "
        f"{summary['matched_occurrence_count']} / {summary['stream_occurrence_count']} occurrences matched, "
        f"{summary['executed_unique_pack_count']} unique packs executed"
    )
    print(f"Wrote {output}")
    return 0 if summary["mismatch_count"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
