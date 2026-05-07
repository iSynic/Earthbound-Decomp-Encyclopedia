# Bank EC First Pass

## Main result

Bank `EC` is an audio-pack bank. It contains fourteen `INSERT_AUDIO_PACK`
payloads and a 108-byte tail slack.

Primary artifacts:

- `notes/bank-ec-asset-data-map.md`
- `build/asset-bank-ec.json`

## Bank layout

- `EC:0000..EC:23EB`: `AUDIO_PACK_114`, `9196` bytes.
- `EC:23EC..EC:4591`: `AUDIO_PACK_109`, `8614` bytes.
- `EC:4592..EC:66FF`: `AUDIO_PACK_107`, `8558` bytes.
- `EC:6700..EC:8863`: `AUDIO_PACK_98`, `8548` bytes.
- `EC:8864..EC:9B75`: `AUDIO_PACK_165`, `4882` bytes.
- `EC:9B76..EC:FF93`: audio packs `62`, `58`, `133`, `97`, `55`, `106`,
  `25`, `15`, and `157`, `25738` bytes total.
- `EC:FF94..EC:FFFF`: tail slack, `108` bytes.

High confidence: EC is data/assets, not executable code, and every non-slack
byte belongs to a named audio pack. Audio-pack internals remain out of scope.
