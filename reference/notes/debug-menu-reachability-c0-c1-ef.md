# Debug Menu Reachability `C0:B8A7 / C1:2E63 / EF:E4EC`

This note records the current reachability pass for the hidden/debug menu code.

See also [debug-menu-window-tick-helpers-c12bf3-c12d17.md](notes/debug-menu-window-tick-helpers-c12bf3-c12d17.md), [c3-e84e-debug-menu-and-embedded-item-helpers-split.md](notes/c3-e84e-debug-menu-and-embedded-item-helpers-split.md), and [bank-ef-first-pass.md](notes/bank-ef-first-pass.md).

## Main Result

The debug menu is real ROM code/data, not just a naming artifact.

The menu dispatcher at `C1:2E63` has two direct control-flow callers:

- `C0:B8A7 -> C1:2E63`
- `EF:E4EC -> C1:2E63`

The C0 caller is in the live overworld/main-loop region. The EF caller sits inside the late `EF:D56F..EB5E` debug/menu helper region identified by the ebsrc bank-`2f` include order.

## `DEBUG` Flag

The reference ebsrc RAM map names `$436C` as `DEBUG`.

Local reads of `$436C` line up with that:

- `C0:B741`, `C0:B778`, `C0:B892`, `C0:B92C`, and `C0:B97A` gate overworld/debug behavior on `$436C`.
- `C1:0177` is the text-halt worker's debug unlock chord gate.
- `C2:384F` is another battle-side read.
- ebsrc `src/battle/init_overworld.asm` explicitly checks `DEBUG` before calling `UNKNOWN_EFE708` and `DEBUG_CHECK_VIEW_CHARACTER_MODE`.

The only clean ROM-side absolute write found in this pass is:

- `C0:B9B4`: `STZ $436C`

That means the current evidence says retail code knows how to clear debug mode, and many paths know how to consume it, but this pass did not find a normal code path that sets it.

## C0 Menu-Open Chord

When `$436C != 0`, the C0 main loop opens the C1 debug menu through:

- `C0:B892`: `LDA $436C`
- `C0:B895`: branch away if zero
- `C0:B897`: test `$0065 & #$A000`
- `C0:B89F`: test `$006D & #$0010`
- `C0:B8A7`: `JSL $C12E63`

So the retail input gate is not just "press one button." It requires debug mode already enabled, a held-state mask from `$0065`, and a pressed-state mask from `$006D`.

The text halt/control worker has a second debug-only chord:

- `C1:0177`: reads `$436C`
- `C1:017E..0187`: checks `$006D & #$8010`
- if matched, it clears `$9645`, the text input lock flag

This is a debug assist path, not the menu opener itself.

## Menu Contents And Dispatch

The menu text is reference-backed in `refs/ebsrc-main/ebsrc-main/src/data/debug/menu_option_strings.asm`:

- `MOTHER2 ROM  1994/07/09  VERSION`
- `DEBUG MENU`
- `1 GAME`
- `2 VIEW MAP`
- `3 VIEW CHARACTER`
- `4 VIEW ATTRIBUTE`
- `5 SHOW BATTLE`
- `6 CHECK POSITION`
- `7 SOUND MODE`

`C1:2E63` builds menu entries from `C3:E874`, runs the shared C1 selection loop, and dispatches at least `0x17` menu results. The branch bodies call gameplay/debug helpers such as view-map/text pointers, battle setup, coffee/tea scene, name-entry prelude, town-map render, cast, Sound Stone, credits/photo, debug overlay toggle, and late EF debug helpers.

## Overworld Menu Button Follow-Up (2026-05-06)

The C0 main-loop button edges around `C0:B892..B91C` now use named C1
contracts:

- debug chord: `C0:B8A7 -> C1:2E63` / `DebugMenuSelectionDispatcher`
- menu button: `C0:B8E8 -> C1:34A7` / `RunOpenMenuSelectionLoop`
- HP/PP display button: `C0:B8FE -> C1:3CA1` / `OpenHpppDisplay`
- town-map button: `C0:B90C -> C1:3CE5` / `ShowTownMap`
- check/talk button: `C0:B91A -> C1:3C32` / `HandlePlayerCheckingObject`

## Current Interpretation

The healthiest current model is:

- the debug menu subsystem is present and source-backed across C1/C3/EF
- `$436C` is the master `DEBUG` flag
- if `$436C` is nonzero, the overworld loop can open `C1:2E63` through a controller chord
- this pass did not find a normal ROM-side setter for `$436C`
- therefore the menu currently looks retail-latent unless `DEBUG` is seeded externally, by an initialization path not yet identified, by a RAM patch, or by a build/debug harness

## Next Checks

- Identify all C0 readers of `$436C` semantically now that the ebsrc `DEBUG` label is confirmed.
- Trace `EF:E07C..E746` with the ebsrc debug helper include order, especially `DEBUG_MENU_LOAD`, cursor movement, command processing, and `DEBUG_CHECK_VIEW_CHARACTER_MODE`.
- Check whether boot, SRAM load, event scripts, or any debug/replay harness can seed `$436C` before `C0:B9B4` clears it.
