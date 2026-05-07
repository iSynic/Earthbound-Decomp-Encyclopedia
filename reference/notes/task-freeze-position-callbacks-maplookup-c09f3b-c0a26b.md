# Task freeze, position callbacks, and map lookup: C0:9F3B-C0:A26B

This note continues the C0 action-script/task seam past `C0:9ECE`. It uses the ebsrc bank00 symbol list and event macros as reference anchors, plus the legacy `Routine_Macros_EB.asm` labels for byte-level corroboration.

## Event-callable task flag wrappers

`C0:9F3B` and `C0:9F71` form a save/freeze/restore pair for active task records:

- `C0:9F3B` / `Freeze_AllActiveTasksExceptMarked`: clears `$1A44` to `#$FFFF`, snapshots all `$10B6[slot]` words into `$284C[slot]`, walks active task slots from `$0A50` through `$0A9E`, and ORs `#$C000` into `$10B6[slot]` for every slot except `$1A44`.
- `C0:9F43` / `Freeze_AllActiveTasksExceptA`: alternate entry that preserves the caller-provided `$1A44` value, then runs the same snapshot/freeze body.
- `C0:9F71` / `Restore_TaskFlagsFromFreezeSnapshot`: restores all `$10B6[slot]` words from `$284C[slot]`.

ebsrc exposes event macros for both `EVENT_UNKNOWN_C09F71` and `EVENT_UNKNOWN_C09F3B_ENTRY2`, which matches their shape as script/event-callable control wrappers.

## Random choice and fade wrappers

The next small entries are action-script helpers rather than normal direct-call routines:

- `C0:9F82` / `ChooseRandomScriptWord`: reads a choice count byte from `[$80],Y`, calls `C0:8E9A` and `C0:912C`, then selects one 16-bit word from the inline choice list. It updates `$94` to the byte after the list and returns the selected word. ebsrc gives this family the semantic symbol `CHOOSE_RANDOM`.
- `C0:9FA8`: calls `C0:8E9A` and returns the result with `XBA`; this looks like the compact random-byte sibling used by action scripts.
- `C0:9FAE`: reads a script word, preserves the post-operand script offset in `$94`, rearranges the word with `XBA/TAX/XBA`, then jumps to `C0:886C`.
- `C0:9FBB`: same operand wrapper, but jumps to `C0:887A`.

The ebsrc symbol order names the `C0:9FAE/C0:9FBB` area as `ACTIONSCRIPT_FADE_IN` / `ACTIONSCRIPT_FADE_OUT` plus extra entries, so the conservative local names are `ActionScript_FadeInWrapper` and `ActionScript_FadeOutWrapper` until the callee-side display state is fully named.

## Per-frame movement and position callbacks

`C0:9FC8-C0:A0BB` are small callback bodies that update entity position and screen-relative offsets:

- `C0:9FC8` / `Integrate_XYVelocityOnly`: for current task slot `$88`, adds fractional X velocity `$0DAA` into `$0C42`, carries into world X `$0B8E`, then adds fractional Y velocity `$0DE6` into `$0C7E` and carries into world Y `$0BCA`.
- `C0:9FF1` / `Integrate_XYAndZVelocity_WithSpriteRefresh`: calls `9FC8`, integrates fractional Z `$0E22` into `$0CBA` and world Z/height `$0C06`, then calls `C0:C7DB`.
- `C0:A00C` / `Integrate_XYAndZVelocity`: same as `9FF1`, without the `C0:C7DB` refresh call.
- `C0:A023` / `ProjectWorldToScreen_FromCamera31`: stores `$0B16 = $0B8E - $0031` and `$0B52 = $0BCA - $0033`.
- `C0:A03A`: same as `A023`, but subtracts `$0C06` from projected Y.
- `C0:A055`: projects from `$0039/$003B` instead of `$0031/$0033`.
- `C0:A06C`: subtracts `$0039/$003B` directly from world position, storing both world and projected X/Y fields.
- `C0:A089`: adds `$0039/$003B` directly into world X/Y.
- `C0:A0A0`: projects from `$0039/$003B` and subtracts `$0C06` from projected Y.
- `C0:A0BB` / `ProjectWorldToScreen_CopyWorld`: copies world X/Y into projected X/Y with no camera subtraction.

Most of these are reached indirectly through task callback pointers rather than normal JSR/JSL xrefs. `C0:A06C` is also exposed by ebsrc as `EVENT_UNKNOWN_C0A06C`, which explains the event-script use.

## Task data callback dispatcher

`C0:A0CA` and `C0:A0E3` are the local task data dispatch path:

- `C0:A0CA` / `Run_TaskDataCallbackByIndex`: builds a local direct page, doubles the incoming task index into `$88`, and calls `C0:A0E3`.
- `C0:A0E3` / `Run_CurrentTaskDataCallback`: rejects slots whose `$116A` is negative or overflow-marked, copies `$116A/$112E` into the long pointer `$8E:$8C`, rejects negative `$10F2`, then jumps through `$11E2[slot]`.
- `C0:A0FA` / `Draw_TaskDataRecordAtIndex`: uses the long data pointer `$8E:$8C` and an index in `A` to fetch a 16-bit record, mirrors `$103E[slot]` into `$2400`, loads projected position from `$0B8E/$0BCA`, and jumps to the display enqueue helper `C0:8C58`.

