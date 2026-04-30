#!/usr/bin/env python3
"""Validate ignored CPU routine byte fixtures used by audio mailbox smoke tests."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MANIFEST = ROOT / "build" / "audio" / "cpu-routine-fixtures" / "audio-cpu-routine-fixtures.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate audio CPU routine byte fixtures.")
    parser.add_argument("manifest", nargs="?", default=str(DEFAULT_MANIFEST))
    return parser.parse_args()


def validate(manifest: dict) -> list[str]:
    errors: list[str] = []
    if manifest.get("schema") != "earthbound-decomp.audio-cpu-routine-fixtures.v1":
        errors.append(f"unexpected schema: {manifest.get('schema')}")
    records = manifest.get("records", [])
    if int(manifest.get("fixture_count", -1)) != len(records):
        errors.append("fixture_count does not match records")
    for record in records:
        fixture_id = str(record.get("id", ""))
        path = Path(str(record.get("path", "")))
        if not path.is_absolute():
            path = ROOT / path
        if not path.exists():
            errors.append(f"{fixture_id}: missing fixture bytes {path}")
            continue
        data = path.read_bytes()
        expected_hex = record.get("expected_hex")
        if expected_hex and data.hex() != str(expected_hex):
            errors.append(f"{fixture_id}: bytes do not match expected_hex")
        if data.hex() != record.get("hex"):
            errors.append(f"{fixture_id}: bytes do not match manifest hex")
        if hashlib.sha1(data).hexdigest() != record.get("sha1"):
            errors.append(f"{fixture_id}: SHA-1 mismatch")
        expected_sha1 = record.get("expected_sha1")
        if expected_sha1 and hashlib.sha1(data).hexdigest() != expected_sha1:
            errors.append(f"{fixture_id}: SHA-1 does not match expected_sha1")
        if not record.get("matches_expected"):
            errors.append(f"{fixture_id}: matches_expected is false")
    return errors


def main() -> int:
    args = parse_args()
    manifest_path = Path(args.manifest)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    errors = validate(manifest)
    if errors:
        print("Audio CPU routine fixture validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Audio CPU routine fixture validation OK: {manifest['fixture_count']} fixtures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
