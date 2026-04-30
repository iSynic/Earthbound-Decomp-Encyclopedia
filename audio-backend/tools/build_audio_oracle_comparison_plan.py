#!/usr/bin/env python3
"""Build the audio emulator-oracle comparison plan.

This does not invoke bsnes/Mesen/Mednafen. It pins the comparison contract and
job set so a future runner can fill in reference captures without changing the
playback/export backend schema again.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PLAYBACK_MANIFEST = (
    ROOT
    / "build"
    / "audio"
    / "c0ab06-change-music-fusion-render-jobs-all"
    / "playback-export-manifest.json"
)
DEFAULT_JSON = ROOT / "manifests" / "audio-oracle-comparison-plan.json"
DEFAULT_MARKDOWN = ROOT / "notes" / "audio-oracle-comparison-plan.md"
DEFAULT_OUTPUT_ROOT = "build/audio/oracle-comparison"

REPRESENTATIVE_TRACK_IDS = (
    1,    # GAS_STATION: quick audible smoke
    2,    # NAMING_SCREEN: menu path
    46,   # ONETT: common overworld
    56,   # SUMMERS: melodic field track
    72,   # GIYGAS_AWAKENS: late-game ambience
    76,   # RUNAWAY5_CONCERT_1: event music
    82,   # BICYCLE: vehicle state
    83,   # SKY_RUNNER: vehicle/event state
    92,   # COFFEE_BREAK: long-form scene music
    95,   # SMILES_AND_TEARS: credits/ending style
    96,   # VS_CRANKY_LADY: battle family
    100,  # VS_NEW_AGE_RETRO_HIPPIE: battle family
    105,  # POKEY_MEANS_BUSINESS: boss/late-game battle
    109,  # EXPLOSION: sound-effect-like music table entry
    121,  # ONETT_INTRO: scripted intro
    133,  # HIDDEN_SONG: unused/hidden content
    157,  # ATTRACT_MODE: title/attract path
    175,  # TITLE_SCREEN: frontend/title path
    185,  # GIYGAS_PHASE3: late-game sequence
    190,  # GIYGAS_DEATH: late-game sequence
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the audio oracle comparison plan.")
    parser.add_argument(
        "--playback-manifest",
        default=str(DEFAULT_PLAYBACK_MANIFEST),
        help="Validated playback/export manifest to plan comparisons from.",
    )
    parser.add_argument("--json", default=str(DEFAULT_JSON), help="JSON output path.")
    parser.add_argument("--markdown", default=str(DEFAULT_MARKDOWN), help="Markdown output path.")
    parser.add_argument(
        "--all-tracks",
        action="store_true",
        help="Build comparison jobs for every playback/export track instead of the representative set.",
    )
    parser.add_argument(
        "--output-root",
        default=DEFAULT_OUTPUT_ROOT,
        help="Ignored reference output root. Defaults to build/audio/oracle-comparison.",
    )
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path_text: str | Path) -> str:
    path = Path(path_text)
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except (OSError, ValueError):
        return path.as_posix()


def oracle_output_root(track_id: int, track_name: str, output_root: str) -> str:
    slug = track_name.lower()
    slug = "".join(ch if ch.isalnum() or ch in "-_" else "_" for ch in slug)
    return f"{output_root.rstrip('/')}/track-{track_id:03d}-{slug}"


def build_jobs(playback: dict[str, Any], *, all_tracks: bool, output_root: str) -> list[dict[str, Any]]:
    tracks = [track for track in playback.get("tracks", []) if track.get("status") == "ok" and track.get("valid")]
    tracks.sort(key=lambda item: int(item["track_id"]))
    if not all_tracks:
        wanted = set(REPRESENTATIVE_TRACK_IDS)
        tracks = [track for track in tracks if int(track["track_id"]) in wanted]

    jobs: list[dict[str, Any]] = []
    for track in tracks:
        track_id = int(track["track_id"])
        track_name = str(track["track_name"])
        track_output_root = oracle_output_root(track_id, track_name, output_root)
        source_spc = track.get("source_spc", {})
        rendered_wav = track.get("rendered_wav", {})
        jobs.append(
            {
                "job_id": f"oracle-track-{track_id:03d}-{track_name.lower()}",
                "track_id": track_id,
                "track_name": track_name,
                "source_state": track.get("source_state"),
                "source_spc": {
                    "path": rel(str(source_spc.get("path", ""))),
                    "sha1": source_spc.get("sha1"),
                    "bytes": source_spc.get("bytes"),
                },
                "source_render": {
                    "path": rel(str(rendered_wav.get("path", ""))),
                    "sha1": rendered_wav.get("sha1"),
                    "bytes": rendered_wav.get("bytes"),
                    "metrics": track.get("metrics", {}),
                },
                "reference_capture_outputs": {
                    "spc_snapshot": f"{track_output_root}/reference-capture.spc",
                    "pcm_wav": f"{track_output_root}/reference-render.wav",
                    "capture_metadata": f"{track_output_root}/reference-capture.json",
                    "comparison_result": f"{track_output_root}/oracle-comparison-result.json",
                },
                "comparison_levels": [
                    "spc_container_signature",
                    "spc_header_registers",
                    "apu_ram_region_hashes",
                    "dsp_register_snapshot",
                    "pcm_feature_similarity",
                    "pcm_alignment_tolerant_similarity",
                ],
            }
        )
    return jobs


def build_plan(playback_manifest_path: Path, *, all_tracks: bool, output_root: str) -> dict[str, Any]:
    playback = load_json(playback_manifest_path)
    jobs = build_jobs(playback, all_tracks=all_tracks, output_root=output_root)
    return {
        "schema": "earthbound-decomp.audio-oracle-comparison-plan.v1",
        "status": "oracle_plan_ready_no_reference_captures_yet",
        "playback_manifest": rel(playback_manifest_path),
        "playback_manifest_track_count": playback.get("track_count"),
        "playback_manifest_skipped_count": playback.get("skipped_count"),
        "job_scope": "all_tracks" if all_tracks else "representative_tracks",
        "job_count": len(jobs),
        "source_policy": {
            "requires_user_supplied_rom": True,
            "generated_reference_outputs_are_ignored": True,
            "generated_outputs_root": output_root,
            "do_not_distribute_reference_spc_wav_or_rom_derived_audio": True,
        },
        "reference_oracles": [
            {
                "id": "ares",
                "role": "permissive accuracy-first in-process/out-of-tree reference capture runner",
                "license_policy": "ISC/permissive core; keep notices reviewed before bundling",
                "integration_policy": "preferred first implementation target because the project already has local ares harnesses",
                "status": "runner_pending",
            },
            {
                "id": "mesen2_or_bsnes_higan_or_mednafen",
                "role": "external emulator validation oracle",
                "license_policy": "GPL or mixed policies; optional out-of-process validation only",
                "integration_policy": "use to corroborate ares/libgme output, not as a required app dependency",
                "status": "optional_runner_pending",
            },
        ],
        "comparison_policy": {
            "spc_exactness": "compare signatures, header registers, selected APU RAM region hashes, and DSP register snapshots where the reference exposes them",
            "pcm_exactness": "do not require byte-perfect PCM across independent renderers before alignment/timing has been characterized",
            "minimum_first_gate": "all representative jobs produce reference captures and classify as pass, audio_equivalent_state_delta, explained_timing_offset, or investigated_mismatch",
            "promotion_gate": "expand the same comparison contract from representative_tracks to all_tracks after the runner is stable",
            "recommended_pcm_thresholds": {
                "sample_rate": 32000,
                "channels": 2,
                "bits_per_sample": 16,
                "minimum_seconds": 30.0,
                "minimum_normalized_correlation_after_alignment": 0.98,
                "maximum_leading_silence_delta_samples": 4096,
            },
        },
        "release_gates": [
            "Reference captures must be generated locally from a user-provided ROM.",
            "Reference SPC/WAV/PCM outputs must stay under ignored build/audio paths.",
            "Each mismatch must be classified as timing offset, renderer difference, snapshot-state difference, or unknown.",
            "Representative-track oracle comparison must pass before claiming release-quality audio playback/export.",
            "All-track oracle comparison should pass before claiming fully validated audio reconstruction.",
        ],
        "jobs": jobs,
    }


def render_markdown(plan: dict[str, Any]) -> str:
    oracle_rows = [
        "| `{id}` | `{status}` | {role} | {integration_policy} |".format(**oracle)
        for oracle in plan["reference_oracles"]
    ]
    job_rows = [
        "| `{track_id:03d}` | `{track_name}` | `{source_spc}` | `{reference}` |".format(
            track_id=job["track_id"],
            track_name=job["track_name"],
            source_spc=Path(job["source_spc"]["path"]).name,
            reference=job["reference_capture_outputs"]["comparison_result"],
        )
        for job in plan["jobs"]
    ]
    gates = [f"- {gate}" for gate in plan["release_gates"]]
    thresholds = plan["comparison_policy"]["recommended_pcm_thresholds"]
    return "\n".join(
        [
            "# Audio Oracle Comparison Plan",
            "",
            "Status: oracle comparison contract ready; reference capture runner pending.",
            "",
            f"- scope: `{plan['job_scope']}`",
            f"- jobs: `{plan['job_count']}`",
            f"- source playback manifest: `{plan['playback_manifest']}`",
            f"- generated output root: `{plan['source_policy']['generated_outputs_root']}`",
            "",
            "## Reference Oracles",
            "",
            "| Oracle | Status | Role | Integration policy |",
            "| --- | --- | --- | --- |",
            *oracle_rows,
            "",
            "## Comparison Policy",
            "",
            f"- SPC exactness: {plan['comparison_policy']['spc_exactness']}",
            f"- PCM exactness: {plan['comparison_policy']['pcm_exactness']}",
            f"- first gate: {plan['comparison_policy']['minimum_first_gate']}",
            f"- promotion gate: {plan['comparison_policy']['promotion_gate']}",
            f"- PCM thresholds: `{thresholds}`",
            "",
            "## Workflow",
            "",
            "1. Build or refresh this plan with `python tools/build_audio_oracle_comparison_plan.py`.",
            "2. Capture a planned track with the reference emulator as SPC plus 32 kHz stereo WAV.",
            "3. Import that capture with `python tools/import_audio_oracle_reference_capture.py --track-id <id> --spc <capture.spc> --wav <capture.wav> --oracle-id <emulator>`.",
            "4. Collect comparison records with `python tools/collect_audio_oracle_comparison_results.py`.",
            "5. Validate the gate with `python tools/validate_audio_oracle_comparison_summary.py`; add `--require-compared` only when the reference capture set should be complete.",
            "6. After the representative gate is stable, regenerate with `--all-tracks` and use the same import/collect/validate flow.",
            "",
            "Current ares-managed near-oracle result: full CHANGE_MUSIC/load-apply captures for the representative set classify `20 / 20` as `audio_equivalent_state_delta`: PCM output is byte-identical/zero-offset equivalent while full APU RAM differs in non-audio-affecting regions, with matching header registers and DSP registers.",
            "",
            "## Release Gates",
            "",
            *gates,
            "",
            "## Jobs",
            "",
            "| Track | Name | Source SPC | Comparison result path |",
            "| ---: | --- | --- | --- |",
            *job_rows,
            "",
        ]
    )


def main() -> int:
    args = parse_args()
    plan = build_plan(Path(args.playback_manifest), all_tracks=args.all_tracks, output_root=args.output_root)
    json_path = Path(args.json)
    markdown_path = Path(args.markdown)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(plan, indent=2) + "\n", encoding="utf-8")
    markdown_path.write_text(render_markdown(plan), encoding="utf-8")
    print(f"Built audio oracle comparison plan: {plan['job_count']} jobs -> {json_path}")
    print(f"Wrote {markdown_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
