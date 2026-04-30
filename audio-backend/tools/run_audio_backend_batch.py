#!/usr/bin/env python3
"""Run or dry-run multiple audio backend jobs from a job index."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import collect_audio_backend_results
import run_audio_backend_job


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_JOBS = ROOT / "build" / "audio" / "backend-jobs" / "ares-jobs.json"
DEFAULT_SUMMARY = ROOT / "build" / "audio" / "backend-jobs" / "ares-result-summary.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run or dry-run multiple audio backend jobs.")
    parser.add_argument("--jobs", default=str(DEFAULT_JOBS), help="Backend job index path.")
    parser.add_argument(
        "--mode",
        default="dry-run-stub",
        choices=["dry-run-stub", "external", "native-ares"],
        help="Run schema-only dry runs or invoke an external backend command.",
    )
    parser.add_argument(
        "--ares-harness",
        default=str(run_audio_backend_job.DEFAULT_ARES_HARNESS),
        help="Path to the local native ares audio harness executable.",
    )
    parser.add_argument("--job-id", action="append", help="Specific job id to run. May be repeated.")
    parser.add_argument("--limit", type=int, help="Maximum number of selected jobs to run.")
    parser.add_argument("--force", action="store_true", help="Re-run jobs that already have result.json.")
    parser.add_argument("--stop-on-error", action="store_true", help="Stop at the first failed job.")
    parser.add_argument("--summary", default=str(DEFAULT_SUMMARY), help="Result summary JSON output path.")
    parser.add_argument(
        "--external",
        nargs=argparse.REMAINDER,
        help="External command vector for external mode. Use placeholders like {job} and {result}.",
    )
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def select_jobs(index: dict[str, Any], requested_ids: list[str] | None, *, force: bool) -> list[dict[str, Any]]:
    requested = set(requested_ids or [])
    jobs: list[dict[str, Any]] = []
    for job in index.get("jobs", []):
        if requested and job["job_id"] not in requested:
            continue
        if not force and Path(job["result_path"]).exists():
            continue
        jobs.append(job)
    missing = requested - {job["job_id"] for job in index.get("jobs", [])}
    if missing:
        raise ValueError(f"requested job ids not found: {', '.join(sorted(missing))}")
    return jobs


def run_one(
    job: dict[str, Any],
    jobs_path: Path,
    mode: str,
    external: list[str] | None,
    ares_harness: Path,
) -> dict[str, Any]:
    job_path = run_audio_backend_job.ensure_job_manifest(job)
    try:
        if mode == "dry-run-stub":
            result_path = run_audio_backend_job.write_dry_run_result(job)
        elif mode == "native-ares":
            result_path = run_audio_backend_job.run_native_ares_backend(job, job_path, ares_harness)
        else:
            result_path = run_audio_backend_job.run_external_backend(job, job_path, external)
        run_audio_backend_job.validate_result(result_path, jobs_path)
        return {
            "job_id": job["job_id"],
            "status": "completed",
            "result_path": str(result_path),
            "error": None,
        }
    except Exception as exc:
        return {
            "job_id": job["job_id"],
            "status": "failed",
            "result_path": job.get("result_path"),
            "error": str(exc),
        }


def write_summary(index: dict[str, Any], jobs_path: Path, summary_path: Path, batch: dict[str, Any]) -> None:
    result_summary = collect_audio_backend_results.collect(index, jobs_path)
    result_summary["last_batch"] = batch
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(json.dumps(result_summary, indent=2) + "\n", encoding="utf-8")
    collect_audio_backend_results.print_summary(result_summary)


def main() -> int:
    args = parse_args()
    jobs_path = Path(args.jobs)
    index = load_json(jobs_path)
    selected = select_jobs(index, args.job_id, force=args.force)
    if args.limit is not None:
        selected = selected[:args.limit]

    runs: list[dict[str, Any]] = []
    print(f"Selected {len(selected)} {index.get('backend_id')} jobs for {args.mode} mode")
    for job in selected:
        record = run_one(job, jobs_path, args.mode, args.external, Path(args.ares_harness))
        runs.append(record)
        print(f"- {record['job_id']}: {record['status']}")
        if record["error"]:
            print(f"  {record['error']}")
        if record["status"] == "failed" and args.stop_on_error:
            break

    batch = {
        "schema": "earthbound-decomp.audio-backend-batch-run.v1",
        "mode": args.mode,
        "selected_count": len(selected),
        "completed_count": sum(1 for run in runs if run["status"] == "completed"),
        "failed_count": sum(1 for run in runs if run["status"] == "failed"),
        "runs": runs,
    }
    write_summary(index, jobs_path, Path(args.summary), batch)
    return 1 if batch["failed_count"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
