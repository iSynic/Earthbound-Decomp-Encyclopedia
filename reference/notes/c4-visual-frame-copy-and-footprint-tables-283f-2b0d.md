# C4 Visual Frame Copy And Footprint Tables `C4:283F-C4:2B0D`

## Scope

This note covers the C4 run immediately after the window/color helpers and the small event data block. The reference include order marks `C4:283F`, `C4:2884`, `C4:28D1`, `C4:28FC`, `C4:2955`, `C4:2965`, `C4:29AE`, `C4:29E8`, and the data tables through `C4:2B0D`.

The important local connection is that this run is not an isolated data island. It sits directly on top of the already-mapped sprite-pose descriptor cache:

- `$2A06/29CA` = pose descriptor frame-list pointer
- `$2A42` = final frame-record data bank
- `$2A7E` = frame-record stride
- `$2ABA` = per-frame piece count
- `$2AF6` = lower-level pose/frame selector

Those fields are documented in the sprite-pose cache notes; the routines here are C4-side consumers and helpers for copying visual frame words, masked tile columns, and footprint geometry tables.

## Frame word copy helpers

`C4:283F` builds a source pointer from the cached pose descriptor state:

- uses caller A as a slot/profile index
- reads source bank from `$2A06,index`
- reads the current selector from `$2AF6,index`
- indexes `C0:A623` (`VisualProfileSecondaryOffsetTable`)
- combines that offset with `$29CA,index` and `$10F2,index`
- follows the selected frame pointer, masking the low nibble with `#$FFF0`
- then copies a caller-sized word span into a `7F:` destination pointer supplied in X/Y

`C4:2884` is the sibling that uses `C0:A60B` (`VisualProfileDirectionOffsetTable`) and advances the cached `$29CA,index` pointer by four bytes per selected direction offset before copying the same kind of word span.

The safest distinction is:

- `C4:283F` selects the secondary visual-profile frame stream.
- `C4:2884` selects the direction-facing visual-profile frame stream.

Both routines copy from the final frame data bank cached in `$2A42,index` into a `7F:` destination buffer.

## Strided and masked 7F copy helpers

`C4:28D1` is a strided 7F-to-7F word copier. It takes source and destination long pointers rooted in bank `7F`, copies words at the current Y offset, then advances Y by `#$10` for each iteration. The loop count is derived from direct-page `$16`.

`C4:28FC` is a row-oriented masked merge helper. It:

- chooses one of eight bit-pair masks from `C4:2955`
- derives the complementary mask with `EOR #$FFFF`
- uses `(Y & #$FFF8) << 2` as the starting row/column offset
- loops over 16 words per row
- takes masked bits from the source and preserves the complementary bits already in the destination
- advances rows by the stride in direct-page `$20`
- repeats for `($1E >> 3)` rows

`C4:2965` is the tiny two-position sibling of that merge path. It chooses a mask through direct-page `$1C`, merges one word at Y, then repeats at `Y + #$10`.

The mask table at `C4:2955` is the eight-entry word-pair mask ladder:

```text
8080, 4040, 2020, 1010, 0808, 0404, 0202, 0101
```

That strongly reads as a bitplane/tile-column merge mask table.

Source polish: `src/c4/visual_frame_copy_helpers.asm` now names the
directional frame-list entry stride, tile-column mask index, row-offset mask,
mask complement word, and zero high-source field used when emitting visual
profile render strip descriptors.

2026-05-06 source polish: the same helper source now documents the caller
inputs and side effects for the secondary/directional frame-word copiers, the
`C0:A56E` render-strip wrapper, and the `$212C` main-screen-layer HDMA starter.
The comments keep ownership narrow: C4 consumes cached sprite-pose descriptor
fields and toggles the `$001F` HDMA enable shadow, while C0 owns descriptor
queueing and broader renderer state.

## Render descriptor and HDMA helpers

`C4:29AE` is a C4 wrapper around `C0:A56E` (`Generate_RenderDmaStripDescriptors`). It takes the caller's initial source in A and a slot/profile selector in X, then:

- loads per-frame piece count from `$2ABA,index`
- loads frame-record stride from `$2A7E,index`
- loads frame data bank from `$2A42,index`
- repeatedly calls `C0:A56E`
- advances the source pointer by the frame-record stride between calls

