# E9 byte-equivalence validation

This report assembles an existing durable Asar source-bank scaffold into a clean ROM copy, then compares the protected byte ranges against the original ROM.

- status: `OK`
- mode: `durable-scaffold`
- modules: `7`
- non-OK modules: `0`
- mismatches: `0`

## Modules

| Status | Source Path | Range | Size | Mismatches | Generated ASM |
| --- | --- | --- | ---: | ---: | --- |
| `OK` | `src/e9/asset_audio_pack_27.asm` | `E9:0000..E9:3A74` | 14964 | 0 | `src/e9/bank_e9_helpers_asar.asm` |
| `OK` | `src/e9/asset_audio_pack_80.asm` | `E9:3A74..E9:7356` | 14562 | 0 | `src/e9/bank_e9_helpers_asar.asm` |
| `OK` | `src/e9/asset_audio_pack_118.asm` | `E9:7356..E9:AC26` | 14544 | 0 | `src/e9/bank_e9_helpers_asar.asm` |
| `OK` | `src/e9/asset_audio_pack_131.asm` | `E9:AC26..E9:E084` | 13406 | 0 | `src/e9/bank_e9_helpers_asar.asm` |
| `OK` | `src/e9/asset_audio_pack_2.asm` | `E9:E084..E9:F8C8` | 6212 | 0 | `src/e9/bank_e9_helpers_asar.asm` |
| `OK` | `src/e9/asset_audio_pack_149.asm` | `E9:F8C8..E9:FF65` | 1693 | 0 | `src/e9/bank_e9_helpers_asar.asm` |
| `OK` | `src/e9/asset_bank_e9_gap_1_tailpadding.asm` | `E9:FF65..E9:10000` | 155 | 0 | `src/e9/bank_e9_helpers_asar.asm` |
