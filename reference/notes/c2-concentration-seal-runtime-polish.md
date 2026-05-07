# C2 Concentration Seal Runtime Polish

This note records the byte-neutral C2 concentration/PSI-seal polish slice for
the enemy-side body at `C2:8D5A` and its local threshold helper at `C2:8D41`.

Primary source modules:

- `src/c2/c2_8d3a_run_strange_status_wrapper_action.asm`
- `src/c2/c2_8d5a_run_concentration_seal_action.asm`

Related evidence notes:

- `notes/class2-concentration-seal-family-c28d5a-c2a3d1.md`
- `notes/c2-item-bomb-runtime-polish.md`
- `notes/c2-late-status-runtime-polish.md`
- `notes/class2-battler-affliction-crosswalk.md`

## Threshold Helper

`C2:8D41` is the local `SUCCESS_LUCK40` helper. It rolls against a 40-point
threshold, then compares the result with selected-row byte `+0x2E`, which the
broader C2 stat field map uses as luck.

The helper returns `0` for pass and `1` for fail, matching the local callers that
branch to no-effect text when the result is zero.

## Concentration/PSI-Seal Body

`C2:8D5A` is the enemy-side concentration/PSI-seal body.

Promoted runtime contract:

| Contract | Runtime shape |
| --- | --- |
| default target gate | `C2:7CFD` / `CheckSelectedBattlerDefaultTextBlocker` |
| luck gate | `C2:8D41` |
| secondary row gate | row `+0x37` through `C2:6BB8` / `RollActionChanceGate` |
| target byte | row `+0x21` |
| installed value | `4` |
| success text | `EF:6C0B` |
| failure text | `EF:766E` |

This is the enemy-side sibling of the item-side concentration body at `C2:A3D1`.
Both bodies converge on row `+0x21 = 4` and the same `EF:6C0B` text.

## Decomp Value

This completes the source-side picture for the local concentration/seal family:

- `C2:8D5A` is the enemy-side body.
- `C2:A3D1` is the item-side body.
- `C2:8D41` is the shared luck-threshold gate.
- row `+0x21 = 4` remains the strongest local concentration/PSI-seal state.

## Remaining Soft Spots

- The exact semantic name for selected-row byte `+0x37` should wait for the
  broader resistance/immunity pass.
- The generated `C2:8D3A` source unit also contains the strange wrapper; this
  slice only promotes its threshold helper because that helper is shared by the
  concentration/seal bodies.
