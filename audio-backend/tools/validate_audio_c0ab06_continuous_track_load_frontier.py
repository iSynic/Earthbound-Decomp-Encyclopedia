#!/usr/bin/env python3
"""Validate continuous C0:AB06 boot-plus-track-pack-sequence frontier evidence."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_FRONTIER = ROOT / "build" / "audio" / "c0ab06-continuous-track-load-frontier" / "c0ab06-continuous-track-load-frontier.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate continuous C0:AB06 track load frontier evidence.")
    parser.add_argument("frontier", nargs="?", default=str(DEFAULT_FRONTIER))
    return parser.parse_args()


def validate(frontier: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if frontier.get("schema") != "earthbound-decomp.c0ab06-continuous-track-load-frontier.v1":
        errors.append(f"unexpected schema: {frontier.get('schema')}")
    if frontier.get("status") != "real_ares_smp_driver_loads_full_representative_track_pack_sequences":
        errors.append(f"unexpected status: {frontier.get('status')}")
    job_count = int(frontier.get("job_count", 0))
    match_count = int(frontier.get("payload_region_match_count", 0))
    if job_count <= 0:
        errors.append("job_count must be positive")
    if match_count != job_count:
        errors.append("payload_region_match_count does not match job_count")
    if int(frontier.get("mismatch_count", -1)) != 0:
        errors.append(f"mismatch_count is {frontier.get('mismatch_count')}")
    records = frontier.get("records", [])
    if len(records) != job_count:
        errors.append("record count does not match job_count")
    for record in records:
        job_id = record.get("job_id")
        if int(record.get("returncode", -1)) != 0:
            errors.append(f"{job_id}: returncode {record.get('returncode')}")
        if not record.get("sequence_pack_ids"):
            errors.append(f"{job_id}: empty pack sequence")
        handshake = record.get("handshake") or {}
        if handshake.get("receiver") != "ares_smp_ipl":
            errors.append(f"{job_id}: receiver is {handshake.get('receiver')}")
        if not handshake.get("sequence_after_bootstrap"):
            errors.append(f"{job_id}: did not run as sequence_after_bootstrap")
        if not (handshake.get("bootstrap") or {}).get("ok"):
            errors.append(f"{job_id}: bootstrap failed")
        if len(handshake.get("sequence", [])) != len(record.get("sequence_pack_ids", [])):
            errors.append(f"{job_id}: sequence length mismatch")
        for step in handshake.get("sequence", []):
            if not step.get("ok"):
                errors.append(f"{job_id}: sequence step {step.get('index')} failed")
            if step.get("final_pc") != "0x008004":
                errors.append(f"{job_id}: sequence step {step.get('index')} final PC is {step.get('final_pc')}")
            if int(step.get("terminal_tokens", 0)) != 1:
                errors.append(f"{job_id}: sequence step {step.get('index')} terminal tokens is {step.get('terminal_tokens')}")
        payload_regions = record.get("payload_regions") or {}
        if not payload_regions.get("payload_regions_match"):
            errors.append(f"{job_id}: payload regions do not match")
        if int(payload_regions.get("payload_region_mismatch_count", -1)) != 0:
            errors.append(f"{job_id}: payload region mismatch count is {payload_regions.get('payload_region_mismatch_count')}")
        if int(payload_regions.get("skipped_mutable_region_count", -1)) < 0:
            errors.append(f"{job_id}: skipped mutable region count is missing")
        if int(payload_regions.get("bytes", 0)) != 0x10000:
            errors.append(f"{job_id}: APU RAM dump size is {payload_regions.get('bytes')}")
        for block in payload_regions.get("blocks", []):
            if not block.get("matches") and not block.get("mutable_runtime_region"):
                errors.append(f"{job_id}: stable block {block.get('pack_id')}:{block.get('block_index')} mismatch")
    return errors


def main() -> int:
    args = parse_args()
    frontier = json.loads(Path(args.frontier).read_text(encoding="utf-8"))
    errors = validate(frontier)
    if errors:
        print("C0:AB06 continuous track load frontier validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "C0:AB06 continuous track load frontier validation OK: "
        f"{frontier['payload_region_match_count']} / {frontier['job_count']} tracks"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
