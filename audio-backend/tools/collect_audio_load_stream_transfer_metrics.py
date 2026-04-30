#!/usr/bin/env python3
"""Collect semantic LOAD_SPC700_DATA transfer metrics for the audio corpus."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import audio_pack_contracts
import rom_tools


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONTRACT = ROOT / "manifests" / "audio-pack-contracts.json"
DEFAULT_CORPUS = ROOT / "build" / "audio" / "corpus" / "audio-snapshot-corpus.json"
DEFAULT_LOAD_STUB_SUMMARY = ROOT / "build" / "audio" / "ares-wdc65816-full-change-music-load-stub-mailbox-smoke-jobs" / "smp-mailbox-smoke-summary.json"
DEFAULT_OUTPUT = ROOT / "build" / "audio" / "load-stream-transfer" / "load-stream-transfer-metrics.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Collect semantic LOAD_SPC700_DATA transfer metrics.")
    parser.add_argument("--rom", help="Optional explicit EarthBound US ROM path.")
    parser.add_argument("--contract", default=str(DEFAULT_CONTRACT), help="Audio pack contract JSON.")
    parser.add_argument("--corpus", default=str(DEFAULT_CORPUS), help="Generated APU RAM corpus JSON.")
    parser.add_argument("--load-stub-summary", default=str(DEFAULT_LOAD_STUB_SUMMARY), help="Full CHANGE_MUSIC load-stub smoke summary JSON.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Metrics JSON output.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_contract(path: Path) -> dict[str, Any]:
    if path.exists():
        return load_json(path)
    return audio_pack_contracts.build_audio_contract()


def pack_by_id(contract: dict[str, Any]) -> dict[int, dict[str, Any]]:
    return {int(pack["pack_id"]): pack for pack in contract["audio_packs"]}


def track_by_id(contract: dict[str, Any]) -> dict[int, dict[str, Any]]:
    return {int(track["track_id"]): track for track in contract["tracks"]}


def smoke_record_by_track(summary: dict[str, Any]) -> dict[int, dict[str, Any]]:
    return {int(record["track_id"]): record for record in summary.get("records", [])}


def corpus_record_by_track(corpus: dict[str, Any]) -> dict[int, dict[str, Any]]:
    return {int(record["track_id"]): record for record in corpus.get("tracks", [])}


def pointer_pair_for_pack(pack: dict[str, Any]) -> dict[str, str] | None:
    pointer = pack.get("pointer") or {}
    if not pointer:
        return None
    return {
        "a": f"0x{int(str(pointer['address']), 16):04X}",
        "x": f"0x{int(str(pointer['bank']), 16):04X}",
    }


def load_order_pack_ids(load_order: list[dict[str, Any]]) -> list[int]:
    return [int(load["pack_id"]) for load in load_order if load.get("pack_id") is not None]


def replay_load_order(
    *,
    rom: bytes,
    packs: dict[int, dict[str, Any]],
    load_order: list[dict[str, Any]],
) -> tuple[bytes, list[dict[str, Any]], Counter[str]]:
    ram = bytearray(0x10000)
    transcript: list[dict[str, Any]] = []
    role_counts: Counter[str] = Counter()

    for load_index, load in enumerate(load_order):
        pack_id = int(load["pack_id"])
        pack = packs[pack_id]
        data = audio_pack_contracts.slice_range(rom, audio_pack_contracts.parse_cpu_range(pack["range"]))
        parsed = audio_pack_contracts.parse_load_spc700_stream(data)
        if parsed.status != "ok":
            raise ValueError(f"AUDIO_PACK_{pack_id} parse status is {parsed.status}")

        payload_bytes = 0
        payload_blocks = 0
        block_records: list[dict[str, Any]] = []
        for block in parsed.blocks:
            if block.terminal:
                block_records.append(
                    {
                        "block": block.index,
                        "terminal": True,
                        "stream_offset": f"0x{block.stream_offset:04X}",
                        "destination": "0x0500",
                    }
                )
                continue
            assert block.payload_offset is not None
            payload = data[block.payload_offset:block.payload_offset + block.count]
            destination_end = block.destination + block.count
            if destination_end > len(ram):
                raise ValueError(f"AUDIO_PACK_{pack_id} block {block.index} writes past APU RAM")
            ram[block.destination:destination_end] = payload
            payload_blocks += 1
            payload_bytes += block.count
            role_counts[block.role_guess] += 1
            block_records.append(
                {
                    "block": block.index,
                    "terminal": False,
                    "stream_offset": f"0x{block.stream_offset:04X}",
                    "payload_offset": f"0x{block.payload_offset:04X}",
                    "destination": f"0x{block.destination:04X}",
                    "bytes": block.count,
                    "payload_sha1": hashlib.sha1(payload).hexdigest(),
                    "role_guess": block.role_guess,
                }
            )

        transcript.append(
            {
                "load_index": load_index,
                "role": load["role"],
                "pack_id": pack_id,
                "pack_range": pack["range"],
                "pointer": pack.get("pointer"),
                "block_count": len(parsed.blocks),
                "payload_block_count": payload_blocks,
                "payload_bytes": payload_bytes,
                "stream_consumed_bytes": parsed.consumed_bytes,
                "blocks": block_records,
            }
        )
    return bytes(ram), transcript, role_counts


def collect(contract: dict[str, Any], corpus: dict[str, Any], load_stub_summary: dict[str, Any], rom: bytes) -> dict[str, Any]:
    packs = pack_by_id(contract)
    tracks = track_by_id(contract)
    smoke_records = smoke_record_by_track(load_stub_summary)
    corpus_records = corpus_record_by_track(corpus)

    records: list[dict[str, Any]] = []
    mismatch_tracks: list[int] = []
    ram_mismatch_tracks: list[int] = []
    load_call_mismatch_tracks: list[int] = []
    destination_roles: Counter[str] = Counter()

    for track_id in sorted(corpus_records):
        track = tracks[track_id]
        corpus_record = corpus_records[track_id]
        smoke_record = smoke_records.get(track_id, {})
        probe = (smoke_record.get("smoke", {}) or {}).get("cpu_instruction_probe", {}) or {}
        actual_load_args = list(probe.get("load_spc700_data_stub_args", []))
        track_load_order = list(track.get("load_order", []))
        cold_start_load_order = list(track.get("cold_start_load_order", []))
        expected_change_music_args = [
            pointer_pair_for_pack(packs[pack_id])
            for pack_id in load_order_pack_ids(track_load_order)
        ]
        expected_change_music_args = [item for item in expected_change_music_args if item is not None]
        change_music_args_match = actual_load_args == expected_change_music_args

        replayed_ram, transcript, role_counts = replay_load_order(
            rom=rom,
            packs=packs,
            load_order=cold_start_load_order,
        )
        destination_roles.update(role_counts)
        replayed_sha1 = hashlib.sha1(replayed_ram).hexdigest()
        corpus_ram_path = Path(corpus_record["ram_path"])
        corpus_ram = corpus_ram_path.read_bytes()
        corpus_sha1 = hashlib.sha1(corpus_ram).hexdigest()
        ram_matches_corpus = replayed_ram == corpus_ram and corpus_sha1 == corpus_record.get("ram_sha1")

        if not ram_matches_corpus or not change_music_args_match:
            mismatch_tracks.append(track_id)
        if not ram_matches_corpus:
            ram_mismatch_tracks.append(track_id)
        if not change_music_args_match:
            load_call_mismatch_tracks.append(track_id)

        records.append(
            {
                "track_id": track_id,
                "track_name": track["name"],
                "cold_start_pack_ids": load_order_pack_ids(cold_start_load_order),
                "change_music_pack_ids": load_order_pack_ids(track_load_order),
                "actual_change_music_load_args": actual_load_args,
                "expected_change_music_load_args": expected_change_music_args,
                "change_music_load_args_match": change_music_args_match,
                "corpus_ram_path": str(corpus_ram_path),
                "corpus_ram_sha1": corpus_sha1,
                "replayed_ram_sha1": replayed_sha1,
                "ram_matches_corpus": ram_matches_corpus,
                "load_transcript": transcript,
            }
        )

    return {
        "schema": "earthbound-decomp.audio-load-stream-transfer-metrics.v1",
        "source_policy": contract["source_policy"],
        "track_count": len(records),
        "mismatch_count": len(mismatch_tracks),
        "ram_mismatch_count": len(ram_mismatch_tracks),
        "load_call_mismatch_count": len(load_call_mismatch_tracks),
        "mismatch_tracks": mismatch_tracks,
        "ram_mismatch_tracks": ram_mismatch_tracks,
        "load_call_mismatch_tracks": load_call_mismatch_tracks,
        "destination_role_counts": dict(destination_roles),
        "records": records,
    }


def main() -> int:
    args = parse_args()
    contract = load_contract(Path(args.contract))
    corpus = load_json(Path(args.corpus))
    load_stub_summary = load_json(Path(args.load_stub_summary))
    rom_path = rom_tools.find_rom(args.rom)
    rom = rom_tools.load_rom(rom_path)
    metrics = collect(contract, corpus, load_stub_summary, rom)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")
    print(
        "Collected audio load-stream transfer metrics: "
        f"{metrics['track_count']} tracks, "
        f"{metrics['mismatch_count']} mismatches, "
        f"{metrics['ram_mismatch_count']} RAM mismatches, "
        f"{metrics['load_call_mismatch_count']} load-call mismatches"
    )
    print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
