#!/usr/bin/env python3
"""Collect audio oracle comparison results from a comparison plan.

The first useful state is explicit pending records. Once an emulator runner
produces reference SPC/WAV files at the planned paths, this same collector
summarizes file integrity and basic WAV feature deltas.
"""

from __future__ import annotations

import argparse
import array
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PLAN = ROOT / "manifests" / "audio-oracle-comparison-plan.json"
DEFAULT_SUMMARY = ROOT / "build" / "audio" / "oracle-comparison" / "oracle-comparison-summary.json"
SPC_SIGNATURE = b"SNES-SPC700 Sound File Data"
SPC_RAM_OFFSET = 0x100
SPC_RAM_SIZE = 0x10000
SPC_DSP_OFFSET = 0x10100
SPC_DSP_SIZE = 0x80
SPC_REGISTERS = {
    "pc_low": 0x25,
    "pc_high": 0x26,
    "a": 0x27,
    "x": 0x28,
    "y": 0x29,
    "psw": 0x2A,
    "sp": 0x2B,
}
APU_REGIONS = {
    "driver_and_overlay": (0x0500, 0x468B),
    "runtime_tables_and_sequences": (0x2000, 0x6C00),
    "brr_sample_payloads": (0x6C00, 0xE700),
    "full_apu_ram": (0x0000, 0x10000),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Collect audio oracle comparison results.")
    parser.add_argument("--plan", default=str(DEFAULT_PLAN), help="Oracle comparison plan JSON path.")
    parser.add_argument("--summary", default=str(DEFAULT_SUMMARY), help="Summary JSON output path.")
    parser.add_argument("--max-align-samples", type=int, help="Override maximum PCM alignment search window.")
    parser.add_argument("--correlation-threshold", type=float, help="Override minimum normalized PCM correlation.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sha1_file(path: Path) -> str:
    digest = hashlib.sha1()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def resolve_repo_path(path_text: str) -> Path:
    path = Path(path_text)
    return path if path.is_absolute() else ROOT / path


def read_u16(data: bytes, offset: int) -> int:
    return int.from_bytes(data[offset : offset + 2], "little")


def read_u32(data: bytes, offset: int) -> int:
    return int.from_bytes(data[offset : offset + 4], "little")


def wav_info(path: Path) -> dict[str, int]:
    data = path.read_bytes()
    if len(data) < 44 or data[0:4] != b"RIFF" or data[8:12] != b"WAVE":
        raise ValueError("missing RIFF/WAVE header")
    if data[12:16] != b"fmt ":
        raise ValueError("missing canonical fmt chunk")
    fmt_size = read_u32(data, 16)
    data_offset = 20 + fmt_size
    if len(data) < data_offset + 8 or data[data_offset : data_offset + 4] != b"data":
        raise ValueError("missing canonical data chunk")
    return {
        "channels": read_u16(data, 22),
        "sample_rate": read_u32(data, 24),
        "bits_per_sample": read_u16(data, 34),
        "data_bytes": read_u32(data, data_offset + 4),
        "total_samples": read_u32(data, data_offset + 4) // 2,
    }


def wav_samples(path: Path) -> array.array:
    data = path.read_bytes()
    if len(data) < 44 or data[0:4] != b"RIFF" or data[8:12] != b"WAVE":
        raise ValueError("missing RIFF/WAVE header")
    fmt_size = read_u32(data, 16)
    data_offset = 20 + fmt_size
    if len(data) < data_offset + 8 or data[data_offset : data_offset + 4] != b"data":
        raise ValueError("missing canonical data chunk")
    payload_offset = data_offset + 8
    payload_size = read_u32(data, data_offset + 4)
    samples = array.array("h")
    samples.frombytes(data[payload_offset : payload_offset + payload_size])
    if samples.itemsize != 2:
        raise ValueError("platform short sample size is not 16-bit")
    return samples


def pcm_features(samples: array.array) -> dict[str, Any]:
    if not samples:
        return {
            "sample_count": 0,
            "peak_abs_sample": 0,
            "sum_abs_samples": 0,
            "rms_sample": 0.0,
            "nonzero_sample_count": 0,
            "first_nonzero_sample_index": -1,
            "last_nonzero_sample_index": -1,
        }
    peak = 0
    sum_abs = 0
    square_sum = 0.0
    nonzero = 0
    first = -1
    last = -1
    for index, sample in enumerate(samples):
        value = abs(int(sample))
        peak = max(peak, value)
        sum_abs += value
        square_sum += int(sample) * int(sample)
        if sample:
            nonzero += 1
            if first == -1:
                first = index
            last = index
    return {
        "sample_count": len(samples),
        "peak_abs_sample": peak,
        "sum_abs_samples": sum_abs,
        "rms_sample": math.sqrt(square_sum / len(samples)),
        "nonzero_sample_count": nonzero,
        "first_nonzero_sample_index": first,
        "last_nonzero_sample_index": last,
    }


def normalized_correlation(
    source: array.array,
    reference: array.array,
    *,
    max_align_samples: int,
    stride: int = 16,
) -> dict[str, Any]:
    if not source or not reference:
        return {"best_offset_samples": 0, "normalized_correlation": 0.0, "compared_samples": 0}
    offsets = list(range(-max_align_samples, max_align_samples + 1, stride))
    if 0 not in offsets:
        offsets.append(0)
    best_offset = 0
    best_corr = -1.0
    best_count = 0
    for offset in offsets:
        source_start = max(0, offset)
        reference_start = max(0, -offset)
        count = min(len(source) - source_start, len(reference) - reference_start)
        if count <= 0:
            continue
        dot = 0.0
        source_square = 0.0
        reference_square = 0.0
        compared = 0
        for index in range(0, count, stride):
            a = int(source[source_start + index])
            b = int(reference[reference_start + index])
            dot += a * b
            source_square += a * a
            reference_square += b * b
            compared += 1
        if not source_square or not reference_square:
            corr = 0.0
        else:
            corr = dot / math.sqrt(source_square * reference_square)
        if corr > best_corr:
            best_corr = corr
            best_offset = offset
            best_count = compared
    return {
        "best_offset_samples": best_offset,
        "normalized_correlation": round(best_corr, 6),
        "compared_samples": best_count,
        "stride": stride,
        "search_window_samples": max_align_samples,
    }


def sha1_bytes(data: bytes) -> str:
    return hashlib.sha1(data).hexdigest()


def spc_info(path: Path) -> dict[str, Any]:
    data = path.read_bytes()
    ram = data[SPC_RAM_OFFSET : SPC_RAM_OFFSET + SPC_RAM_SIZE] if len(data) >= SPC_RAM_OFFSET + SPC_RAM_SIZE else b""
    dsp = data[SPC_DSP_OFFSET : SPC_DSP_OFFSET + SPC_DSP_SIZE] if len(data) >= SPC_DSP_OFFSET + SPC_DSP_SIZE else b""
    registers = {
        name: data[offset] if len(data) > offset else None
        for name, offset in SPC_REGISTERS.items()
    }
    if registers["pc_low"] is not None and registers["pc_high"] is not None:
        registers["pc"] = (int(registers["pc_high"]) << 8) | int(registers["pc_low"])
    region_hashes: dict[str, dict[str, Any]] = {}
    for name, (start, end) in APU_REGIONS.items():
        region = ram[start:end] if len(ram) == SPC_RAM_SIZE else b""
        region_hashes[name] = {
            "start": f"0x{start:04X}",
            "end": f"0x{end:04X}",
            "bytes": len(region),
            "sha1": sha1_bytes(region) if region else None,
        }
    return {
        "signature_ok": data.startswith(SPC_SIGNATURE),
        "registers": registers,
        "ram_sha1": sha1_bytes(ram) if len(ram) == SPC_RAM_SIZE else None,
        "dsp_register_sha1": sha1_bytes(dsp) if len(dsp) == SPC_DSP_SIZE else None,
        "dsp_nonzero_count": sum(1 for byte in dsp if byte) if len(dsp) == SPC_DSP_SIZE else None,
        "apu_region_hashes": region_hashes,
    }


def file_record(path_text: str) -> dict[str, Any]:
    path = resolve_repo_path(path_text)
    record: dict[str, Any] = {
        "path": path_text,
        "exists": path.exists(),
    }
    if path.exists():
        record.update(
            {
                "bytes": path.stat().st_size,
                "sha1": sha1_file(path),
            }
        )
    return record


def classify_comparison(
    *,
    errors: list[str],
    missing: list[str],
    spc_comparison: dict[str, Any],
    wav_comparison: dict[str, Any],
    correlation_threshold: float,
    max_align_samples: int,
) -> str:
    if missing:
        return "pending_reference_capture"
    if errors:
        return "invalid_reference_output"
    if not spc_comparison.get("source_signature_ok") or not spc_comparison.get("reference_signature_ok"):
        return "invalid_reference_output"
    if spc_comparison.get("byte_exact_match"):
        return "pass"
    if (
        wav_comparison.get("byte_exact_match")
        and spc_comparison.get("header_registers_match")
        and spc_comparison.get("dsp_register_match")
    ):
        return "audio_equivalent_state_delta"
    correlation = float(wav_comparison.get("alignment", {}).get("normalized_correlation", 0.0))
    offset = abs(int(wav_comparison.get("alignment", {}).get("best_offset_samples", 0)))
    if correlation >= correlation_threshold and offset <= max_align_samples:
        return "explained_timing_offset"
    if not spc_comparison.get("full_apu_ram_match") or not spc_comparison.get("dsp_register_match"):
        return "state_mismatch"
    return "investigated_mismatch"


def compare_job(
    job: dict[str, Any],
    *,
    max_align_samples: int,
    correlation_threshold: float,
) -> dict[str, Any]:
    outputs = job["reference_capture_outputs"]
    source_spc = file_record(job["source_spc"]["path"])
    source_wav = file_record(job["source_render"]["path"])
    reference_spc = file_record(outputs["spc_snapshot"])
    reference_wav = file_record(outputs["pcm_wav"])

    missing = [
        label
        for label, record in (("reference_spc", reference_spc), ("reference_wav", reference_wav))
        if not record["exists"]
    ]
    errors: list[str] = []
    comparison: dict[str, Any] = {}

    if not missing:
        try:
            source_wav_path = resolve_repo_path(job["source_render"]["path"])
            reference_wav_path = resolve_repo_path(outputs["pcm_wav"])
            source_info = wav_info(source_wav_path)
            reference_info = wav_info(reference_wav_path)
            exact_wav_match = source_wav.get("sha1") == reference_wav.get("sha1")
            if exact_wav_match:
                metric = job.get("source_render", {}).get("metrics", {})
                source_features = {
                    "sample_count": metric.get("rendered_samples", source_info["total_samples"]),
                    "peak_abs_sample": metric.get("peak_abs_sample"),
                    "sum_abs_samples": None,
                    "rms_sample": metric.get("rms_sample"),
                    "nonzero_sample_count": metric.get("nonzero_sample_count"),
                    "first_nonzero_sample_index": metric.get("first_nonzero_sample_index"),
                    "last_nonzero_sample_index": metric.get("last_nonzero_sample_index"),
                }
                reference_features = dict(source_features)
                alignment = {
                    "best_offset_samples": 0,
                    "normalized_correlation": 1.0,
                    "compared_samples": source_info["total_samples"],
                    "stride": 1,
                    "search_window_samples": max_align_samples,
                    "fast_path": "byte_exact_wav_match",
                }
            else:
                source_samples = wav_samples(source_wav_path)
                reference_samples = wav_samples(reference_wav_path)
                source_features = pcm_features(source_samples)
                reference_features = pcm_features(reference_samples)
                alignment = normalized_correlation(
                    source_samples,
                    reference_samples,
                    max_align_samples=max_align_samples,
                )
            comparison["wav"] = {
                "source": source_info,
                "reference": reference_info,
                "sample_rate_match": source_info["sample_rate"] == reference_info["sample_rate"],
                "channels_match": source_info["channels"] == reference_info["channels"],
                "bits_per_sample_match": source_info["bits_per_sample"] == reference_info["bits_per_sample"],
                "total_sample_delta": reference_info["total_samples"] - source_info["total_samples"],
                "byte_exact_match": exact_wav_match,
                "source_features": source_features,
                "reference_features": reference_features,
                "alignment": alignment,
            }
        except ValueError as exc:
            errors.append(str(exc))

        source_spc_path = resolve_repo_path(job["source_spc"]["path"])
        reference_spc_path = resolve_repo_path(outputs["spc_snapshot"])
        if source_spc_path.exists() and reference_spc_path.exists():
            source_info = spc_info(source_spc_path)
            reference_info = spc_info(reference_spc_path)
            source_regions = source_info["apu_region_hashes"]
            reference_regions = reference_info["apu_region_hashes"]
            region_matches = {
                name: source_regions[name]["sha1"] == reference_regions.get(name, {}).get("sha1")
                for name in source_regions
            }
            comparison["spc"] = {
                "source": source_info,
                "reference": reference_info,
                "source_signature_ok": source_info["signature_ok"],
                "reference_signature_ok": reference_info["signature_ok"],
                "byte_exact_match": source_spc.get("sha1") == reference_spc.get("sha1"),
                "header_registers_match": source_info["registers"] == reference_info["registers"],
                "full_apu_ram_match": source_info["ram_sha1"] == reference_info["ram_sha1"],
                "dsp_register_match": source_info["dsp_register_sha1"] == reference_info["dsp_register_sha1"],
                "apu_region_matches": region_matches,
            }

    status = classify_comparison(
        errors=errors,
        missing=missing,
        spc_comparison=comparison.get("spc", {}),
        wav_comparison=comparison.get("wav", {}),
        correlation_threshold=correlation_threshold,
        max_align_samples=max_align_samples,
    )

    result = {
        "schema": "earthbound-decomp.audio-oracle-comparison-result.v1",
        "job_id": job["job_id"],
        "track_id": job["track_id"],
        "track_name": job["track_name"],
        "status": status,
        "missing_reference_outputs": missing,
        "source_spc": source_spc,
        "source_wav": source_wav,
        "reference_spc": reference_spc,
        "reference_wav": reference_wav,
        "comparison": comparison,
        "errors": errors,
    }
    result_path = resolve_repo_path(outputs["comparison_result"])
    result_path.parent.mkdir(parents=True, exist_ok=True)
    result_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return result


def collect(plan_path: Path, *, max_align_samples: int | None = None, correlation_threshold: float | None = None) -> dict[str, Any]:
    plan = load_json(plan_path)
    thresholds = plan.get("comparison_policy", {}).get("recommended_pcm_thresholds", {})
    effective_max_align_samples = (
        max_align_samples
        if max_align_samples is not None
        else int(thresholds.get("maximum_leading_silence_delta_samples", 4096))
    )
    effective_correlation_threshold = (
        correlation_threshold
        if correlation_threshold is not None
        else float(thresholds.get("minimum_normalized_correlation_after_alignment", 0.98))
    )
    results = [
        compare_job(
            job,
            max_align_samples=effective_max_align_samples,
            correlation_threshold=effective_correlation_threshold,
        )
        for job in plan.get("jobs", [])
    ]
    status_counts: dict[str, int] = {}
    for result in results:
        status = str(result["status"])
        status_counts[status] = status_counts.get(status, 0) + 1
    return {
        "schema": "earthbound-decomp.audio-oracle-comparison-summary.v1",
        "plan": str(plan_path),
        "job_scope": plan.get("job_scope"),
        "job_count": len(results),
        "status_counts": status_counts,
        "comparison_thresholds": {
            "maximum_alignment_window_samples": effective_max_align_samples,
            "minimum_normalized_correlation_after_alignment": effective_correlation_threshold,
        },
        "results": [
            {
                "job_id": result["job_id"],
                "track_id": result["track_id"],
                "track_name": result["track_name"],
                "status": result["status"],
                "missing_reference_outputs": result["missing_reference_outputs"],
                "result_path": plan_job_result_path(plan, result["job_id"]),
            }
            for result in results
        ],
    }


def plan_job_result_path(plan: dict[str, Any], job_id: str) -> str:
    for job in plan.get("jobs", []):
        if job.get("job_id") == job_id:
            return job["reference_capture_outputs"]["comparison_result"]
    return ""


def render_markdown(summary: dict[str, Any]) -> str:
    rows = [
        "| `{track_id:03d}` | `{track_name}` | `{status}` | `{missing}` | `{result}` |".format(
            track_id=result["track_id"],
            track_name=result["track_name"],
            status=result["status"],
            missing=", ".join(result["missing_reference_outputs"]),
            result=result["result_path"],
        )
        for result in summary["results"]
    ]
    return "\n".join(
        [
            "# Audio Oracle Comparison Summary",
            "",
            "Status: oracle comparison results collected.",
            "",
            f"- scope: `{summary['job_scope']}`",
            f"- jobs: `{summary['job_count']}`",
            f"- status counts: `{summary['status_counts']}`",
            "",
            "| Track | Name | Status | Missing Reference Outputs | Result |",
            "| ---: | --- | --- | --- | --- |",
            *rows,
            "",
        ]
    )


def main() -> int:
    args = parse_args()
    summary_path = Path(args.summary)
    summary = collect(
        Path(args.plan),
        max_align_samples=args.max_align_samples,
        correlation_threshold=args.correlation_threshold,
    )
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    markdown_path = summary_path.with_suffix(".md")
    markdown_path.write_text(render_markdown(summary), encoding="utf-8")
    print(f"Collected audio oracle comparison results: {summary['status_counts']} -> {summary_path}")
    print(f"Wrote {markdown_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
