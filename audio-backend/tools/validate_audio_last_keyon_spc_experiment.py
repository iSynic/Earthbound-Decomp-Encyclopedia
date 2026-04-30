#!/usr/bin/env python3
"""Validate the real last-key-on diagnostic SPC experiment index."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INDEX = ROOT / "build" / "audio" / "last-keyon-spc" / "last-keyon-spc-snapshots.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate last-key-on SPC experiment metadata.")
    parser.add_argument("index", nargs="?", default=str(DEFAULT_INDEX), help="Experiment index JSON path.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(index: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if index.get("schema") != "earthbound-decomp.audio-last-keyon-spc-experiment.v1":
        errors.append(f"unexpected schema: {index.get('schema')}")
    records = index.get("records", [])
    if int(index.get("snapshot_count", -1)) != len([record for record in records if record.get("snapshot")]):
        errors.append("snapshot_count does not match records with snapshots")
    if index.get("missing_capture_count") != 0:
        errors.append(f"missing_capture_count is {index.get('missing_capture_count')}")
    if index.get("missing_last_keyon_count") != 0:
        errors.append(f"missing_last_keyon_count is {index.get('missing_last_keyon_count')}")
    if index.get("invalid_signature_count") != 0:
        errors.append(f"invalid_signature_count is {index.get('invalid_signature_count')}")
    for record in records:
        job_id = record.get("job_id", "<unknown>")
        snapshot = record.get("snapshot")
        if not snapshot:
            errors.append(f"{job_id}: missing snapshot")
            continue
        path = Path(snapshot.get("path", ""))
        if not path.exists():
            errors.append(f"{job_id}: missing snapshot file {path}")
            continue
        if snapshot.get("bytes") != 0x10200:
            errors.append(f"{job_id}: unexpected SPC size {snapshot.get('bytes')}")
        if not snapshot.get("signature_ok"):
            errors.append(f"{job_id}: bad SPC signature")
        if not record.get("source_declared_matches"):
            errors.append(f"{job_id}: copied snapshot does not match capture declaration")
        if snapshot.get("kon") in (None, "0x00"):
            errors.append(f"{job_id}: captured KON is zero")
        if record.get("key_on_data") != snapshot.get("kon"):
            errors.append(f"{job_id}: key_on_data {record.get('key_on_data')} != snapshot KON {snapshot.get('kon')}")
    return errors


def main() -> int:
    args = parse_args()
    index_path = Path(args.index)
    index = load_json(index_path)
    errors = validate(index)
    if errors:
        print("Last-key-on SPC experiment validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Last-key-on SPC experiment validation OK: {index['snapshot_count']} snapshots")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
