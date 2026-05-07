# C3 shared helper working-name promotion

## Purpose

The C3 anonymous-chunk frontier is now covered, so this pass promotes reusable C3 helpers and tables that were already proven across older notes but did not yet have manifest-visible working names.

This is intentionally conservative: it promotes names where local notes already pin behavior through callers, byte shape, or table consumers. It does not try to name every incidental branch label.

## Window and text lifecycle helpers

The ebsrc bankconfig already names the small C3 window helpers around `E4CA`, and the local C1/text notes explain why those names fit.

- `C3:E4CA` stores `0` to `$9622`. It is called around text/window refresh paths that need instant printing disabled.
- `C3:E4D4` stores `1` to `$9622`. It is the matching enable helper.
- `C3:E4E0` calls `C3:E4CA`, then `C1:2DD5`, then `C3:E4D4`; the reference-side name `WINDOW_TICK_WITHOUT_INSTANT_PRINTING` matches that exact wrapper shape.
- `C3:E4EF` scans up to eight window records and returns the first slot whose `$8654 + slot*0x52` field is `#$FFFF`, otherwise `#$FFFF`.
- `C3:E521` is the close/free path for one window id: it clears focus if needed, calls `C3:E7E3` to clear registered copy chains, relinks neighboring `$8650/$8652` window fields, clears registered tile-copy state, marks redraw flags, and eventually runs a window tick/refresh path. The `C3:E4EF..E6F7` source unit is intentionally one module with two callable labels rather than a split blocker.

These are shared window lifecycle contracts, not C1-local conveniences. They are now safe to expose as C3 names.

## Inventory and equipment helpers

The item/inventory notes already prove several C3 helpers well enough to promote:

- `C3:E977` computes `(character - 1) * 0x5F + 0x99F1 + (slot - 1)` and returns one inventory byte. This is a 1-based character plus 1-based slot accessor over the character inventory list.
- `C3:E9A0` checks the four equipped-slot reference bytes `$99FF..$9A02` for a requested slot/reference value.
- `C3:E9F7` is the item-id predicate used by text command `0x1D 04`; it dereferences the nonzero `$99FF..$9A02` equipped-slot reference bytes into the character inventory list at `$99F1..` before comparing against the requested item id.
- `C3:EAD0` is the insertion-side Fresh Egg / Chick / Chicken family refresh hook called after adding those item-family ids.
- `C3:EB1C` is the removal-side mirror for that same egg-family lifecycle hook.
- `C3:EBCA` is the tracked item-family sync pass called after party-composition / party-overlay arbitration changes. Its `D5:F4BB` row loop is now source-safe: the apparent width hazard at `C3:EC00` is resolved by the callee-return paths restoring M16 before the next pointer rebuild.
- `C3:EE14` tests an item id against one of four equipment-slot masks from `C4:58AB`.

The exact human-facing names of all four equipment slots are still better left to the item table pass, but the helper role itself is now high confidence.

## HP / PP adjustment workers

The HP/PP quartet has a strong local split:

- `C3:EC1F` subtracts an HP amount from current HP, flooring at zero.
- `C3:EC8B` adds HP, caps at max HP, and sets the paired HP-present marker.
- `C3:ED2C` subtracts PP, flooring at zero.
- `C3:ED98` adds PP and caps at max PP; unlike HP recovery, it does not update the paired `$9A19` field.

All four share the same `Y` contract:

- `Y = 0`: compute a percent of max through `C0:9086` / `C0:90FF`
- `Y = 1`: use the direct amount from `X`

That makes these bank-03 workers source-worthy enough to promote as HP/PP adjustment helpers.

## Battle PSI menu metadata

The battle PSI menu notes prove the C3 data/table roles under the C1 battle PSI controller:

- `C3:EF26` maps menu selectors to compact PSI-list groups. A zero byte means no grouped PSI-list display for that selector.
- `C3:F016` supplies the grouped PSI-list slice count/width used after `C3:EF26`.
- `C3:F0B0` is the category/list gate table used while scanning live PSI bytes in `C1:C165`.
- `C3:F112` is a PSI rank/suffix table keyed by PSI level in the direct PSI-id-plus-rank display path.
- `C3:F11C` is the fixed encoded tail appended after a PSI menu-entry row.
- `C3:F124` is the fixed-width encoded battle PSI menu-entry row table with 20-byte rows.
- `C3:F1EC` is the Jeff repair core: it scans Jeff's inventory for a repairable broken item, replaces the matched slot with the fixed item id on success, and returns the original broken item id for paired item-name printing.

The exact decoded text contents of the encoded PSI rows are still a separate text-table job, but the table boundaries and consumers are now pinned.

## Battle / text finalizers

Two finalizer-style helpers are strong enough to expose:

- `C3:EE4D` runs a shared world/text refresh chain and then clears the high `$C000` bits on the active `$B4A8` visual/presentation handle's `$10B6` flag word when that handle exists. Its callers include battle selection, C2 post-transition, and C4 stat-update paths, so it should not be battle-selection-specific.
- `C3:EE7A` resolves one `C4:550F` statistic-selector record into the caller's `$06/$08` result pair. It can return byte, word, pointer/string, or fixed-width-buffer forms, so the best exported name is a statistic-selector value resolver rather than a naming-buffer-specific helper.

## Working Names

- `C3:E4CA` = `ClearInstantPrinting`
- `C3:E4D4` = `SetInstantPrinting`
- `C3:E4E0` = `TickWindowWithoutInstantPrinting`
- `C3:E4EF` = `FindFirstFreeWindowSlot`
- `C3:E521` = `CloseWindowAndReleaseTileState`
- `C3:E977` = `ReadCharacterInventorySlotByte`
- `C3:E9A0` = `CheckEquippedInventorySlotReference`
- `C3:E9F7` = `CheckEquippedInventoryItemPresence`
- `C3:EAD0` = `RefreshEggFamilyLifecycleOnInsert`
- `C3:EB1C` = `RefreshEggFamilyLifecycleOnRemove`
- `C3:EBCA` = `SyncPartyOverlayTrackedItemFamilyState`
- `C3:EC1F` = `DepleteCharacterHp`
- `C3:EC8B` = `RecoverCharacterHp`
- `C3:ED2C` = `DepleteCharacterPp`
- `C3:ED98` = `RecoverCharacterPp`
- `C3:EE14` = `CheckItemEquipmentSlotCompatibility`
- `C3:EE4D` = `RefreshWorldAndReleaseActiveVisualHandle`
- `C3:EE7A` = `ResolveStatisticSelectorValue`
- `C3:EF26` = `BattlePsiMenuSelectorGroupTable`
- `C3:F016` = `BattlePsiMenuGroupSliceCountTable`
- `C3:F0B0` = `BattlePsiKnownStateGateTable`
- `C3:F112` = `BattlePsiRankSuffixTable`
- `C3:F11C` = `BattlePsiMenuEntryFixedTail`
- `C3:F124` = `BattlePsiMenuEntryRowTable`
- `C3:F1EC` = `TryRepairJeffBrokenInventoryItem`

## Remaining questions

- The PSI row/tail tables need a text-decoding pass before the visible strings should be named row-by-row.
