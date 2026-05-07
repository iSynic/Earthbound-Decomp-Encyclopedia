# Text Window Rendering Primitives (`C1:078D-C1:0F40`)

This note captures the current best local read of the early bank-`01` text/window rendering helper cluster after the active-window descriptor accessors.

The reference include map leaves several starts in this area as `unknown/C1/*.asm`, but their neighbors are strongly text-facing: `create_window`, `show_hppp_windows`, `hide_hppp_windows`, `print_letter`, `print_number`, `print_string`, and redirects to bank-`04` text/window helpers.

## Main result

`C1:078D..C1:0F40` is a rendering primitive layer for text windows:

Source-scaffold promotion:

- `C1:078D..07AF` is now decoded source in
  `src/c1/c1_078d_initialize_text_window_tilemap_staging.asm`.
- `C1:07AF..0A85` is now decoded source in
  `src/c1/c1_07af_build_window_tilemap_from_descriptor.asm`.
- `C1:0A85..0BA1` is now decoded source in
  `src/c1/c1_0a85_write_glyph_to_window_descriptor_buffer.asm`.
- `C1:0BA1..0BFE` is now decoded source in
  `src/c1/c1_0ba1_print_glyph_to_active_window.asm`.
- `C1:0BFE..0C49` is now decoded source in
  `src/c1/c1_0bfe_create_pointer_backed_text_entry_record.asm`.
- `C1:0C49..0C55` is now decoded source in
  `src/c1/c1_0c49_count_text_entry_chain_records.asm`.
- `C1:0C55..0D60` is now decoded source in
  `src/c1/c1_0c55_format_number_from_caller_pointer.asm`.
- `C1:0D60..0D7C` is now decoded source in
  `src/c1/c1_0d60_print_glyph_and_mark_window_redraw.asm`.
- `C1:0D7C..0F40` is now decoded source in
  `src/c1/c1_0d7c_format_decimal_digits_to8960.asm`.
- The promoted source validates through the durable C1 scaffold:
  `C1 byte-equivalence: OK, 172 module(s), 0 mismatch(es).`

## Working Names

- `C1:078D` = `InitializeTextWindowTilemapStaging`
- `C1:07AF` = `BuildWindowTilemapFromDescriptor`
- `C1:0A85` = `WriteGlyphToWindowDescriptorBuffer`
- `C1:0BA1` = `PrintGlyphToActiveWindow`
- `C1:0BFE` = `CreatePointerBackedTextEntryRecord`
- `C1:0C55` = `FormatNumberFromCallerPointer`
- `C1:0D60` = `PrintGlyphAndMarkWindowRedraw`
- `C1:0D7C` = `FormatDecimalDigitsTo8960`
- `C4:36D7` = `FillTextWindowRowWithBlankTileWords`
- `C4:3739` = `ClearTextWindowRowAndDisplayObjects`
- `C4:37B8` = `ScrollTextWindowBufferUpOneLine`
- `C4:3874` = `SetWindowDescriptorCursorFields`
- `C4:38A5` = `SetActiveWindowDescriptorCursorFields`
- `C4:38B1` = `AdvanceActiveWindowLineOrScroll`
- `C4:3B15` = `ApplyActiveWindowLineTileAttributeBits`
- `C4:3BB9` = `WriteSpecialActiveWindowStringRun`
- `C4:3CAA` = `AdvanceAnimatedGlyphTileStateOffset`
- `C4:3CD2` = `SetActiveCursorAndStageGlyphRunUpload`
- `C4:3D24` = `StagePendingGlyphVariantTileUpload`
- `C4:3D75` = `StageGlyphVariantTileState`
- `C4:3D95` = `StageActiveCursorGlyphVariantState`
- `C4:3DDB` = `PrintRecordSelectionMarkerAndStageGlyphRun`
- `C4:3E31` = `MeasureActiveWindowStringPixelWidth`
- `C4:3EF8` = `StageCenteredStringGlyphVariantState`
- `C4:3F53` = `LoadMenuNameEntryMaskTableTo1ad6`
- `C4:3F77` = `PrintGlyphWithTileCleanupSoundDelay`
- `C4:406A` = `ReadNameEntryGridCharacter`
- `C4:44FB` = `UploadWindowTitleGlyphTiles`
- `C4:45E1` = `PreflightTextParserWrapForActiveWindow`
- `C4:47FB` = `PrintFixedStringWithWrapPreflight`
- `C4:487C` = `PrintSegmentedStringBufferWithWrapPreflight`
- `C4:4963` = `RefreshTextWindowVramPlanesForMode`
- `C4:4B3A` = `RenderTextTokenGlyphRunToScratchRows`
- `C4:4AD7` = `TextTileBitClearMaskTable`
- `C4:4AF7` = `ReleaseTextTileBitsetSlotForTileWord`
- `C4:4C8C` = `PlaceTextTilePairAtActiveCursor`
- `C4:4E44` = `ClearGlyphVariantOffsetMirrors`
- `C4:4E4D` = `ReleaseNonBlankTextTileWord`
- `C4:4E61` = `StageTextTokenGlyphRunForActiveWindow`
- `C4:4FF3` = `MeasureGlyphByteRunPixelWidth`
- `C4:507A` = `PrintRightAlignedDecimalValueInActiveWindow`
- `C4:5C90` = `RenderMaskedGlyphRunToMenuScratchRows`
- `C4:5DDD` = `FlushMenuGlyphScratchRowsToVram`
- `C4:5E96` = `ResetGlyphScratchAndAdvanceUploadCursor`

