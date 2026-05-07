# Class2 State Machine 99xx

This note captures the current ROM-first model for the compact bank `C2` state machine around `99A7` through `9A79`.

## Working Names

- `C2:7CFD` = `CheckSelectedBattlerDefaultTextBlocker`
- `C2:941D` = `CheckSelectedBattlerTimedSubstateBlocker`
- `C2:94CE` = `TickSelectedBattlerTimedSubstateCleanup`
- `C2:98A1` = `GateSelectedBattlerForRandomStatusAction`
- `C2:98DE` = `TryApplyStrangeStatusToSelectedBattler`
- `C2:9917` = `TryApplyNumbStatusToSelectedBattler`
- `C2:9950` = `TryApplyCryingStatusToSelectedBattler`
- `C2:9A80` = `RunPsiStarstormCommon`
- `C2:9AB8` = `RunFixedAmountHealingCommon`

## The `99A7` / `99E8` / `9A2E` / `9A79` cluster is a shared transition controller

These four routines are not random helpers. They are sibling entry points with the same broad skeleton:

- `JSR C2:7CFD`
- if that returns nonzero, skip to the shared tail and return
- `JSR C2:98A1`
- if that returns zero, fall through to the shared tail and return
- sample `JSL C0:8E9A`, mask to a small status nibble with `AND #$0007`
- branch into one of a small set of message or transition helpers
- finish by calling the shared tail at `C2:94CE`

Current best reading:

- this is a compact per-slot transition controller, not a one-off message script
- the four entry points look like nearby variants within the same object family
- the surrounding `99DC+` state bytes are still the best candidate for choosing which variant is active, but they are no longer best treated as a flat generic selector; the newer reader set now makes `1` the strongest blocked or collapsed value, with `1/2` acting as a stronger special-handling pair than the other states

## Helper roles inside the cluster

### `C2:7CFD`

This routine checks current-slot byte `+0F`.

If that byte is nonzero, it shows the default text pointer `EF:766E` and returns `1`. Otherwise it returns `0`.

That makes it a front-door blocker for the family.

### `C2:98A1`

This routine first calls `C2:941D`, then checks current-slot byte `+39`
through `C2:6BB8` / `RollActionChanceGate`.

Current best reading:

- if `C2:941D` says the slot is blocked, return `0`
- otherwise, if the `+39` test passes, return `1`
- otherwise, show the same default text pointer `EF:766E` and return `0`

So this looks like a second-stage gate for whether the transition is currently allowed.

### `C2:98DE`, `C2:9917`, and `C2:9950`

These are no longer just anonymous message wrappers.

Current local map:

- `C2:98DE` = strange-status application attempt
  - `Y = 1`, `X = 3`, then `C2:724A`
  - success text `EF:6C3A` = `@{target} felt a little strange...`
- `C2:9917` = numbness application attempt
  - `Y = 3`, `X = 0`, then `C2:724A`
  - success text `EF:6AE0` = `@{target}'s body became numb!`
- `C2:9950` = crying-status application attempt
  - `Y = 2`, `X = 2`, then `C2:724A`
  - success text `EF:6BBB` = `@{target} could not stop crying!`

All three still fall back to the default failure pointer `EF:766E` on failure.

The helper body at `C2:724A` now sharpens those calls further:

- `X = 0` targets the primary ailment byte at `+0x1D`
- `X = 2` targets subgroup byte `+0x1F`
- `X = 3` targets subgroup byte `+0x20`
- `Y` is the applied status value within that subgroup

That makes the surrounding `99A7..9A79` cluster read much more like a real random status ladder than a generic transition script.

### `C2:94CE`

This is the shared tail for the cluster.

Current best reading:

- it uses `$AA96` as a countdown-active flag
- if active, it decrements current-slot byte `+25`
- when that countdown reaches zero, it clears current-slot byte `+23`
- it then shows text pointer `EF:7099`
- and clears `$AA96`

So `C2:94CE` looks like the family's countdown tick and expiry cleanup path.

### `C2:941D`

This routine is the other key piece.

Current best reading:

- it consults a type value derived from the current slot through the `D5:7B68` table family
- it then checks current-slot byte `+23`
- when `+23` is `1` or `2`, it routes into state-specific text paths at `EF:70D2` or `EF:70FA`
- the `+23 == 2` case is tied to the same countdown byte `+25`

This fits the idea that `+23` is a local timed-state byte and `+25` is its countdown.

## Parameterized transition helpers

Two nearby helper families plug into the same controller logic.

### `C2:9A80`

This helper gates through `C2:941D`, computes a per-slot parameter through
`C2:6AFD` / `ApplyTwentyFivePercentVariance`, runs `C2:8125` /
`ApplyDamageToSelectedTarget`, then falls into `C2:94CE`.

It has two tiny wrappers:

- `C2:9AAA` passes `#$0168`
- `C2:9AB1` passes `#$02D0`

### `C2:9AB8`

This helper is no longer best read as timer- or duration-driven.

It computes a fixed healing amount through `C2:6AFD` / `ApplyTwentyFivePercentVariance`, then hands that amount to `C2:7294`, which now reads much more strongly as an HP recovery worker over battler `hp_target` and `hp_max`.

Its four tiny wrappers are:

- `C2:9AC6` passes `#$0064`
- `C2:9ACF` passes `#$012C`
- `C2:9AD8` passes `#$2710`
- `C2:9AE1` passes `#$0190`

See [class2-healing-amount-family-c29ab8-c29ae1.md](notes/class2-healing-amount-family-c29ab8-c29ae1.md) for the focused pass. The early action-table quartet at entries `32..35` is now the strongest current local fit for the PSI-side `Lifeup` ladder.

## Current best model

See `notes/class2-slot-fields-and-transition-start.md` for the field-level writeup and the selected-row startup helper at `C2:7550`, and `notes/class2-handoff-4477-4703.md` for the derived-action handoff.

The safest current interpretation is:

- `99DC` is still a per-slot state byte for this object family, with `1` now the strongest blocked or collapsed value and `1/2` the strongest party-level special-handling pair
- the `99A7` through `9A79` cluster is a timed transition controller used by that family
- `C2:7550` now reads better as the startup branch that installs one selected battler into a collapse or affliction-handling path for this family
- `C2:4477` derives an action code in slot `+09` and parameter in `+0A`
- `C2:4703` dispatches that derived action into a bitmask-oriented helper family
- selected-row byte `+1D` now looks more like part of the battler affliction or collapse-state family than like a generic active-transition flag
- selected-row bytes `+1F` through `+23` still form a transient working-state block, with `+23` as the timed substate byte
- current-slot byte `+25` behaves like the countdown for that substate
- current-slot bytes `+38`, `+39`, and `+3A` are configured object parameters consulted by the controller
- the exact gameplay identity of the family is still unproven, but it is no longer reasonable to treat it as a generic misc dispatcher

## Best next target

- See `notes/class2-mask-helper-family.md` for the decoded bitset layer. The best next move is to map the candidate list rooted at `9FAC` or decode the metadata tables around `9FC9`, so the family can be named from concrete behavior instead of just transition structure.
