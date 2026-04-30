#!/usr/bin/env python3
"""Validate a diagnostic command-timing frontier."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_FRONTIER = ROOT / "build" / "audio" / "command-on-first-read-jobs" / "command-timing-frontier.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate command-timing audio frontier.")
    parser.add_argument("frontier", nargs="?", default=str(DEFAULT_FRONTIER), help="Command timing frontier JSON.")
    parser.add_argument("--expect-mode", help="Require every record to use this mode.")
    parser.add_argument("--require-key-on", action="store_true", help="Require every record to reach key-on.")
    return parser.parse_args()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(frontier: dict, *, expect_mode: str | None, require_key_on: bool) -> list[str]:
    errors: list[str] = []
    if frontier.get("schema") != "earthbound-decomp.audio-command-timing-frontier.v1":
        errors.append(f"unexpected schema: {frontier.get('schema')}")
    records = frontier.get("records", [])
    if int(frontier.get("job_count", -1)) != len(records):
        errors.append(f"job_count {frontier.get('job_count')} does not match {len(records)} records")
    summary = frontier.get("summary", {})
    if require_key_on and int(summary.get("tracks_with_key_on_events", 0)) != len(records):
        errors.append("not every track reached key-on")
    if require_key_on and int(summary.get("keyon_after_command_read_count", 0)) != len(records):
        errors.append("not every track reached key-on after command read")
    seen: set[str] = set()
    for record in records:
        job_id = str(record.get("job_id", ""))
        if not job_id:
            errors.append("record without job_id")
        elif job_id in seen:
            errors.append(f"duplicate job_id {job_id}")
        seen.add(job_id)
        if expect_mode and record.get("mode") != expect_mode:
            errors.append(f"{job_id}: mode {record.get('mode')} != {expect_mode}")
        if require_key_on and int(record.get("dsp_key_on_event_count", 0)) <= 0:
            errors.append(f"{job_id}: missing key-on event")
        if not record.get("host_command_injection"):
            errors.append(f"{job_id}: missing host command injection")
        if not record.get("host_command_first_read"):
            errors.append(f"{job_id}: missing host command first read")
    return errors


def main() -> int:
    args = parse_args()
    frontier = load_json(Path(args.frontier))
    errors = validate(frontier, expect_mode=args.expect_mode, require_key_on=args.require_key_on)
    if errors:
        print("Command timing audio frontier validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    summary = frontier["summary"]
    print(
        "Command timing audio frontier validation OK: "
        f"{frontier['capture_count']} captures, "
        f"{summary['tracks_with_key_on_events']} with key-on events"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
