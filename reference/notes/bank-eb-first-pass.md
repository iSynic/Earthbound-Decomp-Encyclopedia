# Bank EB First Pass

## Main result

Bank `EB` is an audio-pack bank. It contains eight `INSERT_AUDIO_PACK` payloads
and a 1-byte tail slack.

Primary artifacts:

- `notes/bank-eb-asset-data-map.md`
- `build/asset-bank-eb.json`

## Bank layout

- `EB:0000..EB:29E7`: `AUDIO_PACK_44`, `10728` bytes.
- `EB:29E8..EB:520B`: `AUDIO_PACK_21`, `10276` bytes.
- `EB:520C..EB:78D5`: `AUDIO_PACK_5`, `9930` bytes.
- `EB:78D6..EB:9F8D`: `AUDIO_PACK_40`, `9912` bytes.
- `EB:9F8E..EB:C4E7`: `AUDIO_PACK_33`, `9562` bytes.
- `EB:C4E8..EB:E9E3`: `AUDIO_PACK_105`, `9468` bytes.
- `EB:E9E4..EB:FE21`: `AUDIO_PACK_154`, `5182` bytes.
- `EB:FE22..EB:FFFE`: `AUDIO_PACK_13`, `477` bytes.
- `EB:FFFF..EB:FFFF`: tail slack, `1` byte.

High confidence: EB is data/assets, not executable code, and every non-slack
byte belongs to a named audio pack. Audio-pack internals remain out of scope.
