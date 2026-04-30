#!/usr/bin/env python3
"""Build a provisional sequence-walk frontier for EarthBound music data.

This is not a full music decoder. It walks from pointer-table roots, records
strong EF call edges, FF terminator candidates, and FD/FE blockers so exact
duration work can advance one conservative semantic rung at a time.
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
DEFAULT_MANIFEST = ROOT / "manifests" / "audio-sequence-walk-frontier.json"
DEFAULT_NOTES = ROOT / "notes" / "audio-sequence-walk-frontier.md"

# Provisional N-SPC-like widths. These are only used to avoid treating operands
# as opcodes while walking static structure; final names still require driver
# dispatch evidence.
PROVISIONAL_OPERAND_WIDTHS = {
    0xE0: 1,
    0xE1: 1,
    0xE2: 2,
    0xE3: 3,
    0xE4: 0,
    0xE5: 1,
    0xE6: 2,
    0xE7: 1,
    0xE8: 2,
    0xE9: 1,
    0xEA: 1,
    0xEB: 3,
    0xEC: 0,
    0xED: 1,
    0xEE: 2,
    0xEF: 3,
    0xF0: 1,
    0xF1: 3,
    0xF2: 1,
    0xF3: 1,
    0xF4: 1,
    0xF5: 3,
    0xF6: 0,
    0xF7: 3,
    0xF8: 3,
    0xF9: 3,
    0xFA: 2,
    0xFB: 1,
    0xFC: 0,
    0xFD: 1,
    0xFE: 1,
    0xFF: 0,
}
CONTROL_BLOCKERS = {0xFD, 0xFE}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the audio sequence walk frontier.")
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


def pointer_roots(prefix: dict[str, Any]) -> list[int]:
    roots = {
        parse_hex_int(entry["target_offset"])
        for entry in prefix["entries_sample"]
        if entry.get("target_offset") is not None
    }
    return sorted(roots)


def segment_end_for(root: int, roots: list[int], payload_len: int) -> int:
    higher = [candidate for candidate in roots if candidate > root]
    return min(higher) if higher else payload_len


def walk_root(payload: bytes, destination: int, root: int, roots: list[int]) -> dict[str, Any]:
    end = segment_end_for(root, roots, len(payload))
    offset = root
    command_counts: Counter[str] = Counter()
    notes_or_literals = 0
    edges: list[dict[str, Any]] = []
    blockers: list[dict[str, Any]] = []
    terminators: list[dict[str, Any]] = []
    truncations: list[dict[str, Any]] = []

    while offset < end:
        value = payload[offset]
        if value < 0xE0:
            notes_or_literals += 1
            offset += 1
            continue

        command_counts[f"0x{value:02X}"] += 1
        width = PROVISIONAL_OPERAND_WIDTHS.get(value)
        if width is None:
            blockers.append(
                {
                    "offset": f"0x{offset:04X}",
                    "command": f"0x{value:02X}",
                    "reason": "no_provisional_operand_width",
                }
            )
            break
        if offset + width >= len(payload) or offset + width >= end:
            truncations.append(
                {
                    "offset": f"0x{offset:04X}",
                    "command": f"0x{value:02X}",
                    "operand_width": width,
                    "segment_end": f"0x{end:04X}",
                }
            )
            break

        if value == 0xEF:
            target_word = word_at(payload, offset + 1)
            target_offset = pointer_target_offset(target_word, destination, len(payload))
            edges.append(
                {
                    "offset": f"0x{offset:04X}",
                    "target_word": None if target_word is None else f"0x{target_word:04X}",
                    "target_offset": None if target_offset is None else f"0x{target_offset:04X}",
                    "repeat_or_arg": f"0x{payload[offset + 3]:02X}",
                    "target_is_pointer_root": target_offset in roots if target_offset is not None else False,
                    "target_inside_block": target_offset is not None,
                }
            )
        elif value in CONTROL_BLOCKERS:
            blockers.append(
                {
                    "offset": f"0x{offset:04X}",
                    "command": f"0x{value:02X}",
                    "reason": "control_semantics_not_promoted",
                    "next_byte": f"0x{payload[offset + 1]:02X}" if width else None,
                }
            )
        elif value == 0xFF:
            terminators.append(
                {
                    "offset": f"0x{offset:04X}",
                    "segment_end": f"0x{end:04X}",
                    "bytes_before_segment_end": end - offset - 1,
                }
            )
            break

        offset += 1 + width

    return {
        "root_offset": f"0x{root:04X}",
        "segment_end": f"0x{end:04X}",
        "walked_until": f"0x{offset:04X}",
        "notes_or_literals": notes_or_literals,
        "command_counts": dict(sorted(command_counts.items())),
        "ef_call_edges": edges,
        "terminators": terminators,
        "blockers": blockers,
        "truncations": truncations,
        "status": (
            "blocked"
            if blockers or truncations
            else "terminates"
            if terminators
            else "falls_through_segment"
        ),
    }


def build_frontier(contract: dict[str, Any], export_plan: dict[str, Any], rom: bytes) -> dict[str, Any]:
    packs = {int(pack["pack_id"]): pack for pack in contract["audio_packs"]}
    export_by_track = {int(track["track_id"]): track for track in export_plan.get("tracks", [])}
    tracks_by_sequence_pack: dict[int, list[dict[str, Any]]] = defaultdict(list)
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

    pack_records = []
    global_counts: Counter[str] = Counter()
    status_counts: Counter[str] = Counter()
    edge_count = 0
    bad_ef_edges = 0
    blocker_counts: Counter[str] = Counter()
    terminator_count = 0

    for pack_id in sorted(tracks_by_sequence_pack):
        pack = packs[pack_id]
        block_records = []
        pack_status_counts: Counter[str] = Counter()
        pack_command_counts: Counter[str] = Counter()
        pack_blocker_counts: Counter[str] = Counter()
        pack_edge_count = 0
        pack_terminator_count = 0
        for block in pack["stream"]["blocks"]:
            if block.get("terminal"):
                continue
            if block["role_guess"] not in {"sequence_or_runtime_tables", "music_sequence_or_sample_directory"}:
                continue
            payload = block_payload(rom, pack, block)
            destination = parse_hex_int(block["destination"])
            prefix = pointer_prefix(payload, destination)
            roots = pointer_roots(prefix)
            root_walks = [walk_root(payload, destination, root, roots) for root in roots]
            block_command_counts: Counter[str] = Counter()
            block_blocker_counts: Counter[str] = Counter()
            block_edges = 0
            block_bad_edges = 0
            block_terminators = 0
            for walk in root_walks:
                status_counts[walk["status"]] += 1
                pack_status_counts[walk["status"]] += 1
                for command, count in walk["command_counts"].items():
                    global_counts[command] += int(count)
                    pack_command_counts[command] += int(count)
                    block_command_counts[command] += int(count)
                for edge in walk["ef_call_edges"]:
                    edge_count += 1
                    pack_edge_count += 1
                    block_edges += 1
                    if not edge["target_inside_block"]:
                        bad_ef_edges += 1
                        block_bad_edges += 1
                for blocker in walk["blockers"]:
                    blocker_counts[blocker["command"]] += 1
                    pack_blocker_counts[blocker["command"]] += 1
                    block_blocker_counts[blocker["command"]] += 1
                terminator_count += len(walk["terminators"])
                pack_terminator_count += len(walk["terminators"])
                block_terminators += len(walk["terminators"])

            block_records.append(
                {
                    "block_index": int(block["index"]),
                    "destination": block["destination"],
                    "bytes": int(block["count"]),
                    "payload_sha1": block["sha1"],
                    "pointer_roots": len(roots),
                    "walk_status_counts": dict(sorted(Counter(walk["status"] for walk in root_walks).items())),
                    "command_counts": dict(sorted(block_command_counts.items())),
                    "ef_call_edges": block_edges,
                    "ef_edges_not_inside_block": block_bad_edges,
                    "terminators": block_terminators,
                    "blocker_counts": dict(sorted(block_blocker_counts.items())),
                    "root_walks_sample": root_walks[:8],
                }
            )

        if block_records:
            pack_records.append(
                {
                    "pack_id": pack_id,
                    "range": pack["range"],
                    "tracks": tracks_by_sequence_pack[pack_id],
                    "block_count": len(block_records),
                    "walk_status_counts": dict(sorted(pack_status_counts.items())),
                    "command_counts": dict(sorted(pack_command_counts.items())),
                    "ef_call_edges": pack_edge_count,
                    "terminators": pack_terminator_count,
                    "blocker_counts": dict(sorted(pack_blocker_counts.items())),
                    "blocks": block_records,
                }
            )

    priority_packs = sorted(
        pack_records,
        key=lambda item: (
            sum(1 for track in item["tracks"] if track["needs_sequence_semantics"]),
            sum(item["blocker_counts"].values()),
            item["ef_call_edges"],
            len(item["tracks"]),
        ),
        reverse=True,
    )[:20]

    return {
        "schema": "earthbound-decomp.audio-sequence-walk-frontier.v1",
        "source_policy": contract["source_policy"],
        "references": [
            "manifests/audio-pack-contracts.json",
            "manifests/audio-export-plan.json",
            "manifests/audio-sequence-control-flow-frontier.json",
            "manifests/audio-sequence-semantics-frontier.json",
        ],
        "summary": {
            "sequence_packs_walked": len(pack_records),
            "walk_status_counts": dict(sorted(status_counts.items())),
            "command_counts": dict(sorted(global_counts.items())),
            "ef_call_edges": edge_count,
            "ef_edges_not_inside_block": bad_ef_edges,
            "ef_edges_not_inside_block_ratio": round(bad_ef_edges / edge_count, 4) if edge_count else 0,
            "terminators": terminator_count,
            "blocker_counts": dict(sorted(blocker_counts.items())),
            "semantic_status": "provisional_static_walk_ef_edges_known_fd_fe_blockers_unpromoted",
        },
        "provisional_operand_widths": {
            f"0x{command:02X}": {
                "operand_width": width,
                "hypothesis": COMMAND_HYPOTHESES.get(command, {}).get("name", "unknown_high_command_candidate"),
            }
            for command, width in sorted(PROVISIONAL_OPERAND_WIDTHS.items())
        },
        "pack_summaries": [
            {
                "pack_id": pack["pack_id"],
                "range": pack["range"],
                "track_count": len(pack["tracks"]),
                "track_ids": [track["track_id"] for track in pack["tracks"]],
                "export_class_counts": dict(Counter(track["export_class"] for track in pack["tracks"])),
                "needs_sequence_semantics_count": sum(1 for track in pack["tracks"] if track["needs_sequence_semantics"]),
                "block_count": pack["block_count"],
                "walk_status_counts": pack["walk_status_counts"],
                "ef_call_edges": pack["ef_call_edges"],
                "terminators": pack["terminators"],
                "blocker_counts": pack["blocker_counts"],
            }
            for pack in pack_records
        ],
        "priority_packs": priority_packs,
        "findings": [
            "EF call edges are now represented as explicit same-block target edges in a static walk frontier.",
            "A small number of EF-like bytes are tracked as out-of-block under the provisional width table, which marks operand-width or data/noise uncertainty rather than promoted call semantics.",
            "FD and FE remain blockers because their control-flow effect is not promoted from driver dispatch yet.",
            "FF is treated as a terminator candidate when encountered by the provisional walker, but exact end/return meaning still needs dispatch corroboration.",
            "The walker records offsets, hashes, counts, and edge metadata only; it does not embed ROM-derived sequence payload byte strings.",
        ],
        "next_work": [
            "tie FD/FE/FF behavior to the SPC700 driver dispatch path",
            "turn EF call edges into a checked sequence subroutine stack model",
            "use walker status to narrow exact-duration work to packs without unpromoted blockers first",
        ],
    }


def render_markdown(data: dict[str, Any]) -> str:
    summary = data["summary"]
    priority_rows = []
    for pack in data["priority_packs"]:
        priority_rows.append(
            f"| `{pack['pack_id']}` | `{pack['range']}` | {len(pack['tracks'])} | "
            f"`{pack['walk_status_counts']}` | {pack['ef_call_edges']} | {pack['terminators']} | "
            f"`{pack['blocker_counts']}` |"
        )
    command_rows = [
        f"| `{command}` | {count} | {data['provisional_operand_widths'].get(command, {}).get('hypothesis', '')} |"
        for command, count in summary["command_counts"].items()
    ]
    return "\n".join(
        [
            "# Audio Sequence Walk Frontier",
            "",
            "Status: provisional static walk built; EF edges are explicit, FD/FE/FF still need driver corroboration before exact duration promotion.",
            "",
            "## Summary",
            "",
            f"- sequence packs walked: `{summary['sequence_packs_walked']}`",
            f"- walk statuses: `{summary['walk_status_counts']}`",
            f"- EF call edges: `{summary['ef_call_edges']}`",
            f"- EF edges outside block: `{summary['ef_edges_not_inside_block']}` (`{summary['ef_edges_not_inside_block_ratio']}`)",
            f"- FF terminator candidates reached: `{summary['terminators']}`",
            f"- blocker counts: `{summary['blocker_counts']}`",
            f"- semantic status: `{summary['semantic_status']}`",
            "",
            "## Commands Seen By Walker",
            "",
            "| Command | Count | Current hypothesis |",
            "| --- | ---: | --- |",
            *command_rows,
            "",
            "## Priority Packs",
            "",
            "| Pack | ROM range | Tracks | Walk statuses | EF edges | Terminators | Blockers |",
            "| ---: | --- | ---: | --- | ---: | ---: | --- |",
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
        "Built audio sequence walk frontier: "
        f"{data['summary']['sequence_packs_walked']} packs, "
        f"{data['summary']['ef_call_edges']} EF edges"
    )
    print(f"Wrote {output}")
    print(f"Wrote {notes}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
