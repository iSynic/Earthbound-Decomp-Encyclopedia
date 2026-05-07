# Stairs / Escalator State Block (`5DAA..5DD6`)

This note tightens the shared traversal-state block that sits next to the doorway fields.

## Crosswalk

Using the `ebsrc` RAM map plus the local door-transition work, the current best mapping is:

- `$5DA8` = `FINAL_MOVEMENT_DIRECTION`
- `$5DAA` = `LADDER_STAIRS_TILE_X`
- `$5DAC` = `LADDER_STAIRS_TILE_Y`
- `$5DAE` = `CHECKED_COLLISION_LEFT_X`
- `$5DB0` = `CHECKED_COLLISION_TOP_Y`
- `$5DB6` = `SET_TEMP_ENTITY_SURFACE_FLAGS`
- `$5DB8` = `NORTH_SOUTH_COLLISION_TEST_RESULT`
- `$5DBA` = `NOT_MOVING_IN_SAME_DIRECTION_FACED`
- `$5DBE` = `DOOR_FOUND`
- `$5DC0` = `DOOR_FOUND_TYPE`
- `$5DC2` = `CURRENT_QUEUED_INTERACTION_TYPE`
- `$5DC4` = `USING_DOOR`
- `$5DC6` = `STAIRS_DIRECTION`
- `$5DC8` = `ESCALATOR_ENTRANCE_DIRECTION`
- `$5DCC` = `AUTO_MOVEMENT_DIRECTION`
- `$5DCE/$5DD0` = `STAIRS_NEW_X / STAIRS_NEW_Y`
- `$5DD2/$5DD4` = `ESCALATOR_NEW_X / ESCALATOR_NEW_Y`
- `$5DD6` = `CURRENT_MAP_MUSIC_TRACK`

## What is locally strong now

### `$5DD6`

This one is the firmest. `C0:068F4` / `C0:06A07` populate it from the door-destination family, and the surrounding `ebsrc` include naming points at change-music logic. So `$5DD6 = CURRENT_MAP_MUSIC_TRACK` is in good shape.

### `$5DC6`

`$5DC6` is no longer just a name borrowed from `ebsrc`.

In the type-`3` movement helper at `C0:6E6E`:

- the low path stores the incoming selector into `$5DC6`
- the follow-up path reloads `$5DC6`
- it uses `$5DC6` to index the tiny local tables at `C0:6E0A` and `C0:6E12`
- those tables drive a facing-like state in `$987F` and the staged target computation that feeds `C48D58`

That is exactly the shape we would expect from a direction field. So `STAIRS_DIRECTION` is now locally supported, not just cross-referenced.

### `$5DD0/$5DD2`

The same `C0:6E6E` helper family also gives a concrete local use for the second staged coordinate pair:

- `C0:6F70` stores the computed target into `$5DD0/$5DD2`
- `C0:6E2C` and `C0:6E4A` later commit that pair into live player X/Y

So this pair really is a staged destination family. The `ebsrc` names `STAIRS_NEW_X / STAIRS_NEW_Y` are now a good fit for the local behavior.

## What is still softer

### `$5DC8`

`ESCALATOR_ENTRANCE_DIRECTION` is still mainly a structural inference from the `ebsrc` RAM map. I do not yet have a comparably strong local consumer for `$5DC8` itself.

### `$5DD2/$5DD4`

`ESCALATOR_NEW_X / ESCALATOR_NEW_Y` is still the best current crosswalk for the second staged pair after the stairs pair, but it is not as directly proved locally as `$5DD6`, `$5DC6`, or `$5DD0/$5DD2`.

## Why this matters for `$9887`

This block gives the class-`4` / class-`6` surface interpretation much better footing.

- class `3` already anchors to door-transition logic
- `$5DC6` now behaves locally like a traversal-direction field
- `$5DD0/$5DD2` now behave locally like a staged traversal destination pair
- the remaining named traversal fields in the same block are stairs/escalator-specific

So the current surface-class read remains:

- `$9887 == 6` is the stronger candidate for a stairs-style surface class
- `$9887 == 4` is the stronger candidate for an escalator-entry-style surface class

## Update: raw ROM scan shows an escalator-side gap and a staged-pair mismatch

A direct raw-ROM scan for plausible `65816` absolute-address references sharpened one important caveat.

### `$5DC8`

I found **no direct code references** to `$5DC8` in this ROM using a filtered scan for plausible absolute-address opcodes.

So `ESCALATOR_ENTRANCE_DIRECTION` is still only a structural crosswalk from the `ebsrc` RAM map. It is useful, but it is not locally proved the way `$5DD6` and now `$5DC6` are.

### `$5DCC/$5DCE` and `$5DD0/$5DD2`

The local bank-`C0` movement callbacks add a second caution.

`C0:6F82/6FED` clearly treat `$5DCC/$5DCE` as a staged X/Y pair:

- they compare `$5DCE` against live Y at `$987B`
- on success they copy `$5DCC -> $9877` and `$5DCE -> $987B`

`C0:6E2C/6E4A` also clearly treat `$5DD0/$5DD2` as a staged X/Y pair:

- they copy `$5DD0 -> $9877` and `$5DD2 -> $987B`

That means the local code is reusing these words more like two staged destination pairs than like the clean `AUTO_MOVEMENT_DIRECTION / STAIRS_NEW_X / STAIRS_NEW_Y / ESCALATOR_NEW_X / ESCALATOR_NEW_Y` naming sequence from `ebsrc`.

## Best current read after this correction

- `$5DD6 = CURRENT_MAP_MUSIC_TRACK` is still strong.
- `$5DC6 = STAIRS_DIRECTION` is now locally supported.
- `$5DC8 = ESCALATOR_ENTRANCE_DIRECTION` remains plausible but unproved.
- The staged destination words from `$5DCC` through `$5DD4` should stay **tentative** because the local code is clearly using them in overlapping X/Y-pair roles.

So the class split still leans the same way:

- class `6` still looks like the stronger stairs-style candidate
- class `4` still looks like the stronger escalator-entry-style candidate

But the exact per-word names on the escalator side should stay provisional until a real local `$5DC8` or `$5DD2/$5DD4` consumer is pinned down.
