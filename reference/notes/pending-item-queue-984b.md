# Pending Item Queue `$984B`

`$984B` is best read as a packed pending-item queue, not just a small anonymous shop-state block.

## Working Names

- `C1:913D` = `EnqueuePendingItemId`
- `C1:9183` = `StoreInventorySlotItemInPendingQueue`
- `C1:91B0` = `RemovePendingItemIdAtIndex`
- `C1:91F8` = `WithdrawPendingItemToInventory`
- `C2:2351` = `FindFirstEmptyInventorySlotForCharacter`

Source-scaffold promotion:

- `C1:913D..91B0` is now decoded source in `src/c1/c1_913d_enqueue_pending_item_id.asm`, split into the queue insert helper and the inventory-slot-to-queue transfer helper.
- `C1:91B0..91F8` is now decoded source in `src/c1/c1_91b0_remove_pending_item_id_at_index.asm`.
- `C1:9A43..9B4E` is now decoded source in `src/c1/c1_9a11_run_selection_helper_with_temporary_focus.asm` as `BuildEscargoStorageSelectionMenu`, the display-side queue consumer for Escargo stored-item selection.
- `C2:2351..239D` is now decoded source in `src/c2/c2_2351_find_first_empty_inventory_slot_for_character.asm`, the destination-inventory capacity helper used by the withdraw path.
- The combined C1 scaffold validates byte-for-byte after promotion: `C1 byte-equivalence: OK, 172 module(s), 0 mismatch(es).`

Source polish follow-up (2026-05-06): `src/c1/c1_575d_test_equipped_item_presence_for_text_command.asm`
now calls the pending-item queue helpers by name from the `0x1D 12/13/18` and
`0x19 1C/1D` text-command leaves. The source now makes the split explicit:
Escargo store/withdraw use the packed `$984B` queue helpers, while delivery and
pickup queue entries either remove from that queue or remove from character
inventory before staging item/owner data.

Source polish follow-up (2026-05-06): `src/c1/c1_913d_enqueue_pending_item_id.asm`
now names the `C3:E977` inventory-slot accessor edge as
`C3E977_ReadCharacterInventorySlotByte`, making the `C1:9183`
inventory-slot-to-pending-queue bridge explicit in source.

Source polish follow-up (2026-05-06): the packed queue helpers now expose their
local scan and compaction ABI directly. `C1:90F1` names the active Escargo
requester bytes at `$98AB`, the remaining storage capacity, and the scan over
the `$984B` item-id queue. `C1:913D/9183` name the pending-item scan index,
queue capacity, and preserved source character/slot pair. `C1:91B0` names the
removed byte, shift byte, next index, and `$984B/$984C` compaction reads.

## Why this interpretation fits

The core helpers around it are now fairly direct.

### `C1:913D`

`C1:913D` scans a `0x24`-entry byte region rooted at `$984B` for the first zero byte.

- if it finds a free slot, it stores the input byte there and returns that byte
- if no free slot exists, it returns `0`

That is a straight packed-queue insertion pattern.

### `C1:9183`

`C1:9183` is the transfer wrapper used by the immediate-store path. It fetches
the selected character inventory byte through `C3:E977`, now named in source as
`C3E977_ReadCharacterInventorySlotByte`, tries to enqueue that item id with
`C1:913D`, and on success removes the original inventory slot through
`C1:8C27`.

So the safest current name is `StoreInventorySlotItemInPendingQueue`: it is not a raw queue helper by itself, but the bridge from character inventory into the packed pending-item queue.

### `C1:91B0`

`C1:91B0` takes a 1-based slot index into the same region and:

- reads the chosen byte
- shifts following bytes left to close the gap
- zeroes the final vacated byte
- returns the removed byte

That is a straight packed-queue removal/compaction pattern.

### `C1:91F8`

`C1:91F8` wraps `C1:91B0`, then forwards the removed byte into `C1:8BC6`. That now reads much more specifically as queue-to-inventory transfer: `C1:8BC6` is the insertion-side mirror of `C1:8C27`, placing the removed item id into the first empty slot of the selected character inventory; see [inventory-slot-insertion-helper-c18bc6.md](notes/inventory-slot-insertion-helper-c18bc6.md).

## Best current read

The safest current interpretation is:

- `$984B..$986E` = `0x24`-entry pending-item queue of item ids

This also explains the nearby bank-`01` text-command leaves much better, and the community control-code docs now line up unusually well with the same local picture: immediate store, immediate withdraw, and direct add-to-storage all target this same queue.

`C1:9A43` is now the display-side partner: it scans the same 0x24-byte queue, turns each nonzero item id into an item-name text-entry row, and returns the selected storage row through the shared menu-selection infrastructure.

### `0x1D 18`

`0x1D 18 -> C1:6124 -> C1:913D`

This now reads cleanly as the queue-add side of the same service item family: it takes the selected item id and inserts it into the first free entry of the packed `$984B` queue. The local ROM path matches the community control-code wording unusually well here, which describes `[1D 18 XX]` as adding item `XX` to Escargo Express inventory.

### `0x1D 12`

`0x1D 12 -> C1:58A5`

This leaf resolves an item through `C3:E977`, inserts that item id into `$984B` via `C1:913D`, and on success calls `C1:8C27` to remove the corresponding entry from the source character inventory. So it now reads much more like "immediately store one character inventory item with Escargo Express" than a generic shop-state helper.

### `0x1D 13`

`0x1D 13 -> C1:58FE`

This leaf removes one queued item through `C1:91F8`, then calls `C2:2351` to find the first empty slot in the selected recipient inventory. So it now reads much more like "immediately withdraw one stored item and give it to the destination character" than a vague pickup branch.

## Confidence

- `$984B` as a packed pending-item queue: high confidence
- queue entries as item ids rather than slot ids: high confidence
- exact gameplay scope of the queue as service-side storage / Escargo-style pending inventory: high confidence
- exact broader subsystem boundary beyond that service/storage role: moderately high but still a little cautious
