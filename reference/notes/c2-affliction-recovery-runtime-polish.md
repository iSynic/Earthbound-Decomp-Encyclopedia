# C2 Affliction Recovery Runtime Polish

This note records the byte-neutral C2 affliction-recovery polish slice. It
promotes the selected-row recovery ladder rooted at `C2:9AEA` and the poison-only
item-side helper at `C2:A39D`.

Primary source modules:

- `src/c2/c2_9aea_try_recover_selected_battler_narrow_affliction.asm`
- `src/c2/c2_9b7a_try_recover_selected_battler_curative_afflictions.asm`
- `src/c2/c2_9c2c_try_recover_selected_battler_broad_afflictions.asm`
- `src/c2/c2_9cb8_try_recover_selected_battler_hard_state.asm`
- `src/c2/c2_a39d_try_recover_selected_battler_poison_only.asm`

Related evidence notes:

- `notes/battle-affliction-recovery-family-c29aea-a39d.md`
- `notes/battle-action-stat-change-family-c2b2e0-b5d7.md`
- `notes/class2-battler-affliction-crosswalk.md`
- `notes/class2-post-selection-controller-phases.md`

## Recovery Ladder

The ladder operates on the active selected row pointer `$A972`.

`C2:9AEA` is the narrow helper:

| Field/value | Action |
| --- | --- |
| `+0x1D == 7` | clear cold/sniffling state, emit `EF:6EBC` |
| `+0x1D == 6` | clear sunstroke state, emit `EF:6F38` |
| `+0x1F == 1` | clear asleep state, emit `EF:6F54` |
| none | emit no-visible-effect text `EF:7696` |

`C2:9B7A` widens the handled set, then falls back to `C2:9AEA`:

| Field/value | Action |
| --- | --- |
| `+0x1D == 5` | clear poison, emit `EF:6E97` |
| `+0x1D == 4` | clear nausea/sickness state, emit `EF:6E81` |
| `+0x1F == 2` | clear crying state, emit `EF:6ED1` |
| `+0x20 == 1` | clear strange/confused-style state, emit `EF:6F1E` |

`C2:9C2C` widens the set again, then falls back to `C2:9B7A`:

| Field/value | Action |
| --- | --- |
| `+0x1D == 3` | clear numb/paralysis state, emit `EF:6E67` |
| `+0x1D == 2` | clear diamondized/body-state value, emit `EF:6E4A` |
| `+0x1D == 1` | hard recovery branch through mask phase and `C2:7397`, or `EF:6F8E` |

`C2:9CB8` is the top wrapper. If `+0x1D == 1`, it calls the heavy recovery/reset
helper `C2:7397` with row word `+0x15`; otherwise it falls back to `C2:9C2C`.
That heavy recovery helper now names its color-wave presentation joins as
`SetEnemySpriteColorWaveDuration` and `EnemySpriteColorWaveComparisonHelper`,
matching the late selected-row visual refresh contract.

## Poison-Only Helper

`C2:A39D` is a narrow item-side helper. It only checks `+0x1D == 5`; on match it
clears poison and emits `EF:6E97`. Otherwise it returns silently.

Source-promotion status: `src/c2/c2_a39d_try_recover_selected_battler_poison_only.asm`
now names the selected-row primary affliction byte, poison value, clear value,
poison-removed text script, EF text bank, and `C1:DC1C` direct-text dispatch.

## Promoted Main Affliction Map

Within this recovery family, row byte `+0x1D` is now strong enough to document as
the main ailment byte:

| Value | Current role |
| --- | --- |
| `1` | hard/unconscious recovery path |
| `2` | diamondized/body-state recovery |
| `3` | numb/paralysis recovery |
| `4` | nausea/sickness recovery |
| `5` | poison recovery |
| `6` | sunstroke recovery |
| `7` | cold/sniffling recovery |

The source comments keep this map scoped to the recovery family. Other selected
row readers may still need their own pass before the enum is promoted globally.

## Timed Substate Neighbor

The same source module also contains the timed-substate helpers. The comments now
record their shared shape:

- row `+0x23` = active timed substate id
- row `+0x25` = bounded refresh counter
- return value from the common helper chooses installed versus strengthened EF
  text

Those helpers now keep the shield gameplay mapping local:

- row `+0x23 == 4`: shield, `EF:6F9A` installed / `EF:6FBD` strengthened
- row `+0x23 == 3`: power shield, `EF:6FD3` installed / `EF:6FF4`
  strengthened
- row `+0x23 == 2`: psychic shield, `EF:700C` installed / `EF:7032`
  strengthened
- row `+0x23 == 1`: psychic power shield, `EF:7050` installed /
  `EF:707A` strengthened

Source follow-up: `C2:B6EB` now calls the same `C2:9CDC` helper by
`ApplyTimedSubstateOrRefreshShieldCounter` when enemy-data byte `+0x59` seeds
initial shield/timed-substate values for newly initialized enemy battler rows.

## Decomp Value

This slice turns the curative action family into a concrete selected-row state
contract:

- the broad recovery ladder is explicit in source comments
- the `+0x1D` values have locally anchored recovery texts
- `C2:B2E0` selector tails now land on documented curative helpers
- the poison-only item helper is separated from the wider Healing-style ladder

## Remaining Soft Spots

- final action-table names for the four ladder entries as Healing alpha/beta/
  gamma/omega remain reference-backed until the whole `D5:7B68` row crosswalk is
  promoted
- global enum promotion for `+0x1D` should wait until non-curative readers are
  checked against the same value map
