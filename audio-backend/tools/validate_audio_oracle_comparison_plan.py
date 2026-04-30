#!/usr/bin/env python3
"""Validate the audio emulator-oracle comparison plan."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PLAN = ROOT / "manifests" / "audio-oracle-comparison-plan.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate the audio oracle comparison plan.")
    parser.add_argument("plan", nargs="?", default=str(DEFAULT_PLAN))
    parser.add_argument(
        "--allow-missing-source-outputs",
        action="store_true",
        help="Do not fail if local playback/export build outputs are absent.",
    )
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def resolve_repo_path(path_text: str) -> Path:
    path = Path(path_text)
    return path if path.is_absolute() else ROOT / path


def validate(plan: dict[str, Any], *, allow_missing_source_outputs: bool) -> list[str]:
    errors: list[str] = []
    if plan.get("schema") != "earthbound-decomp.audio-oracle-comparison-plan.v1":
        errors.append(f"unexpected schema: {plan.get('schema')}")
    if plan.get("status") != "oracle_plan_ready_no_reference_captures_yet":
        errors.append(f"unexpected status: {plan.get('status')}")

    source_policy = plan.get("source_policy", {})
    if not source_policy.get("requires_user_supplied_rom"):
        errors.append("source policy must require a user-supplied ROM")
    if not source_policy.get("generated_reference_outputs_are_ignored"):
        errors.append("reference outputs must be generated/ignored")
    output_root = str(source_policy.get("generated_outputs_root", ""))
    if not output_root.startswith("build/audio/oracle-comparison"):
        errors.append(f"unexpected generated output root: {output_root}")
    if not source_policy.get("do_not_distribute_reference_spc_wav_or_rom_derived_audio"):
        errors.append("policy must forbid distributing ROM-derived reference audio")

    jobs = plan.get("jobs", [])
    if int(plan.get("job_count", -1)) != len(jobs):
        errors.append(f"job_count {plan.get('job_count')} does not match {len(jobs)} jobs")
    if plan.get("job_scope") == "representative_tracks" and len(jobs) < 10:
        errors.append("representative oracle plan should include at least 10 jobs")
    if plan.get("job_scope") == "all_tracks" and len(jobs) < 100:
        errors.append("all-track oracle plan is unexpectedly small")

    oracle_ids = {str(oracle.get("id")) for oracle in plan.get("reference_oracles", [])}
    if "ares" not in oracle_ids:
        errors.append("missing ares reference oracle")
    if not any("mesen" in oracle_id or "bsnes" in oracle_id or "mednafen" in oracle_id for oracle_id in oracle_ids):
        errors.append("missing external emulator oracle record")

    required_levels = {
        "spc_container_signature",
        "spc_header_registers",
        "apu_ram_region_hashes",
        "dsp_register_snapshot",
        "pcm_feature_similarity",
        "pcm_alignment_tolerant_similarity",
    }
    seen_track_ids: set[int] = set()
    for job in jobs:
        job_id = str(job.get("job_id", ""))
        track_id = int(job.get("track_id", -1))
        if not job_id:
            errors.append("job without job_id")
        if track_id <= 0:
            errors.append(f"{job_id}: invalid track_id {track_id}")
        if track_id in seen_track_ids:
            errors.append(f"duplicate track_id {track_id}")
        seen_track_ids.add(track_id)

        levels = set(job.get("comparison_levels", []))
        missing_levels = required_levels - levels
        if missing_levels:
            errors.append(f"{job_id}: missing comparison levels {sorted(missing_levels)}")

        source_spc = job.get("source_spc", {})
        source_render = job.get("source_render", {})
        for label, record in (("source_spc", source_spc), ("source_render", source_render)):
            path_text = str(record.get("path", ""))
            if not path_text:
                errors.append(f"{job_id}: missing {label} path")
                continue
            if not allow_missing_source_outputs and not resolve_repo_path(path_text).exists():
                errors.append(f"{job_id}: {label} path missing: {path_text}")
            if not record.get("sha1"):
                errors.append(f"{job_id}: missing {label} SHA-1")
            if int(record.get("bytes", 0)) <= 0:
                errors.append(f"{job_id}: missing {label} byte count")

        outputs = job.get("reference_capture_outputs", {})
        for key in ("spc_snapshot", "pcm_wav", "capture_metadata", "comparison_result"):
            path_text = str(outputs.get(key, ""))
            if not path_text.startswith(f"{output_root.rstrip('/')}/"):
                errors.append(f"{job_id}: {key} must stay under {output_root}")

    thresholds = plan.get("comparison_policy", {}).get("recommended_pcm_thresholds", {})
    if int(thresholds.get("sample_rate", 0)) != 32000:
        errors.append("PCM threshold sample_rate must be 32000")
    if int(thresholds.get("channels", 0)) != 2:
        errors.append("PCM threshold channels must be 2")
    if float(thresholds.get("minimum_seconds", 0.0)) < 30.0:
        errors.append("PCM threshold minimum_seconds must cover current 30-second export jobs")
    if float(thresholds.get("minimum_normalized_correlation_after_alignment", 0.0)) < 0.95:
        errors.append("PCM correlation threshold is too loose for release-quality comparison")

    release_gates = plan.get("release_gates", [])
    if len(release_gates) < 5:
        errors.append("release gate checklist is too short")
    return errors


def main() -> int:
    args = parse_args()
    plan = load_json(Path(args.plan))
    errors = validate(plan, allow_missing_source_outputs=args.allow_missing_source_outputs)
    if errors:
        print("Audio oracle comparison plan validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Audio oracle comparison plan validation OK: {plan['job_count']} {plan['job_scope']} jobs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
