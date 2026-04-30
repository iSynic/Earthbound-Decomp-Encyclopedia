#!/usr/bin/env python3
"""Validate the diagnostic SPC snapshot index."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INDEX = ROOT / "build" / "audio" / "backend-jobs" / "diagnostic-spc-snapshots.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate generated diagnostic SPC snapshot metadata.")
    parser.add_argument("index", nargs="?", default=str(DEFAULT_INDEX), help="Snapshot index JSON path.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(index: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if index.get("schema") != "earthbound-decomp.audio-diagnostic-spc-snapshot-index.v1":
        errors.append(f"unexpected schema: {index.get('schema')}")
    if index.get("job_count", 0) <= 0:
        errors.append("job_count must be positive")
    if index.get("snapshot_count") != index.get("job_count"):
        errors.append(f"snapshot_count {index.get('snapshot_count')} != job_count {index.get('job_count')}")
    if index.get("missing_result_count") != 0:
        errors.append(f"missing_result_count is {index.get('missing_result_count')}")
    if index.get("missing_spc_output_count") != 0:
        errors.append(f"missing_spc_output_count is {index.get('missing_spc_output_count')}")
    if index.get("invalid_signature_count") != 0:
        errors.append(f"invalid_signature_count is {index.get('invalid_signature_count')}")

    for record in index.get("records", []):
        job_id = record.get("job_id", "<unknown>")
        snapshot = record.get("snapshot")
        if not snapshot:
            errors.append(f"{job_id}: missing snapshot metadata")
            continue
        if snapshot.get("bytes") != 0x10200:
            errors.append(f"{job_id}: unexpected SPC size {snapshot.get('bytes')}")
        if not snapshot.get("signature_ok"):
            errors.append(f"{job_id}: bad SPC signature")
        if not snapshot.get("declared_matches"):
            errors.append(f"{job_id}: declared output bytes/SHA-1 do not match file")
        if not snapshot.get("ram_sha1"):
            errors.append(f"{job_id}: missing RAM SHA-1")
        if not snapshot.get("dsp_register_sha1"):
            errors.append(f"{job_id}: missing DSP register SHA-1")
        if snapshot.get("dsp_nonzero_count") is None:
            errors.append(f"{job_id}: missing DSP nonzero count")
    return errors


def main() -> int:
    args = parse_args()
    index_path = Path(args.index)
    index = load_json(index_path)
    errors = validate(index)
    if errors:
        print("Diagnostic SPC snapshot validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "Diagnostic SPC snapshot validation OK: "
        f"{index['snapshot_count']} snapshots from {index['job_count']} jobs"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
