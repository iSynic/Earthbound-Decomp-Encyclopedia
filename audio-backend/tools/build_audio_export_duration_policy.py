#!/usr/bin/env python3
"""Build the audio export duration policy manifest.

EarthBound tracks are not ordinary fixed-length files. Some are finite jingles
or scene cues; many are music cues that intentionally loop forever. This
manifest makes that distinction explicit before renderer jobs move away from a
flat 30-second diagnostic preview.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONTRACT = ROOT / "manifests" / "audio-pack-contracts.json"
DEFAULT_JSON = ROOT / "manifests" / "audio-export-duration-policy.json"
DEFAULT_MARKDOWN = ROOT / "notes" / "audio-export-duration-policy.md"

SILENT_TRACK_IDS = {4}

FINITE_CANDIDATE_KEYWORDS = (
    "YOU_WON",
    "LEVEL_UP",
    "YOU_LOSE",
    "TELEPORT_IN",
    "TELEPORT_OUT",
    "TELEPORT_FAIL",
    "FALLING_UNDERGROUND",
    "ELEVATOR_DOWN",
    "ELEVATOR_UP",
    "ELEVATOR_STOP",
    "EXPLOSION",
    "SKY_RUNNER_CRASH",
    "BUZZ_BUZZ_SWATTED",
    "PHONE_CALL",
    "KNOCK_KNOCK",
    "SUDDEN_VICTORY",
    "METEOR_STRIKE",
    "METEOR_FALL",
    "SOUNDSTONE_RECORDING",
)

LOOPING_CANDIDATE_KEYWORDS = (
    "ONETT",
    "FOURSIDE",
    "SUMMERS",
    "DALAAM",
    "SCARABA",
    "SATURN_VALLEY",
    "MOONSIDE",
    "WINTERS",
    "DEEP_DARKNESS",
    "Tenda".upper(),
    "VS_",
    "GIYGAS",
    "RUNAWAY5",
    "YOUR_SANCTUARY",
    "BATTLE",
    "TITLE_SCREEN",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the audio export duration policy manifest.")
    parser.add_argument("--contract", default=str(DEFAULT_CONTRACT), help="Audio pack contract JSON path.")
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


def classify_track(track: dict[str, Any]) -> dict[str, Any]:
    track_id = int(track["track_id"])
    name = str(track["name"])
    if track_id in SILENT_TRACK_IDS:
        return {
            "duration_class": "no_audio_no_key_on",
            "exact_duration_status": "not_applicable",
            "export_policy": "skip_render",
            "confidence": "observed",
            "reason": "The all-track fusion corpus classifies this table entry as load-ok/no-key-on.",
        }
    if any(keyword in name for keyword in FINITE_CANDIDATE_KEYWORDS):
        return {
            "duration_class": "finite_candidate",
            "exact_duration_status": "needs_driver_end_or_silence_detection",
            "export_policy": "render_until_driver_end_or_sustained_silence_then_trim_tail",
            "confidence": "name_based_candidate",
            "reason": "Name suggests a jingle, transition cue, crash/explosion cue, or recording cue, but sequence/end semantics still need measurement.",
        }
    if any(keyword in name for keyword in LOOPING_CANDIDATE_KEYWORDS):
        return {
            "duration_class": "looping_candidate",
            "exact_duration_status": "needs_loop_point_detection",
            "export_policy": "export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview",
            "confidence": "name_based_candidate",
            "reason": "Name suggests field, battle, title, boss, or event music that likely loops in-game.",
        }
    return {
        "duration_class": "unknown_candidate",
        "exact_duration_status": "needs_sequence_or_runtime_analysis",
        "export_policy": "keep_diagnostic_preview_until_duration_is_measured",
        "confidence": "unclassified",
        "reason": "No durable end/loop evidence has been recorded yet.",
    }


def build_policy(contract: dict[str, Any], contract_path: Path) -> dict[str, Any]:
    tracks = []
    class_counts: dict[str, int] = {}
    status_counts: dict[str, int] = {}
    for track in sorted(contract.get("tracks", []), key=lambda item: int(item["track_id"])):
        classification = classify_track(track)
        record = {
            "track_id": int(track["track_id"]),
            "track_name": track["name"],
            **classification,
            "current_preview_seconds": 30.0 if int(track["track_id"]) not in SILENT_TRACK_IDS else 0.0,
            "target_metadata": {
                "intro_samples": None,
                "loop_start_sample": None,
                "loop_end_sample": None,
                "finite_end_sample": None,
                "fade_seconds": None,
                "measured_by": None,
            },
        }
        tracks.append(record)
        class_counts[record["duration_class"]] = class_counts.get(record["duration_class"], 0) + 1
        status_counts[record["exact_duration_status"]] = status_counts.get(record["exact_duration_status"], 0) + 1

    return {
        "schema": "earthbound-decomp.audio-export-duration-policy.v1",
        "status": "duration_policy_ready_exact_lengths_not_yet_measured",
        "contract": repo_path(contract_path),
        "summary": {
            "track_count": len(tracks),
            "duration_class_counts": class_counts,
            "exact_duration_status_counts": status_counts,
        },
        "policy": {
            "finite_tracks": "Export to the first confirmed driver end, stop command, or sustained digital silence boundary, then trim tail silence according to measured samples.",
            "looping_tracks": "Do not pretend a looped cue has a finite exact length. Store loop start/end metadata; preview/export WAVs should use an explicit loop-count and fade policy.",
            "unknown_tracks": "Keep 30-second diagnostic previews out of release claims until sequence semantics or runtime measurement classifies the track.",
            "recommended_loop_preview": {
                "loops": 2,
                "fade_seconds": 5.0,
                "minimum_intro_seconds": 0.0,
            },
            "measurement_sources": [
                "music sequence VM end/loop opcodes",
                "runtime DSP key-off and sustained silence detection",
                "external emulator oracle captures",
            ],
        },
        "release_gates": [
            "Every rendered public export must declare finite, looping, no-audio, or unknown duration class.",
            "Finite exports must have a measured end sample or an explained silence threshold.",
            "Looping exports must include loop metadata or explicitly state the chosen loop-count/fade preview policy.",
            "The current 30-second renders remain diagnostic previews until this policy is measured per track.",
            "Exact-length claims require sequence/runtime evidence, not only track-name heuristics.",
        ],
        "tracks": tracks,
    }


def render_markdown(policy: dict[str, Any]) -> str:
    rows = [
        "| `{track_id:03d}` | `{track_name}` | `{duration_class}` | `{exact_duration_status}` | `{export_policy}` | {confidence} |".format(
            **track
        )
        for track in policy["tracks"]
    ]
    gates = [f"- {gate}" for gate in policy["release_gates"]]
    return "\n".join(
        [
            "# Audio Export Duration Policy",
            "",
            "Status: duration policy ready; exact finite lengths and loop points are not yet measured.",
            "",
            f"- tracks: `{policy['summary']['track_count']}`",
            f"- duration classes: `{policy['summary']['duration_class_counts']}`",
            f"- exact-duration statuses: `{policy['summary']['exact_duration_status_counts']}`",
            "",
            "## Policy",
            "",
            f"- finite tracks: {policy['policy']['finite_tracks']}",
            f"- looping tracks: {policy['policy']['looping_tracks']}",
            f"- unknown tracks: {policy['policy']['unknown_tracks']}",
            f"- recommended loop preview: `{policy['policy']['recommended_loop_preview']}`",
            "",
            "## Release Gates",
            "",
            *gates,
            "",
            "## Tracks",
            "",
            "| Track | Name | Class | Exact Status | Export Policy | Confidence |",
            "| ---: | --- | --- | --- | --- | --- |",
            *rows,
            "",
        ]
    )


def main() -> int:
    args = parse_args()
    contract_path = Path(args.contract)
    policy = build_policy(load_json(contract_path), contract_path)
    json_path = Path(args.json)
    markdown_path = Path(args.markdown)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(policy, indent=2) + "\n", encoding="utf-8")
    markdown_path.write_text(render_markdown(policy), encoding="utf-8")
    print(
        "Built audio export duration policy: "
        f"{policy['summary']['track_count']} tracks, classes {policy['summary']['duration_class_counts']}"
    )
    print(f"Wrote {json_path}")
    print(f"Wrote {markdown_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
