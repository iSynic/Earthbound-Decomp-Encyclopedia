#!/usr/bin/env python3
"""Validate diagnostic audio export duration measurements."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MEASUREMENTS = ROOT / "build" / "audio" / "export-duration-measurements" / "export-duration-measurements.json"

ALLOWED_STATUSES = {
    "finite_end_observed_in_preview",
    "finite_candidate_no_end_seen_in_preview",
    "looping_candidate_preview_still_active",
    "looping_candidate_silence_seen_review_needed",
    "unknown_preview_still_active",
    "unknown_silence_seen_needs_classification",
    "no_audio_no_key_on",
    "missing_preview",
    "invalid_preview_wav",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate audio export duration measurements.")
    parser.add_argument("measurements", nargs="?", default=str(DEFAULT_MEASUREMENTS))
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(summary: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if summary.get("schema") != "earthbound-decomp.audio-export-duration-measurements.v1":
        errors.append(f"unexpected schema: {summary.get('schema')}")
    records = summary.get("records", [])
    if int(summary.get("summary", {}).get("track_count", -1)) != len(records):
        errors.append("summary track_count does not match records")

    counts: Counter[str] = Counter()
    seen: set[int] = set()
    release_ready_count = 0
    rendered_count = 0
    finite_preview_end_count = 0
    policy = summary.get("measurement_policy", {})
    threshold = int(policy.get("silence_threshold_abs_sample", -1))
    sustained_seconds = float(policy.get("sustained_tail_silence_seconds", -1.0))
    if threshold < 0:
        errors.append("silence threshold must be non-negative")
    if sustained_seconds <= 0:
        errors.append("sustained tail silence seconds must be positive")

    for record in records:
        track_id = int(record.get("track_id", -1))
        if track_id in seen:
            errors.append(f"duplicate track id {track_id}")
        seen.add(track_id)
        status = str(record.get("measurement_status", ""))
        duration_class = str(record.get("duration_class", ""))
        if status not in ALLOWED_STATUSES:
            errors.append(f"track {track_id}: unexpected status {status}")
        counts[status] += 1

        measurement = record.get("measurement")
        if measurement is not None:
            rendered_count += 1
            if not measurement.get("wav_format_valid", False):
                if status != "invalid_preview_wav":
                    errors.append(f"track {track_id}: invalid WAV must use invalid_preview_wav")
            else:
                sample_rate = int(measurement.get("sample_rate", 0))
                channels = int(measurement.get("channels", 0))
                total_frames = int(measurement.get("total_frames", 0))
                if sample_rate <= 0 or channels <= 0 or total_frames <= 0:
                    errors.append(f"track {track_id}: invalid measured WAV dimensions")
                if bool(measurement.get("sustained_tail_silence_observed")) and "candidate_duration" not in record:
                    errors.append(f"track {track_id}: sustained tail silence must include candidate duration")

        if status == "finite_end_observed_in_preview":
            finite_preview_end_count += 1
            if duration_class != "finite_candidate":
                errors.append(f"track {track_id}: finite end status used for non-finite policy class")
            candidate = record.get("candidate_duration", {})
            if float(candidate.get("tail_silence_seconds", 0.0)) < sustained_seconds:
                errors.append(f"track {track_id}: finite end candidate tail silence below threshold")
        if status == "no_audio_no_key_on" and duration_class != "no_audio_no_key_on":
            errors.append(f"track {track_id}: no-audio status used for non-no-audio class")

        if bool(record.get("release_exact_length_ready", False)):
            release_ready_count += 1
            if status != "finite_end_observed_in_preview":
                errors.append(f"track {track_id}: release-ready exact length without observed finite end")
            if record.get("evidence_level") == "diagnostic_preview_pcm_only":
                errors.append(f"track {track_id}: diagnostic preview evidence cannot be release exact-length ready")

    expected_counts = summary.get("summary", {}).get("status_counts", {})
    if dict(counts) != expected_counts:
        errors.append("status_counts does not match records")
    if int(summary.get("summary", {}).get("rendered_preview_count", -1)) != rendered_count:
        errors.append("rendered_preview_count does not match records")
    if int(summary.get("summary", {}).get("finite_candidates_with_preview_end", -1)) != finite_preview_end_count:
        errors.append("finite candidate preview-end count does not match records")
    if int(summary.get("summary", {}).get("release_exact_length_ready_count", -1)) != release_ready_count:
        errors.append("release exact-length ready count does not match records")
    if "30-second diagnostic previews" not in str(policy.get("source_limit", "")):
        errors.append("measurement policy must keep the 30-second diagnostic-preview source limit explicit")
    return errors


def main() -> int:
    args = parse_args()
    summary = load_json(Path(args.measurements))
    errors = validate(summary)
    if errors:
        print("Audio export duration measurement validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "Audio export duration measurement validation OK: "
        f"{summary['summary']['rendered_preview_count']} previews, statuses {summary['summary']['status_counts']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
