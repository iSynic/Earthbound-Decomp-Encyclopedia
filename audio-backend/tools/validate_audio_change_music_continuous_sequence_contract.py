#!/usr/bin/env python3
"""Validate CHANGE_MUSIC to continuous real-driver C0:AB06 sequence evidence."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONTRACT = (
    ROOT
    / "build"
    / "audio"
    / "change-music-continuous-sequence-contract"
    / "change-music-continuous-sequence-contract.json"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate CHANGE_MUSIC continuous C0:AB06 sequence evidence.")
    parser.add_argument("contract", nargs="?", default=str(DEFAULT_CONTRACT))
    return parser.parse_args()


def validate(contract: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if contract.get("schema") != "earthbound-decomp.change-music-continuous-sequence-contract.v1":
        errors.append(f"unexpected schema: {contract.get('schema')}")
    if contract.get("status") != "change_music_load_order_matches_continuous_real_driver_c0ab06_sequence":
        errors.append(f"unexpected status: {contract.get('status')}")
    records = contract.get("records", [])
    job_count = int(contract.get("job_count", -1))
    match_count = int(contract.get("match_count", -1))
    if job_count != len(records):
        errors.append(f"job_count {job_count} does not match {len(records)} records")
    if job_count <= 0:
        errors.append("job_count must be positive")
    if match_count != job_count:
        errors.append(f"match_count {match_count} does not match job_count {job_count}")
    if int(contract.get("mismatch_count", -1)) != 0:
        errors.append(f"mismatch_count is {contract.get('mismatch_count')}")
    if contract.get("mismatches"):
        errors.append(f"mismatches are present: {contract.get('mismatches')}")
    for record in records:
        job_id = str(record.get("job_id", ""))
        if not record.get("all_match"):
            errors.append(f"{job_id}: all_match is false")
        matches = record.get("matches") or {}
        for key, value in matches.items():
            if value is not True:
                errors.append(f"{job_id}: {key} is {value}")
        expected_pack_ids = record.get("expected_pack_ids", [])
        if not expected_pack_ids:
            errors.append(f"{job_id}: empty expected pack sequence")
        if record.get("loader_contract_pack_ids") != expected_pack_ids:
            errors.append(f"{job_id}: loader pack ids differ from expected")
        if record.get("continuous_frontier_pack_ids") != expected_pack_ids:
            errors.append(f"{job_id}: continuous pack ids differ from expected")
        if record.get("change_music_pointer_args") != record.get("continuous_frontier_pointer_args"):
            errors.append(f"{job_id}: continuous pointer args differ from CHANGE_MUSIC args")
    return errors


def main() -> int:
    args = parse_args()
    contract = json.loads(Path(args.contract).read_text(encoding="utf-8"))
    errors = validate(contract)
    if errors:
        print("CHANGE_MUSIC continuous sequence contract validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "CHANGE_MUSIC continuous sequence contract validation OK: "
        f"{contract['match_count']} / {contract['job_count']} jobs"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
