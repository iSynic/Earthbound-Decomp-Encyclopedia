#!/usr/bin/env python3
"""Validate the EarthBound music sequence control-flow frontier."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MANIFEST = ROOT / "manifests" / "audio-sequence-control-flow-frontier.json"
EXPECTED_COMMANDS = ("0xEF", "0xFD", "0xFE", "0xFF")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate the audio sequence control-flow frontier.")
    parser.add_argument("manifest", nargs="?", default=str(DEFAULT_MANIFEST))
    return parser.parse_args()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def validate(data: dict[str, Any]) -> None:
    require(data.get("schema") == "earthbound-decomp.audio-sequence-control-flow-frontier.v1", "unexpected schema")
    summary = data.get("summary", {})
    command_summaries = data.get("command_summaries", {})
    priority_packs = data.get("priority_packs", [])
    require(summary.get("control_commands") == list(EXPECTED_COMMANDS), "unexpected control command set")
    require(command_summaries, "missing command summaries")
    require(priority_packs, "missing priority packs")
    total = 0
    for command in EXPECTED_COMMANDS:
        record = command_summaries.get(command)
        require(record is not None, f"missing summary for {command}")
        count = record.get("count")
        require(isinstance(count, int) and count >= 0, f"invalid count for {command}")
        require("hypothesis" in record, f"missing hypothesis for {command}")
        require(0 <= record.get("next_word_pointer_count", -1) <= count, f"invalid pointer count for {command}")
        require(0 <= record.get("tail_count", -1) <= count, f"invalid tail count for {command}")
        require(record.get("examples") is not None, f"missing examples for {command}")
        total += count
    require(summary.get("total_control_candidates") == total, "total control candidate mismatch")
    require(summary.get("sequence_packs_with_control_candidates") >= len(priority_packs), "priority pack count mismatch")
    for pack in priority_packs:
        require("pack_id" in pack, "priority pack missing id")
        require(pack.get("blocks"), f"priority pack {pack.get('pack_id')} missing blocks")
        require(pack.get("control_command_counts"), f"priority pack {pack.get('pack_id')} missing control counts")


def main() -> int:
    args = parse_args()
    path = Path(args.manifest)
    data = json.loads(path.read_text(encoding="utf-8"))
    validate(data)
    print(
        "Audio sequence control-flow frontier validation OK: "
        f"{data['summary']['sequence_packs_with_control_candidates']} packs, "
        f"{data['summary']['total_control_candidates']} candidates"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
