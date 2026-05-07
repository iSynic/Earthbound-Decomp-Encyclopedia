# E3 byte-equivalence validation

This report assembles an existing durable Asar source-bank scaffold into a clean ROM copy, then compares the protected byte ranges against the original ROM.

- status: `OK`
- mode: `durable-scaffold`
- modules: `5`
- non-OK modules: `0`
- mismatches: `0`

## Modules

| Status | Source Path | Range | Size | Mismatches | Generated ASM |
| --- | --- | --- | ---: | ---: | --- |
| `OK` | `src/e3/asset_audio_pack_3.asm` | `E3:0000..E3:5F64` | 24420 | 0 | `src/e3/bank_e3_helpers_asar.asm` |
| `OK` | `src/e3/asset_audio_pack_70.asm` | `E3:5F64..E3:B0FA` | 20886 | 0 | `src/e3/bank_e3_helpers_asar.asm` |
| `OK` | `src/e3/asset_audio_pack_37.asm` | `E3:B0FA..E3:FDCC` | 19666 | 0 | `src/e3/bank_e3_helpers_asar.asm` |
| `OK` | `src/e3/asset_audio_pack_32.asm` | `E3:FDCC..E3:FFF2` | 550 | 0 | `src/e3/bank_e3_helpers_asar.asm` |
| `OK` | `src/e3/asset_bank_e3_gap_1_tailpadding.asm` | `E3:FFF2..E3:10000` | 14 | 0 | `src/e3/bank_e3_helpers_asar.asm` |
