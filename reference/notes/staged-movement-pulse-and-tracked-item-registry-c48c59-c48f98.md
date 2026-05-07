# Staged Movement Pulse And Tracked Item Registry (`C4:8C59..C4:90ED`)

This note tightens the movement helper band used by the `C0:6E6E` and `C0:70CB` staged-movement paths, plus the adjacent tracked-item pulse registry used by the Fresh Egg / Chick / Chicken side system.

See also [movement-trigger-helper-bodies.md](notes/movement-trigger-helper-bodies.md), [staged-movement-wrapper-70cb.md](notes/staged-movement-wrapper-70cb.md), and [teddy-bear-and-egg-item-cleanup-branches.md](notes/teddy-bear-and-egg-item-cleanup-branches.md).

## Main result

The range has two connected but distinct roles:

1. `C4:8C59..8E95` accumulates movement-direction pulse tokens into `$9E58/$9E59` and installs them through the animation-script installer path at `C0:402B`.
2. `C4:8ECE..90ED` manages and ticks a four-entry tracked-item pulse registry rooted at `$9F1A`, with per-entry timers sourced from `D5:F4BB`.

The movement side is used by delayed movement setup. The tracked-item side is used by the egg/chick/chicken inventory refresh path.

## Movement pulse accumulator

### `C4:8C59`

This is an eight-word lookup table used after an octant is computed:

```text
00 08 00 09 00 01 00 05 00 04 00 06 00 02 00 0A
```

The values are not raw facing octants. They are direction/action pulse selector ids passed to `C4:8C97`.

### `C4:8C69`

This clears the movement pulse accumulator:

- clears `$9F18`
- clears 64 three-byte-ish slots rooted at `$9E58/$9E59`

The two direct callers are the C0 staged movement setup paths at `C0:6E86` and `C0:70E4`, which clear this accumulator before building a new staged movement script.

### `C4:8C97`

This helper records one movement pulse selector in the `$9E58/$9E59` accumulator. If the selector matches the current tail entry, it increments that entry's repeat count instead of appending a new entry. Otherwise it advances `$9F18` and appends a new selector/count pair.

The exact byte layout is still a little awkward to express because it mixes byte counters and word selectors, but the role is clear from the callers: compress repeated pulse selector ids into a compact runtime script.

### `C4:8D38`

This is a compact signed unit-step table adjacent to the staged-movement pulse builder. It contains sixteen little-endian words:

```text
0000 0001 0001 0001 0000 FFFF FFFF FFFF
FFFF 0000 0001 0001 0001 0000 FFFF FFFF
```

The table shape is an eight-direction/octant vector pair: two eight-word signed components with values `-1`, `0`, and `1`. No direct local consumer has surfaced yet, but its placement between the pulse run accumulator and `C4:8D58` makes it safest to classify as an octant signed-unit-delta table used by this movement corridor.

### `C4:8D58`

This is the main duration/path helper for staged movement.

Inputs are the current position and target position from the C0 callers. It:

- computes signed deltas between current and target coordinates
- returns immediately when both axes are within one pixel-ish unit
- computes the direction from current to target through `C4:1EFF`
- rounds that direction into an octant with `(angle + $1000) / $2000`
- maps that octant through `C4:8C59`
- records the resulting pulse selector through `C4:8C97`
- advances the simulated current position by a four-word delta pair from the `C4:4DD6` and `C4:4F96` tables
- loops until it reaches the target
- returns the number of simulated steps

That matches the delayed-action timer callers: `C0:6EDC`, `C0:6F57`, `C0:7154`, and `C0:71A5` use its return value as the computed delay for staged movement callbacks.

### `C4:8E6B`

This is the simple repeated-pulse sibling. It takes a pulse selector in `A` and repeat count in `X`, maps the selector through `C4:8C59`, and calls `C4:8C97` that many times.

The C0 staged-movement callers use it after `C4:8D58` to append a short tail of direction/action pulses from the `C3:E200` and `C3:E208` parameter tables.

### `C4:8E95`