- clear or initialize a window tilemap staging area
- build framed window tilemaps from the `$8650` descriptor table
- map text/glyph positions into descriptor-backed tile buffers
- print a letter into the active window and mark redraw state
- provide far wrappers around pointer-based text/name/string helpers
- convert a 32-bit value to decimal digits in the `$8960` staging buffer
- print staged decimal digits and fixed strings into the active window

This region should be treated as low-level text/window drawing support, not as a separate text command-family dispatch island.

## Window Tilemap Setup

`C1:078D` initializes a fixed `$7E` staging region.

It sets a local pointer pair to `$7E:4000`, uses `Y = 827E`, `X = 0240`, and calls `C0:862E` with `A = 00`. The exact `C0:862E` helper name is still inherited from C0 work, but the address range and size make this a clear staging-buffer clear/copy primitive for text/window tilemap data.

`C1:07AF` is the main window frame/tilemap builder for one descriptor id.

It treats the incoming accumulator as a window/descriptor index, scales by descriptor size `$52` through `C0:8FF7`, and reads fields from the `$8650` descriptor table:

- `$8656/$8658` feed the tilemap origin calculation
- `$865A/$865C` act like width/height
- `$865E/$8660` act like cursor or current text position fields
- `$8685` is used as a descriptor-local tile/output base
- `$868B/$868C+` describe optional menu/list text material

The body writes familiar SNES tile words such as `$3C10`, `$3C11`, `$3C12`, `$3C13`, `$3C16`, `$7C10`, `$7C12`, `$7C13`, `$7C16`, `$BC10`, `$BC11`, `$BC13`, `$FC10`, and `$FC13`. Those values form the border/corner/fill vocabulary for framed text windows.

So the best current name for `C1:07AF` is "build/redraw window tilemap from descriptor".

The same promoted source file also preserves the nearby HP/PP display helpers:

- `C1:0A04` enters HP/PP window display mode by calling `C3:E6F8`, setting `$89C9 = 1`, setting `$9623 = 1`, and setting the party-window dirty mask `$9647 = FFFF`.
- `C1:0A1D` leaves HP/PP window display mode by calling `C3:E6F8`, clearing `$89C9`, optionally clearing each party-member HP/PP window through `C2:07E1`, synchronizing the party window record fields rooted at `$99CE`, and setting `$9623 = 1`.

## Glyph Position Writer

`C1:0A85` is the core descriptor-backed glyph-position writer.

Inputs are best read as:

- `A` = window focus/index
- `X` = glyph or tile code to write
- `Y` = an auxiliary descriptor/cursor value

The routine resolves `$88E4[A]` into a `$8650` descriptor, reads and updates `$865E/$8660`, computes the target slot from the descriptor output base at `$8685`, and stores tile/position words back into that descriptor-backed buffer.

The important latch behavior is already corroborated by [battle-text-display-mode-latch-964d.md](notes/battle-text-display-mode-latch-964d.md):

