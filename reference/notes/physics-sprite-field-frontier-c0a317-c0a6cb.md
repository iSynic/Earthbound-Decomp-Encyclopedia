# Physics, sprite refresh, and field accessors: C0:A317-C0:A6CB

This note clears the next C0 audit strip after the map/property lookup. The strongest corroboration is the legacy `Routine_Macros_EB.asm` layout around `DATA_C0A2AB`, `DATA_C0A30B`, `DATA_C0A350`, the `C0:A3A4` renderer callback, and the ebsrc event macros for the `A6xx` field helpers.

## Distance comparison callbacks

`C0:A26B` dispatches through `DATA_C0A350` using `$2AF6[current]` when the current slot is in the target context from `$5D76/$5D78`. The table fans into three local comparison routines:

- `C0:A2B7`: compares projected X equality first, then absolute projected Y distance against `DATA_C0A2AB`.
- `C0:A2E1`: compares projected Y equality first, then absolute projected X distance against `DATA_C0A2AB`.
- `C0:A317`: computes absolute world-X distance from target `Y`; if it is at least the threshold from `DATA_C0A30B`, it compares the Y delta against the X delta and returns a signed/normalized difference-ish result.

Data tables:

- `C0:A2AB`: thresholds `0000, 0011, 0020, 002F, 003E, 004D`.
- `C0:A30B`: thresholds `0000, 000B, 0016, 0020, 002B, 0036`.
- `C0:A350`: callback table selecting `A2B7`, `A317`, or `A2E1` depending on the current `$2AF6` class.

## Collision-gated position refresh

`C0:A360` and `C0:A384` are near-twins used as per-frame callbacks after the comparison layer:

- `C0:A360`: if `$2C5E[current]` is negative, or there is no cached neighbor in `$289E[current]`, it integrates position via `C0:9FCA`, calls `C0:C7DB`, and returns. If `$28DA[current] & #$00D0` is nonzero, it jumps into `C0:98F2`.
- `C0:A37A`: entry that reloads current slot in `X` and joins the `A360` refresh tail.
- `C0:A384`: same gating structure, but the refresh tail only runs `C0:9FCA`; it does not call `C0:C7DB`.
- `C0:A39E`: entry that reloads current slot in `X` and joins the `A384` refresh tail.

So the safe local names are `UpdatePosition_WhenNoNeighbor_WithSpriteRefresh` for `A360` and `UpdatePosition_WhenNoNeighbor` for `A384`.

## Sprite/display callback

`C0:A3A4` is a display callback body reached through task setup rather than a direct call. It:

- adjusts the data pointer `$8C` by `$2916[current]` when `$341A[current] & 1` is set
- rewrites packed bytes through `[$8C],Y`, using bits in `$2BAA[current]` plus counts from `$2BE7/$2BE6`
- mirrors `$103E[current]` into `$2400`, with an indirection path when bit `#$8000` is set
- calls `C0:AC43`
- jumps into display enqueue helper `C0:8C58` with projected position `$0B16/$0B52`

This anchors the earlier data-pointer dispatcher note: task data callbacks are not just logic hooks; some are display record builders.

## Profile/sprite refresh family

The `C0:A443-C0:A56E` family updates which sprite/profile data should be drawn for a slot and then streams entries through `C0:A56E`:

- `C0:A443`: combines phase bit from `$2890 + $1A42`, direction/class `$2AF6`, and state `$2C22`; if the composite key differs from `$3456[current]`, it stores the new key and refreshes through `C0:A4C2`.
- `C0:A48F`: explicit slot-index wrapper; reads `$10F2[index]` into `$2892` and calls `C0:A4C4`.
- `C0:A4A8`: sets `$2892=0`, probes `C0:C711`, and refreshes only when that probe succeeds.
- `C0:A4B2`: sets `$2892=1`, probes `C0:C711`, and refreshes only when that probe succeeds.
- `C0:A4BF`: clears `$2892` and joins the refresh body.
- `C0:A4C4`: shared refresh body; builds data pointers from `$2ABA/$2A7E/$298E/$2A06/$29CA`, adjusts by direction table `C0:A60B`, checks control bits, and repeatedly calls `C0:A56E`.
- `C0:A56E`: transfer/chunk helper already tied to the display assembly notes; it calls `C0:8643` and advances `$0097/$0092` across page boundaries.
- `C0:A60B` and `C0:A623`: direction/profile offset tables used by the refresh code.

## Event-callable field accessors

The `A6xx` strip is a compact set of action/event helpers around current slot `$88`:

- `C0:A643`: reads a 16-bit script parameter, writes direction/class through `C0:A65F`, then stores the returned value in `$2C9A[current]`.
- `C0:A651`: reads an 8-bit script parameter, writes through `C0:A65F`, then stores the returned value in `$1A86[current]`.
- `C0:A65F`: if `$2C5E[current]` is nonnegative, stores `A` into `$2AF6[current]`; always returns the incoming value.
- `C0:A66D`: direct setter for `$2AF6[current]`.
- `C0:A673`: getter for `$2AF6[current]`; ebsrc exposes this as `EVENT_UNKNOWN_C0A673`.
- `C0:A679`: reads an 8-bit script parameter into `$2BAA[current]`.
- `C0:A685`: reads a 16-bit script parameter into `$2B32[current]`.
- `C0:A691`: getter for `$2B32[current]`; ebsrc exposes this as `EVENT_UNKNOWN_C0A691`.
- `C0:A697`: reads an 8-bit script parameter and calls `C0:C83B`.
- `C0:A6A2`: reads a 16-bit script parameter and calls `C0:CA4E`; ebsrc exposes a macro that passes one word argument.
- `C0:A6AD`: reads a 16-bit script parameter and calls `C0:CBD3`; ebsrc exposes a macro that passes one word argument.
- `C0:A6B8`: returns `#$FFFF` if `$289E[current]` is nonnegative, otherwise `0`; exposed as `EVENT_UNKNOWN_C0A6B8`.
- `C0:A6C5`: getter for `$28DA[current]`.
- `C0:A6CB`: getter for `$2C5E[current]`.

These field helpers explain why many event scripts use opaque `EVENT_UNKNOWN_C0A...` macros: most are simple accessors or wrappers around current-slot state, not large gameplay routines.

## Working Names

- `C0:A26B` = `PhysicsCallback_TargetComparisonAndProjection`
- `C0:A2AB` = `PhysicsCallbackDistanceThresholdTableA`
- `C0:A2B7` = `CompareProjectedXThenYDistanceThreshold`
- `C0:A2E1` = `CompareProjectedYThenXDistanceThreshold`
- `C0:A30B` = `PhysicsCallbackDistanceThresholdTableB`
- `C0:A317` = `CompareWorldXDistanceAndNormalizeDelta`
- `C0:A350` = `PhysicsCallbackComparisonDispatchTable`
- `C0:A360` = `UpdatePosition_WhenNoNeighbor_WithSpriteRefresh`
- `C0:A37A` = `UpdatePosition_WhenNoNeighbor_WithSpriteRefresh_CurrentSlot`
- `C0:A384` = `UpdatePosition_WhenNoNeighbor`
- `C0:A39E` = `UpdatePosition_WhenNoNeighbor_CurrentSlot`
- `C0:A3A4` = `Build_DisplayRecordFromCurrentTaskData`
- `C0:A443` = `RefreshCurrentSlotProfileIfCompositeKeyChanged`
- `C0:A48F` = `RefreshSlotVisualProfileByIndex`
- `C0:A4A8` = `RefreshCurrentSlotVisualProfile_Mode0IfAligned`
- `C0:A4B2` = `RefreshCurrentSlotVisualProfile_Mode1IfAligned`
- `C0:A4BF` = `RefreshCurrentSlotVisualProfile_Mode0`
- `C0:A4C4` = `RefreshSlotVisualProfileShared`
- `C0:A56E` = `Generate_RenderDmaStripDescriptors`
- `C0:A60B` = `VisualProfileDirectionOffsetTable`
- `C0:A623` = `VisualProfileSecondaryOffsetTable`
- `C0:A643` = `Script_SetDirectionClassAndField2C9A`
- `C0:A651` = `Script_SetDirectionClassAndField1A86`
- `C0:A65F` = `SetCurrentSlotDirectionClassIfActive`
- `C0:A66D` = `SetCurrentSlotDirectionClass`
- `C0:A673` = `GetCurrentSlotDirectionClass`
- `C0:A679` = `Script_SetCurrentSlotDisplayControlBits`
- `C0:A685` = `Script_SetCurrentSlotField2B32`
- `C0:A68B` = `StoreAInCurrentSlotField2B32`
- `C0:A691` = `GetCurrentSlotField2B32`
- `C0:A697` = `Script_SetMovementStateC83B`
- `C0:A6A2` = `Script_SetMovementStateCA4E`
- `C0:A6AD` = `Script_SetMovementStateCBD3`
- `C0:A6B8` = `GetCurrentSlotHasNoCachedNeighborFlag`
- `C0:A6C5` = `GetCurrentSlotCollisionFlags28DA`
- `C0:A6CB` = `GetCurrentSlotActivityState2C5E`
