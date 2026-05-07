# Bank C0 Decompilation Progress Audit

This report cross-checks the local `notes/*.md` corpus against the quarantined `ebsrc-main` US bank include maps and symbol lists.

Treat reference names as corroboration only: a bank entry is not considered understood here just because a side reference gave it a label.

## Bank `C0` / reference bank `00`

- Reference include entries: `666`
- Reference named include entries without an address in the path: `278`
- Reference address-bearing include entries: `386`
- Address-bearing unknown include entries: `385`
- Reference symbols: `579` (`270` semantic-ish, `309` placeholder/redirect/null)
- Local notes mention `3636` distinct `C0:xxxx` addresses
- Reference addresses mentioned by local notes: `391` / `391`
- Unknown include entries not directly mentioned in local notes: `0`

### Reference-Named Include Families

These are already semantically grouped by `ebsrc-main`; use them as corroborating names, not as final local proof.

- `common.asm`
- `config.asm`
- `eventmacros.asm`
- `structs.asm`
- `symbols/bank00.inc.asm`
- `symbols/bank01.inc.asm`
- `symbols/bank02.inc.asm`
- `symbols/bank03.inc.asm`
- `symbols/bank04.inc.asm`
- `symbols/bank2f.inc.asm`
- `symbols/doors.inc.asm`
- `symbols/globals.inc.asm`
- `symbols/map.inc.asm`
- `symbols/misc.inc.asm`
- `symbols/sram.inc.asm`
- `symbols/text.inc.asm`
- `overworld/actionscript/clear_entity_draw_sorting_table.asm`
- `overworld/setup_vram.asm`
- `overworld/initialize.asm`
- `system/load_tileset_anim.asm`
- `system/animate_tileset.asm`
- `system/load_palette_anim.asm`
- `system/animate_palette.asm`
- `system/get_colour_average.asm`
- `overworld/adjust_single_colour.asm`
- `overworld/adjust_sprite_palettes_by_average.asm`
- `overworld/prepare_average_for_sprite_palettes.asm`
- `overworld/load_tile_collision.asm`
- `overworld/replace_block.asm`
- `overworld/load_map_block_event_changes.asm`
- `overworld/load_special_sprite_palette.asm`
- `overworld/load_map_palette.asm`
- `overworld/load_map_at_sector.asm`
- `overworld/load_sector_attributes.asm`
- `overworld/load_map_row.asm`
- `overworld/load_map_column.asm`
- `overworld/load_collision_row.asm`
- `overworld/load_collision_column.asm`
- `overworld/reload_map_at_position.asm`
- `overworld/load_map_at_position.asm`
- `overworld/refresh_map_at_position.asm`
- `overworld/reload_map.asm`
- `overworld/initialize_map.asm`
- `overworld/initialize_misc_object_data.asm`
- `overworld/find_free_space_7E4682.asm`
- `system/alloc_sprite_mem.asm`
- `overworld/create_entity.asm`
- `overworld/spawn_horizontal.asm`
- `overworld/spawn_vertical.asm`
- `overworld/reset_mushroomized_walking.asm`
- `overworld/mushroomization_movement_swap.asm`
- `overworld/adjust_position_horizontal.asm`
- `overworld/adjust_position_vertical.asm`
- `overworld/update_party.asm`
- `overworld/get_on_bicycle.asm`
- `system/center_screen.asm`
- `overworld/map_input_to_direction.asm`
- `overworld/find_nearby_checkable_tpt_entry.asm`
- `overworld/find_nearby_talkable_tpt_entry.asm`
- `battle/init_common.asm`
- `overworld/npc_collision_check.asm`
- `overworld/screen_transition.asm`
- `overworld/get_screen_transition_sound_effect.asm`
- `overworld/change_music_5DD6.asm`
- `overworld/spawn_buzz_buzz.asm`
- `overworld/door_transition.asm`
- `overworld/disable_hotspot.asm`
- `overworld/reload_hotspots.asm`
- `overworld/activate_hotspot.asm`
- `overworld/process_queued_interactions.asm`
- `system/strcat.asm`
- `system/reset.asm`
- `system/reset_vector.asm`
- `system/nmi_vector.asm`
- `system/irq_vector.asm`
- `system/irq_nmi.asm`
- `system/test_sram_size.asm`
- `system/read_joypad.asm`
- `system/process_sfx_queue.asm`
- `system/execute_irq_callback.asm`
- ... 198 more

