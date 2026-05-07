# Map FTS Palette Variant Contract

This contract resolves the 290-character variable rows in EBDecomp
`.fts` exports as map palette variant rows. The earlier structural audit
kept those rows opaque; this pass verifies their byte model against the
bank DA `MAP_DATA_PALETTE_N` assets and `map_palette_settings.yml`.

## Summary

- `.fts` palette rows: `168`
- matching palette-setting keys: `168`
- tileset/palette IDs covered: `32`
- exact raw ROM palette variant matches: `129`
- matches after reserved metadata zeroing: `39`
- unexplained mismatches: `0`
- event-palette override payloads referenced by settings: `14`
- event-palette payloads with 192-byte shape: `14`
- metadata-word/setting mismatches: `0`

## Decoding Model

- row length: `290` characters
- row ID: first two characters
- payload: remaining `288` characters
- decoded payload: `96` SNES BGR555 words (`192` bytes), arranged as `6` subpalettes of `16` colors
- encoding: three `0-v` characters per word, least-significant five-bit digit first
- row ID model: `row_id[0] == tileset/palette asset id`, `row_id[1] == palette variant id`

Raw DA palette variants include small setting fields in reserved color-word
slots. The `.fts` rows are the visual palette payload with those slots
zeroed. This explains every row that does not match the raw ROM bytes
exactly.

| Word Index | Role | Rows Differing From Raw ROM |
| ---: | --- | ---: |
| 0 | `event_flag` | `14` |
| 16 | `event_palette_selector_word` | `14` |
| 32 | `sprite_palette` | `23` |
| 48 | `flash_effect` | `8` |

## Per-Tileset Coverage

