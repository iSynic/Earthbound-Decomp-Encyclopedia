# Bank C4 Decompilation Progress Audit

This report cross-checks the local `notes/*.md` corpus against the quarantined `ebsrc-main` US bank include maps and symbol lists.

Treat reference names as corroboration only: a bank entry is not considered understood here just because a side reference gave it a label.

## Bank `C4` / reference bank `04`

- Reference include entries: `565`
- Reference named include entries without an address in the path: `200`
- Reference address-bearing include entries: `365`
- Address-bearing unknown include entries: `325`
- Reference symbols: `546` (`233` semantic-ish, `313` placeholder/redirect/null)
- Local notes mention `538` distinct `C4:xxxx` addresses
- Reference addresses mentioned by local notes: `327` / `367`
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
- `symbols/audiopacks.inc.asm`
- `symbols/doors.inc.asm`
- `symbols/globals.inc.asm`
- `symbols/map.inc.asm`
- `symbols/misc.inc.asm`
- `symbols/text.inc.asm`
- `data/events/script_pointers.asm`
- `data/map/footstep_sound_table.asm`
- `data/text/floating_sprite_table.asm`
- `data/events/scripts/785.asm`
- `data/events/entity_overlays.asm`
- `data/events/scripts/502.asm`
- `data/events/scripts/503.asm`
- `data/events/scripts/504.asm`
- `data/events/scripts/505.asm`
- `data/events/scripts/506.asm`
- `data/events/scripts/507.asm`
- `data/events/scripts/508.asm`
- `data/events/scripts/509.asm`
- `data/events/scripts/510.asm`
- `data/events/scripts/511.asm`
- `data/events/scripts/512.asm`
- `data/events/scripts/513.asm`
- `data/events/scripts/514.asm`
- `data/events/scripts/515.asm`
- `data/events/scripts/516.asm`
- `data/events/scripts/517.asm`
- `data/events/scripts/518.asm`
- `data/events/scripts/519.asm`
- `data/events/scripts/520.asm`
- `data/events/scripts/521.asm`
- `data/events/scripts/522.asm`
- `data/events/scripts/523.asm`
- `data/events/scripts/524.asm`
- `data/events/scripts/525.asm`
- `data/events/scripts/526.asm`
- `data/events/scripts/527.asm`
- `data/events/scripts/528.asm`
- `data/events/scripts/529.asm`
- `data/events/scripts/530.asm`
- `data/events/scripts/534.asm`
- `system/decomp.asm`
- `data/events/scripts/787.asm`
- `data/events/scripts/860.asm`
- `data/events/scripts/789.asm`
- `data/events/scripts/788.asm`
- `data/events/scripts/790.asm`
- `data/events/scripts/791.asm`
- `data/events/scripts/792.asm`
- `data/events/scripts/793.asm`
- `data/events/scripts/794.asm`
- `data/events/scripts/795.asm`
- `data/events/scripts/796.asm`
- `data/events/scripts/797.asm`
- `data/events/scripts/798.asm`
- `data/events/scripts/859.asm`
- `overworld/set_party_tick_callbacks.asm`
- `data/map/tile_table_chunks_table.asm`
- `overworld/velocity_store.asm`
- `data/item_use_menu_strings.asm`
- `text/print_newline.asm`
- `data/text/locked_tiles.asm`
- `text/get_character_at_cursor_position.asm`
- `text/free_tile.asm`
- `data/powers_of_two_16.asm`
- `text/free_tile_safe.asm`
- `data/text/battle_to_text.asm`
- `data/text/battle_front_row_text.asm`
- `data/text/battle_back_row_text.asm`
- `data/text/CC_1C_01_data.asm`
- ... 120 more

### Locally Corroborated Reference Addresses

