# File Select Tail Helpers `C1:FF2C`, `C1:FF6B`, and `C1:FF99`

This note covers the remaining unknown includes after `intro/file_select_menu_loop.asm` and before the SRAM checksum/copy-protection routine.

See also [overworld-entity-type-registry-9887-98a4.md](notes/overworld-entity-type-registry-9887-98a4.md).
See also [file-select-action-copy-delete-menus-c1f07e-f14f-f2a8.md](notes/file-select-action-copy-delete-menus-c1f07e-f14f-f2a8.md).

## Main Result

These are small glue helpers around file-select entry/exit and text-window layout:

- `C1:FF2C` watches the active lead character's overworld type and reports whether `$B4A2` changed
- `C1:FF6B` is the top-level file-select entry wrapper called from bank `C0`
- `C1:FF99` computes and stores text layout measurements for the C4 text renderer

## `C1:FF2C`: Active Lead Type Change Detector

`C1:FF2C` is called from the frame/update path at `C1:2E28`, only when `$B4B6` is zero. If it reports a change, the caller immediately invokes `C4:7F87`.

The routine:

- reads `$98A4`, the active player-controlled party count / active party slot count
- uses `$9891 + ($98A4 - 1)` to resolve the current lead party entity slot
- indexes the entity/object pointer table at `$4DC8`
- reads byte `+0x0E` from that object record
- maps object-record values `1` and `2` to state `1`; all other values map to state `0`
- compares that state to `$B4A2`
- returns `1` if the state changed, otherwise `0`
- stores the new state into `$B4A2`

This is best understood as a small "lead sprite/entity class changed" watcher. In context, it gates a C4 redraw/update pass while the game is returning from file-select/menu state into live overworld/text processing.

## `C1:FF6B`: File Select Entry Wrapper

`C1:FF6B` has one direct long caller:

- `C0:B633 -> C1:FF6B`

It:

- clears `$5E6E`
- sets `$B49D = 1`
- calls the file-select menu loop at `C1:F805`
- performs the standard C3/C1 post-loop update calls
- clears `$B4B6`
- clears `$B4A2`
- restores `$5E6E = 0x00FF`
- clears `$B49D`
- returns `0`

The decode tool can desync here if it assumes the accumulator is still 8-bit after the `C1:F805` call. The legacy disassembly and byte stream line up as `LDA #$00FF; STA $5E6E; SEP #$20; STZ $B49D; REP #$20; LDA #$0000; RTL`.

So `C1:FF6B` is not another submenu. It is the bank-C1 file-select session wrapper that sets session flags, runs the loop, and normalizes transient state afterward.

## `C1:FF99`: C4 Text Layout Measurement Callback

`C1:FF99` has one direct caller:

- `C4:E5D6 -> C1:FF99`

The C4 caller has a text/data pointer staged in direct page and passes:

- `A` as the text/control value to measure
- `X` as a width-like quantity

`C1:FF99`:

- preserves the incoming `X` in `Y`
- copies the text/data pointer from caller direct-page fields `$22/$24` into `$0E/$10`
- calls `C4:3E31(A)` to compute a measurement
- subtracts that measurement from `incoming X * 8`
- halves the result and stores it in `$9E23`
- shifts it three more times and stores the coarser value in `$9E25`

This is a centering/layout metric callback used by the C4 text renderer, not file-select control logic by itself. It is adjacent to the file-select tail because the file-select path uses the same text-rendering machinery.

`C1:FF99..FFEF` is now source-backed as a mixed bank-end module. The trailing `C1:FFEF..10000` bytes remain modeled as terminal checksum constant/padding data, not executable code.

## Working Names

- `C1:FF2C` = `UpdateLeadEntityTypeRedrawFlag`
- `C1:FF6B` = `RunFileSelectSession`
- `C1:FF99` = `ComputeCenteredTextLayoutMetric`
- `C1:FFD3` = `ComputeBankC1ChecksumTail`

`C1:FF2C` still deserves a later cross-check against the exact object-record byte `+0x0E` meaning, but its caller/return contract and `$B4A2` latch behavior are now pinned down.
