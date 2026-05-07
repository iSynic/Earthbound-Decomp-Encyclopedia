# Cross-bank data contract manifest

Generated from local notes plus quarantined reference structs. This is the machine-readable struct/table front door for source and data emission work; edit `tools/build_data_contract_manifest.py`, then regenerate this file.

## Summary

- schema: `earthbound-decomp.data-contracts.v1`
- contracts: `168`
- fields: `687`

| Contract | Domain | Address | Stride | Count | Struct | Fields | Confidence |
| --- | --- | --- | ---: | ---: | --- | ---: | --- |
| GAME_STATE | wram-root | `7E:9801` | `0x1D9` | 1 | `game_state` | 26 | corroborated |
| PARTY_CHARACTERS | wram-root | `7E:99CE` | `0x5F` | 6 | `char_struct` | 41 | corroborated |
| BATTLERS_TABLE | wram-root | `7E:9FAC` | `0x4E` | 32 | `battler` | 49 | corroborated |
| ITEM_CONFIGURATION_TABLE | rom-table | `D5:5000` | `0x27` | 254 | `item` | 7 | corroborated |
| STORE_TABLE | rom-table | `D5:76B2` | `0x7` | 66 | `store_inventory` | 7 | corroborated |
| PSI_TELEPORT_DEST_TABLE | rom-table | `D5:7880` | `0x1F` | 16 | `psi_teleport_destination` | 4 | corroborated |
| TELEPHONE_CONTACTS_TABLE | rom-table | `D5:7AAE` | `0x1F` | 6 | `telephone_contact` | 3 | corroborated |
| BATTLE_ACTION_TABLE | rom-table | `D5:7B68` | `0xC` | 318 | `battle_action` | 6 | corroborated |
| PSI_ABILITY_TABLE | rom-table | `D5:8A50` | `0xF` | 54 | `psi_ability` | 11 | corroborated |
| PSI_NAME_TABLE | rom-table | `D5:8D7A` | `0x19` | 17 | `psi_name` | 1 | corroborated |
| NPC_AI_TABLE | rom-table | `D5:8F23` | `0x1` | 38 | `npc_ai_selector` | 1 | corroborated |
| EXP_TABLE | rom-table | `D5:8F49` | `0x190` | 4 | `character_exp_curve` | 1 | corroborated |
| ENEMY_CONFIGURATION_TABLE | rom-table | `D5:9589` | `0x5E` | 231 | `enemy_data` | 42 | corroborated |
| STATS_GROWTH_VARS | rom-table | `D5:EA5B` | `0x7` | 4 | `stats_growth_vars` | 7 | corroborated |
| CONDIMENT_TABLE | rom-table | `D5:EA77` | `0x7` | 44 | `condiment_rule` | 7 | corroborated |
| TELEPORT_DESTINATION_TABLE | rom-table | `D5:EBAB` | `0x8` | 234 | `teleport_destination` | 6 | corroborated |
| MAP_HOTSPOTS | rom-table | `D5:F2FB` | `0x8` | 56 | `map_hotspot` | 4 | corroborated |
| TIMED_ITEM_TRANSFORMATION_TABLE | rom-table | `D5:F4BB` | `0x5` | 4 | `timed_item_transformation` | 5 | corroborated |
| DONT_CARE_NAMES | rom-table | `D5:F4CF` | `0x2A` | 7 | `default_name_set` | 7 | corroborated |
| INITIAL_STATS | rom-table | `D5:F5F5` | `0x15` | 4 | `initial_party_member_stats` | 5 | corroborated |
| TIMED_DELIVERY_TABLE | rom-table | `D5:F649` | `0x14` | 10 | `timed_delivery_source_window` | 1 | exact-source-window |
| TIMED_DELIVERY_CONTROLLER_TABLE | rom-table | `D5:F645` | `0x14` | 10 | `timed_delivery_controller_row` | 11 | consumer-corroborated |
| CF_DOOR_DATA | rom-block | `CF:0000` | `0x264F` | 1 | `cf_door_data_payload` | 1 | consumer-corroborated-partial |
| CF_DOOR_CONFIG_TABLE | rom-variable-table | `CF:264F` | `0x32A0` | 1 | `door_sector_list_block` | 1 | exact-variable-lists |
| D0_DOOR_POINTER_TABLE | rom-table | `D0:0000` | `0x4` | 1280 | `door_sector_list_far_pointer` | 3 | exact |
| SCREEN_TRANSITION_CONFIG_TABLE | rom-table | `D0:1400` | `0xC` | 34 | `screen_transition_config` | 12 | corroborated |
| EVENT_CONTROL_PTR_TABLE | rom-table | `D0:1598` | `0x2` | 20 | `word_pointer` | 1 | exact |
| MAP_TILE_EVENT_CONTROL_TABLE | rom-variable-table | `D0:15C0` | `0x2C0` | 1 | `map_tile_event_chain_block` | 1 | exact-variable-chains |
| MAP_ENEMY_PLACEMENT | rom-table | `D0:1880` | `0x2` | 20480 | `map_enemy_placement` | 1 | corroborated |
| ENEMY_PLACEMENT_GROUPS_PTR_TABLE | rom-table | `D0:B880` | `0x4` | 203 | `far_pointer` | 1 | exact |
| ENEMY_PLACEMENT_GROUPS_TABLE | rom-variable-table | `D0:BBAC` | `0xA61` | 1 | `enemy_placement_group_lists` | 1 | exact-variable-lists |
| BTL_ENTRY_PTR_TABLE | rom-table | `D0:C60D` | `0x8` | 484 | `battle_entry_ptr_entry` | 4 | corroborated |
| ENEMY_BATTLE_GROUPS_TABLE | rom-variable-table | `D0:D52D` | `0xA87` | 1 | `enemy_battle_group_payloads` | 1 | exact-variable-lists |
| D7_SECTOR_TILESET_PALETTE_TABLE | rom-table | `D7:A800` | `0x1` | 1280 | `map_sector_tileset_palette` | 1 | consumer-corroborated |
| D7_SECTOR_CONTEXT_WORD_TABLE | rom-table | `D7:B200` | `0x2` | 1280 | `map_sector_context_word` | 1 | consumer-corroborated-low3 |
| MAP_TILE_COLLISION_DATA | rom-table | `D8:0000` | `0x10` | 2293 | `map_tile_collision_record` | 16 | consumer-corroborated |
| MAP_DATA_TILE_COLLISION_PTR_TABLE | rom-table | `EF:117B` | `0x4` | 20 | `far_pointer` | 1 | exact |
| MAP_DATA_TILE_COLLISION_POINTERS_0 | rom-table | `D8:8F50` | `0x2` | 832 | `map_tile_collision_record_offset` | 1 | exact |
| MAP_DATA_TILE_COLLISION_POINTERS_1 | rom-table | `D8:95D0` | `0x2` | 845 | `map_tile_collision_record_offset` | 1 | exact |
| MAP_DATA_TILE_COLLISION_POINTERS_2 | rom-table | `D8:9C6A` | `0x2` | 827 | `map_tile_collision_record_offset` | 1 | exact |
| MAP_DATA_TILE_COLLISION_POINTERS_3 | rom-table | `D8:A2E0` | `0x2` | 524 | `map_tile_collision_record_offset` | 1 | exact |
| MAP_DATA_TILE_COLLISION_POINTERS_4 | rom-table | `D8:A6F8` | `0x2` | 935 | `map_tile_collision_record_offset` | 1 | exact |
| MAP_DATA_TILE_COLLISION_POINTERS_5 | rom-table | `D8:AE46` | `0x2` | 287 | `map_tile_collision_record_offset` | 1 | exact |
| MAP_DATA_TILE_COLLISION_POINTERS_6 | rom-table | `D8:B084` | `0x2` | 875 | `map_tile_collision_record_offset` | 1 | exact |
| MAP_DATA_TILE_COLLISION_POINTERS_7 | rom-table | `D8:B75A` | `0x2` | 749 | `map_tile_collision_record_offset` | 1 | exact |
| MAP_DATA_TILE_COLLISION_POINTERS_8 | rom-table | `D8:BD34` | `0x2` | 628 | `map_tile_collision_record_offset` | 1 | exact |
| MAP_DATA_TILE_COLLISION_POINTERS_9 | rom-table | `D8:C21C` | `0x2` | 933 | `map_tile_collision_record_offset` | 1 | exact |
| MAP_DATA_TILE_COLLISION_POINTERS_10 | rom-table | `D8:C966` | `0x2` | 871 | `map_tile_collision_record_offset` | 1 | exact |
| MAP_DATA_TILE_COLLISION_POINTERS_11 | rom-table | `D8:D034` | `0x2` | 713 | `map_tile_collision_record_offset` | 1 | exact |
| MAP_DATA_TILE_COLLISION_POINTERS_12 | rom-table | `D8:D5C6` | `0x2` | 462 | `map_tile_collision_record_offset` | 1 | exact |
| MAP_DATA_TILE_COLLISION_POINTERS_13 | rom-table | `D8:D962` | `0x2` | 882 | `map_tile_collision_record_offset` | 1 | exact |
| MAP_DATA_TILE_COLLISION_POINTERS_14 | rom-table | `D8:E046` | `0x2` | 203 | `map_tile_collision_record_offset` | 1 | exact |
| MAP_DATA_TILE_COLLISION_POINTERS_15 | rom-table | `D8:E1DC` | `0x2` | 143 | `map_tile_collision_record_offset` | 1 | exact |
| MAP_DATA_TILE_COLLISION_POINTERS_16 | rom-table | `D8:E2FA` | `0x2` | 390 | `map_tile_collision_record_offset` | 1 | exact |
| MAP_DATA_TILE_COLLISION_POINTERS_17 | rom-table | `D8:E606` | `0x2` | 343 | `map_tile_collision_record_offset` | 1 | exact |
| MAP_DATA_TILE_COLLISION_POINTERS_18 | rom-table | `D8:E8B4` | `0x2` | 445 | `map_tile_collision_record_offset` | 1 | exact |
| MAP_DATA_TILE_COLLISION_POINTERS_19 | rom-table | `D8:EC2E` | `0x2` | 536 | `map_tile_collision_record_offset` | 1 | exact |
| MAP_PALETTE_POINTER_TABLE | rom-table | `DA:FAA7` | `0x3` | 32 | `snes_long_pointer24` | 2 | verified |
| DA_MAP_PALETTE_VARIANT_TABLE | rom-table | `DA:7CA7` | `0xC0` | 168 | `da_map_palette_variant` | 10 | tool-and-script-corroborated |
| PER_SECTOR_MUSIC_TABLE | rom-table | `DC:D637` | `0x2` | 1280 | `per_sector_music_options_index` | 1 | structural-corroborated |
| CURRENT_POSITION_EVENT_MUSIC_SELECTOR_TABLE | rom-table | `DC:D637` | `0x1` | 1280 | `current_position_event_music_context_selector` | 1 | consumer-corroborated |
| LANDING_PALETTE_ANIM_PROFILE_POINTER_TABLE | rom-table | `DF:E4E1` | `0x4` | 31 | `far_pointer` | 1 | runtime-corroborated |
| LANDING_PALETTE_ANIM_PROFILE_0 | rom-variable-table | `DF:E55D` | `0x9` | 1 | `landing_palette_anim_profile` | 3 | runtime-corroborated-shape |
| LANDING_PALETTE_ANIM_PROFILE_1 | rom-variable-table | `DF:E566` | `0x9` | 1 | `landing_palette_anim_profile` | 3 | runtime-corroborated-shape |
| LANDING_PALETTE_ANIM_PROFILE_2 | rom-variable-table | `DF:E56F` | `0xB` | 1 | `landing_palette_anim_profile` | 3 | runtime-corroborated-shape |
| LANDING_PALETTE_ANIM_PROFILE_3 | rom-variable-table | `DF:E57A` | `0x8` | 1 | `landing_palette_anim_profile` | 3 | runtime-corroborated-shape |
| LANDING_PALETTE_ANIM_PROFILE_4 | rom-variable-table | `DF:E582` | `0x9` | 1 | `landing_palette_anim_profile` | 3 | runtime-corroborated-shape |
| LANDING_PALETTE_ANIM_PROFILE_5 | rom-variable-table | `DF:E58B` | `0x8` | 1 | `landing_palette_anim_profile` | 3 | runtime-corroborated-shape |
| LANDING_PALETTE_ANIM_PROFILE_6 | rom-variable-table | `DF:E593` | `0x8` | 1 | `landing_palette_anim_profile` | 3 | runtime-corroborated-shape |
| LANDING_PALETTE_ANIM_PROFILE_7 | rom-variable-table | `DF:E59B` | `0xD` | 1 | `landing_palette_anim_profile` | 3 | runtime-corroborated-shape |
| LANDING_PALETTE_ANIM_PROFILE_8 | rom-variable-table | `DF:E5A8` | `0x5` | 1 | `landing_palette_anim_profile` | 2 | runtime-corroborated-shape |
| LANDING_PALETTE_ANIM_PROFILE_9 | rom-variable-table | `DF:E5AD` | `0x5` | 1 | `landing_palette_anim_profile` | 2 | runtime-corroborated-shape |
| LANDING_PALETTE_ANIM_PROFILE_10 | rom-variable-table | `DF:E5B2` | `0x5` | 1 | `landing_palette_anim_profile` | 2 | runtime-corroborated-shape |
| LANDING_PALETTE_ANIM_PROFILE_11 | rom-variable-table | `DF:E5B7` | `0x5` | 1 | `landing_palette_anim_profile` | 2 | runtime-corroborated-shape |
| LANDING_PALETTE_ANIM_PROFILE_12 | rom-variable-table | `DF:E5BC` | `0x5` | 1 | `landing_palette_anim_profile` | 2 | runtime-corroborated-shape |
| LANDING_PALETTE_ANIM_PROFILE_13 | rom-variable-table | `DF:E5C1` | `0x5` | 1 | `landing_palette_anim_profile` | 2 | runtime-corroborated-shape |
| LANDING_PALETTE_ANIM_PROFILE_14 | rom-variable-table | `DF:E5C6` | `0x5` | 1 | `landing_palette_anim_profile` | 2 | runtime-corroborated-shape |
| LANDING_PALETTE_ANIM_PROFILE_15 | rom-variable-table | `DF:E5CB` | `0x5` | 1 | `landing_palette_anim_profile` | 2 | runtime-corroborated-shape |
| LANDING_PALETTE_ANIM_PROFILE_16 | rom-variable-table | `DF:E5D0` | `0x5` | 1 | `landing_palette_anim_profile` | 2 | runtime-corroborated-shape |
| LANDING_PALETTE_ANIM_PROFILE_17 | rom-variable-table | `DF:E5D5` | `0x5` | 1 | `landing_palette_anim_profile` | 2 | runtime-corroborated-shape |
| LANDING_PALETTE_ANIM_PROFILE_18 | rom-variable-table | `DF:E5DA` | `0x5` | 1 | `landing_palette_anim_profile` | 2 | runtime-corroborated-shape |
| LANDING_PALETTE_ANIM_PROFILE_19 | rom-variable-table | `DF:E5DF` | `0x5` | 1 | `landing_palette_anim_profile` | 2 | runtime-corroborated-shape |
| LANDING_PALETTE_ANIM_PROFILE_20 | rom-variable-table | `DF:E5E4` | `0x5` | 1 | `landing_palette_anim_profile` | 2 | runtime-corroborated-shape |
| LANDING_PALETTE_ANIM_PROFILE_21 | rom-variable-table | `DF:E5E9` | `0x5` | 1 | `landing_palette_anim_profile` | 2 | runtime-corroborated-shape |
| LANDING_PALETTE_ANIM_PROFILE_22 | rom-variable-table | `DF:E5EE` | `0x5` | 1 | `landing_palette_anim_profile` | 2 | runtime-corroborated-shape |
| LANDING_PALETTE_ANIM_PROFILE_23 | rom-variable-table | `DF:E5F3` | `0x5` | 1 | `landing_palette_anim_profile` | 2 | runtime-corroborated-shape |
| LANDING_PALETTE_ANIM_PROFILE_24 | rom-variable-table | `DF:E5F8` | `0x5` | 1 | `landing_palette_anim_profile` | 2 | runtime-corroborated-shape |
| LANDING_PALETTE_ANIM_PROFILE_25 | rom-variable-table | `DF:E5FD` | `0x5` | 1 | `landing_palette_anim_profile` | 2 | runtime-corroborated-shape |
| LANDING_PALETTE_ANIM_PROFILE_26 | rom-variable-table | `DF:E602` | `0x5` | 1 | `landing_palette_anim_profile` | 2 | runtime-corroborated-shape |
| LANDING_PALETTE_ANIM_PROFILE_27 | rom-variable-table | `DF:E607` | `0x5` | 1 | `landing_palette_anim_profile` | 2 | runtime-corroborated-shape |
| LANDING_PALETTE_ANIM_PROFILE_28 | rom-variable-table | `DF:E60C` | `0x5` | 1 | `landing_palette_anim_profile` | 2 | runtime-corroborated-shape |
| LANDING_PALETTE_ANIM_PROFILE_29 | rom-variable-table | `DF:E611` | `0x5` | 1 | `landing_palette_anim_profile` | 2 | runtime-corroborated-shape |
| LANDING_PALETTE_ANIM_PROFILE_30 | rom-variable-table | `DF:E616` | `0x5` | 1 | `landing_palette_anim_profile` | 2 | runtime-corroborated-shape |
| LANDING_PALETTE_ANIM_PAYLOAD_0 | rom-compressed-payload | `DF:E61B` | `0x97` | 1 | `landing_palette_anim_compressed_payload` | 1 | pointer-bounded |
| LANDING_PALETTE_ANIM_PAYLOAD_1 | rom-compressed-payload | `DF:E6B2` | `0x8B` | 1 | `landing_palette_anim_compressed_payload` | 1 | pointer-bounded |
| LANDING_PALETTE_ANIM_PAYLOAD_2 | rom-compressed-payload | `DF:E73D` | `0x1A3` | 1 | `landing_palette_anim_compressed_payload` | 1 | pointer-bounded |
| LANDING_PALETTE_ANIM_PAYLOAD_3 | rom-compressed-payload | `DF:E8E0` | `0x8C` | 1 | `landing_palette_anim_compressed_payload` | 1 | pointer-bounded |
| LANDING_PALETTE_ANIM_PAYLOAD_4 | rom-compressed-payload | `DF:E96C` | `0xEA` | 1 | `landing_palette_anim_compressed_payload` | 1 | pointer-bounded |
| LANDING_PALETTE_ANIM_PAYLOAD_5 | rom-compressed-payload | `DF:EA56` | `0xDB` | 1 | `landing_palette_anim_compressed_payload` | 1 | pointer-bounded |
| LANDING_PALETTE_ANIM_PAYLOAD_6 | rom-compressed-payload | `DF:EB31` | `0x7B` | 1 | `landing_palette_anim_compressed_payload` | 1 | pointer-bounded |
| LANDING_PALETTE_ANIM_PAYLOAD_7 | rom-compressed-payload | `DF:EBAC` | `0x9A` | 1 | `landing_palette_anim_compressed_payload` | 1 | pointer-bounded |
| TEXT_WINDOW_FLAVOR_SELECTOR_TABLE | rom-table | `E0:1FB9` | `0x3` | 5 | `text_window_flavor_selector` | 2 | runtime-corroborated |
| TEXT_WINDOW_PALETTE_BLOCKS | rom-table | `E0:1FC8` | `0x40` | 7 | `text_window_palette_block` | 8 | runtime-corroborated |
| MOVEMENT_TEXT_STRING_PALETTE | rom-table | `E0:2188` | `0x8` | 1 | `four_colour_palette_row` | 4 | structural-corroborated |
| TOWN_MAP_GFX_POINTER_TABLE | rom-table | `E0:2190` | `0x4` | 6 | `far_pointer` | 1 | runtime-corroborated |
| TITLE_SCREEN_LETTER_OAM_RECORDS | rom-table | `E1:CE08` | `0x2D` | 9 | `title_screen_letter_oam_record` | 1 | verified |
| TITLE_SCREEN_LETTER_OAM_POINTER_TABLE | rom-table | `E1:CF9D` | `0x2` | 9 | `word_pointer` | 1 | verified |
| PHOTOGRAPHER_CONFIG_TABLE | rom-table | `E1:2F8A` | `0x3E` | 32 | `photographer_config_record` | 31 | consumer-corroborated-partial |
| TOWN_MAP_ICON_GRAPHIC_DESCRIPTOR_RECORDS | rom-table | `E1:F203` | `0x5` | 117 | `town_map_icon_graphic_descriptor` | 4 | runtime-corroborated-shape |
| TOWN_MAP_ICON_GRAPHIC_POINTER_TABLE | rom-table | `E1:F44C` | `0x2` | 23 | `word_pointer` | 1 | runtime-corroborated |
| TOWN_MAP_BLINK_SUPPRESS_TABLE | rom-table | `E1:F47A` | `0x1` | 23 | `town_map_blink_suppress_flag` | 1 | runtime-corroborated |
| TOWN_MAP_ICON_PLACEMENT_POINTER_TABLE | rom-table | `E1:F491` | `0x4` | 6 | `far_pointer` | 1 | runtime-corroborated |
| TOWN_MAP_ICON_PLACEMENT_LIST_0 | rom-variable-table | `E1:F4A9` | `0x5` | 7 | `town_map_icon_placement_record` | 4 | runtime-corroborated-shape |
| TOWN_MAP_ICON_PLACEMENT_LIST_1 | rom-variable-table | `E1:F4CD` | `0x5` | 8 | `town_map_icon_placement_record` | 4 | runtime-corroborated-shape |
| TOWN_MAP_ICON_PLACEMENT_LIST_2 | rom-variable-table | `E1:F4F6` | `0x5` | 9 | `town_map_icon_placement_record` | 4 | runtime-corroborated-shape |
| TOWN_MAP_ICON_PLACEMENT_LIST_3 | rom-variable-table | `E1:F524` | `0x5` | 7 | `town_map_icon_placement_record` | 4 | runtime-corroborated-shape |
| TOWN_MAP_ICON_PLACEMENT_LIST_4 | rom-variable-table | `E1:F548` | `0x5` | 5 | `town_map_icon_placement_record` | 4 | runtime-corroborated-shape |
| TOWN_MAP_ICON_PLACEMENT_LIST_5 | rom-variable-table | `E1:F562` | `0x5` | 6 | `town_map_icon_placement_record` | 4 | runtime-corroborated-shape |
| OVERWORLD_EVENT_MUSIC_POINTER_TABLE | rom-table | `CF:58EF` | `0x2` | 165 | `word_pointer` | 1 | consumer-corroborated |
| OVERWORLD_EVENT_MUSIC_TABLE | rom-variable-table | `CF:5A39` | `0x7A4` | 1 | `overworld_event_music_rows` | 1 | consumer-corroborated |
| CF_INLINE_EVENT_MUSIC_TRAILER | rom-block | `CF:61DD` | `0xA` | 1 | `inline_event_music_trailer` | 1 | exact |
| SPRITE_PLACEMENT_POINTER_TABLE | rom-table | `CF:61E7` | `0x2` | 1280 | `sprite_placement_sector_pointer` | 1 | exact |
| SPRITE_PLACEMENT_TABLE | rom-variable-table | `CF:6BE7` | `0x1D9E` | 1 | `sprite_placement_sector_list_block` | 1 | exact-variable-lists |
| NPC_CONFIG_TABLE | rom-table | `CF:8985` | `0x11` | 1584 | `npc_config` | 8 | corroborated |
| BATTLE_SELECTION_SNAPSHOT | wram-overlay | `7E:9FFA` | `0x4E` | 1 | `battle_menu_selection_header_plus_snapshot` | 17 | corroborated-overlay |
| LOADED_BG_DATA_LAYER1 | wram-root | `7E:ADD4` | `0x77` | 1 | `loaded_bg_data` | 36 | corroborated |
| LOADED_BG_DATA_LAYER2 | wram-root | `7E:AE4B` | `0x77` | 1 | `loaded_bg_data` | 36 | corroborated |
| PATHFINDING_TILE_CONTEXT_GATE_TABLE | rom-table | `C3:DFE8` | `0x1` | 8 | `pathfinding_tile_context_gate` | 1 | corroborated |
| INPUT_DIRECTION_PERMISSION_MASK_TABLE | rom-table | `C3:E12C` | `0x2` | 14 | `input_direction_permission_mask` | 1 | corroborated |
| INTERACTION_PROBE_DIRECTION_X_OFFSETS | rom-table | `C3:E148` | `0x2` | 8 | `signed_direction_offset_word` | 1 | corroborated |
| INTERACTION_PROBE_DIRECTION_Y_OFFSETS | rom-table | `C3:E158` | `0x2` | 8 | `signed_direction_offset_word` | 1 | corroborated |
| INTERACTION_RESULT_FACING_REMAP_TABLE | rom-table | `C3:E168` | `0x2` | 8 | `interaction_result_facing_remap` | 1 | corroborated |
| MAP_ENTITY_PLACEMENT_DIRECTION_PARAM_TABLE | rom-table | `C3:E1D8` | `0x2` | 4 | `map_entity_placement_direction_param` | 1 | proposed |
| MAP_ENTITY_PLACEMENT_DIRECTION_PARAM_TABLE_PAGE1 | rom-table | `C3:E1E0` | `0x2` | 16 | `map_entity_placement_direction_param` | 1 | proposed |
| STAGED_MOVEMENT_PRIMARY_DIRECTION_PARAM_TABLE | rom-table | `C3:E200` | `0x2` | 4 | `staged_movement_direction_param` | 1 | corroborated |
| STAGED_MOVEMENT_ALTERNATE_DIRECTION_PARAM_TABLE | rom-table | `C3:E208` | `0x2` | 4 | `staged_movement_direction_param` | 1 | corroborated |
| STAGED_MOVEMENT_SUBTILE_OFFSET_SET_A_X | rom-table | `C3:E210` | `0x2` | 4 | `signed_subtile_offset_word` | 1 | corroborated |
| STAGED_MOVEMENT_SUBTILE_OFFSET_SET_A_Y | rom-table | `C3:E218` | `0x2` | 4 | `signed_subtile_offset_word` | 1 | corroborated |
| STAGED_MOVEMENT_SUBTILE_OFFSET_SET_B_X | rom-table | `C3:E220` | `0x2` | 4 | `signed_subtile_offset_word` | 1 | corroborated |
| STAGED_MOVEMENT_SUBTILE_OFFSET_SET_B_Y | rom-table | `C3:E228` | `0x2` | 4 | `signed_subtile_offset_word` | 1 | corroborated |
| DOOR_CANDIDATE_DIRECTION_OFFSET_X | rom-table | `C3:E230` | `0x2` | 8 | `door_candidate_direction_offset_word` | 1 | corroborated |
| DOOR_CANDIDATE_DIRECTION_OFFSET_Y | rom-table | `C3:E240` | `0x2` | 8 | `door_candidate_direction_offset_word` | 1 | corroborated |
| MENU_CURSOR_TILE_PREFIX_TABLE | rom-table | `C3:E3F8` | `0x2` | 7 | `menu_cursor_tile_prefix_word` | 1 | proposed |
| ANIMATED_MENU_CURSOR_POINT_RIGHT_TILES | rom-table | `C3:E406` | `0x8` | 1 | `four_tile_word_run` | 4 | corroborated |
| TITLE_NAME_BUFFER_CURSOR_TILE_RUN | rom-table | `C3:E40E` | `0x8` | 1 | `four_tile_word_run` | 4 | corroborated |
| BLINKING_TRIANGLE_BASE_TILES | rom-table | `C3:E416` | `0x6` | 1 | `three_tile_word_run` | 3 | corroborated |
| BLINKING_TRIANGLE_WAIT_FRAME_TILES | rom-table | `C3:E41C` | `0x8` | 4 | `four_tile_word_frame` | 4 | corroborated |
| BLINKING_TRIANGLE_WAIT_FRAME_POINTER_TABLE | rom-table | `C3:E43C` | `0x4` | 4 | `far_pointer` | 1 | corroborated |
| WINDOW_TICK_TRANSFER_PRELUDE_WORDS | rom-table | `C3:E44C` | `0x2` | 2 | `window_tick_transfer_prelude_word` | 1 | proposed |
| BATTLE_PSI_MENU_SELECTOR_GROUP_TABLE | rom-table | `C3:EF26` | `0x1` | 240 | `battle_psi_menu_selector_group` | 1 | corroborated |
| BATTLE_PSI_MENU_GROUP_SLICE_COUNT_TABLE | rom-table | `C3:F016` | `0x1` | 62 | `battle_psi_menu_group_slice_count` | 1 | corroborated |
| BATTLE_PSI_GROUP_RENDER_METADATA_AND_LABELS | rom-block | `C3:F054` | `0x5C` | 1 | `battle_psi_group_render_metadata_and_labels` | 1 | proposed |
| BATTLE_PSI_KNOWN_STATE_GATE_TABLE | rom-table | `C3:F0B0` | `0xE` | 7 | `battle_psi_known_state_gate_row` | 7 | corroborated |
| BATTLE_PSI_RANK_SUFFIX_TABLE | rom-table | `C3:F112` | `0x2` | 5 | `battle_psi_rank_suffix_token` | 1 | corroborated |
| BATTLE_PSI_MENU_ENTRY_FIXED_TAIL | rom-block | `C3:F11C` | `0x8` | 1 | `battle_psi_menu_entry_fixed_tail` | 1 | corroborated |
| BATTLE_PSI_MENU_ENTRY_ROW_TABLE | rom-table | `C3:F124` | `0x14` | 10 | `battle_psi_menu_entry_row` | 1 | corroborated |
| LEVEL_UP_STAT_GROWTH_VARIANCE_TABLE | rom-table | `C3:F2B1` | `0x1` | 4 | `level_up_stat_growth_variance` | 1 | corroborated |
| VISUAL_SELECTOR_POSE_ROW_TABLE | rom-table | `C3:F2B5` | `0x10` | 17 | `visual_selector_pose_row` | 8 | corroborated |
| BATTLE_VISUAL_GRAPHICS_SOURCE_STRIP_OFFSETS | rom-table | `C3:F871` | `0x8` | 8 | `battle_visual_strip_offset_page` | 4 | corroborated |
| BATTLE_VISUAL_OAM_TILE_INDEX_GRID | rom-table | `C3:F8B1` | `0x10` | 4 | `battle_visual_oam_tile_index_row` | 8 | corroborated |
| BATTLE_PALETTE_SET_ROWS | rom-table | `C3:F8F1` | `0x20` | 3 | `rgb555_palette_row` | 16 | corroborated |
| BATTLE_VISUAL_TOKEN_23_TO_2D_COLOUR_TRIPLES | rom-table | `C3:F951` | `0x3` | 11 | `battle_visual_fixed_colour_triple` | 3 | corroborated |
| BATTLE_VISUAL_TOKEN_31_TO_35_COLOUR_TRIPLES | rom-table | `C3:F972` | `0x3` | 5 | `battle_visual_fixed_colour_triple` | 3 | corroborated |
| BLANK_COMMON_TILE_SOURCE_BLOCK | rom-table | `C4:0BE8` | `0x200` | 1 | `blank_common_tile_source_block` | 1 | corroborated |
| WH_WINDOW_SPAN_RADIUS_RAMP_TABLE | rom-table | `C4:74F6` | `0x1` | 11 | `wh_window_span_radius_ramp_entry` | 1 | corroborated |
| MOVEMENT_OCTANT_TO_PULSE_SELECTOR_TABLE | rom-table | `C4:8C59` | `0x2` | 8 | `movement_octant_pulse_selector` | 1 | corroborated |
| MOVEMENT_OCTANT_SIGNED_UNIT_DELTA_TABLE | rom-table | `C4:8D38` | `0x20` | 1 | `movement_octant_signed_unit_delta_components` | 1 | proposed |
| YOUR_SANCTUARY_LOCATION_COORDINATE_TABLE | rom-table | `C4:DE78` | `0x4` | 8 | `your_sanctuary_location_coordinate_pair` | 2 | corroborated |

