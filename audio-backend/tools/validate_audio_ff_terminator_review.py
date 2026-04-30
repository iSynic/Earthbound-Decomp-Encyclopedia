#!/usr/bin/env python3
"""Validate the FF terminator candidate review."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_REVIEW = ROOT / "manifests" / "audio-ff-terminator-review.json"

ALLOWED_PROMOTION_CLASSES = {
    "ff_can_confirm_existing_pcm_trim_candidate",
    "ff_can_promote_after_dispatch",
    "ff_can_promote_after_dispatch_and_track_review",
    "ff_present_but_loop_metadata_still_needed",
    "ff_present_with_fallthrough_roots",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate FF terminator candidate review.")
    parser.add_argument("review", nargs="?", default=str(DEFAULT_REVIEW))
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if data.get("schema") != "earthbound-decomp.audio-ff-terminator-review.v1":
        errors.append(f"unexpected schema: {data.get('schema')}")
    candidates = data.get("candidates", [])
    summary = data.get("summary", {})
    if int(summary.get("candidate_pack_count", -1)) != len(candidates):
        errors.append("candidate_pack_count does not match candidates")

    seen: set[int] = set()
    pack_counts: Counter[str] = Counter()
    track_counts: Counter[str] = Counter()
    total_tracks = 0
    for record in candidates:
        pack_id = int(record.get("pack_id", -1))
        if pack_id in seen:
            errors.append(f"duplicate pack id {pack_id}")
        seen.add(pack_id)
        if record.get("blocker_counts"):
            errors.append(f"pack {pack_id}: FF review candidates must not have FD/FE blockers")
        if int(record.get("ff_terminator_candidates", 0)) <= 0:
            errors.append(f"pack {pack_id}: expected at least one FF terminator candidate")
        if int(record.get("track_count", -1)) != len(record.get("track_ids", [])):
            errors.append(f"pack {pack_id}: track_count does not match track_ids")
        promotion_class = str(record.get("promotion_class", ""))
        if promotion_class not in ALLOWED_PROMOTION_CLASSES:
            errors.append(f"pack {pack_id}: unexpected promotion class {promotion_class}")
        detail = record.get("review_detail", {})
        if int(detail.get("sampled_terminating_roots", 0)) < 0:
            errors.append(f"pack {pack_id}: invalid sampled terminating roots")
        if "terminator_tail_byte_counts" not in detail:
            errors.append(f"pack {pack_id}: missing terminator tail-byte counts")
        pack_counts[promotion_class] += 1
        track_count = int(record.get("track_count", 0))
        track_counts[promotion_class] += track_count
        total_tracks += track_count

    if int(summary.get("candidate_track_count", -1)) != total_tracks:
        errors.append("candidate_track_count does not match candidates")
    if dict(sorted(pack_counts.items())) != summary.get("promotion_class_pack_counts"):
        errors.append("promotion_class_pack_counts does not match candidates")
    if dict(sorted(track_counts.items())) != summary.get("promotion_class_track_counts"):
        errors.append("promotion_class_track_counts does not match candidates")
    if len(data.get("promotion_rules", [])) < 3:
        errors.append("promotion_rules should describe review limits")
    return errors


def main() -> int:
    args = parse_args()
    data = load_json(Path(args.review))
    errors = validate(data)
    if errors:
        print("Audio FF terminator review validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "Audio FF terminator review validation OK: "
        f"{data['summary']['candidate_pack_count']} packs, "
        f"{data['summary']['candidate_track_count']} tracks"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
