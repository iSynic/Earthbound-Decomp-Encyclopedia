# C3 Inventory, Equipped Slot, and Egg-Refresh Helpers `E977..EBCA`

This note consolidates the source-helper corridor from `C3:E977` through `C3:EBCA`. The main new result is a correction: the four bytes at `$99FF..$9A02` are now better modeled as equipped inventory-slot references than as direct equipped item ids.

## Working Names

- `C3:E977` = `ReadCharacterInventorySlotByte`
- `C3:E9A0` = `CheckEquippedInventorySlotReference`
- `C3:E9F7` = `CheckEquippedInventoryItemPresence`
- `C3:EAD0` = `RefreshEggFamilyLifecycleOnInsert`
- `C3:EB1C` = `RefreshEggFamilyLifecycleOnRemove`
- `C3:EBCA` = `SyncPartyOverlayTrackedItemFamilyState`

## Character inventory record shape

The helpers in this corridor repeatedly use the same character-record shape:

- character id inputs are 1-based
- each character record uses stride `0x5F`
- inventory bytes begin at `$99F1`
- the four equipment-reference bytes are `$99FF..$9A02`

`C3:E977` is the clean generic accessor. It computes `(character - 1) * 0x5F + $99F1 + (slot - 1)` and returns the byte stored at that inventory slot. Its direct callers include `C1:3406`, `C1:355D`, `C1:35F0`, `C1:3634`, `C1:37A6`, `C1:387E`, `C1:572E`, `C1:581E`, `C1:59D0`, `C1:6066`, `C1:9195`, `C1:AFA1`, `C1:CEA4`, and `C2:3998`.

Mechanically, `C3:E977` is embedded inside the addressed data include that starts at `C3:E84E`. The split plan in [c3-mixed-source-split-plan.md](notes/c3-mixed-source-split-plan.md) carves that row into leading data, `ReadCharacterInventorySlotByte`, and `CheckEquippedInventorySlotReference`, so these two helpers can be emitted as standalone source units even though the reference include row is mixed.

## Equipped-slot reference correction

`C3:E9A0` compares a requested value directly against the four bytes at `$99FF..$9A02` and returns `1` if any byte matches. On its own, that looked like an equipped-item membership test.

`C3:E9F7` changes the contract. It reads each nonzero `$99FF..$9A02` byte, decrements it, uses that decremented value as an offset into the same character's `$99F1..` inventory bytes, and compares the fetched inventory item id against the requested item id. That is a much stronger fit for:

- `$99FF..$9A02` = four equipped inventory-slot reference bytes
- `C3:E9A0` = direct equipped-slot reference membership test
- `C3:E9F7` = equipped item-id membership test after dereferencing those slot references into inventory

This also explains why `C1:575D` can wrap `C3:E9A0`, while `C1:4D24` wraps `C3:E9F7`: one command is asking about the equipment reference byte itself, and the other is asking whether a concrete item id is equipped through any of those references.

## Egg-family refresh hooks

`C3:EAD0` and `C3:EB1C` are the insert/remove sides of the Fresh Egg / Chick / Chicken lifecycle family already isolated from item byte `+0x1C` bit `0x10`.

`C3:EAD0` scans 5-byte rows at `D5:F4BB` for the inserted item id. On match, it calls `C4:8ECE(index)` and, if that reports inactive/absent, calls `C4:8EEB(index)`.

`C3:EB1C` scans the same row table for the removed item id, calls `C4:8F98(index)`, then scans active party inventory records across the `$99F1..99FE` inventory bytes. If the same item id still exists in an active inventory, it calls `C4:8EEB(index)`.

The pair therefore maintains a small tracked-item lifecycle registry rather than ordinary inventory state.

## Party-overlay tracked-item sync

`C3:EBCA` is the table-wide sync pass called from `C1:FEC5`, `C2:299B`, and `C2:2A10`. The earlier M-width caveat is now closed in [c3-tracked-item-sync-source-contract-ebca.md](notes/c3-tracked-item-sync-source-contract-ebca.md): the loop rebuild at `C3:EC00` is reached in 16-bit accumulator mode, so the `D5:F4BB` pointer setup is ordinary source, not mixed data or a hidden byte-mode decode.

- point `$06/$08` at `D5:F4BB`
- walk 5-byte rows
- read each row's item id
- call `C4:5683` to check party-side item presence/registry state
- dispatch to `C3:EAD0` when present
- dispatch to `C3:EB1C` when absent

The older overlay-state wording captured the caller neighborhood, but this body is more specifically about syncing the tracked item-family rows after party/inventory registry changes. The proposed name keeps the overlay connection while making the tracked item-family role visible.

## Confidence

- `C3:E977` as character inventory-slot byte accessor: high confidence
- `$99FF..$9A02` as equipped inventory-slot references: medium-high confidence
- `C3:E9A0` as equipped-reference membership test: high confidence
- `C3:E9F7` as equipped item-id membership test via reference dereference: high confidence
- `C3:EAD0` / `C3:EB1C` as egg-family insert/remove lifecycle refresh hooks: high confidence
- `C3:EBCA` as tracked item-family sync pass tied to party-overlay/registry refresh: high confidence