## Contracts

### GAME_STATE

- domain: `wram-root`
- address: `7E:9801`
- stride: `0x1D9`
- count: `1`
- struct: `game_state`
- confidence: `corroborated`
- note: saveblock game_state root from ebsrc ram.asm
- evidence: `tools/lookup_wram_field.py`, `refs/ebsrc-main/ebsrc-main/include/structs.asm`, `refs/ebsrc-main/ebsrc-main/src/bankconfig/common/ram.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `mother2_playername` | 1 | 12 | 12-byte Mother 2 carryover name buffer |
| `0xC` | `earthbound_playername` | 1 | 24 | 24-byte EarthBound player-name buffer |
| `0x24` | `pet_name` | 1 | 6 | 6-byte pet-name buffer |
| `0x2A` | `favourite_food` | 1 | 6 | 6-byte favourite-food buffer |
| `0x30` | `favourite_thing` | 1 | 12 | 12-byte favourite-thing / PSI naming buffer |
| `0x3C` | `money_carried` | 4 | 1 | party money carried |
| `0x40` | `bank_balance` | 4 | 1 | bank account balance |
| `0x44` | `party_psi` | 1 | 1 | party PSI latch byte |
| `0x45` | `party_npc_1` | 1 | 1 | party NPC slot 1 id |
| `0x46` | `party_npc_2` | 1 | 1 | party NPC slot 2 id |
| `0x4B` | `party_status` | 1 | 1 | party status byte |
| `0x52` | `wallet_backup` | 4 | 1 | wallet backup dword |
| `0x56` | `escargo_express_items` | 1 | 36 | Escargo Express stored-item queue |
| `0x7A` | `party_members` | 1 | 6 | party member ids |
| `0x82` | `leader_x_coord` | 2 | 1 | leader X coordinate |
| `0x86` | `leader_y_coord` | 2 | 1 | leader Y coordinate |
| `0x8A` | `leader_direction` | 2 | 1 | leader facing direction |
| `0x8C` | `trodden_tile_type` | 2 | 1 | trodden tile type |
| `0x8E` | `walking_style` | 2 | 1 | walking style |
| `0x94` | `current_party_members` | 2 | 1 | current party-members word |
| `0xAE` | `party_count` | 1 | 1 | party count |
| `0xAF` | `player_controlled_party_count` | 1 | 1 | player-controlled party count |
| `0xC1` | `text_speed` | 1 | 1 | selected text speed |
| `0xC2` | `sound_setting` | 1 | 1 | sound setting |
| `0x1D4` | `timer` | 4 | 1 | global timer dword |
| `0x1D8` | `text_flavour` | 1 | 1 | text flavour byte |

### PARTY_CHARACTERS

- domain: `wram-root`
- address: `7E:99CE`
- stride: `0x5F`
- count: `6`
- struct: `char_struct`
- confidence: `corroborated`
- note: party char_struct array from ebsrc ram.asm
- evidence: `tools/lookup_wram_field.py`, `refs/ebsrc-main/ebsrc-main/include/structs.asm`, `refs/ebsrc-main/ebsrc-main/src/bankconfig/common/ram.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `name` | 1 | 5 | 5-byte party member name buffer |
| `0x5` | `level` | 1 | 1 | level |
| `0x6` | `exp` | 4 | 1 | experience dword |
| `0xA` | `max_hp` | 2 | 1 | max HP |
| `0xC` | `max_pp` | 2 | 1 | max PP |
| `0xE` | `afflictions` | 1 | 7 | char_struct affliction-group bytes |
| `0x15` | `offense` | 1 | 1 | display-facing offense |
| `0x16` | `defense` | 1 | 1 | display-facing defense |
| `0x17` | `speed` | 1 | 1 | display-facing speed |
| `0x18` | `guts` | 1 | 1 | display-facing guts |
| `0x19` | `luck` | 1 | 1 | display-facing luck |
| `0x1A` | `vitality` | 1 | 1 | display-facing vitality |
| `0x1B` | `iq` | 1 | 1 | display-facing IQ |
| `0x1C` | `base_offense` | 1 | 1 | base offense before equipment refresh |
| `0x1D` | `base_defense` | 1 | 1 | base defense before equipment refresh |
| `0x1E` | `base_speed` | 1 | 1 | base speed |
| `0x1F` | `base_guts` | 1 | 1 | base guts |
| `0x20` | `base_luck` | 1 | 1 | base luck |
| `0x21` | `base_vitality` | 1 | 1 | base vitality |
| `0x22` | `base_iq` | 1 | 1 | base IQ |
| `0x23` | `items` | 1 | 14 | inventory item ids |
| `0x31` | `equipment` | 1 | 4 | equipped item ids by slot family |
| `0x3D` | `position_index` | 2 | 1 | position index word |
| `0x43` | `current_hp_fraction` | 2 | 1 | HP rolling fraction |
| `0x45` | `current_hp` | 2 | 1 | current HP |
| `0x47` | `current_hp_target` | 2 | 1 | HP target |
| `0x49` | `current_pp_fraction` | 2 | 1 | PP rolling fraction |
| `0x4B` | `current_pp` | 2 | 1 | current PP |
| `0x4D` | `current_pp_target` | 2 | 1 | PP target |
| `0x4F` | `hp_pp_window_options` | 2 | 1 | HP/PP window options |
| `0x51` | `miss_rate` | 1 | 1 | miss-rate byte |
| `0x52` | `fire_resist` | 1 | 1 | fire resistance |
| `0x53` | `freeze_resist` | 1 | 1 | freeze resistance |
| `0x54` | `flash_resist` | 1 | 1 | flash resistance |
| `0x55` | `paralysis_resist` | 1 | 1 | paralysis resistance |
| `0x56` | `hypnosis_brainshock_resist` | 1 | 1 | hypnosis/brainshock resistance |
| `0x57` | `boosted_speed` | 1 | 1 | boosted speed adder |
| `0x58` | `boosted_guts` | 1 | 1 | boosted guts adder |
| `0x59` | `boosted_vitality` | 1 | 1 | boosted vitality adder |
| `0x5A` | `boosted_iq` | 1 | 1 | boosted IQ adder |
| `0x5B` | `boosted_luck` | 1 | 1 | boosted luck adder |

### BATTLERS_TABLE

- domain: `wram-root`
- address: `7E:9FAC`
- stride: `0x4E`
- count: `32`
- struct: `battler`
- confidence: `corroborated`
- note: battler array from ebsrc ram.asm
- evidence: `tools/lookup_wram_field.py`, `refs/ebsrc-main/ebsrc-main/include/structs.asm`, `refs/ebsrc-main/ebsrc-main/src/bankconfig/common/ram.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `id` | 2 | 1 | battler id |
| `0x2` | `sprite` | 1 | 1 | sprite id |
| `0x4` | `current_action` | 2 | 1 | current action id |
| `0x6` | `action_order_var` | 1 | 1 | action-order variable |
| `0x7` | `action_item_slot` | 1 | 1 | selected item slot |
| `0x8` | `current_action_argument` | 1 | 1 | current action argument |
| `0x9` | `action_targetting` | 1 | 1 | action targeting mode |
| `0xA` | `current_target` | 1 | 1 | current target id |
| `0xB` | `the_flag` | 1 | 1 | enemy data the_flag copy |
| `0xC` | `consciousness` | 1 | 1 | consciousness gate byte |
| `0xD` | `has_taken_turn` | 1 | 1 | turn-taken latch |
| `0xE` | `ally_or_enemy` | 1 | 1 | ally-or-enemy side byte |
| `0xF` | `npc_id` | 1 | 1 | NPC or enemy id |
| `0x10` | `row` | 1 | 1 | front/back row byte |
| `0x11` | `hp` | 2 | 1 | battle HP |
| `0x13` | `hp_target` | 2 | 1 | battle HP target |
| `0x15` | `hp_max` | 2 | 1 | battle max HP |
| `0x17` | `pp` | 2 | 1 | battle PP |
| `0x19` | `pp_target` | 2 | 1 | battle PP target |
| `0x1B` | `pp_max` | 2 | 1 | battle max PP |
| `0x1D` | `afflictions` | 1 | 7 | battler affliction-group bytes |
| `0x24` | `guarding` | 1 | 1 | guarding flag |
| `0x25` | `shield_hp` | 1 | 1 | shield HP |
| `0x26` | `offense` | 2 | 1 | battle offense |
| `0x28` | `defense` | 2 | 1 | battle defense |
| `0x2A` | `speed` | 2 | 1 | battle speed |
| `0x2C` | `guts` | 2 | 1 | battle guts |
| `0x2E` | `luck` | 2 | 1 | battle luck |
| `0x30` | `vitality` | 1 | 1 | battle vitality |
| `0x31` | `iq` | 1 | 1 | battle IQ |
| `0x32` | `base_offense` | 1 | 1 | base offense |
| `0x33` | `base_defense` | 1 | 1 | base defense |
| `0x34` | `base_speed` | 1 | 1 | base speed |
| `0x35` | `base_guts` | 1 | 1 | base guts |
| `0x36` | `base_luck` | 1 | 1 | base luck |
| `0x37` | `paralysis_resist` | 1 | 1 | paralysis resistance |
| `0x38` | `freeze_resist` | 1 | 1 | freeze resistance |
| `0x39` | `flash_resist` | 1 | 1 | flash resistance |
| `0x3A` | `fire_resist` | 1 | 1 | fire resistance |
| `0x3B` | `brainshock_resist` | 1 | 1 | brainshock resistance |
| `0x3C` | `hypnosis_resist` | 1 | 1 | hypnosis resistance |
| `0x3D` | `money` | 2 | 1 | money drop |
| `0x3F` | `exp` | 4 | 1 | experience yield |
| `0x43` | `vram_sprite_index` | 1 | 1 | VRAM sprite index |
| `0x44` | `sprite_x` | 1 | 1 | battle sprite X |
| `0x45` | `sprite_y` | 1 | 1 | battle sprite Y |
| `0x46` | `initiative` | 1 | 1 | initiative byte |
| `0x4B` | `use_alt_spritemap` | 1 | 1 | alternate spritemap flag |
| `0x4D` | `id2` | 1 | 1 | secondary id byte |

### ITEM_CONFIGURATION_TABLE

- domain: `rom-table`
- address: `D5:5000`
- stride: `0x27`
- count: `254`
- struct: `item`
- confidence: `corroborated`
- note: Fixed-stride item table used by C1/C2 inventory, equipment, and item-effect helpers.
- evidence: `refs/ebsrc-main/ebsrc-main/include/structs.asm`, `refs/ebsrc-main/ebsrc-main/include/symbols/misc.inc.asm`, `notes/d5-table-splits.md`, `notes/item-byte-19-packed-class-and-slot.md`, `manifests/coilsnake-field-semantics.json`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `name` | 1 | 25 | USA item-name buffer |
| `0x19` | `packed_class_and_slot` | 1 | 1 | item type byte; local notes decode class/equipment slot packing |
| `0x1A` | `cost` | 2 | 1 | store cost; CoilSnake `item-cost-probe` is runtime-correlated to the shop item row builder |
| `0x1C` | `flags` | 1 | 1 | item flags |
| `0x1D` | `effect` | 2 | 1 | item effect id |
| `0x1F` | `params` | 4 | 1 | item parameter dword |
| `0x23` | `help_text` | 4 | 1 | help text pointer |

### STORE_TABLE

- domain: `rom-table`
- address: `D5:76B2`
- stride: `0x7`
- count: `66`
- struct: `store_inventory`
- confidence: `corroborated`
- note: Store inventory rows immediately following the 254-row item table.
- evidence: `refs/eb-decompile-4ef92/store_table.yml`, `notes/d5-table-splits.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `item_id_0` | 1 | 1 |  |
| `0x1` | `item_id_1` | 1 | 1 |  |
| `0x2` | `item_id_2` | 1 | 1 |  |
| `0x3` | `item_id_3` | 1 | 1 |  |
| `0x4` | `item_id_4` | 1 | 1 |  |
| `0x5` | `item_id_5` | 1 | 1 |  |
| `0x6` | `item_id_6` | 1 | 1 |  |

### PSI_TELEPORT_DEST_TABLE

