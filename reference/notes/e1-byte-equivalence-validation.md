# E1 byte-equivalence validation

This report assembles scratch Asar translations of E1 pilot modules into clean ROM copies at their original `org` addresses, then compares the protected byte ranges against the original ROM.

- status: `OK`
- mode: `combined-scaffold`
- modules: `53`
- non-OK modules: `0`
- mismatches: `0`

## Modules

| Status | Source Path | Range | Size | Mismatches | Generated ASM |
| --- | --- | --- | ---: | ---: | --- |
| `OK` | `src/e1/table_000_localeinclude_coffee_flyover.asm` | `E1:0000..E1:0C7A` | 3194 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_main_font_data.asm` | `E1:0C7A..E1:0CDA` | 96 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_main_font_gfx.asm` | `E1:0CDA..E1:18DA` | 3072 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_battle_font_data.asm` | `E1:18DA..E1:193A` | 96 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_battle_font_gfx.asm` | `E1:193A..E1:1F3A` | 1536 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_tiny_font_data.asm` | `E1:1F3A..E1:1F9A` | 96 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_tiny_font_gfx.asm` | `E1:1F9A..E1:229A` | 768 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_large_font_data.asm` | `E1:229A..E1:22FA` | 96 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_large_font_gfx.asm` | `E1:22FA..E1:2EFA` | 3072 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/table_011_data_cast_sequence_formatting_asm.asm` | `E1:2EFA..E1:2F8A` | 144 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/table_012_data_photographer_cfg_asm.asm` | `E1:2F8A..E1:374A` | 1984 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_compressed_palette_unknown.asm` | `E1:374A..E1:413F` | 2549 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/table_014_data_credits_asm.asm` | `E1:413F..E1:4DE8` | 3241 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/table_015_unknown_e1_e14de8_asm.asm` | `E1:4DE8..E1:4EC1` | 217 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_ape_arrangement.asm` | `E1:4EC1..E1:4F2A` | 105 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_ape_graphics.asm` | `E1:4F2A..E1:5130` | 518 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_ape_palette.asm` | `E1:5130..E1:5174` | 68 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_halken_arrangement.asm` | `E1:5174..E1:51E8` | 116 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_halken_graphics.asm` | `E1:51E8..E1:53B8` | 464 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_halken_palette.asm` | `E1:53B8..E1:5455` | 157 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_nintendo_arrangement.asm` | `E1:5455..E1:549E` | 73 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_nintendo_graphics.asm` | `E1:549E..E1:558F` | 241 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_nintendo_palette.asm` | `E1:558F..E1:55D3` | 68 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_gas_station_arrangement.asm` | `E1:55D3..E1:5B33` | 1376 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_gas_station_graphics.asm` | `E1:5B33..E1:A9B7` | 20100 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_gas_station_palette.asm` | `E1:A9B7..E1:AA5D` | 166 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_gas_station_palette_2.asm` | `E1:AA5D..E1:AADF` | 130 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_produced_itoi_arrangement.asm` | `E1:AADF..E1:AB4B` | 108 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_produced_itoi_graphics.asm` | `E1:AB4B..E1:AD01` | 438 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_nintendo_presentation_arrangement.asm` | `E1:AD01..E1:AD4E` | 77 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_nintendo_presentation_graphics.asm` | `E1:AD4E..E1:AE6F` | 289 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_nintendo_itoi_palette.asm` | `E1:AE6F..E1:AE7C` | 13 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_unknown_e1ae7c.asm` | `E1:AE7C..E1:AF7D` | 257 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_title_screen_arrangement.asm` | `E1:AF7D..E1:B211` | 660 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_title_screen_graphics.asm` | `E1:B211..E1:C6E5` | 5332 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_unknown_e1c6e5.asm` | `E1:C6E5..E1:CDE1` | 1788 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_title_screen_palette.asm` | `E1:CDE1..E1:CE08` | 39 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/table_041_data_unknown_e1ce08_asm.asm` | `E1:CE08..E1:CFAF` | 423 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_unknown_e1cfaf.asm` | `E1:CFAF..E1:D4F4` | 1349 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_unknown_e1d4f4.asm` | `E1:D4F4..E1:D5E8` | 244 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_unknown_e1d5e8.asm` | `E1:D5E8..E1:D6E1` | 249 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_cast_scene_prelude_gfx.asm` | `E1:D6E1..E1:D815` | 308 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/table_042_data_unknown_e1d815_asm.asm` | `E1:D815..E1:D835` | 32 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_cast_names_gfx.asm` | `E1:D835..E1:E4E6` | 3249 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_unknown_e1e4e6.asm` | `E1:E4E6..E1:E528` | 66 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_staff_credits_font_graphics.asm` | `E1:E528..E1:E914` | 1004 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_staff_credits_font_palette.asm` | `E1:E914..E1:E924` | 16 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/table_051_data_unknown_e1e924_asm.asm` | `E1:E924..E1:EA50` | 300 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_town_map_label_gfx.asm` | `E1:EA50..E1:F1C3` | 1907 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_town_map_icon_palette.asm` | `E1:F1C3..E1:F203` | 64 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/table_055_data_unknown_e1f203_asm.asm` | `E1:F203..E1:F581` | 894 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_audio_pack_123.asm` | `E1:F581..E1:FFF2` | 2673 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e1/asset_bank_e1_gap_1_tailpadding.asm` | `E1:FFF2..E1:10000` | 14 | 0 | `build/e1-byte-equivalence/bank-e1-helper-scaffold.byte-equivalence.asar.asm` |
