# Bank C0 Entry Notes

These are the first entry points worth annotating in the EarthBound US ROM.

## Correct HiROM interpretation

- The exception vectors are read from CPU bank `00`.

- In this ROM, the reset vector is `00:8141`, not file offset `0x0141`.

- Because this is HiROM, `00:8141` mirrors to canonical ROM address `C0:8141` at file offset `0x008141`.

- The useful first-pass routines are the long jumps reached by the vector trampolines: `C0:8000`, `C0:814F`, and `C0:8170`.

## Vector trampoline bytes

The following bytes come from the ROM at file offset `0x008140`:

```text

008140: C0 18 FB 5C 00 80 C0 5C 70 81 C0 5C 4F 81 C0 08

008150: C2 30 48 DA 5A 0B F4 00 00 2B 8B F4 00 00 AB AB

008160: E2 20 AD 11 42 30 1C C2 30 AB 2B 7A FA 68 28 40

008170: 08 C2 30 48 DA 5A 0B F4 00 00 2B 8B F4 00 00 AB

```

## What we know now

- `Boot_InitHardware` at `C0:8000` is the real reset target after the `00:8141` trampoline.

- That boot routine disables interrupts and DMA, clears large regions of work RAM, initializes the direct page and stack, and writes a broad sweep of PPU register defaults.

- `IRQ_Prologue` at `C0:814F` is a short interrupt wrapper that acknowledges `$4211` and returns quickly unless work needs to be done.

- `NMI_Prologue` at `C0:8170` enters `NMI_FrameUpdate`, which looks like the core per-frame upload path.

- `NMI_ProcessTransferQueue` at `C0:8240` walks an 8-byte command queue in WRAM at `$0400+X`, configures DMA channel 0 via `$4300-$4305`, writes VRAM settings like `$2115` and `$2116`, and kicks DMA with `$420B`.

- `NMI_ApplyScrollSetA` and `NMI_ApplyScrollSetB` upload paired scroll and mode values from WRAM mirrors to `$210D-$2114`.

- `NMI_FinalizeFrame` clears the transfer mode flag in `$2C`, restores display and HDMA-style state from WRAM mirrors, services a small audio/APU queue, optionally runs a callback through a function pointer in `$20`, and then returns from interrupt.

## New subroutine findings

- `NMI_ServiceAudioQueue` at `C0:8501` compares queue indices in WRAM `$CA/$CB`, pulls a byte from WRAM `$1AC2+X`, writes it to `$2143`, and advances the read index modulo 8.

- Because `$2143` is an SNES APU I/O port, this looks like a tiny per-frame sound command drain rather than generic game logic.

- `Frame_CallbackDispatcher` at `C0:8518` is just `JMP ($0020)`, so `$20/$21` act like a frame callback pointer.

- `Frame_CallbackReturn` at `C0:851B` is a bare `RTS`, and boot code initializes `$20` to that address, which makes the callback a no-op by default.

- `Set_FrameCallbackPtr` at `C0:851C` stores a 16-bit address into `$20/$21` and returns with `RTL`, which strongly suggests other banks can install frame-end callbacks through it.

- `Reset_FrameCallbackToDefault` at `C0:8522` writes `#$851B` back into `$20/$21` and returns with `RTL`.

- `Dispatch_DelayedActionTarget` at `C0:9279` is an indirect long jump through `[$00BC]`, used by the delayed-action callback when a slot expires.

- `Init_DelayedActionState` at `C0:9321` now looks like a real task-slot constructor, not a generic helper. It doubles counters at `$0A4C/$0A4E`, aborts early if `JSR $9C02` fails, and on success immediately calls `C0:9D03` to bind a task record to the chosen slot.

- The best current structure model is:

  - `$0A50` active task-slot list head

  - `$0A52` free task-slot list head

  - `$0A54` free task-record list head

  - `$0A9E,X` next task-slot pointer

  - `$0ADA,X` task-slot to task-record index

  - `$125A,Y` task-record free-list next pointer

