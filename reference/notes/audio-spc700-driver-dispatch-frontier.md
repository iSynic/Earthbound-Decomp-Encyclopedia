# Audio SPC700 Driver Dispatch Frontier

Status: byte-perfect source-backed VCMD labels are known; FF runtime effect still pending.

## Summary

- driver block: pack `1` block `2` at `0x0500`, `16779` bytes
- source-backed VCMD table: `0x0BE3`
- source-backed arg-length table: `0x0C21`
- source-backed reader labels: `GetNextByte=0x0955`, `SkipByte=0x0957`
- RAM aliases parsed: `63`
- source-backed command range: `0xE0..0xFE`
- unresolved control bytes: `['0x00', '0xFF']`
- semantic status: `source_backed_vcmd_labels_known_ff_reader_effect_unconfirmed`

## Source-Backed Table

- `VCMD_Jump_Table`: `0x0BE3`
- `VCMD_Arg_Length`: `0x0C21`
- `GetNextByte`: `0x0955`
- `SkipByte`: `0x0957`
- commands `0xE0..0xFE` now come from checked-in source labels, not static table guesses
- `0xFF` remains outside the source-backed VCMD table and still needs reader-path classification

## Entries

| Command | Source label | Driver target | Arg bytes | Target first byte |
| --- | --- | ---: | ---: | --- |
| `0xE0` | `VCMD_Instrument` | `0x095F` | `1` | `0xD5` |
| `0xE1` | `VCMD_Pan` | `0x09B8` | `1` | `0xC4` |
| `0xE2` | `VCMD_PanFade` | `0x09D8` | `2` | `0x2D` |
| `0xE3` | `VCMD_Vibrato` | `0x09FD` | `3` | `0xD5` |
| `0xE4` | `VCMD_VibratoOff` | `0x0A09` | `0` | `0xD4` |
| `0xE5` | `VCMD_Volume` | `0x0A24` | `1` | `0xE8` |
| `0xE6` | `VCMD_VolumeFade` | `0x0A29` | `2` | `0xC4` |
| `0xE7` | `VCMD_Tempo` | `0x0A3B` | `1` | `0xE8` |
| `0xE8` | `VCMD_TempoFade` | `0x0A40` | `2` | `0xC4` |
| `0xE9` | `VCMD_Transpose` | `0x0A52` | `1` | `0xC4` |
| `0xEA` | `VCMD_VoiceTranspose` | `0x0A55` | `1` | `0xD5` |
| `0xEB` | `VCMD_Tremolo` | `0x0A59` | `3` | `0xD5` |
| `0xEC` | `VCMD_TremoloOff` | `0x0A65` | `0` | `0xD4` |
| `0xED` | `VCMD_VoiceVolume` | `0x0A86` | `1` | `0xD5` |
| `0xEE` | `VCMD_VoiceVolumeFade` | `0x0A8F` | `2` | `0xD4` |
| `0xEF` | `VCMD_Subroutine` | `0x0AAC` | `3` | `0xD5` |
| `0xF0` | `VCMD_VibratoFade` | `0x0A14` | `1` | `0xD5` |
| `0xF1` | `VCMD_PortamentoTo` | `0x0A68` | `3` | `0xE8` |
| `0xF2` | `VCMD_PortamentoFrom` | `0x0A6C` | `3` | `0xE8` |
| `0xF3` | `VCMD_PortamentoOff` | `0x0A82` | `0` | `0xD5` |
| `0xF4` | `VCMD_Detune` | `0x0AA8` | `1` | `0xD5` |
| `0xF5` | `VCMD_EchoVolume` | `0x0ACF` | `3` | `0xC4` |
| `0xF6` | `VCMD_EchoOff` | `0x0B03` | `0` | `0xDA` |
| `0xF7` | `VCMD_EchoParameters` | `0x0B0A` | `3` | `0x3F` |
| `0xF8` | `VCMD_EchoVolumeFade` | `0x0AE2` | `3` | `0xC4` |
| `0xF9` | `VCMD_NoteSlide` | `0x0B94` | `3` | `0xD4` |
| `0xFA` | `VCMD_PercussionInstrument` | `0x0B72` | `1` | `0xC4` |
| `0xFB` | `VCMD_Nop` | `0x0B75` | `2` | `0x3F` |
| `0xFC` | `VCMD_MuteVoice` | `0x0B79` | `0` | `0xBC` |
| `0xFD` | `VCMD_FastForward` | `0x0B7E` | `0` | `0xBC` |
| `0xFE` | `VCMD_FastForwardOff` | `0x0B7F` | `0` | `0xC4` |

## Findings

- The ingested byte-perfect source labels the VCMD jump table directly at 0x0BE3 and the argument-length table at 0x0C21.
- Commands 0xE0..0xFE now have source-backed labels and handler targets rather than heuristic candidate names.
- 0x16C7 is refuted as a music high-command dispatch table; the checked-in source shows it is an SFX pointer table.
- 0xFF remains unresolved because the source-backed VCMD table ends at 0xFE, so FF still needs reader-path proof.

## Next Work

- align project-local sequence command names with the source-backed VCMD labels
- trace 0xFF reader behavior relative to the source-backed 0xE0..0xFE VCMD table
- feed the updated labels into the sequence-control and exact-duration lanes
