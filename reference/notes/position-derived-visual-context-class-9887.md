# Position-Derived Visual Context Class (`$9887`)

This note captures the strongest current local read for `$9887`, which is the clearest remaining control value in the `C0780F` visual-selector resolver.

See also [visual-selector-family-c0780f-c3f2b5.md](notes/visual-selector-family-c0780f-c3f2b5.md).
See also [sprite-pose-descriptor-cache-2a06-2cd6.md](notes/sprite-pose-descriptor-cache-2a06-2cd6.md).

## Main result

`$9887` now looks much more like a position-derived cell or terrain context class than a generic animation mode byte.

The strongest current local read is:

- `C00AA1` performs a packed map/cell-data lookup through `D7:B200`
- the low 3 bits of that lookup result are stored into `$9887`
- `C0780F` then uses `$9887` to choose between ordinary and alternate selector buckets for the `C3:F2B5` row lookup

So the safest current name is:

- position-derived visual context class

A slightly stronger but still cautious name would be:

- terrain/cell behavior class

## Working Names

- `C0:0AA1` = `LookupPositionCellContextWord`
- `C0:3A94` = `RefreshPositionDerivedVisualContextClass`

## Why `$9887` looks position-derived

The setup path at `C03A94` is the strongest local proof.

That code either:

- uses explicit coordinates from `$438A/$438C`, or
- falls back to live player position from `$9877/$987B`

Then it does:

- `LDA position_x`
- `LDX position_y`
- `JSL C00AA1`
- `AND #$0007`
- `STA $9887`

That is the shape of a positional map/cell classification, not a free-running animation state.

## What `C00AA1` is doing

`C00AA1` itself is tiny and table-driven.

It:

- takes the caller's `A` low byte and the high bits of `X`
- combines them into a lookup index
- reads a word from `D7:B200`
- returns that word to the caller

The first visible words in `D7:B200` look like packed classification values such as:

- `0082`
- `B008`
- `0080`
- `0089`

Only the low 3 bits are kept for `$9887`, which fits the idea that the returned word is a packed cell-behavior record rather than a dedicated one-byte enum.

## Why class `3` is special

The clearest special handling is around class `3`.

Immediately after setting `$9887`, the local setup does:

- `ASL`
- store to `$289A`
- `STZ $289C`
- if `$9887 == 3`, store `#$000A` to `$9883`
- otherwise clear `$9883`

Later visual setup paths branch directly on `$9887 == 3`.

Examples:

- In the `C03B06+` family, ordinary classes call `C0780F` with `X = #$0000`, but class `3` calls it with `X = #$000A`.
- In the `C04E73+` family, class `3` uses base offset `#$0008`, while ordinary classes use `#$000C` before combining with `DATA_C3E09A`.
- In `C0780F`, `$9887 == 3` shifts the bucket family from `0..3` into alternate buckets `4..7`.

That makes class `3` the strongest current marker for an alternate positional context family.

## Other special classes currently visible

`C0780F` also has small direct tests for:

- `$9887 == 4`
- `$9887 == 6`

Those lead to hard pose-index returns like `#$0006` and `#$0007`, and they also affect how the ordinary bucket logic is bypassed.

So the strongest current statement is:

- class `3` is the main alternate-bucket case
- classes `4` and `6` are smaller special context cases with direct pose overrides

I am still keeping the player-visible names for those classes open.

## Relationship to the visual selector rows

This now fits neatly with the newer `0E5E / 2C22 / C0780F / C3:F2B5` model.

The current layered read is:

- `$9887` = position-derived context class
- `0E5E / 2C22` = visual selector row id
- `C0780F` = resolver that combines the row id with the class-driven bucket family
- `C3:F2B5` = 8-entry-per-row pose resolution table
- `2AF6` = lower-level pose/frame selector inside the chosen row family

So `$9887` is not replacing the row selector. It is selecting which row column family is used.

## Why I am still keeping the name cautious

The evidence for "position-derived" is strong.
The evidence for "terrain/cell behavior" is plausible but not fully locked.

The remaining uncertainty is that the same class value may be encoding more than plain walkable terrain. It could also include special map-object or interaction-context categories, since the same position-derived value is used to influence visual and setup paths rather than only collision.

So the safest wording for now is:

- position-derived visual context class

## Best next target

The best next move is to pin what class values `3`, `4`, and `6` correspond to in gameplay terms. That should let us replace the structural wording with something like stair/ledge/door/water-style names if the local evidence supports it.

## Update: class `3` now looks doorway-related

The current best follow-up is in [class3-doorway-transition-context.md](notes/class3-doorway-transition-context.md).

The strongest new result is that class `3` is no longer just an abstract alternate bucket family. Its special branch seeds `$9883 = #$000A`, then runs through `C06A07 -> C068F4`, and `C068F4` explicitly consults `EB_DoorDestinationTable` before populating `$5DD6`. That makes class `3` look very likely to be a doorway or transition-cell context.

## Update: classes `4` and `6` now look like stair/escalator-family contexts

The remaining special non-door classes now have a better local interpretation too.

The most useful cross-check is the adjacent `5Dxx` WRAM block from `ebsrc`, which maps our local fields as:

- `$5DAA/$5DAC` = `LADDER_STAIRS_TILE_X / LADDER_STAIRS_TILE_Y`
- `$5DC6/$5DC8` = `STAIRS_DIRECTION / ESCALATOR_ENTRANCE_DIRECTION`
- `$5DCE/$5DD0` = `STAIRS_NEW_X / STAIRS_NEW_Y`
- `$5DD2/$5DD4` = `ESCALATOR_NEW_X / ESCALATOR_NEW_Y`

That matters because classes `4` and `6` are the only remaining special `$9887` surface buckets in `C0780F`, and the surrounding helper families already work directly from the same `5DAA/$5DAC` stair-like coordinate block.

The safest current read is now:

- `$9887 == 6` is the stronger candidate for a stairs-style surface class
- `$9887 == 4` is the stronger candidate for an escalator-entry-style surface class

I am still keeping that as an inference rather than a final label, but it is much stronger than the older â€œunidentified special terrain classâ€ wording.
