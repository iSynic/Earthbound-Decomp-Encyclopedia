#!/usr/bin/env python3
"""Collect backend result status across an audio backend job index."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import validate_audio_backend_result


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_JOBS = ROOT / "build" / "audio" / "backend-jobs" / "ares-jobs.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Collect backend result status across a job index.")
    parser.add_argument("jobs", nargs="?", default=str(DEFAULT_JOBS), help="Backend job index path.")
    parser.add_argument("--json", help="Optional JSON summary output path.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def collect(index: dict[str, Any], jobs_path: Path) -> dict[str, Any]:
    records: list[dict[str, Any]] = []
    status_counts: Counter[str] = Counter()
    validation_counts: Counter[str] = Counter()
    backend_version_counts: Counter[str] = Counter()

    for job in index.get("jobs", []):
        result_path = Path(job["result_path"])
        record = {
            "job_id": job["job_id"],
            "track_id": job["track_id"],
            "track_name": job["track_name"],
            "backend_id": job["backend_id"],
            "result_path": str(result_path),
            "result_exists": result_path.exists(),
            "status": "pending",
            "valid": False,
            "errors": [],
        }
        if result_path.exists():
            result = load_json(result_path)
            errors = validate_audio_backend_result.validate(result, result_path, job)
            record["status"] = result.get("status", "unknown")
            record["backend_version"] = result.get("backend_version", "unknown")
            record["valid"] = not errors
            record["errors"] = errors
            backend_version_counts[str(record["backend_version"])] += 1
        status_counts[str(record["status"])] += 1
        validation_counts["valid" if record["valid"] else "invalid_or_pending"] += 1
        records.append(record)

    return {
        "schema": "earthbound-decomp.audio-backend-result-summary.v1",
        "job_index": str(jobs_path),
        "backend_id": index.get("backend_id"),
        "job_count": len(records),
        "status_counts": dict(status_counts),
        "validation_counts": dict(validation_counts),
        "backend_version_counts": dict(backend_version_counts),
        "results": records,
    }


def print_summary(summary: dict[str, Any]) -> None:
    print(
        "Audio backend result summary: "
        f"{summary['job_count']} {summary['backend_id']} jobs, "
        f"statuses {summary['status_counts']}, "
        f"validation {summary['validation_counts']}, "
        f"backend versions {summary.get('backend_version_counts', {})}"
    )
    for record in summary["results"]:
        if record["result_exists"]:
            print(
                f"- {record['job_id']}: {record['status']} "
                f"({'valid' if record['valid'] else 'invalid'})"
            )


def main() -> int:
    args = parse_args()
    jobs_path = Path(args.jobs)
    index = load_json(jobs_path)
    summary = collect(index, jobs_path)
    if args.json:
        output_path = Path(args.json)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print_summary(summary)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