- domain: `rom-table`
- address: `D5:7880`
- stride: `0x1F`
- count: `16`
- struct: `psi_teleport_destination`
- confidence: `corroborated`
- note: Teleport-menu destination rows with fixed-width name, event flag, and map coordinates.
- evidence: `refs/eb-decompile-4ef92/psi_teleport_dest_table.yml`, `notes/landing-destination-table-d57880.md`, `notes/d5-table-splits.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `name` | 1 | 25 | fixed-width USA destination name |
| `0x19` | `event_flag` | 2 | 1 |  |
| `0x1B` | `x` | 2 | 1 |  |
| `0x1D` | `y` | 2 | 1 |  |

### TELEPHONE_CONTACTS_TABLE

- domain: `rom-table`
- address: `D5:7AAE`
- stride: `0x1F`
- count: `6`
- struct: `telephone_contact`
- confidence: `corroborated`
- note: Phone contact rows with fixed-width name, event flag, and text pointer.
- evidence: `refs/eb-decompile-4ef92/telephone_contacts_table.yml`, `notes/d5-table-splits.md`, CoilSnake `telephone-dad-text-pointer-probe`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `name` | 1 | 25 | fixed-width USA phone contact name |
| `0x19` | `event_flag` | 2 | 1 |  |
| `0x1B` | `text_pointer` | 4 | 1 |  |

### BATTLE_ACTION_TABLE

- domain: `rom-table`
- address: `D5:7B68`
- stride: `0xC`
- count: `318`
- struct: `battle_action`
- confidence: `corroborated`
- note: Battle action rows consumed by targetting, menu, PP-cost, text, and battle-function dispatch paths.
- evidence: `refs/ebsrc-main/ebsrc-main/include/structs.asm`, `refs/ebsrc-main/ebsrc-main/src/data/battle/action_table.asm`, `notes/d5-table-splits.md`, `notes/battle-targetting-resolver-c1adb4-af50.md`, `notes/battle-psi-menu-controller-c1cc39-ce73.md`, `manifests/coilsnake-field-semantics.json`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `direction` | 1 | 1 | enemy/ally/immediate direction selector |
| `0x1` | `target` | 1 | 1 | target subtype consumed by the C1 targetting resolver |
| `0x2` | `type` | 1 | 1 | battle action type |
| `0x3` | `pp_cost` | 1 | 1 | PSI/action PP cost; CoilSnake `battle-action-pp-cost-probe` is runtime-correlated to the C1:CC39 battle PSI PP guard |
| `0x4` | `description_text_pointer` | 4 | 1 | battle text pointer |
| `0x8` | `battle_function_pointer` | 4 | 1 | battle action handler pointer |

### PSI_ABILITY_TABLE

- domain: `rom-table`
- address: `D5:8A50`
- stride: `0xF`
- count: `54`
- struct: `psi_ability`
- confidence: `corroborated`
- note: PSI menu metadata table, including linked battle action ids and learn levels.
- evidence: `refs/ebsrc-main/ebsrc-main/include/structs.asm`, `refs/ebsrc-main/ebsrc-main/include/symbols/misc.inc.asm`, `notes/d5-table-splits.md`, `notes/battle-psi-ability-table-d58a50.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `name` | 1 | 1 | PSI name id |
| `0x1` | `level` | 1 | 1 | PSI alpha/beta/gamma/omega level |
| `0x2` | `category` | 1 | 1 |  |
| `0x3` | `usability` | 1 | 1 | menu/use gating byte |
| `0x4` | `battle_action` | 2 | 1 | linked D5:7B68 battle action id |
| `0x6` | `ness_level` | 1 | 1 |  |
| `0x7` | `paula_level` | 1 | 1 |  |
| `0x8` | `poo_level` | 1 | 1 |  |
| `0x9` | `menu_x` | 1 | 1 |  |
| `0xA` | `menu_y` | 1 | 1 |  |
| `0xB` | `text` | 4 | 1 | description text pointer |

### PSI_NAME_TABLE

- domain: `rom-table`
- address: `D5:8D7A`
- stride: `0x19`
- count: `17`
- struct: `psi_name`
- confidence: `corroborated`
- note: Fixed-width PSI display names.
- evidence: `refs/eb-decompile-4ef92/psi_name_table.yml`, `notes/d5-table-splits.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `name` | 1 | 25 | fixed-width USA PSI name |

### NPC_AI_TABLE

- domain: `rom-table`
- address: `D5:8F23`
- stride: `0x1`
- count: `38`
- struct: `npc_ai_selector`
- confidence: `corroborated`
- note: One-byte NPC battle AI selector table.
- evidence: `refs/ebsrc-main/ebsrc-main/src/data/battle/npc_ai_table.asm`, `notes/d5-table-splits.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `value` | 1 | 1 |  |

### EXP_TABLE

- domain: `rom-table`
- address: `D5:8F49`
- stride: `0x190`
- count: `4`
- struct: `character_exp_curve`
- confidence: `corroborated`
- note: Four character EXP curves with 100 32-bit thresholds per curve.
- evidence: `refs/eb-decompile-4ef92/exp_table.yml`, `notes/d5-table-splits.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `level_1_to_100_exp` | 4 | 100 | little-endian EXP thresholds |

### ENEMY_CONFIGURATION_TABLE

- domain: `rom-table`
- address: `D5:9589`
- stride: `0x5E`
- count: `231`
- struct: `enemy_data`
- confidence: `corroborated`
- note: Enemy configuration records copied into battler slots by the C2 battle-init paths.
- evidence: `refs/ebsrc-main/ebsrc-main/include/structs.asm`, `refs/ebsrc-main/ebsrc-main/include/symbols/misc.inc.asm`, `notes/d5-table-splits.md`, `notes/class2-005e-record-domain.md`, `notes/class2-local-enemy-id-to-battler-init-chain.md`, `notes/class2-d59589-enemy-data-crosswalk.md`, `manifests/coilsnake-field-semantics.json`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `the_flag` | 1 | 1 |  |
| `0x1` | `name` | 1 | 25 | USA enemy-name buffer |
| `0x1A` | `gender` | 1 | 1 |  |
| `0x1B` | `type` | 1 | 1 |  |
| `0x1C` | `battle_sprite` | 2 | 1 |  |
| `0x1E` | `overworld_sprite` | 2 | 1 |  |
| `0x20` | `run_flag` | 1 | 1 |  |
| `0x21` | `hp` | 2 | 1 |  |
| `0x23` | `pp` | 2 | 1 |  |
| `0x25` | `exp` | 4 | 1 |  |
| `0x29` | `money` | 2 | 1 |  |
| `0x2B` | `event_script` | 2 | 1 |  |
| `0x2D` | `encounter_text_ptr` | 4 | 1 |  |
| `0x31` | `death_text_ptr` | 4 | 1 |  |
| `0x35` | `battle_sprite_palette` | 1 | 1 |  |
| `0x36` | `level` | 1 | 1 |  |
| `0x37` | `music` | 1 | 1 |  |
| `0x38` | `offense` | 2 | 1 |  |
| `0x3A` | `defense` | 2 | 1 |  |
| `0x3C` | `speed` | 1 | 1 |  |
| `0x3D` | `guts` | 1 | 1 |  |
| `0x3E` | `luck` | 1 | 1 |  |
| `0x3F` | `fire_vulnerability` | 1 | 1 |  |
| `0x40` | `freeze_vulnerability` | 1 | 1 |  |
| `0x41` | `flash_vulnerability` | 1 | 1 |  |
| `0x42` | `paralysis_vulnerability` | 1 | 1 |  |
| `0x43` | `hypnosis_brainshock_vulnerability` | 1 | 1 |  |
| `0x44` | `miss_rate` | 1 | 1 |  |
| `0x45` | `action_order` | 1 | 1 |  |
| `0x46` | `actions` | 2 | 4 | normal action ids; CoilSnake `enemy-insane-cultist-action1-probe` is runtime-correlated to the C2:5024 enemy action-slot staging path |
| `0x4E` | `final_action` | 2 | 1 |  |
| `0x50` | `action_args` | 1 | 4 | arguments for normal actions |
| `0x54` | `final_action_arg` | 1 | 1 |  |
| `0x55` | `iq` | 1 | 1 |  |
| `0x56` | `boss` | 1 | 1 |  |
| `0x57` | `item_drop_rate` | 1 | 1 | locally still softer than the core 0x5E enemy record match |
| `0x58` | `item_dropped` | 1 | 1 | locally still softer than the core 0x5E enemy record match |
| `0x59` | `initial_status` | 1 | 1 |  |
| `0x5A` | `death_type` | 1 | 1 |  |
| `0x5B` | `row` | 1 | 1 |  |
| `0x5C` | `max_called` | 1 | 1 |  |
| `0x5D` | `mirror_success` | 1 | 1 |  |

### STATS_GROWTH_VARS

- domain: `rom-table`
- address: `D5:EA5B`
- stride: `0x7`
- count: `4`
- struct: `stats_growth_vars`
- confidence: `corroborated`
- note: Seven-byte per-character stat growth parameter rows.
- evidence: `refs/eb-decompile-4ef92/stats_growth_vars.yml`, `notes/d5-table-splits.md`, CoilSnake `stats-growth-ness-offense-probe`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `offense` | 1 | 1 |  |
| `0x1` | `defense` | 1 | 1 |  |
| `0x2` | `speed` | 1 | 1 |  |
| `0x3` | `guts` | 1 | 1 |  |
| `0x4` | `vitality` | 1 | 1 |  |
| `0x5` | `iq` | 1 | 1 |  |
| `0x6` | `luck` | 1 | 1 |  |

### CONDIMENT_TABLE

- domain: `rom-table`
- address: `D5:EA77`
- stride: `0x7`
- count: `44`
- struct: `condiment_rule`
- confidence: `corroborated`
- note: Food/condiment pairing table with recovery and runtime effect bytes.
- evidence: `refs/eb-decompile-4ef92/condiment_table.yml`, `notes/d5-table-splits.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `food` | 1 | 1 |  |
| `0x1` | `condiment_1` | 1 | 1 |  |
| `0x2` | `condiment_2` | 1 | 1 |  |
| `0x3` | `effect` | 1 | 1 |  |
| `0x4` | `good_recover` | 1 | 1 |  |
| `0x5` | `bad_recover` | 1 | 1 |  |
| `0x6` | `run_time` | 1 | 1 |  |

### TELEPORT_DESTINATION_TABLE

- domain: `rom-table`
- address: `D5:EBAB`
- stride: `0x8`
- count: `234`
- struct: `teleport_destination`
- confidence: `corroborated`
- note: Map teleport destination coordinate/style rows.
- evidence: `refs/eb-decompile-4ef92/teleport_destination_table.yml`, `notes/d5-table-splits.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `x` | 2 | 1 |  |
| `0x2` | `y` | 2 | 1 |  |
| `0x4` | `direction` | 1 | 1 |  |
| `0x5` | `warp_style` | 1 | 1 |  |
| `0x6` | `unknown` | 1 | 1 |  |
| `0x7` | `reserved` | 1 | 1 |  |

### MAP_HOTSPOTS

- domain: `rom-table`
- address: `D5:F2FB`
- stride: `0x8`
- count: `56`
- struct: `map_hotspot`
- confidence: `corroborated`
- note: Rectangular map hotspot coordinate records.
- evidence: `refs/eb-decompile-4ef92/map_hotspots.yml`, `notes/d5-table-splits.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `x1` | 2 | 1 |  |
| `0x2` | `y1` | 2 | 1 |  |
| `0x4` | `x2` | 2 | 1 |  |
| `0x6` | `y2` | 2 | 1 |  |

### TIMED_ITEM_TRANSFORMATION_TABLE

- domain: `rom-table`
- address: `D5:F4BB`
- stride: `0x5`
- count: `4`
- struct: `timed_item_transformation`
- confidence: `corroborated`
- note: Timed item conversion rows for delayed item changes and sound feedback.
- evidence: `refs/eb-decompile-4ef92/timed_item_transformation_table.yml`, `notes/d5-table-splits.md`, CoilSnake `timed-item-transform-delay-probe`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `item_id` | 1 | 1 |  |
| `0x1` | `sound_effect` | 1 | 1 |  |
| `0x2` | `sound_frequency` | 1 | 1 |  |
| `0x3` | `new_item` | 1 | 1 |  |
| `0x4` | `delay` | 1 | 1 |  |

### DONT_CARE_NAMES

- domain: `rom-table`
- address: `D5:F4CF`
- stride: `0x2A`
- count: `7`
- struct: `default_name_set`
- confidence: `corroborated`
- note: Default naming-screen choices as seven fixed-width names per row.
- evidence: `refs/eb-decompile-4ef92/dont_care_names.yml`, `notes/d5-table-splits.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `name_1` | 1 | 6 | fixed-width USA name |
| `0x6` | `name_2` | 1 | 6 | fixed-width USA name |
| `0xC` | `name_3` | 1 | 6 | fixed-width USA name |
| `0x12` | `name_4` | 1 | 6 | fixed-width USA name |
| `0x18` | `name_5` | 1 | 6 | fixed-width USA name |
| `0x1E` | `name_6` | 1 | 6 | fixed-width USA name |
| `0x24` | `name_7` | 1 | 6 | fixed-width USA name |

### INITIAL_STATS

- domain: `rom-table`
- address: `D5:F5F5`
- stride: `0x15`
- count: `4`
- struct: `initial_party_member_stats`
- confidence: `corroborated`
- note: Initial character setup rows with level, money, EXP, and starting inventory.
- evidence: `refs/eb-decompile-4ef92/initial_stats.yml`, `notes/d5-table-splits.md`, CoilSnake `initial-stats-ness-money-probe`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `unknown` | 1 | 4 |  |
| `0x4` | `money` | 2 | 1 |  |
| `0x6` | `level` | 1 | 1 |  |
| `0x7` | `experience_points` | 4 | 1 |  |
| `0xB` | `items_possessed` | 1 | 10 |  |

### TIMED_DELIVERY_TABLE

- domain: `rom-table`
- address: `D5:F649`
- stride: `0x14`
- count: `10`
- struct: `timed_delivery_source_window`
- confidence: `exact-source-window`
- note: Exact source-order timed-delivery split window; it starts four bytes into the EF consumer-effective controller rows at D5:F645 and ends with four zero padding bytes.
- evidence: `refs/eb-decompile-4ef92/timed_delivery_table.yml`, `notes/d5-table-splits.md`, `notes/delivery-row-helpers-ef0e67-ef0ead.md`, `notes/d5-timed-delivery-row-contracts.md`, CoilSnake `timed-delivery-first-timer-probe`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `source_window_bytes` | 1 | 20 | 20-byte source-order window beginning at D5:F649; this starts at +0x04 into effective controller row 0, so use TIMED_DELIVERY_CONTROLLER_TABLE for row-aligned fields |

### TIMED_DELIVERY_CONTROLLER_TABLE

- domain: `rom-table`
- address: `D5:F645`
- stride: `0x14`
- count: `10`
- struct: `timed_delivery_controller_row`
- confidence: `consumer-corroborated`
- note: Consumer-effective timed-delivery/service table base used by the EF:0CA7..0EE8 helper family and the C1 1F D3 row-selector callback.
- evidence: `notes/d5-timed-delivery-row-contracts.md`, `notes/delivery-row-helpers-ef0e67-ef0ead.md`, `notes/timed-delivery-controller-499-500-common.md`, `notes/timed-delivery-row-index-command-1f-d3.md`, `notes/selector-row-config-family-ef0ee8.md`, `src/ef/ef_0ca7_delivery_selector_helper_cluster.asm`, `notes/coilsnake-field-join-report.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `sprite_object_descriptor` | 2 | 1 | record word 0; EF:0EAD/EF:0EE8 pass this descriptor to C0:1E49, with a placeholder fallback when zero |
| `0x2` | `event_flag_gate` | 2 | 1 | record word 1; EF:0EE8 tests this through C2:1628 before selecting the row |
| `0x4` | `retry_threshold` | 2 | 1 | record word 2; EF:0CA7 compares the row-local retry counter against this threshold, with 0xFFFF supported as an immediate-success sentinel |
| `0x6` | `retry_wait_seconds` | 2 | 1 | record word 3; EF:0D23 returns this to the 499+500_common one-second retry loop |
| `0x8` | `delivery_time` | 2 | 1 | record word 4; EF:0D46 seeds the row-local countdown from this field |
| `0xA` | `success_pointer_low_word` | 2 | 1 | low word of pointer 1; EF:0D8D queues this as staged queue type 0x0008 |
| `0xC` | `success_pointer_bank` | 1 | 1 | bank byte of pointer 1 |
| `0xD` | `failure_pointer_low_word` | 2 | 1 | low word of pointer 2; EF:0DFA queues this as staged queue type 0x000A |
| `0xF` | `failure_pointer_bank` | 1 | 1 | bank byte of pointer 2 |
| `0x10` | `enter_speed` | 2 | 1 | record word 8; EF:0E67 returns this for the arrival-side movement branch |
| `0x12` | `exit_speed` | 2 | 1 | record word 9; EF:0E8A returns this for the departure-side movement branch |

### CF_DOOR_DATA

- domain: `rom-block`
- address: `CF:0000`
- stride: `0x264F`
- count: `1`
- struct: `cf_door_data_payload`
- confidence: `consumer-corroborated-partial`
- note: CF door-data payload block before the 1280 counted sector door-list records. Type 0, type 2, and type 6 payload shapes are decoded by the CF door-data contract; remaining trigger-type parameters stay bounded/raw.
- evidence: `notes/cf-table-splits.md`, `notes/cf-sector-list-contracts.md`, `notes/cf-door-data-contracts.md`, `refs/ebsrc-main/ebsrc-main/src/bankconfig/common/bank0f.asm`, `src/c0/c0_6a1b_movement_trigger_type0_queue_door_destination.asm`, `src/c0/c0_6aca_movement_trigger_type2_queue_door_transition.asm`, `src/c0/c0_6bff_run_deferred_script_pointer_and_refresh_transition_state.asm`, `src/c0/c0_65c2_probe_type6_door_candidate.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `raw_payload` | 1 | 9807 | exact CF door-data payload block; see notes/cf-door-data-contracts.json for consumer-backed type 0 event-gated script pointers, type 2 door-transition records, and type 6 cached interaction pointers |

### CF_DOOR_CONFIG_TABLE

- domain: `rom-variable-table`
- address: `CF:264F`
- stride: `0x32A0`
- count: `1`
- struct: `door_sector_list_block`
- confidence: `exact-variable-lists`
- note: 1280 D0-pointer-addressed counted door/trigger sector lists with complete decoded rows in notes/cf-sector-list-contracts.json and per-type trigger payload semantics in notes/cf-movement-trigger-contracts.json. Source-order physical rows match the map_doors bundle count; a small set of pointer starts overlap prior counted-list tails, so consumers should follow D0 pointers rather than assume a flat sequential table.
- evidence: `notes/cf-table-splits.md`, `notes/cf-sector-list-contracts.md`, `notes/cf-movement-trigger-contracts.md`, `refs/ebsrc-main/ebsrc-main/src/bankconfig/common/bank0f.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `counted_door_sector_lists` | 1 | 12960 | 1280 D0-pointer-addressed counted sector door/trigger lists; see notes/cf-sector-list-contracts.json for complete decoded lists and notes/cf-movement-trigger-contracts.json for trigger_payload_word meanings by movement_trigger_type |

### D0_DOOR_POINTER_TABLE

- domain: `rom-table`
- address: `D0:0000`
- stride: `0x4`
- count: `1280`
- struct: `door_sector_list_far_pointer`
- confidence: `exact`
- note: 40x32 long-pointer grid into the CF door sector lists.
- evidence: `notes/cf-table-splits.md`, `notes/cf-sector-list-contracts.md`, `refs/ebsrc-main/ebsrc-main/src/bankconfig/common/bank10.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `door_sector_list_pointer_low_word` | 2 | 1 | low word of a CF door sector-list start inside CF:264F..CF:58EE |
| `0x2` | `door_sector_list_pointer_bank` | 1 | 1 | bank byte; validated as CF for all 1280 rows |
| `0x3` | `reserved` | 1 | 1 | zero pad byte in the four-byte long-pointer row |

### SCREEN_TRANSITION_CONFIG_TABLE

- domain: `rom-table`
- address: `D0:1400`
- stride: `0xC`
- count: `34`
- struct: `screen_transition_config`
- confidence: `corroborated`
- note: Fixed-size screen transition configuration rows before the event-control pointer table.
- evidence: `refs/ebsrc-main/ebsrc-main/include/structs.asm`, `notes/d0-table-splits.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `duration` | 1 | 1 |  |
| `0x1` | `animation_id` | 1 | 1 |  |
| `0x2` | `animation_flags` | 1 | 1 |  |
| `0x3` | `fade_style` | 1 | 1 |  |
| `0x4` | `direction` | 1 | 1 |  |
| `0x5` | `unknown5` | 1 | 1 |  |
| `0x6` | `slide_speed` | 1 | 1 |  |
| `0x7` | `start_sound_effect` | 1 | 1 |  |
| `0x8` | `secondary_duration` | 1 | 1 |  |
| `0x9` | `secondary_animation_id` | 1 | 1 |  |
| `0xA` | `secondary_animation_flags` | 1 | 1 |  |
| `0xB` | `ending_sound_effect` | 1 | 1 |  |

### EVENT_CONTROL_PTR_TABLE

- domain: `rom-table`
- address: `D0:1598`
- stride: `0x2`
- count: `20`
- struct: `word_pointer`
- confidence: `exact`
- note: Word offsets to the 20 MAP_TILE_EVENT chains; C0:0703 indexes this table by tileset/event-control id.
- evidence: `refs/ebsrc-main/ebsrc-main/src/data/event_control_ptr_table.asm`, `notes/d0-table-splits.md`, `notes/d0-tile-event-contracts.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `pointer` | 2 | 1 |  |

### MAP_TILE_EVENT_CONTROL_TABLE

- domain: `rom-variable-table`
- address: `D0:15C0`
- stride: `0x2C0`
- count: `1`
- struct: `map_tile_event_chain_block`
- confidence: `exact-variable-chains`
- note: 20 variable MAP_TILE_EVENT chains. Each nonzero condition header is event_flag_condition_word plus replacement_pair_count, followed by target/source replacement-block pairs consumed by C0:062A.
- evidence: `refs/ebsrc-main/ebsrc-main/include/structs.asm`, `notes/d0-table-splits.md`, `notes/d0-tile-event-contracts.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `raw_event_chains` | 1 | 704 | 20 variable MAP_TILE_EVENT chains; see notes/d0-tile-event-contracts.json for decoded event-condition headers and replacement pairs |

### MAP_ENEMY_PLACEMENT

- domain: `rom-table`
- address: `D0:1880`
- stride: `0x2`
- count: `20480`
- struct: `map_enemy_placement`
- confidence: `corroborated`
- note: 20480 word enemy-map-group entries.
- evidence: `refs/eb-decompile-4ef92/map_enemy_placement.yml`, `notes/d0-table-splits.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `enemy_map_group` | 2 | 1 |  |

### ENEMY_PLACEMENT_GROUPS_PTR_TABLE

- domain: `rom-table`
- address: `D0:B880`
- stride: `0x4`
- count: `203`
- struct: `far_pointer`
- confidence: `exact`
- note: Long pointers into ENEMY_PLACEMENT_GROUPS_TABLE.
- evidence: `refs/eb-decompile-4ef92/map_enemy_groups.yml`, `notes/d0-table-splits.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `pointer` | 4 | 1 |  |

### ENEMY_PLACEMENT_GROUPS_TABLE

- domain: `rom-variable-table`
- address: `D0:BBAC`
- stride: `0xA61`
- count: `1`
- struct: `enemy_placement_group_lists`
- confidence: `exact-variable-lists`
- note: 203 variable enemy placement group lists: event_flag_gate, primary_spawn_chance, flagged_spawn_chance, then selection_weight + battle_group_id entries consumed by C0:2668.
- evidence: `refs/eb-decompile-4ef92/map_enemy_groups.yml`, `notes/d0-table-splits.md`, `notes/d0-variable-list-contracts.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `raw_group_lists` | 1 | 2657 | 203 variable enemy placement group lists; see notes/d0-variable-list-contracts.json for decoded headers and weighted entries |

### BTL_ENTRY_PTR_TABLE

- domain: `rom-table`
- address: `D0:C60D`
- stride: `0x8`
- count: `484`
- struct: `battle_entry_ptr_entry`
- confidence: `corroborated`
- note: Battle-entry pointer records with run-away and letterbox metadata.
- evidence: `refs/ebsrc-main/ebsrc-main/include/structs.asm`, `refs/eb-decompile-4ef92/enemy_groups.yml`, `notes/d0-table-splits.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `enemy_list_pointer` | 4 | 1 | long pointer to a D0:D52D enemy battle-group list |
| `0x4` | `run_away_flag` | 2 | 1 |  |
| `0x6` | `run_away_flag_state` | 1 | 1 |  |
| `0x7` | `presentation_sprite_style` | 1 | 1 | C2 battle presentation paths pass this byte as Y to C2:D121 LoadPresentationSpriteResource |

