#!/usr/bin/env python3
"""Validate C0:AB06 real ares SMP IPL receiver frontier evidence."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_FRONTIER = ROOT / "build" / "audio" / "c0ab06-real-ipl-frontier" / "c0ab06-real-ipl-frontier.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate C0:AB06 real-IPL receiver frontier evidence.")
    parser.add_argument("frontier", nargs="?", default=str(DEFAULT_FRONTIER))
    return parser.parse_args()


def validate(frontier: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if frontier.get("schema") != "earthbound-decomp.c0ab06-real-ipl-frontier.v1":
        errors.append(f"unexpected schema: {frontier.get('schema')}")
    if frontier.get("status") != "real_ares_smp_ipl_receiver_executes_c0ab06_stream_payloads":
        errors.append(f"unexpected status: {frontier.get('status')}")
    if frontier.get("setup_errors"):
        errors.append(f"setup errors present: {frontier.get('setup_errors')}")
    unique_pack_count = int(frontier.get("unique_pack_count", 0))
    executed_unique_pack_count = int(frontier.get("executed_unique_pack_count", 0))
    payload_region_match_count = int(frontier.get("payload_region_match_count", 0))
    if unique_pack_count <= 0:
        errors.append("unique_pack_count must be positive")
    if executed_unique_pack_count != unique_pack_count:
        errors.append("executed_unique_pack_count does not match unique_pack_count")
    if payload_region_match_count != executed_unique_pack_count:
        errors.append("payload_region_match_count does not match executed_unique_pack_count")
    if int(frontier.get("mismatch_count", -1)) != 0:
        errors.append(f"mismatch_count is {frontier.get('mismatch_count')}")

    for record in frontier.get("records", []):
        pack_id = record.get("pack_id")
        if int(record.get("returncode", -1)) != 0:
            errors.append(f"pack {pack_id}: returncode {record.get('returncode')}")
        handshake = record.get("handshake") or {}
        if handshake.get("receiver") != "ares_smp_ipl":
            errors.append(f"pack {pack_id}: receiver is {handshake.get('receiver')}")
        if not handshake.get("smp_boot_signature_observed"):
            errors.append(f"pack {pack_id}: SMP IPL boot signature not observed")
        if int(handshake.get("terminal_tokens", 0)) != 1:
            errors.append(f"pack {pack_id}: terminal token count is {handshake.get('terminal_tokens')}")
        payload_regions = record.get("payload_regions") or {}
        if not payload_regions.get("payload_regions_match"):
            errors.append(f"pack {pack_id}: payload regions do not match")
        if int(payload_regions.get("payload_region_mismatch_count", -1)) != 0:
            errors.append(f"pack {pack_id}: payload region mismatch count is {payload_regions.get('payload_region_mismatch_count')}")
        if int(payload_regions.get("bytes", 0)) != 0x10000:
            errors.append(f"pack {pack_id}: APU RAM dump size is {payload_regions.get('bytes')}")

    bootstrap = frontier.get("bootstrap_return") or {}
    if not bootstrap.get("fully_returned_to_cpu"):
        errors.append("bootstrap pack 1 did not fully return to the CPU")
    bootstrap_handshake = bootstrap.get("handshake") or {}
    if bootstrap_handshake.get("final_pc") != "0x008004":
        errors.append(f"bootstrap final PC is {bootstrap_handshake.get('final_pc')}")
    if bootstrap_handshake.get("smp_final_pc") is None:
        errors.append("bootstrap missing SMP final PC")
    return errors


def main() -> int:
    args = parse_args()
    frontier = json.loads(Path(args.frontier).read_text(encoding="utf-8"))
    errors = validate(frontier)
    if errors:
        print("C0:AB06 real-IPL frontier validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "C0:AB06 real-IPL frontier validation OK: "
        f"{frontier['payload_region_match_count']} / {frontier['executed_unique_pack_count']} unique packs, "
        "bootstrap return OK"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
