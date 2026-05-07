# Bank DB First Pass

## Main result

Bank `DB` is an asset-only map/audio bank. It contains six compressed map
arrangement payloads followed by an audio pack and a small tail slack region.

Primary artifacts:

- `notes/bank-db-asset-data-map.md`
- `build/asset-bank-db.json`

The generated map accounts for:

- binary assets: `7`
- binary asset bytes: `65380`
- asset mix: `6` compressed arrangements and `1` audio pack
- table includes: `0`
- table bytes: `0`
- coverage gap bytes: `156`
- missing payload metadata: `0`

## Bank layout

The high-level DB layout is:

- `DB:0000..DB:26C0`: `MAP_DATA_TILE_ARRANGEMENT_8`, `9921` bytes.
- `DB:26C1..DB:617E`: `MAP_DATA_TILE_ARRANGEMENT_9`, `15038` bytes.
- `DB:617F..DB:7C21`: `MAP_DATA_TILE_ARRANGEMENT_16`, `6819` bytes.
- `DB:7C22..DB:9217`: `MAP_DATA_TILE_ARRANGEMENT_17`, `5622` bytes.
- `DB:9218..DB:C6CB`: `MAP_DATA_TILE_ARRANGEMENT_10`, `13492` bytes.
- `DB:C6CC..DB:F2EA`: `MAP_DATA_TILE_ARRANGEMENT_11`, `11295` bytes.
- `DB:F2EB..DB:FF63`: `AUDIO_PACK_65`, `3193` bytes.
- `DB:FF64..DB:FFFF`: tail slack, `156` bytes.

## Current DB confidence boundary

High confidence:

- DB is data/assets, not executable code.
- Every non-slack byte belongs to a named compressed arrangement or audio pack.
- The source order intentionally places arrangements `16` and `17` between
  arrangements `9` and `10`.

Still intentionally out of scope:

- Decompressing or rendering arrangements `8`, `9`, `16`, `17`, `10`, and `11`.
- Explaining why the source order differs from numeric arrangement order.
- Audio-pack internals.

## Recommended next move

Proceed to `DC`. Its bank config continues the arrangement stream and introduces
per-sector music data before two audio packs, so it should be another useful
mixed map/audio pass.