- when `$964D == 1`, `C1:0A85` jumps into the shortened write/update path at `C1:0B8A`
- when `$964D == 2`, it normalizes the width-like value to `$20` and then continues
- when `$964D == 0`, it performs the ordinary paired write/update

It also calls `C4:37B8` when the current row/position reaches the descriptor limit, which matches existing line-control notes that treat the bank-`04` helper as a line/window advance side effect.

`C1:0BA1` is the active-window print-letter bridge into `C1:0A85`.

It returns early if `$8958 == FFFF`; otherwise it resolves the active focus through `$8958 -> $88E4 -> $8650`, takes `$8663` as the auxiliary `Y` value, and calls `C1:0A85` with the incoming accumulator as the glyph/tile code.

The same source module also exposes two adjacent bridge entries:

- `C1:0BD2` clears the active row through `C4:3739`, then resets the active
  descriptor cursor through `C4:38A5`.
- `C1:0BF8` redirects to the `C1:008E` close/drain-all-windows helper and
  returns long.

`C1:0D60` is the redraw-aware sibling of `C1:0BA1`.

It first prints through `C1:0BA1`, then compares the focused descriptor id against `$88E2`. If the focus is not the current/active redraw window, it sets byte `$9623 = 1`, marking that window state needs service.

## String, Name, and Bank-04 Bridges

`C1:0BFE` is a far wrapper around `C1:153B`.

It stages caller pointer pairs from the old direct page into `$0A/$0C/$0E/$10/$12/$14`, passes the incoming accumulator through, and calls `C1:153B`. Several existing notes already find `C1:153B` in PSI/name/text construction paths, so the safe current read is "pointer-based text/name construction bridge" rather than a fully independent renderer.

`C1:0C55` is a far wrapper around `C1:0D7C`.

It stages `$20/$22` into the local pointer pair and then calls the decimal formatter. This is a small exported bridge for number formatting, not a separate algorithm.

Several tiny far wrappers in this same neighborhood just expose bank-`04` text helpers or nearby local helpers:

- `C1:0BF8` -> `C1:008E` close/drain-all-windows helper
- `C1:0C49` -> `C1:138D`
- `C1:0C4F` -> `C1:17E2`
- `C1:0C72` -> `C4:38A5`
- `C1:0C79` -> `C4:38B1`
- `C1:0C80` -> `C1:0BA1`
- `C1:0C86` -> `C1:0CB6`
- `C1:0CAF` -> `C4:37B8`

The reference map's redirect names for `C1:008E`, `C1:138D`, `C1:17E2`, `C4:38A5`, and `C4:37B8` fit this export-wrapper pattern.

## Bank-04 Row Buffer Helpers

The bank-`04` helpers behind the wrappers are now clearer from the legacy listing and local decode:

Source scaffold status: `src/c4/battle_and_text_window_row_helpers.asm`
preserves `C4:3568..C4:38A5`, `src/c4/active_window_descriptor_cursor_wrapper.asm`
preserves `C4:38A5..C4:38B1`, `src/c4/active_window_line_advance_helper.asm`
preserves `C4:38B1..C4:3915`, and `src/c4/locked_text_tiles_data.asm`
preserves the following `C4:3915..C4:3B15` locked tile table.

- `C4:36D7` resolves the window descriptor through `$88E4[A]`, uses caller `X` as a row index, computes the row base from descriptor fields `$865A/$8685`, and fills that row with tile word `#$0040`.
- `C4:3739` resolves the current row from descriptor field `$8660`, sends each existing word through `C4:4AF7`, then calls `C4:36D7` on that same row. That makes it a destructive row clear that also tears down the display objects represented by the old row words.
- `C4:37B8` starts by sending the first row's words through `C4:4AF7`, copies subsequent row words upward in the descriptor buffer, and then calls `C4:36D7` on the last row. This is the scroll-up/line-advance helper used when glyph placement reaches the row limit.

These names deliberately describe the buffer mechanics rather than the user-facing script opcode. `C1:8AAA` / command `0x12` is the higher-level "clear line" command; the bank-`04` routines are descriptor-row primitives shared by glyph placement and command handling.

The adjacent cursor/line-state helpers are similarly small:

