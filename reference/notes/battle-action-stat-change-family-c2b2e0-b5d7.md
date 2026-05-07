# Battle Action Stat-Change Family `C2:B2E0..B5E3`

This note captures the current best local model for the battle-action consequence family centered on `C2:B2E0`.

See also [class2-battle-text-cluster-overview.md](notes/class2-battle-text-cluster-overview.md).
See also [battle-text-entry-family-c1dc1c-dd7c.md](notes/battle-text-entry-family-c1dc1c-dd7c.md).
See also [class2-post-selection-controller-phases.md](notes/class2-post-selection-controller-phases.md).
See also [equipped-item-derived-cache-family-c21857-c21e03.md](notes/equipped-item-derived-cache-family-c21857-c21e03.md).
See also [battle-affliction-recovery-family-c29aea-a39d.md](notes/battle-affliction-recovery-family-c29aea-a39d.md).

## Working Names

- `C2:B2E0` = `DispatchBattleStatChangeConsequence`
- `C2:B342` = `ApplyBattleHpRecoveryConsequence`
- `C2:B360` = `ApplyBattlePpRecoveryConsequence`
- `C2:B3D8` = `ApplyBattleIqIncreaseConsequence`
- `C2:B43F` = `ApplyBattleGutsIncreaseConsequence`
- `C2:B4A6` = `ApplyBattleSpeedIncreaseConsequence`
- `C2:B50D` = `ApplyBattleVitalityIncreaseConsequence`
- `C2:B573` = `ApplyBattleLuckIncreaseConsequence`

## Main result

`C2:B2E0` is a real battle-side consequence dispatcher, not a generic helper strip.

The current safest split is:

- selectors `0` and `1`
  - reuse the older bounded feedback helpers `C2:7294` and `C2:7318`
- selector `2`
  - chains those same two helpers in sequence
- selector `3`
  - randomly chooses one of the later one-byte stat-up leaves
- selectors `4..8`
  - are the clean direct late-stat-up leaves for IQ, guts, speed, vitality, and luck
- selectors `9` and `0x0A`
  - tail off into separate battle consequence helpers at `C2:9AEA` and `C2:A39D`

So the family is best read as a mixed battle stat-change and battle-consequence dispatcher, with the `4..8` block now especially well anchored.

## Entry shape

At `C2:B2E0`:

- incoming `A` is copied into `Y` and saved at `$16`
- incoming pointer `$06/$08` is copied to `$0A/$0C`
- the first byte at `[$0A]` is read as a selector
- that selector dispatches to cases `0..0x0A`

The current case map is:

- `0 -> C2:B342`
- `1 -> C2:B360`
- `2 -> C2:B378`
- `3 -> C2:B3AA`
- `4 -> C2:B3D8`
- `5 -> C2:B43F`
- `6 -> C2:B4A6`
- `7 -> C2:B50D`
- `8 -> C2:B573`
- `9 -> C2:B5D9 -> C2:9AEA`
- `0x0A -> C2:B5DF -> C2:A39D`
- otherwise -> `C2:B5E3`

The epilogue at `C2:B5E3` restores the caller pointer from `$18/$1A`, optionally reads a trailing control byte at offset `+3`, and if that byte is nonzero dispatches through `C0:76C8` using the same small `(n * 6)` scaling pattern seen elsewhere in battle-side helper families.

## Selectors `0` and `1`: reused bounded feedback helpers

`C2:B342` and `C2:B360` are not unique one-off battle leaves. They are thin wrappers over the older helper pair already documented in [class2-post-selection-controller-phases.md](notes/class2-post-selection-controller-phases.md).

### Selector `0 -> C2:B342`

This case:

- derives an `X` input from the incoming amount in `Y`
  - `Y == 0` uses fixed script base `#$7530`
  - otherwise it maps `Y` through `C2:6AFD` after the local `n * 6` scaling
- then loads active row pointer `$A972`
- then calls `C2:7294`

The reused `7294` helper is already locally strong as a bounded positive feedback helper:

- overflow or cap case -> `EF:69A1`
  - `@{target}'s HP are maxed out!`
- success case -> `EF:69BA` through `C1:DC66`
  - `@{target} recovered {delta} HP!`
- special blocked row case -> `EF:7696`
  - `@It had no visible effect on {target}!`

So selector `0` is best treated as the battle-side HP-recovery or bounded positive-change wrapper around `C2:7294`, not as a newly separate subsystem.

### Selector `1 -> C2:B360`

This case is the direct sibling:

- `Y == 0` again uses fixed base `#$7530`
- otherwise it maps `Y` through `C2:6AFD`
- then it calls `C2:7318` on active row `$A972`

The reused `7318` helper is already locally strong as the sibling bounded feedback helper using row words `+0x19/+0x1B`, and its battle text is pinned:

- success case -> `EF:69D2` through `C1:DC66`
  - `@{target} recovered {delta} PP!`

So selector `1` is best treated as the battle-side PP-recovery or bounded sibling wrapper around `C2:7318`.

## Selector `2`: chained positive then sibling helper

`C2:B378` simply composes the two older helpers.

It:

- derives the first `X` input from the incoming `Y` amount the same way selector `0` does
- calls `C2:7294`
- then reloads the original amount from `$16`
- derives the second `X` input the same way selector `1` does
- then calls `C2:7318`

So selector `2` is best treated as the combined or paired `7294 + 7318` wrapper.

The safest current summary is:

- selector `2` applies the bounded positive HP-side helper first
- then applies the sibling PP-side helper
- it should stay behavior-described for now rather than overnamed beyond that

## Selector `3`: random late-stat boost chooser

`C2:B3AA` is the first cleanly battle-specific selector in this family.

It:

