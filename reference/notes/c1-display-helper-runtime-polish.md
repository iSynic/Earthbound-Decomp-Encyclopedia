# C1 Display Helper Runtime Polish

Status: compact C1 display-helper polish slice.

This note records byte-neutral source comments added after
`notes/c1-selection-prompt-runtime-polish.md`. The slice focuses on the
table-backed item/statistic/PSI label printers and the target-selection prompt
label open/close pair.

## Source Modules Touched

| Source module | Runtime contract pinned |
| --- | --- |
| `src/c1/c1_9216_print_item_name_from_configuration_table.asm` | Prints a fixed 0x19-byte item name from D5:5000 item configuration rows with stride 0x27. |
| `src/c1/c1_9249_print_statistic_selector_value.asm` | Reads 3-byte statistic selector rows at C4:550F and prints either numeric values or fixed-width string buffers. |
| `src/c1/c1_931b_print_psi_or_small_dynamic_label.asm` | Chooses between party name buffers, `$9819`, or D5:8F23/D5:9589 PSI-name data. |
| `src/c1/c1_93e7_open_target_selection_prompt_label.asm` | Opens temporary window/context 0x28 and prints a 10-byte target-prompt label row from C4:5963. |
| `src/c1/c1_9437_close_target_selection_prompt_label.asm` | Closes/releases the temporary target-prompt window/context 0x28. |

## Evidence Inputs

- `notes/item-psi-name-display-and-target-prompt-c19216-c19437.md`
- `notes/statistic-selector-family-c4550f-c3ee7a.md`
- `notes/battle-targetting-resolver-c1adb4-af50.md`
- `notes/character-selection-prompt-cluster-c11f8a-c1242e.md`

## Runtime Contract

These helpers are short display adapters over existing data contracts:

- D5:5000 item rows, stride `0x27`, fixed item-name field length `0x19`
- C4:550F statistic selector rows, fixed 3-byte descriptors
- `$99CE` party character name buffers with `0x5F` party stride
- `$9819` six-byte dynamic naming buffer
- D5:8F23 PSI name table into padded D5:9589 PSI-name text
- C4:5963 target-prompt label rows, fixed length `0x0A`

The target-prompt pair is the display wrapper around the shared character
selection prompt used by the ally-targeting branch of C1:ADB4.

## Promotion Boundary

This slice promotes comments and local runtime wording only. The adjacent phone
contact/status-window helpers after C1:9437 now have source-facing local ABI
names, but the exact C4:5963 label text names remain deferred to a later
asset/text-table pass.

Source polish follow-up (2026-05-06): the adjacent
`src/c1/c1_9437_close_target_selection_prompt_label.asm` status-window block
now names its `C4:599A` required-experience helper edge as
`C4599A_StoreRequiredExperienceRemainingForCharacter`. The target-prompt close
and adjacent status-window helper unit now has no raw helper-call edges.

Source polish follow-up (2026-05-06): the same adjacent source unit now names
the local caller ABI for the phone-contact menu, character status window, and
inventory/equipment row renderer. `$0E/$10` handoffs are split by role into
window-title, dynamic-tile-block, text-print, decimal-print, fixed-string, and
text-entry source pointers; `$12/$14` are named where they seed text-entry
metadata; and the status/equipment and inventory row scratch slots now expose
their character, row, item, and window-index meanings.

## Validation

Run after source-comment edits:

```powershell
python tools\validate_source_bank_byte_equivalence.py --bank C1 --module all --combined --scaffold src\c1\bank_c1_helpers_asar.asm --strict
```
