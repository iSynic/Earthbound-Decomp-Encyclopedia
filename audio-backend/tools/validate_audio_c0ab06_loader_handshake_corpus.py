#!/usr/bin/env python3
"""Validate the C0:AB06 LOAD_SPC700_DATA byte-level handshake corpus."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SUMMARY = ROOT / "build" / "audio" / "c0ab06-loader-handshake" / "c0ab06-loader-handshake-summary.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate C0:AB06 loader handshake corpus.")
    parser.add_argument("summary", nargs="?", default=str(DEFAULT_SUMMARY))
    return parser.parse_args()


def validate(summary: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if summary.get("schema") != "earthbound-decomp.c0ab06-loader-handshake-corpus.v1":
        errors.append(f"unexpected schema: {summary.get('schema')}")
    if summary.get("status") != "real_C0AB06_cpu_loader_executed_against_modeled_apuio_receiver":
        errors.append(f"unexpected status: {summary.get('status')}")
    if summary.get("setup_errors"):
        errors.append(f"setup errors present: {summary.get('setup_errors')}")
    if int(summary.get("mismatch_count", -1)) != 0:
        errors.append(f"mismatch_count is {summary.get('mismatch_count')}")
    if summary.get("mismatches"):
        errors.append(f"mismatches present: {len(summary.get('mismatches', []))}")

    unique_pack_count = int(summary.get("unique_pack_count", 0))
    executed_unique_pack_count = int(summary.get("executed_unique_pack_count", 0))
    stream_occurrence_count = int(summary.get("stream_occurrence_count", 0))
    matched_occurrence_count = int(summary.get("matched_occurrence_count", 0))
    if unique_pack_count <= 0:
        errors.append("unique_pack_count must be positive")
    if executed_unique_pack_count != unique_pack_count:
        errors.append(
            f"executed_unique_pack_count {executed_unique_pack_count} != unique_pack_count {unique_pack_count}"
        )
    if stream_occurrence_count <= 0:
        errors.append("stream_occurrence_count must be positive")
    if matched_occurrence_count != stream_occurrence_count:
        errors.append(
            f"matched_occurrence_count {matched_occurrence_count} != stream_occurrence_count {stream_occurrence_count}"
        )
    executed_apu_ram_match_count = int(summary.get("executed_apu_ram_match_count", -1))
    if executed_apu_ram_match_count != executed_unique_pack_count:
        errors.append(
            f"executed_apu_ram_match_count {executed_apu_ram_match_count} != executed_unique_pack_count {executed_unique_pack_count}"
        )

    handshakes = summary.get("handshakes", [])
    if len(handshakes) != executed_unique_pack_count:
        errors.append("handshake count does not match executed_unique_pack_count")
    for record in handshakes:
        pack_id = record.get("pack_id")
        handshake = record.get("handshake") or {}
        if int(record.get("returncode", -1)) != 0:
            errors.append(f"pack {pack_id}: returncode {record.get('returncode')}")
        if not handshake.get("ok"):
            errors.append(f"pack {pack_id}: handshake did not report ok")
        if handshake.get("final_pc") != "0x008004":
            errors.append(f"pack {pack_id}: final PC is {handshake.get('final_pc')}")
        if int(handshake.get("payload_bytes", 0)) <= 0:
            errors.append(f"pack {pack_id}: no payload bytes transferred")
        if int(handshake.get("block_start_tokens", 0)) <= 0:
            errors.append(f"pack {pack_id}: no block start tokens observed")
        if int(handshake.get("terminal_tokens", 0)) != 1:
            errors.append(f"pack {pack_id}: terminal token count is {handshake.get('terminal_tokens')}")
        expected_apu_ram = record.get("expected_apu_ram") or {}
        if expected_apu_ram.get("parse_status") != "ok":
            errors.append(f"pack {pack_id}: expected APU RAM stream parse status is {expected_apu_ram.get('parse_status')}")
        apu_ram = record.get("apu_ram") or {}
        if int(apu_ram.get("bytes", 0)) != 0x10000:
            errors.append(f"pack {pack_id}: APU RAM dump size is {apu_ram.get('bytes')}")
        if not apu_ram.get("matches_expected"):
            errors.append(f"pack {pack_id}: APU RAM dump does not match expected semantic reconstruction")
        if int(apu_ram.get("block_mismatch_count", -1)) != 0:
            errors.append(f"pack {pack_id}: APU RAM block mismatch count is {apu_ram.get('block_mismatch_count')}")
        if int(apu_ram.get("nonzero_count", -1)) != int(apu_ram.get("expected_nonzero_count", -2)):
            errors.append(f"pack {pack_id}: APU RAM nonzero count does not match expected")

    for occurrence in summary.get("occurrences", []):
        if not occurrence.get("matches_handshake"):
            errors.append(f"{occurrence.get('job_id')} pack {occurrence.get('pack_id')}: occurrence mismatch")
    totals = summary.get("totals") or {}
    if int(totals.get("selected_payload_blocks", 0)) <= 0 or int(totals.get("selected_payload_bytes", 0)) <= 0:
        errors.append("selected payload totals must be positive")
    if int(totals.get("executed_unique_apu_ram_matches", -1)) != executed_unique_pack_count:
        errors.append("executed_unique_apu_ram_matches does not match executed_unique_pack_count")
    return errors


def main() -> int:
    args = parse_args()
    summary = json.loads(Path(args.summary).read_text(encoding="utf-8"))
    errors = validate(summary)
    if errors:
        print("C0:AB06 loader handshake corpus validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "C0:AB06 loader handshake corpus validation OK: "
        f"{summary['matched_occurrence_count']} / {summary['stream_occurrence_count']} occurrences, "
        f"{summary['executed_unique_pack_count']} unique packs, "
        f"{summary['executed_apu_ram_match_count']} APU RAM matches"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
