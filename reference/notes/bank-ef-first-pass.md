# Bank EF First Pass

## Main result

Bank `EF` is the final configured bank in the reference bankconfig set and is a
mixed code/data/text/debug bank. It is not an asset slab like the late graphics
or audio banks. The front contains battle/audio/save helpers, the middle carries
map tileset and sprite grouping tables plus large text runs, and the tail is
mostly debug-menu code/data with exact debug font and cursor graphics payloads.

Primary artifacts:

- `notes/bank-ef-reference-frontier.md`
- `notes/bank-ef-asset-data-map.md`
- `notes/bank-ef-source-scaffold-handoff.md`
- `build/asset-bank-ef.json`
- `build/ef-build-candidate-ranges.json`
- `build/ef-byte-equivalence-validation.json`

The generated reference frontier accounts for:

- reference entries: `1065`
- ebsrc include entries: `149`
- local note mentions: `680`
- unknown address-bearing includes: `9`

The generated asset map accounts for:

- binary assets: `2`
- binary asset bytes: `1329`
- table includes: `149`
- inferred table bytes: `60326`
- unresolved late padding after named tail data: `2581` bytes
- source scaffold protected bytes: `65536 / 65536`
- byte-equivalence scaffold validation: `durable-scaffold`, `5` modules,
  `0` non-OK modules, `0` byte mismatches

The table-byte and scaffold figures should be treated cautiously for EF. Most
early/middle EF source includes are absent from the checked-in reference tree, so
the asset manifest and byte-preserving scaffold correctly protect the bytes but
over-coalesce the front of the bank into a single inferred generated span. This
note therefore uses reference source order, encoded address anchors, and local
cross-bank notes as the stronger semantic map.

## Bank layout

The current high-level EF layout is:

- `EF:0000..EF:05A5`: battle enemy flashing helpers, audio pause/resume helpers,
  early unknown routines, and SRAM signature setup. The bankconfig anchors this
  area with `EF:00BB`, `EF:00E6`, `EF:0115`, `EF:016F`, `EF:01D2`, `EF:0262`,
  `EF:027D`, `EF:02C4`, `EF:031E`, `EF:04DC`, and `EF:05A6`.
- `EF:05A6..EF:0C3C`: SRAM/save helper family. The reference source order names
  erase/check/copy/checksum/validate/save/load/integrity routines for save
  blocks and save slots.
- `EF:0C3D..EF:101A`: unknown helper cluster before the map-data table run.
  Local note coverage already recognizes several of these addresses through
  timed-delivery and selector-row helper work, but this pass keeps the region
  grouped until its internal call graph is audited directly.
- `EF:101B..EF:4A3F`: map tileset and sprite grouping tables. The bankconfig
  places the tileset table, graphics/arrangement/palette/collision/animation
  pointer tables, twenty tileset animation property includes, and sprite
  grouping pointer/data includes here.
- `EF:4A40..EF:4E1F`: Sound Stone presentation data. The `C4:AC57` presentation
  block has a nine-entry pointer table targeting `EF:4A40`, `EF:4AD0`,
  `EF:4B3A`, `EF:4BA4`, `EF:4C0E`, `EF:4C78`, `EF:4CE2`, `EF:4D4C`, and
  `EF:4DB6`; the reference source labels the target family as
  `data/unknown/EF4A40.asm`.
- `EF:4E20..EF:C51A`: large text and text-adjacent data run. The source order
  begins with `EEXPLPSI.ebtxt` and continues through battle text, goods text,
  command/status window text, keyboard/name-input layout text, unknown text,
  per-sector town map data, and town map mapping. Local D5 PSI ability table
  work proves that description pointers in `D5:8A50` target PSI help text in
  `EF:4E20..EF:5777`.
- `EF:C51B..EF:CD1A`: text-token glyph merge mask table. `C4:4B3A` uses the
  `EF:C51B` table while merging bit-aligned glyph rows into the active text
  scratch buffer.
- `EF:CD1B..EF:D51A`: companion glyph carry-mask/table region. `C4:4B3A`
  uses `EF:CD1B` when a rendered glyph run crosses into the next scratch row.
- `EF:D51B..EF:D56E`: debug sound-menu option and version strings from the
  listing-visible `sound_menu_option_strings.asm` include.