### Locally Corroborated Reference Addresses

- `C0:035B` -> notes/bank-c0-entry-notes.md
- `C0:0E16` -> notes/early-entity-map-reset-family-c019e2-c01a86.md, notes/overworld-stutter-current-truth-state.md, notes/overworld-walking-stutter-producer-split-c01558-c01ca8.md, +1 more
- `C0:0FCB` -> notes/overworld-walking-stutter-producer-split-c01558-c01ca8.md, notes/rom-patch-overworld-stutter-plan.md
- `C0:1181` -> notes/overworld-walking-stutter-producer-split-c01558-c01ca8.md, notes/rom-patch-overworld-stutter-plan.md
- `C0:122A` -> notes/rom-patch-overworld-stutter-plan.md
- `C0:1731` -> notes/rom-patch-overworld-stutter-plan.md
- `C0:17EA` -> notes/input-direction-and-interaction-probes-c0402b-c04116.md, notes/overworld-camera-step-accumulator-c017ea-c018f2.md, notes/overworld-stutter-current-truth-state.md, +1 more
- `C0:19E2` -> notes/early-entity-map-reset-family-c019e2-c01a86.md, notes/entity-pool-allocation-and-release-c01a9d-c020f1.md
- `C0:1A63` -> notes/early-entity-map-reset-family-c019e2-c01a86.md
- `C0:1A86` -> notes/early-entity-map-reset-family-c019e2-c01a86.md, notes/entity-pool-allocation-and-release-c01a9d-c020f1.md, notes/intro-overworld-position-init-c0b65f-c0b67f.md
- `C0:1B15` -> notes/bank-c0-entry-notes.md, notes/early-entity-map-reset-family-c019e2-c01a86.md, notes/entity-pool-allocation-and-release-c01a9d-c020f1.md
- `C0:1B96` -> notes/bank-c0-entry-notes.md, notes/entity-pool-allocation-and-release-c01a9d-c020f1.md
- `C0:1C52` -> notes/entity-pool-allocation-and-release-c01a9d-c020f1.md
- `C0:1D38` -> notes/entity-pool-allocation-and-release-c01a9d-c020f1.md, notes/secondary-visual-descriptor-c42b0d.md, notes/sprite-pose-descriptor-header-bytes-2-7.md
- `C0:1DED` -> notes/entity-pool-allocation-and-release-c01a9d-c020f1.md, notes/secondary-visual-descriptor-c42b0d.md
- `C0:20F1` -> notes/bank-c0-entry-notes.md, notes/early-entity-map-reset-family-c019e2-c01a86.md, notes/entity-placement-probe-c0263d-c02668.md, +1 more
- `C0:2140` -> notes/bank-c0-entry-notes.md, notes/bicycle-transition-and-party-registry-c03c25-c03f1e.md, notes/early-entity-map-reset-family-c019e2-c01a86.md, +3 more
- `C0:2194` -> notes/bank-c0-entry-notes.md, notes/rom-patch-overworld-stutter-plan.md
- `C0:21E6` -> notes/bank-c0-entry-notes.md
- `C0:222B` -> notes/bank-c0-entry-notes.md
- `C0:255C` -> notes/overworld-walking-stutter-producer-split-c01558-c01ca8.md, notes/rom-patch-overworld-stutter-plan.md
- `C0:25CF` -> notes/overworld-walking-stutter-producer-split-c01558-c01ca8.md, notes/rom-patch-overworld-stutter-plan.md
- `C0:263D` -> notes/bank-c0-entry-notes.md, notes/entity-placement-probe-c0263d-c02668.md
- `C0:2668` -> notes/bank-c0-entry-notes.md, notes/entity-placement-probe-c0263d-c02668.md
- `C0:2C3E` -> notes/entity-placement-probe-c0263d-c02668.md, notes/mushroomized-walking-builders-34de-37d0.md
- `C0:2D29` -> notes/class2-c1-display-text-substitution-handler-7af3.md, notes/intro-overworld-position-init-c0b65f-c0b67f.md
- `C0:329F` -> notes/bank-c0-entry-notes.md, notes/bicycle-transition-and-party-registry-c03c25-c03f1e.md, notes/character-affliction-clear-c0329f.md, +2 more
- `C0:32EC` -> notes/character-affliction-clear-c0329f.md, notes/mushroomized-walking-builders-34de-37d0.md
- `C0:369B` -> notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md, notes/class2-cc19-20-eshop2-single-use.md, notes/mushroomized-walking-builders-34de-37d0.md, +1 more
- `C0:3903` -> notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md, notes/teddy-bear-and-egg-item-cleanup-branches.md
- `C0:39E5` -> notes/bank-c0-entry-notes.md, notes/intro-overworld-position-init-c0b65f-c0b67f.md, notes/mushroomized-walking-builders-34de-37d0.md
- `C0:3A24` -> notes/class2-cc19-20-eshop2-single-use.md, notes/intro-overworld-position-init-c0b65f-c0b67f.md, notes/mushroomized-walking-builders-34de-37d0.md, +1 more
- `C0:3A94` -> notes/bicycle-transition-and-party-registry-c03c25-c03f1e.md, notes/class3-doorway-transition-context.md, notes/landing-destination-table-d57880.md, +2 more
- `C0:3C25` -> notes/bank-c0-entry-notes.md, notes/bicycle-transition-and-party-registry-c03c25-c03f1e.md, notes/position-snapshot-and-movement-tick-c0449b-c05200.md, +2 more
- `C0:3C4B` -> notes/bicycle-transition-and-party-registry-c03c25-c03f1e.md, notes/collision-surface-probes-c052d4-c05e3a.md, notes/seam-scout-c0-gap-cluster-329f-3f1e.md
- `C0:3CFD` -> notes/bank-c0-entry-notes.md, notes/bicycle-transition-and-party-registry-c03c25-c03f1e.md, notes/class3-doorway-transition-context.md, +2 more
- `C0:3DAA` -> notes/bicycle-transition-and-party-registry-c03c25-c03f1e.md, notes/seam-scout-c0-gap-cluster-329f-3f1e.md
- `C0:3E25` -> notes/bicycle-transition-and-party-registry-c03c25-c03f1e.md, notes/overworld-entity-type-registry-9887-98a4.md, notes/seam-scout-c0-gap-cluster-329f-3f1e.md
- `C0:3E5A` -> notes/bicycle-transition-and-party-registry-c03c25-c03f1e.md, notes/overworld-entity-type-registry-9887-98a4.md, notes/seam-scout-c0-gap-cluster-329f-3f1e.md
- `C0:3E9D` -> notes/bicycle-transition-and-party-registry-c03c25-c03f1e.md, notes/overworld-entity-type-registry-9887-98a4.md, notes/seam-scout-c0-gap-cluster-329f-3f1e.md
- `C0:3EC3` -> notes/bicycle-transition-and-party-registry-c03c25-c03f1e.md, notes/overworld-entity-type-registry-9887-98a4.md, notes/position-snapshot-and-movement-tick-c0449b-c05200.md, +2 more
- `C0:3F1E` -> notes/bank-c0-entry-notes.md, notes/bicycle-transition-and-party-registry-c03c25-c03f1e.md, notes/collision-surface-probes-c052d4-c05e3a.md, +3 more
- `C0:3FA9` -> notes/bicycle-transition-and-party-registry-c03c25-c03f1e.md, notes/collision-surface-probes-c052d4-c05e3a.md, notes/post-transition-deferred-script-queue-c06b21-c06bff.md, +2 more
- `C0:402B` -> notes/bank-c0-entry-notes.md, notes/input-direction-and-interaction-probes-c0402b-c04116.md
- `C0:4049` -> notes/bank-c0-entry-notes.md, notes/input-direction-and-interaction-probes-c0402b-c04116.md
- `C0:4116` -> notes/bank-c0-entry-notes.md, notes/front-interaction-flow.md, notes/input-direction-and-interaction-probes-c0402b-c04116.md
- `C0:41E3` -> notes/bank-c0-entry-notes.md, notes/bank-c0-first-pass.md, notes/front-interaction-flow.md, +1 more
- `C0:42C2` -> notes/bank-c0-first-pass.md, notes/interaction-result-classes.md, notes/interaction-result-consumers.md
- `C0:42EF` -> notes/bank-c0-first-pass.md, notes/front-interaction-flow.md, notes/input-direction-and-interaction-probes-c0402b-c04116.md
- `C0:43BC` -> notes/bank-c0-first-pass.md, notes/front-interaction-flow.md, notes/input-direction-and-interaction-probes-c0402b-c04116.md, +1 more
- `C0:449B` -> notes/bank-c0-entry-notes.md, notes/position-snapshot-and-movement-tick-c0449b-c05200.md, notes/saved-coordinate-reload-path-c4c718-c0b967.md
- `C0:476D` -> notes/position-snapshot-and-movement-tick-c0449b-c05200.md
- `C0:47CF` -> notes/bank-c0-entry-notes.md, notes/position-snapshot-and-movement-tick-c0449b-c05200.md
- `C0:48D3` -> notes/bank-c0-entry-notes.md, notes/position-snapshot-and-movement-tick-c0449b-c05200.md
- `C0:4A7B` -> notes/position-snapshot-and-movement-tick-c0449b-c05200.md
- `C0:4A88` -> notes/npc-attention-path-coordinator-c0d19b-c0d98f.md, notes/position-snapshot-and-movement-tick-c0449b-c05200.md
- `C0:4AAD` -> notes/position-snapshot-and-movement-tick-c0449b-c05200.md
- `C0:4B53` -> notes/bank-c0-entry-notes.md, notes/position-snapshot-and-movement-tick-c0449b-c05200.md
- `C0:4C45` -> notes/bank-c0-entry-notes.md, notes/collision-surface-probes-c052d4-c05e3a.md, notes/position-snapshot-and-movement-tick-c0449b-c05200.md
- `C0:4D78` -> notes/bank-c0-entry-notes.md, notes/position-snapshot-and-movement-tick-c0449b-c05200.md, notes/teleport-mainloop-state-machines-c0e214-c0ebdf.md
- `C0:4EF0` -> notes/bank-c0-entry-notes.md, notes/position-snapshot-and-movement-tick-c0449b-c05200.md
- `C0:4F47` -> notes/delayed-action-timer-callers.md
- `C0:4F60` -> notes/position-snapshot-and-movement-tick-c0449b-c05200.md
- `C0:4F9F` -> notes/position-snapshot-and-movement-tick-c0449b-c05200.md
- `C0:4FFE` -> notes/position-snapshot-and-movement-tick-c0449b-c05200.md, notes/saved-coordinate-reload-path-c4c718-c0b967.md
- `C0:5200` -> notes/bank-c0-entry-notes.md, notes/position-snapshot-and-movement-tick-c0449b-c05200.md, notes/saved-coordinate-reload-path-c4c718-c0b967.md, +1 more
- `C0:52D4` -> notes/bank-c0-entry-notes.md, notes/class4-class6-surface-contexts.md, notes/collision-surface-probes-c052d4-c05e3a.md, +2 more
- `C0:546B` -> notes/bank-c0-entry-notes.md, notes/collision-surface-probes-c052d4-c05e3a.md, notes/pathfinding-consumers-direction-helpers-c0bd96-c0c7db.md
- `C0:54C9` -> notes/bank-c0-entry-notes.md, notes/collision-surface-probes-c052d4-c05e3a.md, notes/entity-overlap-neighbor-cache-c05ece-c064d3.md, +1 more
- `C0:5503` -> notes/collision-surface-probes-c052d4-c05e3a.md, notes/entity-overlap-neighbor-cache-c05ece-c064d3.md
- `C0:559C` -> notes/collision-surface-probes-c052d4-c05e3a.md, notes/entity-overlap-neighbor-cache-c05ece-c064d3.md
- `C0:5639` -> notes/collision-surface-probes-c052d4-c05e3a.md, notes/entity-overlap-neighbor-cache-c05ece-c064d3.md
- `C0:56D0` -> notes/collision-surface-probes-c052d4-c05e3a.md, notes/entity-overlap-neighbor-cache-c05ece-c064d3.md
- `C0:5769` -> notes/bank-c0-entry-notes.md, notes/collision-surface-probes-c052d4-c05e3a.md
- `C0:57E8` -> notes/class4-class6-surface-contexts.md, notes/collision-surface-probes-c052d4-c05e3a.md
- `C0:583C` -> notes/class4-class6-surface-contexts.md, notes/collision-surface-probes-c052d4-c05e3a.md
- `C0:5890` -> notes/class4-class6-surface-contexts.md, notes/collision-surface-probes-c052d4-c05e3a.md
- `C0:59EF` -> notes/class4-class6-surface-contexts.md, notes/collision-surface-probes-c052d4-c05e3a.md
- `C0:5B4E` -> notes/class4-class6-surface-contexts.md, notes/collision-surface-probes-c052d4-c05e3a.md
- `C0:5B7B` -> notes/bank-c0-entry-notes.md, notes/class4-class6-surface-contexts.md, notes/collision-surface-probes-c052d4-c05e3a.md, +2 more
- ... 311 more

