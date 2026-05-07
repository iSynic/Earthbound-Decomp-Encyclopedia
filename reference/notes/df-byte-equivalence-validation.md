# DF byte-equivalence validation

This report assembles scratch Asar translations of DF pilot modules into clean ROM copies at their original `org` addresses, then compares the protected byte ranges against the original ROM.

- status: `OK`
- mode: `combined-scaffold`
- modules: `24`
- non-OK modules: `0`
- mismatches: `0`

## Modules

| Status | Source Path | Range | Size | Mismatches | Generated ASM |
| --- | --- | --- | ---: | ---: | --- |
| `OK` | `src/df/asset_map_data_tile_set_graphics_12.asm` | `DF:0000..DF:2938` | 10552 | 0 | `build/df-byte-equivalence/bank-df-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/df/asset_map_data_tile_set_graphics_16.asm` | `DF:2938..DF:512A` | 10226 | 0 | `build/df-byte-equivalence/bank-df-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/df/asset_map_data_tile_set_graphics_17.asm` | `DF:512A..DF:6BE8` | 6846 | 0 | `build/df-byte-equivalence/bank-df-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/df/asset_map_data_tile_set_graphics_18.asm` | `DF:6BE8..DF:818B` | 5539 | 0 | `build/df-byte-equivalence/bank-df-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/df/asset_map_data_tile_set_graphics_19.asm` | `DF:818B..DF:9F57` | 7628 | 0 | `build/df-byte-equivalence/bank-df-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/df/asset_map_data_tile_set_graphics_15.asm` | `DF:9F57..DF:C243` | 8940 | 0 | `build/df-byte-equivalence/bank-df-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/df/asset_map_data_tile_animation_gfx_0.asm` | `DF:C243..DF:C93B` | 1784 | 0 | `build/df-byte-equivalence/bank-df-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/df/asset_map_data_tile_animation_gfx_1.asm` | `DF:C93B..DF:CB7F` | 580 | 0 | `build/df-byte-equivalence/bank-df-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/df/asset_map_data_tile_animation_gfx_2.asm` | `DF:CB7F..DF:CB98` | 25 | 0 | `build/df-byte-equivalence/bank-df-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/df/asset_map_data_tile_animation_gfx_3.asm` | `DF:CB98..DF:CBB1` | 25 | 0 | `build/df-byte-equivalence/bank-df-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/df/asset_map_data_tile_animation_gfx_4.asm` | `DF:CBB1..DF:CBCA` | 25 | 0 | `build/df-byte-equivalence/bank-df-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/df/asset_map_data_tile_animation_gfx_5.asm` | `DF:CBCA..DF:D000` | 1078 | 0 | `build/df-byte-equivalence/bank-df-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/df/asset_map_data_tile_animation_gfx_6.asm` | `DF:D000..DF:D6EE` | 1774 | 0 | `build/df-byte-equivalence/bank-df-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/df/asset_map_data_tile_animation_gfx_7.asm` | `DF:D6EE..DF:DD57` | 1641 | 0 | `build/df-byte-equivalence/bank-df-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/df/asset_map_data_tile_animation_gfx_8.asm` | `DF:DD57..DF:E1EB` | 1172 | 0 | `build/df-byte-equivalence/bank-df-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/df/asset_map_data_tile_animation_gfx_9.asm` | `DF:E1EB..DF:E204` | 25 | 0 | `build/df-byte-equivalence/bank-df-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/df/asset_map_data_tile_animation_gfx_10.asm` | `DF:E204..DF:E21D` | 25 | 0 | `build/df-byte-equivalence/bank-df-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/df/asset_map_data_tile_animation_gfx_11.asm` | `DF:E21D..DF:E236` | 25 | 0 | `build/df-byte-equivalence/bank-df-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/df/asset_map_data_tile_animation_gfx_12.asm` | `DF:E236..DF:E402` | 460 | 0 | `build/df-byte-equivalence/bank-df-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/df/asset_map_data_tile_animation_gfx_13.asm` | `DF:E402..DF:E4C8` | 198 | 0 | `build/df-byte-equivalence/bank-df-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/df/asset_map_data_tile_animation_gfx_14.asm` | `DF:E4C8..DF:E4E1` | 25 | 0 | `build/df-byte-equivalence/bank-df-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/df/table_data_map_palette_anim_pointer_table_asm.asm` | `DF:E4E1..DF:EC46` | 1893 | 0 | `build/df-byte-equivalence/bank-df-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/df/asset_audio_pack_4.asm` | `DF:EC46..DF:FFEE` | 5032 | 0 | `build/df-byte-equivalence/bank-df-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/df/asset_bank_df_gap_1_tailpadding.asm` | `DF:FFEE..DF:10000` | 18 | 0 | `build/df-byte-equivalence/bank-df-helper-scaffold.byte-equivalence.asar.asm` |
