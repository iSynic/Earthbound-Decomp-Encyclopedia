# Delivery Row Helpers (`EF:0CA7` / `EF:0D23` / `EF:0D46` / `EF:0D73` / `EF:0D8D` / `EF:0DFA` / `EF:0E67` / `EF:0E8A` / `EF:0EAD` / `EF:0EE8`)

This note captures the bank-`EF` helper family that makes the `D5:F645` delivery table readable in local control flow.

See also [selector-row-config-family-ef0ee8.md](notes/selector-row-config-family-ef0ee8.md).
See also [post-transition-deferred-script-queue-c06b21-c06bff.md](notes/post-transition-deferred-script-queue-c06b21-c06bff.md).

## Main result

These helpers now split into five clean groups:

- retry-threshold helpers
- per-row countdown helpers
- per-row script-pointer queue helpers
- current-row speed helpers
- row-selection and instantiation helpers

The strongest current local read is:

- `EF:0CA7` = increment current row retry counter and compare against record word `2`
- `EF:0D23` = return current row record word `3`
- `EF:0D46` = seed current row countdown from record word `4`
- `EF:0D73` = decrement that current row countdown
- `EF:0D8D` = queue current row pointer `1` as immediate type `#$0008`
- `EF:0DFA` = queue current row pointer `2` as deferred type `#$000A`
- `EF:0E67` = get current row word `8`
- `EF:0E8A` = get current row word `9`
- `EF:0EAD` = instantiate a chosen delivery row's sprite or placeholder
- `EF:0EE8` = scan all rows by event flag and instantiate the first enabled row

## `EF:0CA7`: retry-threshold helper for record word `2`

`EF:0CA7` seeds a table base at `D5:F645`, resolves the current row from `0E5E[current_entity]`, and then reads record word `2` at offset `+0x04`.

Its control flow then:

1. returns `1` immediately if word `2 == FFFF`
2. otherwise increments a per-row WRAM counter at `B511 + row * 2`
3. compares the incremented counter against record word `2`
4. returns `1` once the counter reaches or exceeds the record value, otherwise `0`

That makes record word `2` read much more like a retry-threshold or attempt-count field than a free-form scalar.

## `EF:0D23`: current-row accessor for record word `3`

`EF:0D23` is the matching simple accessor for record word `3` at offset `+0x06`.

By itself that only proves the field is real. The script-side usage below is what makes it interpretable.

## Why words `2` and `3` now look like retry-count and retry-wait fields

The strongest evidence is the shared event script [499+500_common.asm](refs/ebsrc-main/ebsrc-main/src/data/events/scripts/499+500_common.asm).

Inside `UNKNOWN_C3443E` it does:

1. `EVENT_UNKNOWN_EF0CA7`
2. branch out if that helper says the threshold has been reached
3. `EVENT_UNKNOWN_EF0D23`
4. `EVENT_LOOP_TEMPVAR` with `EVENT_PAUSE 1*SECOND`

That means the return from `EF:0D23` is being used directly as a one-second loop count in the retry path.

So the cleanest current read is:

- word `2` = retry-attempt threshold / max retry count
- word `3` = retry wait in seconds

This also matches the concrete table values very well:

- most rows use `0006, 000F` = six attempts with fifteen-second waits
- the HoiHoi row uses `00FF, 00FF` in the byte-equivalent D5 scaffold, which
  fits a very long retry policy; the code still supports `FFFF` as an
  immediate-success sentinel, but that sentinel is not observed in the current
  row data

## `EF:0D46`: seed the per-row delivery countdown

`EF:0D46` does:

1. read the current entity index from `$1A42`
2. load that entity's cached delivery row from `0E5E,X`
3. scale the row by `20`
4. read `D5:F645 + row * 20 + 0x08`
5. store that word into `B525 + row * 2`

So this helper seeds a per-row WRAM countdown from record word `4`.

## `EF:0D73`: decrement the per-row delivery countdown

`EF:0D73` recomputes the same row-local slot in `B525` and decrements it if nonzero.

That makes the `0D46 -> 0D73` pair a strong local proof that record word `4` is a countdown-like field.

Combined with the reference `timed_delivery` struct and the concrete values in
`D5:F645`, now summarized in
[d5-timed-delivery-row-contracts.md](notes/d5-timed-delivery-row-contracts.md),
the cleanest current read is:

- word `4` = `delivery_time`

CoilSnake cross-check: `timed-delivery-first-timer-probe` changed
`timed_delivery_table.yml` row 0 `Timer` from `180` to `181` and produced a
single rebuilt-ROM byte change at `D5:F64D`. That is exactly `D5:F645 + 0x08`,
the low byte read by `EF:0D46`. The older D5 split front door still starts
`TIMED_DELIVERY_TABLE` at `D5:F649`, so the field is runtime-proven while the
source split boundary remains a focused follow-up.

## `EF:0D8D`: queue current row pointer `1`

`EF:0D8D` builds a far pointer from the current row:

- bank byte from `D5:F645 + row * 20 + 0x0C`
- low word from `D5:F645 + row * 20 + 0x0A`

