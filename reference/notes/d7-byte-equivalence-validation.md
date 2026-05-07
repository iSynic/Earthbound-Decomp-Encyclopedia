# D7 byte-equivalence validation

This report assembles scratch Asar translations of D7 pilot modules into clean ROM copies at their original `org` addresses, then compares the protected byte ranges against the original ROM.

- status: `OK`
- mode: `combined-scaffold`
- modules: `7`
- non-OK modules: `0`
- mismatches: `0`

## Modules

| Status | Source Path | Range | Size | Mismatches | Generated ASM |
| --- | --- | --- | ---: | ---: | --- |
| `OK` | `src/d7/asset_map_data_tile_table_chunk_7.asm` | `D7:0000..D7:2800` | 10240 | 0 | `build/d7-byte-equivalence/bank-d7-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d7/asset_map_data_tile_table_chunk_8.asm` | `D7:2800..D7:5000` | 10240 | 0 | `build/d7-byte-equivalence/bank-d7-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d7/asset_map_data_tile_table_chunk_9.asm` | `D7:5000..D7:8000` | 12288 | 0 | `build/d7-byte-equivalence/bank-d7-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d7/asset_map_data_tile_table_chunk_10.asm` | `D7:8000..D7:A800` | 10240 | 0 | `build/d7-byte-equivalence/bank-d7-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d7/table_data_map_global_tileset_palette_data_asm.asm` | `D7:A800..D7:C600` | 7680 | 0 | `build/d7-byte-equivalence/bank-d7-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d7/asset_map_data_tile_arrangement_0.asm` | `D7:C600..D7:FBE8` | 13800 | 0 | `build/d7-byte-equivalence/bank-d7-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d7/asset_bank_d7_gap_1_tailpadding.asm` | `D7:FBE8..D7:10000` | 1048 | 0 | `build/d7-byte-equivalence/bank-d7-helper-scaffold.byte-equivalence.asar.asm` |
