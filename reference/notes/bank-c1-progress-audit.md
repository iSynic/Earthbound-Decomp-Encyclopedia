# Bank C1 Decompilation Progress Audit

This report cross-checks the local `notes/*.md` corpus against the quarantined `ebsrc-main` US bank include maps and symbol lists.

Treat reference names as corroboration only: a bank entry is not considered understood here just because a side reference gave it a label.

## Bank `C1` / reference bank `01`

- Reference include entries: `427`
- Reference named include entries without an address in the path: `281`
- Reference address-bearing include entries: `132`
- Address-bearing unknown include entries: `131`
- Reference symbols: `89` (`34` semantic-ish, `55` placeholder/redirect/null)
- Local notes mention `695` distinct `C1:xxxx` addresses
- Reference addresses mentioned by local notes: `132` / `132`
- Unknown include entries not directly mentioned in local notes: `0`

### Reference-Named Include Families

These are already semantically grouped by `ebsrc-main`; use them as corroborating names, not as final local proof.

- `common.asm`
- `config.asm`
- `structs.asm`
- `symbols/bank00.inc.asm`
- `symbols/bank01.inc.asm`
- `symbols/bank02.inc.asm`
- `symbols/bank03.inc.asm`
- `symbols/bank04.inc.asm`
- `symbols/bank2f.inc.asm`
- `symbols/globals.inc.asm`
- `symbols/misc.inc.asm`
- `symbols/text.inc.asm`
- `text/enable_blinking_triangle.asm`
- `text/clear_blinking_prompt.asm`
- `text/get_blinking_prompt.asm`
- `text/set_text_sound_mode.asm`
- `text/get_window_focus.asm`
- `text/set_window_focus.asm`
- `text/close_focus_window.asm`
- `text/lock_input.asm`
- `text/unlock_input.asm`
- `text/ccs/halt.asm`
- `text/get_active_window_address.asm`
- `text/transfer_active_mem_storage.asm`
- `text/transfer_storage_mem_active.asm`
- `text/get_argument_memory.asm`
- `text/get_secondary_memory.asm`
- `text/get_working_memory.asm`
- `text/increment_secondary_memory.asm`
- `text/set_secondary_memory.asm`
- `text/set_working_memory.asm`
- `text/set_argument_memory.asm`
- `text/get_text_x.asm`
- `text/get_text_y.asm`
- `text/create_window.asm`
- `text/show_hppp_windows.asm`
- `text/hide_hppp_windows.asm`
- `text/ccs/clear_line.asm`
- `text/print_newline_redirect.asm`
- `text/print_letter_redirect.asm`
- `text/print_string_redirect.asm`
- `text/print_letter.asm`
- `text/print_number.asm`
- `text/print_string.asm`
- `text/change_current_window_font.asm`
- `text/num_select_prompt.asm`
- `text/print_menu_items.asm`
- `text/move_cursor.asm`
- `text/selection_menu.asm`
- `text/character_select_prompt.asm`
- `text/window_tick.asm`
- `system/debug/y_button_menu.asm`
- `overworld/talk_to.asm`
- `overworld/check.asm`
- `overworld/open_menu.asm`
- `text/open_hppp_display.asm`
- `overworld/show_town_map.asm`
- `overworld/debug/y_button_flag.asm`
- `overworld/debug/y_button_guide.asm`
- `overworld/debug/set_char_level.asm`
- `overworld/debug/y_button_goods.asm`
- `text/ccs/print_stat.asm`
- `text/ccs/print_party_or_hint_new_line.asm`
- `text/ccs/unknown_1C_09.asm`
- `text/ccs/text_effects.asm`
- `text/ccs/jump.asm`
- `text/ccs/jump_multi.asm`
- `text/ccs/set_event_flag.asm`
- `text/ccs/clear_event_flag.asm`
- `text/ccs/jump_event_flag.asm`
- `text/ccs/get_event_flag.asm`
- `text/ccs/print_special_graphics.asm`
- `text/ccs/open_window.asm`
- `text/ccs/switch_to_window.asm`
- `text/ccs/call.asm`
- `text/ccs/create_number_selector.asm`
- `text/ccs/force_text_alignment.asm`
- `text/ccs/check_equal.asm`
- `text/ccs/check_not_equal.asm`
- `text/ccs/print_horizontal_strings.asm`
- ... 201 more

