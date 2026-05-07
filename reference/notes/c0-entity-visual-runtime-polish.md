# C0 Entity Visual Runtime Polish

Status: first C0 entity/visual lifecycle polish slice.

This note records the byte-neutral source comments added after
`notes/c0-movement-collision-runtime-polish.md`. The slice joins the early
entity reset helpers, `$467E` visual-record pool, `$4A00` reservation map,
sprite-pose descriptor setup, spawn candidate commit path, and release helpers.

## Source Modules Touched

| Source module | Runtime contract pinned |
| --- | --- |
| `src/c0/c0_1a69_reset_entity_slot_state_tables.asm` | Clears 30-slot overworld/entity state words, including `$2C9A` candidate markers. |
| `src/c0/c0_1a86_reset_entity_byte_pool467_e.asm` | `$467E..49FD` is the byte-backed visual/entity record pool initialized to `#$FF`. |
| `src/c0/c0_1a9d_find_free_entity_byte_pool_run467_e.asm` | Allocates byte runs in the `$467E` pool using 5-byte record markers at byte `+4`. |
| `src/c0/c0_1b15_release_entity_byte_pool_run467_e.asm` | Releases `$467E` record runs by clearing 5-byte records until byte `+4` bit 7 ends a run. |
| `src/c0/c0_1b96_reserve_visual_memory_span4_a00.asm` | `$4A00..4A57` is the compact visual-memory reservation map, with high-bit owner tokens. |
| `src/c0/c0_1c11_rewrite_visual_memory_reservations4_a00.asm` | Rewrites or frees `$4A00` reservations for one owner, or all owners with wildcard `#$8000`. |
| `src/c0/c0_1c52_reserve_and_upload_entity_visual_tiles.asm` | Pairs `$4A00` reservation with C4 visual tile uploads into the `$4000/$4100` VRAM bands. |
| `src/c0/c0_1d38_build_entity_visual_records467_e.asm` | Builds two passes of 5-byte `$467E` records from secondary visual descriptors and `C4:303C`. |
| `src/c0/c0_1ded_read_sprite_pose_visual_descriptor.asm` | Reads `EF:133F` sprite-pose descriptors and seeds `$467A/$467C` for visual setup. |
| `src/c0/c0_1e49_initialize_entity_with_sprite_pose.asm` | Creates the slot, stores `$112E/$116A` pointer to `$467E`, and seeds render/movement fields. |
| `src/c0/c0_20f1_script_release_current_entity_visual_state.asm` | Script-facing partial visual release without the broader task cleanup. |
| `src/c0/c0_2140_release_entity_slot_and_visual_state.asm` | Full visual plus slot release that also calls C0:9C35 task/entity cleanup. |
| `src/c0/c0_255c_run_vertical_companion_spawn_producer.asm` | Movement-adjacent vertical producer now calls the C0:222B spawn-entity template front door by name. |
| `src/c0/c0_25cf_run_horizontal_companion_spawn_producer.asm` | Movement-adjacent horizontal producer now calls the C0:222B spawn-entity template front door by name. |
| `src/c0/c0_28e7_try_place_spawn_candidate_from_list_entry.asm` | Resolves spawn-list entries through `D5:9589` row metadata. |
| `src/c0/c0_2957_initialize_spawned_candidate_entity_slot.asm` | Creates spawned candidate slots, probes placement, commits position and identity markers. |
| `src/c0/c0_2a50_iterate_spawn_candidate_list.asm` | Reads spawn-list count and enters the D5 metadata/spawn placement path. |
| `src/c0/c0_2a6b_spawn_horizontal.asm` | Horizontal spawn probes now name the D0:1880 placement lookup and spawn-list resolver calls. |
| `src/c0/c0_2b55_spawn_vertical.asm` | Vertical spawn probes now name the D0:1880 placement lookup and spawn-list resolver calls. |

## Source Polish Follow-Up

The 2026-05-06 C0 follow-up converted the entity visual lifecycle's remaining
ordinary helper-call edges to local contract names in the source. The pass tied
`C0:19E2/1A63` back to the movement strip payload/upload helpers, named the
`C0:1E49` descriptor/allocation/record-build/task-constructor calls, and
connected the release/spawn side through `C0:1B15`, `C0:1C11`, `C0:9C35`,
`C0:222B`, `C0:263D`, `C0:2668`, `C0:5DE7`, and `C0:5F33`. Raw calls still
present after the first `SPAWN_VERTICAL` body belong to later embedded tail
entries and should be handled as a separate presentation/scene lane.

## Evidence Inputs

- `notes/early-entity-map-reset-family-c019e2-c01a86.md`
- `notes/entity-pool-allocation-and-release-c01a9d-c020f1.md`
- `notes/entity-placement-probe-c0263d-c02668.md`
- `notes/overworld-walking-stutter-producer-split-c01558-c01ca8.md`
- `notes/secondary-visual-descriptor-c42b0d.md`

## Promotion Boundary

This slice promotes comments and local runtime wording only. It does not rename
WRAM fields globally, regenerate C0 source, or claim final player-facing names
for the entity visual layer. The open labels remain:

- exact field names for each byte in the 5-byte `$467E` visual records
- final gameplay vocabulary for the `$4A00` reservation map
- caller context for the `C4:D9A3` and `EF:E1A8` users of C0:1C11
- script-side meaning of `C0:20F1` beyond "partial current-slot visual release"
- final row-schema names for the `D5:9589` spawn/terrain metadata fields

## Validation

Run after source-comment edits:

```powershell
python tools\validate_source_bank_byte_equivalence.py --bank C0 --module all --combined --scaffold src\c0\bank_c0_helpers_asar.asm --strict
```
