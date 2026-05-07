# EA byte-equivalence validation

This report assembles an existing durable Asar source-bank scaffold into a clean ROM copy, then compares the protected byte ranges against the original ROM.

- status: `OK`
- mode: `durable-scaffold`
- modules: `8`
- non-OK modules: `0`
- mismatches: `0`

## Modules

| Status | Source Path | Range | Size | Mismatches | Generated ASM |
| --- | --- | --- | ---: | ---: | --- |
| `OK` | `src/ea/asset_audio_pack_54.asm` | `EA:0000..EA:337A` | 13178 | 0 | `src/ea/bank_ea_helpers_asar.asm` |
| `OK` | `src/ea/asset_audio_pack_52.asm` | `EA:337A..EA:6594` | 12826 | 0 | `src/ea/bank_ea_helpers_asar.asm` |
| `OK` | `src/ea/asset_audio_pack_72.asm` | `EA:6594..EA:96F6` | 12642 | 0 | `src/ea/bank_ea_helpers_asar.asm` |
| `OK` | `src/ea/asset_audio_pack_89.asm` | `EA:96F6..EA:C590` | 11930 | 0 | `src/ea/bank_ea_helpers_asar.asm` |
| `OK` | `src/ea/asset_audio_pack_35.asm` | `EA:C590..EA:F124` | 11156 | 0 | `src/ea/bank_ea_helpers_asar.asm` |
| `OK` | `src/ea/asset_audio_pack_140.asm` | `EA:F124..EA:FE8B` | 3431 | 0 | `src/ea/bank_ea_helpers_asar.asm` |
| `OK` | `src/ea/asset_audio_pack_145.asm` | `EA:FE8B..EA:FFE2` | 343 | 0 | `src/ea/bank_ea_helpers_asar.asm` |
| `OK` | `src/ea/asset_bank_ea_gap_1_tailpadding.asm` | `EA:FFE2..EA:10000` | 30 | 0 | `src/ea/bank_ea_helpers_asar.asm` |
