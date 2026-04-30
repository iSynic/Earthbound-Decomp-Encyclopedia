#!/usr/bin/env python3
"""Validate a focused EarthBound audio sequence-pack report."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_REPORT = ROOT / "manifests" / "audio-sequence-pack-025-semantics.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate an audio sequence-pack report.")
    parser.add_argument("report", nargs="?", default=str(DEFAULT_REPORT))
    return parser.parse_args()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def validate(data: dict[str, Any]) -> None:
    require(data.get("schema") == "earthbound-decomp.audio-sequence-pack-report.v1", "unexpected schema")
    summary = data.get("summary", {})
    tracks = data.get("tracks", [])
    blocks = data.get("blocks", [])
    require(summary.get("track_count") == len(tracks), "track count mismatch")
    require(summary.get("sequence_payload_blocks") == len(blocks), "block count mismatch")
    require(blocks, "expected sequence blocks")
    require(summary.get("command_candidate_counts"), "expected command candidate counts")
    require(summary.get("block_prefix_shapes"), "expected block prefix shapes")
    reference_matches = summary.get("reference_song_matches")
    require(isinstance(reference_matches, int), "expected reference song match count")
    require(0 <= reference_matches <= len(blocks), "invalid reference song match count")

    for track in tracks:
        require(track.get("export_class"), f"track {track.get('track_id')} missing export class")
        require("sequence_block_index_guess" in track, f"track {track.get('track_id')} missing block guess")

    for block in blocks:
        require(block.get("payload_sha1"), f"block {block.get('destination')} missing payload hash")
        top = block.get("top_level_table", {})
        require(top.get("word_count", 0) > 0, f"block {block.get('destination')} missing top-level table")
        groups = block.get("pointer_groups", [])
        require(groups, f"block {block.get('destination')} missing pointer groups")
        require(block.get("segments"), f"block {block.get('destination')} missing segments")
        reference_song_match = block.get("reference_song_match", {})
        if reference_song_match.get("available"):
            require(reference_song_match.get("count_matches"), f"block {block.get('destination')} ref count mismatch")
            require(reference_song_match.get("destination_matches"), f"block {block.get('destination')} ref destination mismatch")
            require(reference_song_match.get("payload_matches"), f"block {block.get('destination')} ref payload mismatch")
        for group in groups:
            require(group.get("word_count", 0) > 0, f"block {block.get('destination')} has empty group")
            require("active_pointer_count" in group, f"block {block.get('destination')} group missing active count")


def main() -> int:
    args = parse_args()
    path = Path(args.report)
    data = json.loads(path.read_text(encoding="utf-8"))
    validate(data)
    print(
        "Audio sequence pack report validation OK: "
        f"pack {data['pack_id']}, "
        f"{data['summary']['track_count']} tracks, "
        f"{data['summary']['sequence_payload_blocks']} blocks"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
