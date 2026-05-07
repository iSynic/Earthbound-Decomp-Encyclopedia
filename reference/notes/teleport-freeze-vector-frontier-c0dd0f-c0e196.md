# Teleport freeze and vector frontier (`C0:DD0F-C0:E196`)

## Scope

This strip follows the coordinator/path helpers and leads into the named
teleport include family in `ebsrc-main`. The local evidence points at three
related jobs:

- frame-pump waits used by scripts and transitions,
- teleport state/destination setup,
- object-freeze and vector setup for the teleport/flyover movement effect.

The reference include map explicitly names `C0:DD53` as
`overworld/set_teleport_state.asm`, and the neighboring includes after this
strip are `teleport_freezeobjects`, `teleport_freezeobjects2`, and
`teleport_mainloop`.

## Frame-pump waits

`C0:DD0F` is a wait-until-idle helper. While `$0028` is nonzero, it repeatedly
calls:

- `C0:88B1`
- `C0:9466`
- `C0:8B26`
- `C0:8756`

and returns with `RTS` when `$0028 & #$00FF` is clear.

`C0:DD2C` is the counted sibling. It takes a count in `A`, runs the same four
per-frame helpers once per count, and returns with `RTL`.

## Teleport state and destination setup

`C0:DD53` is corroborated by ebsrc as `SET_TELEPORT_STATE`. It stores the low
byte of `A` in `$9F3F` and another caller byte from the direct-page frame in
`$9F41`. The rest of this frontier treats `$9F3F/$9F41` as mode selectors.

`C0:DD79` consumes that teleport state. It clears or normalizes character state
through repeated `C2:165E` calls, uses `$9F3F` as an index into the `D5:7880`
table family through `C0:8FF7`, stores derived values in `$438A/$438C`, clears
`$5DD4/$4370/$436E` to `#$FFFF`, then calls `C0:19B2`. The safest local read is
that this prepares a destination/entity setup record for the teleport state.

## Freeze-object setup and teardown

`C0:DE16` loops over slots `#$0018..#$001D`, sets `$0F12[slot] = #$0008`, and
sets bit `#$0800` in `$1002[slot]`. This looks like the first phase of freezing
or flagging the transition object set.

`C0:DE46` calls `C0:DE16`, seeds `$9F61` from the RNG helper, writes `$9F63`
as either `4` or `8` depending on `$9F41`, clears `$9F65` in the non-`2` case,
and snapshots player position `$9877/$987B` into `$9F67/$9F69`.

`C0:DE7C` reverses much of the freeze setup for slots `#$0018..#$001D`: it
sets `$0F12 = 8`, clears bit `#$0800` in `$1002`, clears bit `#$8000` in
`$289E`, writes `#$FFFF` into the party record byte/word family rooted at
`$99CE + $37 + n * $5F`, and calls `C0:69ED`. This matches the
`teleport_freezeobjects2` neighborhood in the include map.

## Teleport collision/vector helpers

`C0:DED9` is a two-point footprint check. If `$9F43` is nonzero it returns
zero. Otherwise it calls `C0:5F33` twice, using the current party index `$9889`
as the slot argument, and ORs the two returned footprint masks together.

`C0:DF22` updates the teleport/flyover vector state. It uses `$9F43`,
`$9F45/$9F47`, and the player mode `$9887` to advance a fixed-point phase by
different constants. It then writes paired vector components to
`$9F49/$9F4B` and `$9F4D/$9F4F`, with direction-specific sign and zeroing logic
for direction values `0..7`. Odd directions use the same `#$B505` diagonal
scale constant seen in the normal movement-vector builder, so this is another
normalized cardinal/diagonal vector setup routine.

`C0:E196` snapshots the live player state into the 12-byte ring rooted at
`$5156`, using `$987D` as the ring index. It writes player X/Y, the current
footprint mask from `C0:5F33`, a zero word, and facing `$987F`, then increments
`$987D`. This is the same snapshot family used by the broader movement and
transition code.

## Practical interpretation

This strip is the bridge from ordinary frame waits into teleport/flyover setup:

- `DD0F/DD2C` keep the engine pumping while waits run.
- `DD53/DD79` install teleport state and destination/entity setup.
- `DE16/DE46/DE7C` flag and unflag the transition object set.
- `DED9/DF22/E196` provide collision, vector, and snapshot helpers used during
  the transition.

The next unresolved C0 frontier begins at `C0:E214`, still inside the same
movement/teleport neighborhood.

## Working Names

- `C0:DD0F` = `WaitForFramePumpIdle`
- `C0:DD2C` = `WaitFramePumpCountA`
- `C0:DD53` = `SetTeleportStateSelectors`
- `C0:DD79` = `PrepareTeleportDestinationState`
- `C0:DE16` = `FreezeTeleportTransitionObjects`
- `C0:DE46` = `InitializeTeleportTransitionObjectsAndVectors`
- `C0:DE7C` = `UnfreezeTeleportTransitionObjects`
- `C0:DED9` = `ProbeTeleportTwoPointFootprintCollision`
- `C0:DF22` = `UpdateTeleportDirectionVectorState`
- `C0:E196` = `SnapshotTeleportPlayerStateToRing`
