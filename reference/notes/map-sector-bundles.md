# Map Sector Bundle Contract

This first-pass sector contract joins the 40x32 world-sector grid to placed
objects, sector metadata, tileset bundle references, door/rope/ladder/object trigger refs, enemy-map groups, music
options, hotspots, map-change group counts, and per-sector `map_tiles.map` hashes.

It does not yet decode map graphics, arrangements, palettes, or collision into
engine-ready scene assets. It establishes the scene inventory layer that those
decoders can attach to next.

## Summary

- sector grid: `40x32` = `1280` sectors
- sectors with placed objects: `627`
- placed objects: `1582`
- trigger records: `2080` across `601` sectors
- doors: `1072` across `519` sectors
- object triggers: `220` across `100` sectors
- hotspots: `56` overlapping `65` sectors
- sectors with nonzero enemy-map groups: `107`
- sectors with music override lists: `165`
- sectors whose tileset has map-change groups: `430`
- unique tilesets: `28`
- unique palettes: `8`
- unique music IDs: `84`
- unique town map labels: `6`
- unique enemy-map groups: `21`

## Trigger Types

| Type | Records |
| --- | ---: |
| `door` | 1072 |
| `escalator` | 20 |
| `ladder` | 341 |
| `object` | 220 |
| `person` | 49 |
| `rope` | 300 |
| `stairway` | 72 |
| `switch` | 6 |

## Top Tilesets

| Tileset | Sectors |
| ---: | ---: |
| 1 | 191 |
| 4 | 143 |
| 6 | 131 |
| 13 | 94 |
| 26 | 81 |
| 7 | 81 |
| 0 | 79 |
| 28 | 76 |
| 27 | 66 |
| 5 | 55 |
| 30 | 46 |
| 9 | 43 |
| 18 | 40 |
| 29 | 25 |
| 15 | 16 |
| 19 | 15 |
| 17 | 14 |
| 22 | 14 |
| 10 | 12 |
| 11 | 9 |

## Top Scene-Feature Sectors

| Sector | Objects | Triggers | Doors | Object triggers | Hotspots | Music options | Tileset | Palette |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `0,17` | 1 | 45 | 4 | 5 | 0 | 2 | 27 | 0 |
| `16,27` | 0 | 32 | 0 | 0 | 0 | 0 | 28 | 3 |
| `4,27` | 5 | 11 | 2 | 9 | 0 | 2 | 10 | 6 |
| `23,30` | 18 | 5 | 5 | 0 | 0 | 0 | 22 | 0 |
| `34,17` | 0 | 28 | 0 | 0 | 0 | 0 | 29 | 1 |
| `39,17` | 0 | 14 | 14 | 0 | 0 | 0 | 14 | 0 |
| `5,27` | 2 | 12 | 3 | 9 | 0 | 0 | 17 | 5 |
| `15,19` | 0 | 26 | 0 | 0 | 0 | 0 | 6 | 0 |
| `39,31` | 21 | 2 | 2 | 0 | 0 | 0 | 29 | 3 |
| `27,15` | 1 | 21 | 2 | 0 | 0 | 0 | 4 | 0 |
| `29,1` | 14 | 7 | 2 | 0 | 0 | 0 | 13 | 1 |
| `0,8` | 9 | 4 | 0 | 4 | 0 | 5 | 1 | 0 |
| `0,26` | 0 | 6 | 6 | 0 | 0 | 10 | 5 | 1 |
| `9,4` | 0 | 21 | 1 | 0 | 0 | 0 | 1 | 0 |
| `21,13` | 0 | 21 | 1 | 0 | 0 | 0 | 26 | 0 |
| `2,1` | 0 | 9 | 8 | 1 | 0 | 3 | 30 | 2 |
| `22,12` | 8 | 12 | 0 | 0 | 0 | 0 | 26 | 0 |
| `0,16` | 4 | 6 | 0 | 6 | 0 | 3 | 27 | 0 |
| `2,10` | 5 | 6 | 6 | 0 | 0 | 2 | 1 | 0 |
| `2,30` | 4 | 6 | 5 | 1 | 0 | 3 | 16 | 3 |

## Machine-Readable Data

`notes/map-sector-bundles.json` records one row per sector with:

- `metadata` from `map_sectors.yml`
- `tileset_dependency` as a stable `map_tileset.NN` reference
- `objects` as stable IDs from `notes/map-object-bundles.json`
- `doors` from `map_doors.yml`
- `enemy_map_group` from `map_enemy_placement.yml`
- `music_options` from `map_music.yml`
- `hotspot_ids` by world tile-coordinate overlap
- `map_change_group_count` keyed by sector tileset
- `map_tile_block` hash/byte-count metadata for the sector slice in `map_tiles.map`

## Next Refinement

Attach real decoder outputs to each sector: tileset graphics, arrangements, palettes,
collision, and door/warp destination bundles. The current contract gives those
decoders a stable sector key and scene inventory to attach to.
