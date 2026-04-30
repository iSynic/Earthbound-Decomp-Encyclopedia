#!/usr/bin/env python3
"""Write a dry-run backend result for one audio backend job.

This deliberately does not render audio. It exists to exercise the job/result
schema before an ares or snes_spc harness is available.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_JOBS = ROOT / "build" / "audio" / "backend-jobs" / "ares-jobs.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a dry-run audio backend result for one job.")
    parser.add_argument("--jobs", default=str(DEFAULT_JOBS), help="Backend job index path.")
    parser.add_argument("--job-id", default="ares-track-046-onett", help="Job id to stub.")
    parser.add_argument(
        "--status",
        default="unsupported",
        choices=["failed", "unsupported"],
        help="Dry-run status to write. Successful outputs require a real backend.",
    )
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def find_job(index: dict[str, Any], job_id: str) -> dict[str, Any]:
    for job in index.get("jobs", []):
        if job.get("job_id") == job_id:
            return job
    raise ValueError(f"job id not found: {job_id}")


def build_result(job: dict[str, Any], status: str) -> dict[str, Any]:
    return {
        "schema": "earthbound-decomp.audio-backend-result.v1",
        "job_id": job["job_id"],
        "backend_id": job["backend_id"],
        "backend_version": "dry-run-stub",
        "status": status,
        "input_fixture_path": job["fixture_path"],
        "input_apu_ram_sha1": job["input_apu_ram_sha1"],
        "outputs": [],
        "diagnostics": {
            "execution_mode": "dry_run_no_emulator",
            "handshake_policy": "not_executed",
            "timing_basis": "not_applicable",
            "message": "Schema-only dry run. No SPC, PCM, or WAV output was produced.",
        },
    }


def main() -> int:
    args = parse_args()
    index = load_json(Path(args.jobs))
    job = find_job(index, args.job_id)
    output_dir = Path(job["output_dir"])
    output_dir.mkdir(parents=True, exist_ok=True)
    result = build_result(job, args.status)
    result_path = output_dir / "result.json"
    result_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote dry-run backend result -> {result_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
