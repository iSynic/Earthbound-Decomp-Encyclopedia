#!/usr/bin/env python3
"""Import externally captured audio oracle reference files into planned paths."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PLAN = ROOT / "manifests" / "audio-oracle-comparison-plan.json"
SPC_SIGNATURE = b"SNES-SPC700 Sound File Data"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Import one audio oracle reference capture.")
    parser.add_argument("--plan", default=str(DEFAULT_PLAN), help="Oracle comparison plan JSON path.")
    parser.add_argument("--track-id", type=int, required=True, help="Music table track id to import.")
    parser.add_argument("--spc", required=True, help="Reference SPC snapshot captured by the oracle emulator.")
    parser.add_argument("--wav", required=True, help="Reference WAV/PCM render captured or exported by the oracle emulator.")
    parser.add_argument("--oracle-id", default="external_reference", help="Reference oracle id/name.")
    parser.add_argument("--notes", default="", help="Short capture note.")
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Replace an existing reference capture for this planned track.",
    )
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


def find_job(plan: dict[str, Any], track_id: int) -> dict[str, Any]:
    for job in plan.get("jobs", []):
        if int(job.get("track_id", -1)) == track_id:
            return job
    raise ValueError(f"track id {track_id} is not in oracle comparison plan")


def require_input(path: Path, label: str) -> None:
    if not path.exists():
        raise FileNotFoundError(f"{label} does not exist: {path}")
    if not path.is_file():
        raise ValueError(f"{label} is not a file: {path}")


def validate_spc(path: Path) -> None:
    with path.open("rb") as stream:
        header = stream.read(len(SPC_SIGNATURE))
    if not header.startswith(SPC_SIGNATURE):
        raise ValueError(f"reference SPC is missing SNES-SPC700 signature: {path}")


def validate_wav(path: Path) -> None:
    with path.open("rb") as stream:
        header = stream.read(12)
    if header[0:4] != b"RIFF" or header[8:12] != b"WAVE":
        raise ValueError(f"reference WAV is missing RIFF/WAVE header: {path}")


def copy_checked(src: Path, dst: Path, *, overwrite: bool) -> None:
    if dst.exists() and not overwrite:
        raise FileExistsError(f"refusing to overwrite existing reference output: {dst}")
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)


def main() -> int:
    args = parse_args()
    plan_path = Path(args.plan)
    plan = load_json(plan_path)
    job = find_job(plan, args.track_id)
    outputs = job["reference_capture_outputs"]

    src_spc = Path(args.spc)
    src_wav = Path(args.wav)
    require_input(src_spc, "reference SPC")
    require_input(src_wav, "reference WAV")
    validate_spc(src_spc)
    validate_wav(src_wav)

    dst_spc = resolve_repo_path(outputs["spc_snapshot"])
    dst_wav = resolve_repo_path(outputs["pcm_wav"])
    dst_metadata = resolve_repo_path(outputs["capture_metadata"])
    copy_checked(src_spc, dst_spc, overwrite=args.overwrite)
    copy_checked(src_wav, dst_wav, overwrite=args.overwrite)

    metadata = {
        "schema": "earthbound-decomp.audio-oracle-reference-capture.v1",
        "job_id": job["job_id"],
        "track_id": job["track_id"],
        "track_name": job["track_name"],
        "oracle_id": args.oracle_id,
        "notes": args.notes,
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
    if dst_metadata.exists() and not args.overwrite:
        raise FileExistsError(f"refusing to overwrite existing reference metadata: {dst_metadata}")
    dst_metadata.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    print(f"Imported oracle reference capture for track {args.track_id:03d} -> {dst_metadata}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
