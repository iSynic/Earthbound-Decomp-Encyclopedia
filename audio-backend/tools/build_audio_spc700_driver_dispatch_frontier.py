#!/usr/bin/env python3
"""Build a static frontier for the SPC700 music-driver dispatch tables.

This intentionally stops short of naming command effects. It extracts the
pack-1 driver payload, finds SPC700 indirect-jump table shapes, and records the
strong high-command table candidate that maps E0..FF command bytes to driver
targets. The result gives the FF terminator lane a concrete driver address to
inspect without claiming whether that target ends a sequence, returns from a
subroutine, or stops a channel.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import audio_pack_contracts
import rom_tools
from build_audio_sequence_semantics_frontier import COMMAND_HYPOTHESES


DEFAULT_CONTRACT = ROOT / "manifests" / "audio-pack-contracts.json"
DEFAULT_OUTPUT = ROOT / "manifests" / "audio-spc700-driver-dispatch-frontier.json"
DEFAULT_NOTES = ROOT / "notes" / "audio-spc700-driver-dispatch-frontier.md"
HIGH_COMMAND_TABLE_BASE = 0x16C7
HIGH_COMMAND_FIRST = 0xE0
HIGH_COMMAND_LAST = 0xFF
INDIRECT_JUMP_OPCODE = 0x1F


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the audio SPC700 driver dispatch frontier.")
    parser.add_argument("--contract", default=str(DEFAULT_CONTRACT), help="Audio pack contract JSON.")
    parser.add_argument("--rom", help="Optional explicit EarthBound US ROM path.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Manifest output JSON.")
    parser.add_argument("--notes", default=str(DEFAULT_NOTES), help="Markdown note output.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_hex_int(text: str) -> int:
    return int(text, 16)


def hex_word(value: int) -> str:
    return f"0x{value:04X}"


def hex_byte(value: int) -> str:
    return f"0x{value:02X}"


def extract_driver_payload(contract: dict[str, Any], rom: bytes) -> tuple[dict[str, Any], bytes, int]:
    for pack in contract["audio_packs"]:
        for block in pack.get("stream", {}).get("blocks", []):
            if block.get("role_guess") != "main_spc700_driver_or_driver_overlay":
                continue
            data = audio_pack_contracts.slice_range(rom, audio_pack_contracts.parse_cpu_range(pack["range"]))
            payload_offset = parse_hex_int(block["payload_offset"])
            count = int(block["count"])
            payload = data[payload_offset:payload_offset + count]
            destination = parse_hex_int(block["destination"])
            record = {
                "pack_id": int(pack["pack_id"]),
                "asset_id": pack["asset_id"],
                "range": pack["range"],
                "block_index": int(block["index"]),
                "destination": hex_word(destination),
                "count": count,
                "sha1": block["sha1"],
                "role_guess": block["role_guess"],
            }
            return record, payload, destination
    raise ValueError("audio pack contract does not contain a main SPC700 driver block")


def read_word(payload: bytes, offset: int) -> int | None:
    if offset < 0 or offset + 1 >= len(payload):
        return None
    return payload[offset] | (payload[offset + 1] << 8)


def apu_offset(address: int, base: int, payload: bytes) -> int | None:
    if base <= address < base + len(payload):
        return address - base
    return None


def pointer_run(payload: bytes, base: int, table_address: int, limit: int | None = None) -> list[int]:
    offset = apu_offset(table_address, base, payload)
    if offset is None:
        return []
    words: list[int] = []
    while offset + 1 < len(payload):
        if limit is not None and len(words) >= limit:
            break
        value = read_word(payload, offset)
        if value is None or apu_offset(value, base, payload) is None:
            break
        words.append(value)
        offset += 2
    return words


def target_profile(payload: bytes, base: int, target: int) -> dict[str, Any]:
    offset = apu_offset(target, base, payload)
    if offset is None:
        return {"target": hex_word(target), "inside_driver": False}
    first = payload[offset]
    return {
        "target": hex_word(target),
        "inside_driver": True,
        "target_offset": hex_word(offset),
        "first_byte": hex_byte(first),
        "first_byte_is_sequence_high_command_candidate": first >= 0xE0,
        "first_byte_is_note_or_rest_candidate": 0x80 <= first <= 0xC9,
    }


def scan_indirect_jump_candidates(payload: bytes, base: int) -> list[dict[str, Any]]:
    by_operand: dict[int, dict[str, Any]] = {}
    references: dict[int, list[str]] = defaultdict(list)

    for offset, opcode in enumerate(payload[:-2]):
        if opcode != INDIRECT_JUMP_OPCODE:
            continue
        operand = read_word(payload, offset + 1)
        if operand is None:
            continue
        references[operand].append(hex_word(base + offset))

    for operand, refs in references.items():
        run = pointer_run(payload, base, operand)
        first_32 = run[:32]
        profiles = [target_profile(payload, base, target) for target in first_32[:8]]
        by_operand[operand] = {
            "operand": hex_word(operand),
            "referencing_addresses": refs[:12],
            "reference_count": len(refs),
            "operand_points_into_driver": apu_offset(operand, base, payload) is not None,
            "inside_pointer_run_words": len(run),
            "first_32_words_all_inside_driver": len(first_32) == 32,
            "first_32_unique_targets": len(set(first_32)),
            "first_32_target_range": None if not first_32 else f"{hex_word(min(first_32))}..{hex_word(max(first_32))}",
            "first_8_target_profiles": profiles,
            "candidate_role": "unclassified_indirect_table_candidate",
        }

    candidates = list(by_operand.values())
    for candidate in candidates:
        if candidate["operand"] == hex_word(HIGH_COMMAND_TABLE_BASE):
            candidate["candidate_role"] = "likely_e0_ff_high_command_dispatch_table"
        elif candidate["first_32_words_all_inside_driver"]:
            candidate["candidate_role"] = "pointer_table_candidate_effect_unknown"
        elif candidate["operand_points_into_driver"]:
            candidate["candidate_role"] = "short_or_mixed_indirect_target_candidate"
        else:
            candidate["candidate_role"] = "operand_outside_driver_or_data_false_positive_candidate"

    candidates.sort(
        key=lambda item: (
            item["candidate_role"] != "likely_e0_ff_high_command_dispatch_table",
            -int(item["first_32_words_all_inside_driver"]),
            -int(item["inside_pointer_run_words"]),
            item["operand"],
        )
    )
    return candidates


def build_high_command_candidate(payload: bytes, base: int, indirect_candidates: list[dict[str, Any]]) -> dict[str, Any]:
    table_words = pointer_run(payload, base, HIGH_COMMAND_TABLE_BASE, limit=32)
    source_refs: list[str] = []
    for candidate in indirect_candidates:
        if candidate["operand"] == hex_word(HIGH_COMMAND_TABLE_BASE):
            source_refs = candidate["referencing_addresses"]
            break

    entries = []
    for index, target in enumerate(table_words):
        command = HIGH_COMMAND_FIRST + index
        hypothesis = COMMAND_HYPOTHESES.get(command, {})
        entries.append(
            {
                "command": hex_byte(command),
                "hypothesis": hypothesis.get("name", "unknown_high_command_candidate"),
                "confidence": hypothesis.get("confidence", "unknown"),
                "target": hex_word(target),
                "target_profile": target_profile(payload, base, target),
            }
        )

    ff_entry = entries[-1] if len(entries) == 32 else None
    return {
        "status": "likely_table_static_target_identified_runtime_effect_pending",
        "table_base": hex_word(HIGH_COMMAND_TABLE_BASE),
        "source_indirect_jump_addresses": source_refs,
        "opcode_hypothesis": "0x1F operand is treated as the SPC700 absolute indexed indirect jump shape for static triage.",
        "command_range": f"{hex_byte(HIGH_COMMAND_FIRST)}..{hex_byte(HIGH_COMMAND_LAST)}",
        "entry_count": len(entries),
        "entries": entries,
        "ff_dispatch_candidate": None if ff_entry is None else {
            "command": ff_entry["command"],
            "hypothesis": ff_entry["hypothesis"],
            "target": ff_entry["target"],
            "semantic_status": "driver_target_known_effect_unconfirmed",
            "why_not_promoted": "Static table evidence identifies the target, but exact duration semantics still need an execution/disassembly pass at the target to distinguish end, return, channel stop, hold, or loop behavior.",
        },
    }


def build_frontier(contract: dict[str, Any], rom: bytes) -> dict[str, Any]:
    driver, payload, base = extract_driver_payload(contract, rom)
    indirect_candidates = scan_indirect_jump_candidates(payload, base)
    high_command = build_high_command_candidate(payload, base, indirect_candidates)
    strong_tables = [
        candidate
        for candidate in indirect_candidates
        if candidate["first_32_words_all_inside_driver"]
    ]
    return {
        "schema": "earthbound-decomp.audio-spc700-driver-dispatch-frontier.v1",
        "status": "static_dispatch_table_candidates_recorded_ff_target_effect_pending",
        "references": [
            "manifests/audio-pack-contracts.json",
            "manifests/audio-sequence-semantics-frontier.json",
            "manifests/audio-ff-terminator-review.json",
            "tools/ares_audio_harness/main.cpp",
        ],
        "driver": driver,
        "summary": {
            "driver_base": hex_word(base),
            "driver_bytes": len(payload),
            "indirect_jump_opcode": hex_byte(INDIRECT_JUMP_OPCODE),
            "indirect_jump_operand_count": sum(candidate["reference_count"] for candidate in indirect_candidates),
            "unique_indirect_operands": len(indirect_candidates),
            "first_32_inside_table_candidates": len(strong_tables),
            "high_command_table_base": high_command["table_base"],
            "high_command_entry_count": high_command["entry_count"],
            "ff_dispatch_target": None if high_command["ff_dispatch_candidate"] is None else high_command["ff_dispatch_candidate"]["target"],
            "semantic_status": "ff_driver_target_identified_but_effect_unconfirmed",
        },
        "high_command_dispatch_candidate": high_command,
        "indirect_jump_candidates": indirect_candidates[:24],
        "findings": [
            "The pack-1 driver block contains a strong 0x1F indirect table candidate at $16C7 that cleanly maps 32 entries onto the E0..FF high-command byte range used by sequence payloads.",
            "Under that mapping, FF points at driver target $1A81, giving the FF terminator review lane a concrete address for the next SPC700 disassembly or execution trace.",
            "This artifact does not promote FF to an end command yet; it only names the static dispatch target and keeps the runtime effect pending.",
            "Several other 0x1F operands also point at driver-local tables, so the driver likely uses multiple indirect dispatch tables for lower-level music/runtime control.",
        ],
        "next_work": [
            "disassemble or trace execution at $1A81 with live channel state to determine whether FF ends a sequence, returns from EF, stops a channel, or falls into another control path",
            "capture a short runtime trace around the 0x1F $16C7 dispatch for at least one sequence that reaches FF",
            "after FF effect is confirmed, feed the result back into the FF terminator review and finite/loop metadata lanes",
        ],
    }


def render_markdown(data: dict[str, Any]) -> str:
    summary = data["summary"]
    high = data["high_command_dispatch_candidate"]
    entry_rows = [
        "| `{command}` | `{hypothesis}` | `{target}` | `{first_byte}` |".format(
            command=entry["command"],
            hypothesis=entry["hypothesis"],
            target=entry["target"],
            first_byte=entry["target_profile"].get("first_byte"),
        )
        for entry in high["entries"]
    ]
    candidate_rows = [
        "| `{operand}` | `{role}` | `{refs}` | `{run}` | `{all32}` | `{range}` |".format(
            operand=candidate["operand"],
            role=candidate["candidate_role"],
            refs=", ".join(candidate["referencing_addresses"]),
            run=candidate["inside_pointer_run_words"],
            all32=candidate["first_32_words_all_inside_driver"],
            range=candidate["first_32_target_range"],
        )
        for candidate in data["indirect_jump_candidates"]
    ]
    ff = high["ff_dispatch_candidate"] or {}
    return "\n".join(
        [
            "# Audio SPC700 Driver Dispatch Frontier",
            "",
            "Status: static dispatch targets recorded; FF runtime effect still pending.",
            "",
            "## Summary",
            "",
            f"- driver block: pack `{data['driver']['pack_id']}` block `{data['driver']['block_index']}` at `{data['driver']['destination']}`, `{data['driver']['count']}` bytes",
            f"- unique indirect operands: `{summary['unique_indirect_operands']}`",
            f"- first-32-inside table candidates: `{summary['first_32_inside_table_candidates']}`",
            f"- likely high-command table: `{summary['high_command_table_base']}`",
            f"- FF dispatch target candidate: `{summary['ff_dispatch_target']}`",
            f"- semantic status: `{summary['semantic_status']}`",
            "",
            "## FF Candidate",
            "",
            f"- command: `{ff.get('command')}`",
            f"- hypothesis: `{ff.get('hypothesis')}`",
            f"- target: `{ff.get('target')}`",
            f"- status: `{ff.get('semantic_status')}`",
            f"- not promoted yet: {ff.get('why_not_promoted')}",
            "",
            "## High Command Table",
            "",
            f"- table base: `{high['table_base']}`",
            f"- source indirect jump addresses: `{high['source_indirect_jump_addresses']}`",
            f"- opcode hypothesis: {high['opcode_hypothesis']}",
            "",
            "| Command | Current sequence hypothesis | Driver target | Target first byte |",
            "| --- | --- | ---: | --- |",
            *entry_rows,
            "",
            "## Indirect Jump Candidates",
            "",
            "| Operand | Candidate role | Referencing addresses | Pointer-run words | First 32 inside | First-32 target range |",
            "| ---: | --- | --- | ---: | --- | --- |",
            *candidate_rows,
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
    rom_path = rom_tools.find_rom(args.rom)
    data = build_frontier(contract, rom_tools.load_rom(rom_path))
    output = Path(args.output)
    notes = Path(args.notes)
    output.parent.mkdir(parents=True, exist_ok=True)
    notes.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    notes.write_text(render_markdown(data), encoding="utf-8")
    print(
        "Built audio SPC700 driver dispatch frontier: "
        f"{data['summary']['unique_indirect_operands']} operands, "
        f"FF target {data['summary']['ff_dispatch_target']}"
    )
    print(f"Wrote {output}")
    print(f"Wrote {notes}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
