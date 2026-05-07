# C1 Equipment Runtime Polish

This note records the byte-neutral C1 equipment-menu polish slice. It promotes
the locally supported runtime joins between item-table fields, live equipment
slots, shadow preview slots, comparison markers, and the visible menu loops.

Primary source modules:

- `src/c1/c1_9066_dispatch_equipped_slot_subtype_update.asm`
- `src/c1/c1_9b4e_build_equipment_comparison_markers_for_item.asm`
- `src/c1/c1_9b79_resolve_equipped_slot_for_item_subtype.asm`
- `src/c1/c1_9cdd_initialize_equipment_comparison_markers_default.asm`
- `src/c1/c1_9d49_prepare_equipment_menu_status_display.asm`
- `src/c1/c1_9f29_render_selected_character_equipment_list.asm`
- `src/c1/c1_a778_refresh_selected_character_equipment_display.asm`
- `src/c1/c1_a795_run_character_equipment_slot_selection_loop.asm`
- `src/c1/c1_a1d8_render_equipment_preview_status.asm`
- `src/c1/c1_aa5d_run_party_equipment_menu_controller.asm`

Related evidence notes:

- `notes/equipment-preview-and-derived-state-cluster.md`
- `notes/equipment-slot-subtype-dispatch-c19066-c4577d.md`
- `notes/equipment-preview-slot-block-9cd0-9cd6.md`
- `notes/equipment-comparison-markers-9a1d.md`
- `notes/equipment-menu-display-fringe-c19a11-c19f29.md`
- `notes/equipment-menu-top-level-flow-c1a778-c1aa5d.md`

## Promoted Contracts

`C1:9066` is the live equipment-slot subtype dispatcher. It accepts a 1-based
character id in A and a 1-based inventory slot in X, resolves the item id from
`$99F1 + character_stride + slot - 1`, reads item configuration byte `+0x19`,
and dispatches `+0x19 & 0x0C` to the C4 live-slot helper:

| Subtype bits | Live slot | Helper |
| --- | --- | --- |
| `0x00` | weapon / `$99FF` | `C4:577D` |
| `0x04` | charm, pendant, cloak / `$9A00` | `C4:57CA` |
| `0x08` | bracelet, band / `$9A01` | `C4:5815` |
| `0x0C` | cap, ribbon, coin / `$9A02` | `C4:5860` |

`C1:9B4E..9CDD` is the equipment comparison-marker builder. The shop/equipment
UI passes a candidate item id in A. `C3:EE14` gates compatibility for each of
the four active-party comparison lanes. Failed compatibility writes marker
`0x0C00`; compatible equipment compares the signed item parameter at item row
`+0x1F` against the current live slot and writes `0x1400` for an improving
candidate or `0x0400` for a default/non-improving candidate.

`C1:9CDD` and `C1:9D49` reset `$9A1D..$9A20` to `0x0400` and refresh the
equipment/status tilemap row from the E0 row table. `C1:9D49` is the shop-facing
variant used after `C1:9DB5` returns from the item-selection loop.

`C1:9DB5` is the shop item menu join into equipment semantics. It builds up to
seven item rows from `D5:76B2`, stages D5 item names at `$9C9F`, prints the cost
from item row `+0x1A`, installs `C1:9B4E` as the comparison callback, and runs
the text-entry selection loop.

`C1:9F29` renders the selected character's live equipment list. The four rows
are resolved in the same family order as `C1:9066`: `$99FF`, `$9A00`, `$9A01`,
and `$9A02`. Each nonzero byte is a 1-based inventory slot index, not an item
id; the renderer resolves through the inventory row and then copies the D5 item
name. Empty slots use the C4 fallback label at `C4:5C78`.

`C1:A778` is the selected-character equipment display refresh callback. It
clears `$9CD4`, renders the live equipment list through `C1:9F29`, then renders
the status/preview panel through `C1:A1D8`.

