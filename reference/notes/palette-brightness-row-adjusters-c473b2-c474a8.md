# Palette Brightness Row Adjusters (`C4:73B2..C4:74A8`)

This note covers the compact C4 palette-adjustment band immediately before the already documented `C4:7501..7B77` window-mask/indexed graphics helpers.

See also [c4-window-color-math-and-palette-helpers-23dc-26ed.md](notes/c4-window-color-math-and-palette-helpers-23dc-26ed.md) and [landing-palette-interpolation-export-c4958e-c426ed.md](notes/landing-palette-interpolation-export-c4958e-c426ed.md).

## Main result

This range is a palette brightness/tint adapter family. It has two related outputs:

1. `C4:73D0 / C4:746B / C4:7499` adjust packed 15-bit palette rows into the CGRAM shadow/work area and then schedule a palette upload through `$0030 = #$18`.
2. `C4:74A8` converts a signed per-slot value into the full-screen fixed-color math preset at `C4:249A`.

The field read by the public wrappers is `$0E5E[$1A42]`. The wider visual-selector notes already tie `$1A42` to the current entity slot and `$0E5E` to the per-slot visual context/row family, but this cluster uses that word specifically as a signed brightness or fixed-color magnitude.

## 2026-05-06 source polish

`src/c4/battlebg_load_and_palette_brightness_helpers.asm` now carries a local
contract block for the movement-script battle-background loader and the palette
brightness adapters. `LOAD_BACKGROUND_ANIMATION` is documented as a C4 caller
for the display bracket, BG mode/base queue, and C2 presentation sprite-resource
load. The note intentionally stops at the arguments C4 writes: C0 owns the
display/PPU queue internals, and C2 owns the battle-background resource state.

The palette helpers now name the local row buffers and upload selector in
source: rows are read from `$4476 + row*0x20`, adjusted into `$0240`, and the
batch wrapper writes `$0030 = #$18`. `C4:7499` and `C4:74A8` both read
`$0E5E[current]`, but the source comments keep that meaning local to this effect
family as a signed palette brightness or fixed-color magnitude. `C4:74A8`
passes only the derived magnitude and mode (`#$33` or `#$B3`) to `C4:249A`; the
lower-level fixed-color register choreography remains documented with the C4
window/color helper.

2026-05-06 follow-up source polish: the source now uses the local constants in
the helper bodies as well as the contract block. The battle-background loader
names the BG mode/base queue arguments and the C2 sprite-resource `Y = 4`
argument; the palette path names the signed-negative clamp boundary, 5-bit
component masks, row count, saved-row/work-row bases, full-CGRAM upload
selector, current-slot signed magnitude table, and fixed-color math mode values.
This keeps C4's side of the contract at argument staging and row transformation.

2026-05-06 selector/latch follow-up: the source now splits selector `#$18` from
the `$0030` display-selector latch in the full-row batch wrapper. C4's local
side effect is the adjusted `$0240` row block plus the latch write; C0/NMI owns
the actual CGRAM upload interpretation.

## Component clamp

`C4:73B2` is the shared 5-bit component clamp.

It treats values above the signed negative boundary as underflow and returns `0`, clamps values above `31` to `31`, and otherwise returns `A & #$001F`.

That makes its local purpose clear: clamp a signed-adjusted SNES color component into the valid `0..31` range.

## Palette-row adjustment

`C4:73D0` adjusts one 16-color palette row.

Inputs:

- `A` = row index
- `X` = signed component offset

Local behavior:

- computes source offset `row * 0x20 + $4476`
- computes destination offset `row * 0x20 + $0240`
- loops over 16 packed SNES color words
- extracts low, middle, and high 5-bit components
- adds the same signed offset to each component
- clamps each component through `C4:73B2`
- repacks the adjusted components into one 15-bit color word at the destination row

The source/destination operands are low WRAM offsets under the usual engine data-bank setup, matching the nearby palette-work notes that describe `$0200/$0240` as CGRAM shadow/upload work areas.

## Full row batch

`C4:746B` is the 16-row batch wrapper.

It takes the caller's signed component offset in `A`, then calls `C4:73D0` for rows `0..15`. After all rows have been adjusted, it writes selector `#$18` into the `$0030` display-selector latch, the same selector value used by the palette interpolation/export family for CGRAM refresh. The NMI-side upload behavior stays outside this C4 contract.

`C4:7499` is the current-slot wrapper. It reads `$0E5E[$1A42]` and passes that signed value to `C4:746B`. No direct JSL/JSR caller was found in the split-bank scan, so it may be reached through a table or pointer path.

## Fixed-color math wrapper

`C4:74A8` reads the same `$0E5E[$1A42]` word, turns its absolute value into caller `X`, chooses a color math mode from the sign, and calls `C4:249A`.

- nonnegative values select `CGADSUB = #$33`
- negative values select `CGADSUB = #$B3`
- `X = abs($0E5E[$1A42])` becomes the fixed-color magnitude consumed by `C4:249A`

Direct callers at `C3:F596` and `EF:0585` reach this after clearing `$9641`; both then call `C0:927C`, locally named `Init_DelayedActionPools`. The caller context suggests this is a visual transition cleanup or restore path, but the local C4 behavior is more safely named as a signed fixed-color-math application.

## Working Names

- `C4:73B2` = `ClampSignedPaletteComponentTo5Bit`
- `C4:73D0` = `ApplySignedBrightnessOffsetToPaletteRow`
- `C4:746B` = `ApplySignedBrightnessOffsetToPaletteRowsAndUpload`
- `C4:7499` = `ApplyCurrentSlot0e5eBrightnessToPaletteRows`
- `C4:74A8` = `ApplyCurrentSlot0e5eFixedColorMath`

## Still open

- the human-facing meaning of the signed `$0E5E[$1A42]` values in this effect path
- whether `C4:7499` is pointer-dispatched or currently orphaned in the split-bank direct-call scan
- the exact transition/event name for the `C3:F596` and `EF:0585` callers of `C4:74A8`
