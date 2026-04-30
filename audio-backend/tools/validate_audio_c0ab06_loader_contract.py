#!/usr/bin/env python3
"""Validate C0:AB06 LOAD_SPC700_DATA loader contract evidence."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONTRACT = ROOT / "build" / "audio" / "c0ab06-loader" / "c0ab06-loader-contract.json"
EXPECTED_C0AB06_SHA1 = "e0cfb01348233939a0c4d98c42a0d8350f0ce6d9"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate C0:AB06 loader contract evidence.")
    parser.add_argument("contract", nargs="?", default=str(DEFAULT_CONTRACT))
    return parser.parse_args()


def validate(contract: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if contract.get("schema") != "earthbound-decomp.c0ab06-loader-contract.v1":
        errors.append(f"unexpected schema: {contract.get('schema')}")
    fixture = contract.get("loader_fixture") or {}
    if fixture.get("id") != "c0_ab06_load_spc700_data_stream":
        errors.append("missing C0:AB06 loader fixture")
    if fixture.get("sha1") != EXPECTED_C0AB06_SHA1:
        errors.append(f"C0:AB06 fixture SHA-1 mismatch: {fixture.get('sha1')}")
    if int(contract.get("mismatch_count", -1)) != 0:
        errors.append(f"mismatch_count is {contract.get('mismatch_count')}")
    if contract.get("mismatches"):
        errors.append(f"mismatches present: {contract.get('mismatches')}")
    records = contract.get("records", [])
    if int(contract.get("job_count", -1)) != len(records):
        errors.append("job_count does not match record count")
    totals = contract.get("totals", {})
    if int(totals.get("streams", 0)) <= 0 or int(totals.get("payload_blocks", 0)) <= 0 or int(totals.get("payload_bytes", 0)) <= 0:
        errors.append("totals must include streams, payload blocks, and payload bytes")
    for record in records:
        job_id = record.get("job_id")
        if not record.get("matches_load_apply_probe"):
            errors.append(f"{job_id}: expected stream totals do not match load-apply probe")
        if int(record.get("applied_error_count", -1)) != 0:
            errors.append(f"{job_id}: load-apply probe reported apply errors")
        if int(record.get("expected_stream_count", 0)) <= 0:
            errors.append(f"{job_id}: no expected streams")
        for stream in record.get("streams", []):
            if stream.get("parse_status") != "ok":
                errors.append(f"{job_id}: stream parse status is {stream.get('parse_status')}")
            if int(stream.get("terminal_block_count", 0)) != 1:
                errors.append(f"{job_id}: stream does not have exactly one terminal block")
    return errors


def main() -> int:
    args = parse_args()
    contract = json.loads(Path(args.contract).read_text(encoding="utf-8"))
    errors = validate(contract)
    if errors:
        print("C0:AB06 loader contract validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    totals = contract["totals"]
    print(
        "C0:AB06 loader contract validation OK: "
        f"{contract['job_count']} jobs, "
        f"{totals['streams']} streams, "
        f"{totals['payload_blocks']} blocks, "
        f"{totals['payload_bytes']} bytes"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
