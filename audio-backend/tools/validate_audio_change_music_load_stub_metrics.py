#!/usr/bin/env python3
"""Validate CHANGE_MUSIC load-path stub metrics."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_METRICS = ROOT / "build" / "audio" / "ares-wdc65816-full-change-music-load-stub-mailbox-smoke-jobs" / "change-music-load-stub-metrics.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate CHANGE_MUSIC load-stub metrics.")
    parser.add_argument("metrics", nargs="?", default=str(DEFAULT_METRICS))
    return parser.parse_args()


def validate(metrics: dict) -> list[str]:
    errors: list[str] = []
    if metrics.get("schema") != "earthbound-decomp.change-music-load-stub-metrics.v1":
        errors.append(f"unexpected schema: {metrics.get('schema')}")
    records = metrics.get("records", [])
    job_count = int(metrics.get("job_count", -1))
    if job_count != len(records):
        errors.append(f"job_count {job_count} does not match {len(records)} records")
    if int(metrics.get("mismatch_count", -1)) != 0:
        errors.append(f"mismatch_count is {metrics.get('mismatch_count')}")
    if metrics.get("mismatches"):
        errors.append(f"mismatches are present: {metrics.get('mismatches')}")
    if not records:
        errors.append("no records")
    for record in records:
        job_id = str(record.get("job_id", ""))
        actual = record.get("actual_load_args", [])
        expected = [item for item in record.get("expected_loads", []) if "error" not in item]
        if not job_id:
            errors.append("record without job_id")
        if not record.get("matches_expected"):
            errors.append(f"{job_id}: actual load args do not match expected table loads")
        if int(record.get("call_count", -1)) != int(record.get("expected_call_count", -2)):
            errors.append(f"{job_id}: call_count does not match expected_call_count")
        if len(actual) != int(record.get("call_count", -1)):
            errors.append(f"{job_id}: actual_load_args length does not match call_count")
        if len(expected) != int(record.get("expected_call_count", -1)):
            errors.append(f"{job_id}: expected_loads length does not match expected_call_count")
        for item in record.get("expected_loads", []):
            if "error" in item:
                errors.append(f"{job_id}: expected load error for pack {item.get('pack_id')}: {item.get('error')}")
    return errors


def main() -> int:
    args = parse_args()
    metrics = json.loads(Path(args.metrics).read_text(encoding="utf-8"))
    errors = validate(metrics)
    if errors:
        print("CHANGE_MUSIC load-stub metrics validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "CHANGE_MUSIC load-stub metrics validation OK: "
        f"{metrics['job_count']} jobs, "
        f"{metrics['mismatch_count']} mismatches, "
        f"call counts {metrics['call_count_distribution']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
