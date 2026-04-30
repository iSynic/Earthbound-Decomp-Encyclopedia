#!/usr/bin/env python3
"""Summarize the ares probe with diagnostic APUIO0 command preseed disabled."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_METRICS = ROOT / "build" / "audio" / "no-command-jobs" / "ares-capture-metrics.json"
DEFAULT_OUTPUT = ROOT / "build" / "audio" / "no-command-jobs" / "no-command-frontier.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Collect no-command ares probe frontier.")
    parser.add_argument("--metrics", default=str(DEFAULT_METRICS), help="No-command capture metrics JSON.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Output frontier JSON path.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def collect(metrics: dict[str, Any]) -> dict[str, Any]:
    records: list[dict[str, Any]] = []
    final_pc_counts: Counter[str] = Counter()
    key_on_tracks = 0
    command_injected = 0
    command_read = 0
    preseed_enabled = 0

    for record in metrics.get("records", []):
        final_pc = str(record.get("final_pc", ""))
        final_pc_counts[final_pc] += 1
        if int(record.get("dsp_key_on_event_count", 0)) > 0:
            key_on_tracks += 1
        if record.get("host_command_injected"):
            command_injected += 1
        if record.get("host_command_first_read"):
            command_read += 1
        if record.get("host_command_preseed_enabled"):
            preseed_enabled += 1
        records.append(
            {
                "job_id": record.get("job_id"),
                "track_id": record.get("track_id"),
                "track_name": record.get("track_name"),
                "executed_instructions": int(record.get("executed_instructions", 0)),
                "final_pc": final_pc,
                "timer0_output_read_count": int(record.get("timer0_output_read_count", 0)),
                "dsp_register_write_count": int(record.get("dsp_register_write_count", 0)),
                "dsp_key_on_event_count": int(record.get("dsp_key_on_event_count", 0)),
                "dsp_key_off_event_count": int(record.get("dsp_key_off_event_count", 0)),
                "host_command": record.get("host_command"),
                "host_command_preseed_enabled": bool(record.get("host_command_preseed_enabled")),
                "host_command_preseed_value": record.get("host_command_preseed_value"),
                "host_command_injected": bool(record.get("host_command_injected")),
                "host_command_first_read": record.get("host_command_first_read"),
            }
        )

    records.sort(key=lambda item: (str(item.get("final_pc", "")), int(item.get("track_id", 0))))
    return {
        "schema": "earthbound-decomp.audio-no-command-frontier.v1",
        "status": "diagnostic_command_preseed_disabled",
        "source_metrics": metrics.get("job_index"),
        "job_count": len(records),
        "capture_count": int(metrics.get("capture_count", 0)),
        "summary": {
            "preseed_enabled_count": preseed_enabled,
            "host_command_injected_count": command_injected,
            "host_command_first_read_count": command_read,
            "tracks_with_key_on_events": key_on_tracks,
            "final_pc_counts": dict(sorted(final_pc_counts.items())),
        },
        "interpretation": {
            "claim": "This run disables the harness APUIO0 preseed. It identifies what the APU driver reaches without the CPU-side track-start command.",
            "expected_next_use": "Use this as the negative-control frontier while replacing the diagnostic preseed with the real CPU/APU handshake.",
        },
        "records": records,
    }


def render_markdown(frontier: dict[str, Any]) -> str:
    summary = frontier["summary"]
    rows = [
        "| `{job_id}` | {track_id} | `{track_name}` | `{pc}` | {kon} | {timer} | `{preseed}` | `{read}` |".format(
            job_id=record["job_id"],
            track_id=record["track_id"],
            track_name=record["track_name"],
            pc=record["final_pc"],
            kon=record["dsp_key_on_event_count"],
            timer=record["timer0_output_read_count"],
            preseed=record["host_command_preseed_value"],
            read=record["host_command_first_read"],
        )
        for record in frontier["records"]
    ]
    return "\n".join(
        [
            "# No-Command Audio Frontier",
            "",
            "Status: diagnostic APUIO0 command preseed disabled.",
            "",
            f"- captures: `{frontier['capture_count']} / {frontier['job_count']}`",
            f"- preseed enabled: `{summary['preseed_enabled_count']}`",
            f"- host-command injections: `{summary['host_command_injected_count']}`",
            f"- host-command first reads: `{summary['host_command_first_read_count']}`",
            f"- tracks with key-on events: `{summary['tracks_with_key_on_events']}`",
            f"- final PC counts: `{summary['final_pc_counts']}`",
            "",
            "## Tracks",
            "",
            "| Job | Track | Name | Final PC | KON events | Timer reads | Preseed | First command read |",
            "| --- | ---: | --- | --- | ---: | ---: | --- | --- |",
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
        "Collected no-command frontier: "
        f"{frontier['capture_count']} / {frontier['job_count']} captures, "
        f"{summary['tracks_with_key_on_events']} with key-on events"
    )
    print(f"Wrote {output_path}")
    print(f"Wrote {markdown_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
