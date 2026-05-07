# Battle Text Entry Family `C1:DC1C .. DD7C`

This note captures the current best local model for the small bank-`01` battle-text entry and redirect family centered on `C1:DC1C`.

See also [class2-battle-text-dispatch-stack.md](notes/class2-battle-text-dispatch-stack.md).
See also [class2-concrete-battle-text-call-paths.md](notes/class2-concrete-battle-text-call-paths.md).
See also [class2-enemy-text-pointer-consumers.md](notes/class2-enemy-text-pointer-consumers.md).
See also [class2-dispatch-family.md](notes/class2-dispatch-family.md).
See also [battle-text-entry-tail-dd82-dd9f.md](notes/battle-text-entry-tail-dd82-dd9f.md).
See also [battle-text-context-buffer-family-c1ac4a-ad42.md](notes/battle-text-context-buffer-family-c1ac4a-ad42.md).

## Main result

The local `C1:DC1C .. DD7C` region now reads more cleanly as a small battle-text entry family, not just one anonymous pointer sink plus unrelated neighbors.

## Working Names

- `C1:DC1C` = `DisplayBattleTextFromPointer`
- `C1:DC66` = `DisplayBattleTextWithSubstitutionPayload`
- `C1:DCCB` = `InitializePartyBattleStartState`
- `C1:DD3B` = `RedirectShowHpppWindows`
- `C1:DD41` = `RedirectHideHpppWindows`
- `C1:DD47` = `RedirectCreateWindow`
- `C1:DD4D` = `RedirectSetWindowFocus`
- `C1:DD53` = `RedirectTextEntryHelper0FA3`
- `C1:DD59` = `RedirectCloseFocusWindow`
- `C1:DD5F` = `BattleDisplayCloseAndSyncWait`
- `C1:DD70` = `RedirectBuildBattleAttackerNameBuffer`
- `C1:DD76` = `RedirectBuildBattleTargetNameBuffer`
- `C1:DD7C` = `RedirectStageBattleTextSubstitutionByte`

The strongest current split is:

- `C1:DC1C`
  - main one-pointer battle-text display wrapper over `C1:86B1`
- `C1:DC66`
  - companion battle-text display wrapper with committed substitution payload, best named locally as `DISPLAY_IN_BATTLE_TEXT_WITH_SUBSTITUTION_PAYLOAD`, and now promoted as the best final match for reference `DISPLAY_TEXT_WAIT`
- `C1:DCCB`
  - battle-start party-state initializer, best named locally as `INITIALIZE_PARTY_BATTLE_START_STATE`
- `C1:DD3B .. DD53`
  - short redirect/helper strip that lines up well with the `ebsrc` include ordering for battle-text-adjacent window helpers
- `C1:DD5F`
  - battle-display close-and-sync wait wrapper, best named locally as `BATTLE_DISPLAY_CLOSE_AND_SYNC_WAIT`
- `C1:DD70 / DD76 / DD7C`
  - local battle-text context refresh redirects to `C1:AC4A / ACA1 / ACF8`

The `C1:DC1C..DD3B` display-wrapper and battle-start initializer strip is now source-backed in the C1 scaffold.

That makes the surrounding `class2` battle-text notes much healthier: we are no longer relying on `C1:DC1C` alone to carry the whole family.

Source polish: `src/c1/c1_dc1c_display_battle_text_from_pointer.asm` and
`src/c1/c1_dc66_display_battle_text_with_substitution_payload.asm` now name
the caller-frame pointer slots, `$98B1/$0065` battle-text gate, `$9643` mode
latch, prompt-wait mode value, primary text pointer pair, and secondary
substitution payload pair used by these wrappers.

Implementation update: the wrapper sources now also name the shared
caller-frame alias offset and processor-width masks directly. `C1:DC1C` is
called out as the one-pointer display lane with no secondary payload commit,
while `C1:DC66` is called out as the primary-script plus `$9D12/$9D14`
payload lane whose EF consumers include `1C 0F` amount text and `19 1E`
pointer substitution.

Adjacent-tail update: `src/c1/c1_dd9f_display_current_action_table_text_mode1.asm`
now carries the neighboring battle selection/equipment tail with named
action-table pointer offsets, selected-row fields, C7 equip text scripts, and
inventory/equipment/stat-refresh helper calls. That keeps the `DD82..DD9F`
tail tied to the same battle-text ABI family without folding its equipment
side effects into the simpler `DC1C/DC66/DD7C` display contracts.