- `C4:0000` -> notes/c4-early-ppu-and-text-tile-helpers-0000-0085.md
- `C4:0009` -> notes/c4-early-ppu-and-text-tile-helpers-0000-0085.md
- `C4:0015` -> notes/c3-actionscript-movement-pulse-presets-a0b2-ab26.md, notes/c3-temporary-actor-movement-and-release-scripts.md, notes/c4-early-ppu-and-text-tile-helpers-0000-0085.md
- `C4:0023` -> notes/c3-temporary-actor-movement-and-release-scripts.md, notes/c4-early-ppu-and-text-tile-helpers-0000-0085.md
- `C4:002F` -> notes/active-window-text-tile-pair-placement-c44c8c.md, notes/c4-early-ppu-and-text-tile-helpers-0000-0085.md, notes/c4-text-tile-staging-and-vector-helpers-1db6-213f.md
- `C4:0085` -> notes/active-window-text-tile-pair-placement-c44c8c.md, notes/c4-early-ppu-and-text-tile-helpers-0000-0085.md
- `C4:0B51` -> notes/c4-system-error-screen-render-0b51-0b75.md
- `C4:0B75` -> notes/c4-system-error-screen-render-0b51-0b75.md
- `C4:0BE8` -> notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md, notes/c4-system-error-screen-render-0b51-0b75.md, notes/entity-pool-allocation-and-release-c01a9d-c020f1.md, +3 more
- `C4:1DB6` -> notes/c4-text-tile-staging-and-vector-helpers-1db6-213f.md
- `C4:1EB9` -> notes/c4-text-tile-staging-and-vector-helpers-1db6-213f.md
- `C4:1EC9` -> notes/c4-text-tile-staging-and-vector-helpers-1db6-213f.md
- `C4:1ED9` -> notes/c4-text-tile-staging-and-vector-helpers-1db6-213f.md
- `C4:1EE9` -> notes/c4-text-tile-staging-and-vector-helpers-1db6-213f.md
- `C4:1EF4` -> notes/c4-text-tile-staging-and-vector-helpers-1db6-213f.md
- `C4:1EFF` -> notes/c4-text-tile-staging-and-vector-helpers-1db6-213f.md, notes/direction-octant-normalizers-c46a5e-c46b51.md, notes/entity-resolver-script-and-direction-wrappers-c460ce-c4645a.md, +4 more
- `C4:1FC5` -> notes/c4-text-tile-staging-and-vector-helpers-1db6-213f.md
- `C4:1FDF` -> notes/c4-text-tile-staging-and-vector-helpers-1db6-213f.md
- `C4:1FFF` -> notes/c0-small-utility-frontier-69f7-8c54.md, notes/c4-text-tile-staging-and-vector-helpers-1db6-213f.md, notes/direction-octant-normalizers-c46a5e-c46b51.md, +3 more
- `C4:205D` -> notes/c4-text-tile-staging-and-vector-helpers-1db6-213f.md
- `C4:20BD` -> notes/c4-text-tile-staging-and-vector-helpers-1db6-213f.md
- `C4:213F` -> notes/c4-text-tile-staging-and-vector-helpers-1db6-213f.md
- `C4:220E` -> notes/title-screen-logo-palette-event-helpers-c0ebe0-c0ee53.md
- `C4:2235` -> notes/title-screen-logo-palette-event-helpers-c0ebe0-c0ee53.md
- `C4:23DC` -> notes/c4-window-color-math-and-palette-helpers-23dc-26ed.md
- `C4:240A` -> notes/c4-window-color-math-and-palette-helpers-23dc-26ed.md
- `C4:2439` -> notes/actionscript-wrapper-strip-c0a841-c0aafd.md, notes/c4-window-color-math-and-palette-helpers-23dc-26ed.md
- `C4:245D` -> notes/c4-window-color-math-and-palette-helpers-23dc-26ed.md, notes/window-mask-and-indexed-gfx-c47501-c47b77.md
- `C4:248A` -> notes/c4-window-color-math-and-palette-helpers-23dc-26ed.md
- `C4:249A` -> notes/c4-window-color-math-and-palette-helpers-23dc-26ed.md, notes/palette-brightness-row-adjusters-c473b2-c474a8.md
- `C4:24D1` -> notes/c4-window-color-math-and-palette-helpers-23dc-26ed.md
- `C4:2509` -> notes/c4-window-color-math-and-palette-helpers-23dc-26ed.md
- `C4:2542` -> notes/c4-window-color-math-and-palette-helpers-23dc-26ed.md, notes/window-mask-and-indexed-gfx-c47501-c47b77.md
- `C4:2569` -> notes/c4-window-color-math-and-palette-helpers-23dc-26ed.md
- `C4:2574` -> notes/c4-window-color-math-and-palette-helpers-23dc-26ed.md
- `C4:257F` -> notes/c4-window-color-math-and-palette-helpers-23dc-26ed.md
- `C4:258C` -> notes/c4-window-color-math-and-palette-helpers-23dc-26ed.md
- `C4:25CC` -> notes/c4-window-color-math-and-palette-helpers-23dc-26ed.md, notes/window-mask-and-indexed-gfx-c47501-c47b77.md
- `C4:25F3` -> notes/c4-window-color-math-and-palette-helpers-23dc-26ed.md
- `C4:25FD` -> notes/c4-window-color-math-and-palette-helpers-23dc-26ed.md, notes/window-mask-and-indexed-gfx-c47501-c47b77.md
- `C4:2624` -> notes/c4-window-color-math-and-palette-helpers-23dc-26ed.md
- `C4:2631` -> notes/c4-window-color-math-and-palette-helpers-23dc-26ed.md
- `C4:268A` -> notes/c4-window-color-math-and-palette-helpers-23dc-26ed.md
- `C4:26C7` -> notes/c4-window-color-math-and-palette-helpers-23dc-26ed.md
- `C4:26ED` -> notes/c2-instant-win-and-magic-butterfly-helpers-c26189-c2654c.md, notes/c4-window-color-math-and-palette-helpers-23dc-26ed.md, notes/intro-logo-wait-and-gas-station-helpers-c0efe1-c0f21e.md, +7 more
- `C4:283F` -> notes/c4-visual-frame-copy-and-footprint-tables-283f-2b0d.md, notes/visual-record-constructor-and-latches-c4c8a4-c4cbe3.md
- `C4:2884` -> notes/c4-visual-frame-copy-and-footprint-tables-283f-2b0d.md, notes/visual-record-constructor-and-latches-c4c8a4-c4cbe3.md
- `C4:28D1` -> notes/c4-visual-frame-copy-and-footprint-tables-283f-2b0d.md, notes/visual-record-walkers-and-naming-remap-c4cc2f-c4d065.md
- `C4:28FC` -> notes/c4-visual-frame-copy-and-footprint-tables-283f-2b0d.md, notes/visual-record-walkers-and-naming-remap-c4cc2f-c4d065.md
- `C4:2955` -> notes/c4-visual-frame-copy-and-footprint-tables-283f-2b0d.md
- `C4:2965` -> notes/c4-visual-frame-copy-and-footprint-tables-283f-2b0d.md, notes/visual-record-walkers-and-naming-remap-c4cc2f-c4d065.md
- `C4:29AE` -> notes/c4-visual-frame-copy-and-footprint-tables-283f-2b0d.md, notes/visual-record-walkers-and-naming-remap-c4cc2f-c4d065.md
- `C4:29E8` -> notes/c4-visual-frame-copy-and-footprint-tables-283f-2b0d.md
- `C4:2A1F` -> notes/c4-visual-frame-copy-and-footprint-tables-283f-2b0d.md, notes/child-entity-spawn-c4b3d0-c40de8.md, notes/collision-surface-probes-c052d4-c05e3a.md, +5 more
- `C4:2A41` -> notes/c4-visual-frame-copy-and-footprint-tables-283f-2b0d.md, notes/child-entity-spawn-c4b3d0-c40de8.md, notes/collision-surface-probes-c052d4-c05e3a.md, +5 more
- `C4:2A63` -> notes/c4-visual-frame-copy-and-footprint-tables-283f-2b0d.md, notes/visual-record-constructor-and-latches-c4c8a4-c4cbe3.md
- `C4:2A85` -> notes/c4-visual-frame-copy-and-footprint-tables-283f-2b0d.md
- `C4:2AA7` -> notes/c4-visual-frame-copy-and-footprint-tables-283f-2b0d.md, notes/collision-surface-probes-c052d4-c05e3a.md, notes/pathfinding-frontier-c0b9bc-c0ba35.md
- `C4:2AC9` -> notes/c4-visual-frame-copy-and-footprint-tables-283f-2b0d.md, notes/collision-surface-probes-c052d4-c05e3a.md, notes/pathfinding-frontier-c0b9bc-c0ba35.md
- `C4:2AEB` -> notes/c4-visual-frame-copy-and-footprint-tables-283f-2b0d.md, notes/collision-surface-probes-c052d4-c05e3a.md, notes/entity-overlap-neighbor-cache-c05ece-c064d3.md, +3 more
- `C4:2B0D` -> notes/c4-visual-frame-copy-and-footprint-tables-283f-2b0d.md, notes/child-entity-spawn-c4b3d0-c40de8.md, notes/entity-pool-allocation-and-release-c01a9d-c020f1.md, +4 more
- `C4:2B51` -> notes/secondary-visual-descriptor-c42b0d.md
- `C4:2B5D` -> notes/secondary-visual-descriptor-c42b0d.md
- `C4:2B73` -> notes/secondary-visual-descriptor-c42b0d.md
- `C4:2B89` -> notes/secondary-visual-descriptor-c42b0d.md
- `C4:2BA9` -> notes/secondary-visual-descriptor-c42b0d.md
- `C4:2BBF` -> notes/secondary-visual-descriptor-c42b0d.md
- `C4:2BE9` -> notes/secondary-visual-descriptor-c42b0d.md
- `C4:2BFF` -> notes/secondary-visual-descriptor-c42b0d.md
- `C4:2C29` -> notes/secondary-visual-descriptor-c42b0d.md
- `C4:2C67` -> notes/secondary-visual-descriptor-c42b0d.md
- `C4:2CA5` -> notes/secondary-visual-descriptor-c42b0d.md
- `C4:2CC5` -> notes/secondary-visual-descriptor-c42b0d.md
- `C4:2D03` -> notes/secondary-visual-descriptor-c42b0d.md
- `C4:2D5F` -> notes/secondary-visual-descriptor-c42b0d.md
- `C4:2DD9` -> notes/secondary-visual-descriptor-c42b0d.md
- `C4:2E7B` -> notes/secondary-visual-descriptor-c42b0d.md
- `C4:2F8C` -> notes/entity-pool-allocation-and-release-c01a9d-c020f1.md, notes/overworld-companion-family-priority-a794.md, notes/overworld-walking-stutter-producer-split-c01558-c01ca8.md, +1 more
- `C4:303C` -> notes/entity-pool-allocation-and-release-c01a9d-c020f1.md, notes/secondary-visual-descriptor-c42b0d.md
- `C4:32B1` -> notes/c4-party-state-reset-and-callback-tables-30ec-3317.md
- ... 247 more

