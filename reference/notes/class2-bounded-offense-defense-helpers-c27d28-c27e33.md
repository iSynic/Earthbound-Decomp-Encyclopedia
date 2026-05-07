# Class2 Bounded Offense Defense Helpers C27D28 C27E33

This note captures the strongest current local model for the small helper quartet `C2:7D28`, `C2:7D82`, `C2:7DDC`, and `C2:7E33`.

See also [class2-late-stat-and-resource-family-c28e42-c29e38.md](notes/class2-late-stat-and-resource-family-c28e42-c29e38.md).
See also [class2-late-normalization-and-odor-family-c29051-c29254.md](notes/class2-late-normalization-and-odor-family-c29051-c29254.md).

## Working Names

- `C2:7D28` = `ApplyBoundedOffenseIncrease`
- `C2:7D82` = `ApplyBoundedDefenseIncrease`
- `C2:7DDC` = `ApplyBoundedOffenseDecrease`
- `C2:7E33` = `ApplyBoundedDefenseDecrease`

## Main result

These helpers are now much better understood as a bounded offense or defense adjustment quartet over battler rows.

The safest current split is:

- `C2:7D28` = bounded offense increase helper
- `C2:7D82` = bounded defense increase helper
- `C2:7DDC` = bounded offense decrease helper
- `C2:7E33` = bounded defense decrease helper

## Common shape

All four helpers take a battler-row pointer in `A`, then:

- operate on either row `+0x26` (offense) or row `+0x28` (defense)
- derive a step size from the high nibble of the current stat, with minimum step `1`
- apply one increment or decrement of that size
- clamp the result against a bound derived from the corresponding base stat byte

The relevant battler fields are:

- `+0x26` = offense
- `+0x28` = defense
- `+0x32` = base offense
- `+0x33` = base defense

## Increase-side helpers

### `C2:7D28`

`7D28` operates on offense.

It:

- reads current offense at `+0x26`
- derives the step from the high nibble, minimum `1`
- adds that step to current offense
- computes a cap from base offense `+0x32` as roughly `base * 5 / 4`
- if the new current offense exceeds that cap, clamps it back down to the cap

So the healthiest local name is a bounded offense increase helper.

### `C2:7D82`

`7D82` is the defense twin.

It:

- reads current defense at `+0x28`
- derives the same high-nibble step, minimum `1`
- adds that step to current defense
- computes a cap from base defense `+0x33` as roughly `base * 5 / 4`
- clamps the result to that cap when needed

So the healthiest local name is a bounded defense increase helper.

## Decrease-side helpers

### `C2:7DDC`

`7DDC` operates on offense.

It:

- reads current offense at `+0x26`
- derives the same high-nibble step, minimum `1`
- subtracts that step from current offense
- computes a floor from base offense `+0x32` as roughly `base * 3 / 4`
- if the new current offense falls below that floor, raises it back to the floor

So the healthiest local name is a bounded offense decrease helper.

### `C2:7E33`

`7E33` is the defense twin.

It:

- reads current defense at `+0x28`
- derives the same high-nibble step, minimum `1`
- subtracts that step from current defense
- computes a floor from base defense `+0x33` as roughly `base * 3 / 4`
- clamps the result back up to that floor when needed

So the healthiest local name is a bounded defense decrease helper.

## Caller anchors

Current useful callers are:

- `C2:9E53 -> 7D28` for offense-increase family behavior
- `C2:7D82` remains the bounded defense-increase helper, but this pass does not
  promote a concrete `9E38` caller for it
- `C2:8F3C -> 7DDC` for offense decrease
- `C2:926F -> 7DDC` for odor or stinky-gas offense reduction
- `C2:8F6E -> 7E33` and `C2:9EA9 -> 7E33` for defense decrease

That makes the quartet a real shared helper layer behind the late stat-mutation actions, not just a one-off curiosity.

## Current takeaway

The current takeaway is:

- late action-table stat mutators are built on a small reusable helper quartet
- the helpers use the same step heuristic and mirrored `5/4` cap vs `3/4` floor bounds
- offense and defense now have a clean local increase/decrease helper map

That gives the later `8EAE`, `8F21`, `9E38`, `9E7F`, and `9254` action notes a stronger common mechanical foundation.
