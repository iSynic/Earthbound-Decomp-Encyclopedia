#!/usr/bin/env python3
"""Validate semantic LOAD_SPC700_DATA transfer metrics."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_METRICS = ROOT / "build" / "audio" / "load-stream-transfer" / "load-stream-transfer-metrics.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate semantic LOAD_SPC700_DATA transfer metrics.")
    parser.add_argument("metrics", nargs="?", default=str(DEFAULT_METRICS))
    return parser.parse_args()


def validate(metrics: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if metrics.get("schema") != "earthbound-decomp.audio-load-stream-transfer-metrics.v1":
        errors.append(f"unexpected schema: {metrics.get('schema')}")
    records = metrics.get("records", [])
    track_count = int(metrics.get("track_count", -1))
    if track_count != len(records):
        errors.append(f"track_count {track_count} does not match {len(records)} records")
    for field in ("mismatch_count", "ram_mismatch_count", "load_call_mismatch_count"):
        if int(metrics.get(field, -1)) != 0:
            errors.append(f"{field} is {metrics.get(field)}")
    for field in ("mismatch_tracks", "ram_mismatch_tracks", "load_call_mismatch_tracks"):
        if metrics.get(field):
            errors.append(f"{field} is non-empty: {metrics.get(field)}")
    if not records:
        errors.append("no records")

    for record in records:
        track_id = int(record.get("track_id", -1))
        if not record.get("ram_matches_corpus"):
            errors.append(f"track {track_id}: replayed RAM does not match corpus RAM")
        if not record.get("change_music_load_args_match"):
            errors.append(f"track {track_id}: CHANGE_MUSIC load args do not match track load order")
        if not record.get("cold_start_pack_ids"):
            errors.append(f"track {track_id}: empty cold-start pack list")
        if record.get("corpus_ram_sha1") != record.get("replayed_ram_sha1"):
            errors.append(f"track {track_id}: corpus/replayed SHA-1 mismatch")
        for load in record.get("load_transcript", []):
            if int(load.get("payload_block_count", 0)) <= 0:
                errors.append(f"track {track_id}: pack {load.get('pack_id')} has no payload blocks")
            if int(load.get("payload_bytes", 0)) <= 0:
                errors.append(f"track {track_id}: pack {load.get('pack_id')} has no payload bytes")
            if not load.get("blocks"):
                errors.append(f"track {track_id}: pack {load.get('pack_id')} has no transfer blocks")
    return errors


def main() -> int:
    args = parse_args()
    metrics = json.loads(Path(args.metrics).read_text(encoding="utf-8"))
    errors = validate(metrics)
    if errors:
        print("Audio load-stream transfer metrics validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "Audio load-stream transfer metrics validation OK: "
        f"{metrics['track_count']} tracks, "
        f"{metrics['destination_role_counts']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
