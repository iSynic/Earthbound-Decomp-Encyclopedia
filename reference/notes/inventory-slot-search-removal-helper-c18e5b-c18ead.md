# Inventory Slot Search/Removal Helper Family `C1:8E5B` and `C1:8EAD`

These helpers are the take-side counterparts to [inventory-slot-insertion-helper-c18bc6.md](notes/inventory-slot-insertion-helper-c18bc6.md) and [inventory-slot-removal-helper-c18c27.md](notes/inventory-slot-removal-helper-c18c27.md).

## Main result

The current best local split is:

## Working Names

- `C1:8E5B` = `SearchAndRemoveItemFromCharacterInventory`
- `C1:8EAD` = `SearchAndRemoveItemFromActiveInventories`

Source-scaffold promotion:

- `C1:8E5B..8EAD` is now decoded source in `src/c1/c1_8e5b_search_and_remove_item_from_character_inventory.asm`.
- `C1:8EAD..8F0E` is now decoded source in `src/c1/c1_8ead_search_and_remove_item_from_active_inventories.asm`.
- The combined C1 scaffold validates byte-for-byte after promotion: `C1 byte-equivalence: OK, 172 module(s), 0 mismatch(es).`

## Helper Split

- `C1:8E5B` = search one character inventory for a requested item id, remove the first matching slot, and return the owning character id on success
- `C1:8EAD` = wrapper that applies that search/removal either to one explicit character or to the wildcard active-id family at `$986F..` up to `$98A4`

That makes `0x1D 01 -> C1:4C86` a real take-item search/removal wrapper, not just a parser-side label.

## `C1:8E5B`

Entry behavior:

- `A` behaves like a 1-based character id
- `X` behaves like a 1-based item id to search for

The helper then:

1. computes the selected character's `0x5F`-stride record rooted at `99F1`
2. scans the 14-byte inventory region at `99F1..99FE`
3. compares each byte against the requested item id
4. on the first match, calls [inventory-slot-removal-helper-c18c27.md](notes/inventory-slot-removal-helper-c18c27.md) with the matching 1-based slot index
5. returns the owning character id on success, or `0` if no matching item exists

So the safest current read is: search one character inventory for an item and remove the first matching entry.

## `C1:8EAD`

`C1:8EAD` is the outer wrapper used by the text-command family.

Entry behavior:

- `A` behaves like a 1-based character id, or `#$00FF` for wildcard search
- `X` behaves like the requested item id

Behavior split:

- if `A != #$00FF`, it just calls `C1:8E5B`
- if `A == #$00FF`, it scans the active-id family at `$986F`, bounded by `$98A4`, and calls `C1:8E5B` on each active entry until one succeeds

On success, it returns the character id that owned the removed item.

So the safest current read is: wildcard-aware search-and-remove wrapper over the active character/inventory family.

## Why this matters for `0x1D 01`

The front-half `0x1D` leaf now has a much firmer local shape:

- `0x1D 01 -> C1:4C86`
- resolves the item/character arguments from the live text context
- calls `C1:8EAD`
- stages the resulting owner character id through `C1:045D`

So `TAKE_ITEM_FROM_CHARACTER` is now locally supported as a real search/removal command family rather than just a parser-backed name.

## Relationship to neighboring bank-`03` helpers

The adjacent family at `C3:EC1F`, `C3:EC8B`, `C3:ED2C`, and `C3:ED98` is now mapped more concretely as the shared HP/PP adjust quartet behind the early `0x1E` commands; see [hp-pp-adjust-helper-quartet-c18f0e-c19010.md](notes/hp-pp-adjust-helper-quartet-c18f0e-c19010.md).

That family is useful context, but it is separate from the core search/removal role of `C1:8E5B` and `C1:8EAD`.

## Confidence

- `C1:8E5B` as per-character search-and-remove helper: high confidence
- `C1:8EAD` as explicit/wildcard wrapper over that helper: high confidence
- exact broader meaning of the wildcard `$986F` family in every subsystem: still cautious
