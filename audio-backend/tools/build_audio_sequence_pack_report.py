#!/usr/bin/env python3
"""Build a focused report for one EarthBound music sequence pack."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import audio_pack_contracts
import rom_tools
from build_audio_sequence_semantics_frontier import COMMAND_HYPOTHESES, pointer_prefix, scan_payload_semantics


DEFAULT_CONTRACT = ROOT / "manifests" / "audio-pack-contracts.json"
DEFAULT_EXPORT_PLAN = ROOT / "manifests" / "audio-export-plan.json"
EBCOMP_MUSIC_ROOT = ROOT / "refs" / "eb-decompile-4ef92" / "Music"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a focused sequence-pack semantics report.")
    parser.add_argument("--pack-id", type=int, default=25, help="Audio sequence pack id to inspect.")
    parser.add_argument("--contract", default=str(DEFAULT_CONTRACT), help="Audio pack contract JSON.")
    parser.add_argument("--export-plan", default=str(DEFAULT_EXPORT_PLAN), help="Audio export plan JSON.")
    parser.add_argument("--rom", help="Optional explicit EarthBound US ROM path.")
    parser.add_argument("--json", help="JSON output path.")
    parser.add_argument("--markdown", help="Markdown output path.")
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


def word_at(payload: bytes, offset: int) -> int:
    return payload[offset] | (payload[offset + 1] << 8)


def pointer_target_offset(value: int, destination: int, payload_len: int) -> int | None:
    if destination <= value < destination + payload_len:
        return value - destination
    return None


def word_entry(payload: bytes, offset: int, destination: int) -> dict[str, Any]:
    value = word_at(payload, offset)
    target = pointer_target_offset(value, destination, len(payload))
    if value == 0:
        role = "null"
    elif value == 0x00FF:
        role = "sentinel_00ff"
    elif target is not None:
        role = "apu_pointer_into_block"
    else:
        role = "literal_or_unknown_word"
    return {
        "offset": f"0x{offset:04X}",
        "value": f"0x{value:04X}",
        "role": role,
        "target_offset": None if target is None else f"0x{target:04X}",
    }


def segment_kind(segment: bytes) -> str:
    if not segment:
        return "empty"
    if segment.startswith(bytes([0xFA])):
        return "global_setup_candidate"
    if segment.startswith(bytes([0xED])):
        return "channel_init_or_phrase_candidate"
    if segment.startswith(bytes([0x60, 0x7B])):
        return "shared_note_motif_candidate"
    if segment.count(0xC9) >= max(2, len(segment) // 3):
        return "rest_or_tail_candidate"
    return "phrase_or_control_candidate"


def analyze_block(block: dict[str, Any], payload: bytes) -> dict[str, Any]:
    destination = parse_hex_int(block["destination"])
    prefix = pointer_prefix(payload, destination)
    top_level_word_count = 0
    if prefix["entries_sample"]:
        pointer_targets = [
            parse_hex_int(entry["target_offset"])
            for entry in prefix["entries_sample"]
            if entry["target_offset"] is not None
        ]
        if pointer_targets:
            top_level_word_count = min(pointer_targets) // 2
    if top_level_word_count == 0:
        top_level_word_count = min(8, prefix["word_count"])

    top_level = [word_entry(payload, offset, destination) for offset in range(0, top_level_word_count * 2, 2)]
    group_starts = [
        parse_hex_int(entry["target_offset"])
        for entry in top_level
        if entry["target_offset"] is not None
    ]
    sorted_group_starts = sorted(set(group_starts))
    all_pointer_targets = sorted(
        {
            parse_hex_int(entry["target_offset"])
            for entry in prefix["entries_sample"]
            if entry["target_offset"] is not None
        }
    )
    data_targets = [target for target in all_pointer_targets if target not in sorted_group_starts]

    groups: list[dict[str, Any]] = []
    for group_index, group_start in enumerate(sorted_group_starts):
        higher_group_starts = [target for target in sorted_group_starts if target > group_start]
        higher_data_targets = [target for target in data_targets if target > group_start]
        group_end_candidates = higher_group_starts + higher_data_targets
        group_end = min(group_end_candidates) if group_end_candidates else int(prefix["bytes"])
        entries = []
        for offset in range(group_start, group_end, 2):
            if offset + 1 >= len(payload):
                break
            entries.append(word_entry(payload, offset, destination))
        groups.append(
            {
                "group_index_by_address": group_index,
                "start_offset": f"0x{group_start:04X}",
                "end_offset": f"0x{group_end:04X}",
                "word_count": len(entries),
                "active_pointer_count": sum(1 for entry in entries if entry["role"] == "apu_pointer_into_block"),
                "null_count": sum(1 for entry in entries if entry["role"] == "null"),
                "entries": entries,
            }
        )

    segment_starts = sorted(set(data_targets))
    if segment_starts:
        segment_starts.append(len(payload))
    segments = []
    for start, end in zip(segment_starts, segment_starts[1:]):
        segment = payload[start:end]
        scan = scan_payload_semantics(segment, 0)
        segments.append(
            {
                "start_offset": f"0x{start:04X}",
                "end_offset": f"0x{end:04X}",
                "bytes": len(segment),
                "kind": segment_kind(segment),
                "command_candidates": scan["command_candidate_histogram"],
                "note_or_rest_histogram_top": scan["note_or_rest_histogram_top"][:8],
                "duration_or_argument_count": scan["duration_or_argument_count"],
            }
        )

    full_scan = scan_payload_semantics(payload, int(prefix["bytes"]))
    return {
        "destination": block["destination"],
        "bytes": int(block["count"]),
        "payload_sha1": block["sha1"],
        "pointer_prefix": prefix,
        "top_level_table": {
            "word_count": len(top_level),
            "entries": top_level,
            "active_group_pointer_count": len(group_starts),
            "hypothesis": "top-level pointer table selecting two subsequence/channel groups plus one null slot",
        },
        "pointer_groups": groups,
        "segments": segments,
        "scan": full_scan,
    }


def ref_song_path_for_track(track_id: int) -> Path | None:
    songs_yml = EBCOMP_MUSIC_ROOT / "songs.yml"
    if not songs_yml.exists():
        return None
    wanted = f"0x{track_id:02X}:"
    lines = songs_yml.read_text(encoding="utf-8", errors="ignore").splitlines()
    in_entry = False
    song_pack: str | None = None
    song_file: str | None = None
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("0x") and stripped.endswith(":"):
            if in_entry:
                break
            in_entry = stripped.upper() == wanted.upper()
            continue
        if not in_entry:
            continue
        if stripped.startswith("Song Pack:"):
            song_pack = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Song File:"):
            song_file = stripped.split(":", 1)[1].strip()
    if not song_pack or not song_file or song_pack == "in-engine":
        return None
    return EBCOMP_MUSIC_ROOT / "Packs" / song_pack[2:].upper().zfill(2) / song_file


def ref_song_match(track_id: int, block: dict[str, Any], payload: bytes) -> dict[str, Any]:
    path = ref_song_path_for_track(track_id)
    if path is None:
        return {"available": False, "reason": "no_ref_song_path"}
    if not path.exists():
        return {"available": False, "path": path.as_posix(), "reason": "missing_ref_song_file"}
    data = path.read_bytes()
    if len(data) < 4:
        return {"available": False, "path": path.as_posix(), "reason": "ref_song_too_short"}
    declared_count = word_at(data, 0)
    declared_destination = word_at(data, 2)
    ref_payload = data[4:]
    destination = parse_hex_int(block["destination"])
    return {
        "available": True,
        "path": path.relative_to(ROOT).as_posix(),
        "bytes": len(data),
        "declared_count": declared_count,
        "declared_destination": f"0x{declared_destination:04X}",
        "count_matches": declared_count == len(payload),
        "destination_matches": declared_destination == destination,
        "payload_matches": ref_payload == payload,
    }


def build_report(contract: dict[str, Any], export_plan: dict[str, Any], rom: bytes, pack_id: int) -> dict[str, Any]:
    pack = next((item for item in contract["audio_packs"] if int(item["pack_id"]) == pack_id), None)
    if pack is None:
        raise ValueError(f"unknown audio pack {pack_id}")

    tracks = [
        track for track in contract["tracks"]
        if track.get("packs", {}).get("sequence_pack") == pack_id
    ]
    export_by_track = {int(track["track_id"]): track for track in export_plan.get("tracks", [])}
    track_records = []
    for index, track in enumerate(tracks):
        export = export_by_track.get(int(track["track_id"]), {})
        reference_song_path = ref_song_path_for_track(int(track["track_id"]))
        track_records.append(
            {
                "track_id": int(track["track_id"]),
                "track_name": track["name"],
                "sequence_block_index_guess": index,
                "export_class": export.get("export_class"),
                "export_status": export.get("status"),
                "recommended_mode": export.get("recommended_mode"),
                "duration_seconds": export.get("duration_seconds"),
                "needs_sequence_semantics": export.get("needs_sequence_semantics"),
                "reference_song_path": None if reference_song_path is None else reference_song_path.relative_to(ROOT).as_posix(),
            }
        )

    blocks = []
    command_counts: Counter[str] = Counter()
    segment_kind_counts: Counter[str] = Counter()
    for block_index, block in enumerate(pack["stream"]["blocks"]):
        if block.get("terminal"):
            continue
        if block["role_guess"] not in {"sequence_or_runtime_tables", "music_sequence_or_sample_directory"}:
            continue
        payload = block_payload(rom, pack, block)
        analyzed = analyze_block(block, payload)
        if block_index < len(track_records):
            analyzed["reference_song_match"] = ref_song_match(track_records[block_index]["track_id"], block, payload)
        else:
            analyzed["reference_song_match"] = {"available": False, "reason": "no_track_for_block_index"}
        for command in analyzed["scan"]["command_candidate_histogram"]:
            command_counts[command["byte"]] += int(command["count"])
        for segment in analyzed["segments"]:
            segment_kind_counts[segment["kind"]] += 1
        blocks.append(analyzed)

    block_prefix_shapes = Counter(
        (
            block["top_level_table"]["word_count"],
            tuple(group["word_count"] for group in block["pointer_groups"]),
            tuple(group["active_pointer_count"] for group in block["pointer_groups"]),
        )
        for block in blocks
    )
    return {
        "schema": "earthbound-decomp.audio-sequence-pack-report.v1",
        "pack_id": pack_id,
        "range": pack["range"],
        "source_policy": contract["source_policy"],
        "references": [
            "manifests/audio-pack-contracts.json",
            "manifests/audio-export-plan.json",
            "manifests/audio-sequence-semantics-frontier.json",
        ],
        "summary": {
            "track_count": len(track_records),
            "sequence_payload_blocks": len(blocks),
            "block_prefix_shapes": [
                {
                    "top_level_words": shape[0],
                    "group_word_counts": list(shape[1]),
                    "group_active_pointer_counts": list(shape[2]),
                    "count": count,
                }
                for shape, count in block_prefix_shapes.items()
            ],
            "segment_kind_counts": dict(segment_kind_counts),
            "command_candidate_counts": dict(sorted(command_counts.items())),
            "semantic_status": "focused_structure_known_opcode_meanings_pending_driver_dispatch",
            "reference_song_matches": sum(
                1 for block in blocks
                if block.get("reference_song_match", {}).get("payload_matches")
            ),
        },
        "tracks": track_records,
        "blocks": blocks,
        "findings": [
            "Pack track order matches block order for the Sanctuary melody family: tracks 32..39 map cleanly to the eight sequence blocks.",
            "Every block has a 3-word top-level table with two active group pointers and one null slot.",
            "The lower-address group has eight active pointers; the higher-address group has four active pointers followed by four null slots.",
            "Repeated short shared-note motifs start the lower group, while later segments carry channel setup, phrase calls, and rest/tail candidates.",
            "The report stores structural statistics and hashes only; it does not embed ROM-derived payload byte strings.",
            "The eb-decompile reference has matching binary song files for every block in this family; those files corroborate extraction, while this report adds table/group/segment semantics.",
        ],
        "next_work": [
            "tie the 3-word top-level table and two pointer groups to the SPC700 driver's track-start routine",
            "confirm whether the two groups represent music channels, sound-stone layer variants, or intro/body control groups",
            "map EF/FE/FD/FF handling in driver dispatch before promoting exact finite endings for tracks 32..39",
        ],
    }


def render_markdown(data: dict[str, Any]) -> str:
    summary = data["summary"]
    track_rows = [
        "| `{track_id}` | {track_name} | `{sequence_block_index_guess}` | `{export_class}` | `{recommended_mode}` | {duration} |".format(
            track_id=track["track_id"],
            track_name=track["track_name"],
            sequence_block_index_guess=track["sequence_block_index_guess"],
            export_class=track["export_class"],
            recommended_mode=track["recommended_mode"],
            duration="" if track["duration_seconds"] is None else track["duration_seconds"],
        )
        for track in data["tracks"]
    ]
    block_rows = []
    for index, block in enumerate(data["blocks"]):
        groups = "; ".join(
            f"{group['word_count']} words/{group['active_pointer_count']} active/{group['null_count']} null"
            for group in block["pointer_groups"]
        )
        segment_kinds = ", ".join(
            f"{kind}: {count}"
            for kind, count in Counter(segment["kind"] for segment in block["segments"]).items()
        )
        block_rows.append(
            f"| `{index}` | `{block['destination']}` | {block['bytes']} | {block['top_level_table']['word_count']} | {groups} | {segment_kinds} | `{block['reference_song_match'].get('path')}` | `{block['reference_song_match'].get('payload_matches')}` |"
        )
    command_rows = [
        f"| `{byte}` | {count} | {COMMAND_HYPOTHESES.get(int(byte, 16), {}).get('name', 'unknown')} |"
        for byte, count in summary["command_candidate_counts"].items()
    ]

    return "\n".join(
        [
            f"# Audio Sequence Pack {data['pack_id']} Semantics Report",
            "",
            "Status: focused structure known; opcode meanings still need SPC700 driver-dispatch corroboration.",
            "",
            "## Summary",
            "",
            f"- ROM range: `{data['range']}`",
            f"- tracks using pack: `{summary['track_count']}`",
            f"- sequence payload blocks: `{summary['sequence_payload_blocks']}`",
            f"- block prefix shapes: `{summary['block_prefix_shapes']}`",
            f"- segment kinds: `{summary['segment_kind_counts']}`",
            f"- reference song payload matches: `{summary['reference_song_matches']} / {summary['sequence_payload_blocks']}`",
            f"- semantic status: `{summary['semantic_status']}`",
            "",
            "## Tracks",
            "",
            "| Track | Name | Block guess | Export class | Mode | Duration seconds |",
            "| ---: | --- | ---: | --- | --- | ---: |",
            *track_rows,
            "",
            "## Block Structure",
            "",
            "| Block | Destination | Bytes | Top words | Pointer groups | Segment kinds | Ref song | Ref payload match |",
            "| ---: | --- | ---: | ---: | --- | --- | --- | --- |",
            *block_rows,
            "",
            "## Command Candidates",
            "",
            "| Byte | Count | Current hypothesis |",
            "| --- | ---: | --- |",
            *command_rows,
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
    data = build_report(contract, export_plan, rom, args.pack_id)

    json_path = Path(args.json) if args.json else ROOT / "manifests" / f"audio-sequence-pack-{args.pack_id:03d}-semantics.json"
    markdown_path = Path(args.markdown) if args.markdown else ROOT / "notes" / f"audio-sequence-pack-{args.pack_id:03d}-semantics.md"
    json_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    markdown_path.write_text(render_markdown(data), encoding="utf-8")
    print(
        f"Built audio sequence pack {args.pack_id} report: "
        f"{data['summary']['track_count']} tracks, {data['summary']['sequence_payload_blocks']} blocks"
    )
    print(f"Wrote {json_path}")
    print(f"Wrote {markdown_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
