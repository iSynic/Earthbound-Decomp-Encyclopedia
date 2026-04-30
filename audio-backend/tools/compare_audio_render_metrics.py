#!/usr/bin/env python3
"""Compare two diagnostic audio render metrics corpora."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_BASELINE = ROOT / "build" / "audio" / "backend-jobs" / "libgme-render-metrics.json"
DEFAULT_EXPERIMENT = ROOT / "build" / "audio" / "keyon-primed-jobs" / "libgme-render-metrics.json"
DEFAULT_OUTPUT = ROOT / "build" / "audio" / "keyon-primed-jobs" / "render-metrics-comparison.json"


RANK = {
    "missing": 0,
    "silent": 1,
    "click_or_trace": 2,
    "very_quiet": 3,
    "audible": 4,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compare diagnostic render metric corpora.")
    parser.add_argument("--baseline", default=str(DEFAULT_BASELINE), help="Baseline metrics JSON.")
    parser.add_argument("--experiment", default=str(DEFAULT_EXPERIMENT), help="Experiment metrics JSON.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Comparison JSON output path.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def by_track(metrics: dict[str, Any]) -> dict[int, dict[str, Any]]:
    return {int(record["track_id"]): record for record in metrics.get("records", [])}


def compare(baseline: dict[str, Any], experiment: dict[str, Any]) -> dict[str, Any]:
    baseline_by_track = by_track(baseline)
    experiment_by_track = by_track(experiment)
    records: list[dict[str, Any]] = []
    improved = 0
    worsened = 0
    unchanged = 0

    for track_id in sorted(set(baseline_by_track) | set(experiment_by_track)):
        base = baseline_by_track.get(track_id, {})
        exp = experiment_by_track.get(track_id, {})
        base_class = str(base.get("classification", "missing"))
        exp_class = str(exp.get("classification", "missing"))
        delta_rank = RANK.get(exp_class, 0) - RANK.get(base_class, 0)
        if delta_rank > 0:
            improved += 1
        elif delta_rank < 0:
            worsened += 1
        else:
            unchanged += 1
        records.append(
            {
                "track_id": track_id,
                "track_name": exp.get("track_name", base.get("track_name", "")),
                "baseline_classification": base_class,
                "experiment_classification": exp_class,
                "classification_delta_rank": delta_rank,
                "baseline_peak_abs_sample": int(base.get("peak_abs_sample", 0)),
                "experiment_peak_abs_sample": int(exp.get("peak_abs_sample", 0)),
                "peak_delta": int(exp.get("peak_abs_sample", 0)) - int(base.get("peak_abs_sample", 0)),
                "baseline_nonzero_sample_count": int(base.get("nonzero_sample_count", 0)),
                "experiment_nonzero_sample_count": int(exp.get("nonzero_sample_count", 0)),
            }
        )

    records.sort(key=lambda record: (-record["classification_delta_rank"], -record["peak_delta"], record["track_id"]))
    return {
        "schema": "earthbound-decomp.audio-render-metrics-comparison.v1",
        "baseline": baseline.get("job_index"),
        "experiment": experiment.get("job_index"),
        "baseline_classification_counts": baseline.get("classification_counts", {}),
        "experiment_classification_counts": experiment.get("classification_counts", {}),
        "track_count": len(records),
        "improved_count": improved,
        "worsened_count": worsened,
        "unchanged_count": unchanged,
        "records": records,
    }


def render_markdown(comparison: dict[str, Any]) -> str:
    rows = [
        "| {track_id} | `{track_name}` | `{base}` | `{exp}` | {peak0} | {peak1} | {delta} |".format(
            track_id=record["track_id"],
            track_name=record["track_name"],
            base=record["baseline_classification"],
            exp=record["experiment_classification"],
            peak0=record["baseline_peak_abs_sample"],
            peak1=record["experiment_peak_abs_sample"],
            delta=record["peak_delta"],
        )
        for record in comparison["records"]
    ]
    return "\n".join(
        [
            "# Diagnostic Render Metrics Comparison",
            "",
            "Status: render metric corpora compared by per-track output classification and sample peak.",
            "",
            f"- baseline classes: `{comparison['baseline_classification_counts']}`",
            f"- experiment classes: `{comparison['experiment_classification_counts']}`",
            f"- improved tracks: `{comparison['improved_count']}`",
            f"- unchanged tracks: `{comparison['unchanged_count']}`",
            f"- worsened tracks: `{comparison['worsened_count']}`",
            "",
            "## Tracks",
            "",
            "| Track | Name | Baseline | Experiment | Base Peak | Exp Peak | Peak Delta |",
            "| ---: | --- | --- | --- | ---: | ---: | ---: |",
            *rows,
            "",
        ]
    )


def main() -> int:
    args = parse_args()
    baseline = load_json(Path(args.baseline))
    experiment = load_json(Path(args.experiment))
    comparison = compare(baseline, experiment)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(comparison, indent=2) + "\n", encoding="utf-8")
    markdown_path = output_path.with_suffix(".md")
    markdown_path.write_text(render_markdown(comparison), encoding="utf-8")
    print(
        "Compared render metrics: "
        f"{comparison['improved_count']} improved, "
        f"{comparison['unchanged_count']} unchanged, "
        f"{comparison['worsened_count']} worsened"
    )
    print(f"Wrote {output_path}")
    print(f"Wrote {markdown_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
