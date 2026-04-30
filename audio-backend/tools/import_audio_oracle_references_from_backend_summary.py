#!/usr/bin/env python3
"""Import oracle reference captures from an audio backend result summary."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PLAN = ROOT / "manifests" / "audio-oracle-comparison-plan.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Import oracle references from backend results.")
    parser.add_argument("--plan", default=str(DEFAULT_PLAN), help="Oracle comparison plan JSON path.")
    parser.add_argument("--summary", required=True, help="Audio backend result summary JSON path.")
    parser.add_argument("--oracle-id", default="backend_summary_reference", help="Oracle id/name to record.")
    parser.add_argument("--notes", default="", help="Short import note.")
    parser.add_argument("--track-id", type=int, action="append", help="Specific track id to import. May repeat.")
    parser.add_argument("--overwrite", action="store_true", help="Replace existing planned reference outputs.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sha1_file(path: Path) -> str:
    digest = hashlib.sha1()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def resolve_repo_path(path_text: str) -> Path:
    path = Path(path_text)
    return path if path.is_absolute() else ROOT / path


def output_by_kind(result: dict[str, Any], kind: str) -> dict[str, Any] | None:
    for output in result.get("outputs", []):
        if output.get("kind") == kind:
            return output
    return None


def copy_checked(src: Path, dst: Path, *, overwrite: bool) -> None:
    if not src.exists():
        raise FileNotFoundError(f"source output does not exist: {src}")
    if dst.exists() and not overwrite:
        raise FileExistsError(f"refusing to overwrite existing reference output: {dst}")
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)


def planned_jobs_by_track(plan: dict[str, Any]) -> dict[int, dict[str, Any]]:
    return {int(job["track_id"]): job for job in plan.get("jobs", [])}


def summary_records_by_track(summary: dict[str, Any]) -> dict[int, dict[str, Any]]:
    return {
        int(record["track_id"]): record
        for record in summary.get("results", [])
        if record.get("status") == "ok" and record.get("valid") is True
    }


def import_track(
    *,
    job: dict[str, Any],
    summary_record: dict[str, Any],
    oracle_id: str,
    notes: str,
    overwrite: bool,
) -> dict[str, Any]:
    result = load_json(resolve_repo_path(summary_record["result_path"]))
    spc = output_by_kind(result, "complete_spc_snapshot")
    wav = output_by_kind(result, "rendered_wav")
    if not spc or not wav:
        raise ValueError(f"{summary_record['job_id']}: result lacks complete_spc_snapshot or rendered_wav")

    outputs = job["reference_capture_outputs"]
    src_spc = resolve_repo_path(str(spc["path"]))
    src_wav = resolve_repo_path(str(wav["path"]))
    dst_spc = resolve_repo_path(outputs["spc_snapshot"])
    dst_wav = resolve_repo_path(outputs["pcm_wav"])
    dst_metadata = resolve_repo_path(outputs["capture_metadata"])

    copy_checked(src_spc, dst_spc, overwrite=overwrite)
    copy_checked(src_wav, dst_wav, overwrite=overwrite)
    if dst_metadata.exists() and not overwrite:
        raise FileExistsError(f"refusing to overwrite existing reference metadata: {dst_metadata}")

    metadata = {
        "schema": "earthbound-decomp.audio-oracle-reference-capture.v1",
        "job_id": job["job_id"],
        "track_id": job["track_id"],
        "track_name": job["track_name"],
        "oracle_id": oracle_id,
        "oracle_kind": "backend_result_summary_import",
        "independent_emulator_capture": False,
        "notes": notes,
        "source_backend_result": {
            "job_id": summary_record["job_id"],
            "result_path": summary_record["result_path"],
            "backend_id": summary_record.get("backend_id"),
            "backend_version": summary_record.get("backend_version"),
        },
        "source_inputs": {
            "spc": str(src_spc),
            "wav": str(src_wav),
        },
        "imported_outputs": {
            "spc_snapshot": {
                "path": outputs["spc_snapshot"],
                "bytes": dst_spc.stat().st_size,
                "sha1": sha1_file(dst_spc),
            },
            "pcm_wav": {
                "path": outputs["pcm_wav"],
                "bytes": dst_wav.stat().st_size,
                "sha1": sha1_file(dst_wav),
            },
        },
        "distribution_policy": "generated_from_user_provided_rom_or_reference_emulator_output_do_not_commit",
    }
    dst_metadata.parent.mkdir(parents=True, exist_ok=True)
    dst_metadata.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    return {
        "track_id": job["track_id"],
        "track_name": job["track_name"],
        "capture_metadata": outputs["capture_metadata"],
    }


def main() -> int:
    args = parse_args()
    plan = load_json(Path(args.plan))
    summary = load_json(Path(args.summary))
    planned = planned_jobs_by_track(plan)
    summary_records = summary_records_by_track(summary)
    wanted = set(args.track_id or planned.keys())
    missing_plan = wanted - set(planned)
    if missing_plan:
        raise ValueError(f"requested tracks are not in oracle plan: {sorted(missing_plan)}")
    missing_summary = wanted - set(summary_records)
    if missing_summary:
        raise ValueError(f"requested tracks are missing valid backend results: {sorted(missing_summary)}")

    imported = [
        import_track(
            job=planned[track_id],
            summary_record=summary_records[track_id],
            oracle_id=args.oracle_id,
            notes=args.notes,
            overwrite=args.overwrite,
        )
        for track_id in sorted(wanted)
    ]
    print(f"Imported {len(imported)} oracle references from backend summary")
    for record in imported:
        print(f"- {record['track_id']:03d} {record['track_name']}: {record['capture_metadata']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
