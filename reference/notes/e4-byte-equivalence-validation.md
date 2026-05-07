# E4 byte-equivalence validation

This report assembles an existing durable Asar source-bank scaffold into a clean ROM copy, then compares the protected byte ranges against the original ROM.

- status: `OK`
- mode: `durable-scaffold`
- modules: `6`
- non-OK modules: `0`
- mismatches: `0`

## Modules

| Status | Source Path | Range | Size | Mismatches | Generated ASM |
| --- | --- | --- | ---: | ---: | --- |
| `OK` | `src/e4/asset_audio_pack_64.asm` | `E4:0000..E4:514A` | 20810 | 0 | `src/e4/bank_e4_helpers_asar.asm` |
| `OK` | `src/e4/asset_audio_pack_42.asm` | `E4:514A..E4:A232` | 20712 | 0 | `src/e4/bank_e4_helpers_asar.asm` |
| `OK` | `src/e4/asset_audio_pack_126.asm` | `E4:A232..E4:EED0` | 19614 | 0 | `src/e4/bank_e4_helpers_asar.asm` |
| `OK` | `src/e4/asset_audio_pack_125.asm` | `E4:EED0..E4:FD92` | 3778 | 0 | `src/e4/bank_e4_helpers_asar.asm` |
| `OK` | `src/e4/asset_audio_pack_155.asm` | `E4:FD92..E4:FFF9` | 615 | 0 | `src/e4/bank_e4_helpers_asar.asm` |
| `OK` | `src/e4/asset_bank_e4_gap_1_tailpadding.asm` | `E4:FFF9..E4:10000` | 7 | 0 | `src/e4/bank_e4_helpers_asar.asm` |
