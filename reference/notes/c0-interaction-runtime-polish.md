# C0 Interaction Runtime Polish

Status: first C0 interaction runtime polish slice.

This note records the byte-neutral source comments added after
`notes/c0-entity-visual-runtime-polish.md`. The slice joins input-to-facing
helpers, single-facing interaction probes, facing-rotation resolver policy, and
door fallback result states.

## Source Modules Touched

| Source module | Runtime contract pinned |
| --- | --- |
| `src/c0/c0_402b_install_animation_script_from_caller_pointer.asm` | Copies caller-frame pointer state into the C0:83E3 stream installer contract. |
| `src/c0/c0_4049_clear_animation_script_countdown.asm` | Clears `$0081`, the countdown set by the C0:83E3 animation/script stream installer. |
| `src/c0/c0_404f_map_input_to_direction.asm` | Maps `$0065` input nibble through `C3:E12C` permission masks unless `$5D9A` suppresses movement input. |
| `src/c0/c0_4116_probe_interactable_in_facing_direction.asm` | Single-facing probe for the `41E3 -> 4279` path; writes result code to `$5D62` and raw slot to `$5D64`. |
| `src/c0/c0_41e3_probe_interactable_along_facing.asm` | Facing-rotation policy over C0:4116, restoring `$987F` on failure. |
| `src/c0/c0_4279_resolve_interactable_along_facing_target.asm` | Public resolver for the `41E3 -> 4116` path, including `$2AF6[active slot]` facing-cache refresh. |
| `src/c0/c0_42ef_probe_front_interaction_facing.asm` | Core front-facing interaction probe for the `43BC -> 4452` path. |
| `src/c0/c0_43bc_resolve_interaction_facing_rotation.asm` | Facing-rotation policy over C0:42EF, restoring `$987F` on failure. |
| `src/c0/c0_4452_resolve_front_interaction_target.asm` | Public front-interaction resolver used by bank C1. |
| `src/c0/c0_65c2_probe_type6_door_candidate.asm` | Type-6 movement-trigger fallback; caches CF destination pointer and signals `$5D62 = #$FFFE`. |

## Evidence Inputs

- `notes/input-direction-and-interaction-probes-c0402b-c04116.md`
- `notes/front-interaction-flow.md`
- `notes/movement-trigger-lookup-7477.md`
- `notes/position-snapshot-and-movement-tick-c0449b-c05200.md`
- `notes/collision-surface-probes-c052d4-c05e3a.md`

## Runtime Result Contract

The interaction probe paths share the `$5D62/$5D64` result-state family:

- `$5D62 = 0` or `#$FFFF`: no usable ordinary interaction target
- `$5D62 = #$FFFE`: use cached fallback destination state
- other `$5D62` values: mapped target/result code from `$2C9A[slot]`
- `$5D64`: raw overlapped slot id when a live entity/slot probe succeeds

The sibling fallbacks differ:

- C0:4116 calls C4:334A, which probes door destinations ahead of the party.
- C0:42EF calls C0:65C2, which accepts movement-trigger type `#$06`.

## Promotion Boundary

This slice promotes comments and local runtime wording only. It does not rename
WRAM fields globally, change bank C1 consumers, or collapse the two sibling
probe paths into one name. The open labels remain:

- higher-level C1 call-site intent for C0:4279 versus C0:4452
- final vocabulary for `$5D62 = #$FFFE` fallback handling at the script/menu layer
- exact human-facing difference between the C4:334A and C0:65C2 fallback cases
- final names for the C0:83E3 animation/script stream state family

## Validation

Run after source-comment edits:

```powershell
python tools\validate_source_bank_byte_equivalence.py --bank C0 --module all --combined --scaffold src\c0\bank_c0_helpers_asar.asm --strict
```
