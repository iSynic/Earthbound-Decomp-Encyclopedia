#!/usr/bin/env python3
"""Summarize a diagnostic command-timing ares probe run."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_METRICS = ROOT / "build" / "audio" / "command-on-first-read-jobs" / "ares-capture-metrics.json"
DEFAULT_OUTPUT = ROOT / "build" / "audio" / "command-on-first-read-jobs" / "command-timing-frontier.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Collect command-timing ares probe frontier.")
    parser.add_argument("--metrics", default=str(DEFAULT_METRICS), help="Capture metrics JSON.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Output frontier JSON path.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def collect(metrics: dict[str, Any]) -> dict[str, Any]:
    records: list[dict[str, Any]] = []
    mode_counts: Counter[str] = Counter()
    final_pc_counts: Counter[str] = Counter()
    key_on_tracks = 0
    command_injected = 0
    command_read = 0
    keyon_after_read = 0

    for record in metrics.get("records", []):
        mode = str(record.get("host_command_preseed_mode", "unknown"))
        final_pc = str(record.get("final_pc", ""))
        mode_counts[mode] += 1
        final_pc_counts[final_pc] += 1
        if int(record.get("dsp_key_on_event_count", 0)) > 0:
            key_on_tracks += 1
        if record.get("host_command_injected"):
            command_injected += 1
        first_read = record.get("host_command_first_read") or {}
        if first_read:
            command_read += 1
        capture_path = Path(record.get("capture_path", ""))
        last_keyon_instruction = None
        if capture_path.exists():
            capture = load_json(capture_path)
            last_keyon = capture.get("spc700_entry_execution_probe", {}).get("last_key_on_snapshot", {})
            last_keyon_instruction = last_keyon.get("instruction")
        if first_read and last_keyon_instruction is not None:
            if int(last_keyon_instruction) >= int(first_read.get("instruction", 0)):
                keyon_after_read += 1
        records.append(
            {
                "job_id": record.get("job_id"),
                "track_id": record.get("track_id"),
                "track_name": record.get("track_name"),
                "mode": mode,
                "executed_instructions": int(record.get("executed_instructions", 0)),
                "final_pc": final_pc,
                "timer0_output_read_count": int(record.get("timer0_output_read_count", 0)),
                "dsp_register_write_count": int(record.get("dsp_register_write_count", 0)),
                "dsp_key_on_event_count": int(record.get("dsp_key_on_event_count", 0)),
                "host_command": record.get("host_command"),
                "host_command_preseed_value": record.get("host_command_preseed_value"),
                "host_command_injection": record.get("host_command_injection"),
                "host_command_first_read": first_read or None,
                "last_keyon_instruction": last_keyon_instruction,
            }
        )

    records.sort(key=lambda item: int(item.get("track_id", 0)))
    return {
        "schema": "earthbound-decomp.audio-command-timing-frontier.v1",
        "status": "diagnostic_command_timing_experiment",
        "source_metrics": metrics.get("job_index"),
        "job_count": len(records),
        "capture_count": int(metrics.get("capture_count", 0)),
        "summary": {
            "mode_counts": dict(sorted(mode_counts.items())),
            "final_pc_counts": dict(sorted(final_pc_counts.items())),
            "host_command_injected_count": command_injected,
            "host_command_first_read_count": command_read,
            "tracks_with_key_on_events": key_on_tracks,
            "keyon_after_command_read_count": keyon_after_read,
        },
        "interpretation": {
            "claim": "This run varies when the diagnostic APUIO0 command appears to the APU driver.",
            "expected_next_use": "Prefer the latest command timing that still reaches the last-key-on/audible boundary as the target for real CPU/APU handshake replacement.",
        },
        "records": records,
    }


def render_markdown(frontier: dict[str, Any]) -> str:
    summary = frontier["summary"]
    rows = [
        "| `{job_id}` | {track_id} | `{track_name}` | `{mode}` | `{pc}` | {kon} | `{inject}` | `{read}` |".format(
            job_id=record["job_id"],
            track_id=record["track_id"],
            track_name=record["track_name"],
            mode=record["mode"],
            pc=record["final_pc"],
            kon=record["dsp_key_on_event_count"],
            inject=record["host_command_injection"],
            read=record["host_command_first_read"],
        )
        for record in frontier["records"]
    ]
    return "\n".join(
        [
            "# Command Timing Audio Frontier",
            "",
            "Status: diagnostic APUIO0 command timing experiment.",
            "",
            f"- captures: `{frontier['capture_count']} / {frontier['job_count']}`",
            f"- modes: `{summary['mode_counts']}`",
            f"- final PC counts: `{summary['final_pc_counts']}`",
            f"- host-command injections: `{summary['host_command_injected_count']}`",
            f"- host-command first reads: `{summary['host_command_first_read_count']}`",
            f"- tracks with key-on events: `{summary['tracks_with_key_on_events']}`",
            f"- key-on after command read: `{summary['keyon_after_command_read_count']}`",
            "",
            "## Tracks",
            "",
            "| Job | Track | Name | Mode | Final PC | KON events | Injection | First command read |",
            "| --- | ---: | --- | --- | --- | ---: | --- | --- |",
            *rows,
            "",
        ]
    )


def main() -> int:
    args = parse_args()
    metrics = load_json(Path(args.metrics))
    frontier = collect(metrics)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(frontier, indent=2) + "\n", encoding="utf-8")
    markdown_path = output_path.with_suffix(".md")
    markdown_path.write_text(render_markdown(frontier), encoding="utf-8")
    summary = frontier["summary"]
    print(
        "Collected command timing frontier: "
        f"{frontier['capture_count']} / {frontier['job_count']} captures, "
        f"{summary['tracks_with_key_on_events']} with key-on events"
    )
    print(f"Wrote {output_path}")
    print(f"Wrote {markdown_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
