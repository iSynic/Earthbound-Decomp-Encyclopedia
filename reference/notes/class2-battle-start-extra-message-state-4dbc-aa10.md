# Class2 Battle-Start Extra Message State 4DBC AA10

This note captures the current best read on the small battle-start state pair around WRAM `$4DBC` and `$AA10`.

See also [class2-b6eb-caller-family-4dxx.md](notes/class2-b6eb-caller-family-4dxx.md).
See also [class2-005e-record-domain.md](notes/class2-005e-record-domain.md).
See also [class2-d59589-enemy-data-crosswalk.md](notes/class2-d59589-enemy-data-crosswalk.md).
See also [class2-c1-display-text-substitution-handler-7af3.md](notes/class2-c1-display-text-substitution-handler-7af3.md).
See also [class2-ufo-present-message-family.md](notes/class2-ufo-present-message-family.md).

## Working Names

- `C2:3109` = `BattleStartUfoPresentFallbackTable`

## Main result

The battle-start preamble in `C2:4D7D..4EEC` uses two small WRAM values with clearly different roles:

- `$4DBC` is an upstream battle-start mode byte written in bank `C0` and consumed once by the `4Dxx -> 4Fxx` family
- `$AA10` is a local battle-start selector seeded from enemy-data bytes `+0x57/+0x58`, sometimes zeroed by chance logic, and sometimes repopulated by a fallback UFO/item scan

Neither one looks like generic scratch anymore.

## `$4DBC` is upstream state, not a local temporary

A whole-bank scan found only three writes to `$4DBC`, all in bank `C0`:

- `C0:D233` -> `STZ $4DBC`
- `C0:D243` -> `STA $4DBC` with value `1`
- `C0:D253` -> `STA $4DBC` with value `2`

On the consuming side in bank `C2`:

- `C2:4ECF` reads `$4DBC`
- `C2:4EEC` immediately clears it again
- the read value is normalized into local `$1D`

So `$4DBC` is best read as one-shot upstream battle-start mode state.

## What sets `$4DBC`

The writer cluster at `C0:D1F0..D253` derives two booleans from masked `& 7` comparisons, then encodes them into `$4DBC`:

- default is `0`
- one comparison pattern stores `1`
- the opposite comparison pattern stores `2`

I am not naming those values yet, but the shape looks much more like approach or orientation state than like a generic text id.

That fits the consumer-side behavior well: the value is sampled once at battle start and then cleared.

## `$AA10` is seeded from enemy-data `+0x57/+0x58`

The local bytes at `C2:4D7D..4E3C` show a concrete use of two tail bytes from `D5:9589`:

- `enemy_data + 0x58` is loaded first and stored to `$AA10`
- `enemy_data + 0x57` is then read as a small mode value `0..6`
- that mode chooses a random-mask filter through `JSL C0:8E9A`
- if the chosen filter fails, `$AA10` is cleared back to zero

The filter masks are progressively narrower:

- mode `0` -> keep `AA10` as-is
- mode `1` -> random `& 0x7F`
- mode `2` -> random `& 0x3F`
- mode `3` -> random `& 0x1F`
- mode `4` -> random `& 0x0F`
- mode `5` -> random `& 0x07`
- mode `6` -> random `& 0x03`
- final fallback -> random `& 0x01`

If the masked result is zero, the code clears `$AA10`.

## Why that matters

This is the first clear local battle-start consumer for the `enemy_data + 0x57/+0x58` pair.

It also creates a useful caution: the local behavior does not fit cleanly with the reference names we had borrowed for those fields.

So the safest current statement is:

- `+0x57/+0x58` definitely participate in a battle-start extra-message or selector path locally
- the exact semantic names of those two fields still need verification
- the overall enemy-data match remains strong, but these two tail fields should stay tentative

## How `$AA10` feeds the battle-start family

At `C2:4E3C`, the family checks `$AA10`:

- if `$AA10 != 0`, it jumps straight into the main encounter-text path at `C2:4ECD`
- if `$AA10 == 0`, it falls into the fallback scan at `C2:4E4B..4EBC`