This makes the earlier script opcode installers at `C0:9B4D`, `C0:9BE4`, and `C0:9BEE` concrete: they install the data pointer and callback consumed here.

## Cached map/property lookup

`C0:A152` is a far wrapper around `C0:A156`; direct callers also include `C0:0B8C` and `C0:0C9C`.

`C0:A156` / `Lookup_CachedMapPropertyNibble` takes `A` and `X` as lookup coordinates/selectors. It:

- rejects negative combined inputs by returning `#$FFFF`
- returns cached `$288C` when `$2888/$288A` match the incoming pair
- derives an index from `A` and bits of `X`
- reads from D7 map/property data rooted at either `$D7:5000` or `$D7:8000`
- dispatches through `C0:A1AE` to one of four shift entries at `C0:A1CE/C0:A1D0/C0:A1D2/C0:A1D4`
- masks the selected two-bit value, combines it with a high-byte fragment in `$08`, caches it in `$288C`, and returns it

`C0:A1AE` is therefore a data table of four-byte jump entries, not linear code. `C0:A1CE`, `C0:A1D0`, `C0:A1D2`, and `C0:A1D4` are staggered shift entries that select one packed two-bit field.

## Nearby task/map helpers

The next few starts belong to the same broad task and map-support band:

- `C0:A1F2` / `Copy_MapBufferPageToWorkBuffer`: indexes a source pointer table at `C0:A20C`, copies a block within WRAM bank `$7E` to `$0240` using `MVN`, then sets transfer flag `$0030 = #$08`.
- `C0:A20C`: WRAM source pointer table for `A1F2`, with entries in the `$B800-$BD40` range.
- `C0:A21C` / `FindActiveTaskByField2C9A`: direct caller `C0:2317`; walks active task slots and returns success by preserving `A` when `$2C9A[slot] == A`, otherwise returns `0`.
- `C0:A230`: adds the position/fractional fields of a linked slot selected through `$0E5E[X]` into the current slot's projected offsets. This is likely a child/attached-entity position helper.
- `C0:A254`: direct caller `C0:3A14`; doubles slot index `A`, then projects that slot's world X/Y from camera `$0031/$0033`.
- `C0:A26B`: physics callback reached from `C0:89F1` and widely installed by `EVENT_SET_PHYSICS_CALLBACK`. It checks current slot `$88` against active target fields `$5D76/$5D78`, skips special states, runs one of the comparison helpers through the table at `C0:A350`, and falls back to `A023`-style camera projection.

`C0:A2AB` and `C0:A30B` are small distance threshold tables used by the comparison helpers at `C0:A2B7`, `C0:A2E1`, and following entries.

## Working Names

- `C0:9F3B` = `Freeze_AllActiveTasksExceptMarked`
- `C0:9F43` = `Freeze_AllActiveTasksExceptA`
- `C0:9F71` = `Restore_TaskFlagsFromFreezeSnapshot`
- `C0:9F82` = `ChooseRandomScriptWord`
- `C0:9FA8` = `ChooseRandomScriptByte`
- `C0:9FAE` = `ActionScript_FadeInWrapper`
- `C0:9FBB` = `ActionScript_FadeOutWrapper`
- `C0:9FC8` = `Integrate_XYVelocityOnly`
- `C0:9FF1` = `Integrate_XYAndZVelocity_WithSpriteRefresh`
- `C0:A00C` = `Integrate_XYAndZVelocity`
- `C0:A023` = `ProjectWorldToScreen_FromCamera31`
- `C0:A03A` = `ProjectWorldToScreen_FromCamera31AndHeight`
- `C0:A055` = `ProjectWorldToScreen_FromCamera39`
- `C0:A06C` = `ProjectWorldToScreen_DirectCamera39Event`
- `C0:A089` = `AddCamera39ToWorldPosition`
- `C0:A0A0` = `ProjectWorldToScreen_FromCamera39AndHeight`
- `C0:A0BB` = `ProjectWorldToScreen_CopyWorld`
- `C0:A0CA` = `Run_TaskDataCallbackByIndex`
- `C0:A0E3` = `Run_CurrentTaskDataCallback`
- `C0:A0FA` = `Draw_TaskDataRecordAtIndex`
- `C0:A152` = `Lookup_CachedMapPropertyNibble_Far`
- `C0:A156` = `Lookup_CachedMapPropertyNibble`
- `C0:A1AE` = `CachedMapPropertyShiftDispatchTable`
- `C0:A1CE` = `SelectPackedMapPropertyBits0`
- `C0:A1D0` = `SelectPackedMapPropertyBits1`
- `C0:A1D2` = `SelectPackedMapPropertyBits2`
- `C0:A1D4` = `SelectPackedMapPropertyBits3`
- `C0:A1F2` = `Copy_MapBufferPageToWorkBuffer`
- `C0:A20C` = `MapBufferPageSourcePointerTable`
- `C0:A21C` = `FindActiveTaskByField2C9A`
- `C0:A230` = `AddLinkedSlotPositionToCurrentProjection`
- `C0:A254` = `ProjectSlotWorldPositionFromCamera31`
- `C0:A26B` = `PhysicsCallback_TargetComparisonAndProjection`
- `C0:A2AB` = `PhysicsCallbackDistanceThresholdTableA`
- `C0:A30B` = `PhysicsCallbackDistanceThresholdTableB`