- `C0:9321` stores the allocated task-record index from `Y` into `$0ADA,X`, writes `#$FFFF` into `$125A,Y`, then seeds a wide set of per-slot and per-record table families.

- The `C0:9321` success path copies a configuration block from `$0A38-$0A4A` into several table families such as `$0E5E/$0E9A/$0ED6/$0F12/$0F4E/$0F8A/$0FC6/$1002/$103E`, writes constants like `#$9FC8`, `#$A023`, `#$A3A4`, and stores stack-sourced values into `$0B8E/$0B16/$0BCA/$0B52`.

- The tail of `C0:9321` also pulls template data from bank `C4` tables at `C4:00D4` and `C4:00D6`, then clears several associated state fields at `$10F2/$0DAA/$0CF6/$0DE6/$0D32/$0E22/$0D6E` before branching into a short helper at `C0:941E`.

- The legacy reference explicitly names `C4:00D4` as `ScriptPtrs`; that is not proven by our ROM alone, but it fits the observed behavior cleanly and is our best current borrowed table name.

- `C0:941E` reloads the task-record index through `$0ADA,Y`, writes caller-supplied values into `$13FE,X` and `$148A,X`, clears `$1372,X` and `$12E6,X`, and returns with `RTL`.

- Taken together, `C0:9321` looks like allocation plus initialization for a structured delayed-action task slot and its bound task record rather than a one-off callback flip.

## Known callback targets

- `FrameCallback_ProcessDelayedActions` at `C0:DC4E` runs with `DBR=7E`, scans WRAM slots at `7E:9E3C`, decrements countdowns, and dispatches expired entries through `C0:9279`.

- `FrameCallback_ProcessCommandStream` at `C0:F41E` runs with `DBR=7E` and appears to interpret a small frame-driven command stream backed by WRAM state.

- `FrameCallback_ProcessDelayedActions` is installed from `C0:B6C8`, `C4:F6FE`, and `EF:E2C7`.

- `FrameCallback_ProcessCommandStream` is installed from `C4:F592`.

- `C4:F673` explicitly resets the callback through `C0:8522`.

- The current cross-reference report lives in `notes/frame-callback-xrefs.md`.

- The callback-body summary lives in `notes/frame-callback-bodies.md`.

## Recent refinements

## Active-slot dispatch bridge

- `Process_ActiveTaskSlots` at `C0:94AA` walks the active task-slot list through `$0A9E`. For each slot it runs up to two per-slot phase handlers through `($121E,X)` and `($11A6,X)`, then after the list is exhausted it dispatches through `($0A5E,X)` with `X=0`.

- Because `Init_DelayedActionPools` seeds `$0A5E` with `#$DB0F`, the default tail call from `C0:94AA` lands in `Dispatch_ActiveTaskSlots` at `C0:DB0F`. That routine traverses the active slot list rooted at `$0A50`, filters entries using position-like fields at `$0B16/$0B52`, directly dispatches some slots through `C0:A0CA`, and chains others through `$280C` for a second ordered pass keyed by `$0BCA`.

- `Process_TaskSlotRecordChain` at `C0:94D0` is the per-slot record walker. It follows the record chain rooted in `$0ADA,X` via `$125A`, calls the script-oriented helper at `C0:9506` for each record, then seeds `$0A5A/$0A5C` from `$107A/$10B6` and performs a long indirect dispatch through `JSL $C09D9E`, which is `JMP [$0A5A]`.

- `Queue_DelayedActionTimer` at `C0:DBE6` is the missing timer-arm helper for the visible `7E:9E3C` table. It takes a delay value in `A`, copies a callback pointer from `$20/$22`, scans the four 6-byte records for a free slot, writes the delay to the first word and the callback target to the next two words, and returns the chosen timer-slot index in `A`.
- The current direct-caller map for `C0:DBE6` lives in `notes/delayed-action-timer-callers.md` and `notes/direct-callers-c0-dbe6.md`. So far all 8 confirmed direct callers are in bank `C0`, and the repeated callback targets are `C0:6F82` and `C0:6FED`.

