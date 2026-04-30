#!/usr/bin/env python3
"""Collect CHANGE_MUSIC load-path stub metrics from the ares smoke corpus."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SUMMARY = ROOT / "build" / "audio" / "ares-wdc65816-full-change-music-load-stub-mailbox-smoke-jobs" / "smp-mailbox-smoke-summary.json"
DEFAULT_DATASET = ROOT / "build" / "audio" / "cpu-routine-fixtures" / "c4-f70a-music-dataset-table.bin"
DEFAULT_POINTERS = ROOT / "build" / "audio" / "cpu-routine-fixtures" / "c4-f947-music-pack-pointer-table.bin"
DEFAULT_OUTPUT = ROOT / "build" / "audio" / "ares-wdc65816-full-change-music-load-stub-mailbox-smoke-jobs" / "change-music-load-stub-metrics.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Collect CHANGE_MUSIC load-stub metrics.")
    parser.add_argument("--summary", default=str(DEFAULT_SUMMARY), help="Load-stub smoke summary JSON.")
    parser.add_argument("--music-dataset", default=str(DEFAULT_DATASET), help="ROM-derived MusicDatasetTable fixture.")
    parser.add_argument("--music-pack-pointers", default=str(DEFAULT_POINTERS), help="ROM-derived MusicPackPointerTable fixture.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Metrics JSON output.")
    return parser.parse_args()


def expected_args(track_id: int, dataset: bytes, pointers: bytes) -> list[dict[str, Any]]:
    row_offset = (track_id - 1) * 3
    if row_offset < 0 or row_offset + 2 >= len(dataset):
        return []

    expected: list[dict[str, Any]] = []
    for role, pack_id in zip(("primary", "secondary", "sequence"), dataset[row_offset:row_offset + 3], strict=True):
        if pack_id == 0xFF:
            continue
        pointer_offset = pack_id * 3
        if pointer_offset + 2 >= len(pointers):
            expected.append({
                "role": role,
                "pack_id": pack_id,
                "error": "pack pointer outside fixture",
            })
            continue
        bank = pointers[pointer_offset]
        address = pointers[pointer_offset + 1] | (pointers[pointer_offset + 2] << 8)
        expected.append({
            "role": role,
            "pack_id": pack_id,
            "a": f"0x{address:04X}",
            "x": f"0x{bank:04X}",
        })
    return expected


def collect(summary: dict[str, Any], dataset: bytes, pointers: bytes, *, source_summary: Path) -> dict[str, Any]:
    records: list[dict[str, Any]] = []
    mismatches: list[str] = []
    call_counts: dict[str, int] = {}

    for record in summary.get("records", []):
        job_id = str(record.get("job_id", ""))
        track_id = int(record.get("track_id", 0))
        probe = (record.get("smoke", {}) or {}).get("cpu_instruction_probe", {}) or {}
        actual = list(probe.get("load_spc700_data_stub_args", []))
        expected = expected_args(track_id, dataset, pointers)
        expected_pairs = [{"a": item.get("a"), "x": item.get("x")} for item in expected if "error" not in item]
        call_count = int(probe.get("load_spc700_data_stub_calls", 0))
        call_counts[str(call_count)] = call_counts.get(str(call_count), 0) + 1
        match = actual == expected_pairs
        if not match:
            mismatches.append(job_id)
        records.append({
            "job_id": job_id,
            "track_id": track_id,
            "track_name": record.get("track_name"),
            "call_count": call_count,
            "expected_call_count": len(expected_pairs),
            "expected_loads": expected,
            "actual_load_args": actual,
            "matches_expected": match,
        })

    return {
        "schema": "earthbound-decomp.change-music-load-stub-metrics.v1",
        "source_summary": str(source_summary),
        "job_count": len(records),
        "call_count_distribution": call_counts,
        "mismatch_count": len(mismatches),
        "mismatches": mismatches,
        "records": records,
    }


def main() -> int:
    args = parse_args()
    summary_path = Path(args.summary)
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    dataset = Path(args.music_dataset).read_bytes()
    pointers = Path(args.music_pack_pointers).read_bytes()
    metrics = collect(summary, dataset, pointers, source_summary=summary_path)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")
    print(
        "Collected CHANGE_MUSIC load-stub metrics: "
        f"{metrics['job_count']} jobs, {metrics['mismatch_count']} mismatches, "
        f"call counts {metrics['call_count_distribution']}"
    )
    print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
