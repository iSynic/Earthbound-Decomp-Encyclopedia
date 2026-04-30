#!/usr/bin/env python3
"""Run the last-key-on SPC render experiment end to end."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_LAST_KEYON_SPC = ROOT / "build" / "audio" / "last-keyon-spc"
DEFAULT_LAST_KEYON_JOBS = ROOT / "build" / "audio" / "last-keyon-jobs"
DEFAULT_LIBGME_HARNESS = (
    ROOT
    / "build"
    / "audio"
    / "libgme-audio-harness-msvc"
    / "RelWithDebInfo"
    / "earthbound_libgme_audio_harness.exe"
)
DEFAULT_BASELINE_METRICS = ROOT / "build" / "audio" / "backend-jobs" / "libgme-render-metrics.json"
DEFAULT_KEYON_PRIMED_METRICS = ROOT / "build" / "audio" / "keyon-primed-jobs" / "libgme-render-metrics.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the last-key-on SPC render experiment.")
    parser.add_argument("--spc-out", default=str(DEFAULT_LAST_KEYON_SPC), help="Last-key-on SPC index output dir.")
    parser.add_argument("--jobs-out", default=str(DEFAULT_LAST_KEYON_JOBS), help="Last-key-on snes_spc job dir.")
    parser.add_argument("--libgme-harness", default=str(DEFAULT_LIBGME_HARNESS), help="libgme harness executable.")
    parser.add_argument("--skip-render", action="store_true", help="Only build and validate the snapshot index.")
    parser.add_argument(
        "--baseline-metrics",
        default=str(DEFAULT_BASELINE_METRICS),
        help="Baseline render metrics for comparison when present.",
    )
    parser.add_argument(
        "--keyon-primed-metrics",
        default=str(DEFAULT_KEYON_PRIMED_METRICS),
        help="Key-on primed render metrics for comparison when present.",
    )
    return parser.parse_args()


def run(command: list[str]) -> None:
    print("+ " + " ".join(command))
    subprocess.run(command, cwd=ROOT, check=True)


def main() -> int:
    args = parse_args()
    spc_out = Path(args.spc_out)
    jobs_out = Path(args.jobs_out)
    snapshot_index = spc_out / "last-keyon-spc-snapshots.json"
    jobs_index = jobs_out / "snes_spc-jobs.json"
    result_summary = jobs_out / "snes_spc-result-summary.json"
    render_metrics = jobs_out / "libgme-render-metrics.json"
    baseline_comparison = jobs_out / "last-keyon-vs-baseline-render-comparison.json"
    keyon_primed_comparison = jobs_out / "last-keyon-vs-keyon-primed-render-comparison.json"
    runtime_frontier = jobs_out / "audio-runtime-frontier.json"

    run([sys.executable, "tools/build_audio_last_keyon_spc_experiment.py", "--out", str(spc_out)])
    run([sys.executable, "tools/validate_audio_last_keyon_spc_experiment.py", str(snapshot_index)])

    if args.skip_render:
        return 0

    harness = Path(args.libgme_harness)
    if not harness.exists():
        raise FileNotFoundError(f"missing libgme harness: {harness}")

    run([sys.executable, "tools/build_audio_backend_jobs.py", "--backend", "snes_spc", "--out", str(jobs_out)])
    run(
        [
            sys.executable,
            "tools/run_audio_backend_batch.py",
            "--jobs",
            str(jobs_index),
            "--summary",
            str(result_summary),
            "--mode",
            "external",
            "--force",
            "--external",
            str(harness),
            "--job",
            "{job}",
            "--result",
            "{result}",
            "--snapshot-index",
            str(snapshot_index),
        ]
    )
    run([sys.executable, "tools/validate_audio_backend_result_summary.py", str(result_summary)])
    run(
        [
            sys.executable,
            "tools/collect_audio_render_metrics.py",
            "--jobs",
            str(jobs_index),
            "--output",
            str(render_metrics),
        ]
    )
    run([sys.executable, "tools/validate_audio_render_metrics.py", str(render_metrics)])

    baseline_metrics = Path(args.baseline_metrics)
    if baseline_metrics.exists():
        run(
            [
                sys.executable,
                "tools/compare_audio_render_metrics.py",
                "--baseline",
                str(baseline_metrics),
                "--experiment",
                str(render_metrics),
                "--output",
                str(baseline_comparison),
            ]
        )
        run([sys.executable, "tools/validate_audio_render_metrics_comparison.py", str(baseline_comparison)])

    keyon_primed_metrics = Path(args.keyon_primed_metrics)
    if keyon_primed_metrics.exists():
        run(
            [
                sys.executable,
                "tools/compare_audio_render_metrics.py",
                "--baseline",
                str(keyon_primed_metrics),
                "--experiment",
                str(render_metrics),
                "--output",
                str(keyon_primed_comparison),
            ]
        )
        run([sys.executable, "tools/validate_audio_render_metrics_comparison.py", str(keyon_primed_comparison)])

    run([sys.executable, "tools/collect_audio_runtime_frontier.py", "--output", str(runtime_frontier)])
    run([sys.executable, "tools/validate_audio_runtime_frontier.py", str(runtime_frontier)])

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