- The repeated timer callbacks are no longer generic threshold checks. `TimerCallback_WaitForStagedY_State0D` at `C0:6F82` and `TimerCallback_WaitForStagedY_ClearMotion` at `C0:6FED` both self-rearm through `DBE6` until live Y at `$987B` crosses staged Y at `$5DCE`, then copy staged X/Y from `$5DCC/$5DCE` into `$9877/$987B`.

- `TimerCallback_CommitStagedPosition_State0C` at `C0:6E2C` and `TimerCallback_CommitStagedPosition_ClearMotion` at `C0:6E4A` commit a second staged X/Y pair from `$5DD0/$5DD2`. The first leaves `$9883 = #$000C`, while the second clears `$9883`, `$5D56`, and `$5DBA`.

- The legacy reference names `$9877/$987B` as player X/Y low position. That is still a borrowed clue rather than a proven label, but it matches the ROM-local access pattern well enough that this timer layer now looks movement-oriented rather than generic.

- `Queue_StagedMovementFromGridCoords` at `C0:70CB` now decodes cleanly and looks like a staged movement setup wrapper, not a generic queue helper. It takes grid-like inputs in `X/Y`, scales them by 8, picks one of two 4-entry offset families from `C3:E210/E218` or `C3:E220/E228`, derives a delay from current live position through `C48D58`, then arms either `C0:6F82` or `C0:6FED` and stores the staged target in `$5DCC/$5DCE`.

- Its helper `Select_StagedMovementFacing` at `C0:705F` inspects the mode family in `$5DC4`, reads `$987F`, writes a shadow-facing value to `$5DCA`, and returns zero or nonzero to decide whether the movement wrapper should proceed. The strongest current inference is that `$987F/$5DCA` are facing-like state words.

- The focused write-up for this wrapper lives in `notes/staged-movement-wrapper-70cb.md`.

- The queue family behind this movement system is now mapped. `Reset_StagedMovementQueue` at `C0:64D4` clears a 4-entry WRAM ring, `Enqueue_StagedMovementQueueEntry` at `C0:64E3` writes 6-byte records rooted at `$5DEA`, and `Process_StagedMovementQueueEntry` at `C0:75DD` drains one record when the engine is idle enough to accept it.

- The strongest current queue model is: `$5E04` write index, `$5E02` read index, `$5DC0` current or last queue type for duplicate suppression, and `$5D9A` a queue-pending flag. The focused write-up lives in `notes/staged-movement-queue.md`.

- The upstream trigger lookup is now mapped too. `Lookup_MovementTriggerType` at `C0:7477` scans bank `D0` bucket data using coarse 32-pixel cell selection plus low 5-bit coordinate matching, returns a small trigger type in `A`, and copies side data into `$5DBC/$5DBE`. `Dispatch_MovementHelperFromLookup` at `C0:7526` branches that type into the `75xx` helper family, including type `4 -> C0:70CB`.

- The focused write-up for that layer lives in `notes/movement-trigger-lookup-7477.md`.

- The sibling helper bodies are now decoded too. Type `0` at `C0:6A1B` and type `2` at `C0:6ACA` both resolve entries from the bank `CF` destination table family and enqueue them as queue types `0` and `2`; type `1` at `C0:6A91` writes paired special states `#$0007/#$0008` into `$9883`; type `3` at `C0:6E6E` stages a small offset move through the `6E2C/6E4A` timer callbacks; types `5` and `7` are stubs in this local dispatcher path, and type `6` now looks like a cached door-candidate sentinel because `C0:65C2` stores a resolved fallback pointer in `$5DDE/$5DE0` and marks `$5D62 = #$FFFE`. The focused write-up lives in `notes/movement-trigger-helper-bodies.md`, and the type-`6` probe details live in `notes/type6-door-candidate-probe-65c2.md`. The broader interaction pipeline now has its own write-up in `notes/front-interaction-flow.md` and `notes/interaction-result-consumers.md, and notes/interaction-result-classes.md, and notes/interaction-context-and-event-flags.md and `notes/class2-c2-handlers.md and `notes/class2-dispatch-family.md```.