- loads `A = #4`
- calls `C2:6A2D`
- then uses the returned `0..4` result to choose one of the later direct leaves

Current local map:

- `0 -> C2:B3D8` = IQ up
- `1 -> C2:B43F` = guts up
- `2 -> C2:B4A6` = speed up
- `3 -> C2:B50D` = vitality up
- `4 -> C2:B573` = luck up
- anything else -> `C2:B5E3`

So selector `3` is best treated as a random late-stat-up chooser over the `IQ/guts/speed/vitality/luck` set.

## Selectors `4..8`: direct late-stat-up leaves

The `4..8` block is the strongest part of this family.

All five leaves share the same shape:

- add incoming amount `Y` into one row-local one-byte field on the active row at `$A972`
- mirror the same amount into one byte of the live `0x5F`-stride slot family via `C0:8FF7`
- run the matching bank-`C2` derived-stat refresh helper
- stage a fixed `C8:F7xx/F8xx` battle-text pointer
- pass the amount through `C1:DC66`

### Selector `4 -> C2:B3D8`

This leaf:

- updates row byte `+0x31`
- updates slot byte `$9A28`
- calls `C2:1D7D`
- dispatches text `C8:F7B8`

Pinned battle text from `data_43.ccs`:

- `@{target}'s IQ went up by {delta}!`

Strongest current read:

- selector `4` = IQ up

### Selector `5 -> C2:B43F`

This leaf:

- updates row byte `+0x2C`
- updates slot byte `$9A26`
- calls `C2:1BA4`
- dispatches text `C8:F7D2`

Pinned battle text:

- `@{target}'s guts went up by {delta}!`

Strongest current read:

- selector `5` = guts up

### Selector `6 -> C2:B4A6`

This leaf:

- updates row byte `+0x2A`
- updates slot byte `$9A25`
- calls `C2:1AEB`
- dispatches text `C8:F82F`

Pinned battle text:

- `@{target}'s speed went up by {delta}!`

Strongest current read:

- selector `6` = speed up

### Selector `7 -> C2:B50D`

This leaf:

- updates row byte `+0x30`
- updates slot byte `$9A27`
- calls `C2:1D65`
- dispatches text `C8:F84C`

Pinned battle text:

- `@{target}'s vitality went up by {delta}!`

Strongest current read:

- selector `7` = vitality up

### Selector `8 -> C2:B573`

This leaf:

- updates row byte `+0x2E`
- updates slot byte `$9A29`
- calls `C2:1C5D`
- dispatches text `C8:F86B`

Pinned battle text:

- `@{target}'s luck went up by {delta}!`

Strongest current read:

- selector `8` = luck up

## Relation to the equipped-item derived family

The direct leaves are not isolated battle-only side effects.

Their slot-byte and refresh-helper pairings line up exactly with the already-mapped bank-`C2` stat refresh family:

- `$9A25 -> C2:1AEB -> $99E5` = speed
- `$9A26 -> C2:1BA4 -> $99E6` = guts
- `$9A27 -> C2:1D65 -> $99E8` = vitality
- `$9A28 -> C2:1D7D -> $99E9` = IQ
- `$9A29 -> C2:1C5D -> $99E7` = luck

So the battle consequence leaves are now one of the strongest local bridges between battle-side row logic and the live slot-family stat refresh layer.

## Selectors `9` and `0x0A`

The last two in-range selectors now read more clearly than before.

- `9 -> C2:9AEA`
  - enters the narrow end of the battle affliction-recovery ladder documented in [battle-affliction-recovery-family-c29aea-a39d.md](notes/battle-affliction-recovery-family-c29aea-a39d.md)
  - strongest current local fit: cold, sunstroke, and asleep-style recovery tail
- `0x0A -> C2:A39D`
  - enters the narrow poison-only item-side cure helper in that same note

So these two selectors are still tail helpers, but they are no longer anonymous tails.

## Current safest interpretation

The safest current interpretation is:

- `C2:B2E0` is a mixed battle consequence dispatcher keyed by the first byte of a caller-supplied record or script fragment
- selectors `0..2` reuse the older bounded positive/sibling feedback helpers `7294/7318`
- selector `3` randomly chooses one of the late direct stat-up leaves
- selectors `4..8` are firmly pinned as direct IQ, guts, speed, vitality, and luck increase leaves
- selector `9` is the narrow affliction-recovery tail and selector `0x0A` is the poison-only item-side cure tail

That is already a useful subsystem map even though the front half is still a little more generic than the late stat-up side.

## Confidence

- `C2:B2E0` as a real battle consequence dispatcher: high confidence
- selector source as first byte at `[$0A]`: high confidence
- selectors `0..2` as reused `7294/7318` helper wrappers: high confidence
- selector `0` as HP-recovery or bounded positive helper wrapper: moderate-to-high confidence
- selector `1` as PP-recovery or bounded sibling helper wrapper: moderate-to-high confidence
- selector `2` as chained `7294 + 7318`: high confidence
- selector `3` as random late-stat-up chooser: high confidence
- selectors `4..8` as direct IQ/guts/speed/vitality/luck up leaves: high confidence
- selector `9` as the narrow affliction-recovery tail and selector `0x0A` as the poison-only item-side cure tail: moderate-to-high confidence

## What is still open

- whether selector `0` and `1` deserve tighter final names than the current behavior-first wording
- whether selector `2` corresponds to one specific gameplay action family rather than just the paired helper composition
- whether selector `9` should eventually be promoted from generic affliction-recovery wording to a specific final curative action name like a Healing-tier entry
- whether selector `0x0A` is best kept as poison-only item-side cure wording or tied to one specific remedy action
- the exact meaning of the optional trailing control byte consumed by the common epilogue at `C2:B5E3`
