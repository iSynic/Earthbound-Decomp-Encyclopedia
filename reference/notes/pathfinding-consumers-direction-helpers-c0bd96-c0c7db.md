# Pathfinding consumers and direction helpers (`C0:BD96-C0:C7DB`)

## Scope

This strip sits immediately after the `C0:B9BC/C0:BA35` pathfinding setup
layer and before the larger movement-state setter beginning at `C0:C83B`.
It is mostly consumer code: wrappers that prepare a one-target path request,
copy path steps into local lanes, and then small helpers that choose or gate
entity directions relative to the player.

The ebsrc reference corroborates several boundaries here:

- `C0:BC74` is included as `misc/find_path_to_party.asm`.
- `C0:C4F7` is included as `overworld/get_direction_from_player_to_entity.asm`.
- `C0:C608` is included as
  `overworld/get_opposite_direction_from_player_to_entity.asm`.
- `C0:C69E` is included as
  `overworld/actionscript/get_direction_turned_randomly_left_or_right.asm`.

Those names fit the local access patterns, but the details below are from the
ROM-local decode.

## Path request wrappers

`C0:BD96` builds a one-entity path request using the party/member index in
`$9889`. It:

- Uses `$F200` as the temporary path-record base.
- Seeds `$F278/$F27A` with a fixed `#$0038` rectangle.
- Converts the selected entity's `$0B8E/$0BCA` position into 64x64 path-grid
  coordinates through the C4 coordinate tables at `C4:2A1F`, `C4:2A41`, and
  `C4:2AEB`.
- Calls `C0:B9BC` to snapshot live positions into the caller record.
- Calls `C0:BA35` with one candidate, range-like constants `#$00FC` and
  `#$0032`, and the same `$F200` record.
- On success, uses the chosen entity in `$F2B0` plus path result fields
  `$F2A6/$F2A8` to write a new `$0B8E/$0BCA` position, advances that slot's
  `$2E02` path pointer by four bytes, and decrements `$2E3E`.

`C0:BF72` is the same family, but it targets the current entity slot in
`$1A42` instead of `$9889`. It prepares the same `$F200` record and calls
`C0:BA35`, but does not apply the returned step back into `$0B8E/$0BCA`.
Before the solver call it also writes wrapped coordinates into `$F27C/$F27E`,
which look like caller-visible target or origin coordinates for this variant.

## Path lane copy wrappers

`C0:C0B4`, `C0:C19B`, and `C0:C251` are higher-level path consumers. Each takes
an input lane number in `A`, derives a lane base as:

```text
$4A96 + lane * $50
```

and copies up to `#$0014` four-byte path steps into that lane.

The three wrappers differ by path source:

- `C0:C0B4` temporarily disables the current slot through `$2C5E`, calls the
  named `FIND_PATH_TO_PARTY` entry at `C0:BC74` with a `#$0030` rectangle, then
  advances `$2E02/$2E3E` before copying remaining steps forward.
- `C0:C19B` uses `C0:BD96`, then copies the current `$2E02` path buffer forward
  into the lane.
- `C0:C251` uses `C0:BF72`, decrements `$2E3E`, then copies path steps backward
  from the tail of the source buffer into the lane.

All three wrappers first consult the current player tile context through
`C0:0AA1` and `C3:DFE8`; a zero table result aborts the path consumer before
the expensive path call.

## Small state and distance helpers

`C0:C30C` refreshes a current-slot profile/state. It uses `$2C9A[slot]` to
index a `CF:8985` table family, calls `C2:1628`, stores either `0` or `4` into
`$2AF6[slot]`, then calls the profile refresh helper at `C0:A48F`. `C0:C353`
is the current-slot wrapper for it, and `C0:C35D` simply returns `$9885`.

`C0:C363` and `C0:C3F9` compute Manhattan distance buckets from the player
position `$9877/$987B` to the current slot's `$0B8E/$0BCA` position. Both return
small values from `0..3`; `C0:C3F9` uses tighter thresholds
(`#$0080`, `#$0050`, `#$0040`) than `C0:C363`
(`#$0100`, `#$00A0`, `#$0080`).

`C0:C48F` and `C0:C4AF` gate those distance buckets:

- If `$2C5E[current]` is nonzero, return `0`.
- If `$5D58` is nonzero, return `#$FFFF`.
- Otherwise return the bucket from `C0:C363` or `C0:C3F9`.

## Direction helpers

`C0:C4CF-C0:C4F6` is data, not executable code. The tail of this table is used
as the direction remap table for the reference-named
`GET_OPPOSITE_DIRECTION_FROM_PLAYER_TO_ENTITY` entry at `C0:C608`.

`C0:C4F7` computes the direction from the player to the current entity. It
passes player coordinates `$9877/$987B`, current entity coordinates
`$0B8E/$0BCA`, and the current slot from `$1A42` into the C4 direction helper
at `C4:5FA8`, then returns that direction.

`C0:C524` is a direction/encounter gating predicate for the current slot. It
first checks a table family rooted at `D0:C60D` through `C2:1628`. If that path
does not produce a match, it falls back to a party-level threshold check via
`C0:546B`, `$2D12[current]`, `C0:8FF7`, and the `D5:9589` data family. It also
uses `$3186[current]` as a secondary threshold. The safest local name is still
"current-slot direction/encounter gate" rather than a more specific gameplay
label.

