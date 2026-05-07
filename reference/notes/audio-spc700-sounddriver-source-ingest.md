# Audio SPC700 Sound Driver Source Ingest

Status: byte-perfect SPC700-side source is checked in and linked to the audio frontier notes.

## Provenance

- source archive: `C:/Users/Eric/Downloads/sounddriver.zip`
- archive SHA-256: `1BB195F9C2C4BB5B9440B28C5110209F48826B6AE07955848964F02BC50742F2`
- extracted root: `refs/earthbound-sounddriver-byte-perfect`
- manifest: `manifests/audio-spc700-sounddriver-source-ingest.json`

## Extracted Files

| File | Size | SHA-256 | Role |
| --- | ---: | --- | --- |
| `refs/earthbound-sounddriver-byte-perfect/main.asm` | `150086` | `5C8C6C30E80F35B355DFFE86AEB920DF8A645A2806C4509CB2908FB20F63AEEE` | main_driver_disassembly |
| `refs/earthbound-sounddriver-byte-perfect/ram.asm` | `2992` | `21F396FA687509752BEBE8B27AF5078CDADCE20088AB818B3AD2A920CC68849F` | spc700_ram_layout |
| `refs/earthbound-sounddriver-byte-perfect/macros.asm` | `1836` | `BBF6E597ADE44B785941483CE7B23C03B96DA8C1B7170A7B5A7F01914F75BA5E` | assembler_macros_and_constants |
| `refs/earthbound-sounddriver-byte-perfect/sfx_sequences.asm` | `77332` | `188B5CF01DE8FA664D7706DF9860B789213F8CD018144D158E03B3EB36547F70` | sound_effect_sequence_data |

## Source Navigation

- `VCMD_Jump_Table`: `0x0BE3`
- `VCMD_Arg_Length`: `0x0C21`
- `GetNextByte`: `0x0955`
- `SkipByte`: `0x0957`
- VCMD command range: `0xE0..0xFE`
- RAM aliases parsed: `63`

## Immediate Source-Backed Facts

- main.asm declares base $0500 and presents a byte-accurate engine.bin build path through asar
- 0x0955 is GetNextByte and 0x0957 is SkipByte
- VCMD_Jump_Table starts at 0x0BE3 and names handlers for 0xE0..0xFE
- VCMD_Arg_Length starts at 0x0C21 and defines argument lengths for 0xE0..0xFE
- 0x16C7 is an SFX pointer table, not the music high-command dispatch table

## Next Work

- Keep command/effect promotion evidence-gated through the generated audio frontiers.
- Use this source as the navigation layer for VCMD names, reader helpers, and RAM aliases.
