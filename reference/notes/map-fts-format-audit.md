# Map FTS Format Audit

This audit maps the local EBDecomp `.fts` tileset export shape without
checking in raw export rows or decoded graphics/data payloads.

## Summary

- direct `.fts` exports audited: `20`
- exports matching current 64/290/96 shape: `20`
- tileset IDs with exports: `0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19`
- variable 290-character row count range: `1-52`

## Inferred Components

| Component | Files | Row Length | Rows/File | Packed Bytes Total | Hex-Like | Character Set |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| `arrangement_collision_rows_96_chars` | 20 | 96 | 1024 | 983040 | `yes` | `0123456789abcdef` |
| `tile_animation_settings_rows_290_chars` | 20 | 290 | 1-52 |  | `no` | `0123456789abcdefghijklmnopqrstuv` |
| `tile_pixel_rows_64_chars` | 20 | 64 | 1024 | 655360 | `yes` | `0123456789abcdef` |

## Current Interpretation

- `tile_pixel_rows_64_chars`: high-confidence 8x8 indexed tile rows. Each row
  has 64 hex-like nibbles, matching one 4bpp 8x8 tile if packed to 32 bytes.
- `tile_animation_settings_rows_290_chars`: variable-count base32-like
  animation/settings rows. Each row splits into 5 blocks of 58 characters.
- `arrangement_collision_rows_96_chars`: fixed 1024-row arrangement/collision
  records. Each row splits into 16 three-byte cells, matching a 4x4 grid of
  8x8 subtiles per map tile/metatile.

## Per-File Shape

| Tileset | Sections | 64 Rows | 290 Rows | 96 Rows | Shape OK |
| ---: | --- | ---: | ---: | ---: | --- |
| 0 | `64/290/96` | 1024 | 12 | 1024 | `yes` |
| 1 | `64/290/96` | 1024 | 3 | 1024 | `yes` |
| 2 | `64/290/96` | 1024 | 4 | 1024 | `yes` |
| 3 | `64/290/96` | 1024 | 2 | 1024 | `yes` |
| 4 | `64/290/96` | 1024 | 2 | 1024 | `yes` |
| 5 | `64/290/96` | 1024 | 4 | 1024 | `yes` |
| 6 | `64/290/96` | 1024 | 7 | 1024 | `yes` |
| 7 | `64/290/96` | 1024 | 1 | 1024 | `yes` |
| 8 | `64/290/96` | 1024 | 2 | 1024 | `yes` |
| 9 | `64/290/96` | 1024 | 6 | 1024 | `yes` |
| 10 | `64/290/96` | 1024 | 52 | 1024 | `yes` |
| 11 | `64/290/96` | 1024 | 14 | 1024 | `yes` |
| 12 | `64/290/96` | 1024 | 8 | 1024 | `yes` |
| 13 | `64/290/96` | 1024 | 20 | 1024 | `yes` |
| 14 | `64/290/96` | 1024 | 8 | 1024 | `yes` |
| 15 | `64/290/96` | 1024 | 5 | 1024 | `yes` |
| 16 | `64/290/96` | 1024 | 7 | 1024 | `yes` |
| 17 | `64/290/96` | 1024 | 4 | 1024 | `yes` |
| 18 | `64/290/96` | 1024 | 1 | 1024 | `yes` |
| 19 | `64/290/96` | 1024 | 6 | 1024 | `yes` |

## Machine-Readable Data

`notes/map-fts-format-audit.json` records each file's line profile, section
hashes, packed byte counts where applicable, and conservative component labels.