`C0:C608` returns the opposite/remapped direction from player to entity.
`C0:C615` chooses the opposite/remapped direction only when `C0:C524` passes;
otherwise it returns the direct `C0:C4F7` direction.

`C0:C62B` combines the same `C0:C524` gate with an entity-position lookup
through `C4:1EFF`. If `$2C9A[current] >= #$7FFF` and the gate passes, it adds
`#$8000` to the result, so the high bit looks like a flagged direction or
targeting result.

`C0:C682` rotates an input direction by the current slot's `$2AF6` value and
masks it to three bits. `C0:C69E` calls the RNG helper at `C0:8E9A`, chooses
`+1` or `-1`, and passes that into `C0:C682`; this matches the ebsrc
`GET_DIRECTION_TURNED_RANDOMLY_LEFT_OR_RIGHT` name.

## Visibility, grid, and footprint checks

`C0:C6B6` is a screen/proximity gate for the current slot. If `$9F47 >= 4`, it
returns `#$FFFF` immediately. Otherwise it compares the current entity's
position against a rectangle around `$9877/$987B` and returns `#$FFFF` when the
entity is inside that live-area window, or `0` when it is outside.

`C0:C711` checks whether the current slot is aligned closely enough to its
direction-adjusted grid position. It subtracts C4 direction offsets from the
entity position fields, ORs together the low-byte residuals, and returns
`#$FFFF` only when the residual collapses to zero.

`C0:C760` is the parameterized sibling of `C0:C711`. It takes caller-supplied
coordinates in `A/X` and a direction in `Y`, subtracts the same `C4:2A1F` and
`C4:2A41` offsets, and returns `#$FFFF` when the adjusted low-byte residuals
are grid-aligned.

`C0:C7AC` refreshes the current slot's footprint mask from the cached
coordinates at `$2848/$284A`, but only when `C0:9EFF` reports that the cached
position context is valid.

`C0:C7DB` is a current-slot footprint probe. It calls the already-mapped
`C0:5F33` half-footprint collision helper with the current slot's
`$0B8E/$0BCA` coordinates and stores the returned mask in `$2BAA[current]`.

`C0:C808` is the same footprint probe with the current slot's `$0C06` value
subtracted from Y before the `C0:5F33` call. This looks like the version used
when the collision footprint needs to be checked at a vertical offset instead
of the raw entity origin.

## Practical interpretation

The pathfinding subsystem now has a clearer top and bottom:

- `C0:B9BC/C0:BA35` build the grid and candidate records.
- `C0:BD96/C0:BF72/C0:BC74` are the caller-facing path request variants.
- `C0:C0B4/C0:C19B/C0:C251` consume those path buffers into `$4A96` lanes.
- `C0:C4F7-C0:C69E` supplies direction choices around those movement decisions.
- `C0:C6B6-C0:C7DB` supplies proximity, alignment, and collision-footprint
  gates for the current slot.

The next natural frontier is `C0:C83B`, where those helper decisions appear to
feed a larger movement-state update routine.

## Working Names

- `C0:BC74` = `FindPathToParty`
- `C0:BD96` = `BuildPathRequestToPartyMemberAndApplyStep`
- `C0:BF72` = `BuildPathRequestToCurrentEntity`
- `C0:C0B4` = `CopyPathToLane_FromPartyPath`
- `C0:C19B` = `CopyPathToLane_FromPartyMemberRequest`
- `C0:C251` = `CopyPathToLane_FromCurrentEntityRequestReverse`
- `C0:C30C` = `RefreshCurrentSlotProfileFromField2C9A`
- `C0:C353` = `RefreshCurrentSlotProfileFromField2C9A_Current`
- `C0:C35D` = `GetPlayerContext9885`
- `C0:C363` = `GetPlayerDistanceBucketWide`
- `C0:C3F9` = `GetPlayerDistanceBucketTight`
- `C0:C48F` = `GateWidePlayerDistanceBucket`
- `C0:C4AF` = `GateTightPlayerDistanceBucket`
- `C0:C4CF` = `PlayerDirectionRemapTable`
- `C0:C4F7` = `GetDirectionFromPlayerToEntity`
- `C0:C524` = `CheckCurrentSlotDirectionEncounterGate`
- `C0:C608` = `GetOppositeDirectionFromPlayerToEntity`
- `C0:C615` = `GetGatedOppositeOrDirectPlayerEntityDirection`
- `C0:C62B` = `GetGatedEntityPositionDirectionFlag`
- `C0:C682` = `RotateDirectionByCurrentSlotClass`
- `C0:C69E` = `GetDirectionTurnedRandomlyLeftOrRight`
- `C0:C6B6` = `CheckCurrentSlotInsideLiveAreaWindow`
- `C0:C711` = `CheckCurrentSlotDirectionAdjustedGridAlignment`
- `C0:C760` = `CheckDirectionAdjustedGridAlignment`
- `C0:C7AC` = `RefreshCurrentSlotFootprintMaskFromCachedPosition`
- `C0:C7DB` = `UpdateCurrentSlotFootprintMask`
- `C0:C808` = `UpdateCurrentSlotFootprintMaskWithHeightOffset`
