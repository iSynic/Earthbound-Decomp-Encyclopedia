# Frame Callback Bodies

This note focuses on the concrete callback routines reached through `C0:8518`.

## Execution context

- `NMI_FinalizeFrame` calls the callback near the end of the NMI path.

- The callback runs in bank `C0` via `JMP ($0020)`.

- The callback inherits a frame-oriented environment with `DBR=7E` and `DP=0200`.

- That means absolute references like `$9E54` inside callback code point into `7E:9E54`, not ROM bank `C0`.

## `C0:DC4E` `FrameCallback_ProcessDelayedActions`

Observed behavior from the refreshed decode:

- Gates itself on several WRAM state variables and returns early if any of them are nonzero or not ready.

- Specifically checks or touches `7E:9E54`, `7E:88E0`, `7E:9643`, `7E:5D60`, and `7E:4DBA` before entering the main loop.

- Uses a 4-entry loop driven by a local counter in direct page.

- Walks a table beginning at `7E:9E3C` in 6-byte records.

- Treats the first word of each record like a countdown or delay value.

- When a countdown reaches zero, it loads later record fields into `$BC/$BE` and calls `C0:9279`.

- `C0:9279` is an indirect long jump through `[$00BC]`, so the record is effectively supplying a delayed callback target.

- Advances the table pointer by 6 bytes each iteration and returns cleanly with `RTS`.

Working interpretation:

- This is a per-frame delayed-action scheduler living in WRAM.

- The `7E:9E3C` table is best thought of as four timed action slots.

- `7E:9E54` appears to be a companion activation or cooldown value for this callback family.

## `C0:9321` `Init_DelayedActionState`

This routine is not itself the frame callback, but it now looks tightly coupled to the delayed-action subsystem:

- It is called immediately after `FrameCallback_ProcessDelayedActions` is installed from the `C0:B6C8` setup chain.

- `Init_DelayedActionPools` at `C0:927C` appears to bootstrap this subsystem earlier by clearing the active-list heads, seeding the free task-slot and free task-record chains, and zeroing broad state tables.
- It doubles values at `$0A4C` and `$0A4E`, then calls `C0:9C02` and aborts with `RTL` and `A=0` on failure.

- The best current structure model is:

  - `$0A50` active task-slot list head

  - `$0A52` free task-slot list head

  - `$0A54` free task-record list head

  - `$0A9E,X` next task-slot pointer

  - `$0ADA,X` task-slot to task-record index

  - `$125A,Y` task-record free-list next pointer

- On success, it calls `C0:9D03`, stores the returned task-record index from `Y` into `$0ADA,X`, writes `#$FFFF` into `$125A,Y`, seeds several constant fields, and copies a contiguous parameter block from `$0A38-$0A4A` into multiple table families.

- It also pulls template words from bank `C4` tables at `C4:00D4` and `C4:00D6`.

- The legacy reference explicitly names `C4:00D4` as `ScriptPtrs`; we should still treat that as borrowed until a stronger ROM-local confirmation appears, but it fits the observed data flow well.

- The tail of the routine clears a cluster of per-entry state fields at `$10F2/$0DAA/$0CF6/$0DE6/$0D32/$0E22/$0D6E` and then hands off to `C0:941E`.

- `C0:941E` reloads the task-record index through `$0ADA,Y`, writes into `$13FE,X` and `$148A,X`, clears `$1372,X` and `$12E6,X`, and returns with `RTL`.

Working interpretation:

- `C0:9321` and `C0:941E` look like constructors for a delayed-action task slot and its bound task record, not just loose table initialization.

- The countdown table at `7E:9E3C` is probably only the visible trigger layer; this setup code suggests a larger set of parallel tables store script pointers, handler state, and task-record metadata behind each live slot.

## Pool bootstrap and timer helpers

- `Queue_DelayedActionTimer` at `C0:DBE6` now looks like the helper that arms one of the four timer records in `7E:9E3C`. It takes a delay in `A`, copies a callback target from `$20/$22`, finds the first empty 6-byte record, stores the delay and target there, and returns the timer-slot index in `A`.
- The current direct-caller map for this helper lives in `notes/delayed-action-timer-callers.md`. All 8 confirmed direct callers are in bank `C0`, with repeated callback targets at `C0:6F82` and `C0:6FED`.

## Movement-oriented timer callbacks

- `TimerCallback_CommitStagedPosition_State0C` at `C0:6E2C` writes `$9883 = #$000C`, clears `$5D56`, copies staged X/Y from `$5DD0/$5DD2` into `$9877/$987B`, clears `$9875/$9879`, and returns.

- `TimerCallback_CommitStagedPosition_ClearMotion` at `C0:6E4A` writes `$5DC4 = #$FFFF`, clears `$9883`, `$5D56`, and `$5DBA`, copies the same secondary staged X/Y pair from `$5DD0/$5DD2`, clears `$9875/$9879`, and returns.