The fallback scan is now decoded enough to describe mechanically:

- it scans battler slots `8..31`
- it ignores battlers whose `consciousness` byte at `+0x0C` is zero
- it compares each live battler's id field at `+0x00` against a small hardcoded record table at `C2:3109`
- on a match, it chooses one of eight follow-up bytes from that record with
  `C2:6A2D` / `GetRandomBelow`
- it stores that chosen byte back into `$AA10`
- then it continues until either two records are checked or the fallback loop terminates

So `$AA10` is best read as a battle-start selector value, not as arbitrary scratch.

## The fallback table at `C2:3109`

The `C2:3109` data turned out to be a pair of 9-byte records, not a 5-byte table.

A later pass also corrected an important detail: these records are mixed-domain, not "all enemy ids."

The first two records are:

- record 0: `84 58 59 5A 5B 5C 5D 5F 00`
- record 1: `85 6A 6B 6C 6D 6E 6F 70 00`

Mechanically, each record is:

- byte `0`: a battler enemy id to match against `BATTLERS_TABLE + 0x00`
- bytes `1..8`: eight candidate bytes, one of which is chosen and copied into `$AA10`

The matching ids are:

- `84` -> `Cute Li'l UFO`
- `85` -> `Beautiful UFO`

The candidate bytes make better sense as item ids:

- record 0 candidates -> `COOKIE`, `BAG_OF_FRIES`, `HAMBURGER`, `BOILED_EGG`, `FRESH_EGG`, `PICNIC_LUNCH`, `PIZZA`, `null`
- record 1 candidates -> `CAN_OF_FRUIT_JUICE`, `ROYAL_ICED_TEA`, `PROTEIN_DRINK`, `KRAKEN_SOUP`, `BOTTLE_OF_WATER`, `COLD_REMEDY`, `VIAL_OF_SERUM`, `null`

That makes the fallback path look much more like a UFO-specific present-content selector than like a linked-enemy selector.

## Why `$AA10` now looks item-like instead

The strongest later clue is from the downstream readers in bank `C2`.

At `C2:6003` and `C2:8881`, the code:

- tests `$AA10`
- switches to 8-bit `A`
- loads `$AA10`
- calls `JSL C1:DD7C`
- then displays a hardcoded `EF` battle-text pointer through `C1:DC1C`

The helper at `C1:DD7C` is itself tiny:

- `REP #$31`
- `JSR C1:ACF8`
- `RTL`

That ties `$AA10` directly back into the same `C1` substitution-helper family we had already associated with battle-text context setup.

A later local pass tightened the message side too:

- `C2:6003` dispatches `EF:7BDF`
- `C2:8881` dispatches `EF:7DD5`
- those addresses are now identified from `earthbound.yml` as `MSG_BTL_PRESENT` and `MSG_BTL_CHECK_PRESENT_GET` in `EBATTLE8`
- `EF:7DD5` contains `1F 02 10` (sound effect `PRESENT_OPENED`) and `1C 05 00` (`PRINT_ITEM_NAME 0`)

So the safest current read is:

- `$AA10` is probably not a raw message-number flag
- it behaves much more like an item-like present-content substitution input used by later battle text

## Current safest interpretation

The safest interpretation is:

- `$4DBC` is upstream battle-start mode state written in bank `C0`
- `$1D` is the local normalized copy of that mode in the `4Dxx -> 4Fxx` battle-start family
- `$AA10` is a second battle-start selector value derived from `enemy_data + 0x57/+0x58` and fallback UFO/item logic
- the fallback path around `C2:3109` matches `Cute Li'l UFO` and `Beautiful UFO`, then chooses one of several item ids to store in `$AA10`
- later code treats `$AA10` as a present-family battle-text substitution input rather than a plain boolean flag

## Best next target

The best next move is to pin the exact display-text token that consumes `$9D11`, or to decode the `EF:7BDF` and `EF:7DD5` scripts far enough to say exactly how this present-content substitution value appears in the player-visible battle lines.