- `C4:3874` is the generic setter. It takes a window/focus id in `A`, caller coordinate/state values in `X/Y`, runs `C4:3CAA`, resolves `$88E4[A]` into the `$8650` descriptor table, then writes the caller values to descriptor fields `$865E` and `$8660`.
- `C4:38A5` is the active-window wrapper for `C4:3874`; it supplies `$8958` as the window id and forwards the caller's `A/X` pair into the descriptor fields.
- `C4:38B1` is the active-window line advance helper. It resolves `$8958`, calls `C4:5E96`, increments the descriptor's line field at offset `+$10` until it reaches the height-derived last row, and otherwise calls `C4:37B8` to scroll the buffer before clearing descriptor offset `+$0E`.

This pins `C4:38A5` as a descriptor cursor/state setter rather than a renderer by itself. The broader rendering side effects come from the helpers it calls and from consumers that redraw dirty windows after these fields change.

## Attribute And Variant State Helpers

Source scaffold status: `src/c4/active_window_attribute_and_glyph_state_helpers.asm`
now preserves `C4:3B15..C4:3F77` byte-for-byte in the C4 scaffold. That
promotes the ebsrc exact spans through the centering wrapper and `$1AD6`
menu/name-entry mask reload. `src/c4/active_window_glyph_print_and_cursor_read_helpers.asm`
then preserves `C4:3F77..C4:40B5`, covering the larger glyph-print path and
the adjacent name-entry grid character reader.

The next local block (`C4:3B15..3D95`) is still descriptor-backed text/window presentation code. The useful split is:

- `C4:3B15` resolves the active descriptor, finds the current row's rightmost nonblank tile word, then ORs descriptor field `+$13` into nonblank tile words from the current cursor region through that visible tail. It preserves the low tile id bits with `& #$03FF`, so this is an attribute/palette-bit pass over existing tile words rather than a glyph writer.
- `C4:3BB9` is a special active-window string-run writer used by selection/file-style menu paths. It only operates for focus ids `#$0014`, `#$0018`, `#$0019`, and `#$0024`, reads bytes from the caller pointer in `$28/$2A`, and writes through either `EF:00E6` or `EF:00BB` depending on the caller flag in `X`. It updates descriptor cursor field `+$0E` and clears `$9622`.
- `C4:3CAA` advances the small animated tile-state counter at `$9E25`, derives `$9E23 = $9E25 * 8`, mirrors that value to `$9652`, and clears `$9654`. It wraps after `#$33`.
- `C4:3CD2` sets the active descriptor cursor through the `C1:0C72 -> C4:38A5` wrapper, then, when caller record byte `+$2C` is nonzero, adds that byte to `$9E23` and fills a 32-byte tile-state/upload scratch row rooted at `$3492 + $9E25 * #$20` with `#$FF`.
- `C4:3D24` is the same tile-state upload side without the caller record: it consumes pending byte `$5E72`, adds it to `$9E23`, fills the same `$3492 + frame*#$20` scratch row, latches `$5E72` into `$5E73`, and clears `$5E72`.
- `C4:3D75` is the compact public splitter for that state: low 3 bits of `A` become pending `$5E72`, while the high bits are shifted down and passed to `C4:3D24`.
- `C4:3D95` folds the active descriptor's cursor fields into that compact state. It adds descriptor field `$865E * 8` and the latched `$5E73` to caller `A`, uses descriptor `$8660` as the `X` value, then stages the result through `C4:3D75`.

The exact visual vocabulary behind `$3492` and the `$9E23/$9E25` state still needs asset-level decoding, but the control contract is now local: this family mutates active-window tile words and stages animated/variant tile-state rows used by menu text and equipment/status presentation.

The following helpers bridge that state into actual string/menu operations:

