# Map FTS 290-Row Structural Contract

This contract maps the variable 290-character section of each local EBDecomp
`.fts` tileset export. It keeps the payload opaque but records the stable
row/block shape that led to the resolved palette-variant decoder.

The initial working label was tile-animation/settings metadata. That is now
split: `notes/map-fts-palette-variant-contract.md` resolves these 290-character
rows as map palette variant visual payloads, while
`notes/map-tile-animation-runtime-contract.md` covers the separate C0/EF
tile-animation runtime tables.

## Summary

- tilesets audited: `20`
- rows: `168`
- row count range per tileset: `1-52`
- blocks: `840`
- row shape: `variable rows per tileset; each row is 5 blocks of 58 base32-like characters`
- unique row IDs: `168`
- duplicate row IDs: `none`
- single-tileset-owned row groups: `32`
- multi-tileset row groups: `0`
- character set: `0123456789abcdefghijklmnopqrstuv`
- separate runtime animation graphics payloads tracked elsewhere: `20`

## Row ID Distribution

- groups: `0`:4, `1`:3, `2`:4, `3`:2, `4`:2, `5`:4, `6`:7, `7`:1, `8`:2, `9`:6, `a`:8, `b`:8, `c`:8, `d`:4, `e`:8, `f`:8, `g`:4, `h`:8, `i`:1, `j`:7, `k`:8, `l`:5, `m`:5, `n`:4, `o`:5, `p`:8, `q`:6, `r`:5, `s`:6, `t`:6, `u`:3, `v`:8
- slots: `0`:32, `1`:30, `2`:27, `3`:25, `4`:19, `5`:15, `6`:11, `7`:9

## Separate Runtime Animation Anchors

These anchors are retained to document why the original broad working
label included animation. They describe the separate C0/EF tile-animation
runtime path, not the resolved 290-character palette payload rows.

- WRAM runtime state: `$43DC..$445B` (`128` bytes) is labeled map tile animation data in `refs/community-earthbound-docs/RAM_map.txt`.
- Legacy ROM map anchors compressed tile-animation character blocks at `0x1EF2E7..0x1EFEDC` and `0x1FC443..0x1FE6E0`.
- The ROM-verified runtime contract anchors the active C0 tables at `EF:11CB..EF:121B` for graphics pointers, `EF:121B..EF:126B` for upload-script pointers, and `EF:126B..EF:133F` for upload-script records.
- Older community ROM map labels around `0x2F13CB..0x2F153E` conflict with local C0/sprite-grouping evidence and are treated as stale for runtime table identity.
- ebsrc exposes `MAP_DATA_TILE_ANIMATION_PTR_TABLE`, `MAP_DATA_WEIRD_TILE_ANIMATION_PTR_TABLE`, and `MAP_DATA_TILE_ANIMATION_GFX_0..19` symbols.
- Local bank maps identify `20` `MAP_DATA_TILE_ANIMATION_GFX_N` payloads; 25-byte placeholder/tiny payload IDs are `2, 3, 4, 9, 10, 11, 14, 15`.
- Bank EF's include list names the tileset animation pointer table, animation properties pointer table, and per-tileset animation property files `00..19`.

## Row ID Model

The leading two characters of each 290-character row are now treated as a
structural row ID: `row_id[0]` is the base32-like palette/tileset group
and `row_id[1]` is the palette variant slot within that group. The
resolved palette contract verifies this model against `MAP_DATA_PALETTE_N`
assets and `map_palette_settings.yml`.

