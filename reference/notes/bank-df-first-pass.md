# Bank DF First Pass

## Main result

Bank `DF` is a mixed map/audio data bank. It contains compressed map tileset
graphics, compressed map animation graphics, the landing palette-animation
profile/payload table family, and one audio pack.

Primary artifacts:

- `notes/bank-df-asset-data-map.md`
- `notes/df-landing-palette-animation-contracts.md`
- `build/asset-bank-df.json`

The generated map accounts for:

- binary assets: `22`
- binary asset bytes: `63625`
- asset mix: `21` compressed graphics payloads and `1` audio pack
- inferred generated table bytes: `1893`
- coverage gap bytes: `18`
- missing payload metadata: `0`

## Bank layout

The high-level DF layout is:

- `DF:0000..DF:C242`: `MAP_DATA_TILE_SET_GRAPHICS_12`, `16`, `17`, `18`,
  `19`, and `15`, `49731` bytes total.
- `DF:C243..DF:E4E0`: `MAP_DATA_TILE_ANIMATION_GFX_0` through
  `MAP_DATA_TILE_ANIMATION_GFX_14`, `8862` bytes total.
- `DF:E4E1..DF:EC45`: landing palette-animation table family, `1893` bytes.
- `DF:EC46..DF:FFED`: `AUDIO_PACK_4`, `5032` bytes.
- `DF:FFEE..DF:FFFF`: tail slack, `18` bytes.

## Generated Palette-Animation Data

The bank config names three missing generated includes between animation
graphics and the audio pack:

- `data/map/palette_anim_pointer_table.asm`
- `data/map/palette_anim_secondary_table.asm`
- `data/map/palette_anim_table.asm`

Those source files are absent from the checked-in reference tree, but local C0
consumers and the generated DF scaffold now support an internal split:

- `DF:E4E1..DF:E55C`: 31 long pointers indexed by `C0:023F` as
  `$02A0 - 1`.
- `DF:E55D..DF:E61A`: 31 variable profile records. Each record is a four-byte
  compressed-payload pointer, a one-byte step count, and `step_count`
  one-byte sequencer values copied into `$4460`.
- `DF:E61B..DF:EC45`: eight non-empty compressed palette-animation payloads.
  Empty profiles point at the terminal `DF:EC46` sentinel and have count zero.

`tools/build_data_contract_manifest.py` promotes these as
`LANDING_PALETTE_ANIM_PROFILE_POINTER_TABLE`,
`LANDING_PALETTE_ANIM_PROFILE_0..30`, and
`LANDING_PALETTE_ANIM_PAYLOAD_0..7`.
`notes/df-landing-palette-animation-contracts.md` summarizes the 31 profile
rows, eight compressed payload rows, empty-profile sentinel rows, and the
source-emission boundary for this family. It now records explicit
source-emission rows for the pointer table, variable profile records, compressed
payload rows, and the `DF:EC46` zero-step sentinel. The sentinel is also the
start of `AUDIO_PACK_4`, so source emission should preserve that numeric
address overlap instead of carving it into a synthetic palette payload.

## Current DF confidence boundary

High confidence:

- DF is data/assets, not executable code.
- Tileset graphics, animation graphics, landing palette-animation profile data,
  landing palette-animation payload data, and audio spans are exact for the US
  retail build.
- Only `18` bytes at the end of the bank are unclaimed slack.

Still intentionally out of scope:

- Decompressing or rendering tileset/animation graphics.
- Naming the human-facing meaning of each landing palette-animation profile.
- Audio-pack internals.

## Recommended next move

Use `notes/df-landing-palette-animation-contracts.md` plus the central manifest
contracts for source emission. The table/profile/payload rows and the
zero-step/audio-boundary sentinel policy are now source-emission ready. Remaining
DF semantic work is optional human-facing profile names and render fixtures, not
table/payload split discovery.
