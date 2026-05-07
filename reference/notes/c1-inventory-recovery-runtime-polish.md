# C1 Inventory And Recovery Runtime Polish

This note records the byte-neutral C1 inventory/recovery helper polish slice. It
promotes the shared helper contracts used by text-command families `0x1D` and
`0x1E`, without trying to rename every dispatcher leaf in one pass.

Primary source modules:

- `src/c1/c1_8b2c_insert_item_into_first_empty_inventory_slot.asm`
- `src/c1/c1_8bc6_insert_item_into_character_inventory.asm`
- `src/c1/c1_8c27_remove_item_from_character_inventory_slot.asm`
- `src/c1/c1_8e5b_search_and_remove_item_from_character_inventory.asm`
- `src/c1/c1_8ead_search_and_remove_item_from_active_inventories.asm`
- `src/c1/c1_8f0e_deplete_hp_for_character_or_active_party.asm`
- `src/c1/c1_8f64_recover_hp_for_character_or_active_party.asm`
- `src/c1/c1_8fba_deplete_pp_for_character_or_active_party.asm`
- `src/c1/c1_9010_recover_pp_for_character_or_active_party.asm`
- `src/c1/c1_913d_enqueue_pending_item_id.asm`

Related evidence notes:

- `notes/text-command-family-1d-inventory-money.md`
- `notes/text-command-family-1e-stat-recovery.md`
- `notes/inventory-slot-insertion-helper-c18bc6.md`
- `notes/inventory-slot-removal-helper-c18c27.md`
- `notes/inventory-slot-search-removal-helper-c18e5b-c18ead.md`
- `notes/hp-pp-adjust-helper-quartet-c18f0e-c19010.md`

Source polish follow-up (2026-05-06): the primary inventory/recovery helpers
now name their cross-bank worker edges directly. `C1:8B2C` and `C1:8C27` call
the C2 party-overlay/Teddy Bear hooks and C3 egg-family lifecycle hooks by
name; `C1:8C27` and `C1:9066` call the four C4 equipped-slot index installers
by name; and the HP/PP quartet now calls the C3 recover/deplete workers by
name. The combined C1 scaffold remains byte-equivalent.

Source polish follow-up (2026-05-06): the adjacent pending-item queue transfer
module now names its inventory-slot reader as
`C3E977_ReadCharacterInventorySlotByte`, so `C1:9183` reads as a direct bridge
from a selected character inventory slot into the packed `$984B` pending-item
queue before calling the `C1:8C27` removal worker.

## Inventory Helpers

`C1:8B2C` is the single-character insertion worker. It accepts a 1-based
character id in A and an item id in Y, scans the selected character inventory
bytes `$99F1..$99FE` for the first zero byte, writes the item id, and returns
the recipient character id. If the 14-byte inventory list is full, it returns
zero.

The insertion worker also runs item-family side effects:

- item byte `+0x19 == 4`: Teddy Bear-family insertion hook
- item byte `+0x1C & 0x10`: Fresh Egg / Chick / Chicken-family hook

Those edges are now explicit in source as
`C216DB_ArbitratePartyOverlayEntityPresence` and
`C3EAD0_RefreshEggFamilyLifecycleOnInsert`.

`C1:8BC6` wraps insertion with active-party wildcard handling. A contains either
a 1-based character id or `0x00FF`; X contains the item id. For wildcard input,
it scans active party ids from `$986F` up to `$98A4`, calls `C1:8B2C`, and
returns the first active party member that accepted the item. It returns zero
when no target inventory has room.

`C1:8C27` is the slot-removal worker. It accepts a 1-based character id in A and
a 1-based inventory slot in Y. It clears a matching live equipment-slot index
through the appropriate C4 helper, decrements any live slot index above the
removed slot, removes one byte from `$99F1..$99FE`, compacts following nonzero
entries left, and clears the final vacated byte.

The removal worker runs the mirror cleanup side effects for Teddy Bear-family
and Fresh Egg / Chick / Chicken-family items before returning the source
character id.

The removal side now names `C229BB_RemovePartyOverlayTrackedItemId`,
`C216DB_ArbitratePartyOverlayEntityPresence`, and
`C3EB1C_RefreshEggFamilyLifecycleOnRemove`. Its equipment-slot exact-match
clear paths also use the same four C4 slot-index installer contracts as the
equip dispatcher.

`C1:8E5B` searches one selected character inventory for an item id and removes
the first matching slot through `C1:8C27`. `C1:8EAD` wraps that with the same
`0x00FF` active-party wildcard pattern as insertion and returns the first active
party member that lost the item.

## HP/PP Workers

The recovery/depletion quartet shares one control shape:

- A = 1-based character id, or `0x00FF` for active-party wildcard
- X = amount/percent payload
- Y = mode selector from the text-command leaf

Each helper dispatches either to one explicit target or loops active party ids
from `$986F` up to `$98A4`.

| Helper | Worker | Role |
| --- | --- | --- |
| `C1:8F0E` | `C3:EC1F` | HP depletion |
| `C1:8F64` | `C3:EC8B` | HP recovery |
| `C1:8FBA` | `C3:ED2C` | PP depletion |
| `C1:9010` | `C3:ED98` | PP recovery |

The source names these workers as `C3EC1F_DepleteCharacterHp`,
`C3EC8B_RecoverCharacterHp`, `C3ED2C_DepleteCharacterPp`, and
`C3ED98_RecoverCharacterPp`.

The text-command dispatcher leaves choose percent versus direct amount by the Y
mode passed into these workers. The C3 workers own the actual stat arithmetic
and cap/floor behavior; this C1 layer owns target selection and wildcard active
party looping.

## Decomp Value

This slice makes the text-command families more actionable:

- `0x1D` give/take/check commands are now tied to concrete inventory list bytes,
  wildcard target behavior, and equipment-slot index maintenance.
- inventory mutation now has explicit side-effect hooks for item families that
  matter to gameplay state.
- `0x1E` HP/PP text commands now have a compact target-selection contract that
  separates C1 script targeting from C3 stat mutation.

## Remaining Soft Spots

- final local names for the C3 HP/PP workers should be promoted from C3-local
  source evidence when the C3 runtime polish pass reaches them
- the exact player-facing labels for the Teddy Bear and egg-family hooks are
  already strong, but the deeper side-system behavior lives outside this C1
  helper slice
