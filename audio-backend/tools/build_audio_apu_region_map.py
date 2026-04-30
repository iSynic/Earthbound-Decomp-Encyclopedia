#!/usr/bin/env python3
"""Build an APU RAM destination-region map from the audio-pack contract."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONTRACT = ROOT / "manifests" / "audio-pack-contracts.json"
DEFAULT_JSON = ROOT / "manifests" / "audio-apu-region-map.json"
DEFAULT_MARKDOWN = ROOT / "notes" / "audio-apu-region-map.md"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the audio APU RAM destination region map.")
    parser.add_argument("--contract", default=str(DEFAULT_CONTRACT), help="Audio contract JSON path.")
    parser.add_argument("--json", default=str(DEFAULT_JSON), help="JSON output path.")
    parser.add_argument("--markdown", default=str(DEFAULT_MARKDOWN), help="Markdown output path.")
    return parser.parse_args()


def parse_hex(text: str) -> int:
    return int(text, 16)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def collect_writes(contract: dict[str, Any]) -> list[dict[str, Any]]:
    writes: list[dict[str, Any]] = []
    for pack in contract["audio_packs"]:
        pack_id = int(pack["pack_id"])
        for block in pack["stream"]["blocks"]:
            if block.get("terminal"):
                continue
            destination = parse_hex(block["destination"])
            count = int(block["count"])
            writes.append(
                {
                    "pack_id": pack_id,
                    "pack_kind": pack["kind"],
                    "pack_range": pack["range"],
                    "block_index": int(block["index"]),
                    "destination": destination,
                    "end": destination + count,
                    "bytes": count,
                    "role_guess": block["role_guess"],
                    "payload_sha1": block["sha1"],
                }
            )
    return writes


def summarize_by_role(writes: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for write in writes:
        grouped[write["role_guess"]].append(write)

    summaries: list[dict[str, Any]] = []
    for role, role_writes in sorted(grouped.items()):
        exact_destinations = Counter(write["destination"] for write in role_writes)
        largest = max(role_writes, key=lambda write: write["bytes"])
        summaries.append(
            {
                "role_guess": role,
                "write_count": len(role_writes),
                "total_payload_bytes": sum(write["bytes"] for write in role_writes),
                "lowest_destination": f"0x{min(write['destination'] for write in role_writes):04X}",
                "highest_end": f"0x{max(write['end'] for write in role_writes):04X}",
                "unique_destination_count": len(exact_destinations),
                "common_destinations": [
                    {
                        "destination": f"0x{destination:04X}",
                        "write_count": count,
                    }
                    for destination, count in exact_destinations.most_common(8)
                ],
                "largest_write": {
                    "pack_id": largest["pack_id"],
                    "block_index": largest["block_index"],
                    "destination": f"0x{largest['destination']:04X}",
                    "end": f"0x{largest['end']:04X}",
                    "bytes": largest["bytes"],
                },
            }
        )
    return summaries


def find_overlapping_write_shapes(writes: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_shape: dict[tuple[int, int, str], list[dict[str, Any]]] = defaultdict(list)
    for write in writes:
        by_shape[(write["destination"], write["end"], write["role_guess"])].append(write)

    repeated_shapes: list[dict[str, Any]] = []
    for (destination, end, role), shape_writes in sorted(by_shape.items()):
        if len(shape_writes) < 2:
            continue
        repeated_shapes.append(
            {
                "destination": f"0x{destination:04X}",
                "end": f"0x{end:04X}",
                "role_guess": role,
                "bytes": end - destination,
                "write_count": len(shape_writes),
                "sample_pack_ids": [write["pack_id"] for write in shape_writes[:12]],
            }
        )
    repeated_shapes.sort(key=lambda item: (-int(item["write_count"]), item["destination"]))
    return repeated_shapes


def build_region_map(contract: dict[str, Any]) -> dict[str, Any]:
    writes = collect_writes(contract)
    role_summaries = summarize_by_role(writes)
    repeated_shapes = find_overlapping_write_shapes(writes)
    role_counts = Counter(write["role_guess"] for write in writes)
    return {
        "schema": "earthbound-decomp.audio-apu-region-map.v1",
        "source": "manifests/audio-pack-contracts.json",
        "summary": {
            "pack_count": len(contract["audio_packs"]),
            "payload_write_count": len(writes),
            "payload_byte_count": sum(write["bytes"] for write in writes),
            "destination_role_counts": dict(role_counts),
            "lowest_destination": f"0x{min(write['destination'] for write in writes):04X}",
            "highest_end": f"0x{max(write['end'] for write in writes):04X}",
        },
        "regions_by_role": role_summaries,
        "repeated_write_shapes": repeated_shapes[:80],
    }


def render_markdown(region_map: dict[str, Any]) -> str:
    summary = region_map["summary"]
    region_rows = [
        "| `{role}` | {writes} | {bytes} | `{low}` | `{high}` | {unique} | `{largest}` |".format(
            role=region["role_guess"],
            writes=region["write_count"],
            bytes=region["total_payload_bytes"],
            low=region["lowest_destination"],
            high=region["highest_end"],
            unique=region["unique_destination_count"],
            largest=(
                f"AUDIO_PACK_{region['largest_write']['pack_id']} "
                f"{region['largest_write']['destination']}..{region['largest_write']['end']}"
            ),
        )
        for region in region_map["regions_by_role"]
    ]
    shape_rows = [
        "| `{destination}` | `{end}` | `{role}` | {bytes} | {count} | `{packs}` |".format(
            destination=shape["destination"],
            end=shape["end"],
            role=shape["role_guess"],
            bytes=shape["bytes"],
            count=shape["write_count"],
            packs=", ".join(str(pack_id) for pack_id in shape["sample_pack_ids"]),
        )
        for shape in region_map["repeated_write_shapes"][:24]
    ]
    return "\n".join(
        [
            "# Audio APU Region Map",
            "",
            "Status: derived from the audio-pack contract; no ROM-derived payload bytes are included.",
            "",
            "This map summarizes where EarthBound audio packs write inside SPC/APU RAM. It is meant to guide driver, sample, and sequence-state work before a renderer backend starts consuming the generated RAM seeds.",
            "",
            "## Summary",
            "",
            f"- audio packs: `{summary['pack_count']}`",
            f"- payload writes: `{summary['payload_write_count']}`",
            f"- payload bytes across all pack streams: `{summary['payload_byte_count']}`",
            f"- destination span: `{summary['lowest_destination']}..{summary['highest_end']}`",
            f"- destination role counts: `{summary['destination_role_counts']}`",
            "",
            "## Regions By Role",
            "",
            "| Role guess | Writes | Payload bytes | Lowest destination | Highest end | Unique destinations | Largest write |",
            "| --- | ---: | ---: | --- | --- | ---: | --- |",
            *region_rows,
            "",
            "## Common Repeated Write Shapes",
            "",
            "| Destination | End | Role guess | Bytes | Writes | Sample pack ids |",
            "| --- | --- | --- | ---: | ---: | --- |",
            *shape_rows,
            "",
        ]
    )


def write_json(data: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    contract = load_json(Path(args.contract))
    region_map = build_region_map(contract)
    json_path = Path(args.json)
    markdown_path = Path(args.markdown)
    write_json(region_map, json_path)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.write_text(render_markdown(region_map), encoding="utf-8")
    summary = region_map["summary"]
    print(
        "Built audio APU region map: "
        f"{summary['payload_write_count']} writes, "
        f"{summary['payload_byte_count']} payload bytes"
    )
    print(f"Wrote {json_path}")
    print(f"Wrote {markdown_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
