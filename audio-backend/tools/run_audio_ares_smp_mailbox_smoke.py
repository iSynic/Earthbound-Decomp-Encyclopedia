#!/usr/bin/env python3
"""Run the real ares SMP mailbox smoke across representative audio jobs."""

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


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUT = ROOT / "build" / "audio" / "ares-smp-mailbox-smoke-jobs"
DEFAULT_SMOKE_EXE = (
    ROOT
    / "build"
    / "audio"
    / "ares-smp-mailbox-smoke-msvc"
    / "RelWithDebInfo"
    / "earthbound_ares_smp_mailbox_smoke.exe"
)
DEFAULT_CPU_ROUTINE_FILE = ROOT / "build" / "audio" / "cpu-routine-fixtures" / "c0-abbd-send-apu-port0-command-byte.bin"
DEFAULT_CPU_TAIL_FILE = ROOT / "build" / "audio" / "cpu-routine-fixtures" / "c4-fd0e-change-music-tail-send-track-command.bin"
DEFAULT_CHANGE_MUSIC_FILE = ROOT / "build" / "audio" / "cpu-routine-fixtures" / "c4-fbbd-change-music.bin"
DEFAULT_CHANGE_MUSIC_HELPER_FILE = ROOT / "build" / "audio" / "cpu-routine-fixtures" / "c4-fb42-change-music-helpers.bin"
DEFAULT_MUSIC_DATASET_FILE = ROOT / "build" / "audio" / "cpu-routine-fixtures" / "c4-f70a-music-dataset-table.bin"
DEFAULT_MUSIC_PACK_POINTER_FILE = ROOT / "build" / "audio" / "cpu-routine-fixtures" / "c4-f947-music-pack-pointer-table.bin"
DEFAULT_BOOTSTRAP_CORPUS = ROOT / "build" / "audio" / "bootstrap-corpus" / "audio-bootstrap-snapshot-corpus.json"
DEFAULT_FIXTURES = ROOT / "build" / "audio" / "renderer-fixtures" / "audio-renderer-fixtures.json"
SPC_SIGNATURE = b"SNES-SPC700 Sound File Data v0.30"
DSP_OFFSET = 0x10100
DSP_KON = 0x4C
DSP_KOF = 0x5C


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run ares SMP mailbox smoke corpus.")
    parser.add_argument("--out", default=str(DEFAULT_OUT), help="Ignored output directory.")
    parser.add_argument("--smoke-exe", default=str(DEFAULT_SMOKE_EXE), help="Built ares SMP mailbox smoke executable.")
    parser.add_argument("--steps", type=int, default=200000, help="Instruction step limit per track.")
    parser.add_argument(
        "--delivery",
        choices=("smp_portwrite", "cpu_writeapu", "wdc65816_sta2140", "wdc65816_c0abbd", "wdc65816_rom_c0abbd", "wdc65816_rom_c0abbd_jsl", "wdc65816_change_music_tail", "wdc65816_full_change_music", "wdc65816_full_change_music_load_stub", "wdc65816_full_change_music_load_apply"),
        default="smp_portwrite",
        help="Command delivery path to exercise at the $062A command-read boundary.",
    )
    parser.add_argument("--cpu-routine-file", default=str(DEFAULT_CPU_ROUTINE_FILE), help="CPU routine byte fixture for wdc65816_rom_c0abbd delivery.")
    parser.add_argument("--cpu-tail-file", default=str(DEFAULT_CPU_TAIL_FILE), help="CPU tail byte fixture for wdc65816_change_music_tail delivery.")
    parser.add_argument("--change-music-file", default=str(DEFAULT_CHANGE_MUSIC_FILE), help="ChangeMusic byte fixture for wdc65816_full_change_music delivery.")
    parser.add_argument("--change-music-helper-file", default=str(DEFAULT_CHANGE_MUSIC_HELPER_FILE), help="ChangeMusic helper byte fixture for wdc65816_full_change_music_load_stub delivery.")
    parser.add_argument("--music-dataset-file", default=str(DEFAULT_MUSIC_DATASET_FILE), help="MusicDatasetTable byte fixture for wdc65816_full_change_music delivery.")
    parser.add_argument("--music-pack-pointer-file", default=str(DEFAULT_MUSIC_PACK_POINTER_FILE), help="MusicPackPointerTable byte fixture for wdc65816_full_change_music_load_stub delivery.")
    parser.add_argument("--rom", help="Optional explicit EarthBound US ROM path for load-apply delivery.")
    parser.add_argument("--apu-ram-corpus", default=str(DEFAULT_BOOTSTRAP_CORPUS), help="Bootstrap APU RAM corpus for load-apply delivery.")
    parser.add_argument("--fixtures", default=str(DEFAULT_FIXTURES), help="Renderer fixture index for backend job generation.")
    return parser.parse_args()