## `C1:DC1C` as the main one-pointer battle-text wrapper

The strongest locally proved behavior of `C1:DC1C` is:

- copies caller pointer pair from stack-frame args into local `$06/$08`
- applies the same `98B1` / `$0065 bit 15` gate used by nearby battle-text entries
- stages `$06/$08` into `$0E/$10`
- calls `C1:86B1`
- finishes through the small `JSR $003C` tail

That keeps the existing safest wording intact:

- `C1:DC1C` is a very strong local fit for the main battle-text display wrapper
- it consumes a far pointer through `$0E/$10`
- it feeds the generic textbox processor rooted at `C1:86B1`

This is still slightly cautious locally, but it is now stronger as part of a family rather than as a standalone guess.

## `C1:DC66` as a companion display wrapper with committed substitution payload

`C1:DC66` is clearly not just a byte-shifted copy of `C1:DC1C`.

The strongest locally proved behavior is:

- reads one caller pair into local `$06/$08`
- reads a second caller pair into local `$0A/$0C`
- first stages `$06/$08` through `C1:AD0A`, which stores that secondary payload into stable words `$9D12/$9D14`
- then reloads `$0A/$0C` as the primary display pointer
- then runs the same `C1:86B1` display path and `JSR $003C` tail as `C1:DC1C`

The newer caller and text-side bridge make that secondary input healthier than before. The staged `$9D12/$9D14` pair is read back by `C1:AD26`, and `C1:AD26` is exactly the helper used by bank-`01` text command `0x1C 0F`, our current best local fit for `PRINT_ACTION_AMOUNT`. The `DC66` caller families repeatedly point at `EF:` battle strings that use `0x1C 0F` in the visible text body, especially HP and PP loss or gain messages, poison or dizziness damage text, and the offense or defense change messages around `EF:69BA / 69D2`, `EF:75AB / 75C2 / 75D9 / 75F0`, and `EF:7755 / 7768 / 7787 / 77B1 / 77DB`.

That makes the safest local read stronger:

- `C1:DC66` is a companion battle-text display wrapper that commits a secondary numeric or substitution payload through `C1:AD0A -> $9D12/$9D14`
- the primary text pointer is then reloaded from the other argument pair and dispatched through the same `C1:86B1` path as `C1:DC1C`
- this is the strongest current local bridge between the `class2` battle-text wrappers and the `0x1C 0F` amount-printing path
- the best current local symbolic identity is therefore `DISPLAY_IN_BATTLE_TEXT_WITH_SUBSTITUTION_PAYLOAD`

I am now comfortable promoting the reference-side counterpart for `C1:DC66`. `ebsrc` battle-action routines like `reduce_pp.asm` and `offense_up_alpha.asm` call `DISPLAY_TEXT_WAIT` exactly in the pattern our local ROM uses `DC66` for, staging a text pointer plus an amount-like payload before dispatch. The local callers around `C2:5915`, `C2:5FE0`, and `C2:8E98` show the same shape and then continue ordinary control flow without bolting on a manual display-wait loop afterward. So the healthiest final mapping is:

- local behavioral name: `DISPLAY_IN_BATTLE_TEXT_WITH_SUBSTITUTION_PAYLOAD`
- best final reference/export match: `DISPLAY_TEXT_WAIT`

## Concrete caller patterns for `C1:DC66`

The local callers now show a broader and cleaner pattern than the earlier note captured.

At `C2:5915 / 593B / 5961 / 5987`:

- the caller stages a far text pointer like `EF:7768`, `EF:7787`, `EF:77B1`, or `EF:77DB`
- it also stages a small numeric pair derived from `C2:6AFD`
- then it calls `C1:DC66`

At `C2:5FE0 / 5FF8`, `C2:7302 / 7391`, `C2:802F / 8051 / 80B3 / 80DC / 8106`, and `C2:8E98 / 8F1B / 8F5F / 8F91`:

- the caller again stages an `EF:` battle message pointer as the primary text
- it computes a small signed or unsigned amount-like value into the secondary input slots
- then it calls `C1:DC66`

These primary texts are not random. They repeatedly use the bank-`01` amount-printing path through `0x1C 0F`, which is the same substitution slot family backed by `C1:AD26 -> $9D12/$9D14`.

