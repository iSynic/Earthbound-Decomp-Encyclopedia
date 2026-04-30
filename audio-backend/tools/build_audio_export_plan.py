#!/usr/bin/env python3
"""Build the public-facing audio export plan.

This combines the policy manifest, the 30-second diagnostic measurements, and
any longer targeted measurements into a practical per-track export contract.
It does not create WAV files; it describes how the app/CLI should export them.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_POLICY = ROOT / "manifests" / "audio-export-duration-policy.json"
DEFAULT_MEASUREMENTS = ROOT / "build" / "audio" / "export-duration-measurements" / "export-duration-measurements.json"
DEFAULT_EXTENDED_MEASUREMENTS = (
    ROOT / "build" / "audio" / "finite-candidate-extended-duration-measurements" / "export-duration-measurements.json"
)
DEFAULT_ORACLE_REPORT = ROOT / "manifests" / "audio-oracle-verification-report-all-tracks.json"
DEFAULT_JSON = ROOT / "manifests" / "audio-export-plan.json"
DEFAULT_MARKDOWN = ROOT / "notes" / "audio-export-plan.md"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the audio export plan.")
    parser.add_argument("--policy", default=str(DEFAULT_POLICY), help="Duration policy manifest.")
    parser.add_argument("--measurements", default=str(DEFAULT_MEASUREMENTS), help="30-second duration measurements.")
    parser.add_argument(
        "--extended-measurements",
        default=str(DEFAULT_EXTENDED_MEASUREMENTS),
        help="Optional longer targeted measurements.",
    )
    parser.add_argument("--oracle-report", default=str(DEFAULT_ORACLE_REPORT), help="All-track oracle report.")
    parser.add_argument("--json", default=str(DEFAULT_JSON), help="JSON output path.")
    parser.add_argument("--markdown", default=str(DEFAULT_MARKDOWN), help="Markdown output path.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def repo_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def records_by_track(measurements: dict[str, Any]) -> dict[int, dict[str, Any]]:
    return {int(record["track_id"]): record for record in measurements.get("records", [])}


def best_measurement(track_id: int, base: dict[int, dict[str, Any]], extended: dict[int, dict[str, Any]]) -> dict[str, Any] | None:
    extended_record = extended.get(track_id)
    if extended_record and extended_record.get("measurement") is not None:
        return extended_record
    base_record = base.get(track_id)
    if base_record and base_record.get("measurement") is not None:
        return base_record
    return base_record or extended_record


def export_decision(policy_track: dict[str, Any], measurement_record: dict[str, Any] | None) -> dict[str, Any]:
    track_id = int(policy_track["track_id"])
    duration_class = str(policy_track["duration_class"])
    status = str(measurement_record.get("measurement_status")) if measurement_record else "missing_preview"
    measurement = measurement_record.get("measurement") if measurement_record else None
    candidate = measurement_record.get("candidate_duration") if measurement_record else None
    target = policy_track.get("target_metadata", {})

    if duration_class == "no_audio_no_key_on":
        return {
            "export_class": "skip_no_audio",
            "export_status": "ready",
            "recommended_mode": "skip",
            "reason": "Load path is valid but no key-on render is expected.",
            "duration_seconds": 0.0,
            "fade_seconds": 0.0,
            "loop_count": 0,
            "loop_metadata": None,
            "finite_metadata": None,
            "needs_sequence_semantics": False,
        }

    if status == "finite_end_observed_in_preview" and candidate:
        return {
            "export_class": "finite_trim_candidate",
            "export_status": "usable_with_pcm_silence_evidence",
            "recommended_mode": "trim_to_observed_end",
            "reason": "Sustained trailing silence was observed in a rendered preview.",
            "duration_seconds": candidate["end_seconds"],
            "fade_seconds": 0.0,
            "loop_count": 0,
            "loop_metadata": None,
            "finite_metadata": {
                "finite_end_sample": candidate["end_frame"],
                "finite_end_seconds": candidate["end_seconds"],
                "evidence": "sustained_tail_pcm_silence",
                "measured_by": "audio_export_duration_measurement",
            },
            "needs_sequence_semantics": False,
            "evidence": {
                "end_frame": candidate["end_frame"],
                "tail_silence_seconds": candidate["tail_silence_seconds"],
                "silence_threshold_abs_sample": candidate["silence_threshold_abs_sample"],
            },
        }

    if status in ("looping_candidate_preview_still_active", "finite_candidate_no_end_seen_in_preview"):
        return {
            "export_class": "loop_or_held_candidate",
            "export_status": "preview_policy_ready_exact_loop_pending",
            "recommended_mode": "loop_count_plus_fade_preview",
            "reason": "The render stays active through the longest available measurement; exact loop/end semantics are not pinned.",
            "duration_seconds": 120.0 if measurement and float(measurement.get("total_seconds", 0.0)) >= 120 else 30.0,
            "fade_seconds": 5.0,
            "loop_count": 2,
            "loop_metadata": {
                "intro_samples": target.get("intro_samples"),
                "loop_start_sample": target.get("loop_start_sample"),
                "loop_end_sample": target.get("loop_end_sample"),
                "measured_by": target.get("measured_by"),
                "status": "loop_points_pending",
                "preview_policy": {
                    "mode": "loop_count_plus_fade_preview",
                    "loop_count": 2,
                    "fade_seconds": 5.0,
                },
            },
            "finite_metadata": None,
            "needs_sequence_semantics": True,
        }

    if status in ("looping_candidate_silence_seen_review_needed", "unknown_silence_seen_needs_classification"):
        end_seconds = candidate.get("end_seconds") if candidate else measurement.get("candidate_end_seconds") if measurement else None
        return {
            "export_class": "finite_or_transition_review_candidate",
            "export_status": "review_needed_before_public_exact_export",
            "recommended_mode": "trim_candidate_after_manual_or_sequence_review",
            "reason": "Trailing silence was observed, but the policy class is not confidently finite.",
            "duration_seconds": end_seconds,
            "fade_seconds": 0.0,
            "loop_count": 0,
            "loop_metadata": None,
            "finite_metadata": {
                "finite_end_sample": candidate.get("end_frame") if candidate else None,
                "finite_end_seconds": end_seconds,
                "evidence": "trailing_pcm_silence_review_needed",
                "measured_by": "audio_export_duration_measurement",
            },
            "needs_sequence_semantics": True,
        }

    if status == "unknown_preview_still_active":
        return {
            "export_class": "unknown_active_preview",
            "export_status": "preview_only",
            "recommended_mode": "diagnostic_preview",
            "reason": "Track remains active and has not been classified as finite or looping.",
            "duration_seconds": 30.0,
            "fade_seconds": 5.0,
            "loop_count": 0,
            "loop_metadata": None,
            "finite_metadata": None,
            "needs_sequence_semantics": True,
        }

    return {
        "export_class": "unmeasured_or_missing",
        "export_status": "blocked_or_skip_until_measured",
        "recommended_mode": "do_not_public_export",
        "reason": "No rendered measurement is available for this table entry.",
        "duration_seconds": None,
        "fade_seconds": None,
        "loop_count": None,
        "loop_metadata": None,
        "finite_metadata": None,
        "needs_sequence_semantics": track_id != 0,
    }


def build_plan(
    policy_path: Path,
    measurements_path: Path,
    extended_measurements_path: Path,
    oracle_report_path: Path,
) -> dict[str, Any]:
    policy = load_json(policy_path)
    measurements = load_json(measurements_path)
    extended_measurements = load_json(extended_measurements_path) if extended_measurements_path.exists() else {"records": []}
    oracle_report = load_json(oracle_report_path) if oracle_report_path.exists() else {}
    base_by_track = records_by_track(measurements)
    extended_by_track = records_by_track(extended_measurements)

    records: list[dict[str, Any]] = []
    class_counts: Counter[str] = Counter()
    status_counts: Counter[str] = Counter()
    mode_counts: Counter[str] = Counter()
    semantics_count = 0

    for track in policy.get("tracks", []):
        measurement_record = best_measurement(int(track["track_id"]), base_by_track, extended_by_track)
        decision = export_decision(track, measurement_record)
        record = {
            "track_id": int(track["track_id"]),
            "track_name": track["track_name"],
            "policy_duration_class": track["duration_class"],
            "measurement_status": measurement_record.get("measurement_status") if measurement_record else "missing_preview",
            **decision,
        }
        records.append(record)
        class_counts[record["export_class"]] += 1
        status_counts[record["export_status"]] += 1
        mode_counts[record["recommended_mode"]] += 1
        if record["needs_sequence_semantics"]:
            semantics_count += 1

    return {
        "schema": "earthbound-decomp.audio-export-plan.v1",
        "status": "export_policy_ready_exact_loop_points_pending",
        "inputs": {
            "duration_policy": repo_path(policy_path),
            "duration_measurements": repo_path(measurements_path),
            "extended_duration_measurements": repo_path(extended_measurements_path) if extended_measurements_path.exists() else None,
            "oracle_report": repo_path(oracle_report_path) if oracle_report_path.exists() else None,
        },
        "playback_confidence": {
            "all_track_near_oracle_passed": bool(
                oracle_report.get("gate_results", {}).get("all_track_oracle_gate_passed")
            ),
            "independent_emulator_gate_passed": bool(
                oracle_report.get("gate_results", {}).get("independent_emulator_gate_passed")
            ),
            "release_quality_playback_claim_ready": bool(
                oracle_report.get("gate_results", {}).get("release_quality_playback_claim_ready")
            ),
        },
        "defaults": {
            "sample_rate": 32000,
            "channels": 2,
            "bits_per_sample": 16,
            "loop_preview_count": 2,
            "loop_preview_fade_seconds": 5.0,
            "finite_trim_tail_policy": "trim after the last sample above the silence threshold; keep no extra generated silence",
        },
        "summary": {
            "track_count": len(records),
            "export_class_counts": dict(class_counts),
            "export_status_counts": dict(status_counts),
            "recommended_mode_counts": dict(mode_counts),
            "needs_sequence_semantics_count": semantics_count,
        },
        "release_gates": [
            "Finite trim candidates are usable where sustained trailing silence is observed, but sequence semantics can still refine exact musical intent.",
            "Loop or held candidates must use an explicit loop-count/fade preview until loop points are decoded.",
            "Unknown active previews are not exact exports.",
            "Independent external-emulator playback validation remains optional for development but open for public release confidence.",
            "Generated WAV/SPC/audio outputs remain local ignored artifacts derived from a user-provided ROM.",
        ],
        "tracks": records,
    }


def render_markdown(plan: dict[str, Any]) -> str:
    rows = [
        "| `{track_id:03d}` | `{track_name}` | `{policy}` | `{export_class}` | `{status}` | `{mode}` | {duration} | {semantics} |".format(
            track_id=record["track_id"],
            track_name=record["track_name"],
            policy=record["policy_duration_class"],
            export_class=record["export_class"],
            status=record["export_status"],
            mode=record["recommended_mode"],
            duration="" if record["duration_seconds"] is None else record["duration_seconds"],
            semantics="yes" if record["needs_sequence_semantics"] else "no",
        )
        for record in plan["tracks"]
    ]
    loop_metadata_count = sum(1 for record in plan["tracks"] if record.get("loop_metadata"))
    gates = [f"- {gate}" for gate in plan["release_gates"]]
    return "\n".join(
        [
            "# Audio Export Plan",
            "",
            "Status: export policy ready; exact loop points and some sequence-level duration semantics remain open.",
            "",
            f"- tracks: `{plan['summary']['track_count']}`",
            f"- export classes: `{plan['summary']['export_class_counts']}`",
            f"- export statuses: `{plan['summary']['export_status_counts']}`",
            f"- recommended modes: `{plan['summary']['recommended_mode_counts']}`",
            f"- tracks needing sequence semantics: `{plan['summary']['needs_sequence_semantics_count']}`",
            f"- tracks with loop metadata placeholders: `{loop_metadata_count}`",
            "",
            "## Playback Confidence",
            "",
            f"- all-track near-oracle passed: `{plan['playback_confidence']['all_track_near_oracle_passed']}`",
            f"- independent emulator gate passed: `{plan['playback_confidence']['independent_emulator_gate_passed']}`",
            f"- release-quality playback claim ready: `{plan['playback_confidence']['release_quality_playback_claim_ready']}`",
            "",
            "## Defaults",
            "",
            f"- sample format: `{plan['defaults']['sample_rate']}` Hz, `{plan['defaults']['channels']}` channels, `{plan['defaults']['bits_per_sample']}` bits",
            f"- loop preview: `{plan['defaults']['loop_preview_count']}` loops plus `{plan['defaults']['loop_preview_fade_seconds']}` second fade",
            f"- finite trim policy: {plan['defaults']['finite_trim_tail_policy']}",
            "",
            "## Release Gates",
            "",
            *gates,
            "",
            "## Tracks",
            "",
            "| Track | Name | Policy Class | Export Class | Status | Mode | Duration Seconds | Needs Semantics |",
            "| ---: | --- | --- | --- | --- | --- | ---: | --- |",
            *rows,
            "",
        ]
    )


def main() -> int:
    args = parse_args()
    plan = build_plan(
        Path(args.policy),
        Path(args.measurements),
        Path(args.extended_measurements),
        Path(args.oracle_report),
    )
    json_path = Path(args.json)
    markdown_path = Path(args.markdown)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(plan, indent=2) + "\n", encoding="utf-8")
    markdown_path.write_text(render_markdown(plan), encoding="utf-8")
    print(
        "Built audio export plan: "
        f"{plan['summary']['track_count']} tracks, classes {plan['summary']['export_class_counts']}"
    )
    print(f"Wrote {json_path}")
    print(f"Wrote {markdown_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