That is exactly record pointer `1` at bytes `10..12`.

It stages that far pointer into `$0E/$10` and then calls `C064E3` with:

- `A = #$0008`

So the current best read is:

- pointer `1` = queued as WRAM queue type `#$0008`
- queue type `#$0008` is handled by `C0:75DD` through the direct `JSL $C10004` pointer-dispatch path
- so pointer `1` looks like the immediate success-side text or presentation pointer

## `EF:0DFA`: queue current row pointer `2`

`EF:0DFA` does the same construction for the second packed pointer:

- bank byte from `D5:F645 + row * 20 + 0x0F`
- low word from `D5:F645 + row * 20 + 0x0D`

That is record pointer `2` at bytes `13..15`.

It stages that far pointer into `$0E/$10` and then calls `C064E3` with:

- `A = #$000A`

So the current best read is:

- pointer `2` = queued as WRAM queue type `#$000A`
- queue type `#$000A` is the narrower deferred far-script-pointer class already traced through `C06B3D` / `C06BFF`
- so pointer `2` looks like the deferred failure-side or follow-up pointer

This is a strong local bridge from the delivery table into the shared deferred-script queue family.

## `EF:0E67`: current-row speed helper A

`EF:0E67` does:

1. read the current entity index from `$1A42`
2. load that entity's cached delivery row from `0E5E,X`
3. scale the row by `20`
4. read `D5:F645 + row * 20 + 0x10`
5. return that word

So this helper is a pure field getter for record word `8`.

## `EF:0E8A`: current-row speed helper B

`EF:0E8A` is the same pattern, but it reads:

- `D5:F645 + row * 20 + 0x12`

So it is the paired getter for record word `9`.

## Why words `8` and `9` still look like `enter_speed` / `exit_speed`

The strongest evidence is behavioral, not just structural.

In the `ebsrc` event script [499+500_common.asm](refs/ebsrc-main/ebsrc-main/src/data/events/scripts/499+500_common.asm):

- `EVENT_UNKNOWN_EF0E67` is used in the earlier arrival-side branch `UNKNOWN_C344DE`
- `EVENT_UNKNOWN_EF0E8A` is used in the later departure-side branch `UNKNOWN_C344A8`

Both branches immediately feed the returned value into the same movement-side helper family around `C0:A685`, which is exactly what we would expect for paired arrival/departure speeds.

So the cleanest current read remains:

- word `8` = `enter_speed`
- word `9` = `exit_speed`

## `EF:0EAD`: instantiate delivery sprite or placeholder

`EF:0EAD` takes a 1-based row selector in `A` and then:
A new bank-`01` bridge now supports that row-selector interpretation locally: `C1:7440`, the low word returned by text command `0x1F D3`, is a tiny adapter that does `TXA ; JSL EF:0EAD ; LDA #0 ; RTS`. So the timed-delivery text-command path is now directly tied back into this helper family by local bytes, not just by script structure.


1. decrements it and stores the zero-based row to `0A38`
2. scales the row by `20`
3. loads record word `0` from `D5:F645`
4. if that sprite id is zero, calls `C08E9A`, masks the result with `#0003`, and uses `C3:FDBD` as a placeholder table
5. clears `$0E/$10`
6. calls `C01E49` with `Y = FFFF` and `X = 01F3`

So this helper is the row-to-visible-entity bridge for a chosen delivery row.

## `EF:0EE8`: scan rows by event flag and instantiate

`EF:0EE8` is the table walker.

For each of the 10 rows it:

1. computes `entry = D5:F645 + row * 20`
2. loads record word `1` at offset `+0x02`
3. tests that word through `C21628`
4. if the flag is set, stores the row index to `0A38`
5. loads record word `0`
6. falls back to the same placeholder path if the sprite id is zero
7. calls `C01E49` with `Y = FFFF` and `X = 01F4`

So the corrected split is:

- record word `1` = event-flag gate
- record word `0` = sprite/object descriptor id

## Relationship to the selector-row cache

These helpers are the cleanest local explanation for how the delivery table feeds the visual-selector family:

- chosen row index -> `0A38`
- later copied to `0E5E`
- later mirrored to `2C22`

That means the delivery row is one source for the broader selector-row path, but the row id and the sprite id are still separate values.

## Script anchor

The shared event script [499+500_common.asm](refs/ebsrc-main/ebsrc-main/src/data/events/scripts/499+500_common.asm) is the strongest current runtime anchor for this family.

It uses:

- `EVENT_UNKNOWN_EF0D73` at the one-second looped pre-check stage
- `EVENT_UNKNOWN_EF0CA7` / `EVENT_UNKNOWN_EF0D23` in the bounded retry-and-wait branch
- `EVENT_UNKNOWN_EF0FDB` in the branch that starts a delivery/service arrival sequence
- `EVENT_UNKNOWN_EF0FF6` in the branch that tears the sequence down again
- `EVENT_UNKNOWN_EF0E67` in the approach/arrival-side movement branch
- `EVENT_UNKNOWN_EF0E8A` in the leave/departure-side movement branch

That makes the family read much more like a real timed-delivery controller than an unrelated collection of small helpers.
