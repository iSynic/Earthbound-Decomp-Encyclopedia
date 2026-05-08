# Class2 Affliction Apply Helper `C2:724A`

This note captures the current local model for `C2:724A`, the helper reused by the Flash-family status branches and several other battle-side callers.

See also `notes/class2-battler-affliction-crosswalk.md`.
See also `notes/class2-psi-flash-common-local-flow.md`.
See also `notes/class2-state-machine-99xx.md`.
See also [class2-solidification-item-action-c2a5ec-a630.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-solidification-item-action-c2a5ec-a630.md).

## Main result

`C2:724A` is not best read as a generic random-success helper.

The current safest local model is:

- input `A` = target row base
- input `X` = affliction-group offset relative to row byte `+0x1D`
- input `Y` = new affliction value to apply inside that group
- if target row byte `+0x0F` is nonzero, fail immediately
- otherwise inspect byte `target + 0x1D + X`
- if that byte is zero, write the new `Y` value and succeed
- if that byte is nonzero but smaller than `Y`, overwrite it with `Y` and succeed
- if that byte is nonzero and greater than or equal to `Y`, fail

So `724A` is a grouped affliction install-or-upgrade helper.

## Local body shape

The key local steps are:

1. save incoming `X` to local `$02`
2. move incoming row base `A` into `X` and local `$0E`
3. test target row byte `+0x0F`
4. if nonzero, return `0`
5. compute `target + 0x1D + incoming_X`
6. read the current byte from that location
7. if current is nonzero and `current >= Y`, return `0`
8. otherwise write `Y` back to that same byte and return `1`

That means the helper is deciding whether a new status can replace the existing value in one affliction subgroup byte.

## Why this matters

This finally gives the `X/Y` parameter pairs real local meaning.

### Flash-family callers

From the Flash ladder:

- `C2:98DE` uses `Y = 1`, `X = 3`
  - applies value `1` to row byte `+0x20`
  - success text `EF:6C3A` = `@{target} felt a little strange...`
- `C2:9917` uses `Y = 3`, `X = 0`
  - applies value `3` to row byte `+0x1D`
  - success text `EF:6AE0` = `@{target}'s body became numb!`
- `C2:9950` uses `Y = 2`, `X = 2`
  - applies value `2` to row byte `+0x1F`
  - success text `EF:6BBB` = `@{target} could not stop crying!`

### Additional non-Flash callers

Several non-Flash callers now give more concrete value assignments too:

#### Primary byte `+0x1D`

- `C2:89FD` uses `Y = 2`, `X = 0`
  - success text `EF:6AC7` = `@{target} was diamondized!`
- `C2:91BF` uses `Y = 2`, `X = 0`
  - duplicate diamondized-grade writer in a different wrapper family
- `C2:8AC3` uses `Y = 3`, `X = 0`
  - same primary-byte write as `C2:9917`
  - success text `EF:6AE0` confirms local value `3` again as numbness
- `C2:A027` uses `Y = 3`, `X = 0`
  - duplicate numbness-grade writer in another wrapper family
- `C2:8B04` uses `Y = 4`, `X = 0`
  - success text `EF:6AFB` = `@{target} felt somewhat nauseous...`
- `C2:8FD1` uses `Y = 5`, `X = 0`
  - applies value `5` to row byte `+0x1D`
  - success text `EF:6B18` = `@{target} got poisoned!`
- `C2:8B96` uses `Y = 7`, `X = 0`
  - applies value `7` to row byte `+0x1D`
  - success text `EF:6B2F` = `@{target} caught a cold!`

#### Subgroup byte `+0x1E`

- `C2:8BD5` uses `Y = 1`, `X = 1`
  - applies value `1` to row byte `+0x1E`
  - success text `EF:6B81` = `@{target} began to feel strange!`
  - together with the reference `STATUS_1::MUSHROOMIZED = 1` and the dedicated `BTLACT_MUSHROOMIZE` action file, this is now the strongest current fit for mushroomized