### ENEMY_BATTLE_GROUPS_TABLE

- domain: `rom-variable-table`
- address: `D0:D52D`
- stride: `0xA87`
- count: `1`
- struct: `enemy_battle_group_payloads`
- confidence: `exact-variable-lists`
- note: Consumer-visible suffix slices addressed by BTL_ENTRY_PTR_TABLE; entries are repeat_count + enemy_id until an FF terminator and are consumed by C2 battle setup, sprite loading, and call-for-help selection.
- evidence: `refs/eb-decompile-4ef92/enemy_groups.yml`, `notes/d0-table-splits.md`, `notes/d0-variable-list-contracts.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `raw_battle_groups` | 1 | 2695 | consumer-visible battle group pointer slices; see notes/d0-variable-list-contracts.json for repeat-count enemy entries |

### D7_SECTOR_TILESET_PALETTE_TABLE

- domain: `rom-table`
- address: `D7:A800`
- stride: `0x1`
- count: `1280`
- struct: `map_sector_tileset_palette`
- confidence: `consumer-corroborated`
- note: 40x32 sector table whose packed byte is bits 3..7 tileset_id and bits 0..2 palette_variant; every row matches map-sector metadata and multiple C0/C4 consumers.
- evidence: `notes/d7-sector-metadata-contracts.md`, `notes/map-sector-bundles.md`, `src/c0/c0_08cf_derive_landing_region_profile_from_destination.asm`, `src/c0/c0_0ac5_load_vertical_movement_map_strip_payload.asm`, `src/c0/c0_0bdc_load_horizontal_movement_map_strip_payload.asm`, `src/c4/your_sanctuary_tile_arrangement_helpers.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `packed_tileset_palette` | 1 | 1 | bits 3..7 are tileset_id and bits 0..2 are palette_variant; exact join to map-sector metadata and D7A800 consumers |

### D7_SECTOR_CONTEXT_WORD_TABLE

- domain: `rom-table`
- address: `D7:B200`
- stride: `0x2`
- count: `1280`
- struct: `map_sector_context_word`
- confidence: `consumer-corroborated-low3`
- note: 40x32 sector context-word table. C0:0AA1 loads the full word to $438E; C0:2668, C0:3A94, and path-lane callers consume the low three bits, which match map-sector Setting for every row.
- evidence: `notes/d7-sector-metadata-contracts.md`, `notes/map-sector-bundles.md`, `src/c0/c0_0aa1_lookup_position_cell_context_word.asm`, `src/c0/c0_2668_resolve_spawn_probe_candidate_list.asm`, `src/c0/c0_3a94_refresh_position_derived_visual_context_class.asm`, `src/c0/c0_c0b4_copy_path_to_lane_from_party_path.asm`, `src/c0/c0_c19b_copy_path_to_lane_from_party_member_request.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `sector_context_word` | 2 | 1 | per-sector context word loaded by C0:0AA1 into $438E; low three bits match map-sector Setting and feed spawn, visual-context, and path-lane gates |

### MAP_TILE_COLLISION_DATA

- domain: `rom-table`
- address: `D8:0000`
- stride: `0x10`
- count: `2293`
- struct: `map_tile_collision_record`
- confidence: `consumer-corroborated`
- note: Contiguous pool of 16-byte metatile collision records; every D8 pointer-table entry resolves to one 4x4 surface/collision flag grid.
- evidence: `refs/ebsrc-main/ebsrc-main/src/bankconfig/common/bank18.asm`, `notes/d8-table-splits.md`, `notes/map-collision-pointer-contract.md`, `notes/map-collision-runtime-bit-contract.md`, `notes/d8-collision-subrecord-contracts.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `cell_r0_c0_surface_collision_flags` | 1 | 1 | surface/collision flags for one 4x4 metatile cell; D8 pointer tables expand these records into the .fts collision grid, and C0 runtime masks define 0x80 as observed high collision, 0x10 as special-surface coordinate latch, 0x04/0x08 as entity terrain-compatibility class, and 0x01/0x02 as preserved low surface modifiers with provisional gameplay labels |
| `0x1` | `cell_r0_c1_surface_collision_flags` | 1 | 1 | surface/collision flags for one 4x4 metatile cell; D8 pointer tables expand these records into the .fts collision grid, and C0 runtime masks define 0x80 as observed high collision, 0x10 as special-surface coordinate latch, 0x04/0x08 as entity terrain-compatibility class, and 0x01/0x02 as preserved low surface modifiers with provisional gameplay labels |
| `0x2` | `cell_r0_c2_surface_collision_flags` | 1 | 1 | surface/collision flags for one 4x4 metatile cell; D8 pointer tables expand these records into the .fts collision grid, and C0 runtime masks define 0x80 as observed high collision, 0x10 as special-surface coordinate latch, 0x04/0x08 as entity terrain-compatibility class, and 0x01/0x02 as preserved low surface modifiers with provisional gameplay labels |
| `0x3` | `cell_r0_c3_surface_collision_flags` | 1 | 1 | surface/collision flags for one 4x4 metatile cell; D8 pointer tables expand these records into the .fts collision grid, and C0 runtime masks define 0x80 as observed high collision, 0x10 as special-surface coordinate latch, 0x04/0x08 as entity terrain-compatibility class, and 0x01/0x02 as preserved low surface modifiers with provisional gameplay labels |
| `0x4` | `cell_r1_c0_surface_collision_flags` | 1 | 1 | surface/collision flags for one 4x4 metatile cell; D8 pointer tables expand these records into the .fts collision grid, and C0 runtime masks define 0x80 as observed high collision, 0x10 as special-surface coordinate latch, 0x04/0x08 as entity terrain-compatibility class, and 0x01/0x02 as preserved low surface modifiers with provisional gameplay labels |
| `0x5` | `cell_r1_c1_surface_collision_flags` | 1 | 1 | surface/collision flags for one 4x4 metatile cell; D8 pointer tables expand these records into the .fts collision grid, and C0 runtime masks define 0x80 as observed high collision, 0x10 as special-surface coordinate latch, 0x04/0x08 as entity terrain-compatibility class, and 0x01/0x02 as preserved low surface modifiers with provisional gameplay labels |
| `0x6` | `cell_r1_c2_surface_collision_flags` | 1 | 1 | surface/collision flags for one 4x4 metatile cell; D8 pointer tables expand these records into the .fts collision grid, and C0 runtime masks define 0x80 as observed high collision, 0x10 as special-surface coordinate latch, 0x04/0x08 as entity terrain-compatibility class, and 0x01/0x02 as preserved low surface modifiers with provisional gameplay labels |
| `0x7` | `cell_r1_c3_surface_collision_flags` | 1 | 1 | surface/collision flags for one 4x4 metatile cell; D8 pointer tables expand these records into the .fts collision grid, and C0 runtime masks define 0x80 as observed high collision, 0x10 as special-surface coordinate latch, 0x04/0x08 as entity terrain-compatibility class, and 0x01/0x02 as preserved low surface modifiers with provisional gameplay labels |
| `0x8` | `cell_r2_c0_surface_collision_flags` | 1 | 1 | surface/collision flags for one 4x4 metatile cell; D8 pointer tables expand these records into the .fts collision grid, and C0 runtime masks define 0x80 as observed high collision, 0x10 as special-surface coordinate latch, 0x04/0x08 as entity terrain-compatibility class, and 0x01/0x02 as preserved low surface modifiers with provisional gameplay labels |
| `0x9` | `cell_r2_c1_surface_collision_flags` | 1 | 1 | surface/collision flags for one 4x4 metatile cell; D8 pointer tables expand these records into the .fts collision grid, and C0 runtime masks define 0x80 as observed high collision, 0x10 as special-surface coordinate latch, 0x04/0x08 as entity terrain-compatibility class, and 0x01/0x02 as preserved low surface modifiers with provisional gameplay labels |
| `0xA` | `cell_r2_c2_surface_collision_flags` | 1 | 1 | surface/collision flags for one 4x4 metatile cell; D8 pointer tables expand these records into the .fts collision grid, and C0 runtime masks define 0x80 as observed high collision, 0x10 as special-surface coordinate latch, 0x04/0x08 as entity terrain-compatibility class, and 0x01/0x02 as preserved low surface modifiers with provisional gameplay labels |
| `0xB` | `cell_r2_c3_surface_collision_flags` | 1 | 1 | surface/collision flags for one 4x4 metatile cell; D8 pointer tables expand these records into the .fts collision grid, and C0 runtime masks define 0x80 as observed high collision, 0x10 as special-surface coordinate latch, 0x04/0x08 as entity terrain-compatibility class, and 0x01/0x02 as preserved low surface modifiers with provisional gameplay labels |
| `0xC` | `cell_r3_c0_surface_collision_flags` | 1 | 1 | surface/collision flags for one 4x4 metatile cell; D8 pointer tables expand these records into the .fts collision grid, and C0 runtime masks define 0x80 as observed high collision, 0x10 as special-surface coordinate latch, 0x04/0x08 as entity terrain-compatibility class, and 0x01/0x02 as preserved low surface modifiers with provisional gameplay labels |
| `0xD` | `cell_r3_c1_surface_collision_flags` | 1 | 1 | surface/collision flags for one 4x4 metatile cell; D8 pointer tables expand these records into the .fts collision grid, and C0 runtime masks define 0x80 as observed high collision, 0x10 as special-surface coordinate latch, 0x04/0x08 as entity terrain-compatibility class, and 0x01/0x02 as preserved low surface modifiers with provisional gameplay labels |
| `0xE` | `cell_r3_c2_surface_collision_flags` | 1 | 1 | surface/collision flags for one 4x4 metatile cell; D8 pointer tables expand these records into the .fts collision grid, and C0 runtime masks define 0x80 as observed high collision, 0x10 as special-surface coordinate latch, 0x04/0x08 as entity terrain-compatibility class, and 0x01/0x02 as preserved low surface modifiers with provisional gameplay labels |
| `0xF` | `cell_r3_c3_surface_collision_flags` | 1 | 1 | surface/collision flags for one 4x4 metatile cell; D8 pointer tables expand these records into the .fts collision grid, and C0 runtime masks define 0x80 as observed high collision, 0x10 as special-surface coordinate latch, 0x04/0x08 as entity terrain-compatibility class, and 0x01/0x02 as preserved low surface modifiers with provisional gameplay labels |

### MAP_DATA_TILE_COLLISION_PTR_TABLE

- domain: `rom-table`
- address: `EF:117B`
- stride: `0x4`
- count: `20`
- struct: `far_pointer`
- confidence: `exact`
- note: 20-entry long-pointer table anchoring the D8 tileset collision pointer-table family.
- evidence: `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank2f.asm`, `notes/d8-table-splits.md`, `notes/landing-hdma-dispatch-family-ef117b-c00d7e.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `pointer` | 4 | 1 |  |

### MAP_DATA_TILE_COLLISION_POINTERS_0

- domain: `rom-table`
- address: `D8:8F50`
- stride: `0x2`
- count: `832`
- struct: `map_tile_collision_record_offset`
- confidence: `exact`
- note: 16-byte-aligned word offsets into MAP_TILE_COLLISION_DATA for one tileset/profile collision table.
- evidence: `refs/ebsrc-main/ebsrc-main/src/bankconfig/common/bank18.asm`, `notes/d8-table-splits.md`, `notes/map-collision-pointer-contract.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `collision_record_offset` | 2 | 1 | 16-byte-aligned offset into D8:0000 MAP_TILE_COLLISION_DATA; 0x0000 is a real collision record, not a null pointer |

### MAP_DATA_TILE_COLLISION_POINTERS_1

- domain: `rom-table`
- address: `D8:95D0`
- stride: `0x2`
- count: `845`
- struct: `map_tile_collision_record_offset`
- confidence: `exact`
- note: 16-byte-aligned word offsets into MAP_TILE_COLLISION_DATA for one tileset/profile collision table.
- evidence: `refs/ebsrc-main/ebsrc-main/src/bankconfig/common/bank18.asm`, `notes/d8-table-splits.md`, `notes/map-collision-pointer-contract.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `collision_record_offset` | 2 | 1 | 16-byte-aligned offset into D8:0000 MAP_TILE_COLLISION_DATA; 0x0000 is a real collision record, not a null pointer |

### MAP_DATA_TILE_COLLISION_POINTERS_2

- domain: `rom-table`
- address: `D8:9C6A`
- stride: `0x2`
- count: `827`
- struct: `map_tile_collision_record_offset`
- confidence: `exact`
- note: 16-byte-aligned word offsets into MAP_TILE_COLLISION_DATA for one tileset/profile collision table.
- evidence: `refs/ebsrc-main/ebsrc-main/src/bankconfig/common/bank18.asm`, `notes/d8-table-splits.md`, `notes/map-collision-pointer-contract.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `collision_record_offset` | 2 | 1 | 16-byte-aligned offset into D8:0000 MAP_TILE_COLLISION_DATA; 0x0000 is a real collision record, not a null pointer |

### MAP_DATA_TILE_COLLISION_POINTERS_3

- domain: `rom-table`
- address: `D8:A2E0`
- stride: `0x2`
- count: `524`
- struct: `map_tile_collision_record_offset`
- confidence: `exact`
- note: 16-byte-aligned word offsets into MAP_TILE_COLLISION_DATA for one tileset/profile collision table.
- evidence: `refs/ebsrc-main/ebsrc-main/src/bankconfig/common/bank18.asm`, `notes/d8-table-splits.md`, `notes/map-collision-pointer-contract.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `collision_record_offset` | 2 | 1 | 16-byte-aligned offset into D8:0000 MAP_TILE_COLLISION_DATA; 0x0000 is a real collision record, not a null pointer |

### MAP_DATA_TILE_COLLISION_POINTERS_4

- domain: `rom-table`
- address: `D8:A6F8`
- stride: `0x2`
- count: `935`
- struct: `map_tile_collision_record_offset`
- confidence: `exact`
- note: 16-byte-aligned word offsets into MAP_TILE_COLLISION_DATA for one tileset/profile collision table.
- evidence: `refs/ebsrc-main/ebsrc-main/src/bankconfig/common/bank18.asm`, `notes/d8-table-splits.md`, `notes/map-collision-pointer-contract.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `collision_record_offset` | 2 | 1 | 16-byte-aligned offset into D8:0000 MAP_TILE_COLLISION_DATA; 0x0000 is a real collision record, not a null pointer |

### MAP_DATA_TILE_COLLISION_POINTERS_5

- domain: `rom-table`
- address: `D8:AE46`
- stride: `0x2`
- count: `287`
- struct: `map_tile_collision_record_offset`
- confidence: `exact`
- note: 16-byte-aligned word offsets into MAP_TILE_COLLISION_DATA for one tileset/profile collision table.
- evidence: `refs/ebsrc-main/ebsrc-main/src/bankconfig/common/bank18.asm`, `notes/d8-table-splits.md`, `notes/map-collision-pointer-contract.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `collision_record_offset` | 2 | 1 | 16-byte-aligned offset into D8:0000 MAP_TILE_COLLISION_DATA; 0x0000 is a real collision record, not a null pointer |

### MAP_DATA_TILE_COLLISION_POINTERS_6

- domain: `rom-table`
- address: `D8:B084`
- stride: `0x2`
- count: `875`
- struct: `map_tile_collision_record_offset`
- confidence: `exact`
- note: 16-byte-aligned word offsets into MAP_TILE_COLLISION_DATA for one tileset/profile collision table.
- evidence: `refs/ebsrc-main/ebsrc-main/src/bankconfig/common/bank18.asm`, `notes/d8-table-splits.md`, `notes/map-collision-pointer-contract.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `collision_record_offset` | 2 | 1 | 16-byte-aligned offset into D8:0000 MAP_TILE_COLLISION_DATA; 0x0000 is a real collision record, not a null pointer |

### MAP_DATA_TILE_COLLISION_POINTERS_7

- domain: `rom-table`
- address: `D8:B75A`
- stride: `0x2`
- count: `749`
- struct: `map_tile_collision_record_offset`
- confidence: `exact`
- note: 16-byte-aligned word offsets into MAP_TILE_COLLISION_DATA for one tileset/profile collision table.
- evidence: `refs/ebsrc-main/ebsrc-main/src/bankconfig/common/bank18.asm`, `notes/d8-table-splits.md`, `notes/map-collision-pointer-contract.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `collision_record_offset` | 2 | 1 | 16-byte-aligned offset into D8:0000 MAP_TILE_COLLISION_DATA; 0x0000 is a real collision record, not a null pointer |

### MAP_DATA_TILE_COLLISION_POINTERS_8

- domain: `rom-table`
- address: `D8:BD34`
- stride: `0x2`
- count: `628`
- struct: `map_tile_collision_record_offset`
- confidence: `exact`
- note: 16-byte-aligned word offsets into MAP_TILE_COLLISION_DATA for one tileset/profile collision table.
- evidence: `refs/ebsrc-main/ebsrc-main/src/bankconfig/common/bank18.asm`, `notes/d8-table-splits.md`, `notes/map-collision-pointer-contract.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `collision_record_offset` | 2 | 1 | 16-byte-aligned offset into D8:0000 MAP_TILE_COLLISION_DATA; 0x0000 is a real collision record, not a null pointer |

### MAP_DATA_TILE_COLLISION_POINTERS_9

- domain: `rom-table`
- address: `D8:C21C`
- stride: `0x2`
- count: `933`
- struct: `map_tile_collision_record_offset`
- confidence: `exact`
- note: 16-byte-aligned word offsets into MAP_TILE_COLLISION_DATA for one tileset/profile collision table.
- evidence: `refs/ebsrc-main/ebsrc-main/src/bankconfig/common/bank18.asm`, `notes/d8-table-splits.md`, `notes/map-collision-pointer-contract.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `collision_record_offset` | 2 | 1 | 16-byte-aligned offset into D8:0000 MAP_TILE_COLLISION_DATA; 0x0000 is a real collision record, not a null pointer |

### MAP_DATA_TILE_COLLISION_POINTERS_10

- domain: `rom-table`
- address: `D8:C966`
- stride: `0x2`
- count: `871`
- struct: `map_tile_collision_record_offset`
- confidence: `exact`
- note: 16-byte-aligned word offsets into MAP_TILE_COLLISION_DATA for one tileset/profile collision table.
- evidence: `refs/ebsrc-main/ebsrc-main/src/bankconfig/common/bank18.asm`, `notes/d8-table-splits.md`, `notes/map-collision-pointer-contract.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `collision_record_offset` | 2 | 1 | 16-byte-aligned offset into D8:0000 MAP_TILE_COLLISION_DATA; 0x0000 is a real collision record, not a null pointer |

### MAP_DATA_TILE_COLLISION_POINTERS_11

- domain: `rom-table`
- address: `D8:D034`
- stride: `0x2`
- count: `713`
- struct: `map_tile_collision_record_offset`
- confidence: `exact`
- note: 16-byte-aligned word offsets into MAP_TILE_COLLISION_DATA for one tileset/profile collision table.
- evidence: `refs/ebsrc-main/ebsrc-main/src/bankconfig/common/bank18.asm`, `notes/d8-table-splits.md`, `notes/map-collision-pointer-contract.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `collision_record_offset` | 2 | 1 | 16-byte-aligned offset into D8:0000 MAP_TILE_COLLISION_DATA; 0x0000 is a real collision record, not a null pointer |

### MAP_DATA_TILE_COLLISION_POINTERS_12

- domain: `rom-table`
- address: `D8:D5C6`
- stride: `0x2`
- count: `462`
- struct: `map_tile_collision_record_offset`
- confidence: `exact`
- note: 16-byte-aligned word offsets into MAP_TILE_COLLISION_DATA for one tileset/profile collision table.
- evidence: `refs/ebsrc-main/ebsrc-main/src/bankconfig/common/bank18.asm`, `notes/d8-table-splits.md`, `notes/map-collision-pointer-contract.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `collision_record_offset` | 2 | 1 | 16-byte-aligned offset into D8:0000 MAP_TILE_COLLISION_DATA; 0x0000 is a real collision record, not a null pointer |

### MAP_DATA_TILE_COLLISION_POINTERS_13

- domain: `rom-table`
- address: `D8:D962`
- stride: `0x2`
- count: `882`
- struct: `map_tile_collision_record_offset`
- confidence: `exact`
- note: 16-byte-aligned word offsets into MAP_TILE_COLLISION_DATA for one tileset/profile collision table.
- evidence: `refs/ebsrc-main/ebsrc-main/src/bankconfig/common/bank18.asm`, `notes/d8-table-splits.md`, `notes/map-collision-pointer-contract.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `collision_record_offset` | 2 | 1 | 16-byte-aligned offset into D8:0000 MAP_TILE_COLLISION_DATA; 0x0000 is a real collision record, not a null pointer |

### MAP_DATA_TILE_COLLISION_POINTERS_14

- domain: `rom-table`
- address: `D8:E046`
- stride: `0x2`
- count: `203`
- struct: `map_tile_collision_record_offset`
- confidence: `exact`
- note: 16-byte-aligned word offsets into MAP_TILE_COLLISION_DATA for one tileset/profile collision table.
- evidence: `refs/ebsrc-main/ebsrc-main/src/bankconfig/common/bank18.asm`, `notes/d8-table-splits.md`, `notes/map-collision-pointer-contract.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `collision_record_offset` | 2 | 1 | 16-byte-aligned offset into D8:0000 MAP_TILE_COLLISION_DATA; 0x0000 is a real collision record, not a null pointer |

### MAP_DATA_TILE_COLLISION_POINTERS_15

- domain: `rom-table`
- address: `D8:E1DC`
- stride: `0x2`
- count: `143`
- struct: `map_tile_collision_record_offset`
- confidence: `exact`
- note: 16-byte-aligned word offsets into MAP_TILE_COLLISION_DATA for one tileset/profile collision table.
- evidence: `refs/ebsrc-main/ebsrc-main/src/bankconfig/common/bank18.asm`, `notes/d8-table-splits.md`, `notes/map-collision-pointer-contract.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `collision_record_offset` | 2 | 1 | 16-byte-aligned offset into D8:0000 MAP_TILE_COLLISION_DATA; 0x0000 is a real collision record, not a null pointer |

### MAP_DATA_TILE_COLLISION_POINTERS_16

- domain: `rom-table`
- address: `D8:E2FA`
- stride: `0x2`
- count: `390`
- struct: `map_tile_collision_record_offset`
- confidence: `exact`
- note: 16-byte-aligned word offsets into MAP_TILE_COLLISION_DATA for one tileset/profile collision table.
- evidence: `refs/ebsrc-main/ebsrc-main/src/bankconfig/common/bank18.asm`, `notes/d8-table-splits.md`, `notes/map-collision-pointer-contract.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `collision_record_offset` | 2 | 1 | 16-byte-aligned offset into D8:0000 MAP_TILE_COLLISION_DATA; 0x0000 is a real collision record, not a null pointer |

