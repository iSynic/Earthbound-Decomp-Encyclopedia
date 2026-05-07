# DE byte-equivalence validation

This report assembles scratch Asar translations of DE pilot modules into clean ROM copies at their original `org` addresses, then compares the protected byte ranges against the original ROM.

- status: `OK`
- mode: `combined-scaffold`
- modules: `13`
- non-OK modules: `0`
- mismatches: `0`

## Modules

| Status | Source Path | Range | Size | Mismatches | Generated ASM |
| --- | --- | --- | ---: | ---: | --- |
| `OK` | `src/de/asset_map_data_tile_set_graphics_6.asm` | `DE:0000..DE:32C9` | 13001 | 0 | `build/de-byte-equivalence/bank-de-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/de/asset_map_data_tile_set_graphics_7.asm` | `DE:32C9..DE:543F` | 8566 | 0 | `build/de-byte-equivalence/bank-de-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/de/asset_map_data_tile_set_graphics_8.asm` | `DE:543F..DE:747E` | 8255 | 0 | `build/de-byte-equivalence/bank-de-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/de/asset_map_data_tile_set_graphics_2.asm` | `DE:747E..DE:A101` | 11395 | 0 | `build/de-byte-equivalence/bank-de-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/de/asset_map_data_tile_set_graphics_10.asm` | `DE:A101..DE:CE3A` | 11577 | 0 | `build/de-byte-equivalence/bank-de-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/de/asset_map_data_tile_set_graphics_11.asm` | `DE:CE3A..DE:F0E7` | 8877 | 0 | `build/de-byte-equivalence/bank-de-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/de/asset_map_data_tile_animation_gfx_15.asm` | `DE:F0E7..DE:F100` | 25 | 0 | `build/de-byte-equivalence/bank-de-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/de/asset_map_data_tile_animation_gfx_16.asm` | `DE:F100..DE:F2CF` | 463 | 0 | `build/de-byte-equivalence/bank-de-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/de/asset_map_data_tile_animation_gfx_17.asm` | `DE:F2CF..DE:F5EB` | 796 | 0 | `build/de-byte-equivalence/bank-de-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/de/asset_map_data_tile_animation_gfx_18.asm` | `DE:F5EB..DE:F869` | 638 | 0 | `build/de-byte-equivalence/bank-de-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/de/asset_map_data_tile_animation_gfx_19.asm` | `DE:F869..DE:FCDD` | 1140 | 0 | `build/de-byte-equivalence/bank-de-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/de/asset_audio_pack_143.asm` | `DE:FCDD..DE:FFD4` | 759 | 0 | `build/de-byte-equivalence/bank-de-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/de/asset_bank_de_gap_1_tailpadding.asm` | `DE:FFD4..DE:10000` | 44 | 0 | `build/de-byte-equivalence/bank-de-helper-scaffold.byte-equivalence.asar.asm` |
