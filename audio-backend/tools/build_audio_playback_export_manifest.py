#!/usr/bin/env python3
"""Build a local playback/export manifest from validated audio backend results."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SUMMARY = (
    ROOT
    / "build"
    / "audio"
    / "c0ab06-change-music-fusion-render-jobs-all"
    / "snes_spc-result-summary.json"
)
DEFAULT_DURATION_POLICY = ROOT / "manifests" / "audio-export-duration-policy.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build an audio playback/export manifest.")
    parser.add_argument("--summary", default=str(DEFAULT_SUMMARY), help="Backend result summary JSON path.")
    parser.add_argument(
        "--metrics",
        help="Render metrics JSON path. Defaults to libgme-render-metrics.json beside the summary.",
    )
    parser.add_argument(
        "--output",
        help="Manifest JSON path. Defaults to playback-export-manifest.json beside the summary.",
    )
    parser.add_argument(
        "--duration-policy",
        default=str(DEFAULT_DURATION_POLICY),
        help="Duration/loop policy JSON path to embed per-track export metadata.",
    )
    parser.add_argument(
        "--source-state",
        default="full_change_music_real_c0ab06_live_driver_zero_burst_keyon_snapshot",
        help="Human-readable capture state used by this export set.",
    )
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def output_by_kind(result: dict[str, Any], kind: str) -> dict[str, Any] | None:
    for output in result.get("outputs", []):
        if output.get("kind") == kind:
            return output
    return None


def policy_by_track(policy_path: Path) -> dict[int, dict[str, Any]]:
    if not policy_path.exists():
        return {}
    policy = load_json(policy_path)
    return {int(track["track_id"]): track for track in policy.get("tracks", [])}


def export_metadata(policy_track: dict[str, Any] | None) -> dict[str, Any]:
    if not policy_track:
        return {
            "duration_class": "unknown_candidate",
            "metadata_status": "missing_duration_policy",
            "release_ready": False,
            "preview": {
                "mode": "diagnostic_preview",
                "seconds": 30.0,
                "fade_seconds": 5.0,
            },
            "loop": None,
            "finite": None,
        }

    duration_class = str(policy_track["duration_class"])
    target = dict(policy_track.get("target_metadata", {}))
    metadata = {
        "duration_class": duration_class,
        "exact_duration_status": policy_track.get("exact_duration_status"),
        "policy": policy_track.get("export_policy"),
        "confidence": policy_track.get("confidence"),
        "release_ready": False,
        "target_metadata": target,
    }
    if duration_class == "looping_candidate":
        metadata.update(
            {
                "metadata_status": "loop_points_pending",
                "preview": {
                    "mode": "loop_count_plus_fade_preview",
                    "loop_count": 2,
                    "fade_seconds": 5.0,
                    "requires_measured_loop_points": True,
                },
                "loop": {
                    "intro_samples": target.get("intro_samples"),
                    "loop_start_sample": target.get("loop_start_sample"),
                    "loop_end_sample": target.get("loop_end_sample"),
                    "measured_by": target.get("measured_by"),
                },
                "finite": None,
            }
        )
    elif duration_class == "finite_candidate":
        metadata.update(
            {
                "metadata_status": "finite_end_pending",
                "preview": {
                    "mode": "diagnostic_or_trim_candidate",
                    "seconds": policy_track.get("current_preview_seconds", 30.0),
                    "fade_seconds": 0.0,
                },
                "loop": None,
                "finite": {
                    "finite_end_sample": target.get("finite_end_sample"),
                    "measured_by": target.get("measured_by"),
                },
            }
        )
    elif duration_class == "no_audio_no_key_on":
        metadata.update(
            {
                "metadata_status": "not_applicable",
                "release_ready": True,
                "preview": {"mode": "skip", "seconds": 0.0, "fade_seconds": 0.0},
                "loop": None,
                "finite": None,
            }
        )
    else:
        metadata.update(
            {
                "metadata_status": "needs_sequence_or_runtime_analysis",
                "preview": {
                    "mode": "diagnostic_preview",
                    "seconds": policy_track.get("current_preview_seconds", 30.0),
                    "fade_seconds": 5.0,
                },
                "loop": None,
                "finite": None,
            }
        )
    return metadata


def build_manifest(summary_path: Path, metrics_path: Path, source_state: str, duration_policy_path: Path) -> dict[str, Any]:
    summary = load_json(summary_path)
    metrics = load_json(metrics_path)
    job_index_path = Path(str(summary.get("job_index", "")))
    job_index = load_json(job_index_path) if job_index_path.exists() else {}
    metrics_by_job = {record["job_id"]: record for record in metrics.get("records", [])}
    duration_policy_by_track = policy_by_track(duration_policy_path)
    tracks: list[dict[str, Any]] = []

    for record in summary.get("results", []):
        result_path = Path(record["result_path"])
        result = load_json(result_path)
        metric = metrics_by_job.get(record["job_id"], {})
        wav = output_by_kind(result, "rendered_wav")
        spc = output_by_kind(result, "complete_spc_snapshot")
        render_hash = output_by_kind(result, "render_hash_json")
        tracks.append(
            {
                "job_id": record["job_id"],
                "track_id": int(record["track_id"]),
                "track_name": record["track_name"],
                "backend_id": record["backend_id"],
                "backend_version": result.get("backend_version"),
                "status": record.get("status"),
                "valid": bool(record.get("valid")),
                "classification": metric.get("classification", "missing"),
                "source_state": source_state,
                "source_spc": spc,
                "rendered_wav": wav,
                "render_hash": render_hash,
                "export_metadata": export_metadata(duration_policy_by_track.get(int(record["track_id"]))),
                "metrics": {
                    "peak_abs_sample": metric.get("peak_abs_sample"),
                    "rms_sample": metric.get("rms_sample"),
                    "nonzero_sample_count": metric.get("nonzero_sample_count"),
                    "first_nonzero_sample_index": metric.get("first_nonzero_sample_index"),
                    "last_nonzero_sample_index": metric.get("last_nonzero_sample_index"),
                    "voice_count": metric.get("voice_count"),
                    "rendered_samples": metric.get("rendered_samples"),
                    "warning": metric.get("warning", ""),
                },
            }
        )

    tracks.sort(key=lambda item: int(item["track_id"]))
    status_counts: dict[str, int] = {}
    classification_counts: dict[str, int] = {}
    for track in tracks:
        status_counts[str(track["status"])] = status_counts.get(str(track["status"]), 0) + 1
        classification_counts[str(track["classification"])] = classification_counts.get(str(track["classification"]), 0) + 1

    passed_tracks = [
        track
        for track in tracks
        if track["status"] == "ok" and track["valid"] and track["classification"] == "audible"
    ]
    return {
        "schema": "earthbound-decomp.audio-playback-export-manifest.v1",
        "summary_path": str(summary_path),
        "metrics_path": str(metrics_path),
        "duration_policy_path": str(duration_policy_path),
        "backend_id": summary.get("backend_id"),
        "job_index": summary.get("job_index"),
        "track_count": len(tracks),
        "table_entry_count": len(tracks) + int(job_index.get("skipped_count", 0)),
        "skipped_count": int(job_index.get("skipped_count", 0)),
        "skipped_records": job_index.get("skipped_records", []),
        "status_counts": status_counts,
        "classification_counts": classification_counts,
        "quality_gate": {
            "required_status": "ok",
            "required_validation": True,
            "required_classification": "audible",
            "passed_count": len(passed_tracks),
            "failed_count": len(tracks) - len(passed_tracks),
        },
        "source_policy": {
            "generated_locally": True,
            "contains_rom_derived_payloads": True,
            "distribution": "never_distribute_generated_audio_or_spc_outputs",
            "consumer": "local_app_playback_and_user_export_only",
        },
        "tracks": tracks,
    }


def render_markdown(manifest: dict[str, Any]) -> str:
    rows = [
        "| `{track_id:03d}` | `{track_name}` | `{status}` | `{classification}` | `{duration_class}` | `{metadata_status}` | {peak} | `{wav}` |".format(
            track_id=track["track_id"],
            track_name=track["track_name"],
            status=track["status"],
            classification=track["classification"],
            duration_class=track["export_metadata"]["duration_class"],
            metadata_status=track["export_metadata"]["metadata_status"],
            peak=track["metrics"].get("peak_abs_sample", ""),
            wav=Path(track["rendered_wav"]["path"]).name if track.get("rendered_wav") else "",
        )
        for track in manifest["tracks"]
    ]
    return "\n".join(
        [
            "# Audio Playback Export Manifest",
            "",
            "Status: local playback/export handoff generated from validated backend results.",
            "",
            f"- backend: `{manifest['backend_id']}`",
            f"- tracks: `{manifest['track_count']}`",
            f"- skipped table entries: `{manifest.get('skipped_count', 0)}`",
            f"- status counts: `{manifest['status_counts']}`",
            f"- classification counts: `{manifest['classification_counts']}`",
            f"- quality gate: `{manifest['quality_gate']['passed_count']}` passed, `{manifest['quality_gate']['failed_count']}` failed",
            f"- duration policy: `{manifest['duration_policy_path']}`",
            "",
            "The WAV/SPC outputs referenced here are ROM-derived local artifacts. They are for local playback/export only and must not be distributed.",
            "Looping tracks carry explicit preview metadata now; exact loop start/end samples remain pending until sequence/runtime measurement fills them.",
            "",
            "## Tracks",
            "",
            "| Track | Name | Status | Class | Duration Class | Metadata | Peak | WAV |",
            "| ---: | --- | --- | --- | --- | --- | ---: | --- |",
            *rows,
            "",
        ]
    )


def main() -> int:
    args = parse_args()
    summary_path = Path(args.summary)
    metrics_path = Path(args.metrics) if args.metrics else summary_path.parent / "libgme-render-metrics.json"
    output_path = Path(args.output) if args.output else summary_path.parent / "playback-export-manifest.json"
    manifest = build_manifest(summary_path, metrics_path, args.source_state, Path(args.duration_policy))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    markdown_path = output_path.with_suffix(".md")
    markdown_path.write_text(render_markdown(manifest), encoding="utf-8")
    print(f"Built audio playback/export manifest: {manifest['track_count']} tracks -> {output_path}")
    print(f"Wrote {markdown_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
