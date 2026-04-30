#!/usr/bin/env python3
"""Build snes_spc/libgme backend jobs directly from an SPC snapshot index."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from audio_renderers import AudioBackendJob, AudioRenderOptions, backend_job_to_dict, describe_renderer_backends
from build_audio_backend_jobs import expected_outputs_for_backend


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INDEX = (
    ROOT
    / "build"
    / "audio"
    / "c0ab06-change-music-fusion-spc-all"
    / "c0ab06-change-music-fusion-spc-all-snapshots.json"
)
DEFAULT_OUT = ROOT / "build" / "audio" / "c0ab06-change-music-fusion-render-jobs-all"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build backend jobs from an SPC snapshot index.")
    parser.add_argument("--snapshot-index", default=str(DEFAULT_INDEX), help="SPC snapshot index JSON.")
    parser.add_argument("--backend", default="snes_spc", choices=["snes_spc"])
    parser.add_argument("--out", default=str(DEFAULT_OUT), help="Ignored backend job output directory.")
    parser.add_argument("--seconds", type=float, default=30.0)
    parser.add_argument("--fade-seconds", type=float, default=5.0)
    parser.add_argument("--sample-rate", type=int, default=32000)
    parser.add_argument("--channels", type=int, default=2)
    parser.add_argument("--format", default="wav", choices=["wav", "pcm"])
    parser.add_argument(
        "--tracks",
        help="Optional comma-separated track ids to include from the snapshot index.",
    )
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_track_ids(text: str | None) -> set[int] | None:
    if not text:
        return None
    track_ids: set[int] = set()
    for part in text.split(","):
        part = part.strip()
        if part:
            track_ids.add(int(part, 0))
    return track_ids


def safe_track_name(track_name: str) -> str:
    lowered = track_name.lower()
    return "".join(ch if ch.isalnum() or ch in "-_" else "_" for ch in lowered)


def build_job_record(
    record: dict[str, Any],
    backend_id: str,
    output_root: Path,
    options: AudioRenderOptions,
    snapshot_index_path: Path,
) -> dict[str, Any]:
    snapshot = record["snapshot"]
    track_id = int(record["track_id"])
    job_id = f"{backend_id}-track-{track_id:03d}-{safe_track_name(str(record['track_name']))}"
    output_dir = output_root / job_id
    fixture_path = Path(record.get("capture_path") or snapshot_index_path)
    job = AudioBackendJob(
        job_id=job_id,
        backend_id=backend_id,
        fixture_path=fixture_path,
        output_dir=output_dir,
        render_options=options,
        expected_outputs=expected_outputs_for_backend(backend_id, options.output_format),
    )
    job_record = backend_job_to_dict(job)
    job_record["track_id"] = track_id
    job_record["track_name"] = record["track_name"]
    job_record["input_apu_ram_sha1"] = snapshot.get("sha1", "")
    job_record["input_load_mode"] = "spc_snapshot_index"
    job_record["source_snapshot_index"] = str(snapshot_index_path)
    job_record["source_snapshot_path"] = snapshot.get("path")
    job_record["source_snapshot_sha1"] = snapshot.get("sha1")
    job_record["source_snapshot_kind"] = "complete_spc_snapshot"
    job_record["status"] = "planned_waiting_for_backend_harness"
    job_record["result_schema"] = "earthbound-decomp.audio-backend-result.v1"
    job_record["result_path"] = str(output_dir / "result.json")
    job_record["job_path"] = str(output_dir / "job.json")
    return job_record


def render_markdown(job_index: dict[str, Any]) -> str:
    rows = [
        "| `{job_id}` | {track_id} | `{track_name}` | `{snapshot}` | `{job_path}` |".format(
            job_id=job["job_id"],
            track_id=job["track_id"],
            track_name=job["track_name"],
            snapshot=job.get("source_snapshot_path", ""),
            job_path=job["job_path"],
        )
        for job in job_index["jobs"]
    ]
    skipped_rows = [
        "| {track_id} | `{track_name}` | {reason} |".format(
            track_id=record.get("track_id", ""),
            track_name=record.get("track_name", ""),
            reason=record.get("reason", ""),
        )
        for record in job_index.get("skipped_records", [])
    ]
    return "\n".join(
        [
            "# Audio Backend Jobs From SPC Index",
            "",
            "Status: generated local renderer job queue from complete SPC snapshots.",
            "",
            f"- snapshot index: `{job_index['snapshot_index']}`",
            f"- jobs: `{job_index['job_count']}`",
            f"- skipped records: `{job_index['skipped_count']}`",
            "",
            "## Jobs",
            "",
            "| Job | Track | Name | Snapshot | Job path |",
            "| --- | ---: | --- | --- | --- |",
            *rows,
            "",
            "## Skipped Records",
            "",
            "| Track | Name | Reason |",
            "| ---: | --- | --- |",
            *skipped_rows,
            "",
        ]
    )


def main() -> int:
    args = parse_args()
    snapshot_index_path = Path(args.snapshot_index).resolve()
    snapshot_index = load_json(snapshot_index_path)
    output_root = Path(args.out)
    output_root.mkdir(parents=True, exist_ok=True)
    options = AudioRenderOptions(
        seconds=args.seconds,
        fade_seconds=args.fade_seconds,
        sample_rate=args.sample_rate,
        channels=args.channels,
        output_format=args.format,
    )
    wanted_track_ids = parse_track_ids(args.tracks)

    jobs: list[dict[str, Any]] = []
    skipped: list[dict[str, Any]] = []
    for record in snapshot_index.get("records", []):
        track_id = int(record.get("track_id", -1))
        if wanted_track_ids is not None and track_id not in wanted_track_ids:
            continue
        snapshot = record.get("snapshot")
        if not snapshot:
            skipped.append(
                {
                    "track_id": record.get("track_id"),
                    "track_name": record.get("track_name"),
                    "reason": "missing_snapshot",
                }
            )
            continue
        jobs.append(build_job_record(record, args.backend, output_root, options, snapshot_index_path))

    job_index = {
        "schema": "earthbound-decomp.audio-backend-job-index.v1",
        "fixture_index": str(snapshot_index_path),
        "snapshot_index": str(snapshot_index_path),
        "backend_id": args.backend,
        "job_count": len(jobs),
        "skipped_count": len(skipped),
        "skipped_records": skipped,
        "jobs": jobs,
        "backend_catalog": describe_renderer_backends(),
        "source_policy": {
            "requires_user_supplied_rom": True,
            "do_not_commit_generated_outputs": True,
            "generated_audio_output_root": "build/audio",
        },
        "status": "planned_waiting_for_backend_harness",
    }
    index_path = output_root / f"{args.backend}-jobs.json"
    note_path = output_root / f"{args.backend}-jobs.md"
    for job in jobs:
        job_path = Path(job["job_path"])
        job_path.parent.mkdir(parents=True, exist_ok=True)
        job_path.write_text(json.dumps(job, indent=2) + "\n", encoding="utf-8")
    index_path.write_text(json.dumps(job_index, indent=2) + "\n", encoding="utf-8")
    note_path.write_text(render_markdown(job_index), encoding="utf-8")
    print(
        "Built audio backend jobs from SPC index: "
        f"{len(jobs)} {args.backend} jobs, {len(skipped)} skipped -> {index_path}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
