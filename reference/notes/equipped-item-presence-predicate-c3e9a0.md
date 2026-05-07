# Equipped Slot Reference Predicate `C3:E9A0`

This note captures the local role of the bank-`03` helper at `C3:E9A0` and its bank-`01` `0x1D 10` wrapper.

## Main result

The corrected current local read is:

- `C3:E9A0` = test whether a requested equipped-slot reference value is present in any of the four equipped-reference bytes for the selected character
- `0x1D 10 -> C1:575D` = text-command wrapper around that predicate, with wildcard support and boolean result staging

This supersedes the older wording that treated `$99FF..$9A02` as direct equipped item-id bytes. The neighboring helper `C3:E9F7` dereferences these same four bytes into the character inventory region at `$99F1..`, which makes them look like equipped inventory-slot references rather than item ids.

## Working Names

- `C1:575D` = `TestEquippedItemPresenceForTextCommand`

## Predicate Role

So `0x1D 10` is no longer best described as a vague shop/helper leaf. It behaves like an equipped-item presence check.

## `C3:E9A0`

Entry behavior:

- `A` behaves like a 1-based character id
- `X` behaves like a 1-based equipped-slot reference value to test for

The helper then:

1. maps the selected character through the shared `0x5F`-stride record family
2. reads the four adjacent bytes at:
   - `$99FF`
   - `$9A00`
   - `$9A01`
   - `$9A02`
3. compares each of those bytes directly against the requested reference value
4. returns `1` on the first match, otherwise `0`

The important point is that this helper does not dereference the inventory list. It checks only the four equipped-reference bytes, not the 14-byte general inventory block at `$99F1..99FE`.

## Why this looks like equipped-slot reference presence

The local evidence lines up unusually well:

- the checked fields are exactly four bytes wide, which matches the equipment-side shape better than ordinary inventory
- sibling helper [item-slot-helper-pair-c3e977-c3ee14.md](notes/item-slot-helper-pair-c3e977-c3ee14.md) already established a four-slot equipment compatibility predicate through `C3:EE14`
- non-`0x1D` callers at `C1:9956`, `C1:A0F6`, and `C1:A860` use `C3:E9A0` in item-table / text-display flows that make much more sense as equipment-slot/reference checks than as a generic category test
- `C3:E9F7` reads each nonzero `$99FF..$9A02` byte, decrements it, and uses the result as an offset into `$99F1..`; that is the strongest local correction to the older direct-item-id interpretation

So the safest current read is that `$99FF..$9A02` are the selected character's four equipped inventory-slot reference bytes, and `C3:E9A0` is the corresponding membership test.

## `0x1D 10 -> C1:575D`

The bank-`01` leaf at `C1:575D` wraps that same predicate in the familiar text-command shape:

- it supports either an explicit character id or wildcard `A = #$00FF`
- on wildcard input, it loops the active-id family at `$986F` up to `$98A4`
- for each selected character, it forwards the requested reference value into `C3:E9A0`
- it stages the boolean result through `C1:045D`

So the best current command-level reading is: test whether the selected or active-party character currently has the given equipment slot/reference selected. The visible script-facing wording may still be "equipped item" in practice, but the low-level value passed to `C3:E9A0` is now better modeled as the reference byte itself.

## Confidence

- `C3:E9A0` as four-byte membership test over `$99FF..$9A02`: high confidence
- `$99FF..$9A02` as equipped inventory-slot reference bytes: medium-high confidence
- `0x1D 10` as equipment-reference presence check: medium confidence