### Local-Only Address Mentions

These may be derived local discoveries, cross-bank targets, or address forms absent from the reference include/symbol map.

- `C0:0085` -> notes/landing-display-assembly-cluster-c007b6-c4b26b.md, notes/landing-profile-bundles-ef121b-43dc.md, notes/landing-profile-cache-436e-4474.md
- `C0:0172` -> notes/landing-profile-asset-families-ef105b-10ab-11cb-121b.md, notes/landing-profile-bundles-ef121b-43dc.md, notes/position-snapshot-and-movement-tick-c0449b-c05200.md
- `C0:023F` -> notes/landing-display-assembly-cluster-c007b6-c4b26b.md, notes/landing-profile-cache-436e-4474.md
- `C0:030F` -> notes/landing-display-assembly-cluster-c007b6-c4b26b.md, notes/landing-profile-cache-436e-4474.md, notes/position-snapshot-and-movement-tick-c0449b-c05200.md
- `C0:0391` -> notes/landing-display-assembly-cluster-c007b6-c4b26b.md, notes/landing-palette-interpolation-export-c4958e-c426ed.md
- `C0:0480` -> notes/landing-display-assembly-cluster-c007b6-c4b26b.md, notes/landing-display-profile-overview.md, notes/landing-palette-interpolation-export-c4958e-c426ed.md
- `C0:062A` -> notes/landing-hdma-dispatch-family-ef117b-c00d7e.md, notes/landing-profile-asset-families-ef105b-10ab-11cb-121b.md
- `C0:0778` -> notes/landing-display-assembly-cluster-c007b6-c4b26b.md, notes/landing-display-profile-overview.md
- `C0:07B6` -> notes/landing-display-assembly-cluster-c007b6-c4b26b.md, notes/landing-display-control-words-2baa-2e7a.md, notes/landing-display-profile-overview.md, +3 more
- `C0:08CF` -> notes/landing-destination-table-d57880.md, notes/landing-display-profile-overview.md, notes/landing-profile-asset-families-ef105b-10ab-11cb-121b.md, +3 more
- `C0:090E` -> notes/landing-profile-asset-families-ef105b-10ab-11cb-121b.md
- `C0:091A` -> notes/landing-profile-asset-families-ef105b-10ab-11cb-121b.md
- `C0:0968` -> notes/landing-profile-asset-families-ef105b-10ab-11cb-121b.md
- `C0:0974` -> notes/landing-profile-cache-436e-4474.md
- `C0:097B` -> notes/landing-profile-cache-436e-4474.md
- `C0:097E` -> notes/landing-profile-asset-families-ef105b-10ab-11cb-121b.md
- `C0:09BE` -> notes/landing-profile-asset-families-ef105b-10ab-11cb-121b.md
- `C0:09D1` -> notes/rom-patch-overworld-stutter-plan.md
- `C0:09EA` -> notes/rom-patch-overworld-stutter-plan.md
- `C0:09FA` -> notes/landing-display-assembly-cluster-c007b6-c4b26b.md
- `C0:0A0B` -> notes/landing-display-assembly-cluster-c007b6-c4b26b.md
- `C0:0A12` -> notes/landing-display-assembly-cluster-c007b6-c4b26b.md
- `C0:0A95` -> notes/landing-profile-cache-436e-4474.md
- `C0:0A9A` -> notes/landing-profile-cache-436e-4474.md
- `C0:0AA1` -> notes/c2-battle-sprite-render-and-palette-tail-c2eee7-c2ff9a.md, notes/class3-doorway-transition-context.md, notes/landing-destination-table-d57880.md, +5 more
- `C0:0AC5` -> notes/early-entity-map-reset-family-c019e2-c01a86.md, notes/overworld-walking-stutter-producer-split-c01558-c01ca8.md, notes/rom-patch-overworld-stutter-plan.md
- `C0:0B8C` -> notes/task-freeze-position-callbacks-maplookup-c09f3b-c0a26b.md
- `C0:0BDC` -> notes/overworld-walking-stutter-producer-split-c01558-c01ca8.md, notes/rom-patch-overworld-stutter-plan.md
- `C0:0C9C` -> notes/task-freeze-position-callbacks-maplookup-c09f3b-c0a26b.md
- `C0:0CF3` -> notes/early-entity-map-reset-family-c019e2-c01a86.md, notes/overworld-walking-stutter-producer-split-c01558-c01ca8.md, notes/rom-patch-overworld-stutter-plan.md
- `C0:0D39` -> notes/landing-hdma-dispatch-family-ef117b-c00d7e.md, notes/landing-profile-asset-families-ef105b-10ab-11cb-121b.md
- `C0:0D7E` -> notes/landing-display-profile-overview.md, notes/landing-hdma-dispatch-family-ef117b-c00d7e.md, notes/landing-profile-asset-families-ef105b-10ab-11cb-121b.md, +2 more
- `C0:0DB7` -> notes/landing-hdma-dispatch-family-ef117b-c00d7e.md, notes/landing-profile-asset-families-ef105b-10ab-11cb-121b.md
- `C0:0F40` -> notes/rom-patch-overworld-stutter-plan.md
- `C0:0F6C` -> notes/rom-patch-overworld-stutter-plan.md
- `C0:0F99` -> notes/rom-patch-overworld-stutter-plan.md
- `C0:0FC5` -> notes/rom-patch-overworld-stutter-plan.md
- `C0:10FA` -> notes/rom-patch-overworld-stutter-plan.md
- `C0:1122` -> notes/rom-patch-overworld-stutter-plan.md
- `C0:1153` -> notes/rom-patch-overworld-stutter-plan.md
- `C0:117B` -> notes/rom-patch-overworld-stutter-plan.md
- `C0:13F6` -> notes/intro-overworld-position-init-c0b65f-c0b67f.md, notes/overworld-camera-step-accumulator-c017ea-c018f2.md, notes/post-transition-deferred-script-queue-c06b21-c06bff.md, +2 more
- `C0:1404` -> notes/overworld-a794-watcher-gate-safe-v4.md, notes/rom-patch-overworld-stutter-plan.md
- `C0:1533` -> notes/entity-placement-probe-c0263d-c02668.md
- `C0:1558` -> notes/overworld-camera-step-accumulator-c017ea-c018f2.md, notes/overworld-companion-family-priority-a794.md, notes/overworld-stutter-current-truth-state.md, +4 more
- `C0:1566` -> notes/overworld-timing-scroll-commit-slice-c08b20-c08284.md
- `C0:156B` -> notes/overworld-timing-scroll-commit-slice-c08b20-c08284.md
- `C0:1570` -> notes/overworld-timing-scroll-commit-slice-c08b20-c08284.md
- `C0:1575` -> notes/overworld-timing-scroll-commit-slice-c08b20-c08284.md
- `C0:15B0` -> notes/rom-patch-overworld-stutter-plan.md
- `C0:15F4` -> notes/rom-patch-overworld-stutter-plan.md
- `C0:1606` -> notes/entity-placement-probe-c0263d-c02668.md, notes/rom-patch-overworld-stutter-plan.md
- `C0:1659` -> notes/entity-placement-probe-c0263d-c02668.md
- `C0:165D` -> notes/rom-patch-overworld-stutter-plan.md
- `C0:166B` -> notes/rom-patch-overworld-stutter-plan.md
- `C0:16B2` -> notes/rom-patch-overworld-stutter-plan.md
- `C0:16C4` -> notes/entity-placement-probe-c0263d-c02668.md, notes/rom-patch-overworld-stutter-plan.md
- `C0:1716` -> notes/entity-placement-probe-c0263d-c02668.md
- `C0:171A` -> notes/rom-patch-overworld-stutter-plan.md
- `C0:1725` -> notes/rom-patch-overworld-stutter-plan.md
- `C0:17C4` -> notes/overworld-walking-stutter-producer-split-c01558-c01ca8.md
- `C0:17D3` -> notes/overworld-walking-stutter-producer-split-c01558-c01ca8.md
- `C0:187E` -> notes/overworld-camera-step-accumulator-c017ea-c018f2.md
- `C0:1882` -> notes/overworld-camera-step-accumulator-c017ea-c018f2.md
- `C0:1887` -> notes/overworld-camera-step-accumulator-c017ea-c018f2.md
- `C0:188C` -> notes/overworld-camera-step-accumulator-c017ea-c018f2.md
- `C0:188F` -> notes/overworld-camera-step-accumulator-c017ea-c018f2.md
- `C0:1894` -> notes/overworld-camera-step-accumulator-c017ea-c018f2.md
- `C0:18A8` -> notes/overworld-camera-step-accumulator-c017ea-c018f2.md, notes/overworld-timing-scroll-commit-slice-c08b20-c08284.md
- `C0:18E5` -> notes/overworld-camera-step-accumulator-c017ea-c018f2.md
- `C0:18E8` -> notes/overworld-camera-step-accumulator-c017ea-c018f2.md
- `C0:18EB` -> notes/overworld-camera-step-accumulator-c017ea-c018f2.md
- `C0:18EE` -> notes/overworld-camera-step-accumulator-c017ea-c018f2.md
- `C0:18F1` -> notes/overworld-camera-step-accumulator-c017ea-c018f2.md
- `C0:18F2` -> notes/input-direction-and-interaction-probes-c0402b-c04116.md, notes/overworld-camera-step-accumulator-c017ea-c018f2.md
- `C0:19B2` -> notes/landing-destination-table-d57880.md, notes/saved-coordinate-reload-path-c4c718-c0b967.md, notes/teleport-freeze-vector-frontier-c0dd0f-c0e196.md, +1 more
- `C0:1A65` -> notes/early-entity-map-reset-family-c019e2-c01a86.md
- `C0:1A68` -> notes/early-entity-map-reset-family-c019e2-c01a86.md
- `C0:1A69` -> notes/early-entity-map-reset-family-c019e2-c01a86.md, notes/intro-overworld-position-init-c0b65f-c0b67f.md
- `C0:1A88` -> notes/early-entity-map-reset-family-c019e2-c01a86.md
- ... 3165 more

## Suggested Workflow

1. Pick an unmentioned `unknown/...` chunk from this report.
2. Run `tools/decode_snippet.py` or a targeted helper around the address.
3. Cross-check `refs/ebsrc-main` symbols, `refs/earthbound-disasm-legacy`, and any data table in `refs/eb-decompile-4ef92` that the routine touches.
4. Write a focused note that states byte-level evidence, borrowed reference names, remaining uncertainty, and direct callers/xrefs.
5. Rerun this audit and promote the next gap.

