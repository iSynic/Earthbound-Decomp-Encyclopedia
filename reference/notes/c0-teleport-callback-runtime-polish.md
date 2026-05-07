# C0 Teleport Callback Runtime Polish

Status: second C0 teleport/transition runtime polish slice.

This note records the byte-neutral source comments added after
`notes/c0-teleport-state-runtime-polish.md`. The slice focuses on the movement,
restore, success, exit, and failure callbacks installed by `TELEPORT_MAINLOOP`.

## Source Modules Touched

| Source module | Runtime contract pinned |
| --- | --- |
| `src/c0/c0_e214_advance_teleport_object_snapshot_ring_cursor.asm` | Advances the object metadata `+$3D` cursor for the `$5156` snapshot ring. |
| `src/c0/c0_e28f_tick_teleport_straight_movement_callback.asm` | Straight/alpha callback computes next coordinates, gates collision, snapshots, and sets `$9F43`. |
| `src/c0/c0_e3c1_restore_teleport_object_from_snapshot_ring.asm` | Restore callback for movement phase: reads `$5156` snapshots and advances metadata cursor. |
| `src/c0/c0_e44d_apply_teleport_beta_manual_steering.asm` | Manual beta/curved steering nudges `$9F67/$9F69` from input `$0065`. |
| `src/c0/c0_e48a_seed_teleport_post_success_drift_vector.asm` | Seeds small signed post-success drift components from facing `$987F`. |
| `src/c0/c0_e516_tick_teleport_curved_movement_callback.asm` | Curved/beta callback derives arc targets from `$9F61/$9F63`, gates collision, advances arc fields, and sets `$9F43`. |
| `src/c0/c0_e674_tick_teleport_post_success_drift_callback.asm` | Post-success drift callback updates live coordinates plus `$9F5B/$9F5F` screen state. |
| `src/c0/c0_e6fe_restore_teleport_exit_object_from_snapshot_ring.asm` | Exit restore sibling of C0:E3C1 for the straight exit phase. |
| `src/c0/c0_e776_tick_teleport_straight_exit_callback.asm` | Straight exit callback applies vectors and subtracts scaled phase from recenter Y. |
| `src/c0/c0_e815_setup_teleport_successful_arrival.asm` | Success setup installs C0:E674/C0:E3C1 and copies live vector/screen state into `$9F59..$9F5F`. |
| `src/c0/c0_e897_finalize_teleport_arrival_or_failure.asm` | Finalizer installs C0:E776/C0:E3C1 and pumps frames until `$9F47` decays. |
| `src/c0/c0_e979_teleport_no_op_callback.asm` | No-op active callback paired with failure-hold pose refresh. |
| `src/c0/c0_e97c_refresh_teleport_current_slot_pose.asm` | Failure-hold restore callback recomputes `$2BAA` and refreshes draw state. |
| `src/c0/c0_e9ba_hold_teleport_failure_state.asm` | Failure hold installs C0:E979/C0:E97C and pumps 180 frames. |

## Evidence Inputs

- `notes/teleport-mainloop-state-machines-c0e214-c0ebdf.md`
- `notes/teleport-freeze-vector-frontier-c0dd0f-c0e196.md`
- `notes/c0-teleport-state-runtime-polish.md`
- `notes/position-snapshot-and-movement-tick-c0449b-c05200.md`
- `notes/collision-surface-probes-c052d4-c05e3a.md`

## Callback Contract

The teleport mainloop installs active/restore callback pairs through C4:2F45:

- styles `1` and `5`: active C0:E28F, restore C0:E3C1
- styles `2` and `4`: active C0:E516, restore C0:E3C1
- post-success drift: active C0:E674, restore C0:E3C1
- straight exit: active C0:E776, restore C0:E3C1
- failure hold: active C0:E979, restore C0:E97C

The movement callbacks use `$9F43` as the terminal state latch:

- `0`: still running
- `1`: success
- `2`: failure/collision
- `3`: post-arrival exit phase seeded by the finalizer

## Promotion Boundary

This slice promotes comments and local runtime wording only. It does not name
the exact player-facing teleport styles beyond straight/curved grouping, does
not globally rename the `$9F3F+` block, and does not decode C4:1FFF or C4:2F45.
The open labels remain:

- exact style names for `$9F41` values `1..5`
- final human-facing role for transition slots `$18..$1D`
- C4:1FFF curve/trig helper semantics
- C4:2F45 callback installation contract field layout

## Validation

Run after source-comment edits:

```powershell
python tools\validate_source_bank_byte_equivalence.py --bank C0 --module all --combined --scaffold src\c0\bank_c0_helpers_asar.asm --strict
```
