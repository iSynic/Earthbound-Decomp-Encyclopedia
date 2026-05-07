# E7 byte-equivalence validation

This report assembles an existing durable Asar source-bank scaffold into a clean ROM copy, then compares the protected byte ranges against the original ROM.

- status: `OK`
- mode: `durable-scaffold`
- modules: `5`
- non-OK modules: `0`
- mismatches: `0`

## Modules

| Status | Source Path | Range | Size | Mismatches | Generated ASM |
| --- | --- | --- | ---: | ---: | --- |
| `OK` | `src/e7/asset_audio_pack_78.asm` | `E7:0000..E7:4314` | 17172 | 0 | `src/e7/bank_e7_helpers_asar.asm` |
| `OK` | `src/e7/asset_audio_pack_82.asm` | `E7:4314..E7:849C` | 16776 | 0 | `src/e7/bank_e7_helpers_asar.asm` |
| `OK` | `src/e7/asset_audio_pack_8.asm` | `E7:849C..E7:C5C8` | 16684 | 0 | `src/e7/bank_e7_helpers_asar.asm` |
| `OK` | `src/e7/asset_audio_pack_24.asm` | `E7:C5C8..E7:FF64` | 14748 | 0 | `src/e7/bank_e7_helpers_asar.asm` |
| `OK` | `src/e7/asset_bank_e7_gap_1_tailpadding.asm` | `E7:FF64..E7:10000` | 156 | 0 | `src/e7/bank_e7_helpers_asar.asm` |