- `C2:8C21` uses `Y = 2`, `X = 1`
  - applies value `2` to row byte `+0x1E`
  - success text `EF:6B98` = `@{target} was possessed by a mini-ghost!`
  - together with the reference `STATUS_1::POSSESSED = 2` and the dedicated `BTLACT_POSSESS` action file, this is now the strongest current fit for possessed
  - together with the `X = 1` family shape, this makes `+0x1E` read much more strongly as the `STATUS_1` subgroup byte rather than spare scratch

#### Subgroup byte `+0x1F`

- `C2:ACB2` uses `Y = 1`, `X = 2`
  - applies value `1` to row byte `+0x1F`
  - success text `EF:6C55` = `@{target} fell asleep!`
- `C2:8C90` and `C2:8E13` both use `Y = 2`, `X = 2`
  - both succeed with `EF:6BBB` = `@{target} could not stop crying!`
- `C2:8CC9` uses `Y = 3`, `X = 2`
  - success text `EF:6BD3` = `@{target} suddenly could not move!`
- `C2:8D12`, `C2:962C`, `C2:A630`, and `C2:A843` all use `Y = 4`, `X = 2`
  - all succeed with `EF:6BEF` = `@{target}'s body solidified!`
  - that lines up exactly with the reference `STATUS_2::SOLIDIFIED`
  - `C2:A630` is now especially useful because [class2-solidification-item-action-c2a5ec-a630.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-solidification-item-action-c2a5ec-a630.md) pins it as the concrete status-apply branch inside live item-side action entry `C2:A5EC`

#### Subgroup byte `+0x20`

- `C2:98DE`, `C2:8DD4`, `C2:A07F`, and `C2:ACF3` all use `Y = 1`, `X = 3`
  - all succeed with `EF:6C3A` = `@{target} felt a little strange...`
  - that makes `+0x20 = 1` very strong as the strange-style subgroup value

Those are not just thematic matches. The helper body itself now says these branches are writing into specific subgroup bytes, and the success texts line up cleanly with the reference affliction enums.

## Stronger field map from this helper

This strengthens the current battler-affliction crosswalk:

- `X = 0` targets the primary ailment byte at `+0x1D`
- `X = 1` targets the subgroup byte at `+0x1E`
- `X = 2` targets the subgroup byte at `+0x1F`
- `X = 3` targets the subgroup byte at `+0x20`

Combined with the already-pinned battle-start texts and the newer non-Flash callers, the safest current read is now:

- row `+0x1D` = primary one-byte ailment enum
  - local values `2`, `3`, `4`, `5`, and `7` are now pinned as diamondized, numbness, nausea, poison, and cold
- row `+0x1E` = `STATUS_1` subgroup byte
  - local value `1` is now the strongest current fit for mushroomized
  - local value `2` is now the strongest current fit for possessed
- row `+0x1F` = `STATUS_2`-style subgroup byte used by asleep, crying, mobility, or body-state values
  - local values `1`, `2`, `3`, and `4` are now pinned as asleep, crying, could-not-move, and solidified
- row `+0x20` = `STATUS_3`-style subgroup byte used by strange-style states
  - local value `1` is strongly pinned as strange

This is still slightly cautious as a full global field map, but the subgroup coverage is much better than it was before this pass.

## Current safest takeaway

The safest takeaway is:

- `C2:724A` applies or upgrades a status value inside one affliction subgroup byte
- `X` selects which subgroup byte to touch relative to `+0x1D`
- `Y` is the value written into that subgroup
- the helper succeeds only when the current value is zero or lower-priority than the incoming one
- this no longer just clarifies the Flash family; it now locally confirms primary-byte values for diamondized, numbness, nausea, poison, and cold, plus subgroup values for mushroomized, possessed, asleep, crying, could-not-move, solidified, and strange
- that materially strengthens the battler-affliction field map and the relation between the local row layout and the reference `battler::afflictions` groups

## Best next target

The best next move is to map more `724A` callers so the remaining subgroup values can be named from local behavior, especially the callers that use `X = 1`, `2`, or `3` outside the current battle-heavy clusters.