So the best current summary is:

- `C1:DC66` is used where battle text needs both an immediate display pointer and an additional committed substitution payload
- in the currently pinned caller families, that payload is most often an amount or delta later consumed by `0x1C 0F`

## `C1:DD3B .. DD5F` as the nearby redirect/helper strip

The local wrapper strip immediately after `C1:DCCB` is now cleaner when read beside the `ebsrc` bank-`01` include order.

Locally we have:

- `C1:DD3B` -> `JSR $0A04`
- `C1:DD41` -> `JSR $0A1D`
- `C1:DD47` -> `JSR $04EE`
- `C1:DD4D` -> `JSR $007E`
- `C1:DD53` -> `JSR $0FA3`
- `C1:DD59` -> `JSR $0084`
- `C1:DD5F` -> `JSR $008E`, `JSL C12DD5`, `JSR $0A1D`, `JSL C12DD5`

Source-scaffold promotion:

- `C1:DD3B..DD5F` and `C1:DD70..DD82` have started moving from
  byte-preserved corridors into real decoded source modules.
- `src/c1/c1_dd3b_redirect_show_hppp_windows.asm` through
  `src/c1/c1_dd59_redirect_close_focus_window.asm` now assemble as source
  segments in `build/c1-build-candidate-ranges.json`.
- `src/c1/c1_dd70_redirect_build_battle_attacker_name_buffer.asm` through
  `src/c1/c1_dd7c_redirect_stage_battle_text_substitution_byte.asm` now do the
  same for the context-refresh redirect trio.
- The callee-side context helpers at `C1:AC4A..AD42` are also source-promoted
  through `src/c1/c1_ad26_load_battle_text_substitution_pointer.asm`, so the
  wrappers now point at decoded local source rather than only named byte
  corridors.
- Validation remains clean: `C1 byte-equivalence: OK, 172 module(s), 0
  mismatch(es).`

Reference-backed ordering clue from `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank01.asm` and `include/symbols/bank01.inc.asm`:

- `DISPLAY_IN_BATTLE_TEXT`
- `DISPLAY_IN_BATTLE_TEXT_NO_PROMPT`
- `DISPLAY_TEXT_WAIT`
- `UNKNOWN_C1DCCB`
- `REDIRECT_SHOW_HPPP_WINDOWS`
- `REDIRECT_HIDE_HPPP_WINDOWS`
- `REDIRECT_CREATE_WINDOW`
- `REDIRECT_SET_WINDOW_FOCUS`
- `REDIRECT_C10FA3`
- `UNKNOWN_C1DD5F`
- `REDIRECT_C1AC4A`
- `REDIRECT_C1ACA1`
- `REDIRECT_C1ACF8`

That is not byte-for-byte local proof, but it is a strong reference-backed fit for the local strip:

- `DD3B .. DD53` are very likely the short redirect helpers exported immediately after `UNKNOWN_C1DCCB`
- `DD5F` is very likely the surviving unknown helper in that strip

## `C1:DD70 / DD76 / DD7C` as battle-text context refresh redirects

This part is now one of the cleaner pieces of the family.

Locally:

- `C1:DD70` -> `JSR C1:AC4A`
- `C1:DD76` -> `JSR C1:ACA1`
- `C1:DD7C` -> `JSR C1:ACF8`

Reference-backed ordering matches exactly here, because the `ebsrc` symbol strip exports:

- `REDIRECT_C1AC4A`
- `REDIRECT_C1ACA1`
- `REDIRECT_C1ACF8`

immediately after `UNKNOWN_C1DD5F`.

That makes the surrounding `class2` battle-text bridges much healthier:

- `C2:3BCF -> C1:DD70`
- `C2:3D05 -> C1:DD76`
- then `C1:DC1C` for the actual display dispatch

## `C1:DCCB` as a party-side battle-state priming helper

`C1:DCCB` no longer looks best as another battle-text entry.

Its only currently pinned direct caller is still `C2:4A7B`, but the local body is now much cleaner:

- begins with `JSL C2:00D9`, which clears and seeds a broad battle-local state block
- sets `9643 = 1`
- iterates `A = 1..4`
- for each party member, calls `C1:D8D0`
- then runs the HP and PP recover-side workers `C1:8F64` and `C1:9010` with `X = #$0064`
- copies the paired HP/PP-side words at `$9A15/$9A1B` into the active-marker words at `$9A13/$9A19`
- exports an 8-byte block rooted at `$99DC + Y` through `JSL C08EFC`

