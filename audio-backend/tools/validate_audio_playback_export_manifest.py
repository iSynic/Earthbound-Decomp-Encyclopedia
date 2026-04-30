#!/usr/bin/env python3
"""Validate a local audio playback/export manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MANIFEST = (
    ROOT
    / "build"
    / "audio"
    / "c0ab06-change-music-fusion-render-jobs-all"
    / "playback-export-manifest.json"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate an audio playback/export manifest.")
    parser.add_argument("manifest", nargs="?", default=str(DEFAULT_MANIFEST))
    parser.add_argument("--allow-nonaudible", action="store_true", help="Do not fail on non-audible tracks.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sha1_file(path: Path) -> str:
    digest = hashlib.sha1()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_little_u16(data: bytes, offset: int) -> int:
    return int.from_bytes(data[offset : offset + 2], "little")


def read_little_u32(data: bytes, offset: int) -> int:
    return int.from_bytes(data[offset : offset + 4], "little")


def read_wav_info(path: Path) -> dict[str, int | str]:
    data = path.read_bytes()
    if len(data) < 44:
        raise ValueError("WAV is shorter than the canonical PCM header")
    if data[0:4] != b"RIFF" or data[8:12] != b"WAVE":
        raise ValueError("missing RIFF/WAVE header")
    if data[12:16] != b"fmt ":
        raise ValueError("missing fmt chunk at canonical offset")
    fmt_size = read_little_u32(data, 16)
    if fmt_size < 16:
        raise ValueError("fmt chunk is too short")
    data_tag_offset = 20 + fmt_size
    if len(data) < data_tag_offset + 8 or data[data_tag_offset : data_tag_offset + 4] != b"data":
        raise ValueError("missing data chunk at canonical offset")
    return {
        "audio_format": read_little_u16(data, 20),
        "channels": read_little_u16(data, 22),
        "sample_rate": read_little_u32(data, 24),
        "byte_rate": read_little_u32(data, 28),
        "block_align": read_little_u16(data, 32),
        "bits_per_sample": read_little_u16(data, 34),
        "data_bytes": read_little_u32(data, data_tag_offset + 4),
        "file_bytes": len(data),
    }


def validate_output(
    track_id: str,
    label: str,
    output: dict[str, Any] | None,
    *,
    metrics: dict[str, Any] | None = None,
) -> list[str]:
    errors: list[str] = []
    if not output:
        return [f"{track_id}: missing {label} output record"]
    path = Path(str(output.get("path", "")))
    if not path.exists():
        return [f"{track_id}: {label} path missing: {path}"]
    data_size = path.stat().st_size
    if int(output.get("bytes", -1)) != data_size:
        errors.append(f"{track_id}: {label} byte count mismatch {output.get('bytes')} != {data_size}")
    actual_sha1 = sha1_file(path)
    if output.get("sha1") != actual_sha1:
        errors.append(f"{track_id}: {label} SHA-1 mismatch {output.get('sha1')} != {actual_sha1}")
    if label == "rendered_wav":
        try:
            wav = read_wav_info(path)
        except ValueError as exc:
            errors.append(f"{track_id}: rendered_wav malformed: {exc}")
        else:
            if wav["audio_format"] != 1:
                errors.append(f"{track_id}: rendered_wav must be PCM format")
            if wav["channels"] != 2:
                errors.append(f"{track_id}: rendered_wav channels {wav['channels']} != 2")
            if wav["sample_rate"] != 32000:
                errors.append(f"{track_id}: rendered_wav sample_rate {wav['sample_rate']} != 32000")
            if wav["bits_per_sample"] != 16:
                errors.append(f"{track_id}: rendered_wav bits_per_sample {wav['bits_per_sample']} != 16")
            expected_byte_rate = int(wav["sample_rate"]) * int(wav["channels"]) * int(wav["bits_per_sample"]) // 8
            if wav["byte_rate"] != expected_byte_rate:
                errors.append(f"{track_id}: rendered_wav byte_rate {wav['byte_rate']} != {expected_byte_rate}")
            expected_block_align = int(wav["channels"]) * int(wav["bits_per_sample"]) // 8
            if wav["block_align"] != expected_block_align:
                errors.append(f"{track_id}: rendered_wav block_align {wav['block_align']} != {expected_block_align}")
            if int(wav["data_bytes"]) + 44 != int(wav["file_bytes"]):
                errors.append(f"{track_id}: rendered_wav data chunk size does not match file size")
            if metrics and metrics.get("rendered_samples") is not None:
                expected_data_samples = int(metrics["rendered_samples"])
                actual_data_samples = int(wav["data_bytes"]) // 2
                if actual_data_samples != expected_data_samples:
                    errors.append(
                        f"{track_id}: rendered_wav sample count {actual_data_samples} "
                        f"!= metrics rendered_samples {expected_data_samples}"
                    )
    if label == "source_spc":
        with path.open("rb") as stream:
            header = stream.read(27)
        if not header.startswith(b"SNES-SPC700 Sound File Data"):
            errors.append(f"{track_id}: source_spc missing SNES-SPC700 signature")
    return errors


def validate(manifest: dict[str, Any], *, allow_nonaudible: bool) -> list[str]:
    errors: list[str] = []
    if manifest.get("schema") != "earthbound-decomp.audio-playback-export-manifest.v1":
        errors.append(f"unexpected schema: {manifest.get('schema')}")
    tracks = manifest.get("tracks", [])
    if int(manifest.get("track_count", -1)) != len(tracks):
        errors.append(f"track_count {manifest.get('track_count')} does not match {len(tracks)} tracks")
    skipped_records = manifest.get("skipped_records", [])
    if int(manifest.get("skipped_count", 0)) != len(skipped_records):
        errors.append("skipped_count does not match skipped_records")
    expected_table_entries = len(tracks) + len(skipped_records)
    if int(manifest.get("table_entry_count", expected_table_entries)) != expected_table_entries:
        errors.append("table_entry_count does not match tracks plus skipped_records")
    if not manifest.get("source_policy", {}).get("contains_rom_derived_payloads"):
        errors.append("source_policy must mark playback/export outputs as ROM-derived local payloads")

    seen: set[int] = set()
    passed = 0
    for track in tracks:
        track_id = int(track.get("track_id", -1))
        label = f"track {track_id:03d}"
        if track_id in seen:
            errors.append(f"duplicate track_id {track_id}")
        seen.add(track_id)
        if track.get("status") == "ok" and track.get("valid") is True and track.get("classification") == "audible":
            passed += 1
        else:
            errors.append(
                f"{label}: quality gate failed "
                f"status={track.get('status')} valid={track.get('valid')} classification={track.get('classification')}"
            )
        if not allow_nonaudible and track.get("classification") != "audible":
            errors.append(f"{label}: expected audible classification")
        errors.extend(validate_output(label, "source_spc", track.get("source_spc")))
        errors.extend(validate_output(label, "rendered_wav", track.get("rendered_wav"), metrics=track.get("metrics")))
        errors.extend(validate_output(label, "render_hash", track.get("render_hash")))

    gate = manifest.get("quality_gate", {})
    if int(gate.get("passed_count", -1)) != passed:
        errors.append(f"quality_gate passed_count {gate.get('passed_count')} does not match {passed}")
    if int(gate.get("failed_count", -1)) != len(tracks) - passed:
        errors.append(f"quality_gate failed_count {gate.get('failed_count')} does not match {len(tracks) - passed}")
    return errors


def main() -> int:
    args = parse_args()
    manifest_path = Path(args.manifest)
    manifest = load_json(manifest_path)
    errors = validate(manifest, allow_nonaudible=args.allow_nonaudible)
    if errors:
        print("Audio playback/export manifest validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "Audio playback/export manifest validation OK: "
        f"{manifest['track_count']} tracks, classifications {manifest['classification_counts']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
