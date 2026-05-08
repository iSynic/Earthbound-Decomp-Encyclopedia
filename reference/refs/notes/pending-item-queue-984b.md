# Pending Item Queue `$984B`

`$984B` is best read as a packed pending-item queue, not just a small anonymous shop-state block.

## Why this interpretation fits

The core helpers around it are now fairly direct.

### `C1:913D`

`C1:913D` scans a `0x24`-entry byte region rooted at `$984B` for the first zero byte.

- if it finds a free slot, it stores the input byte there and returns that byte
- if no free slot exists, it returns `0`

That is a straight packed-queue insertion pattern.

### `C1:91B0`

`C1:91B0` takes a 1-based slot index into the same region and:

- reads the chosen byte
- shifts following bytes left to close the gap
- zeroes the final vacated byte
- returns the removed byte

That is a straight packed-queue removal/compaction pattern.

### `C1:91F8`

`C1:91F8` wraps `C1:91B0`, then forwards the removed byte into `C1:8BC6`. That now reads much more specifically as queue-to-inventory transfer: `C1:8BC6` is the insertion-side mirror of `C1:8C27`, placing the removed item id into the first empty slot of the selected character inventory; see [inventory-slot-insertion-helper-c18bc6.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/inventory-slot-insertion-helper-c18bc6.md).

## Best current read

The safest current interpretation is:

- `$984B..$986E` = `0x24`-entry pending-item queue of item ids

This also explains the nearby bank-`01` text-command leaves much better, and the community control-code docs now line up unusually well with the same local picture: immediate store, immediate withdraw, and direct add-to-storage all target this same queue.

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
