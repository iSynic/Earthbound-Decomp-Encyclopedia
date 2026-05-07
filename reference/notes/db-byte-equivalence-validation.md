# DB byte-equivalence validation

This report assembles scratch Asar translations of DB pilot modules into clean ROM copies at their original `org` addresses, then compares the protected byte ranges against the original ROM.

- status: `OK`
- mode: `combined-scaffold`
- modules: `8`
- non-OK modules: `0`
- mismatches: `0`

## Modules

| Status | Source Path | Range | Size | Mismatches | Generated ASM |
| --- | --- | --- | ---: | ---: | --- |
| `OK` | `src/db/asset_map_data_tile_arrangement_8.asm` | `DB:0000..DB:26C1` | 9921 | 0 | `build/db-byte-equivalence/bank-db-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/db/asset_map_data_tile_arrangement_9.asm` | `DB:26C1..DB:617F` | 15038 | 0 | `build/db-byte-equivalence/bank-db-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/db/asset_map_data_tile_arrangement_16.asm` | `DB:617F..DB:7C22` | 6819 | 0 | `build/db-byte-equivalence/bank-db-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/db/asset_map_data_tile_arrangement_17.asm` | `DB:7C22..DB:9218` | 5622 | 0 | `build/db-byte-equivalence/bank-db-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/db/asset_map_data_tile_arrangement_10.asm` | `DB:9218..DB:C6CC` | 13492 | 0 | `build/db-byte-equivalence/bank-db-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/db/asset_map_data_tile_arrangement_11.asm` | `DB:C6CC..DB:F2EB` | 11295 | 0 | `build/db-byte-equivalence/bank-db-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/db/asset_audio_pack_65.asm` | `DB:F2EB..DB:FF64` | 3193 | 0 | `build/db-byte-equivalence/bank-db-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/db/asset_bank_db_gap_1_tailpadding.asm` | `DB:FF64..DB:10000` | 156 | 0 | `build/db-byte-equivalence/bank-db-helper-scaffold.byte-equivalence.asar.asm` |
