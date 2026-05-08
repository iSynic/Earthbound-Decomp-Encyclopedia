# Item/Slot Helper Pair `C3:E977` and `C3:EE14`

These two bank-`03` helpers recur in the bank-`01` shop/item command families and are now strong enough to treat as reusable local anchors.

## `C3:E977`

`C3:E977` is best read as a compact 1-based character inventory-slot byte accessor.

Local shape:

- entry `A` behaves like a 1-based character id
- entry `X` behaves like a 1-based inventory-slot selector
- the routine computes `(character - 1) * 0x5F + 0x99F1 + (selector - 1)`
- it returns the byte stored at that computed address

The strongest local clues are the arithmetic and the fixed stride:

- the helper uses `C0:8FF7` with `Y = #$005F`
- it adds base `C3:99F1`
- it adds the decremented selector byte as a small in-record offset
- it returns a single byte

So the safest current read is: this is a generic byte accessor over the 14-byte inventory region at the front of each `0x5F`-stride character record rooted at `C3:99F1`, not an item classifier or text-only helper.

## `C3:EE14`

`C3:EE14` is best read as a small equipment-slot compatibility predicate.

Local shape:

- entry `A` behaves like a 1-based equipment-slot selector
- entry `X` behaves like a 1-based item id
- the routine resolves the item through the `D5:5000` item table using stride `0x27`
- it reads item byte `+0x1C`
- it ANDs that byte with one of four masks from `C4:58AB`
- it returns `1` if the masked result is nonzero, otherwise `0`

The strongest local clue is the tiny mask table itself. The first four bytes at `C4:58AB` are:

- `0x01`
- `0x02`
- `0x04`
- `0x08`

That is exactly the shape you would expect for a four-slot compatibility mask. I am still keeping the final slot names cautious here, but the overall behavior now looks much more like "can this item be equipped in this selected slot?" than any broader item-property test.

This also matches the contextual reuse unusually well:

- `C1:57CD` uses it in the `0x1D 11` inventory-item usability branch
- the quarantined `ebsrc-main` tree reuses `UNKNOWN_C3EE14` in `switch_weapon.asm` and `switch_armor.asm`

So the safest current read is: `C3:EE14` is a slot-vs-item compatibility test, very likely for the four equip slots.

## Current value to the project

These two helpers tighten several bank-`01` notes:

- `0x1D 0F` now reads more concretely as a paired resolver using a character-side byte from `C3:E977` and a recipient/service-side value from `C1:8C27`
- `0x1D 11` now reads more concretely as a direct inventory-item usability/equipability check that uses `C3:E977` to fetch one inventory item id and `C3:EE14` to test whether that item can be equipped in the selected slot for the selected character
- the equipment/shop side can now lean on a real local helper pair instead of repeating vague "item-side helper" wording

## Confidence

- `C3:E977` as a generic character-field byte accessor: high confidence
- `C3:EE14` as a four-slot equipment compatibility predicate: high confidence
- exact human-facing names of the four slots: still slightly tentative
