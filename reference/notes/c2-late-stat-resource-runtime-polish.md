# C2 Late Stat Resource Runtime Polish

This note records the byte-neutral C2 late stat/resource action polish slice for
`C2:8E42`, `C2:8EAE`, and `C2:8F21`.

Primary source modules:

- `src/c2/c2_8e42_run_pp_reduction_action.asm`
- `src/c2/c2_8eae_run_guts_reduction_action.asm`
- `src/c2/c2_8f21_run_offense_defense_reduction_action.asm`

Related evidence notes:

- `notes/class2-late-stat-and-resource-family-c28e42-c29e38.md`
- `notes/class2-bounded-offense-defense-helpers-c27d28-c27e33.md`
- `notes/c2-offense-defense-stat-actions-runtime-polish.md`
- `notes/c2-action-dispatch-runtime-polish.md`

## PP Reduction

`C2:8E42` is the PP-reduction side of the late numeric-effect cluster.

Promoted runtime contract:

| Contract | Runtime shape |
| --- | --- |
| target row | `$A972` |
| current PP field | row word `+0x19` |
| max PP field | row word `+0x1B` |
| amount source | high nibble of `+0x1B`, rolled through `C2:6A44` / `RollRandomAmount` |
| reducer | `C2:721D` |
| zero-current text | C8:FB05 |
| zero-range/no-effect text | EF:766E |
| success text | EF:7755 with amount payload |

This is stronger than a generic "resource action" label: the byte path explicitly
joins max PP, current PP, capped PP reduction, and the PP-loss message.

## Guts Reduction

`C2:8EAE` is the guts-cutting body. It snapshots row `+0x2C`, reduces that value
to roughly three quarters of its prior value, then clamps against a floor derived
from base guts at row `+0x35`.

The battle text at C8:F7EE reports the positive delta between old guts and final
clamped guts through the C1 amount-bearing path.

## Offense And Defense Reduction

`C2:8F21` is a paired reduction body:

| Pass | Row field | Helper | Text |
| --- | --- | --- | --- |
| offense | `+0x26` | `C2:7DDC` | C8:F885 |
| defense | `+0x28` | `C2:7E33` | C8:F8A2 |

Each pass snapshots the old value, applies the bounded decrease helper, and
reports the positive loss delta.

## Decomp Value

Together with the previous `9E38..9F06` correction, this gives the late numeric
cluster a cleaner runtime map:

- `8E42`: PP target reduction
- `8EAE`: guts reduction
- `8F21`: paired offense/defense reduction
- `9E38/9E7F`: offense-up body/wrapper
- `9E86/9EFF`: defense-down body/wrapper

That is a useful bridge from action-table entries into concrete selected-row
fields and amount-bearing battle text.

## Phase 2 Trace-Oracles

PP reduction should stay the loss-only sibling of PSI Magnet. Phase 2 traces
should compare its max-PP-derived amount roll, current-PP cap, `C2:721D`
reducer, and PP-loss text against PSI Magnet's transfer behavior, without
borrowing recovery wording from the Magnet path.

Current controlled runtime evidence covers the reducer half of this comparison.
The `bash-row-pp-reduction` fixture plus the `resource-target-pp32` runner
profile seeds the selected row with `32/32` PP. The manual capture observes
`C2:8E42 -> C2:721D -> C2:7191`: rolled amount `2`, target PP `32 -> 30`, and no
active-row PP recovery. This is controlled fixture evidence only; natural
PP-bearing target evidence is still required before this lane can become a
proof-grade resource contract.

The generated PSI Magnet versus PP-reduction controlled comparison lives at
`notes/c2-resource-amount-controlled-comparison.md`.

Late numeric reducers need small 16-bit edge tests before the C port relies on
normalized integer widths. Target cases should include zero current values,
small max-resource nibbles, clamp floors for guts, bounded offense/defense
decreases, and amount text deltas near `0`, `1`, and word-boundary values.

Fixed PP recovery is a resource-lane trace candidate from the feedback intake:
document it as a mirror of fixed HP recovery only after the local source path
proves the target row, target resource, clamp behavior, and EF/C1 text payload.

## Remaining Soft Spots

- The final player-facing names for later action-table reuses should wait for a
  row-by-row `D5:7B68` crosswalk pass.
