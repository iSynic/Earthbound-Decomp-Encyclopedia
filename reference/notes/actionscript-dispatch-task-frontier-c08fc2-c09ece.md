# Action-script dispatch and task frontier: C0:8FC2-C0:9ECE

This note clears the next C0 audit frontier after the display/input utility strip. The addresses here are corroborated by `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank00.asm`, `refs/ebsrc-main/ebsrc-main/include/symbols/bank00.inc.asm`, and the legacy `Routine_Macros_EB.asm` labels around the same region.

## C0:8FC2 is table data, not code

`C0:8FC2` is included by ebsrc as `data/unknown/C08FC2.asm`, but the legacy reference places it inside the tail of `DATA_C08FB0`, a sequence of byte triples around the VRAM data port registers. Decoding from this address as code drifts immediately because the bytes are table data.

The broader local layout is:

- `C0:8FB0` / `DATA_C08FB0`: triples using `$2118/$2119/$2139/$213A`, named in the legacy reference as `REGISTER_WriteToVRAMPortLo`, `REGISTER_WriteToVRAMPortHi`, `REGISTER_ReadFromVRAMPortLo`, and `REGISTER_ReadFromVRAMPortHi`.
- `C0:8FC2`: the reference unknown start falls in the middle of that triple table, at the entry sequence that begins `81 39 80 ...`.
- `C0:8FE6-C0:8FF6`: small 8-bit multiply helper using `$4202/$4216`.
- `C0:8FF7`: the heavily used 16-by-8 multiply helper (`MULT168` in ebsrc), with hundreds of direct JSL callers.
- `C0:9032`: the next multiply helper (`MULT16` in ebsrc), also directly called across banks.

Working name: `VRAMPortTripleTable_Tail` for `C0:8FC2`. The exact table consumer still wants a deeper read, but the important audit point is that this is not a routine entry.

## C0:9506 action-script interpreter context

The action-script frame runner at `C0:9506` reads bytecode from `[$80],Y`, dispatches opcodes below `#$70` through the pointer table at `C0:9558`, and treats bytecodes `#$70-#$7F` as wait/state encodings. It persists:

- current script offset in `$13FE[slot]`
- script bank/page-ish state in `$148A[slot]`
- wait counter in `$1372[slot]`
- per-slot scratch/value cell in `$1516[slot]`
- per-slot return stack rooted at `$15A2 + slot*8`, with depth in `$12E6[slot]`

The legacy reference names this table `ScriptOpcodePtrs`; ebsrc has most entries already split into `overworld/actionscript/script/*.asm`, with the small unknowns below still exposed by address.

One residual symbol-only start in this interpreter is `C0:9622` (`UNKNOWN_C09622` in ebsrc). The legacy table entry actually points at `C0:9620`; `C0:9622` is the operand after `LDX $8A`, loading `$1516,X` and branching to the shared `C0:9608` store/jump helper. So this is not a separate semantic routine, just the inner alternate entry of the `MOVEMENT_CODE_24` handler.

## C0:9ABD mini-operation table

`C0:9ABD` is a four-entry pointer table used by the script opcodes at `C0:9A5C` and `C0:9A9F`. The interpreter selects a target address into `$8C`, a value/mask into `$90`, loads a table entry into `$0A5A`, and then jumps indirectly through `$0A5A`.

Table:

- `C0:9ABD -> C0:9AC5`
- `C0:9ABF -> C0:9ACC`
- `C0:9AC1 -> C0:9AD3`
- `C0:9AC3 -> C0:9ADB`

Handlers:

- `C0:9AC5` / `ScriptOp_MutateTarget_AND`: `($8C) = ($8C) & $90`
- `C0:9ACC` / `ScriptOp_MutateTarget_OR`: `($8C) = ($8C) | $90`
- `C0:9AD3` / `ScriptOp_MutateTarget_ADD`: `($8C) = ($8C) + $90`
- `C0:9ADB` / `ScriptOp_MutateTarget_EOR`: `($8C) = ($8C) ^ $90`

`C0:9A87` and `C0:9AE2` use the variable-offset table at `C0:9AF9`, which points at eight per-entity variable tables:

- `$0E5E`, `$0E9A`, `$0ED6`, `$0F12`, `$0F4E`, `$0F8A`, `$0FC6`, `$1002`

