#!/usr/bin/env python3
"""Validate collected audio oracle comparison summary output."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SUMMARY = ROOT / "build" / "audio" / "oracle-comparison" / "oracle-comparison-summary.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate audio oracle comparison summary output.")
    parser.add_argument("summary", nargs="?", default=str(DEFAULT_SUMMARY))
    parser.add_argument("--require-compared", action="store_true", help="Fail unless every oracle job is compared.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def resolve_repo_path(path_text: str) -> Path:
    path = Path(path_text)
    return path if path.is_absolute() else ROOT / path


def validate_result(path: Path) -> list[str]:
    errors: list[str] = []
    result = load_json(path)
    if result.get("schema") != "earthbound-decomp.audio-oracle-comparison-result.v1":
        errors.append(f"{path}: unexpected result schema {result.get('schema')}")
    status = result.get("status")
    if status not in (
        "pending_reference_capture",
        "pass",
        "audio_equivalent_state_delta",
        "explained_timing_offset",
        "state_mismatch",
        "investigated_mismatch",
        "invalid_reference_output",
    ):
        errors.append(f"{path}: unexpected status {status}")
    if status == "pending_reference_capture" and not result.get("missing_reference_outputs"):
        errors.append(f"{path}: pending result must list missing reference outputs")
    if not result.get("source_spc", {}).get("exists"):
        errors.append(f"{path}: source SPC evidence missing")
    if not result.get("source_wav", {}).get("exists"):
        errors.append(f"{path}: source WAV evidence missing")
    if status in ("pass", "audio_equivalent_state_delta", "explained_timing_offset", "state_mismatch", "investigated_mismatch"):
        comparison = result.get("comparison", {})
        wav = comparison.get("wav", {})
        spc = comparison.get("spc", {})
        if not wav.get("sample_rate_match"):
            errors.append(f"{path}: compared WAV sample rate mismatch")
        if not wav.get("channels_match"):
            errors.append(f"{path}: compared WAV channel mismatch")
        if not wav.get("bits_per_sample_match"):
            errors.append(f"{path}: compared WAV bit-depth mismatch")
        if not spc.get("reference_signature_ok"):
            errors.append(f"{path}: compared reference SPC signature invalid")
        if "alignment" not in wav:
            errors.append(f"{path}: compared WAV missing alignment metrics")
        if "apu_region_matches" not in spc:
            errors.append(f"{path}: compared SPC missing APU region match metrics")
    return errors


def validate(summary: dict[str, Any], *, require_compared: bool) -> list[str]:
    errors: list[str] = []
    if summary.get("schema") != "earthbound-decomp.audio-oracle-comparison-summary.v1":
        errors.append(f"unexpected schema: {summary.get('schema')}")
    results = summary.get("results", [])
    if int(summary.get("job_count", -1)) != len(results):
        errors.append(f"job_count {summary.get('job_count')} does not match {len(results)} results")
    status_total = sum(int(count) for count in summary.get("status_counts", {}).values())
    if status_total != len(results):
        errors.append(f"status_counts total {status_total} does not match {len(results)} results")
    compared_statuses = {"pass", "audio_equivalent_state_delta", "explained_timing_offset", "state_mismatch", "investigated_mismatch"}
    compared_count = sum(int(summary.get("status_counts", {}).get(status, 0)) for status in compared_statuses)
    if require_compared and compared_count != len(results):
        errors.append("not all oracle jobs have completed comparison statuses")

    seen: set[str] = set()
    for record in results:
        job_id = str(record.get("job_id", ""))
        if not job_id:
            errors.append("summary result without job_id")
        if job_id in seen:
            errors.append(f"duplicate job_id {job_id}")
        seen.add(job_id)
        result_path = resolve_repo_path(str(record.get("result_path", "")))
        if not result_path.exists():
            errors.append(f"{job_id}: comparison result missing: {result_path}")
        else:
            errors.extend(validate_result(result_path))
    return errors


def main() -> int:
    args = parse_args()
    summary = load_json(Path(args.summary))
    errors = validate(summary, require_compared=args.require_compared)
    if errors:
        print("Audio oracle comparison summary validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Audio oracle comparison summary validation OK: {summary['job_count']} jobs, statuses {summary['status_counts']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
