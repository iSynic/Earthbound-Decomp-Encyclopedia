# Equipment Menu Display Fringe (`C1:9A11-C1:9F29`)

This note covers three remaining unknown starts around the already-mapped item, Escargo, and equipment menu cluster.

See also [text-command-family-1a-menus.md](notes/text-command-family-1a-menus.md), [equipment-comparison-markers-9a1d.md](notes/equipment-comparison-markers-9a1d.md), [equipment-preview-and-derived-state-cluster.md](notes/equipment-preview-and-derived-state-cluster.md), and [equipment-preview-slot-block-9cd0-9cd6.md](notes/equipment-preview-slot-block-9cd0-9cd6.md).

## Main Result

The remaining starts in this slice are presentation helpers, not new inventory models:

## Working Names

- `C1:9A11` = `RunSelectionHelperWithTemporaryFocus`
- `C1:9A43` = `BuildEscargoStorageSelectionMenu`
- `C1:9D49` = `PrepareEquipmentMenuStatusDisplay`
- `C1:9DB5` = `RunShopItemSelectionMenu`
- `C1:9F29` = `RenderSelectedCharacterEquipmentList`

- `C1:9A11` is a scoped focus-and-selection wrapper
- `C1:9A43` builds the Escargo stored-item selection menu from the `$984B` pending-item queue
- `C1:9D49` resets per-character equipment comparison markers and primes a small HPPP/status display buffer
- `C1:9DB5` builds the active shop item menu, including item-name rows, prices, and comparison-marker refresh
- `C1:9F29` renders the selected character's four live equipment slots into the menu text-entry system

The structural equipment model remains the one from the existing focused notes:

- live equipment-slot bytes at `$99FF/$9A00/$9A01/$9A02`
- per-character comparison markers at `$9A1D..$9A20`
- short item-name staging at `$9C9F`
- text-entry construction through `C1:14B1`, `C1:15F4`, and `C1:13D1`

## Scoped Focus / Selection Wrapper

`C1:9A11` takes two inputs:

- incoming `A` becomes the active window/focus id
- incoming `X` is passed into the shared menu-selection helper

It:

1. reserves the temporary `$9C8A` work area through `C2:0A20`
2. calls `C1:007E` to store the requested focus in `$8958`
3. calls `C1:196A` with the second input
4. releases `$9C8A` through `C2:0ABC`
5. returns the selection result

So `C1:9A11` is best read as a small "run selection helper under temporary focus/work-area context" wrapper.

`C1:9A11..9B4E` is now source-backed in `src/c1/c1_9a11_run_selection_helper_with_temporary_focus.asm`, with `C1:9A43` labeled as the adjacent Escargo storage menu builder.

## Escargo Storage Selection Menu

`C1:9A43` reserves the same temporary `$9C8A` work area, opens text/window context `0x0D`, writes a fixed title/header, then iterates the 0x24-byte pending-item queue rooted at `$984B`. Each nonzero queue byte is treated as an item id, resolved through `ITEM_CONFIGURATION_TABLE` at `D5:5000`, staged through `$9C9F`, and installed as a text-entry record through `C1:13D1`. After building the visible rows it runs the shared selection loop through `C1:196A(1)`, releases window/context `0x0D` through `EF:0115`, restores `$9C8A` through `C2:0ABC`, and returns the selected row.

## Comparison Marker / Status-Buffer Primer

`C1:9CDD` is now source-backed as the default comparison-marker initializer in `src/c1/c1_9cdd_initialize_equipment_comparison_markers_default.asm`.

It first walks four character rows and writes `0x0400` into each row's `$9A1D` marker field. This is the same default comparison marker documented in [equipment-comparison-markers-9a1d.md](notes/equipment-comparison-markers-9a1d.md):

- `0x0400` = default / normal / non-improving equipment-window state

It then uses `$99CD` as a selector into a table at `E0:1FB9`, derives a pointer into `E0:1FC8`, copies eight bytes into `$0218`, writes `$0030 = 0x18`, and sets `$9623 = 1`.

