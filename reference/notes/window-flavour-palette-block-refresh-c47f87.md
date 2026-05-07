# Window Flavour Palette Block Refresh (`C4:7F87`)

This note pins down the small high-fanout helper at `C4:7F87`.

See also [file-select-window-flavour-refresh-c1ec8f-ecd1.md](notes/file-select-window-flavour-refresh-c1ec8f-ecd1.md), [file-select-tail-helpers-c1ff2c-ff6b-ff99.md](notes/file-select-tail-helpers-c1ff2c-ff6b-ff99.md), [equipment-menu-display-fringe-c19a11-c19f29.md](notes/equipment-menu-display-fringe-c19a11-c19f29.md), and [saved-landing-display-stage-c4c2de-c4c64d.md](notes/saved-landing-display-stage-c4c2de-c4c64d.md).

## Main result

`C4:7F87` refreshes the 0x40-byte palette work block at `$0200` for the current text-window flavour, then marks display dirty byte `$0030` with selector `#$08` through `C0:856B`.

Most callers surround it with the already-mapped text/window redraw helpers:

- `C4:7C3F`
- `C4:4963`, locally named `RefreshTextWindowVramPlanesForMode`
- often an outer `$0030 = #$18` refresh marker after `C4:7F87` returns

That makes this helper the palette-side sibling of the C4 text-window tile/plane refresh path, not another parser or menu controller.

## Source selection

The normal path uses `$99CD`, the current window-flavour byte:

- computes `($99CD & 0xFF) - 1`
- multiplies by three
- reads a word offset from `E0:1FB9 + flavour_index * 3`
- adds the offset to base `E0:1FC8`
- copies 0x40 bytes from that source to `$0200` through `C0:8ED2`
- clears `$0200`
- calls `C0:856B(#$08)`

The same `E0:1FB9/E0:1FC8` family was already seen from `C1:9D49`, which copies an eight-byte slice into `$0218` for equipment/status display prep. Here the copied block is larger and starts at `$0200`, so this is the broader window-flavour palette block refresh.

## Lead-entity override

Before using `$99CD`, `C4:7F87` checks the current lead entity type:

- reads active slot count / selected lead index from `$98A4`
- maps through `$9891`
- indexes the object pointer table at `$4DC8`
- reads object-record byte `+0x0E`

If that object-record byte is `1` or `2` and `$B4B6 == 0`, it copies the fixed 0x40-byte block at `E0:2108` instead of the `$99CD`-selected flavour block.

This lines up with `C1:FF2C`, which watches the same object-record byte and stores a latched changed/not-changed state in `$B4A2`; its caller refreshes through `C4:7F87` when that state changes. The special source block is therefore an overworld lead-entity palette/window override, while `$B4B6` suppresses it during file-select/session handling.

## Extra block status

The seven-block E0 palette span also contains `E0:2148`, the block rendered by EBDecomp's `WindowGraphics/Windows1_6.png` and `Windows2_6.png` references. No checked-in source-backed path currently selects that address directly: the known retail refresh helper selects only blocks 0..4 through `$99CD`/`E0:1FB9`, or the fixed block 5 override at `E0:2108`.

Until a caller proves a narrower role, block 6 should be treated as a preserved unused/nonselectable extra system window block rather than one of the five user-selectable flavors.

## Caller shape

Direct callers found locally:

- `C0:0A25`, in a display refresh path that also copies the `$0200`-adjacent palette work region to `$4476`
- `C0:3695`, after rebuilding/exporting the active mushroomized-walking controller
- `C0:B70A`, during file-select/session return and overworld display rebuild
- `C1:ECBB`, inside `PreviewWindowFlavourAndRedraw`
- `C1:FF2C`'s caller at `C1:2E30`, when lead entity type changes
- `C2:4A3A`, after battle/scene visual refresh helpers and before setting `$9643`
- `C4:8029`, the local full text-window/display setup wrapper
- `C4:AD30`, during a larger decompression/display initialization path
- `C4:C42E`, during saved landing display setup
- `C4:E47C`, during a late display setup path after decompressed VRAM work
- `EF:D98B` / `EF:DA00`, in EF display setup wrappers that either run the same refresh or delegate to a larger EF branch

The callers are broad, but they agree on one contract: after text/window VRAM state is set up, `C4:7F87` refreshes the palette-side `$0200` block for the current visible window context.

## Working Name

- `C4:7F87` = `RefreshWindowFlavourPaletteBlock`

## Still open

- exact palette subfields inside the 0x40-byte `$0200` work block
- whether object-record byte `+0x0E` should be globally named as a lead sprite class, body type, or a narrower overworld render class
