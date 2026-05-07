# E6 byte-equivalence validation

This report assembles an existing durable Asar source-bank scaffold into a clean ROM copy, then compares the protected byte ranges against the original ROM.

- status: `OK`
- mode: `durable-scaffold`
- modules: `14`
- non-OK modules: `0`
- mismatches: `0`

## Modules

| Status | Source Path | Range | Size | Mismatches | Generated ASM |
| --- | --- | --- | ---: | ---: | --- |
| `OK` | `src/e6/table_000_inline_audio_pack_1.asm` | `E6:0000..E6:0002` | 2 | 0 | `src/e6/bank_e6_helpers_asar.asm` |
| `OK` | `src/e6/table_001_inline_word.asm` | `E6:0002..E6:0004` | 2 | 0 | `src/e6/bank_e6_helpers_asar.asm` |
| `OK` | `src/e6/table_002_inline_audio_subpack_0_data_start.asm` | `E6:0004..E6:0022` | 30 | 0 | `src/e6/bank_e6_helpers_asar.asm` |
| `OK` | `src/e6/table_003_inline_audio_subpack_0_data_end.asm` | `E6:0022..E6:0024` | 2 | 0 | `src/e6/bank_e6_helpers_asar.asm` |
| `OK` | `src/e6/table_004_inline_word.asm` | `E6:0024..E6:0026` | 2 | 0 | `src/e6/bank_e6_helpers_asar.asm` |
| `OK` | `src/e6/table_005_inline_audio_subpack_1_data_start.asm` | `E6:0026..E6:003E` | 24 | 0 | `src/e6/bank_e6_helpers_asar.asm` |
| `OK` | `src/e6/table_006_inline_audio_subpack_1_data_end.asm` | `E6:003E..E6:0040` | 2 | 0 | `src/e6/bank_e6_helpers_asar.asm` |
| `OK` | `src/e6/table_007_inline_word.asm` | `E6:0040..E6:0042` | 2 | 0 | `src/e6/bank_e6_helpers_asar.asm` |
| `OK` | `src/e6/table_008_incbin_main_spc700_bin.asm` | `E6:0042..E6:45D8` | 17814 | 0 | `src/e6/bank_e6_helpers_asar.asm` |
| `OK` | `src/e6/asset_audio_pack_74.asm` | `E6:45D8..E6:8B9A` | 17858 | 0 | `src/e6/bank_e6_helpers_asar.asm` |
| `OK` | `src/e6/asset_audio_pack_76.asm` | `E6:8B9A..E6:CF08` | 17262 | 0 | `src/e6/bank_e6_helpers_asar.asm` |
| `OK` | `src/e6/asset_audio_pack_47.asm` | `E6:CF08..E6:FF18` | 12304 | 0 | `src/e6/bank_e6_helpers_asar.asm` |
| `OK` | `src/e6/asset_audio_pack_73.asm` | `E6:FF18..E6:FFF5` | 221 | 0 | `src/e6/bank_e6_helpers_asar.asm` |
| `OK` | `src/e6/asset_bank_e6_gap_1_tailpadding.asm` | `E6:FFF5..E6:10000` | 11 | 0 | `src/e6/bank_e6_helpers_asar.asm` |
