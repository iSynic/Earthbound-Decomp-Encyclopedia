#!/usr/bin/env python3
"""Validate the audio exact-duration triage report."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MANIFEST = ROOT / "manifests" / "audio-exact-duration-triage.json"
EXPECTED_CATEGORIES = {
    "candidate_for_ff_terminator_review",
    "blocked_by_unpromoted_fd_fe_control",
    "needs_loop_or_fallthrough_semantics",
    "no_sequence_semantics_needed",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate audio exact-duration triage.")
    parser.add_argument("manifest", nargs="?", default=str(DEFAULT_MANIFEST))
    return parser.parse_args()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def validate(data: dict[str, Any]) -> None:
    require(data.get("schema") == "earthbound-decomp.audio-exact-duration-triage.v1", "unexpected schema")
    summary = data.get("summary", {})
    categories = data.get("categories", {})
    require(summary.get("sequence_packs_triaged", 0) > 0, "expected triaged sequence packs")
    require(set(categories).issubset(EXPECTED_CATEGORIES), "unexpected triage category")
    counted = sum(len(records) for records in categories.values())
    require(counted == summary.get("sequence_packs_triaged"), "triage category count mismatch")
    require("blocked_by_unpromoted_fd_fe_control" in categories, "expected FD/FE blocked lane")
    require("candidate_for_ff_terminator_review" in categories, "expected FF terminator review lane")
    for records in categories.values():
        for pack in records:
            require("pack_id" in pack, "pack missing id")
            require("tracks" in pack, f"pack {pack.get('pack_id')} missing tracks")
            require("recommended_next_step" in pack, f"pack {pack.get('pack_id')} missing next step")


def main() -> int:
    args = parse_args()
    data = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    validate(data)
    print(
        "Audio exact-duration triage validation OK: "
        f"{data['summary']['sequence_packs_triaged']} packs"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
