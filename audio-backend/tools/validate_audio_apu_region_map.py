#!/usr/bin/env python3
"""Validate the generated audio APU region map."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_REGION_MAP = ROOT / "manifests" / "audio-apu-region-map.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate the audio APU region map.")
    parser.add_argument("region_map", nargs="?", default=str(DEFAULT_REGION_MAP))
    return parser.parse_args()


def validate(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if data.get("schema") != "earthbound-decomp.audio-apu-region-map.v1":
        errors.append(f"unexpected schema: {data.get('schema')}")

    summary = data.get("summary", {})
    if int(summary.get("pack_count", 0)) <= 0:
        errors.append("summary has no packs")
    if int(summary.get("payload_write_count", 0)) <= 0:
        errors.append("summary has no payload writes")
    if int(summary.get("payload_byte_count", 0)) <= 0:
        errors.append("summary has no payload bytes")

    roles = data.get("regions_by_role", [])
    if not roles:
        errors.append("regions_by_role is empty")
    for role in roles:
        if int(role.get("write_count", 0)) <= 0:
            errors.append(f"{role.get('role_guess')}: zero writes")
        if int(role.get("total_payload_bytes", 0)) <= 0:
            errors.append(f"{role.get('role_guess')}: zero payload bytes")
        largest = role.get("largest_write", {})
        if int(largest.get("bytes", 0)) <= 0:
            errors.append(f"{role.get('role_guess')}: invalid largest write")

    return errors


def main() -> int:
    args = parse_args()
    path = Path(args.region_map)
    data = json.loads(path.read_text(encoding="utf-8"))
    errors = validate(data)
    if errors:
        print("Audio APU region map validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "Audio APU region map validation OK: "
        f"{data['summary']['payload_write_count']} writes, "
        f"{len(data['regions_by_role'])} role regions"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
