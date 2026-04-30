#!/usr/bin/env python3
"""External-harness-shaped audio backend stub.

This consumes one per-job `job.json` and writes one `result.json`, matching the
interface expected from a future ares wrapper. It does not render audio.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a schema-only audio backend harness stub.")
    parser.add_argument("--job", required=True, help="Per-job job.json path.")
    parser.add_argument("--result", help="Result JSON path. Defaults to the job result_path.")
    parser.add_argument("--backend-version", default="external-stub-harness")
    parser.add_argument(
        "--status",
        default="unsupported",
        choices=["failed", "unsupported"],
        help="Dry-run status to write. Successful outputs require a real backend.",
    )
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_result(job: dict[str, Any], *, backend_version: str, status: str) -> dict[str, Any]:
    return {
        "schema": "earthbound-decomp.audio-backend-result.v1",
        "job_id": job["job_id"],
        "backend_id": job["backend_id"],
        "backend_version": backend_version,
        "status": status,
        "input_fixture_path": job["fixture_path"],
        "input_apu_ram_sha1": job["input_apu_ram_sha1"],
        "outputs": [],
        "diagnostics": {
            "execution_mode": "external_stub_no_emulator",
            "handshake_policy": "not_executed",
            "timing_basis": "not_applicable",
            "message": "External harness shape check. No SPC, PCM, or WAV output was produced.",
        },
    }


def main() -> int:
    args = parse_args()
    job_path = Path(args.job)
    job = load_json(job_path)
    result_path = Path(args.result) if args.result else Path(job["result_path"])
    result_path.parent.mkdir(parents=True, exist_ok=True)
    result = build_result(job, backend_version=args.backend_version, status=args.status)
    result_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote external stub backend result -> {result_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