`C1:A795` is the per-character equipment loop. It prompts for one of the four
slot families, scans the selected character inventory, filters to equipment
class through `C1:9EE6`, requires the selected family through `C2:24E1`, gates
equipability through `C3:EE14`, and installs the matching C2 preview callback:

| Category | Preview slot | Callback |
| --- | --- | --- |
| `1` | `$9CD0` | `C2:2562` |
| `2` | `$9CD1` | `C2:25AC` |
| `3` | `$9CD2` | `C2:260D` |
| `4` | `$9CD3` | `C2:2673` |

After the item prompt, `C1:A795` either clears the selected live family through
the C4 helper with X = 0 or calls `C1:9066` to equip the chosen inventory slot.
It closes the temporary category window and re-renders through `C1:A778`.

`C1:A1D8` is the status/preview renderer. It starts from base display stats
`$99EA/$99EB`, adds signed item parameter byte `+0x1F` from the live slots, and
clamps printed values into the unsigned `0..255` display range. When `$9CD4` is
set, it also evaluates shadow preview slots `$9CD0..$9CD3`.

`C1:AA5D` is the top-level party equipment controller. It snapshots `$9C8A`,
selects the target party member directly for one-person parties or through
`C1:27EF` with `C1:A778` as the display callback for multi-person parties,
calls `C1:A795`, closes the equipment windows, restores `$9C8A`, and returns the
selected party code or zero on cancel.

Source polish follow-up (2026-05-06): `src/c1/c1_a795_run_character_equipment_slot_selection_loop.asm`
now names the remaining helper-call surface in the per-character equipment loop
and its wallet/status refresh tail. The promoted calls cover the `C1:9066`
equipped-slot subtype dispatcher, the `C1:A778` display refresh, C2 managed
text-event snapshot/restore, C3 window update/close helpers, the C1 active
window text-mode/content helpers, and the C4 right-aligned decimal/status
printer.

Source polish follow-up (2026-05-06): the equipment/shop UI callback handoffs
now expose their caller-side ABI. The party equipment controller stages the
`C1:A778` display callback for `C1:27EF` through named `$0E/$10` callback
slots, the per-character equipment loop stages the four C2 preview callbacks
through named `C1:1F5A` preview-callback slots, and the shop menu names the
`C1:9B4E` comparison callback install before the shared selection loop.

Source polish follow-up (2026-05-07): the shop item menu builder at
`C1:9DB5` now names its local row/table selector, item id, item-row pointer,
item-name tile source, text-entry source/metadata, price-print source, and
returned menu selection. The adjacent `C1:9D49` status refresh now names the
comparison-marker reset index and E0 tile-block source pointer.

Source polish follow-up (2026-05-07): the per-character equipment slot loop at
`C1:A795` now names its selected character, selected family, inventory slot
scan index, visible-row count, default row, item id, one-based character id,
item-name tile source, text-entry source/metadata, item-selection result, and
wallet decimal-print source. This keeps the equipment menu's row builder and
preview-selection ABI aligned with the shop menu vocabulary above.

## Decomp Value

This slice turns the editor-facing item/equipment vocabulary into concrete
runtime joins:

- item row `+0x19` is both the CoilSnake-facing slot-family field and the local
  runtime dispatch byte for live equipment mutation and comparison markers.
- item row `+0x1F` is the signed equipment-preview/comparison parameter used by
  C1 display code.
- live slots, shadow slots, and comparison markers all share the same four
  family order.
- shop item rows are now linked to the same comparison callback used by the
  equipment display path.

## Remaining Soft Spots

The structural control flow is strong. The still-soft parts are mostly
presentation vocabulary:

- exact visible labels for the non-weapon slot families
- final human names for the marker graphics behind `0x0400`, `0x0C00`, and
  `0x1400`
- whether the character-index-3 adjacent `+0x1F/+0x20` item-parameter lane
  should receive a local field name before more C2/C4 evidence is polished
