#!/usr/bin/env python3
"""Run or dry-run one audio backend job.

The external mode intentionally avoids shell evaluation. Pass a command vector
after `--external`; placeholders are expanded in individual argv tokens:
`{job}`, `{result}`, `{fixture}`, and `{output_dir}`.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import build_audio_backend_result_stub
import validate_audio_backend_result


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_JOBS = ROOT / "build" / "audio" / "backend-jobs" / "ares-jobs.json"
DEFAULT_ARES_HARNESS = (
    ROOT
    / "build"
    / "audio"
    / "ares-audio-harness-msvc"
    / "RelWithDebInfo"
    / "earthbound_ares_audio_harness.exe"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run or dry-run one audio backend job.")
    parser.add_argument("job_id", help="Backend job id, such as ares-track-046-onett.")
    parser.add_argument("--jobs", default=str(DEFAULT_JOBS), help="Backend job index path.")
    parser.add_argument(
        "--mode",
        default="dry-run-stub",
        choices=["dry-run-stub", "external", "native-ares"],
        help="Run a schema-only dry run or invoke an external backend command.",
    )
    parser.add_argument(
        "--ares-harness",
        default=str(DEFAULT_ARES_HARNESS),
        help="Path to the local native ares audio harness executable.",
    )
    parser.add_argument(
        "--external",
        nargs=argparse.REMAINDER,
        help="External command vector. Use placeholders like {job} and {result}.",
    )
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def find_job(index: dict[str, Any], job_id: str) -> dict[str, Any]:
    for job in index.get("jobs", []):
        if job.get("job_id") == job_id:
            return job
    raise ValueError(f"job id not found: {job_id}")


def ensure_job_manifest(job: dict[str, Any]) -> Path:
    job_path = Path(job["job_path"])
    if not job_path.exists():
        job_path.parent.mkdir(parents=True, exist_ok=True)
        job_path.write_text(json.dumps(job, indent=2) + "\n", encoding="utf-8")
    return job_path


def write_dry_run_result(job: dict[str, Any]) -> Path:
    output_dir = Path(job["output_dir"])
    output_dir.mkdir(parents=True, exist_ok=True)
    result = build_audio_backend_result_stub.build_result(job, "unsupported")
    result_path = Path(job["result_path"])
    result_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return result_path


def expand_external_command(command: list[str], job: dict[str, Any], job_path: Path) -> list[str]:
    replacements = {
        "{job}": str(job_path),
        "{result}": str(Path(job["result_path"])),
        "{fixture}": str(Path(job["fixture_path"])),
        "{output_dir}": str(Path(job["output_dir"])),
    }
    expanded: list[str] = []
    for token in command:
        for key, value in replacements.items():
            token = token.replace(key, value)
        expanded.append(token)
    return expanded


def run_external_backend(job: dict[str, Any], job_path: Path, command: list[str] | None) -> Path:
    if not command:
        raise ValueError("external mode requires --external command arguments")
    expanded = expand_external_command(command, job, job_path)
    result = subprocess.run(expanded, cwd=ROOT, text=True, capture_output=True, check=False)
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)
    if result.returncode:
        raise RuntimeError(f"external backend exited with status {result.returncode}: {expanded}")
    return Path(job["result_path"])


def run_native_ares_backend(job: dict[str, Any], job_path: Path, harness_path: Path) -> Path:
    if not harness_path.exists():
        raise FileNotFoundError(
            f"native ares harness not found: {harness_path}. "
            "Build it with CMake from tools/ares_audio_harness first."
        )
    return run_external_backend(
        job,
        job_path,
        [str(harness_path), "--job", "{job}", "--result", "{result}"],
    )


def validate_result(result_path: Path, jobs_path: Path) -> None:
    result = validate_audio_backend_result.load_json(result_path)
    job_data = validate_audio_backend_result.load_json(jobs_path)
    job = validate_audio_backend_result.find_job(job_data, str(result.get("job_id", "")))
    errors = validate_audio_backend_result.validate(result, result_path, job)
    if errors:
        formatted = "\n".join(f"- {error}" for error in errors)
        raise ValueError(f"backend result validation failed:\n{formatted}")


def main() -> int:
    args = parse_args()
    jobs_path = Path(args.jobs)
    index = load_json(jobs_path)
    job = find_job(index, args.job_id)
    job_path = ensure_job_manifest(job)

    if args.mode == "dry-run-stub":
        result_path = write_dry_run_result(job)
    elif args.mode == "native-ares":
        result_path = run_native_ares_backend(job, job_path, Path(args.ares_harness))
    else:
        result_path = run_external_backend(job, job_path, args.external)

    validate_result(result_path, jobs_path)
    print(f"Audio backend job {args.job_id} completed in {args.mode} mode")
    print(f"Result: {result_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
