# C4 Window Color Math And Palette Helpers `C4:23DC-C4:26ED`

## Scope

This note promotes the compact C4 helper run between the `earthBound` logo scripts and the next event-script block. The reference order marks these as `unknown/C4/C423DC.asm` through `unknown/C4/C426ED.asm`, but the byte patterns are not opaque: this run is mostly direct PPU window/color-math setup, HDMA setup for window edge registers, a screen-position interpolation helper, and the already-correlated palette interpolation export routine.

The surrounding evidence comes from:

- legacy labels in `refs/earthbound-disasm-legacy/Earthbound Decomp/EB/Routine_Macros_EB.asm`
- ebsrc bank04 include order in `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank04.asm`
- the existing landing palette note for the `7F:0200..0C00` color-work planes
- the C0 frontier note that identifies the nearby `C0:B400/C0:B40B` pair as sine/cosine-family helpers

## Window and color math presets

`C4:23DC` and `C4:240A` are small register presets for the color window range and color-window math state.

- `C4:23DC` writes `WH0/WH2 = #$80`, `WH1/WH3 = #$7F`, `CGWSEL = #$10`, `TMW = #$13`, and clears `WBGLOG/WOBJLOG`.
- `C4:240A` writes `WH0/WH2 = #$00`, `WH1/WH3 = #$FF`, `CGWSEL = #$20`, `TMW = #$13`, and clears `WBGLOG/WOBJLOG`.

So the safe local read is:

- `C4:23DC` selects the centered/inverted color-window range used by effects that want the window edge pair crossed over.
- `C4:240A` selects the full-screen color-window range.

`C4:2439` writes caller A to `CGADSUB` and then writes the fixed color from `$9E37-$9E39` into `COLDATA`, ORing the three bytes with the blue/green/red selector bits. This is the C4-side equivalent of the direct fixed-color helper family noted in the C0 PPU frontier.

Source polish: `src/c4/window_color_hdma_helpers.asm` now names the
`COLDATA` red/green/blue selector bits and the WOBJSEL clear value used by
the channel-4 teardown helper.

2026-05-06 source polish: the same source module now documents the direct PPU
side effects for the color-window presets and the WH0/WH2 HDMA setup/teardown
helpers. The comments intentionally stop at register writes and `$001F` HDMA
enable-shadow bits; C4 does not claim the broader C0 renderer bracket semantics
for these small entries.

`C4:249A`, `C4:24D1`, `C4:2509`, and `C4:258C` are larger one-shot presets:

- `C4:249A` takes caller A as `CGADSUB`, uses a full-screen `WH0/WH1` range, enables the object/color window through `WOBJSEL = #$20`, and writes fixed color from caller X ORed with `#$E0`.
- `C4:24D1` uses the centered/crossed `WH0/WH1` range, `CGWSEL = #$20`, `CGADSUB = #$B3`, and `COLDATA = #$EF`.
- `C4:2509` is the full-screen `WH0/WH1` version of that subtract/half-style preset and uses `COLDATA = #$FF`.
- `C4:258C` applies the same subtract/half-style preset with both window pairs set to the centered/crossed range and `WOBJSEL = #$A0`.

`C4:2569` and `C4:2574` are tiny mode setters for `CGADSUB = #$33` and `CGADSUB = #$B3`.

## Window HDMA helpers

The HDMA helpers in this run program B-bus targets for the window edge registers:

- `C4:245D` programs DMA channel 4 as HDMA mode `#$01`, B-bus target register `#$26` (`WH0`), table bank and indirect data bank from caller A, table address from caller X, writes `WOBJSEL = #$A0`, then sets bit `#$10` in `$001F`.
- `C4:2542` programs the same channel-4 `WH0` HDMA setup but does not touch `WOBJSEL`.
- `C4:25CC` is another channel-4 `WH0` setup entry with the same register shape as `C4:2542`; the callsite semantics are still open, so it keeps a distinct working name for now.
- `C4:25FD` programs DMA channel 5 as HDMA mode `#$01`, B-bus target register `#$28` (`WH2`), table bank and indirect data bank from caller A, table address from caller X, then sets bit `#$20` in `$001F`.

2026-05-06 HDMA register-name follow-up: `window_color_hdma_helpers.asm` now
splits the channel-4/channel-5 DMA register aliases into HDMA mode, B-bus
target, table address, table bank, and indirect-bank fields. The entry comments
now say caller A is written to both bank fields and caller X to the table
address, without assigning semantics to the stream payload bytes themselves.

The disable helpers are similarly small:

- `C4:248A` clears channel-4's `$001F` bit with `TRB #$10` and also clears `WOBJSEL`.
- `C4:257F` clears channel-4's `$001F` bit through load/AND/store.
- `C4:25F3` clears channel-4's `$001F` bit through `TRB #$10`.
- `C4:2624` clears channel-5's `$001F` bit through load/AND/store.

This ties the cluster directly to the C0-side window DMA frontier: C0 contains the generic streamed/generated window-position DMA helpers, while this C4 run contains hardwired effect presets for C4 callers.

## Screen position interpolation

`C4:2631` initializes a small fixed-point screen-position interpolation state at `$3C22-$3C30`.

