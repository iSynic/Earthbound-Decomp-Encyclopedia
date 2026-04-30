#!/usr/bin/env python3
"""Validate the audio backend dependency and distribution policy manifest."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_POLICY = ROOT / "manifests" / "audio-dependency-policy.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate the audio dependency policy manifest.")
    parser.add_argument("policy", nargs="?", default=str(DEFAULT_POLICY))
    return parser.parse_args()


def validate(policy: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if policy.get("schema") != "earthbound-decomp.audio-dependency-policy.v1":
        errors.append(f"unexpected schema: {policy.get('schema')}")
    source_policy = policy.get("source_policy", {})
    if not source_policy.get("requires_user_supplied_rom"):
        errors.append("source policy must require user-supplied ROM")
    if not source_policy.get("generated_audio_outputs_are_ignored"):
        errors.append("generated audio outputs must be ignored")
    if not source_policy.get("do_not_distribute_spc_wav_or_rom_derived_audio"):
        errors.append("policy must forbid distributing generated ROM-derived audio")
    dependencies = policy.get("dependencies", [])
    if len(dependencies) < 3:
        errors.append("expected ares, libgme, and reference dependency records")
    by_id = {dependency.get("id"): dependency for dependency in dependencies}
    for required in ("ares", "libgme", "bsnes_higan_mesen2_mednafen"):
        if required not in by_id:
            errors.append(f"missing dependency record {required}")
    for dependency_id in ("ares", "libgme"):
        dependency = by_id.get(dependency_id, {})
        if not dependency.get("local_root_exists"):
            errors.append(f"{dependency_id}: local root missing")
        if not dependency.get("observed_commit"):
            errors.append(f"{dependency_id}: observed commit missing")
        if not dependency.get("license_file_exists"):
            errors.append(f"{dependency_id}: license file missing")
        if not dependency.get("license_sha1"):
            errors.append(f"{dependency_id}: license SHA-1 missing")
    libgme = by_id.get("libgme", {})
    if "LGPL" not in str(libgme.get("license_policy", "")):
        errors.append("libgme policy must mention LGPL")
    refs = by_id.get("bsnes_higan_mesen2_mednafen", {})
    if "reference_only" not in str(refs.get("status", "")):
        errors.append("GPL/reference tools must be reference-only")
    release_gates = policy.get("release_gates", [])
    if len(release_gates) < 5:
        errors.append("release gate checklist is too short")
    return errors


def main() -> int:
    args = parse_args()
    policy = json.loads(Path(args.policy).read_text(encoding="utf-8"))
    errors = validate(policy)
    if errors:
        print("Audio dependency policy validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Audio dependency policy validation OK: {len(policy['dependencies'])} dependency records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
