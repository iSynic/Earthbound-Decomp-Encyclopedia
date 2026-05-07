# Open Menu Prelude Helpers (`C1:339E-C1:33B0`)

This note covers the three remaining unknown starts between the named `CHECK` routine and the named `OPEN_MENU_BUTTON` / `OPEN_MENU_BUTTON_CHECKTALK` includes in reference bank `01`.

The reference symbols name only the first two:

- `C1:339E` / `UNKNOWN_C1339E`
- `C1:33A7` / `UNKNOWN_C133A7`
- `C1:33B0`

## Main result

These routines are menu-entry preparation helpers.

Source-scaffold promotion:

- `C1:339E..33A7` is now decoded source in
  `src/c1/c1_339e_build_check_menu_entries_wrapper.asm`.
- `C1:33A7..33B0` is now decoded source in
  `src/c1/c1_33a7_build_open_menu_entries_wrapper.asm`.
- `C1:33B0..4103` is now decoded source in
  `src/c1/c1_33b0_rebuild_open_menu_text_entry_records.asm`.
- The promoted source validates through the durable C1 scaffold:
  `C1 byte-equivalence: OK, 172 module(s), 0 mismatch(es).`

## Working Names

- `C1:339E` = `BuildCheckMenuEntriesWrapper`
- `C1:33A7` = `BuildOpenMenuEntriesWrapper`
- `C1:33B0` = `RebuildOpenMenuTextEntryRecords`
- `C1:3CA1` = `OpenHpppDisplay`
- `C1:3CE5` = `ShowTownMap`
- `C1:3D03` = `RunDebugEventFlagToggleViewer`
- `C1:3E0E` = `RunDebugGuideEntryCountViewer`
- `C1:3E7A` = `RunDebugSetCharacterLevelPrompt`
- `C1:3EE7` = `RunDebugGoodsGrantViewer`

- `C1:339E` is a tiny wrapper around `C1:98DE` with `X = 2`.
- `C1:33A7` is the same wrapper with `X = $2C`.
- `C1:33B0` rebuilds the active menu text-entry records from debug/menu option tables and then refreshes the entry chain through `C1:163C`.

## Two Narrow Dispatch Wrappers

`C1:339E`:

```asm
REP #$31
LDX #$0002
JSR C1:98DE
RTL
```

`C1:33A7`:

```asm
REP #$31
LDX #$002C
JSR C1:98DE
RTL
```

`C1:98DE` is now source-backed as `RenderCharacterInventoryOrEquipmentRows` inside `src/c1/c1_9437_close_target_selection_prompt_label.asm`. It is the broader menu/text construction helper already seen from text command family `0x1A`. These two starts are therefore not independent systems; they are fixed-argument entry points into the existing menu builder.

## Menu Entry Record Builder

`C1:33B0` exits early if `$5E6C` is already nonzero, otherwise it walks menu selector values `1..6` and installs typed text-entry records with `C1:1596`.

For each selector it:

- skips selector `3` when `C1:C373` returns zero
- chooses a metadata byte of `1` for selectors `1`, `5`, and some selector-`2` cases, otherwise `$1B`
- uses selector - 1 as an index into `C3:E964`, which the reference data names `DEBUG_MENU_ELEMENT_SPACING_DATA`
- uses the same index into a ten-byte row table rooted at `EF:A37A`
- passes the derived source pointer, display byte, and type byte into `C1:1596`

The selector-`2` special case checks `$98A4` and `$986F`, then calls `C3:E977`. Existing notes now identify `$98A4` as the active party-member count and `$986F` as the active overworld entity-type source array, so this branch is likely deciding whether a party-dependent menu option gets the compact metadata byte.

The routine ends by clearing `$5E6C` and calling `C1:163C`, matching the active-entry-chain refresh path documented with the `$89D4` text-entry records.

## Why this belongs with Open Menu

The reference include order is the useful external corroboration:

```asm
.INCLUDE "overworld/check.asm"
.INCLUDE "unknown/C1/C1339E.asm"
.INCLUDE "unknown/C1/C133A7.asm"
.INCLUDE "unknown/C1/C133B0.asm"
.INCLUDE "overworld/open_menu.asm"
```

Mechanically, the code also matches that placement. It does not read controller state or run the open-menu state machine itself; it prepares the menu-visible records that the following open-menu routines consume.

## Adjacent Open Menu And Debug Tail Follow-Up (2026-05-06)

The adjacent `C1:34A7..4103` body now carries reference-backed labels for the
open-menu tail starts that were previously buried inside the large source unit:

- `OPEN_HPPP_DISPLAY` opens the HP/PP display shell, waits on `WINDOW_TICK`,
  enters `OPEN_MENU_BUTTON` on A/L, or closes HP/PP windows on B/Select.
- `SHOW_TOWN_MAP` checks for item `$00CA` through the party inventory wildcard
  helper before calling the C4 town-map display routine.
- `DEBUG_Y_BUTTON_FLAG` is the event-flag debug viewer. D-pad changes the flag
  id, A/L toggles the current flag through the C2 event-flag helpers, and
  B/Select closes the debug window.
- `DEBUG_Y_BUTTON_GUIDE` counts nonempty entity-script table entries and shows
  that count in the debug window.
- `DEBUG_SET_CHAR_LEVEL` prompts for a level and character, refreshes the
  character battle-state block, then restores HP/PP to 100 percent.
- `DEBUG_Y_BUTTON_GOODS` browses item ids, prints the item name, and on A/L can
  grant the selected item to a chosen character, including the equipment refresh
  path when the granted item is equippable.

## Open-Menu Helper-Call Polish Follow-Up (2026-05-06)

The same `C1:33B0..4103` source unit now names its evidence-backed
helper-call surface. The open-menu record rebuild, main selection loop, goods
and status branches, target prompts, inventory/equipment row renderers, HP/PP
focus helpers, party PSI/equipment/teleport branch calls, window cleanup, and
debug tail ticks now call through local symbolic contracts instead of raw
addresses. A follow-up closed the last four deferred edges by naming:

- the direct `C1:AF74` body entry as the item-use battle/field bridge body,
  immediately after the `C1:AF73` return stub.
- the two post-`C1:4070` `C1:03DC` fallback reads as text-command argument
  word reads.
- the final `C1:0FEA` text-command wrapper edge as the active-window
  tile-attribute setter, matching the `0x1C 00` local runtime note.

After this pass, the source unit has no raw `jsr/jsl $...` helper-call edges.

Validation after the helper-call pass:

```text
C1 byte-equivalence: OK, 172 module(s), 0 mismatch(es).
```

## Practical Conclusion

`C1:339E`, `C1:33A7`, and `C1:33B0` are now covered as open-menu prelude helpers: two fixed-argument calls into `C1:98DE`, plus a local menu-entry record rebuild over the debug/menu option tables. The adjacent `C1:34A7..4103` body is also source-backed now, tying those prepared records to the open-menu selection loop, the checking-object path at `C1:3C32`, and the small name-entry pointer helpers at `C1:4012`, `C1:4049`, and `C1:4070`.
