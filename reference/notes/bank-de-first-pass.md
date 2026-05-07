# Bank DE First Pass

## Main result

Bank `DE` is an asset-only map/audio bank. It contains compressed map tileset
graphics, compressed map animation graphics, and one audio pack.

Primary artifacts:

- `notes/bank-de-asset-data-map.md`
- `build/asset-bank-de.json`

The generated map accounts for:

- binary assets: `12`
- binary asset bytes: `65492`
- asset mix: `11` compressed graphics payloads and `1` audio pack
- table includes: `0`
- table bytes: `0`
- coverage gap bytes: `44`
- missing payload metadata: `0`

## Bank layout

The high-level DE layout is:

- `DE:0000..DE:32C8`: `MAP_DATA_TILE_SET_GRAPHICS_6`, `13001` bytes.
- `DE:32C9..DE:543E`: `MAP_DATA_TILE_SET_GRAPHICS_7`, `8566` bytes.
- `DE:543F..DE:747D`: `MAP_DATA_TILE_SET_GRAPHICS_8`, `8255` bytes.
- `DE:747E..DE:A100`: `MAP_DATA_TILE_SET_GRAPHICS_2`, `11395` bytes.
- `DE:A101..DE:CE39`: `MAP_DATA_TILE_SET_GRAPHICS_10`, `11577` bytes.
- `DE:CE3A..DE:F0E6`: `MAP_DATA_TILE_SET_GRAPHICS_11`, `8877` bytes.
- `DE:F0E7..DE:FCDC`: `MAP_DATA_TILE_ANIMATION_GFX_15` through
  `MAP_DATA_TILE_ANIMATION_GFX_19`, `3062` bytes total.
- `DE:FCDD..DE:FFD3`: `AUDIO_PACK_143`, `759` bytes.
- `DE:FFD4..DE:FFFF`: tail slack, `44` bytes.

## Current DE confidence boundary

High confidence:

- DE is data/assets, not executable code.
- Every non-slack byte belongs to a named compressed graphics payload or audio
  pack.
- Animation graphics `15` through `19` are present after tileset graphics `11`.

Still intentionally out of scope:

- Decompressing or rendering tileset graphics or animation graphics.
- Mapping animation graphics to palette-animation metadata.
- Audio-pack internals.

## Recommended next move

Proceed to `DF`. It continues tileset/animation graphics and introduces the
palette-animation table family.
