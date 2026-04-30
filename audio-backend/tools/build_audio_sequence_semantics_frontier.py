#!/usr/bin/env python3
"""Build the EarthBound music sequence semantics frontier.

This is deliberately conservative. It inventories sequence-pack payload blocks
and records evidence for likely N-SPC-style command bytes without claiming a
full decoder yet. Generated audio outputs stay ignored; this manifest is a
checked-in semantic frontier built from existing contracts.
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

DEFAULT_CONTRACT = ROOT / "manifests" / "audio-pack-contracts.json"
DEFAULT_EXPORT_PLAN = ROOT / "manifests" / "audio-export-plan.json"
DEFAULT_MANIFEST = ROOT / "manifests" / "audio-sequence-semantics-frontier.json"
DEFAULT_NOTES = ROOT / "notes" / "audio-sequence-semantics-frontier.md"
FOCUSED_REPORTS = [
    {
        "pack_id": 25,
        "json": "manifests/audio-sequence-pack-025-semantics.json",
        "notes": "notes/audio-sequence-pack-025-semantics.md",
        "builder": "tools/build_audio_sequence_pack_report.py --pack-id 25",
        "validation": "tools/validate_audio_sequence_pack_report.py manifests/audio-sequence-pack-025-semantics.json",
        "status": "structure_known_opcode_dispatch_pending",
        "claim": "Sanctuary melody family tracks 32..39 map to eight sequence blocks with a stable 3-word top-level table, two pointer groups, and repeated channel/phrase segment shapes.",
    }
]


COMMAND_HYPOTHESES: dict[int, dict[str, str]] = {
    0xE0: {"name": "set_instrument_candidate", "confidence": "medium"},
    0xE1: {"name": "set_pan_candidate", "confidence": "medium"},
    0xE2: {"name": "pan_fade_candidate", "confidence": "low"},
    0xE3: {"name": "vibrato_on_candidate", "confidence": "low"},
    0xE4: {"name": "vibrato_off_candidate", "confidence": "low"},
    0xE5: {"name": "master_volume_or_channel_state_candidate", "confidence": "low"},
    0xE6: {"name": "volume_or_master_fade_candidate", "confidence": "low"},
    0xE7: {"name": "tempo_or_tuning_candidate", "confidence": "low"},
    0xE8: {"name": "tempo_fade_candidate", "confidence": "low"},
    0xE9: {"name": "global_transpose_candidate", "confidence": "low"},
    0xEA: {"name": "channel_transpose_candidate", "confidence": "low"},
    0xEB: {"name": "tremolo_or_modulation_on_candidate", "confidence": "low"},
    0xEC: {"name": "tremolo_or_modulation_off_candidate", "confidence": "low"},
    0xED: {"name": "set_channel_volume_candidate", "confidence": "medium"},
    0xEE: {"name": "channel_volume_fade_candidate", "confidence": "low"},
    0xEF: {"name": "subroutine_call_candidate", "confidence": "medium"},
    0xF0: {"name": "modulation_fade_candidate", "confidence": "low"},
    0xF1: {"name": "pitch_envelope_or_portamento_candidate", "confidence": "low"},
    0xF2: {"name": "pitch_envelope_off_candidate", "confidence": "low"},
    0xF3: {"name": "tuning_or_detune_candidate", "confidence": "low"},
    0xF4: {"name": "driver_toggle_or_extended_control_candidate", "confidence": "low"},
    0xF5: {"name": "echo_or_voice_param_candidate", "confidence": "low"},
    0xF6: {"name": "echo_off_or_effect_disable_candidate", "confidence": "low"},
    0xF7: {"name": "echo_or_effect_setup_candidate", "confidence": "low"},
    0xF8: {"name": "echo_or_effect_fade_candidate", "confidence": "low"},
    0xF9: {"name": "pitch_slide_candidate", "confidence": "low"},
    0xFA: {"name": "earthbound_extended_command_candidate", "confidence": "medium"},
    0xFB: {"name": "loop_start_or_control_candidate", "confidence": "low"},
    0xFC: {"name": "loop_end_or_control_candidate", "confidence": "low"},
    0xFD: {"name": "loop_or_jump_control_candidate", "confidence": "low"},
    0xFE: {"name": "jump_or_long_control_candidate", "confidence": "low"},
    0xFF: {"name": "end_or_sentinel_candidate", "confidence": "medium"},
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the audio sequence semantics frontier.")
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


def pointer_prefix(payload: bytes, destination: int) -> dict[str, Any]:
    entries: list[dict[str, Any]] = []
    end = destination + len(payload)
    offset = 0
    while offset + 1 < len(payload):
        value = payload[offset] | (payload[offset + 1] << 8)
        role: str | None = None
        if value == 0x0000:
            role = "null"
        elif value == 0x00FF:
            role = "sentinel_00ff"
        elif destination <= value < end:
            role = "apu_pointer_into_block"
        if role is None:
            break
        entries.append(
            {
                "offset": f"0x{offset:04X}",
                "value": f"0x{value:04X}",
                "role": role,
                "target_offset": None if role != "apu_pointer_into_block" else f"0x{value - destination:04X}",
            }
        )
        offset += 2
    counts = Counter(entry["role"] for entry in entries)
    return {
        "bytes": offset,
        "word_count": len(entries),
        "role_counts": dict(counts),
        "entries_sample": entries[:24],
    }


def scan_payload_semantics(payload: bytes, scan_start: int) -> dict[str, Any]:
    body = payload[scan_start:]
    byte_counts = Counter(body)
    command_counts = Counter(value for value in body if value >= 0xE0)
    next_byte_counts: dict[int, Counter[int]] = defaultdict(Counter)
    second_next_byte_counts: dict[int, Counter[int]] = defaultdict(Counter)
    for index, value in enumerate(body):
        if value < 0xE0:
            continue
        if index + 1 < len(body):
            next_byte_counts[value][body[index + 1]] += 1
        if index + 2 < len(body):
            second_next_byte_counts[value][body[index + 2]] += 1
    note_counts = Counter(value for value in body if 0x80 <= value <= 0xC9)
    duration_or_arg_counts = Counter(value for value in body if value < 0x80)
    return {
        "scan_start": f"0x{scan_start:04X}",
        "scan_bytes": len(body),
        "byte_histogram_top": [{"byte": f"0x{value:02X}", "count": count} for value, count in byte_counts.most_common(24)],
        "command_candidate_histogram": [
            {
                "byte": f"0x{value:02X}",
                "count": count,
                "hypothesis": COMMAND_HYPOTHESES.get(value, {}).get("name", "unknown_high_command_candidate"),
                "confidence": COMMAND_HYPOTHESES.get(value, {}).get("confidence", "unknown"),
                "next_byte_top": [
                    {"byte": f"0x{next_value:02X}", "count": next_count}
                    for next_value, next_count in next_byte_counts[value].most_common(8)
                ],
                "second_next_byte_top": [
                    {"byte": f"0x{next_value:02X}", "count": next_count}
                    for next_value, next_count in second_next_byte_counts[value].most_common(8)
                ],
            }
            for value, count in sorted(command_counts.items())
        ],
        "note_or_rest_candidate_count": sum(note_counts.values()),
        "note_or_rest_histogram_top": [
            {"byte": f"0x{value:02X}", "count": count}
            for value, count in note_counts.most_common(16)
        ],
        "duration_or_argument_count": sum(duration_or_arg_counts.values()),
    }


def block_payload(rom: bytes, pack: dict[str, Any], block: dict[str, Any]) -> bytes:
    payload_offset = block.get("payload_offset")
    if payload_offset is None:
        return b""
    data = audio_pack_contracts.slice_range(rom, audio_pack_contracts.parse_cpu_range(pack["range"]))
    offset = parse_hex_int(payload_offset)
    return data[offset:offset + int(block["count"])]


def build_frontier(
    contract: dict[str, Any],
    export_plan: dict[str, Any] | None,
    rom: bytes,
) -> dict[str, Any]:
    packs = {int(pack["pack_id"]): pack for pack in contract["audio_packs"]}
    tracks_by_sequence_pack: dict[int, list[dict[str, Any]]] = defaultdict(list)
    export_by_track: dict[int, dict[str, Any]] = {}
    if export_plan:
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

    sequence_pack_ids = sorted(tracks_by_sequence_pack)
    blocks: list[dict[str, Any]] = []
    global_command_counts: Counter[int] = Counter()
    command_next_byte_counts: dict[int, Counter[int]] = defaultdict(Counter)
    command_second_next_byte_counts: dict[int, Counter[int]] = defaultdict(Counter)
    destination_counts: Counter[str] = Counter()
    pointer_shape_counts: Counter[str] = Counter()
    block_shapes_by_pack: dict[int, list[dict[str, Any]]] = defaultdict(list)

    for pack_id in sequence_pack_ids:
        pack = packs[pack_id]
        for block in pack["stream"]["blocks"]:
            if block.get("terminal"):
                continue
            role = block["role_guess"]
            if role not in {"sequence_or_runtime_tables", "music_sequence_or_sample_directory"}:
                continue

            destination = parse_hex_int(block["destination"])
            count = int(block["count"])
            payload = block_payload(rom, pack, block)
            prefix = pointer_prefix(payload, destination)
            scan = scan_payload_semantics(payload, int(prefix["bytes"]))
            for command_entry in scan["command_candidate_histogram"]:
                command_value = parse_hex_int(command_entry["byte"])
                global_command_counts[command_value] += int(command_entry["count"])
                for next_entry in command_entry["next_byte_top"]:
                    command_next_byte_counts[command_value][parse_hex_int(next_entry["byte"])] += int(next_entry["count"])
                for next_entry in command_entry["second_next_byte_top"]:
                    command_second_next_byte_counts[command_value][parse_hex_int(next_entry["byte"])] += int(next_entry["count"])
            block_record = {
                "pack_id": pack_id,
                "pack_range": pack["range"],
                "destination": block["destination"],
                "bytes": count,
                "role_guess": role,
                "payload_sha1": block["sha1"],
                "tracks_using_pack": tracks_by_sequence_pack[pack_id],
                "pointer_prefix": prefix,
                "scan": scan,
            }
            blocks.append(block_record)
            block_shapes_by_pack[pack_id].append(
                {
                    "destination": block["destination"],
                    "bytes": count,
                    "pointer_prefix_words": prefix["word_count"],
                    "scan_bytes": scan["scan_bytes"],
                }
            )
            destination_counts[block["destination"]] += 1
            pointer_shape_counts[f"{prefix['word_count']}_prefix_words"] += 1

    export_pressure = Counter()
    for tracks in tracks_by_sequence_pack.values():
        for track in tracks:
            export_pressure[track["export_class"]] += 1

    priority_sequence_packs = []
    for pack_id, tracks in tracks_by_sequence_pack.items():
        class_counts = Counter(track["export_class"] for track in tracks)
        priority_sequence_packs.append(
            {
                "pack_id": pack_id,
                "range": packs[pack_id]["range"],
                "track_count": len(tracks),
                "needs_sequence_semantics_count": sum(1 for track in tracks if track["needs_sequence_semantics"]),
                "export_class_counts": dict(class_counts),
                "block_shapes": block_shapes_by_pack.get(pack_id, []),
                "tracks": tracks,
            }
        )
    priority_sequence_packs.sort(
        key=lambda item: (
            item["needs_sequence_semantics_count"],
            item["export_class_counts"].get("finite_or_transition_review_candidate", 0),
            item["export_class_counts"].get("loop_or_held_candidate", 0),
            item["track_count"],
        ),
        reverse=True,
    )

    command_contexts = {}
    for value, count in sorted(global_command_counts.items()):
        command_contexts[f"0x{value:02X}"] = {
            "count": count,
            "hypothesis": COMMAND_HYPOTHESES.get(value, {}).get("name", "unknown_high_command_candidate"),
            "confidence": COMMAND_HYPOTHESES.get(value, {}).get("confidence", "unknown"),
            "next_byte_top": [
                {"byte": f"0x{next_value:02X}", "count": next_count}
                for next_value, next_count in command_next_byte_counts[value].most_common(12)
            ],
            "second_next_byte_top": [
                {"byte": f"0x{next_value:02X}", "count": next_count}
                for next_value, next_count in command_second_next_byte_counts[value].most_common(12)
            ],
        }

    return {
        "schema": "earthbound-decomp.audio-sequence-semantics-frontier.v1",
        "source_policy": contract["source_policy"],
        "references": [
            "manifests/audio-pack-contracts.json",
            "manifests/audio-export-plan.json",
            "notes/audio-export-plan.md",
            "refs/ebsrc-main/ebsrc-main/src/audio/change_music.asm",
            "refs/ebsrc-main/ebsrc-main/src/audio/load_spc700_data.asm",
        ],
        "summary": {
            "music_tracks": len(contract["tracks"]),
            "sequence_pack_count": len(sequence_pack_ids),
            "sequence_payload_block_count": len(blocks),
            "destination_counts": dict(destination_counts),
            "export_pressure": dict(export_pressure),
            "pointer_shape_counts": dict(pointer_shape_counts),
            "observed_high_command_candidates": {
                f"0x{value:02X}": count for value, count in sorted(global_command_counts.items())
            },
            "opcode_semantics_status": "payload_histograms_built_command_meanings_still_hypotheses",
        },
        "known_command_hypotheses": {
            f"0x{value:02X}": hypothesis for value, hypothesis in sorted(COMMAND_HYPOTHESES.items())
        },
        "command_contexts": command_contexts,
        "priority_sequence_packs": priority_sequence_packs[:40],
        "focused_reports": [
            {**report, "exists": (ROOT / report["json"]).exists() and (ROOT / report["notes"]).exists()}
            for report in FOCUSED_REPORTS
        ],
        "sequence_packs": [
            {
                "pack_id": pack_id,
                "range": packs[pack_id]["range"],
                "track_count": len(tracks_by_sequence_pack[pack_id]),
                "tracks": tracks_by_sequence_pack[pack_id],
            }
            for pack_id in sequence_pack_ids
        ],
        "sequence_blocks": blocks,
        "next_work": [
            "identify the sequence entry table shape that maps the APU track command to channel/subsequence pointers",
            "map high-byte command candidates to the SPC700 driver dispatch paths",
            "use command semantics to promote exact finite endings and loop/fade export policy",
        ],
    }


def render_markdown(data: dict[str, Any]) -> str:
    summary = data["summary"]
    command_rows = [
        f"| `{byte}` | {entry['name']} | {entry['confidence']} |"
        for byte, entry in data["known_command_hypotheses"].items()
    ]
    pack_rows = []
    for pack in data["sequence_packs"][:40]:
        classes = Counter(track["export_class"] for track in pack["tracks"])
        pack_rows.append(
            f"| `{pack['pack_id']}` | `{pack['range']}` | {pack['track_count']} | `{dict(classes)}` |"
        )
    priority_rows = [
        f"| `{pack['pack_id']}` | `{pack['range']}` | {pack['needs_sequence_semantics_count']} | {pack['track_count']} | `{pack['export_class_counts']}` | `{pack['block_shapes']}` |"
        for pack in data["priority_sequence_packs"][:20]
    ]
    focused_rows = [
        f"| `{report['pack_id']}` | {report['status']} | `{report['json']}` | {report['claim']} |"
        for report in data["focused_reports"]
    ]
    context_rows = [
        f"| `{byte}` | {context['count']} | {context['hypothesis']} | `{context['next_byte_top'][:6]}` |"
        for byte, context in data["command_contexts"].items()
    ]

    return "\n".join(
        [
            "# Audio Sequence Semantics Frontier",
            "",
            "Status: first-pass sequence-pack frontier inventory; payload-level opcode decoding is the next active work.",
            "",
            "EarthBound's music sequence data is loaded by `CHANGE_MUSIC` as the third pack role, after primary and secondary sample packs. "
            "The current audio renderer can play/export all snapshot-backed tracks, but exact endings and loop points still need sequence bytecode semantics.",
            "",
            "## Summary",
            "",
            f"- music tracks represented: `{summary['music_tracks']}`",
            f"- unique sequence packs used by tracks: `{summary['sequence_pack_count']}`",
            f"- sequence payload blocks inventoried: `{summary['sequence_payload_block_count']}`",
            f"- destination counts: `{summary['destination_counts']}`",
            f"- export-pressure classes: `{summary['export_pressure']}`",
            f"- observed high-command candidates: `{summary['observed_high_command_candidates']}`",
            f"- opcode status: `{summary['opcode_semantics_status']}`",
            "",
            "## Current Boundary",
            "",
            "- This frontier is contract-backed and safe to check in.",
            "- It does not embed ROM-derived sequence payload bytes; it stores structural statistics, pointer candidates, hashes, and command histograms.",
            "- It separates track/export pressure from opcode semantics so exact-duration work can focus on the tracks that still need it.",
            "",
            "## First-Pass Command Hypotheses",
            "",
            "These names are hypotheses to guide driver work, not final source names. They are intentionally marked as candidates until tied to SPC700 dispatch evidence.",
            "",
            "| Byte | Candidate meaning | Confidence |",
            "| --- | --- | --- |",
            *command_rows,
            "",
            "## Command Contexts",
            "",
            "Top next-byte profiles are statistical evidence for operand widths and control-flow commands. They still need SPC700 driver-dispatch corroboration before promotion to final names.",
            "",
            "| Byte | Count | Candidate meaning | Top following bytes |",
            "| --- | ---: | --- | --- |",
            *context_rows,
            "",
            "## Exact-Duration Priority Packs",
            "",
            "These packs have the most tracks still needing sequence semantics for exact export behavior.",
            "",
            "| Pack | ROM range | Needs semantics | Tracks | Export classes | Block shapes |",
            "| ---: | --- | ---: | ---: | --- | --- |",
            *priority_rows,
            "",
            "## Focused Pack Reports",
            "",
            "| Pack | Status | Manifest | Claim |",
            "| ---: | --- | --- | --- |",
            *focused_rows,
            "",
            "## Sequence Packs",
            "",
            "First 40 sequence packs by id:",
            "",
            "| Pack | ROM range | Track count | Export classes |",
            "| ---: | --- | ---: | --- |",
            *pack_rows,
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
    export_path = Path(args.export_plan)
    export_plan = load_json(export_path) if export_path.exists() else None
    rom_path = rom_tools.find_rom(args.rom)
    rom = rom_tools.load_rom(rom_path)
    data = build_frontier(contract, export_plan, rom)

    output_path = Path(args.output)
    notes_path = Path(args.notes)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    notes_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    notes_path.write_text(render_markdown(data), encoding="utf-8")
    print(
        "Built audio sequence semantics frontier: "
        f"{data['summary']['sequence_pack_count']} sequence packs, "
        f"{data['summary']['sequence_payload_block_count']} payload blocks"
    )
    print(f"Wrote {output_path}")
    print(f"Wrote {notes_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
