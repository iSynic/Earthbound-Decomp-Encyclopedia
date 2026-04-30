#!/usr/bin/env python3
"""Build the EarthBound audio-pack contract manifest and companion note."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import audio_pack_contracts


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_JSON = ROOT / "manifests" / "audio-pack-contracts.json"
DEFAULT_MARKDOWN = ROOT / "notes" / "audio-pack-format-and-renderer-frontier.md"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build audio pack stream, track, and renderer-frontier contracts."
    )
    parser.add_argument("--rom", help="Optional explicit EarthBound US ROM path.")
    parser.add_argument("--json", default=str(DEFAULT_JSON), help="JSON output path.")
    parser.add_argument("--markdown", default=str(DEFAULT_MARKDOWN), help="Markdown output path.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    contract = audio_pack_contracts.build_audio_contract(Path(args.rom) if args.rom else None)

    json_path = Path(args.json)
    markdown_path = Path(args.markdown)
    audio_pack_contracts.write_json(contract, json_path)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.write_text(audio_pack_contracts.render_markdown(contract), encoding="utf-8")

    summary = contract["summary"]
    print(
        "Built audio contracts: "
        f"{summary['pack_count']} packs, {summary['track_count']} tracks, "
        f"{summary['stream_status_counts']} stream statuses"
    )
    print(f"Wrote {json_path}")
    print(f"Wrote {markdown_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
