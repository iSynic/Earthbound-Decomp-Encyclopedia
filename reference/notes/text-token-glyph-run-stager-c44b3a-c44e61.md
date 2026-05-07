# Text Token Glyph Run Stager (`C4:4B3A` and `C4:4E61`)

This note promotes the text-token glyph staging path that had already appeared in the text/window and reflected-hit notes but did not yet have a bank-`C4` working name.

See also [text-window-rendering-primitives-c1078d-c10d7c.md](notes/text-window-rendering-primitives-c1078d-c10d7c.md), [text-input-dialog-option-helpers-c1e48d-c1e4be.md](notes/text-input-dialog-option-helpers-c1e48d-c1e4be.md), and [class2-reflected-hit-side-token-consumers.md](notes/class2-reflected-hit-side-token-consumers.md).

## Main result

`C4:4E61` stages one text token/glyph from the `0x50..0x7F` text-token family into the active text/window glyph scratch stream. It records the incoming token in `$5E76`, resolves width/source metadata through the `C3:F054` table family, and delegates the actual pixel/run merge to `C4:4B3A`.

`C4:4B3A` is the lower scratch-row renderer. It consumes a glyph source pointer, byte count, and pixel width, merges the source into the `$3492` glyph scratch rows using bit masks, and advances the global bit cursor at `$9E23/$9E25`.

Together these routines are the renderer-facing side of text-token handling. They are not battle mechanics, even though battle text uses them heavily.

## `C4:4E61`: token-to-glyph-run stager

Inputs observed locally:

- `A` = metadata set / table selector, often active descriptor field `$8665` or zero in name-entry builders
- `X` / `Y` = incoming text token or glyph code

The routine returns early if no active focus is set (`$8958 == FFFF`).

It special-cases a few visible/control tokens:

- `#$002F`
- `#$0022`
- `#$0020`

Those are printed through `C4:3F77` and then advance the animated glyph tile-state offset through `C4:3CAA`.

For the ordinary `0x50..0x7F` family it:

- resolves the active window descriptor from `$8958 -> $88E4 -> $8650`
- uses `$5E75` as a suppression/line-advance flag around token `#$0050`
- stores the incoming token byte in `$5E76`
- computes `(token - #$50) & #$7F`
- selects metadata from `C3:F054 + selector * 12`
- resolves a glyph source pointer and per-token width/length byte
- adds global spacing byte `$5E6D`
- sends 8-pixel chunks through `C4:4B3A`
- flushes the final remaining chunk through `C4:4B3A`
- calls `C4:4DCA` after the final chunk

This is why reflected-hit/article notes were able to treat `$5E76 == #$0070` as meaningful text-control context: `C4:4E61` is the routine that records the last token from this formatter family.

## `C4:4B3A`: scratch-row renderer

`C4:4B3A` is the lower row writer used by `C4:4E61` and the text-input rendering path.

Its contract is mechanical:

- caller `A` is the run width in pixels/bits
- caller `X` is the number of source bytes to merge
- caller source pointer comes from the shifted direct-page pair that lands in local `$0A/$0C`
- current bit offset comes from `$9E23`
- current scratch row comes from `$9E25`
- destination rows are rooted at `$3492 + $9E25 * #$20`

When the current bit offset is byte-aligned, it first clears the destination span through `C0:8EFC`. Then it walks the source bytes and merges them into the odd bytes of the destination row using the mask table at `EF:C51B`.

After advancing `$9E23` by the run width, it updates `$9E25` from `$9E23 >> 3`. If the run crosses into a new scratch row, it clears that next row and writes the carry portion using the companion mask table at `EF:CD1B`.

Source polish: `src/c4/text_token_glyph_scratch_renderer.asm` now names the
`$3492` active text glyph scratch row base, `$9E23/$9E25` bit/row cursors,
the `#$01A0` cursor wrap, byte-alignment mask, clear-fill byte, and the
`EF:C51B` / `EF:CD1B` merge-mask roles.

This is the `$3492` sibling of the already-documented `$9D23` menu scratch renderer `C4:5C90`. The shared theme is bit-aligned glyph-plane composition, but `C4:4B3A` is the active text-token path.

## Direct callers

`C4:4E61` is called from:

- `C1:0CE4`, the print-visible-letter side-effect path
- `C4:4127`, inside `BuildTextInputStringGlyphMetrics`
- `C4:4163`, `C4:419A`, `C4:41F3`, and `C4:4238`, while initializing or padding text-input option glyph metrics

`C4:4B3A` has more callers, but the key local one for this seam is `C4:4E61`; the other callers sit in nearby text-input/menu rendering paths and use the same scratch-row contract.

## Working Names

- `C4:4B3A` = `RenderTextTokenGlyphRunToScratchRows`
- `C4:4C8C` = `PlaceTextTilePairAtActiveCursor`
- `C4:4E61` = `StageTextTokenGlyphRunForActiveWindow`

## Still open

- final names for the fields inside each 12-byte `C3:F054` metadata row
- exact player-visible meaning of every special token in the `0x50..0x7F` family
- finer vocabulary for `$5E75/$5E6E` wrap-suppression state
