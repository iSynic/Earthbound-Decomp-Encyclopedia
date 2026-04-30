#!/usr/bin/env python3
"""Collect full CHANGE_MUSIC -> real C0:AB06 live-driver fusion evidence."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import rom_tools
from collect_audio_c0ab06_continuous_track_load_frontier import expected_track_ram, payload_regions
from collect_audio_c0ab06_real_ipl_frontier import DEFAULT_IPL
from run_audio_c0ab06_loader_handshake_corpus import (
    DEFAULT_EXE,
    DEFAULT_LOADER_CONTRACT,
    DEFAULT_LOADER_FILE,
    DEFAULT_PACK_CONTRACT,
    load_json,
    pack_pointer_map,
    write_json,
)


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT = (
    ROOT
    / "build"
    / "audio"
    / "c0ab06-change-music-fusion-frontier"
    / "c0ab06-change-music-fusion-frontier.json"
)
BOOTSTRAP_PACK_ID = 1
SPC_SIGNATURE = b"SNES-SPC700 Sound File Data v0.30"
DSP_OFFSET = 0x10100
DSP_KON = 0x4C
DSP_KOF = 0x5C


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Collect full CHANGE_MUSIC / real C0:AB06 fusion evidence.")
    parser.add_argument("--rom", help="Optional explicit EarthBound US ROM path.")
    parser.add_argument("--exe", default=str(DEFAULT_EXE), help="Built C0:AB06 loader handshake executable.")
    parser.add_argument("--loader-file", default=str(DEFAULT_LOADER_FILE), help="C0:AB06 routine fixture.")
    parser.add_argument("--loader-contract", default=str(DEFAULT_LOADER_CONTRACT), help="C0:AB06 loader contract JSON.")
    parser.add_argument("--pack-contract", default=str(DEFAULT_PACK_CONTRACT), help="Audio pack contract JSON.")
    parser.add_argument("--ipl-file", default=str(DEFAULT_IPL), help="ares Super Famicom IPL ROM.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Ignored frontier JSON.")
    parser.add_argument("--all-tracks", action="store_true", help="Run every CHANGE_MUSIC track in the audio pack contract instead of the representative loader-contract corpus.")
    parser.add_argument("--limit", type=int, help="Optional track limit for debugging.")
    parser.add_argument(
        "--command-write-smp-burst",
        type=int,
        default=0,
        help="Immediate SMP instructions to run after the final C0:ABBD APUIO0 write before the post-command observation loop.",
    )
    return parser.parse_args()


def run_fusion(
    exe: Path,
    loader_file: Path,
    rom_path: Path,
    ipl_file: Path,
    bootstrap: dict[str, Any],
    track_id: int,
    first_sequence_pointer: dict[str, Any],
    apu_ram_out: Path,
    snapshot_out: Path,
    command_write_smp_burst: int,
) -> dict[str, Any]:
    command = [
        str(exe),
        "--receiver",
        "ares_smp_ipl",
        "--bootstrap-bank",
        f"0x{int(bootstrap['bank']):02X}",
        "--bootstrap-address",
        f"0x{int(bootstrap['address']):04X}",
        "--change-music-track",
        f"0x{track_id:02X}",
        "--ipl-file",
        str(ipl_file),
        "--loader-file",
        str(loader_file),
        "--rom-file",
        str(rom_path),
        "--stream-bank",
        f"0x{int(first_sequence_pointer['bank']):02X}",
        "--stream-address",
        f"0x{int(first_sequence_pointer['address']):04X}",
        "--apu-ram-out",
        str(apu_ram_out),
        "--snapshot-out",
        str(snapshot_out),
        "--command-write-smp-burst",
        str(command_write_smp_burst),
    ]
    completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
    try:
        handshake = json.loads(completed.stdout)
    except json.JSONDecodeError as error:
        handshake = {
            "schema": "earthbound-decomp.c0ab06-loader-handshake.v1",
            "parse_error": str(error),
            "stdout": completed.stdout,
        }
    return {
        "returncode": completed.returncode,
        "stderr": completed.stderr.strip(),
        "handshake": handshake,
    }


def sha1(data: bytes) -> str:
    return hashlib.sha1(data).hexdigest()


def snapshot_metadata(path: Path) -> dict[str, Any]:
    data = path.read_bytes()
    ram = data[0x100:0x10100] if len(data) >= 0x10100 else b""
    dsp = data[DSP_OFFSET:DSP_OFFSET + 128] if len(data) >= DSP_OFFSET + 128 else b""
    return {
        "path": str(path),
        "bytes": len(data),
        "sha1": sha1(data),
        "signature_ok": data.startswith(SPC_SIGNATURE),
        "pc": f"0x{data[0x26]:02X}{data[0x25]:02X}" if len(data) > 0x26 else None,
        "a": f"0x{data[0x27]:02X}" if len(data) > 0x27 else None,
        "x": f"0x{data[0x28]:02X}" if len(data) > 0x28 else None,
        "y": f"0x{data[0x29]:02X}" if len(data) > 0x29 else None,
        "psw": f"0x{data[0x2A]:02X}" if len(data) > 0x2A else None,
        "sp": f"0x{data[0x2B]:02X}" if len(data) > 0x2B else None,
        "ram_sha1": sha1(ram) if len(ram) == 65536 else None,
        "dsp_register_sha1": sha1(dsp) if len(dsp) == 128 else None,
        "dsp_nonzero_count": sum(1 for byte in dsp if byte) if len(dsp) == 128 else None,
        "kon": f"0x{data[DSP_OFFSET + DSP_KON]:02X}" if len(data) > DSP_OFFSET + DSP_KON else None,
        "kof": f"0x{data[DSP_OFFSET + DSP_KOF]:02X}" if len(data) > DSP_OFFSET + DSP_KOF else None,
    }


def load_path_ok(record: dict[str, Any]) -> bool:
    handshake = record.get("handshake") or {}
    bootstrap = handshake.get("bootstrap") or {}
    change_music = handshake.get("change_music") or {}
    expected_pack_ids = record.get("expected_sequence_pack_ids", [])
    payload_regions = record.get("payload_regions") or {}
    return (
        bool(bootstrap.get("ok"))
        and change_music.get("final_pc") == "0x008004"
        and int(change_music.get("command_writes", -1)) == 1
        and int(change_music.get("load_calls", -1)) == len(expected_pack_ids)
        and bool(change_music.get("reached_command_read_pc_062a"))
        and bool(change_music.get("reached_zero_ack_shape"))
        and bool(payload_regions.get("payload_regions_match"))
    )


def safe_name(text: str) -> str:
    return "".join(ch.lower() if ch.isalnum() or ch in "-_" else "_" for ch in text)


def representative_records(loader_contract: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        {
            "job_id": record["job_id"],
            "track_id": int(record["track_id"]),
            "track_name": record.get("track_name"),
            "stream_pack_ids": [int(stream["pack_id"]) for stream in record.get("streams", [])],
        }
        for record in loader_contract.get("records", [])
    ]


def all_track_records(pack_contract: dict[str, Any]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for track in pack_contract.get("tracks", []):
        track_id = int(track["track_id"])
        load_order = track.get("load_order", [])
        if track_id == 0 or not load_order:
            continue
        track_name = str(track.get("name") or f"track_{track_id:03d}")
        records.append(
            {
                "job_id": f"fusion-track-{track_id:03d}-{safe_name(track_name)}",
                "track_id": track_id,
                "track_name": track_name,
                "stream_pack_ids": [int(item["pack_id"]) for item in load_order],
            }
        )
    return records


def main() -> int:
    args = parse_args()
    exe = Path(args.exe)
    loader_file = Path(args.loader_file)
    ipl_file = Path(args.ipl_file)
    if not exe.exists():
        raise FileNotFoundError(f"missing C0:AB06 loader executable: {exe}")
    if not loader_file.exists():
        raise FileNotFoundError(f"missing C0:AB06 loader fixture: {loader_file}")
    if not ipl_file.exists():
        raise FileNotFoundError(f"missing SFC IPL ROM: {ipl_file}")

    rom_path = rom_tools.find_rom(args.rom)
    rom = rom_tools.load_rom(rom_path)
    loader_contract = load_json(Path(args.loader_contract))
    pack_contract = load_json(Path(args.pack_contract))
    pointer_by_pack = pack_pointer_map(pack_contract)
    bootstrap = pointer_by_pack[BOOTSTRAP_PACK_ID]
    records = all_track_records(pack_contract) if args.all_tracks else representative_records(loader_contract)
    if args.limit is not None:
        records = records[: args.limit]

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    out_records: list[dict[str, Any]] = []
    for record in records:
        stream_pack_ids = [int(pack_id) for pack_id in record.get("stream_pack_ids", [])]
        if not stream_pack_ids:
            raise ValueError(f"{record.get('job_id')}: empty stream pack sequence")
        expected = expected_track_ram(rom, pointer_by_pack, stream_pack_ids)
        safe_job = str(record["job_id"]).replace("/", "_")
        apu_ram_out = output.parent / f"{safe_job}-change-music-fusion-apu-ram.bin"
        snapshot_out = output.parent / f"{safe_job}-change-music-fusion-last-keyon.spc"
        run = run_fusion(
            exe,
            loader_file,
            rom_path,
            ipl_file,
            bootstrap,
            int(record["track_id"]),
            pointer_by_pack[stream_pack_ids[0]],
            apu_ram_out,
            snapshot_out,
            args.command_write_smp_burst,
        )
        run["expected_apu_ram"] = expected
        run["payload_regions"] = payload_regions(apu_ram_out, expected) if apu_ram_out.exists() else None
        run["snapshot"] = snapshot_metadata(snapshot_out) if snapshot_out.exists() else None
        run["job_id"] = record["job_id"]
        run["track_id"] = int(record["track_id"])
        run["track_name"] = record.get("track_name")
        run["expected_sequence_pack_ids"] = stream_pack_ids
        change_music = (run.get("handshake") or {}).get("change_music") or {}
        run["actual_sequence_pointers"] = [
            {"bank": step.get("bank"), "address": step.get("address")}
            for step in change_music.get("load_steps", [])
        ]
        run["load_path_ok"] = load_path_ok(run)
        run["reached_key_on_after_ack"] = bool(change_music.get("reached_key_on_after_ack"))
        status = (
            "ok"
            if run["load_path_ok"] and run["reached_key_on_after_ack"]
            else "load_ok_no_keyon"
            if run["load_path_ok"]
            else f"failed({run['returncode']})"
        )
        print(f"- {record['job_id']}: {status}")
        out_records.append(run)

    match_count = sum(1 for record in out_records if (record.get("payload_regions") or {}).get("payload_regions_match"))
    success_count = sum(1 for record in out_records if int(record.get("returncode", -1)) == 0)
    load_path_success_count = sum(1 for record in out_records if record.get("load_path_ok"))
    key_on_count = sum(1 for record in out_records if record.get("reached_key_on_after_ack"))
    snapshot_count = sum(1 for record in out_records if (record.get("snapshot") or {}).get("signature_ok"))
    summary = {
        "schema": "earthbound-decomp.c0ab06-change-music-fusion-frontier.v1",
        "status": "full_change_music_invokes_real_c0ab06_against_live_driver",
        "source_policy": loader_contract.get("source_policy"),
        "corpus": "all_change_music_tracks" if args.all_tracks else "representative_backend_tracks",
        "remaining_shortcut": "The fused CHANGE_MUSIC/C0:AB06 run still starts from a harness-booted audio subsystem and uses a bounded post-command SMP drain; the next gate is natural CPU/APU command timing in a fuller scheduled runtime.",
        "post_command_timing": {
            "command_write_smp_burst": args.command_write_smp_burst,
            "post_command_observation": "SMP instructions are observed one at a time after ChangeMusic returns; command-read, zero-ack, and key-on steps are recorded relative to that loop.",
        },
        "loader_contract": str(Path(args.loader_contract)),
        "pack_contract": str(Path(args.pack_contract)),
        "handshake_executable": str(exe),
        "loader_fixture": str(loader_file),
        "ipl_file": str(ipl_file),
        "job_count": len(out_records),
        "success_count": success_count,
        "load_path_success_count": load_path_success_count,
        "key_on_count": key_on_count,
        "payload_region_match_count": match_count,
        "snapshot_count": snapshot_count,
        "no_key_on_count": len(out_records) - key_on_count,
        "mismatch_count": len(out_records) - min(load_path_success_count, match_count),
        "records": out_records,
    }
    write_json(output, summary)
    print(
        "C0:AB06 CHANGE_MUSIC fusion frontier: "
        f"{success_count} / {len(out_records)} runs ok, "
        f"{match_count} / {len(out_records)} payload-region matches"
    )
    print(f"Wrote {output}")
    return 0 if summary["mismatch_count"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