### MAP_DATA_TILE_COLLISION_POINTERS_17

- domain: `rom-table`
- address: `D8:E606`
- stride: `0x2`
- count: `343`
- struct: `map_tile_collision_record_offset`
- confidence: `exact`
- note: 16-byte-aligned word offsets into MAP_TILE_COLLISION_DATA for one tileset/profile collision table.
- evidence: `refs/ebsrc-main/ebsrc-main/src/bankconfig/common/bank18.asm`, `notes/d8-table-splits.md`, `notes/map-collision-pointer-contract.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `collision_record_offset` | 2 | 1 | 16-byte-aligned offset into D8:0000 MAP_TILE_COLLISION_DATA; 0x0000 is a real collision record, not a null pointer |

### MAP_DATA_TILE_COLLISION_POINTERS_18

- domain: `rom-table`
- address: `D8:E8B4`
- stride: `0x2`
- count: `445`
- struct: `map_tile_collision_record_offset`
- confidence: `exact`
- note: 16-byte-aligned word offsets into MAP_TILE_COLLISION_DATA for one tileset/profile collision table.
- evidence: `refs/ebsrc-main/ebsrc-main/src/bankconfig/common/bank18.asm`, `notes/d8-table-splits.md`, `notes/map-collision-pointer-contract.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `collision_record_offset` | 2 | 1 | 16-byte-aligned offset into D8:0000 MAP_TILE_COLLISION_DATA; 0x0000 is a real collision record, not a null pointer |

### MAP_DATA_TILE_COLLISION_POINTERS_19

- domain: `rom-table`
- address: `D8:EC2E`
- stride: `0x2`
- count: `536`
- struct: `map_tile_collision_record_offset`
- confidence: `exact`
- note: 16-byte-aligned word offsets into MAP_TILE_COLLISION_DATA for one tileset/profile collision table.
- evidence: `refs/ebsrc-main/ebsrc-main/src/bankconfig/common/bank18.asm`, `notes/d8-table-splits.md`, `notes/map-collision-pointer-contract.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `collision_record_offset` | 2 | 1 | 16-byte-aligned offset into D8:0000 MAP_TILE_COLLISION_DATA; 0x0000 is a real collision record, not a null pointer |

### MAP_PALETTE_POINTER_TABLE

- domain: `rom-table`
- address: `DA:FAA7`
- stride: `0x3`
- count: `32`
- struct: `snes_long_pointer24`
- confidence: `verified`
- note: Thirty-two 24-bit pointers to the bank DA map-palette payloads; each entry matches the corresponding MAP_DATA_PALETTE_N asset.
- evidence: `notes/bank-da-asset-data-map.md`, `notes/map-palette-pointer-table-contract.md`, `notes/map-palette-descriptor-context.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `target_low_word` | 2 | 1 |  |
| `0x2` | `target_bank` | 1 | 1 |  |

### DA_MAP_PALETTE_VARIANT_TABLE

- domain: `rom-table`
- address: `DA:7CA7`
- stride: `0xC0`
- count: `168`
- struct: `da_map_palette_variant`
- confidence: `tool-and-script-corroborated`
- note: Contiguous physical DA map-palette variant rows. Each row is six 16-colour SNES BGR555 subpalettes; the first words of subpalettes 0..3 carry raw-ROM metadata that matches map_palette_settings and is zeroed in .fts visual rows.
- evidence: `notes/da-map-palette-subrecord-contracts.md`, `notes/map-fts-palette-variant-contract.md`, `notes/map-palette-pointer-table-contract.md`, `notes/map-palette-descriptor-context.md`, `notes/map-palette-command-usage-contract.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `event_flag` | 2 | 1 | raw ROM metadata word matching map_palette_settings; zeroed in .fts visual palette rows |
| `0x0` | `map_subpalette_0_colours` | 2 | 16 | 16 SNES BGR555 colours for arrangement descriptor palette 2 / CGRAM $0240..$025F; colour 0 overlaps event_flag in raw ROM |
| `0x20` | `event_palette_selector_word` | 2 | 1 | raw ROM metadata word whose presence matches event-palette payload settings; runtime dispatch semantics remain deferred |
| `0x20` | `map_subpalette_1_colours` | 2 | 16 | 16 SNES BGR555 colours for arrangement descriptor palette 3 / CGRAM $0260..$027F; colour 0 overlaps event_palette_selector_word in raw ROM |
| `0x40` | `sprite_palette` | 2 | 1 | raw ROM metadata word matching map_palette_settings Sprite Palette; zeroed in .fts visual palette rows |
| `0x40` | `map_subpalette_2_colours` | 2 | 16 | 16 SNES BGR555 colours for arrangement descriptor palette 4 / CGRAM $0280..$029F; colour 0 overlaps sprite_palette in raw ROM |
| `0x60` | `flash_effect` | 2 | 1 | raw ROM metadata word matching map_palette_settings Flash Effect; zeroed in .fts visual palette rows |
| `0x60` | `map_subpalette_3_colours` | 2 | 16 | 16 SNES BGR555 colours for arrangement descriptor palette 5 / CGRAM $02A0..$02BF; colour 0 overlaps flash_effect in raw ROM |
| `0x80` | `map_subpalette_4_colours` | 2 | 16 | 16 SNES BGR555 colours for arrangement descriptor palette 6 / CGRAM $02C0..$02DF |
| `0xA0` | `map_subpalette_5_colours` | 2 | 16 | 16 SNES BGR555 colours for arrangement descriptor palette 7 / CGRAM $02E0..$02FF |

### PER_SECTOR_MUSIC_TABLE

- domain: `rom-table`
- address: `DC:D637`
- stride: `0x2`
- count: `1280`
- struct: `per_sector_music_options_index`
- confidence: `structural-corroborated`
- note: 40x32 sector-indexed music-options table used by the map sector bundle inventory. The overlapping C0 byte-indexed selector plane is tracked separately as CURRENT_POSITION_EVENT_MUSIC_SELECTOR_TABLE.
- evidence: `notes/bank-dc-asset-data-map.md`, `notes/map-sector-bundles.md`, `tools/build_map_sector_bundle_contract.py`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `music_options_index` | 2 | 1 | 40x32 sector-indexed word joined to map_music.yml option lists by the map sector bundle contract |

### CURRENT_POSITION_EVENT_MUSIC_SELECTOR_TABLE

- domain: `rom-table`
- address: `DC:D637`
- stride: `0x1`
- count: `1280`
- struct: `current_position_event_music_context_selector`
- confidence: `consumer-corroborated`
- note: The byte-indexed first plane of DC:D637..DC:E036. C0:68F4 computes sector_y*32 + sector_x, reads this byte, and uses it as the selector into CF:58EF; it also matches map-sector Music for every checked sector row.
- evidence: `notes/cf-event-music-context-contracts.md`, `notes/map-sector-bundles.md`, `notes/c0-current-position-music-refresh-c068f4-c069af.md`, `src/c0/c0_65c2_probe_type6_door_candidate.asm`, `src/ef/ef_dcbc_de1a_debug_check_position_overlay.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `event_music_context_selector` | 1 | 1 | byte-indexed first plane at DC:D637; C0:68F4 and the EF debug overlay use this selector to index CF:58EF; matches map-sector Music for all 1280 rows |

### LANDING_PALETTE_ANIM_PROFILE_POINTER_TABLE

- domain: `rom-table`
- address: `DF:E4E1`
- stride: `0x4`
- count: `31`
- struct: `far_pointer`
- confidence: `runtime-corroborated`
- note: Thirty-one long pointers from landing palette/profile selector ($02A0 - 1) to DF:E55D..DF:E61B profile records.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `pointer` | 4 | 1 |  |

### LANDING_PALETTE_ANIM_PROFILE_0

- domain: `rom-variable-table`
- address: `DF:E55D`
- stride: `0x9`
- count: `1`
- struct: `landing_palette_anim_profile`
- confidence: `runtime-corroborated-shape`
- note: Landing palette-animation profile 0; C0:023F selects this record through DF:E4E1, decompresses DF:E61B, and copies 4 step bytes after the payload pointer.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/c0/c0_030f_advance_landing_profile_step_sequencer.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_palette_payload_pointer` | 4 | 1 | C0:023F decompresses this payload to 7E:B800 |
| `0x4` | `step_count` | 1 | 1 | C0:023F uses zero to skip loading the sequencer, otherwise bounds the step-duration copy |
| `0x5` | `step_durations` | 1 | 4 | one-byte sequencer values copied to $4460 by C0:023F and consumed by C0:030F |

### LANDING_PALETTE_ANIM_PROFILE_1

- domain: `rom-variable-table`
- address: `DF:E566`
- stride: `0x9`
- count: `1`
- struct: `landing_palette_anim_profile`
- confidence: `runtime-corroborated-shape`
- note: Landing palette-animation profile 1; C0:023F selects this record through DF:E4E1, decompresses DF:E6B2, and copies 4 step bytes after the payload pointer.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/c0/c0_030f_advance_landing_profile_step_sequencer.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_palette_payload_pointer` | 4 | 1 | C0:023F decompresses this payload to 7E:B800 |
| `0x4` | `step_count` | 1 | 1 | C0:023F uses zero to skip loading the sequencer, otherwise bounds the step-duration copy |
| `0x5` | `step_durations` | 1 | 4 | one-byte sequencer values copied to $4460 by C0:023F and consumed by C0:030F |

### LANDING_PALETTE_ANIM_PROFILE_2

- domain: `rom-variable-table`
- address: `DF:E56F`
- stride: `0xB`
- count: `1`
- struct: `landing_palette_anim_profile`
- confidence: `runtime-corroborated-shape`
- note: Landing palette-animation profile 2; C0:023F selects this record through DF:E4E1, decompresses DF:E73D, and copies 6 step bytes after the payload pointer.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/c0/c0_030f_advance_landing_profile_step_sequencer.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_palette_payload_pointer` | 4 | 1 | C0:023F decompresses this payload to 7E:B800 |
| `0x4` | `step_count` | 1 | 1 | C0:023F uses zero to skip loading the sequencer, otherwise bounds the step-duration copy |
| `0x5` | `step_durations` | 1 | 6 | one-byte sequencer values copied to $4460 by C0:023F and consumed by C0:030F |

### LANDING_PALETTE_ANIM_PROFILE_3

- domain: `rom-variable-table`
- address: `DF:E57A`
- stride: `0x8`
- count: `1`
- struct: `landing_palette_anim_profile`
- confidence: `runtime-corroborated-shape`
- note: Landing palette-animation profile 3; C0:023F selects this record through DF:E4E1, decompresses DF:E8E0, and copies 3 step bytes after the payload pointer.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/c0/c0_030f_advance_landing_profile_step_sequencer.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_palette_payload_pointer` | 4 | 1 | C0:023F decompresses this payload to 7E:B800 |
| `0x4` | `step_count` | 1 | 1 | C0:023F uses zero to skip loading the sequencer, otherwise bounds the step-duration copy |
| `0x5` | `step_durations` | 1 | 3 | one-byte sequencer values copied to $4460 by C0:023F and consumed by C0:030F |

### LANDING_PALETTE_ANIM_PROFILE_4

- domain: `rom-variable-table`
- address: `DF:E582`
- stride: `0x9`
- count: `1`
- struct: `landing_palette_anim_profile`
- confidence: `runtime-corroborated-shape`
- note: Landing palette-animation profile 4; C0:023F selects this record through DF:E4E1, decompresses DF:E96C, and copies 4 step bytes after the payload pointer.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/c0/c0_030f_advance_landing_profile_step_sequencer.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_palette_payload_pointer` | 4 | 1 | C0:023F decompresses this payload to 7E:B800 |
| `0x4` | `step_count` | 1 | 1 | C0:023F uses zero to skip loading the sequencer, otherwise bounds the step-duration copy |
| `0x5` | `step_durations` | 1 | 4 | one-byte sequencer values copied to $4460 by C0:023F and consumed by C0:030F |

### LANDING_PALETTE_ANIM_PROFILE_5

- domain: `rom-variable-table`
- address: `DF:E58B`
- stride: `0x8`
- count: `1`
- struct: `landing_palette_anim_profile`
- confidence: `runtime-corroborated-shape`
- note: Landing palette-animation profile 5; C0:023F selects this record through DF:E4E1, decompresses DF:EA56, and copies 3 step bytes after the payload pointer.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/c0/c0_030f_advance_landing_profile_step_sequencer.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_palette_payload_pointer` | 4 | 1 | C0:023F decompresses this payload to 7E:B800 |
| `0x4` | `step_count` | 1 | 1 | C0:023F uses zero to skip loading the sequencer, otherwise bounds the step-duration copy |
| `0x5` | `step_durations` | 1 | 3 | one-byte sequencer values copied to $4460 by C0:023F and consumed by C0:030F |

### LANDING_PALETTE_ANIM_PROFILE_6

- domain: `rom-variable-table`
- address: `DF:E593`
- stride: `0x8`
- count: `1`
- struct: `landing_palette_anim_profile`
- confidence: `runtime-corroborated-shape`
- note: Landing palette-animation profile 6; C0:023F selects this record through DF:E4E1, decompresses DF:EB31, and copies 3 step bytes after the payload pointer.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/c0/c0_030f_advance_landing_profile_step_sequencer.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_palette_payload_pointer` | 4 | 1 | C0:023F decompresses this payload to 7E:B800 |
| `0x4` | `step_count` | 1 | 1 | C0:023F uses zero to skip loading the sequencer, otherwise bounds the step-duration copy |
| `0x5` | `step_durations` | 1 | 3 | one-byte sequencer values copied to $4460 by C0:023F and consumed by C0:030F |

### LANDING_PALETTE_ANIM_PROFILE_7

- domain: `rom-variable-table`
- address: `DF:E59B`
- stride: `0xD`
- count: `1`
- struct: `landing_palette_anim_profile`
- confidence: `runtime-corroborated-shape`
- note: Landing palette-animation profile 7; C0:023F selects this record through DF:E4E1, decompresses DF:EBAC, and copies 8 step bytes after the payload pointer.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/c0/c0_030f_advance_landing_profile_step_sequencer.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_palette_payload_pointer` | 4 | 1 | C0:023F decompresses this payload to 7E:B800 |
| `0x4` | `step_count` | 1 | 1 | C0:023F uses zero to skip loading the sequencer, otherwise bounds the step-duration copy |
| `0x5` | `step_durations` | 1 | 8 | one-byte sequencer values copied to $4460 by C0:023F and consumed by C0:030F |

### LANDING_PALETTE_ANIM_PROFILE_8

- domain: `rom-variable-table`
- address: `DF:E5A8`
- stride: `0x5`
- count: `1`
- struct: `landing_palette_anim_profile`
- confidence: `runtime-corroborated-shape`
- note: Landing palette-animation profile 8; C0:023F selects this record through DF:E4E1, decompresses DF:EC46, and copies 0 step bytes after the payload pointer.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/c0/c0_030f_advance_landing_profile_step_sequencer.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_palette_payload_pointer` | 4 | 1 | C0:023F decompresses this payload to 7E:B800 |
| `0x4` | `step_count` | 1 | 1 | C0:023F uses zero to skip loading the sequencer, otherwise bounds the step-duration copy |

### LANDING_PALETTE_ANIM_PROFILE_9

- domain: `rom-variable-table`
- address: `DF:E5AD`
- stride: `0x5`
- count: `1`
- struct: `landing_palette_anim_profile`
- confidence: `runtime-corroborated-shape`
- note: Landing palette-animation profile 9; C0:023F selects this record through DF:E4E1, decompresses DF:EC46, and copies 0 step bytes after the payload pointer.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/c0/c0_030f_advance_landing_profile_step_sequencer.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_palette_payload_pointer` | 4 | 1 | C0:023F decompresses this payload to 7E:B800 |
| `0x4` | `step_count` | 1 | 1 | C0:023F uses zero to skip loading the sequencer, otherwise bounds the step-duration copy |

### LANDING_PALETTE_ANIM_PROFILE_10

- domain: `rom-variable-table`
- address: `DF:E5B2`
- stride: `0x5`
- count: `1`
- struct: `landing_palette_anim_profile`
- confidence: `runtime-corroborated-shape`
- note: Landing palette-animation profile 10; C0:023F selects this record through DF:E4E1, decompresses DF:EC46, and copies 0 step bytes after the payload pointer.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/c0/c0_030f_advance_landing_profile_step_sequencer.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_palette_payload_pointer` | 4 | 1 | C0:023F decompresses this payload to 7E:B800 |
| `0x4` | `step_count` | 1 | 1 | C0:023F uses zero to skip loading the sequencer, otherwise bounds the step-duration copy |

### LANDING_PALETTE_ANIM_PROFILE_11

- domain: `rom-variable-table`
- address: `DF:E5B7`
- stride: `0x5`
- count: `1`
- struct: `landing_palette_anim_profile`
- confidence: `runtime-corroborated-shape`
- note: Landing palette-animation profile 11; C0:023F selects this record through DF:E4E1, decompresses DF:EC46, and copies 0 step bytes after the payload pointer.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/c0/c0_030f_advance_landing_profile_step_sequencer.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_palette_payload_pointer` | 4 | 1 | C0:023F decompresses this payload to 7E:B800 |
| `0x4` | `step_count` | 1 | 1 | C0:023F uses zero to skip loading the sequencer, otherwise bounds the step-duration copy |

### LANDING_PALETTE_ANIM_PROFILE_12

- domain: `rom-variable-table`
- address: `DF:E5BC`
- stride: `0x5`
- count: `1`
- struct: `landing_palette_anim_profile`
- confidence: `runtime-corroborated-shape`
- note: Landing palette-animation profile 12; C0:023F selects this record through DF:E4E1, decompresses DF:EC46, and copies 0 step bytes after the payload pointer.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/c0/c0_030f_advance_landing_profile_step_sequencer.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_palette_payload_pointer` | 4 | 1 | C0:023F decompresses this payload to 7E:B800 |
| `0x4` | `step_count` | 1 | 1 | C0:023F uses zero to skip loading the sequencer, otherwise bounds the step-duration copy |

### LANDING_PALETTE_ANIM_PROFILE_13

- domain: `rom-variable-table`
- address: `DF:E5C1`
- stride: `0x5`
- count: `1`
- struct: `landing_palette_anim_profile`
- confidence: `runtime-corroborated-shape`
- note: Landing palette-animation profile 13; C0:023F selects this record through DF:E4E1, decompresses DF:EC46, and copies 0 step bytes after the payload pointer.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/c0/c0_030f_advance_landing_profile_step_sequencer.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_palette_payload_pointer` | 4 | 1 | C0:023F decompresses this payload to 7E:B800 |
| `0x4` | `step_count` | 1 | 1 | C0:023F uses zero to skip loading the sequencer, otherwise bounds the step-duration copy |

### LANDING_PALETTE_ANIM_PROFILE_14

- domain: `rom-variable-table`
- address: `DF:E5C6`
- stride: `0x5`
- count: `1`
- struct: `landing_palette_anim_profile`
- confidence: `runtime-corroborated-shape`
- note: Landing palette-animation profile 14; C0:023F selects this record through DF:E4E1, decompresses DF:EC46, and copies 0 step bytes after the payload pointer.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/c0/c0_030f_advance_landing_profile_step_sequencer.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_palette_payload_pointer` | 4 | 1 | C0:023F decompresses this payload to 7E:B800 |
| `0x4` | `step_count` | 1 | 1 | C0:023F uses zero to skip loading the sequencer, otherwise bounds the step-duration copy |

### LANDING_PALETTE_ANIM_PROFILE_15

- domain: `rom-variable-table`
- address: `DF:E5CB`
- stride: `0x5`
- count: `1`
- struct: `landing_palette_anim_profile`
- confidence: `runtime-corroborated-shape`
- note: Landing palette-animation profile 15; C0:023F selects this record through DF:E4E1, decompresses DF:EC46, and copies 0 step bytes after the payload pointer.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/c0/c0_030f_advance_landing_profile_step_sequencer.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_palette_payload_pointer` | 4 | 1 | C0:023F decompresses this payload to 7E:B800 |
| `0x4` | `step_count` | 1 | 1 | C0:023F uses zero to skip loading the sequencer, otherwise bounds the step-duration copy |

### LANDING_PALETTE_ANIM_PROFILE_16

- domain: `rom-variable-table`
- address: `DF:E5D0`
- stride: `0x5`
- count: `1`
- struct: `landing_palette_anim_profile`
- confidence: `runtime-corroborated-shape`
- note: Landing palette-animation profile 16; C0:023F selects this record through DF:E4E1, decompresses DF:EC46, and copies 0 step bytes after the payload pointer.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/c0/c0_030f_advance_landing_profile_step_sequencer.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_palette_payload_pointer` | 4 | 1 | C0:023F decompresses this payload to 7E:B800 |
| `0x4` | `step_count` | 1 | 1 | C0:023F uses zero to skip loading the sequencer, otherwise bounds the step-duration copy |

### LANDING_PALETTE_ANIM_PROFILE_17

- domain: `rom-variable-table`
- address: `DF:E5D5`
- stride: `0x5`
- count: `1`
- struct: `landing_palette_anim_profile`
- confidence: `runtime-corroborated-shape`
- note: Landing palette-animation profile 17; C0:023F selects this record through DF:E4E1, decompresses DF:EC46, and copies 0 step bytes after the payload pointer.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/c0/c0_030f_advance_landing_profile_step_sequencer.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_palette_payload_pointer` | 4 | 1 | C0:023F decompresses this payload to 7E:B800 |
| `0x4` | `step_count` | 1 | 1 | C0:023F uses zero to skip loading the sequencer, otherwise bounds the step-duration copy |

### LANDING_PALETTE_ANIM_PROFILE_18

- domain: `rom-variable-table`
- address: `DF:E5DA`
- stride: `0x5`
- count: `1`
- struct: `landing_palette_anim_profile`
- confidence: `runtime-corroborated-shape`
- note: Landing palette-animation profile 18; C0:023F selects this record through DF:E4E1, decompresses DF:EC46, and copies 0 step bytes after the payload pointer.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/c0/c0_030f_advance_landing_profile_step_sequencer.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_palette_payload_pointer` | 4 | 1 | C0:023F decompresses this payload to 7E:B800 |
| `0x4` | `step_count` | 1 | 1 | C0:023F uses zero to skip loading the sequencer, otherwise bounds the step-duration copy |

### LANDING_PALETTE_ANIM_PROFILE_19

- domain: `rom-variable-table`
- address: `DF:E5DF`
- stride: `0x5`
- count: `1`
- struct: `landing_palette_anim_profile`
- confidence: `runtime-corroborated-shape`
- note: Landing palette-animation profile 19; C0:023F selects this record through DF:E4E1, decompresses DF:EC46, and copies 0 step bytes after the payload pointer.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/c0/c0_030f_advance_landing_profile_step_sequencer.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_palette_payload_pointer` | 4 | 1 | C0:023F decompresses this payload to 7E:B800 |
| `0x4` | `step_count` | 1 | 1 | C0:023F uses zero to skip loading the sequencer, otherwise bounds the step-duration copy |

