# E8 byte-equivalence validation

This report assembles an existing durable Asar source-bank scaffold into a clean ROM copy, then compares the protected byte ranges against the original ROM.

- status: `OK`
- mode: `durable-scaffold`
- modules: `7`
- non-OK modules: `0`
- mismatches: `0`

## Modules

| Status | Source Path | Range | Size | Mismatches | Generated ASM |
| --- | --- | --- | ---: | ---: | --- |
| `OK` | `src/e8/asset_audio_pack_84.asm` | `E8:0000..E8:4066` | 16486 | 0 | `src/e8/bank_e8_helpers_asar.asm` |
| `OK` | `src/e8/asset_audio_pack_60.asm` | `E8:4066..E8:7EA6` | 15936 | 0 | `src/e8/bank_e8_helpers_asar.asm` |
| `OK` | `src/e8/asset_audio_pack_153.asm` | `E8:7EA6..E8:BC88` | 15842 | 0 | `src/e8/bank_e8_helpers_asar.asm` |
| `OK` | `src/e8/asset_audio_pack_124.asm` | `E8:BC88..E8:F872` | 15338 | 0 | `src/e8/bank_e8_helpers_asar.asm` |
| `OK` | `src/e8/asset_audio_pack_46.asm` | `E8:F872..E8:FF1B` | 1705 | 0 | `src/e8/bank_e8_helpers_asar.asm` |
| `OK` | `src/e8/asset_audio_pack_7.asm` | `E8:FF1B..E8:FFED` | 210 | 0 | `src/e8/bank_e8_helpers_asar.asm` |
| `OK` | `src/e8/asset_bank_e8_gap_1_tailpadding.asm` | `E8:FFED..E8:10000` | 19 | 0 | `src/e8/bank_e8_helpers_asar.asm` |
