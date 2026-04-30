#!/usr/bin/env python3
"""Validate the provisional EarthBound music sequence-walk frontier."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MANIFEST = ROOT / "manifests" / "audio-sequence-walk-frontier.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate the audio sequence-walk frontier.")
    parser.add_argument("manifest", nargs="?", default=str(DEFAULT_MANIFEST))
    return parser.parse_args()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def validate(data: dict[str, Any]) -> None:
    require(data.get("schema") == "earthbound-decomp.audio-sequence-walk-frontier.v1", "unexpected schema")
    summary = data.get("summary", {})
    pack_summaries = data.get("pack_summaries", [])
    priority_packs = data.get("priority_packs", [])
    require(summary.get("sequence_packs_walked", 0) > 0, "expected walked sequence packs")
    ef_edges = summary.get("ef_call_edges", -1)
    bad_ef_edges = summary.get("ef_edges_not_inside_block", -1)
    require(ef_edges >= 0, "invalid EF edge count")
    require(0 <= bad_ef_edges <= ef_edges, "invalid out-of-block EF edge count")
    require(
        ef_edges == 0 or bad_ef_edges / ef_edges <= 0.01,
        "out-of-block EF edge count exceeds provisional-walk tolerance",
    )
    require(summary.get("walk_status_counts"), "missing walk status counts")
    require(summary.get("command_counts"), "missing command counts")
    require("0xEF" in summary["command_counts"], "expected EF command evidence")
    require(len(pack_summaries) == summary.get("sequence_packs_walked"), "pack summary count mismatch")
    require(priority_packs, "missing priority packs")
    require(data.get("provisional_operand_widths"), "missing provisional operand widths")
    for pack in priority_packs:
        require("pack_id" in pack, "priority pack missing id")
        require(pack.get("blocks"), f"pack {pack.get('pack_id')} missing blocks")
        require(pack.get("walk_status_counts"), f"pack {pack.get('pack_id')} missing walk status counts")
        for block in pack["blocks"]:
            require(block.get("payload_sha1"), f"pack {pack['pack_id']} block missing hash")
            require("root_walks_sample" in block, f"pack {pack['pack_id']} block missing walk sample")
    for pack in pack_summaries:
        require("pack_id" in pack, "pack summary missing id")
        require("track_ids" in pack, f"pack summary {pack.get('pack_id')} missing track ids")
        require("walk_status_counts" in pack, f"pack summary {pack.get('pack_id')} missing status counts")


def main() -> int:
    args = parse_args()
    data = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    validate(data)
    print(
        "Audio sequence walk frontier validation OK: "
        f"{data['summary']['sequence_packs_walked']} packs, "
        f"{data['summary']['ef_call_edges']} EF edges"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
