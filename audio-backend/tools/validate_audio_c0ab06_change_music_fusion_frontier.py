#!/usr/bin/env python3
"""Validate full CHANGE_MUSIC -> real C0:AB06 live-driver fusion evidence."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_FRONTIER = (
    ROOT
    / "build"
    / "audio"
    / "c0ab06-change-music-fusion-frontier"
    / "c0ab06-change-music-fusion-frontier.json"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate full CHANGE_MUSIC / real C0:AB06 fusion evidence.")
    parser.add_argument("frontier", nargs="?", default=str(DEFAULT_FRONTIER))
    return parser.parse_args()


def validate(frontier: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if frontier.get("schema") != "earthbound-decomp.c0ab06-change-music-fusion-frontier.v1":
        errors.append(f"unexpected schema: {frontier.get('schema')}")
    if frontier.get("status") != "full_change_music_invokes_real_c0ab06_against_live_driver":
        errors.append(f"unexpected status: {frontier.get('status')}")
    job_count = int(frontier.get("job_count", 0))
    if job_count <= 0:
        errors.append("job_count must be positive")
    representative = frontier.get("corpus", "representative_backend_tracks") == "representative_backend_tracks"
    if representative and int(frontier.get("success_count", -1)) != job_count:
        errors.append(f"success_count is {frontier.get('success_count')}")
    if int(frontier.get("load_path_success_count", frontier.get("success_count", -1))) != job_count:
        errors.append(f"load_path_success_count is {frontier.get('load_path_success_count')}")
    if representative and int(frontier.get("key_on_count", -1)) != job_count:
        errors.append(f"key_on_count is {frontier.get('key_on_count')}")
    if int(frontier.get("payload_region_match_count", -1)) != job_count:
        errors.append(f"payload_region_match_count is {frontier.get('payload_region_match_count')}")
    if representative and int(frontier.get("snapshot_count", -1)) != job_count:
        errors.append(f"snapshot_count is {frontier.get('snapshot_count')}")
    if int(frontier.get("mismatch_count", -1)) != 0:
        errors.append(f"mismatch_count is {frontier.get('mismatch_count')}")
    records = frontier.get("records", [])
    if len(records) != job_count:
        errors.append("record count does not match job_count")
    for record in records:
        job_id = record.get("job_id")
        expected_pack_ids = record.get("expected_sequence_pack_ids", [])
        if representative and int(record.get("returncode", -1)) != 0:
            errors.append(f"{job_id}: returncode {record.get('returncode')}")
        if not record.get("load_path_ok", True):
            errors.append(f"{job_id}: load_path_ok is false")
        if not expected_pack_ids:
            errors.append(f"{job_id}: empty expected sequence")
        handshake = record.get("handshake") or {}
        if representative and not handshake.get("ok"):
            errors.append(f"{job_id}: handshake not ok")
        if handshake.get("receiver") != "ares_smp_ipl":
            errors.append(f"{job_id}: receiver is {handshake.get('receiver')}")
        if not handshake.get("change_music_after_bootstrap"):
            errors.append(f"{job_id}: did not run change_music_after_bootstrap")
        if not (handshake.get("bootstrap") or {}).get("ok"):
            errors.append(f"{job_id}: bootstrap failed")
        change_music = handshake.get("change_music") or {}
        if change_music.get("final_pc") != "0x008004":
            errors.append(f"{job_id}: ChangeMusic final PC is {change_music.get('final_pc')}")
        if int(change_music.get("command_writes", -1)) != 1:
            errors.append(f"{job_id}: command writes is {change_music.get('command_writes')}")
        if int(change_music.get("load_calls", -1)) != len(expected_pack_ids):
            errors.append(f"{job_id}: load call count differs from expected sequence")
        if not change_music.get("reached_command_read_pc_062a"):
            errors.append(f"{job_id}: did not reach command read PC")
        if not change_music.get("reached_zero_ack_shape"):
            errors.append(f"{job_id}: did not reach zero ack")
        if representative and not change_music.get("reached_key_on_after_ack"):
            errors.append(f"{job_id}: did not reach key-on after ack")
        load_steps = change_music.get("load_steps", [])
        if len(load_steps) != len(expected_pack_ids):
            errors.append(f"{job_id}: load step count differs from expected sequence")
        for index, step in enumerate(load_steps):
            if int(step.get("terminal_tokens", -1)) != 1:
                errors.append(f"{job_id}: load step {index} terminal tokens is {step.get('terminal_tokens')}")
            if int(step.get("block_start_tokens", 0)) <= 0:
                errors.append(f"{job_id}: load step {index} has no block-start tokens")
            if int(step.get("payload_bytes", 0)) <= 0:
                errors.append(f"{job_id}: load step {index} has no payload bytes")
        payload_regions = record.get("payload_regions") or {}
        if not payload_regions.get("payload_regions_match"):
            errors.append(f"{job_id}: payload regions do not match")
        if int(payload_regions.get("payload_region_mismatch_count", -1)) != 0:
            errors.append(f"{job_id}: payload region mismatch count is {payload_regions.get('payload_region_mismatch_count')}")
        if int(payload_regions.get("bytes", 0)) != 0x10000:
            errors.append(f"{job_id}: APU RAM dump size is {payload_regions.get('bytes')}")
        snapshot = record.get("snapshot") or {}
        if representative and not snapshot:
            errors.append(f"{job_id}: missing snapshot metadata")
        elif snapshot and not snapshot.get("signature_ok"):
            errors.append(f"{job_id}: snapshot signature is invalid")
        elif snapshot and snapshot.get("kon") in (None, "0x00"):
            errors.append(f"{job_id}: snapshot KON is not set")
    return errors


def main() -> int:
    args = parse_args()
    frontier = json.loads(Path(args.frontier).read_text(encoding="utf-8"))
    errors = validate(frontier)
    if errors:
        print("C0:AB06 CHANGE_MUSIC fusion frontier validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "C0:AB06 CHANGE_MUSIC fusion frontier validation OK: "
        f"{frontier.get('load_path_success_count', frontier['success_count'])} / {frontier['job_count']} load paths, "
        f"{frontier['payload_region_match_count']} / {frontier['job_count']} payload matches, "
        f"{frontier.get('key_on_count', frontier['success_count'])} key-on, "
        f"{frontier['snapshot_count']} snapshots"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