| Group | Owner tileset(s) | Slots |
| --- | --- | --- |
| `0` | `0` | `0, 1, 2, 3` |
| `1` | `1` | `0, 1, 2` |
| `2` | `2` | `0, 1, 2, 3` |
| `3` | `3` | `0, 1` |
| `4` | `4` | `0, 1` |
| `5` | `5` | `0, 1, 2, 3` |
| `6` | `6` | `0, 1, 2, 3, 4, 5, 6` |
| `7` | `7` | `0` |
| `8` | `8` | `0, 1` |
| `9` | `9` | `0, 1, 2, 3, 4, 5` |
| `a` | `10` | `0, 1, 2, 3, 4, 5, 6, 7` |
| `b` | `10` | `0, 1, 2, 3, 4, 5, 6, 7` |
| `c` | `10` | `0, 1, 2, 3, 4, 5, 6, 7` |
| `d` | `17` | `0, 1, 2, 3` |
| `e` | `10` | `0, 1, 2, 3, 4, 5, 6, 7` |
| `f` | `10` | `0, 1, 2, 3, 4, 5, 6, 7` |
| `g` | `10` | `0, 1, 2, 3` |
| `h` | `10` | `0, 1, 2, 3, 4, 5, 6, 7` |
| `i` | `18` | `0` |
| `j` | `16` | `0, 1, 2, 3, 4, 5, 6` |
| `k` | `12` | `0, 1, 2, 3, 4, 5, 6, 7` |
| `l` | `11` | `0, 1, 2, 3, 4` |
| `m` | `11` | `0, 1, 2, 3, 4` |
| `n` | `11` | `0, 1, 2, 3` |
| `o` | `15` | `0, 1, 2, 3, 4` |
| `p` | `14` | `0, 1, 2, 3, 4, 5, 6, 7` |
| `q` | `19` | `0, 1, 2, 3, 4, 5` |
| `r` | `13` | `0, 1, 2, 3, 4` |
| `s` | `13` | `0, 1, 2, 3, 4, 5` |
| `t` | `13` | `0, 1, 2, 3, 4, 5` |
| `u` | `13` | `0, 1, 2` |
| `v` | `0` | `0, 1, 2, 3, 4, 5, 6, 7` |

## Block Position Profiles

Each row splits into five 58-character blocks. The profile below records
stable position-level shape without committing the raw block text.

| Block | Unique blocks | Zero-only blocks | Constant zero positions | Common chars |
| ---: | ---: | ---: | --- | --- |
| 0 | 168 | 0 | `2, 3, 4, 50, 51, 52` | `0`:2884, `v`:879, `8`:349, `h`:262, `k`:252 |
| 1 | 160 | 0 | `40, 41, 42` | `0`:2210, `v`:1263, `8`:352, `j`:283, `f`:279 |
| 2 | 153 | 1 | `30, 31, 32` | `0`:2653, `v`:1234, `8`:336, `f`:285, `j`:260 |
| 3 | 146 | 2 | `20, 21, 22` | `0`:3008, `v`:1071, `8`:360, `j`:257, `f`:251 |
| 4 | 138 | 2 | `10, 11, 12` | `0`:3211, `v`:1000, `8`:471, `6`:262, `k`:261 |

## Per-Tileset Shape

| Tileset | Rows | Blocks | Row IDs |
| ---: | ---: | ---: | --- |
| 0 | 12 | 60 | `00, 01, 02, 03, v0, v1, v2, v3, v4, v5, v6, v7` |
| 1 | 3 | 15 | `10, 11, 12` |
| 2 | 4 | 20 | `20, 21, 22, 23` |
| 3 | 2 | 10 | `30, 31` |
| 4 | 2 | 10 | `40, 41` |
| 5 | 4 | 20 | `50, 51, 52, 53` |
| 6 | 7 | 35 | `60, 61, 62, 63, 64, 65, 66` |
| 7 | 1 | 5 | `70` |
| 8 | 2 | 10 | `80, 81` |
| 9 | 6 | 30 | `90, 91, 92, 93, 94, 95` |
| 10 | 52 | 260 | `a0, a1, a2, a3, a4, a5, a6, a7, b0, b1, b2, b3, b4, b5, b6, b7, c0, c1, c2, c3, c4, c5, c6, c7, e0, e1, e2, e3, e4, e5, e6, e7, f0, f1, f2, f3, f4, f5, f6, f7, g0, g1, g2, g3, h0, h1, h2, h3, h4, h5, h6, h7` |
| 11 | 14 | 70 | `l0, l1, l2, l3, l4, m0, m1, m2, m3, m4, n0, n1, n2, n3` |
| 12 | 8 | 40 | `k0, k1, k2, k3, k4, k5, k6, k7` |
| 13 | 20 | 100 | `r0, r1, r2, r3, r4, s0, s1, s2, s3, s4, s5, t0, t1, t2, t3, t4, t5, u0, u1, u2` |
| 14 | 8 | 40 | `p0, p1, p2, p3, p4, p5, p6, p7` |
| 15 | 5 | 25 | `o0, o1, o2, o3, o4` |
| 16 | 7 | 35 | `j0, j1, j2, j3, j4, j5, j6` |
| 17 | 4 | 20 | `d0, d1, d2, d3` |
| 18 | 1 | 5 | `i0` |
| 19 | 6 | 30 | `q0, q1, q2, q3, q4, q5` |

## Machine-Readable Data

`notes/map-fts-animation-settings-contract.json` records one row per
direct `.fts` export with row IDs, row/block SHA-1 hashes, character sets,
and fixed-shape counts. It intentionally omits raw row content.
