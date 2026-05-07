# Bank D9 First Pass

## Main result

Bank `D9` is an asset-only map/audio bank. It continues the compressed map
arrangement stream, includes one compressed map tileset graphics payload, and
ends with an audio pack plus a small tail slack region.

Primary artifacts:

- `notes/bank-d9-asset-data-map.md`
- `build/asset-bank-d9.json`

The generated map accounts for:

- binary assets: `6`
- binary asset bytes: `65505`
- asset mix: `4` compressed arrangements, `1` compressed graphics payload, and
  `1` audio pack
- table includes: `0`
- table bytes: `0`
- coverage gap bytes: `31`
- missing payload metadata: `0`

## Bank layout

The high-level D9 layout is:

- `D9:0000..D9:34E8`: `MAP_DATA_TILE_ARRANGEMENT_1`, `13545` bytes.
- `D9:34E9..D9:68AA`: `MAP_DATA_TILE_ARRANGEMENT_2`, `13250` bytes.
- `D9:68AB..D9:8DD4`: `MAP_DATA_TILE_ARRANGEMENT_3`, `9514` bytes.
- `D9:8DD5..D9:CE51`: `MAP_DATA_TILE_ARRANGEMENT_4`, `16509` bytes.
- `D9:CE52..D9:FC17`: `MAP_DATA_TILE_SET_GRAPHICS_13`, `11718` bytes.
- `D9:FC18..D9:FFE0`: `AUDIO_PACK_45`, `969` bytes.
- `D9:FFE1..D9:FFFF`: tail slack, `31` bytes.

## Current D9 confidence boundary

High confidence:

- D9 is data/assets, not executable code.
- Every non-slack byte in the bank belongs to a named payload.
- The arrangement, graphics, and audio spans are exact for the US retail build.

Still intentionally out of scope:

- Decompressing or rendering arrangements `1` through `4`.
- Decompressing or rendering `MAP_DATA_TILE_SET_GRAPHICS_13`.
- Audio-pack internals.

## Recommended next move

Proceed to `DA`. Its bank config starts with arrangements `5` through `7`, then
switches into many map palette payloads and an unknown palette pointer table, so
it should help connect arrangement graphics to palette metadata.
