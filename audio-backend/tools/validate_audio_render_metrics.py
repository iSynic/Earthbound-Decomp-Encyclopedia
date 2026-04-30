#!/usr/bin/env python3
"""Validate collected libgme diagnostic render metrics."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_METRICS = ROOT / "build" / "audio" / "backend-jobs" / "libgme-render-metrics.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate diagnostic libgme render metrics.")
    parser.add_argument("metrics", nargs="?", default=str(DEFAULT_METRICS), help="Metrics JSON path.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expected_rendered_samples(job: dict[str, Any]) -> int | None:
    options = job.get("render_options", {})
    try:
        sample_rate = int(options["sample_rate"])
        channels = int(options["channels"])
        seconds = float(options["seconds"])
    except (KeyError, TypeError, ValueError):
        return None
    return round(sample_rate * channels * seconds)


def validate(metrics: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if metrics.get("schema") != "earthbound-decomp.audio-render-metrics.v1":
        errors.append(f"unexpected schema: {metrics.get('schema')}")
    job_index_path = Path(str(metrics.get("job_index", "")))
    jobs_by_id: dict[str, dict[str, Any]] = {}
    if job_index_path.exists():
        job_index = load_json(job_index_path)
        jobs_by_id = {str(job.get("job_id", "")): job for job in job_index.get("jobs", [])}
    records = metrics.get("records", [])
    if int(metrics.get("job_count", -1)) != len(records):
        errors.append(f"job_count {metrics.get('job_count')} does not match {len(records)} records")
    if int(metrics.get("metrics_count", -1)) + int(metrics.get("missing_metrics_count", -1)) != len(records):
        errors.append("metrics_count + missing_metrics_count does not match records")
    class_total = sum(int(count) for count in metrics.get("classification_counts", {}).values())
    if class_total != len(records):
        errors.append(f"classification_counts total {class_total} does not match {len(records)} records")
    seen: set[str] = set()
    for record in records:
      job_id = str(record.get("job_id", ""))
      if not job_id:
          errors.append("record without job_id")
      elif job_id in seen:
          errors.append(f"duplicate job_id {job_id}")
      seen.add(job_id)
      classification = record.get("classification")
      if classification not in ("missing", "silent", "click_or_trace", "very_quiet", "audible"):
          errors.append(f"{job_id}: unexpected classification {classification}")
      if classification != "missing":
          if int(record.get("rendered_samples", 0)) <= 0:
              errors.append(f"{job_id}: rendered_samples must be positive")
          if int(record.get("voice_count", 0)) <= 0:
              errors.append(f"{job_id}: voice_count must be positive")
          if int(record.get("peak_abs_sample", -1)) < 0:
              errors.append(f"{job_id}: peak_abs_sample must be non-negative")
          job = jobs_by_id.get(job_id)
          if job:
              expected_samples = expected_rendered_samples(job)
              if expected_samples is not None and int(record.get("rendered_samples", -1)) != expected_samples:
                  errors.append(
                      f"{job_id}: rendered_samples {record.get('rendered_samples')} "
                      f"does not match job render_options ({expected_samples})"
                  )
    return errors


def main() -> int:
    args = parse_args()
    metrics_path = Path(args.metrics)
    metrics = load_json(metrics_path)
    errors = validate(metrics)
    if errors:
        print("Audio render metrics validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "Audio render metrics validation OK: "
        f"{metrics['metrics_count']} metrics, classifications {metrics['classification_counts']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
