# C2 Offense Defense Stat Actions Runtime Polish

This note records the byte-neutral C2 stat-action correction and polish slice
around `C2:9E38..9F06`.

Primary source modules:

- `src/c2/c2_9e38_run_defense_spray_action.asm`
- `src/c2/c2_9e7f_run_defense_shower_action.asm`

Related evidence notes:

- `notes/class2-late-stat-and-resource-family-c28e42-c29e38.md`
- `notes/class2-bounded-offense-defense-helpers-c27d28-c27e33.md`
- `notes/class2-d57b68-battle-action-table-match.md`
- `notes/class2-d57b68-early-entry-name-crosswalk.md`

## Correction

The earlier local notes overfit `C2:9E38` and `C2:9E7F` to Defense Spray/Shower
wording. The source bytes show a stronger local result:

| Address | Source shape | Promoted behavior |
| --- | --- | --- |
| `C2:9E38` | row `+0x26`, `C2:7D28`, C8:F77D | bounded offense increase |
| `C2:9E7F` | `JSL C2:9E38` | offense-up wrapper |
| `C2:9E86` | row `+0x28`, `C2:7E33`, C8:F8A2 | gated defense decrease |
| `C2:9EFF` | `JSL C2:9E86` | defense-down wrapper |

The generated filenames and older labels remain in place for stability, but the
source now carries behavior-correct aliases and comments.

## Offense-Up Body

`C2:9E38` gates through the selected-battler default blocker, snapshots row
`+0x26`, calls `C2:7D28`, and prints the resulting positive delta through the
C8:F77D amount-bearing battle text.

That makes it an offense-up body in local runtime terms, not a defense-up body.
`C2:9E7F` is the paired wrapper that simply dispatches to `C2:9E38`.

## Defense-Down Body

`C2:9E86` is the defense-down body. It gates through the same ordinary battle
blocker, passes through the luck/threshold helper, snapshots row `+0x28`, calls
`C2:7E33`, and emits C8:F8A2 with the positive amount lost. On failed gate it
prints the shared no-effect text `EF:766E`.

The unlabeled tail at `C2:9EFF` is now source-labeled as the wrapper over this
defense-down body.

## Decomp Value

This slice is useful because it fixes a misleading action-family bridge:

- `C2:7D28` remains the bounded offense-increase helper.
- `C2:7E33` remains the bounded defense-decrease helper.
- `C2:9E38/9E7F` now point to offense-up behavior.
- `C2:9E86/9EFF` now point to defense-down behavior.

Future action-table naming can still reconcile final player-facing names, but
the runtime field/helper evidence is now recorded in the source and notes.

## Remaining Soft Spots

- Final action-table entry names should be rechecked against the live `D5:7B68`
  row metadata before renaming the generated files.
- The Defense Spray/Shower labels elsewhere in C2 need a separate pass; this
  slice only corrects the `9E38..9F06` runtime cluster.
