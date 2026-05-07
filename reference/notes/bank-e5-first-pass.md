# Bank E5 First Pass

## Main result

Bank `E5` is an audio-pack bank. It contains five `INSERT_AUDIO_PACK` payloads
and a 34-byte tail slack.

Primary artifacts:

- `notes/bank-e5-asset-data-map.md`
- `build/asset-bank-e5.json`

The generated map accounts for:

- binary assets: `5`
- binary asset bytes: `65502`
- asset mix: `5` audio packs
- table includes: `0`
- table bytes: `0`
- coverage gap bytes: `34`
- missing payload metadata: `0`

## Bank layout

- `E5:0000..E5:4C49`: `AUDIO_PACK_50`, `19530` bytes.
- `E5:4C4A..E5:954D`: `AUDIO_PACK_92`, `18692` bytes.
- `E5:954E..E5:DD31`: `AUDIO_PACK_56`, `18404` bytes.
- `E5:DD32..E5:FF37`: `AUDIO_PACK_122`, `8710` bytes.
- `E5:FF38..E5:FFDD`: `AUDIO_PACK_166`, `166` bytes.
- `E5:FFDE..E5:FFFF`: tail slack, `34` bytes.

## Current E5 confidence boundary

High confidence:

- E5 is data/assets, not executable code.
- Every non-slack byte belongs to a named audio pack.

Still intentionally out of scope:

- Audio-pack internals.

## Recommended next move

Proceed to `E6`, but expect tooling work: the bank config manually defines
`AUDIO_PACK_1` with inline subpack headers, an `.INCBIN`, and sliced `BINARY`
segments before returning to normal `INSERT_AUDIO_PACK` directives.
