# Equipped Item Presence Predicate `C3:E9A0`

This note captures the local role of the bank-`03` helper at `C3:E9A0` and its bank-`01` `0x1D 10` wrapper.

## Main result

The safest current local read is:

- `C3:E9A0` = test whether a requested item id is currently present in any of the four equipped-item bytes for the selected character
- `0x1D 10 -> C1:575D` = text-command wrapper around that predicate, with wildcard support and boolean result staging

So `0x1D 10` is no longer best described as a vague shop/helper leaf. It behaves like an equipped-item presence check.

## `C3:E9A0`

Entry behavior:

- `A` behaves like a 1-based character id
- `X` behaves like a 1-based item id to test for

The helper then:

1. maps the selected character through the shared `0x5F`-stride record family
2. reads the four adjacent bytes at:
   - `$99FF`
   - `$9A00`
   - `$9A01`
   - `$9A02`
3. compares each of those bytes directly against the requested item id
4. returns `1` on the first match, otherwise `0`

The important point is that these are not inventory scans. The helper checks only the four equipped-item bytes, not the 14-byte general inventory block at `$99F1..99FE`.

## Why this looks like equipped-item presence

The local evidence lines up unusually well:

- the checked fields are exactly four bytes wide, which matches the equipment-side shape better than ordinary inventory
- sibling helper [item-slot-helper-pair-c3e977-c3ee14.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/item-slot-helper-pair-c3e977-c3ee14.md) already established a four-slot equipment compatibility predicate through `C3:EE14`
- non-`0x1D` callers at `C1:9956`, `C1:A0F6`, and `C1:A860` use `C3:E9A0` in item-table / text-display flows that make much more sense as "is this item currently equipped?" than as a generic category test

So the safest current read is that `$99FF..$9A02` are the selected character's four equipped item-id bytes, and `C3:E9A0` is the corresponding membership test.

## `0x1D 10 -> C1:575D`

The bank-`01` leaf at `C1:575D` wraps that same predicate in the familiar text-command shape:

- it supports either an explicit character id or wildcard `A = #$00FF`
- on wildcard input, it loops the active-id family at `$986F` up to `$98A4`
- for each selected character, it forwards the requested item id into `C3:E9A0`
- it stages the boolean result through `C1:045D`

So the best current command-level reading is: test whether the selected or active-party character currently has the given item equipped.

## Confidence

- `C3:E9A0` as four-byte membership test over `$99FF..$9A02`: high confidence
- `$99FF..$9A02` as equipped item-id bytes: medium-high confidence
- `0x1D 10` as equipped-item presence check: medium-high confidence
