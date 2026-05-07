# Staged Movement Wrapper at `C0:70CB`

This note captures the current ROM-first interpretation of `Queue_StagedMovementFromGridCoords` at `C0:70CB` and its helper `Select_StagedMovementFacing` at `C0:705F`.

## Scope

- This routine is now decoded cleanly in `notes/bank-c0-first-pass.md` because the bank-C0 helper understands opcode `7F` (`ADC long,X`).
- Direct-caller scan shows one confirmed caller so far: `JSR C0:70CB` at `C0:75AF`.
- The current interpretation is still partly inferential, but the byte-level structure is much firmer than before.

## Verified structure from the ROM

- `C0:70CB` takes a packed mode word in `A` and two coordinate-like inputs in `Y` and `X`.
- It preserves the original mode word in `$16`, stores the incoming `Y` in `$02`, copies incoming `X` into `$18`, and scales both `$02` and `$18` by 8.
- The high byte of the original mode word becomes a 0-3 selector in `$04`.
- That selector is also shifted back into the high byte and stored in `$5DC4`, which matches the later callback checks against `#$0000`, `#$0100`, `#$0200`, and `#$0300`.
- If `$9883` is zero, the routine first calls `Select_StagedMovementFacing` at `C0:705F`. If that helper returns nonzero, the wrapper aborts early.
- On the success path, the wrapper copies `$5DCA -> $987F`, clears `$5DB8`, writes `$5D56 = #$0003`, and writes `$5DBA = #$0001` before staging target coordinates.
- The primary target pair is built from:
  - `scaled X + C3:E210[index]`
  - `scaled Y + C3:E218[index]`
- The alternate target pair is built from:
  - `scaled X + C3:E220[index]`
  - `scaled Y + C3:E228[index]`
- After building a target pair, the wrapper calls `JSL $C48D58` with live position from `$9877/$987B` and the staged target in `Y/A`, then normalizes the returned delay so it is never zero.
- The wrapper then calls `JSL $C48E6B` with one table-driven parameter from `C3:E200` or `C3:E208` plus a small constant index (`#$0006` or `#$000C`).
- Finally it arms either `TimerCallback_WaitForStagedY_State0D` (`C0:6F82`) or `TimerCallback_WaitForStagedY_ClearMotion` (`C0:6FED`) through `Queue_DelayedActionTimer`, stores the staged target into `$5DCC/$5DCE`, calls `JSL $C48E95`, and returns.

## Table contents

For selector values `0..3`, the tables currently decode as:

- `C3:E200`: `0007 0001 0005 0003`
- `C3:E208`: `0002 0006 0002 0006`
- `C3:E210`: `0000 0008 0000 0008`
- `C3:E218`: `0000 0000 0008 0008`
- `C3:E220`: `0008 0000 0008 0000`
- `C3:E228`: `0008 0008 0000 0000`

The strongest current interpretation is:

- `C3:E210/E218` are one 4-entry set of 8-pixel sub-tile offsets.
- `C3:E220/E228` are the alternate 4-entry set of 8-pixel sub-tile offsets.
- `C3:E200/E208` are direction-like or movement-parameter tables consumed by `C48E6B`.

## Helper at `C0:705F`

`Select_StagedMovementFacing` does three concrete things:

- It inspects the high-byte mode family via comparisons against `#$0000`, `#$0100`, `#$0200`, and `#$0300`.
- It reads current state from `$987F`.
- It chooses one of two shadow-facing values in `$5DCA`: `#$0002` or `#$0006`.

The helper returns `A = 0` on the path where the main wrapper should continue and `A = 1` on the path where it should abort.

What is still uncertain is the exact semantic meaning of `$987F` and `$5DCA`. The legacy reference names `$987F` as player facing direction, and ROM-local cross-references support that broadly, but we have not yet proven the exact value encoding.

## Current interpretation

The wrapper no longer looks like a generic timer helper. It looks like a staged movement setup routine that:

- starts from grid-like coordinates,
- chooses one of two sub-tile target families,
- derives a delay from current live position to the staged target,
- seeds movement-state words in `$5D56/$5DBA/$5DC4/$5DCA`, and
- hands off completion to the delayed timer callbacks at `C0:6F82` or `C0:6FED`.

A reasonable working description is: queued staged movement toward one of several 8-pixel offset targets, with callback-driven completion.

## Best next target

- Decode the caller/selector around `C0:75AF` and the table family rooted at `$5DEA`, because that is what chooses `C0:70CB` instead of its sibling helpers at `C0:6A8B`, `C0:6A8E`, `C0:6A91`, `C0:6ACA`, and `C0:6E6E`.
