# Offensive / Defensive Item Check `C1:7708`

This note captures the current local role of the bank-`01` helper at `C1:7708`, which is the live leaf for `0x1D 23`.

## Main result

The safest current read is:

- `0x1D 23 -> C1:7708`
- `C1:7708` = small equippable-item subtype classifier
- return `1` for the first equipment subtype (`+0x19 & 0x0C == 0x00`)
- return `2` for the other three equipment subtypes (`0x04`, `0x08`, `0x0C`)
- return `0` for anything outside those expected subtype values

## Working Names

- `C1:7708` = `ClassifyEquippedItemOffensiveDefensive`

Source-scaffold promotion:

- `C1:7708..776A` is now decoded source in `src/c1/c1_7708_classify_equipped_item_offensive_defensive.asm`.
- The same module also carries the adjacent statistic-selector staging leaf at `C1:776A..7796`.
- The combined C1 scaffold validates byte-for-byte after promotion: `C1 byte-equivalence: OK, 172 module(s), 0 mismatch(es).`

With the community control-code cross-check, the best current command-level wording is `Offensive or Defensive Item Check`: locally it distinguishes one offensive equipment subtype from the remaining defensive/accessory-like subtypes.

## Local body

`C1:7708` accepts an item id either from explicit `X` or, when `X == 0`, from the live text context through `C1:03DC`. It then:

1. maps the item through `C0:8FF7` with stride `#$0027`
2. lands on item-table byte `+0x19` in `D5:5000`
3. masks that byte with `0x0C`
4. returns:
   - `1` when the masked subtype is `0x00`
   - `2` when the masked subtype is `0x04`, `0x08`, or `0x0C`
   - `0` otherwise
5. stages the result through `C1:045D`

So the helper is not doing a broad class check itself. It assumes the item byte already carries a meaningful four-way subtype in bits `2-3`, and then collapses that into a `weapon` versus `everything else equippable` style split.

## Relationship to item byte `+0x19`

The shared field map in [item-byte-19-packed-class-and-slot.md](notes/item-byte-19-packed-class-and-slot.md) already showed that bits `2-3` of `+0x19` act like a four-way equipped-slot selector when the item is equippable. `C1:7708` now gives that field a second, simpler view:

- subtype `0x00` = offensive branch
- subtypes `0x04`, `0x08`, `0x0C` = non-offensive branch

That is exactly the kind of collapse a shop script would want when deciding between weapon-flavored and armor/accessory-flavored follow-up text.

## Script-side cross-check

The only exposed parsed hit is in `ESHOP1` at `C5:E25B`:

- `UNKNOWN_1D_23 0x00`
- `TEST_IF_WORKMEM_TRUE 0x01`
- on true, set `flag 0x0292`

That pattern matches the local body very well: the script is branching only on whether the helper returned `1`, not on the exact three-way or four-way subtype.

The community `Control_codes.txt` entry matches this unusually closely and calls `0x1D 23` `Offensive or Defensive Item Check`, with return `1` for weapons and `2` for items meant to be equipped on the character instead. That wording should still be treated as reference-backed, but it is strongly locally consistent with the ROM behavior.

## Confidence

- `0x1D 23 -> C1:7708`: high confidence
- return `1` for subtype `0x00`, `2` for `0x04/0x08/0x0C`, `0` otherwise: high confidence
- semantic naming as offensive versus defensive/non-weapon equipment: medium-high confidence, reference-backed and locally consistent
