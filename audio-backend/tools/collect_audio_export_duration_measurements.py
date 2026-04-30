#!/usr/bin/env python3
"""Measure duration evidence from the local audio playback/export corpus.

The current renderer corpus is intentionally a 30-second diagnostic preview.
This tool records what those WAVs can prove about finite endings without
pretending that every track has a fixed length.
"""

from __future__ import annotations

import argparse
import json
import wave
from array import array
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_POLICY = ROOT / "manifests" / "audio-export-duration-policy.json"
DEFAULT_PLAYBACK = (
    ROOT
    / "build"
    / "audio"
    / "c0ab06-change-music-fusion-render-jobs-all"
    / "playback-export-manifest.json"
)
DEFAULT_OUTPUT = ROOT / "build" / "audio" / "export-duration-measurements" / "export-duration-measurements.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Measure export duration evidence from rendered WAV previews.")
    parser.add_argument("--policy", default=str(DEFAULT_POLICY), help="Audio export duration policy JSON.")
    parser.add_argument("--playback", default=str(DEFAULT_PLAYBACK), help="Audio playback/export manifest JSON.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Measurement JSON output path.")
    parser.add_argument(
        "--silence-threshold",
        type=int,
        default=16,
        help="Absolute 16-bit PCM sample threshold treated as digital silence.",
    )
    parser.add_argument(
        "--sustained-silence-seconds",
        type=float,
        default=2.0,
        help="Tail silence duration required before a finite ending is observed.",
    )
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def abs16(value: int) -> int:
    return -value if value < 0 else value


def read_wav_measurement(path: Path, silence_threshold: int, sustained_silence_seconds: float) -> dict[str, Any]:
    with wave.open(str(path), "rb") as wav:
        channels = wav.getnchannels()
        sample_width = wav.getsampwidth()
        sample_rate = wav.getframerate()
        frame_count = wav.getnframes()
        pcm = wav.readframes(frame_count)

    if sample_width != 2:
        return {
            "wav_format_valid": False,
            "format_error": f"unsupported sample width: {sample_width}",
            "sample_rate": sample_rate,
            "channels": channels,
            "sample_width": sample_width,
            "total_frames": frame_count,
        }

    samples = array("h")
    samples.frombytes(pcm)
    if samples.itemsize != 2:
        raise RuntimeError("unexpected platform array('h') item size")

    first_above_sample: int | None = None
    last_above_sample: int | None = None
    peak_abs = 0

    for index, value in enumerate(samples):
        magnitude = abs16(int(value))
        if magnitude > peak_abs:
            peak_abs = magnitude
        if first_above_sample is None and magnitude > silence_threshold:
            first_above_sample = index

    for index in range(len(samples) - 1, -1, -1):
        if abs16(int(samples[index])) > silence_threshold:
            last_above_sample = index
            break

    total_seconds = frame_count / sample_rate if sample_rate else 0.0
    sustained_silence_frames = int(round(sustained_silence_seconds * sample_rate))

    if first_above_sample is None or last_above_sample is None:
        return {
            "wav_format_valid": True,
            "sample_rate": sample_rate,
            "channels": channels,
            "sample_width": sample_width,
            "total_frames": frame_count,
            "total_seconds": round(total_seconds, 6),
            "peak_abs_sample": peak_abs,
            "first_above_threshold_frame": None,
            "last_above_threshold_frame": None,
            "tail_silence_frames": frame_count,
            "tail_silence_seconds": round(total_seconds, 6),
            "sustained_tail_silence_observed": frame_count >= sustained_silence_frames,
            "candidate_end_frame": 0,
            "candidate_end_seconds": 0.0,
        }

    first_frame = first_above_sample // channels
    last_frame = last_above_sample // channels
    candidate_end_frame = min(last_frame + 1, frame_count)
    tail_silence_frames = max(0, frame_count - candidate_end_frame)
    tail_silence_seconds = tail_silence_frames / sample_rate if sample_rate else 0.0

    return {
        "wav_format_valid": True,
        "sample_rate": sample_rate,
        "channels": channels,
        "sample_width": sample_width,
        "total_frames": frame_count,
        "total_seconds": round(total_seconds, 6),
        "peak_abs_sample": peak_abs,
        "first_above_threshold_frame": first_frame,
        "last_above_threshold_frame": last_frame,
        "tail_silence_frames": tail_silence_frames,
        "tail_silence_seconds": round(tail_silence_seconds, 6),
        "sustained_tail_silence_observed": tail_silence_frames >= sustained_silence_frames,
        "candidate_end_frame": candidate_end_frame,
        "candidate_end_seconds": round(candidate_end_frame / sample_rate, 6) if sample_rate else 0.0,
    }


