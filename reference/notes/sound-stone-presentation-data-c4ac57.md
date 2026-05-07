# Sound Stone Presentation Data `C4:AC57`

## Scope

This note classifies the former large unknown-data include at `C4:AC57..B1B7`.
It sits after the battle overlay script interpreter/data corridor and
immediately before the landing-display asset stream helpers.

See also [battle-overlay-script-state-c4a67e-c4a7b0.md](notes/battle-overlay-script-state-c4a67e-c4a7b0.md).

## Main result

`C4:AC57` is data, not a routine entry. The first bytes decode as invalid-looking
65816 only because they are table bytes. Interpreted as little-endian long
pointers, the prefix is a nine-entry pointer table:

| index | pointer |
|---:|---|
| `0` | `EF:4A40` |
| `1` | `EF:4AD0` |
| `2` | `EF:4B3A` |
| `3` | `EF:4BA4` |
| `4` | `EF:4C0E` |
| `5` | `EF:4C78` |
| `6` | `EF:4CE2` |
| `7` | `EF:4D4C` |
| `8` | `EF:4DB6` |

The `EF:4A40` target is the start of ebsrc's `data/unknown/EF4A40.asm` family,
whose bytes are small, repeated numeric values rather than code. That makes the
front of `C4:AC57` a cross-bank presentation-data pointer block.

The bytes after the pointer prefix are now split more tightly. `C4:AC57..ACCE`
is local presentation data, while `C4:ACCE..B1B8` is code: it begins with
`REP #$31`, has three direct `JSL` callers (`C1:30DA`, `C1:BFDF`, and
`C1:C01F`), walks the `C4:AC57` pointer table at `C4:AFB8..AFD5`, reads the
local coordinate/control tables at `C4:AC7B`, `C4:AC83`, `C4:AC8B`, `C4:AC93`,
`C4:AC9B`, `C4:ACA3`, `C4:ACAB`, `C4:ACB4`, and `C4:ACC6`, and draws through
the same C0/C2/C4 presentation helpers used elsewhere in C4.

Current build-candidate boundary:

- `C4:AC57..ACCE`: protected Sound Stone table block in
  `src/c4/sound_stone_presentation_tables.asm`
- `C4:ACCE..B1B8`: promoted Sound Stone presentation controller in
  `src/c4/sound_stone_presentation_controller.asm`; its scaffold source uses
  explicit state-aware immediate widths after the VRAM transfer helper call at
  `C4:AD18`
- `C4:B1B8..B329`: promoted landing-display asset transfer and stream init
  helper source in `src/c4/landing_display_asset_stream_helpers.asm`

Source polish: `src/c4/sound_stone_presentation_controller.asm` now names the
CE Sound Stone graphics/palette payload addresses, 7F work buffer, VRAM
transfer sizes, sprite resource load arguments, staging tile blocks at
`$B3EE/$B3F3`, the eight-Sanctuary state record bases rooted at `$B37E`,
state values, initial orbit delay, frame-group period, and end-hold timer.
The animation loop also names the phrase-length stinger lead, EF payload
pointer-table walk, per-Sanctuary orbit angle/phase/glyph fields, opposite
orbit projection, spinner frame, battle-visual script ids, input exit mask,
and presentation closeout fade/busy gates.

2026-05-06 table polish: `src/c4/sound_stone_presentation_tables.asm` now
keeps the original `C4:AC57` block label while splitting the bytes into
table-local labels for the nine EF payload pointers, the coordinate/control
and timing rows, plus the melody id and Sanctuary event rows. The labels
intentionally remain C4-owned because the C1 callers enter the controller at
`C4:ACCE` rather than reading these rows directly.

2026-05-06 source polish follow-up: the EF payload pointer prefix is now
encoded as nine explicit 4-byte rows (`low word`, `bank`, padding), matching
the controller's low-word plus bank-byte pointer walk. The controller also now
marks its C4-owned setup, Sanctuary-record initialization, per-frame sequence,
render pass, animated EF-payload path, and closeout side effects without
assigning C0/C2 renderer or transition internals to this bank.

## Working Names

- `C4:AC57` = `SoundStonePresentationDataBlock`
- `C4:AC57` = `SoundStonePresentationEfPayloadPointerTable`
- `C4:AC57` = `SoundStonePresentationEfPayloadPointer0`
- `C4:AC5B` = `SoundStonePresentationEfPayloadPointer1`
- `C4:AC5F` = `SoundStonePresentationEfPayloadPointer2`
- `C4:AC63` = `SoundStonePresentationEfPayloadPointer3`
- `C4:AC67` = `SoundStonePresentationEfPayloadPointer4`
- `C4:AC6B` = `SoundStonePresentationEfPayloadPointer5`
- `C4:AC6F` = `SoundStonePresentationEfPayloadPointer6`
- `C4:AC73` = `SoundStonePresentationEfPayloadPointer7`
- `C4:AC77` = `SoundStonePresentationEfPayloadPointer8`
- `C4:AC7B` = `SoundStonePresentationTileXTable`
- `C4:AC83` = `SoundStonePresentationTileYTable`
- `C4:AC8B` = `SoundStonePresentationSpriteXTable`
- `C4:AC93` = `SoundStonePresentationSpriteYTable`
- `C4:AC9B` = `SoundStonePresentationSpriteOffsetXTable`
- `C4:ACA3` = `SoundStonePresentationSpriteOffsetYTable`
- `C4:ACAB` = `SoundStonePresentationMelodyIdTable`
- `C4:ACB4` = `SoundStonePresentationPhraseLengthTable`
- `C4:ACC6` = `SoundStonePresentationSanctuaryEventTable`
- `C4:ACCE` = `RunSoundStonePresentationSequence`

## Still open

- confirm the final high-level names for the local coordinate/control tables
- map which caller path selects each of the nine `EF:4A40..4DB6` targets
