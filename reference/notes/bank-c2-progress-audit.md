# Bank C2 Decompilation Progress Audit

This report cross-checks the local `notes/*.md` corpus against the quarantined `ebsrc-main` US bank include maps and symbol lists.

Treat reference names as corroboration only: a bank entry is not considered understood here just because a side reference gave it a label.

## Bank `C2` / reference bank `02`

- Reference include entries: `406`
- Reference named include entries without an address in the path: `320`
- Reference address-bearing include entries: `86`
- Address-bearing unknown include entries: `86`
- Reference symbols: `350` (`257` semantic-ish, `93` placeholder/redirect/null)
- Local notes mention `563` distinct `C2:xxxx` addresses
- Reference addresses mentioned by local notes: `90` / `90`
- Unknown include entries not directly mentioned in local notes: `0`

### Reference-Named Include Families

These are already semantically grouped by `ebsrc-main`; use them as corroborating names, not as final local proof.

- `eventmacros.asm`
- `common.asm`
- `config.asm`
- `structs.asm`
- `symbols/bank00.inc.asm`
- `symbols/bank01.inc.asm`
- `symbols/bank02.inc.asm`
- `symbols/bank03.inc.asm`
- `symbols/bank04.inc.asm`
- `symbols/bank2f.inc.asm`
- `symbols/battle_bgs.inc.asm`
- `symbols/battle_sprites.inc.asm`
- `symbols/globals.inc.asm`
- `symbols/misc.inc.asm`
- `symbols/text.inc.asm`
- `overworld/inflict_sunstroke_check.asm`
- `text/set_window_title.asm`
- `text/hp_pp_window/draw.asm`
- `text/hp_pp_window/undraw.asm`
- `data/text/name_entry_grid_character_offset_table.asm`
- `data/text/the.asm`
- `text/hp_pp_window/separate_decimal_digits.asm`
- `text/hp_pp_window/fill_tile_buffer_x.asm`
- `text/hp_pp_window/fill_tile_buffer.asm`
- `text/hp_pp_window/fill_character_hp_tile_buffer.asm`
- `text/hp_pp_window/fill_character_pp_tile_buffer.asm`
- `misc/reset_hppp_rolling.asm`
- `misc/hp_pp_roller.asm`
- `text/update_hppp_meter_tiles.asm`
- `text/get_event_flag.asm`
- `text/set_event_flag.asm`
- `audio/stop_music_redirect.asm`
- `audio/play_sound_and_unknown.asm`
- `misc/recalc_character_postmath_offense.asm`
- `misc/recalc_character_postmath_defense.asm`
- `misc/recalc_character_postmath_speed.asm`
- `misc/recalc_character_postmath_guts.asm`
- `misc/recalc_character_postmath_luck.asm`
- `misc/recalc_character_postmath_vitality.asm`
- `misc/recalc_character_postmath_iq.asm`
- `battle/recalc_character_miss_rate.asm`
- `battle/calc_resistances.asm`
- `misc/increase_wallet_balance.asm`
- `misc/decrease_wallet_balance.asm`
- `text/get_party_character_name.asm`
- `inventory/get_item_subtype.asm`
- `inventory/get_item_subtype2.asm`
- `misc/learn_special_psi.asm`
- `misc/atm_deposit.asm`
- `misc/atm_withdraw.asm`
- `misc/party_add_char.asm`
- `misc/party_remove_char.asm`
- `misc/save_game.asm`
- `battle/init_scripted.asm`
- `misc/set_teleport_box_destination.asm`
- `data/battle/consolation_item_table.asm`
- `battle/menu_handler.asm`
- `text/copy_enemy_name.asm`
- `text/fix_attacker_name.asm`
- `text/fix_target_name.asm`
- `battle/find_targettable_npc.asm`
- `battle/get_shield_targetting.asm`
- `battle/feeling_strange_retargetting.asm`
- `battle/remove_status_untargettable_targets.asm`
- `battle/find_stealable_items.asm`
- `battle/select_stealable_item.asm`
- `battle/choose_target.asm`
- `battle/main_battle_routine.asm`
- `battle/instant_win_handler.asm`
- `battle/instant_win_check.asm`
- `battle/get_battle_action_type.asm`
- `battle/get_enemy_type.asm`
- `system/wait.asm`
- `system/math/rand_long.asm`
- `system/math/truncate_16_to_8.asm`
- `system/math/rand_limit.asm`
- `battle/50_percent_variance.asm`
- `battle/25_percent_variance.asm`
- `battle/success_255.asm`
- `battle/success_500.asm`
- ... 240 more

