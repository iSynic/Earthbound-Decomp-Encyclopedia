#!/usr/bin/env python3
"""Build ignored CPU routine byte fixtures used by audio mailbox smoke tests."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import rom_tools


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUT = ROOT / "build" / "audio" / "cpu-routine-fixtures"

FIXTURES = [
    {
        "id": "c0_ab06_load_spc700_data_stream",
        "label": "C0:AB06 LoadSpc700DataStream",
        "cpu_address": "0xC0AB06",
        "bank": 0xC0,
        "address": 0xAB06,
        "length": 162,
        "expected_sha1": "e0cfb01348233939a0c4d98c42a0d8350f0ce6d9",
        "source_path": "src/c0/c0_ab06_load_spc700_data_stream.asm",
        "output_stem": "c0-ab06-load-spc700-data-stream",
    },
    {
        "id": "c0_abbd_send_apu_port0_command_byte",
        "label": "C0:ABBD SendApuPort0CommandByte",
        "cpu_address": "0xC0ABBD",
        "bank": 0xC0,
        "address": 0xABBD,
        "length": 9,
        "expected_hex": "e2208f402100c2306b",
        "source_path": "src/c0/c0_abbd_send_apu_port0_command_byte.asm",
        "output_stem": "c0-abbd-send-apu-port0-command-byte",
    },
    {
        "id": "c0_abc6_stop_music_and_latch_no_track",
        "label": "C0:ABC6 StopMusicAndLatchNoTrack",
        "cpu_address": "0xC0ABC6",
        "bank": 0xC0,
        "address": 0xABC6,
        "length": 26,
        "expected_hex": "e220a9008f402100c2302220acc0c90000d0f7a9ffff8d3bb56b",
        "source_path": "src/c0/c0_abc6_stop_music_and_latch_no_track.asm",
        "output_stem": "c0-abc6-stop-music-and-latch-no-track",
    },
    {
        "id": "c4_fd0e_change_music_tail_send_track_command",
        "label": "C4:FD0E ChangeMusic tail send track command",
        "cpu_address": "0xC4FD0E",
        "bank": 0xC4,
        "address": 0xFD0E,
        "length": 10,
        "expected_hex": "a410981a22bdabc02b6b",
        "source_path": "src/c4/music_change_pack_loader.asm",
        "output_stem": "c4-fd0e-change-music-tail-send-track-command",
    },
    {
        "id": "c4_fbbd_change_music",
        "label": "C4:FBBD ChangeMusic",
        "cpu_address": "0xC4FBBD",
        "bank": 0xC4,
        "address": 0xFBBD,
        "length": 347,
        "expected_sha1": "e7a0911bb630b17ce709cc227c191eda12037332",
        "source_path": "src/c4/music_change_pack_loader.asm",
        "output_stem": "c4-fbbd-change-music",
    },
    {
        "id": "c4_fb42_change_music_helpers",
        "label": "C4:FB42 ChangeMusic helper routines",
        "cpu_address": "0xC4FB42",
        "bank": 0xC4,
        "address": 0xFB42,
        "length": 123,
        "expected_sha1": "d9fb04b3c9745e7282d058cdbd57b4972c0fa7d4",
        "source_path": "src/c4/music_change_pack_loader.asm",
        "output_stem": "c4-fb42-change-music-helpers",
    },
    {
        "id": "c4_f70a_music_dataset_table",
        "label": "C4:F70A MusicDatasetTable",
        "cpu_address": "0xC4F70A",
        "bank": 0xC4,
        "address": 0xF70A,
        "length": 573,
        "expected_sha1": "b449c58897c4f99674868a48b61b5eecc9ba69e5",
        "source_path": "src/c4/music_change_pack_loader.asm",
        "output_stem": "c4-f70a-music-dataset-table",
    },
    {
        "id": "c4_f947_music_pack_pointer_table",
        "label": "C4:F947 MusicPackPointerTable",
        "cpu_address": "0xC4F947",
        "bank": 0xC4,
        "address": 0xF947,
        "length": 507,
        "expected_sha1": "f18980670044ba36aeedc9e2808c53426b080574",
        "source_path": "refs/ebsrc-main/ebsrc-main/src/audio/change_music.asm",
        "output_stem": "c4-f947-music-pack-pointer-table",
    },
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build ignored audio CPU routine byte fixtures from a user ROM.")
    parser.add_argument("--rom", help="Optional explicit EarthBound US ROM path.")
    parser.add_argument("--out", default=str(DEFAULT_OUT), help="Ignored output directory.")
    return parser.parse_args()


def fixture_record(fixture: dict[str, Any], rom: bytes, out_dir: Path) -> dict[str, Any]:
    file_offset = rom_tools.hirom_to_file_offset(fixture["bank"], fixture["address"], len(rom))
    if file_offset is None:
        raise ValueError(f"{fixture['id']} does not map to a ROM file offset")

    data = rom[file_offset:file_offset + fixture["length"]]
    expected_hex = fixture.get("expected_hex")
    expected_sha1 = fixture.get("expected_sha1")
    matches = True
    if expected_hex:
        expected = bytes.fromhex(expected_hex)
        matches = data == expected
    if expected_sha1:
        matches = hashlib.sha1(data).hexdigest() == expected_sha1
    if not matches:
        raise ValueError(
            f"{fixture['id']} bytes do not match expected source contract: "
            f"got hex {data.hex()} sha1 {hashlib.sha1(data).hexdigest()}, "
            f"expected hex {expected_hex or '<not specified>'} sha1 {expected_sha1 or '<not specified>'}"
        )

    bin_path = out_dir / f"{fixture['output_stem']}.bin"
    bin_path.write_bytes(data)
    return {
        "id": fixture["id"],
        "label": fixture["label"],
        "cpu_address": fixture["cpu_address"],
        "file_offset": f"0x{file_offset:06X}",
        "bytes": len(data),
        "sha1": hashlib.sha1(data).hexdigest(),
        "hex": data.hex(),
        "expected_hex": expected_hex,
        "expected_sha1": expected_sha1,
        "matches_expected": matches,
        "source_path": fixture["source_path"],
        "path": str(bin_path),
    }


def main() -> int:
    args = parse_args()
    rom_path = rom_tools.find_rom(args.rom)
    rom = rom_tools.load_rom(rom_path)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    records = [fixture_record(fixture, rom, out_dir) for fixture in FIXTURES]
    manifest = {
        "schema": "earthbound-decomp.audio-cpu-routine-fixtures.v1",
        "source_policy": {
            "requires_user_supplied_rom": True,
            "generated_outputs_are_ignored": True,
            "contains_rom_derived_bytes": True,
        },
        "rom": {
            "path": str(rom_path),
            "sha1": hashlib.sha1(rom).hexdigest(),
            "bytes": len(rom),
        },
        "fixture_count": len(records),
        "records": records,
    }
    manifest_path = out_dir / "audio-cpu-routine-fixtures.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Built audio CPU routine fixtures: {len(records)}")
    print(f"Wrote {manifest_path}")
    for record in records:
        print(f"Wrote {record['path']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
