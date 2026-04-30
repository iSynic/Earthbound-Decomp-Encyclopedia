#!/usr/bin/env python3
"""Validate one result emitted by an audio backend harness."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate an audio backend result.json file.")
    parser.add_argument("result", help="Backend result JSON path.")
    parser.add_argument("--job", help="Optional backend job JSON path or job-index path for cross-checking.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def find_job(job_data: dict[str, Any], job_id: str) -> dict[str, Any] | None:
    if job_data.get("schema") == "earthbound-decomp.audio-backend-job-index.v1":
        for job in job_data.get("jobs", []):
            if job.get("job_id") == job_id:
                return job
        return None
    if job_data.get("job_id") == job_id:
        return job_data
    return None


def validate_output_record(record: dict[str, Any], result_path: Path) -> list[str]:
    errors: list[str] = []
    kind = record.get("kind")
    if not kind:
        errors.append("output record missing kind")
    path_text = record.get("path")
    if not path_text:
        errors.append(f"{kind}: output record missing path")
        return errors
    output_path = Path(path_text)
    if not output_path.is_absolute():
        output_path = result_path.parent / output_path
    if not output_path.exists():
        errors.append(f"{kind}: output path missing: {output_path}")
        return errors
    data = output_path.read_bytes()
    if int(record.get("bytes", -1)) != len(data):
        errors.append(f"{kind}: byte count mismatch {record.get('bytes')} != {len(data)}")
    sha1 = hashlib.sha1(data).hexdigest()
    if record.get("sha1") != sha1:
        errors.append(f"{kind}: SHA-1 mismatch {record.get('sha1')} != {sha1}")
    errors.extend(validate_output_kind(str(kind), data))
    return errors


def validate_output_kind(kind: str, data: bytes) -> list[str]:
    errors: list[str] = []
    if kind == "rendered_wav":
        if len(data) < 44:
            errors.append("rendered_wav: file is too small for a WAV header")
        elif data[0:4] != b"RIFF" or data[8:12] != b"WAVE":
            errors.append("rendered_wav: missing RIFF/WAVE header")
    elif kind == "complete_spc_snapshot":
        if len(data) < 0x10100:
            errors.append(f"complete_spc_snapshot: file is too small ({len(data)} bytes)")
        if not data.startswith(b"SNES-SPC700 Sound File Data"):
            errors.append("complete_spc_snapshot: missing SNES-SPC700 signature")
    elif kind in ("rendered_pcm", "state_capture_json", "render_hash_json", "reference_capture_json"):
        if not data:
            errors.append(f"{kind}: output is empty")
    return errors


def validate(result: dict[str, Any], result_path: Path, job: dict[str, Any] | None) -> list[str]:
    errors: list[str] = []
    if result.get("schema") != "earthbound-decomp.audio-backend-result.v1":
        errors.append(f"unexpected schema: {result.get('schema')}")

    for field in (
        "job_id",
        "backend_id",
        "backend_version",
        "status",
        "input_fixture_path",
        "input_apu_ram_sha1",
        "outputs",
        "diagnostics",
    ):
        if field not in result:
            errors.append(f"missing required result field {field}")

    status = result.get("status")
    if status not in ("ok", "failed", "unsupported", "mismatch"):
        errors.append(f"unexpected status: {status}")

    if job is not None:
        if result.get("backend_id") != job.get("backend_id"):
            errors.append(f"backend mismatch {result.get('backend_id')} != {job.get('backend_id')}")
        if result.get("input_fixture_path") != job.get("fixture_path"):
            errors.append("input_fixture_path does not match job fixture_path")
        if result.get("input_apu_ram_sha1") != job.get("input_apu_ram_sha1"):
            errors.append("input_apu_ram_sha1 does not match job")

    outputs = result.get("outputs", [])
    if status == "ok" and not outputs:
        errors.append("ok result has no outputs")
    for output in outputs:
        errors.extend(validate_output_record(output, result_path))

    diagnostics = result.get("diagnostics", {})
    if status == "ok":
        for field in ("execution_mode", "handshake_policy", "timing_basis"):
            if field not in diagnostics:
                errors.append(f"ok result diagnostics missing {field}")

    return errors


def main() -> int:
    args = parse_args()
    result_path = Path(args.result)
    result = load_json(result_path)
    job = None
    if args.job:
        job_data = load_json(Path(args.job))
        job = find_job(job_data, str(result.get("job_id", "")))
        if job is None:
            print(f"Audio backend result validation failed:")
            print(f"- job {result.get('job_id')} was not found in {args.job}")
            return 1
    errors = validate(result, result_path, job)
    if errors:
        print("Audio backend result validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Audio backend result validation OK: {result['job_id']} {result['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
