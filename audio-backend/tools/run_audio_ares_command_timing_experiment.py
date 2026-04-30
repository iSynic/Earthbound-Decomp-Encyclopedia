#!/usr/bin/env python3
"""Run a native ares command-timing experiment."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUT = ROOT / "build" / "audio" / "command-on-first-read-jobs"
DEFAULT_ARES_HARNESS = (
    ROOT
    / "build"
    / "audio"
    / "ares-audio-harness-msvc"
    / "RelWithDebInfo"
    / "earthbound_ares_audio_harness.exe"
)
MODE_FLAGS = {
    "after_timer_enable": [],
    "initial": ["--diagnostic-command-preseed-initial"],
    "on_first_read": ["--diagnostic-command-preseed-on-first-read"],
    "disabled": ["--disable-diagnostic-command-preseed"],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a command-timing ares audio probe experiment.")
    parser.add_argument("--mode", default="on_first_read", choices=sorted(MODE_FLAGS))
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
    timing_frontier = out_dir / "command-timing-frontier.json"
    mailbox_frontier = out_dir / "mailbox-frontier.json"
    harness = Path(args.ares_harness)
    if not harness.exists():
        raise FileNotFoundError(f"missing ares harness: {harness}")

    run([sys.executable, "tools/build_audio_backend_jobs.py", "--backend", "ares", "--out", str(out_dir)])
    external = [
        str(harness),
        "--job",
        "{job}",
        "--result",
        "{result}",
        *MODE_FLAGS[args.mode],
    ]
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
            *external,
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
    allow_missing = ["--allow-missing-host-command"] if args.mode == "disabled" else []
    run([sys.executable, "tools/validate_audio_capture_metrics.py", str(capture_metrics), *allow_missing])
    run(
        [
            sys.executable,
            "tools/collect_audio_command_timing_frontier.py",
            "--metrics",
            str(capture_metrics),
            "--output",
            str(timing_frontier),
        ]
    )
    validate_args = [sys.executable, "tools/validate_audio_command_timing_frontier.py", str(timing_frontier)]
    if args.mode != "disabled":
        validate_args += ["--require-key-on"]
    expected_mode = "on_first_port0_read" if args.mode == "on_first_read" else args.mode
    validate_args += ["--expect-mode", expected_mode]
    run(validate_args)
    run(
        [
            sys.executable,
            "tools/collect_audio_mailbox_frontier.py",
            "--jobs",
            str(jobs_index),
            "--output",
            str(mailbox_frontier),
        ]
    )
    mailbox_validate_args = [
        sys.executable,
        "tools/validate_audio_mailbox_frontier.py",
        str(mailbox_frontier),
        "--expect-mode",
        expected_mode,
    ]
    if args.mode != "disabled":
        mailbox_validate_args += ["--require-key-on"]
    run(mailbox_validate_args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
