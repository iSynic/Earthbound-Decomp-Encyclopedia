#!/usr/bin/env python3
"""Build a control-flow frontier for EarthBound music sequence commands.

This complements the broad sequence semantics inventory by focusing on the
commands that decide exact export boundaries: likely subroutine calls, jumps,
loops, and end sentinels. It records offsets, counts, and pointer-shape evidence
without embedding ROM-derived sequence payload byte strings.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import audio_pack_contracts
import rom_tools
from build_audio_sequence_semantics_frontier import COMMAND_HYPOTHESES, pointer_prefix


DEFAULT_CONTRACT = ROOT / "manifests" / "audio-pack-contracts.json"
DEFAULT_EXPORT_PLAN = ROOT / "manifests" / "audio-export-plan.json"
DEFAULT_MANIFEST = ROOT / "manifests" / "audio-sequence-control-flow-frontier.json"
DEFAULT_NOTES = ROOT / "notes" / "audio-sequence-control-flow-frontier.md"
CONTROL_COMMANDS = (0xEF, 0xFD, 0xFE, 0xFF)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the audio sequence control-flow frontier.")
    parser.add_argument("--contract", default=str(DEFAULT_CONTRACT), help="Audio pack contract JSON.")
    parser.add_argument("--export-plan", default=str(DEFAULT_EXPORT_PLAN), help="Audio export plan JSON.")
    parser.add_argument("--rom", help="Optional explicit EarthBound US ROM path.")
    parser.add_argument("--output", default=str(DEFAULT_MANIFEST), help="Manifest output JSON.")
    parser.add_argument("--notes", default=str(DEFAULT_NOTES), help="Markdown note output.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_hex_int(text: str) -> int:
    return int(text, 16)


def block_payload(rom: bytes, pack: dict[str, Any], block: dict[str, Any]) -> bytes:
    payload_offset = block.get("payload_offset")
    if payload_offset is None:
        return b""
    data = audio_pack_contracts.slice_range(rom, audio_pack_contracts.parse_cpu_range(pack["range"]))
    offset = parse_hex_int(payload_offset)
    return data[offset:offset + int(block["count"])]


def word_at(payload: bytes, offset: int) -> int | None:
    if offset + 1 >= len(payload):
        return None
    return payload[offset] | (payload[offset + 1] << 8)


def pointer_target_offset(value: int | None, destination: int, payload_len: int) -> int | None:
    if value is None:
        return None
    if destination <= value < destination + payload_len:
        return value - destination
    return None


def pointer_target_set(prefix: dict[str, Any]) -> set[int]:
    return {
        parse_hex_int(entry["target_offset"])
        for entry in prefix["entries_sample"]
        if entry.get("target_offset") is not None
    }


def likely_segment_ranges(payload: bytes, prefix: dict[str, Any]) -> list[tuple[int, int]]:
    starts = sorted(pointer_target_set(prefix))
    body_start = int(prefix["bytes"])
    starts = [start for start in starts if start >= body_start and start < len(payload)]
    if not starts:
        return [(body_start, len(payload))]
    ranges: list[tuple[int, int]] = []
    for index, start in enumerate(starts):
        end = starts[index + 1] if index + 1 < len(starts) else len(payload)
        if start < end:
            ranges.append((start, end))
    return ranges


def classify_occurrence(
    payload: bytes,
    destination: int,
    segment_start: int,
    segment_end: int,
    offset: int,
) -> dict[str, Any]:
    command = payload[offset]
    next1 = payload[offset + 1] if offset + 1 < segment_end else None
    next2 = payload[offset + 2] if offset + 2 < segment_end else None
    next_word = word_at(payload, offset + 1) if offset + 2 < segment_end else None
    pointer_offset = pointer_target_offset(next_word, destination, len(payload))
    remaining_in_segment = segment_end - offset - 1
    return {
        "offset": f"0x{offset:04X}",
        "segment_start": f"0x{segment_start:04X}",
        "segment_end": f"0x{segment_end:04X}",
        "command": f"0x{command:02X}",
        "remaining_bytes_after_command_in_segment": remaining_in_segment,
        "next_byte": None if next1 is None else f"0x{next1:02X}",
        "next_word_le": None if next_word is None else f"0x{next_word:04X}",
        "next_word_points_into_block": pointer_offset is not None,
        "next_word_target_offset": None if pointer_offset is None else f"0x{pointer_offset:04X}",
        "at_segment_tail": remaining_in_segment == 0,
    }


def summarize_command(occurrences: list[dict[str, Any]]) -> dict[str, Any]:
    tail_count = sum(1 for item in occurrences if item["at_segment_tail"])
    pointer_count = sum(1 for item in occurrences if item["next_word_points_into_block"])
    remaining_counts = Counter(str(item["remaining_bytes_after_command_in_segment"]) for item in occurrences)
    next_byte_counts = Counter(item["next_byte"] for item in occurrences if item["next_byte"] is not None)
    next_word_target_counts = Counter(
        item["next_word_target_offset"]
        for item in occurrences
        if item["next_word_target_offset"] is not None
    )
    return {
        "count": len(occurrences),
        "tail_count": tail_count,
        "next_word_pointer_count": pointer_count,
        "tail_ratio": round(tail_count / len(occurrences), 4) if occurrences else 0,
        "next_word_pointer_ratio": round(pointer_count / len(occurrences), 4) if occurrences else 0,
        "remaining_bytes_after_command_top": [
            {"remaining": remaining, "count": count}
            for remaining, count in remaining_counts.most_common(10)
        ],
        "next_byte_top": [
            {"byte": byte, "count": count}
            for byte, count in next_byte_counts.most_common(10)
        ],
        "next_word_target_top": [
            {"target_offset": target, "count": count}
            for target, count in next_word_target_counts.most_common(10)
        ],
        "examples": occurrences[:12],
    }


def build_frontier(contract: dict[str, Any], export_plan: dict[str, Any], rom: bytes) -> dict[str, Any]:
    packs = {int(pack["pack_id"]): pack for pack in contract["audio_packs"]}
    tracks_by_sequence_pack: dict[int, list[dict[str, Any]]] = defaultdict(list)
    export_by_track = {int(track["track_id"]): track for track in export_plan.get("tracks", [])}
    for track in contract["tracks"]:
        sequence_pack = track.get("packs", {}).get("sequence_pack")
        if sequence_pack is None:
            continue
        export = export_by_track.get(int(track["track_id"]), {})
        tracks_by_sequence_pack[int(sequence_pack)].append(
            {
                "track_id": int(track["track_id"]),
                "track_name": track["name"],
                "export_class": export.get("export_class", "unknown"),
                "needs_sequence_semantics": bool(export.get("needs_sequence_semantics", True)),
            }
        )

    command_occurrences: dict[int, list[dict[str, Any]]] = {command: [] for command in CONTROL_COMMANDS}
    pack_records: list[dict[str, Any]] = []
    for pack_id in sorted(tracks_by_sequence_pack):
        pack = packs[pack_id]
        pack_counts: Counter[int] = Counter()
        pack_pointer_counts: Counter[int] = Counter()
        block_records = []
        for block_index, block in enumerate(pack["stream"]["blocks"]):
            if block.get("terminal"):
                continue
            if block["role_guess"] not in {"sequence_or_runtime_tables", "music_sequence_or_sample_directory"}:
                continue
            payload = block_payload(rom, pack, block)
            destination = parse_hex_int(block["destination"])
            prefix = pointer_prefix(payload, destination)
            segment_ranges = likely_segment_ranges(payload, prefix)
            block_counts: Counter[int] = Counter()
            block_pointer_counts: Counter[int] = Counter()
            for segment_start, segment_end in segment_ranges:
                for offset in range(segment_start, segment_end):
                    command = payload[offset]
                    if command not in CONTROL_COMMANDS:
                        continue
                    occurrence = classify_occurrence(payload, destination, segment_start, segment_end, offset)
                    command_occurrences[command].append(
                        {
                            "pack_id": pack_id,
                            "block_index": block_index,
                            "destination": block["destination"],
                            **occurrence,
                        }
                    )
                    block_counts[command] += 1
                    pack_counts[command] += 1
                    if occurrence["next_word_points_into_block"]:
                        block_pointer_counts[command] += 1
                        pack_pointer_counts[command] += 1
            if block_counts:
                block_records.append(
                    {
                        "block_index": block_index,
                        "destination": block["destination"],
                        "bytes": int(block["count"]),
                        "payload_sha1": block["sha1"],
                        "pointer_prefix_words": prefix["word_count"],
                        "segment_count": len(segment_ranges),
                        "control_command_counts": {f"0x{command:02X}": count for command, count in sorted(block_counts.items())},
                        "next_word_pointer_counts": {
                            f"0x{command:02X}": count
                            for command, count in sorted(block_pointer_counts.items())
                        },
                    }
                )
        if pack_counts:
            pack_records.append(
                {
                    "pack_id": pack_id,
                    "range": pack["range"],
                    "track_count": len(tracks_by_sequence_pack[pack_id]),
                    "tracks": tracks_by_sequence_pack[pack_id],
                    "control_command_counts": {f"0x{command:02X}": count for command, count in sorted(pack_counts.items())},
                    "next_word_pointer_counts": {
                        f"0x{command:02X}": count
                        for command, count in sorted(pack_pointer_counts.items())
                    },
                    "blocks": block_records,
                }
            )

    command_summaries = {
        f"0x{command:02X}": {
            "hypothesis": COMMAND_HYPOTHESES.get(command, {}).get("name", "unknown_high_command_candidate"),
            "confidence": COMMAND_HYPOTHESES.get(command, {}).get("confidence", "unknown"),
            **summarize_command(command_occurrences[command]),
        }
        for command in CONTROL_COMMANDS
    }

    priority_packs = sorted(
        pack_records,
        key=lambda item: (
            sum(1 for track in item["tracks"] if track["needs_sequence_semantics"]),
            sum(item["control_command_counts"].values()),
            item["track_count"],
        ),
        reverse=True,
    )[:20]

    return {
        "schema": "earthbound-decomp.audio-sequence-control-flow-frontier.v1",
        "source_policy": contract["source_policy"],
        "references": [
            "manifests/audio-pack-contracts.json",
            "manifests/audio-export-plan.json",
            "manifests/audio-sequence-semantics-frontier.json",
            "notes/audio-sequence-pack-025-semantics.md",
        ],
        "summary": {
            "sequence_packs_with_control_candidates": len(pack_records),
            "control_commands": [f"0x{command:02X}" for command in CONTROL_COMMANDS],
            "total_control_candidates": sum(summary["count"] for summary in command_summaries.values()),
            "semantic_status": "control_flow_operand_shapes_known_driver_dispatch_pending",
        },
        "command_summaries": command_summaries,
        "priority_packs": priority_packs,
        "findings": [
            "EF/FD/FE/FF occurrences are now isolated from pointer-table bytes and grouped by likely sequence segment.",
            "The next-word pointer ratio is the main static evidence for call/jump-like commands before SPC700 driver dispatch is named.",
            "FF tail ratio separates likely end sentinels from FF bytes that appear as operands or data inside longer phrases.",
            "This frontier stores offsets, counts, hashes, and operand-shape evidence only; it does not embed song payload byte strings.",
        ],
        "next_work": [
            "tie the static EF/FD/FE/FF operand shapes to the SPC700 driver's command dispatch table",
            "promote commands with pointer-shaped operands into a checked sequence-walker used by exact-duration export planning",
            "feed high-confidence end and jump behavior back into audio-export-plan exact finite/loop classifications",
        ],
    }


def render_markdown(data: dict[str, Any]) -> str:
    summary = data["summary"]
    command_rows = []
    for command, record in data["command_summaries"].items():
        command_rows.append(
            f"| `{command}` | {record['count']} | {record['hypothesis']} | "
            f"{record['next_word_pointer_count']} ({record['next_word_pointer_ratio']}) | "
            f"{record['tail_count']} ({record['tail_ratio']}) | `{record['remaining_bytes_after_command_top'][:5]}` |"
        )
    priority_rows = []
    for pack in data["priority_packs"]:
        priority_rows.append(
            f"| `{pack['pack_id']}` | `{pack['range']}` | {pack['track_count']} | "
            f"`{pack['control_command_counts']}` | `{pack['next_word_pointer_counts']}` |"
        )
    return "\n".join(
        [
            "# Audio Sequence Control-Flow Frontier",
            "",
            "Status: static control-flow operand shapes known; SPC700 driver dispatch still needs naming.",
            "",
            "## Summary",
            "",
            f"- sequence packs with control candidates: `{summary['sequence_packs_with_control_candidates']}`",
            f"- control commands inspected: `{summary['control_commands']}`",
            f"- total control candidates: `{summary['total_control_candidates']}`",
            f"- semantic status: `{summary['semantic_status']}`",
            "",
            "## Command Summaries",
            "",
            "| Command | Count | Current hypothesis | Next-word pointers | Tail occurrences | Remaining-byte shapes |",
            "| --- | ---: | --- | ---: | ---: | --- |",
            *command_rows,
            "",
            "## Priority Packs",
            "",
            "| Pack | ROM range | Tracks | Control counts | Pointer-shaped operands |",
            "| ---: | --- | ---: | --- | --- |",
            *priority_rows,
            "",
            "## Findings",
            "",
            *[f"- {finding}" for finding in data["findings"]],
            "",
            "## Next Work",
            "",
            *[f"- {item}" for item in data["next_work"]],
            "",
        ]
    )


def main() -> int:
    args = parse_args()
    contract = load_json(Path(args.contract))
    export_plan = load_json(Path(args.export_plan))
    rom = rom_tools.load_rom(rom_tools.find_rom(args.rom))
    data = build_frontier(contract, export_plan, rom)

    output = Path(args.output)
    notes = Path(args.notes)
    output.parent.mkdir(parents=True, exist_ok=True)
    notes.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    notes.write_text(render_markdown(data), encoding="utf-8")
    print(
        "Built audio sequence control-flow frontier: "
        f"{data['summary']['sequence_packs_with_control_candidates']} packs, "
        f"{data['summary']['total_control_candidates']} candidates"
    )
    print(f"Wrote {output}")
    print(f"Wrote {notes}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
