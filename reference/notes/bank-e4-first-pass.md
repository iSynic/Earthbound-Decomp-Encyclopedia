# Bank E4 First Pass

## Main result

Bank `E4` is an audio-pack bank. It contains five `INSERT_AUDIO_PACK` payloads
and a 7-byte tail slack.

Primary artifacts:

- `notes/bank-e4-asset-data-map.md`
- `build/asset-bank-e4.json`

The generated map accounts for:

- binary assets: `5`
- binary asset bytes: `65529`
- asset mix: `5` audio packs
- table includes: `0`
- table bytes: `0`
- coverage gap bytes: `7`
- missing payload metadata: `0`

## Bank layout

- `E4:0000..E4:5149`: `AUDIO_PACK_64`, `20810` bytes.
- `E4:514A..E4:A231`: `AUDIO_PACK_42`, `20712` bytes.
- `E4:A232..E4:EECF`: `AUDIO_PACK_126`, `19614` bytes.
- `E4:EED0..E4:FD91`: `AUDIO_PACK_125`, `3778` bytes.
- `E4:FD92..E4:FFF8`: `AUDIO_PACK_155`, `615` bytes.
- `E4:FFF9..E4:FFFF`: tail slack, `7` bytes.

## Current E4 confidence boundary

High confidence:

- E4 is data/assets, not executable code.
- Every non-slack byte belongs to a named audio pack.

Still intentionally out of scope:

- Audio-pack internals.

## Recommended next move

Proceed to `E5`.
