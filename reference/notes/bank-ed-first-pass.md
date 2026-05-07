# Bank ED First Pass

## Main result

Bank `ED` is an audio-pack bank. It contains thirty-six `INSERT_AUDIO_PACK`
payloads and a 2-byte tail slack.

Primary artifacts:

- `notes/bank-ed-asset-data-map.md`
- `build/asset-bank-ed.json`

The generated map accounts for:

- binary assets: `36`
- binary asset bytes: `65534`
- table includes: `0`
- table bytes: `0`
- coverage gap bytes: `2`
- missing payload metadata: `0`

## Bank layout

`ED:0000..ED:FFFD` is a dense run of audio packs:

- starts with `AUDIO_PACK_121`, `ED:0000..ED:0A06`, `2567` bytes.
- continues through many small packs, including `87`, `132`, `116`, `34`,
  `119`, `141`, `48`, `39`, `150`, `120`, `38`, `161`, `68`, `104`, `90`,
  `86`, `100`, `26`, `43`, `162`, `85`, `99`, `28`, `10`, `117`, `77`, `19`,
  `57`, `14`, `158`, `30`, `134`, `113`, and `146`.
- ends with `AUDIO_PACK_29`, `ED:FC9C..ED:FFFD`, `866` bytes.
- `ED:FFFE..ED:FFFF` is tail slack, `2` bytes.

## Current ED confidence boundary

High confidence:

- ED is data/assets, not executable code.
- Every non-slack byte belongs to a named audio pack.

Still intentionally out of scope:

- Audio-pack internals.

## Recommended next move

Proceed to `EE`, which appears to finish the available audio pack bank configs.
