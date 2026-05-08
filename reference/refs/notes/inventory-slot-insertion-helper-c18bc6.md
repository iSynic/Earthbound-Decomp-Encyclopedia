# Inventory Slot Insertion Helper `C1:8BC6`

`C1:8BC6` is best read as the insertion-side mirror of [inventory-slot-removal-helper-c18c27.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/inventory-slot-removal-helper-c18c27.md).

## Main result

The bank-`01` shop/item family now has a matched pair:

- `C1:8BC6` = insert one item into a character inventory slot, with item-family-specific side effects
- `C1:8C27` = remove one item from a character inventory slot, maintain equipment-slot indices, and run the matching cleanup side effects

## Why this interpretation fits

`C1:8BC6` either:

- uses the explicit character id passed in `A`, or
- if `A == #$00FF`, scans the active id list at `$986F` up to `$98A4`

and then calls the inner helper `C1:8B2C`.

That inner helper does the local work.

### `C1:8B2C`

The helper computes the selected character's `0x5F`-stride record rooted at `99F1`, scans the 14-byte inventory region for the first zero byte, and writes the input item id there.

So the safest current read is:

- `99F1..99FE` = 14-byte inventory list
- `C1:8B2C` = insert one item id into the first empty slot of that list

If the list is full, it returns `0`.

If insertion succeeds, it returns the selected character id.

## Item-family-sensitive side effects

After inserting the item id, `C1:8B2C` resolves the item through the `D5:5000` table and runs the same special-family hooks we now see on removal, but in the insertion direction.

### Teddy Bear family

If item byte `+0x19 == 4`, the helper calls `C2:16DB`.

The item-table cross-check shows that this type is the Teddy Bear family:

- `2 = Teddy bear`
- `3 = Super plush bear`

So insertion of a Teddy Bear-family item triggers a Teddy-Bear-specific side-system update.

### Fresh Egg / Chick / Chicken family

If item byte `+0x1C` bit `0x10` is set, the helper calls `C3:EAD0`.

The only items with that bit set are:

- `92 = Fresh Egg`
- `168 = Chick`
- `169 = Chicken`

So this now reads best as the insertion-side refresh for the same tracked Fresh-Egg / Chick / Chicken family whose removal-side helper is `C3:EB1C`; see [teddy-bear-and-egg-item-cleanup-branches.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/teddy-bear-and-egg-item-cleanup-branches.md).

## Best current interpretation

The safest current read is:

- `C1:8BC6` inserts an item into the first empty inventory slot of a selected character
- wildcard character `#$00FF` means scan the active id list at `$986F`
- insertion of Teddy Bear-family items triggers the Teddy-Bear side system
- insertion of Fresh Egg / Chick / Chicken items triggers the egg-family presence/lifecycle side system

That makes it a very clean mirror of `C1:8C27`, even though the two routines are not exact structural inverses.

## Confidence

- `C1:8BC6` as inventory-slot insertion helper: high confidence
- `C1:8B2C` as first-empty-slot inserter over `99F1..99FE`: high confidence
- Teddy Bear and egg-family special-case hooks: high confidence
- exact broader meaning of the wildcard `$986F` scan: still slightly cautious
