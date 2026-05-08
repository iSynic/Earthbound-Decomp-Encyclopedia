# HP / PP Adjust Helper Quartet `C1:8F0E` .. `C1:9010`

This note captures the shared helper family behind the early bank-`01` `0x1E` recovery / depletion commands.

## Main result

The current safest local split is:

- `C1:8F0E -> C3:EC1F` = HP depletion helper family
- `C1:8F64 -> C3:EC8B` = HP recovery helper family
- `C1:8FBA -> C3:ED2C` = PP depletion helper family
- `C1:9010 -> C3:ED98` = PP recovery helper family

The other important correction is the `Y` split.

Inside each of those four families:

- `Y = 0` means percent-based adjustment
- `Y = 1` means direct amount-based adjustment

So the early `0x1E` block is not split by HP versus PP through `Y`. HP versus PP is determined by which helper family is called, while `Y` chooses percent versus amount.

## Bank-`01` wrappers

The live `0x1E` leaves line up cleanly:

- `0x1E 00 -> C1:49B6 -> C1:8F64` = recover HP percent
- `0x1E 01 -> C1:4A03 -> C1:8F0E` = deplete HP percent
- `0x1E 02 -> C1:4A50 -> C1:8F64` with `Y=1` = recover HP amount
- `0x1E 03 -> C1:4A9D -> C1:8F0E` with `Y=1` = deplete HP amount
- `0x1E 04 -> C1:4AEA -> C1:9010` = recover PP percent
- `0x1E 05 -> C1:4B37 -> C1:8FBA` = deplete PP percent
- `0x1E 06 -> C1:4B84 -> C1:9010` with `Y=1` = recover PP amount
- `0x1E 07 -> C1:4BD1 -> C1:8FBA` with `Y=1` = deplete PP amount

All four wrappers also support the wildcard `A = #$00FF` path, which loops the active-id family at `$986F` up to `$98A4` and applies the same adjustment per selected entry.

## Bank-`03` worker behavior

### `C3:EC1F` and `C3:EC8B`

These two operate on the HP-side derived-state pair:

- `$99D8` behaves like max HP
- `$9A15` behaves like current HP
- `$9A13` behaves like an HP-present / HP-active marker that is forced to `1` on recovery if still clear

Shared behavior:

- if `Y = 0`, the helper treats incoming `X` as a percent and computes `max * percent / 100` through `C0:9086` and `C0:90FF`
- if `Y = 1`, it treats incoming `X` as the direct amount

Then:

- `C3:EC1F` subtracts that amount from current HP at `$9A15`, flooring at `0`
- `C3:EC8B` adds that amount into current HP at `$9A15`, capping at max HP `$99D8`

`C3:EC8B` also sets the paired marker at `$9A13` to `1` if it was still `0`.

### `C3:ED2C` and `C3:ED98`

These are the PP-side mirrors:

- `$99DA` behaves like max PP
- `$9A1B` behaves like current PP
- `$9A19` behaves like a PP-present / PP-active marker that is forced to `1` on recovery if still clear

Shared behavior matches the HP side:

- `Y = 0` computes `max * percent / 100`
- `Y = 1` uses the direct amount

Then:

- `C3:ED2C` subtracts that amount from current PP at `$9A1B`, flooring at `0`
- `C3:ED98` adds that amount into current PP at `$9A1B`, capping at max PP `$99DA`

`C3:ED98` also sets the paired marker at `$9A19` to `1` if it was still `0`.

## Why this matters

This tightens the early `0x1E` family quite a bit.

What used to be only parser-order-backed is now mostly local:

- HP versus PP is locally determined by which helper family runs
- percent versus amount is locally determined by `Y`
- recovery versus depletion is locally determined by the bank-`03` worker body
- the wildcard active-party path is common to all four

So the early `0x1E` block is no longer just ?probably the recover/deplete family because the macro list says so.? It is now a locally coherent quartet of HP/PP add/subtract helpers with a proved percent/amount split.

## Confidence

- helper-family split into HP recover / HP deplete / PP recover / PP deplete: high confidence
- `Y=0` percent and `Y=1` amount: high confidence
- `$99D8/$9A15` as max/current HP pair: high confidence
- `$99DA/$9A1B` as max/current PP pair: high confidence
- `$9A13/$9A19` as paired nonzero/currently-active markers: medium confidence
