#!/usr/bin/env python3
"""Validate generated audio renderer input fixtures."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INDEX = ROOT / "build" / "audio" / "renderer-fixtures" / "audio-renderer-fixtures.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate generated audio renderer fixtures.")
    parser.add_argument("index", nargs="?", default=str(DEFAULT_INDEX))
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def resolve_repo_path(path_text: str, *, base: Path | None = None) -> Path:
    path = Path(path_text)
    if path.is_absolute():
        return path
    if path.exists():
        return path
    repo_path = ROOT / path
    if repo_path.exists():
        return repo_path
    return (base or ROOT) / path


def validate_fixture(path: Path) -> list[str]:
    errors: list[str] = []
    fixture = load_json(path)
    track_id = fixture.get("track_id", "?")
    if fixture.get("schema") != "earthbound-decomp.audio-renderer-fixture.v1":
        errors.append(f"{path}: unexpected schema {fixture.get('schema')}")

    ram = fixture.get("apu_ram", {})
    ram_path = resolve_repo_path(str(ram.get("path", "")), base=path.parent)
    if not ram_path.exists():
        errors.append(f"track {track_id}: missing APU RAM image {ram_path}")
    else:
        ram_bytes = ram_path.read_bytes()
        if len(ram_bytes) != 0x10000:
            errors.append(f"track {track_id}: APU RAM size {len(ram_bytes)}, expected 65536")
        sha1 = hashlib.sha1(ram_bytes).hexdigest()
        if sha1 != ram.get("sha1"):
            errors.append(f"track {track_id}: APU RAM SHA-1 mismatch {sha1} != {ram.get('sha1')}")

    load_transcript = fixture.get("load_transcript", [])
    if not load_transcript:
        errors.append(f"track {track_id}: empty load transcript")
    elif load_transcript[-1].get("role") != "post_load_track_start_command":
        errors.append(f"track {track_id}: final transcript step is not track start command")
    else:
        value = int(load_transcript[-1].get("value", -1))
        if value != int(track_id):
            errors.append(f"track {track_id}: final command value {value} does not match track id")

    if fixture.get("load_mode") == "cold_start":
        first_load = fixture.get("load_order", [{}])[0]
        if first_load.get("role") != "initialize_music_subsystem_sequence_pack":
            errors.append(f"track {track_id}: cold-start fixture does not begin with initializer pack")

    if not fixture.get("missing_state"):
        errors.append(f"track {track_id}: missing_state frontier is empty")
    if int(fixture.get("payload_block_count", 0)) <= 0:
        errors.append(f"track {track_id}: no payload blocks applied")

    return errors


def validate(index: dict[str, Any], index_path: Path) -> list[str]:
    errors: list[str] = []
    if index.get("schema") != "earthbound-decomp.audio-renderer-fixture-index.v1":
        errors.append(f"unexpected schema: {index.get('schema')}")
    fixtures = index.get("fixtures", [])
    if int(index.get("track_count", -1)) != len(fixtures):
        errors.append(f"track_count {index.get('track_count')} does not match {len(fixtures)} fixture records")
    for record in fixtures:
        fixture_path = resolve_repo_path(str(record["fixture_path"]), base=index_path.parent)
        if not fixture_path.exists():
            errors.append(f"missing fixture {fixture_path}")
            continue
        errors.extend(validate_fixture(fixture_path))
    return errors


def main() -> int:
    args = parse_args()
    index_path = Path(args.index)
    index = load_json(index_path)
    errors = validate(index, index_path)
    if errors:
        print("Audio renderer fixture validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Audio renderer fixtures validation OK: {index['track_count']} tracks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
