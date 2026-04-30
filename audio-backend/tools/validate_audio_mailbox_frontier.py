#!/usr/bin/env python3
"""Validate the diagnostic audio mailbox frontier."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_FRONTIER = ROOT / "build" / "audio" / "command-on-first-read-jobs" / "mailbox-frontier.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate audio mailbox frontier.")
    parser.add_argument("frontier", nargs="?", default=str(DEFAULT_FRONTIER), help="Mailbox frontier JSON.")
    parser.add_argument("--expect-mode", help="Require every record to use this mode.")
    parser.add_argument("--require-key-on", action="store_true", help="Require every record to key-on after command read.")
    return parser.parse_args()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(frontier: dict, *, expect_mode: str | None, require_key_on: bool) -> list[str]:
    errors: list[str] = []
    if frontier.get("schema") != "earthbound-decomp.audio-mailbox-frontier.v1":
        errors.append(f"unexpected schema: {frontier.get('schema')}")
    records = frontier.get("records", [])
    if int(frontier.get("job_count", -1)) != len(records):
        errors.append(f"job_count {frontier.get('job_count')} does not match {len(records)} records")
    summary = frontier.get("summary", {})
    if int(summary.get("capture_count", 0)) != len(records):
        errors.append("not every record has a capture")
    if int(summary.get("io_window_count", 0)) != len(records):
        errors.append("not every record has an IO window")
    if int(summary.get("command_read_count", 0)) != len(records):
        errors.append("not every record has a command read")
    if int(summary.get("command_match_count", 0)) != len(records):
        errors.append("not every host command matches the track id")
    if int(summary.get("zero_ack_write_count", 0)) != len(records):
        errors.append("not every record has a zero APUIO0 write after command read")
    if require_key_on and int(summary.get("keyon_after_command_read_count", 0)) != len(records):
        errors.append("not every record reaches key-on after command read")

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
        if not record.get("command_matches_track_id"):
            errors.append(f"{job_id}: command does not match track id")
        first_read = record.get("first_command_read") or {}
        if first_read.get("address") != "0x00F4":
            errors.append(f"{job_id}: first command read is not APUIO0")
        if first_read.get("data") != record.get("expected_track_command"):
            errors.append(f"{job_id}: first command read data does not match expected track command")
        ack = record.get("first_port0_write_after_read") or {}
        if ack.get("address") != "0x00F4" or ack.get("data") != "0x00":
            errors.append(f"{job_id}: missing zero APUIO0 ack write after command read")
        if int(record.get("io_window_event_count", 0)) <= 0:
            errors.append(f"{job_id}: empty IO window")
        if int(record.get("port0_reads_after_read_count", 0)) <= 0:
            errors.append(f"{job_id}: no APUIO0 reads in command window")
        if require_key_on and not record.get("keyon_after_command_read"):
            errors.append(f"{job_id}: missing key-on after command read")
    return errors


def main() -> int:
    args = parse_args()
    frontier = load_json(Path(args.frontier))
    errors = validate(frontier, expect_mode=args.expect_mode, require_key_on=args.require_key_on)
    if errors:
        print("Audio mailbox frontier validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    summary = frontier["summary"]
    print(
        "Audio mailbox frontier validation OK: "
        f"{summary['capture_count']} captures, "
        f"{summary['command_read_count']} command reads, "
        f"{summary['zero_ack_write_count']} zero ack writes"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
