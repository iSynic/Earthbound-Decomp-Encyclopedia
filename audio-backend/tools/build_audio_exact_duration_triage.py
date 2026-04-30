#!/usr/bin/env python3
"""Build an exact-duration triage report from export policy and sequence walking."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_EXPORT_PLAN = ROOT / "manifests" / "audio-export-plan.json"
DEFAULT_WALK_FRONTIER = ROOT / "manifests" / "audio-sequence-walk-frontier.json"
DEFAULT_MANIFEST = ROOT / "manifests" / "audio-exact-duration-triage.json"
DEFAULT_NOTES = ROOT / "notes" / "audio-exact-duration-triage.md"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build audio exact-duration triage.")
    parser.add_argument("--export-plan", default=str(DEFAULT_EXPORT_PLAN), help="Audio export plan JSON.")
    parser.add_argument("--walk-frontier", default=str(DEFAULT_WALK_FRONTIER), help="Sequence walk frontier JSON.")
    parser.add_argument("--output", default=str(DEFAULT_MANIFEST), help="Manifest output JSON.")
    parser.add_argument("--notes", default=str(DEFAULT_NOTES), help="Markdown note output.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def classify_pack(pack: dict[str, Any]) -> str:
    blockers = pack.get("blocker_counts", {})
    needs = int(pack.get("needs_sequence_semantics_count", 0))
    terminators = int(pack.get("terminators", 0))
    if needs == 0:
        return "no_sequence_semantics_needed"
    if blockers:
        return "blocked_by_unpromoted_fd_fe_control"
    if terminators > 0:
        return "candidate_for_ff_terminator_review"
    return "needs_loop_or_fallthrough_semantics"


def build_triage(export_plan: dict[str, Any], walk_frontier: dict[str, Any]) -> dict[str, Any]:
    tracks_by_id = {int(track["track_id"]): track for track in export_plan["tracks"]}
    categories: dict[str, list[dict[str, Any]]] = {}
    status_counts: Counter[str] = Counter()
    track_counts: Counter[str] = Counter()

    for pack in walk_frontier.get("pack_summaries", []):
        category = classify_pack(pack)
        status_counts[category] += 1
        track_counts[category] += len(pack.get("track_ids", []))
        track_records = []
        for track_id in pack.get("track_ids", []):
            track = tracks_by_id.get(int(track_id), {})
            track_records.append(
                {
                    "track_id": int(track_id),
                    "track_name": track.get("track_name"),
                    "export_class": track.get("export_class"),
                    "recommended_mode": track.get("recommended_mode"),
                    "duration_seconds": track.get("duration_seconds"),
                    "needs_sequence_semantics": track.get("needs_sequence_semantics"),
                }
            )
        categories.setdefault(category, []).append(
            {
                "pack_id": pack["pack_id"],
                "range": pack["range"],
                "track_count": pack["track_count"],
                "track_ids": pack["track_ids"],
                "tracks": track_records,
                "export_class_counts": pack["export_class_counts"],
                "walk_status_counts": pack["walk_status_counts"],
                "ef_call_edges": pack["ef_call_edges"],
                "terminators": pack["terminators"],
                "blocker_counts": pack["blocker_counts"],
                "recommended_next_step": recommended_next_step(category),
            }
        )

    for records in categories.values():
        records.sort(
            key=lambda item: (
                item["track_count"],
                item["terminators"],
                item["ef_call_edges"],
            ),
            reverse=True,
        )

    return {
        "schema": "earthbound-decomp.audio-exact-duration-triage.v1",
        "source_policy": export_plan["source_policy"] if "source_policy" in export_plan else {
            "requires_user_supplied_rom": True,
            "do_not_commit_generated_outputs": True,
            "generated_audio_output_root": "build/audio",
        },
        "references": [
            "manifests/audio-export-plan.json",
            "manifests/audio-sequence-walk-frontier.json",
            "manifests/audio-sequence-control-flow-frontier.json",
        ],
        "summary": {
            "sequence_packs_triaged": sum(status_counts.values()),
            "category_pack_counts": dict(sorted(status_counts.items())),
            "category_track_counts": dict(sorted(track_counts.items())),
            "release_status": "exact_duration_not_promoted_sequence_triage_ready",
        },
        "categories": categories,
        "findings": [
            "Exact-duration work now splits into packs with FF terminator candidates, packs blocked by FD/FE, and packs needing loop/fallthrough semantics.",
            "Pack 25 remains blocked by FE behavior despite clean eb-decompile payload corroboration and strong EF call-edge evidence.",
            "Packs without FD/FE blockers and with FF terminator candidates are the fastest next candidates for exact finite review.",
            "Loop/held preview tracks still need explicit loop-point or fade policy even when playback/export is already near-oracle accurate.",
        ],
        "next_work": [
            "promote candidate_for_ff_terminator_review packs into focused reports before tackling FD/FE dispatch",
            "decode FE behavior because it blocks pack 25 and several finite/review families",
            "feed resolved exact finite or loop outcomes back into audio-export-plan",
        ],
    }


def recommended_next_step(category: str) -> str:
    if category == "candidate_for_ff_terminator_review":
        return "build focused pack report and confirm whether FF marks sequence end or subroutine return"
    if category == "blocked_by_unpromoted_fd_fe_control":
        return "decode FD/FE command behavior through SPC700 driver dispatch before exact duration promotion"
    if category == "needs_loop_or_fallthrough_semantics":
        return "inspect loop/fallthrough behavior and runtime timing before choosing public export mode"
    return "no sequence-duration action required"


def render_markdown(data: dict[str, Any]) -> str:
    summary = data["summary"]
    sections = [
        "# Audio Exact-Duration Triage",
        "",
        "Status: exact-duration release promotion is still pending, but sequence work is now sorted into actionable lanes.",
        "",
        "## Summary",
        "",
        f"- sequence packs triaged: `{summary['sequence_packs_triaged']}`",
        f"- category pack counts: `{summary['category_pack_counts']}`",
        f"- category track counts: `{summary['category_track_counts']}`",
        f"- release status: `{summary['release_status']}`",
        "",
    ]
    for category in [
        "candidate_for_ff_terminator_review",
        "blocked_by_unpromoted_fd_fe_control",
        "needs_loop_or_fallthrough_semantics",
        "no_sequence_semantics_needed",
    ]:
        rows = []
        for pack in data["categories"].get(category, [])[:20]:
            rows.append(
                f"| `{pack['pack_id']}` | `{pack['range']}` | `{pack['track_ids']}` | "
                f"`{pack['export_class_counts']}` | {pack['ef_call_edges']} | {pack['terminators']} | "
                f"`{pack['blocker_counts']}` |"
            )
        sections.extend(
            [
                f"## {category}",
                "",
                "| Pack | ROM range | Tracks | Export classes | EF edges | Terminators | Blockers |",
                "| ---: | --- | --- | --- | ---: | ---: | --- |",
                *rows,
                "",
            ]
        )
    sections.extend(
        [
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
    return "\n".join(sections)


def main() -> int:
    args = parse_args()
    export_plan = load_json(Path(args.export_plan))
    walk_frontier = load_json(Path(args.walk_frontier))
    data = build_triage(export_plan, walk_frontier)
    output = Path(args.output)
    notes = Path(args.notes)
    output.parent.mkdir(parents=True, exist_ok=True)
    notes.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    notes.write_text(render_markdown(data), encoding="utf-8")
    print(
        "Built audio exact-duration triage: "
        f"{data['summary']['sequence_packs_triaged']} packs"
    )
    print(f"Wrote {output}")
    print(f"Wrote {notes}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
