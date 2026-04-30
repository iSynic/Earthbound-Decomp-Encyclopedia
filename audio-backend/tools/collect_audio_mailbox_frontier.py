#!/usr/bin/env python3
"""Collect the diagnostic CPU/APU mailbox transcript around track command read."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_JOBS = ROOT / "build" / "audio" / "command-on-first-read-jobs" / "ares-jobs.json"
DEFAULT_OUTPUT = ROOT / "build" / "audio" / "command-on-first-read-jobs" / "mailbox-frontier.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Collect diagnostic audio mailbox frontier.")
    parser.add_argument("--jobs", default=str(DEFAULT_JOBS), help="ares backend job index.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Output frontier JSON path.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def hex_byte(value: int) -> str:
    return f"0x{value & 0xFF:02X}"


def first_after(events: list[dict[str, Any]], *, sequence: int, kind: str, address: str) -> dict[str, Any] | None:
    for event in events:
        if event.get("kind") == kind and event.get("address") == address and int(event.get("sequence", 0)) > sequence:
            return event
    return None


def collect(jobs_index: dict[str, Any]) -> dict[str, Any]:
    records: list[dict[str, Any]] = []
    mode_counts: Counter[str] = Counter()
    first_read_pc_counts: Counter[str] = Counter()
    first_ack_pc_counts: Counter[str] = Counter()
    command_read_count = 0
    command_match_count = 0
    io_window_count = 0
    zero_ack_count = 0
    keyon_after_read_count = 0

    for job in jobs_index.get("jobs", []):
        capture_path = Path(job["output_dir"]) / "ares-state-capture.json"
        record: dict[str, Any] = {
            "job_id": job["job_id"],
            "track_id": int(job["track_id"]),
            "track_name": job["track_name"],
            "capture_path": str(capture_path),
            "capture_exists": capture_path.exists(),
            "mode": None,
            "expected_track_command": hex_byte(int(job["track_id"])),
            "host_command": None,
            "command_matches_track_id": False,
            "host_command_injection": None,
            "first_command_read": None,
            "first_port0_write_after_read": None,
            "port0_reads_after_read_count": 0,
            "port0_writes_after_read_count": 0,
            "io_window_event_count": 0,
            "io_window_pre_read_count": 0,
            "io_window_post_read_count": 0,
            "keyon_after_command_read": False,
            "last_keyon_instruction": None,
        }
        if not capture_path.exists():
            records.append(record)
            continue

        capture = load_json(capture_path)
        probe = capture.get("spc700_entry_execution_probe", {})
        mode = str(probe.get("diagnostic_host_port0_preseed_mode", "unknown"))
        host_command = probe.get("diagnostic_host_port0_command")
        injection = probe.get("diagnostic_host_port0_injection")
        first_read = probe.get("diagnostic_host_port0_first_read")
        io_window = probe.get("diagnostic_host_port0_io_window", [])
        last_keyon = probe.get("last_key_on_snapshot", {})
        last_keyon_instruction = last_keyon.get("instruction")

        mode_counts[mode] += 1
        if io_window:
            io_window_count += 1
        if first_read:
            command_read_count += 1
            first_read_pc_counts[str(first_read.get("pc"))] += 1
        if host_command == record["expected_track_command"]:
            command_match_count += 1

        first_read_sequence = int(first_read.get("sequence", 0)) if first_read else 0
        ack_write = first_after(io_window, sequence=first_read_sequence, kind="write", address="0x00F4")
        if ack_write:
            first_ack_pc_counts[str(ack_write.get("pc"))] += 1
            if ack_write.get("data") == "0x00":
                zero_ack_count += 1

        port0_reads_after_read = [
            event
            for event in io_window
            if event.get("kind") == "read"
            and event.get("address") == "0x00F4"
            and int(event.get("sequence", 0)) >= first_read_sequence
        ]
        port0_writes_after_read = [
            event
            for event in io_window
            if event.get("kind") == "write"
            and event.get("address") == "0x00F4"
            and int(event.get("sequence", 0)) > first_read_sequence
        ]
        pre_read_count = sum(1 for event in io_window if int(event.get("sequence", 0)) < first_read_sequence)
        post_read_count = sum(1 for event in io_window if int(event.get("sequence", 0)) >= first_read_sequence)
        keyon_after_read = (
            first_read is not None
            and last_keyon_instruction is not None
            and int(last_keyon_instruction) >= int(first_read.get("instruction", 0))
        )
        if keyon_after_read:
            keyon_after_read_count += 1

        record.update(
            {
                "mode": mode,
                "host_command": host_command,
                "command_matches_track_id": host_command == record["expected_track_command"],
                "host_command_injection": injection,
                "first_command_read": first_read,
                "first_port0_write_after_read": ack_write,
                "port0_reads_after_read_count": len(port0_reads_after_read),
                "port0_writes_after_read_count": len(port0_writes_after_read),
                "io_window_event_count": len(io_window),
                "io_window_pre_read_count": pre_read_count,
                "io_window_post_read_count": post_read_count,
                "keyon_after_command_read": keyon_after_read,
                "last_keyon_instruction": last_keyon_instruction,
                "io_window": io_window,
            }
        )
        records.append(record)

    return {
        "schema": "earthbound-decomp.audio-mailbox-frontier.v1",
        "status": "diagnostic_track_command_mailbox_transcript",
        "source_jobs": jobs_index.get("path", str(DEFAULT_JOBS)),
        "job_count": len(records),
        "summary": {
            "mode_counts": dict(sorted(mode_counts.items())),
            "capture_count": sum(1 for record in records if record["capture_exists"]),
            "io_window_count": io_window_count,
            "command_read_count": command_read_count,
            "command_match_count": command_match_count,
            "zero_ack_write_count": zero_ack_count,
            "keyon_after_command_read_count": keyon_after_read_count,
            "first_read_pc_counts": dict(sorted(first_read_pc_counts.items())),
            "first_ack_pc_counts": dict(sorted(first_ack_pc_counts.items())),
        },
        "interpretation": {
            "claim": "The diagnostic harness now records the ordered APU IO neighborhood around the first driver read of the CPU track command.",
            "next_use": "Use this transcript to replace diagnostic APUIO0 delivery with the real CPU/APU mailbox path while preserving the same command-read, ack-write, and key-on ordering.",
        },
        "records": records,
    }


def render_markdown(frontier: dict[str, Any]) -> str:
    summary = frontier["summary"]
    rows = [
        "| `{job_id}` | {track_id} | `{track_name}` | `{command}` | `{read_pc}` | `{ack_pc}` | `{ack}` | {reads} | {keyon} |".format(
            job_id=record["job_id"],
            track_id=record["track_id"],
            track_name=record["track_name"],
            command=record.get("host_command"),
            read_pc=(record.get("first_command_read") or {}).get("pc"),
            ack_pc=(record.get("first_port0_write_after_read") or {}).get("pc"),
            ack=(record.get("first_port0_write_after_read") or {}).get("data"),
            reads=record.get("port0_reads_after_read_count", 0),
            keyon="yes" if record.get("keyon_after_command_read") else "no",
        )
        for record in frontier["records"]
    ]
    return "\n".join(
        [
            "# Audio Mailbox Frontier",
            "",
            "Status: diagnostic CPU/APU track-command mailbox transcript.",
            "",
            f"- captures: `{summary['capture_count']} / {frontier['job_count']}`",
            f"- modes: `{summary['mode_counts']}`",
            f"- IO windows: `{summary['io_window_count']}`",
            f"- command reads: `{summary['command_read_count']}`",
            f"- commands matching track id: `{summary['command_match_count']}`",
            f"- zero ack writes: `{summary['zero_ack_write_count']}`",
            f"- key-on after command read: `{summary['keyon_after_command_read_count']}`",
            f"- first read PCs: `{summary['first_read_pc_counts']}`",
            f"- first ack PCs: `{summary['first_ack_pc_counts']}`",
            "",
            "## Tracks",
            "",
            "| Job | Track | Name | Command | First Read PC | Ack PC | Ack Data | Port0 Reads In Window | Key-On After Read |",
            "| --- | ---: | --- | --- | --- | --- | --- | ---: | --- |",
            *rows,
            "",
        ]
    )


def main() -> int:
    args = parse_args()
    jobs_path = Path(args.jobs)
    jobs_index = load_json(jobs_path)
    jobs_index["path"] = str(jobs_path)
    frontier = collect(jobs_index)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(frontier, indent=2) + "\n", encoding="utf-8")
    markdown_path = output_path.with_suffix(".md")
    markdown_path.write_text(render_markdown(frontier), encoding="utf-8")
    summary = frontier["summary"]
    print(
        "Collected audio mailbox frontier: "
        f"{summary['capture_count']} / {frontier['job_count']} captures, "
        f"{summary['command_read_count']} command reads, "
        f"{summary['zero_ack_write_count']} zero ack writes"
    )
    print(f"Wrote {output_path}")
    print(f"Wrote {markdown_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