- `C4:3DDB` takes a caller record pointer, uses record fields `+8` and `+A` as cursor inputs through `C1:0C72`, prints marker glyph `#$002F` through `C4:3F77`, advances the animated tile-state offset, and optionally stages a glyph-run upload through `C4:3CD2` when record byte `+$2C` is nonzero. Its only direct external caller sits in the C1 menu/selection path around `C1:169F`.
- `C4:3E31` measures a caller string for the active window. It walks bytes from the pointer in `$24/$26`, uses the current window descriptor and C3 width tables rooted around `C3:F054`, adds spacing byte `$5E6D`, and returns the accumulated width. When `$B4CE` is set, it uses the direct `C3:F054` table; otherwise it selects a table through descriptor field `+$15`.
- `C4:3EF8` is the centering wrapper. It measures the caller string through `C4:3E31`, computes `(descriptor_width * 8 - measured_width) / 2`, and stages that value through `C4:3D75` using the active descriptor's current line field.
- `C4:3F53` copies the 32-word `C2:0958` menu/name-entry mask table into `$1AD6`. It is reached from window/session reset paths at `C0:B810`, `C1:00C2`, and `C2:0202`.
- `C4:3F77` prints one glyph through the active-window writer (`C1:0C80 -> C1:0BA1`) after first passing the current tile words through `C4:4E4D`. It handles the same visible-text side effects seen in the C1 print helpers: clear `$5E75` for glyph `#$002F`, mark redraw through `$9623` when focus differs from `$88E2`, play sound effect `7` when the mode gates allow it, and wait `$9625 + 1` frames unless `$9622` suppresses delay.
- `C4:406A` indexes the name-entry grid tables (`EF:A6D3` plus offsets from `C2:0912`) and returns one zero-extended character byte for the caller's row/column-style inputs.
- `C4:44FB` is the C2-facing window-title upload helper. It takes the descriptor title string pointer in `A` and the registered title VRAM destination in `X`, builds glyph scratch rows through `C4:4B3A`, then queues one `C0:8616` transfer per produced glyph.

Source scaffold status: `src/c4/window_title_wrap_and_fixed_string_print_helpers.asm`
now preserves `C4:44FB..C4:4963`, covering the title upload helper, wrap
preflight, fixed-string wrap/print adapter, and segmented-buffer print adapter.

## Wrap Preflight And Fixed-String Printers

`C4:45E1` is the active text parser's wrap preflight helper.

It is only called directly from `C1:877E`, just before the main text parser consumes the next byte when `$5E6E` is enabled and `$9660` has counted down to zero. The helper copies the live parser pointers, expands text macro tokens `#$15`, `#$16`, and `#$17` through `EB_TextMacroBank1Ptrs`, `EB_TextMacroBank2Ptrs`, and `EB_TextMacroBank3Ptrs`, and sums printable glyph widths from the same C3 width-table family used by `C4:3E31`.

When the predicted width plus the active descriptor cursor would exceed descriptor width field `+$0A`, it calls `C1:0C79` (`C4:38B1`) and sets `$5E75 = 1`. That makes `$5E6E` a parser-side auto-wrap/preflight gate, while `$9660` is the countdown of printable characters already seen by the preflight walker.

The adjacent fixed-string helpers are the renderer-facing counterparts:

- `C4:47FB` accepts a caller string pointer and length, measures it through `C4:3E31`, performs the same descriptor-width comparison, line-advances through `C1:0C79` when needed, then prints through `C1:0C8C -> C1:0EFC`.
- `C4:487C` copies a caller byte stream into the temporary buffer at `$9664`, splitting on terminator `#$00` and explicit marker `#$50`. Each completed segment is sent through `C4:47FB`, so item/PSI/menu labels get the same active-window wrap preflight before being printed.

This closes the practical distinction noted in the item/PSI label cluster: `C1:0EFC` is the lower fixed-length string printer, `C4:47FB` is the fixed-length printer with active-window wrap preflight, and `C4:487C` is the buffered segmented-source adapter used by padded table strings such as item names.

## VRAM Plane Refresh And Tile Bitset Release

`C4:4963` is a mode-selected text/window VRAM plane refresh helper.

Source scaffold status: `src/c4/text_window_vram_plane_refresh_helpers.asm`
now preserves `C4:4963..C4:4AD7`, including the mode `0`, `1`, and `2`
transfer paths. The follow-up scaffold slices now preserve the full
`C4:4AD7..C4:4E61` tile-management corridor: the bit-clear table
(`src/c4/text_tile_bit_clear_mask_table.asm`), release helper
(`src/c4/text_tile_bitset_release_helper.asm`), glyph-run scratch renderer
(`src/c4/text_token_glyph_scratch_renderer.asm`), bit-mask / power-of-two
table (`src/c4/text_tile_power_of_two_word_table.asm`), and placement/catch-up
helpers (`src/c4/text_tile_placement_and_release_helpers.asm`).