- `Init_DelayedActionPools` at `C0:927C` now looks like the subsystem-wide pool bootstrap. It seeds `$0A5E` with `#$DB0F`, clears active heads like `$0A50`, builds the free task-slot chain in `$0A9E`, builds the free task-record chain in `$125A`, and clears broad per-slot state tables before later constructors run.

- `Push_TaskRecordToFreeList` at `C0:9D12`, `Unlink_TaskRecordFromSlotChain` at `C0:9D1F`, and `Find_TaskRecordPredecessor` at `C0:9D3E` show that task records can be detached and recycled independently of task slots through the `$0ADA` to `$125A` linkage.

- `Clear_DelayedActionTimerSlot` at `C0:DC38` clears one of the four 6-byte records at `7E:9E3C` using `slot_index * 6`, which strongly suggests the visible timer table is a lightweight dispatch layer sitting beside the heavier `$0A50/$0A52/$0A54` allocator structures.

## Practical interpretation

- Bank `C0` is already giving us a clean skeleton of EarthBound's boot, video upload, audio queue, delayed-action scheduling, callback installation, and per-frame command processing pipeline.

- The delayed-action side is no longer just a single callback body. We now have a pool bootstrap at `927C`, a task-slot and task-record constructor at `9321/941E`, an active-slot dispatcher path at `94AA -> $0A5E -> DB0F`, and the runtime scheduler at `DC4E`.
- The four 6-byte records at `7E:9E3C` now look like a lightweight timed-dispatch front end rather than the same thing as the larger `$0A50/$0A52/$0A54` allocator structures, and `DBE6` now looks like the helper that arms those timer records.

- The command-stream side at `F41E` is decoding much farther now, but one branch still depends on understanding CPU-width restoration after `JSL $C4EFC4`, so some `brk` artifacts there should be treated as analysis-state issues rather than literal code.

## Caution

- Several other vectors point to `00:5FFF`, which is not directly ROM-mapped in bank `00` on HiROM.

- We should treat those as unresolved until debugger traces or broader disassembly give us a reason to interpret them differently.

- Some state-width mismatches remain in the first-pass listing where different control-flow paths reconverge or calls may restore `P`; that is expected until the decoder learns more about status restoration and call boundaries.

## Entity lifecycle layer

- Claude's latest bank-`C0` pass added one genuinely useful new bridge: the previously loose `C0:1B15..3D20` stretch now looks much more like an entity-slot lifecycle layer sitting between the allocator-heavy task code and the already-mapped movement or display-side consumers.

- `Free_EntitySlot` at `C0:2140` is the strongest new anchor. It takes a slot id in `A`, validates or releases the per-slot record pointer from `$112E,Y` through `C0:1B15`, clears the slot through `C0:1C11`, conditionally decrements `$4A5C` when `$2C9A,Y & $F000 == $8000`, clears `$4A60` when `$2D12,X == $00E1`, writes `$FFFF` into `$2CD6,X` and `$2C9A,X`, then calls `C0:9C35` for secondary cleanup.

- That gives the surrounding WRAM block a healthier local read:
  - `$4A00+` = per-slot allocation or state array scanned by `C0:1C11`
  - `$112E,Y` = per-slot record pointer or pool handle consumed by `C0:1B15` during teardown
  - `$2C9A,X` = per-slot persistence or type-flags word, with high-bit persistence behavior on free
  - `$2CD6,X` = per-slot cached id or mirror cleared on free
  - `$2D12,X` = per-slot type field with special `$00E1` behavior
  - `$4A5C/$4A60/$4A68` = small allocator or scene counters reset by the scene wrappers

