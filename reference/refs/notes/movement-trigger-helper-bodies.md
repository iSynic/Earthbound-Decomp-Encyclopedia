# Movement Trigger Helper Bodies

This note captures the current ROM-first interpretation of the helper routines dispatched by `C0:7526`.

## Dispatch map recap

- type `0` -> `MovementTriggerType0_QueueDoorDestination` at `C0:6A1B`
- type `1` -> `MovementTriggerType1_SetState07Or08` at `C0:6A91`
- type `2` -> `MovementTriggerType2_QueueDoorTransition` at `C0:6ACA`
- type `3` -> `MovementTriggerType3_QueueOffsetStep` at `C0:6E6E`
- type `4` -> `Queue_StagedMovementFromGridCoords` at `C0:70CB`
- types `5` and `7` -> `MovementTriggerType5Or7_NoOp` at `C0:6A8B`
- type `6` -> `MovementTriggerType6_NoOp` at `C0:6A8E`

## Type `0` `C0:6A1B`

What the ROM clearly shows:

- Treats the incoming parameter as an offset into a bank `CF` table.
- Reads the first word from that table, masks off bit 15, and passes it to `JSL $C21628`.
- Compares the return value against whether the original table word had bit 15 set.
- On match, reads the next long-like pointer from the same table entry and enqueues it through `C0:64E3` as queue type `0`.
- Clears `$5DAA` and `$5DA8` after the enqueue.

A narrow legacy cross-check names that bank `CF` table `EB_DoorDestinationTable`. That name is still borrowed, but it fits this helper and the related queue consumers well.

Working interpretation:

- type `0` is a door-destination-style queue helper gated by one side-or-orientation bit.

## Type `1` `C0:6A91`

What the ROM clearly shows:

- If `$9883` is already `#$0007` or `#$0008`, the helper returns immediately.
- Otherwise it writes `#$0007` when the input parameter is zero, or `#$0008` when the input parameter is nonzero.
- It then clears bit 0 of `$987F` and resets `$5DC4` to `#$FFFF`.

Working interpretation:

- type `1` is a small state switcher for two special movement states rather than a queued movement setup.
- `#$0007` and `#$0008` are strong candidates for two paired movement modes, but their gameplay labels are not proven yet.

## Type `2` `C0:6ACA`

What the ROM clearly shows:

- Bails out unless `$0A34` is nonzero.
- Also requires `$98A5 != #$0002`, `$5D9A == 0`, and `($4DBA | $5D60) == 0`.
- Uses the same bank `CF` table family as type `0`.
- Sets `$5DC2 = #$0001`, enqueues the resolved pointer through `C0:64E3` as queue type `2`, and immediately calls `C0:7C5B`.

Working interpretation:

- type `2` is another door-destination-style helper, but one that only fires when the movement queue is empty and the engine is idle enough to accept a transition.

## Type `3` `C0:6E6E`

What the ROM clearly shows:

- Rejects the request if `$0081` is nonzero.
- Uses three tiny local table families rooted at `C0:6E02`, `C0:6E0A`, and `C0:6E12`.
- The low path stores the incoming selector in `$5DC6`, writes a facing-like value from `C0:6E12` into `$987F`, sets `$5D56 = #$0003` and `$5DBA = #$0001`, computes a staged coordinate through `C48D58`, queues callback `C0:6E2C`, and stores the target X/Y in `$5DD0/$5DD2`.
- The high-bit path only proceeds when `$9883 == #$000C`; it clears `$9883`, keeps `$5D56 = #$0003`, uses `$5DC6` plus the `C0:6E0A/C0:6E12` tables, queues callback `C0:6E4A`, then stores the target X/Y in `$5DD0/$5DD2`.
- In both cases the queued callback delay is derived through `C48D58`, and completion cleanup goes through `C48E95`.

The local tables currently decode as:

- `C0:6E02` -> `$0008, $0000, $0000, $0008`
- `C0:6E0A` -> `$0000, $0008, $0000, $0008`
- `C0:6E12` -> `$0006, $0002, $0006, $0002`

Working interpretation:

- type `3` is an offset-step helper that stages a small coordinate move and resolves it through the delayed-action timer path.
- The exact gameplay meaning is still open, but this now looks like a specialized movement interaction rather than a generic script hook.

## Types `5`, `6`, and `7`

What the ROM clearly shows in the `C0:7526` dispatcher path:

- type `5` and type `7` both land in `C0:6A8B`, which is just `REP #$31` followed by `RTS`.
- type `6` lands in `C0:6A8E`, which is also just `REP #$31` followed by `RTS`.

Working interpretation:

- In this dispatcher path, types `5`, `6`, and `7` are currently stubbed or intentionally handled elsewhere.
- We now have a concrete reason for type `6`: the front-interaction helper at `C0:65C2` treats it as a sentinel for a cached door-like fallback result, storing a resolved pointer in `$5DDE/$5DE0` and marking `$5D62 = #$FFFE`.
- A targeted cross-check against the legacy reference still suggests broader door-related semantics somewhere in this type range, but the `C0` local dispatcher body alone does not prove more than that cached-fallback role.

## Current best model

- types `0` and `2` are now strongly tied to the bank `CF` door-destination table family.
- type `1` flips between two special movement states in `$9883`.
- type `3` feeds the same delayed movement/timer machinery used by the `6E2C/6E4A` callback pair.
- type `4` remains the staged-grid movement wrapper at `C0:70CB`.
- types `5` and `7` still need broader-context tracing because their local `C0` helper body is a no-op.
- type `6` now looks less mysterious: in at least one important path it means "cache a door-like fallback interaction result" rather than "run a visible helper here."

The focused probe write-up now lives in `notes/type6-door-candidate-probe-65c2.md`, and the surrounding interaction pipeline is summarized in `notes/front-interaction-flow.md` and `notes/interaction-result-consumers.md`.

## Best next targets

- Trace the higher-level C2 state family around `99DC`, and pair that with object-refresh helpers that consume `$2AF6`, so selector values `1/2` and target states `0/4` can be named from behavior instead of control flow.
- Tighten the roles of `$9883`, `$987F`, `$5DC2`, `$5DC4`, `$5DA8`, and `$5DAA` with a broader movement-state pass.
