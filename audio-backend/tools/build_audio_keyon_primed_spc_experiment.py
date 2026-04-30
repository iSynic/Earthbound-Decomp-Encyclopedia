#!/usr/bin/env python3
"""Build key-on-primed diagnostic SPC variants.

This is an experiment, not a faithful state builder. It patches the generated
diagnostic SPC container's DSP KON register to the last observed key-on byte
from the ares probe and clears KOF. If libgme output improves, the result tells
us the next faithful capture boundary should land near real key-on activity.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SNAPSHOT_INDEX = ROOT / "build" / "audio" / "backend-jobs" / "diagnostic-spc-snapshots.json"
DEFAULT_CAPTURE_METRICS = ROOT / "build" / "audio" / "backend-jobs" / "ares-capture-metrics.json"
DEFAULT_OUT = ROOT / "build" / "audio" / "keyon-primed-spc"
SPC_SIGNATURE = b"SNES-SPC700 Sound File Data v0.30"
DSP_OFFSET = 0x10100
DSP_KON = 0x4C
DSP_KOF = 0x5C


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build key-on-primed diagnostic SPC variants.")
    parser.add_argument("--snapshots", default=str(DEFAULT_SNAPSHOT_INDEX), help="Diagnostic SPC snapshot index.")
    parser.add_argument("--capture-metrics", default=str(DEFAULT_CAPTURE_METRICS), help="ares capture metrics JSON.")
    parser.add_argument("--out", default=str(DEFAULT_OUT), help="Output directory.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sha1(data: bytes) -> str:
    return hashlib.sha1(data).hexdigest()


def parse_hex_byte(text: str | None) -> int:
    if not text:
        return 0
    return int(text, 16) & 0xFF


def safe_name(track_id: int, track_name: str) -> str:
    name = "".join(ch if ch.isalnum() or ch in "-_" else "_" for ch in track_name.lower())
    return f"track-{track_id:03d}-{name}"


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


def main() -> int:
    args = parse_args()
    snapshots_path = Path(args.snapshots).resolve()
    capture_metrics_path = Path(args.capture_metrics).resolve()
    snapshot_index = load_json(snapshots_path)
    capture_metrics = load_json(capture_metrics_path)
    capture_by_track = {int(record["track_id"]): record for record in capture_metrics.get("records", [])}
    out_dir = Path(args.out).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    records: list[dict[str, Any]] = []
    for record in snapshot_index.get("records", []):
        snapshot = record.get("snapshot")
        if not snapshot:
            continue
        track_id = int(record["track_id"])
        track_name = str(record["track_name"])
        capture = capture_by_track.get(track_id, {})
        last_kon = parse_hex_byte(capture.get("dsp_last_key_on_data"))
        source_path = Path(snapshot["path"])
        data = bytearray(source_path.read_bytes())
        if not data.startswith(SPC_SIGNATURE):
            raise ValueError(f"bad SPC signature: {source_path}")
        original_kon = data[DSP_OFFSET + DSP_KON]
        original_kof = data[DSP_OFFSET + DSP_KOF]
        data[DSP_OFFSET + DSP_KON] = last_kon
        data[DSP_OFFSET + DSP_KOF] = 0
        track_dir = out_dir / safe_name(track_id, track_name)
        track_dir.mkdir(parents=True, exist_ok=True)
        output_path = track_dir / "keyon-primed.spc"
        output_path.write_bytes(data)
        records.append(
            {
                "job_id": record["job_id"],
                "track_id": track_id,
                "track_name": track_name,
                "source_snapshot_path": str(source_path),
                "source_snapshot_sha1": snapshot["sha1"],
                "patch": {
                    "source": "last observed ares diagnostic DSP key-on byte",
                    "original_kon": f"0x{original_kon:02X}",
                    "primed_kon": f"0x{last_kon:02X}",
                    "original_kof": f"0x{original_kof:02X}",
                    "primed_kof": "0x00",
                    "key_on_event_count": int(capture.get("dsp_key_on_event_count", 0)),
                    "key_off_event_count": int(capture.get("dsp_key_off_event_count", 0)),
                },
                "snapshot": snapshot_metadata(output_path, bytes(data)),
            }
        )

    index = {
        "schema": "earthbound-decomp.audio-keyon-primed-spc-experiment.v1",
        "snapshot_kind": "keyon_primed_diagnostic_spc_snapshot",
        "faithfulness": "experiment_only_not_runtime_faithful",
        "source_snapshot_index": str(snapshots_path),
        "source_capture_metrics": str(capture_metrics_path),
        "job_count": len(records),
        "snapshot_count": len(records),
        "records": records,
    }
    output_index = out_dir / "keyon-primed-spc-snapshots.json"
    output_index.write_text(json.dumps(index, indent=2) + "\n", encoding="utf-8")
    shutil.copyfile(output_index, out_dir / "diagnostic-spc-snapshots.json")
    print(f"Built key-on-primed SPC experiment: {len(records)} snapshots")
    print(f"Wrote {output_index}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
