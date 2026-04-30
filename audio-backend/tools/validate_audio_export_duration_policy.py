#!/usr/bin/env python3
"""Validate the audio export duration policy manifest."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_POLICY = ROOT / "manifests" / "audio-export-duration-policy.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate the audio export duration policy manifest.")
    parser.add_argument("policy", nargs="?", default=str(DEFAULT_POLICY))
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(policy: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if policy.get("schema") != "earthbound-decomp.audio-export-duration-policy.v1":
        errors.append(f"unexpected schema: {policy.get('schema')}")
    tracks = policy.get("tracks", [])
    if int(policy.get("summary", {}).get("track_count", -1)) != len(tracks):
        errors.append("summary track_count does not match tracks")
    allowed_classes = {"finite_candidate", "looping_candidate", "unknown_candidate", "no_audio_no_key_on"}
    allowed_statuses = {
        "needs_driver_end_or_silence_detection",
        "needs_loop_point_detection",
        "needs_sequence_or_runtime_analysis",
        "not_applicable",
    }
    seen: set[int] = set()
    class_counts: dict[str, int] = {}
    status_counts: dict[str, int] = {}
    for track in tracks:
        track_id = int(track.get("track_id", -1))
        if track_id in seen:
            errors.append(f"duplicate track id {track_id}")
        seen.add(track_id)
        duration_class = str(track.get("duration_class", ""))
        exact_status = str(track.get("exact_duration_status", ""))
        if duration_class not in allowed_classes:
            errors.append(f"track {track_id}: unexpected duration class {duration_class}")
        if exact_status not in allowed_statuses:
            errors.append(f"track {track_id}: unexpected exact status {exact_status}")
        if duration_class == "no_audio_no_key_on" and exact_status != "not_applicable":
            errors.append(f"track {track_id}: no-audio track must have not_applicable exact status")
        if duration_class != "no_audio_no_key_on" and float(track.get("current_preview_seconds", 0.0)) <= 0:
            errors.append(f"track {track_id}: audible/unknown track must keep a positive diagnostic preview")
        target = track.get("target_metadata", {})
        for key in ("intro_samples", "loop_start_sample", "loop_end_sample", "finite_end_sample", "measured_by"):
            if key not in target:
                errors.append(f"track {track_id}: missing target metadata {key}")
        class_counts[duration_class] = class_counts.get(duration_class, 0) + 1
        status_counts[exact_status] = status_counts.get(exact_status, 0) + 1

    if class_counts != policy.get("summary", {}).get("duration_class_counts"):
        errors.append("duration_class_counts does not match tracks")
    if status_counts != policy.get("summary", {}).get("exact_duration_status_counts"):
        errors.append("exact_duration_status_counts does not match tracks")
    gates = policy.get("release_gates", [])
    if len(gates) < 5:
        errors.append("release gate checklist is too short")
    if "looping_tracks" not in policy.get("policy", {}):
        errors.append("policy must describe looping tracks")
    return errors


def main() -> int:
    args = parse_args()
    policy = load_json(Path(args.policy))
    errors = validate(policy)
    if errors:
        print("Audio export duration policy validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "Audio export duration policy validation OK: "
        f"{policy['summary']['track_count']} tracks, classes {policy['summary']['duration_class_counts']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
