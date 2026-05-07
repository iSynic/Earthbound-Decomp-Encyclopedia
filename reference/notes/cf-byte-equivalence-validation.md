# CF byte-equivalence validation

This report assembles an existing durable Asar source-bank scaffold into a clean ROM copy, then compares the protected byte ranges against the original ROM.

- status: `OK`
- mode: `durable-scaffold`
- modules: `11`
- non-OK modules: `0`
- mismatches: `0`

## Modules

| Status | Source Path | Range | Size | Mismatches | Generated ASM |
| --- | --- | --- | ---: | ---: | --- |
| `OK` | `src/cf/table_door_data.asm` | `CF:0000..CF:264F` | 9807 | 0 | `src/cf/bank_cf_helpers_asar.asm` |
| `OK` | `src/cf/table_door_config_table.asm` | `CF:264F..CF:58EF` | 12960 | 0 | `src/cf/bank_cf_helpers_asar.asm` |
| `OK` | `src/cf/table_overworld_event_music_pointer_table.asm` | `CF:58EF..CF:5A39` | 330 | 0 | `src/cf/bank_cf_helpers_asar.asm` |
| `OK` | `src/cf/table_overworld_event_music_table.asm` | `CF:5A39..CF:61DD` | 1956 | 0 | `src/cf/bank_cf_helpers_asar.asm` |
| `OK` | `src/cf/table_cf_inline_event_music_trailer.asm` | `CF:61DD..CF:61E7` | 10 | 0 | `src/cf/bank_cf_helpers_asar.asm` |
| `OK` | `src/cf/table_sprite_placement_pointer_table.asm` | `CF:61E7..CF:6BE7` | 2560 | 0 | `src/cf/bank_cf_helpers_asar.asm` |
| `OK` | `src/cf/table_sprite_placement_table.asm` | `CF:6BE7..CF:8985` | 7582 | 0 | `src/cf/bank_cf_helpers_asar.asm` |
| `OK` | `src/cf/table_npc_config_table.asm` | `CF:8985..CF:F2B5` | 26928 | 0 | `src/cf/bank_cf_helpers_asar.asm` |
| `OK` | `src/cf/asset_audio_pack_94.asm` | `CF:F2B5..CF:FF38` | 3203 | 0 | `src/cf/bank_cf_helpers_asar.asm` |
| `OK` | `src/cf/asset_audio_pack_96.asm` | `CF:FF38..CF:FFF9` | 193 | 0 | `src/cf/bank_cf_helpers_asar.asm` |
| `OK` | `src/cf/padding_cf_tail_slack.asm` | `CF:FFF9..CF:10000` | 7 | 0 | `src/cf/bank_cf_helpers_asar.asm` |