It clears the fractional delta words, offsets caller X by `#$80`, calls the C0 sine/cosine-family helpers with caller A and the adjusted angle, sign-extends their low-byte outputs into high words, seeds the current screen origin from `$0031/$0033`, and clears the fractional accumulators at `$3C2A/$3C2E`.

`C4:268A` advances that state:

- adds `$3C22/$3C24` into `$3C2A/$3C2C`
- writes the resulting X origin to `$0031/$0035`
- adds `$3C26/$3C28` into `$3C2E/$3C30`
- writes the resulting Y origin to `$0033/$0037`
- calls the broader map-position refresh helper at `C0:1731`

`C4:26C7` then rebases each live entity slot against the updated screen origin:

- live slots are selected by a nonnegative `$0A62,X`
- `$0B16,X = $0B8E,X - $0031`
- `$0B52,X = $0BCA,X - $0033`

The three routines form a tidy movement/camera step: initialize direction-based deltas, advance the screen origin, then rebuild per-entity relative positions.

2026-05-06 screen-position source follow-up: the source now marks the side
effect boundary explicitly. `C4:2631` owns only the `$3C22..$3C30` fixed-point
step staging and sign extension from the C0 projection helpers; `C4:268A` owns
the screen-origin accumulator writes before handing the new origin to
`C0:1731`; `C4:26C7` owns the live-slot screen-relative rebase from world
coordinates.

## Palette interpolation export

`C4:26ED` already has a strong local identity from the landing palette interpolation note. In this local run it belongs after the screen-position helpers, but its behavior is independent and much more palette-facing.

It reads three delta/current plane pairs:

- `7F:0200 + 7F:0800`
- `7F:0400 + 7F:0A00`
- `7F:0600 + 7F:0C00`

For each packed color entry, it advances each current component, clamps each component to the 5-bit color range, clears finished deltas at the bounds, repacks the three components into a 15-bit SNES color word at `$0200,X`, and finally writes `$0030 = #$18`. The existing NMI/DMA notes identify `$0030 = #$18` as the selector for a full `CGRAM` upload from `$0200`.

2026-05-06 palette-export source follow-up: the source now names the local
direct-page frame size and zero component value in addition to the existing
7F-plane, component-mask, `$0200` CGRAM shadow, byte-count, and `$0030` upload
selector contracts. The unusual negative high-channel path still preserves the
observed middle-delta clear exactly as byte-equivalence evidence, not as a
broader semantic claim.

2026-05-06 selector/rebase follow-up: the palette stepper source now separates
the full-CGRAM-upload selector byte (`#$18`) from the `$0030` display-selector
latch, explicitly leaving the actual CGRAM upload to C0/NMI behavior. The
screen-position rebase helper now names the live-entity scan bound as a byte
bound over two-byte slot table entries.

## Working Names

- `C4:23DC` = `SetCenteredColorWindowRangePreset`
- `C4:240A` = `SetFullscreenColorWindowRangePreset`
- `C4:2439` = `ApplyColorMathAndFixedColorFrom9e37`
- `C4:245D` = `StartWh0HdmaChannel4AndWhselA0`
- `C4:248A` = `StopWh0HdmaChannel4AndClearWhsel`
- `C4:249A` = `ApplyFullscreenColorMathWithFixedColorX`
- `C4:24D1` = `ApplyCenteredColorSubtractHalfPreset`
- `C4:2509` = `ApplyFullscreenColorSubtractHalfPreset`
- `C4:2542` = `StartWh0HdmaChannel4`
- `C4:2569` = `SetColorMathMode33`
- `C4:2574` = `SetColorMathModeB3`
- `C4:257F` = `ClearWh0HdmaChannel4Enable`
- `C4:258C` = `ApplyDualCenteredColorSubtractHalfPreset`
- `C4:25CC` = `StartWh0HdmaChannel4AltEntry`
- `C4:25F3` = `ClearWh0HdmaChannel4EnableViaTrb`
- `C4:25FD` = `StartWh2HdmaChannel5`
- `C4:2624` = `ClearWh2HdmaChannel5Enable`
- `C4:2631` = `InitScreenPositionInterpolationFromAngle`
- `C4:268A` = `StepScreenPositionInterpolationAndApply`
- `C4:26C7` = `RebaseLiveEntityPositionsToScreenOrigin`
- `C4:26ED` = `StepPaletteComponentInterpolationToCgramShadow`

## Confidence boundaries

### Locally proved

- the PPU helpers write direct `WH*`, `CGWSEL`, `CGADSUB`, `COLDATA`, `TMW`, `WBGLOG`, and `WOBJLOG` register presets
- the HDMA helpers program channels 4 and 5 for `WH0/WH2` window-edge targets and toggle the matching `$001F` bits
- `C4:2631-C4:26C7` use `$0031/$0033` as a screen-origin pair and update live entity relative coordinates
- `C4:26ED` advances and repacks the six-plane palette interpolation state into the `$0200` CGRAM upload buffer

### Still open

- exact user-facing effect names for the color-window presets
- whether the duplicate channel-4 setup entries have distinct callsite meanings or are purely redundant compiler/source artifacts
- the exact visual event family that owns the `C4:2631-C4:26C7` screen-position interpolation helpers outside the landing/action-script context
