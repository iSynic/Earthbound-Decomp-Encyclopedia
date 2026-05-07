# Map Scene Composition Contract

This contract joins sector metadata, placed scene features, tileset bundle
dependencies, `.fts` component contracts, palette variants, and sector-local
`map_tiles.map` tile-reference statistics.

It intentionally does not store the 8x8 tile grids themselves. The JSON keeps
hashes, counts, and dependency status so preview/build tools can regenerate
ROM-derived scene payloads locally.

## Summary

- scenes/sectors: `1280`
- used tilesets: `28`
- direct `.fts` scenes: `950`
- palette-settings-only scenes: `330`
- scene dependency status: `direct_fts_contracts_present`:950, `palette_settings_only`:330
- palette status: `palette_variant_present`:1280
- global unique map-tile IDs: `935`
- global map-tile ID range: `0-934`
- direct `.fts` out-of-range tile IDs: `0`

## `map_tiles.map` Shape

- world token grid: `320x256`
- sector grid: `40x32`
- sector-local tile-reference grid: `8x8`
- tokens per sector: `64`

Rows in `map_tiles.map` are world `x` columns; each row contains world `y`
entries. A sector at `(x, y)` consumes an 8x8 window starting at `(x*8, y*8)`.

## Top Feature Scenes

| Scene | Sector | Tileset | Palette | Objects | Triggers | Hotspots | Music |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `map_scene.1279` | `39,31` | 29 | 3 | 21 | 2 | 0 | 51 |
| `map_scene.0766` | `23,30` | 22 | 0 | 18 | 5 | 0 | 122 |
| `map_scene.0329` | `10,9` | 1 | 0 | 15 | 0 | 0 | 2 |
| `map_scene.0929` | `29,1` | 13 | 1 | 14 | 7 | 0 | 7 |
| `map_scene.1141` | `35,21` | 5 | 0 | 12 | 3 | 0 | 20 |
| `map_scene.0061` | `1,29` | 12 | 7 | 12 | 2 | 0 | 70 |
| `map_scene.0518` | `16,6` | 1 | 0 | 11 | 0 | 0 | 2 |
| `map_scene.1198` | `37,14` | 4 | 0 | 10 | 2 | 0 | 11 |
| `map_scene.0418` | `13,2` | 1 | 0 | 10 | 1 | 0 | 2 |
| `map_scene.0759` | `23,23` | 7 | 0 | 9 | 5 | 0 | 12 |
| `map_scene.1178` | `36,26` | 26 | 2 | 9 | 5 | 0 | 32 |
| `map_scene.0008` | `0,8` | 1 | 0 | 9 | 4 | 0 | 2 |
| `map_scene.0254` | `7,30` | 14 | 0 | 9 | 2 | 0 | 81 |
| `map_scene.0490` | `15,10` | 1 | 0 | 9 | 1 | 0 | 2 |
| `map_scene.1082` | `33,26` | 29 | 4 | 9 | 1 | 0 | 53 |
| `map_scene.0716` | `22,12` | 26 | 0 | 8 | 12 | 0 | 47 |
| `map_scene.0821` | `25,21` | 7 | 0 | 8 | 3 | 0 | 12 |
| `map_scene.0190` | `5,30` | 24 | 0 | 8 | 2 | 0 | 62 |
| `map_scene.0318` | `9,30` | 14 | 0 | 8 | 2 | 0 | 81 |
| `map_scene.0990` | `30,30` | 4 | 1 | 8 | 2 | 0 | 59 |

## Machine-Readable Data

`notes/map-scene-composition-contract.json` records one row per sector with:

- stable `map_scene.NNNN` IDs
- tileset and `.fts` component dependency statuses
- palette variant availability
- sector-local `map_tiles.map` window hash and tile-ID statistics
- object/trigger/hotspot/music/enemy-map feature counts

## Next Refinement

Use this contract to drive ignored scene previews. The first preview pass can
render each sector's 8x8 arrangement IDs as grayscale blocks, then expand to
real metatile composition using the `.fts` arrangement/collision and tile-pixel
contracts.
