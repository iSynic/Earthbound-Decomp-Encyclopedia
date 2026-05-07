# Compact Item Category Classifier `C1:9EE6`

This note captures the local role of the bank-`01` helper at `C1:9EE6` and its current implications for `0x1D 02`.

## Main result

The safest current local read is:

## Working Names

- `C1:48AC` = `TestCurrentItemCompactCategory`
- `C1:9EE6` = `ClassifyItemCompactCategory`

`C1:9EE6..9F29` is now source-backed in `src/c1/c1_9ee6_classify_item_compact_category.asm`.

## Local Read

- `C1:9EE6` = compact item category classifier over item-table byte `+0x19`, using mask `0x30`
- `0x1D 02 -> C1:48AC` = compare the current item's compact category code against the command argument and stage a truthy result

So the inherited parser label `GET_PLAYER_HAS_INVENTORY_FULL` is almost certainly not describing the low-level mechanics of `0x1D 02`.

## `C1:9EE6`

Entry behavior:

- `A` behaves like a 1-based item id

The helper then:

1. maps the item through `C0:8FF7` with stride `#$0027`
2. lands on item-table byte `+0x19` in `D5:5000`
3. masks that byte with `0x30`
4. converts the masked value into a compact result:
   - `0x00 -> 1`
   - `0x10 -> 2`
   - `0x20 -> 3`
   - `0x30 -> 4`
   - anything else -> `0`

So the helper is not checking inventory fullness at all. It is reading a 2-bit category field already embedded in the item data. The broader packed-field model now lives in [item-byte-19-packed-class-and-slot.md](notes/item-byte-19-packed-class-and-slot.md).

## `0x1D 02 -> C1:48AC`

The `0x1D 02` leaf is simple once the classifier is named.

It:

1. resolves the current item id through `C1:03DC`
2. passes that item id into `C1:9EE6`
3. compares the returned compact class code against the command argument
4. stages `1` on match or `0` on mismatch through `C1:045D`

So the safest local command-level wording is something like "test whether the current item belongs to compact class N." The parser label `GET_PLAYER_HAS_INVENTORY_FULL` may still reflect how some scripts use that test, but it does not match the actual leaf behavior.

## Caller-side cross-checks

Three other local callers all reinforce the classifier reading.

- `C1:3FD5` uses `C1:9EE6 == 2` before branching into a more specific equipment-side path.
- `C1:9B79` does the same before decoding another item-table subfield at `+0x19 & 0x0C` and selecting one of the four equipped-reference bytes.
- `C1:A82C` also requires `C1:9EE6 == 2` before continuing into compatibility and equipped-item checks.

So class `2` is very likely the equippable-gear family, and the neighboring callers now make the packed layout much clearer: `C1:9B79` uses `+0x19 & 0x0C` as a four-way equipped-slot selector after the broad class check. The fuller shared-field writeup lives in [item-byte-19-packed-class-and-slot.md](notes/item-byte-19-packed-class-and-slot.md).

As a supporting cross-check, the community `Control_codes.txt` description for `0x1D 02` matches the local class split unusually well: class `1` as general non-equippable items, class `2` as equippable gear, class `3` as edible items, and class `4` as other usable items. That should still be treated as reference-backed rather than fully local semantic proof, but it is consistent with the ROM behavior.

## Confidence

- `C1:9EE6` as compact classifier over item byte `+0x19 & 0x30`: high confidence
- `0x1D 02` as direct compare against that classifier result: high confidence
- exact player-facing names of classes `1..4`: still tentative