### Locally Corroborated Reference Addresses

- `C2:00B9` -> notes/c2-symbol-only-stragglers-c200d1-c20d3f.md, notes/collision-surface-probes-c052d4-c05e3a.md
- `C2:00C5` -> notes/collision-surface-probes-c052d4-c05e3a.md
- `C2:00D1` -> notes/c2-symbol-only-stragglers-c200d1-c20d3f.md
- `C2:00D9` -> notes/battle-text-entry-family-c1dc1c-dd7c.md, notes/c2-symbol-only-stragglers-c200d1-c20d3f.md
- `C2:0266` -> notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md
- `C2:0293` -> notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md
- `C2:02AC` -> notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md
- `C2:038B` -> notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md
- `C2:077D` -> notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md
- `C2:07B6` -> notes/c2-battlebg-load-and-palette-effect-corridor-c2cfe5-c2e0e7.md, notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md
- `C2:087C` -> notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md, notes/debug-menu-window-tick-helpers-c12bf3-c12d17.md
- `C2:08B8` -> notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md
- `C2:0958` -> notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md
- `C2:09A0` -> notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md
- `C2:0A20` -> notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md, notes/equipment-menu-display-fringe-c19a11-c19f29.md, notes/item-psi-name-display-and-target-prompt-c19216-c19437.md, +3 more
- `C2:0ABC` -> notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md, notes/equipment-menu-display-fringe-c19a11-c19f29.md, notes/item-psi-name-display-and-target-prompt-c19216-c19437.md, +5 more
- `C2:0B65` -> notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md
- `C2:0D3F` -> notes/c2-symbol-only-stragglers-c200d1-c20d3f.md
- `C2:0F58` -> notes/c2-symbol-only-stragglers-c200d1-c20d3f.md, notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md
- `C2:1034` -> notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md
- `C2:108C` -> notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md
- `C2:16AD` -> notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md
- `C2:16DB` -> notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md, notes/inventory-slot-insertion-helper-c18bc6.md, notes/inventory-slot-removal-helper-c18c27.md, +4 more
- `C2:2351` -> notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md, notes/pending-item-queue-984b.md, notes/text-command-family-1d-inventory-money.md
- `C2:239D` -> notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md, notes/party-overlay-arbitration-c216db-c3ebca.md
- `C2:23D9` -> notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md
- `C2:2474` -> notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md
- `C2:2562` -> notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md, notes/equipment-menu-top-level-flow-c1a778-c1aa5d.md, notes/equipment-preview-and-derived-state-cluster.md, +1 more
- `C2:25AC` -> notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md, notes/equipment-menu-top-level-flow-c1a778-c1aa5d.md, notes/equipment-preview-slot-block-9cd0-9cd6.md
- `C2:260D` -> notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md, notes/equipment-menu-top-level-flow-c1a778-c1aa5d.md, notes/equipment-preview-slot-block-9cd0-9cd6.md
- `C2:2673` -> notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md, notes/equipment-menu-top-level-flow-c1a778-c1aa5d.md, notes/equipment-preview-slot-block-9cd0-9cd6.md
- `C2:26C5` -> notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md
- `C2:26E6` -> notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md
- `C2:26F0` -> notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md, notes/class2-dispatch-family.md, notes/text-command-family-1d-inventory-money.md
- `C2:272F` -> notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md
- `C2:277C` -> notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md, notes/class2-dispatch-family.md
- `C2:2A3A` -> notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md
- `C2:3008` -> notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md
- `C2:307B` -> notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md
- `C2:3E32` -> notes/class2-late-controller-path-77ca.md
- `C2:3E8A` -> notes/character-selection-prompt-cluster-c11f8a-c1242e.md
- `C2:40A4` -> notes/class2-busy-helper-eacf-and-window-setup.md, notes/class2-d57b68-battle-action-table-match.md, notes/class2-descriptor-field-4e-and-d57b68.md, +6 more
- `C2:4348` -> notes/c2-steal-and-target-selection-helpers-c241dc-c24434.md
- `C2:437E` -> notes/c2-steal-and-target-selection-helpers-c241dc-c24434.md
- `C2:4434` -> notes/c2-steal-and-target-selection-helpers-c241dc-c24434.md
- `C2:4703` -> notes/class2-dispatch-family.md, notes/class2-end-to-end-gate-path-5540.md, notes/class2-handoff-4477-4703.md, +4 more
- `C2:6189` -> notes/c2-instant-win-and-magic-butterfly-helpers-c26189-c2654c.md
- `C2:654C` -> notes/c2-instant-win-and-magic-butterfly-helpers-c26189-c2654c.md
- `C2:69DE` -> notes/class2-prayer-common-helpers-c2c37a-c2c3e2-c2c41f.md
- `C2:90C6` -> notes/class2-d57b68-battle-action-table-match.md, notes/class2-d57b68-early-entry-name-crosswalk.md, notes/class2-late-normalization-and-odor-family-c29051-c29254.md
- `C2:B66A` -> notes/class2-battler-core-field-crosswalk.md, notes/class2-local-enemy-id-to-battler-init-chain.md, notes/class2-reflected-hit-side-buffer-flags.md
- `C2:BCB9` -> notes/c2-pp-loss-and-call-for-help-width-helpers-c2bcb9-c2bd13.md
- `C2:BD13` -> notes/c2-pp-loss-and-call-for-help-width-helpers-c2bcb9-c2bd13.md
- `C2:C21F` -> notes/class2-final-prayer-family-c2c572-c2c6f0.md, notes/class2-prayer-common-helpers-c2c37a-c2c3e2-c2c41f.md
- `C2:C32C` -> notes/class2-final-prayer-family-c2c572-c2c6f0.md
- `C2:C37A` -> notes/class2-final-prayer-family-c2c572-c2c6f0.md, notes/class2-prayer-common-helpers-c2c37a-c2c3e2-c2c41f.md
- `C2:C41F` -> notes/class2-final-prayer-family-c2c572-c2c6f0.md, notes/class2-prayer-common-helpers-c2c37a-c2c3e2-c2c41f.md
- `C2:CFE5` -> notes/c2-battlebg-load-and-palette-effect-corridor-c2cfe5-c2e0e7.md
- `C2:D0AC` -> notes/c2-battlebg-load-and-palette-effect-corridor-c2cfe5-c2e0e7.md
- `C2:DAE3` -> notes/c2-battlebg-load-and-palette-effect-corridor-c2cfe5-c2e0e7.md
- `C2:DB14` -> notes/intro-logo-wait-and-gas-station-helpers-c0efe1-c0f21e.md
- `C2:DB3F` -> notes/c2-battlebg-load-and-palette-effect-corridor-c2cfe5-c2e0e7.md, notes/intro-logo-wait-and-gas-station-helpers-c0efe1-c0f21e.md
- `C2:DE0F` -> notes/c2-battlebg-load-and-palette-effect-corridor-c2cfe5-c2e0e7.md
- `C2:DE96` -> notes/c2-battlebg-load-and-palette-effect-corridor-c2cfe5-c2e0e7.md
- `C2:DF2E` -> notes/c2-battlebg-load-and-palette-effect-corridor-c2cfe5-c2e0e7.md
- `C2:E08E` -> notes/c2-battlebg-load-and-palette-effect-corridor-c2cfe5-c2e0e7.md
- `C2:E0E7` -> notes/c2-battlebg-load-and-palette-effect-corridor-c2cfe5-c2e0e7.md
- `C2:E6B3` -> notes/c2-psi-swirl-overlay-tail-c2e6b3-c2ea74.md
- `C2:E6B6` -> notes/c2-psi-swirl-overlay-tail-c2e6b3-c2ea74.md
- `C2:E8C4` -> notes/c2-psi-swirl-overlay-tail-c2e6b3-c2ea74.md
- `C2:E9C8` -> notes/c2-psi-swirl-overlay-tail-c2e6b3-c2ea74.md, notes/npc-attention-path-coordinator-c0d19b-c0d98f.md
- `C2:E9ED` -> notes/c2-psi-swirl-overlay-tail-c2e6b3-c2ea74.md
- `C2:EA15` -> notes/c2-psi-swirl-overlay-tail-c2e6b3-c2ea74.md
- `C2:EA74` -> notes/c2-psi-swirl-overlay-tail-c2e6b3-c2ea74.md
- `C2:EAAA` -> notes/c2-psi-swirl-overlay-tail-c2e6b3-c2ea74.md, notes/class2-busy-helper-eacf-and-window-setup.md
- `C2:EACF` -> notes/battle-text-display-mode-latch-964d.md, notes/battle-text-entry-tail-dd82-dd9f.md, notes/c2-psi-swirl-overlay-tail-c2e6b3-c2ea74.md, +3 more
- `C2:EEE7` -> notes/c2-battle-sprite-render-and-palette-tail-c2eee7-c2ff9a.md
- `C2:F09F` -> notes/c2-battle-sprite-render-and-palette-tail-c2eee7-c2ff9a.md
- `C2:F0D1` -> notes/c2-battle-sprite-render-and-palette-tail-c2eee7-c2ff9a.md
- `C2:F121` -> notes/c2-battle-sprite-render-and-palette-tail-c2eee7-c2ff9a.md
- ... 10 more

