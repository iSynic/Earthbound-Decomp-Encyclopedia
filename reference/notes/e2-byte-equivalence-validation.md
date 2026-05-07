# E2 byte-equivalence validation

This report assembles an existing durable Asar source-bank scaffold into a clean ROM copy, then compares the protected byte ranges against the original ROM.

- status: `OK`
- mode: `durable-scaffold`
- modules: `5`
- non-OK modules: `0`
- mismatches: `0`

## Modules

| Status | Source Path | Range | Size | Mismatches | Generated ASM |
| --- | --- | --- | ---: | ---: | --- |
| `OK` | `src/e2/asset_audio_pack_108.asm` | `E2:0000..E2:77F0` | 30704 | 0 | `src/e2/bank_e2_helpers_asar.asm` |
| `OK` | `src/e2/asset_audio_pack_0.asm` | `E2:77F0..E2:ED2C` | 30012 | 0 | `src/e2/bank_e2_helpers_asar.asm` |
| `OK` | `src/e2/asset_audio_pack_36.asm` | `E2:ED2C..E2:FC88` | 3932 | 0 | `src/e2/bank_e2_helpers_asar.asm` |
| `OK` | `src/e2/asset_audio_pack_18.asm` | `E2:FC88..E2:FFFD` | 885 | 0 | `src/e2/bank_e2_helpers_asar.asm` |
| `OK` | `src/e2/asset_bank_e2_gap_1_tailpadding.asm` | `E2:FFFD..E2:10000` | 3 | 0 | `src/e2/bank_e2_helpers_asar.asm` |
