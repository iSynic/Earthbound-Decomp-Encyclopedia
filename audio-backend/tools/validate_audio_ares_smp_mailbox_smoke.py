#!/usr/bin/env python3
"""Validate the ares SMP mailbox smoke corpus."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SUMMARY = ROOT / "build" / "audio" / "ares-smp-mailbox-smoke-jobs" / "smp-mailbox-smoke-summary.json"
ALLOWED_DELIVERY_MODES = {
    "ares_smp_portwrite_on_pc_062a",
    "ares_cpu_writeapu_2140_on_pc_062a",
    "ares_wdc65816_sta_2140_on_pc_062a",
    "ares_wdc65816_full_c0abbd_on_pc_062a",
    "ares_wdc65816_rom_c0abbd_on_pc_062a",
    "ares_wdc65816_rom_c0abbd_jsl_on_pc_062a",
    "ares_wdc65816_change_music_tail_on_pc_062a",
    "ares_wdc65816_full_change_music_on_pc_062a",
    "ares_wdc65816_full_change_music_load_stub_on_pc_062a",
    "ares_wdc65816_full_change_music_load_apply_on_pc_062a",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate ares SMP mailbox smoke summary.")
    parser.add_argument("summary", nargs="?", default=str(DEFAULT_SUMMARY))
    parser.add_argument(
        "--require-delivery-mode",
        choices=sorted(ALLOWED_DELIVERY_MODES),
        help="Require every record to use this exact command delivery mode.",
    )
    return parser.parse_args()


def validate(summary: dict, *, require_delivery_mode: str | None) -> list[str]:
    errors: list[str] = []
    if summary.get("schema") != "earthbound-decomp.ares-smp-mailbox-smoke-summary.v1":
        errors.append(f"unexpected schema: {summary.get('schema')}")
    records = summary.get("records", [])
    job_count = int(summary.get("job_count", -1))
    if job_count != len(records):
        errors.append(f"job_count {job_count} does not match {len(records)} records")
    for field in ("success_count", "command_read_count", "zero_ack_count", "key_on_count"):
        if int(summary.get(field, 0)) != job_count:
            errors.append(f"{field} does not match job_count")
    if int(summary.get("snapshot_count", 0)) != job_count:
        errors.append("snapshot_count does not match job_count")
    seen: set[str] = set()
    for record in records:
        job_id = str(record.get("job_id", ""))
        if not job_id:
            errors.append("record without job_id")
        elif job_id in seen:
            errors.append(f"duplicate job_id {job_id}")
        seen.add(job_id)
        if int(record.get("returncode", -1)) != 0:
            errors.append(f"{job_id}: nonzero return code {record.get('returncode')}")
        smoke = record.get("smoke", {})
        delivery_mode = smoke.get("command_delivery_mode")
        if delivery_mode not in ALLOWED_DELIVERY_MODES:
            errors.append(f"{job_id}: unexpected delivery mode {delivery_mode}")
        if require_delivery_mode and delivery_mode != require_delivery_mode:
            errors.append(f"{job_id}: delivery mode {delivery_mode} does not match required {require_delivery_mode}")
        if delivery_mode in (
            "ares_wdc65816_sta_2140_on_pc_062a",
            "ares_wdc65816_full_c0abbd_on_pc_062a",
            "ares_wdc65816_rom_c0abbd_on_pc_062a",
            "ares_wdc65816_rom_c0abbd_jsl_on_pc_062a",
            "ares_wdc65816_change_music_tail_on_pc_062a",
            "ares_wdc65816_full_change_music_on_pc_062a",
            "ares_wdc65816_full_change_music_load_stub_on_pc_062a",
        ):
            probe = smoke.get("cpu_instruction_probe") or {}
            if not probe.get("ok"):
                errors.append(f"{job_id}: CPU instruction probe did not report ok")
            expected_routine = (
                "full_C0ABBD_sep_sta_rep_rtl"
                if delivery_mode == "ares_wdc65816_full_c0abbd_on_pc_062a"
                else "rom_fixture_ChangeMusic_full_load_path_applied_loader"
                if delivery_mode == "ares_wdc65816_full_change_music_load_apply_on_pc_062a"
                else "rom_fixture_ChangeMusic_full_load_path_stubbed_loader"
                if delivery_mode == "ares_wdc65816_full_change_music_load_stub_on_pc_062a"
                else "rom_fixture_ChangeMusic_full_presatisfied_packs"
                if delivery_mode == "ares_wdc65816_full_change_music_on_pc_062a"
                else "rom_fixture_ChangeMusic_tail_to_C0ABBD"
                if delivery_mode == "ares_wdc65816_change_music_tail_on_pc_062a"
                else "rom_fixture_C0ABBD_jsl_call_context"
                if delivery_mode == "ares_wdc65816_rom_c0abbd_jsl_on_pc_062a"
                else "rom_fixture_C0ABBD_sep_sta_long_rep_rtl"
                if delivery_mode == "ares_wdc65816_rom_c0abbd_on_pc_062a"
                else "sep_20_sta_002140_prefix_of_C0ABBD"
            )
            if probe.get("routine") != expected_routine:
                errors.append(f"{job_id}: unexpected CPU instruction routine {probe.get('routine')}")
            if int(probe.get("writes_to_2140", 0)) != 1:
                errors.append(f"{job_id}: CPU instruction probe did not write exactly once to $2140")
            if probe.get("last_write_data") != smoke.get("command"):
                errors.append(f"{job_id}: CPU instruction probe write data does not match command")
            if delivery_mode == "ares_wdc65816_rom_c0abbd_jsl_on_pc_062a" and not probe.get("call_through_jsl"):
                errors.append(f"{job_id}: CPU instruction probe did not report JSL call context")
            if delivery_mode == "ares_wdc65816_change_music_tail_on_pc_062a":
                if not probe.get("call_through_change_music_tail"):
                    errors.append(f"{job_id}: CPU instruction probe did not report ChangeMusic tail context")
                if int(probe.get("change_music_tail_bytes", 0)) <= 0:
                    errors.append(f"{job_id}: CPU instruction probe did not report ChangeMusic tail bytes")
            if delivery_mode in (
                "ares_wdc65816_full_change_music_on_pc_062a",
                "ares_wdc65816_full_change_music_load_stub_on_pc_062a",
                "ares_wdc65816_full_change_music_load_apply_on_pc_062a",
            ):
                if not probe.get("call_through_full_change_music"):
                    errors.append(f"{job_id}: CPU instruction probe did not report full ChangeMusic context")
                if int(probe.get("change_music_bytes", 0)) <= 0:
                    errors.append(f"{job_id}: CPU instruction probe did not report ChangeMusic bytes")
                if int(probe.get("music_dataset_bytes", 0)) <= 0:
                    errors.append(f"{job_id}: CPU instruction probe did not report MusicDatasetTable bytes")
            if delivery_mode == "ares_wdc65816_full_change_music_load_stub_on_pc_062a":
                if probe.get("pre_satisfy_change_music_packs"):
                    errors.append(f"{job_id}: full ChangeMusic load-path probe unexpectedly pre-satisfied packs")
                if int(probe.get("change_music_helper_bytes", 0)) <= 0:
                    errors.append(f"{job_id}: CPU instruction probe did not report ChangeMusic helper bytes")
                if int(probe.get("music_pack_pointer_bytes", 0)) <= 0:
                    errors.append(f"{job_id}: CPU instruction probe did not report MusicPackPointerTable bytes")
                if int(probe.get("load_spc700_data_stub_calls", 0)) <= 0:
                    errors.append(f"{job_id}: CPU instruction probe did not call LOAD_SPC700_DATA stub")
                if len(probe.get("load_spc700_data_stub_args", [])) != int(probe.get("load_spc700_data_stub_calls", 0)):
                    errors.append(f"{job_id}: LOAD_SPC700_DATA stub arg count does not match call count")
            if delivery_mode == "ares_wdc65816_full_change_music_load_apply_on_pc_062a":
                if probe.get("pre_satisfy_change_music_packs"):
                    errors.append(f"{job_id}: full ChangeMusic load-apply probe unexpectedly pre-satisfied packs")
                if int(probe.get("change_music_helper_bytes", 0)) <= 0:
                    errors.append(f"{job_id}: CPU instruction probe did not report ChangeMusic helper bytes")
                if int(probe.get("music_pack_pointer_bytes", 0)) <= 0:
                    errors.append(f"{job_id}: CPU instruction probe did not report MusicPackPointerTable bytes")
                if int(probe.get("load_spc700_data_stub_calls", 0)) <= 0:
                    errors.append(f"{job_id}: CPU instruction probe did not call LOAD_SPC700_DATA stub")
                if len(probe.get("load_spc700_data_stub_args", [])) != int(probe.get("load_spc700_data_stub_calls", 0)):
                    errors.append(f"{job_id}: LOAD_SPC700_DATA stub arg count does not match call count")
                if not probe.get("load_spc700_data_apply_streams"):
                    errors.append(f"{job_id}: LOAD_SPC700_DATA apply mode was not enabled")
                if int(probe.get("load_spc700_data_apply_errors", -1)) != 0:
                    errors.append(f"{job_id}: LOAD_SPC700_DATA apply errors were reported")
                if int(probe.get("load_spc700_data_applied_streams", 0)) != int(probe.get("load_spc700_data_stub_calls", 0)):
                    errors.append(f"{job_id}: applied stream count does not match stub calls")
                if int(probe.get("load_spc700_data_applied_blocks", 0)) <= 0:
                    errors.append(f"{job_id}: no LOAD_SPC700_DATA payload blocks were applied")
        if not smoke.get("reached_command_read_pc_062a"):
            errors.append(f"{job_id}: did not reach command read PC")
        if not smoke.get("reached_zero_ack_shape"):
            errors.append(f"{job_id}: did not reach zero ack shape")
        if not smoke.get("reached_key_on_after_ack"):
            errors.append(f"{job_id}: did not reach key-on after ack")
        if int(smoke.get("command_injection_step", -1)) != int(smoke.get("command_read_step", -2)):
            errors.append(f"{job_id}: command injection step does not match command read step")
        snapshot = record.get("snapshot") or {}
        if not snapshot:
            errors.append(f"{job_id}: missing snapshot metadata")
        elif not snapshot.get("signature_ok"):
            errors.append(f"{job_id}: snapshot signature is invalid")
        elif snapshot.get("kon") in (None, "0x00"):
            errors.append(f"{job_id}: snapshot KON is not set")
    return errors


def main() -> int:
    args = parse_args()
    summary = json.loads(Path(args.summary).read_text(encoding="utf-8"))
    errors = validate(summary, require_delivery_mode=args.require_delivery_mode)
    if errors:
        print("ares SMP mailbox smoke validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "ares SMP mailbox smoke validation OK: "
        f"{summary['success_count']} / {summary['job_count']} ok, "
        f"{summary['key_on_count']} key-on, "
        f"{summary.get('snapshot_count', 0)} snapshots"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