`C1:9D49..9EE6` is now source-backed in `src/c1/c1_9d49_prepare_equipment_menu_status_display.asm`, split into the display primer at `C1:9D49` and the shop item menu entry at `C1:9DB5`.

The `C1:9D49` display primer:

- reset equipment comparison markers to the default visual state
- seed the HPPP/status display buffer for the current item/equipment menu mode
- mark the text/status display as needing refresh through `$9623`

The exact identity of the `E0:1FB9/E0:1FC8` rows is still soft, but this is clearly display preparation rather than an inventory mutation.

`C1:9DB5` is the local shop item selection menu used by the `0x1A 06` text-command family. It opens context `0x0C`, uses the active shop selector to read seven candidate item bytes from `D5:76B2`, copies nonzero item names from `ITEM_CONFIGURATION_TABLE` into `$9C9F`, prints each row's price through the active-window right-aligned decimal helper at `C4:507A`, installs the `C1:9B4E` equipment-comparison callback, refreshes default comparison markers through `C1:9CDD`, runs the shared selection loop through `C1:196A`, and returns the selected row.

## Live Equipment List Renderer

`C1:9F29` renders the four live equipment-slot rows for one selected character.

`C1:9F29..A1D8` is now source-backed in `src/c1/c1_9f29_render_selected_character_equipment_list.asm`.

The setup path:

- converts the incoming character selector to a zero-based record index
- opens text/window context `0x06`
- refreshes HPPP/window state through `C3:E4E0`
- if more than one party member is active (`$98A4 != 1`), writes `6` to `$5E7A`
- points the display source at the selected character's name buffer rooted at `$99CE`
- prints a five-byte name/header through `C2:032B`

Then it loops four row indices, matching the established slot order:

- row `0` reads live slot `$99FF`
- row `1` reads live slot `$9A00`
- row `2` reads live slot `$9A01`
- row `3` reads live slot `$9A02`

For each row it:

1. creates a row label from the fixed `C4:5C2C` text table through `C1:14B1`
2. reads the selected character's live equipped-slot byte
3. if the slot is nonzero, uses `$99F1 + slot - 1` to fetch the actual item id from the character inventory
4. copies that item name from `ITEM_CONFIGURATION_TABLE` into `$9C9F` or `$9CA0`
5. uses `C3:E9A0` to decide whether to prefix the staged name with byte `$22`
6. prints the staged row text through the usual text-entry and print helpers

After the four rows, it refreshes the active text chain through `C1:163C`, clears `$5E71`, and calls `C3:E4CA`.

The nearby menu/status renderer at `C1:9E8F` also reuses `C4:507A`, now identified as the active-window right-aligned decimal printer. That means the same presentation corridor handles both text-entry equipment rows and compact numeric values, while the inventory/equipment data model remains in the `$99F1..$9A02` character record fields.

The adjacent broader row builder at `C1:98DE` is now source-backed as `RenderCharacterInventoryOrEquipmentRows` inside `src/c1/c1_9437_close_target_selection_prompt_label.asm`; callers use it from battle item selection and open-menu preparation as well as equipment/menu presentation paths.

This makes `C1:9F29` the live equipment-list renderer. It is distinct from both the broader `C1:98DE` row builder and the `C1:A1D8` preview/status renderer, which consumes the `$9CD0..$9CD3` shadow slot block instead of the live `$99FF..$9A02` slots.

## Practical Conclusion

The unknown starts `C1:9A11`, `C1:9D49`, `C1:9DB5`, and `C1:9F29` now fit into the already documented menu/equipment presentation layer:

- scoped selection wrapper
- marker/status display prep
- shop item menu builder
- selected-character live equipment list renderer

The remaining soft spots are presentation details: the exact HPPP/status rows behind `E0:1FB9/E0:1FC8`, and the exact visible meaning of the `$22` prefix byte in the staged equipment row.
