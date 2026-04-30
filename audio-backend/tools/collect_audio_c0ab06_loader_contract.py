#!/usr/bin/env python3
"""Collect a C0:AB06 LOAD_SPC700_DATA loader contract from load-apply evidence."""

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

import audio_pack_contracts
import rom_tools


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONTRACT = ROOT / "manifests" / "audio-pack-contracts.json"
DEFAULT_FIXTURES = ROOT / "build" / "audio" / "cpu-routine-fixtures" / "audio-cpu-routine-fixtures.json"
DEFAULT_LOAD_APPLY_SUMMARY = ROOT / "build" / "audio" / "ares-wdc65816-full-change-music-load-apply-mailbox-smoke-jobs" / "smp-mailbox-smoke-summary.json"
DEFAULT_OUTPUT = ROOT / "build" / "audio" / "c0ab06-loader" / "c0ab06-loader-contract.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Collect C0:AB06 loader contract evidence.")
    parser.add_argument("--rom", help="Optional explicit EarthBound US ROM path.")
    parser.add_argument("--contract", default=str(DEFAULT_CONTRACT), help="Audio pack contract JSON.")
    parser.add_argument("--fixtures", default=str(DEFAULT_FIXTURES), help="CPU routine fixture manifest JSON.")
    parser.add_argument("--load-apply-summary", default=str(DEFAULT_LOAD_APPLY_SUMMARY), help="Full CHANGE_MUSIC load-apply smoke summary JSON.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Contract JSON output.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_contract(path: Path) -> dict[str, Any]:
    if path.exists():
        return load_json(path)
    return audio_pack_contracts.build_audio_contract()


def fixture_by_id(fixtures: dict[str, Any], fixture_id: str) -> dict[str, Any] | None:
    for record in fixtures.get("records", []):
        if record.get("id") == fixture_id:
            return record
    return None


def pack_maps(contract: dict[str, Any]) -> tuple[dict[int, dict[str, Any]], dict[tuple[str, str], dict[str, Any]]]:
    by_id = {int(pack["pack_id"]): pack for pack in contract["audio_packs"]}
    by_pointer: dict[tuple[str, str], dict[str, Any]] = {}
    for pack in by_id.values():
        pointer = pack.get("pointer") or {}
        if pointer:
            by_pointer[(f"0x{int(str(pointer['address']), 16):04X}", f"0x{int(str(pointer['bank']), 16):04X}")] = pack
    return by_id, by_pointer


def stream_record(rom: bytes, pack: dict[str, Any]) -> dict[str, Any]:
    data = audio_pack_contracts.slice_range(rom, audio_pack_contracts.parse_cpu_range(pack["range"]))
    parsed = audio_pack_contracts.parse_load_spc700_stream(data)
    payload_blocks = [block for block in parsed.blocks if not block.terminal]
    terminal_blocks = [block for block in parsed.blocks if block.terminal]
    return {
        "pack_id": int(pack["pack_id"]),
        "pack_range": pack["range"],
        "pack_sha1": hashlib.sha1(data).hexdigest(),
        "parse_status": parsed.status,
        "consumed_bytes": parsed.consumed_bytes,
        "payload_block_count": len(payload_blocks),
        "terminal_block_count": len(terminal_blocks),
        "payload_bytes": sum(block.count for block in payload_blocks),
        "destination_roles": dict(Counter(block.role_guess for block in payload_blocks)),
        "blocks": [
            {
                "index": block.index,
                "terminal": block.terminal,
                "stream_offset": f"0x{block.stream_offset:04X}",
                "destination": f"0x{block.destination:04X}",
                "payload_bytes": block.count,
                "payload_sha1": block.sha1,
                "role_guess": block.role_guess,
            }
            for block in parsed.blocks
        ],
    }


def collect(contract: dict[str, Any], fixtures: dict[str, Any], load_apply_summary: dict[str, Any], rom: bytes) -> dict[str, Any]:
    _packs_by_id, packs_by_pointer = pack_maps(contract)
    loader_fixture = fixture_by_id(fixtures, "c0_ab06_load_spc700_data_stream")
    records: list[dict[str, Any]] = []
    totals = Counter()
    mismatches: list[str] = []
    role_counts: Counter[str] = Counter()

    for record in load_apply_summary.get("records", []):
        job_id = str(record.get("job_id", ""))
        probe = (record.get("smoke", {}) or {}).get("cpu_instruction_probe", {}) or {}
        expected_streams: list[dict[str, Any]] = []
        for arg in probe.get("load_spc700_data_stub_args", []):
            key = (str(arg.get("a")), str(arg.get("x")))
            pack = packs_by_pointer.get(key)
            if pack is None:
                expected_streams.append({"pointer": {"a": key[0], "x": key[1]}, "error": "pointer not in pack table"})
                continue
            stream = stream_record(rom, pack)
            expected_streams.append(stream)
            totals["streams"] += 1
            totals["blocks"] += stream["payload_block_count"]
            totals["bytes"] += stream["payload_bytes"]
            role_counts.update(stream["destination_roles"])

        expected_stream_count = len([stream for stream in expected_streams if "error" not in stream])
        expected_block_count = sum(int(stream.get("payload_block_count", 0)) for stream in expected_streams)
        expected_byte_count = sum(int(stream.get("payload_bytes", 0)) for stream in expected_streams)
        applied_stream_count = int(probe.get("load_spc700_data_applied_streams", 0))
        applied_block_count = int(probe.get("load_spc700_data_applied_blocks", 0))
        applied_byte_count = int(probe.get("load_spc700_data_applied_bytes", 0))
        applied_error_count = int(probe.get("load_spc700_data_apply_errors", -1))
        match = (
            expected_stream_count == applied_stream_count
            and expected_block_count == applied_block_count
            and expected_byte_count == applied_byte_count
            and applied_error_count == 0
            and all("error" not in stream for stream in expected_streams)
        )
        if not match:
            mismatches.append(job_id)
        records.append(
            {
                "job_id": job_id,
                "track_id": int(record.get("track_id", 0)),
                "track_name": record.get("track_name"),
                "expected_stream_count": expected_stream_count,
                "applied_stream_count": applied_stream_count,
                "expected_payload_block_count": expected_block_count,
                "applied_payload_block_count": applied_block_count,
                "expected_payload_bytes": expected_byte_count,
                "applied_payload_bytes": applied_byte_count,
                "applied_error_count": applied_error_count,
                "matches_load_apply_probe": match,
                "streams": expected_streams,
            }
        )

    return {
        "schema": "earthbound-decomp.c0ab06-loader-contract.v1",
        "source_policy": contract["source_policy"],
        "loader_fixture": loader_fixture,
        "load_apply_summary": str(DEFAULT_LOAD_APPLY_SUMMARY),
        "job_count": len(records),
        "mismatch_count": len(mismatches),
        "mismatches": mismatches,
        "totals": {
            "streams": int(totals["streams"]),
            "payload_blocks": int(totals["blocks"]),
            "payload_bytes": int(totals["bytes"]),
            "destination_roles": dict(role_counts),
        },
        "protocol_boundary": {
            "current_status": "real_C0AB06_bytes_are_fixture_checked_semantic_payload_application_matches_load_apply_probe",
            "remaining_shortcut": "APUIO byte-level sender/receiver acknowledgement loop is not yet executed against real SMP receiver code.",
            "next_step": "Execute C0:AB06 through WDC65816 while a modeled or real APU receiver acknowledges APUIO0/1/2/3, then compare the resulting APU RAM and key-on snapshots against the load-apply corpus.",
        },
        "records": records,
    }


def main() -> int:
    args = parse_args()
    contract = load_contract(Path(args.contract))
    fixtures = load_json(Path(args.fixtures))
    load_apply_summary = load_json(Path(args.load_apply_summary))
    rom_path = rom_tools.find_rom(args.rom)
    rom = rom_tools.load_rom(rom_path)
    result = collect(contract, fixtures, load_apply_summary, rom)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(
        "Collected C0:AB06 loader contract: "
        f"{result['job_count']} jobs, {result['mismatch_count']} mismatches, "
        f"{result['totals']['streams']} streams, "
        f"{result['totals']['payload_blocks']} blocks, "
        f"{result['totals']['payload_bytes']} bytes"
    )
    print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
