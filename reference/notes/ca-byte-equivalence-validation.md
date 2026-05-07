# CA byte-equivalence validation

This report assembles scratch Asar translations of CA pilot modules into clean ROM copies at their original `org` addresses, then compares the protected byte ranges against the original ROM.

- status: `OK`
- mode: `combined-scaffold`
- modules: `27`
- non-OK modules: `0`
- mismatches: `0`

## Modules

| Status | Source Path | Range | Size | Mismatches | Generated ASM |
| --- | --- | --- | ---: | ---: | --- |
| `OK` | `src/ca/asset_battle_background_gfx_63.asm` | `CA:0000..CA:2042` | 8258 | 0 | `build/ca-byte-equivalence/bank-ca-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/ca/asset_battle_background_gfx_64.asm` | `CA:2042..CA:382D` | 6123 | 0 | `build/ca-byte-equivalence/bank-ca-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/ca/asset_battle_background_gfx_61.asm` | `CA:382D..CA:480F` | 4066 | 0 | `build/ca-byte-equivalence/bank-ca-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/ca/asset_battle_background_gfx_60.asm` | `CA:480F..CA:5723` | 3860 | 0 | `build/ca-byte-equivalence/bank-ca-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/ca/asset_battle_background_gfx_42.asm` | `CA:5723..CA:65D3` | 3760 | 0 | `build/ca-byte-equivalence/bank-ca-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/ca/asset_battle_background_gfx_38.asm` | `CA:65D3..CA:7314` | 3393 | 0 | `build/ca-byte-equivalence/bank-ca-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/ca/asset_battle_background_gfx_37.asm` | `CA:7314..CA:7F6C` | 3160 | 0 | `build/ca-byte-equivalence/bank-ca-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/ca/asset_battle_background_gfx_43.asm` | `CA:7F6C..CA:8B4F` | 3043 | 0 | `build/ca-byte-equivalence/bank-ca-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/ca/asset_battle_background_gfx_39.asm` | `CA:8B4F..CA:965F` | 2832 | 0 | `build/ca-byte-equivalence/bank-ca-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/ca/asset_battle_background_gfx_41.asm` | `CA:965F..CA:A049` | 2538 | 0 | `build/ca-byte-equivalence/bank-ca-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/ca/asset_battle_background_gfx_62.asm` | `CA:A049..CA:A8F9` | 2224 | 0 | `build/ca-byte-equivalence/bank-ca-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/ca/asset_battle_background_gfx_40.asm` | `CA:A8F9..CA:B092` | 1945 | 0 | `build/ca-byte-equivalence/bank-ca-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/ca/asset_battle_background_arr_37.asm` | `CA:B092..CA:B75B` | 1737 | 0 | `build/ca-byte-equivalence/bank-ca-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/ca/asset_battle_background_gfx_66.asm` | `CA:B75B..CA:BE1E` | 1731 | 0 | `build/ca-byte-equivalence/bank-ca-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/ca/asset_battle_background_arr_38.asm` | `CA:BE1E..CA:C4A1` | 1667 | 0 | `build/ca-byte-equivalence/bank-ca-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/ca/asset_battle_background_arr_39.asm` | `CA:C4A1..CA:CB09` | 1640 | 0 | `build/ca-byte-equivalence/bank-ca-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/ca/asset_battle_background_arr_42.asm` | `CA:CB09..CA:D149` | 1600 | 0 | `build/ca-byte-equivalence/bank-ca-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/ca/asset_battle_background_arr_100.asm` | `CA:D149..CA:D755` | 1548 | 0 | `build/ca-byte-equivalence/bank-ca-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/ca/asset_battle_background_gfx_56.asm` | `CA:D755..CA:D79E` | 73 | 0 | `build/ca-byte-equivalence/bank-ca-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/ca/asset_battle_background_gfx_90.asm` | `CA:D79E..CA:D7A1` | 3 | 0 | `build/ca-byte-equivalence/bank-ca-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/ca/table_data_battle_backgrounds_graphics_pointers_asm.asm` | `CA:D7A1..CA:D93D` | 412 | 0 | `build/ca-byte-equivalence/bank-ca-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/ca/table_data_battle_backgrounds_arrangement_pointers_asm.asm` | `CA:D93D..CA:DAD9` | 412 | 0 | `build/ca-byte-equivalence/bank-ca-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/ca/table_data_battle_backgrounds_palette_pointers_asm.asm` | `CA:DAD9..CA:DCA1` | 456 | 0 | `build/ca-byte-equivalence/bank-ca-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/ca/table_data_battle_backgrounds_config_table_asm.asm` | `CA:DCA1..CA:F258` | 5559 | 0 | `build/ca-byte-equivalence/bank-ca-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/ca/table_data_battle_backgrounds_scrolling_table_asm.asm` | `CA:F258..CA:F708` | 1200 | 0 | `build/ca-byte-equivalence/bank-ca-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/ca/table_data_battle_backgrounds_distortion_table_asm.asm` | `CA:F708..CA:FFFF` | 2295 | 0 | `build/ca-byte-equivalence/bank-ca-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/ca/asset_bank_ca_gap_1_tailpadding.asm` | `CA:FFFF..CA:10000` | 1 | 0 | `build/ca-byte-equivalence/bank-ca-helper-scaffold.byte-equivalence.asar.asm` |
