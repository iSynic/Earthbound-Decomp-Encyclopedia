# DA byte-equivalence validation

This report assembles scratch Asar translations of DA pilot modules into clean ROM copies at their original `org` addresses, then compares the protected byte ranges against the original ROM.

- status: `OK`
- mode: `combined-scaffold`
- modules: `38`
- non-OK modules: `0`
- mismatches: `0`

## Modules

| Status | Source Path | Range | Size | Mismatches | Generated ASM |
| --- | --- | --- | ---: | ---: | --- |
| `OK` | `src/da/asset_map_data_tile_arrangement_5.asm` | `DA:0000..DA:1342` | 4930 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/asset_map_data_tile_arrangement_6.asm` | `DA:1342..DA:4EA3` | 15201 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/asset_map_data_tile_arrangement_7.asm` | `DA:4EA3..DA:7CA7` | 11780 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/asset_map_data_palette_0.asm` | `DA:7CA7..DA:7FA7` | 768 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/asset_map_data_palette_1.asm` | `DA:7FA7..DA:81E7` | 576 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/asset_map_data_palette_2.asm` | `DA:81E7..DA:84E7` | 768 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/asset_map_data_palette_3.asm` | `DA:84E7..DA:8667` | 384 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/asset_map_data_palette_4.asm` | `DA:8667..DA:87E7` | 384 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/asset_map_data_palette_5.asm` | `DA:87E7..DA:8AE7` | 768 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/asset_map_data_palette_6.asm` | `DA:8AE7..DA:9027` | 1344 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/asset_map_data_palette_7.asm` | `DA:9027..DA:90E7` | 192 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/asset_map_data_palette_8.asm` | `DA:90E7..DA:9267` | 384 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/asset_map_data_palette_9.asm` | `DA:9267..DA:96E7` | 1152 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/asset_map_data_palette_10.asm` | `DA:96E7..DA:9CE7` | 1536 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/asset_map_data_palette_11.asm` | `DA:9CE7..DA:A2E7` | 1536 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/asset_map_data_palette_12.asm` | `DA:A2E7..DA:A8E7` | 1536 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/asset_map_data_palette_13.asm` | `DA:A8E7..DA:ABE7` | 768 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/asset_map_data_palette_14.asm` | `DA:ABE7..DA:B1E7` | 1536 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/asset_map_data_palette_15.asm` | `DA:B1E7..DA:B7E7` | 1536 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/asset_map_data_palette_16.asm` | `DA:B7E7..DA:BAE7` | 768 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/asset_map_data_palette_17.asm` | `DA:BAE7..DA:C0E7` | 1536 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/asset_map_data_palette_18.asm` | `DA:C0E7..DA:C1A7` | 192 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/asset_map_data_palette_19.asm` | `DA:C1A7..DA:C6E7` | 1344 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/asset_map_data_palette_20.asm` | `DA:C6E7..DA:CCE7` | 1536 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/asset_map_data_palette_21.asm` | `DA:CCE7..DA:D0A7` | 960 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/asset_map_data_palette_22.asm` | `DA:D0A7..DA:D467` | 960 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/asset_map_data_palette_23.asm` | `DA:D467..DA:D767` | 768 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/asset_map_data_palette_24.asm` | `DA:D767..DA:DB27` | 960 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/asset_map_data_palette_25.asm` | `DA:DB27..DA:E127` | 1536 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/asset_map_data_palette_26.asm` | `DA:E127..DA:E5A7` | 1152 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/asset_map_data_palette_27.asm` | `DA:E5A7..DA:E967` | 960 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/asset_map_data_palette_28.asm` | `DA:E967..DA:EDE7` | 1152 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/asset_map_data_palette_29.asm` | `DA:EDE7..DA:F267` | 1152 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/asset_map_data_palette_30.asm` | `DA:F267..DA:F4A7` | 576 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/asset_map_data_palette_31.asm` | `DA:F4A7..DA:FAA7` | 1536 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/table_data_map_unknown_map_palette_pointer_table_asm.asm` | `DA:FAA7..DA:FB07` | 96 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/asset_audio_pack_111.asm` | `DA:FB07..DA:FFEE` | 1255 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/da/asset_bank_da_gap_1_tailpadding.asm` | `DA:FFEE..DA:10000` | 18 | 0 | `build/da-byte-equivalence/bank-da-helper-scaffold.byte-equivalence.asar.asm` |
