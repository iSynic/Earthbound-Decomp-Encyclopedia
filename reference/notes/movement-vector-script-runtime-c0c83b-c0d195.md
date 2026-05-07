# Movement vector script runtime (`C0:C83B-C0:D195`)

## Scope

This frontier is the action-script movement layer immediately after the
pathfinding/direction helper strip. It converts script-facing direction and
speed fields into per-slot velocity words, computes script task timers from
those velocities, and supplies a few collision/target helpers used by roaming
NPC scripts.

The ebsrc event scripts corroborate the usage:

- `EVENT_UNKNOWN_C0C83B` is commonly called after `EVENT_SET_DIRECTION`.
- `EVENT_UNKNOWN_C0CA4E` is called after a random direction and before
  velocities are cleared.
- `EVENT_UNKNOWN_C0CCCC`, `EVENT_UNKNOWN_C0CD50`, `EVENT_UNKNOWN_C0CC11`,
  `EVENT_UNKNOWN_C0D0D9`, and `EVENT_UNKNOWN_C0D0E6` appear in the same
  wandering/chase-style scripts.

## Working Names

- `C0:C83B` = `InstallScriptMovementVectorFromDirection`
- `C0:CA4E` = `SetMovementTaskTimerFromActiveVector`
- `C0:CBD3` = `SetMovementTaskTimerFromSpeedScale`
- `C0:CC11` = `SetMovementTaskTimerFromCachedTarget`
- `C0:CCCC` = `InitializeArcMovementTargetState`
- `C0:CD50` = `AdvanceArcMovementVectorFromPhase`
- `C0:CEBE` = `TurnArcPhaseTowardTargetAngle`
- `C0:CF97` = `FindNearbyCollisionMapTarget`
- `C0:D0D9` = `FindNearbyRoamingCollisionTarget`
- `C0:D0E6` = `MoveOrSnapSlotTowardCachedPlayerTarget`
- `C0:D15C` = `HasUsableOverlapNeighborContext`
- `C0:D195` = `ReturnFalse_MovementPredicate`

## `C0:C83B`: build per-slot movement vectors

`C0:C83B` takes a direction/mode value in `A`, stores it in
`$1A86[current]`, and uses the current slot's `$2B32` speed-like field to
derive signed vector components.

The routine writes four per-slot velocity words:

```text
$0DAA[current] = X/fraction component
$0CF6[current] = X/high or paired component
$0DE6[current] = Y/fraction component
$0D32[current] = Y/high or paired component
```

That field family matches the already-documented `C0:9FC8` movement integrator,
which adds `$0DAA` into fractional X state and `$0DE6` into fractional Y state.

The mode values `0..7` select signed combinations of the derived components:

- Modes `0`, `2`, `4`, and `6` are axial: one component pair is zeroed while
  the other is positive or negative.
- Modes `1`, `3`, `5`, and `7` are diagonal: both component pairs are populated,
  with signs selected by the mode.

For odd modes it uses a `#$B505` multiplier constant, which is the familiar
fixed-point diagonal scale value for `sqrt(1/2)`. That strongly supports the
interpretation that this routine is setting normalized cardinal/diagonal
movement velocities from the script's current direction.

## Timer helpers from active vectors

`C0:CA4E` reads the current slot's active vector words, normalizes their signs,
selects the dominant component, and uses the shared math helpers at
`C0:9246` and `C0:90FF` to compute a task timer. It writes the result to
`$1372[$1A46]`. Event script `C3:AB9E` calls it with small random values after
setting a random direction, so the safest local name is "set movement task
timer from current vector and distance/count".

`C0:CBD3` is the simpler sibling. It scales the current slot's `$2B32` speed
field by caller input and stores the math result into the same `$1372[$1A46]`
task timer field.

`C0:CC11` computes a timer from a cached target point. It compares the absolute
distance from current position `$0B8E/$0BCA` to target `$0FC6/$1002`, chooses
the axis with the larger delta, divides that delta by the corresponding active
vector component, forces the result to at least `1`, and writes it to
`$1372[$1A46]`.

Together these helpers explain why so many event scripts do:

```text
set direction -> C0:C83B -> movement wait/timer helper
```

The script layer is installing velocity, then deriving how long the current
task should run before the next action-script instruction resumes.

## Target and arc state helpers

`C0:CCCC` initializes an arc or wander target for the current slot. It copies
the current X position into `$0FC6[current]`, copies current Y plus `#$0010`
into `$1002[current]`, computes a step increment into `$0F8A[current]`, chooses
either `$2AF6 = 0` or `$2AF6 = 4` at random, converts that into the sign flag
`$2DC6`, and clears the angle/phase accumulator at `$0F4E`.

`C0:CD50` advances that accumulator by adding or subtracting `$0F8A` according
to `$2DC6`, stores the new phase in `$0F4E`, calls `C4:1FFF` with
`X = #$1000`, and converts the resulting offsets into the same `$0CF6/$0DAA`
and `$0D32/$0DE6` vector fields used by `C0:C83B`. It returns a phase shifted
by `#$4000` in the direction implied by `$2DC6`.

`C0:CEBE` smoothly turns the current phase `$0F4E` toward the input angle in
`A`. It chooses the shortest direction around the 16-bit angle space, steps by
`#$0800`, increases `$2B32` toward the cap in `$0F12`, and calls `C0:A48F` when
the coarse direction from `C4:6B0A` changes. This looks like a sprite/profile
refresh on facing-sector crossings.

## Collision-map target search

`C0:CF58-C0:CF96` is byte data, not code. It is a compact direction walk table
made of values `1..4`.

`C0:CF97` scans outward around the current slot in 64x64 wrapped path-grid
space. It takes an 8-bit collision mask in `A` and a maximum step count in `X`,
tests the active collision page at `$E000`, and walks according to the
`C0:CF58` direction table. On the first matching collision cell it converts the
grid coordinate back through the C4 coordinate tables and writes target
coordinates to `$0FC6[current]` and `$1002[current]`, returning `#$FFFF`.
If it exhausts the scan, it returns `0`.

`C0:D0D9` is the event-callable wrapper for that scan. It searches up to
`#$003C` steps with mask `#$03`.

`C0:D0E6` moves or snaps the current slot toward the cached `$2848/$284A`
position. If the current slot is at distance bucket zero and `$2C5E` is set,
it snaps directly to the player position `$9877/$987B`. Otherwise it refreshes
the cached position through `C0:9EFF`, probes collision with `C0:5CD7`, reduces
`$2B32` by `#$1000` on blocked movement, and writes `$2848/$284A` into
`$0B8E/$0BCA` on success.

## Small boolean helpers

`C0:D15C` checks whether the current slot has a usable overlap/neighbor context.
It returns `0` while `$5D56 & 2` is set, returns `#$FFFF` if `$28CC` is the
current slot, and otherwise checks the per-slot neighbor cache at `$289E`.

`C0:D195` is a hard false helper: it returns `0`.

## Practical interpretation

This gives the action-script movement layer a much stronger model:

- `C0:C83B` installs velocity from direction and speed.
- `C0:CA4E`, `C0:CBD3`, and `C0:CC11` translate those vectors into task
  timers.
- `C0:CCCC`, `C0:CD50`, and `C0:CEBE` maintain arc/phase style movement.
- `C0:CF97/D0D9` find nearby collision-map targets for roaming scripts.
- `C0:D0E6/D15C/D195` provide small movement/neighbor predicates around that
  same script family.

The next frontier starts at `C0:D19B`, which appears to consume the same
`$1A86`, `$2C9A`, `$2C5E`, and pathfinding data in a broader NPC/party
relation routine.
