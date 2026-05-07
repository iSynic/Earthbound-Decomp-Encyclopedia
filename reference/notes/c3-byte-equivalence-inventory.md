# C3 byte-equivalence validation

This report assembles a scratch Asar translation of one C3 pilot module into a clean ROM copy at its original `org`, then compares the protected byte range against the original ROM.

- status: `OK`
- source path: `src/c3/inventory_equipment_tracked_items.asm`
- range: `C3:E977..C3:EC1F`
- size: `680` bytes
- mismatches: `0`
- generated asm: `build/c3-byte-equivalence/inventory-equipment-tracked-items.byte-equivalence.asar.asm`
- patched ROM: `build/c3-byte-equivalence/inventory-equipment-tracked-items.byte-equivalence.sfc`
