#!/usr/bin/env python3
"""Validate the key-on-primed diagnostic SPC experiment index."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INDEX = ROOT / "build" / "audio" / "keyon-primed-spc" / "keyon-primed-spc-snapshots.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate key-on-primed SPC experiment metadata.")
    parser.add_argument("index", nargs="?", default=str(DEFAULT_INDEX), help="Experiment index JSON path.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(index: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if index.get("schema") != "earthbound-decomp.audio-keyon-primed-spc-experiment.v1":
        errors.append(f"unexpected schema: {index.get('schema')}")
    records = index.get("records", [])
    if int(index.get("snapshot_count", -1)) != len(records):
        errors.append(f"snapshot_count {index.get('snapshot_count')} does not match {len(records)} records")
    for record in records:
        job_id = record.get("job_id", "<unknown>")
        snapshot = record.get("snapshot", {})
        path = Path(snapshot.get("path", ""))
        if not path.exists():
            errors.append(f"{job_id}: missing snapshot {path}")
            continue
        if snapshot.get("bytes") != 0x10200:
            errors.append(f"{job_id}: unexpected SPC size {snapshot.get('bytes')}")
        if not snapshot.get("signature_ok"):
            errors.append(f"{job_id}: bad SPC signature")
        patch = record.get("patch", {})
        if patch.get("primed_kon") in (None, "0x00"):
            errors.append(f"{job_id}: primed KON is zero")
        if patch.get("primed_kof") != "0x00":
            errors.append(f"{job_id}: primed KOF is not clear")
    return errors


def main() -> int:
    args = parse_args()
    index_path = Path(args.index)
    index = load_json(index_path)
    errors = validate(index)
    if errors:
        print("Key-on-primed SPC experiment validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Key-on-primed SPC experiment validation OK: {index['snapshot_count']} snapshots")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
