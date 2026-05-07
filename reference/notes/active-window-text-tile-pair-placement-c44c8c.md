# Active Window Text Tile Pair Placement (`C4:4C8C`)

This note names the text/window tilemap placement helper between the scratch-row renderer and the tile-transfer catch-up path.

See also [c4-early-ppu-and-text-tile-helpers-0000-0085.md](notes/c4-early-ppu-and-text-tile-helpers-0000-0085.md).
See also [text-token-glyph-run-stager-c44b3a-c44e61.md](notes/text-token-glyph-run-stager-c44b3a-c44e61.md).
See also [text-window-rendering-primitives-c1078d-c10d7c.md](notes/text-window-rendering-primitives-c1078d-c10d7c.md).

## Working Names

- `C4:4C8C` = `PlaceTextTilePairAtActiveCursor`

## Main result

`C4:4C8C` installs a two-tile text/glyph pair into the active window descriptor buffer at the current cursor.

The routine takes:

- `A` = first tile id or tile word low bits
- `X` = second tile id or tile word low bits

It resolves the active window descriptor through `$8958 -> $88E4 -> $8650`, reads the descriptor cursor fields, writes the first tile word at the current row/column, writes the second tile word one descriptor row below it, and then advances the cursor column.

## Descriptor fields used

The helper reads the active descriptor as:

- `+0A`: row width in columns
- `+0C`: row capacity in half-row units; this routine uses `+0C / 2`
- `+0E`: current cursor column
- `+10`: current cursor row
- `+13`: tile attribute bits added to ordinary tile ids
- `+35`: base pointer for the descriptor tile word buffer

So the descriptor buffer offset is:

`descriptor[+35] + ((row * descriptor[+0A]) + column) * 2`

The second tile lands at the same column one row below the first by adding `descriptor[+0A] * 2` to the first tile-word address.

## Wrap and scroll behavior

If cursor column `+0E` has reached descriptor width `+0A`, the routine wraps the column back to `0`.

If there is still row capacity, it increments descriptor row `+10`. If the cursor is already on the last available row, it either exits early when `$7E:B49D` is nonzero or calls `C1:0CAF` with the active focus id, which matches the existing scroll/line-advance family.

When `$5E6E` is set during a wrap, it also sets `$5E75 = 1`. This lines up with the parser-side wrap-preflight notes where `$5E75` suppresses or records a just-handled text-control advance.

## Tile replacement behavior

Before writing either tile word, `C4:4C8C` checks the destination word. If it is nonzero, it calls `C4:4E4D` / `ReleaseNonBlankTextTileWord` so any previously claimed dynamic tile slot is released before being overwritten.

Then it writes:

- first destination: attribute bits plus incoming `A`
- second destination: attribute bits plus incoming `X`

There is one special visible-character case: input `#$0022` uses attribute base `#$0C00` instead of descriptor field `+13`. Ordinary inputs use descriptor field `+13`.

## Caller fit

The two direct callers explain the helper's position in the renderer stack:

- `C4:4DCA` / `CatchUpTextTileStripTransfers` allocates two dynamic text tile slots with `C4:0085`, submits the corresponding scratch-row transfers with `C4:002F`, then calls `C4:4C8C` to install those two tile ids into the active descriptor tilemap.
- `C4:447A`, inside the text-input option renderer, also calls this helper after building tile ids for the option strip.

So `C4:002F` is the transfer side, while `C4:4C8C` is the descriptor tilemap placement side.

## Practical conclusion

The safest current name is `PlaceTextTilePairAtActiveCursor`.

This closes the local `C4:4C8C..4E44` cluster:

- `C4:4C8C` = place a two-tile text/glyph pair in the active window buffer
- `C4:4DCA` = catch up pending dynamic tile transfers and place their tile pairs
- `C4:4E44` = clear the glyph-variant offset mirrors

The remaining fuzz is mostly user-facing vocabulary around `$5E75`, `$5E6E`, and `$964D`; the byte-level tile placement contract is clear.