- `Reset_AllEntitySlots` at `C0:2194` and `Reset_ActiveEntitySlots` at `C0:21E6` now fit that same layer cleanly. The first frees slots whose `$0A62` state is at least `5`, then clears `$289E`; the second frees slots whose `$0A62` state is at least `1`, then runs the reserved-slot cleanup on slot `$0017`.

- `Spawn_Entity` at `C0:222B` is also healthier now as the front door of that same lifecycle layer. The current safest local model is that it validates slot id `< $20` and variant id `< $28`, indexes a `CF:61E7` template registry using `(slot * $40) + variant`, rejects zero entries, then enters the initialization path at `C0:2500`. I am still keeping the exact semantic name of `CF:61E7` cautious, but a slot/variant template registry is now a strong local fit.

- The battle and scene wrappers around this layer are worth recording too. `C0:3C80` and `C0:3D20` both free slot `$0018`, zero the same small scene-state words like `$9A0B/$987D/$0A38/$0A3A`, and call `C0:1E49` with different spawn counts. So the safest current read is that these are scene-transition wrappers over the same slot lifecycle machinery, not isolated battle-only oddities.

- One earlier local note also gets a healthier boundary from this pass: `C0:39E5` is probably broader than a mushroomized-only helper. It still fits the builder family we mapped earlier, but it now also looks like a shared sync helper that copies live player position into staged per-entry arrays through `$988B/$9897`, then calls `C0:A254` for each live entry.

## Delayed-action helper model

- `Alloc_TaskSlotOrFail` at `C0:9C02` only succeeds if both the free task-record head at `$0A54` and the free task-slot head at `$0A52` are valid, then removes one slot from the free-slot chain rooted at `$0A52`.

- `Link_TaskSlotIntoActiveList` at `C0:9C57` appends the chosen slot onto the active chain rooted at `$0A50`.

- `Detach_TaskSlotLink` at `C0:9C73` removes a slot from the active chain and updates `$0A50` and `$0A56` when needed.

- `Push_TaskSlotToFreeList` at `C0:9C8F` pushes a released slot back onto the free-slot chain at `$0A52`.

- `Pop_TaskRecordFromFreeList` at `C0:9D03` pops one task-record index from the free-record chain rooted at `$0A54`.

- `Restore_TaskRecordChain` at `C0:9C99` pushes a released task-record chain back into the free-record list using `$125A`.

- `Push_TaskRecordToFreeList` at `C0:9D12` detaches a task record from a slot-owned chain and pushes it back onto the free-record head at `$0A54`.

- `Unlink_TaskRecordFromSlotChain` at `C0:9D1F` removes a specific record from the chain rooted in `$0ADA,X`, while `Find_TaskRecordPredecessor` at `C0:9D3E` walks `$125A` to locate the predecessor of the target record in `Y`.

- `Init_TaskRecordDefaults` at `C0:9DA1` seeds each task record with `#$943B` and `#$00C0`, which likely act as a default handler pointer and bank/state field.

## Next targets

- Trace the higher-level C2 state family around `99DC`, and pair that with object-refresh helpers that consume `$2AF6`, so selector values `1/2` and target states `0/4` can be named from behavior instead of control flow.

- Tighten the role of `$5DC2`, `$5DC4`, `$5D56`, `$5DBA`, `$5DA8`, `$5DAA`, and `$9883` in movement terms, especially the `#$0007/#$0008/#$000C/#$000D` cases and the value encoding used by `$987F/$5DCA`.

- Tighten the interpretation of `Dispatch_ActiveTaskSlots` at `C0:DB0F`, especially the `$103E == 1` path and the ordering chain in `$280C/$0BCA`, so we can tell whether that second pass is render sorting, collision ordering, or another visibility-driven dispatch.

- Resolve the accumulator-width transition around `JSL $C4EFC4` in `C0:F41E` so the remaining command handlers stop looking like they hit `BRK`.