That makes the safest current local read stronger:

- `C1:DCCB` is used only from the early `main_battle_routine` start path at local `C2:4A7B` and reference-side `main_battle_routine.asm` line 345
- it begins by calling `C2:00D9`, which clears and seeds a broad battle-local display/state block
- it then iterates party members `1..4`, refreshes character-side battle records through `C1:D8D0`, applies fixed HP and PP side workers, mirrors the paired HP/PP values into active marker fields, and exports an 8-byte block through `C08EFC`
- downstream readers now make that exported block healthier: the leading byte at `$99DC + X` is treated as a small enumerated selector/state byte, with values `1` and `2` repeatedly grouped together and other values treated as the active/default side
- that aligns better with the broader model in [class2-dispatch-family.md](notes/class2-dispatch-family.md), which already treats `$99DC` as a per-slot selector/state family rather than a battle-only field
- the best current local symbolic identity is therefore `INITIALIZE_PARTY_BATTLE_START_STATE`

So this helper now reads less like a generic priming routine and more like the dedicated party-side battle-start initializer that prepares live party combat/display state before the main per-party loop begins, including a reused `$99DC` selector/state byte even if the exact enum labels are still not pinned.

## `C1:DD5F` as a shared wait-and-sync helper

`C1:DD5F` also now looks more specific than a generic unknown.

The local body is:

- `JSR C1:008E`
- `JSL C12DD5`
- `JSR C1:0A1D`
- `JSL C12DD5`

The called helpers make that more concrete:

- `C1:008E` sets `$5E70`, walks the `$88E2/$8654` family through `C3:E521`, then runs `C3:E4CA`, `C12DD5`, clears `$5E70`, and finishes through `C43F53`
- `C1:0A1D` is the already-mapped battle-text-adjacent window and HP/PP sync helper
- `C12DD5` is the shared wait or display-state progress helper used all over bank `01`

The caller set is still small and distinctive:

- `C2:617D`
- `C2:652D`
- `C2:C3A4`
- `C2:C449`
- `C4:C669`

That makes the safest current wording stronger:

- `C1:DD5F` wraps the same close/reset/sync core as text command `0x18 04`, because `C1:7976` is exactly `JSR C1:008E`, `JSR C1:0A1D`, and `JSL C12DD5`, while `DD5F` adds one extra `C12DD5` before and after the `0A1D` sync step
- the small caller set uses it around battle or display-state transitions, not as a generic textbox entry
- the best current local symbolic identity is therefore `BATTLE_DISPLAY_CLOSE_AND_SYNC_WAIT`

I am intentionally not collapsing that into the reference export `DISPLAY_TEXT_WAIT`. The reference ordering around this strip is not reliable enough to force the mapping, and the locally proved body is richer than a plain one-stage wait helper. So the healthier state is: `DD5F` now has a strong local symbolic name, while the exact reference-export correspondence stays open.

## Best current interpretation

The safest current family model is:

- `C1:DC1C` = strong local fit for the main battle-text display wrapper
- `C1:DC66` = strong local fit for a companion battle-text display wrapper with committed substitution payload, especially amount-like payloads later read through `0x1C 0F`
- `C1:DCCB` = `INITIALIZE_PARTY_BATTLE_START_STATE`, the party-side battle-start initializer
- `C1:DD3B .. DD53` = likely short battle-text-adjacent redirect strip
- `C1:DD5F` = `BATTLE_DISPLAY_CLOSE_AND_SYNC_WAIT`, a battle-display close/reset/sync wrapper with extra waits, and no longer a good `DISPLAY_TEXT_WAIT` fit
- `C1:DD70 / DD76 / DD7C` = locally proved redirects into the battle-text context refresh helpers at `AC4A / ACA1 / ACF8`, where `AC4A` and `ACA1` now read as counted-copy builders for the live attacker/target name buffers and `ACF8` remains the one-byte substitution-slot setter

## What is still open

- the exact user-facing meaning of the reused `$99DC` selector/state values, especially `1` versus `2`
- whether the promoted `DISPLAY_TEXT_WAIT -> C1:DC66` mapping should eventually replace the local helper-style name in summaries
- whether either surviving unknown in the `ebsrc` include ordering can be matched to these bodies more concretely from caller-side behavior


