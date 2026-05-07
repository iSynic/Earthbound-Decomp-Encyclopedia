# Bank DD First Pass

## Main result

Bank `DD` is an asset-only map/audio bank. It contains six compressed map
tileset graphics payloads followed by one audio pack and an 8-byte tail slack.

Primary artifacts:

- `notes/bank-dd-asset-data-map.md`
- `build/asset-bank-dd.json`

The generated map accounts for:

- binary assets: `7`
- binary asset bytes: `65528`
- asset mix: `6` compressed graphics payloads and `1` audio pack
- table includes: `0`
- table bytes: `0`
- coverage gap bytes: `8`
- missing payload metadata: `0`

## Bank layout

The high-level DD layout is:

- `DD:0000..DD:3293`: `MAP_DATA_TILE_SET_GRAPHICS_0`, `12948` bytes.
- `DD:3294..DD:5F16`: `MAP_DATA_TILE_SET_GRAPHICS_1`, `11395` bytes.
- `DD:5F17..DD:89A1`: `MAP_DATA_TILE_SET_GRAPHICS_9`, `10891` bytes.
- `DD:89A2..DD:B7D0`: `MAP_DATA_TILE_SET_GRAPHICS_3`, `11823` bytes.
- `DD:B7D1..DD:DF3A`: `MAP_DATA_TILE_SET_GRAPHICS_4`, `10090` bytes.
- `DD:DF3B..DD:FECD`: `MAP_DATA_TILE_SET_GRAPHICS_5`, `8083` bytes.
- `DD:FECE..DD:FFF7`: `AUDIO_PACK_75`, `298` bytes.
- `DD:FFF8..DD:FFFF`: tail slack, `8` bytes.

## Current DD confidence boundary

High confidence:

- DD is data/assets, not executable code.
- Every non-slack byte belongs to a named compressed tileset graphics payload or
  audio pack.
- The source order intentionally places tileset graphics `9` between graphics
  `1` and `3`.

Still intentionally out of scope:

- Decompressing or rendering the map tileset graphics.
- Explaining source-order versus numeric tileset order.
- Audio-pack internals.

## Recommended next move

Proceed to `DE`. It continues the compressed tileset graphics run and introduces
map animation graphics.