def run(command: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    print("+ " + " ".join(command))
    return subprocess.run(command, cwd=ROOT, check=check, text=True, capture_output=True)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def sha1(data: bytes) -> str:
    return hashlib.sha1(data).hexdigest()


def apu_ram_overrides(corpus_path: Path) -> dict[int, Path]:
    if not corpus_path.exists():
        return {}
    corpus = load_json(corpus_path)
    return {int(record["track_id"]): Path(record["ram_path"]) for record in corpus.get("tracks", [])}


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


def main() -> int:
    args = parse_args()
    out_dir = Path(args.out)
    smoke_exe = Path(args.smoke_exe)
    if not smoke_exe.exists():
        raise FileNotFoundError(f"missing ares SMP mailbox smoke executable: {smoke_exe}")
    cpu_routine_file = Path(args.cpu_routine_file)
    if args.delivery in ("wdc65816_rom_c0abbd", "wdc65816_rom_c0abbd_jsl", "wdc65816_change_music_tail", "wdc65816_full_change_music", "wdc65816_full_change_music_load_stub", "wdc65816_full_change_music_load_apply") and not cpu_routine_file.exists():
        raise FileNotFoundError(
            f"missing CPU routine fixture: {cpu_routine_file}; "
            "run tools/build_audio_cpu_routine_fixtures.py first"
        )
    cpu_tail_file = Path(args.cpu_tail_file)
    if args.delivery == "wdc65816_change_music_tail" and not cpu_tail_file.exists():
        raise FileNotFoundError(
            f"missing CPU tail fixture: {cpu_tail_file}; "
            "run tools/build_audio_cpu_routine_fixtures.py first"
        )
    change_music_file = Path(args.change_music_file)
    if args.delivery in ("wdc65816_full_change_music", "wdc65816_full_change_music_load_stub", "wdc65816_full_change_music_load_apply") and not change_music_file.exists():
        raise FileNotFoundError(
            f"missing ChangeMusic fixture: {change_music_file}; "
            "run tools/build_audio_cpu_routine_fixtures.py first"
        )
    change_music_helper_file = Path(args.change_music_helper_file)
    if args.delivery in ("wdc65816_full_change_music_load_stub", "wdc65816_full_change_music_load_apply") and not change_music_helper_file.exists():
        raise FileNotFoundError(
            f"missing ChangeMusic helper fixture: {change_music_helper_file}; "
            "run tools/build_audio_cpu_routine_fixtures.py first"
        )
    music_dataset_file = Path(args.music_dataset_file)
    if args.delivery in ("wdc65816_full_change_music", "wdc65816_full_change_music_load_stub", "wdc65816_full_change_music_load_apply") and not music_dataset_file.exists():
        raise FileNotFoundError(
            f"missing MusicDatasetTable fixture: {music_dataset_file}; "
            "run tools/build_audio_cpu_routine_fixtures.py first"
        )
    music_pack_pointer_file = Path(args.music_pack_pointer_file)
    if args.delivery in ("wdc65816_full_change_music_load_stub", "wdc65816_full_change_music_load_apply") and not music_pack_pointer_file.exists():
        raise FileNotFoundError(
            f"missing MusicPackPointerTable fixture: {music_pack_pointer_file}; "
            "run tools/build_audio_cpu_routine_fixtures.py first"
        )
    rom_path: Path | None = None
    override_apu_ram: dict[int, Path] = {}
    if args.delivery == "wdc65816_full_change_music_load_apply":
        rom_path = rom_tools.find_rom(args.rom)
        override_apu_ram = apu_ram_overrides(Path(args.apu_ram_corpus))
        if not override_apu_ram:
            raise FileNotFoundError(
                f"missing bootstrap APU RAM corpus: {args.apu_ram_corpus}; "
                "run tools/build_audio_bootstrap_snapshot_corpus.py first"
            )

    jobs_index_path = out_dir / "ares-jobs.json"
    run(
        [
            sys.executable,
            "tools/build_audio_backend_jobs.py",
            "--backend",
            "ares",
            "--out",
            str(out_dir),
            "--fixtures",
            str(Path(args.fixtures)),
        ]
    )
    jobs_index = load_json(jobs_index_path)

    records: list[dict[str, Any]] = []
    for job in jobs_index.get("jobs", []):
      fixture = load_json(Path(job["fixture_path"]))
      apu_ram_path = override_apu_ram.get(int(job["track_id"]), Path(fixture["apu_ram"]["path"]))
      job_out = Path(job["output_dir"])
      result_path = job_out / "smp-mailbox-smoke.json"
      snapshot_path = job_out / "ares-smp-mailbox-last-keyon.spc"
      command = int(job["track_id"]) & 0xFF
      completed = run(
          [
              str(smoke_exe),
              "--apu-ram",
              str(apu_ram_path),
              "--command",
              f"0x{command:02x}",
              "--steps",
              str(args.steps),
              "--inject-on-pc-062a",
              "--snapshot-out",
              str(snapshot_path),
          ]
          + (["--inject-via-cpu-apu-write"] if args.delivery == "cpu_writeapu" else [])
          + (["--inject-via-cpu-instruction"] if args.delivery == "wdc65816_sta2140" else [])
          + (["--inject-via-cpu-routine"] if args.delivery == "wdc65816_c0abbd" else [])
          + (["--inject-via-cpu-routine-file", "--cpu-routine-file", str(cpu_routine_file)] if args.delivery == "wdc65816_rom_c0abbd" else [])
          + (["--inject-via-cpu-routine-file-jsl", "--cpu-routine-file", str(cpu_routine_file)] if args.delivery == "wdc65816_rom_c0abbd_jsl" else [])
          + (["--inject-via-change-music-tail", "--cpu-routine-file", str(cpu_routine_file), "--cpu-tail-file", str(cpu_tail_file)] if args.delivery == "wdc65816_change_music_tail" else [])
          + ([
              "--inject-via-full-change-music",
              "--cpu-routine-file",
              str(cpu_routine_file),
              "--change-music-file",
              str(change_music_file),
              "--music-dataset-file",
              str(music_dataset_file),
          ] if args.delivery == "wdc65816_full_change_music" else [])
          + ([
              "--inject-via-full-change-music",
              "--full-change-music-run-load-path",
              "--cpu-routine-file",
              str(cpu_routine_file),
              "--change-music-file",
              str(change_music_file),
              "--change-music-helper-file",
              str(change_music_helper_file),
              "--music-dataset-file",
              str(music_dataset_file),
              "--music-pack-pointer-file",
              str(music_pack_pointer_file),
          ] if args.delivery == "wdc65816_full_change_music_load_stub" else [])
          + ([
              "--inject-via-full-change-music",
              "--full-change-music-run-load-path",
              "--apply-load-spc700-data-streams",
              "--rom-file",
              str(rom_path),
              "--cpu-routine-file",
              str(cpu_routine_file),
              "--change-music-file",
              str(change_music_file),
              "--change-music-helper-file",
              str(change_music_helper_file),
              "--music-dataset-file",
              str(music_dataset_file),
              "--music-pack-pointer-file",
              str(music_pack_pointer_file),
          ] if args.delivery == "wdc65816_full_change_music_load_apply" else []),
          check=False,
      )
      try:
          smoke = json.loads(completed.stdout)
      except json.JSONDecodeError as error:
          smoke = {
              "schema": "earthbound-decomp.ares-smp-mailbox-smoke.v1",
              "parse_error": str(error),
              "stdout": completed.stdout,
          }
      record = {
          "job_id": job["job_id"],
          "track_id": int(job["track_id"]),
          "track_name": job["track_name"],
          "returncode": completed.returncode,
          "stderr": completed.stderr.strip(),
          "result_path": str(result_path),
          "smoke": smoke,
          "snapshot": snapshot_metadata(snapshot_path) if snapshot_path.exists() else None,
      }
      write_json(result_path, record)
      status = "ok" if completed.returncode == 0 else f"failed({completed.returncode})"
      print(f"- {job['job_id']}: {status}")
      records.append(record)

    summary = {
        "schema": "earthbound-decomp.ares-smp-mailbox-smoke-summary.v1",
        "status": f"real_ares_{args.delivery}_mailbox_smoke",
        "delivery": args.delivery,
        "source_jobs": str(jobs_index_path),
        "smoke_executable": str(smoke_exe),
        "job_count": len(records),
        "success_count": sum(1 for record in records if record["returncode"] == 0),
        "command_read_count": sum(1 for record in records if record["smoke"].get("reached_command_read_pc_062a")),
        "zero_ack_count": sum(1 for record in records if record["smoke"].get("reached_zero_ack_shape")),
        "key_on_count": sum(1 for record in records if record["smoke"].get("reached_key_on_after_ack")),
        "snapshot_count": sum(1 for record in records if record.get("snapshot")),
        "records": records,
    }
    summary_path = out_dir / "smp-mailbox-smoke-summary.json"
    write_json(summary_path, summary)
    print(
        "ares SMP mailbox smoke summary: "
        f"{summary['success_count']} / {summary['job_count']} ok, "
        f"{summary['key_on_count']} key-on, "
        f"{summary['snapshot_count']} snapshots"
    )
    print(f"Wrote {summary_path}")
    return 0 if summary["success_count"] == summary["job_count"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