Its mode argument selects between DMA and queued-transfer paths for the same `$7F` source windows:

- mode `1` first refreshes `$7F:2000 -> VRAM $7000` for `#$1800` bytes, then falls through to the mode-`0` refresh set.
- mode `0` submits a fixed set of `C0:8616` transfers from `$7F:0000`, `$7F:04F0`, `$7F:05F0`, `$7F:0700`, `$7F:0800`, and `$7F:0900` to VRAM ranges `$6000`, `$6278`, `$62F8`, `$6380`, `$6400`, and `$6480`.
- mode `2` performs the same fixed set through `C0:85B7`, then includes the `$7F:2000 -> $7000` block at the end.

The known caller at `C1:ECB7` sits in the file-select window-flavour preview path after `C4:7C3F`, which fits the helper as a bulk window-tile/plane refresh rather than a text parser routine.

`C4:4AD7` is the bit-clear mask byte table used by `C4:4AF7`. `C4:4AF7` takes an existing descriptor tile word, strips it to the low tile id bits, ignores ids that are not tracked by `DATA_C43915`, and otherwise clears the corresponding bit in the `$1AD6` text-tile allocation bitset. `C4:4E4D` is the safe public wrapper: it ignores blank tile `#$0040` and zero, and only releases tracked nonblank tile words. That is why row clear and scroll helpers call it before overwriting old tile words with blank tile `#$0040`.

`C4:4B3A` renders a text-token glyph run into the `$3492` scratch rows. It merges bytes through the `EF:C51B` / `EF:CD1B` glyph bit-mask tables, commits a row through `C0:8EFC` when starting a fresh row or crossing row boundaries, advances `$9E23` modulo `#$01A0`, and mirrors the active scratch-row index in `$9E25`.

`C4:4C8C` is the active descriptor placement side for dynamic glyph tiles. It takes a two-tile pair in `A/X`, resolves the active descriptor, releases any old nonblank tile words at the current cursor and the row below it, writes the replacement pair into the descriptor tilemap buffer, and advances/wraps the cursor fields.

`C4:4DCA` catches the tile-strip transfer state up to the current scratch-row index. It submits any saved tile pair through `C4:002F`, claims fresh tile words through `C4:0085`, submits the two halves of each row transfer, and feeds the new pair into `C4:4C8C` for descriptor placement.

`C4:4E44` is the tiny reset helper for the two glyph-variant offset mirrors `$9654` and `$9652`. Its only direct caller is the broader text/window state reset around `C4:5EC9`, immediately after that path clears `$9E25/$9E23`, advances/wraps `$9E27`, and clears `$9E29`.

## Numeric And Short-Buffer Layout Helpers

Source scaffold status: `src/c4/active_window_text_token_glyph_run_staging.asm`
now preserves `C4:4E61..C4:4FF3`,
`src/c4/glyph_byte_run_pixel_width_metric_helper.asm` preserves
`C4:4FF3..C4:507A`, and
`src/c4/active_window_right_aligned_decimal_printer.asm` preserves
`C4:507A..C4:51FA`. `src/c4/active_text_entry_chain_layout_helper.asm`
preserves `C4:51FA..C4:54F2`, and
`src/c4/battle_row_position_text_fragments.asm` preserves the adjacent
`C4:54F2..C4:550E` front-row/back-row phrase data.

`C4:4E61` is the active-window staging side of visible text-token glyphs. It
lets direct glyphs such as space/quote/newline go through the ordinary
print-and-advance path, but for rendered glyph bytes it resolves the active
descriptor, clears pending wrap state, looks up the glyph bitmap and width
through the C3 width/pointer matrix, breaks the run into 8-pixel scratch-row
chunks, renders each chunk through `C4:4B3A`, then catches the tile-strip
transfer state up through `C4:4DCA`.

`C4:4FF3` measures a raw byte run using the same C3 width-table family as the active text measurers.

Its caller supplies:

- `A` = byte count
- `X` = width-table selector
- `$24/$26` = source pointer