- `TimerCallback_WaitForStagedY_State0D` at `C0:6F82` and `TimerCallback_WaitForStagedY_ClearMotion` at `C0:6FED` are self-rearming pollers. Both compare live Y at `$987B` against staged Y at `$5DCE`; if the condition is not met they requeue themselves for 1 frame later through `DBE6`, and if the condition is met they copy staged X/Y from `$5DCC/$5DCE` into `$9877/$987B` and clear `$9875/$9879`.

- The difference between those two pollers is the completion state they leave behind. `C0:6F82` sets `$9883 = #$000D`, while `C0:6FED` clears `$9883`, `$5D56`, and `$5DBA` and also resets `$5DC4` to `#$FFFF`.

- The arming wrappers at `C0:6F68`, `C0:7180`, and `C0:71D1` seed the staged coordinate pairs and derive delay values from `C48D58`, `C48E6B`, and tables at `C3:E200`, `C3:E208`, `C3:E220`, and `C3:E228`.

- `Queue_StagedMovementFromGridCoords` at `C0:70CB` is now the clearest upstream wrapper for this family. It scales grid-like inputs by 8, uses `C3:E210/E218` or `C3:E220/E228` as 8-pixel offset tables, seeds movement-state words in `$5D56/$5DBA/$5DC4/$5DCA`, and then hands off completion to `C0:6F82` or `C0:6FED`.

- Its helper `Select_StagedMovementFacing` at `C0:705F` chooses between shadow-facing values `#$0002` and `#$0006` in `$5DCA` and can veto the movement setup entirely. That makes `$5DCA` look like a temporary facing field used while the delayed callback path is active.

- Separate from the timer layer, the broader movement subsystem now clearly has a 4-entry WRAM queue rooted at `$5DEA`. `C0:64E3` enqueues 6-byte records into that ring, and `C0:75DD` consumes one record when blocking state like `$5D60`, `$4DBA`, and `$4DC2` is clear.

- Above that queue layer, `Lookup_MovementTriggerType` at `C0:7477` and `Dispatch_MovementHelperFromLookup` at `C0:7526` now give us a real trigger-dispatch map. The lookup scans bank `D0` bucket data, returns a small type in `A`, and the dispatcher maps that type into helper families such as `6A91`, `6ACA`, `6E6E`, and the staged-movement path at `70CB`.

- Those helper bodies are now much clearer too. Types `0` and `2` both resolve pointers from the bank `CF` destination table family and enqueue them through the WRAM queue, type `1` writes paired movement states `#$0007/#$0008` into `$9883`, type `3` stages a timed offset move through the `6E2C/6E4A` callback pair, types `5` and `7` are stubs in this local dispatcher path, and type `6` now looks like a cached door-candidate sentinel because `C0:65C2` stores a resolved fallback pointer in `$5DDE/$5DE0` and marks `$5D62 = #$FFFE`. The focused write-up lives in `notes/movement-trigger-helper-bodies.md`, and the type-`6` probe details live in `notes/type6-door-candidate-probe-65c2.md`. The broader interaction pipeline now has its own write-up in `notes/front-interaction-flow.md` and `notes/interaction-result-consumers.md, and notes/interaction-result-classes.md, and notes/interaction-context-and-event-flags.md and `notes/class2-c2-handlers.md and `notes/class2-dispatch-family.md```.

- The legacy reference names `$9877/$987B` as player X/Y low position. That remains borrowed rather than proven, but it matches the observed access pattern closely enough that this whole timer family now looks like movement-state sequencing.

- `Process_ActiveTaskSlots` at `C0:94AA` ties the larger allocator world back into this timer layer by walking the active slot list, running per-slot handlers through `($121E,X)` and `($11A6,X)`, and finally tail-dispatching through `($0A5E,X)`. With `Init_DelayedActionPools` seeding `$0A5E` to `DB0F`, that default tail dispatch lands in `Dispatch_ActiveTaskSlots` at `C0:DB0F`.

- `Dispatch_ActiveTaskSlots` at `C0:DB0F` traverses the active slot list, filters entries using position-like fields at `$0B16/$0B52`, dispatches some directly through `C0:A0CA`, and chains others through `$280C` for a second ordered pass keyed by `$0BCA`. That looks like the heavier active-object side of the subsystem, separate from the tiny four-entry timer table.

- `Init_DelayedActionPools` at `C0:927C` appears to bootstrap this subsystem before later constructors run by clearing active-list heads, seeding the free task-slot and free task-record chains, and zeroing broad state tables.

- `Clear_DelayedActionTimerSlot` at `C0:DC38` clears one of the four 6-byte timer records at `7E:9E3C` by computing `slot_index * 6` and zeroing the record's first word.

- That makes the visible `7E:9E3C` timer table look like a lightweight dispatch layer rather than the same thing as the larger task-slot and task-record pools under `$0A50/$0A52/$0A54`.

## Delayed-action helper routines

