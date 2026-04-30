#!/usr/bin/env python3
"""Join CHANGE_MUSIC load calls to the continuous real-driver C0:AB06 frontier."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_LOAD_STUB_METRICS = (
    ROOT
    / "build"
    / "audio"
    / "ares-wdc65816-full-change-music-load-stub-mailbox-smoke-jobs"
    / "change-music-load-stub-metrics.json"
)
DEFAULT_LOADER_CONTRACT = ROOT / "build" / "audio" / "c0ab06-loader" / "c0ab06-loader-contract.json"
DEFAULT_CONTINUOUS_FRONTIER = (
    ROOT
    / "build"
    / "audio"
    / "c0ab06-continuous-track-load-frontier"
    / "c0ab06-continuous-track-load-frontier.json"
)
DEFAULT_OUTPUT = (
    ROOT
    / "build"
    / "audio"
    / "change-music-continuous-sequence-contract"
    / "change-music-continuous-sequence-contract.json"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Collect CHANGE_MUSIC to continuous C0:AB06 sequence evidence.")
    parser.add_argument("--load-stub-metrics", default=str(DEFAULT_LOAD_STUB_METRICS))
    parser.add_argument("--loader-contract", default=str(DEFAULT_LOADER_CONTRACT))
    parser.add_argument("--continuous-frontier", default=str(DEFAULT_CONTINUOUS_FRONTIER))
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def norm_hex(text: Any, width: int) -> str:
    return f"0x{int(str(text), 16):0{width}X}"


def load_pair(item: dict[str, Any]) -> dict[str, str]:
    return {
        "a": norm_hex(item.get("a"), 4),
        "x": norm_hex(item.get("x"), 4),
    }


def sequence_pair(step: dict[str, Any]) -> dict[str, str]:
    return {
        "a": norm_hex(step.get("address"), 4),
        "x": norm_hex(step.get("bank"), 4),
    }


def by_job_id(records: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {str(record.get("job_id")): record for record in records}


def collect(load_stub: dict[str, Any], loader: dict[str, Any], continuous: dict[str, Any]) -> dict[str, Any]:
    loader_by_job = by_job_id(loader.get("records", []))
    continuous_by_job = by_job_id(continuous.get("records", []))
    records: list[dict[str, Any]] = []
    mismatches: list[str] = []

    for load_record in load_stub.get("records", []):
        job_id = str(load_record.get("job_id"))
        loader_record = loader_by_job.get(job_id)
        continuous_record = continuous_by_job.get(job_id)
        expected_loads = [item for item in load_record.get("expected_loads", []) if "error" not in item]
        change_music_pairs = [load_pair(item) for item in load_record.get("actual_load_args", [])]
        expected_pairs = [load_pair(item) for item in expected_loads]
        expected_pack_ids = [int(item["pack_id"]) for item in expected_loads]

        loader_pack_ids = []
        loader_matches_change_music = False
        if loader_record is not None:
            loader_pack_ids = [int(stream["pack_id"]) for stream in loader_record.get("streams", [])]
            loader_matches_change_music = (
                bool(loader_record.get("matches_load_apply_probe"))
                and loader_pack_ids == expected_pack_ids
            )

        continuous_pack_ids = []
        continuous_pairs: list[dict[str, str]] = []
        continuous_payload_regions_match = False
        continuous_steps_ok = False
        if continuous_record is not None:
            continuous_pack_ids = [int(pack_id) for pack_id in continuous_record.get("sequence_pack_ids", [])]
            handshake = continuous_record.get("handshake") or {}
            continuous_pairs = [sequence_pair(step) for step in handshake.get("sequence", [])]
            continuous_payload_regions_match = bool((continuous_record.get("payload_regions") or {}).get("payload_regions_match"))
            continuous_steps_ok = all(
                bool(step.get("ok")) and step.get("final_pc") == "0x008004"
                for step in handshake.get("sequence", [])
            )

        matches = {
            "change_music_calls_match_table": bool(load_record.get("matches_expected")) and change_music_pairs == expected_pairs,
            "loader_contract_matches_change_music_pack_ids": loader_matches_change_music,
            "continuous_frontier_matches_change_music_pack_ids": continuous_pack_ids == expected_pack_ids,
            "continuous_frontier_matches_change_music_pointer_args": continuous_pairs == expected_pairs,
            "continuous_frontier_payload_regions_match": continuous_payload_regions_match,
            "continuous_frontier_steps_return_to_loader_caller": continuous_steps_ok,
        }
        all_match = all(matches.values())
        if not all_match:
            mismatches.append(job_id)

        records.append(
            {
                "job_id": job_id,
                "track_id": int(load_record.get("track_id", 0)),
                "track_name": load_record.get("track_name"),
                "expected_pack_ids": expected_pack_ids,
                "change_music_pointer_args": change_music_pairs,
                "loader_contract_pack_ids": loader_pack_ids,
                "continuous_frontier_pack_ids": continuous_pack_ids,
                "continuous_frontier_pointer_args": continuous_pairs,
                "matches": matches,
                "all_match": all_match,
            }
        )

    match_count = sum(1 for record in records if record["all_match"])
    return {
        "schema": "earthbound-decomp.change-music-continuous-sequence-contract.v1",
        "status": "change_music_load_order_matches_continuous_real_driver_c0ab06_sequence",
        "source_policy": continuous.get("source_policy"),
        "load_stub_metrics": str(DEFAULT_LOAD_STUB_METRICS),
        "loader_contract": str(DEFAULT_LOADER_CONTRACT),
        "continuous_frontier": str(DEFAULT_CONTINUOUS_FRONTIER),
        "remaining_shortcut": "The continuous C0:AB06 run still receives the already-recorded CHANGE_MUSIC pack sequence from the harness; the next step is to execute CHANGE_MUSIC and invoke the real C0:AB06 loader in one combined run.",
        "job_count": len(records),
        "match_count": match_count,
        "mismatch_count": len(records) - match_count,
        "mismatches": mismatches,
        "records": records,
    }


def main() -> int:
    args = parse_args()
    load_stub = load_json(Path(args.load_stub_metrics))
    loader = load_json(Path(args.loader_contract))
    continuous = load_json(Path(args.continuous_frontier))
    result = collect(load_stub, loader, continuous)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(
        "Collected CHANGE_MUSIC continuous sequence contract: "
        f"{result['match_count']} / {result['job_count']} jobs matched"
    )
    print(f"Wrote {output}")
    return 0 if result["mismatch_count"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