This finalizes the movement pulse accumulator. It reserves a new accumulator tail entry, then passes the `$9E58` runtime script buffer to `C0:402B`, locally named `Install_AnimationScriptFromCallerPointer`.

The C0 movement setup paths call it immediately after queuing the delayed movement callback and storing staged target coordinates, which makes this the "install the generated movement pulse script" step.

Source polish: `src/c4/staged_movement_and_tracked_item_pulse_helpers.asm`
now names the movement pulse first index, active run flag, minimum staged
movement delta, signed-word inversion mask, direction half/full octant rounding
span, and repeated-pulse done count used by `C4:8C69..8E95`.

## Tracked item pulse registry

### `C4:8ECE`

This helper checks whether a tracked-item slot is active. For a small index in `A`, it inspects the matching four-byte record at `$9F1A + index * 4` and returns `1` if either of the two pulse/timer bytes is nonzero, otherwise `0`.

### `C4:8EEB`

This arms or refreshes one tracked-item pulse record. If the selected record was previously inactive, it reloads the global throttle at `$9F2C` to `#$3C` and increments the active count at `$9F2A`.

It then reads a five-byte record from `D5:F4BB + index * 5` and writes the record's timer/id bytes into the `$9F1A` runtime slot. The helper also calls `C4:5F7B(2)` while computing the refreshed timer value.

The direct callers are `C3:EAFC` and `C3:EB88`, both in the party overlay / egg-family refresh corridor.

### `C4:8F98`

This is the clearing sibling for `C4:8EEB`. If the selected tracked-item record is active, it decrements `$9F2A` and clears the record's two activity bytes.

The direct caller is `C3:EB50`, which runs before scanning active inventories for the egg/chick/chicken item family.

### `C4:8FC4`

This is the periodic tick worker for the same tracked-item records.

It returns early while broader display/menu gates are active:

- `$4DBA + $5D60 != 0`
- `$B4B6 != 0`
- `$98A5 == 2`

Otherwise it decrements global throttle byte `$9F2C`. When the throttle reaches zero, it reloads `$9F2C = #$3C` and walks four records rooted at `$9F1A`.

For each active record it:

- decrements the pulse countdown byte
- when that countdown reaches zero, refreshes it using the slot's base byte plus `C4:5F7B(2) - 1`
- plays or triggers the slot's effect id through `C0:ABE0`
- decrements the item-transition countdown byte
- when that countdown reaches zero, reads the five-byte `D5:F4BB + index * 5` row and runs the `C1:8EAD` / `C1:8BC6` item update pair

The direct caller is `C0:5246`, which makes this a global periodic service routine rather than another explicit egg/chick/chicken inventory scan helper.

Source polish: the tracked-item half now names the active/inactive return
values, blocked overworld state, first-slot and first-pulse sentinels, low-byte
masks, and the full-value argument passed to `C1:8EAD` while ticking records.

## Working Names

- `C4:8C59` = `MovementOctantToPulseSelectorTable`
- `C4:8C69` = `ClearMovementPulseAccumulator`
- `C4:8C97` = `AppendMovementPulseSelectorRun`
- `C4:8D38` = `MovementOctantSignedUnitDeltaTable`
- `C4:8D58` = `BuildStagedMovementPulsesAndReturnDelay`
- `C4:8E6B` = `AppendRepeatedMovementPulseSelector`
- `C4:8E95` = `InstallGeneratedMovementPulseScript`
- `C4:8ECE` = `CheckTrackedItemPulseSlotActive`
- `C4:8EEB` = `ArmTrackedItemPulseSlotFromD5f4bb`
- `C4:8F98` = `ClearTrackedItemPulseSlot`
- `C4:8FC4` = `StepTrackedItemPulseSlots`

## Still open

- exact byte-field names for the `$9E58/$9E59` generated movement pulse script
- exact byte-field names for each four-byte `$9F1A` tracked-item pulse record
- exact X/Y or component ordering for the two halves of `C4:8D38`, because the direct table consumer has not been found locally yet
- whether the pulse selector ids from `C4:8C59` correspond to actor-facing animation ids, movement-command ids, or a narrower action-script selector enum