For each source byte, it normalizes the glyph code through `(byte - #$50) & #$7F`, looks up the selected `C3:F054` width table, adds global spacing byte `$5E6D`, and returns the accumulated pixel width. It does not expand text macros or inspect the active descriptor; it is a compact metric helper for already-buffered glyph bytes.

The direct callers line up with that narrower contract:

- `C1:FB3F` measures the committed favorite-food buffer at `$981F` before positioning it on the name-entry confirmation screen.
- `C1:FBF1` measures the favorite-thing suffix buffer at `$9829` before positioning that same confirmation screen section.
- `C4:516B` measures the temporary digit glyph buffer assembled by `C4:507A`.

`C4:507A` is the active-window right-aligned decimal-value printer.

It takes the caller's numeric value pointer from the shifted direct-page slots that become `$0E/$10`, formats the value through `C1:0C55 -> C1:0D7C` into the `$895A` decimal staging buffer, and then builds a local byte run by converting each digit byte to the glyph-code range used by `C1:0C86`. Before printing, it measures that run through `C4:4FF3`, folds in the active descriptor width and spacing, stages the right-aligned glyph variant state through `C4:3D75`, prints a leading glyph `#$0054`, prints the digits, prints a trailing glyph `#$0024`, and restores the descriptor cursor and `$5E75`.

This makes `C4:507A` a presentation helper, not a money-specific routine. The direct callers cover several display contexts:

- `C1:5650`, in the text-command inventory/money family
- `C1:9E8F`, while rendering equipment/status menu rows
- `C1:AA4C`, where the caller passes the `$9831/$9833` wallet-side value

`C4:51FA` lays out the active text-entry chain attached to the current window
descriptor. It resolves the descriptor's entry list, optionally measures each
linked entry through `C4:3E31`, distributes leftover width into the `$9691`
spacing scratch bytes, writes per-entry X/row fields back into the `$89D4`
records, and clears a stale tail entry when the visible range wraps. The
nearby row-position data begins immediately after the helper at `C4:54F2` with
the locally decoded `To the Front Row` and `the Back Row` fragments.

## Menu Glyph Scratch Upload Helpers

Source scaffold status: `src/c4/masked_menu_glyph_scratch_renderer.asm`
now preserves `C4:5C90..C4:5DDD`, and
`src/c4/menu_glyph_scratch_vram_flush_helper.asm` preserves
`C4:5DDD..C4:5E96`. The follow-on bridge
`src/c4/glyph_scratch_psi_rng_direction_helpers.asm` preserves
`C4:5E96..C4:6028`, including the glyph scratch reset helper, PSI-known
check, inclusive RNG modulo helper, direction matrix, and coordinate direction
resolver.

Source polish: the menu glyph scratch renderer/flush pair now names the
`$9D23` scratch row base, `$9E23/$9E25/$9E27` bit/current/upload cursors,
`$9E2B` transfer latch, `$7900` VRAM base, `+0x80` companion plane
destination, and `C0:8616` transfer-queue tag byte at `$0685`.

`C4:5C90` renders a short masked glyph run into the menu/text glyph scratch rows rooted at `$9D23`.

It waits for `$9E2B` to clear, derives a bit offset from `$9E23`, and writes into the current scratch row selected by `$9E25`. For each of 16 source bytes, it reads both the base plane and the companion byte at source `+$0100`, shifts/masks those bytes through `C0:9251` / `C0:923E`, and merges them into the two 16-byte halves of the `$9D23 + row * #$20` scratch record. After advancing `$9E23` by the caller's width, it updates `$9E25` when the bit position crosses an 8-pixel row boundary and carries the remaining mask work into the next scratch row.

`C4:5DDD` flushes pending scratch rows to VRAM. Its only direct caller is the battle PSI menu display refresh path at `C1:C12F`. It walks from the current `$9E27` upload row toward `$9E25`, computes the VRAM destination under `$7900` from the row index, and submits both 16-byte halves of each `$9D23 + row * #$20` scratch record through `C0:8616`, using the companion destination at `+0x80` for the second half. At completion it stores the new `$9E27` and marks `$9E2B = 1`, matching the busy/wait checks in the scratch renderer.

