# Bank Deposit Accumulator `$98B9/$98BB`

This note captures the current local role of the WRAM pair `$98B9/$98BB` and its bank-`01` front end `0x1D 24 -> C1:7274`.

## Main result

The safest current read is:

- `$98B9/$98BB` = cached 32-bit bank-deposit accumulator
- `0x1D 24 -> C1:7274` = stage that accumulator into the active text context
- command argument `2` = clear the accumulator after staging it

## Working Names

- `C1:7274` = `StageBankDepositAccumulatorTextValue`

Source-scaffold promotion:

- `C1:7274..72BC` is now decoded source in `src/c1/c1_7274_stage_bank_deposit_accumulator_text_value.asm`.
- The same source module carries the adjacent small `0x1F` event-helper leaves through `C1:7440`.
- The combined C1 scaffold validates byte-for-byte after promotion: `C1 byte-equivalence: OK, 172 module(s), 0 mismatch(es).`

Source polish follow-up (2026-05-06): the `C1:7274..7440` source module now
names its helper-call surface, including the standard primary-context installer
used by this accumulator leaf plus the adjacent special-event, photographer,
attached-child, and battle visual effect helper calls.

So the older wording that treated `$98B9/$98BB` like a far-pointer pair is no longer the best fit. The local code and the `ESHOP3` script neighborhood both line up much better with a running deposited-money total.

## `C1:7274`

The live leaf for `0x1D 24` is `C1:7274`. It:

1. reads low word `$98B9` and high word `$98BB`
2. stages that 32-bit value through the standard `C1:045D` context installer
3. if the command argument is `2`, zeros both `$98B9` and `$98BB` after staging them

So the leaf is not computing a new amount. It is exposing a cached accumulator to the text engine, with optional clear-on-consume behavior.

## Local writers

The strongest local writers are in bank `C2`:

- `C2:5F3D..5F7D`
- `C2:6279..62B9`

Both sequences:

1. take a 16-bit running amount from `$A978` (or its local equivalent)
2. convert or extend it through `C2:281D`
3. add that result into `$98B9/$98BB` as a 32-bit quantity
4. store the new accumulated total back to `$98B9/$98BB`

That is arithmetic on a dword accumulator, not pointer math on a far address.

## Script-side cross-check

The exposed `ESHOP3` hits now make much more sense under the accumulator model:

- `0x1D 24 0x01`
- `JUMP_IF_FALSE ...`
- print `deposited $... to your bank account`
- later `0x1D 24 0x02`

That is exactly what we would expect from:

- `0x01` = fetch the current deposited-total value without clearing it
- `0x02` = fetch it again and then clear it for the next reporting cycle

## Reference-backed wording

The community `Control_codes.txt` entry matches the local model unusually well here. It describes `0x1D 24` as returning the cash earned since the last Dad call, with argument `2` also resetting the value to zero. That should still be treated as reference-backed wording, but it is strongly locally consistent with the ROM behavior.

## Confidence

- `$98B9/$98BB` as cached 32-bit accumulator rather than pointer pair: high confidence
- `0x1D 24 -> C1:7274` as stage-and-optional-clear front end: high confidence
- exact player-facing semantic wording as Dad/bank deposited-cash total: medium-high confidence, reference-backed and locally consistent
