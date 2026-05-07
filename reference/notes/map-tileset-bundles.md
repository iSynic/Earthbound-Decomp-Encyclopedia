# Map Tileset Bundle Contract

This first-pass tileset contract catalogs the EBDecomp `.fts` exports,
palette-setting groups, and the sector `Tileset` IDs that depend on them.

It is intentionally conservative: sector tileset IDs `20`, `22-30` have
palette settings and sector use, but no direct `.fts` export in the local
ref checkout. The contract records that gap instead of inventing a mapping.

## Summary

- tileset ID domain: `32`
- tileset IDs used by sectors: `28`
- direct `.fts` exports in refs: `20`
- used IDs with direct `.fts` export: `18`
- used IDs without direct `.fts` export: `10`
- palette-setting tileset groups: `32`
- palette-setting variants: `168`
- unused direct `.fts` export IDs: `2, 3`
- used IDs without direct `.fts` export: `20, 22, 23, 24, 25, 26, 27, 28, 29, 30`
- unused tileset IDs: `2, 3, 21, 31`

## Top Tilesets By Sector Count

| Tileset | Sectors | Status |
| ---: | ---: | --- |
| 1 | 191 | `direct_fts_export` |
| 4 | 143 | `direct_fts_export` |
| 6 | 131 | `direct_fts_export` |
| 13 | 94 | `direct_fts_export` |
| 7 | 81 | `direct_fts_export` |
| 26 | 81 | `palette_settings_only` |
| 0 | 79 | `direct_fts_export` |
| 28 | 76 | `palette_settings_only` |
| 27 | 66 | `palette_settings_only` |
| 5 | 55 | `direct_fts_export` |
| 30 | 46 | `palette_settings_only` |
| 9 | 43 | `direct_fts_export` |
| 18 | 40 | `direct_fts_export` |
| 29 | 25 | `palette_settings_only` |
| 15 | 16 | `direct_fts_export` |
| 19 | 15 | `direct_fts_export` |
| 17 | 14 | `direct_fts_export` |
| 22 | 14 | `palette_settings_only` |
| 10 | 12 | `direct_fts_export` |
| 11 | 9 | `direct_fts_export` |

## `.fts` Export Shape

All present `.fts` exports have a stable line profile:

- `1024` nonblank rows of length `64`
- `1024` nonblank rows of length `96`
- a variable number of nonblank rows of length `290`

The contract stores these as inferred component counts and SHA-1 hashes for
future decoders. The 96-character section is now split structurally as
arrangement/collision records; palette/settings rows remain a follow-up
decoding step.

`notes/map-fts-format-audit.md` expands this into a checked format audit
with per-section hashes, packed byte counts, and conservative component labels.
`notes/map-fts-arrangement-contract.md` decodes the 96-character section
as 1024 arrangement/collision records with 16 three-byte cells each.
`notes/map-fts-animation-settings-contract.md` records the 290-character
tile-animation/settings rows as five 58-character blocks per row.

## CoilSnake Probe Context

- `tileset00-fts-nibble-probe`: changing one hex nibble in
  `Tilesets/00.fts` compiles, but the rebuilt diff is broad (`21693` bytes
  across `D8:8F7B..EF:10B8`). Treat this as evidence that CoilSnake accepts the
  `.fts` edit and then recompresses/reinserts downstream payloads; it is not a
  direct one-byte map runtime field.

## Machine-Readable Data

`notes/map-tileset-bundles.json` records one row per tileset ID with:

- stable `map_tileset.NN` bundle ID
- sector IDs and sector palette/town-map counts
- direct `.fts` export metadata when present
- palette-setting variants from `map_palette_settings.yml`
- dependency status for downstream sector consumers
