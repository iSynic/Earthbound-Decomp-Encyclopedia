# Bank E3 First Pass

## Main result

Bank `E3` is an audio-pack bank. It contains four `INSERT_AUDIO_PACK` payloads
and a 14-byte tail slack.

Primary artifacts:

- `notes/bank-e3-asset-data-map.md`
- `build/asset-bank-e3.json`

The generated map accounts for:

- binary assets: `4`
- binary asset bytes: `65522`
- asset mix: `4` audio packs
- table includes: `0`
- table bytes: `0`
- coverage gap bytes: `14`
- missing payload metadata: `0`

## Bank layout

- `E3:0000..E3:5F63`: `AUDIO_PACK_3`, `24420` bytes.
- `E3:5F64..E3:B0F9`: `AUDIO_PACK_70`, `20886` bytes.
- `E3:B0FA..E3:FDCB`: `AUDIO_PACK_37`, `19666` bytes.
- `E3:FDCC..E3:FFF1`: `AUDIO_PACK_32`, `550` bytes.
- `E3:FFF2..E3:FFFF`: tail slack, `14` bytes.

## Current E3 confidence boundary

High confidence:

- E3 is data/assets, not executable code.
- Every non-slack byte belongs to a named audio pack.

Still intentionally out of scope:

- Audio-pack internals.

## Recommended next move

Proceed to `E4`.
