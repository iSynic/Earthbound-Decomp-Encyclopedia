#!/usr/bin/env python3
"""Validate ignored audio snapshot corpus outputs."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CORPUS = ROOT / "build" / "audio" / "corpus" / "audio-snapshot-corpus.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate generated APU RAM snapshot corpus files.")
    parser.add_argument("corpus", nargs="?", default=str(DEFAULT_CORPUS))
    return parser.parse_args()


def validate(corpus: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if corpus.get("schema") != "earthbound-decomp.audio-snapshot-corpus.v1":
        errors.append(f"unexpected schema: {corpus.get('schema')}")
    tracks = corpus.get("tracks", [])
    if not isinstance(tracks, list) or not tracks:
        errors.append("corpus has no track records")
        return errors
    if int(corpus.get("track_count", -1)) != len(tracks):
        errors.append(f"track_count {corpus.get('track_count')} does not match {len(tracks)} records")

    seen_tracks: set[int] = set()
    for record in tracks:
        track_id = int(record["track_id"])
        if track_id in seen_tracks:
            errors.append(f"duplicate track id {track_id}")
        seen_tracks.add(track_id)
        ram_path = Path(record["ram_path"])
        if not ram_path.exists():
            errors.append(f"track {track_id}: missing RAM image {ram_path}")
            continue
        data = ram_path.read_bytes()
        if len(data) != 0x10000:
            errors.append(f"track {track_id}: RAM image size is {len(data)}, expected 65536")
        sha1 = hashlib.sha1(data).hexdigest()
        if sha1 != record.get("ram_sha1"):
            errors.append(f"track {track_id}: RAM SHA-1 mismatch {sha1} != {record.get('ram_sha1')}")
        if not record.get("load_order"):
            errors.append(f"track {track_id}: empty load order")
        if int(record.get("payload_block_count", 0)) <= 0:
            errors.append(f"track {track_id}: no payload blocks applied")

    summary = corpus.get("summary", {})
    if int(summary.get("unique_pack_count", 0)) <= 0:
        errors.append("summary has no unique packs")
    return errors


def main() -> int:
    args = parse_args()
    path = Path(args.corpus)
    corpus = json.loads(path.read_text(encoding="utf-8"))
    errors = validate(corpus)
    if errors:
        print("Audio snapshot corpus validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "Audio snapshot corpus validation OK: "
        f"{corpus['track_count']} tracks, "
        f"{corpus['summary']['unique_pack_count']} unique packs"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

