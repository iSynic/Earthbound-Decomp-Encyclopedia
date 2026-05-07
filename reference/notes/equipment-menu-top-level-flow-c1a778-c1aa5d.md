# Equipment Menu Top-Level Flow (`C1:A778-C1:AA5D`)

This note covers the remaining top-level starts around the equipment menu flow.

See also [equipment-menu-display-fringe-c19a11-c19f29.md](notes/equipment-menu-display-fringe-c19a11-c19f29.md), [equipment-preview-slot-block-9cd0-9cd6.md](notes/equipment-preview-slot-block-9cd0-9cd6.md), and [equipment-slot-subtype-dispatch-c19066-c4577d.md](notes/equipment-slot-subtype-dispatch-c19066-c4577d.md).

## Main Result

The top-level equipment path splits cleanly:

## Working Names

- `C1:A778` = `RefreshSelectedCharacterEquipmentDisplay`
- `C1:A795` = `RunCharacterEquipmentSlotSelectionLoop`
- `C1:AA18` = `RefreshWalletOrStatusDisplay`
- `C1:AA5D` = `RunPartyEquipmentMenuController`

- `C1:A778` refreshes the selected character's live equipment list and preview/status panel
- `C1:A795` runs the per-character equipment slot/item selection loop
- `C1:AA18` refreshes the wallet/status display context used by shop and text-display setup paths
- `C1:AA5D` is the party-facing equipment menu wrapper

`C1:A795` was already covered by the preview-slot notes, but it is included here because `C1:A778` and `C1:AA5D` are its practical entry and orchestration layer.

`C1:A778..AC4A` is now source-backed across the durable C1 scaffold: `C1:A778`, `C1:A795`, `C1:AA18`, `C1:AA5D`, `C1:AAFA`, and `C1:AC00` all validate byte-for-byte as decoded source.

Source polish follow-up (2026-05-06): the `C1:A795..AA5D` source unit now names
the last raw helper calls in the per-character equipment loop and wallet/status
refresh tail, including `C1:9066`, `C1:A778`, `C20A20/C20ABC`,
`C3:E4D4/E4CA/E521`, `C1:0EB4/0FA3`, and `C4:507A`.

## Selected-Character Refresh

`C1:A778` is tiny but important:

1. clear `$9CD4`
2. call `C1:9F29` for the selected character
3. call `C1:A1D8` for the same selected character
4. return

Existing notes now identify the two callees:

- `C1:9F29` renders the selected character's live equipment rows from `$99FF/$9A00/$9A01/$9A02`
- `C1:A1D8` renders preview/status values from the `$9CD0..$9CD3` shadow slot block

So `C1:A778` is the selected-character equipment display refresh wrapper. Clearing `$9CD4` before both calls fits the preview-ready latch model documented in the shadow-slot note.

## Per-Character Equipment Loop

`C1:A795` handles the actual equipment choice for one selected character.

Its high-level shape:

1. open a slot/category prompt through `C1:93E7(4)` and `C1:196A(1)`
2. if the player cancels, return
3. use the selected category to scan the character inventory for matching equipment-class items
4. create text-entry rows for each matching item name
5. mark the currently equipped item with byte `$22` in the staged name buffer
6. install a sentinel row from `C4:5C82`
7. route the chosen slot family through one of the four preview-block setup helpers:
   - `C2:2562`
   - `C2:25AC`
   - `C2:260D`
   - `C2:2673`
8. set `$9CD4 = 1`
9. prompt for the actual item row
10. on selection, call `C1:9066` to equip the item; on the unequip path, call the matching `C4:577D/57CA/5815/5860` slot-family helper
11. close the temporary category window and call `C1:A778` to refresh the display

The routine therefore sits exactly at the join between:

- inventory item-name staging
- slot-family filtering
- shadow preview-slot setup
- live equipment-slot mutation

## Wallet / Status Refresh

`C1:AA18` snapshots `$9C8A`, opens context `0x0A`, clears/prepares row `0x05`, refreshes the menu display context, clears the active focus window, prints the pointer pair stored at `$9831/$9833` through the right-aligned decimal/status printer at `C4:507A`, finalizes the menu display, restores `$9C8A`, and returns.

This matches the earlier `C1:134B` wrapper reading: `C1:AA18` is the local wallet/status display refresh helper shared by text-display setup and shop/menu presentation paths.

## Party-Facing Equipment Wrapper

`C1:AA5D` is the broader equipment menu entry.

It reserves `$9C8A`, reads the first active party code from `$986F`, and branches on `$98A4`:

- if there is only one active party member, it refreshes that member directly through `C1:A778`
- if there are multiple party members, it opens a character-selection prompt using `C1:93E7(0)`, callback `C1:A778`, and `C1:27EF`

After a party member is selected, it calls `C1:A795` for that member. If `C1:A795` returns a nonzero selection and there are multiple party members, it loops back through the same prompt/selection path. On exit it closes the temporary `0x2D` and `0x06` windows, releases `$9C8A`, and returns the selected party code or zero.

So `C1:AA5D` is best read as the top-level equipment menu controller: choose a party member, run that member's equipment slot loop, refresh, and keep going until the user backs out.

## Practical Conclusion

The unknown starts `C1:A778` and `C1:AA5D` are now covered as equipment-menu orchestration:

- `C1:A778` = selected-character equipment display refresh
- `C1:A795` = per-character equipment slot/item loop
- `C1:AA18` = wallet/status display refresh helper
- `C1:AA5D` = top-level party-facing equipment menu controller

The remaining uncertainty is presentational rather than structural: the exact visible label text for the category table at `C4:5C58`, and the exact glyph/icon meaning of byte `$22` in the staged item-name buffer.
