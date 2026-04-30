#!/usr/bin/env python3
"""Validate generated audio backend job manifests."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_JOBS = ROOT / "build" / "audio" / "backend-jobs" / "ares-jobs.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate generated audio backend jobs.")
    parser.add_argument("jobs", nargs="?", default=str(DEFAULT_JOBS))
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if data.get("schema") != "earthbound-decomp.audio-backend-job-index.v1":
        errors.append(f"unexpected schema: {data.get('schema')}")
    jobs = data.get("jobs", [])
    if int(data.get("job_count", -1)) != len(jobs):
        errors.append(f"job_count {data.get('job_count')} does not match {len(jobs)} jobs")
    if not jobs:
        errors.append("job index has no jobs")

    seen: set[str] = set()
    for job in jobs:
        job_id = str(job.get("job_id", ""))
        if not job_id:
            errors.append("job without job_id")
        elif job_id in seen:
            errors.append(f"duplicate job_id {job_id}")
        seen.add(job_id)

        fixture_path = Path(str(job.get("fixture_path", "")))
        if not fixture_path.exists():
            errors.append(f"{job_id}: missing fixture {fixture_path}")
        output_dir = Path(str(job.get("output_dir", "")))
        if output_dir.suffix:
            errors.append(f"{job_id}: output_dir looks like a file path: {output_dir}")
        if not job.get("expected_outputs"):
            errors.append(f"{job_id}: no expected outputs")
        result_path = Path(str(job.get("result_path", "")))
        if result_path.name != "result.json":
            errors.append(f"{job_id}: result_path must end with result.json")
        job_path = Path(str(job.get("job_path", "")))
        if job_path.name != "job.json":
            errors.append(f"{job_id}: job_path must end with job.json")
        elif not job_path.exists():
            errors.append(f"{job_id}: missing per-job manifest {job_path}")
        else:
            job_manifest = load_json(job_path)
            if job_manifest.get("job_id") != job_id:
                errors.append(f"{job_id}: per-job manifest has job_id {job_manifest.get('job_id')}")
            if job_manifest.get("result_path") != job.get("result_path"):
                errors.append(f"{job_id}: per-job manifest result_path differs from index")
        options = job.get("render_options", {})
        if int(options.get("sample_rate", 0)) <= 0:
            errors.append(f"{job_id}: invalid sample_rate")
        if int(options.get("channels", 0)) not in (1, 2):
            errors.append(f"{job_id}: invalid channel count")
        if float(options.get("seconds", 0.0)) <= 0:
            errors.append(f"{job_id}: invalid render duration")

    return errors


def main() -> int:
    args = parse_args()
    path = Path(args.jobs)
    data = load_json(path)
    errors = validate(data)
    if errors:
        print("Audio backend job validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Audio backend jobs validation OK: {data['job_count']} {data['backend_id']} jobs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
