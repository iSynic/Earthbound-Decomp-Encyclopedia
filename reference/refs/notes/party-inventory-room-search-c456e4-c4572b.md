# Party Inventory Room Search `C4:56E4` / `C4:572B`

This note captures the local role of the bank-`04` helper pair at `C4:56E4` and `C4:572B`, and their bank-`01` `0x1D 03` wrapper.

## Main result

The safest current local read is:

- `C4:56E4` = search one character inventory for the first empty slot and return that character id on success
- `C4:572B` = wrapper around that search, supporting either one explicit character or wildcard `A = #$00FF` over the active party range
- `0x1D 03 -> C1:4CEE` = text-command front end to that inventory-room search family

So `0x1D 03` is now locally consistent with the inherited parser name `GET_PLAYER_HAS_INVENTORY_ROOM`, not just script-backed.

## `C4:56E4`

Entry behavior:

- `A` behaves like a 1-based character id

The helper then:

1. decrements the character id and maps it through `C0:8FF7` with stride `#$005F`
2. lands on the selected character record at `$99F1 + 0x5F * (character - 1)`
3. scans the same 14-byte item area used by [party-item-possession-search-c45637-c45683.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/party-item-possession-search-c45637-c45683.md)
4. looks for the first byte equal to `0`
5. returns the original character id on the first empty slot, otherwise `0`

So this is the per-character inventory-room mirror of the possession search family.

## `C4:572B`

This is the wildcard-capable wrapper.

- If `A != #$00FF`, it just forwards the explicit character id to `C4:56E4`.
- If `A == #$00FF`, it loops over the leading party-range entries in `$986F`, stopping at `$98A4`, and calls `C4:56E4` for each active party character code until room is found.
- On success it returns the matching character id.
- On failure it returns `0`.

So this is not a generic world-entity scan. Like the possession helper, it is explicitly scoped to the active party range.

## `0x1D 03 -> C1:4CEE`

The bank-`01` leaf at `C1:4CEE` wraps the same family in the usual text-command shape:

- it accepts either an explicit character id or wildcard `0x00FF`
- it resolves the holder selector from either queued command bytes or the live text context
- it calls `C4:572B`
- it stages the returned character id through `C1:045D`

At the script level, that matches `GET_PLAYER_HAS_INVENTORY_ROOM` very well, because most callers immediately branch on the result before awarding an item.

## Script-side cross-checks

The exposed parser hits line up unusually well with the local mechanics.

- Many `E01ONET*` and `E01ONET2` hits use `GET_PLAYER_HAS_INVENTORY_ROOM 0xFF` immediately before `GIVE_ITEM_TO_CHARACTER_B`, which is the exact pattern we would expect from a wildcard room search over the party.
- The failure branches read like ordinary "inventory full" or "can't carry any more" text, which is consistent with the helper returning `0` when no party member has an empty slot.

So the old parser-facing name is not just a script-level convenience here; it matches the actual local behavior of the leaf.

## Confidence

- `C4:56E4` as per-character first-empty-slot search over the 14-byte inventory area: high confidence
- `C4:572B` as explicit-or-wildcard wrapper over that search: high confidence
- `0x1D 03` as front end to that search family: high confidence
