#!/usr/bin/env python3
"""Validate the no-command ares probe frontier."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_FRONTIER = ROOT / "build" / "audio" / "no-command-jobs" / "no-command-frontier.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate no-command audio frontier.")
    parser.add_argument("frontier", nargs="?", default=str(DEFAULT_FRONTIER), help="No-command frontier JSON.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(frontier: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if frontier.get("schema") != "earthbound-decomp.audio-no-command-frontier.v1":
        errors.append(f"unexpected schema: {frontier.get('schema')}")
    records = frontier.get("records", [])
    if int(frontier.get("job_count", -1)) != len(records):
        errors.append(f"job_count {frontier.get('job_count')} does not match {len(records)} records")
    summary = frontier.get("summary", {})
    if int(summary.get("preseed_enabled_count", -1)) != 0:
        errors.append(f"preseed_enabled_count is {summary.get('preseed_enabled_count')}, expected 0")
    if int(summary.get("host_command_injected_count", -1)) != 0:
        errors.append(f"host_command_injected_count is {summary.get('host_command_injected_count')}, expected 0")
    seen: set[str] = set()
    for record in records:
        job_id = str(record.get("job_id", ""))
        if not job_id:
            errors.append("record without job_id")
        elif job_id in seen:
            errors.append(f"duplicate job_id {job_id}")
        seen.add(job_id)
        if record.get("host_command_preseed_enabled"):
            errors.append(f"{job_id}: preseed unexpectedly enabled")
        if record.get("host_command_injected"):
            errors.append(f"{job_id}: command unexpectedly injected")
        if str(record.get("host_command_preseed_value")) != "0x00":
            errors.append(f"{job_id}: preseed value is {record.get('host_command_preseed_value')}, expected 0x00")
        if int(record.get("executed_instructions", 0)) <= 0:
            errors.append(f"{job_id}: executed_instructions must be positive")
    return errors


def main() -> int:
    args = parse_args()
    frontier = load_json(Path(args.frontier))
    errors = validate(frontier)
    if errors:
        print("No-command audio frontier validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    summary = frontier["summary"]
    print(
        "No-command audio frontier validation OK: "
        f"{frontier['capture_count']} captures, "
        f"{summary['tracks_with_key_on_events']} with key-on events"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