### Locally Corroborated Reference Addresses

- `C1:0000` -> notes/bank-c1-first-pass.md, notes/bank-c1-subsystem-and-symbol-synthesis.md, notes/c4-early-ppu-and-text-tile-helpers-0000-0085.md, +1 more
- `C1:0004` -> notes/bank-c0-first-pass.md, notes/delivery-row-helpers-ef0e67-ef0ead.md, notes/post-transition-deferred-script-queue-c06b21-c06bff.md, +4 more
- `C1:004E` -> notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md, notes/c3-equipment-selector-source-contract-ee14-ef22.md, notes/c3-window-text-source-helper-corridor-e450-e7e3.md, +3 more
- `C1:008E` -> notes/battle-text-entry-family-c1dc1c-dd7c.md, notes/text-command-family-18-windows-and-selection.md, notes/text-engine-entry-waits-window-gates-c10000-c102d0.md, +1 more
- `C1:00D6` -> notes/text-command-10-parameterized-pause.md, notes/text-engine-entry-waits-window-gates-c10000-c102d0.md
- `C1:00FE` -> notes/text-engine-entry-waits-window-gates-c10000-c102d0.md
- `C1:02D0` -> notes/bank-c1-subsystem-and-symbol-synthesis.md, notes/text-engine-entry-waits-window-gates-c10000-c102d0.md
- `C1:078D` -> notes/active-window-text-tile-pair-placement-c44c8c.md, notes/bank-c1-subsystem-and-symbol-synthesis.md, notes/bank-ef-reference-frontier.md, +4 more
- `C1:07AF` -> notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md, notes/debug-menu-window-tick-helpers-c12bf3-c12d17.md, notes/text-window-rendering-primitives-c1078d-c10d7c.md
- `C1:0A85` -> notes/text-window-rendering-primitives-c1078d-c10d7c.md
- `C1:0BA1` -> notes/battle-psi-menu-table-helpers-c1c046-c1c165.md, notes/text-window-rendering-primitives-c1078d-c10d7c.md
- `C1:0BFE` -> notes/active-text-entry-chain-layout-c451fa.md, notes/text-window-rendering-primitives-c1078d-c10d7c.md
- `C1:0C55` -> notes/text-window-rendering-primitives-c1078d-c10d7c.md
- `C1:0D60` -> notes/debug-menu-window-tick-helpers-c12bf3-c12d17.md, notes/text-window-rendering-primitives-c1078d-c10d7c.md
- `C1:0D7C` -> notes/active-window-text-tile-pair-placement-c44c8c.md, notes/bank-c1-subsystem-and-symbol-synthesis.md, notes/bank-ef-reference-frontier.md, +4 more
- `C1:0EB4` -> notes/jeff-repair-item-name-bridge.md
- `C1:0EE3` -> notes/jeff-repair-item-name-bridge.md
- `C1:0F40` -> notes/active-text-entry-chain-layout-c451fa.md, notes/bank-c1-subsystem-and-symbol-synthesis.md, notes/text-entry-record-builder-neighbors-c10f40-c11887.md
- `C1:0FA3` -> notes/battle-text-entry-family-c1dc1c-dd7c.md, notes/text-command-family-18-windows-and-selection.md, notes/text-entry-record-builder-neighbors-c10f40-c11887.md
- `C1:0FEA` -> notes/battle-psi-selection-refresh-c1ca72.md, notes/debug-menu-window-tick-helpers-c12bf3-c12d17.md, notes/jeff-repair-item-name-bridge.md
- `C1:134B` -> notes/text-entry-record-builder-neighbors-c10f40-c11887.md
- `C1:1354` -> notes/text-entry-builder-c113d1-89d4.md
- `C1:1383` -> notes/text-command-family-1a-menus.md, notes/text-commands-11-and-12-menu-and-line-control.md
- `C1:138D` -> notes/active-text-entry-chain-layout-c451fa.md, notes/jeff-repair-item-name-bridge.md, notes/text-entry-record-builder-neighbors-c10f40-c11887.md, +1 more
- `C1:13D1` -> notes/active-text-entry-chain-layout-c451fa.md, notes/bank-c1-subsystem-and-symbol-synthesis.md, notes/equipment-menu-display-fringe-c19a11-c19f29.md, +6 more
- `C1:14B1` -> notes/equipment-menu-display-fringe-c19a11-c19f29.md, notes/text-entry-record-builder-neighbors-c10f40-c11887.md
- `C1:153B` -> notes/battle-psi-ability-table-d58a50.md, notes/battle-psi-category-list-family-c1caf5-c1cb7f.md, notes/text-entry-record-builder-neighbors-c10f40-c11887.md, +1 more
- `C1:1596` -> notes/open-menu-prelude-helpers-c1339e-c133b0.md, notes/text-entry-record-builder-neighbors-c10f40-c11887.md
- `C1:15F4` -> notes/equipment-menu-display-fringe-c19a11-c19f29.md, notes/teleport-menu-wrapper-c1bb71-bcab.md, notes/text-entry-record-builder-neighbors-c10f40-c11887.md
- `C1:17E2` -> notes/text-entry-record-builder-neighbors-c10f40-c11887.md, notes/text-window-rendering-primitives-c1078d-c10d7c.md
- `C1:180D` -> notes/active-text-entry-chain-layout-c451fa.md, notes/jeff-repair-item-name-bridge.md
- `C1:181B` -> notes/active-text-entry-chain-layout-c451fa.md, notes/text-entry-record-builder-neighbors-c10f40-c11887.md
- `C1:1887` -> notes/active-text-entry-chain-layout-c451fa.md, notes/bank-c1-subsystem-and-symbol-synthesis.md, notes/text-entry-record-builder-neighbors-c10f40-c11887.md
- `C1:1F5A` -> notes/battle-psi-user-selection-front-end-c1b5b6-b7c6.md, notes/character-selection-prompt-cluster-c11f8a-c1242e.md
- `C1:1F8A` -> notes/bank-c1-subsystem-and-symbol-synthesis.md, notes/character-selection-prompt-cluster-c11f8a-c1242e.md, notes/item-psi-name-display-and-target-prompt-c19216-c19437.md
- `C1:1FBC` -> notes/character-selection-prompt-cluster-c11f8a-c1242e.md
- `C1:1FD4` -> notes/character-selection-prompt-cluster-c11f8a-c1242e.md
- `C1:2012` -> notes/character-selection-prompt-cluster-c11f8a-c1242e.md
- `C1:2070` -> notes/character-selection-prompt-cluster-c11f8a-c1242e.md
- `C1:20D6` -> notes/character-selection-prompt-cluster-c11f8a-c1242e.md
- `C1:21B8` -> notes/character-selection-prompt-cluster-c11f8a-c1242e.md
- `C1:2362` -> notes/character-selection-prompt-cluster-c11f8a-c1242e.md
- `C1:242E` -> notes/bank-c1-subsystem-and-symbol-synthesis.md, notes/character-selection-prompt-cluster-c11f8a-c1242e.md, notes/item-psi-name-display-and-target-prompt-c19216-c19437.md
- `C1:244C` -> notes/character-selection-prompt-cluster-c11f8a-c1242e.md, notes/jeff-repair-item-name-bridge.md
- `C1:2BD5` -> notes/jeff-repair-item-name-bridge.md, notes/text-command-family-19-data-and-substitution.md
- `C1:2BF3` -> notes/bank-c1-subsystem-and-symbol-synthesis.md, notes/bank-ef-reference-frontier.md, notes/debug-menu-window-tick-helpers-c12bf3-c12d17.md
- `C1:2C36` -> notes/debug-menu-window-tick-helpers-c12bf3-c12d17.md
- `C1:2CCC` -> notes/debug-menu-window-tick-helpers-c12bf3-c12d17.md
- `C1:2D17` -> notes/bank-c1-subsystem-and-symbol-synthesis.md, notes/bank-ef-reference-frontier.md, notes/debug-menu-window-tick-helpers-c12bf3-c12d17.md, +1 more
- `C1:2E42` -> notes/character-selection-prompt-cluster-c11f8a-c1242e.md, notes/debug-menu-window-tick-helpers-c12bf3-c12d17.md, notes/text-command-10-parameterized-pause.md, +1 more
- `C1:339E` -> notes/bank-c1-first-pass.md, notes/bank-c1-subsystem-and-symbol-synthesis.md, notes/open-menu-prelude-helpers-c1339e-c133b0.md
- `C1:33A7` -> notes/open-menu-prelude-helpers-c1339e-c133b0.md
- `C1:33B0` -> notes/bank-c1-subsystem-and-symbol-synthesis.md, notes/open-menu-prelude-helpers-c1339e-c133b0.md
- `C1:4012` -> notes/timed-delivery-row-index-command-1f-d3.md, notes/timed-event-slot-block-7440-and-c20abc.md
- `C1:4049` -> notes/timed-event-slot-block-7440-and-c20abc.md
- `C1:4070` -> notes/bank-c1-first-pass.md, notes/bank-c1-subsystem-and-symbol-synthesis.md, notes/deferred-text-byte-queue-97ba-97ca.md, +2 more
- `C1:5FB1` -> notes/text-command-family-19-data-and-substitution.md
- `C1:621F` -> notes/text-command-1f-c0-jump-multi2-c1621f.md
- `C1:7796` -> notes/text-command-load-string-pointer-c17796-c17889.md
- `C1:7889` -> notes/text-command-family-19-data-and-substitution.md, notes/text-command-load-string-pointer-c17796-c17889.md
- `C1:866D` -> notes/bank-c1-first-pass.md, notes/bank-c1-subsystem-and-symbol-synthesis.md, notes/timed-delivery-row-index-command-1f-d3.md, +1 more
- `C1:869D` -> notes/timed-delivery-row-index-command-1f-d3.md, notes/timed-event-slot-block-7440-and-c20abc.md
- `C1:90E6` -> notes/overworld-registry-accessor-c190e6.md
- `C1:90F1` -> notes/text-command-family-1d-inventory-money.md
- `C1:91B0` -> notes/pending-item-queue-984b.md
- `C1:91F8` -> notes/pending-item-queue-984b.md, notes/text-command-family-1d-inventory-money.md
- `C1:9216` -> notes/bank-c1-subsystem-and-symbol-synthesis.md, notes/battle-item-action-selection-c1ce85-c1cfc6.md, notes/item-psi-name-display-and-target-prompt-c19216-c19437.md
- `C1:9249` -> notes/c3-equipment-selector-source-contract-ee14-ef22.md, notes/statistic-selector-family-c4550f-c3ee7a.md
- `C1:931B` -> notes/file-select-action-copy-delete-menus-c1f07e-f14f-f2a8.md, notes/item-psi-name-display-and-target-prompt-c19216-c19437.md
- `C1:93E7` -> notes/equipment-menu-top-level-flow-c1a778-c1aa5d.md, notes/item-psi-name-display-and-target-prompt-c19216-c19437.md
- `C1:9437` -> notes/bank-c1-subsystem-and-symbol-synthesis.md, notes/battle-item-action-selection-c1ce85-c1cfc6.md, notes/item-psi-name-display-and-target-prompt-c19216-c19437.md
- `C1:9441` -> notes/text-command-family-1a-menus.md
- `C1:952F` -> notes/teleport-menu-wrapper-c1bb71-bcab.md, notes/text-command-family-18-windows-and-selection.md
- `C1:9A11` -> notes/bank-c1-subsystem-and-symbol-synthesis.md, notes/equipment-menu-display-fringe-c19a11-c19f29.md, notes/equipment-menu-top-level-flow-c1a778-c1aa5d.md, +1 more
- `C1:9A43` -> notes/jeff-repair-item-name-bridge.md, notes/text-command-15-compressed-bank-1-pseudo-opcode.md, notes/text-command-16-compressed-bank-2-pseudo-opcode.md, +2 more
- `C1:9CDD` -> notes/equipment-comparison-markers-9a1d.md, notes/equipment-menu-display-fringe-c19a11-c19f29.md, notes/equipment-preview-and-derived-state-cluster.md
- `C1:9D49` -> notes/equipment-menu-display-fringe-c19a11-c19f29.md, notes/window-flavour-palette-block-refresh-c47f87.md
- `C1:9DB5` -> notes/equipment-menu-display-fringe-c19a11-c19f29.md, notes/text-command-family-1a-menus.md
- `C1:9F29` -> notes/bank-c1-subsystem-and-symbol-synthesis.md, notes/equipment-menu-display-fringe-c19a11-c19f29.md, notes/equipment-menu-top-level-flow-c1a778-c1aa5d.md, +1 more
- `C1:A1D8` -> notes/bank-c1-first-pass.md, notes/bank-c1-subsystem-and-symbol-synthesis.md, notes/equipment-menu-display-fringe-c19a11-c19f29.md, +4 more
- ... 52 more

