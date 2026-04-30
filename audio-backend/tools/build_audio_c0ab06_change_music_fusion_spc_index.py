#!/usr/bin/env python3
"""Build a snes_spc-compatible index from fused CHANGE_MUSIC/C0:AB06 snapshots."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_FRONTIER = (
    ROOT
    / "build"
    / "audio"
    / "c0ab06-change-music-fusion-frontier"
    / "c0ab06-change-music-fusion-frontier.json"
)
DEFAULT_OUTPUT = (
    ROOT
    / "build"
    / "audio"
    / "c0ab06-change-music-fusion-spc"
    / "c0ab06-change-music-fusion-spc-snapshots.json"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build fused CHANGE_MUSIC/C0:AB06 SPC snapshot index.")
    parser.add_argument("--frontier", default=str(DEFAULT_FRONTIER), help="Fusion frontier JSON.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Snapshot index output JSON.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def absolutize(path_text: str, *, base: Path) -> str:
    path = Path(path_text)
    if not path.is_absolute():
        path = base / path
    return str(path.resolve())


def main() -> int:
    args = parse_args()
    frontier_path = Path(args.frontier).resolve()
    frontier = load_json(frontier_path)
    records: list[dict[str, Any]] = []
    missing_snapshot_count = 0
    invalid_signature_count = 0
    for record in frontier.get("records", []):
        snapshot = record.get("snapshot")
        normalized_snapshot = dict(snapshot) if snapshot else None
        if normalized_snapshot and normalized_snapshot.get("path"):
            normalized_snapshot["path"] = absolutize(str(normalized_snapshot["path"]), base=ROOT)
        if not snapshot:
            missing_snapshot_count += 1
        elif not snapshot.get("signature_ok"):
            invalid_signature_count += 1
        records.append(
            {
                "job_id": record["job_id"],
                "track_id": int(record["track_id"]),
                "track_name": record["track_name"],
                "capture_path": str(frontier_path),
                "capture_exists": frontier_path.exists(),
                "snapshot": normalized_snapshot,
                "smoke": {
                    "reached_key_on_after_ack": bool((record.get("handshake") or {}).get("change_music", {}).get("reached_key_on_after_ack")),
                    "source_frontier_status": frontier.get("status"),
                },
            }
        )

    index = {
        "schema": "earthbound-decomp.audio-ares-smp-mailbox-spc-index.v1",
        "snapshot_kind": "c0ab06_change_music_fusion_last_keyon_spc_snapshot",
        "faithfulness": "full_change_music_invokes_real_c0ab06_against_live_driver_then_captures_last_keyon",
        "source_summary": str(frontier_path),
        "job_count": len(records),
        "snapshot_count": sum(1 for record in records if record.get("snapshot")),
        "missing_snapshot_count": missing_snapshot_count,
        "invalid_signature_count": invalid_signature_count,
        "records": records,
    }
    output_path = Path(args.output).resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(index, indent=2) + "\n", encoding="utf-8")
    diagnostic_alias = output_path.parent / "diagnostic-spc-snapshots.json"
    diagnostic_alias.write_text(json.dumps(index, indent=2) + "\n", encoding="utf-8")
    print(
        "Built fused CHANGE_MUSIC/C0:AB06 SPC index: "
        f"{index['snapshot_count']} / {index['job_count']} snapshots"
    )
    print(f"Wrote {output_path}")
    print(f"Wrote {diagnostic_alias}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
