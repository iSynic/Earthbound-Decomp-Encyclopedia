# D6 byte-equivalence validation

This report assembles scratch Asar translations of D6 pilot modules into clean ROM copies at their original `org` addresses, then compares the protected byte ranges against the original ROM.

- status: `OK`
- mode: `combined-scaffold`
- modules: `6`
- non-OK modules: `0`
- mismatches: `0`

## Modules

| Status | Source Path | Range | Size | Mismatches | Generated ASM |
| --- | --- | --- | ---: | ---: | --- |
| `OK` | `src/d6/asset_map_data_tile_table_chunk_1.asm` | `D6:0000..D6:2800` | 10240 | 0 | `build/d6-byte-equivalence/bank-d6-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d6/asset_map_data_tile_table_chunk_2.asm` | `D6:2800..D6:5000` | 10240 | 0 | `build/d6-byte-equivalence/bank-d6-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d6/asset_map_data_tile_table_chunk_3.asm` | `D6:5000..D6:8000` | 12288 | 0 | `build/d6-byte-equivalence/bank-d6-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d6/asset_map_data_tile_table_chunk_4.asm` | `D6:8000..D6:A800` | 10240 | 0 | `build/d6-byte-equivalence/bank-d6-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d6/asset_map_data_tile_table_chunk_5.asm` | `D6:A800..D6:D000` | 10240 | 0 | `build/d6-byte-equivalence/bank-d6-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d6/asset_map_data_tile_table_chunk_6.asm` | `D6:D000..D6:10000` | 12288 | 0 | `build/d6-byte-equivalence/bank-d6-helper-scaffold.byte-equivalence.asar.asm` |
