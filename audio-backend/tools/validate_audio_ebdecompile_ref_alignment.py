#!/usr/bin/env python3
"""Validate eb-decompile audio reference alignment."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MANIFEST = ROOT / "manifests" / "audio-ebdecompile-ref-alignment.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate eb-decompile audio reference alignment.")
    parser.add_argument("manifest", nargs="?", default=str(DEFAULT_MANIFEST))
    return parser.parse_args()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def validate(data: dict[str, Any]) -> None:
    require(data.get("schema") == "earthbound-decomp.audio-ebdecompile-ref-alignment.v1", "unexpected schema")
    summary = data.get("summary", {})
    records = data.get("records", [])
    require(records, "missing records")
    require(summary.get("songs_yml_entries") == len(records), "record count mismatch")
    direct_ref_files = summary.get("direct_ref_song_files")
    direct_ref_matches = summary.get("direct_ref_payload_matches")
    require(isinstance(direct_ref_files, int) and direct_ref_files > 0, "expected direct ref files")
    require(isinstance(direct_ref_matches, int), "expected direct ref match count")
    require(0 <= direct_ref_matches <= direct_ref_files, "invalid direct ref match count")
    status_counts = summary.get("alignment_status_counts", {})
    require(status_counts, "missing status counts")
    require(sum(status_counts.values()) == len(records), "status counts do not sum to records")
    for record in records:
        require("track_id" in record, "record missing track id")
        require(record.get("alignment_status"), f"track {record.get('track_id')} missing alignment status")
        if record["alignment_status"] == "payload_matches_contract_sequence_block":
            require(record.get("matching_contract_blocks"), f"track {record['track_id']} missing contract block match")
            require(record.get("reference_song_path"), f"track {record['track_id']} missing reference path")


def main() -> int:
    args = parse_args()
    data = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    validate(data)
    print(
        "Audio eb-decompile reference alignment validation OK: "
        f"{data['summary']['direct_ref_payload_matches']} / "
        f"{data['summary']['direct_ref_song_files']} direct files match"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
