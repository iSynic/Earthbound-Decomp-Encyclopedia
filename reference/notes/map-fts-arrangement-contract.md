# Map FTS Arrangement/Collision Contract

This contract decodes the 96-character section of each local EBDecomp `.fts`
tileset export as `1024` arrangement/collision records.

The first two bytes in each cell are the BG tilemap descriptor. The
third byte is now storage-verified as the tile collision/behavior byte
by `notes/map-collision-pointer-contract.md`; only its exact low-bit
gameplay meanings remain under runtime naming.

## Summary

- tilesets audited: `20`
- records: `20480`
- cells: `327680`
- packed bytes represented: `983040`
- record shape: `1024 records per tileset; each record is 16 cells in a 4x4 grid; each cell is 3 bytes`
- zero records: `8057`
- nonzero cells: `198768`
- tile index range from descriptor words: `0-989`
- priority cells: `94726`
- horizontal-flip cells: `99895`
- vertical-flip cells: `96150`
- attribute-byte high-bit cells: `110422`

## Field Model

| Offset In Cell | Size | Working Name | Status |
| ---: | ---: | --- | --- |
| 0 | 2 | `descriptor_word_le` | high-confidence SNES BG tilemap-word candidate |
| 2 | 1 | `collision_attribute_byte` | ROM-verified tile collision/behavior byte; low-bit gameplay names still pending |

`descriptor_word_le` cleanly yields normal SNES tilemap fields: tile index
bits `0-9`, palette bits `10-12`, priority bit `13`, horizontal flip bit
`14`, and vertical flip bit `15`.

## Attribute Byte Values

`0x00`:193583, `0x01`:7876, `0x02`:12, `0x03`:6874, `0x04`:4617, `0x05`:88, `0x07`:2, `0x08`:1666, `0x09`:357, `0x0B`:324, `0x0C`:1064, `0x0D`:141, `0x0F`:403, `0x10`:251, `0x80`:109335, `0x82`:468, `0x84`:3, `0x90`:611, `0x92`:3, `0x94`:2

## Per-Tileset Shape

| Tileset | Zero Records | Unique Records | Nonzero Cells | Attr Values |
| ---: | ---: | ---: | ---: | ---: |
| 0 | 192 | 833 | 13312 | 6 |
| 1 | 179 | 843 | 13520 | 8 |
| 2 | 197 | 827 | 13232 | 7 |
| 3 | 500 | 524 | 8384 | 7 |
| 4 | 89 | 936 | 14960 | 6 |
| 5 | 737 | 288 | 4592 | 5 |
| 6 | 149 | 876 | 14000 | 13 |
| 7 | 275 | 750 | 11984 | 8 |
| 8 | 396 | 629 | 10048 | 8 |
| 9 | 91 | 934 | 14928 | 5 |
| 10 | 153 | 872 | 13936 | 6 |
| 11 | 311 | 714 | 11408 | 6 |
| 12 | 562 | 463 | 7392 | 7 |
| 13 | 142 | 883 | 14112 | 10 |
| 14 | 821 | 204 | 3248 | 7 |
| 15 | 881 | 144 | 2288 | 6 |
| 16 | 634 | 391 | 6240 | 6 |
| 17 | 681 | 344 | 5488 | 5 |
| 18 | 579 | 446 | 7120 | 9 |
| 19 | 488 | 537 | 8576 | 7 |

## Machine-Readable Data

`notes/map-fts-arrangement-contract.json` records one row per direct `.fts`
export with per-tileset row hashes, record/cell counts, descriptor-word
statistics, and attribute-byte distributions.