def classify_measurement(policy_track: dict[str, Any], measurement: dict[str, Any] | None) -> tuple[str, str, bool]:
    duration_class = str(policy_track["duration_class"])
    if duration_class == "no_audio_no_key_on":
        return "no_audio_no_key_on", "No render is expected for this load-ok/no-key-on table entry.", False
    if measurement is None:
        return "missing_preview", "No rendered WAV preview was available for measurement.", False
    if not measurement.get("wav_format_valid", False):
        return "invalid_preview_wav", "Rendered WAV exists but is not a supported 16-bit PCM WAV.", False

    sustained = bool(measurement.get("sustained_tail_silence_observed", False))
    if duration_class == "finite_candidate":
        if sustained:
            return (
                "finite_end_observed_in_preview",
                "Name-based finite candidate reaches sustained trailing PCM silence within the diagnostic preview.",
                False,
            )
        return (
            "finite_candidate_no_end_seen_in_preview",
            "Name-based finite candidate remains above the silence threshold through the diagnostic preview.",
            False,
        )
    if duration_class == "looping_candidate":
        if sustained:
            return (
                "looping_candidate_silence_seen_review_needed",
                "A likely looping candidate reaches trailing silence; review sequence/runtime semantics before classifying as finite.",
                False,
            )
        return (
            "looping_candidate_preview_still_active",
            "Likely looping candidate remains active through the diagnostic preview; loop points still need sequence/runtime evidence.",
            False,
        )
    if sustained:
        return (
            "unknown_silence_seen_needs_classification",
            "Unclassified track reaches trailing silence; sequence/runtime semantics should decide whether this is finite.",
            False,
        )
    return (
        "unknown_preview_still_active",
        "Unclassified track remains active through the diagnostic preview; sequence/runtime semantics still needed.",
        False,
    )


