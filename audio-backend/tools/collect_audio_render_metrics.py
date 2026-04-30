#!/usr/bin/env python3
"""Collect libgme diagnostic render metrics across backend jobs."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_JOBS = ROOT / "build" / "audio" / "backend-jobs" / "snes_spc-jobs.json"
DEFAULT_OUTPUT = ROOT / "build" / "audio" / "backend-jobs" / "libgme-render-metrics.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Collect diagnostic libgme render metrics.")
    parser.add_argument("--jobs", default=str(DEFAULT_JOBS), help="Backend job index path.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Metrics JSON output path.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def classify_render(metrics: dict[str, Any]) -> str:
    peak = int(metrics.get("peak_abs_sample", 0))
    nonzero = int(metrics.get("nonzero_sample_count", 0))
    if peak == 0 or nonzero == 0:
        return "silent"
    if peak < 16 or nonzero < 128:
        return "click_or_trace"
    if peak < 512:
        return "very_quiet"
    return "audible"


def collect(jobs_path: Path) -> dict[str, Any]:
    index = load_json(jobs_path)
    records: list[dict[str, Any]] = []
    class_counts: Counter[str] = Counter()
    missing_metrics = 0

    for job in index.get("jobs", []):
        output_dir = Path(job["output_dir"])
        metrics_path = output_dir / "libgme-render-hash.json"
        record: dict[str, Any] = {
            "job_id": job["job_id"],
            "track_id": job["track_id"],
            "track_name": job["track_name"],
            "metrics_path": str(metrics_path),
            "metrics_exists": metrics_path.exists(),
        }
        if not metrics_path.exists():
            missing_metrics += 1
            record["classification"] = "missing"
            class_counts["missing"] += 1
            records.append(record)
            continue
        metrics = load_json(metrics_path)
        classification = classify_render(metrics)
        class_counts[classification] += 1
        record.update(
            {
                "classification": classification,
                "sample_rate": int(metrics.get("sample_rate", 0)),
                "channels": int(metrics.get("channels", 0)),
                "seconds": float(metrics.get("seconds", 0.0)),
                "peak_abs_sample": int(metrics.get("peak_abs_sample", 0)),
                "sum_abs_samples": int(metrics.get("sum_abs_samples", 0)),
                "nonzero_sample_count": int(metrics.get("nonzero_sample_count", 0)),
                "first_nonzero_sample_index": int(metrics.get("first_nonzero_sample_index", -1)),
                "last_nonzero_sample_index": int(metrics.get("last_nonzero_sample_index", -1)),
                "rms_sample": float(metrics.get("rms_sample", 0.0)),
                "voice_count": int(metrics.get("voice_count", 0)),
                "rendered_samples": int(metrics.get("rendered_samples", 0)),
                "warning": str(metrics.get("warning", "")),
                "source_spc_sha1": metrics.get("source_spc_sha1"),
            }
        )
        records.append(record)

    records.sort(key=lambda item: (item.get("classification", ""), -int(item.get("peak_abs_sample", 0))))
    return {
        "schema": "earthbound-decomp.audio-render-metrics.v1",
        "job_index": str(jobs_path),
        "backend": "libgme",
        "snapshot_faithfulness": "diagnostic_input_snapshot_not_runtime_faithful",
        "render_options_source": "backend_job_render_options",
        "job_count": len(records),
        "metrics_count": len(records) - missing_metrics,
        "missing_metrics_count": missing_metrics,
        "classification_counts": dict(class_counts),
        "classification_policy": {
            "silent": "peak_abs_sample == 0 or nonzero_sample_count == 0",
            "click_or_trace": "peak_abs_sample < 16 or nonzero_sample_count < 128",
            "very_quiet": "peak_abs_sample < 512",
            "audible": "peak_abs_sample >= 512",
        },
        "records": records,
    }


def render_markdown(summary: dict[str, Any]) -> str:
    rows = [
        "| `{job_id}` | {track_id} | `{track_name}` | `{classification}` | {peak} | {nonzero} | {rms:.3f} | {first} | {last} |".format(
            job_id=record["job_id"],
            track_id=record["track_id"],
            track_name=record["track_name"],
            classification=record["classification"],
            peak=record.get("peak_abs_sample", ""),
            nonzero=record.get("nonzero_sample_count", ""),
            rms=float(record.get("rms_sample", 0.0)),
            first=record.get("first_nonzero_sample_index", ""),
            last=record.get("last_nonzero_sample_index", ""),
        )
        for record in summary["records"]
    ]
    return "\n".join(
        [
            "# libgme Diagnostic Render Metrics",
            "",
            "Status: diagnostic render corpus measured; source SPC snapshots are not final faithful runtime captures.",
            "",
            f"- jobs: `{summary['job_count']}`",
            f"- metrics: `{summary['metrics_count']}`",
            f"- classifications: `{summary['classification_counts']}`",
            "",
            "## Tracks",
            "",
            "| Job | Track | Name | Class | Peak | Nonzero Samples | RMS | First Nonzero | Last Nonzero |",
            "| --- | ---: | --- | --- | ---: | ---: | ---: | ---: | ---: |",
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
        "Collected libgme render metrics: "
        f"{summary['metrics_count']} / {summary['job_count']} metrics, "
        f"classifications {summary['classification_counts']}"
    )
    print(f"Wrote {output_path}")
    print(f"Wrote {markdown_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
