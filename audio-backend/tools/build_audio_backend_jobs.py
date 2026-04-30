#!/usr/bin/env python3
"""Build ignored backend job manifests from renderer fixtures."""

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


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_FIXTURES = ROOT / "build" / "audio" / "renderer-fixtures" / "audio-renderer-fixtures.json"
DEFAULT_OUT = ROOT / "build" / "audio" / "backend-jobs"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build audio backend job manifests from renderer fixtures.")
    parser.add_argument("--fixtures", default=str(DEFAULT_FIXTURES), help="Renderer fixture index path.")
    parser.add_argument("--backend", default="ares", choices=["ares", "snes_spc", "external_reference"])
    parser.add_argument("--out", default=str(DEFAULT_OUT), help="Ignored backend job output directory.")
    parser.add_argument("--seconds", type=float, default=30.0)
    parser.add_argument("--fade-seconds", type=float, default=5.0)
    parser.add_argument("--sample-rate", type=int, default=32000)
    parser.add_argument("--channels", type=int, default=2)
    parser.add_argument("--format", default="wav", choices=["wav", "pcm"])
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expected_outputs_for_backend(backend_id: str, output_format: str) -> tuple[str, ...]:
    if backend_id == "ares":
        return ("state_capture_json", f"rendered_{output_format}", "render_hash_json")
    if backend_id == "snes_spc":
        return ("complete_spc_snapshot", f"rendered_{output_format}", "render_hash_json")
    return ("reference_capture_json", f"rendered_{output_format}", "render_hash_json")


def build_job_record(
    fixture_record: dict[str, Any],
    backend_id: str,
    output_root: Path,
    options: AudioRenderOptions,
) -> dict[str, Any]:
    track_id = int(fixture_record["track_id"])
    track_name = str(fixture_record["track_name"]).lower()
    safe_name = "".join(ch if ch.isalnum() or ch in "-_" else "_" for ch in track_name)
    job_id = f"{backend_id}-track-{track_id:03d}-{safe_name}"
    output_dir = output_root / job_id
    fixture_path = Path(fixture_record["fixture_path"])
    job = AudioBackendJob(
        job_id=job_id,
        backend_id=backend_id,
        fixture_path=fixture_path,
        output_dir=output_dir,
        render_options=options,
        expected_outputs=expected_outputs_for_backend(backend_id, options.output_format),
    )
    record = backend_job_to_dict(job)
    record["track_id"] = track_id
    record["track_name"] = fixture_record["track_name"]
    record["input_apu_ram_sha1"] = fixture_record["apu_ram_sha1"]
    record["input_load_mode"] = fixture_record["load_mode"]
    record["status"] = "planned_waiting_for_backend_harness"
    record["result_schema"] = "earthbound-decomp.audio-backend-result.v1"
    record["result_path"] = str(output_dir / "result.json")
    record["job_path"] = str(output_dir / "job.json")
    return record


def render_markdown(job_index: dict[str, Any]) -> str:
    rows = [
        "| `{job_id}` | {track_id} | `{track_name}` | `{backend}` | `{status}` | `{job_path}` | `{outputs}` |".format(
            job_id=job["job_id"],
            track_id=job["track_id"],
            track_name=job["track_name"],
            backend=job["backend_id"],
            status=job["status"],
            job_path=job["job_path"],
            outputs=", ".join(job["expected_outputs"]),
        )
        for job in job_index["jobs"]
    ]
    backend_rows = [
        "| `{id}` | {license} | {policy} | {implemented} |".format(
            id=backend["id"],
            license=backend["license_policy"],
            policy=backend["execution_policy"],
            implemented=backend["implemented"],
        )
        for backend in job_index["backend_catalog"]
    ]
    return "\n".join(
        [
            "# Audio Backend Job Queue",
            "",
            "Status: generated local job queue for external renderer/backend prototypes.",
            "",
            "These jobs are not render results. They describe the exact fixture input and output contract an ares, snes_spc, or reference backend must satisfy. Generated job files and any WAV/SPC/PCM outputs stay under ignored `build/audio`.",
            "",
            "## Backend Catalog",
            "",
            "| Backend | License policy | Execution policy | Implemented |",
            "| --- | --- | --- | --- |",
            *backend_rows,
            "",
            "## Jobs",
            "",
            "| Job | Track | Name | Backend | Status | Job path | Expected outputs |",
            "| --- | ---: | --- | --- | --- | --- | --- |",
            *rows,
            "",
            "## Result Contract",
            "",
            "Each backend result should write `result.json` with schema `earthbound-decomp.audio-backend-result.v1`, the input `job_id`, output paths, hashes, backend version/build metadata, and whether the output is a complete SPC snapshot, rendered PCM/WAV, or reference capture.",
            "",
        ]
    )


def main() -> int:
    args = parse_args()
    fixture_index_path = Path(args.fixtures)
    fixture_index = load_json(fixture_index_path)
    output_root = Path(args.out)
    output_root.mkdir(parents=True, exist_ok=True)
    options = AudioRenderOptions(
        seconds=args.seconds,
        fade_seconds=args.fade_seconds,
        sample_rate=args.sample_rate,
        channels=args.channels,
        output_format=args.format,
    )
    jobs = [
        build_job_record(record, args.backend, output_root, options)
        for record in fixture_index.get("fixtures", [])
    ]
    job_index = {
        "schema": "earthbound-decomp.audio-backend-job-index.v1",
        "fixture_index": str(fixture_index_path),
        "backend_id": args.backend,
        "job_count": len(jobs),
        "jobs": jobs,
        "backend_catalog": describe_renderer_backends(),
        "source_policy": fixture_index["source_policy"],
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
    print(f"Built audio backend jobs: {len(jobs)} {args.backend} jobs -> {index_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