### LANDING_PALETTE_ANIM_PROFILE_20

- domain: `rom-variable-table`
- address: `DF:E5E4`
- stride: `0x5`
- count: `1`
- struct: `landing_palette_anim_profile`
- confidence: `runtime-corroborated-shape`
- note: Landing palette-animation profile 20; C0:023F selects this record through DF:E4E1, decompresses DF:EC46, and copies 0 step bytes after the payload pointer.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/c0/c0_030f_advance_landing_profile_step_sequencer.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_palette_payload_pointer` | 4 | 1 | C0:023F decompresses this payload to 7E:B800 |
| `0x4` | `step_count` | 1 | 1 | C0:023F uses zero to skip loading the sequencer, otherwise bounds the step-duration copy |

### LANDING_PALETTE_ANIM_PROFILE_21

- domain: `rom-variable-table`
- address: `DF:E5E9`
- stride: `0x5`
- count: `1`
- struct: `landing_palette_anim_profile`
- confidence: `runtime-corroborated-shape`
- note: Landing palette-animation profile 21; C0:023F selects this record through DF:E4E1, decompresses DF:EC46, and copies 0 step bytes after the payload pointer.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/c0/c0_030f_advance_landing_profile_step_sequencer.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_palette_payload_pointer` | 4 | 1 | C0:023F decompresses this payload to 7E:B800 |
| `0x4` | `step_count` | 1 | 1 | C0:023F uses zero to skip loading the sequencer, otherwise bounds the step-duration copy |

### LANDING_PALETTE_ANIM_PROFILE_22

- domain: `rom-variable-table`
- address: `DF:E5EE`
- stride: `0x5`
- count: `1`
- struct: `landing_palette_anim_profile`
- confidence: `runtime-corroborated-shape`
- note: Landing palette-animation profile 22; C0:023F selects this record through DF:E4E1, decompresses DF:EC46, and copies 0 step bytes after the payload pointer.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/c0/c0_030f_advance_landing_profile_step_sequencer.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_palette_payload_pointer` | 4 | 1 | C0:023F decompresses this payload to 7E:B800 |
| `0x4` | `step_count` | 1 | 1 | C0:023F uses zero to skip loading the sequencer, otherwise bounds the step-duration copy |

### LANDING_PALETTE_ANIM_PROFILE_23

- domain: `rom-variable-table`
- address: `DF:E5F3`
- stride: `0x5`
- count: `1`
- struct: `landing_palette_anim_profile`
- confidence: `runtime-corroborated-shape`
- note: Landing palette-animation profile 23; C0:023F selects this record through DF:E4E1, decompresses DF:EC46, and copies 0 step bytes after the payload pointer.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/c0/c0_030f_advance_landing_profile_step_sequencer.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_palette_payload_pointer` | 4 | 1 | C0:023F decompresses this payload to 7E:B800 |
| `0x4` | `step_count` | 1 | 1 | C0:023F uses zero to skip loading the sequencer, otherwise bounds the step-duration copy |

### LANDING_PALETTE_ANIM_PROFILE_24

- domain: `rom-variable-table`
- address: `DF:E5F8`
- stride: `0x5`
- count: `1`
- struct: `landing_palette_anim_profile`
- confidence: `runtime-corroborated-shape`
- note: Landing palette-animation profile 24; C0:023F selects this record through DF:E4E1, decompresses DF:EC46, and copies 0 step bytes after the payload pointer.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/c0/c0_030f_advance_landing_profile_step_sequencer.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_palette_payload_pointer` | 4 | 1 | C0:023F decompresses this payload to 7E:B800 |
| `0x4` | `step_count` | 1 | 1 | C0:023F uses zero to skip loading the sequencer, otherwise bounds the step-duration copy |

### LANDING_PALETTE_ANIM_PROFILE_25

- domain: `rom-variable-table`
- address: `DF:E5FD`
- stride: `0x5`
- count: `1`
- struct: `landing_palette_anim_profile`
- confidence: `runtime-corroborated-shape`
- note: Landing palette-animation profile 25; C0:023F selects this record through DF:E4E1, decompresses DF:EC46, and copies 0 step bytes after the payload pointer.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/c0/c0_030f_advance_landing_profile_step_sequencer.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_palette_payload_pointer` | 4 | 1 | C0:023F decompresses this payload to 7E:B800 |
| `0x4` | `step_count` | 1 | 1 | C0:023F uses zero to skip loading the sequencer, otherwise bounds the step-duration copy |

### LANDING_PALETTE_ANIM_PROFILE_26

- domain: `rom-variable-table`
- address: `DF:E602`
- stride: `0x5`
- count: `1`
- struct: `landing_palette_anim_profile`
- confidence: `runtime-corroborated-shape`
- note: Landing palette-animation profile 26; C0:023F selects this record through DF:E4E1, decompresses DF:EC46, and copies 0 step bytes after the payload pointer.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/c0/c0_030f_advance_landing_profile_step_sequencer.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_palette_payload_pointer` | 4 | 1 | C0:023F decompresses this payload to 7E:B800 |
| `0x4` | `step_count` | 1 | 1 | C0:023F uses zero to skip loading the sequencer, otherwise bounds the step-duration copy |

### LANDING_PALETTE_ANIM_PROFILE_27

- domain: `rom-variable-table`
- address: `DF:E607`
- stride: `0x5`
- count: `1`
- struct: `landing_palette_anim_profile`
- confidence: `runtime-corroborated-shape`
- note: Landing palette-animation profile 27; C0:023F selects this record through DF:E4E1, decompresses DF:EC46, and copies 0 step bytes after the payload pointer.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/c0/c0_030f_advance_landing_profile_step_sequencer.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_palette_payload_pointer` | 4 | 1 | C0:023F decompresses this payload to 7E:B800 |
| `0x4` | `step_count` | 1 | 1 | C0:023F uses zero to skip loading the sequencer, otherwise bounds the step-duration copy |

### LANDING_PALETTE_ANIM_PROFILE_28

- domain: `rom-variable-table`
- address: `DF:E60C`
- stride: `0x5`
- count: `1`
- struct: `landing_palette_anim_profile`
- confidence: `runtime-corroborated-shape`
- note: Landing palette-animation profile 28; C0:023F selects this record through DF:E4E1, decompresses DF:EC46, and copies 0 step bytes after the payload pointer.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/c0/c0_030f_advance_landing_profile_step_sequencer.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_palette_payload_pointer` | 4 | 1 | C0:023F decompresses this payload to 7E:B800 |
| `0x4` | `step_count` | 1 | 1 | C0:023F uses zero to skip loading the sequencer, otherwise bounds the step-duration copy |

### LANDING_PALETTE_ANIM_PROFILE_29

- domain: `rom-variable-table`
- address: `DF:E611`
- stride: `0x5`
- count: `1`
- struct: `landing_palette_anim_profile`
- confidence: `runtime-corroborated-shape`
- note: Landing palette-animation profile 29; C0:023F selects this record through DF:E4E1, decompresses DF:EC46, and copies 0 step bytes after the payload pointer.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/c0/c0_030f_advance_landing_profile_step_sequencer.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_palette_payload_pointer` | 4 | 1 | C0:023F decompresses this payload to 7E:B800 |
| `0x4` | `step_count` | 1 | 1 | C0:023F uses zero to skip loading the sequencer, otherwise bounds the step-duration copy |

### LANDING_PALETTE_ANIM_PROFILE_30

- domain: `rom-variable-table`
- address: `DF:E616`
- stride: `0x5`
- count: `1`
- struct: `landing_palette_anim_profile`
- confidence: `runtime-corroborated-shape`
- note: Landing palette-animation profile 30; C0:023F selects this record through DF:E4E1, decompresses DF:EC46, and copies 0 step bytes after the payload pointer.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/c0/c0_030f_advance_landing_profile_step_sequencer.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_palette_payload_pointer` | 4 | 1 | C0:023F decompresses this payload to 7E:B800 |
| `0x4` | `step_count` | 1 | 1 | C0:023F uses zero to skip loading the sequencer, otherwise bounds the step-duration copy |

### LANDING_PALETTE_ANIM_PAYLOAD_0

- domain: `rom-compressed-payload`
- address: `DF:E61B`
- stride: `0x97`
- count: `1`
- struct: `landing_palette_anim_compressed_payload`
- confidence: `pointer-bounded`
- note: Compressed palette-animation payload selected by a non-empty DF landing palette-animation profile and decompressed by C0:023F.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/df/bank_df_helpers_asar.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_payload` | 1 | 151 | C4:1A9E-compatible compressed payload bytes |

### LANDING_PALETTE_ANIM_PAYLOAD_1

- domain: `rom-compressed-payload`
- address: `DF:E6B2`
- stride: `0x8B`
- count: `1`
- struct: `landing_palette_anim_compressed_payload`
- confidence: `pointer-bounded`
- note: Compressed palette-animation payload selected by a non-empty DF landing palette-animation profile and decompressed by C0:023F.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/df/bank_df_helpers_asar.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_payload` | 1 | 139 | C4:1A9E-compatible compressed payload bytes |

### LANDING_PALETTE_ANIM_PAYLOAD_2

- domain: `rom-compressed-payload`
- address: `DF:E73D`
- stride: `0x1A3`
- count: `1`
- struct: `landing_palette_anim_compressed_payload`
- confidence: `pointer-bounded`
- note: Compressed palette-animation payload selected by a non-empty DF landing palette-animation profile and decompressed by C0:023F.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/df/bank_df_helpers_asar.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_payload` | 1 | 419 | C4:1A9E-compatible compressed payload bytes |

### LANDING_PALETTE_ANIM_PAYLOAD_3

- domain: `rom-compressed-payload`
- address: `DF:E8E0`
- stride: `0x8C`
- count: `1`
- struct: `landing_palette_anim_compressed_payload`
- confidence: `pointer-bounded`
- note: Compressed palette-animation payload selected by a non-empty DF landing palette-animation profile and decompressed by C0:023F.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/df/bank_df_helpers_asar.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_payload` | 1 | 140 | C4:1A9E-compatible compressed payload bytes |

### LANDING_PALETTE_ANIM_PAYLOAD_4

- domain: `rom-compressed-payload`
- address: `DF:E96C`
- stride: `0xEA`
- count: `1`
- struct: `landing_palette_anim_compressed_payload`
- confidence: `pointer-bounded`
- note: Compressed palette-animation payload selected by a non-empty DF landing palette-animation profile and decompressed by C0:023F.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/df/bank_df_helpers_asar.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_payload` | 1 | 234 | C4:1A9E-compatible compressed payload bytes |

### LANDING_PALETTE_ANIM_PAYLOAD_5

- domain: `rom-compressed-payload`
- address: `DF:EA56`
- stride: `0xDB`
- count: `1`
- struct: `landing_palette_anim_compressed_payload`
- confidence: `pointer-bounded`
- note: Compressed palette-animation payload selected by a non-empty DF landing palette-animation profile and decompressed by C0:023F.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/df/bank_df_helpers_asar.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_payload` | 1 | 219 | C4:1A9E-compatible compressed payload bytes |

### LANDING_PALETTE_ANIM_PAYLOAD_6

- domain: `rom-compressed-payload`
- address: `DF:EB31`
- stride: `0x7B`
- count: `1`
- struct: `landing_palette_anim_compressed_payload`
- confidence: `pointer-bounded`
- note: Compressed palette-animation payload selected by a non-empty DF landing palette-animation profile and decompressed by C0:023F.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/df/bank_df_helpers_asar.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_payload` | 1 | 123 | C4:1A9E-compatible compressed payload bytes |

### LANDING_PALETTE_ANIM_PAYLOAD_7

- domain: `rom-compressed-payload`
- address: `DF:EBAC`
- stride: `0x9A`
- count: `1`
- struct: `landing_palette_anim_compressed_payload`
- confidence: `pointer-bounded`
- note: Compressed palette-animation payload selected by a non-empty DF landing palette-animation profile and decompressed by C0:023F.
- evidence: `notes/bank-df-first-pass.md`, `notes/landing-profile-cache-436e-4474.md`, `src/c0/c0_023f_build_landing_profile_step_sequencer.asm`, `src/df/bank_df_helpers_asar.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `compressed_payload` | 1 | 154 | C4:1A9E-compatible compressed payload bytes |

### TEXT_WINDOW_FLAVOR_SELECTOR_TABLE

- domain: `rom-table`
- address: `E0:1FB9`
- stride: `0x3`
- count: `5`
- struct: `text_window_flavor_selector`
- confidence: `runtime-corroborated`
- note: Five selectable text-window flavour rows; C4:7F87 and C1:9D49 use the low word as an offset from E0:1FC8.
- evidence: `notes/text-window-skin-bundle-contracts.md`, `notes/ui-font-town-map-asset-contracts.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `palette_block_offset` | 2 | 1 | offset from E0:1FC8 selected by C4:7F87/C1:9D49 for the current text-window flavour |
| `0x2` | `selector_aux_byte` | 1 | 1 | third selector byte preserved by the checked E0 window-skin contract |

### TEXT_WINDOW_PALETTE_BLOCKS

- domain: `rom-table`
- address: `E0:1FC8`
- stride: `0x40`
- count: `7`
- struct: `text_window_palette_block`
- confidence: `runtime-corroborated`
- note: Seven 0x40-byte text-window palette blocks; blocks 0..4 are selectable, block 5 is the lead-entity override, and block 6 is preserved as nonselectable/extra.
- evidence: `notes/text-window-skin-bundle-contracts.md`, `notes/ui-font-town-map-asset-contracts.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `palette_row_0` | 2 | 4 | four SNES BGR555 colours copied as part of a 0x40-byte text-window palette block |
| `0x8` | `palette_row_1` | 2 | 4 | four SNES BGR555 colours copied as part of a 0x40-byte text-window palette block |
| `0x10` | `palette_row_2` | 2 | 4 | four SNES BGR555 colours copied as part of a 0x40-byte text-window palette block |
| `0x18` | `palette_row_3` | 2 | 4 | four SNES BGR555 colours copied as part of a 0x40-byte text-window palette block |
| `0x20` | `palette_row_4` | 2 | 4 | four SNES BGR555 colours copied as part of a 0x40-byte text-window palette block |
| `0x28` | `palette_row_5` | 2 | 4 | four SNES BGR555 colours copied as part of a 0x40-byte text-window palette block |
| `0x30` | `palette_row_6` | 2 | 4 | four SNES BGR555 colours copied as part of a 0x40-byte text-window palette block |
| `0x38` | `palette_row_7` | 2 | 4 | four SNES BGR555 colours copied as part of a 0x40-byte text-window palette block |

### MOVEMENT_TEXT_STRING_PALETTE

- domain: `rom-table`
- address: `E0:2188`
- stride: `0x8`
- count: `1`
- struct: `four_colour_palette_row`
- confidence: `structural-corroborated`
- note: Standalone four-colour movement-text palette row between the text-window palette blocks and the town-map pointer tail.
- evidence: `notes/text-window-skin-bundle-contracts.md`, `notes/bank-e0-asset-data-map.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `colour_0` | 2 | 1 |  |
| `0x2` | `colour_1` | 2 | 1 |  |
| `0x4` | `colour_2` | 2 | 1 |  |
| `0x6` | `colour_3` | 2 | 1 |  |

### TOWN_MAP_GFX_POINTER_TABLE

- domain: `rom-table`
- address: `E0:2190`
- stride: `0x4`
- count: `6`
- struct: `far_pointer`
- confidence: `runtime-corroborated`
- note: Six long pointers consumed by C4:D553 to decompress the selected E0 town-map graphics payload.
- evidence: `notes/text-window-skin-bundle-contracts.md`, `notes/ui-font-town-map-asset-contracts.md`, `notes/town-map-selection-rendering-c4d274-c4d744.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `pointer` | 4 | 1 |  |

### TITLE_SCREEN_LETTER_OAM_RECORDS

- domain: `rom-table`
- address: `E1:CE08`
- stride: `0x2D`
- count: `9`
- struct: `title_screen_letter_oam_record`
- confidence: `verified`
- note: Nine animated letter OAM record rows for EARTHOUND; each row contains nine 5-byte OAM-ish entries.
- evidence: `notes/title-screen-letter-oam-contracts.md`, `notes/intro-title-visual-bundle-contracts.md`, `notes/ui-font-town-map-asset-contracts.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `oam_entries` | 5 | 9 | nine OAM-ish entries: y, tile, attrs, x, control; terminal entries have bit 7 set in control |

### TITLE_SCREEN_LETTER_OAM_POINTER_TABLE

- domain: `rom-table`
- address: `E1:CF9D`
- stride: `0x2`
- count: `9`
- struct: `word_pointer`
- confidence: `verified`
- note: Nine local pointers whose targets match the E1:CE08 title-screen letter OAM record starts.
- evidence: `notes/title-screen-letter-oam-contracts.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `pointer` | 2 | 1 |  |

### PHOTOGRAPHER_CONFIG_TABLE

- domain: `rom-table`
- address: `E1:2F8A`
- stride: `0x3E`
- count: `32`
- struct: `photographer_config_record`
- confidence: `consumer-corroborated-partial`
- note: Thirty-two photographer/photo-scene configuration records; named fields are limited to offsets read by C4 photo, credits, and current-slot consumers.
- evidence: `notes/bank-e1-asset-data-map.md`, `notes/current-slot-position-staging-c46b8d-c46d4b.md`, `src/c4/credits_photo_flag_counter.asm`, `src/c4/credits_photograph_render_helpers.asm`, `src/c4/credits_photograph_slide_helpers.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `event_flag_gate` | 2 | 1 | credits/photo helpers test this event flag before counting or rendering a photo scene |
| `0x2` | `map_load_x_tile` | 2 | 1 | C4:F264 shifts this word left three before calling C0:13F6 LoadMapAtPosition |
| `0x4` | `map_load_y_tile` | 2 | 1 | C4:F264 shifts this word left three before calling C0:13F6 LoadMapAtPosition |
| `0x8` | `slide_angle` | 1 | 1 | C4:F46F projects the credits photograph slide vector from this angle byte |
| `0x9` | `slide_duration` | 1 | 1 | C4:F46F scales this byte into the slide frame count |
| `0xA` | `photo_scene_x_tile` | 2 | 1 | C4:6D4B shifts this word left three and writes the current slot live X |
| `0xC` | `photo_scene_y_tile` | 2 | 1 | C4:6D4B shifts this word left three and writes the current slot live Y |
| `0xE` | `attached_visual_0_x_tile` | 2 | 1 | C4:F264 shifts this attached visual X tile coordinate left three before spawning |
| `0x10` | `attached_visual_0_y_tile` | 2 | 1 | C4:F264 shifts this attached visual Y tile coordinate left three before spawning |
| `0x12` | `attached_visual_1_x_tile` | 2 | 1 | C4:F264 shifts this attached visual X tile coordinate left three before spawning |
| `0x14` | `attached_visual_1_y_tile` | 2 | 1 | C4:F264 shifts this attached visual Y tile coordinate left three before spawning |
| `0x16` | `attached_visual_2_x_tile` | 2 | 1 | C4:F264 shifts this attached visual X tile coordinate left three before spawning |
| `0x18` | `attached_visual_2_y_tile` | 2 | 1 | C4:F264 shifts this attached visual Y tile coordinate left three before spawning |
| `0x1A` | `attached_visual_3_x_tile` | 2 | 1 | C4:F264 shifts this attached visual X tile coordinate left three before spawning |
| `0x1C` | `attached_visual_3_y_tile` | 2 | 1 | C4:F264 shifts this attached visual Y tile coordinate left three before spawning |
| `0x1E` | `attached_visual_4_x_tile` | 2 | 1 | C4:F264 shifts this attached visual X tile coordinate left three before spawning |
| `0x20` | `attached_visual_4_y_tile` | 2 | 1 | C4:F264 shifts this attached visual Y tile coordinate left three before spawning |
| `0x22` | `attached_visual_5_x_tile` | 2 | 1 | C4:F264 shifts this attached visual X tile coordinate left three before spawning |
| `0x24` | `attached_visual_5_y_tile` | 2 | 1 | C4:F264 shifts this attached visual Y tile coordinate left three before spawning |
| `0x26` | `photo_entity_0_x_tile` | 2 | 1 | C4:F264 shifts this live photo-entity X tile coordinate left three before spawning |
| `0x28` | `photo_entity_0_y_tile` | 2 | 1 | C4:F264 shifts this live photo-entity Y tile coordinate left three before spawning |
| `0x2A` | `photo_entity_0_descriptor` | 2 | 1 | C4:F264 skips this live photo-entity slot when the descriptor word is zero |
| `0x2C` | `photo_entity_1_x_tile` | 2 | 1 | C4:F264 shifts this live photo-entity X tile coordinate left three before spawning |
| `0x2E` | `photo_entity_1_y_tile` | 2 | 1 | C4:F264 shifts this live photo-entity Y tile coordinate left three before spawning |
| `0x30` | `photo_entity_1_descriptor` | 2 | 1 | C4:F264 skips this live photo-entity slot when the descriptor word is zero |
| `0x32` | `photo_entity_2_x_tile` | 2 | 1 | C4:F264 shifts this live photo-entity X tile coordinate left three before spawning |
| `0x34` | `photo_entity_2_y_tile` | 2 | 1 | C4:F264 shifts this live photo-entity Y tile coordinate left three before spawning |
| `0x36` | `photo_entity_2_descriptor` | 2 | 1 | C4:F264 skips this live photo-entity slot when the descriptor word is zero |
| `0x38` | `photo_entity_3_x_tile` | 2 | 1 | C4:F264 shifts this live photo-entity X tile coordinate left three before spawning |
| `0x3A` | `photo_entity_3_y_tile` | 2 | 1 | C4:F264 shifts this live photo-entity Y tile coordinate left three before spawning |
| `0x3C` | `photo_entity_3_descriptor` | 2 | 1 | C4:F264 skips this live photo-entity slot when the descriptor word is zero |

### TOWN_MAP_ICON_GRAPHIC_DESCRIPTOR_RECORDS

