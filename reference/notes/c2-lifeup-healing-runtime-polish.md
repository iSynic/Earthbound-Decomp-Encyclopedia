# C2 Lifeup Healing Runtime Polish

This note records the byte-neutral C2 Lifeup/fixed-amount healing polish slice.
It promotes the common fixed-amount HP recovery wrapper at `C2:9AB8` and the
four thin literal wrappers at `C2:9AC6`, `C2:9ACF`, `C2:9AD8`, and `C2:9AE1`.

Primary source module:

- `src/c2/c2_9ab8_run_fixed_amount_healing_common.asm`

Related evidence notes:

- `notes/class2-healing-amount-family-c29ab8-c29ae1.md`
- `notes/class2-d57b68-battle-action-table-match.md`
- `notes/class2-d57b68-early-entry-name-crosswalk.md`
- `notes/c2-selected-row-controller-runtime-polish.md`
- `notes/c2-action-dispatch-runtime-polish.md`

## Common Helper

`C2:9AB8` is the common fixed-amount HP recovery wrapper. It accepts a base
literal in A, passes that literal through `C2:6AFD` /
`ApplyTwentyFivePercentVariance`, then calls the selected-row HP recovery
feedback helper at `C2:7294`.

Runtime contract:

| Step | Runtime shape |
| --- | --- |
| caller input | A = base recovery literal |
| amount shaping | `C2:6AFD` / `ApplyTwentyFivePercentVariance`, returned through X |
| target row | `$A972` selected battler row |
| recovery worker | `C2:7294` with A = row, X = effective amount |
| text behavior | inherited from `C2:7294` maxed/amount/no-effect paths |

This keeps `C2:9AB8` named as a fixed-amount healing common helper rather than a
PSI-only routine. Its consumers include the canonical PSI-side Lifeup ladder and
later item/other action-table reuses.

## Literal Wrappers

The four wrappers are byte-small but semantically important because their
literals line up with the early `D5:7B68` action-table PSI quartet:

| Entry | Wrapper | Literal | Current local role |
| --- | --- | --- | --- |
| `32` | `C2:9AC6` | `0x0064` | Lifeup alpha |
| `33` | `C2:9ACF` | `0x012C` | Lifeup beta |
| `34` | `C2:9AD8` | `0x2710` | Lifeup gamma/full-heal-style recovery |
| `35` | `C2:9AE1` | `0x0190` | Lifeup omega |

The same wrappers are also reused by later non-PSI rows. The safest wording is
therefore that entries `32..35` are the canonical PSI-side Lifeup use of this
family, while the routines themselves remain shared fixed-amount healing leaves.

## Decomp Value

This slice strengthens a useful runtime join:

- `D5:7B68` action descriptors choose the Lifeup/fixed-heal wrappers.
- The wrappers reduce to a literal plus the common `C2:9AB8` helper.
- `C2:9AB8` joins the selected-row domain through `$A972`.
- `C2:7294` owns the actual HP-side row update, clamp, and battle text feedback.

That makes the decomp more useful than a name-only action table: a contributor
can now follow a Lifeup table entry from editor-visible action metadata through
the fixed literal wrapper to the selected-row HP recovery feedback worker.

## Phase 2 Trace-Oracles

Fixed HP recovery is the healing-side sibling of the damage/resource amount
lane. Phase 2 should trace the literal wrapper, `C2:6AFD` amount shaping,
selected row `$A972`, the `C2:7294` HP recovery worker, clamp/maxed behavior,
and amount/no-effect text selection.

The C-port feedback pairs this with fixed PP recovery as a structural mirror,
but this note only locally promotes the HP wrapper family. Fixed PP recovery
should be kept as a trace candidate in resource-lane notes until its C2 source
path is pinned with the same target-resource and text-contract specificity.

## Remaining Soft Spots

- Later item/other reuses of these wrappers should eventually get their own
  action-table row note so the shared helper is not overfit to PSI wording.
- The corridor-only wrapper modules remain source anchors; the decoded combined
  body in `src/c2/c2_9ab8_run_fixed_amount_healing_common.asm` is the source
  location promoted by this slice.
