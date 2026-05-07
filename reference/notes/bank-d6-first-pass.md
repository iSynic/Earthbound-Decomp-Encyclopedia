# Bank D6 First Pass

## Main result

Bank `D6` is a pure map tile data bank. It contains six binary tile-table chunks
and no code, no inline tables, and no unclaimed bytes.

Primary artifacts:

- `notes/bank-d6-asset-data-map.md`
- `notes/bank-d6-source-scaffold-handoff.md`
- `build/asset-bank-d6.json`
- `build/d6-build-candidate-ranges.json`
- `build/d6-byte-equivalence-validation.json`

The generated map accounts for:

- binary assets: `6`
- binary asset bytes: `65536`
- asset mix: `6` binary map tile chunks (`bin`)
- table includes: `0`
- table bytes: `0`
- coverage gap bytes: `0`
- missing payload metadata: `0`
- source scaffold protected bytes: `65536 / 65536`
- byte-equivalence scaffold validation: `durable-scaffold`, `6` modules,
  `0` non-OK modules, `0` byte mismatches

## Bank layout

The bank is a source-order run of `maps/tiles/chunk_*.bin` payloads:

- `MAP_DATA_TILE_TABLE_CHUNK_1`: `D6:0000..D6:27FF`, `10240` bytes.
- `MAP_DATA_TILE_TABLE_CHUNK_2`: `D6:2800..D6:4FFF`, `10240` bytes.
- `MAP_DATA_TILE_TABLE_CHUNK_3`: `D6:5000..D6:7FFF`, `12288` bytes.
- `MAP_DATA_TILE_TABLE_CHUNK_4`: `D6:8000..D6:A7FF`, `10240` bytes.
- `MAP_DATA_TILE_TABLE_CHUNK_5`: `D6:A800..D6:CFFF`, `10240` bytes.
- `MAP_DATA_TILE_TABLE_CHUNK_6`: `D6:D000..D6:FFFF`, `12288` bytes.

## Current D6 confidence boundary

High confidence:

- D6 is data/assets, not executable code.
- Every byte from `D6:0000` through `D6:FFFF` belongs to a named map tile
  chunk.
- The US retail locale-specific tile chunk is resolved through `LOCALEBINARY`.
- `src/d6/bank_d6_helpers_asar.asm` protects the full bank through the reusable
  source-bank scaffold pipeline.

Still intentionally out of scope:

- Tile decoding/rendering semantics.
- Tileset palette assignment.
- Map sector attributes and tile arrangement metadata, which begin in later
  bank configs.

## Recommended next move

D6 is now closed for byte-preserving scaffold purposes. The remaining work is
optional tile rendering/decompression fixtures and cross-bank linkage to later
arrangement/palette metadata.
