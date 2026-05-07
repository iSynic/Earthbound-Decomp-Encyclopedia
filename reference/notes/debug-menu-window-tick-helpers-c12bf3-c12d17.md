# Debug Menu Window Tick Helpers (`C1:2BF3-C1:3187`)

This note covers the remaining unknown starts between the character-select prompt block and the named `WINDOW_TICK` include in reference bank `01`.

See also [debug-menu-reachability-c0-c1-ef.md](notes/debug-menu-reachability-c0-c1-ef.md).

The reference split places these immediately after `text/character_select_prompt.asm`:

- `C1:2BF3` / `UNKNOWN_C12BF3`
- `C1:2C36` / `UNKNOWN_C12C36`
- `C1:2CCC`
- `C1:2D17`
- then `C1:2DD5` / `WINDOW_TICK`
- then `C1:2E42` / `UNKNOWN_C12E42`

## Main result

This cluster is the debug-menu title/animation side that sits next to the ordinary window tick.

## Working Names

- `C1:2BF3` = `PrintDebugMenuTitleWordsWithTicks`
- `C1:2C36` = `PrintDebugMenuFixedWordGroups`
- `C1:2CCC` = `FormatDebugDecimalFiveDigits`
- `C1:2D17` = `ToggleDebugMeterDisplayOverlay`

- `C1:2BF3` prints a zero-terminated word stream from `C3:E84E`, one word at a time through `C1:0D60`, with one `C1:2DD5` frame pump between each printed word.
- `C1:2C36` prints two fixed groups of words from `C3:E862`, four words first and five words after an eight-frame `C1:2E42` pause.
- `C1:2CCC` formats the incoming value as five decimal digits into `$895A`.
- `C1:2D17` toggles a `$9698` debug/display mode and snapshots/restores five mapped rows of `$9A15/$9A1B` into `$969A/$96A2`.

## Fixed Debug Text Printers

`C1:2BF3` and `C1:2C36` both temporarily switch the active text/display context by calling `C1:0FEA` with `A = 3`, print literal words with `C1:0D60`, then restore context with `C1:0FEA(A = 0)`.

`C1:2BF3` points `$06/$08` at `C3:E84E`, reads 16-bit words until it reaches `0000`, and advances by two bytes before each print. After every printed word it runs one `C1:2DD5` tick.

`C1:2C36` points at `C3:E862` and prints a fixed layout:

- four words from the table
- eight calls to `C1:2E42`
- five more words from the table

The reference symbols only name the source data as `UNKNOWN_C3E84E` and `UNKNOWN_C3E862`. The surrounding bank-`03` include order is still useful corroboration: these sit just before `DEBUG_MENU_TEXT` and `DEBUG_MENU_ELEMENT_SPACING_DATA`, and are therefore part of the debug-menu fixed-text region rather than general dialogue text.

## Decimal Staging Helper

`C1:2CCC` writes five decimal ASCII digits to `$895A`.

It takes the input value in `A`, stores it in local `$10`, initializes a divisor at `$2710`, and loops while the divisor is nonzero. Each iteration:

- divides the current value by the divisor through `C0:915B`
- writes quotient + `$30` to `$895A+N`
- replaces the value with the remainder through `C0:9231`
- divides the divisor by ten through `C0:915B`

This is not the same as the general text-number formatter at `C1:0D7C`; it is a fixed-width debug decimal renderer for the nearby debug UI buffer.

## Debug Meter / Display Toggle

`C1:2D17` takes an on/off flag in `A` and stores it to `$9698`.

When `$9698` was clear and the incoming flag is nonzero, it snapshots five mapped entries:

- maps each row index through `C0:8FF7` with stride `$005F`
- copies `$9A15 + mapped` into `$969A + row*2`
- writes `$03E7` into `$9A15 + mapped` and `$9A13 + mapped`
- copies `$9A1B + mapped` into `$96A2 + row*2`
- clears `$9A1B + mapped` and `$9A19 + mapped`

When `$9698` was set and the incoming flag is zero, it reverses the process by restoring `$9A15/$9A1B` from `$969A/$96A2` for the same five mapped rows.

Both transitions end by storing the new `$9698` value and calling `EF:026E`, so this looks like a debug display/meter overlay guard that temporarily hides or neutralizes some per-row values while active.

## Neighboring Tick Routines

The named `C1:2DD5` is the heavier window tick. It starts with `C0:8E9A`, checks `$968C`, `$9622`, `$9623`, and `$88E0`, can redraw through `C1:07AF` or call `C2:087C`, then runs the normal C2 frame/update side and the shared text pump `C1:004E`.

`C1:2E42` is the lighter tick used by wait loops: it calls `C2:109F`, refreshes the `$9649` redraw path through `C1:078D` when needed, then calls `C2:13AC` and `C1:004E`.

`C1:2E63..3187` is now source-backed as `DebugMenuSelectionDispatcher`. It opens the debug/menu presentation state, builds entries from `C3:E874`, drives selection through the shared `C1:196A` menu controller, dispatches the selected branch, then waits on `C1:2DD5` until `$B4A8` clears from `$FFFF`.

## Source Scaffold Promotion

The debug-window island is now checked in as decoded source:

- `src/c1/c1_2bf3_print_debug_menu_title_words_with_ticks.asm` (`C1:2BF3..2C36`)
- `src/c1/c1_2c36_print_debug_menu_fixed_word_groups.asm` (`C1:2C36..2CCC`)
- `src/c1/c1_2ccc_format_debug_decimal_five_digits.asm` (`C1:2CCC..2D17`)
- `src/c1/c1_2d17_toggle_debug_meter_display_overlay.asm` (`C1:2D17..3187`)

The combined C1 scaffold validates byte-for-byte after promotion:

- `C1 byte-equivalence: OK, 172 module(s), 0 mismatch(es).`

## Source Polish Follow-Up (2026-05-06)

The source-backed debug-window island now names the evidence-backed helper-call
surface used by the fixed debug text printers, `WINDOW_TICK`, `C1:2E42`, and
the `C1:2E63..3187` debug menu dispatcher. The promoted calls cover active
tile attributes, glyph printing, window/tick pumps, HP/PP redraw helpers,
debug menu construction, text-entry selection, teleport setup, presentation
scene launches, debug input playback view entry/exit, and file/menu cleanup.

The three dispatcher presentation calls that were left raw in the first
follow-up pass are now named from the adjacent open-menu/debug source and the
reference include order:

- `C1:3031` calls `C1:3D03` / `RunDebugEventFlagToggleViewer`
- `C1:3034` calls `C1:3EE7` / `RunDebugGoodsGrantViewer`
- `C1:30C5` calls `C1:3E0E` / `RunDebugGuideEntryCountViewer`

## Practical Conclusion

The unknown starts here are no longer free-floating. They are debug-menu presentation helpers adjacent to `WINDOW_TICK`: two fixed text printers, one fixed-width decimal formatter, one overlay snapshot/restore toggle, two window-tick variants, and a debug-menu selection dispatcher.
