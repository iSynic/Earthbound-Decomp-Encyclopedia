#!/usr/bin/env python3
"""Inspect one or more music tracks from the audio-pack contract."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONTRACT = ROOT / "manifests" / "audio-pack-contracts.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Look up EarthBound music track pack contracts.")
    parser.add_argument("query", nargs="*", help="Track id or case-insensitive name fragment.")
    parser.add_argument("--contract", default=str(DEFAULT_CONTRACT), help="Audio contract JSON path.")
    parser.add_argument("--json", action="store_true", help="Print raw JSON records.")
    return parser.parse_args()


def load_contract(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def find_tracks(contract: dict[str, Any], queries: list[str]) -> list[dict[str, Any]]:
    tracks = contract["tracks"]
    if not queries:
        return tracks

    matches: list[dict[str, Any]] = []
    seen: set[int] = set()
    for query in queries:
        query = query.strip()
        if not query:
            continue
        query_id: int | None = None
        try:
            query_id = int(query, 0)
        except ValueError:
            pass

        query_lower = query.lower()
        for track in tracks:
            track_id = int(track["track_id"])
            if query_id is not None:
                matched = track_id == query_id
            else:
                matched = query_lower in str(track["name"]).lower()
            if matched and track_id not in seen:
                matches.append(track)
                seen.add(track_id)
    return matches


def format_load_order(loads: list[dict[str, Any]]) -> str:
    if not loads:
        return "(none)"
    return ", ".join(f"{load['role']}=AUDIO_PACK_{load['pack_id']}" for load in loads)


def print_track(track: dict[str, Any]) -> None:
    print(f"{track['track_id']:3d} {track['name']}")
    print(f"    row packs:   {format_load_order(track.get('load_order', []))}")
    print(f"    cold start:  {format_load_order(track.get('cold_start_load_order', []))}")


def main() -> int:
    args = parse_args()
    contract = load_contract(Path(args.contract))
    tracks = find_tracks(contract, args.query)
    if args.json:
        print(json.dumps(tracks, indent=2))
        return 0
    if not tracks:
        print("No tracks matched.")
        return 1
    for track in tracks:
        print_track(track)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
