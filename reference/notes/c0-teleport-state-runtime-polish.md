# C0 Teleport State Runtime Polish

Status: first C0 teleport/transition runtime polish slice.

This note records the byte-neutral source comments added after
`notes/c0-interaction-runtime-polish.md`. The slice focuses on teleport state
setup, transition-object freeze/unfreeze, collision/vector helpers, snapshot
ring writes, cadence updates, and interaction suppression around
`TELEPORT_MAINLOOP`.

## Source Modules Touched

| Source module | Runtime contract pinned |
| --- | --- |
| `src/c0/c0_dd0f_wait_for_frame_pump_idle.asm` | Waits while `$0028` is active and keeps the standard renderer/entity/queue/input frame pump alive. |
| `src/c0/c0_dd2c_wait_frame_pump_count_a.asm` | Counted version of the same transition frame pump. |
| `src/c0/c0_dd53_set_teleport_state_selectors.asm` | Installs PSI teleport selector bytes into `$9F3F/$9F41`. |
| `src/c0/c0_de16_freeze_teleport_transition_objects.asm` | Marks transition object slots `$18..$1D` through `$0F12` cadence and `$1002` flag `#$0800`. |
| `src/c0/c0_de46_initialize_teleport_transition_objects_and_vectors.asm` | Seeds beta/arc state in `$9F61..$9F69` and snapshots player position. |
| `src/c0/c0_de7c_unfreeze_teleport_transition_objects.asm` | Clears transition flags for slots `$18..$1D` and resets metadata offset `+$37`. |
| `src/c0/c0_ded9_probe_teleport_two_point_footprint_collision.asm` | ORs two C0:5F33 footprint probes unless teleport state `$9F43` is already terminal. |
| `src/c0/c0_df22_update_teleport_direction_vector_state.asm` | Advances `$9F45/$9F47` and derives signed vector components in `$9F49/$9F4B/$9F4D/$9F4F`. |
| `src/c0/c0_e196_snapshot_teleport_player_state_to_ring.asm` | Writes 12-byte snapshots into the `$5156` ring using cursor `$987D`. |
| `src/c0/c0_e254_update_teleport_transition_object_cadence.asm` | Stores `max(1, #$000C - $9F47)` into `$0F12` for transition object slots. |
| `src/c0/c0_ea3e_suppress_interactions_for_teleport_slots.asm` | ORs `#$C000` into `$10B6` for slots `0..$16` at teleport entry. |
| `src/c0/c0_ea68_ensure_teleport_slot_interaction_suppression.asm` | Maintains `$10B6` high-bit suppression while the teleport mainloop pumps frames. |
| `src/c0/c0_ea99_teleport_mainloop_state_machine.asm` | Dispatches by `$9F41`, waits for `$9F43` success/failure, and restores normal overworld callbacks. |

## Evidence Inputs

- `notes/teleport-freeze-vector-frontier-c0dd0f-c0e196.md`
- `notes/teleport-mainloop-state-machines-c0e214-c0ebdf.md`
- `notes/position-snapshot-and-movement-tick-c0449b-c05200.md`
- `notes/collision-surface-probes-c052d4-c05e3a.md`
- `notes/c0-interaction-runtime-polish.md`

## Runtime State Contract

This slice uses the reference-backed PSI teleport state block:

- `$9F3F`: teleport destination/state selector
- `$9F41`: teleport style selector
- `$9F43`: active state (`0` running, `1` success, `2` failure)
- `$9F45/$9F47`: fixed-point speed/phase
- `$9F49/$9F4B` and `$9F4D/$9F4F`: signed X/Y vector components
- `$9F61..$9F69`: beta/arc seed and steering fields

The transition object set is slots `$18..$1D`. The teleport interaction
suppression sweep covers ordinary slots `0..$16` through `$10B6 | #$C000`.

## Promotion Boundary

This slice promotes comments and local runtime wording only. It does not
decode the full straight/curved movement callbacks, rename all PSI teleport
state fields globally, or claim final meanings for every `$9F41` style value.
The open labels remain:

- dedicated polish pass for C0:E28F, C0:E516, C0:E674, and C0:E776 callbacks
- exact style names for `$9F41` beyond the reference alpha/beta-style grouping
- final role names for transition object slots `$18..$1D`
- caller-side boundary between battle/scripted transition entry and C0:EA99

## Validation

Run after source-comment edits:

```powershell
python tools\validate_source_bank_byte_equivalence.py --bank C0 --module all --combined --scaffold src\c0\bank_c0_helpers_asar.asm --strict
```
