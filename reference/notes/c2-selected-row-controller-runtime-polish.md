# C2 Selected-Row Controller Runtime Polish

This note records the byte-neutral C2 selected-row controller polish slice. It
promotes the HP/PP feedback pair, the heavy recovery reset helper, and the
collapse/affliction startup entry that sits beside the late controller path.

Primary source modules:

- `src/c2/c2_7294_apply_battler_hp_recovery_feedback.asm`
- `src/c2/c2_7318_apply_battler_pp_recovery_feedback.asm`
- `src/c2/c2_7397_install_battler_heavy_recovery_reset.asm`
- `src/c2/c2_7550_start_selected_battler_collapse_affliction_path.asm`

Related evidence notes:

- `notes/class2-post-selection-controller-phases.md`
- `notes/class2-late-controller-path-77ca.md`
- `notes/battle-action-stat-change-family-c2b2e0-b5d7.md`
- `notes/c2-stat-consequence-runtime-polish.md`
- `notes/c2-affliction-recovery-runtime-polish.md`

## Feedback Helpers

`C2:7294` and `C2:7318` are sibling selected-row feedback helpers. Both accept a
selected-row base in A and a caller-provided amount in X.

`C2:7294` is the HP-side helper:

| Contract | Runtime shape |
| --- | --- |
| row gate | requires `+0x0C == 1` |
| hard-state gate | `+0x1D == 1` emits `EF:7696` |
| bounded pair | row words `+0x13/+0x15` |
| target setter/clamp | `C2:7126` / `SetBattlerHpTarget` |
| cap/no-gain text | `EF:69A1` |
| success text | amount-bearing `EF:69BA` through `C1:DC66` |

`C2:7318` is the PP-side helper:

| Contract | Runtime shape |
| --- | --- |
| row gate | requires `+0x0C == 1` |
| hard-state gate | `+0x1D == 1` returns silently |
| bounded pair | row words `+0x19/+0x1B` |
| target setter/clamp | `C2:7191` / `SetBattlerPpTarget` |
| success text | amount-bearing `EF:69D2` through `C1:DC66` |

The battle consequence dispatcher at `C2:B2E0` reuses these helpers for selector
`0`, selector `1`, and the chained selector `2`. That makes the helpers shared
selected-row infrastructure, not one-off item or PSI leaves.

The battle-start back half now also calls `C2:BCB9` /
`ApplyBattlerPpTargetLoss` by name for the D5:7B68 PP-cost gate, keeping the
PP target-loss edge aligned with the selected-row setter/clamp vocabulary.

## Heavy Recovery Reset

`C2:7397` is the revival-grade reset helper used by curative paths when row
`+0x1D == 1`.

Promoted runtime contract:

- emit `EF:6F7C`
- clear row bytes `+0x1D..+0x23`
- clear row word `+0x04`
- set row byte `+0x0D = 1`
- set/clamp the row's HP-side target through `C2:7126` /
  `SetBattlerHpTarget`
- if row bytes `+0x0E/+0x0F` are both clear, update linked `9A15/9A13` marker
  tables through the id stored at row `+0x10`
- if row `+0x0E == 1` and `+0x0F == 0`, reset row-membership byte `+0x4B`
  across candidate rows, mark the selected row, and run the visual refresh loops
  through `C2:FAD8` / `SetEnemySpriteColorWaveDuration`,
  `C2:FB35` / `EnemySpriteColorWaveComparisonHelper`, and `C2:69BE` /
  `WaitFrames`
- the refresh loop's palette component extraction now calls the shared
  `C0:9251` / `SignedDivide16By8` helper by name, matching the nearby
  color-wave initializer vocabulary

This keeps the helper named around behavior instead of final gameplay wording:
it is wider than "print revived" because it also resets selected-row state,
linked markers, membership flags, and presentation state.

## Collapse/Affliction Startup

`C2:7550` is the startup entry for the heavier selected-row collapse or
affliction controller.

Promoted runtime contract:

- A is the selected-row base
- `$AA92` is cleared on entry
- nonzero row `+0x0E` jumps to the late controller at `C2:77CA`
- startup rows with `+0x1E == 2` scan six upstream source entries
- the startup scan accepts entries with enabled `9FB8`, clear `9FBB`, and
  neighboring metadata `9FCA == 2`
- after the scan, the selected row is seeded with `+0x1D = 1`
- sibling state bytes `+0x1E..+0x23` are cleared
- row `+0x0F == 0` routes to the hardcoded collapse text tail
- nonzero row `+0x0F` routes to the descriptor-backed `D5:9589 + 0x31` text
  pointer path

This strengthens the local model that selected-row `+0x1D == 1` is the
hard/collapsed state for this controller family, while `+0x0E` is the major
startup-vs-late phase discriminator.

## Decomp Value

This slice ties together several previously separate-looking facts:

- HP and PP recovery feedback are reusable selected-row helpers with explicit
  row gates, bounded pairs, clamp helpers, and amount-bearing text scripts.
- The hard-state value installed by `C2:7550` is the same value blocked by
  `C2:7294/7318` and recovered by `C2:7397`.
- `C2:7397` is a reset/install helper with row-state, linked-record, marker, and
  visual-refresh effects.
- `C2:7550` now has a source-commented boundary between startup handling and the
  late `C2:77CA` controller path.
- `C2:7126/7191` are now named as target setter/clamp helpers, while the
  adjacent `C2:71F0/721D` bodies are the subtract-and-floor HP/PP target-loss
  wrappers that delegate to those setters.
- `C2:69BE` is now named as the counted frame wait used by the selected-row
  visual refresh loops.
- `C2:7397` now shares named color-wave duration and per-entry setup helpers
  with the late selected-row collapse visual pass.
- the heavy-recovery visual refresh now names the signed divide helper used for
  RGB555 component extraction before calling the color-wave comparison helper.
- battle-start front/back controller callsites now name the second-stage row
  counter and source-entry promoter that bridge battle-start row selection into
  the collapse/affliction controller state.
- the startup/death-text continuation now names its hardcoded collapse-text tail
  and shared late-controller return join, clarifying where row `+0x0F` routes
  leave the selected-row startup body.

## Remaining Soft Spots

- final gameplay names for row bytes `+0x0D`, `+0x0F`, and `+0x10`
- whether every non-curative reader of row `+0x1D == 1` should be promoted to
  the same global hard/collapsed enum
- final gameplay names for the two-stage color-wave refresh performed after
  heavy recovery
