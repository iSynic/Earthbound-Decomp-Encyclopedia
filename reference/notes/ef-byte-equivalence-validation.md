# EF byte-equivalence validation

This report assembles an existing durable Asar source-bank scaffold into a clean ROM copy, then compares the protected byte ranges against the original ROM.

- status: `OK`
- mode: `durable-scaffold`
- modules: `28`
- non-OK modules: `0`
- mismatches: `0`

## Modules

| Status | Source Path | Range | Size | Mismatches | Generated ASM |
| --- | --- | --- | ---: | ---: | --- |
| `OK` | `src/ef/ef_0000_00bb_enemy_flashing_helpers.asm` | `EF:0000..EF:00BB` | 187 | 0 | `src/ef/bank_ef_helpers_asar.asm` |
| `OK` | `src/ef/ef_00bb_0256_battle_overworld_visual_helpers.asm` | `EF:00BB..EF:0256` | 411 | 0 | `src/ef/bank_ef_helpers_asar.asm` |
| `OK` | `src/ef/ef_0256_027d_audio_pause_resume_flags.asm` | `EF:0256..EF:027D` | 39 | 0 | `src/ef/bank_ef_helpers_asar.asm` |
| `OK` | `src/ef/ef_027d_0591_overworld_entity_snapshot_helpers.asm` | `EF:027D..EF:0591` | 788 | 0 | `src/ef/bank_ef_helpers_asar.asm` |
| `OK` | `src/ef/ef_0591_05a9_sram_signature_and_save_block_flags.asm` | `EF:0591..EF:05A9` | 24 | 0 | `src/ef/bank_ef_helpers_asar.asm` |
| `OK` | `src/ef/ef_05a9_0c3d_save_sram_helpers.asm` | `EF:05A9..EF:0C3D` | 1684 | 0 | `src/ef/bank_ef_helpers_asar.asm` |
| `OK` | `src/ef/ef_0c3d_0ca7_front_unknown_tail_helpers.asm` | `EF:0C3D..EF:0CA7` | 106 | 0 | `src/ef/bank_ef_helpers_asar.asm` |
| `OK` | `src/ef/ef_0ca7_delivery_selector_helper_cluster.asm` | `EF:0CA7..EF:101B` | 884 | 0 | `src/ef/bank_ef_helpers_asar.asm` |
| `OK` | `src/ef/ef_101b_4a40_map_tileset_sprite_table_data.asm` | `EF:101B..EF:4A40` | 14885 | 0 | `src/ef/bank_ef_helpers_asar.asm` |
| `OK` | `src/ef/ef_4a40_4e20_sound_stone_presentation_table_data.asm` | `EF:4A40..EF:4E20` | 992 | 0 | `src/ef/bank_ef_helpers_asar.asm` |
| `OK` | `src/ef/ef_4e20_c51b_text_payload_data.asm` | `EF:4E20..EF:C51B` | 30459 | 0 | `src/ef/bank_ef_helpers_asar.asm` |
| `OK` | `src/ef/ef_c51b_d56f_text_glyph_mask_tables.asm` | `EF:C51B..EF:D56F` | 4180 | 0 | `src/ef/bank_ef_helpers_asar.asm` |
| `OK` | `src/ef/ef_d56f_d6d4_debug_sound_menu_helpers.asm` | `EF:D56F..EF:D6D4` | 357 | 0 | `src/ef/bank_ef_helpers_asar.asm` |
| `OK` | `src/ef/ef_d6d4_d8b5_debug_sound_menu_controller.asm` | `EF:D6D4..EF:D8B5` | 481 | 0 | `src/ef/bank_ef_helpers_asar.asm` |
| `OK` | `src/ef/ef_d8b5_d95e_debug_menu_option_strings.asm` | `EF:D8B5..EF:D95E` | 169 | 0 | `src/ef/bank_ef_helpers_asar.asm` |
| `OK` | `src/ef/ef_d95e_dabd_debug_menu_graphics_state_init.asm` | `EF:D95E..EF:DABD` | 351 | 0 | `src/ef/bank_ef_helpers_asar.asm` |
| `OK` | `src/ef/ef_dabd_dcbc_debug_menu_text_number_helpers.asm` | `EF:DABD..EF:DCBC` | 511 | 0 | `src/ef/bank_ef_helpers_asar.asm` |
| `OK` | `src/ef/ef_dcbc_de1a_debug_check_position_overlay.asm` | `EF:DCBC..EF:DE1A` | 350 | 0 | `src/ef/bank_ef_helpers_asar.asm` |
| `OK` | `src/ef/ef_de1a_df0b_debug_view_character_overlay.asm` | `EF:DE1A..EF:DF0B` | 241 | 0 | `src/ef/bank_ef_helpers_asar.asm` |
| `OK` | `src/ef/ef_df0b_e175_debug_overlay_tile_helpers.asm` | `EF:DF0B..EF:E175` | 618 | 0 | `src/ef/bank_ef_helpers_asar.asm` |
| `OK` | `src/ef/ef_e175_eb1d_debug_menu_runtime_helpers.asm` | `EF:E175..EF:EB1D` | 2472 | 0 | `src/ef/bank_ef_helpers_asar.asm` |
| `OK` | `src/ef/ef_eb1d_eb2a_debug_color_math_window_table.asm` | `EF:EB1D..EF:EB2A` | 13 | 0 | `src/ef/bank_ef_helpers_asar.asm` |
| `OK` | `src/ef/ef_eb2a_eb3d_debug_color_math_dma_reset.asm` | `EF:EB2A..EF:EB3D` | 19 | 0 | `src/ef/bank_ef_helpers_asar.asm` |
| `OK` | `src/ef/ef_eb3d_eb5f_debug_cursor_tilemap_data.asm` | `EF:EB3D..EF:EB5F` | 34 | 0 | `src/ef/bank_ef_helpers_asar.asm` |
| `OK` | `src/ef/asset_debug_menu_font.asm` | `EF:EB5F..EF:EF70` | 1041 | 0 | `src/ef/bank_ef_helpers_asar.asm` |
| `OK` | `src/ef/table_141_data_unknown_efef70_asm.asm` | `EF:EF70..EF:EFB7` | 71 | 0 | `src/ef/bank_ef_helpers_asar.asm` |
| `OK` | `src/ef/asset_debug_cursor_graphics.asm` | `EF:EFB7..EF:F0D7` | 288 | 0 | `src/ef/bank_ef_helpers_asar.asm` |
| `OK` | `src/ef/asset_bank_ef_gap_1_tailpadding.asm` | `EF:F0D7..EF:10000` | 3881 | 0 | `src/ef/bank_ef_helpers_asar.asm` |
