# Bank E2 First Pass

## Main result

Bank `E2` is an audio-pack bank. It contains four `INSERT_AUDIO_PACK` payloads
and a 3-byte tail slack.

Primary artifacts:

- `notes/bank-e2-asset-data-map.md`
- `build/asset-bank-e2.json`

The generated map accounts for:

- binary assets: `4`
- binary asset bytes: `65533`
- asset mix: `4` audio packs
- table includes: `0`
- table bytes: `0`
- coverage gap bytes: `3`
- missing payload metadata: `0`

## Bank layout

- `E2:0000..E2:77EF`: `AUDIO_PACK_108`, `30704` bytes.
- `E2:77F0..E2:ED2B`: `AUDIO_PACK_0`, `30012` bytes.
- `E2:ED2C..E2:FC87`: `AUDIO_PACK_36`, `3932` bytes.
- `E2:FC88..E2:FFFC`: `AUDIO_PACK_18`, `885` bytes.
- `E2:FFFD..E2:FFFF`: tail slack, `3` bytes.

## Current E2 confidence boundary

High confidence:

- E2 is data/assets, not executable code.
- Every non-slack byte belongs to a named audio pack.

Still intentionally out of scope:

- Audio-pack internals.

## Recommended next move

Proceed through the adjacent audio-pack banks while the manifest can close them
quickly.
