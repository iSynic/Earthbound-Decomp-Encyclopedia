# C0 Movement And Collision Runtime Polish

Status: first C0 runtime semantic polish slice.

This note records the byte-neutral source comments added for the movement plus
collision slice from `notes/c0-runtime-semantic-polish-plan.md`. The goal is to
make the existing source modules easier to read without promoting new opcodes,
splitting scaffolds, or changing generated manifests.

## Source Modules Touched

| Source module | Runtime contract pinned |
| --- | --- |
| `src/c0/c0_4c45_commit_player_position_snapshot_tick.asm` | `$987D` indexes the 12-byte `$5156` party trail/snapshot ring; `$98A5` diverts normal movement into temporary modes. |
| `src/c0/c0_449b_step_player_from_directional_input.asm` | Normal input path runs `C0:404F -> C0:5B7B/C0:5FD1/C0:5FF6 -> C0:7526` before committing accepted movement. |
| `src/c0/c0_54c9_read_collision_byte_and_latch_bit10_coord.asm` | `$E000` is the active 64x64 collision byte page; collision bit `#$10` latches trigger coordinates into `$5DA8/$5DAA`. |
| `src/c0/c0_5b7b_resolve_movement_surface_collision.asm` | `$5DA4` accumulates collision bytes, `$5DA6` stores selected surface mode, and `$5DB8` marks mode changes. |
| `src/c0/c0_5e3b_update_slot_collision_cache.asm` | `$28DA[slot]` is the per-slot collision/terrain cache populated from footprint collision bits. |
| `src/c0/c0_5e82_update_current_slot_collision_cache_with_terrain_compatibility.asm` | Terrain compatibility is ORed into the cache only when the ordinary collision probe is clear. |
| `src/c0/c0_5de7_classify_entity_terrain_compatibility.asm` | Low collision bits map into the `D5:9589 + $20` terrain-compatibility byte and return `#$0080` on failure. |

## Evidence Inputs

- `notes/position-snapshot-and-movement-tick-c0449b-c05200.md`
- `notes/collision-surface-probes-c052d4-c05e3a.md`
- `notes/map-collision-runtime-bit-contract.md`
- `notes/movement-trigger-lookup-7477.md`
- `notes/staged-movement-queue.md`

## Promotion Boundary

This slice promotes comments and local runtime wording only. It does not rename
WRAM fields globally, regenerate C0 source, or claim final gameplay labels for
surface modes. The open labels remain:

- final names for `$5DA4/$5DA6/$5DB8` beyond collision/surface resolver context
- final gameplay labels for surface-mode return values
- the loader/populator contract for the active `$E000` collision page
- broader C0/C4 naming for footprint geometry tables

## Validation

Run after source-comment edits:

```powershell
python tools\validate_source_bank_byte_equivalence.py --bank C0 --module all --combined --scaffold src\c0\bank_c0_helpers_asar.asm --strict
```