def build_measurements(
    policy_path: Path,
    playback_path: Path,
    silence_threshold: int,
    sustained_silence_seconds: float,
) -> dict[str, Any]:
    policy = load_json(policy_path)
    playback = load_json(playback_path)
    playback_by_track = {int(track["track_id"]): track for track in playback.get("tracks", [])}

    records: list[dict[str, Any]] = []
    status_counts: Counter[str] = Counter()
    finite_observed = 0

    for policy_track in policy.get("tracks", []):
        track_id = int(policy_track["track_id"])
        playback_track = playback_by_track.get(track_id)
        wav_path: Path | None = None
        measurement: dict[str, Any] | None = None
        if playback_track and playback_track.get("rendered_wav"):
            wav_path = Path(playback_track["rendered_wav"]["path"])
            if wav_path.exists():
                measurement = read_wav_measurement(wav_path, silence_threshold, sustained_silence_seconds)

        status, reason, exact_ready = classify_measurement(policy_track, measurement)
        status_counts[status] += 1
        if status == "finite_end_observed_in_preview":
            finite_observed += 1

        record: dict[str, Any] = {
            "track_id": track_id,
            "track_name": policy_track["track_name"],
            "duration_class": policy_track["duration_class"],
            "policy_exact_duration_status": policy_track["exact_duration_status"],
            "measurement_status": status,
            "reason": reason,
            "release_exact_length_ready": exact_ready,
            "evidence_level": "diagnostic_preview_pcm_only" if measurement else "no_preview_measurement",
            "rendered_wav": str(wav_path) if wav_path else None,
            "measurement": measurement,
        }
        if measurement and measurement.get("sustained_tail_silence_observed"):
            record["candidate_duration"] = {
                "end_frame": measurement.get("candidate_end_frame"),
                "end_seconds": measurement.get("candidate_end_seconds"),
                "tail_silence_seconds": measurement.get("tail_silence_seconds"),
                "silence_threshold_abs_sample": silence_threshold,
            }
        records.append(record)

    return {
        "schema": "earthbound-decomp.audio-export-duration-measurements.v1",
        "status": "diagnostic_preview_duration_measurements_collected",
        "policy": str(policy_path),
        "playback_manifest": str(playback_path),
        "measurement_policy": {
            "silence_threshold_abs_sample": silence_threshold,
            "sustained_tail_silence_seconds": sustained_silence_seconds,
            "source_limit": "30-second diagnostic previews only",
            "release_claim": "preview measurements are candidates; exact release lengths still require sequence/runtime or oracle confirmation",
        },
        "summary": {
            "track_count": len(records),
            "rendered_preview_count": sum(1 for record in records if record["measurement"] is not None),
            "status_counts": dict(status_counts),
            "finite_candidates_with_preview_end": finite_observed,
            "release_exact_length_ready_count": sum(1 for record in records if record["release_exact_length_ready"]),
        },
        "records": records,
    }


def render_markdown(summary: dict[str, Any]) -> str:
    rows = []
    for record in summary["records"]:
        measurement = record.get("measurement") or {}
        candidate = record.get("candidate_duration") or {}
        rows.append(
            "| `{track_id:03d}` | `{track_name}` | `{duration_class}` | `{measurement_status}` | {end} | {tail} |".format(
                track_id=record["track_id"],
                track_name=record["track_name"],
                duration_class=record["duration_class"],
                measurement_status=record["measurement_status"],
                end=candidate.get("end_seconds", ""),
                tail=measurement.get("tail_silence_seconds", ""),
            )
        )
    return "\n".join(
        [
            "# Audio Export Duration Measurements",
            "",
            "Status: diagnostic preview duration evidence collected. These measurements do not by themselves make release exact-length claims.",
            "",
            f"- tracks: `{summary['summary']['track_count']}`",
            f"- rendered previews measured: `{summary['summary']['rendered_preview_count']}`",
            f"- statuses: `{summary['summary']['status_counts']}`",
            f"- finite candidates with preview end: `{summary['summary']['finite_candidates_with_preview_end']}`",
            f"- release exact-length ready: `{summary['summary']['release_exact_length_ready_count']}`",
            "",
            "## Measurement Policy",
            "",
            f"- silence threshold: `{summary['measurement_policy']['silence_threshold_abs_sample']}` absolute PCM sample",
            f"- sustained tail silence: `{summary['measurement_policy']['sustained_tail_silence_seconds']}` seconds",
            f"- source limit: {summary['measurement_policy']['source_limit']}",
            f"- release claim: {summary['measurement_policy']['release_claim']}",
            "",
            "## Tracks",
            "",
            "| Track | Name | Policy Class | Measurement Status | Candidate End Seconds | Tail Silence Seconds |",
            "| ---: | --- | --- | --- | ---: | ---: |",
            *rows,
            "",
        ]
    )


def main() -> int:
    args = parse_args()
    output_path = Path(args.output)
    summary = build_measurements(
        Path(args.policy),
        Path(args.playback),
        args.silence_threshold,
        args.sustained_silence_seconds,
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    markdown_path = output_path.with_suffix(".md")
    markdown_path.write_text(render_markdown(summary), encoding="utf-8")
    print(
        "Collected audio export duration measurements: "
        f"{summary['summary']['rendered_preview_count']} previews, statuses {summary['summary']['status_counts']}"
    )
    print(f"Wrote {output_path}")
    print(f"Wrote {markdown_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
