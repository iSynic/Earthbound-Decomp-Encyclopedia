# Map Tile Animation Runtime Contract

This ROM-verified contract closes the active EF/C0 map tile-animation
runtime tables used by `C0:0085` and consumed by `C0:0172`.

## Summary

- entries: `20`
- graphics pointer/asset matches: `20`
- upload-script records: `24`
- nonempty scripts: `12`
- empty scripts: `8`
- tiny placeholder payload IDs: `2, 3, 4, 9, 10, 11, 14, 15`
- placeholder/empty-script matches: `8`
- nonplaceholder/nonempty-script matches: `12`
- max script records per entry: `6`
- all scripts fit `$43DC` runtime capacity: `True`
- all scripts end at the next pointer: `True`
- script data ends at sprite grouping table start: `True`

## Runtime Model

- selector: `$4372`
- graphics pointer table: `EF:11CB..EF:121B`
- upload-script pointer table: `EF:121B..EF:126B`
- upload-script data: `EF:126B..EF:133F`
- decompressed graphics buffer: `7E:C000`
- runtime records: `$43DC` records of `16` bytes
- active record count: `$4472`
- VRAM transfer routine: `C0:8616 mode A=0`

Each 8-byte upload-script record expands to one 16-byte runtime record:

| Runtime offset | Field | Source |
| --- | --- | --- |
| `+0x00` | `frame_count_limit` | script byte +0 |
| `+0x02` | `reload_delay` | script byte +1 |
| `+0x04` | `transfer_size_bytes` | script word +2 |
| `+0x06` | `source_base_offset` | script word +4 |
| `+0x08` | `vram_destination` | script word +6 |
| `+0x0A` | `live_countdown` | initialized from +0x02 |
| `+0x0C` | `live_frame_counter` | initialized to 0 |
| `+0x0E` | `live_source_offset` | initialized from +0x06 |

## Entries

| ID | Graphics Pointer | Asset | Compressed Bytes | Script Records | Sector Count | Direct `.fts` Rows | Max Source End | Status |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 0 | `DF:C243` | `MAP_DATA_TILE_ANIMATION_GFX_0` | 1784 | 5 | 79 | 12 | `0x0CA0` | `active` |
| 1 | `DF:C93B` | `MAP_DATA_TILE_ANIMATION_GFX_1` | 580 | 2 | 191 | 3 | `0x05A0` | `active` |
| 2 | `DF:CB7F` | `MAP_DATA_TILE_ANIMATION_GFX_2` | 25 | 0 | 0 | 4 | `0x0000` | `placeholder-empty` |
| 3 | `DF:CB98` | `MAP_DATA_TILE_ANIMATION_GFX_3` | 25 | 0 | 0 | 2 | `0x0000` | `placeholder-empty` |
| 4 | `DF:CBB1` | `MAP_DATA_TILE_ANIMATION_GFX_4` | 25 | 0 | 143 | 2 | `0x0000` | `placeholder-empty` |
| 5 | `DF:CBCA` | `MAP_DATA_TILE_ANIMATION_GFX_5` | 1078 | 1 | 55 | 4 | `0x0820` | `active` |
| 6 | `DF:D000` | `MAP_DATA_TILE_ANIMATION_GFX_6` | 1774 | 2 | 131 | 7 | `0x0F20` | `active` |
| 7 | `DF:D6EE` | `MAP_DATA_TILE_ANIMATION_GFX_7` | 1641 | 2 | 81 | 1 | `0x1120` | `active` |
| 8 | `DF:DD57` | `MAP_DATA_TILE_ANIMATION_GFX_8` | 1172 | 1 | 8 | 2 | `0x0FA0` | `active` |
| 9 | `DF:E1EB` | `MAP_DATA_TILE_ANIMATION_GFX_9` | 25 | 0 | 43 | 6 | `0x0000` | `placeholder-empty` |
| 10 | `DF:E204` | `MAP_DATA_TILE_ANIMATION_GFX_10` | 25 | 0 | 12 | 52 | `0x0000` | `placeholder-empty` |
| 11 | `DF:E21D` | `MAP_DATA_TILE_ANIMATION_GFX_11` | 25 | 0 | 9 | 14 | `0x0000` | `placeholder-empty` |
| 12 | `DF:E236` | `MAP_DATA_TILE_ANIMATION_GFX_12` | 460 | 1 | 5 | 8 | `0x06E0` | `active` |
| 13 | `DF:E402` | `MAP_DATA_TILE_ANIMATION_GFX_13` | 198 | 1 | 94 | 20 | `0x0220` | `active` |
| 14 | `DF:E4C8` | `MAP_DATA_TILE_ANIMATION_GFX_14` | 25 | 0 | 8 | 8 | `0x0000` | `placeholder-empty` |
| 15 | `DE:F0E7` | `MAP_DATA_TILE_ANIMATION_GFX_15` | 25 | 0 | 16 | 5 | `0x0000` | `placeholder-empty` |
| 16 | `DE:F100` | `MAP_DATA_TILE_ANIMATION_GFX_16` | 463 | 6 | 6 | 7 | `0x0720` | `active` |
| 17 | `DE:F2CF` | `MAP_DATA_TILE_ANIMATION_GFX_17` | 796 | 1 | 14 | 4 | `0x0AA0` | `active` |
| 18 | `DE:F5EB` | `MAP_DATA_TILE_ANIMATION_GFX_18` | 638 | 1 | 40 | 1 | `0x0820` | `active` |
| 19 | `DE:F869` | `MAP_DATA_TILE_ANIMATION_GFX_19` | 1140 | 1 | 15 | 6 | `0x0B60` | `active` |

