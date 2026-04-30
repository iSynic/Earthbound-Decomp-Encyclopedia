#!/usr/bin/env python3
"""Collect diagnostic SPC snapshot metadata from native audio backend results."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_JOBS = ROOT / "build" / "audio" / "backend-jobs" / "ares-jobs.json"
DEFAULT_OUTPUT = ROOT / "build" / "audio" / "backend-jobs" / "diagnostic-spc-snapshots.json"
SPC_SIGNATURE = b"SNES-SPC700 Sound File Data v0.30"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Collect generated diagnostic SPC snapshot metadata.")
    parser.add_argument("--jobs", default=str(DEFAULT_JOBS), help="Backend job index path.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Snapshot index JSON output path.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sha1(data: bytes) -> str:
    return hashlib.sha1(data).hexdigest()


def find_output(result: dict[str, Any], kind: str) -> dict[str, Any] | None:
    for output in result.get("outputs", []):
        if output.get("kind") == kind:
            return output
    return None


def parse_spc(path: Path) -> dict[str, Any]:
    data = path.read_bytes()
    ram = data[0x100:0x10100] if len(data) >= 0x10100 else b""
    dsp = data[0x10100:0x10180] if len(data) >= 0x10180 else b""
    signature_ok = data.startswith(SPC_SIGNATURE)
    return {
        "path": str(path),
        "bytes": len(data),
        "sha1": sha1(data),
        "signature_ok": signature_ok,
        "pc": f"0x{data[0x26]:02X}{data[0x25]:02X}" if len(data) > 0x26 else None,
        "a": f"0x{data[0x27]:02X}" if len(data) > 0x27 else None,
        "x": f"0x{data[0x28]:02X}" if len(data) > 0x28 else None,
        "y": f"0x{data[0x29]:02X}" if len(data) > 0x29 else None,
        "psw": f"0x{data[0x2A]:02X}" if len(data) > 0x2A else None,
        "sp": f"0x{data[0x2B]:02X}" if len(data) > 0x2B else None,
        "ram_sha1": sha1(ram) if len(ram) == 65536 else None,
        "dsp_register_sha1": sha1(dsp) if len(dsp) == 128 else None,
        "dsp_nonzero_count": sum(1 for byte in dsp if byte) if len(dsp) == 128 else None,
    }


def collect(jobs_path: Path) -> dict[str, Any]:
    index = load_json(jobs_path)
    records: list[dict[str, Any]] = []
    missing_results = 0
    missing_spc_outputs = 0
    invalid_signatures = 0

    for job in index.get("jobs", []):
        result_path = Path(job["result_path"])
        record: dict[str, Any] = {
            "job_id": job["job_id"],
            "track_id": job["track_id"],
            "track_name": job["track_name"],
            "result_path": str(result_path),
            "result_exists": result_path.exists(),
            "snapshot": None,
        }
        if not result_path.exists():
            missing_results += 1
            records.append(record)
            continue
        result = load_json(result_path)
        record["result_status"] = result.get("status")
        record["backend_version"] = result.get("backend_version")
        output = find_output(result, "complete_spc_snapshot")
        if output is None:
            missing_spc_outputs += 1
            records.append(record)
            continue
        spc_path = Path(output["path"])
        snapshot = parse_spc(spc_path)
        snapshot["declared_bytes"] = output.get("bytes")
        snapshot["declared_sha1"] = output.get("sha1")
        snapshot["declared_matches"] = (
            output.get("bytes") == snapshot["bytes"] and output.get("sha1") == snapshot["sha1"]
        )
        if not snapshot["signature_ok"]:
            invalid_signatures += 1
        record["snapshot"] = snapshot
        records.append(record)

    return {
        "schema": "earthbound-decomp.audio-diagnostic-spc-snapshot-index.v1",
        "job_index": str(jobs_path),
        "snapshot_kind": "diagnostic_complete_spc_snapshot",
        "faithfulness": "diagnostic_container_only_not_runtime_faithful",
        "job_count": len(records),
        "snapshot_count": sum(1 for record in records if record.get("snapshot")),
        "missing_result_count": missing_results,
        "missing_spc_output_count": missing_spc_outputs,
        "invalid_signature_count": invalid_signatures,
        "records": records,
    }


def main() -> int:
    args = parse_args()
    jobs_path = Path(args.jobs)
    output_path = Path(args.output)
    summary = collect(jobs_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(
        "Collected diagnostic SPC snapshots: "
        f"{summary['snapshot_count']} / {summary['job_count']} snapshots, "
        f"{summary['invalid_signature_count']} invalid signatures"
    )
    print(f"Wrote {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
