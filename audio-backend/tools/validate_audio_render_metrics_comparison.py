#!/usr/bin/env python3
"""Validate a diagnostic audio render metrics comparison."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_COMPARISON = ROOT / "build" / "audio" / "keyon-primed-jobs" / "render-metrics-comparison.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate diagnostic render metrics comparison.")
    parser.add_argument("comparison", nargs="?", default=str(DEFAULT_COMPARISON), help="Comparison JSON path.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(comparison: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if comparison.get("schema") != "earthbound-decomp.audio-render-metrics-comparison.v1":
        errors.append(f"unexpected schema: {comparison.get('schema')}")
    records = comparison.get("records", [])
    if int(comparison.get("track_count", -1)) != len(records):
        errors.append(f"track_count {comparison.get('track_count')} does not match {len(records)} records")
    total = (
        int(comparison.get("improved_count", -1))
        + int(comparison.get("unchanged_count", -1))
        + int(comparison.get("worsened_count", -1))
    )
    if total != len(records):
        errors.append(f"improved+unchanged+worsened total {total} does not match {len(records)} records")
    seen: set[int] = set()
    for record in records:
        track_id = int(record.get("track_id", -1))
        if track_id in seen:
            errors.append(f"duplicate track {track_id}")
        seen.add(track_id)
        if record.get("experiment_peak_abs_sample") is None:
            errors.append(f"track {track_id}: missing experiment peak")
        if record.get("baseline_peak_abs_sample") is None:
            errors.append(f"track {track_id}: missing baseline peak")
    return errors


def main() -> int:
    args = parse_args()
    comparison = load_json(Path(args.comparison))
    errors = validate(comparison)
    if errors:
        print("Audio render metrics comparison validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "Audio render metrics comparison validation OK: "
        f"{comparison['improved_count']} improved, "
        f"{comparison['unchanged_count']} unchanged, "
        f"{comparison['worsened_count']} worsened"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
