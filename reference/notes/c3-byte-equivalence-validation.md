# C3 byte-equivalence validation

This report assembles an existing durable Asar source-bank scaffold into a clean ROM copy, then compares the protected byte ranges against the original ROM.

- status: `OK`
- mode: `durable-scaffold`
- modules: `12`
- non-OK modules: `0`
- mismatches: `0`

## Modules

| Status | Source Path | Range | Size | Mismatches | Generated ASM |
| --- | --- | --- | ---: | ---: | --- |
| `OK` | `src/c3/script_event_payloads_0000_e450.asm` | `C3:0000..C3:E450` | 58448 | 0 | `src/c3/bank_c3_helpers_asar.asm` |
| `OK` | `src/c3/window_text_helpers.asm` | `C3:E450..C3:E84E` | 1022 | 0 | `src/c3/bank_c3_helpers_asar.asm` |
| `OK` | `src/c3/data_debug_menu_mixed_inventory_prefix.asm` | `C3:E84E..C3:E977` | 297 | 0 | `src/c3/bank_c3_helpers_asar.asm` |
| `OK` | `src/c3/inventory_equipment_tracked_items.asm` | `C3:E977..C3:EC1F` | 680 | 0 | `src/c3/bank_c3_helpers_asar.asm` |
| `OK` | `src/c3/hp_pp_adjustment_helpers.asm` | `C3:EC1F..C3:EE14` | 501 | 0 | `src/c3/bank_c3_helpers_asar.asm` |
| `OK` | `src/c3/equipment_battle_selector_helpers.asm` | `C3:EE14..C3:EF23` | 271 | 0 | `src/c3/bank_c3_helpers_asar.asm` |
| `OK` | `src/c3/data_battle_menu_tables_ef23_f1ec.asm` | `C3:EF23..C3:F1EC` | 713 | 0 | `src/c3/bank_c3_helpers_asar.asm` |
| `OK` | `src/c3/jeff_repair_psi_helpers.asm` | `C3:F1EC..C3:F2B1` | 197 | 0 | `src/c3/bank_c3_helpers_asar.asm` |
| `OK` | `src/c3/data_battle_visual_tables_f2b1_f5f9.asm` | `C3:F2B1..C3:F3C5` | 276 | 0 | `src/c3/bank_c3_helpers_asar.asm` |
| `OK` | `src/c3/file_select_visual_transition_helper.asm` | `C3:F3C5..C3:F5F9` | 564 | 0 | `src/c3/bank_c3_helpers_asar.asm` |
| `OK` | `src/c3/battle_visual_effect_helpers.asm` | `C3:F5F9..C3:FB1F` | 1318 | 0 | `src/c3/bank_c3_helpers_asar.asm` |
| `OK` | `src/c3/data_battle_tail_and_delivery_payloads_fb1f_10000.asm` | `C3:FB1F..C3:10000` | 1249 | 0 | `src/c3/bank_c3_helpers_asar.asm` |
