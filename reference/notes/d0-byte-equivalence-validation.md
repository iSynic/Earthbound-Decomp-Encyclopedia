# D0 byte-equivalence validation

This report assembles scratch Asar translations of D0 pilot modules into clean ROM copies at their original `org` addresses, then compares the protected byte ranges against the original ROM.

- status: `OK`
- mode: `combined-scaffold`
- modules: `11`
- non-OK modules: `0`
- mismatches: `0`

## Modules

| Status | Source Path | Range | Size | Mismatches | Generated ASM |
| --- | --- | --- | ---: | ---: | --- |
| `OK` | `src/d0/table_door_pointer_table.asm` | `D0:0000..D0:1400` | 5120 | 0 | `build/d0-byte-equivalence/bank-d0-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d0/table_screen_transition_config_table.asm` | `D0:1400..D0:1598` | 408 | 0 | `build/d0-byte-equivalence/bank-d0-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d0/table_event_control_ptr_table.asm` | `D0:1598..D0:15C0` | 40 | 0 | `build/d0-byte-equivalence/bank-d0-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d0/table_map_tile_event_control_table.asm` | `D0:15C0..D0:1880` | 704 | 0 | `build/d0-byte-equivalence/bank-d0-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d0/table_map_enemy_placement.asm` | `D0:1880..D0:B880` | 40960 | 0 | `build/d0-byte-equivalence/bank-d0-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d0/table_enemy_placement_groups_ptr_table.asm` | `D0:B880..D0:BBAC` | 812 | 0 | `build/d0-byte-equivalence/bank-d0-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d0/table_enemy_placement_groups_table.asm` | `D0:BBAC..D0:C60D` | 2657 | 0 | `build/d0-byte-equivalence/bank-d0-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d0/table_btl_entry_ptr_table.asm` | `D0:C60D..D0:D52D` | 3872 | 0 | `build/d0-byte-equivalence/bank-d0-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d0/table_enemy_battle_groups_table.asm` | `D0:D52D..D0:DFB4` | 2695 | 0 | `build/d0-byte-equivalence/bank-d0-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d0/asset_audio_pack_139.asm` | `D0:DFB4..D0:FFA8` | 8180 | 0 | `build/d0-byte-equivalence/bank-d0-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/d0/padding_d0_tail_slack.asm` | `D0:FFA8..D0:10000` | 88 | 0 | `build/d0-byte-equivalence/bank-d0-helper-scaffold.byte-equivalence.asar.asm` |
