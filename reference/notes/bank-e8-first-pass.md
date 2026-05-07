# Bank E8 First Pass

## Main result

Bank `E8` is an audio-pack bank. It contains six `INSERT_AUDIO_PACK` payloads
and a 19-byte tail slack.

Primary artifacts:

- `notes/bank-e8-asset-data-map.md`
- `build/asset-bank-e8.json`

## Bank layout

- `E8:0000..E8:4065`: `AUDIO_PACK_84`, `16486` bytes.
- `E8:4066..E8:7EA5`: `AUDIO_PACK_60`, `15936` bytes.
- `E8:7EA6..E8:BC87`: `AUDIO_PACK_153`, `15842` bytes.
- `E8:BC88..E8:F871`: `AUDIO_PACK_124`, `15338` bytes.
- `E8:F872..E8:FF1A`: `AUDIO_PACK_46`, `1705` bytes.
- `E8:FF1B..E8:FFEC`: `AUDIO_PACK_7`, `210` bytes.
- `E8:FFED..E8:FFFF`: tail slack, `19` bytes.

High confidence: E8 is data/assets, not executable code, and every non-slack
byte belongs to a named audio pack. Audio-pack internals remain out of scope.
