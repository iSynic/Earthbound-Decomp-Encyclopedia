# Window Title Glyph Upload (`C4:44FB`)

This note names the bank-`C4` helper called by the C2 window-title registration path.

See also [c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md](notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md).
See also [text-token-glyph-run-stager-c44b3a-c44e61.md](notes/text-token-glyph-run-stager-c44b3a-c44e61.md).
See also [text-window-rendering-primitives-c1078d-c10d7c.md](notes/text-window-rendering-primitives-c1078d-c10d7c.md).

## Working Names

- `C4:44FB` = `UploadWindowTitleGlyphTiles`

## Main result

`C4:44FB` is the renderer/uploader behind registered window-title strings.

The only direct caller is `C2:0325`, inside `C2:02AC` / `RegisterAndUploadWindowTitleBuffer`. That caller passes:

- `A = window descriptor + 0x3C`, the title/source byte string
- `X = $7700 + (registered_slot - 1) * 0x80`, the title tile upload destination

`C4:44FB` then compiles the source bytes into the shared `$3492` glyph scratch rows and queues one transfer per produced title glyph through `C0:8616`.

## First pass: build glyph scratch rows

The helper first saves the destination in `$1A` and the source pointer in `$02`, then calls `C4:3CAA` / `AdvanceAnimatedGlyphTileStateOffset`.

It reads text-token metadata from the `C3:F054` family:

- table word `+2C` becomes the stride/scale used to find glyph bytes
- table word `+2E` becomes the byte count passed to `C4:4B3A`
- width `6` is used as the glyph advance

Then it walks the nul-terminated source title bytes. For each nonzero byte, it normalizes the token as `(byte - 0x50) & 0x7F`, derives the glyph source pointer from the `C3:F07C/F07E` table base plus the metadata stride, and calls `C4:4B3A` / `RenderTextTokenGlyphRunToScratchRows`.

So this pass does not queue VRAM transfers yet. It materializes the title glyphs into the same animated/variant scratch-row system used by nearby text-token rendering.

## Second pass: queue title tile transfers

After the glyph rows are built, the routine restores the saved starting `$9E25` value and walks the same nul-terminated source string again.

For each produced glyph, it:

- computes the scratch-row source as `$3492 + tile_state_index * 0x20`
- sets `A=0`, `X=0x10`, and `Y=$1A`
- calls `C0:8616` / `QueueVramTransfer_FromDpSource`
- advances the destination by `8`
- advances the tile-state index, wrapping from `0x33` back to `0`

The `X=0x10` transfer size matches one 16-byte tile-plane chunk from the scratch row, while the destination stride of `8` matches the compact title-tile placement used by the window-title slot.

## Why this is window-title specific

The C2 caller gives the strongest context. `C2:02AC` maps a window id to the `$8650` descriptor table, allocates a small slot in `$894E`, records the 1-based slot in descriptor byte `+3B`, and calls this helper with descriptor field `+3C` as the source.

`C2:032B` writes a capped nul-terminated title string into the descriptor region beginning at `$868C + offset`, then immediately calls `C2:02AC`. That makes the `+3C` source exactly the registered title/name buffer for the window.

## Practical conclusion

The safest current name is `UploadWindowTitleGlyphTiles`.

This closes the remaining unnamed start between the text-input option renderer at `C4:42AC` and the parser wrap preflight helper at `C4:45E1`: `C4:44FB` is not a text command parser, but the window-title glyph materialization and transfer helper used by C2's registered title slots.
