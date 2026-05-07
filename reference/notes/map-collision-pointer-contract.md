# Map Collision Pointer Contract

This ROM-verified contract ties the third byte in each `.fts`
arrangement/collision cell to the bank D8 tile-collision pointer tables.
It promotes that byte from a scene-counted candidate into the actual
collision record byte used by the runtime loader.

## Summary

- D8 collision data pool: `D8:0000..D8:8F50` (`2293` records of `16` bytes)
- pointer tables: `20`
- pointer entries: `12423`
- matched pointer entries against `.fts`: `12423`
- mismatched pointer entries: `0`
- out-of-range pointers: `0`
- misaligned pointers: `0`
- unique pointer offsets: `2293`
- all D8 data records referenced: `True`
- covered `.fts` metatiles: `12423`
- implicit all-zero trailing `.fts` metatiles: `8057`
- trailing nonzero collision cells: `0`
- pointer-expanded values match covered `.fts`: `True`
- full `.fts` values absent from scene sample: `0x84`

## Data Flow

- The D8 data pool is a contiguous set of 16-byte collision records.
- Every pointer word is a 16-byte-aligned offset into that pool.
- For tileset `N`, pointer entry `M` resolves to the exact 16 third-byte
  values in `.fts` metatile `M`.
- Pointer tables stop before the fixed `.fts` length of 1024 metatiles;
  every omitted trailing metatile has all-zero collision bytes.
- Pointer offset `0x0000` is a real data-record offset, not a null pointer.

## Per-Tileset Validation

| Tileset | Entries | Matches | Unique Offsets | Zero-Offset Entries | Implicit Zero Metatiles | Trailing Nonzero Cells | Max Offset |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 832 | 832 | 301 | 339 | 192 | 0 | `0x12C0` |
| 1 | 845 | 845 | 239 | 236 | 179 | 0 | `0x1F10` |
| 2 | 827 | 827 | 271 | 158 | 197 | 0 | `0x2860` |
| 3 | 524 | 524 | 169 | 113 | 500 | 0 | `0x2D00` |
| 4 | 935 | 935 | 240 | 197 | 89 | 0 | `0x36D0` |
| 5 | 287 | 287 | 79 | 112 | 737 | 0 | `0x3990` |
| 6 | 875 | 875 | 376 | 207 | 149 | 0 | `0x4A30` |
| 7 | 749 | 749 | 149 | 443 | 275 | 0 | `0x4DF0` |
| 8 | 628 | 628 | 186 | 228 | 396 | 0 | `0x5900` |
| 9 | 933 | 933 | 159 | 298 | 91 | 0 | `0x5C00` |
| 10 | 871 | 871 | 170 | 399 | 153 | 0 | `0x6230` |
| 11 | 713 | 713 | 192 | 338 | 311 | 0 | `0x6930` |
| 12 | 462 | 462 | 135 | 243 | 562 | 0 | `0x6E10` |
| 13 | 882 | 882 | 280 | 318 | 142 | 0 | `0x7750` |
| 14 | 203 | 203 | 81 | 92 | 821 | 0 | `0x7980` |
| 15 | 143 | 143 | 50 | 64 | 881 | 0 | `0x7AA0` |
| 16 | 390 | 390 | 114 | 149 | 634 | 0 | `0x7DB0` |
| 17 | 343 | 343 | 157 | 105 | 681 | 0 | `0x8270` |
| 18 | 445 | 445 | 185 | 86 | 579 | 0 | `0x8A50` |
| 19 | 536 | 536 | 228 | 190 | 488 | 0 | `0x8F40` |

## Value Alphabet

| Source | Unique Values |
| --- | --- |
| `d8_pool_unique_values` | `0x00`, `0x01`, `0x02`, `0x03`, `0x04`, `0x05`, `0x07`, `0x08`, `0x09`, `0x0B`, `0x0C`, `0x0D`, `0x0F`, `0x10`, `0x80`, `0x82`, `0x84`, `0x90`, `0x92`, `0x94` |
| `fts_unique_values` | `0x00`, `0x01`, `0x02`, `0x03`, `0x04`, `0x05`, `0x07`, `0x08`, `0x09`, `0x0B`, `0x0C`, `0x0D`, `0x0F`, `0x10`, `0x80`, `0x82`, `0x84`, `0x90`, `0x92`, `0x94` |
| `scene_context_unique_values` | `0x00`, `0x01`, `0x02`, `0x03`, `0x04`, `0x05`, `0x07`, `0x08`, `0x09`, `0x0B`, `0x0C`, `0x0D`, `0x0F`, `0x10`, `0x80`, `0x82`, `0x90`, `0x92`, `0x94` |

## Runtime Anchors

- `C0:0CF3` `Load_VerticalMovementCollisionStripPayload`: Reads $7FF800 offset cache, sources bank D8 records, writes collision bytes into $E000 active page.
- `C0:54C9` `Read_CollisionByteAndLatchBit10Coord`: Reads one byte from $E000 active 64x64 page and latches coordinates when bit 0x10 is set.
- `C0:5503/C0:559C/C0:5639/C0:56D0` `Footprint edge collision probes`: OR horizontal/vertical edge samples from $E000 into $5DA4.
- `C0:5E3B/C0:5ECE` `Entity collision cache updates`: Cache probed collision flags with mask #$00D0 before terrain compatibility checks.

## Interpretation Boundary

This contract proves the storage and load relationship for the collision
byte grid. Runtime mask names are now owned by
`notes/map-collision-runtime-bit-contract.md`: `0x80` is the observed
solid/high-collision bit, `0x10` is the special surface coordinate-latch
bit, and `0x04/0x08` feed the entity terrain-compatibility class. The
remaining `0x01/0x02` low modifier labels still need more caller-side
evidence before they should become final gameplay names.

## Machine-Readable Data

`notes/map-collision-pointer-contract.json` records source ranges,
per-table validation, pointer-offset coverage, value distributions,
and runtime anchors without committing raw ROM-derived collision records.
