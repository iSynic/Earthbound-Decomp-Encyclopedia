# E5 byte-equivalence validation

This report assembles an existing durable Asar source-bank scaffold into a clean ROM copy, then compares the protected byte ranges against the original ROM.

- status: `OK`
- mode: `durable-scaffold`
- modules: `6`
- non-OK modules: `0`
- mismatches: `0`

## Modules

| Status | Source Path | Range | Size | Mismatches | Generated ASM |
| --- | --- | --- | ---: | ---: | --- |
| `OK` | `src/e5/asset_audio_pack_50.asm` | `E5:0000..E5:4C4A` | 19530 | 0 | `src/e5/bank_e5_helpers_asar.asm` |
| `OK` | `src/e5/asset_audio_pack_92.asm` | `E5:4C4A..E5:954E` | 18692 | 0 | `src/e5/bank_e5_helpers_asar.asm` |
| `OK` | `src/e5/asset_audio_pack_56.asm` | `E5:954E..E5:DD32` | 18404 | 0 | `src/e5/bank_e5_helpers_asar.asm` |
| `OK` | `src/e5/asset_audio_pack_122.asm` | `E5:DD32..E5:FF38` | 8710 | 0 | `src/e5/bank_e5_helpers_asar.asm` |
| `OK` | `src/e5/asset_audio_pack_166.asm` | `E5:FF38..E5:FFDE` | 166 | 0 | `src/e5/bank_e5_helpers_asar.asm` |
| `OK` | `src/e5/asset_bank_e5_gap_1_tailpadding.asm` | `E5:FFDE..E5:10000` | 34 | 0 | `src/e5/bank_e5_helpers_asar.asm` |