- domain: `rom-table`
- address: `E1:F203`
- stride: `0x5`
- count: `117`
- struct: `town_map_icon_graphic_descriptor`
- confidence: `runtime-corroborated-shape`
- note: Five-byte town-map icon graphic descriptors split by the E1:F44C icon pointer table and consumed by C0:8C54/C0:8CD5.
- evidence: `notes/ui-font-town-map-asset-contracts.md`, `notes/town-map-selection-rendering-c4d274-c4d744.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `relative_y_offset` | 1 | 1 | signed Y offset consumed by C0:8C54/C0:8CD5 |
| `0x1` | `tile_attribute_word` | 2 | 1 | tile/attribute word staged by the town-map icon renderer |
| `0x3` | `relative_x_offset` | 1 | 1 | signed X offset consumed by C0:8C54/C0:8CD5 |
| `0x4` | `control_flags` | 1 | 1 | bit 7 terminates the descriptor list; bit 0 feeds C0:8CD5's packed renderer mask/attribute bit |

### TOWN_MAP_ICON_GRAPHIC_POINTER_TABLE

- domain: `rom-table`
- address: `E1:F44C`
- stride: `0x2`
- count: `23`
- struct: `word_pointer`
- confidence: `runtime-corroborated`
- note: Twenty-three local pointers mapping town-map icon ids to E1:F203 five-byte graphic descriptor lists.
- evidence: `notes/ui-font-town-map-asset-contracts.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `pointer` | 2 | 1 |  |

### TOWN_MAP_BLINK_SUPPRESS_TABLE

- domain: `rom-table`
- address: `E1:F47A`
- stride: `0x1`
- count: `23`
- struct: `town_map_blink_suppress_flag`
- confidence: `runtime-corroborated`
- note: Town-map icon blink/suppression flags checked before static icon drawing.
- evidence: `notes/ui-font-town-map-asset-contracts.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `value` | 1 | 1 |  |

### TOWN_MAP_ICON_PLACEMENT_POINTER_TABLE

- domain: `rom-table`
- address: `E1:F491`
- stride: `0x4`
- count: `6`
- struct: `far_pointer`
- confidence: `runtime-corroborated`
- note: Six long pointers from selected town-map id to variable icon placement lists in E1:F4A9..E1:F581.
- evidence: `notes/ui-font-town-map-asset-contracts.md`, `notes/town-map-selection-rendering-c4d274-c4d744.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `pointer` | 4 | 1 |  |

### TOWN_MAP_ICON_PLACEMENT_LIST_0

- domain: `rom-variable-table`
- address: `E1:F4A9`
- stride: `0x5`
- count: `7`
- struct: `town_map_icon_placement_record`
- confidence: `runtime-corroborated-shape`
- note: Town-map icon placement list 0; C4:D43F walks five-byte records until the FF terminator at E1:F4CC.
- evidence: `notes/ui-font-town-map-asset-contracts.md`, `notes/town-map-selection-rendering-c4d274-c4d744.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `x` | 1 | 1 | base X coordinate passed to C0:8C54 by C4:D43F |
| `0x1` | `y` | 1 | 1 | base Y coordinate passed to C0:8C54 by C4:D43F |
| `0x2` | `icon_id` | 1 | 1 | town-map icon id remapped through the E1:F44C graphic pointer table |
| `0x3` | `event_flag_with_draw_polarity` | 2 | 1 | event flag word; high bit means draw when set, clear high bit means draw when clear |

### TOWN_MAP_ICON_PLACEMENT_LIST_1

- domain: `rom-variable-table`
- address: `E1:F4CD`
- stride: `0x5`
- count: `8`
- struct: `town_map_icon_placement_record`
- confidence: `runtime-corroborated-shape`
- note: Town-map icon placement list 1; C4:D43F walks five-byte records until the FF terminator at E1:F4F5.
- evidence: `notes/ui-font-town-map-asset-contracts.md`, `notes/town-map-selection-rendering-c4d274-c4d744.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `x` | 1 | 1 | base X coordinate passed to C0:8C54 by C4:D43F |
| `0x1` | `y` | 1 | 1 | base Y coordinate passed to C0:8C54 by C4:D43F |
| `0x2` | `icon_id` | 1 | 1 | town-map icon id remapped through the E1:F44C graphic pointer table |
| `0x3` | `event_flag_with_draw_polarity` | 2 | 1 | event flag word; high bit means draw when set, clear high bit means draw when clear |

### TOWN_MAP_ICON_PLACEMENT_LIST_2

- domain: `rom-variable-table`
- address: `E1:F4F6`
- stride: `0x5`
- count: `9`
- struct: `town_map_icon_placement_record`
- confidence: `runtime-corroborated-shape`
- note: Town-map icon placement list 2; C4:D43F walks five-byte records until the FF terminator at E1:F523.
- evidence: `notes/ui-font-town-map-asset-contracts.md`, `notes/town-map-selection-rendering-c4d274-c4d744.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `x` | 1 | 1 | base X coordinate passed to C0:8C54 by C4:D43F |
| `0x1` | `y` | 1 | 1 | base Y coordinate passed to C0:8C54 by C4:D43F |
| `0x2` | `icon_id` | 1 | 1 | town-map icon id remapped through the E1:F44C graphic pointer table |
| `0x3` | `event_flag_with_draw_polarity` | 2 | 1 | event flag word; high bit means draw when set, clear high bit means draw when clear |

### TOWN_MAP_ICON_PLACEMENT_LIST_3

- domain: `rom-variable-table`
- address: `E1:F524`
- stride: `0x5`
- count: `7`
- struct: `town_map_icon_placement_record`
- confidence: `runtime-corroborated-shape`
- note: Town-map icon placement list 3; C4:D43F walks five-byte records until the FF terminator at E1:F547.
- evidence: `notes/ui-font-town-map-asset-contracts.md`, `notes/town-map-selection-rendering-c4d274-c4d744.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `x` | 1 | 1 | base X coordinate passed to C0:8C54 by C4:D43F |
| `0x1` | `y` | 1 | 1 | base Y coordinate passed to C0:8C54 by C4:D43F |
| `0x2` | `icon_id` | 1 | 1 | town-map icon id remapped through the E1:F44C graphic pointer table |
| `0x3` | `event_flag_with_draw_polarity` | 2 | 1 | event flag word; high bit means draw when set, clear high bit means draw when clear |

### TOWN_MAP_ICON_PLACEMENT_LIST_4

- domain: `rom-variable-table`
- address: `E1:F548`
- stride: `0x5`
- count: `5`
- struct: `town_map_icon_placement_record`
- confidence: `runtime-corroborated-shape`
- note: Town-map icon placement list 4; C4:D43F walks five-byte records until the FF terminator at E1:F561.
- evidence: `notes/ui-font-town-map-asset-contracts.md`, `notes/town-map-selection-rendering-c4d274-c4d744.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `x` | 1 | 1 | base X coordinate passed to C0:8C54 by C4:D43F |
| `0x1` | `y` | 1 | 1 | base Y coordinate passed to C0:8C54 by C4:D43F |
| `0x2` | `icon_id` | 1 | 1 | town-map icon id remapped through the E1:F44C graphic pointer table |
| `0x3` | `event_flag_with_draw_polarity` | 2 | 1 | event flag word; high bit means draw when set, clear high bit means draw when clear |

### TOWN_MAP_ICON_PLACEMENT_LIST_5

- domain: `rom-variable-table`
- address: `E1:F562`
- stride: `0x5`
- count: `6`
- struct: `town_map_icon_placement_record`
- confidence: `runtime-corroborated-shape`
- note: Town-map icon placement list 5; C4:D43F walks five-byte records until the FF terminator at E1:F580.
- evidence: `notes/ui-font-town-map-asset-contracts.md`, `notes/town-map-selection-rendering-c4d274-c4d744.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `x` | 1 | 1 | base X coordinate passed to C0:8C54 by C4:D43F |
| `0x1` | `y` | 1 | 1 | base Y coordinate passed to C0:8C54 by C4:D43F |
| `0x2` | `icon_id` | 1 | 1 | town-map icon id remapped through the E1:F44C graphic pointer table |
| `0x3` | `event_flag_with_draw_polarity` | 2 | 1 | event flag word; high bit means draw when set, clear high bit means draw when clear |

### OVERWORLD_EVENT_MUSIC_POINTER_TABLE

- domain: `rom-table`
- address: `CF:58EF`
- stride: `0x2`
- count: `165`
- struct: `word_pointer`
- confidence: `consumer-corroborated`
- note: Selector-indexed low-word pointers into the CF current-position event-music context chains; selector 0 is null and selectors 1..164 target CF:5A39..CF:61DC.
- evidence: `refs/eb-decompile-4ef92/map_music.yml`, `notes/cf-table-splits.md`, `notes/cf-event-music-context-contracts.md`, `src/c0/c0_65c2_probe_type6_door_candidate.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `pointer` | 2 | 1 |  |

### OVERWORLD_EVENT_MUSIC_TABLE

- domain: `rom-variable-table`
- address: `CF:5A39`
- stride: `0x7A4`
- count: `1`
- struct: `overworld_event_music_rows`
- confidence: `consumer-corroborated`
- note: Variable-length current-position event-music context chains ending at the inline bank0f byte block; each four-byte row is an event-condition/default row plus music-track and screen-transition-SFX bytes.
- evidence: `refs/eb-decompile-4ef92/map_music.yml`, `notes/cf-table-splits.md`, `notes/cf-event-music-context-contracts.md`, `notes/c0-current-position-music-refresh-c068f4-c069af.md`, `src/c0/c0_65c2_probe_type6_door_candidate.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `raw_event_music_context_rows` | 1 | 1956 | 164 CF selector-addressed variable chains; see notes/cf-event-music-context-contracts.json for decoded event-flag condition/default rows and music/SFX bytes |

### CF_INLINE_EVENT_MUSIC_TRAILER

- domain: `rom-block`
- address: `CF:61DD`
- stride: `0xA`
- count: `1`
- struct: `inline_event_music_trailer`
- confidence: `exact`
- note: Inline ten-byte bank0f block between event music and sprite placement pointers.
- evidence: `refs/ebsrc-main/ebsrc-main/src/bankconfig/common/bank0f.asm`, `notes/cf-table-splits.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `byte` | 1 | 10 | inline bank0f byte block |

### SPRITE_PLACEMENT_POINTER_TABLE

- domain: `rom-table`
- address: `CF:61E7`
- stride: `0x2`
- count: `1280`
- struct: `sprite_placement_sector_pointer`
- confidence: `exact`
- note: 40x32 sector pointer grid into the CF sprite placement table; zero means empty.
- evidence: `refs/eb-decompile-4ef92/map_sprites.yml`, `notes/cf-table-splits.md`, `notes/cf-sector-list-contracts.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `sprite_placement_list_offset` | 2 | 1 | zero means empty sector; nonzero is a CPU low word into CF:6BE7..CF:8984 |

### SPRITE_PLACEMENT_TABLE

- domain: `rom-variable-table`
- address: `CF:6BE7`
- stride: `0x1D9E`
- count: `1`
- struct: `sprite_placement_sector_list_block`
- confidence: `exact-variable-lists`
- note: 627 counted sprite-placement sector lists with complete decoded rows in notes/cf-sector-list-contracts.json; each four-byte row is npc_config_id plus sector-local Y/X placement bytes.
- evidence: `refs/ebsrc-main/ebsrc-main/include/structs.asm`, `refs/eb-decompile-4ef92/map_sprites.yml`, `notes/cf-table-splits.md`, `notes/cf-sector-list-contracts.md`, `notes/coilsnake-field-join-report.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `counted_sprite_placement_sector_lists` | 1 | 7582 | 627 counted sprite-placement sector lists; see notes/cf-sector-list-contracts.json for complete decoded lists and npc_config_id/sector_local_y/sector_local_x entries |

### NPC_CONFIG_TABLE

- domain: `rom-table`
- address: `CF:8985`
- stride: `0x11`
- count: `1584`
- struct: `npc_config`
- confidence: `corroborated`
- note: Fixed-size NPC configuration rows ending exactly at CF's audio tail.
- evidence: `refs/ebsrc-main/ebsrc-main/include/structs.asm`, `refs/eb-decompile-4ef92/npc_config_table.yml`, `notes/cf-table-splits.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `type` | 1 | 1 |  |
| `0x1` | `sprite` | 2 | 1 |  |
| `0x3` | `direction` | 1 | 1 |  |
| `0x4` | `event_script` | 2 | 1 |  |
| `0x6` | `event_flag` | 2 | 1 |  |
| `0x8` | `appearance_style` | 1 | 1 |  |
| `0x9` | `text_pointer` | 4 | 1 |  |
| `0xD` | `secondary_payload` | 4 | 1 | union: item byte or second text pointer depending on NPC type |

### BATTLE_SELECTION_SNAPSHOT

- domain: `wram-overlay`
- address: `7E:9FFA`
- stride: `0x4E`
- count: `1`
- struct: `battle_menu_selection_header_plus_snapshot`
- confidence: `corroborated-overlay`
- note: Formal battle_menu_selection header at the front of a larger C2:B930 selected-slot snapshot overlay. This base overlaps BATTLERS_TABLE[1] in local address terms, so consumers should treat it as an overlay/scratch contract rather than an independent root.
- evidence: `refs/ebsrc-main/ebsrc-main/include/structs.asm`, `notes/battle-selection-snapshot-export-c2b930.md`, `notes/battle-targetting-resolver-c1adb4-af50.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `user` | 1 | 1 |  |
| `0x1` | `param1` | 1 | 1 |  |
| `0x2` | `selected_action` | 2 | 1 |  |
| `0x4` | `targetting` | 1 | 1 |  |
| `0x5` | `selected_target` | 1 | 1 |  |
| `0xC` | `snapshot_active` | 1 | 1 | C2:B930 sets this byte to 1 when exporting a live slot snapshot |
| `0xE` | `snapshot_ally_or_enemy` | 1 | 1 | snapshot byte cleared by C2:B930; same offset family as battler::ally_or_enemy |
| `0xF` | `snapshot_npc_id` | 1 | 1 | snapshot byte cleared by C2:B930; same offset family as battler::npc_id |
| `0x10` | `selected_user_zero_based` | 1 | 1 | zero-based selected user or battler id |
| `0x11` | `current_hp` | 2 | 1 | copied from selected char_struct current_hp |
| `0x13` | `current_hp_target` | 2 | 1 | copied from selected char_struct current_hp_target |
| `0x15` | `max_hp` | 2 | 1 | copied from selected char_struct max_hp |
| `0x17` | `current_pp` | 2 | 1 | copied from selected char_struct current_pp |
| `0x19` | `current_pp_target` | 2 | 1 | copied from selected char_struct current_pp_target |
| `0x1B` | `max_pp` | 2 | 1 | copied from selected char_struct max_pp |
| `0x1D` | `afflictions` | 1 | 7 | copied from selected char_struct affliction/status bytes |
| `0x37` | `resistance_summary` | 1 | 6 | derived from selected char_struct late resistance fields |

### LOADED_BG_DATA_LAYER1

- domain: `wram-root`
- address: `7E:ADD4`
- stride: `0x77`
- count: `1`
- struct: `loaded_bg_data`
- confidence: `corroborated`
- note: Layer 1 runtime state for battle background palette, scroll, and distortion effects.
- evidence: `refs/ebsrc-main/ebsrc-main/include/structs.asm`, `refs/ebsrc-main/ebsrc-main/src/bankconfig/common/ram.asm`, `notes/c2-battlebg-load-and-palette-effect-corridor-c2cfe5-c2e0e7.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `target_layer` | 1 | 1 |  |
| `0x1` | `bitdepth` | 1 | 1 |  |
| `0x2` | `freeze_palette_scrolling` | 1 | 1 |  |
| `0x3` | `palette_shifting_style` | 1 | 1 |  |
| `0x4` | `palette_cycle_1_first` | 1 | 1 |  |
| `0x5` | `palette_cycle_1_last` | 1 | 1 |  |
| `0x6` | `palette_cycle_2_first` | 1 | 1 |  |
| `0x7` | `palette_cycle_2_last` | 1 | 1 |  |
| `0x8` | `palette_cycle_1_step` | 1 | 1 |  |
| `0x9` | `palette_cycle_2_step` | 1 | 1 |  |
| `0xA` | `palette_change_speed` | 1 | 1 |  |
| `0xB` | `palette_change_duration_left` | 1 | 1 |  |
| `0xC` | `palette` | 2 | 16 | current RGB555 palette words |
| `0x2C` | `palette2` | 2 | 16 | backup/original RGB555 palette words |
| `0x4C` | `palette_pointer` | 2 | 1 | displayed palette destination pointer |
| `0x4E` | `scrolling_movements` | 1 | 4 |  |
| `0x52` | `current_scrolling_movement` | 1 | 1 |  |
| `0x53` | `scrolling_duration_left` | 2 | 1 |  |
| `0x55` | `horizontal_position` | 2 | 1 |  |
| `0x57` | `vertical_position` | 2 | 1 |  |
| `0x59` | `horizontal_velocity` | 2 | 1 |  |
| `0x5B` | `vertical_velocity` | 2 | 1 |  |
| `0x5D` | `horizontal_acceleration` | 2 | 1 |  |
| `0x5F` | `vertical_acceleration` | 2 | 1 |  |
| `0x61` | `distortion_styles` | 1 | 4 |  |
| `0x65` | `current_distortion_style_index` | 1 | 1 |  |
| `0x66` | `distortion_duration_left` | 2 | 1 |  |
| `0x68` | `distortion_type` | 1 | 1 |  |
| `0x69` | `distortion_ripple_frequency` | 2 | 1 |  |
| `0x6B` | `distortion_ripple_amplitude` | 2 | 1 |  |
| `0x6D` | `distortion_speed` | 1 | 1 |  |
| `0x6E` | `distortion_compression_rate` | 2 | 1 |  |
| `0x70` | `distortion_ripple_frequency_acceleration` | 2 | 1 |  |
| `0x72` | `distortion_ripple_amplitude_acceleration` | 2 | 1 |  |
| `0x74` | `distortion_speed_acceleration` | 1 | 1 |  |
| `0x75` | `distortion_compression_acceleration` | 2 | 1 |  |

### LOADED_BG_DATA_LAYER2

- domain: `wram-root`
- address: `7E:AE4B`
- stride: `0x77`
- count: `1`
- struct: `loaded_bg_data`
- confidence: `corroborated`
- note: Layer 2 runtime state for battle background palette, scroll, and distortion effects.
- evidence: `refs/ebsrc-main/ebsrc-main/include/structs.asm`, `refs/ebsrc-main/ebsrc-main/src/bankconfig/common/ram.asm`, `notes/c2-battlebg-load-and-palette-effect-corridor-c2cfe5-c2e0e7.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `target_layer` | 1 | 1 |  |
| `0x1` | `bitdepth` | 1 | 1 |  |
| `0x2` | `freeze_palette_scrolling` | 1 | 1 |  |
| `0x3` | `palette_shifting_style` | 1 | 1 |  |
| `0x4` | `palette_cycle_1_first` | 1 | 1 |  |
| `0x5` | `palette_cycle_1_last` | 1 | 1 |  |
| `0x6` | `palette_cycle_2_first` | 1 | 1 |  |
| `0x7` | `palette_cycle_2_last` | 1 | 1 |  |
| `0x8` | `palette_cycle_1_step` | 1 | 1 |  |
| `0x9` | `palette_cycle_2_step` | 1 | 1 |  |
| `0xA` | `palette_change_speed` | 1 | 1 |  |
| `0xB` | `palette_change_duration_left` | 1 | 1 |  |
| `0xC` | `palette` | 2 | 16 | current RGB555 palette words |
| `0x2C` | `palette2` | 2 | 16 | backup/original RGB555 palette words |
| `0x4C` | `palette_pointer` | 2 | 1 | displayed palette destination pointer |
| `0x4E` | `scrolling_movements` | 1 | 4 |  |
| `0x52` | `current_scrolling_movement` | 1 | 1 |  |
| `0x53` | `scrolling_duration_left` | 2 | 1 |  |
| `0x55` | `horizontal_position` | 2 | 1 |  |
| `0x57` | `vertical_position` | 2 | 1 |  |
| `0x59` | `horizontal_velocity` | 2 | 1 |  |
| `0x5B` | `vertical_velocity` | 2 | 1 |  |
| `0x5D` | `horizontal_acceleration` | 2 | 1 |  |
| `0x5F` | `vertical_acceleration` | 2 | 1 |  |
| `0x61` | `distortion_styles` | 1 | 4 |  |
| `0x65` | `current_distortion_style_index` | 1 | 1 |  |
| `0x66` | `distortion_duration_left` | 2 | 1 |  |
| `0x68` | `distortion_type` | 1 | 1 |  |
| `0x69` | `distortion_ripple_frequency` | 2 | 1 |  |
| `0x6B` | `distortion_ripple_amplitude` | 2 | 1 |  |
| `0x6D` | `distortion_speed` | 1 | 1 |  |
| `0x6E` | `distortion_compression_rate` | 2 | 1 |  |
| `0x70` | `distortion_ripple_frequency_acceleration` | 2 | 1 |  |
| `0x72` | `distortion_ripple_amplitude_acceleration` | 2 | 1 |  |
| `0x74` | `distortion_speed_acceleration` | 1 | 1 |  |
| `0x75` | `distortion_compression_acceleration` | 2 | 1 |  |

### PATHFINDING_TILE_CONTEXT_GATE_TABLE

- domain: `rom-table`
- address: `C3:DFE8`
- stride: `0x1`
- count: `8`
- struct: `pathfinding_tile_context_gate`
- confidence: `corroborated`
- note: Low-byte tile-context gate table consumed by C0:C0B4 and C0:C19B after C0:0AA1; zero aborts the path lane copy before pathfinding.
- evidence: `notes/pathfinding-consumers-direction-helpers-c0bd96-c0c7db.md`, `notes/c3-late-interaction-table-contracts.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `gate_enabled` | 1 | 1 | nonzero allows the C0:C0B4/C0:C19B path consumer to continue after C0:0AA1 |

### INPUT_DIRECTION_PERMISSION_MASK_TABLE

- domain: `rom-table`
- address: `C3:E12C`
- stride: `0x2`
- count: `14`
- struct: `input_direction_permission_mask`
- confidence: `corroborated`
- note: Direction permission mask table consumed by C0:404F MapInputToDirection.
- evidence: `notes/input-direction-and-interaction-probes-c0402b-c04116.md`, `refs/earthbound-disasm-legacy/Earthbound Decomp/EB/Routine_Macros_EB.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `permission_mask` | 2 | 1 | bitmask consumed by C0:404F MapInputToDirection |

### INTERACTION_PROBE_DIRECTION_X_OFFSETS

- domain: `rom-table`
- address: `C3:E148`
- stride: `0x2`
- count: `8`
- struct: `signed_direction_offset_word`
- confidence: `corroborated`
- note: Signed X probe offsets used by C0:4116 for one facing-direction interaction probe.
- evidence: `notes/input-direction-and-interaction-probes-c0402b-c04116.md`, `notes/front-interaction-flow.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `offset_pixels` | 2 | 1 | signed probe offset in pixels for one direction index |

### INTERACTION_PROBE_DIRECTION_Y_OFFSETS

