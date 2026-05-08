# Item Record Byte `+0x19` (Packed Class And Equip Slot)

This note captures the current local picture of item-table byte `+0x19` in the `D5:5000` item records.

## Main result

The safest current read is that item byte `+0x19` is a packed classification byte with at least two locally meaningful subfields:

- bits `4-5` = broad item class, exposed through `C1:9EE6` as compact classes `1..4`
- bits `2-3` = equippable-item slot subtype, used when the broad class is the equippable family

So `+0x19` is no longer best treated like an opaque item-type byte. It now looks like a compact class-and-subtype field shared by several bank-`01` helpers.

## Broad class via `C1:9EE6`

The bank-`01` helper `C1:9EE6`:

1. maps a 1-based item id through `C0:8FF7` with stride `#$0027`
2. lands on `D5:5000 + 0x19`
3. masks that byte with `0x30`
4. converts the masked value into a compact class code:
   - `0x00 -> 1`
   - `0x10 -> 2`
   - `0x20 -> 3`
   - `0x30 -> 4`
   - anything else -> `0`

That behavior is locally proved and is the key reason `0x1D 02` now reads as an item-class test rather than an inventory-fullness test.

## Equip-slot subtype via `C1:9B79`

The stronger local consumer of the remaining bits is `C1:9B79`.

That path:

1. requires `C1:9EE6 == 2` first
2. reloads the same item byte `+0x19`
3. masks it with `0x0C`
4. uses the result to choose one of the four equipped-item bytes in the selected character record:
   - `0x00 -> $99FF`
   - `0x04 -> $9A00`
   - `0x08 -> $9A01`
   - `0x0C -> $9A02`

So bits `2-3` behave like a four-way equipped-slot selector when the broad class says the item is equippable.

`C1:A82C` reinforces that same split: it also requires broad class `2` before continuing into compatibility and equipped-item checks.

## Current safest field sketch

The strongest current local sketch for item byte `+0x19` is:

- bits `4-5` = broad class
- bits `2-3` = equipped-slot subtype when broad class indicates equippable gear
- bits `0-1` = still locally unresolved
- bits `6-7` = not yet interpreted from the current caller set

## Reference-backed class names

The community `Control_codes.txt` cross-check matches the local behavior unusually well for `0x1D 02`:

- class `1` = general non-equippable items
- class `2` = equippable items
- class `3` = edible items
- class `4` = other usable items

That naming is reference-backed and locally consistent, but the mainline proof level should still be described that way rather than as fully local semantic proof for every class.

## Implications

This shared field now explains two formerly awkward bank-`01` leaves cleanly:

- `0x1D 02` tests the broad class from bits `4-5`
- the equipment-side helpers like `C1:9B79` and `C1:A82C` use the same broad class plus the slot subtype in bits `2-3`

So the remaining uncertainty is not whether `+0x19` is packed. That now looks strong. The remaining uncertainty is the exact semantic naming of every class and any remaining low/high-bit payloads outside the already proved masks.

## Confidence

- bits `4-5` as broad class field: high confidence
- bits `2-3` as equippable-slot selector: high confidence
- exact player-facing names of all four broad classes: medium confidence, reference-backed
- meanings of bits `0-1` and `6-7`: open
