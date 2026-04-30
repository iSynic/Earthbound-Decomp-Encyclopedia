#!/usr/bin/env python3
"""Validate the local audio runtime frontier report."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_REPORT = ROOT / "build" / "audio" / "last-keyon-jobs" / "audio-runtime-frontier.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate the audio runtime frontier report.")
    parser.add_argument("report", nargs="?", default=str(DEFAULT_REPORT), help="Runtime frontier JSON path.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(report: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if report.get("schema") != "earthbound-decomp.audio-runtime-frontier.v1":
        errors.append(f"unexpected schema: {report.get('schema')}")
    records = report.get("records", [])
    summary = report.get("summary", {})
    if int(summary.get("track_count", -1)) != len(records):
        errors.append(f"track_count {summary.get('track_count')} does not match {len(records)} records")
    regression = report.get("regression_target", {})
    required_true = [
        "all_tracks_have_key_on_events",
        "all_tracks_have_last_keyon_snapshots",
        "all_tracks_render_audible",
        "all_render_sources_match_last_keyon_snapshots",
        "all_tracks_have_command_injection",
        "all_tracks_have_command_first_read",
        "all_command_reads_follow_injection",
        "all_keyon_snapshots_follow_command_read",
        "no_track_worse_than_baseline",
        "no_track_worse_than_keyon_primed",
    ]
    for field in required_true:
        if regression.get(field) is not True:
            errors.append(f"regression target failed: {field}")
    audit = report.get("shortcut_audit", {})
    if audit.get("snapshot_is_final_faithful_runtime") is not False:
        errors.append("shortcut audit should still mark final faithful runtime as false")
    if audit.get("uses_real_cpu_apu_track_start_handshake") is not False:
        errors.append("shortcut audit should still mark real CPU/APU handshake as false")
    seen: set[int] = set()
    for record in records:
        track_id = int(record.get("track_id", -1))
        if track_id in seen:
            errors.append(f"duplicate track {track_id}")
        seen.add(track_id)
        capture = record.get("capture", {})
        snapshot = record.get("last_keyon_snapshot", {})
        render = record.get("render", {})
        injection = capture.get("host_command_injection") or {}
        first_read = capture.get("host_command_first_read") or {}
        capture_snapshot = capture.get("last_key_on_snapshot") or {}
        if int(capture.get("dsp_key_on_event_count", 0)) <= 0:
            errors.append(f"track {track_id}: missing key-on event")
        if not injection:
            errors.append(f"track {track_id}: missing host command injection event")
        if not first_read:
            errors.append(f"track {track_id}: missing host command first-read event")
        if injection and first_read and int(first_read.get("sequence", 0)) < int(injection.get("sequence", 0)):
            errors.append(f"track {track_id}: host command first read occurs before injection")
        if first_read and capture_snapshot and int(capture_snapshot.get("instruction", 0)) < int(first_read.get("instruction", 0)):
            errors.append(f"track {track_id}: last key-on snapshot occurs before command first read")
        if not snapshot.get("available"):
            errors.append(f"track {track_id}: missing last-key-on snapshot")
        if snapshot.get("kon") in (None, "0x00"):
            errors.append(f"track {track_id}: missing nonzero KON")
        if snapshot.get("sha1") != render.get("source_spc_sha1"):
            errors.append(f"track {track_id}: render source SHA-1 does not match last-key-on snapshot")
        if render.get("classification") != "audible":
            errors.append(f"track {track_id}: render is {render.get('classification')}, expected audible")
        if int(render.get("peak_abs_sample", 0)) < 512:
            errors.append(f"track {track_id}: peak_abs_sample below audible threshold")
    return errors


def main() -> int:
    args = parse_args()
    report = load_json(Path(args.report))
    errors = validate(report)
    if errors:
        print("Audio runtime frontier validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    summary = report["summary"]
    print(
        "Audio runtime frontier validation OK: "
        f"{summary['audible_render_count']} audible renders, "
        f"{summary['matching_render_source_sha1_count']} matching render sources"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