- `EF:D56F..EF:EB5E`: debug/menu code, debug menu strings, debug overlay
  helpers, cursor/menu processing helpers, and remaining unknown routines. This
  region is mostly debug-facing by source order, but `EF:E759` is also called by
  the overworld spawn/placement path when `$436C != 0`, so not every unknown
  routine here should be assumed to be debug-only.
- `EF:EB5F..EF:EF6F`: `DEBUG_MENU_FONT`, exact binary span, `1041` bytes.
- `EF:EF70..EF:EF9E`: unknown data block before the debug font palette.
- `EF:EF9F..EF:EFB6`: `DEBUG_FONT_PALETTE`, `24` bytes.
- `EF:EFB7..EF:F0D6`: `DEBUG_CURSOR_GRAPHICS`, exact binary span, `288` bytes.
- `EF:F0D7..EF:F5EA`: named late data tail. The bankconfig names
  `data/unknown/EFF0D7.asm`, `data/unknown/EFF1BB.asm`,
  `data/unknown_version_string.asm`, three unused data includes, and
  `data/debug/debug_cursor_spritemap.asm`; the scaffold now preserves these as
  split data islands.
- `EF:F5EB..EF:FFFF`: residual end-of-bank padding after the debug cursor
  spritemap.

## Cross-bank anchors

The strongest local anchors for EF come from consumers in already-audited banks:

- `C4:AC57` points at `EF:4A40..EF:4DB6`, grounding that region as Sound Stone
  presentation data rather than code.
- `D5:8A50` PSI ability rows carry description pointers into `EF:4E20..EF:5777`,
  grounding the front of the text run as PSI help text.
- `C1:D15B..D76D` level-up/stat-gain narration dispatches fixed scripts at
  `EF:7A66..EF:7B46`, grounding part of the text run as level-up battle text.
- `C4:4B3A` uses `EF:C51B` and `EF:CD1B` as glyph mask/carry-mask tables for
  text-token rendering.
- `C0:2668` can call `EF:E759` while resolving spawn candidates, grounding at
  least one late EF routine as a reusable overworld helper rather than pure
  debug-menu private code.
- `C3`/`C4` visual-tail notes mention the `EF:EB3D` area, so the tail before
  `DEBUG_MENU_FONT` should stay on the integration watchlist.

## Current EF confidence boundary

High confidence:

- EF is mixed code/data/text/debug, not a pure asset or audio bank.
- The reference source order in `bank2f.asm` is the best available global map.
- `EF:05A6..0C3C` is a save/SRAM helper family by named source includes.
- `EF:101B..4A3F` is map tileset/sprite grouping table data by named source
  includes.
- `EF:4A40..4E1F`, `EF:4E20..C51A`, `EF:C51B..CD1A`, `EF:CD1B..D51A`, and
  `EF:D51B..D56E` have strong cross-bank corroboration from C4, D5, C1, and
  listing-visible debug-string notes.
- `EF:EB5F..EF:EF6F` and `EF:EFB7..EF:F0D6` are exact binary graphics payloads.
- `src/ef/bank_ef_helpers_asar.asm` protects the full bank through the reusable
  source-bank scaffold pipeline. This is byte closure, not semantic EF source
  completion; true source/data/text splits remain explicit follow-up work.

Still intentionally out of scope:

- Exact internal splits for absent `unknown/EF/*.asm` files.
- Exact byte boundaries inside the large text run between `EF:4E20` and
  `EF:C51A`.
- Semantic meaning of the unknown/unused late-tail payloads at
  `EF:F0D7..F5BA`; the include boundaries are now explicit.
- Full semantic names for the save helpers, map tables, and debug routines.

## Recommended next move

EF is now closed for byte-preserving scaffold purposes. The best follow-up is a
targeted EF split pass if we want semantic confidence in this final bank:

- audit `EF:05A6..0C3C` as the save/SRAM contract family.
- audit `EF:101B..4A3F` as the map tileset and sprite grouping table contract.
- split `EF:4E20..C51A` into text-script families, starting from known D5/C1
  consumers.
- audit `EF:D56F..FFFF` as the debug/tail region, with special attention to
  non-debug callers like `EF:E759`.

Otherwise, the higher-value integration step is to add formal first-pass summary
notes for `C1` through `C4`, since those banks are deeply documented but do not
yet have the same compact `bank-cN-first-pass.md` wrapper files as the later
banks.