`C4:5E96` is the reset side of that contract. It waits for `$9E2B` to clear, fills the first 32-byte scratch row at `$9D23` with `#$FF`, clears `$9E25/$9E23`, advances and wraps `$9E27` modulo `#$30`, clears `$9E29`, and calls `C4:4E44` to clear the `$9652/$9654` glyph-variant mirrors. This is why line-advance and row-clear paths call it before mutating active text-window state.

Source polish: `src/c4/glyph_scratch_psi_rng_direction_helpers.asm` now names
the reset side's `$9D23` scratch row base, `$9E23/$9E25/$9E27` cursors,
`$9E29` PSI-menu continuation flag, `$9E2B` transfer latch, scratch clear
byte, and modulo-`#$30` upload cursor wrap.

The same checked-in bridge also corroborates the nearby ebsrc include order:
after the glyph reset helper, the bank enters `CHECK_IF_PSI_KNOWN`,
`RAND_MOD`, the `C4:5F96` direction matrix, and `GET_DIRECTION_TO` before
the entity-slot resolver family begins at `C4:6028`.

## Print Letter Side Effects

`C1:0CB6` is the fuller print-letter side-effect helper.

It resolves the active focus exactly like `C1:0BA1`, but before/around the final delay it also:

  - passes descriptor field `$8665` and the input character to `C4:4E61`, locally named `StageTextTokenGlyphRunForActiveWindow`
- marks `$9623 = 1` if the focus descriptor differs from `$88E2`
- gates sound through `$964F`, `$964D`, `$9622`, and the incoming character
- plays sound effect `7` through `C0:ABE0` for ordinary printable characters when sound is enabled
- waits `$9625 + 1` iterations through `C1:2DD5` unless `$9622` suppresses the delay

That makes `C1:0CB6` the best local candidate for "print visible letter with sound/delay side effects", while `C1:0BA1` remains the lower raw active-window glyph writer.

## Decimal Formatter

`C1:0D7C` converts a 32-bit value to decimal digits in the `$8960` staging area and returns the digit count.

The routine reads the caller-supplied value pointer through the shifted direct-page frame, initializes `X = 8960`, and repeatedly divides the current value by `10` using the shared C0 divide helper chain (`C0:9237` / `C0:91A6`). Each remainder byte is written backward into the staging buffer. When the quotient drops below `10`, the final byte is written and the digit count in `$12` is returned in `A`.

The exact byte-to-glyph translation happens downstream; locally, `C1:0D7C` is the numeric decimal digit builder that feeds print-number paths.

The adjacent source-promoted entries complete the local numeric/string bridge:

- `C1:0DF6` clamps caller values to `$FFFF967F`, formats them through `C1:0D7C`, stages active-window digit alignment through `C4:3D95`, and prints glyph digits through `C1:0CB6`.
- `C1:0EB4` sets the active window descriptor's text-mode byte at descriptor field `$8662`.
- `C1:0EE3` dispatches debug/menu print mode `1` to `C1:2BF3` and mode `2` to `C1:2C36`.
- `C1:0EFC` prints a caller-supplied fixed-length string through the active-window glyph path, with optional centering setup through `C4:3EF8` when `$5E74` is set.
- `C1:0FAC` sets the active window descriptor's glyph-mode flag at descriptor
  field `$8665`, mapping command value `$30` to zero and other values to one.
  The dynamic source-selector corridor now calls it by that mechanical contract.

## Practical Conclusion

The unknown starts `C1:078D`, `C1:07AF`, `C1:0A04`, `C1:0A1D`, `C1:0A85`, `C1:0BA1`, `C1:0BFE`, `C1:0C55`, `C1:0D60`, `C1:0D7C`, `C1:0DF6`, `C1:0EB4`, `C1:0EE3`, `C1:0EFC`, and `C1:0FAC` are now locally accounted for as text/window rendering primitives and wrappers.

The early `C1:078D..0F40` strip is now source-backed through the durable C1 scaffold. The C1 side is much clearer: descriptor-backed window tilemap construction, HP/PP display window sync, glyph placement, side-effectful letter print, decimal staging, decimal printing, and fixed-string printing. The adjacent `C1:0F40..1F8A` text-entry/window-record corridor is also source-backed; the latest polish passes name its clear-window, glyph reset, instant-print, decimal-format, active-chain rendering, selection-menu, title-upload, text-length, sound, input-tick, multiply, and divide helper joins.