| Tileset/Palette ID | Row Group | Variants | Owner `.fts` Export(s) | Status Counts | Sector Count | Dependency |
| ---: | --- | ---: | --- | --- | ---: | --- |
| 0 | `0` | 4 | `refs/eb-decompile-4ef92/Tilesets/00.fts` | `exact_rom_palette_variant_match`:2, `matches_rom_variant_after_reserved_metadata_zeroing`:2 | 79 | `direct_fts_export` |
| 1 | `1` | 3 | `refs/eb-decompile-4ef92/Tilesets/01.fts` | `exact_rom_palette_variant_match`:1, `matches_rom_variant_after_reserved_metadata_zeroing`:2 | 191 | `direct_fts_export` |
| 2 | `2` | 4 | `refs/eb-decompile-4ef92/Tilesets/02.fts` | `exact_rom_palette_variant_match`:2, `matches_rom_variant_after_reserved_metadata_zeroing`:2 | 0 | `direct_fts_export` |
| 3 | `3` | 2 | `refs/eb-decompile-4ef92/Tilesets/03.fts` | `exact_rom_palette_variant_match`:1, `matches_rom_variant_after_reserved_metadata_zeroing`:1 | 0 | `direct_fts_export` |
| 4 | `4` | 2 | `refs/eb-decompile-4ef92/Tilesets/04.fts` | `exact_rom_palette_variant_match`:1, `matches_rom_variant_after_reserved_metadata_zeroing`:1 | 143 | `direct_fts_export` |
| 5 | `5` | 4 | `refs/eb-decompile-4ef92/Tilesets/05.fts` | `exact_rom_palette_variant_match`:4 | 55 | `direct_fts_export` |
| 6 | `6` | 7 | `refs/eb-decompile-4ef92/Tilesets/06.fts` | `exact_rom_palette_variant_match`:5, `matches_rom_variant_after_reserved_metadata_zeroing`:2 | 131 | `direct_fts_export` |
| 7 | `7` | 1 | `refs/eb-decompile-4ef92/Tilesets/07.fts` | `exact_rom_palette_variant_match`:1 | 81 | `direct_fts_export` |
| 8 | `8` | 2 | `refs/eb-decompile-4ef92/Tilesets/08.fts` | `exact_rom_palette_variant_match`:2 | 8 | `direct_fts_export` |
| 9 | `9` | 6 | `refs/eb-decompile-4ef92/Tilesets/09.fts` | `exact_rom_palette_variant_match`:5, `matches_rom_variant_after_reserved_metadata_zeroing`:1 | 43 | `direct_fts_export` |
| 10 | `a` | 8 | `refs/eb-decompile-4ef92/Tilesets/10.fts` | `exact_rom_palette_variant_match`:7, `matches_rom_variant_after_reserved_metadata_zeroing`:1 | 12 | `direct_fts_export` |
| 11 | `b` | 8 | `refs/eb-decompile-4ef92/Tilesets/10.fts` | `exact_rom_palette_variant_match`:7, `matches_rom_variant_after_reserved_metadata_zeroing`:1 | 9 | `direct_fts_export` |
| 12 | `c` | 8 | `refs/eb-decompile-4ef92/Tilesets/10.fts` | `exact_rom_palette_variant_match`:6, `matches_rom_variant_after_reserved_metadata_zeroing`:2 | 5 | `direct_fts_export` |
| 13 | `d` | 4 | `refs/eb-decompile-4ef92/Tilesets/17.fts` | `exact_rom_palette_variant_match`:2, `matches_rom_variant_after_reserved_metadata_zeroing`:2 | 94 | `direct_fts_export` |
| 14 | `e` | 8 | `refs/eb-decompile-4ef92/Tilesets/10.fts` | `exact_rom_palette_variant_match`:5, `matches_rom_variant_after_reserved_metadata_zeroing`:3 | 8 | `direct_fts_export` |
| 15 | `f` | 8 | `refs/eb-decompile-4ef92/Tilesets/10.fts` | `exact_rom_palette_variant_match`:7, `matches_rom_variant_after_reserved_metadata_zeroing`:1 | 16 | `direct_fts_export` |
| 16 | `g` | 4 | `refs/eb-decompile-4ef92/Tilesets/10.fts` | `exact_rom_palette_variant_match`:3, `matches_rom_variant_after_reserved_metadata_zeroing`:1 | 6 | `direct_fts_export` |
| 17 | `h` | 8 | `refs/eb-decompile-4ef92/Tilesets/10.fts` | `exact_rom_palette_variant_match`:6, `matches_rom_variant_after_reserved_metadata_zeroing`:2 | 14 | `direct_fts_export` |
| 18 | `i` | 1 | `refs/eb-decompile-4ef92/Tilesets/18.fts` | `exact_rom_palette_variant_match`:1 | 40 | `direct_fts_export` |
| 19 | `j` | 7 | `refs/eb-decompile-4ef92/Tilesets/16.fts` | `exact_rom_palette_variant_match`:5, `matches_rom_variant_after_reserved_metadata_zeroing`:2 | 15 | `direct_fts_export` |
| 20 | `k` | 8 | `refs/eb-decompile-4ef92/Tilesets/12.fts` | `exact_rom_palette_variant_match`:7, `matches_rom_variant_after_reserved_metadata_zeroing`:1 | 5 | `palette_settings_only` |
| 21 | `l` | 5 | `refs/eb-decompile-4ef92/Tilesets/11.fts` | `exact_rom_palette_variant_match`:5 | 0 | `palette_settings_only` |
| 22 | `m` | 5 | `refs/eb-decompile-4ef92/Tilesets/11.fts` | `exact_rom_palette_variant_match`:4, `matches_rom_variant_after_reserved_metadata_zeroing`:1 | 14 | `palette_settings_only` |
| 23 | `n` | 4 | `refs/eb-decompile-4ef92/Tilesets/11.fts` | `exact_rom_palette_variant_match`:4 | 7 | `palette_settings_only` |
| 24 | `o` | 5 | `refs/eb-decompile-4ef92/Tilesets/15.fts` | `exact_rom_palette_variant_match`:4, `matches_rom_variant_after_reserved_metadata_zeroing`:1 | 4 | `palette_settings_only` |
| 25 | `p` | 8 | `refs/eb-decompile-4ef92/Tilesets/14.fts` | `exact_rom_palette_variant_match`:6, `matches_rom_variant_after_reserved_metadata_zeroing`:2 | 6 | `palette_settings_only` |
| 26 | `q` | 6 | `refs/eb-decompile-4ef92/Tilesets/19.fts` | `exact_rom_palette_variant_match`:2, `matches_rom_variant_after_reserved_metadata_zeroing`:4 | 81 | `palette_settings_only` |
| 27 | `r` | 5 | `refs/eb-decompile-4ef92/Tilesets/13.fts` | `exact_rom_palette_variant_match`:4, `matches_rom_variant_after_reserved_metadata_zeroing`:1 | 66 | `palette_settings_only` |
| 28 | `s` | 6 | `refs/eb-decompile-4ef92/Tilesets/13.fts` | `exact_rom_palette_variant_match`:5, `matches_rom_variant_after_reserved_metadata_zeroing`:1 | 76 | `palette_settings_only` |
| 29 | `t` | 6 | `refs/eb-decompile-4ef92/Tilesets/13.fts` | `exact_rom_palette_variant_match`:4, `matches_rom_variant_after_reserved_metadata_zeroing`:2 | 25 | `palette_settings_only` |
| 30 | `u` | 3 | `refs/eb-decompile-4ef92/Tilesets/13.fts` | `exact_rom_palette_variant_match`:3 | 46 | `palette_settings_only` |
| 31 | `v` | 8 | `refs/eb-decompile-4ef92/Tilesets/00.fts` | `exact_rom_palette_variant_match`:8 | 0 | `palette_settings_only` |

## Interpretation Boundary

This closes the `.fts` 290-row byte shape and ties it to the DA palette
assets. Event-palette override color strings in `map_palette_settings.yml`
are separate 192-byte-shaped payloads referenced by settings; they are
not the base visual row stored inline in the `.fts` palette row.

The map tile-animation runtime path remains documented separately in
`notes/map-tile-animation-runtime-contract.md`.

Script-side palette changes are joined back to these rows in
`notes/map-palette-command-usage-contract.md`.

## Machine-Readable Data

`notes/map-fts-palette-variant-contract.json` records one row per
palette variant with row IDs, owner export, hashes, ROM asset identity,
reserved metadata-word checks, and mismatch classification.
