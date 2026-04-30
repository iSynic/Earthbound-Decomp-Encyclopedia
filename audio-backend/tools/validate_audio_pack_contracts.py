#!/usr/bin/env python3
"""Validate EarthBound audio-pack contracts against the local ROM."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import audio_pack_contracts


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONTRACT = ROOT / "manifests" / "audio-pack-contracts.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate generated audio-pack contracts.")
    parser.add_argument("contract", nargs="?", default=str(DEFAULT_CONTRACT))
    return parser.parse_args()


def validate(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    seen_pack_ids: set[int] = set()
    pointer_count = len(data.get("music_pack_pointers", []))
    pack_ids = {int(pack["pack_id"]) for pack in data.get("audio_packs", [])}

    for pack in data.get("audio_packs", []):
        pack_id = int(pack["pack_id"])
        if pack_id in seen_pack_ids:
            errors.append(f"duplicate audio pack id {pack_id}")
        seen_pack_ids.add(pack_id)
        if not pack.get("rom_sha1_verified"):
            errors.append(f"AUDIO_PACK_{pack_id}: ROM SHA-1 mismatch")
        stream = pack.get("stream", {})
        if stream.get("status") != "ok":
            errors.append(f"AUDIO_PACK_{pack_id}: stream parse status {stream.get('status')}")
        if int(stream.get("consumed_bytes", -1)) != int(pack.get("bytes", -2)):
            errors.append(
                f"AUDIO_PACK_{pack_id}: consumed {stream.get('consumed_bytes')} bytes, "
                f"asset has {pack.get('bytes')}"
            )
        if pack.get("pointer") is None and 0 <= pack_id < pointer_count:
            errors.append(f"AUDIO_PACK_{pack_id}: missing pointer entry")

    for track in data.get("tracks", []):
        if int(track["track_id"]) != 0 and not track.get("cold_start_load_order"):
            errors.append(f"track {track['track_id']} {track['name']}: missing cold_start_load_order")
        for load in track.get("load_order", []):
            pack_id = int(load["pack_id"])
            if pack_id not in pack_ids:
                errors.append(
                    f"track {track['track_id']} {track['name']}: "
                    f"{load['role']} references missing AUDIO_PACK_{pack_id}"
                )
        for load in track.get("cold_start_load_order", []):
            pack_id = int(load["pack_id"])
            if pack_id not in pack_ids:
                errors.append(
                    f"track {track['track_id']} {track['name']}: "
                    f"cold-start {load['role']} references missing AUDIO_PACK_{pack_id}"
                )

    if pointer_count != 169:
        errors.append(f"expected 169 music pack pointer entries, found {pointer_count}")
    if len(data.get("tracks", [])) != 192:
        errors.append(f"expected 192 music track entries including NONE, found {len(data.get('tracks', []))}")

    return errors


def main() -> int:
    args = parse_args()
    path = Path(args.contract)
    data = json.loads(path.read_text(encoding="utf-8"))
    errors = validate(data)
    if errors:
        print("Audio contract validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "Audio contract validation OK: "
        f"{len(data['audio_packs'])} packs, {len(data['tracks'])} tracks, "
        f"{len(data['music_pack_pointers'])} pointer entries"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
