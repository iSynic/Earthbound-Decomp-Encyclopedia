#!/usr/bin/env python3
"""Validate collected ares diagnostic capture metrics."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_METRICS = ROOT / "build" / "audio" / "backend-jobs" / "ares-capture-metrics.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate ares diagnostic capture metrics.")
    parser.add_argument("metrics", nargs="?", default=str(DEFAULT_METRICS), help="Metrics JSON path.")
    parser.add_argument(
        "--allow-missing-host-command",
        action="store_true",
        help="Allow captures from experiments that intentionally disable diagnostic APUIO0 preseed.",
    )
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(metrics: dict[str, Any], *, allow_missing_host_command: bool = False) -> list[str]:
    errors: list[str] = []
    if metrics.get("schema") != "earthbound-decomp.audio-capture-metrics.v1":
        errors.append(f"unexpected schema: {metrics.get('schema')}")
    records = metrics.get("records", [])
    if int(metrics.get("job_count", -1)) != len(records):
        errors.append(f"job_count {metrics.get('job_count')} does not match {len(records)} records")
    if int(metrics.get("capture_count", -1)) + int(metrics.get("missing_capture_count", -1)) != len(records):
        errors.append("capture_count + missing_capture_count does not match records")
    if int(metrics.get("tracks_with_key_on_events", -1)) > int(metrics.get("capture_count", 0)):
        errors.append("tracks_with_key_on_events exceeds capture_count")
    seen: set[str] = set()
    for record in records:
        job_id = str(record.get("job_id", ""))
        if not job_id:
            errors.append("record without job_id")
        elif job_id in seen:
            errors.append(f"duplicate job_id {job_id}")
        seen.add(job_id)
        if record.get("capture_exists"):
            if int(record.get("executed_instructions", 0)) <= 0:
                errors.append(f"{job_id}: executed_instructions must be positive")
            if int(record.get("dsp_register_write_count", 0)) <= 0:
                errors.append(f"{job_id}: dsp_register_write_count must be positive")
            if not allow_missing_host_command and not record.get("host_command_injected"):
                errors.append(f"{job_id}: diagnostic host command was not injected")
    return errors


def main() -> int:
    args = parse_args()
    metrics_path = Path(args.metrics)
    metrics = load_json(metrics_path)
    errors = validate(metrics, allow_missing_host_command=args.allow_missing_host_command)
    if errors:
        print("Audio capture metrics validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "Audio capture metrics validation OK: "
        f"{metrics['capture_count']} captures, "
        f"{metrics['tracks_with_key_on_events']} with key-on events"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
