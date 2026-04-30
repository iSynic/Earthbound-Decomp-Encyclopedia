#!/usr/bin/env python3
"""Validate the ares SMP mailbox SPC snapshot index."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INDEX = ROOT / "build" / "audio" / "ares-smp-mailbox-spc" / "ares-smp-mailbox-spc-snapshots.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate ares SMP mailbox SPC snapshot index.")
    parser.add_argument("index", nargs="?", default=str(DEFAULT_INDEX))
    parser.add_argument(
        "--allow-missing-snapshots",
        action="store_true",
        help="Allow load-ok/no-key-on records without a snapshot in broad all-track corpora.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    index = json.loads(Path(args.index).read_text(encoding="utf-8"))
    errors: list[str] = []
    if index.get("schema") != "earthbound-decomp.audio-ares-smp-mailbox-spc-index.v1":
        errors.append(f"unexpected schema: {index.get('schema')}")
    records = index.get("records", [])
    if int(index.get("job_count", -1)) != len(records):
        errors.append("job_count does not match records")
    missing_snapshot_count = int(index.get("missing_snapshot_count", -1))
    snapshot_count = int(index.get("snapshot_count", 0))
    if snapshot_count + max(missing_snapshot_count, 0) != len(records):
        errors.append("snapshot_count plus missing_snapshot_count does not match records")
    if not args.allow_missing_snapshots and snapshot_count != len(records):
        errors.append("snapshot_count does not match records")
    if not args.allow_missing_snapshots and missing_snapshot_count != 0:
        errors.append("missing_snapshot_count must be 0")
    if int(index.get("invalid_signature_count", -1)) != 0:
        errors.append("invalid_signature_count must be 0")
    seen: set[int] = set()
    for record in records:
        track_id = int(record.get("track_id", 0))
        if track_id in seen:
            errors.append(f"duplicate track id {track_id}")
        seen.add(track_id)
        snapshot = record.get("snapshot") or {}
        if not snapshot:
            if not args.allow_missing_snapshots:
                errors.append(f"{record.get('job_id')}: snapshot path missing")
            if record.get("smoke", {}).get("reached_key_on_after_ack"):
                errors.append(f"{record.get('job_id')}: missing snapshot despite key-on evidence")
            continue
        if not snapshot.get("path") or not Path(snapshot["path"]).exists():
            errors.append(f"{record.get('job_id')}: snapshot path missing")
        if not snapshot.get("signature_ok"):
            errors.append(f"{record.get('job_id')}: snapshot signature invalid")
        if snapshot.get("kon") in (None, "0x00"):
            errors.append(f"{record.get('job_id')}: snapshot KON is not set")
        smoke = record.get("smoke", {})
        if not smoke.get("reached_key_on_after_ack"):
            errors.append(f"{record.get('job_id')}: smoke did not reach key-on")
    if errors:
        print("ares SMP mailbox SPC index validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "ares SMP mailbox SPC index validation OK: "
        f"{index['snapshot_count']} / {index['job_count']} snapshots"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
