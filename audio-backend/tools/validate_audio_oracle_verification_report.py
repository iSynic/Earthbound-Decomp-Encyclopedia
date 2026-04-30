#!/usr/bin/env python3
"""Validate the compact audio oracle verification report."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_REPORT = ROOT / "manifests" / "audio-oracle-verification-report.json"

ALLOWED_STATUSES = {
    "pending_reference_capture",
    "pass",
    "audio_equivalent_state_delta",
    "explained_timing_offset",
    "state_mismatch",
    "investigated_mismatch",
    "invalid_reference_output",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate the audio oracle verification report.")
    parser.add_argument("report", nargs="?", default=str(DEFAULT_REPORT))
    parser.add_argument("--require-representative-pass", action="store_true")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(report: dict[str, Any], *, require_representative_pass: bool) -> list[str]:
    errors: list[str] = []
    if report.get("schema") != "earthbound-decomp.audio-oracle-verification-report.v1":
        errors.append(f"unexpected schema: {report.get('schema')}")
    records = report.get("records", [])
    if int(report.get("job_count", -1)) != len(records):
        errors.append("job_count does not match records")

    status_counts: Counter[str] = Counter()
    seen: set[int] = set()
    wav_exact = 0
    header_matches = 0
    dsp_matches = 0
    full_ram_matches = 0
    independent_count = 0

    for record in records:
        track_id = int(record.get("track_id", -1))
        if track_id in seen:
            errors.append(f"duplicate track id {track_id}")
        seen.add(track_id)
        status = str(record.get("status", ""))
        if status not in ALLOWED_STATUSES:
            errors.append(f"track {track_id}: unexpected status {status}")
        status_counts[status] += 1
        if record.get("wav_byte_exact_match"):
            wav_exact += 1
        if record.get("independent_emulator_capture"):
            independent_count += 1
        spc = record.get("spc_state", {})
        if spc.get("header_registers_match"):
            header_matches += 1
        if spc.get("dsp_register_match"):
            dsp_matches += 1
        if spc.get("full_apu_ram_match"):
            full_ram_matches += 1
        alignment = record.get("pcm_alignment", {})
        if float(alignment.get("normalized_correlation", 0.0)) < 0:
            errors.append(f"track {track_id}: negative correlation")

    if dict(status_counts) != report.get("status_counts"):
        errors.append("status_counts does not match records")
    gates = report.get("gate_results", {})
    if require_representative_pass and not gates.get("representative_oracle_gate_passed"):
        errors.append("representative oracle gate is not passed")
    if gates.get("release_quality_playback_claim_ready") and not (
        gates.get("representative_oracle_gate_passed")
        and gates.get("independent_emulator_gate_passed")
        and gates.get("all_track_oracle_gate_passed")
    ):
        errors.append("release-quality claim ready without all required gates")

    audio = report.get("audio_equivalence", {})
    if int(audio.get("wav_byte_exact_match_count", -1)) != wav_exact:
        errors.append("WAV exact count does not match records")
    if int(audio.get("header_register_match_count", -1)) != header_matches:
        errors.append("header match count does not match records")
    if int(audio.get("dsp_register_match_count", -1)) != dsp_matches:
        errors.append("DSP match count does not match records")
    if int(audio.get("full_apu_ram_match_count", -1)) != full_ram_matches:
        errors.append("full APU RAM match count does not match records")

    if gates.get("independent_emulator_gate_passed") and independent_count != len(records):
        errors.append("independent gate passed but not every record is independent")
    if "why_not_final" not in report.get("interpretation", {}):
        errors.append("report must include why_not_final interpretation")
    return errors


def main() -> int:
    args = parse_args()
    report = load_json(Path(args.report))
    errors = validate(report, require_representative_pass=args.require_representative_pass)
    if errors:
        print("Audio oracle verification report validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "Audio oracle verification report validation OK: "
        f"{report['job_count']} jobs, gates {report['gate_results']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
