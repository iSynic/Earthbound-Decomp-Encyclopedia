#!/usr/bin/env python3
"""Build a focused review of FF terminator candidates in music sequences."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_TRIAGE = ROOT / "manifests" / "audio-exact-duration-triage.json"
DEFAULT_WALK_FRONTIER = ROOT / "manifests" / "audio-sequence-walk-frontier.json"
DEFAULT_OUTPUT = ROOT / "manifests" / "audio-ff-terminator-review.json"
DEFAULT_NOTES = ROOT / "notes" / "audio-ff-terminator-review.md"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build FF terminator candidate review.")
    parser.add_argument("--triage", default=str(DEFAULT_TRIAGE), help="Exact-duration triage JSON.")
    parser.add_argument("--walk-frontier", default=str(DEFAULT_WALK_FRONTIER), help="Sequence walk frontier JSON.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Review manifest output JSON.")
    parser.add_argument("--notes", default=str(DEFAULT_NOTES), help="Review markdown output.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def walk_status_detail(pack_record: dict[str, Any]) -> dict[str, Any]:
    root_count = 0
    terminate_roots = 0
    fallthrough_roots = 0
    blocked_roots = 0
    terminators = []
    terminator_tail_counts: Counter[str] = Counter()

    for block in pack_record.get("blocks", []):
        for walk in block.get("root_walks_sample", []):
            root_count += 1
            status = str(walk.get("status"))
            if status == "terminates":
                terminate_roots += 1
            elif status == "falls_through_segment":
                fallthrough_roots += 1
            elif status == "blocked":
                blocked_roots += 1
            for terminator in walk.get("terminators", []):
                tail = int(terminator.get("bytes_before_segment_end", 0))
                terminator_tail_counts[str(tail)] += 1
                terminators.append(
                    {
                        "block_index": block.get("block_index"),
                        "destination": block.get("destination"),
                        "root_offset": walk.get("root_offset"),
                        "terminator_offset": terminator.get("offset"),
                        "segment_end": terminator.get("segment_end"),
                        "bytes_before_segment_end": tail,
                    }
                )

    return {
        "sampled_root_count": root_count,
        "sampled_terminating_roots": terminate_roots,
        "sampled_fallthrough_roots": fallthrough_roots,
        "sampled_blocked_roots": blocked_roots,
        "sampled_terminators": terminators,
        "terminator_tail_byte_counts": dict(sorted(terminator_tail_counts.items(), key=lambda item: int(item[0]))),
    }


def promotion_class(pack: dict[str, Any], detail: dict[str, Any]) -> str:
    export_classes = pack.get("export_class_counts", {})
    if pack.get("blocker_counts"):
        return "blocked"
    if int(pack.get("ff_terminator_candidates", 0)) <= 0:
        return "no_ff_candidate"
    if "loop_or_held_candidate" in export_classes:
        return "ff_present_but_loop_metadata_still_needed"
    if "finite_or_transition_review_candidate" in export_classes:
        return "ff_can_promote_after_dispatch_and_track_review"
    if "finite_trim_candidate" in export_classes:
        return "ff_can_confirm_existing_pcm_trim_candidate"
    if detail.get("sampled_fallthrough_roots", 0):
        return "ff_present_with_fallthrough_roots"
    return "ff_can_promote_after_dispatch"


def build_review(triage: dict[str, Any], walk_frontier: dict[str, Any]) -> dict[str, Any]:
    priority_pack_ids = {
        int(pack["pack_id"])
        for pack in triage.get("categories", {}).get("candidate_for_ff_terminator_review", [])
    }
    walk_by_pack = {int(pack["pack_id"]): pack for pack in walk_frontier.get("priority_packs", [])}
    summary_by_pack = {int(pack["pack_id"]): pack for pack in walk_frontier.get("pack_summaries", [])}
    candidate_records = []
    promotion_counts: Counter[str] = Counter()
    track_counts: Counter[str] = Counter()

    for triage_pack in triage.get("categories", {}).get("candidate_for_ff_terminator_review", []):
        pack_id = int(triage_pack["pack_id"])
        detail_source = walk_by_pack.get(pack_id, summary_by_pack.get(pack_id, {}))
        detail = walk_status_detail(detail_source)
        record = {
            "pack_id": pack_id,
            "range": triage_pack["range"],
            "track_count": int(triage_pack["track_count"]),
            "track_ids": triage_pack["track_ids"],
            "tracks": triage_pack.get("tracks", []),
            "export_class_counts": triage_pack["export_class_counts"],
            "walk_status_counts": triage_pack["walk_status_counts"],
            "ef_call_edges": int(triage_pack["ef_call_edges"]),
            "ff_terminator_candidates": int(triage_pack["terminators"]),
            "blocker_counts": triage_pack["blocker_counts"],
            "review_detail": detail,
        }
        record["promotion_class"] = promotion_class(record, detail)
        candidate_records.append(record)
        promotion_counts[record["promotion_class"]] += 1
        track_counts[record["promotion_class"]] += record["track_count"]

    candidate_records.sort(
        key=lambda item: (
            item["promotion_class"],
            item["track_count"],
            item["ff_terminator_candidates"],
            item["ef_call_edges"],
        ),
        reverse=True,
    )

    missing_detail = sorted(priority_pack_ids - set(summary_by_pack))
    return {
        "schema": "earthbound-decomp.audio-ff-terminator-review.v1",
        "status": "ff_terminator_candidates_grouped_dispatch_pending",
        "references": [
            "manifests/audio-exact-duration-triage.json",
            "manifests/audio-sequence-walk-frontier.json",
            "manifests/audio-sequence-control-flow-frontier.json",
        ],
        "summary": {
            "candidate_pack_count": len(candidate_records),
            "candidate_track_count": sum(record["track_count"] for record in candidate_records),
            "promotion_class_pack_counts": dict(sorted(promotion_counts.items())),
            "promotion_class_track_counts": dict(sorted(track_counts.items())),
            "missing_walk_detail_pack_ids": missing_detail,
            "semantic_status": "static_ff_candidates_ready_for_spc700_dispatch_corroboration",
        },
        "promotion_rules": [
            "No record in this review has FD/FE blockers; those stay in the separate blocked lane.",
            "FF can only be promoted to a true end/return command after SPC700 dispatch confirms its effect.",
            "Finite/transition review tracks still need track-context review even when FF is confirmed.",
            "Loop/held candidates with FF still require loop-point or hold/fade interpretation before release exactness.",
        ],
        "candidates": candidate_records,
        "findings": [
            "The no-FD/FE FF lane covers packs that are structurally ready for dispatch corroboration.",
            "Candidate packs mix finite trims, finite/transition reviews, unknown active previews, and loop/held tracks, so FF confirmation alone is necessary but not sufficient for public exact exports.",
            "Tracks whose export class is finite_trim_candidate can use FF as sequence corroboration for existing PCM silence evidence once the driver dispatch is named.",
            "Loop/held packs with FF likely need intro/body loop modeling rather than simple finite-end promotion.",
        ],
        "next_work": [
            "inspect the SPC700 high-command dispatch path for FF and record whether it stops a channel, returns from EF, or ends a sequence",
            "after FF dispatch is confirmed, promote finite_trim_candidate records to sequence-corroborated finite metadata",
            "keep loop_or_held_candidate records in the loop-point lane even if FF is confirmed as a local terminator",
        ],
    }


def render_markdown(data: dict[str, Any]) -> str:
    summary = data["summary"]
    rows = [
        "| `{pack_id}` | `{range}` | `{track_ids}` | `{export_class_counts}` | `{ff}` | `{ef}` | `{promotion}` |".format(
            pack_id=record["pack_id"],
            range=record["range"],
            track_ids=record["track_ids"],
            export_class_counts=record["export_class_counts"],
            ff=record["ff_terminator_candidates"],
            ef=record["ef_call_edges"],
            promotion=record["promotion_class"],
        )
        for record in data["candidates"]
    ]
    return "\n".join(
        [
            "# Audio FF Terminator Review",
            "",
            "Status: FF terminator candidates grouped; SPC700 dispatch corroboration still pending.",
            "",
            "## Summary",
            "",
            f"- candidate packs: `{summary['candidate_pack_count']}`",
            f"- candidate tracks: `{summary['candidate_track_count']}`",
            f"- promotion classes: `{summary['promotion_class_pack_counts']}`",
            f"- promotion-class tracks: `{summary['promotion_class_track_counts']}`",
            f"- semantic status: `{summary['semantic_status']}`",
            "",
            "## Promotion Rules",
            "",
            *[f"- {rule}" for rule in data["promotion_rules"]],
            "",
            "## Candidates",
            "",
            "| Pack | ROM range | Tracks | Export classes | FF candidates | EF edges | Promotion class |",
            "| ---: | --- | --- | --- | ---: | ---: | --- |",
            *rows,
            "",
            "## Findings",
            "",
            *[f"- {finding}" for finding in data["findings"]],
            "",
            "## Next Work",
            "",
            *[f"- {item}" for item in data["next_work"]],
            "",
        ]
    )


def main() -> int:
    args = parse_args()
    data = build_review(load_json(Path(args.triage)), load_json(Path(args.walk_frontier)))
    output = Path(args.output)
    notes = Path(args.notes)
    output.parent.mkdir(parents=True, exist_ok=True)
    notes.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    notes.write_text(render_markdown(data), encoding="utf-8")
    print(
        "Built audio FF terminator review: "
        f"{data['summary']['candidate_pack_count']} packs, "
        f"{data['summary']['candidate_track_count']} tracks"
    )
    print(f"Wrote {output}")
    print(f"Wrote {notes}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
