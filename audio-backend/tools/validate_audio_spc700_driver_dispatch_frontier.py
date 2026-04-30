#!/usr/bin/env python3
"""Validate the SPC700 driver dispatch frontier manifest."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MANIFEST = ROOT / "manifests" / "audio-spc700-driver-dispatch-frontier.json"
EXPECTED_COMMANDS = [f"0x{value:02X}" for value in range(0xE0, 0x100)]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate the audio SPC700 driver dispatch frontier.")
    parser.add_argument("manifest", nargs="?", default=str(DEFAULT_MANIFEST))
    return parser.parse_args()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def validate(data: dict[str, Any]) -> None:
    require(data.get("schema") == "earthbound-decomp.audio-spc700-driver-dispatch-frontier.v1", "unexpected schema")
    driver = data.get("driver", {})
    summary = data.get("summary", {})
    high = data.get("high_command_dispatch_candidate", {})
    entries = high.get("entries", [])
    ff = high.get("ff_dispatch_candidate", {})
    indirect = data.get("indirect_jump_candidates", [])

    require(driver.get("destination") == "0x0500", "driver block must load at $0500")
    require(int(driver.get("count", 0)) > 0, "driver block has no bytes")
    require(bool(driver.get("sha1")), "driver block missing sha1")
    require(summary.get("driver_base") == "0x0500", "unexpected driver base")
    require(summary.get("indirect_jump_opcode") == "0x1F", "unexpected indirect jump opcode")
    require(summary.get("unique_indirect_operands", 0) > 0, "missing indirect operands")
    require(summary.get("first_32_inside_table_candidates", 0) > 0, "missing pointer-table candidates")

    require(high.get("table_base") == "0x16C7", "unexpected high-command table base")
    require(high.get("entry_count") == 32, "high-command table must have 32 entries")
    require(entries and len(entries) == 32, "high-command entries missing")
    require([entry.get("command") for entry in entries] == EXPECTED_COMMANDS, "high-command entry range mismatch")
    require(entries[0].get("target") == "0x1833", "unexpected E0 target")
    require(entries[-1].get("command") == "0xFF", "last high-command entry is not FF")
    require(entries[-1].get("target") == "0x1A81", "unexpected FF target")
    require(ff.get("target") == "0x1A81", "FF dispatch candidate target mismatch")
    require(ff.get("semantic_status") == "driver_target_known_effect_unconfirmed", "FF should remain effect-pending")
    require(summary.get("ff_dispatch_target") == "0x1A81", "summary FF target mismatch")

    source_refs = set(high.get("source_indirect_jump_addresses", []))
    require("0x12FD" in source_refs, "missing $12FD source jump into high-command table")
    roles = {candidate.get("candidate_role") for candidate in indirect}
    require("likely_e0_ff_high_command_dispatch_table" in roles, "missing high-command indirect candidate")


def main() -> int:
    args = parse_args()
    path = Path(args.manifest)
    data = json.loads(path.read_text(encoding="utf-8"))
    validate(data)
    print(
        "Audio SPC700 driver dispatch frontier validation OK: "
        f"{data['summary']['unique_indirect_operands']} operands, "
        f"FF target {data['summary']['ff_dispatch_target']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
