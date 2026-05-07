# Overworld Sprite Pointer Flag Semantics

This note captures the current local read of the low bits in the `spritepointerarray` words inside the EF sprite grouping records.

The frame contract now resolves every runtime slot to a D1-D5 sprite payload by masking the low two bits of each pointer word. Those low bits are not disposable alignment noise: C0-side consumers preserve the raw word in `$341A` and branch on its low bits before building renderer/DMA records.

## Evidence

- `C0:A4C4` and `C0:A794` both load the selected frame word from the cached `2A06/29CA` descriptor stream and test `AND #$0002`.
- When bit 1 is set, both paths skip the optional fixed-source auxiliary pass rooted at `C4:0BE8` and continue to the main D1-D5 sprite payload stream.
- `C0:A3A4` later reads cached `$341A`, tests `AND #$0001`, and if set adds `$2916` to the display-record base pointer in `$8C` before queue submission.
- `C0:1E49` initializes `$2916` as descriptor piece count multiplied by `10`, exactly one secondary visual descriptor body-pass span. That makes bit 0 a pass selector for the second, horizontally flipped record pass rather than a vague address bias.
- The selected word is also masked for source addressing before DMA descriptor generation, so the renderer consumes the aligned payload offset and the low-bit behavior separately.

## Current Names

| Bit | Name | Confidence | Meaning |
| ---: | --- | --- | --- |
| 0 | `select_flipped_piece_record_pass` | high | Adds the per-visual-profile `$2916` span to the display-record base pointer, selecting secondary descriptor pass 1, the horizontally flipped piece-record pass. |
| 1 | `suppress_auxiliary_c40be8_prepass` | high | Skips the optional `C4:0BE8` auxiliary render/DMA prepass and uses only the main D1-D5 payload stream for that slot. |

## Contract Counts

The generated frame contract currently reports:

- flag value `0`: `1769` slots
- flag value `1`: `653` slots
- flag value `2`: `12` slots
- flag value `3`: `4` slots

Interpreted as bit effects:

- `select_flipped_piece_record_pass`: `657` slots
- `suppress_auxiliary_c40be8_prepass`: `16` slots

## Boundaries

These names describe observed renderer behavior, not yet final art-facing terminology. Bit 0 is now tied to the secondary descriptor pass-1 record span, but a later art-facing name may still phrase that as a mirrored, horizontal, or right-facing selector depending on how the direction slots shake out. Bit 1 is firm because both relevant refresh paths branch directly on it before the auxiliary `C4:0BE8` pass.

## Preview Tool

`tools/build_overworld_sprite_preview_sheets.py` now consumes `notes/overworld-sprite-frame-contracts.json` and generated palette-00 tile previews to produce ignored slot contact sheets under `build/overworld-sprite-preview-sheets/`.

Those sheets apply the flag effects as metadata and colored cell borders first. They are not final in-game OAM composition yet; they are a visual QA layer over the exact slot-to-payload mapping.

`tools/build_overworld_sprite_composed_previews.py` is the next prototype layer. It consumes the frame contract, the secondary visual descriptor contract, raw D1-D5 graphics, and the ROM-backed overworld sprite palettes to write ignored composed preview sheets under `build/overworld-sprite-composed-previews/`. It uses bit 0 to choose descriptor pass 0 or pass 1 and records that choice per slot.

The composed preview tool now builds each secondary descriptor piece as a 16x16 chunk from the extracted D1-D5 tile stream. Sprite grouping header byte +3 is preserved as the base OAM attribute byte; the previewer decodes its palette bits as `(byte >> 1) & 7` and uses that palette by default. It can also force palette 0 or a specific palette ID for audit comparisons, tint the contract priority bands, and outline pieces whose trailing byte carries the pass-terminal marker.

## Next Step

Use the composed preview metadata to keep tightening art-facing direction and phase names against movement/controller code.