- domain: `rom-table`
- address: `C3:E158`
- stride: `0x2`
- count: `8`
- struct: `signed_direction_offset_word`
- confidence: `corroborated`
- note: Signed Y probe offsets used by C0:4116 for one facing-direction interaction probe.
- evidence: `notes/input-direction-and-interaction-probes-c0402b-c04116.md`, `notes/front-interaction-flow.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `offset_pixels` | 2 | 1 | signed probe offset in pixels for one direction index |

### INTERACTION_RESULT_FACING_REMAP_TABLE

- domain: `rom-table`
- address: `C3:E168`
- stride: `0x2`
- count: `8`
- struct: `interaction_result_facing_remap`
- confidence: `corroborated`
- note: Facing/result-state remap consumed by C0:42C2; the selected word is stored to $2AF6[target] for class-1 interaction results.
- evidence: `notes/interaction-result-classes.md`, `notes/interaction-result-consumers.md`, `notes/c3-late-interaction-table-contracts.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `target_facing_state` | 2 | 1 | stored into $2AF6[target] by C0:42C2 |

### MAP_ENTITY_PLACEMENT_DIRECTION_PARAM_TABLE

- domain: `rom-table`
- address: `C3:E1D8`
- stride: `0x2`
- count: `4`
- struct: `map_entity_placement_direction_param`
- confidence: `proposed`
- note: First word page consumed by the C0 entity placement path around C0:6D27/C0:6D91.
- evidence: `notes/c3-map-movement-parameter-table-e1d8-e240.md`, `notes/staged-movement-wrapper-70cb.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `value` | 2 | 1 |  |

### MAP_ENTITY_PLACEMENT_DIRECTION_PARAM_TABLE_PAGE1

- domain: `rom-table`
- address: `C3:E1E0`
- stride: `0x2`
- count: `16`
- struct: `map_entity_placement_direction_param`
- confidence: `proposed`
- note: Second word page in the C0 entity placement direction parameter family.
- evidence: `notes/c3-map-movement-parameter-table-e1d8-e240.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `value` | 2 | 1 |  |

### STAGED_MOVEMENT_PRIMARY_DIRECTION_PARAM_TABLE

- domain: `rom-table`
- address: `C3:E200`
- stride: `0x2`
- count: `4`
- struct: `staged_movement_direction_param`
- confidence: `corroborated`
- note: Primary direction parameter words consumed by staged movement setup.
- evidence: `notes/c3-map-movement-parameter-table-e1d8-e240.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `value` | 2 | 1 |  |

### STAGED_MOVEMENT_ALTERNATE_DIRECTION_PARAM_TABLE

- domain: `rom-table`
- address: `C3:E208`
- stride: `0x2`
- count: `4`
- struct: `staged_movement_direction_param`
- confidence: `corroborated`
- note: Alternate direction parameter words consumed by staged movement setup.
- evidence: `notes/c3-map-movement-parameter-table-e1d8-e240.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `value` | 2 | 1 |  |

### STAGED_MOVEMENT_SUBTILE_OFFSET_SET_A_X

- domain: `rom-table`
- address: `C3:E210`
- stride: `0x2`
- count: `4`
- struct: `signed_subtile_offset_word`
- confidence: `corroborated`
- note: X offsets for staged movement subtile offset set A.
- evidence: `notes/c3-map-movement-parameter-table-e1d8-e240.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `value` | 2 | 1 |  |

### STAGED_MOVEMENT_SUBTILE_OFFSET_SET_A_Y

- domain: `rom-table`
- address: `C3:E218`
- stride: `0x2`
- count: `4`
- struct: `signed_subtile_offset_word`
- confidence: `corroborated`
- note: Y offsets for staged movement subtile offset set A.
- evidence: `notes/c3-map-movement-parameter-table-e1d8-e240.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `value` | 2 | 1 |  |

### STAGED_MOVEMENT_SUBTILE_OFFSET_SET_B_X

- domain: `rom-table`
- address: `C3:E220`
- stride: `0x2`
- count: `4`
- struct: `signed_subtile_offset_word`
- confidence: `corroborated`
- note: X offsets for staged movement subtile offset set B.
- evidence: `notes/c3-map-movement-parameter-table-e1d8-e240.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `value` | 2 | 1 |  |

### STAGED_MOVEMENT_SUBTILE_OFFSET_SET_B_Y

- domain: `rom-table`
- address: `C3:E228`
- stride: `0x2`
- count: `4`
- struct: `signed_subtile_offset_word`
- confidence: `corroborated`
- note: Y offsets for staged movement subtile offset set B.
- evidence: `notes/c3-map-movement-parameter-table-e1d8-e240.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `value` | 2 | 1 |  |

### DOOR_CANDIDATE_DIRECTION_OFFSET_X

- domain: `rom-table`
- address: `C3:E230`
- stride: `0x2`
- count: `8`
- struct: `door_candidate_direction_offset_word`
- confidence: `corroborated`
- note: X coarse-cell direction offsets consumed by C4:334A while probing cached door fallback candidates.
- evidence: `notes/c3-map-movement-parameter-table-e1d8-e240.md`, `notes/c3-late-interaction-table-contracts.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `cell_delta` | 2 | 1 | signed coarse-cell offset added by C4:334A |

### DOOR_CANDIDATE_DIRECTION_OFFSET_Y

- domain: `rom-table`
- address: `C3:E240`
- stride: `0x2`
- count: `8`
- struct: `door_candidate_direction_offset_word`
- confidence: `corroborated`
- note: Y coarse-cell direction offsets consumed by C4:334A while probing cached door fallback candidates.
- evidence: `notes/c3-map-movement-parameter-table-e1d8-e240.md`, `notes/c3-late-interaction-table-contracts.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `cell_delta` | 2 | 1 | signed coarse-cell offset added by C4:334A |

### MENU_CURSOR_TILE_PREFIX_TABLE

- domain: `rom-table`
- address: `C3:E3F8`
- stride: `0x2`
- count: `7`
- struct: `menu_cursor_tile_prefix_word`
- confidence: `proposed`
- note: Seven tile/attribute words before the legacy animated menu cursor right-pointing tile run.
- evidence: `notes/c3-menu-cursor-tile-data-e3f8-e450.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `value` | 2 | 1 |  |

### ANIMATED_MENU_CURSOR_POINT_RIGHT_TILES

- domain: `rom-table`
- address: `C3:E406`
- stride: `0x8`
- count: `1`
- struct: `four_tile_word_run`
- confidence: `corroborated`
- note: Legacy AnimatedMenuCursorTiles.PointRight four-tile run.
- evidence: `notes/c3-menu-cursor-tile-data-e3f8-e450.md`, `refs/earthbound-disasm-legacy/Earthbound Decomp/EB/Routine_Macros_EB.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `tile_0` | 2 | 1 |  |
| `0x2` | `tile_1` | 2 | 1 |  |
| `0x4` | `tile_2` | 2 | 1 |  |
| `0x6` | `tile_3` | 2 | 1 |  |

### TITLE_NAME_BUFFER_CURSOR_TILE_RUN

- domain: `rom-table`
- address: `C3:E40E`
- stride: `0x8`
- count: `1`
- struct: `four_tile_word_run`
- confidence: `corroborated`
- note: Four tile/attribute words copied by C2:0266 into the title/name upload buffer.
- evidence: `notes/c3-menu-cursor-tile-data-e3f8-e450.md`, `notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `tile_0` | 2 | 1 |  |
| `0x2` | `tile_1` | 2 | 1 |  |
| `0x4` | `tile_2` | 2 | 1 |  |
| `0x6` | `tile_3` | 2 | 1 |  |

### BLINKING_TRIANGLE_BASE_TILES

- domain: `rom-table`
- address: `C3:E416`
- stride: `0x6`
- count: `1`
- struct: `three_tile_word_run`
- confidence: `corroborated`
- note: Three base/down-cursor tile words immediately before the four blinking triangle wait frames.
- evidence: `notes/c3-menu-cursor-tile-data-e3f8-e450.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `tile_0` | 2 | 1 |  |
| `0x2` | `tile_1` | 2 | 1 |  |
| `0x4` | `tile_2` | 2 | 1 |  |

### BLINKING_TRIANGLE_WAIT_FRAME_TILES

- domain: `rom-table`
- address: `C3:E41C`
- stride: `0x8`
- count: `4`
- struct: `four_tile_word_frame`
- confidence: `corroborated`
- note: Four 4-word blinking/down cursor frames selected by the long pointer table at C3:E43C.
- evidence: `notes/c3-menu-cursor-tile-data-e3f8-e450.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `tile_0` | 2 | 1 |  |
| `0x2` | `tile_1` | 2 | 1 |  |
| `0x4` | `tile_2` | 2 | 1 |  |
| `0x6` | `tile_3` | 2 | 1 |  |

### BLINKING_TRIANGLE_WAIT_FRAME_POINTER_TABLE

- domain: `rom-table`
- address: `C3:E43C`
- stride: `0x4`
- count: `4`
- struct: `far_pointer`
- confidence: `corroborated`
- note: Long pointers selecting the four blinking triangle wait frames at C3:E41C/C3:E424/C3:E42C/C3:E434.
- evidence: `notes/c3-menu-cursor-tile-data-e3f8-e450.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `pointer` | 4 | 1 |  |

### WINDOW_TICK_TRANSFER_PRELUDE_WORDS

- domain: `rom-table`
- address: `C3:E44C`
- stride: `0x2`
- count: `2`
- struct: `window_tick_transfer_prelude_word`
- confidence: `proposed`
- note: Two-word data island immediately before the C3:E450 window tick transfer helper.
- evidence: `notes/c3-menu-cursor-tile-data-e3f8-e450.md`, `notes/active-text-entry-chain-layout-c451fa.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `value` | 2 | 1 |  |

### BATTLE_PSI_MENU_SELECTOR_GROUP_TABLE

- domain: `rom-table`
- address: `C3:EF26`
- stride: `0x1`
- count: `240`
- struct: `battle_psi_menu_selector_group`
- confidence: `corroborated`
- note: Selector-minus-0x10 byte table consumed by C1:C046; zero means print the raw selector, nonzero selects a grouped PSI-list row.
- evidence: `notes/battle-psi-menu-table-helpers-c1c046-c1c165.md`, `notes/c3-battle-psi-menu-data-contracts.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `value` | 1 | 1 |  |

### BATTLE_PSI_MENU_GROUP_SLICE_COUNT_TABLE

- domain: `rom-table`
- address: `C3:F016`
- stride: `0x1`
- count: `62`
- struct: `battle_psi_menu_group_slice_count`
- confidence: `corroborated`
- note: Grouped PSI-list slice count/width byte indexed after the C3:EF26 selector-group remap.
- evidence: `notes/battle-psi-menu-table-helpers-c1c046-c1c165.md`, `notes/c3-shared-helper-working-name-promotion.md`, `notes/c3-battle-psi-menu-data-contracts.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `value` | 1 | 1 |  |

### BATTLE_PSI_GROUP_RENDER_METADATA_AND_LABELS

- domain: `rom-block`
- address: `C3:F054`
- stride: `0x5C`
- count: `1`
- struct: `battle_psi_group_render_metadata_and_labels`
- confidence: `proposed`
- note: Raw render metadata and encoded labels between the PSI selector-group slice table and the known-state gate table.
- evidence: `notes/c3-shared-helper-working-name-promotion.md`, `notes/c3-battle-psi-menu-data-contracts.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `raw_group_render_metadata_and_labels` | 1 | 92 |  |

### BATTLE_PSI_KNOWN_STATE_GATE_TABLE

- domain: `rom-table`
- address: `C3:F0B0`
- stride: `0xE`
- count: `7`
- struct: `battle_psi_known_state_gate_row`
- confidence: `corroborated`
- note: Seven 7-word live PSI-state gate rows consumed by C1:C165 while scanning a character's live PSI bytes.
- evidence: `notes/battle-psi-menu-table-helpers-c1c046-c1c165.md`, `notes/c3-battle-psi-menu-data-contracts.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `psi_slot_0_gate` | 2 | 1 |  |
| `0x2` | `psi_slot_1_gate` | 2 | 1 |  |
| `0x4` | `psi_slot_2_gate` | 2 | 1 |  |
| `0x6` | `psi_slot_3_gate` | 2 | 1 |  |
| `0x8` | `psi_slot_4_gate` | 2 | 1 |  |
| `0xA` | `psi_slot_5_gate` | 2 | 1 |  |
| `0xC` | `psi_slot_6_gate` | 2 | 1 |  |

### BATTLE_PSI_RANK_SUFFIX_TABLE

- domain: `rom-table`
- address: `C3:F112`
- stride: `0x2`
- count: `5`
- struct: `battle_psi_rank_suffix_token`
- confidence: `corroborated`
- note: Five PSI rank/suffix token words used by the PSI name/menu row formatting family.
- evidence: `notes/battle-psi-name-builder-family-c1c8bc-ca06-c3f112-f124.md`, `notes/c3-shared-helper-working-name-promotion.md`, `notes/c3-battle-psi-menu-data-contracts.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `value` | 2 | 1 |  |

### BATTLE_PSI_MENU_ENTRY_FIXED_TAIL

- domain: `rom-block`
- address: `C3:F11C`
- stride: `0x8`
- count: `1`
- struct: `battle_psi_menu_entry_fixed_tail`
- confidence: `corroborated`
- note: Eight encoded bytes appended after a formatted PSI menu-entry row.
- evidence: `notes/battle-psi-name-builder-family-c1c8bc-ca06-c3f112-f124.md`, `notes/c3-shared-helper-working-name-promotion.md`, `notes/c3-battle-psi-menu-data-contracts.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `encoded_tail` | 1 | 8 |  |

### BATTLE_PSI_MENU_ENTRY_ROW_TABLE

- domain: `rom-table`
- address: `C3:F124`
- stride: `0x14`
- count: `10`
- struct: `battle_psi_menu_entry_row`
- confidence: `corroborated`
- note: Ten fixed-width encoded PSI menu-entry text rows.
- evidence: `notes/battle-psi-name-builder-family-c1c8bc-ca06-c3f112-f124.md`, `notes/c3-shared-helper-working-name-promotion.md`, `notes/c3-battle-psi-menu-data-contracts.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `encoded_text` | 1 | 20 |  |

### LEVEL_UP_STAT_GROWTH_VARIANCE_TABLE

- domain: `rom-table`
- address: `C3:F2B1`
- stride: `0x1`
- count: `4`
- struct: `level_up_stat_growth_variance`
- confidence: `corroborated`
- note: Four-byte variance table consumed by C1:D08B while computing level-up stat growth deltas.
- evidence: `notes/level-up-stat-growth-helper-c1d08b.md`, `notes/c3-battle-visual-data-and-file-select-transition-split.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `variance` | 1 | 1 | byte added to the C4:5F7B random result by C1:D08B |

### VISUAL_SELECTOR_POSE_ROW_TABLE

- domain: `rom-table`
- address: `C3:F2B5`
- stride: `0x10`
- count: `17`
- struct: `visual_selector_pose_row`
- confidence: `corroborated`
- note: Seventeen 8-word pose-resolution rows consumed by C0:780F/C0:79EC to map higher-level visual selectors to concrete pose indices.
- evidence: `notes/visual-selector-family-c0780f-c3f2b5.md`, `notes/position-derived-visual-context-class-9887.md`, `notes/c3-battle-visual-data-and-file-select-transition-split.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `bucket_0_pose` | 2 | 1 |  |
| `0x2` | `bucket_1_pose` | 2 | 1 |  |
| `0x4` | `bucket_2_pose` | 2 | 1 |  |
| `0x6` | `bucket_3_pose` | 2 | 1 |  |
| `0x8` | `bucket_4_pose` | 2 | 1 |  |
| `0xA` | `bucket_5_pose` | 2 | 1 |  |
| `0xC` | `bucket_6_pose` | 2 | 1 |  |
| `0xE` | `bucket_7_pose` | 2 | 1 |  |

### BATTLE_VISUAL_GRAPHICS_SOURCE_STRIP_OFFSETS

- domain: `rom-table`
- address: `C3:F871`
- stride: `0x8`
- count: `8`
- struct: `battle_visual_strip_offset_page`
- confidence: `corroborated`
- note: Eight pages of four source-strip offsets into the $7F:0000 battle visual work buffer.
- evidence: `notes/c3-battle-visual-offset-tables-f871-f8f1.md`, `notes/c3-battle-visual-table-and-token-sublabels.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `strip_0_offset` | 2 | 1 |  |
| `0x2` | `strip_1_offset` | 2 | 1 |  |
| `0x4` | `strip_2_offset` | 2 | 1 |  |
| `0x6` | `strip_3_offset` | 2 | 1 |  |

### BATTLE_VISUAL_OAM_TILE_INDEX_GRID

- domain: `rom-table`
- address: `C3:F8B1`
- stride: `0x10`
- count: `4`
- struct: `battle_visual_oam_tile_index_row`
- confidence: `corroborated`
- note: Four-row OAM tile-index grid consumed by the C2 battle visual sprite renderer.
- evidence: `notes/c3-battle-visual-offset-tables-f871-f8f1.md`, `notes/c3-battle-visual-table-and-token-sublabels.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `tile_0` | 2 | 1 |  |
| `0x2` | `tile_1` | 2 | 1 |  |
| `0x4` | `tile_2` | 2 | 1 |  |
| `0x6` | `tile_3` | 2 | 1 |  |
| `0x8` | `tile_4` | 2 | 1 |  |
| `0xA` | `tile_5` | 2 | 1 |  |
| `0xC` | `tile_6` | 2 | 1 |  |
| `0xE` | `tile_7` | 2 | 1 |  |

### BATTLE_PALETTE_SET_ROWS

- domain: `rom-table`
- address: `C3:F8F1`
- stride: `0x20`
- count: `3`
- struct: `rgb555_palette_row`
- confidence: `corroborated`
- note: Three confirmed 16-colour palette rows selected by C2:FEF9.
- evidence: `notes/c3-battle-visual-offset-tables-f871-f8f1.md`, `notes/c3-battle-visual-table-and-token-sublabels.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `rgb555_colour_0` | 2 | 1 |  |
| `0x2` | `rgb555_colour_1` | 2 | 1 |  |
| `0x4` | `rgb555_colour_2` | 2 | 1 |  |
| `0x6` | `rgb555_colour_3` | 2 | 1 |  |
| `0x8` | `rgb555_colour_4` | 2 | 1 |  |
| `0xA` | `rgb555_colour_5` | 2 | 1 |  |
| `0xC` | `rgb555_colour_6` | 2 | 1 |  |
| `0xE` | `rgb555_colour_7` | 2 | 1 |  |
| `0x10` | `rgb555_colour_8` | 2 | 1 |  |
| `0x12` | `rgb555_colour_9` | 2 | 1 |  |
| `0x14` | `rgb555_colour_10` | 2 | 1 |  |
| `0x16` | `rgb555_colour_11` | 2 | 1 |  |
| `0x18` | `rgb555_colour_12` | 2 | 1 |  |
| `0x1A` | `rgb555_colour_13` | 2 | 1 |  |
| `0x1C` | `rgb555_colour_14` | 2 | 1 |  |
| `0x1E` | `rgb555_colour_15` | 2 | 1 |  |

### BATTLE_VISUAL_TOKEN_23_TO_2D_COLOUR_TRIPLES

- domain: `rom-table`
- address: `C3:F951`
- stride: `0x3`
- count: `11`
- struct: `battle_visual_fixed_colour_triple`
- confidence: `corroborated`
- note: RGB component triples for visual tokens #$23..#$2D.
- evidence: `notes/c3-battle-visual-table-and-token-sublabels.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `red_component` | 1 | 1 | table byte 0; passed through Y to SetFixedColourRgbComponents |
| `0x1` | `green_component` | 1 | 1 | table byte 1; passed through X to SetFixedColourRgbComponents |
| `0x2` | `blue_component` | 1 | 1 | table byte 2; passed through A to SetFixedColourRgbComponents |

### BATTLE_VISUAL_TOKEN_31_TO_35_COLOUR_TRIPLES

- domain: `rom-table`
- address: `C3:F972`
- stride: `0x3`
- count: `5`
- struct: `battle_visual_fixed_colour_triple`
- confidence: `corroborated`
- note: RGB component triples for visual tokens #$31..#$35.
- evidence: `notes/c3-battle-visual-table-and-token-sublabels.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `red_component` | 1 | 1 | table byte 0; passed through Y to SetFixedColourRgbComponents |
| `0x1` | `green_component` | 1 | 1 | table byte 1; passed through X to SetFixedColourRgbComponents |
| `0x2` | `blue_component` | 1 | 1 | table byte 2; passed through A to SetFixedColourRgbComponents |

### BLANK_COMMON_TILE_SOURCE_BLOCK

- domain: `rom-table`
- address: `C4:0BE8`
- stride: `0x200`
- count: `1`
- struct: `blank_common_tile_source_block`
- confidence: `corroborated`
- note: Zero-filled C4 source block used by setup/visual paths as a common blank graphics or tile-memory seed.
- evidence: `notes/landing-and-coffee-tea-visual-helpers-c492d2-c49d1e.md`, `notes/bank-c4-progress-audit.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `zero_byte` | 1 | 512 | all bytes are zero; copied as a blank graphics/tile source block |

### WH_WINDOW_SPAN_RADIUS_RAMP_TABLE

- domain: `rom-table`
- address: `C4:74F6`
- stride: `0x1`
- count: `11`
- struct: `wh_window_span_radius_ramp_entry`
- confidence: `corroborated`
- note: Half-width/radius bytes indexed in reverse by C4:7501 while generating tapered WH window spans.
- evidence: `notes/window-mask-and-indexed-gfx-c47501-c47b77.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `value` | 1 | 1 |  |

### MOVEMENT_OCTANT_TO_PULSE_SELECTOR_TABLE

- domain: `rom-table`
- address: `C4:8C59`
- stride: `0x2`
- count: `8`
- struct: `movement_octant_pulse_selector`
- confidence: `corroborated`
- note: Eight word selectors mapping rounded movement octants to generated movement pulse ids.
- evidence: `notes/staged-movement-pulse-and-tracked-item-registry-c48c59-c48f98.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `value` | 2 | 1 |  |

### MOVEMENT_OCTANT_SIGNED_UNIT_DELTA_TABLE

- domain: `rom-table`
- address: `C4:8D38`
- stride: `0x20`
- count: `1`
- struct: `movement_octant_signed_unit_delta_components`
- confidence: `proposed`
- note: Sixteen signed words forming two eight-entry unit-delta component arrays adjacent to the staged movement builder.
- evidence: `notes/staged-movement-pulse-and-tracked-item-registry-c48c59-c48f98.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `component` | 2 | 16 | two eight-word signed unit-vector component arrays |

### YOUR_SANCTUARY_LOCATION_COORDINATE_TABLE

- domain: `rom-table`
- address: `C4:DE78`
- stride: `0x4`
- count: `8`
- struct: `your_sanctuary_location_coordinate_pair`
- confidence: `corroborated`
- note: Eight two-word coordinate/source records consumed by the Your Sanctuary display loader at C4:E281.
- evidence: `notes/your-sanctuary-location-coordinate-table-c4de78.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `word_0` | 2 | 1 | first coordinate/source word passed to C4:E13E |
| `0x2` | `word_1` | 2 | 1 | second coordinate/source word passed to C4:E13E |