## Upload Script Records

| ID | Record | Frames | Delay | Transfer Bytes | Source Offset | Source End | VRAM Destination |
| ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| 0 | 0 | 4 | 12 | 96 | `0x0020` | `0x01A0` | `0x0010` |
| 0 | 1 | 4 | 15 | 96 | `0x01A0` | `0x0320` | `0x0040` |
| 0 | 2 | 4 | 15 | 128 | `0x0320` | `0x0520` | `0x0070` |
| 0 | 3 | 4 | 21 | 224 | `0x0520` | `0x08A0` | `0x00B0` |
| 0 | 4 | 4 | 21 | 256 | `0x08A0` | `0x0CA0` | `0x0120` |
| 1 | 0 | 4 | 19 | 320 | `0x0020` | `0x0520` | `0x0010` |
| 1 | 1 | 2 | 20 | 64 | `0x0520` | `0x05A0` | `0x00B0` |
| 5 | 0 | 8 | 10 | 256 | `0x0020` | `0x0820` | `0x0010` |
| 6 | 0 | 4 | 10 | 384 | `0x0020` | `0x0620` | `0x2010` |
| 6 | 1 | 4 | 21 | 576 | `0x0620` | `0x0F20` | `0x00D0` |
| 7 | 0 | 5 | 49 | 640 | `0x0020` | `0x0CA0` | `0x0010` |
| 7 | 1 | 4 | 18 | 288 | `0x0CA0` | `0x1120` | `0x0150` |
| 8 | 0 | 4 | 20 | 992 | `0x0020` | `0x0FA0` | `0x0010` |
| 12 | 0 | 3 | 5 | 576 | `0x0020` | `0x06E0` | `0x0010` |
| 13 | 0 | 8 | 3 | 64 | `0x0020` | `0x0220` | `0x0010` |
| 16 | 0 | 2 | 31 | 64 | `0x0020` | `0x00A0` | `0x2010` |
| 16 | 1 | 2 | 31 | 192 | `0x00A0` | `0x0220` | `0x0030` |
| 16 | 2 | 2 | 31 | 64 | `0x0220` | `0x02A0` | `0x2090` |
| 16 | 3 | 2 | 31 | 320 | `0x02A0` | `0x0520` | `0x00B0` |
| 16 | 4 | 2 | 25 | 64 | `0x0520` | `0x05A0` | `0x2150` |
| 16 | 5 | 2 | 25 | 192 | `0x05A0` | `0x0720` | `0x0170` |
| 17 | 0 | 4 | 15 | 672 | `0x0020` | `0x0AA0` | `0x0010` |
| 18 | 0 | 4 | 19 | 512 | `0x0020` | `0x0820` | `0x0010` |
| 19 | 0 | 6 | 20 | 480 | `0x0020` | `0x0B60` | `0x0010` |

## Interpretation Boundary

This contract resolves the active runtime graphics/script table pair. The
290-character `.fts` animation/settings rows are still a separate export
layer: they are structurally related to map tileset animation/settings work,
but their row counts do not equal these C0 upload-script record counts.

The older community ROM map labels around `0x2F13CB..0x2F153E` are not used
as the current runtime anchor here; local C0 code and the sprite-frame
contract place those bytes inside the sprite grouping pointer/data region.

## Machine-Readable Data

`notes/map-tile-animation-runtime-contract.json` records one row per
animation ID with matched graphics asset metadata, decoded upload-script
fields, tileset/sector context, and direct `.fts` row context.
