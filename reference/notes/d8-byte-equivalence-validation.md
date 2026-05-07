# D8 byte-equivalence validation

This report assembles scratch Asar translations of D8 pilot modules into clean ROM copies at their original `org` addresses, then compares the protected byte ranges against the original ROM.

- status: `OK`
- mode: `combined-scaffold`
- modules: `28`
- non-OK modules: `0`
- mismatches: `0`

## Modules

| Status | Source Path | Range | Size | Mismatches | Generated ASM |
| --- | --- | --- | ---: | ---: | --- |
| `OK` | `src/d8/table_map_tile_collision_data.asm` | `D8:0000..D8:8F50` | 36688 | 0 | `build/d8-byte-equivalence/bank-d8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d8/table_map_data_tile_collision_pointers_0.asm` | `D8:8F50..D8:95D0` | 1664 | 0 | `build/d8-byte-equivalence/bank-d8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d8/table_map_data_tile_collision_pointers_1.asm` | `D8:95D0..D8:9C6A` | 1690 | 0 | `build/d8-byte-equivalence/bank-d8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d8/table_map_data_tile_collision_pointers_2.asm` | `D8:9C6A..D8:A2E0` | 1654 | 0 | `build/d8-byte-equivalence/bank-d8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d8/table_map_data_tile_collision_pointers_3.asm` | `D8:A2E0..D8:A6F8` | 1048 | 0 | `build/d8-byte-equivalence/bank-d8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d8/table_map_data_tile_collision_pointers_4.asm` | `D8:A6F8..D8:AE46` | 1870 | 0 | `build/d8-byte-equivalence/bank-d8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d8/table_map_data_tile_collision_pointers_5.asm` | `D8:AE46..D8:B084` | 574 | 0 | `build/d8-byte-equivalence/bank-d8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d8/table_map_data_tile_collision_pointers_6.asm` | `D8:B084..D8:B75A` | 1750 | 0 | `build/d8-byte-equivalence/bank-d8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d8/table_map_data_tile_collision_pointers_7.asm` | `D8:B75A..D8:BD34` | 1498 | 0 | `build/d8-byte-equivalence/bank-d8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d8/table_map_data_tile_collision_pointers_8.asm` | `D8:BD34..D8:C21C` | 1256 | 0 | `build/d8-byte-equivalence/bank-d8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d8/table_map_data_tile_collision_pointers_9.asm` | `D8:C21C..D8:C966` | 1866 | 0 | `build/d8-byte-equivalence/bank-d8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d8/table_map_data_tile_collision_pointers_10.asm` | `D8:C966..D8:D034` | 1742 | 0 | `build/d8-byte-equivalence/bank-d8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d8/table_map_data_tile_collision_pointers_11.asm` | `D8:D034..D8:D5C6` | 1426 | 0 | `build/d8-byte-equivalence/bank-d8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d8/table_map_data_tile_collision_pointers_12.asm` | `D8:D5C6..D8:D962` | 924 | 0 | `build/d8-byte-equivalence/bank-d8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d8/table_map_data_tile_collision_pointers_13.asm` | `D8:D962..D8:E046` | 1764 | 0 | `build/d8-byte-equivalence/bank-d8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d8/table_map_data_tile_collision_pointers_14.asm` | `D8:E046..D8:E1DC` | 406 | 0 | `build/d8-byte-equivalence/bank-d8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d8/table_map_data_tile_collision_pointers_15.asm` | `D8:E1DC..D8:E2FA` | 286 | 0 | `build/d8-byte-equivalence/bank-d8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d8/table_map_data_tile_collision_pointers_16.asm` | `D8:E2FA..D8:E606` | 780 | 0 | `build/d8-byte-equivalence/bank-d8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d8/table_map_data_tile_collision_pointers_17.asm` | `D8:E606..D8:E8B4` | 686 | 0 | `build/d8-byte-equivalence/bank-d8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d8/table_map_data_tile_collision_pointers_18.asm` | `D8:E8B4..D8:EC2E` | 890 | 0 | `build/d8-byte-equivalence/bank-d8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d8/table_map_data_tile_collision_pointers_19.asm` | `D8:EC2E..D8:F05E` | 1072 | 0 | `build/d8-byte-equivalence/bank-d8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d8/table_anti_piracy_notice_arrangement.asm` | `D8:F05E..D8:F20D` | 431 | 0 | `build/d8-byte-equivalence/bank-d8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d8/table_anti_piracy_notice_graphics.asm` | `D8:F20D..D8:F3BE` | 433 | 0 | `build/d8-byte-equivalence/bank-d8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d8/table_warning_palette.asm` | `D8:F3BE..D8:F3C6` | 8 | 0 | `build/d8-byte-equivalence/bank-d8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d8/table_faulty_game_pak_arrangement.asm` | `D8:F3C6..D8:F5C4` | 510 | 0 | `build/d8-byte-equivalence/bank-d8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d8/table_faulty_game_pak_graphics.asm` | `D8:F5C4..D8:F6B7` | 243 | 0 | `build/d8-byte-equivalence/bank-d8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d8/asset_audio_pack_61.asm` | `D8:F6B7..D8:FFE9` | 2354 | 0 | `build/d8-byte-equivalence/bank-d8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d8/padding_d8_tail_slack.asm` | `D8:FFE9..D8:10000` | 23 | 0 | `build/d8-byte-equivalence/bank-d8-helper-scaffold.byte-equivalence.asar.asm` |