### Local-Only Address Mentions

These may be derived local discoveries, cross-bank targets, or address forms absent from the reference include/symbol map.

- `C2:0000` -> notes/timed-delivery-state-helpers-ef0f60-fdb-ff6.md
- `C2:00D0` -> notes/c2-symbol-only-stragglers-c200d1-c20d3f.md
- `C2:00D2` -> notes/c2-symbol-only-stragglers-c200d1-c20d3f.md
- `C2:00D4` -> notes/c2-symbol-only-stragglers-c200d1-c20d3f.md
- `C2:00D6` -> notes/c2-symbol-only-stragglers-c200d1-c20d3f.md
- `C2:00D8` -> notes/c2-symbol-only-stragglers-c200d1-c20d3f.md
- `C2:032B` -> notes/battle-psi-menu-metadata-family-c1c853-c1c8bc.md, notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md, notes/equipment-menu-display-fringe-c19a11-c19f29.md
- `C2:03C3` -> notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md, notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md
- `C2:07E1` -> notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md
- `C2:0912` -> notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md
- `C2:0998` -> notes/class2-reflected-hit-side-buffer-flags.md, notes/class2-reflected-hit-side-token-consumers.md
- `C2:099C` -> notes/class2-reflected-hit-side-buffer-flags.md, notes/class2-reflected-hit-side-token-consumers.md
- `C2:0A68` -> notes/jeff-repair-item-name-bridge.md
- `C2:0D89` -> notes/c2-symbol-only-stragglers-c200d1-c20d3f.md
- `C2:0DC5` -> notes/c2-symbol-only-stragglers-c200d1-c20d3f.md
- `C2:0F17` -> notes/c2-symbol-only-stragglers-c200d1-c20d3f.md
- `C2:0F49` -> notes/c2-symbol-only-stragglers-c200d1-c20d3f.md
- `C2:0F9A` -> notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md, notes/class2-final-prayer-family-c2c572-c2c6f0.md
- `C2:109F` -> notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md, notes/debug-menu-window-tick-helpers-c12bf3-c12d17.md
- `C2:13AC` -> notes/debug-menu-window-tick-helpers-c12bf3-c12d17.md
- `C2:1628` -> notes/actionscript-wrapper-strip-c0a841-c0aafd.md, notes/bank-c0-first-pass.md, notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md, +14 more
- `C2:165E` -> notes/actionscript-wrapper-strip-c0a841-c0aafd.md, notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md, notes/teleport-freeze-vector-frontier-c0dd0f-c0e196.md, +4 more
- `C2:182A` -> notes/overworld-entity-type-registry-9887-98a4.md
- `C2:1857` -> notes/bank-c1-subsystem-and-symbol-synthesis.md, notes/battle-action-stat-change-family-c2b2e0-b5d7.md, notes/equipment-preview-and-derived-state-cluster.md, +5 more
- `C2:192B` -> notes/equipment-slot-subtype-dispatch-c19066-c4577d.md, notes/equipped-item-derived-cache-family-c21857-c21e03.md, notes/level-up-stat-growth-helper-c1d08b.md
- `C2:1AEB` -> notes/battle-action-stat-change-family-c2b2e0-b5d7.md, notes/equipment-slot-subtype-dispatch-c19066-c4577d.md, notes/equipped-item-derived-cache-family-c21857-c21e03.md, +2 more
- `C2:1BA4` -> notes/battle-action-stat-change-family-c2b2e0-b5d7.md, notes/equipment-slot-subtype-dispatch-c19066-c4577d.md, notes/equipped-item-derived-cache-family-c21857-c21e03.md, +2 more
- `C2:1C5D` -> notes/battle-action-stat-change-family-c2b2e0-b5d7.md, notes/equipment-slot-subtype-dispatch-c19066-c4577d.md, notes/equipped-item-derived-cache-family-c21857-c21e03.md, +1 more
- `C2:1D65` -> notes/battle-action-stat-change-family-c2b2e0-b5d7.md, notes/equipped-item-derived-cache-family-c21857-c21e03.md, notes/level-up-stat-growth-helper-c1d08b.md, +1 more
- `C2:1D7D` -> notes/battle-action-stat-change-family-c2b2e0-b5d7.md, notes/equipped-item-derived-cache-family-c21857-c21e03.md, notes/text-command-family-1e-stat-recovery.md
- `C2:1D95` -> notes/equipment-slot-subtype-dispatch-c19066-c4577d.md, notes/equipped-item-derived-cache-family-c21857-c21e03.md
- `C2:1E03` -> notes/bank-c1-subsystem-and-symbol-synthesis.md, notes/battle-action-stat-change-family-c2b2e0-b5d7.md, notes/equipment-preview-and-derived-state-cluster.md, +5 more
- `C2:1F38` -> notes/equipped-item-derived-cache-family-c21857-c21e03.md
- `C2:2028` -> notes/equipped-item-derived-cache-family-c21857-c21e03.md
- `C2:20C7` -> notes/equipped-item-derived-cache-family-c21857-c21e03.md
- `C2:21B7` -> notes/equipment-slot-subtype-dispatch-c19066-c4577d.md, notes/equipped-item-derived-cache-family-c21857-c21e03.md
- `C2:2524` -> notes/text-command-family-19-data-and-substitution.md
- `C2:26D0` -> notes/class2-c2-handlers.md, notes/class2-dispatch-family.md
- `C2:26EB` -> notes/class2-c2-handlers.md, notes/class2-dispatch-family.md
- `C2:2730` -> notes/class2-dispatch-family.md
- `C2:27C8` -> notes/class2-dispatch-family.md, notes/reference-community-earthbound-docs.md
- `C2:281D` -> notes/bank-deposit-accumulator-98b9-98bb.md
- `C2:28F8` -> notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md, notes/class2-special-event-results-c29298-c2c14e.md, notes/mushroomized-walking-remap-family.md, +3 more
- `C2:29BB` -> notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md, notes/inventory-slot-removal-helper-c18c27.md, notes/mushroomized-walking-remap-family.md, +3 more
- `C2:30F3` -> notes/landing-display-profile-overview.md, notes/respawn-warp-target-snapshot-helper-c230f3.md, notes/saved-coordinate-reload-path-c4c718-c0b967.md, +2 more
- `C2:3109` -> notes/class2-battle-start-extra-message-state-4dbc-aa10.md, notes/class2-ufo-present-message-family.md
- `C2:312E` -> notes/c2-battle-sprite-render-and-palette-tail-c2eee7-c2ff9a.md
- `C2:38AF` -> notes/battle-selection-snapshot-export-c2b930.md
- `C2:39B4` -> notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md
- `C2:3B66` -> notes/class2-reflected-hit-context-rebuild.md
- `C2:3B91` -> notes/statistic-selector-family-c4550f-c3ee7a.md
- `C2:3BCF` -> notes/battle-text-entry-family-c1dc1c-dd7c.md, notes/class2-battle-text-cluster-overview.md, notes/class2-battle-text-dispatch-stack.md, +9 more
- `C2:3D05` -> notes/battle-text-entry-family-c1dc1c-dd7c.md, notes/class2-b6eb-caller-family-4dxx.md, notes/class2-battle-text-cluster-overview.md, +15 more
- `C2:3E60` -> notes/class2-mask-helper-family.md
- `C2:3E84` -> notes/direct-callers-c2-3d05.md
- `C2:40DA` -> notes/direct-callers-c2-3d05.md
- `C2:412F` -> notes/direct-callers-c2-3d05.md
- `C2:416F` -> notes/class2-handoff-4477-4703.md, notes/class2-psi-thunder-common-local-flow.md
- `C2:41B8` -> notes/class2-late-controller-path-77ca.md
- `C2:41CC` -> notes/class2-mask-helper-family.md
- `C2:41DC` -> notes/c2-steal-and-target-selection-helpers-c241dc-c24434.md
- `C2:4316` -> notes/c2-steal-and-target-selection-helpers-c241dc-c24434.md
- `C2:4477` -> notes/class2-dispatch-family.md, notes/class2-end-to-end-gate-path-5540.md, notes/class2-handoff-4477-4703.md, +4 more
- `C2:44C3` -> notes/c2-battle-sprite-render-and-palette-tail-c2eee7-c2ff9a.md
- `C2:462D` -> notes/c2-steal-and-target-selection-helpers-c241dc-c24434.md
- `C2:465A` -> notes/c2-steal-and-target-selection-helpers-c241dc-c24434.md
- `C2:4905` -> notes/c2-battlebg-load-and-palette-effect-corridor-c2cfe5-c2e0e7.md
- `C2:4922` -> notes/c2-battle-sprite-render-and-palette-tail-c2eee7-c2ff9a.md, notes/class2-candidate-population-and-ranking.md
- `C2:4958` -> notes/class2-candidate-population-and-ranking.md, notes/class2-source-families-986f-9f8a.md
- `C2:4984` -> notes/battle-selection-snapshot-export-c2b930.md
- `C2:49B1` -> notes/class2-local-enemy-id-to-battler-init-chain.md
- `C2:4A00` -> notes/c2-battle-sprite-render-and-palette-tail-c2eee7-c2ff9a.md, notes/class2-candidate-population-and-ranking.md
- `C2:4A18` -> notes/class2-local-enemy-id-to-battler-init-chain.md
- `C2:4A1F` -> notes/class2-9f8c-upstream-verification.md
- `C2:4A24` -> notes/class2-9f8c-upstream-verification.md, notes/class2-battlers-table-layout-9f8a-9fac.md, notes/class2-local-enemy-id-to-battler-init-chain.md
- `C2:4A32` -> notes/c2-battle-sprite-render-and-palette-tail-c2eee7-c2ff9a.md
- `C2:4A36` -> notes/c2-battle-sprite-render-and-palette-tail-c2eee7-c2ff9a.md
- `C2:4A4B` -> notes/class2-005e-record-domain.md, notes/class2-record-consumer-families.md
- `C2:4A7B` -> notes/battle-text-entry-family-c1dc1c-dd7c.md
- `C2:4A80` -> notes/class2-candidate-population-and-ranking.md, notes/class2-source-families-986f-9f8a.md
- ... 393 more

## Suggested Workflow

1. Pick an unmentioned `unknown/...` chunk from this report.
2. Run `tools/decode_snippet.py` or a targeted helper around the address.
3. Cross-check `refs/ebsrc-main` symbols, `refs/earthbound-disasm-legacy`, and any data table in `refs/eb-decompile-4ef92` that the routine touches.
4. Write a focused note that states byte-level evidence, borrowed reference names, remaining uncertainty, and direct callers/xrefs.
5. Rerun this audit and promote the next gap.