This is the C4-local "emit the render strips for each piece in this visual profile" wrapper.

`C4:29E8` configures a selected HDMA channel for `TM` / main-screen layer selection (`$212C`) using a fixed source at `7E:ADB8`, HDMA mode `#$01`, and the channel enable bit from `C0:AE16`. This is a compact main-screen layer HDMA starter rather than a general DMA helper.

## Footprint and descriptor tables

The data tables from `C4:2A1F` onward are already cross-referenced by the collision, pathfinding, and secondary visual descriptor notes. This pass promotes their C4 names together:

- `C4:2A1F` and `C4:2A41` are footprint X/Y offset tables used when collision and pathfinding convert entity positions into probe anchors.
- `C4:2A63` and `C4:2A85` are 17-entry pixel-size tables. Their values are width/height-like dimensions in multiples of eight or related sprite/footprint spans.
- `C4:2AA7` and `C4:2AC9` are tile-span count tables used by horizontal and vertical edge collision probes.
- `C4:2AEB` is another footprint anchor/offset table used with the first two geometry tables by full-footprint and half-footprint probes.
- `C4:2B0D` is the pointer table for the secondary visual descriptor records documented separately.

2026-05-06 table polish: `src/c4/entity_footprint_visual_profile_tables.asm`
now splits the former raw byte corridor into labeled footprint geometry tables,
the 17-entry secondary visual descriptor pointer table, named descriptor rows,
the adjacent preserved `C4:2F45..2F65` callback byte island, map-tile chunk
pointers, and the two visual tile-word ladders. The descriptor labels follow
the generated secondary-visual descriptor contract note and remain C4-local.

2026-05-06 equipment comparison row follow-up:
`src/c4/party_equipment_comparison_visual_state_rows.asm` now marks the
equipment-comparison visual row packing at `$98C9/$98CB`, the six slot bytes
per row, the candidate source base, party-record stride/base, clamp limit, and
the three packed flag bits (`$20/$40/$80`). This is a local presentation-row
contract only; it does not promote the descriptor bytes at record offsets
`+$0E/+$0F` to global field names.

## Working Names

- `C4:283F` = `CopySecondaryVisualProfileFrameWords`
- `C4:2884` = `CopyDirectionalVisualProfileFrameWords`
- `C4:28D1` = `Copy7fWordsEvery16ByCount`
- `C4:28FC` = `MergeMasked7fTileColumnRows`
- `C4:2955` = `TileColumnWordPairMaskTable`
- `C4:2965` = `MergeMasked7fTileColumnPair`
- `C4:29AE` = `GenerateVisualProfileRenderDmaStrips`
- `C4:29E8` = `StartMainScreenLayerHdmaFromAdb8`
- `C4:2A1F` = `EntityFootprintXOffsetTable`
- `C4:2A41` = `EntityFootprintYOffsetTable`
- `C4:2A63` = `EntityFootprintPixelWidthTable`
- `C4:2A85` = `EntityFootprintPixelHeightTable`
- `C4:2AA7` = `EntityFootprintTileWidthTable`
- `C4:2AC9` = `EntityFootprintTileHeightTable`
- `C4:2AEB` = `EntityFootprintAnchorOffsetTable`
- `C4:2B0D` = `SecondaryVisualDescriptorPointerTable`

## Confidence boundaries

### Locally proved

- `C4:283F` and `C4:2884` consume the cached sprite-pose descriptor fields and copy frame words into `7F:` buffers
- `C4:28FC` and `C4:2965` merge source and destination words through the `8080..0101` mask ladder
- `C4:29AE` wraps `C0:A56E` with `$2ABA/$2A7E/$2A42` as count, stride, and bank
- `C4:29E8` configures HDMA for `$212C` from `7E:ADB8`
- `C4:2AA7/2AC9` are tile-span count tables used by movement collision probes
- `C4:2B0D` points at the secondary visual descriptor family

### Still open

- exact visual names for the two frame-word copy variants
- exact field names for the `C4:2A63/2A85` pixel-size pair beyond width/height-like behavior
- whether `C4:28FC` is best named as tile-column, bitplane-column, or mask-column once its concrete caller-side visual effect is pinned
