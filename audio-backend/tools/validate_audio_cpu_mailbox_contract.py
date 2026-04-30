#!/usr/bin/env python3
"""Validate the CPU/APU audio mailbox contract."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONTRACT = ROOT / "manifests" / "audio-cpu-mailbox-contract.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate the audio CPU/APU mailbox contract.")
    parser.add_argument("contract", nargs="?", default=str(DEFAULT_CONTRACT))
    parser.add_argument("--require-frontier", action="store_true", help="Require generated mailbox frontier counts.")
    parser.add_argument("--require-smp-smoke", action="store_true", help="Require generated ares SMP mailbox smoke counts.")
    return parser.parse_args()


def validate(contract: dict[str, Any], *, require_frontier: bool, require_smp_smoke: bool) -> list[str]:
    errors: list[str] = []
    if contract.get("schema") != "earthbound-decomp.audio-cpu-mailbox-contract.v1":
        errors.append(f"unexpected schema: {contract.get('schema')}")

    cpu = contract.get("cpu_side_contract", {})
    if cpu.get("send_track_command_entry") != "C0:ABBD":
        errors.append("send track command entry must be C0:ABBD")
    if cpu.get("send_track_command_register") != "$2140/APUIO0":
        errors.append("send track command register must be $2140/APUIO0")
    if cpu.get("send_track_command_opcode") != "STA long $002140":
        errors.append("send track command opcode must be STA long $002140")
    if cpu.get("send_track_command_rom_bytes") != "E2 20 8F 40 21 00 C2 30 6B":
        errors.append("send track command ROM bytes must match retail C0:ABBD")
    if cpu.get("track_command_value") != "one_based_track_id":
        errors.append("track command value must be one_based_track_id")

    apu = contract.get("apu_side_diagnostic_contract", {})
    if apu.get("driver_first_command_read_pc") != "0x062A":
        errors.append("first command read PC must be 0x062A")
    if apu.get("driver_first_ack_write_data") != "0x00":
        errors.append("first ack write data must be 0x00")

    ares = contract.get("ares_bridge_contract", {})
    if "smp.portWrite" not in ares.get("cpu_to_apu_entrypoint", ""):
        errors.append("ares CPU->APU bridge must mention smp.portWrite")
    if "smp.portRead" not in ares.get("apu_to_cpu_entrypoint", ""):
        errors.append("ares APU->CPU bridge must mention smp.portRead")

    summary = contract.get("current_frontier_summary", {})
    if require_frontier:
        job_count = int(summary.get("job_count", 0))
        for field in ("capture_count", "command_read_count", "command_match_count", "zero_ack_write_count", "keyon_after_command_read_count"):
            if int(summary.get(field, 0)) != job_count:
                errors.append(f"frontier {field} does not match job_count")
        if summary.get("first_read_pc_counts") != {"0x062A": job_count}:
            errors.append("frontier first read PC counts must be all 0x062A")
        if summary.get("first_ack_pc_counts") != {"0x062A": job_count}:
            errors.append("frontier first ack PC counts must be all 0x062A")

    smp_summary = contract.get("current_ares_smp_smoke_summary", {})
    if require_smp_smoke:
        job_count = int(smp_summary.get("job_count", 0))
        for field in ("success_count", "command_read_count", "zero_ack_count", "key_on_count"):
            if int(smp_summary.get(field, 0)) != job_count:
                errors.append(f"smp smoke {field} does not match job_count")
        if smp_summary.get("delivery_mode") != "ares_smp_portwrite_on_pc_062a":
            errors.append("smp smoke delivery mode must be ares_smp_portwrite_on_pc_062a")

        jsl_summary = contract.get("current_ares_rom_c0abbd_jsl_summary", {})
        jsl_job_count = int(jsl_summary.get("job_count", 0))
        for field in ("success_count", "command_read_count", "zero_ack_count", "key_on_count"):
            if int(jsl_summary.get(field, 0)) != jsl_job_count:
                errors.append(f"ROM C0:ABBD JSL smoke {field} does not match job_count")
        if jsl_summary.get("delivery_mode") != "ares_wdc65816_rom_c0abbd_jsl_on_pc_062a":
            errors.append("ROM C0:ABBD JSL smoke delivery mode must be ares_wdc65816_rom_c0abbd_jsl_on_pc_062a")
        if jsl_summary.get("routine") != "rom_fixture_C0ABBD_jsl_call_context":
            errors.append("ROM C0:ABBD JSL smoke routine must be rom_fixture_C0ABBD_jsl_call_context")

        tail_summary = contract.get("current_ares_change_music_tail_summary", {})
        tail_job_count = int(tail_summary.get("job_count", 0))
        for field in ("success_count", "command_read_count", "zero_ack_count", "key_on_count"):
            if int(tail_summary.get(field, 0)) != tail_job_count:
                errors.append(f"CHANGE_MUSIC tail smoke {field} does not match job_count")
        if tail_summary.get("delivery_mode") != "ares_wdc65816_change_music_tail_on_pc_062a":
            errors.append("CHANGE_MUSIC tail smoke delivery mode must be ares_wdc65816_change_music_tail_on_pc_062a")
        if tail_summary.get("routine") != "rom_fixture_ChangeMusic_tail_to_C0ABBD":
            errors.append("CHANGE_MUSIC tail smoke routine must be rom_fixture_ChangeMusic_tail_to_C0ABBD")

        full_change_music_summary = contract.get("current_ares_full_change_music_summary", {})
        full_change_music_job_count = int(full_change_music_summary.get("job_count", 0))
        for field in ("success_count", "command_read_count", "zero_ack_count", "key_on_count"):
            if int(full_change_music_summary.get(field, 0)) != full_change_music_job_count:
                errors.append(f"full CHANGE_MUSIC smoke {field} does not match job_count")
        if full_change_music_summary.get("delivery_mode") != "ares_wdc65816_full_change_music_on_pc_062a":
            errors.append("full CHANGE_MUSIC smoke delivery mode must be ares_wdc65816_full_change_music_on_pc_062a")
        if full_change_music_summary.get("routine") != "rom_fixture_ChangeMusic_full_presatisfied_packs":
            errors.append("full CHANGE_MUSIC smoke routine must be rom_fixture_ChangeMusic_full_presatisfied_packs")

        load_stub_summary = contract.get("current_ares_full_change_music_load_stub_summary", {})
        load_stub_job_count = int(load_stub_summary.get("job_count", 0))
        for field in ("success_count", "command_read_count", "zero_ack_count", "key_on_count"):
            if int(load_stub_summary.get(field, 0)) != load_stub_job_count:
                errors.append(f"full CHANGE_MUSIC load-stub smoke {field} does not match job_count")
        if load_stub_summary.get("delivery_mode") != "ares_wdc65816_full_change_music_load_stub_on_pc_062a":
            errors.append("full CHANGE_MUSIC load-stub delivery mode must be ares_wdc65816_full_change_music_load_stub_on_pc_062a")
        if load_stub_summary.get("routine") != "rom_fixture_ChangeMusic_full_load_path_stubbed_loader":
            errors.append("full CHANGE_MUSIC load-stub routine must be rom_fixture_ChangeMusic_full_load_path_stubbed_loader")
        loader_metrics = load_stub_summary.get("loader_metrics", {})
        if int(loader_metrics.get("job_count", 0)) != load_stub_job_count:
            errors.append("full CHANGE_MUSIC load-stub metrics job_count must match smoke job_count")
        if int(loader_metrics.get("mismatch_count", -1)) != 0:
            errors.append("full CHANGE_MUSIC load-stub metrics must have zero mismatches")

        load_apply_summary = contract.get("current_ares_full_change_music_load_apply_summary", {})
        load_apply_job_count = int(load_apply_summary.get("job_count", 0))
        for field in ("success_count", "command_read_count", "zero_ack_count", "key_on_count"):
            if int(load_apply_summary.get(field, 0)) != load_apply_job_count:
                errors.append(f"full CHANGE_MUSIC load-apply smoke {field} does not match job_count")
        if load_apply_summary.get("delivery_mode") != "ares_wdc65816_full_change_music_load_apply_on_pc_062a":
            errors.append("full CHANGE_MUSIC load-apply delivery mode must be ares_wdc65816_full_change_music_load_apply_on_pc_062a")
        if load_apply_summary.get("routine") != "rom_fixture_ChangeMusic_full_load_path_applied_loader":
            errors.append("full CHANGE_MUSIC load-apply routine must be rom_fixture_ChangeMusic_full_load_path_applied_loader")
        apply_metrics = load_apply_summary.get("loader_metrics", {})
        if int(apply_metrics.get("job_count", 0)) != load_apply_job_count:
            errors.append("full CHANGE_MUSIC load-apply metrics job_count must match smoke job_count")
        if int(apply_metrics.get("mismatch_count", -1)) != 0:
            errors.append("full CHANGE_MUSIC load-apply metrics must have zero mismatches")
        applied = load_apply_summary.get("applied_stream_totals", {})
        if int(applied.get("streams", 0)) <= 0 or int(applied.get("blocks", 0)) <= 0 or int(applied.get("bytes", 0)) <= 0:
            errors.append("full CHANGE_MUSIC load-apply must apply streams, blocks, and bytes")
        if int(applied.get("errors", -1)) != 0:
            errors.append("full CHANGE_MUSIC load-apply must have zero apply errors")

    for item in contract.get("evidence", []):
        if not item.get("exists"):
            errors.append(f"evidence path missing: {item.get('path')}")
    return errors


def main() -> int:
    args = parse_args()
    contract = json.loads(Path(args.contract).read_text(encoding="utf-8"))
    errors = validate(contract, require_frontier=args.require_frontier, require_smp_smoke=args.require_smp_smoke)
    if errors:
        print("Audio CPU/APU mailbox contract validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    summary = contract["current_frontier_summary"]
    print(
        "Audio CPU/APU mailbox contract validation OK: "
        f"{summary['capture_count']} captures, "
        f"{summary['command_read_count']} command reads, "
        f"{contract.get('current_ares_smp_smoke_summary', {}).get('key_on_count', 0)} smp-smoke key-on"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
