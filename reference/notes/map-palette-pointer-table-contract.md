# Map Palette Pointer Table Contract

This contract verifies the previously inferred DA map palette pointer table.
The 96-byte table at `DA:FAA7..DA:FB07` is a 32-entry long-pointer table,
and each entry points exactly at the corresponding `MAP_DATA_PALETTE_N`
asset in bank DA.

## Summary

- entries: `32`
- entry size: `3` bytes
- table bytes: `96`
- exact pointer/asset matches: `32`
- palette variant size: `192` bytes
- palette-setting/variant-count mismatches: `0`
- variant-size remainder mismatches: `0`
- palette assets used by sectors: `28`
- palette assets with direct `.fts` exports: `20`

## Entries

| Index | Pointer | Asset | Bytes | Variants | Sectors | Palette Settings | Status |
| ---: | --- | --- | ---: | ---: | ---: | ---: | --- |
| 0 | `DA:7CA7` | `MAP_DATA_PALETTE_0` | 768 | 4 | 79 | 4 | `matches_map_data_palette_asset` |
| 1 | `DA:7FA7` | `MAP_DATA_PALETTE_1` | 576 | 3 | 191 | 3 | `matches_map_data_palette_asset` |
| 2 | `DA:81E7` | `MAP_DATA_PALETTE_2` | 768 | 4 | 0 | 4 | `matches_map_data_palette_asset` |
| 3 | `DA:84E7` | `MAP_DATA_PALETTE_3` | 384 | 2 | 0 | 2 | `matches_map_data_palette_asset` |
| 4 | `DA:8667` | `MAP_DATA_PALETTE_4` | 384 | 2 | 143 | 2 | `matches_map_data_palette_asset` |
| 5 | `DA:87E7` | `MAP_DATA_PALETTE_5` | 768 | 4 | 55 | 4 | `matches_map_data_palette_asset` |
| 6 | `DA:8AE7` | `MAP_DATA_PALETTE_6` | 1344 | 7 | 131 | 7 | `matches_map_data_palette_asset` |
| 7 | `DA:9027` | `MAP_DATA_PALETTE_7` | 192 | 1 | 81 | 1 | `matches_map_data_palette_asset` |
| 8 | `DA:90E7` | `MAP_DATA_PALETTE_8` | 384 | 2 | 8 | 2 | `matches_map_data_palette_asset` |
| 9 | `DA:9267` | `MAP_DATA_PALETTE_9` | 1152 | 6 | 43 | 6 | `matches_map_data_palette_asset` |
| 10 | `DA:96E7` | `MAP_DATA_PALETTE_10` | 1536 | 8 | 12 | 8 | `matches_map_data_palette_asset` |
| 11 | `DA:9CE7` | `MAP_DATA_PALETTE_11` | 1536 | 8 | 9 | 8 | `matches_map_data_palette_asset` |
| 12 | `DA:A2E7` | `MAP_DATA_PALETTE_12` | 1536 | 8 | 5 | 8 | `matches_map_data_palette_asset` |
| 13 | `DA:A8E7` | `MAP_DATA_PALETTE_13` | 768 | 4 | 94 | 4 | `matches_map_data_palette_asset` |
| 14 | `DA:ABE7` | `MAP_DATA_PALETTE_14` | 1536 | 8 | 8 | 8 | `matches_map_data_palette_asset` |
| 15 | `DA:B1E7` | `MAP_DATA_PALETTE_15` | 1536 | 8 | 16 | 8 | `matches_map_data_palette_asset` |
| 16 | `DA:B7E7` | `MAP_DATA_PALETTE_16` | 768 | 4 | 6 | 4 | `matches_map_data_palette_asset` |
| 17 | `DA:BAE7` | `MAP_DATA_PALETTE_17` | 1536 | 8 | 14 | 8 | `matches_map_data_palette_asset` |
| 18 | `DA:C0E7` | `MAP_DATA_PALETTE_18` | 192 | 1 | 40 | 1 | `matches_map_data_palette_asset` |
| 19 | `DA:C1A7` | `MAP_DATA_PALETTE_19` | 1344 | 7 | 15 | 7 | `matches_map_data_palette_asset` |
| 20 | `DA:C6E7` | `MAP_DATA_PALETTE_20` | 1536 | 8 | 5 | 8 | `matches_map_data_palette_asset` |
| 21 | `DA:CCE7` | `MAP_DATA_PALETTE_21` | 960 | 5 | 0 | 5 | `matches_map_data_palette_asset` |
| 22 | `DA:D0A7` | `MAP_DATA_PALETTE_22` | 960 | 5 | 14 | 5 | `matches_map_data_palette_asset` |
| 23 | `DA:D467` | `MAP_DATA_PALETTE_23` | 768 | 4 | 7 | 4 | `matches_map_data_palette_asset` |
| 24 | `DA:D767` | `MAP_DATA_PALETTE_24` | 960 | 5 | 4 | 5 | `matches_map_data_palette_asset` |
| 25 | `DA:DB27` | `MAP_DATA_PALETTE_25` | 1536 | 8 | 6 | 8 | `matches_map_data_palette_asset` |
| 26 | `DA:E127` | `MAP_DATA_PALETTE_26` | 1152 | 6 | 81 | 6 | `matches_map_data_palette_asset` |
| 27 | `DA:E5A7` | `MAP_DATA_PALETTE_27` | 960 | 5 | 66 | 5 | `matches_map_data_palette_asset` |
| 28 | `DA:E967` | `MAP_DATA_PALETTE_28` | 1152 | 6 | 76 | 6 | `matches_map_data_palette_asset` |
| 29 | `DA:EDE7` | `MAP_DATA_PALETTE_29` | 1152 | 6 | 25 | 6 | `matches_map_data_palette_asset` |
| 30 | `DA:F267` | `MAP_DATA_PALETTE_30` | 576 | 3 | 46 | 3 | `matches_map_data_palette_asset` |
| 31 | `DA:F4A7` | `MAP_DATA_PALETTE_31` | 1536 | 8 | 0 | 8 | `matches_map_data_palette_asset` |

## Interpretation Boundary

This closes the table identity: the table maps palette/tileset IDs to bank DA
map palette payload starts. It does not by itself resolve how the three-bit
arrangement descriptor palette field maps onto the six 16-color subpalettes
inside one selected 192-byte palette variant.

## Machine-Readable Data

`notes/map-palette-pointer-table-contract.json` records one row per entry
with pointer target, matched asset metadata, palette variant counts, and
sector/tileset dependency counts.
