#!/usr/bin/env python3
"""Validate the audio sequence semantics frontier manifest."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MANIFEST = ROOT / "manifests" / "audio-sequence-semantics-frontier.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate the audio sequence semantics frontier.")
    parser.add_argument("manifest", nargs="?", default=str(DEFAULT_MANIFEST))
    return parser.parse_args()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def load_json(path: Path) -> dict[str, Any]:
    require(path.exists(), f"missing manifest: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def validate(data: dict[str, Any]) -> None:
    require(data.get("schema") == "earthbound-decomp.audio-sequence-semantics-frontier.v1", "unexpected schema")
    summary = data.get("summary", {})
    require(summary.get("music_tracks") == 192, "expected 192 music tracks")
    require(int(summary.get("sequence_pack_count", 0)) > 0, "expected sequence packs")
    require(int(summary.get("sequence_payload_block_count", 0)) > 0, "expected sequence payload blocks")
    require(summary.get("observed_high_command_candidates"), "expected observed high-command candidates")
    require(data.get("command_contexts"), "expected command contexts")
    require(data.get("priority_sequence_packs"), "expected priority sequence pack queue")
    require(data.get("focused_reports") is not None, "expected focused reports list")

    sequence_packs = data.get("sequence_packs", [])
    sequence_blocks = data.get("sequence_blocks", [])
    require(len(sequence_packs) == summary["sequence_pack_count"], "sequence pack count mismatch")
    require(len(sequence_blocks) == summary["sequence_payload_block_count"], "sequence block count mismatch")

    pack_ids = {int(pack["pack_id"]) for pack in sequence_packs}
    for pack in sequence_packs:
        require(pack.get("tracks"), f"sequence pack {pack.get('pack_id')} has no tracks")
        require(int(pack["track_count"]) == len(pack["tracks"]), f"track count mismatch for pack {pack.get('pack_id')}")

    for block in sequence_blocks:
        pack_id = int(block["pack_id"])
        require(pack_id in pack_ids, f"block references unknown pack {pack_id}")
        require(int(block["bytes"]) > 0, f"block in pack {pack_id} has no bytes")
        require(block.get("payload_sha1"), f"block in pack {pack_id} missing payload sha1")
        prefix = block.get("pointer_prefix", {})
        scan = block.get("scan", {})
        require("word_count" in prefix, f"block in pack {pack_id} missing pointer prefix")
        require(int(scan.get("scan_bytes", -1)) >= 0, f"block in pack {pack_id} missing scan byte count")
        require(scan.get("command_candidate_histogram") is not None, f"block in pack {pack_id} missing command histogram")

    hypotheses = data.get("known_command_hypotheses", {})
    for byte in summary["observed_high_command_candidates"]:
        require(byte in hypotheses, f"observed command {byte} lacks a hypothesis entry")
        require(byte in data["command_contexts"], f"observed command {byte} lacks context")

    for pack in data["priority_sequence_packs"]:
        require("needs_sequence_semantics_count" in pack, f"priority pack {pack.get('pack_id')} missing needs count")
        require(pack.get("block_shapes") is not None, f"priority pack {pack.get('pack_id')} missing block shapes")

    for report in data["focused_reports"]:
        require(report.get("json"), f"focused report {report.get('pack_id')} missing json path")
        require(report.get("notes"), f"focused report {report.get('pack_id')} missing notes path")
        require(report.get("exists"), f"focused report {report.get('pack_id')} outputs are missing")


def main() -> int:
    args = parse_args()
    path = Path(args.manifest)
    data = load_json(path)
    validate(data)
    summary = data["summary"]
    print(
        "Audio sequence semantics frontier validation OK: "
        f"{summary['sequence_pack_count']} sequence packs, "
        f"{summary['sequence_payload_block_count']} blocks, "
        f"{len(summary['observed_high_command_candidates'])} high-command candidates"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
