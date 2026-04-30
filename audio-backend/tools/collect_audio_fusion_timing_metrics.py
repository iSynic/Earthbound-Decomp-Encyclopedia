#!/usr/bin/env python3
"""Collect post-command timing metrics from the fused CHANGE_MUSIC/C0:AB06 frontier."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import mean
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_FRONTIER = (
    ROOT
    / "build"
    / "audio"
    / "c0ab06-change-music-fusion-frontier-all"
    / "c0ab06-change-music-fusion-frontier-all.json"
)
DEFAULT_OUTPUT = (
    ROOT
    / "build"
    / "audio"
    / "c0ab06-change-music-fusion-frontier-all"
    / "c0ab06-change-music-fusion-timing-metrics.json"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Collect fused audio post-command timing metrics.")
    parser.add_argument("--frontier", default=str(DEFAULT_FRONTIER), help="Fusion frontier JSON.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Timing metrics JSON output.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def summarize(values: list[int]) -> dict[str, Any]:
    if not values:
        return {"count": 0, "min": None, "max": None, "mean": None}
    return {
        "count": len(values),
        "min": min(values),
        "max": max(values),
        "mean": round(mean(values), 3),
    }


def collect(frontier: dict[str, Any], frontier_path: Path) -> dict[str, Any]:
    records: list[dict[str, Any]] = []
    command_read_steps: list[int] = []
    zero_ack_steps: list[int] = []
    key_on_steps: list[int] = []
    ack_after_read_deltas: list[int] = []
    key_on_after_ack_deltas: list[int] = []
    no_key_on: list[dict[str, Any]] = []

    for record in frontier.get("records", []):
        change_music = (record.get("handshake") or {}).get("change_music") or {}
        command_read_step = int(change_music.get("command_read_step", -1))
        zero_ack_step = int(change_music.get("zero_ack_step", -1))
        key_on_step = int(change_music.get("key_on_step", -1))
        reached_key_on = bool(change_music.get("reached_key_on_after_ack"))
        metric = {
            "job_id": record.get("job_id"),
            "track_id": record.get("track_id"),
            "track_name": record.get("track_name"),
            "command_write_smp_burst": int(change_music.get("command_write_smp_burst", -1)),
            "command_read_step": command_read_step,
            "zero_ack_step": zero_ack_step,
            "key_on_step": key_on_step,
            "ack_after_read_delta": zero_ack_step - command_read_step if command_read_step >= 0 and zero_ack_step >= 0 else None,
            "key_on_after_ack_delta": key_on_step - zero_ack_step if key_on_step >= 0 and zero_ack_step >= 0 else None,
            "reached_key_on_after_ack": reached_key_on,
        }
        records.append(metric)
        if command_read_step >= 0:
            command_read_steps.append(command_read_step)
        if zero_ack_step >= 0:
            zero_ack_steps.append(zero_ack_step)
        if reached_key_on and key_on_step >= 0:
            key_on_steps.append(key_on_step)
            ack_after_read_deltas.append(metric["ack_after_read_delta"])
            key_on_after_ack_deltas.append(metric["key_on_after_ack_delta"])
        elif record.get("load_path_ok"):
            no_key_on.append(
                {
                    "job_id": record.get("job_id"),
                    "track_id": record.get("track_id"),
                    "track_name": record.get("track_name"),
                }
            )

    burst_values = sorted({record["command_write_smp_burst"] for record in records})
    return {
        "schema": "earthbound-decomp.audio-fusion-timing-metrics.v1",
        "frontier": str(frontier_path),
        "corpus": frontier.get("corpus"),
        "job_count": len(records),
        "load_path_success_count": int(frontier.get("load_path_success_count", 0)),
        "key_on_count": int(frontier.get("key_on_count", 0)),
        "no_key_on_count": len(no_key_on),
        "command_write_smp_burst_values": burst_values,
        "command_read_step": summarize(command_read_steps),
        "zero_ack_step": summarize(zero_ack_steps),
        "key_on_step": summarize(key_on_steps),
        "ack_after_read_delta": summarize([value for value in ack_after_read_deltas if value is not None]),
        "key_on_after_ack_delta": summarize([value for value in key_on_after_ack_deltas if value is not None]),
        "no_key_on_records": no_key_on,
        "records": records,
    }


def render_markdown(metrics: dict[str, Any]) -> str:
    no_key_rows = [
        "| {track_id} | `{track_name}` | `{job_id}` |".format(
            track_id=record["track_id"],
            track_name=record["track_name"],
            job_id=record["job_id"],
        )
        for record in metrics["no_key_on_records"]
    ]
    return "\n".join(
        [
            "# Audio Fusion Timing Metrics",
            "",
            "Status: post-command timing measured for the fused CHANGE_MUSIC/C0:AB06 frontier.",
            "",
            f"- corpus: `{metrics['corpus']}`",
            f"- jobs: `{metrics['job_count']}`",
            f"- load paths: `{metrics['load_path_success_count']}`",
            f"- key-on tracks: `{metrics['key_on_count']}`",
            f"- command-write SMP burst values: `{metrics['command_write_smp_burst_values']}`",
            f"- command-read step: `{metrics['command_read_step']}`",
            f"- zero-ack step: `{metrics['zero_ack_step']}`",
            f"- key-on step: `{metrics['key_on_step']}`",
            f"- ack-after-read delta: `{metrics['ack_after_read_delta']}`",
            f"- key-on-after-ack delta: `{metrics['key_on_after_ack_delta']}`",
            "",
            "## No-Key-On Records",
            "",
            "| Track | Name | Job |",
            "| ---: | --- | --- |",
            *no_key_rows,
            "",
        ]
    )


def main() -> int:
    args = parse_args()
    frontier_path = Path(args.frontier)
    metrics = collect(load_json(frontier_path), frontier_path)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")
    markdown_path = output_path.with_suffix(".md")
    markdown_path.write_text(render_markdown(metrics), encoding="utf-8")
    print(
        "Collected audio fusion timing metrics: "
        f"{metrics['key_on_count']} key-on tracks, "
        f"burst values {metrics['command_write_smp_burst_values']}"
    )
    print(f"Wrote {output_path}")
    print(f"Wrote {markdown_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