### Local-Only Address Mentions

These may be derived local discoveries, cross-bank targets, or address forms absent from the reference include/symbol map.

- `C1:0036` -> notes/battle-text-display-mode-latch-964d.md, notes/text-engine-entry-waits-window-gates-c10000-c102d0.md
- `C1:003C` -> notes/battle-text-display-mode-latch-964d.md, notes/text-engine-entry-waits-window-gates-c10000-c102d0.md
- `C1:0042` -> notes/battle-text-display-mode-latch-964d.md, notes/text-engine-entry-waits-window-gates-c10000-c102d0.md
- `C1:0048` -> notes/text-engine-entry-waits-window-gates-c10000-c102d0.md
- `C1:0058` -> notes/c3-menu-cursor-tile-data-e3f8-e450.md, notes/c3-window-text-source-helper-corridor-e450-e7e3.md
- `C1:0078` -> notes/text-engine-entry-waits-window-gates-c10000-c102d0.md
- `C1:007E` -> notes/equipment-menu-display-fringe-c19a11-c19f29.md, notes/text-engine-entry-waits-window-gates-c10000-c102d0.md, notes/text-input-dialog-option-helpers-c1e48d-c1e4be.md
- `C1:0084` -> notes/battle-item-action-selection-c1ce85-c1cfc6.md, notes/character-selection-prompt-cluster-c11f8a-c1242e.md, notes/file-select-action-copy-delete-menus-c1f07e-f14f-f2a8.md, +3 more
- `C1:00C2` -> notes/text-window-rendering-primitives-c1078d-c10d7c.md
- `C1:00C7` -> notes/text-engine-entry-waits-window-gates-c10000-c102d0.md
- `C1:00D0` -> notes/text-engine-entry-waits-window-gates-c10000-c102d0.md
- `C1:0166` -> notes/bank01-text-command-map-00-1f.md, notes/lower-bank01-text-control-strip-00-17.md, notes/text-command-03-halt-with-prompt.md, +2 more
- `C1:0301` -> notes/class2-c1-display-text-substitution-handler-7af3.md, notes/interaction-context-and-event-flags.md, notes/interaction-result-classes.md, +4 more
- `C1:0324` -> notes/jeff-repair-item-name-bridge.md
- `C1:0326` -> notes/interaction-context-and-event-flags.md
- `C1:0327` -> notes/jeff-repair-item-name-bridge.md
- `C1:0380` -> notes/interaction-context-and-event-flags.md, notes/jeff-repair-item-name-bridge.md
- `C1:0381` -> notes/jeff-repair-item-name-bridge.md
- `C1:03DC` -> notes/interaction-context-and-event-flags.md, notes/item-category-classifier-c19ee6.md, notes/jeff-repair-item-name-bridge.md, +4 more
- `C1:0400` -> notes/jeff-repair-item-name-bridge.md, notes/statistic-selector-family-c4550f-c3ee7a.md, notes/text-command-0d-parameterized-copy-to-argmem.md, +2 more
- `C1:040A` -> notes/jeff-repair-item-name-bridge.md, notes/text-command-09-jump-multi.md, notes/text-command-0b-parameterized-test-if-workmem-true.md, +5 more
- `C1:0410` -> notes/interaction-context-and-event-flags.md
- `C1:042E` -> notes/text-command-0f-parameterized-workmem-increment.md, notes/text-command-family-19-data-and-substitution.md
- `C1:0443` -> notes/jeff-repair-item-name-bridge.md, notes/text-command-0e-parameterized-store-to-argmem.md
- `C1:0450` -> notes/interaction-context-and-event-flags.md
- `C1:045D` -> notes/bank-deposit-accumulator-98b9-98bb.md, notes/c3-jeff-repair-source-contract-f1ec.md, notes/class2-c1-display-text-substitution-handler-7af3.md, +22 more
- `C1:0489` -> notes/c3-jeff-repair-source-contract-f1ec.md, notes/interaction-context-and-event-flags.md, notes/interaction-result-classes.md, +5 more
- `C1:04B5` -> notes/battle-psi-menu-table-helpers-c1c046-c1c165.md, notes/interaction-context-and-event-flags.md, notes/text-command-00-line-break.md, +1 more
- `C1:04D8` -> notes/battle-psi-menu-table-helpers-c1c046-c1c165.md, notes/battle-psi-selection-refresh-c1ca72.md, notes/interaction-context-and-event-flags.md
- `C1:04EE` -> notes/text-input-dialog-option-helpers-c1e48d-c1e4be.md
- `C1:0528` -> notes/c3-window-text-source-helper-corridor-e450-e7e3.md
- `C1:0A04` -> notes/c3-focused-party-hppp-actor-clear-e6f8.md, notes/text-entry-record-builder-neighbors-c10f40-c11887.md
- `C1:0A1D` -> notes/battle-text-entry-family-c1dc1c-dd7c.md, notes/c3-focused-party-hppp-actor-clear-e6f8.md, notes/text-command-family-18-windows-and-selection.md, +1 more
- `C1:0ADC` -> notes/battle-text-display-mode-latch-964d.md
- `C1:0B8A` -> notes/text-window-rendering-primitives-c1078d-c10d7c.md
- `C1:0BD3` -> notes/text-commands-11-and-12-menu-and-line-control.md
- `C1:0BF8` -> notes/c4-early-ppu-and-text-tile-helpers-0000-0085.md, notes/text-window-rendering-primitives-c1078d-c10d7c.md
- `C1:0C49` -> notes/active-text-entry-chain-layout-c451fa.md, notes/text-entry-record-builder-neighbors-c10f40-c11887.md, notes/text-window-rendering-primitives-c1078d-c10d7c.md
- `C1:0C4F` -> notes/text-window-rendering-primitives-c1078d-c10d7c.md
- `C1:0C72` -> notes/text-window-rendering-primitives-c1078d-c10d7c.md
- `C1:0C79` -> notes/class2-reflected-hit-side-token-consumers.md, notes/text-window-rendering-primitives-c1078d-c10d7c.md
- `C1:0C80` -> notes/text-window-rendering-primitives-c1078d-c10d7c.md
- `C1:0C86` -> notes/text-window-rendering-primitives-c1078d-c10d7c.md
- `C1:0C8C` -> notes/class2-reflected-hit-side-token-consumers.md, notes/text-window-rendering-primitives-c1078d-c10d7c.md
- `C1:0CAF` -> notes/active-window-text-tile-pair-placement-c44c8c.md, notes/text-window-rendering-primitives-c1078d-c10d7c.md
- `C1:0CB6` -> notes/text-window-rendering-primitives-c1078d-c10d7c.md
- `C1:0CE4` -> notes/text-token-glyph-run-stager-c44b3a-c44e61.md
- `C1:0DF6` -> notes/battle-psi-menu-metadata-family-c1c853-c1c8bc.md, notes/battle-psi-name-builder-family-c1c8bc-ca06-c3f112-f124.md, notes/equipped-item-derived-cache-family-c21857-c21e03.md, +1 more
- `C1:0EFC` -> notes/battle-psi-menu-metadata-family-c1c853-c1c8bc.md, notes/battle-psi-name-builder-family-c1c8bc-ca06-c3f112-f124.md, notes/character-selection-prompt-cluster-c11f8a-c1242e.md, +3 more
- `C1:1388` -> notes/c3-window-and-battle-visual-unknown-tail-e7e3-f981.md, notes/c3-window-text-source-helper-corridor-e450-e7e3.md
- `C1:14F8` -> notes/text-entry-builder-c113d1-89d4.md
- `C1:1629` -> notes/text-entry-builder-c113d1-89d4.md
- `C1:163C` -> notes/active-text-entry-chain-layout-c451fa.md, notes/battle-psi-selection-refresh-c1ca72.md, notes/equipment-menu-display-fringe-c19a11-c19f29.md, +4 more
- `C1:169F` -> notes/text-window-rendering-primitives-c1078d-c10d7c.md
- `C1:1914` -> notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md
- `C1:192F` -> notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md
- `C1:196A` -> notes/battle-item-action-selection-c1ce85-c1cfc6.md, notes/battle-psi-menu-controller-c1cc39-ce73.md, notes/equipment-menu-display-fringe-c19a11-c19f29.md, +7 more
- `C1:1CBB` -> notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md
- `C1:1CE8` -> notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md
- `C1:1D12` -> notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md
- `C1:1D3F` -> notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md
- `C1:2120` -> notes/c3-window-text-source-helper-corridor-e450-e7e3.md
- `C1:2180` -> notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md
- `C1:2714` -> notes/c3-focused-party-hppp-actor-clear-e6f8.md
- `C1:27EF` -> notes/battle-psi-user-selection-front-end-c1b5b6-b7c6.md, notes/equipment-menu-top-level-flow-c1a778-c1aa5d.md
- `C1:2AAD` -> notes/c3-focused-party-hppp-actor-clear-e6f8.md
- `C1:2DD5` -> notes/battle-text-entry-family-c1dc1c-dd7c.md, notes/c3-shared-helper-working-name-promotion.md, notes/c3-window-text-source-helper-corridor-e450-e7e3.md, +8 more
- `C1:2E14` -> notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md
- `C1:2E28` -> notes/file-select-tail-helpers-c1ff2c-ff6b-ff99.md
- `C1:2E30` -> notes/window-flavour-palette-block-refresh-c47f87.md
- `C1:2E37` -> notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md
- `C1:2E44` -> notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md
- `C1:2EB2` -> notes/text-entry-builder-c113d1-89d4.md
- `C1:2FB2` -> notes/respawn-warp-target-snapshot-helper-c230f3.md
- `C1:3032` -> notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md
- `C1:30BF` -> notes/town-map-selection-rendering-c4d274-c4d744.md
- `C1:3187` -> notes/interaction-result-classes.md, notes/interaction-result-consumers.md
- `C1:323B` -> notes/interaction-result-classes.md, notes/interaction-result-consumers.md
- `C1:3406` -> notes/c3-e84e-debug-menu-and-embedded-item-helpers-split.md, notes/c3-inventory-equipped-slot-and-egg-refresh-helpers-e977-ebca.md
- `C1:355D` -> notes/c3-e84e-debug-menu-and-embedded-item-helpers-split.md, notes/c3-inventory-equipped-slot-and-egg-refresh-helpers-e977-ebca.md
- ... 483 more

## Suggested Workflow

1. Pick an unmentioned `unknown/...` chunk from this report.
2. Run `tools/decode_snippet.py` or a targeted helper around the address.
3. Cross-check `refs/ebsrc-main` symbols, `refs/earthbound-disasm-legacy`, and any data table in `refs/eb-decompile-4ef92` that the routine touches.
4. Write a focused note that states byte-level evidence, borrowed reference names, remaining uncertainty, and direct callers/xrefs.
5. Rerun this audit and promote the next gap.

