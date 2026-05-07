# PPU colour/window and BG-offset frontier (`C0:AFCD-C0:B3FF`)

## Scope

`C0:AFCD-C0:B3FF` is the PPU-side partner to the APU/DMA frontier just
before it. It covers battle-background colour math presets, fixed colour
writes, window mask setup, window-position DMA helpers, and the BG offset
table generator that fills `$3FD0`.

The ebsrc symbol order corroborates the local sequence:
`UNKNOWN_C0AFCD`, `UNKNOWN_C0AFF1`, `SET_COLDATA`,
`SET_COLOUR_ADDSUB_MODE`, `SET_WINDOW_MASK`, `UNKNOWN_C0B0A6`,
`UNKNOWN_C0B0AA`, `UNKNOWN_C0B0B8`, `UNKNOWN_C0B0EF`,
`UNKNOWN_C0B149`, `UNKNOWN_C0B2FF`, and `UNKNOWN_C0B3FF`.

## Colour math presets

- `C0:AFCD` takes A as a preset index, moves it to X, and applies four table
  bytes:
  - `C0:AFF1,X` -> `$001A`
  - `C0:AFFC,X` -> `$001B`
  - `C0:B006,X` -> `CGWSEL` (`$2130`)
  - `C0:B010,X` -> `CGADSUB` (`$2131`)
- `refs/ebsrc-main/src/battle/load_battlebg.asm` calls this after setting
  `CURRENT_LAYER_CONFIG`, so the preset index is a battle-background layer
  configuration rather than an arbitrary PPU mode.
- `C0:AFF1-C0:B019` are the compact preset tables for those four outputs.

## Fixed colour and window mask helpers

- `C0:B01A` is `SET_COLDATA`. It writes A, X, and Y as 5-bit RGB components
  to `COLDATA` (`$2132`), ORing them with `$20`, `$40`, and `$80`
  respectively.
- `C0:B039` is `SET_COLOUR_ADDSUB_MODE`. It writes the low byte of A to
  `CGWSEL` (`$2130`) and the low byte of X to `CGADSUB` (`$2131`).
- `C0:B047` is `SET_WINDOW_MASK`. It splits A into three two-bit mask fields,
  translates each through `C0:B0A6`, writes `W12SEL`, `W34SEL`, and `WOBJSEL`
  (`$2123-$2125`), then writes A's low five bits to `TMW/TSW`
  (`$212E/$212F`). X is copied to Y on entry and selects normal masks versus
  masks ANDed with `$AA`; the final `WBGLOG/WOBJLOG` (`$212A`) value is
  `$5555` for normal mode and `$0000` for the alternate mode.
- `C0:B0A6-C0:B0A9` is the four-byte mask translation table:
  `00, 0F, F0, FF`.
- `C0:B0AA` resets window left positions by writing `$00FF` to `WH0/WH2`
  (`$2126/$2128`).

## Window-position DMA helpers

- `C0:B0B8` configures a DMA channel selected by A/Y. It uses the source bank
  in `$10`, the long source pointer at `$0E`, targets B-bus register `$26`
  (`WH0`), writes source address `$0E+1`, and ORs the channel bit from
  `DMA_FLAGS` (`C0:AE16`) into `$001F`.
- `C0:B0EF` builds a small descriptor at `$3FC6-$3FCC`, selects one of two
  source lengths/targets (`$4098` or `$4160`) from bit `$04`, programs the
  DMA channel for B-bus register `$26`, points it at `$3FC6`, and marks the
  channel active in `$001F`.

Together these helpers make the window edge registers data-driven: one path
streams an existing table, and the other creates a tiny descriptor table first.

## BG offset table generator

- `C0:B149` prepares the `$3FD0` offset table used by battle-background HDMA
  or per-scanline window/offset effects. It reserves local DP space, stores
  A/X/Y inputs in `$00/$02/$04`, and reads an additional control/count value
  from caller DP `$1C` into `$06`.
- For X in the normal range (`$0070` and above), it fills leading rows with
  `$00FF`, then walks forward through `$3FD0`. For low/negative X it jumps to
  the mirrored/backward fill path at `C0:B233` and walks from `$01BE`
  downward.
- Each row uses SNES hardware math registers:
  - `$4202` receives the scale/multiplier from `$04`.
  - `$4204-$4206` perform division when the row count is nonzero.
  - `$4214/$4216` feed an index through the `C0:B2FF` lookup table and then
    produce a clamped byte pair stored into `$3FD0`.
- The routine mirrors each generated word by writing a second copy offset by
  `row_count * 4`, giving the table its symmetric battle-background shape.
- `C0:B2FF-C0:B400` is the signed/clamped lookup table consumed during the
  divide/multiply pass. It descends from `$FF` through smaller values and
  ends at `$00` immediately before the projection helper pair at `C0:B400`.
- The adjacent source split names `C0:B400/C0:B40B` as the presentation X/Y
  projection helpers and `C0:B425` as the signed sine/projection table. See
  `notes/file-select-init-and-projection-c0b2ff-c0b65f.md`.

## Practical decomp notes

The group is already close to a portable rendering API:

- Colour math can lift as `applyBattleBgColourPreset(index)`,
  `setFixedColour(r,g,b)`, and `setColourAddSubMode(cgwsel,cgadsub)`.
- Window masks can lift as a small enum-to-register translation over
  `00/0F/F0/FF`.
- The window-position DMA helpers can become "upload generated/streamed window
  edge table" calls.
- `C0:B149` is the main piece that still wants visual naming, but its output
  buffer, symmetry, clamp behavior, and dependence on hardware math are now
  explicit.

## Working Names

- `C0:AFCD` = `ApplyBattleBgColourMathPreset`
- `C0:B01A` = `SetFixedColourRgbComponents`
- `C0:B039` = `SetColourAddSubModeRegisters`
- `C0:B047` = `SetWindowMaskRegisters`
- `C0:B0A6` = `WindowMaskNibbleLookupTable`
- `C0:B0AA` = `ResetWindowLeftPositions`
- `C0:B0B8` = `ConfigureWindowPositionDmaFromSource`
- `C0:B0EF` = `BuildAndConfigureWindowPositionDmaDescriptor`
- `C0:B149` = `BuildBattleBgOffsetEffectTable3FD0`
- `C0:B2FF` = `BattleBgOffsetClampLookupTable`
- `C0:B400` = `ProjectPresentationXOffset`
- `C0:B40B` = `ProjectPresentationYOffset`
- `C0:B425` = `PresentationProjectionSineTable`
