# Bank E7 First Pass

## Main result

Bank `E7` is an audio-pack bank. It contains four `INSERT_AUDIO_PACK` payloads
and a 156-byte tail slack.

Primary artifacts:

- `notes/bank-e7-asset-data-map.md`
- `build/asset-bank-e7.json`

## Bank layout

- `E7:0000..E7:4313`: `AUDIO_PACK_78`, `17172` bytes.
- `E7:4314..E7:849B`: `AUDIO_PACK_82`, `16776` bytes.
- `E7:849C..E7:C5C7`: `AUDIO_PACK_8`, `16684` bytes.
- `E7:C5C8..E7:FF63`: `AUDIO_PACK_24`, `14748` bytes.
- `E7:FF64..E7:FFFF`: tail slack, `156` bytes.

High confidence: E7 is data/assets, not executable code, and every non-slack
byte belongs to a named audio pack. Audio-pack internals remain out of scope.
