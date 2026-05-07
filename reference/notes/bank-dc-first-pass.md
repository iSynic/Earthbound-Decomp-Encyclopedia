# Bank DC First Pass

## Main result

Bank `DC` is a mixed map/audio data bank. It contains six compressed map
arrangements, one compressed tileset graphics payload, an inferred per-sector
music table, and two audio packs.

Primary artifacts:

- `notes/bank-dc-asset-data-map.md`
- `notes/cf-event-music-context-contracts.md`
- `build/asset-bank-dc.json`

The generated map accounts for:

- binary assets: `9`
- binary asset bytes: `62866`
- asset mix: `6` compressed arrangements, `1` compressed graphics payload, and
  `2` audio packs
- inferred generated table bytes: `2560`
- coverage gap bytes: `110`
- missing payload metadata: `0`

## Bank layout

The high-level DC layout is:

- `DC:0000..DC:1FC9`: `MAP_DATA_TILE_ARRANGEMENT_12`, `8138` bytes.
- `DC:1FCA..DC:593B`: `MAP_DATA_TILE_ARRANGEMENT_13`, `14706` bytes.
- `DC:593C..DC:687A`: `MAP_DATA_TILE_ARRANGEMENT_14`, `3903` bytes.
- `DC:687B..DC:72BF`: `MAP_DATA_TILE_ARRANGEMENT_15`, `2629` bytes.
- `DC:72C0..DC:8E49`: `MAP_DATA_TILE_ARRANGEMENT_18`, `7050` bytes.
- `DC:8E4A..DC:B022`: `MAP_DATA_TILE_ARRANGEMENT_19`, `8665` bytes.
- `DC:B023..DC:D636`: `MAP_DATA_TILE_SET_GRAPHICS_14`, `9748` bytes.
- `DC:D637..DC:E036`: `data/map/per-sector_music.asm`, inferred as
  `2560` bytes.
- `DC:E037..DC:F8BE`: `AUDIO_PACK_156`, `6280` bytes.
- `DC:F8BF..DC:FF91`: `AUDIO_PACK_79`, `1747` bytes.
- `DC:FF92..DC:FFFF`: tail slack, `110` bytes.

## Per-Sector Music

The checked-in source tree does not contain
`data/map/per-sector_music.asm`, but the next known binary asset starts at
`DC:E037`. The manifest therefore safely infers the per-sector music table as
`DC:D637..DC:E036`.

The consumer-backed subshape now has a narrow contract:

- `C0:68F4` computes `sector_index = sector_y * 32 + sector_x`, reads the byte
  at `DC:D637 + sector_index`, and uses that value as a selector into the CF
  event-music context pointer table at `CF:58EF`.
- The first 1280 bytes are therefore a 32x40 current-position
  `event_music_context_selector` plane. They reference selectors 1..164, use
  84 unique selectors, never reference selector 0, and match map-sector `Music`
  for all 1280 checked sector rows.
- The second 1280 bytes remain byte-accounted and distribution-summarized but
  intentionally unnamed here; this pass did not find a cited C0/EF consumer for
  that plane. The contract now carries a numeric-preserve source-emission row,
  104 full value counts, and confirms the second plane has no zero rows.

## Current DC confidence boundary

High confidence:

- DC is data/assets, not executable code.
- Arrangement, graphics, inferred per-sector music, and audio spans are exact
  for the US retail build.
- The first per-sector music byte plane is tied to the CF event-music context
  contract, C0/EF consumers, and the map-sector `Music` inventory.
- `notes/cf-event-music-context-contracts.md` now carries source-emission rows
  for the CF pointer table, CF variable-list context table, typed DC selector
  plane, and numeric-preserve DC second plane.
- Only `110` bytes at the end of the bank are unclaimed slack.

Still intentionally out of scope:

- The second per-sector music byte plane and human names for map_music option
  lists. The central manifest still carries a separate word-level
  per-sector-music options contract; the CF/DC event-music context contract
  narrows only the C0/EF selector-plane path.
- Decompressing or rendering arrangements/tileset graphics.
- Audio-pack internals.

## Recommended next move

Keep the CF/DC event-music selector contract regression-tested while source
emission work proceeds. Source emission should split `DC:D637..DC:E036` into
the typed current-position selector plane and the numeric-preserve second plane
recorded in `notes/cf-event-music-context-contracts.md`. The remaining DC
semantic work is identifying the unnamed second per-sector byte plane if a
consumer proves it, plus optional arrangement/music cross-reference fixtures.