These are the same eight tables named by ebsrc as `ENTITY_SCRIPT_VAR_TABLES`.

## Adjacent script opcodes at C0:9B09-C0:9BF8

The next strip is a compact set of action-script operations around direct writes, scratch-variable movement, conditional branch/return-stack work, and callback pointer installs:

- `C0:9B09`: calls `Init_TaskRecordDefaults` for the current active task slot.
- `C0:9B0F`: writes an 8-bit immediate to an absolute script-specified address.
- `C0:9B1F`: writes a 16-bit immediate to an absolute script-specified address.
- `C0:9B2C`: if `$1516[slot] == 0`, branches to script pointer operand and pops one return-stack frame.
- `C0:9B44`: inverse of `C0:9B2C`, branching when `$1516[slot] != 0`.
- `C0:9B4D`: installs a far data pointer pair into `$112E[slot]` and `$116A[slot]`.
- `C0:9B61`: loads a 16-bit immediate into `$1516[slot]`.
- `C0:9B6B`: loads `$1516[slot]` from an absolute script-specified address.
- `C0:9B79`: stores `$1516[slot]` into one of the eight `ENTITY_SCRIPT_VAR_TABLES` tables.
- `C0:9B91`: loads `$1516[slot]` from one of the eight `ENTITY_SCRIPT_VAR_TABLES` tables.
- `C0:9BA9`: copies nonzero `$1516[slot]` into the wait counter `$1372[slot]`.
- `C0:9BB4`: loads the wait counter from one of the eight variable tables.
- `C0:9BCC`: loads `$10F2[current task]` from one of the eight variable tables.
- `C0:9BE4`: installs `$11E2[current task]`.
- `C0:9BEE`: installs `$11A6[current task]`.
- `C0:9BF8`: installs `$121E[current task]`.

This set explains why the `9ABD` mutation table is shared: the bytecode interpreter has both direct absolute and per-entity variable access paths, then uses the four mini-operations as reusable store modifiers.

## Task-list helpers at C0:9CD7-C0:9D78

The existing delayed-action helper model already names most of `C0:9C02-C0:9DA1`. The next exact starts are:

- `C0:9CD7` / `Compact_TaskSlotFreeList`: called by `C0:38D9`. It marks the current free-slot chain from `$0A52` with `#$8000`, scans task slots downward from `#$003A`, rebuilds `$0A9E` as a compact free list, and stores the new head in `$0A52`.
- `C0:9D60` / `Count_RecordLinksUntilY`: for a task slot in `X`, walks the `$0ADA[X]` / `$125A` record chain until it reaches target record `Y`, returning the zero-based link count in `A`.
- `C0:9D78` / `Select_NthTaskRecordInA`: for a task slot in `X`, starts at `$0ADA[X]` and advances through `$125A` `A-1` times, leaving the selected record in `Y`.

The helper model around this strip remains:

- `$0A50`: active task-slot list head
- `$0A52`: free task-slot list head
- `$0A54`: free task-record list head
- `$0A9E`: task-slot next-pointer table
- `$0ADA`: first task-record index owned by each slot
- `$125A`: task-record next-pointer/free-list table

## Script-facing task constructors and removers

`C0:9DAE` starts a family of script-facing constructors/removers around the task allocator:

- `C0:9DAE` / `Script_CreateTask_DefaultSlotRange`: sets alloc window `$0A4C=0`, `$0A4E=#003C`, reads six 16-bit parameters, offsets position fields from the current slot, initializes task work fields `$0A38-$0A48`, then jumps to `C0:9321`.
- `C0:9E0A` / `Script_CreateTask_WithSlotRange`: reads explicit `$0A4C/$0A4E`, then joins the `C0:9DAE` constructor body.
- `C0:9E18` / `Script_CreateTask_OneSlotRange`: reads a lower bound, sets upper bound to lower+2, then joins the constructor body.
- `C0:9E25` / `Script_RecreateTaskInOneSlotRange`: same one-slot range as `C0:9E18`, but first releases that slot through `C0:9C3B`.
- `C0:9E3B` / `Script_CreateTask_AbsolutePosition`: zeros the relative position/motion fields, reads handler/pointer parameters directly, and jumps to `C0:9321`.
- `C0:9E71`: reads a word and jumps to `C0:92F5`, so this is a compact script wrapper around that setup path.
- `C0:9E79`: reads an entity-script-var selector, uses `C0:9AF9` to fetch a task slot from that table, and releases it via `C0:9C3B`.
- `C0:9E8E`: reads an explicit task slot and releases it via `C0:9C3B`.
- `C0:9E98`: iterates the active task-slot list at `$0A50` and releases every slot except the current one in `$88`.
- `C0:9EAC`: reads a task-state word and releases every active slot whose `$0A62[slot]` matches, except the current slot.
- `C0:9ECE`: reads three script parameters and jumps to `C0:9403`, preserving the middle word on the stack; likely a task/script setup wrapper whose callee defines the final semantic name.

