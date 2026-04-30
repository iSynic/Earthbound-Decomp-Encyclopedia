#!/usr/bin/env python3
"""Run the native ares probe with diagnostic APUIO0 preseed disabled."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUT = ROOT / "build" / "audio" / "no-command-jobs"
DEFAULT_ARES_HARNESS = (
    ROOT
    / "build"
    / "audio"
    / "ares-audio-harness-msvc"
    / "RelWithDebInfo"
    / "earthbound_ares_audio_harness.exe"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run no-command ares audio probe experiment.")
    parser.add_argument("--out", default=str(DEFAULT_OUT), help="Ignored output directory.")
    parser.add_argument("--ares-harness", default=str(DEFAULT_ARES_HARNESS), help="Native ares harness executable.")
    return parser.parse_args()


def run(command: list[str]) -> None:
    print("+ " + " ".join(command))
    subprocess.run(command, cwd=ROOT, check=True)


def main() -> int:
    args = parse_args()
    out_dir = Path(args.out)
    jobs_index = out_dir / "ares-jobs.json"
    result_summary = out_dir / "ares-result-summary.json"
    capture_metrics = out_dir / "ares-capture-metrics.json"
    no_command_frontier = out_dir / "no-command-frontier.json"
    harness = Path(args.ares_harness)
    if not harness.exists():
        raise FileNotFoundError(f"missing ares harness: {harness}")

    run([sys.executable, "tools/build_audio_backend_jobs.py", "--backend", "ares", "--out", str(out_dir)])
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
            "--disable-diagnostic-command-preseed",
        ]
    )
    run([sys.executable, "tools/validate_audio_backend_result_summary.py", str(result_summary)])
    run(
        [
            sys.executable,
            "tools/collect_audio_capture_metrics.py",
            "--jobs",
            str(jobs_index),
            "--output",
            str(capture_metrics),
        ]
    )
    run(
        [
            sys.executable,
            "tools/validate_audio_capture_metrics.py",
            str(capture_metrics),
            "--allow-missing-host-command",
        ]
    )
    run(
        [
            sys.executable,
            "tools/collect_audio_no_command_frontier.py",
            "--metrics",
            str(capture_metrics),
            "--output",
            str(no_command_frontier),
        ]
    )
    run([sys.executable, "tools/validate_audio_no_command_frontier.py", str(no_command_frontier)])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
