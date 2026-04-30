#!/usr/bin/env python3
"""Validate fused CHANGE_MUSIC/C0:AB06 post-command timing metrics."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_METRICS = (
    ROOT
    / "build"
    / "audio"
    / "c0ab06-change-music-fusion-frontier-all"
    / "c0ab06-change-music-fusion-timing-metrics.json"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate fused audio timing metrics.")
    parser.add_argument("metrics", nargs="?", default=str(DEFAULT_METRICS))
    return parser.parse_args()


def validate(metrics: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if metrics.get("schema") != "earthbound-decomp.audio-fusion-timing-metrics.v1":
        errors.append(f"unexpected schema: {metrics.get('schema')}")
    records = metrics.get("records", [])
    if int(metrics.get("job_count", -1)) != len(records):
        errors.append("job_count does not match records")
    if int(metrics.get("load_path_success_count", -1)) != len(records):
        errors.append("load_path_success_count does not match records")
    key_on_records = [record for record in records if record.get("reached_key_on_after_ack")]
    if int(metrics.get("key_on_count", -1)) != len(key_on_records):
        errors.append("key_on_count does not match records")
    if int(metrics.get("no_key_on_count", -1)) != len(metrics.get("no_key_on_records", [])):
        errors.append("no_key_on_count does not match no_key_on_records")
    if metrics.get("command_write_smp_burst_values") != [0]:
        errors.append(f"expected zero-burst command timing, saw {metrics.get('command_write_smp_burst_values')}")
    for record in records:
        job_id = record.get("job_id")
        if int(record.get("command_write_smp_burst", -1)) != 0:
            errors.append(f"{job_id}: command_write_smp_burst is not zero")
        if int(record.get("command_read_step", -1)) < 0:
            errors.append(f"{job_id}: missing command_read_step")
        if int(record.get("zero_ack_step", -1)) < int(record.get("command_read_step", -1)):
            errors.append(f"{job_id}: zero_ack_step precedes command_read_step")
        if record.get("reached_key_on_after_ack"):
            if int(record.get("key_on_step", -1)) < int(record.get("zero_ack_step", -1)):
                errors.append(f"{job_id}: key_on_step precedes zero_ack_step")
            if int(record.get("key_on_after_ack_delta", -1)) <= 0:
                errors.append(f"{job_id}: key_on_after_ack_delta must be positive")
    return errors


def main() -> int:
    args = parse_args()
    metrics = json.loads(Path(args.metrics).read_text(encoding="utf-8"))
    errors = validate(metrics)
    if errors:
        print("Audio fusion timing metrics validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "Audio fusion timing metrics validation OK: "
        f"{metrics['job_count']} jobs, {metrics['key_on_count']} key-on, "
        f"burst values {metrics['command_write_smp_burst_values']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
