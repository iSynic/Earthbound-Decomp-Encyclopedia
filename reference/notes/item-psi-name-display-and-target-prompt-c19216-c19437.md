# Item / PSI Name Display And Target Prompt Helpers (`C1:9216-C1:9437`)

This note covers the remaining display-side unknown starts in the `C1:9216..9437` cluster.

See also [statistic-selector-family-c4550f-c3ee7a.md](notes/statistic-selector-family-c4550f-c3ee7a.md), [character-selection-prompt-cluster-c11f8a-c1242e.md](notes/character-selection-prompt-cluster-c11f8a-c1242e.md), and [battle-targetting-resolver-c1adb4-af50.md](notes/battle-targetting-resolver-c1adb4-af50.md).

## Main Result

This cluster is mostly short display adapters over known data tables:

The `C1:9216..9437` display-helper cluster is now source-backed in the C1 scaffold:

- `src/c1/c1_9216_print_item_name_from_configuration_table.asm`
- `src/c1/c1_9249_print_statistic_selector_value.asm`
- `src/c1/c1_931b_print_psi_or_small_dynamic_label.asm`
- `src/c1/c1_93e7_open_target_selection_prompt_label.asm`
- `src/c1/c1_9437_close_target_selection_prompt_label.asm` covers the tiny close helper plus adjacent menu/status bridge entries.

## Working Names

- `C1:9216` = `PrintItemNameFromConfigurationTable`
- `C1:931B` = `PrintPsiOrSmallDynamicLabel`
- `C1:93E7` = `OpenTargetSelectionPromptLabel`
- `C1:9437` = `CloseTargetSelectionPromptLabel`

- `C1:9216` prints one item name from `ITEM_CONFIGURATION_TABLE`
- `C1:931B` prints a PSI category/name/suffix-like label from a few mixed string sources
- `C1:93E7` opens and paints a small target-selection prompt label
- `C1:9437` closes the temporary prompt/window opened by that target-selection path

The two target-prompt helpers are corroborated directly by the reference `DETERMINE_TARGETTING` source: the ally-single target path calls `UNKNOWN_C193E7` before `CHAR_SELECT_PROMPT`, then calls `UNKNOWN_C19437` immediately after the selection.

## Item Name Printer

`C1:9216` takes an item id in `A`.

It builds a pointer into `ITEM_CONFIGURATION_TABLE` at `D5:5000`:

- base pointer = `D5:5000`
- record size = `0x27`
- selected record = `item_id * 0x27`

It then prints `0x19` bytes from that record through `C4:487C`.

This matches the reference symbol layout: `ITEM_CONFIGURATION_TABLE` is the first named table in this bank-`D5` region, and local item-table consumers elsewhere use the same `0x27` record stride.

## PSI / Small Label Printer

`C1:931B` is a mixed string-label printer.

Its input selector chooses one of three local paths:

- selectors `1..4` use fixed-width five-byte buffers rooted at `$99CE`, with stride `0x5F`
- selector `7` uses the six-byte dynamic buffer at `$9819`
- all other selectors use `PSI_NAME_TABLE` at `D5:8F23` to find text in the padded PSI-name text block at `D5:9589`, then print `0x19` bytes

The reference data makes the last path much less anonymous:

- `D5:8F23` is `PSI_NAME_TABLE`
- `D5:9589` is the padded PSI-name text area, containing strings such as `PSI Fire`, `Lifeup`, `Healing`, and `Teleport`

The dynamic-buffer paths choose between `C1:0EFC` and `C4:47FB` based on `$7E:B49D`. The exact display-mode meaning of that flag is still soft, but the printer distinction is now clearer: `C1:0EFC` is the lower fixed-length string printer, while `C4:47FB` measures the same fixed string against the active descriptor and line-advances before printing when it would overflow.

## Target Prompt Setup / Cleanup

`C1:93E7` is a scoped prompt setup wrapper.

It:

1. reserves or clears a temporary work area at `$9C8A` through `C2:0A20`
2. calls `C3:E4D4`
3. initializes a text/window context with selector `0x28`
4. indexes a fixed bank-`04` text table at `C4:5963` with `selector * 0x0A`
5. prints `0x0A` bytes through `C1:0EFC`
6. refreshes text state with `C3:E4CA`
7. releases the `$9C8A` work area through `C2:0ABC`

`C1:9437` is the matching tiny cleanup wrapper:

- load `0x28`
- call `C3:E521`
- return

This tiny close helper is now source-backed as the first segment of `src/c1/c1_9437_close_target_selection_prompt_label.asm`; the rest of that file labels the adjacent public entries at `C1:9441`, `C1:952F`, and `C1:98DE`.

The reference `DETERMINE_TARGETTING` source pins the user-facing use: when an ally-targeting battle action needs the player to choose one ally, it calls `C1:93E7` before `CHAR_SELECT_PROMPT` and `C1:9437` after the prompt returns.

So the safest current read is that `C1:93E7` opens/labels the ally-target selection prompt, while `C1:9437` closes the temporary prompt/window state for selector `0x28`.

## Practical Conclusion

The unknown starts `C1:9216`, `C1:931B`, `C1:93E7`, and `C1:9437` are now covered as table-backed display helpers:

- item names from the item configuration table
- PSI/small dynamic labels from `PSI_NAME_TABLE` and short RAM buffers
- battle ally-target prompt setup and cleanup around the shared character-selection prompt

The main remaining uncertainty is mostly display-mode polish around `$B49D` and the exact label text at `C4:5963`. The printer split itself is now covered: `C4:487C` is the segmented buffered adapter, `C4:47FB` is the wrap-preflight fixed-string printer, and `C1:0EFC` is the lower fixed-length string printer.
