#!/usr/bin/env python3
"""Build the audio backend dependency and distribution policy manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_JSON = ROOT / "manifests" / "audio-dependency-policy.json"
DEFAULT_MARKDOWN = ROOT / "notes" / "audio-dependency-policy.md"
DEFAULT_ARES_ROOT = Path(os.environ.get("EARTHBOUND_ARES_ROOT", ROOT.parent / "ares-earthbound-audio-backend"))
DEFAULT_LIBGME_ROOT = Path(
    os.environ.get("EARTHBOUND_LIBGME_ROOT", ROOT.parent / "game-music-emu-earthbound-audio-backend")
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the audio dependency policy manifest.")
    parser.add_argument("--json", default=str(DEFAULT_JSON), help="JSON output path.")
    parser.add_argument("--markdown", default=str(DEFAULT_MARKDOWN), help="Markdown output path.")
    parser.add_argument("--ares-root", default=str(DEFAULT_ARES_ROOT), help="Local ares checkout path.")
    parser.add_argument("--libgme-root", default=str(DEFAULT_LIBGME_ROOT), help="Local libgme checkout path.")
    return parser.parse_args()


def sha1_file(path: Path) -> str | None:
    if not path.exists():
        return None
    digest = hashlib.sha1()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def git_head(path: Path) -> str | None:
    head_path = path / ".git" / "HEAD"
    if not head_path.exists():
        return None
    head = head_path.read_text(encoding="utf-8").strip()
    if head.startswith("ref: "):
        ref_path = path / ".git" / head[5:].strip()
        if ref_path.exists():
            return ref_path.read_text(encoding="utf-8").strip()
        packed_refs = path / ".git" / "packed-refs"
        if packed_refs.exists():
            ref_name = head[5:].strip()
            for line in packed_refs.read_text(encoding="utf-8").splitlines():
                if line.startswith("#") or not line.strip():
                    continue
                parts = line.split(" ")
                if len(parts) == 2 and parts[1] == ref_name:
                    return parts[0]
        return None
    return head


def dependency_record(
    *,
    dependency_id: str,
    role: str,
    root: Path,
    license_file: str,
    license_policy: str,
    integration_policy: str,
    distribution_policy: str,
    status: str,
) -> dict[str, Any]:
    license_path = root / license_file
    commit = git_head(root)
    return {
        "id": dependency_id,
        "role": role,
        "status": status,
        "local_root": "<local external checkout outside this repository>",
        "local_root_exists": root.exists(),
        "observed_commit": commit,
        "observed_commit_short": commit[:8] if commit else None,
        "license_file": license_file,
        "license_file_exists": license_path.exists(),
        "license_sha1": sha1_file(license_path),
        "license_policy": license_policy,
        "integration_policy": integration_policy,
        "distribution_policy": distribution_policy,
    }


def build_policy(ares_root: Path, libgme_root: Path) -> dict[str, Any]:
    return {
        "schema": "earthbound-decomp.audio-dependency-policy.v1",
        "status": "audio_dependency_policy_recorded",
        "source_policy": {
            "requires_user_supplied_rom": True,
            "generated_audio_outputs_are_ignored": True,
            "generated_outputs_root": "build/audio",
            "do_not_distribute_spc_wav_or_rom_derived_audio": True,
        },
        "dependencies": [
            dependency_record(
                dependency_id="ares",
                role="accuracy-first SNES/APU runtime and capture backend prototype",
                root=ares_root,
                license_file="LICENSE",
                license_policy="ISC/permissive for core ares; bundled third-party notices must be reviewed before vendoring or binary distribution.",
                integration_policy="External checkout/build for now. Future submodule is acceptable after license-notice review; avoid copying a carved subset until the boundary is stable.",
                distribution_policy="May be distributed with notices if license review is complete; current generated outputs remain local only.",
                status="local_external_checkout_used_by_diagnostic_harness",
            ),
            dependency_record(
                dependency_id="libgme",
                role="lightweight SPC snapshot playback/export renderer",
                root=libgme_root,
                license_file="license.txt",
                license_policy="LGPL-2.1; dynamic/external linkage preferred for app distribution, with notices and relinkability/source obligations respected.",
                integration_policy="External checkout/build for now. Keep the renderer swappable and avoid GPL-only optional components in the core path.",
                distribution_policy="Can support local playback/export with LGPL compliance; generated SPC/WAV outputs remain user-local ROM-derived artifacts.",
                status="local_external_checkout_used_by_snes_spc_render_harness",
            ),
            {
                "id": "bsnes_higan_mesen2_mednafen",
                "role": "optional reference oracles for accuracy comparison",
                "status": "reference_only_not_core_dependency",
                "local_root": None,
                "local_root_exists": False,
                "observed_commit": None,
                "license_file": None,
                "license_file_exists": False,
                "license_sha1": None,
                "license_policy": "GPL or mixed/non-core policies; keep optional and out-of-process unless the project intentionally changes license posture.",
                "integration_policy": "Use for comparison captures, not required app playback/export.",
                "distribution_policy": "Do not bundle as a required core dependency without explicit licensing decision.",
            },
        ],
        "release_gates": [
            "Generated ROM-derived SPC/WAV/PCM/sample outputs must stay ignored and out of commits.",
            "Dependency notices must be included before distributing binaries that invoke or link renderer backends.",
            "LGPL renderer integration must preserve relinkability or remain external/plugin-like.",
            "GPL reference tools must remain optional or out-of-process unless the whole relevant distribution adopts compatible terms.",
            "Public docs must state that end users provide their own ROM and that audio exports are generated locally.",
        ],
    }


def render_markdown(policy: dict[str, Any]) -> str:
    rows = [
        "| `{id}` | `{status}` | {role} | `{commit}` | {license_policy} | {integration_policy} |".format(
            id=dependency["id"],
            status=dependency["status"],
            role=dependency["role"],
            commit=dependency.get("observed_commit_short") or "",
            license_policy=dependency["license_policy"],
            integration_policy=dependency["integration_policy"],
        )
        for dependency in policy["dependencies"]
    ]
    gates = [f"- {gate}" for gate in policy["release_gates"]]
    return "\n".join(
        [
            "# Audio Dependency Policy",
            "",
            "Status: audio dependency and distribution policy recorded.",
            "",
            "This policy keeps the audio backend useful for the local Electron app and porter tooling without boxing the project into an accidental license posture.",
            "",
            "## Dependencies",
            "",
            "| Dependency | Status | Role | Commit | License policy | Integration policy |",
            "| --- | --- | --- | --- | --- | --- |",
            *rows,
            "",
            "## Release Gates",
            "",
            *gates,
            "",
        ]
    )


def main() -> int:
    args = parse_args()
    policy = build_policy(Path(args.ares_root), Path(args.libgme_root))
    json_path = Path(args.json)
    markdown_path = Path(args.markdown)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(policy, indent=2) + "\n", encoding="utf-8")
    markdown_path.write_text(render_markdown(policy), encoding="utf-8")
    print(f"Built audio dependency policy -> {json_path}")
    print(f"Wrote {markdown_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
