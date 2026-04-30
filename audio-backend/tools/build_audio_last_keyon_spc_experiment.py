#!/usr/bin/env python3
"""Build an index of real last-key-on SPC snapshots from ares captures."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_JOBS = ROOT / "build" / "audio" / "backend-jobs" / "ares-jobs.json"
DEFAULT_OUT = ROOT / "build" / "audio" / "last-keyon-spc"
SPC_SIGNATURE = b"SNES-SPC700 Sound File Data v0.30"
DSP_OFFSET = 0x10100
DSP_KON = 0x4C
DSP_KOF = 0x5C


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build last-key-on SPC snapshot experiment metadata.")
    parser.add_argument("--jobs", default=str(DEFAULT_JOBS), help="Native ares backend job index.")
    parser.add_argument("--out", default=str(DEFAULT_OUT), help="Output directory for the experiment index.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sha1(data: bytes) -> str:
    return hashlib.sha1(data).hexdigest()


def snapshot_metadata(path: Path, data: bytes) -> dict[str, Any]:
    ram = data[0x100:0x10100] if len(data) >= 0x10100 else b""
    dsp = data[DSP_OFFSET:DSP_OFFSET + 128] if len(data) >= DSP_OFFSET + 128 else b""
    return {
        "path": str(path),
        "bytes": len(data),
        "sha1": sha1(data),
        "signature_ok": data.startswith(SPC_SIGNATURE),
        "pc": f"0x{data[0x26]:02X}{data[0x25]:02X}" if len(data) > 0x26 else None,
        "a": f"0x{data[0x27]:02X}" if len(data) > 0x27 else None,
        "x": f"0x{data[0x28]:02X}" if len(data) > 0x28 else None,
        "y": f"0x{data[0x29]:02X}" if len(data) > 0x29 else None,
        "psw": f"0x{data[0x2A]:02X}" if len(data) > 0x2A else None,
        "sp": f"0x{data[0x2B]:02X}" if len(data) > 0x2B else None,
        "ram_sha1": sha1(ram) if len(ram) == 65536 else None,
        "dsp_register_sha1": sha1(dsp) if len(dsp) == 128 else None,
        "dsp_nonzero_count": sum(1 for byte in dsp if byte) if len(dsp) == 128 else None,
        "kon": f"0x{data[DSP_OFFSET + DSP_KON]:02X}" if len(data) > DSP_OFFSET + DSP_KON else None,
        "kof": f"0x{data[DSP_OFFSET + DSP_KOF]:02X}" if len(data) > DSP_OFFSET + DSP_KOF else None,
    }


def safe_name(track_id: int, track_name: str) -> str:
    name = "".join(ch if ch.isalnum() or ch in "-_" else "_" for ch in track_name.lower())
    return f"track-{track_id:03d}-{name}"


def main() -> int:
    args = parse_args()
    jobs_path = Path(args.jobs).resolve()
    jobs_index = load_json(jobs_path)
    out_dir = Path(args.out).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    records: list[dict[str, Any]] = []
    missing_captures = 0
    missing_last_keyon = 0
    invalid_signatures = 0
    for job in jobs_index.get("jobs", []):
        capture_path = Path(job["output_dir"]) / "ares-state-capture.json"
        record: dict[str, Any] = {
            "job_id": job["job_id"],
            "track_id": job["track_id"],
            "track_name": job["track_name"],
            "capture_path": str(capture_path),
            "capture_exists": capture_path.exists(),
            "snapshot": None,
        }
        if not capture_path.exists():
            missing_captures += 1
            records.append(record)
            continue
        capture = load_json(capture_path)
        last_keyon = capture.get("spc700_entry_execution_probe", {}).get("last_key_on_snapshot", {})
        if not last_keyon.get("available"):
            missing_last_keyon += 1
            records.append(record)
            continue
        source_path = Path(last_keyon["path"])
        data = source_path.read_bytes()
        if not data.startswith(SPC_SIGNATURE):
            invalid_signatures += 1
        track_dir = out_dir / safe_name(int(job["track_id"]), str(job["track_name"]))
        track_dir.mkdir(parents=True, exist_ok=True)
        output_path = track_dir / "last-keyon.spc"
        shutil.copyfile(source_path, output_path)
        copied_data = output_path.read_bytes()
        snapshot = snapshot_metadata(output_path, copied_data)
        record.update(
            {
                "snapshot": snapshot,
                "source_snapshot_path": str(source_path),
                "source_snapshot_sha1": last_keyon.get("sha1"),
                "source_declared_matches": last_keyon.get("bytes") == snapshot["bytes"]
                and last_keyon.get("sha1") == snapshot["sha1"],
                "key_on_event_index": last_keyon.get("key_on_event_index"),
                "key_on_data": last_keyon.get("key_on_data"),
            }
        )
        records.append(record)

    index = {
        "schema": "earthbound-decomp.audio-last-keyon-spc-experiment.v1",
        "snapshot_kind": "diagnostic_last_keyon_spc_snapshot",
        "faithfulness": "diagnostic_harness_capture_at_last_nonzero_dsp_kon_write",
        "source_job_index": str(jobs_path),
        "job_count": len(records),
        "snapshot_count": sum(1 for record in records if record.get("snapshot")),
        "missing_capture_count": missing_captures,
        "missing_last_keyon_count": missing_last_keyon,
        "invalid_signature_count": invalid_signatures,
        "records": records,
    }
    output_index = out_dir / "last-keyon-spc-snapshots.json"
    output_index.write_text(json.dumps(index, indent=2) + "\n", encoding="utf-8")
    shutil.copyfile(output_index, out_dir / "diagnostic-spc-snapshots.json")
    print(
        "Built last-key-on SPC experiment: "
        f"{index['snapshot_count']} / {index['job_count']} snapshots, "
        f"{index['missing_last_keyon_count']} missing last-key-on captures"
    )
    print(f"Wrote {output_index}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
