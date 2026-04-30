#!/usr/bin/env python3
"""Validate a collected audio backend result summary."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SUMMARY = ROOT / "build" / "audio" / "backend-jobs" / "ares-result-summary.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate an audio backend result summary.")
    parser.add_argument("summary", nargs="?", default=str(DEFAULT_SUMMARY))
    return parser.parse_args()


def validate(summary: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if summary.get("schema") != "earthbound-decomp.audio-backend-result-summary.v1":
        errors.append(f"unexpected schema: {summary.get('schema')}")
    results = summary.get("results", [])
    if int(summary.get("job_count", -1)) != len(results):
        errors.append(f"job_count {summary.get('job_count')} does not match {len(results)} results")
    status_total = sum(int(count) for count in summary.get("status_counts", {}).values())
    if status_total != len(results):
        errors.append(f"status_counts total {status_total} does not match {len(results)} results")
    validation_total = sum(int(count) for count in summary.get("validation_counts", {}).values())
    if validation_total != len(results):
        errors.append(f"validation_counts total {validation_total} does not match {len(results)} results")
    seen: set[str] = set()
    for result in results:
        job_id = str(result.get("job_id", ""))
        if not job_id:
            errors.append("result record without job_id")
        elif job_id in seen:
            errors.append(f"duplicate result record {job_id}")
        seen.add(job_id)
        if result.get("result_exists") and not Path(str(result.get("result_path"))).exists():
            errors.append(f"{job_id}: result_exists is true but path is missing")
    return errors


def main() -> int:
    args = parse_args()
    path = Path(args.summary)
    summary = json.loads(path.read_text(encoding="utf-8"))
    errors = validate(summary)
    if errors:
        print("Audio backend result summary validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "Audio backend result summary validation OK: "
        f"{summary['job_count']} jobs, statuses {summary['status_counts']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
