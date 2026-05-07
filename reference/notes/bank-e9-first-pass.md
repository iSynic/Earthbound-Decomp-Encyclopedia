# Bank E9 First Pass

## Main result

Bank `E9` is an audio-pack bank. It contains six `INSERT_AUDIO_PACK` payloads
and a 155-byte tail slack.

Primary artifacts:

- `notes/bank-e9-asset-data-map.md`
- `build/asset-bank-e9.json`

## Bank layout

- `E9:0000..E9:3A73`: `AUDIO_PACK_27`, `14964` bytes.
- `E9:3A74..E9:7355`: `AUDIO_PACK_80`, `14562` bytes.
- `E9:7356..E9:AC25`: `AUDIO_PACK_118`, `14544` bytes.
- `E9:AC26..E9:E083`: `AUDIO_PACK_131`, `13406` bytes.
- `E9:E084..E9:F8C7`: `AUDIO_PACK_2`, `6212` bytes.
- `E9:F8C8..E9:FF64`: `AUDIO_PACK_149`, `1693` bytes.
- `E9:FF65..E9:FFFF`: tail slack, `155` bytes.

High confidence: E9 is data/assets, not executable code, and every non-slack
byte belongs to a named audio pack. Audio-pack internals remain out of scope.
