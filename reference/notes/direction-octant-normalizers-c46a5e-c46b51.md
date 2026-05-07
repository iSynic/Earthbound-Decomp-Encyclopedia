# Direction Octant Normalizers `C4:6A5E..6B51`

This note closes the small direction-conversion corridor that sits between the coordinate/vector helpers at `C4:1EFF / C4:1FFF` and the movement/slot update code around `C4:6FC0..72FF`.

The immediately following movement-target/vector layer is now documented in `notes/movement-target-bounds-and-vector-refresh-c46ef8-c47369.md`. That note shows the main consumers of `C4:6AAC`, `C4:6ADB`, `C4:6B0A`, `C4:6B37`, and `C4:6B51`.

The common pattern is:

- direction angles are represented in a 16-bit circle
- one octant is `0x2000`
- adding `0x1000` before division rounds an angle to the nearest octant
- `$2AF6[current]` stores the last/current facing octant used by movement refresh logic
- `$1A86[current]` caches a rounded octant produced by `C4:6B0A`

## Small direction tables

`C4:6A7A` and `C4:6A8A` are both 8-word octant-to-even-facing tables. The two tables use different boundary bias:

- `C4:6A7A`: `0,2,2,2,4,6,6,6`
- `C4:6A8A`: `0,0,2,4,4,4,6,0`

The second table is the one used at the sprite-facing refresh sites. Callers compare the previous `$2AF6[current]` bucket against the new bucket and call `C0:A48F(current)` when the coarse sprite-facing bucket changes.

`C4:6B41` is another 8-word table used by `C4:6B51` after angle rounding:

- `2,3,4,5,6,7,7,1`

This is not the same even-facing map as `C4:6A7A / C4:6A8A`; it is used as a walk/step direction encoding by the caller at `C4:72C9`.

## Direction and target helpers

`C4:6AAC` computes a direction from the current slot position `$0B8E/$0BCA` to that slot's cached target `$0FC6/$1002` through the sign/delta helper at `C4:5FA8`.

`C4:6ADB` computes the same current-slot-to-target direction through `C4:1EFF`, giving the slope-threshold octant path already documented in the vector helper note.

`C4:6B0A` rounds an input angle to the nearest octant by evaluating `(angle + 0x1000) / 0x2000`, then stores the result to `$1A86[current]`.

`C4:6B2D` floors an input angle to an octant by evaluating `angle / 0x2000`.

`C4:6B37` rotates a direction octant by half a turn with `(octant + 4) & 7`.

`C4:6B65` and `C4:6B79` are exact target setters:

- `C4:6B65` copies player position `$9877/$987B` into current slot target `$0FC6/$1002`.
- `C4:6B79` copies `$9E2D/$9E2F` into current slot target `$0FC6/$1002`.

2026-05-06 source polish follow-up:
`src/c4/direction_octant_target_helpers.asm` now names the current-slot live
anchor tables, cached target pair, rounded-octant cache, staged new-entity
position words, player position/facing words, registry slot list, angle
rounding constants, octant mask, and the `$00FE` recent-registry target path.
The comments keep the helper ownership to direction conversion and C4-side
target staging while leaving the external resolver and angle/delta helpers to
their owning modules.

## Caller evidence

Direct callers found locally:

- `C4:6AA3`: `C4:7021`, `C4:702B`, `C4:7203`, `C4:720D`, `C4:72EF`, `C4:72F9`
- `C4:6AAC`: `C4:6FF4`
- `C4:6ADB`: `C4:71CA`
- `C4:6B0A`: `C0:CF38`, `C0:CF41`, `C0:D96D`, `C4:71DD`
- `C4:6B37`: `C4:71E9`, `C4:72D5`
- `C4:6B51`: `C4:72C9`

The C0 callers line up with the movement-vector note: `C0:CEBE` and nearby movement code use `C4:6B0A` to detect coarse facing-sector changes and refresh sprites when needed.

The C4 movement-target pass adds the other half of the contract: `C4:6F7C` uses `C4:6AAC` for sign/delta target stepping, while `C4:7143` uses `C4:6ADB` and `C4:7044` for angle-based target stepping and vector projection.

## Working Names

- `C4:6A5E` = `PlayerDirection987fTurnBiasTable`
- `C4:6A6E` = `MapPlayerDirection987fToTurnBias`
- `C4:6A7A` = `DirectionOctantToAltFacingQuadrantTable`
- `C4:6A8A` = `DirectionOctantToSpriteFacingQuadrantTable`
- `C4:6A9A` = `MapOctantToAltFacingQuadrant`
- `C4:6AA3` = `MapOctantToSpriteFacingQuadrant`
- `C4:6AAC` = `ComputeCurrentSlotSignDeltaTargetDirection`
- `C4:6ADB` = `ComputeCurrentSlotTargetDirectionOctant`
- `C4:6B0A` = `RoundAngleToOctantAndCacheCurrentSlot`
- `C4:6B2D` = `FloorAngleToDirectionOctant`
- `C4:6B37` = `RotateDirectionOctantHalfTurn`
- `C4:6B41` = `RoundedAngleToWalkDirectionTable`
- `C4:6B51` = `RoundAngleToWalkDirectionStep`
- `C4:6B65` = `SetCurrentSlotTargetToPlayerPosition`
- `C4:6B79` = `SetCurrentSlotTargetTo9e2dPosition`

## Confidence boundaries

### Locally proved

- `C4:6B0A` is rounded octant conversion and writes `$1A86[current]`.
- `C4:6B2D` is unrounded/floored octant conversion.
- `C4:6B37` is a half-turn octant rotation.
- `C4:6AA3` is the coarse-facing map used to decide whether `C0:A48F` should refresh the current slot.
- `C4:6B65` and `C4:6B79` are exact current-slot target-position setters.

### Still open

- the exact player-visible facing labels for direction values `0..7`
- why `C4:6A7A` and `C4:6A8A` use different boundary bias, beyond their observed caller split
- the broader identity of `$1A86[current]` outside the rounded-octant cache use seen here
