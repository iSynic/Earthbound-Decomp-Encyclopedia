# ebsrc Bank EF Reference Map

Generated from ebsrc bankconfig include order, ebsrc bank symbols, and local source-bank build-candidate spans.

## Summary

- includes: `164`
- exact spans: `94`
- promoted exact spans: `94`
- promotion candidates: `0`
- open/unresolved entries: `55`
- latest promoted end: `EF:F5BD`

## Current Open Frontier

| Start | End | Size | Status | Include | ebsrc Symbol | Local Name | Kind |
| --- | --- | ---: | --- | --- | --- | --- | --- |

## Current Exact Frontier Candidates

| Start | End | Size | Include | ebsrc Symbol | Local Name | Kind |
| --- | --- | ---: | --- | --- | --- | --- |

## Candidate Backlog

| Start | End | Size | Include | ebsrc Symbol | Local Name | Kind |
| --- | --- | ---: | --- | --- | --- | --- |

## Include Map

| # | Start | End | Size | Status | Promoted | Include | ebsrc Symbol | Local Name |
| ---: | --- | --- | ---: | --- | --- | --- | --- | --- |
| 0 |  |  | 0 | `support` |  | `common.asm` | `` | `` |
| 1 |  |  | 0 | `support` |  | `config.asm` | `` | `` |
| 2 |  |  | 0 | `support` |  | `structs.asm` | `` | `` |
| 3 |  |  | 0 | `support` |  | `symbols/bank00.inc.asm` | `` | `` |
| 4 |  |  | 0 | `support` |  | `symbols/bank01.inc.asm` | `` | `` |
| 5 |  |  | 0 | `support` |  | `symbols/bank02.inc.asm` | `` | `` |
| 6 |  |  | 0 | `support` |  | `symbols/bank03.inc.asm` | `` | `` |
| 7 |  |  | 0 | `support` |  | `symbols/bank04.inc.asm` | `` | `` |
| 8 |  |  | 0 | `support` |  | `symbols/bank2f.inc.asm` | `` | `` |
| 9 |  |  | 0 | `support` |  | `symbols/globals.inc.asm` | `` | `` |
| 10 |  |  | 0 | `support` |  | `symbols/map.inc.asm` | `` | `` |
| 11 |  |  | 0 | `support` |  | `symbols/misc.inc.asm` | `` | `` |
| 12 |  |  | 0 | `support` |  | `symbols/overworld_sprites.inc.asm` | `` | `` |
| 13 |  |  | 0 | `support` |  | `symbols/sram.inc.asm` | `` | `` |
| 14 |  |  | 0 | `support` |  | `symbols/text.inc.asm` | `` | `` |
| 15 |  |  | 0 | `open` |  | `battle/enemy_flashing_off.asm` | `ENEMY_FLASHING_OFF` | `` |
| 16 |  |  | 0 | `open` |  | `battle/enemy_flashing_on.asm` | `ENEMY_FLASHING_ON` | `` |
| 17 | EF:00BB | EF:0256 | 411 | `exact` | yes | `unknown/EF/EF00BB.asm` | `UNKNOWN_EF00BB` | `` |
| 18 | EF:00E6 | EF:0115 | 47 | `exact` | yes | `unknown/EF/EF00E6.asm` | `UNKNOWN_EF00E6` | `` |
| 19 | EF:0115 | EF:016F | 90 | `exact` | yes | `unknown/EF/EF0115.asm` | `UNKNOWN_EF0115` | `` |
| 20 | EF:016F | EF:01D2 | 99 | `exact` | yes | `unknown/EF/EF016F.asm` | `UNKNOWN_EF016F` | `` |
| 21 | EF:01D2 |  | 0 | `open` |  | `unknown/EF/EF01D2.asm` | `UNKNOWN_EF01D2` | `` |
| 22 |  |  | 0 | `open` |  | `audio/pause_music.asm` | `PAUSE_MUSIC` | `` |
| 23 | EF:0262 |  | 0 | `open` |  | `unknown/EF/EF0262.asm` | `UNKNOWN_EF0262` | `` |
| 24 |  |  | 0 | `open` |  | `audio/resume_music.asm` | `RESUME_MUSIC` | `` |
| 25 | EF:027D | EF:0591 | 788 | `exact` | yes | `unknown/EF/EF027D.asm` | `UNKNOWN_EF027D` | `` |
| 26 | EF:02C4 | EF:031E | 90 | `exact` | yes | `unknown/EF/EF02C4.asm` | `` | `` |
| 27 | EF:031E | EF:04DC | 446 | `exact` | yes | `unknown/EF/EF031E.asm` | `UNKNOWN_EF031E` | `` |
| 28 | EF:04DC |  | 0 | `open` |  | `unknown/EF/EF04DC.asm` | `UNKNOWN_EF04DC` | `` |
| 29 |  |  | 0 | `open` |  | `data/sram_signature.asm` | `SRAM_SIGNATURE` | `` |
| 30 | EF:05A6 |  | 0 | `open` |  | `data/unknown/EF05A6.asm` | `UNKNOWN_EF05A6` | `` |
| 31 |  |  | 0 | `open` |  | `system/saves/erase_save_block.asm` | `` | `` |
| 32 |  |  | 0 | `open` |  | `system/saves/check_block_signature.asm` | `` | `` |
| 33 |  |  | 0 | `open` |  | `system/saves/check_all_blocks_signature.asm` | `` | `` |
| 34 |  |  | 0 | `open` |  | `system/saves/copy_save_block.asm` | `` | `` |
| 35 |  |  | 0 | `open` |  | `system/saves/calc_save_block_checksum.asm` | `` | `` |
| 36 |  |  | 0 | `open` |  | `system/saves/calc_save_block_checksum_complement.asm` | `` | `` |
| 37 |  |  | 0 | `open` |  | `system/saves/validate_save_block_checksums.asm` | `` | `` |
| 38 |  |  | 0 | `open` |  | `system/saves/check_save_corruption.asm` | `` | `` |
| 39 |  |  | 0 | `open` |  | `system/saves/save_game_block.asm` | `` | `` |
| 40 |  |  | 0 | `open` |  | `system/saves/save_game_slot.asm` | `SAVE_GAME_SLOT` | `` |
| 41 |  |  | 0 | `open` |  | `system/saves/load_game_slot.asm` | `LOAD_GAME_SLOT` | `` |
| 42 |  |  | 0 | `open` |  | `system/saves/check_sram_integrity.asm` | `CHECK_SRAM_INTEGRITY` | `` |
| 43 |  |  | 0 | `open` |  | `system/saves/erase_save_slot.asm` | `` | `` |
| 44 |  |  | 0 | `open` |  | `system/saves/copy_save_slot.asm` | `` | `` |
| 45 | EF:0C3D | EF:0CA7 | 106 | `exact` | yes | `unknown/EF/EF0C3D.asm` | `UNKNOWN_EF0C3D` | `` |
| 46 | EF:0C87 | EF:0C97 | 16 | `exact` | yes | `unknown/EF/EF0C87.asm` | `UNKNOWN_EF0C87` | `` |
| 47 | EF:0C97 | EF:0CA7 | 16 | `exact` | yes | `unknown/EF/EF0C97.asm` | `UNKNOWN_EF0C97` | `` |
| 48 | EF:0CA7 | EF:101B | 884 | `exact` | yes | `unknown/EF/EF0CA7.asm` | `UNKNOWN_EF0CA7` | `` |
| 49 | EF:0D23 | EF:0D46 | 35 | `exact` | yes | `unknown/EF/EF0D23.asm` | `UNKNOWN_EF0D23` | `` |
| 50 | EF:0D46 | EF:0D73 | 45 | `exact` | yes | `unknown/EF/EF0D46.asm` | `UNKNOWN_EF0D46` | `` |
| 51 | EF:0D73 | EF:0D8D | 26 | `exact` | yes | `unknown/EF/EF0D73.asm` | `UNKNOWN_EF0D73` | `` |
| 52 | EF:0D8D | EF:0DFA | 109 | `exact` | yes | `unknown/EF/EF0D8D.asm` | `UNKNOWN_EF0D8D` | `` |
| 53 | EF:0DFA | EF:0E67 | 109 | `exact` | yes | `unknown/EF/EF0DFA.asm` | `UNKNOWN_EF0DFA` | `` |
| 54 | EF:0E67 | EF:0E8A | 35 | `exact` | yes | `unknown/EF/EF0E67.asm` | `UNKNOWN_EF0E67` | `` |
| 55 | EF:0E8A | EF:0EAD | 35 | `exact` | yes | `unknown/EF/EF0E8A.asm` | `UNKNOWN_EF0E8A` | `` |
| 56 | EF:0EAD | EF:0EE8 | 59 | `exact` | yes | `unknown/EF/EF0EAD.asm` | `` | `` |
| 57 | EF:0EE8 | EF:0F60 | 120 | `exact` | yes | `unknown/EF/EF0EE8.asm` | `UNKNOWN_EF0EE8` | `` |
| 58 | EF:0F60 | EF:0FDB | 123 | `exact` | yes | `unknown/EF/EF0F60.asm` | `UNKNOWN_EF0F60` | `` |
| 59 | EF:0FDB | EF:0FF6 | 27 | `exact` | yes | `unknown/EF/EF0FDB.asm` | `UNKNOWN_EF0FDB` | `` |
| 60 | EF:0FF6 |  | 0 | `open` |  | `unknown/EF/EF0FF6.asm` | `UNKNOWN_EF0FF6` | `` |
| 61 |  |  | 0 | `open` |  | `data/map/tileset_table.asm` | `TILESET_TABLE` | `` |
| 62 |  |  | 0 | `open` |  | `data/map/tileset_graphics_pointer_table.asm` | `` | `` |
| 63 |  |  | 0 | `open` |  | `data/map/tileset_arrangement_pointer_table.asm` | `` | `` |
| 64 |  |  | 0 | `open` |  | `data/map/tileset_palette_pointer_table.asm` | `` | `` |
| 65 |  |  | 0 | `open` |  | `data/map/tileset_collision_pointer_table.asm` | `` | `` |
| 66 |  |  | 0 | `open` |  | `data/map/tileset_animation_pointer_table.asm` | `` | `` |
| 67 |  |  | 0 | `open` |  | `data/map/tileset_animation_properties_pointer_table.asm` | `` | `` |
| 68 |  |  | 0 | `open` |  | `data/map/tileset_animation_properties/00.asm` | `` | `` |
| 69 |  |  | 0 | `open` |  | `data/map/tileset_animation_properties/01.asm` | `` | `` |
| 70 |  |  | 0 | `open` |  | `data/map/tileset_animation_properties/02.asm` | `` | `` |
| 71 |  |  | 0 | `open` |  | `data/map/tileset_animation_properties/03.asm` | `` | `` |
| 72 |  |  | 0 | `open` |  | `data/map/tileset_animation_properties/04.asm` | `` | `` |
| 73 |  |  | 0 | `open` |  | `data/map/tileset_animation_properties/05.asm` | `` | `` |
| 74 |  |  | 0 | `open` |  | `data/map/tileset_animation_properties/06.asm` | `` | `` |
| 75 |  |  | 0 | `open` |  | `data/map/tileset_animation_properties/07.asm` | `` | `` |
| 76 |  |  | 0 | `open` |  | `data/map/tileset_animation_properties/08.asm` | `` | `` |
| 77 |  |  | 0 | `open` |  | `data/map/tileset_animation_properties/09.asm` | `` | `` |
| 78 |  |  | 0 | `open` |  | `data/map/tileset_animation_properties/10.asm` | `` | `` |
| 79 |  |  | 0 | `open` |  | `data/map/tileset_animation_properties/11.asm` | `` | `` |
| 80 |  |  | 0 | `open` |  | `data/map/tileset_animation_properties/12.asm` | `` | `` |
| 81 |  |  | 0 | `open` |  | `data/map/tileset_animation_properties/13.asm` | `` | `` |
| 82 |  |  | 0 | `open` |  | `data/map/tileset_animation_properties/14.asm` | `` | `` |
| 83 |  |  | 0 | `open` |  | `data/map/tileset_animation_properties/15.asm` | `` | `` |
| 84 |  |  | 0 | `open` |  | `data/map/tileset_animation_properties/16.asm` | `` | `` |
| 85 |  |  | 0 | `open` |  | `data/map/tileset_animation_properties/17.asm` | `` | `` |
| 86 |  |  | 0 | `open` |  | `data/map/tileset_animation_properties/18.asm` | `` | `` |
| 87 |  |  | 0 | `open` |  | `data/map/tileset_animation_properties/19.asm` | `` | `` |
| 88 |  |  | 0 | `open` |  | `data/sprite_grouping_pointers.asm` | `` | `` |
| 89 |  |  | 0 | `open` |  | `data/sprite_grouping_data.asm` | `SPRITE_GROUPING_DATA` | `` |
| 90 | EF:4A40 | EF:4E20 | 992 | `exact` | yes | `data/unknown/EF4A40.asm` | `UNKNOWN_EF4A40` | `` |
| 91 | EF:4E20 | EF:4E38 | 24 | `exact` | yes | `text_data/EEXPLPSI.ebtxt` | `` | `` |
| 92 | EF:4E38 | EF:4E51 | 25 | `exact` | yes | `text_data/E16DKFD.ebtxt` | `` | `` |
| 93 | EF:4E51 | EF:4E6A | 25 | `exact` | yes | `text_data/E07GPFT.ebtxt` | `` | `` |
| 94 | EF:4E6A | EF:4E83 | 25 | `exact` | yes | `text_data/EBATTLE5.ebtxt` | `` | `` |
| 95 | EF:4E83 | EF:4E99 | 22 | `exact` | yes | `text_data/EBATTLE4.ebtxt` | `` | `` |
| 96 | EF:4E99 | EF:4EB0 | 23 | `exact` | yes | `text_data/EBATTLE8.ebtxt` | `` | `` |
| 97 | EF:4EB0 | EF:4EC7 | 23 | `exact` | yes | `text_data/EBATTLE2.ebtxt` | `` | `` |
| 98 | EF:4EC7 | EF:4EDE | 23 | `exact` | yes | `text_data/EBATTLE0.ebtxt` | `` | `` |
| 99 | EF:4EDE | EF:4F06 | 40 | `exact` | yes | `text_data/EBATTLE3.ebtxt` | `` | `` |
| 100 | EF:4F06 | EF:4F2E | 40 | `exact` | yes | `text_data/EBATTLE9.ebtxt` | `` | `` |
| 101 | EF:4F2E | EF:4F56 | 40 | `exact` | yes | `text_data/E04GRFD.ebtxt` | `` | `` |
| 102 | EF:4F56 | EF:4F7E | 40 | `exact` | yes | `text_data/EBATTLE1.ebtxt` | `` | `` |
| 103 | EF:4F7E | EF:4FA6 | 40 | `exact` | yes | `text_data/EGOODS2.ebtxt` | `` | `` |
| 104 | EF:A2FA | EF:A37A | 128 | `exact` | yes | `text_data/UNKNOWN_EFA2FA.ebtxt` | `` | `` |
| 105 | EF:A37A | EF:A3B6 | 60 | `exact` | yes | `data/command_window_text.asm` | `` | `` |
| 106 | EF:A3B6 | EF:A459 | 163 | `exact` | yes | `data/status_window_text.asm` | `STATUS_WINDOW_TEXT` | `` |
| 107 | EF:A459 | EF:A460 | 7 | `exact` | yes | `text_data/KEYBOARD.ebtxt` | `` | `` |
| 108 | EF:A460 | EF:A4E3 | 131 | `exact` | yes | `data/name_input_window_selection_layout_pointers.asm` | `NAME_INPUT_WINDOW_SELECTION_LAYOUT_POINTERS` | `` |
| 109 | EF:A4E3 | EF:A566 | 131 | `exact` | yes | `text_data/UNKNOWN7.ebtxt` | `` | `` |
| 110 | EF:A566 | EF:A5E9 | 131 | `exact` | yes | `data/map/per_sector_town_map_data.asm` | `` | `` |
| 111 | EF:A5E9 | EF:A66C | 131 | `exact` | yes | `data/map/town_map_mapping.asm` | `TOWN_MAP_MAPPING` | `` |
| 112 | EF:C51B | EF:CD1B | 2048 | `exact` | yes | `data/unknown/EFC51B.asm` | `UNKNOWN_EFC51B` | `` |
| 113 | EF:CD1B | EF:D51B | 2048 | `exact` | yes | `data/unknown/EFCD1B.asm` | `UNKNOWN_EFCD1B` | `` |
| 114 | EF:D51B | EF:D56F | 84 | `exact` | yes | `data/debug/sound_menu_option_strings.asm` | `` | `` |
| 115 | EF:D56F | EF:D6D4 | 357 | `exact` | yes | `unknown/EF/EFD56F.asm` | `` | `` |
| 116 | EF:D5D9 | EF:D6D4 | 251 | `exact` | yes | `unknown/EF/EFD5D9.asm` | `` | `` |
| 117 | EF:D6D4 | EF:D8B5 | 481 | `exact` | yes | `unknown/EF/EFD6D4.asm` | `UNKNOWN_EFD6D4` | `` |
| 118 | EF:D8B5 | EF:D8D6 | 33 | `exact` | yes | `data/debug/menu_option_strings.asm` | `` | `` |
| 119 | EF:D95E | EF:DABD | 351 | `exact` | yes | `unknown/EF/EFD95E.asm` | `UNKNOWN_EFD95E` | `` |
| 120 | EF:D9F3 | EF:DA05 | 18 | `exact` | yes | `unknown/EF/EFD9F3.asm` | `UNKNOWN_EFD9F3` | `` |
| 121 | EF:DA05 | EF:DABD | 184 | `exact` | yes | `unknown/EF/EFDA05.asm` | `` | `` |
| 122 | EF:DABD | EF:DCBC | 511 | `exact` | yes | `unknown/EF/EFDABD.asm` | `` | `` |
| 123 | EF:DCBC | EF:DE1A | 350 | `exact` | yes | `system/debug/display_menu_options.asm` | `` | `` |
| 124 | EF:DE1A | EF:DF0B | 241 | `exact` | yes | `system/debug/integer_to_hex_debug_tiles.asm` | `` | `` |
| 125 | EF:DF0B | EF:E175 | 618 | `exact` | yes | `system/debug/integer_to_decimal_debug_tiles.asm` | `` | `` |
| 126 | EF:E175 | EF:EB1D | 2472 | `exact` | yes | `system/debug/integer_to_binary_debug_tiles.asm` | `` | `` |
| 127 | EF:EB1D | EF:EB2A | 13 | `exact` | yes | `system/debug/display_check_position_debug_overlay.asm` | `UNKNOWN_EFEB1D` | `` |
| 128 | EF:EB2A | EF:EB3D | 19 | `exact` | yes | `system/debug/display_view_character_debug_overlay.asm` | `UNKNOWN_EFEB2A` | `` |
| 129 | EF:DF0B | EF:E175 | 618 | `exact` | yes | `unknown/EF/EFDF0B.asm` | `` | `` |
| 130 | EF:DFC4 | EF:E07C | 184 | `exact` | yes | `unknown/EF/EFDFC4.asm` | `UNKNOWN_EFDFC4` | `` |
| 131 | EF:E07C | EF:E133 | 183 | `exact` | yes | `unknown/EF/EFE07C.asm` | `UNKNOWN_EFE07C` | `` |
| 132 | EF:E133 | EF:E175 | 66 | `exact` | yes | `unknown/EF/EFE133.asm` | `` | `` |
| 133 | EF:E175 | EF:EB1D | 2472 | `exact` | yes | `unknown/EF/EFE175.asm` | `` | `` |
| 134 | EF:EB1D | EF:EB2A | 13 | `exact` | yes | `system/debug/load_debug_cursor_graphics.asm` | `UNKNOWN_EFEB1D` | `` |
| 135 | EF:EB2A | EF:EB3D | 19 | `exact` | yes | `system/debug/handle_cursor_movement.asm` | `UNKNOWN_EFEB2A` | `` |
| 136 | EF:EB3D | EF:EB5F | 34 | `exact` | yes | `system/debug/process_command_selection.asm` | `UNKNOWN_EFEB3D` | `` |
| 137 | EF:EB5F | EF:EF70 | 1041 | `exact` | yes | `system/debug/load_menu.asm` | `` | `` |
| 138 | EF:E6CF | EF:E6E2 | 19 | `exact` | yes | `unknown/EF/EFE6CF.asm` | `UNKNOWN_EFE6CF` | `` |
| 139 | EF:E6E2 | EF:E708 | 38 | `exact` | yes | `unknown/EF/EFE6E2.asm` | `UNKNOWN_EFE6E2` | `` |
| 140 | EF:E708 |  | 0 | `open` |  | `unknown/EF/EFE708.asm` | `UNKNOWN_EFE708` | `` |
| 141 |  |  | 0 | `open` |  | `system/debug/check_view_character_mode.asm` | `DEBUG_CHECK_VIEW_CHARACTER_MODE` | `` |
| 142 | EF:E759 | EF:E771 | 24 | `exact` | yes | `unknown/EF/EFE759.asm` | `UNKNOWN_EFE759` | `` |
| 143 | EF:E771 | EF:E873 | 258 | `exact` | yes | `unknown/EF/EFE771.asm` | `` | `` |
| 144 | EF:E873 | EF:E895 | 34 | `exact` | yes | `unknown/EF/EFE873.asm` | `UNKNOWN_EFE873` | `` |
| 145 | EF:E895 | EF:E8C7 | 50 | `exact` | yes | `unknown/EF/EFE895.asm` | `UNKNOWN_EFE895` | `` |
| 146 | EF:E8C7 | EF:EA23 | 348 | `exact` | yes | `unknown/EF/EFE8C7.asm` | `` | `` |
| 147 | EF:EA23 | EF:EA4A | 39 | `exact` | yes | `unknown/EF/EFEA23.asm` | `UNKNOWN_EFEA23` | `` |
| 148 | EF:EA4A | EF:EA9E | 84 | `exact` | yes | `unknown/EF/EFEA4A.asm` | `UNKNOWN_EFEA4A` | `` |
| 149 | EF:EA9E | EF:EAA4 | 6 | `exact` | yes | `unknown/EF/EFEA9E.asm` | `UNKNOWN_EFEA9E` | `` |
| 150 | EF:EAA4 | EF:EAC8 | 36 | `exact` | yes | `unknown/EF/EFEAA4.asm` | `UNKNOWN_EFEAA4` | `` |
| 151 | EF:EAC8 | EF:EB1D | 85 | `exact` | yes | `unknown/EF/EFEAC8.asm` | `UNKNOWN_EFEAC8` | `` |
| 152 | EF:EB1D | EF:EB2A | 13 | `exact` | yes | `data/unknown/EFEB1D.asm` | `UNKNOWN_EFEB1D` | `` |
| 153 | EF:EB2A | EF:EB3D | 19 | `exact` | yes | `unknown/EF/EFEB2A.asm` | `UNKNOWN_EFEB2A` | `` |
| 154 | EF:EB3D | EF:EB5F | 34 | `exact` | yes | `data/unknown/EFEB3D.asm` | `UNKNOWN_EFEB3D` | `` |
| 155 | EF:EF70 | EF:EF9F | 47 | `exact` | yes | `data/unknown/EFEF70.asm` | `UNKNOWN_EFEF70` | `` |
| 156 | EF:EF9F | EF:EFB7 | 24 | `exact` | yes | `data/debug/debug_font_palette.asm` | `DEBUG_FONT_PALETTE` | `` |
| 157 | EF:F0D7 | EF:F1BB | 228 | `exact` | yes | `data/unknown/EFF0D7.asm` | `UNKNOWN_EFF0D7` | `` |
| 158 | EF:F1BB | EF:F3BB | 512 | `exact` | yes | `data/unknown/EFF1BB.asm` | `UNKNOWN_EFF1BB` | `` |
| 159 | EF:F3BB | EF:F3DB | 32 | `exact` | yes | `data/unknown_version_string.asm` | `UNKNOWN_VERSION_STRING` | `` |
| 160 | EF:F3DB | EF:F511 | 310 | `exact` | yes | `data/unused/EFF3DB.asm` | `` | `` |
| 161 | EF:F511 | EF:F53B | 42 | `exact` | yes | `data/unused/EFF511.asm` | `` | `` |
| 162 | EF:F53B | EF:F5BB | 128 | `exact` | yes | `data/unused/EFF53B.asm` | `` | `` |
| 163 | EF:F5BB | EF:F5BD | 2 | `exact` | yes | `data/debug/debug_cursor_spritemap.asm` | `DEBUG_CURSOR_SPRITEMAP` | `` |
