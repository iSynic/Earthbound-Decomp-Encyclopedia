#!/usr/bin/env python3
"""Validate the audio SPC state frontier manifest."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_FRONTIER = ROOT / "manifests" / "audio-spc-state-frontier.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate the audio SPC state frontier manifest.")
    parser.add_argument("frontier", nargs="?", default=str(DEFAULT_FRONTIER))
    return parser.parse_args()


def validate(frontier: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if frontier.get("schema") != "earthbound-decomp.audio-spc-state-frontier.v1":
        errors.append(f"unexpected schema: {frontier.get('schema')}")

    summary = frontier.get("contract_summary", {})
    if int(summary.get("pack_count", 0)) <= 0:
        errors.append("contract summary has no audio packs")
    if int(summary.get("track_count", 0)) <= 0:
        errors.append("contract summary has no tracks")

    known_fields = {item.get("field") for item in frontier.get("known_state", [])}
    for required in ("apu_ram", "cold_start_bootstrap", "post_load_track_command"):
        if required not in known_fields:
            errors.append(f"missing known state field {required}")

    missing_fields = {item.get("field") for item in frontier.get("missing_state", [])}
    for required in ("spc700_registers", "dsp_registers", "apu_control_timer_state"):
        if required not in missing_fields:
            errors.append(f"missing required frontier gap {required}")

    gates = {item.get("gate"): item for item in frontier.get("renderer_gates", [])}
    if gates.get("diagnostic_apu_ram_seed", {}).get("status") != "open":
        errors.append("diagnostic_apu_ram_seed gate must be open")
    if "complete_spc_snapshot" not in gates:
        errors.append("missing complete_spc_snapshot gate")
    if "accurate_pcm_wav_export" not in gates:
        errors.append("missing accurate_pcm_wav_export gate")

    for item in frontier.get("evidence", []):
        if not item.get("exists"):
            errors.append(f"evidence path missing: {item.get('path')}")

    return errors


def main() -> int:
    args = parse_args()
    path = Path(args.frontier)
    frontier = json.loads(path.read_text(encoding="utf-8"))
    errors = validate(frontier)
    if errors:
        print("Audio SPC state frontier validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "Audio SPC state frontier validation OK: "
        f"{len(frontier['known_state'])} known fields, "
        f"{len(frontier['missing_state'])} missing fields, "
        f"{len(frontier['renderer_gates'])} renderer gates"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