- `Alloc_TaskSlotOrFail` at `C0:9C02` only succeeds if both `$0A54` and `$0A52` are valid, then removes one slot from the free-slot chain.

- `Link_TaskSlotIntoActiveList` at `C0:9C57` appends a slot to the active chain rooted at `$0A50`.

- `Detach_TaskSlotLink` at `C0:9C73` removes a slot from that active chain and updates `$0A50/$0A56` when needed.

- `Push_TaskSlotToFreeList` at `C0:9C8F` returns a slot to the free-slot chain rooted at `$0A52`.

- `Pop_TaskRecordFromFreeList` at `C0:9D03` pops one task-record index from the free-record chain rooted at `$0A54`.

- `Push_TaskRecordToFreeList` at `C0:9D12` detaches a task record from a slot-owned chain and pushes it back onto the free-record head at `$0A54`.

- `Unlink_TaskRecordFromSlotChain` at `C0:9D1F` removes a specific record from the chain rooted in `$0ADA,X`, and `Find_TaskRecordPredecessor` at `C0:9D3E` walks `$125A` to locate the predecessor of the target record in `Y`.

- `Restore_TaskRecordChain` at `C0:9C99` pushes a released task-record chain back into the free-record list via `$125A`.

- `Init_TaskRecordDefaults` at `C0:9DA1` seeds each task record with `#$943B` and `#$00C0`, which likely act as a default handler pointer and bank or state field.

## `C0:F41E` `FrameCallback_ProcessCommandStream`

Observed behavior from the refreshed decode:

- Compares frame or state values against WRAM state at `7E:B4E3` and a rolling index at `7E:B4F7`.

- Builds pointers based on that nibble-sized index.

- Derives addresses in the `7Dxx` WRAM range and stores them into local direct-page temporaries.

- Reads a command byte through an indirect long pointer at `[$1B]`.

- Dispatches on command values `01`, `02`, `03`, `04`, and `FF`.

- The `01` and `02` paths build destination addresses under `7Dxx`, write values derived from the stream, and advance both source and destination pointers.

- The `03` path scales the command byte and adds it into `7E:B4E3`, which looks like a variable advance or timing update.

- The `04` path runs a small byte-processing loop using `7E:B4F9` and writes transformed values back out through indexed pointers.

- `FF` resets `7E:B4E3` to `#$FFFF`.

Working interpretation:

- This is a frame-driven command-stream interpreter rather than a one-off callback.

- It likely feeds one or more WRAM-backed staging buffers in the `7Dxx` range.

- Some late branches still depend on understanding processor-width restoration after `JSL $C4EFC4`, so the remaining `BRK`-looking artifacts in that region should be treated as decoder-state ambiguity, not final semantic conclusions.

## Support routines

- `NMI_ServiceAudioQueue` at `C0:8501` runs before the frame callback and drains a small 8-entry queue from WRAM through APU port `$2143`.

- `Frame_CallbackDispatcher` at `C0:8518` jumps through the callback pointer in `$20/$21`.

- `Frame_CallbackReturn` at `C0:851B` is the default no-op callback.

- `Set_FrameCallbackPtr` at `C0:851C` installs a new 16-bit callback target.

- `Reset_FrameCallbackToDefault` at `C0:8522` restores the no-op callback.

- `Dispatch_DelayedActionTarget` at `C0:9279` is a `JML [$00BC]` helper used by the delayed-action callback.

- `Init_DelayedActionState` at `C0:9321` appears to allocate and seed the delayed-action subsystem's backing task-slot and task-record tables right after the callback is installed.

## Known installs

- `FrameCallback_ProcessDelayedActions` is installed from `C0:B6C8`, `C4:F6FE`, and `EF:E2C7`.

- `FrameCallback_ProcessCommandStream` is installed from `C4:F592`.

- `C4:F673` resets the callback to the default `RTS` stub through `C0:8522`.

- `C0:B6C5` seeds `7E:9E54` with `#$0697` immediately before installing `FrameCallback_ProcessDelayedActions`.

- `C0:766F` and `EF:E6A0` also write `7E:9E54`, which makes that address a strong cross-reference point for this subsystem.

## Next targets

- Trace the higher-level C2 state family around `99DC`, and pair that with object-refresh helpers that consume `$2AF6`, so selector values `1/2` and target states `0/4` can be named from behavior instead of control flow.

- Tighten the interpretation of `Dispatch_ActiveTaskSlots` at `C0:DB0F`, especially the `$103E == 1` path and the ordering chain in `$280C/$0BCA`, so we can tell whether that second pass is render sorting, collision ordering, or another visibility-driven dispatch.

- Name the table families around `$0E5E-$103E`, `$107A/$10B6`, `$13FE`, and `$148A` in task-record terms instead of raw offsets.

- Resolve accumulator-width restoration after `JSL $C4EFC4` inside `C0:F41E` to finish naming the command handlers with confidence.
