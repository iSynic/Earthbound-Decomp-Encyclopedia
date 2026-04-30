#!/usr/bin/env python3
"""Populate oracle reference slots from the current fused playback/export outputs.

This is a comparator self-check, not an independent emulator oracle. It copies
the source SPC/WAV artifacts from the oracle plan into the planned reference
locations so the collector must classify the corpus as exact pass.
"""

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
    parser = argparse.ArgumentParser(description="Populate audio oracle reference slots with self-reference artifacts.")
    parser.add_argument("--plan", default=str(DEFAULT_PLAN), help="Oracle comparison plan JSON path.")
    parser.add_argument("--track-id", type=int, action="append", help="Specific planned track id to populate. May repeat.")
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


def copy_checked(src: Path, dst: Path, *, overwrite: bool) -> None:
    if not src.exists():
        raise FileNotFoundError(f"source artifact does not exist: {src}")
    if dst.exists() and not overwrite:
        raise FileExistsError(f"refusing to overwrite existing reference output: {dst}")
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)


def selected_jobs(plan: dict[str, Any], track_ids: list[int] | None) -> list[dict[str, Any]]:
    wanted = set(track_ids or [])
    jobs = [job for job in plan.get("jobs", []) if not wanted or int(job["track_id"]) in wanted]
    found = {int(job["track_id"]) for job in jobs}
    missing = wanted - found
    if missing:
        raise ValueError(f"requested track ids are not in the oracle plan: {sorted(missing)}")
    return jobs


def populate_job(job: dict[str, Any], *, overwrite: bool) -> dict[str, Any]:
    outputs = job["reference_capture_outputs"]
    src_spc = resolve_repo_path(job["source_spc"]["path"])
    src_wav = resolve_repo_path(job["source_render"]["path"])
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
        "oracle_id": "ares_fusion_self_reference",
        "oracle_kind": "self_reference_comparator_smoke",
        "independent_emulator_capture": False,
        "notes": "Comparator smoke test: planned reference outputs are exact copies of current fused playback/export artifacts.",
        "source_inputs": {
            "spc": job["source_spc"]["path"],
            "wav": job["source_render"]["path"],
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
        "distribution_policy": "generated_from_user_provided_rom_do_not_commit",
    }
    dst_metadata.parent.mkdir(parents=True, exist_ok=True)
    dst_metadata.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    return {
        "job_id": job["job_id"],
        "track_id": job["track_id"],
        "track_name": job["track_name"],
        "spc_snapshot": outputs["spc_snapshot"],
        "pcm_wav": outputs["pcm_wav"],
        "capture_metadata": outputs["capture_metadata"],
    }


def main() -> int:
    args = parse_args()
    plan = load_json(Path(args.plan))
    populated = [populate_job(job, overwrite=args.overwrite) for job in selected_jobs(plan, args.track_id)]
    print(f"Populated {len(populated)} self-reference oracle captures")
    for record in populated:
        print(f"- {record['track_id']:03d} {record['track_name']}: {record['capture_metadata']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
