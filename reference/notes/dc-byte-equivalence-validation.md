# DC byte-equivalence validation

This report assembles scratch Asar translations of DC pilot modules into clean ROM copies at their original `org` addresses, then compares the protected byte ranges against the original ROM.

- status: `OK`
- mode: `combined-scaffold`
- modules: `11`
- non-OK modules: `0`
- mismatches: `0`

## Modules

| Status | Source Path | Range | Size | Mismatches | Generated ASM |
| --- | --- | --- | ---: | ---: | --- |
| `OK` | `src/dc/asset_map_data_tile_arrangement_12.asm` | `DC:0000..DC:1FCA` | 8138 | 0 | `build/dc-byte-equivalence/bank-dc-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/dc/asset_map_data_tile_arrangement_13.asm` | `DC:1FCA..DC:593C` | 14706 | 0 | `build/dc-byte-equivalence/bank-dc-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/dc/asset_map_data_tile_arrangement_14.asm` | `DC:593C..DC:687B` | 3903 | 0 | `build/dc-byte-equivalence/bank-dc-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/dc/asset_map_data_tile_arrangement_15.asm` | `DC:687B..DC:72C0` | 2629 | 0 | `build/dc-byte-equivalence/bank-dc-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/dc/asset_map_data_tile_arrangement_18.asm` | `DC:72C0..DC:8E4A` | 7050 | 0 | `build/dc-byte-equivalence/bank-dc-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/dc/asset_map_data_tile_arrangement_19.asm` | `DC:8E4A..DC:B023` | 8665 | 0 | `build/dc-byte-equivalence/bank-dc-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/dc/asset_map_data_tile_set_graphics_14.asm` | `DC:B023..DC:D637` | 9748 | 0 | `build/dc-byte-equivalence/bank-dc-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/dc/table_data_map_per_sector_music_asm.asm` | `DC:D637..DC:E037` | 2560 | 0 | `build/dc-byte-equivalence/bank-dc-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/dc/asset_audio_pack_156.asm` | `DC:E037..DC:F8BF` | 6280 | 0 | `build/dc-byte-equivalence/bank-dc-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/dc/asset_audio_pack_79.asm` | `DC:F8BF..DC:FF92` | 1747 | 0 | `build/dc-byte-equivalence/bank-dc-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/dc/asset_bank_dc_gap_1_tailpadding.asm` | `DC:FF92..DC:10000` | 110 | 0 | `build/dc-byte-equivalence/bank-dc-helper-scaffold.byte-equivalence.asar.asm` |
