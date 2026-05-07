# Inventory Slot Removal Helper `C1:8C27`

`C1:8C27` is best read as a character-inventory slot removal helper with equipment-slot index maintenance.

## Working Names

- `C1:8C27` = `RemoveItemFromCharacterInventorySlot`

Source-scaffold promotion:

- `C1:8C27..8E5B` is now decoded source in `src/c1/c1_8c27_remove_item_from_character_inventory_slot.asm`.
- The combined C1 scaffold validates byte-for-byte after promotion: `C1 byte-equivalence: OK, 172 module(s), 0 mismatch(es).`

Source polish follow-up (2026-05-06): this source now names its cross-bank
equipment and item-family side-effect edges directly: the four C4 equipped-slot
index installers, the C2 party-overlay/Teddy Bear removal/arbitration helpers,
and the C3 Fresh Egg / Chick / Chicken removal lifecycle refresh.

## Why this interpretation fits

The strongest local structural clue is the `0x5F`-stride record rooted at `C3:99F1`:

- `C3:E977` now reads cleanly as a byte accessor over that record
- `C1:8C27` treats bytes `99FF..9A02` as four special 1-byte fields
- after that, it walks and compacts a 14-byte byte list starting at `99F1`

That is exactly the shape you would expect for:

- inventory bytes at `99F1..99FE` (14 entries)
- four equipment-slot index bytes at `99FF..9A02`

## Local behavior

Entry behavior:

- input `A` behaves like a 1-based character id
- input `Y` behaves like a 1-based inventory slot index inside that character record

The helper then does three major things.

### 1. Maintain the four special slot-index bytes

It reads the four bytes at:

- `99FF`
- `9A00`
- `9A01`
- `9A02`

for the selected character and compares each one against the input slot index.

If one matches exactly, it calls one of four bank-`C4` helpers:

- `C4:577D`
- `C4:57CA`
- `C4:5815`
- `C4:5860`

Those helpers now have their own structural note at [equipment-slot-subtype-dispatch-c19066-c4577d.md](notes/equipment-slot-subtype-dispatch-c19066-c4577d.md). The important shared behavior here is that each one writes the current inventory-slot index back into the matched equipped-slot byte, runs a small bank-`C2` refresh family, and returns the previous byte value.

In source those calls are now named
`C4577D_InstallWeaponSlotIndexAndRefreshDerivedStats`,
`C457CA_InstallBodySlotIndexAndRefreshDerivedStats`,
`C45815_InstallArmsSlotIndexAndRefreshDerivedStats`, and
`C45860_InstallOtherSlotIndexAndRefreshDerivedStats`.

After the exact-match checks, `C1:8C27` revisits those same four bytes and decrements any value that is strictly greater than the removed slot index. That is exactly what you would do if those bytes were 1-based indices into the inventory list and one entry was being removed.

### 2. Remove one entry from the 14-byte list at `99F1`

After the slot-index maintenance, the routine:

- reads the removed byte from `99F1 + (slot - 1)`
- stores it temporarily
- shifts following nonzero bytes left to close the gap
- writes `0` into the final vacated position

This is a direct packed-list removal/compaction pattern.

### 3. Run item-type-sensitive cleanup on the removed item

The helper then resolves the removed byte as an item id through the `D5:5000` item table:

- it checks item byte `+0x19`
- if that byte equals `4`, it runs a Teddy-Bear-family cleanup branch through `C2:29BB` and `C2:16DB`
- it also checks item byte `+0x1C` bit `0x10`
- if that bit is set, it calls `C3:EB1C`, which now reads much more like a Fresh-Egg / Chick / Chicken family refresh

The source now names those side-effect calls as
`C229BB_RemovePartyOverlayTrackedItemId`,
`C216DB_ArbitratePartyOverlayEntityPresence`, and
`C3EB1C_RefreshEggFamilyLifecycleOnRemove`.

See [teddy-bear-and-egg-item-cleanup-branches.md](notes/teddy-bear-and-egg-item-cleanup-branches.md) for the stronger local breakdown. So the removed item can trigger additional side effects depending on its type/flags, and those side effects now look tied to real item families rather than generic post-delete housekeeping.

## Best current read

The safest current interpretation is:

- `99F1..99FE` = 14-byte character inventory list
- `99FF..9A02` = four 1-based equipment-slot indices into that inventory list
- `C1:8C27` = remove one inventory entry, maintain those four indices, and run item-type-sensitive cleanup for the removed item

That also explains several neighboring helpers much better:

- `C3:E977` as an inventory-slot byte accessor
- `C3:EE14` as a slot-vs-item compatibility predicate over the same inventory/equipment model
- `0x1D 0F` as the slot-based removal wrapper that stages the removed item id plus the source character id, exactly matching the community control-code wording for removing character `XX`'s `YY`th inventory item
- `0x1D 12` as the pending-item queue transfer mirror that removes one source inventory item into service-side storage

## Confidence

- packed 14-byte inventory list at `99F1..99FE`: high confidence
- four equipment-slot index bytes at `99FF..9A02`: high confidence
- `C1:8C27` as inventory-entry removal plus slot-index maintenance: high confidence
- exact human-facing names of the four slots: still slightly tentative
