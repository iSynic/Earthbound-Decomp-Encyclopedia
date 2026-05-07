# Class2 PSI Flash Common Local Flow

This note captures the current local behavior model for the Flash-family action wrappers `C2:9987`, `99AE`, `99EF`, and `9A35`.

See also `notes/class2-d57b68-early-entry-name-crosswalk.md`.
See also `notes/class2-psi-action-wrapper-local-verification.md`.
See also `notes/class2-state-machine-99xx.md`.
See also `notes/class2-battler-affliction-crosswalk.md`.
See also `notes/class2-affliction-apply-helper-724a.md`.

## Working Names

- `C2:7550` = `StartSelectedBattlerCollapseAfflictionPath`
- `C2:98A1` = `GateSelectedBattlerForRandomStatusAction`
- `C2:98DE` = `TryApplyStrangeStatusToSelectedBattler`
- `C2:9917` = `TryApplyNumbStatusToSelectedBattler`
- `C2:9950` = `TryApplyCryingStatusToSelectedBattler`
- `C2:9987` = `RunPsiFlashAlphaAction`
- `C2:99AE` = `RunPsiFlashBetaAction`
- `C2:99EF` = `RunPsiFlashGammaAction`
- `C2:9A35` = `RunPsiFlashOmegaAction`

## Main result

The Flash family is no longer just "the complicated PSI quartet."

The current safest local model is:

- `C2:9987`, `99AE`, `99EF`, and `9A35` are the four tier wrappers for the early `PSI_FLASH_*` action slots
- all four share the same two front gates:
  - `C2:7CFD` as the front-door blocker
  - `C2:98A1` as the second-stage gate on selected-row state
- if both gates pass, each tier samples `C0:8E9A & 7` and branches into a small status or collapse ladder
- the ladder is built from four concrete local outcomes:
  - `C2:7550` = collapse or unconscious-style startup path
  - `C2:9917` = numbness application attempt
  - `C2:98DE` = strange-status application attempt
  - `C2:9950` = crying-status application attempt
- all four tiers finish through the shared tail `C2:94CE`

That is a much stronger local statement than the earlier "Flash still looks complex" wording.

## Shared gating

All four wrappers begin the same way:

1. `JSR C2:7CFD`
2. if nonzero, return immediately
3. `JSR C2:98A1`
4. if zero, return immediately
5. sample `JSL C0:8E9A`, mask with `AND #$0007`
6. branch by the resulting `0..7` value
7. finish through `JSR C2:94CE`

So the tier difference is not in the front half of the helper. It is entirely in how many random outcomes collapse into each status branch.

## The shared outcome helpers

### `C2:98DE`

This helper runs:

- `Y = 1`, `X = 3`
- `JSR C2:724A`
- on success: dispatch `EF:6C3A`
- on failure: dispatch `EF:766E`

The helper body at `724A` now shows that this writes value `1` into selected-row byte `+0x20`. The reference script text at `EF:6C3A` is:

- `@{target} felt a little strange...`

So `C2:98DE` is the local strange-status application attempt.

### `C2:9917`

This helper runs:

- `Y = 3`, `X = 0`
- `JSR C2:724A`
- on success: dispatch `EF:6AE0`
- on failure: dispatch `EF:766E`

The helper body at `724A` now shows that this writes value `3` into the primary ailment byte at `+0x1D`. The reference script text at `EF:6AE0` is:

- `@{target}'s body became numb!`

So `C2:9917` is the local numbness application attempt.

### `C2:9950`

This helper runs:

- `Y = 2`, `X = 2`
- `JSR C2:724A`
- on success: dispatch `EF:6BBB`
- on failure: dispatch `EF:766E`

The helper body at `724A` now shows that this writes value `2` into selected-row byte `+0x1F`. The reference script text at `EF:6BBB` is:

- `@{target} could not stop crying!`

So `C2:9950` is the local crying-status application attempt.

### `C2:7550`

This branch is the same broader startup path already documented in the `class2` state-family notes.

The current safest local fit is:

- selected-row collapse or unconscious-style startup
- not a generic active-transition helper

That makes it the strongest current Flash-family local fit for the hardest outcome in the branch ladder.

## Tier-by-tier random branch map

### `C2:9987` -> strongest reference-backed fit for `PSI_FLASH_ALPHA`

Branch map from `C0:8E9A & 7`:

- `0` -> `C2:98DE` = strange attempt
- `1..7` -> `C2:9950` = crying attempt

So Alpha is currently the simplest local ladder: one strange branch and otherwise crying.

### `C2:99AE` -> strongest reference-backed fit for `PSI_FLASH_BETA`

Branch map:

- `0` -> `C2:7550` = collapse or unconscious-style startup
- `1` -> `C2:9917` = numbness attempt
- `2` -> `C2:98DE` = strange attempt
- `3..7` -> `C2:9950` = crying attempt

### `C2:99EF` -> strongest reference-backed fit for `PSI_FLASH_GAMMA`

Branch map:

- `0..1` -> `C2:7550` = collapse or unconscious-style startup
- `2` -> `C2:9917` = numbness attempt
- `3` -> `C2:98DE` = strange attempt
- `4..7` -> `C2:9950` = crying attempt

### `C2:9A35` -> strongest reference-backed fit for `PSI_FLASH_OMEGA`

Branch map:

- `0..2` -> `C2:7550` = collapse or unconscious-style startup
- `3` -> `C2:9917` = numbness attempt
- `4` -> `C2:98DE` = strange attempt
- `5..7` -> `C2:9950` = crying attempt

## What `C2:98A1` is doing here

`C2:98A1` now reads cleanly as a shared precondition gate for this family.

Current safest local summary:

- it first gates through `C2:941D`
- if that blocks, it returns `0`
- otherwise it tests selected-row byte `+0x39` through `C2:6BB8` /
  `RollActionChanceGate`
- if that passes, it returns `1`
- otherwise it dispatches the default failure text `EF:766E` and returns `0`

So Flash does not directly jump into its random ladder. It first asks whether the selected row currently admits this family at all.

## Why this fits Flash unusually well

The action-table crosswalk already gave the reference-backed family names:

- `0x001A` -> Flash Alpha -> `C2:9987`
- `0x001B` -> Flash Beta -> `C2:99AE`
- `0x001C` -> Flash Gamma -> `C2:99EF`
- `0x001D` -> Flash Omega -> `C2:9A35`

The local branch ladder now matches the gameplay flavor of that family unusually well:

- weaker tiers skew toward crying and strange
- higher tiers increasingly add numbness and collapse-style outcomes

This is still phrased as a local behavior map plus a reference-backed family-name promotion, not as a full one-to-one proof of every gameplay label. But it is much stronger than the earlier "complex wrapper" description.

## Current safest takeaway

The safest takeaway is:

- the Flash quartet is a real local random status ladder, not just an unresolved wrapper family
- `C2:9987`, `99AE`, `99EF`, and `9A35` are best treated as the local `PSI_FLASH_ALPHA/BETA/GAMMA/OMEGA` action wrappers, with the final names still carried as reference-backed promotions
- the four concrete outcome helpers are now pinned locally as collapse-style startup, numbness, strange, and crying branches
- the tier difference is expressed by how many random results route into each outcome, not by different front-end gating logic

## Best next target

The best next move is to tighten the `C2:724A` parameter pair meanings behind the `strange / numbness / crying` branches, or to revisit `C2:7550` from the Flash side and decide whether the strongest user-facing wording should now be `collapse`, `faint`, `unconscious`, or something slightly broader.
