# Bank E6 First Pass

## Main result

Bank `E6` is an audio data bank with one hand-authored audio-pack block followed
by four normal `INSERT_AUDIO_PACK` payloads. The custom block defines
`AUDIO_PACK_1` directly in assembly using subpack headers, inline bytes, an
`.INCBIN`, and sliced `BINARY` ranges.

Primary artifacts:

- `notes/bank-e6-asset-data-map.md`
- `build/asset-bank-e6.json`

The generated map accounts for:

- binary assets: `4`
- binary asset bytes: `47645`
- table/custom audio bytes: `17880`
- coverage gap bytes: `11`
- missing payload metadata: `0`

## Bank layout

- `E6:0000..E6:45D7`: custom `AUDIO_PACK_1` assembly block, `17880` bytes.
- `E6:45D8..E6:8B99`: `AUDIO_PACK_74`, `17858` bytes.
- `E6:8B9A..E6:CF07`: `AUDIO_PACK_76`, `17262` bytes.
- `E6:CF08..E6:FF17`: `AUDIO_PACK_47`, `12304` bytes.
- `E6:FF18..E6:FFF4`: `AUDIO_PACK_73`, `221` bytes.
- `E6:FFF5..E6:FFFF`: tail slack, `11` bytes.

## Custom Audio-Pack Handling

The manifest tool now treats sliced `BINARY "file", offset, length` directives
as inline byte spans instead of looking up the whole referenced payload. It also
models unresolved `.INCBIN` data as an inferred span up to the next known binary
anchor. For E6, that lets the custom `AUDIO_PACK_1` block close cleanly at
`E6:45D7` without double-counting the full `audiopacks/1.ebm` metadata entry.

## Current E6 confidence boundary

High confidence:

- E6 is data/assets, not executable code.
- `AUDIO_PACK_1` occupies `E6:0000..E6:45D7`.
- Normal audio packs `74`, `76`, `47`, and `73` have exact spans.
- Only `11` bytes at the end of the bank are unclaimed slack.

Still intentionally out of scope:

- Internal SPC/audio subpack semantics.
- Exact split inside the inferred `.INCBIN` portion of custom `AUDIO_PACK_1`.

## Recommended next move

Proceed to `E7`. The next bank returns to normal `INSERT_AUDIO_PACK` payloads,
so it should close quickly.
