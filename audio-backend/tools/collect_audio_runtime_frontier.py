#!/usr/bin/env python3
"""Collect the current audio runtime/capture frontier into one local report."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import median
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_ARES_JOBS = ROOT / "build" / "audio" / "backend-jobs" / "ares-jobs.json"
DEFAULT_LAST_KEYON_INDEX = ROOT / "build" / "audio" / "last-keyon-spc" / "last-keyon-spc-snapshots.json"
DEFAULT_RENDER_METRICS = ROOT / "build" / "audio" / "last-keyon-jobs" / "libgme-render-metrics.json"
DEFAULT_BASELINE_COMPARISON = (
    ROOT / "build" / "audio" / "last-keyon-jobs" / "last-keyon-vs-baseline-render-comparison.json"
)
DEFAULT_KEYON_PRIMED_COMPARISON = (
    ROOT / "build" / "audio" / "last-keyon-jobs" / "last-keyon-vs-keyon-primed-render-comparison.json"
)
DEFAULT_OUTPUT = ROOT / "build" / "audio" / "last-keyon-jobs" / "audio-runtime-frontier.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Collect current audio runtime frontier evidence.")
    parser.add_argument("--ares-jobs", default=str(DEFAULT_ARES_JOBS), help="Native ares job index.")
    parser.add_argument("--last-keyon-index", default=str(DEFAULT_LAST_KEYON_INDEX), help="Last-key-on SPC index.")
    parser.add_argument("--render-metrics", default=str(DEFAULT_RENDER_METRICS), help="Last-key-on render metrics.")
    parser.add_argument("--baseline-comparison", default=str(DEFAULT_BASELINE_COMPARISON), help="Baseline comparison.")
    parser.add_argument(
        "--keyon-primed-comparison",
        default=str(DEFAULT_KEYON_PRIMED_COMPARISON),
        help="Key-on primed comparison.",
    )
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Output JSON path.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def by_track(records: list[dict[str, Any]]) -> dict[int, dict[str, Any]]:
    return {int(record["track_id"]): record for record in records}


def capture_for_job(job: dict[str, Any]) -> dict[str, Any]:
    capture_path = Path(job["output_dir"]) / "ares-state-capture.json"
    if not capture_path.exists():
        return {"capture_path": str(capture_path), "capture_exists": False}
    capture = load_json(capture_path)
    probe = capture.get("spc700_entry_execution_probe", {})
    return {
        "capture_path": str(capture_path),
        "capture_exists": True,
        "executed_instructions": int(probe.get("executed_instructions", 0)),
        "final_pc": probe.get("final_pc"),
        "dsp_key_on_event_count": int(probe.get("dsp_key_on_event_count", 0)),
        "dsp_key_off_event_count": int(probe.get("dsp_key_off_event_count", 0)),
        "dsp_last_key_on_data": probe.get("dsp_last_key_on_data"),
        "dsp_last_key_off_data": probe.get("dsp_last_key_off_data"),
        "timer0_output_read_count": int(probe.get("timer0_output_read_count", 0)),
        "host_command": probe.get("diagnostic_host_port0_command"),
        "host_command_injected": bool(probe.get("diagnostic_host_port0_injected_after_timer_enable")),
        "host_command_injection": probe.get("diagnostic_host_port0_injection"),
        "host_command_first_read": probe.get("diagnostic_host_port0_first_read"),
        "last_key_on_snapshot": probe.get("last_key_on_snapshot", {}),
        "timing_model": probe.get("timing_model"),
    }


def collect(args: argparse.Namespace) -> dict[str, Any]:
    ares_jobs_path = Path(args.ares_jobs)
    last_keyon_path = Path(args.last_keyon_index)
    render_metrics_path = Path(args.render_metrics)
    baseline_comparison_path = Path(args.baseline_comparison)
    keyon_primed_comparison_path = Path(args.keyon_primed_comparison)

    ares_jobs = load_json(ares_jobs_path)
    last_keyon = load_json(last_keyon_path)
    render_metrics = load_json(render_metrics_path)
    baseline_comparison = load_json(baseline_comparison_path)
    keyon_primed_comparison = load_json(keyon_primed_comparison_path)

    snapshots_by_track = by_track(last_keyon.get("records", []))
    renders_by_track = by_track(render_metrics.get("records", []))
    baseline_by_track = by_track(baseline_comparison.get("records", []))
    keyon_primed_by_track = by_track(keyon_primed_comparison.get("records", []))

    records: list[dict[str, Any]] = []
    for job in ares_jobs.get("jobs", []):
        track_id = int(job["track_id"])
        capture = capture_for_job(job)
        snapshot_record = snapshots_by_track.get(track_id, {})
        render_record = renders_by_track.get(track_id, {})
        baseline_record = baseline_by_track.get(track_id, {})
        keyon_primed_record = keyon_primed_by_track.get(track_id, {})
        snapshot = snapshot_record.get("snapshot") or {}
        records.append(
            {
                "track_id": track_id,
                "track_name": job["track_name"],
                "capture": capture,
                "last_keyon_snapshot": {
                    "available": bool(snapshot),
                    "path": snapshot.get("path"),
                    "sha1": snapshot.get("sha1"),
                    "pc": snapshot.get("pc"),
                    "kon": snapshot.get("kon"),
                    "kof": snapshot.get("kof"),
                    "key_on_event_index": snapshot_record.get("key_on_event_index"),
                    "key_on_data": snapshot_record.get("key_on_data"),
                    "source_declared_matches": snapshot_record.get("source_declared_matches"),
                },
                "render": {
                    "classification": render_record.get("classification", "missing"),
                    "peak_abs_sample": int(render_record.get("peak_abs_sample", 0)),
                    "nonzero_sample_count": int(render_record.get("nonzero_sample_count", 0)),
                    "rms_sample": float(render_record.get("rms_sample", 0.0)),
                    "first_nonzero_sample_index": int(render_record.get("first_nonzero_sample_index", -1)),
                    "source_spc_sha1": render_record.get("source_spc_sha1"),
                },
                "baseline_comparison": {
                    "classification_delta_rank": int(baseline_record.get("classification_delta_rank", 0)),
                    "peak_delta": int(baseline_record.get("peak_delta", 0)),
                    "baseline_classification": baseline_record.get("baseline_classification", "missing"),
                },
                "keyon_primed_comparison": {
                    "classification_delta_rank": int(keyon_primed_record.get("classification_delta_rank", 0)),
                    "peak_delta": int(keyon_primed_record.get("peak_delta", 0)),
                    "baseline_classification": keyon_primed_record.get("baseline_classification", "missing"),
                },
            }
        )

    peaks = [int(record["render"]["peak_abs_sample"]) for record in records]
    rms_values = [float(record["render"]["rms_sample"]) for record in records]
    audible_count = sum(1 for record in records if record["render"]["classification"] == "audible")
    key_on_count = sum(1 for record in records if int(record["capture"].get("dsp_key_on_event_count", 0)) > 0)
    last_keyon_count = sum(1 for record in records if record["last_keyon_snapshot"]["available"])
    matching_render_sources = sum(
        1
        for record in records
        if record["last_keyon_snapshot"].get("sha1")
        and record["last_keyon_snapshot"].get("sha1") == record["render"].get("source_spc_sha1")
    )
    command_injection_count = sum(1 for record in records if record["capture"].get("host_command_injection"))
    command_read_count = sum(1 for record in records if record["capture"].get("host_command_first_read"))
    command_read_after_injection_count = 0
    keyon_after_command_read_count = 0
    for record in records:
        injection = record["capture"].get("host_command_injection") or {}
        first_read = record["capture"].get("host_command_first_read") or {}
        snapshot = record["capture"].get("last_key_on_snapshot") or {}
        if first_read and injection and int(first_read.get("sequence", 0)) >= int(injection.get("sequence", 0)):
            command_read_after_injection_count += 1
        if first_read and snapshot and int(snapshot.get("instruction", 0)) >= int(first_read.get("instruction", 0)):
            keyon_after_command_read_count += 1

    return {
        "schema": "earthbound-decomp.audio-runtime-frontier.v1",
        "status": "diagnostic_last_keyon_boundary_audible_faithful_runtime_pending",
        "inputs": {
            "ares_jobs": str(ares_jobs_path),
            "last_keyon_index": str(last_keyon_path),
            "render_metrics": str(render_metrics_path),
            "baseline_comparison": str(baseline_comparison_path),
            "keyon_primed_comparison": str(keyon_primed_comparison_path),
        },
        "source_policy": {
            "contains_rom_derived_bytes": False,
            "references_ignored_rom_derived_outputs": True,
            "detail_report_stays_under_build_audio": True,
        },
        "shortcut_audit": {
            "uses_diagnostic_timer0_shim": True,
            "uses_diagnostic_apuio0_preseed": True,
            "uses_full_sfc_scheduler": False,
            "uses_real_cpu_apu_track_start_handshake": False,
            "snapshot_is_audible": True,
            "snapshot_is_final_faithful_runtime": False,
        },
        "summary": {
            "track_count": len(records),
            "tracks_with_key_on_events": key_on_count,
            "last_keyon_snapshot_count": last_keyon_count,
            "render_metric_count": int(render_metrics.get("metrics_count", 0)),
            "audible_render_count": audible_count,
            "matching_render_source_sha1_count": matching_render_sources,
            "command_injection_count": command_injection_count,
            "command_first_read_count": command_read_count,
            "command_read_after_injection_count": command_read_after_injection_count,
            "keyon_after_command_read_count": keyon_after_command_read_count,
            "baseline_improved_count": int(baseline_comparison.get("improved_count", 0)),
            "baseline_unchanged_count": int(baseline_comparison.get("unchanged_count", 0)),
            "baseline_worsened_count": int(baseline_comparison.get("worsened_count", 0)),
            "keyon_primed_improved_count": int(keyon_primed_comparison.get("improved_count", 0)),
            "keyon_primed_unchanged_count": int(keyon_primed_comparison.get("unchanged_count", 0)),
            "keyon_primed_worsened_count": int(keyon_primed_comparison.get("worsened_count", 0)),
            "min_peak_abs_sample": min(peaks) if peaks else 0,
            "median_peak_abs_sample": median(peaks) if peaks else 0,
            "median_rms_sample": median(rms_values) if rms_values else 0,
        },
        "regression_target": {
            "all_tracks_have_key_on_events": key_on_count == len(records),
            "all_tracks_have_last_keyon_snapshots": last_keyon_count == len(records),
            "all_tracks_render_audible": audible_count == len(records),
            "all_render_sources_match_last_keyon_snapshots": matching_render_sources == len(records),
            "all_tracks_have_command_injection": command_injection_count == len(records),
            "all_tracks_have_command_first_read": command_read_count == len(records),
            "all_command_reads_follow_injection": command_read_after_injection_count == len(records),
            "all_keyon_snapshots_follow_command_read": keyon_after_command_read_count == len(records),
            "no_track_worse_than_baseline": int(baseline_comparison.get("worsened_count", 0)) == 0,
            "no_track_worse_than_keyon_primed": int(keyon_primed_comparison.get("worsened_count", 0)) == 0,
        },
        "records": records,
    }


def render_markdown(report: dict[str, Any]) -> str:
    summary = report["summary"]
    audit = report["shortcut_audit"]
    rows = [
        "| {track_id} | `{track_name}` | `{kon}` | `{pc}` | `{classification}` | {peak} | {rms:.3f} | {base_delta} | {primed_delta} |".format(
            track_id=record["track_id"],
            track_name=record["track_name"],
            kon=record["last_keyon_snapshot"].get("kon", ""),
            pc=record["last_keyon_snapshot"].get("pc", ""),
            classification=record["render"]["classification"],
            peak=record["render"]["peak_abs_sample"],
            rms=record["render"]["rms_sample"],
            base_delta=record["baseline_comparison"]["classification_delta_rank"],
            primed_delta=record["keyon_primed_comparison"]["classification_delta_rank"],
        )
        for record in sorted(report["records"], key=lambda item: int(item["track_id"]))
    ]
    return "\n".join(
        [
            "# Audio Runtime Frontier",
            "",
            "Status: diagnostic last-key-on boundary is audible; faithful runtime capture is still pending.",
            "",
            "## Summary",
            "",
            f"- tracks: `{summary['track_count']}`",
            f"- key-on captures: `{summary['tracks_with_key_on_events']}`",
            f"- last-key-on snapshots: `{summary['last_keyon_snapshot_count']}`",
            f"- audible renders: `{summary['audible_render_count']}`",
            f"- matching render source hashes: `{summary['matching_render_source_sha1_count']}`",
            f"- command injections: `{summary['command_injection_count']}`",
            f"- command first reads: `{summary['command_first_read_count']}`",
            f"- command reads after injection: `{summary['command_read_after_injection_count']}`",
            f"- key-on snapshots after command read: `{summary['keyon_after_command_read_count']}`",
            f"- baseline comparison: `{summary['baseline_improved_count']}` improved, `{summary['baseline_unchanged_count']}` unchanged, `{summary['baseline_worsened_count']}` worsened",
            f"- key-on primed comparison: `{summary['keyon_primed_improved_count']}` improved, `{summary['keyon_primed_unchanged_count']}` unchanged, `{summary['keyon_primed_worsened_count']}` worsened",
            f"- minimum peak sample: `{summary['min_peak_abs_sample']}`",
            f"- median peak sample: `{summary['median_peak_abs_sample']}`",
            f"- median RMS: `{summary['median_rms_sample']:.3f}`",
            "",
            "## Shortcut Audit",
            "",
            f"- diagnostic timer0 shim: `{audit['uses_diagnostic_timer0_shim']}`",
            f"- diagnostic APUIO0 preseed: `{audit['uses_diagnostic_apuio0_preseed']}`",
            f"- full SFC scheduler: `{audit['uses_full_sfc_scheduler']}`",
            f"- real CPU/APU track-start handshake: `{audit['uses_real_cpu_apu_track_start_handshake']}`",
            f"- final faithful runtime snapshot: `{audit['snapshot_is_final_faithful_runtime']}`",
            "",
            "## Tracks",
            "",
            "| Track | Name | KON | Snapshot PC | Render | Peak | RMS | vs Baseline | vs Primed |",
            "| ---: | --- | --- | --- | --- | ---: | ---: | ---: | ---: |",
            *rows,
            "",
        ]
    )


def main() -> int:
    args = parse_args()
    report = collect(args)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    markdown_path = output_path.with_suffix(".md")
    markdown_path.write_text(render_markdown(report), encoding="utf-8")
    summary = report["summary"]
    print(
        "Collected audio runtime frontier: "
        f"{summary['audible_render_count']} / {summary['track_count']} audible, "
        f"{summary['matching_render_source_sha1_count']} matching render sources"
    )
    print(f"Wrote {output_path}")
    print(f"Wrote {markdown_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
