# Legacy Reference Findings

This note records the useful, low-risk findings from the legacy EarthBound disassembly extracted under `refs/earthbound-disasm-legacy/`.

## Reference scope

- Source archive: `<local reference archive>`

- Extracted copy: `refs/earthbound-disasm-legacy/Earthbound Decomp/`

- The project is an Asar-based assembly framework, so it is useful as a cross-reference but should not be treated as ground truth.

## Immediate confirmations

- The legacy project maps the entry trampolines exactly the way our current notes do:

  - `EB_InitAndMainLoop_Main` at `C0:8141` jumps to `C0:8000`

  - `EB_VBlankRoutine_Main` at `C0:8147` jumps to `C0:8170`

  - `EB_IRQRoutine_Main` at `C0:814B` jumps to `C0:814F`

- It confirms the callback helper cluster verbatim:

  - `C0:8501` drains the `$1AC2,X` queue to `$2143`

  - `C0:8518` is `JMP ($0020)`

  - `C0:851C` stores a callback pointer into `$0020`

  - `C0:9279` is `JMP [$00BC]`

- It confirms that `C0:B6C8` installs `C0:DC4E` as a callback after writing `$9E54`.

## Strong new clues for the delayed-action system

The most useful new information is around `C0:9321` and its helpers.

- The legacy source explicitly resolves the `C4:00D4` table used at `C0:93D5` as `ScriptPtrs`.

- That means the `C0:9321` setup path is not just filling generic tables; it is assigning script pointers.

- `C0:9321` stores the addresses of `label_C09FC8`, `label_C0A023`, and `label_C0A3A4`, which likely act as per-task handlers or state-machine entry points.

## Helper routine interpretation

The helper cluster around `C0:9C02` to `C0:9DA1` strongly suggests a two-layer allocator: one free list for task slots and another for task records.

- `C0:9C02`

  - requires both `$0A54` and `$0A52` to be valid

  - walks the slot chain through `$0A9E`

  - removes one chosen slot from the free-slot list

  - returns carry set on failure

- `C0:9C57`

  - writes `#$FFFF` to `$0A9E,X`

  - appends the slot onto the active chain rooted at `$0A50`

- `C0:9C99`

  - uses `$0ADA,X`, `$0A54`, and `$125A`

  - restores a released task-record chain to the free-record list

- `C0:9D03`

  - loads `Y` from `$0A54`

  - returns carry set if no record is available

  - otherwise advances `$0A54` through `$125A,Y`

  - behaves like pop-from-free-record-list logic

- `C0:9DA1`

  - stores `#$943B` into `$107A,X`

  - stores `#$00C0` into `$10B6,X`

  - looks like a small per-record initializer

Working interpretation:

- `$0A50` behaves like an active task-slot list head.

- `$0A52` behaves like a free task-slot list head.

- `$0A54` behaves like a free task-record list head.

- `$0A9E` behaves like the task-slot next-pointer table.

- `$0ADA` appears to associate a task slot with a task-record index.

- `$125A` behaves like a next-pointer table for the task-record free list.

## Useful RAM-map carryover

The legacy `RAM_Map_EB.asm` is sparse, but it does confirm a few basics cleanly:

- `$0400` is the DMA-to-VRAM update table.

- The 8-byte DMA record layout in that table matches our `NMI_ProcessTransferQueue` interpretation.

- The map file does not name the delayed-action addresses we care about, so it is only mildly helpful there.

## Limits of the legacy reference

- The project mostly uses raw address labels like `label_C09321` rather than semantic names, so it does not save much naming work by itself.

- It does not appear to provide an immediately discoverable semantic label for our `C0:F41E` command-stream callback.

- The Asar framework and bundled tools are useful context, but we should avoid importing their assumptions wholesale.

## Best use going forward

- Use the legacy source to borrow exact table names when they are explicit, like `ScriptPtrs`.

- Use helper routines in the `9Cxx` and `9Dxx` range as structural evidence for separate task-slot and task-record free lists.

- Keep all higher-level naming in our project ROM-first and verify any borrowed name against bytes or runtime behavior.