The constructors use the shared indirect executor at `C0:9D9E` (`JMP [$0A5A]`) and the parameter readers at `C0:9D8D` / `C0:9D99`.

## Working Names

- `C0:8FC2` = `VRAMPortTripleTable_Tail`
- `C0:8FE6` = `Multiply8x8_ViaHardwareRegisters`
- `C0:8FF7` = `Multiply16By8_ViaHardwareRegisters`
- `C0:9032` = `Multiply16By16_ViaHardwareRegisters`
- `C0:9506` = `Run_ActionScriptFrame`
- `C0:9558` = `ScriptOpcodePointerTable`
- `C0:9ABD` = `ScriptOpTargetMutationTable`
- `C0:9AC5` = `ScriptOp_MutateTarget_AND`
- `C0:9ACC` = `ScriptOp_MutateTarget_OR`
- `C0:9AD3` = `ScriptOp_MutateTarget_ADD`
- `C0:9ADB` = `ScriptOp_MutateTarget_EOR`
- `C0:9AF9` = `EntityScriptVarTablePointers`
- `C0:9B09` = `ScriptOp_InitCurrentTaskRecordDefaults`
- `C0:9B0F` = `ScriptOp_WriteImmediateByteToAddress`
- `C0:9B1F` = `ScriptOp_WriteImmediateWordToAddress`
- `C0:9B2C` = `ScriptOp_BranchIfScratchZeroAndReturn`
- `C0:9B44` = `ScriptOp_BranchIfScratchNonzeroAndReturn`
- `C0:9B4D` = `ScriptOp_InstallFarDataPointer`
- `C0:9B61` = `ScriptOp_LoadScratchImmediateWord`
- `C0:9B6B` = `ScriptOp_LoadScratchFromAddress`
- `C0:9B79` = `ScriptOp_StoreScratchToEntityVar`
- `C0:9B91` = `ScriptOp_LoadScratchFromEntityVar`
- `C0:9BA9` = `ScriptOp_CopyScratchToWaitCounterIfNonzero`
- `C0:9BB4` = `ScriptOp_LoadWaitCounterFromEntityVar`
- `C0:9BCC` = `ScriptOp_LoadTaskField10F2FromEntityVar`
- `C0:9BE4` = `ScriptOp_InstallTaskCallback11E2`
- `C0:9BEE` = `ScriptOp_InstallTaskCallback11A6`
- `C0:9BF8` = `ScriptOp_InstallTaskCallback121E`
- `C0:9CD7` = `Compact_TaskSlotFreeList`
- `C0:9D60` = `Count_RecordLinksUntilY`
- `C0:9D78` = `Select_NthTaskRecordInA`
- `C0:9DAE` = `Script_CreateTask_DefaultSlotRange`
- `C0:9E0A` = `Script_CreateTask_WithSlotRange`
- `C0:9E18` = `Script_CreateTask_OneSlotRange`
- `C0:9E25` = `Script_RecreateTaskInOneSlotRange`
- `C0:9E3B` = `Script_CreateTask_AbsolutePosition`
- `C0:9E71` = `Script_SetupTaskPath92F5`
- `C0:9E79` = `Script_ReleaseTaskFromEntityVar`
- `C0:9E8E` = `Script_ReleaseExplicitTaskSlot`
- `C0:9E98` = `Script_ReleaseAllOtherTasks`
- `C0:9EAC` = `Script_ReleaseTasksByStateExceptCurrent`
- `C0:9ECE` = `Script_SetupTaskWithThreeParameters`
