# File-select init and projection split (`C0:B2FF-C0:B65F`)

## Scope

`C0:B2FF-C0:B65F` is a mixed presentation/file-select corridor that was
previously carried as a single byte table. The 2026-05-06 C0 source polish pass
split it into four local pieces:

- `C0:B2FF-C0:B400`: battle-background offset clamp lookup table.
- `C0:B400-C0:B425`: projection helper pair that writes the SNES multiply
  registers and reads the hardware product.
- `C0:B425-C0:B525`: signed byte sine/projection table consumed by the helper.
- `C0:B525-C0:B65F`: file-select initialization routine.

## Projection Helpers

`C0:B400` adjusts the caller's X phase by `-$40`, masks it to one byte, and
falls through to the Y-projection helper at `C0:B40B`. `C0:B40B` writes the
incoming A value to `M7A` (`$211B`), reads the phase-indexed byte from
`C0:B425`, writes it to `M7B` (`$211C`), then returns the product from
`MPYL/MPYM` (`$2135`).

The absolute long table read is intentionally preserved in source as
`lda $C0B425,X`; forcing it through the local label lets Asar shrink the
operand and breaks byte equivalence.

## File-select Init

`C0:B525` is the same-bank prelude called by the intro/file-select continuation
inside `C0:B67F..B967`. It resets the renderer, delayed-action pools, sprite
work, entity byte pool, entity state tables, overworld VRAM state, and party
visual masks before staging the file-select presentation.

The routine then copies palette/window blocks from long sources, clears the
battle/presentation state, clears the text-layer tilemap, queues a VRAM
transfer for the text layer, decompresses text-window graphics into `$7F`,
copies a second long block, resets active glyph state, loads background
animation `$00E6`, initializes the file-select entity/script state, runs the
file-select session through `C1:FF6B`, cleans up entity slot `$17`, and restores
the selected audio-channel setting from `$98B7 - 1`.

## Working Names

- `C0:B2FF` = `BattleBgOffsetClampLookupTable`
- `C0:B400` = `ProjectPresentationXOffset`
- `C0:B40B` = `ProjectPresentationYOffset`
- `C0:B425` = `PresentationProjectionSineTable`
- `C0:B525` = `FileSelectInit`

## Source Polish Follow-Up

`src/c0/c0_b2ff_battle_bg_offset_clamp_lookup_table.asm` now carries the mixed
source/data unit directly, and
`src/c0/c0_b67f_initialize_intro_overworld_scene.asm` calls
`C0B525_FileSelectInit` instead of the previous raw `jsr $B525`. Strict C0
byte-equivalence validation passes with the split source scaffold.
