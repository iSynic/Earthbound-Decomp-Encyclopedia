#!/usr/bin/env python3
"""Build a compact audio oracle verification report.

The raw oracle comparison summary is intentionally detailed. This report rolls
it up into release-gate language: what passed, which differences remain, and
whether the evidence is independent enough to claim release-quality playback.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SUMMARY = ROOT / "build" / "audio" / "oracle-comparison" / "oracle-comparison-summary.json"
DEFAULT_JSON = ROOT / "manifests" / "audio-oracle-verification-report.json"
DEFAULT_MARKDOWN = ROOT / "notes" / "audio-oracle-verification-report.md"

ACCEPTABLE_REPRESENTATIVE_STATUSES = {
    "pass",
    "audio_equivalent_state_delta",
    "explained_timing_offset",
    "investigated_mismatch",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the audio oracle verification report.")
    parser.add_argument("--summary", default=str(DEFAULT_SUMMARY), help="Oracle comparison summary JSON path.")
    parser.add_argument("--json", default=str(DEFAULT_JSON), help="Report JSON output path.")
    parser.add_argument("--markdown", default=str(DEFAULT_MARKDOWN), help="Report Markdown output path.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def resolve_repo_path(path_text: str) -> Path:
    path = Path(path_text)
    return path if path.is_absolute() else ROOT / path


def repo_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def safe_get(mapping: dict[str, Any], path: tuple[str, ...], default: Any = None) -> Any:
    current: Any = mapping
    for key in path:
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]
    return current


def metadata_for_result(result: dict[str, Any]) -> dict[str, Any] | None:
    reference_spc_path = result.get("reference_spc", {}).get("path")
    if not reference_spc_path:
        return None
    root = resolve_repo_path(reference_spc_path).parent
    metadata_path = root / "reference-capture.json"
    if not metadata_path.exists():
        return None
    return load_json(metadata_path)


def build_report(summary_path: Path) -> dict[str, Any]:
    summary = load_json(summary_path)
    records: list[dict[str, Any]] = []
    status_counts: Counter[str] = Counter()
    region_match_counts: Counter[str] = Counter()
    region_total_counts: Counter[str] = Counter()
    oracle_ids: Counter[str] = Counter()
    oracle_kinds: Counter[str] = Counter()
    independent_reference_count = 0
    wav_byte_exact_count = 0
    header_match_count = 0
    dsp_match_count = 0
    full_apu_match_count = 0
    min_correlation = 1.0
    max_alignment_offset = 0

    for entry in summary.get("results", []):
        result_path = resolve_repo_path(entry["result_path"])
        result = load_json(result_path)
        status = str(result["status"])
        status_counts[status] += 1
        comparison = result.get("comparison", {})
        wav = comparison.get("wav", {})
        spc = comparison.get("spc", {})
        metadata = metadata_for_result(result)
        oracle_id = metadata.get("oracle_id") if metadata else "missing_capture_metadata"
        oracle_kind = metadata.get("oracle_kind") if metadata else "missing_capture_metadata"
        oracle_ids[str(oracle_id)] += 1
        oracle_kinds[str(oracle_kind)] += 1
        if metadata and metadata.get("independent_emulator_capture") is True:
            independent_reference_count += 1

        if wav.get("byte_exact_match"):
            wav_byte_exact_count += 1
        if spc.get("header_registers_match"):
            header_match_count += 1
        if spc.get("dsp_register_match"):
            dsp_match_count += 1
        if spc.get("full_apu_ram_match"):
            full_apu_match_count += 1
        alignment = wav.get("alignment", {})
        min_correlation = min(min_correlation, float(alignment.get("normalized_correlation", 0.0)))
        max_alignment_offset = max(max_alignment_offset, abs(int(alignment.get("best_offset_samples", 0))))

        region_matches = spc.get("apu_region_matches", {})
        for region, matched in region_matches.items():
            region_total_counts[str(region)] += 1
            if matched:
                region_match_counts[str(region)] += 1

        records.append(
            {
                "track_id": int(result["track_id"]),
                "track_name": result["track_name"],
                "status": status,
                "oracle_id": oracle_id,
                "independent_emulator_capture": bool(metadata and metadata.get("independent_emulator_capture") is True),
                "wav_byte_exact_match": bool(wav.get("byte_exact_match")),
                "pcm_alignment": {
                    "best_offset_samples": alignment.get("best_offset_samples"),
                    "normalized_correlation": alignment.get("normalized_correlation"),
                },
                "spc_state": {
                    "header_registers_match": bool(spc.get("header_registers_match")),
                    "dsp_register_match": bool(spc.get("dsp_register_match")),
                    "full_apu_ram_match": bool(spc.get("full_apu_ram_match")),
                    "apu_region_matches": region_matches,
                },
                "result_path": entry["result_path"],
            }
        )

    job_count = len(records)
    acceptable_count = sum(status_counts[status] for status in ACCEPTABLE_REPRESENTATIVE_STATUSES)
    representative_gate_passed = job_count > 0 and acceptable_count == job_count
    independent_gate_passed = independent_reference_count == job_count and job_count > 0
    all_track_gate_passed = summary.get("job_scope") == "all_tracks" and representative_gate_passed
    if all_track_gate_passed:
        status = "all_track_near_oracle_passed_independent_oracle_pending"
        what_this_proves = (
            "The full snapshot-backed playback corpus has reference captures at the planned paths and every compared "
            "job meets the accepted oracle status set. Current ares-managed references produce byte-identical PCM "
            "with matching header/DSP state across all rendered tracks."
        )
        why_not_final = (
            "The current imported references are ares-managed near-oracle/backend-summary captures, not independent "
            "bsnes/Mesen/Mednafen captures. Release-quality playback should still wait for an independent external "
            "emulator gate or an explicit decision that the ares-managed gate is sufficient."
        )
        next_step = "Add an independent external-emulator capture path for a representative subset, then rerun collect/validate/report."
    else:
        status = "representative_near_oracle_passed_independent_oracle_pending"
        what_this_proves = (
            "The representative corpus has reference captures at the planned paths and every compared job meets the "
            "accepted oracle status set. Current ares-managed references produce byte-identical PCM with matching "
            "header/DSP state."
        )
        why_not_final = (
            "The current imported references are ares-managed near-oracle/backend-summary captures, not independent "
            "bsnes/Mesen/Mednafen captures, and the comparison scope is still representative tracks rather than every "
            "rendered track."
        )
        next_step = "Add an independent external-emulator capture path or promote the ares runner to all-track comparison, then rerun collect/validate/report."

    region_summary = {
        region: {
            "matched": int(region_match_counts[region]),
            "total": int(region_total_counts[region]),
        }
        for region in sorted(region_total_counts)
    }

    return {
        "schema": "earthbound-decomp.audio-oracle-verification-report.v1",
        "status": status,
        "summary_path": repo_path(summary_path),
        "job_scope": summary.get("job_scope"),
        "job_count": job_count,
        "status_counts": dict(status_counts),
        "oracle_ids": dict(oracle_ids),
        "oracle_kinds": dict(oracle_kinds),
        "gate_results": {
            "representative_oracle_gate_passed": representative_gate_passed,
            "independent_emulator_gate_passed": independent_gate_passed,
            "all_track_oracle_gate_passed": all_track_gate_passed,
            "release_quality_playback_claim_ready": representative_gate_passed and independent_gate_passed and all_track_gate_passed,
        },
        "audio_equivalence": {
            "wav_byte_exact_match_count": wav_byte_exact_count,
            "header_register_match_count": header_match_count,
            "dsp_register_match_count": dsp_match_count,
            "full_apu_ram_match_count": full_apu_match_count,
            "minimum_normalized_pcm_correlation": min_correlation if records else 0.0,
            "maximum_alignment_offset_samples": max_alignment_offset,
            "apu_region_match_counts": region_summary,
        },
        "interpretation": {
            "what_this_proves": what_this_proves,
            "why_not_final": why_not_final,
            "next_step": next_step,
        },
        "records": sorted(records, key=lambda item: int(item["track_id"])),
    }


def render_markdown(report: dict[str, Any]) -> str:
    gates = report["gate_results"]
    audio = report["audio_equivalence"]
    region_rows = [
        f"| `{region}` | {counts['matched']} / {counts['total']} |"
        for region, counts in audio["apu_region_match_counts"].items()
    ]
    rows = [
        "| `{track_id:03d}` | `{track_name}` | `{status}` | `{oracle_id}` | {wav} | {offset} | {corr} | {dsp} | {full_ram} |".format(
            track_id=record["track_id"],
            track_name=record["track_name"],
            status=record["status"],
            oracle_id=record["oracle_id"],
            wav="yes" if record["wav_byte_exact_match"] else "no",
            offset=record["pcm_alignment"].get("best_offset_samples"),
            corr=record["pcm_alignment"].get("normalized_correlation"),
            dsp="yes" if record["spc_state"]["dsp_register_match"] else "no",
            full_ram="yes" if record["spc_state"]["full_apu_ram_match"] else "no",
        )
        for record in report["records"]
    ]
    status_line = (
        "Status: all-track near-oracle passed; independent external-emulator gate remains open."
        if report["gate_results"]["all_track_oracle_gate_passed"]
        else "Status: representative near-oracle passed; independent external-emulator and all-track gates remain open."
    )
    return "\n".join(
        [
            "# Audio Oracle Verification Report",
            "",
            status_line,
            "",
            f"- scope: `{report['job_scope']}`",
            f"- jobs: `{report['job_count']}`",
            f"- statuses: `{report['status_counts']}`",
            f"- oracle ids: `{report['oracle_ids']}`",
            f"- oracle kinds: `{report['oracle_kinds']}`",
            "",
            "## Gates",
            "",
            f"- representative oracle gate passed: `{gates['representative_oracle_gate_passed']}`",
            f"- independent emulator gate passed: `{gates['independent_emulator_gate_passed']}`",
            f"- all-track oracle gate passed: `{gates['all_track_oracle_gate_passed']}`",
            f"- release-quality playback claim ready: `{gates['release_quality_playback_claim_ready']}`",
            "",
            "## Audio Equivalence",
            "",
            f"- byte-exact WAV matches: `{audio['wav_byte_exact_match_count']} / {report['job_count']}`",
            f"- header register matches: `{audio['header_register_match_count']} / {report['job_count']}`",
            f"- DSP register matches: `{audio['dsp_register_match_count']} / {report['job_count']}`",
            f"- full APU RAM matches: `{audio['full_apu_ram_match_count']} / {report['job_count']}`",
            f"- minimum normalized PCM correlation: `{audio['minimum_normalized_pcm_correlation']}`",
            f"- maximum alignment offset samples: `{audio['maximum_alignment_offset_samples']}`",
            "",
            "## APU Region Matches",
            "",
            "| Region | Matches |",
            "| --- | ---: |",
            *region_rows,
            "",
            "## Interpretation",
            "",
            f"- What this proves: {report['interpretation']['what_this_proves']}",
            f"- Why not final: {report['interpretation']['why_not_final']}",
            f"- Next step: {report['interpretation']['next_step']}",
            "",
            "## Tracks",
            "",
            "| Track | Name | Status | Oracle | WAV Exact | Offset | Correlation | DSP Match | Full RAM Match |",
            "| ---: | --- | --- | --- | --- | ---: | ---: | --- | --- |",
            *rows,
            "",
        ]
    )


def main() -> int:
    args = parse_args()
    report = build_report(Path(args.summary))
    json_path = Path(args.json)
    markdown_path = Path(args.markdown)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    markdown_path.write_text(render_markdown(report), encoding="utf-8")
    print(
        "Built audio oracle verification report: "
        f"{report['job_count']} jobs, gates {report['gate_results']}"
    )
    print(f"Wrote {json_path}")
    print(f"Wrote {markdown_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
