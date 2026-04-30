#!/usr/bin/env python3
"""Collect ares diagnostic capture metrics across backend jobs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_JOBS = ROOT / "build" / "audio" / "backend-jobs" / "ares-jobs.json"
DEFAULT_OUTPUT = ROOT / "build" / "audio" / "backend-jobs" / "ares-capture-metrics.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Collect ares diagnostic capture metrics.")
    parser.add_argument("--jobs", default=str(DEFAULT_JOBS), help="ares backend job index path.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Metrics JSON output path.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def collect(jobs_path: Path) -> dict[str, Any]:
    index = load_json(jobs_path)
    records: list[dict[str, Any]] = []
    missing_captures = 0
    key_on_tracks = 0
    key_off_tracks = 0
    host_command_injected_tracks = 0
    host_command_first_read_tracks = 0

    for job in index.get("jobs", []):
        capture_path = Path(job["output_dir"]) / "ares-state-capture.json"
        record: dict[str, Any] = {
            "job_id": job["job_id"],
            "track_id": job["track_id"],
            "track_name": job["track_name"],
            "capture_path": str(capture_path),
            "capture_exists": capture_path.exists(),
        }
        if not capture_path.exists():
            missing_captures += 1
            records.append(record)
            continue
        capture = load_json(capture_path)
        probe = capture.get("spc700_entry_execution_probe", {})
        key_on_count = int(probe.get("dsp_key_on_event_count", 0))
        key_off_count = int(probe.get("dsp_key_off_event_count", 0))
        if key_on_count:
            key_on_tracks += 1
        if key_off_count:
            key_off_tracks += 1
        if probe.get("diagnostic_host_port0_injected_after_timer_enable"):
            host_command_injected_tracks += 1
        if probe.get("diagnostic_host_port0_first_read"):
            host_command_first_read_tracks += 1
        record.update(
            {
                "executed_instructions": int(probe.get("executed_instructions", 0)),
                "final_pc": probe.get("final_pc"),
                "apu_io_read_count": int(probe.get("apu_io_read_count", 0)),
                "apu_io_write_count": int(probe.get("apu_io_write_count", 0)),
                "dsp_register_write_count": int(probe.get("dsp_register_write_count", 0)),
                "dsp_key_on_event_count": key_on_count,
                "dsp_key_off_event_count": key_off_count,
                "dsp_last_key_on_data": probe.get("dsp_last_key_on_data"),
                "dsp_last_key_off_data": probe.get("dsp_last_key_off_data"),
                "timer0_output_read_count": int(probe.get("timer0_output_read_count", 0)),
                "host_command_preseed_enabled": bool(probe.get("diagnostic_host_port0_preseed_enabled", True)),
                "host_command_preseed_mode": probe.get("diagnostic_host_port0_preseed_mode", "after_timer_enable"),
                "host_command": probe.get("diagnostic_host_port0_command"),
                "host_command_preseed_value": probe.get("diagnostic_host_port0_preseed_value"),
                "host_command_injected": bool(probe.get("diagnostic_host_port0_injected_after_timer_enable")),
                "host_command_injection": probe.get("diagnostic_host_port0_injection"),
                "host_command_first_read": probe.get("diagnostic_host_port0_first_read"),
                "dsp_register_write_counts": probe.get("dsp_register_write_counts", {}),
            }
        )
        records.append(record)

    records.sort(key=lambda item: (-int(item.get("dsp_key_on_event_count", 0)), item.get("job_id", "")))
    return {
        "schema": "earthbound-decomp.audio-capture-metrics.v1",
        "job_index": str(jobs_path),
        "backend": "ares",
        "capture_kind": "diagnostic_spc700_entry_probe",
        "job_count": len(records),
        "capture_count": len(records) - missing_captures,
        "missing_capture_count": missing_captures,
        "tracks_with_key_on_events": key_on_tracks,
        "tracks_with_key_off_events": key_off_tracks,
        "tracks_with_host_command_injected": host_command_injected_tracks,
        "tracks_with_host_command_first_read": host_command_first_read_tracks,
        "snapshot_boundary_diagnosis": "driver emits key-on events during probe, but final SPC headers currently have KON cleared by the selected stop boundary",
        "records": records,
    }


def render_markdown(summary: dict[str, Any]) -> str:
    rows = [
        "| `{job_id}` | {track_id} | `{track_name}` | {kon} | {kof} | `{last_kon}` | `{last_kof}` | `{pc}` | {dsp} |".format(
            job_id=record["job_id"],
            track_id=record["track_id"],
            track_name=record["track_name"],
            kon=record.get("dsp_key_on_event_count", ""),
            kof=record.get("dsp_key_off_event_count", ""),
            last_kon=record.get("dsp_last_key_on_data", ""),
            last_kof=record.get("dsp_last_key_off_data", ""),
            pc=record.get("final_pc", ""),
            dsp=record.get("dsp_register_write_count", ""),
        )
        for record in summary["records"]
    ]
    return "\n".join(
        [
            "# ares Diagnostic Capture Metrics",
            "",
            "Status: diagnostic capture corpus measured; source SPC stop boundary is not final.",
            "",
            f"- captures: `{summary['capture_count']} / {summary['job_count']}`",
            f"- tracks with key-on events: `{summary['tracks_with_key_on_events']}`",
            f"- tracks with key-off events: `{summary['tracks_with_key_off_events']}`",
            f"- tracks with host-command injection: `{summary['tracks_with_host_command_injected']}`",
            f"- tracks with host-command first read: `{summary['tracks_with_host_command_first_read']}`",
            f"- diagnosis: {summary['snapshot_boundary_diagnosis']}",
            "",
            "## Tracks",
            "",
            "| Job | Track | Name | KON events | KOF events | Last KON | Last KOF | Final PC | DSP writes |",
            "| --- | ---: | --- | ---: | ---: | --- | --- | --- | ---: |",
            *rows,
            "",
        ]
    )


def main() -> int:
    args = parse_args()
    jobs_path = Path(args.jobs)
    output_path = Path(args.output)
    summary = collect(jobs_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    markdown_path = output_path.with_suffix(".md")
    markdown_path.write_text(render_markdown(summary), encoding="utf-8")
    print(
        "Collected ares capture metrics: "
        f"{summary['capture_count']} / {summary['job_count']} captures, "
        f"{summary['tracks_with_key_on_events']} with key-on events"
    )
    print(f"Wrote {output_path}")
    print(f"Wrote {markdown_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