### Local-Only Address Mentions

These may be derived local discoveries, cross-bank targets, or address forms absent from the reference include/symbol map.

- `C4:008F` -> notes/c4-early-ppu-and-text-tile-helpers-0000-0085.md
- `C4:00A9` -> notes/c4-early-ppu-and-text-tile-helpers-0000-0085.md
- `C4:00B6` -> notes/c4-early-ppu-and-text-tile-helpers-0000-0085.md
- `C4:00B9` -> notes/c4-early-ppu-and-text-tile-helpers-0000-0085.md
- `C4:00D4` -> notes/bank-c0-entry-notes.md, notes/bank-c0-first-pass.md, notes/file-select-entity-scripts-and-swirl-transition-c4d830-c4d989.md, +2 more
- `C4:00D6` -> notes/bank-c0-entry-notes.md, notes/bank-c0-first-pass.md, notes/frame-callback-bodies.md
- `C4:0BD2` -> notes/c4-system-error-screen-render-0b51-0b75.md
- `C4:0DE8` -> notes/child-entity-spawn-c4b3d0-c40de8.md, notes/landing-and-coffee-tea-visual-helpers-c492d2-c49d1e.md, notes/landing-display-assembly-cluster-c007b6-c4b26b.md, +3 more
- `C4:0E32` -> notes/landing-display-assembly-cluster-c007b6-c4b26b.md
- `C4:0E42` -> notes/mushroomized-overlay-animation-scripts.md
- `C4:0EB0` -> notes/landing-display-assembly-cluster-c007b6-c4b26b.md, notes/mushroomized-overlay-animation-scripts.md, notes/mushroomized-walking-builders-34de-37d0.md
- `C4:0EE4` -> notes/landing-display-assembly-cluster-c007b6-c4b26b.md, notes/mushroomized-overlay-animation-scripts.md, notes/mushroomized-walking-builders-34de-37d0.md
- `C4:0EF0` -> notes/landing-display-assembly-cluster-c007b6-c4b26b.md, notes/mushroomized-overlay-animation-scripts.md, notes/mushroomized-walking-builders-34de-37d0.md
- `C4:0F04` -> notes/landing-display-assembly-cluster-c007b6-c4b26b.md, notes/mushroomized-overlay-animation-scripts.md, notes/mushroomized-walking-builders-34de-37d0.md
- `C4:1A9E` -> notes/c4-system-error-screen-render-0b51-0b75.md, notes/file-select-entity-scripts-and-swirl-transition-c4d830-c4d989.md, notes/gas-station-intro-asset-loader-c4a377.md, +6 more
- `C4:1BCA` -> notes/c4-text-tile-staging-and-vector-helpers-1db6-213f.md
- `C4:29D3` -> notes/overworld-walking-stutter-producer-split-c01558-c01ca8.md
- `C4:2B07` -> notes/c4-early-ppu-and-text-tile-helpers-0000-0085.md
- `C4:2F45` -> notes/teleport-mainloop-state-machines-c0e214-c0ebdf.md
- `C4:30EC` -> notes/c4-party-state-reset-and-callback-tables-30ec-3317.md
- `C4:339B` -> notes/collision-surface-probes-c052d4-c05e3a.md
- `C4:3492` -> notes/equipment-comparison-markers-9a1d.md
- `C4:38B1` -> notes/battle-psi-menu-table-helpers-c1c046-c1c165.md, notes/class2-reflected-hit-side-token-consumers.md, notes/text-command-00-line-break.md, +3 more
- `C4:3915` -> notes/text-window-rendering-primitives-c1078d-c10d7c.md
- `C4:406A` -> notes/text-input-dialog-option-helpers-c1e48d-c1e4be.md
- `C4:4127` -> notes/text-token-glyph-run-stager-c44b3a-c44e61.md
- `C4:4163` -> notes/text-token-glyph-run-stager-c44b3a-c44e61.md
- `C4:419A` -> notes/text-token-glyph-run-stager-c44b3a-c44e61.md
- `C4:41F3` -> notes/text-token-glyph-run-stager-c44b3a-c44e61.md
- `C4:4238` -> notes/text-token-glyph-run-stager-c44b3a-c44e61.md
- `C4:447A` -> notes/active-window-text-tile-pair-placement-c44c8c.md
- `C4:44F9` -> notes/text-input-dialog-option-helpers-c1e48d-c1e4be.md
- `C4:4AF7` -> notes/text-window-rendering-primitives-c1078d-c10d7c.md
- `C4:4C6C` -> notes/c4-early-ppu-and-text-tile-helpers-0000-0085.md
- `C4:4D17` -> notes/battle-text-display-mode-latch-964d.md
- `C4:4DD6` -> notes/staged-movement-pulse-and-tracked-item-registry-c48c59-c48f98.md
- `C4:4DFA` -> notes/c4-early-ppu-and-text-tile-helpers-0000-0085.md
- `C4:4E06` -> notes/c4-early-ppu-and-text-tile-helpers-0000-0085.md
- `C4:4E10` -> notes/c4-early-ppu-and-text-tile-helpers-0000-0085.md
- `C4:4E2D` -> notes/c4-early-ppu-and-text-tile-helpers-0000-0085.md
- `C4:4E4D` -> notes/active-window-text-tile-pair-placement-c44c8c.md, notes/text-entry-record-builder-neighbors-c10f40-c11887.md, notes/text-window-rendering-primitives-c1078d-c10d7c.md
- `C4:4F96` -> notes/staged-movement-pulse-and-tracked-item-registry-c48c59-c48f98.md
- `C4:516B` -> notes/text-window-rendering-primitives-c1078d-c10d7c.md
- `C4:54F0` -> notes/active-text-entry-chain-layout-c451fa.md, notes/class2-reflected-hit-side-buffer-flags.md, notes/class2-reflected-hit-side-token-consumers.md, +1 more
- `C4:54F1` -> notes/class2-reflected-hit-side-token-consumers.md, notes/class2-row-position-text-cluster-c454f0.md
- `C4:54F2` -> notes/class2-reflected-hit-side-token-consumers.md, notes/class2-row-position-text-cluster-c454f0.md
- `C4:54F5` -> notes/character-selection-prompt-cluster-c11f8a-c1242e.md
- `C4:5501` -> notes/class2-reflected-hit-side-token-consumers.md, notes/class2-row-position-text-cluster-c454f0.md
- `C4:5502` -> notes/character-selection-prompt-cluster-c11f8a-c1242e.md, notes/class2-reflected-hit-side-token-consumers.md, notes/class2-row-position-text-cluster-c454f0.md
- `C4:550D` -> notes/class2-reflected-hit-side-token-consumers.md, notes/class2-row-position-text-cluster-c454f0.md
- `C4:550E` -> notes/text-command-08-call-text.md
- `C4:550F` -> notes/early-naming-buffers-9819-9829.md, notes/item-psi-name-display-and-target-prompt-c19216-c19437.md, notes/naming-buffer-commit-family-c1ead6-c4d065.md, +3 more
- `C4:562F` -> notes/interaction-context-and-event-flags.md, notes/selector-row-config-family-ef0ee8.md
- `C4:5637` -> notes/class2-psi-thunder-reflection-branch.md, notes/party-inventory-room-search-c456e4-c4572b.md, notes/party-item-possession-search-c45637-c45683.md, +1 more
- `C4:5683` -> notes/class2-battler-core-field-crosswalk.md, notes/class2-psi-thunder-common-local-flow.md, notes/class2-psi-thunder-reflection-branch.md, +3 more
- `C4:56E4` -> notes/party-inventory-room-search-c456e4-c4572b.md, notes/text-command-family-1d-inventory-money.md
- `C4:572B` -> notes/party-inventory-room-search-c456e4-c4572b.md, notes/text-command-family-1d-inventory-money.md
- `C4:577D` -> notes/equipment-comparison-markers-9a1d.md, notes/equipment-menu-top-level-flow-c1a778-c1aa5d.md, notes/equipment-preview-and-derived-state-cluster.md, +4 more
- `C4:57CA` -> notes/equipment-slot-subtype-dispatch-c19066-c4577d.md, notes/inventory-slot-removal-helper-c18c27.md
- `C4:5815` -> notes/equipment-slot-subtype-dispatch-c19066-c4577d.md, notes/inventory-slot-removal-helper-c18c27.md
- `C4:5860` -> notes/equipment-slot-subtype-dispatch-c19066-c4577d.md, notes/inventory-slot-removal-helper-c18c27.md
- `C4:58AB` -> notes/battle-item-action-selection-c1ce85-c1cfc6.md, notes/c3-shared-helper-working-name-promotion.md, notes/item-slot-helper-pair-c3e977-c3ee14.md
- `C4:58AF` -> notes/text-command-family-19-data-and-substitution.md
- `C4:58FE` -> notes/text-command-1f41-special-event-dispatch-c1befc.md, notes/text-command-family-19-data-and-substitution.md
- `C4:5963` -> notes/item-psi-name-display-and-target-prompt-c19216-c19437.md
- `C4:599A` -> notes/text-command-family-19-data-and-substitution.md
- `C4:59A0` -> notes/statistic-selector-family-c4550f-c3ee7a.md
- `C4:5A27` -> notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md
- `C4:5A89` -> notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md
- `C4:5AE7` -> notes/c4-early-ppu-and-text-tile-helpers-0000-0085.md
- `C4:5AEB` -> notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md
- `C4:5C2C` -> notes/equipment-menu-display-fringe-c19a11-c19f29.md
- `C4:5C58` -> notes/equipment-menu-top-level-flow-c1a778-c1aa5d.md
- `C4:5C82` -> notes/equipment-menu-top-level-flow-c1a778-c1aa5d.md
- `C4:5C8A` -> notes/text-command-1f41-special-event-dispatch-c1befc.md
- `C4:5EC9` -> notes/text-window-rendering-primitives-c1078d-c10d7c.md
- `C4:5F40` -> notes/statistic-selector-family-c4550f-c3ee7a.md
- `C4:5F7B` -> notes/level-up-stat-growth-helper-c1d08b.md, notes/staged-movement-pulse-and-tracked-item-registry-c48c59-c48f98.md, notes/text-command-1f41-special-event-dispatch-c1befc.md, +2 more
- `C4:5FA8` -> notes/direction-octant-normalizers-c46a5e-c46b51.md, notes/pathfinding-consumers-direction-helpers-c0bd96-c0c7db.md
- `C4:629D` -> notes/c4-text-tile-staging-and-vector-helpers-1db6-213f.md
- ... 131 more

## Suggested Workflow

1. Pick an unmentioned `unknown/...` chunk from this report.
2. Run `tools/decode_snippet.py` or a targeted helper around the address.
3. Cross-check `refs/ebsrc-main` symbols, `refs/earthbound-disasm-legacy`, and any data table in `refs/eb-decompile-4ef92` that the routine touches.
4. Write a focused note that states byte-level evidence, borrowed reference names, remaining uncertainty, and direct callers/xrefs.
5. Rerun this audit and promote the next gap.

