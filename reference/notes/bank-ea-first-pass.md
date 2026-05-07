# Bank EA First Pass

## Main result

Bank `EA` is an audio-pack bank. It contains seven `INSERT_AUDIO_PACK` payloads
and a 30-byte tail slack.

Primary artifacts:

- `notes/bank-ea-asset-data-map.md`
- `build/asset-bank-ea.json`

## Bank layout

- `EA:0000..EA:3379`: `AUDIO_PACK_54`, `13178` bytes.
- `EA:337A..EA:6593`: `AUDIO_PACK_52`, `12826` bytes.
- `EA:6594..EA:96F5`: `AUDIO_PACK_72`, `12642` bytes.
- `EA:96F6..EA:C58F`: `AUDIO_PACK_89`, `11930` bytes.
- `EA:C590..EA:F123`: `AUDIO_PACK_35`, `11156` bytes.
- `EA:F124..EA:FE8A`: `AUDIO_PACK_140`, `3431` bytes.
- `EA:FE8B..EA:FFE1`: `AUDIO_PACK_145`, `343` bytes.
- `EA:FFE2..EA:FFFF`: tail slack, `30` bytes.

High confidence: EA is data/assets, not executable code, and every non-slack
byte belongs to a named audio pack. Audio-pack internals remain out of scope.
