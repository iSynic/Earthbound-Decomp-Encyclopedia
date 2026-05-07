# C1 build-candidate byte ranges

This manifest records source slices promoted into the reusable source-bank scaffold pipeline.

## Summary

- ranges: `172`
- total bytes: `65536`
- source bytes: `65536`
- data gap bytes: `0`

## Ranges

| Level | Source Path | Range | Span Bytes | Source Bytes | Data Gap Bytes | SHA-1 |
| --- | --- | --- | ---: | ---: | ---: | --- |
| `build-candidate` | `src/c1/c1_0000_run_text_display_setup_wrapper.asm` | `C1:0000..C1:0004` | 4 | 4 | 0 | `a5d859d705ea9593946d357a7ab686c37e674291` |
| `build-candidate` | `src/c1/c1_0004_process_textbox_data_from_caller_pointer.asm` | `C1:0004..C1:004E` | 74 | 74 | 0 | `8b5ed13f249f9491055bb86633e177868b7d3214` |
| `build-candidate` | `src/c1/c1_004e_pump_text_wait_frame.asm` | `C1:004E..C1:008E` | 64 | 64 | 0 | `3c03a3da7cf562ee81735f188a567dc74915be85` |
| `build-candidate` | `src/c1/c1_008e_close_and_drain_all_windows.asm` | `C1:008E..C1:00D6` | 72 | 72 | 0 | `678643d391d471a4144d1d2166f88558bea64a19` |
| `build-candidate` | `src/c1/c1_00d6_wait_text_ticks.asm` | `C1:00D6..C1:00FE` | 40 | 40 | 0 | `b018c469eb83d7d62b5790d0b67a7ed01ac824a7` |
| `build-candidate` | `src/c1/c1_00fe_wait_for_text_prompt_or_input_gate.asm` | `C1:00FE..C1:0166` | 104 | 104 | 0 | `1f2dda96ef66f5240883f0e525e2643958ea630b` |
| `build-candidate` | `src/c1/c1_0166_run_text_halt_control_worker.asm` | `C1:0166..C1:02D0` | 362 | 362 | 0 | `dafacf0fdccc6ec8dff9aac3b97f5002af406643` |
| `build-candidate` | `src/c1/c1_02d0_wait_for_text_state_flag9641.asm` | `C1:02D0..C1:0301` | 49 | 49 | 0 | `d8e1be84c972ad1d1a169aed8a68b4bb7c314f37` |
| `build-candidate` | `src/c1/c1_0301_get_active_interaction_context_record.asm` | `C1:0301..C1:042E` | 301 | 301 | 0 | `8ca4917c2435cd5cf66d60c11c6c101cb014aa85` |
| `build-candidate` | `src/c1/c1_042e_increment_current_text_context_workmem.asm` | `C1:042E..C1:045D` | 47 | 47 | 0 | `6139e06b5304c33312f0b8cc505c9c3f41d24e16` |
| `build-candidate` | `src/c1/c1_045d_install_primary_interaction_context_pointer.asm` | `C1:045D..C1:0489` | 44 | 44 | 0 | `b6c5d64a488b327efef82188ba55b8cae2eb24b2` |
| `build-candidate` | `src/c1/c1_0489_install_secondary_interaction_context_pointer.asm` | `C1:0489..C1:04B5` | 44 | 44 | 0 | `28e188e439ca906a889d8983e54f1c8809a9a833` |
| `build-candidate` | `src/c1/c1_04b5_get_current_text_context_line_state.asm` | `C1:04B5..C1:078D` | 728 | 728 | 0 | `722e4541b18c500d78e6a2c994218173d4ca3287` |
| `build-candidate` | `src/c1/c1_078d_initialize_text_window_tilemap_staging.asm` | `C1:078D..C1:07AF` | 34 | 34 | 0 | `aac284b123aa7cfcb778252046fed317cc3097db` |
| `build-candidate` | `src/c1/c1_07af_build_window_tilemap_from_descriptor.asm` | `C1:07AF..C1:0A85` | 726 | 726 | 0 | `6ff65bdca5c19da8b98f35d4544ec438bac9d7ac` |
| `build-candidate` | `src/c1/c1_0a85_write_glyph_to_window_descriptor_buffer.asm` | `C1:0A85..C1:0BA1` | 284 | 284 | 0 | `e5e692407ff007130e54273a9b464b9ce7585793` |
| `build-candidate` | `src/c1/c1_0ba1_print_glyph_to_active_window.asm` | `C1:0BA1..C1:0BFE` | 93 | 93 | 0 | `30085841a009f84e60364760cfea6ed821dd9931` |
| `build-candidate` | `src/c1/c1_0bfe_create_pointer_backed_text_entry_record.asm` | `C1:0BFE..C1:0C49` | 75 | 75 | 0 | `8bfdd71da075744a4244a84739a182d756822cbd` |
| `build-candidate` | `src/c1/c1_0c49_count_text_entry_chain_records.asm` | `C1:0C49..C1:0C55` | 12 | 12 | 0 | `e9fe278b649e32c343ddd376cfd3306456fcca1c` |
| `build-candidate` | `src/c1/c1_0c55_format_number_from_caller_pointer.asm` | `C1:0C55..C1:0D60` | 267 | 267 | 0 | `88c42900ff8e25c457646053b5ff057acda61653` |
| `build-candidate` | `src/c1/c1_0d60_print_glyph_and_mark_window_redraw.asm` | `C1:0D60..C1:0D7C` | 28 | 28 | 0 | `d2d1346820d2353ed820311a33e040fec0a25317` |
| `build-candidate` | `src/c1/c1_0d7c_format_decimal_digits_to8960.asm` | `C1:0D7C..C1:0F40` | 452 | 452 | 0 | `b3f74bf406e93d84687c0dce165af67b7d7086b4` |
| `build-candidate` | `src/c1/c1_0f40_clear_window_content_by_focus_index.asm` | `C1:0F40..C1:134B` | 1035 | 1035 | 0 | `a9c171e13b632ecf8e3ca9167cfa397d8d194f48` |
| `build-candidate` | `src/c1/c1_134b_setup_text_display_with_wallet_status.asm` | `C1:134B..C1:138D` | 66 | 66 | 0 | `75e608219197f4ff0a38791e627a0556fb3d37b3` |
| `build-candidate` | `src/c1/c1_138d_count_text_entry_chain_records_local.asm` | `C1:138D..C1:13D1` | 68 | 68 | 0 | `0d61705ee6b873277d92142874ce3ff5ef73eeb3` |
| `build-candidate` | `src/c1/c1_13d1_install_text_entry_record.asm` | `C1:13D1..C1:14B1` | 224 | 224 | 0 | `5d00f83b53f4c08cafe6dfd35643e18492a1b386` |
| `build-candidate` | `src/c1/c1_14b1_create_text_entry_record_with_display_metadata.asm` | `C1:14B1..C1:153B` | 138 | 138 | 0 | `267968eab530f55a5b34b9eb3e77351d77090d07` |
| `build-candidate` | `src/c1/c1_153b_create_typed_text_entry_record.asm` | `C1:153B..C1:1596` | 91 | 91 | 0 | `3cac37d3c656fa9b395a02f9e23edcfc6ccdb807` |
| `build-candidate` | `src/c1/c1_1596_create_typed_text_entry_record_with_extra_byte.asm` | `C1:1596..C1:15F4` | 94 | 94 | 0 | `65694f3d023f56170aab36a79335e3e25fdb6670` |
| `build-candidate` | `src/c1/c1_15f4_create_typed_text_entry_record_direct.asm` | `C1:15F4..C1:17E2` | 494 | 494 | 0 | `b01d0b0ae86d74ed7fea2df84b3bb422573827fe` |
| `build-candidate` | `src/c1/c1_17e2_measure_bounded_string_length.asm` | `C1:17E2..C1:180D` | 43 | 43 | 0 | `5b7f97f7e39817b87ed8d9f08c8a4b1fe43ca36c` |
| `build-candidate` | `src/c1/c1_180d_layout_active_text_entries_and_refresh.asm` | `C1:180D..C1:181B` | 14 | 14 | 0 | `f4c8b10b0f3fdfd2f60c3e601fe700bb363e672f` |
| `build-candidate` | `src/c1/c1_181b_select_active_text_entry_by_y.asm` | `C1:181B..C1:1887` | 108 | 108 | 0 | `ab32bfec56edffff8337b9f424c2898e7ef6153c` |
| `build-candidate` | `src/c1/c1_1887_select_active_text_entry_by_a.asm` | `C1:1887..C1:1F8A` | 1795 | 1795 | 0 | `679eb3c74881bc2412200686d839125d1edc8e2e` |
| `build-candidate` | `src/c1/c1_1f8a_clear_active_selection_prompt_scratch.asm` | `C1:1F8A..C1:1FBC` | 50 | 50 | 0 | `f79cffb41852d058d90e0de82f82c4361174e6ce` |
| `build-candidate` | `src/c1/c1_1fbc_read_selection_prompt_candidate_byte.asm` | `C1:1FBC..C1:1FD4` | 24 | 24 | 0 | `a8b1d5a249e38c749ecd16d73893c04ceb87d5bf` |
| `build-candidate` | `src/c1/c1_1fd4_is_selection_prompt_candidate_eligible.asm` | `C1:1FD4..C1:2012` | 62 | 62 | 0 | `c2af7f1c0e7e0a97f7800b4f3f7d20258e7850e7` |
| `build-candidate` | `src/c1/c1_2012_find_next_selection_prompt_candidate.asm` | `C1:2012..C1:2070` | 94 | 94 | 0 | `c705d06ac195a83310541455bc1a62390e1d700c` |
| `build-candidate` | `src/c1/c1_2070_find_previous_selection_prompt_candidate.asm` | `C1:2070..C1:20D6` | 102 | 102 | 0 | `ccc4f32808b89e38887ccb560fd5e7d7bd29d037` |
| `build-candidate` | `src/c1/c1_20d6_refresh_selection_prompt_candidate_text.asm` | `C1:20D6..C1:21B8` | 226 | 226 | 0 | `9371f6ee3b662fecf4820559d0bae5840b340bfb` |
| `build-candidate` | `src/c1/c1_21b8_run_two_list_character_selection_prompt.asm` | `C1:21B8..C1:2362` | 426 | 426 | 0 | `e868071c905abad0d9920f6e00cc8deb581c0c6b` |
| `build-candidate` | `src/c1/c1_2362_run_simple_side_selection_prompt.asm` | `C1:2362..C1:242E` | 204 | 204 | 0 | `aeea32d272e4a8c391b93ac2b272aecf77d91396` |
| `build-candidate` | `src/c1/c1_2bf3_print_debug_menu_title_words_with_ticks.asm` | `C1:2BF3..C1:2C36` | 67 | 67 | 0 | `9bc16ff667923e1658a45458734657e8b44b58d3` |
| `build-candidate` | `src/c1/c1_2c36_print_debug_menu_fixed_word_groups.asm` | `C1:2C36..C1:2CCC` | 150 | 150 | 0 | `0b905a67c7b92430ff52bd56e506895d83792470` |
| `build-candidate` | `src/c1/c1_2ccc_format_debug_decimal_five_digits.asm` | `C1:2CCC..C1:2D17` | 75 | 75 | 0 | `52098afd72d74552ea4ae40d380412d549e3b443` |
| `build-candidate` | `src/c1/c1_2d17_toggle_debug_meter_display_overlay.asm` | `C1:2D17..C1:3187` | 1136 | 1136 | 0 | `c1ce90b717e3b1d0f8f3fdab4ff92b7f5bd8134c` |
| `build-candidate` | `src/c1/c1_3187_resolve_primary_front_interaction_output.asm` | `C1:3187..C1:323B` | 180 | 180 | 0 | `492d69d0f7dd1882bcbdcec3c82deb342ffdd24b` |
| `build-candidate` | `src/c1/c1_323b_resolve_secondary_facing_interaction_output.asm` | `C1:323B..C1:339E` | 355 | 355 | 0 | `f4f1a42f4e4914ff8f022d341b542e2b53a30ca7` |
| `build-candidate` | `src/c1/c1_339e_build_check_menu_entries_wrapper.asm` | `C1:339E..C1:33A7` | 9 | 9 | 0 | `e34f8f780c8fb99b738b7b01f7490fabff092049` |
| `build-candidate` | `src/c1/c1_33a7_build_open_menu_entries_wrapper.asm` | `C1:33A7..C1:33B0` | 9 | 9 | 0 | `19ec07343b65fa276bac468e6d569704a5634977` |
| `build-candidate` | `src/c1/c1_33b0_rebuild_open_menu_text_entry_records.asm` | `C1:33B0..C1:4103` | 3411 | 3411 | 0 | `65982a644f5cc1c64b3fb6966720b2e6da3de00a` |
| `build-candidate` | `src/c1/c1_4103_build_text_command24_bit_jump_target.asm` | `C1:4103..C1:41D0` | 205 | 205 | 0 | `bac5ef8186135b1541d8674d5aec72a7304170e4` |
| `build-candidate` | `src/c1/c1_41d0_handle_text_command09_jump_multi.asm` | `C1:41D0..C1:4265` | 149 | 149 | 0 | `c85e53f17c21d90c57cb68f115cdc6025ed65dee` |
| `build-candidate` | `src/c1/c1_4265_handle_text_command04_set_event_flag.asm` | `C1:4265..C1:42AD` | 72 | 72 | 0 | `d94dead8106d8668d5e5f33a8b698966845d6cf9` |
| `build-candidate` | `src/c1/c1_42ad_handle_text_command05_clear_event_flag.asm` | `C1:42AD..C1:42F5` | 72 | 72 | 0 | `0e76518285a4fb80938b3fbe9667460198eb08b5` |
| `build-candidate` | `src/c1/c1_42f5_handle_text_command06_jump_if_flag_set.asm` | `C1:42F5..C1:435F` | 106 | 106 | 0 | `10e6288e84d6ff1b42bf65774299ea23bcb957f8` |
| `build-candidate` | `src/c1/c1_435f_handle_text_command07_check_event_flag.asm` | `C1:435F..C1:43D6` | 119 | 119 | 0 | `143f89292ea9db3d081837decc7e5d82a6a913b1` |
| `build-candidate` | `src/c1/c1_43d6_build_call_text_far_pointer_and_dispatch.asm` | `C1:43D6..C1:4558` | 386 | 386 | 0 | `ed27ebf8828f158e17d5799d2b1dd08f80e6dd15` |
| `build-candidate` | `src/c1/c1_4558_handle_text_command0_btest_workmem_true.asm` | `C1:4558..C1:4591` | 57 | 57 | 0 | `8e13a68e48efb2ae7b5ceb24ea65f365868c8af9` |
| `build-candidate` | `src/c1/c1_4591_handle_text_command0_ctest_workmem_false.asm` | `C1:4591..C1:45EF` | 94 | 94 | 0 | `03ea9491c913ed147dcf7abb39402a8989c8a695` |
| `build-candidate` | `src/c1/c1_45ef_handle_text_command0_dcopy_to_argmem.asm` | `C1:45EF..C1:461A` | 43 | 43 | 0 | `3006d8346fa4571bb8f76d5c365e8e115f531711` |
| `build-candidate` | `src/c1/c1_461a_handle_text_command0_estore_to_argmem.asm` | `C1:461A..C1:4819` | 511 | 511 | 0 | `3ff6a821a6daa22f8b6ddc4b5f0e315bdb915a4f` |
| `build-candidate` | `src/c1/c1_4819_read_statistic_selector_string_character.asm` | `C1:4819..C1:48AC` | 147 | 147 | 0 | `149a41dcf12edbf060f6b5c0b1daa83e9fef89bf` |
| `build-candidate` | `src/c1/c1_48ac_test_current_item_compact_category.asm` | `C1:48AC..C1:4CEE` | 1090 | 1090 | 0 | `2502a61cdecefd1bf160dfde1576b86c565d0075` |
| `build-candidate` | `src/c1/c1_4cee_find_party_member_with_inventory_room_for_text_command.asm` | `C1:4CEE..C1:4D93` | 165 | 165 | 0 | `69877d43b463c87bae2a9d4a5e68cd847f8a1762` |
| `build-candidate` | `src/c1/c1_4d93_find_party_member_with_item_for_text_command.asm` | `C1:4D93..C1:4EAB` | 280 | 280 | 0 | `d95d7d0220b4c0106f6fea524800308c913b766a` |
| `build-candidate` | `src/c1/c1_4eab_handle_text_command10_parameterized_pause.asm` | `C1:4EAB..C1:575D` | 2226 | 2226 | 0 | `630a0ae3bfb26e89c34c184f1629c036489d84c5` |
| `build-candidate` | `src/c1/c1_575d_test_equipped_item_presence_for_text_command.asm` | `C1:575D..C1:621F` | 2754 | 2754 | 0 | `a3dd53b9d961dea0f74dfbe87b76f62ffd5f5a3f` |
| `build-candidate` | `src/c1/c1_621f_finalize_text_command1_fc0_jump_multi2_target.asm` | `C1:621F..C1:7274` | 4181 | 4181 | 0 | `423e42139dbcf2b8830f2c498abc9552c5996054` |
| `build-candidate` | `src/c1/c1_7274_stage_bank_deposit_accumulator_text_value.asm` | `C1:7274..C1:7440` | 460 | 460 | 0 | `4dd1828f2c1bd8c3ded97248ce2b3daad3a1f40b` |
| `build-candidate` | `src/c1/c1_7440_timed_delivery_row_selector_callback.asm` | `C1:7440..C1:7708` | 712 | 712 | 0 | `98508df0ba99a3d8cc4813c7e6e68037d3d6e19d` |
| `build-candidate` | `src/c1/c1_7708_classify_equipped_item_offensive_defensive.asm` | `C1:7708..C1:7796` | 142 | 142 | 0 | `4b79e8127a5b7283524dfc02c6b8e14a5b93b3e6` |
| `build-candidate` | `src/c1/c1_7796_finalize_loaded_string_with_companion_pointer.asm` | `C1:7796..C1:7889` | 243 | 243 | 0 | `db39cf8e55731f1eb17a100e0a48df28dcf8467a` |
| `build-candidate` | `src/c1/c1_7889_continue_loaded_string_inline_collector.asm` | `C1:7889..C1:78F7` | 110 | 110 | 0 | `a6512489cbf220df1dcbaaaa7137e7a8ef71b4de` |
| `build-candidate` | `src/c1/c1_78f7_start_loaded_string_inline_collector.asm` | `C1:78F7..C1:7AE3` | 492 | 492 | 0 | `857a2bc4962c79a994f641c03dfba6236cc87f93` |
| `build-candidate` | `src/c1/c1_7ae3_load_display_text_pointer_substitution_slot.asm` | `C1:7AE3..C1:7AF3` | 16 | 16 | 0 | `46f16391ed49a2aed4e71284ad3261e1740c3426` |
| `build-candidate` | `src/c1/c1_7af3_load_display_text_byte_substitution_slot.asm` | `C1:7AF3..C1:7B0D` | 26 | 26 | 0 | `95e5856f6ac87fdcc1a403f590a31289b8920d39` |
| `build-candidate` | `src/c1/c1_7b0d_load_display_text_mushroomized_selector_byte.asm` | `C1:7B0D..C1:7B56` | 73 | 73 | 0 | `333943af757b553092fac7f33c0fad5ee9001486` |
| `build-candidate` | `src/c1/c1_7b56_dispatch_display_text_dynamic_source_selector.asm` | `C1:7B56..C1:866D` | 2839 | 2839 | 0 | `11e2e2fb0cad350be15d0acf3005c15905d5d0ee` |
| `build-candidate` | `src/c1/c1_866d_initialize_managed_text_event_slot_front.asm` | `C1:866D..C1:869D` | 48 | 48 | 0 | `4cbf6d189f9481ff6ece6c1128d9cf3917785a8f` |
| `build-candidate` | `src/c1/c1_869d_apply_active_managed_text_event_slot_snapshot.asm` | `C1:869D..C1:86B1` | 20 | 20 | 0 | `994d598162289c5c6d5abbf369266b602de4deb1` |
| `build-candidate` | `src/c1/c1_91f8_withdraw_pending_item_to_inventory.asm` | `C1:91F8..C1:9216` | 30 | 30 | 0 | `0cbe7a9e670945056b57189c07d600950ba0e009` |
| `build-candidate` | `src/c1/c1_9216_print_item_name_from_configuration_table.asm` | `C1:9216..C1:9249` | 51 | 51 | 0 | `0e80da8de6afd0e20cb30c4ae4d70f30791b69d1` |
| `build-candidate` | `src/c1/c1_9b4e_build_equipment_comparison_markers_for_item.asm` | `C1:9B4E..C1:9B79` | 43 | 43 | 0 | `0bdf4a12841e97436ae88d34af2018907ccc5ea2` |
| `build-candidate` | `src/c1/c1_a778_refresh_selected_character_equipment_display.asm` | `C1:A778..C1:A795` | 29 | 29 | 0 | `461c87932697ae13de762edceca15e00dc17f30c` |
| `build-candidate` | `src/c1/c1_ac4a_build_battle_attacker_name_buffer.asm` | `C1:AC4A..C1:AC9B` | 81 | 81 | 0 | `4029d4d0db585f58a71bb574c1d37b38ddcbffc2` |
| `build-candidate` | `src/c1/c1_ac9b_get_battle_attacker_name_buffer_base.asm` | `C1:AC9B..C1:ACA1` | 6 | 6 | 0 | `e5eecb34b2d04d492702c9d3a604823f8f33e4b7` |
| `build-candidate` | `src/c1/c1_aca1_build_battle_target_name_buffer.asm` | `C1:ACA1..C1:ACF2` | 81 | 81 | 0 | `3ebf541a990da4e46cf0a0fdde4afdf7510b7a27` |
| `build-candidate` | `src/c1/c1_acf2_get_battle_target_name_buffer_base.asm` | `C1:ACF2..C1:ACF8` | 6 | 6 | 0 | `fd547842b75297d0da7419a95b271200e7d70d8a` |
| `build-candidate` | `src/c1/c1_acf8_stage_battle_text_substitution_byte.asm` | `C1:ACF8..C1:AD02` | 10 | 10 | 0 | `72e72eb17175b873da1837029d2fb3237bbbdf2f` |
| `build-candidate` | `src/c1/c1_ad02_read_battle_text_substitution_byte.asm` | `C1:AD02..C1:AD0A` | 8 | 8 | 0 | `da9946e6589ad8d9a3e97c8f62954ba17ab5f5e8` |
| `build-candidate` | `src/c1/c1_ad0a_stage_battle_text_substitution_pointer.asm` | `C1:AD0A..C1:AD26` | 28 | 28 | 0 | `78aaaa34af0f0b508671a42833600dbd6eb93818` |
| `build-candidate` | `src/c1/c1_ad26_load_battle_text_substitution_pointer.asm` | `C1:AD26..C1:AD42` | 28 | 28 | 0 | `17e1629a0fa1f3f489e66107d50571c7bce19454` |
| `build-candidate` | `src/c1/c1_ad42_get_front_interaction_result_class.asm` | `C1:AD42..C1:AD7D` | 59 | 59 | 0 | `1b6a47e2372ec3ee54feb02569913222798a73df` |
| `build-candidate` | `src/c1/c1_ad7d_read_overworld_position_context_byte.asm` | `C1:AD7D..C1:ADB4` | 55 | 55 | 0 | `13a238f618edddd2dbeae85a1bd936f1f9e11bd8` |
| `build-candidate` | `src/c1/c1_dd3b_redirect_show_hppp_windows.asm` | `C1:DD3B..C1:DD41` | 6 | 6 | 0 | `779e396c38703329e8bbd6d9b35276a61eec6c6d` |
| `build-candidate` | `src/c1/c1_dd41_redirect_hide_hppp_windows.asm` | `C1:DD41..C1:DD47` | 6 | 6 | 0 | `71b34d46f6003d9213098e913e2fd01d9cefbfe4` |
| `build-candidate` | `src/c1/c1_dd47_redirect_create_window.asm` | `C1:DD47..C1:DD4D` | 6 | 6 | 0 | `6f2699556c09f7541dd350944a41027fa073910d` |
| `build-candidate` | `src/c1/c1_dd4d_redirect_set_window_focus.asm` | `C1:DD4D..C1:DD53` | 6 | 6 | 0 | `b2cb18b4ae8caf1260614a94dd43f3fe981d80c1` |
| `build-candidate` | `src/c1/c1_dd53_redirect_text_entry_helper0_fa3.asm` | `C1:DD53..C1:DD59` | 6 | 6 | 0 | `3df60d84e743f988b4ad26be6001efd7c50f05a8` |
| `build-candidate` | `src/c1/c1_dd59_redirect_close_focus_window.asm` | `C1:DD59..C1:DD5F` | 6 | 6 | 0 | `e3dbc0ed43c864ff2ef2e151a8281ceb3f5bbba6` |
| `build-candidate` | `src/c1/c1_dd5f_battle_display_close_and_sync_wait.asm` | `C1:DD5F..C1:DD70` | 17 | 17 | 0 | `b5ea12cdf7add591a34247f922b426dcad829d87` |
| `build-candidate` | `src/c1/c1_dd70_redirect_build_battle_attacker_name_buffer.asm` | `C1:DD70..C1:DD76` | 6 | 6 | 0 | `60665b618a3c2a8b2e183a46d8ae8867e9cfd142` |
| `build-candidate` | `src/c1/c1_dd76_redirect_build_battle_target_name_buffer.asm` | `C1:DD76..C1:DD7C` | 6 | 6 | 0 | `bd5cd95ee85cf5cfc5c7da61b0adbd3a66c160c4` |
| `build-candidate` | `src/c1/c1_dd7c_redirect_stage_battle_text_substitution_byte.asm` | `C1:DD7C..C1:DD82` | 6 | 6 | 0 | `7cbfc4e4e84372d7afd1fd0bf4d2f3ad888719a7` |
| `build-candidate` | `src/c1/c1_dd82_stage_battle_text_pointer_substitution_only.asm` | `C1:DD82..C1:DD9F` | 29 | 29 | 0 | `e71f8ee11bf3ee2e1984b98f1cc7de26e995acf6` |
| `build-candidate` | `src/c1/c1_e48d_render_single_text_input_option_row_scoped.asm` | `C1:E48D..C1:E4BE` | 49 | 49 | 0 | `0d6c39d2aa2a0636ab8b3d6fed86df0c977899e4` |
| `build-candidate` | `src/c1/c1_ff2c_update_lead_entity_type_redraw_flag.asm` | `C1:FF2C..C1:FF6B` | 63 | 63 | 0 | `df0b233c5cd5cf81e2b716b2a341000b4d400e3b` |
| `build-candidate` | `src/c1/c1_ff6b_run_file_select_session.asm` | `C1:FF6B..C1:FF99` | 46 | 46 | 0 | `74a658f2c5fbdcff227873b796deff7a413d5559` |
| `build-candidate` | `src/c1/c1_242e_dispatch_character_selection_prompt_mode.asm` | `C1:242E..C1:2BF3` | 1989 | 1989 | 0 | `f4ec423087f9830f6ec26f2eb75bb00d6c40f88a` |
| `build-candidate` | `src/c1/c1_86b1_execute_nested_text_pointer.asm` | `C1:86B1..C1:87CC` | 283 | 283 | 0 | `2e7f0c5152c905a14c61c664a4e850661d94fb15` |
| `build-candidate` | `src/c1/c1_87cc_invoke_text_engine_callback_low_word.asm` | `C1:87CC..C1:8B2C` | 864 | 864 | 0 | `f4714904318998cea84cc24052ee8e03afd1457e` |
| `build-candidate` | `src/c1/c1_8b2c_insert_item_into_first_empty_inventory_slot.asm` | `C1:8B2C..C1:8BC6` | 154 | 154 | 0 | `3f1f8d255c40fd24f559eb20fb28360c8737697f` |
| `build-candidate` | `src/c1/c1_8bc6_insert_item_into_character_inventory.asm` | `C1:8BC6..C1:8C27` | 97 | 97 | 0 | `bbf5bd015ef316cd1c07e283bc807658d1144ad4` |
| `build-candidate` | `src/c1/c1_8c27_remove_item_from_character_inventory_slot.asm` | `C1:8C27..C1:8E5B` | 564 | 564 | 0 | `45b0a412abe0b59eae3a71e9e8076e4af4648743` |
| `build-candidate` | `src/c1/c1_8e5b_search_and_remove_item_from_character_inventory.asm` | `C1:8E5B..C1:8EAD` | 82 | 82 | 0 | `e68b13b7369a7f3dab1efa57784d7e6f8df88499` |
| `build-candidate` | `src/c1/c1_8ead_search_and_remove_item_from_active_inventories.asm` | `C1:8EAD..C1:8F0E` | 97 | 97 | 0 | `6f89fdec770c5f7801bf2fb98cd7c364ff3d9bb6` |
| `build-candidate` | `src/c1/c1_8f0e_deplete_hp_for_character_or_active_party.asm` | `C1:8F0E..C1:8F64` | 86 | 86 | 0 | `22dfcf1ead6ace358f6005ebe61fad226bf50e02` |
| `build-candidate` | `src/c1/c1_8f64_recover_hp_for_character_or_active_party.asm` | `C1:8F64..C1:8FBA` | 86 | 86 | 0 | `5b15128cb98cdce62a69a37d4224ef02cc8dd09e` |
| `build-candidate` | `src/c1/c1_8fba_deplete_pp_for_character_or_active_party.asm` | `C1:8FBA..C1:9010` | 86 | 86 | 0 | `d3bdf43fbe5ab289745d3e6e31e6b4ddd84c9d2c` |
| `build-candidate` | `src/c1/c1_9010_recover_pp_for_character_or_active_party.asm` | `C1:9010..C1:9066` | 86 | 86 | 0 | `3d09b08ffb112276dc7c5e9d4a2c2f4f12081874` |
| `build-candidate` | `src/c1/c1_9066_dispatch_equipped_slot_subtype_update.asm` | `C1:9066..C1:90E6` | 128 | 128 | 0 | `c0f098541c22a494cab3c7844f1d42796a6cb007` |
| `build-candidate` | `src/c1/c1_90e6_read_active_overworld_registry_type_code.asm` | `C1:90E6..C1:913D` | 87 | 87 | 0 | `f7d9cf72d9af22ef89020f669a183cfa5709a6ce` |
| `build-candidate` | `src/c1/c1_913d_enqueue_pending_item_id.asm` | `C1:913D..C1:91B0` | 115 | 115 | 0 | `1ea9d865f731d6a14424d4f1fd5d2fc9af971c90` |
| `build-candidate` | `src/c1/c1_91b0_remove_pending_item_id_at_index.asm` | `C1:91B0..C1:91F8` | 72 | 72 | 0 | `46579dd1adcd2f5dbac68c24ee5a85bd58522aa8` |
| `build-candidate` | `src/c1/c1_9249_print_statistic_selector_value.asm` | `C1:9249..C1:931B` | 210 | 210 | 0 | `1669edfe8918c7a9120997d3dec4fb1c8b7c7c59` |
| `build-candidate` | `src/c1/c1_931b_print_psi_or_small_dynamic_label.asm` | `C1:931B..C1:93E7` | 204 | 204 | 0 | `fcbaef42a7c8e720fb9a92e5c1d1966a8ba9b3b4` |
| `build-candidate` | `src/c1/c1_93e7_open_target_selection_prompt_label.asm` | `C1:93E7..C1:9437` | 80 | 80 | 0 | `57e6955ccb173ca6352827716cc8cf3a76bda97b` |
| `build-candidate` | `src/c1/c1_9437_close_target_selection_prompt_label.asm` | `C1:9437..C1:9A11` | 1498 | 1498 | 0 | `2a788c6a8b7f70ae7ae3fc3da61a78cef0499982` |
| `build-candidate` | `src/c1/c1_9a11_run_selection_helper_with_temporary_focus.asm` | `C1:9A11..C1:9B4E` | 317 | 317 | 0 | `5570c16e195fea7c2da046cafe7ced55a4fbdfc3` |
| `build-candidate` | `src/c1/c1_9b79_resolve_equipped_slot_for_item_subtype.asm` | `C1:9B79..C1:9CDD` | 356 | 356 | 0 | `e36e3d0a720f69fc97c43e4f25f44bb58e65b505` |
| `build-candidate` | `src/c1/c1_9cdd_initialize_equipment_comparison_markers_default.asm` | `C1:9CDD..C1:9D49` | 108 | 108 | 0 | `1b930ab0b502ee264c76a0c525f85f86bdf0c3b4` |
| `build-candidate` | `src/c1/c1_9d49_prepare_equipment_menu_status_display.asm` | `C1:9D49..C1:9EE6` | 413 | 413 | 0 | `46d05f16213959f1ee1d173eb84b134d788d45c4` |
| `build-candidate` | `src/c1/c1_9ee6_classify_item_compact_category.asm` | `C1:9EE6..C1:9F29` | 67 | 67 | 0 | `741379a1b5240e62d07424ed2ec51c95dc1f7667` |
| `build-candidate` | `src/c1/c1_9f29_render_selected_character_equipment_list.asm` | `C1:9F29..C1:A1D8` | 687 | 687 | 0 | `e68c89da31a1842699356bfb6febe527a0f69155` |
| `build-candidate` | `src/c1/c1_a1d8_render_equipment_preview_status.asm` | `C1:A1D8..C1:A778` | 1440 | 1440 | 0 | `2284e7fb9261354a0e49cdf59fef6a01fa31eb82` |
| `build-candidate` | `src/c1/c1_a795_run_character_equipment_slot_selection_loop.asm` | `C1:A795..C1:AA5D` | 712 | 712 | 0 | `d2c672982057ad9ee64c85c6a31ad9a42a087ed1` |
| `build-candidate` | `src/c1/c1_aa5d_run_party_equipment_menu_controller.asm` | `C1:AA5D..C1:AC4A` | 493 | 493 | 0 | `c5ca310c1e4d1a568071e44532e9911310a613b4` |
| `build-candidate` | `src/c1/c1_d08b_compute_level_up_stat_growth_delta.asm` | `C1:D08B..C1:D109` | 126 | 126 | 0 | `c19ae582d2e8b40e41bdd97a3bb49735ac5b36ad` |
| `build-candidate` | `src/c1/c1_d109_level_up_character_and_refresh_derived_stats.asm` | `C1:D109..C1:DC1C` | 2835 | 2835 | 0 | `854548288e521b942ab45ba896c2d094ea10b8bf` |
| `build-candidate` | `src/c1/c1_f616_open_or_refresh_sound_setting_selection.asm` | `C1:F616..C1:FF2C` | 2326 | 2326 | 0 | `b3da215d626e4adada2202c93385e0b881a5e566` |
| `build-candidate` | `src/c1/c1_adb4_determine_battle_targetting.asm` | `C1:ADB4..C1:B5B6` | 2050 | 2050 | 0 | `b1e00650d09cbbc7fd3b8a1f216f34a8a8967023` |
| `build-candidate` | `src/c1/c1_e4be_build_text_input_option_strip.asm` | `C1:E4BE..C1:EAD6` | 1560 | 1560 | 0 | `12645a95296f302b71d9aa9cc532fe7b640e222f` |
| `build-candidate` | `src/c1/c1_b5b6_open_battle_psi_user_selection.asm` | `C1:B5B6..C1:BB71` | 1467 | 1467 | 0 | `09e46606aa5591b3418e786084bb36ef8d17cdeb` |
| `build-candidate` | `src/c1/c1_dd9f_display_current_action_table_text_mode1.asm` | `C1:DD9F..C1:E1A2` | 1027 | 1027 | 0 | `5b30250364f21f400870628405c383e1faa6f2bc` |
| `build-candidate` | `src/c1/c1_c452_build_shared_battle_psi_entry_list.asm` | `C1:C452..C1:C853` | 1025 | 1025 | 0 | `d20480c57b57ec18a2c4214a28a0e1181bf4e743` |
| `build-candidate` | `src/c1/c1_cb7f_has_battle_psi_category_entries.asm` | `C1:CB7F..C1:CE85` | 774 | 774 | 0 | `97e82269d1ba42661e47962cccecd977a7d35413` |
| `build-candidate` | `src/c1/c1_c165_current_character_knows_psi.asm` | `C1:C165..C1:C452` | 749 | 749 | 0 | `3b473563e726787e8975995835ae88ffcdd6c036` |
| `build-candidate` | `src/c1/c1_ecd1_preview_packed_high_byte_window_flavour.asm` | `C1:ECD1..C1:F07E` | 941 | 941 | 0 | `40b4aee5a47e49d0c8524c11ec15b2d2990085ad` |
| `build-candidate` | `src/c1/c1_e1a2_null_far_callback.asm` | `C1:E1A2..C1:E48D` | 747 | 747 | 0 | `8f6916dba38d6439951eef9d339b37d246128893` |
| `build-candidate` | `src/c1/c1_bcab_execute_teleport_destination.asm` | `C1:BCAB..C1:BEFC` | 593 | 593 | 0 | `a3bb9def6f7284dd59a1d5a4d51a37fce5c47d4e` |
| `build-candidate` | `src/c1/c1_ead6_run_naming_buffer_commit_flow.asm` | `C1:EAD6..C1:EC8F` | 441 | 441 | 0 | `6e84f3b9b0e60f7e71a2e3b508a55372539d0dd3` |
| `build-candidate` | `src/c1/c1_f497_open_or_refresh_text_speed_selection.asm` | `C1:F497..C1:F616` | 383 | 383 | 0 | `e2b4f22aef6d3f14efe6dc503e9b45918e9b5a4d` |
| `build-candidate` | `src/c1/c1_f14f_open_copy_destination_menu.asm` | `C1:F14F..C1:F2A8` | 345 | 345 | 0 | `1dcebb151f16eee4ae936196a008486d2a8800a4` |
| `build-candidate` | `src/c1/c1_f07e_open_file_select_action_menu.asm` | `C1:F07E..C1:F14F` | 209 | 209 | 0 | `d7fd6582a82f85188188d1d62cf19e4fc2f920b5` |
| `build-candidate` | `src/c1/c1_ec8f_preview_window_flavour_and_redraw.asm` | `C1:EC8F..C1:ECD1` | 66 | 66 | 0 | `e790803938226d41ecfa7543f41701ea60d6ad72` |
| `build-candidate` | `src/c1/c1_f2a8_open_delete_file_confirmation_menu.asm` | `C1:F2A8..C1:F497` | 495 | 495 | 0 | `4cdf07888f87b0bf26451c298324d024eb3d6f3a` |
| `build-candidate` | `src/c1/c1_c8bc_format_battle_psi_menu_entry_row.asm` | `C1:C8BC..C1:CA06` | 330 | 330 | 0 | `0c1ed2f533f2727acd4553ab09c0ef9e63c0083b` |
| `build-candidate` | `src/c1/c1_befc_dispatch_text_command1_f41_special_event.asm` | `C1:BEFC..C1:C046` | 330 | 330 | 0 | `0a39edb1ea8b6457e4b0fac14965c016d5ac86af` |
| `build-candidate` | `src/c1/c1_c046_refresh_psi_menu_cursor_category.asm` | `C1:C046..C1:C165` | 287 | 287 | 0 | `3264bae8372b69c77154ec9f7f911739c703e19f` |
| `build-candidate` | `src/c1/c1_bb71_open_field_psi_destination_menu.asm` | `C1:BB71..C1:BCAB` | 314 | 314 | 0 | `227411a4ca092b17623f226d434b7d902dc67b71` |
| `build-candidate` | `src/c1/c1_ce85_resolve_selected_battle_item_action.asm` | `C1:CE85..C1:CFC6` | 321 | 321 | 0 | `af04c2b9affd01fa0c7d273181f7a483d326fb11` |
| `build-candidate` | `src/c1/c1_c853_resolve_battle_psi_targeting_metadata.asm` | `C1:C853..C1:C8BC` | 105 | 105 | 0 | `05e500a36fc92e7e4672509d9cbb547a357b8ff9` |
| `build-candidate` | `src/c1/c1_ca06_build_psi_rank_name.asm` | `C1:CA06..C1:CA72` | 108 | 108 | 0 | `0fda80ebe3a50ae6b0f274247df4b3ecb01eafe8` |
| `build-candidate` | `src/c1/c1_ca72_refresh_battle_psi_selection.asm` | `C1:CA72..C1:CAF5` | 131 | 131 | 0 | `c22a65232f46f1dfde357c7e2539758c2781d558` |
| `build-candidate` | `src/c1/c1_caf5_build_battle_psi_category_entry_list.asm` | `C1:CAF5..C1:CB7F` | 138 | 138 | 0 | `64b28a9934a429c8cb44a118d2602200cf46a35b` |
| `build-candidate` | `src/c1/c1_cfc6_open_battle_item_selection_loop.asm` | `C1:CFC6..C1:D038` | 114 | 114 | 0 | `fd19c1f73ce02069c0b3195d385bdc60b0046606` |
| `build-candidate` | `src/c1/c1_d038_map_broken_item_to_repaired_item.asm` | `C1:D038..C1:D08B` | 83 | 83 | 0 | `474851964a7cc48b08527829cd2571a6e36873bc` |
| `build-candidate` | `src/c1/c1_dc1c_display_battle_text_from_pointer.asm` | `C1:DC1C..C1:DC66` | 74 | 74 | 0 | `708b0501ec877e0cbaed78234ecd782025186920` |
| `build-candidate` | `src/c1/c1_dc66_display_battle_text_with_substitution_payload.asm` | `C1:DC66..C1:DCCB` | 101 | 101 | 0 | `950a389f2300186ef1fd2a4ec9755a615bfa2255` |
| `build-candidate` | `src/c1/c1_dccb_initialize_party_battle_start_state.asm` | `C1:DCCB..C1:DD3B` | 112 | 112 | 0 | `3ae598fa0583ec8e169fc1db8cc0ffc797fdea2d` |
| `build-candidate` | `src/c1/c1_ff99_compute_centered_text_layout_metric.asm` | `C1:FF99..C1:10000` | 103 | 103 | 0 | `4457178b89b69e639aa3db1a86e5b29c3349279e` |

## Source Segments

### `src/c1/c1_0000_run_text_display_setup_wrapper.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:0000..C1:0004` | 4 | `RunTextDisplaySetupWrapper` | `a5d859d705ea9593946d357a7ab686c37e674291` |

Labels:

- `C1:0000 RunTextDisplaySetupWrapper`

Evidence:

- `notes/text-engine-entry-waits-window-gates-c10000-c102d0.md`

### `src/c1/c1_0004_process_textbox_data_from_caller_pointer.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:0004..C1:004E` | 74 | `ProcessTextboxDataFromCallerPointerAndStateLatches` | `8b5ed13f249f9491055bb86633e177868b7d3214` |

Labels:

- `C1:0004 ProcessTextboxDataFromCallerPointerAndStateLatches`

Evidence:

- `notes/text-engine-entry-waits-window-gates-c10000-c102d0.md`
- `refs/earthbound-disasm-legacy/Earthbound Decomp/EB/Routine_Macros_EB.asm`

### `src/c1/c1_004e_pump_text_wait_frame.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:004E..C1:008E` | 64 | `PumpTextWaitFrameAndFocusHelpers` | `3c03a3da7cf562ee81735f188a567dc74915be85` |

Labels:

- `C1:004E PumpTextWaitFrameAndFocusHelpers`

Evidence:

- `notes/text-engine-entry-waits-window-gates-c10000-c102d0.md`

### `src/c1/c1_008e_close_and_drain_all_windows.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:008E..C1:00D6` | 72 | `CloseAndDrainAllWindowsAndInputLocks` | `678643d391d471a4144d1d2166f88558bea64a19` |

Labels:

- `C1:008E CloseAndDrainAllWindowsAndInputLocks`

Evidence:

- `notes/text-engine-entry-waits-window-gates-c10000-c102d0.md`
- `notes/text-command-family-18-windows-and-selection.md`

### `src/c1/c1_00d6_wait_text_ticks.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:00D6..C1:00FE` | 40 | `WaitTextTicks` | `b018c469eb83d7d62b5790d0b67a7ed01ac824a7` |

Labels:

- `C1:00D6 WaitTextTicks`

Evidence:

- `notes/text-engine-entry-waits-window-gates-c10000-c102d0.md`

### `src/c1/c1_00fe_wait_for_text_prompt_or_input_gate.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:00FE..C1:0166` | 104 | `WaitForTextPromptOrInputGate` | `1f2dda96ef66f5240883f0e525e2643958ea630b` |

Labels:

- `C1:00FE WaitForTextPromptOrInputGate`

Evidence:

- `notes/text-engine-entry-waits-window-gates-c10000-c102d0.md`
- `refs/earthbound-disasm-legacy/Earthbound Decomp/EB/Routine_Macros_EB.asm`

### `src/c1/c1_0166_run_text_halt_control_worker.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:0166..C1:02D0` | 362 | `RunTextHaltControlWorker` | `dafacf0fdccc6ec8dff9aac3b97f5002af406643` |

Labels:

- `C1:0166 RunTextHaltControlWorker`

Evidence:

- `notes/text-commands-13-and-14-halt-control.md`

### `src/c1/c1_02d0_wait_for_text_state_flag9641.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:02D0..C1:0301` | 49 | `WaitForTextStateFlag9641` | `d8e1be84c972ad1d1a169aed8a68b4bb7c314f37` |

Labels:

- `C1:02D0 WaitForTextStateFlag9641`

Evidence:

- `notes/text-engine-entry-waits-window-gates-c10000-c102d0.md`

### `src/c1/c1_0301_get_active_interaction_context_record.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:0301..C1:042E` | 301 | `GetActiveInteractionContextRecord` | `8ca4917c2435cd5cf66d60c11c6c101cb014aa85` |

Labels:

- `C1:0301 GetActiveInteractionContextRecord`

Evidence:

- `notes/interaction-context-and-event-flags.md`

### `src/c1/c1_042e_increment_current_text_context_workmem.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:042E..C1:045D` | 47 | `IncrementCurrentTextContextWorkmem` | `6139e06b5304c33312f0b8cc505c9c3f41d24e16` |

Labels:

- `C1:042E IncrementCurrentTextContextWorkmem`

Evidence:

- `notes/interaction-context-and-event-flags.md`

### `src/c1/c1_045d_install_primary_interaction_context_pointer.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:045D..C1:0489` | 44 | `InstallPrimaryInteractionContextPointer` | `b6c5d64a488b327efef82188ba55b8cae2eb24b2` |

Labels:

- `C1:045D InstallPrimaryInteractionContextPointer`

Evidence:

- `notes/interaction-context-and-event-flags.md`

### `src/c1/c1_0489_install_secondary_interaction_context_pointer.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:0489..C1:04B5` | 44 | `InstallSecondaryInteractionContextPointer` | `28e188e439ca906a889d8983e54f1c8809a9a833` |

Labels:

- `C1:0489 InstallSecondaryInteractionContextPointer`

Evidence:

- `notes/interaction-context-and-event-flags.md`

### `src/c1/c1_04b5_get_current_text_context_line_state.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:04B5..C1:078D` | 728 | `GetCurrentTextContextLineState` | `722e4541b18c500d78e6a2c994218173d4ca3287` |

Labels:

- `C1:04B5 GetCurrentTextContextLineState`

Evidence:

- `notes/interaction-context-and-event-flags.md`

### `src/c1/c1_078d_initialize_text_window_tilemap_staging.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:078D..C1:07AF` | 34 | `InitializeTextWindowTilemapStaging` | `aac284b123aa7cfcb778252046fed317cc3097db` |

Labels:

- `C1:078D InitializeTextWindowTilemapStaging`

Evidence:

- `notes/text-window-rendering-primitives-c1078d-c10d7c.md`

### `src/c1/c1_07af_build_window_tilemap_from_descriptor.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:07AF..C1:0A85` | 726 | `BuildWindowTilemapFromDescriptor` | `6ff65bdca5c19da8b98f35d4544ec438bac9d7ac` |

Labels:

- `C1:07AF BuildWindowTilemapFromDescriptor`

Evidence:

- `notes/text-window-rendering-primitives-c1078d-c10d7c.md`

### `src/c1/c1_0a85_write_glyph_to_window_descriptor_buffer.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:0A85..C1:0BA1` | 284 | `WriteGlyphToWindowDescriptorBuffer` | `e5e692407ff007130e54273a9b464b9ce7585793` |

Labels:

- `C1:0A85 WriteGlyphToWindowDescriptorBuffer`

Evidence:

- `notes/text-window-rendering-primitives-c1078d-c10d7c.md`

### `src/c1/c1_0ba1_print_glyph_to_active_window.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:0BA1..C1:0BFE` | 93 | `PrintGlyphToActiveWindow` | `30085841a009f84e60364760cfea6ed821dd9931` |

Labels:

- `C1:0BA1 PrintGlyphToActiveWindow`

Evidence:

- `notes/text-window-rendering-primitives-c1078d-c10d7c.md`

### `src/c1/c1_0bfe_create_pointer_backed_text_entry_record.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:0BFE..C1:0C49` | 75 | `CreatePointerBackedTextEntryRecord` | `8bfdd71da075744a4244a84739a182d756822cbd` |

Labels:

- `C1:0BFE CreatePointerBackedTextEntryRecord`

Evidence:

- `notes/text-window-rendering-primitives-c1078d-c10d7c.md`

### `src/c1/c1_0c49_count_text_entry_chain_records.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:0C49..C1:0C55` | 12 | `CountTextEntryChainRecordsAndMeasureLengthRedirects` | `e9fe278b649e32c343ddd376cfd3306456fcca1c` |

Labels:

- `C1:0C49 CountTextEntryChainRecordsAndMeasureLengthRedirects`

Evidence:

- `notes/text-window-rendering-primitives-c1078d-c10d7c.md`
- `notes/text-entry-record-builder-neighbors-c10f40-c11887.md`

### `src/c1/c1_0c55_format_number_from_caller_pointer.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:0C55..C1:0D60` | 267 | `FormatNumberFromCallerPointer` | `88c42900ff8e25c457646053b5ff057acda61653` |

Labels:

- `C1:0C55 FormatNumberFromCallerPointer`

Evidence:

- `notes/text-window-rendering-primitives-c1078d-c10d7c.md`

### `src/c1/c1_0d60_print_glyph_and_mark_window_redraw.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:0D60..C1:0D7C` | 28 | `PrintGlyphAndMarkWindowRedraw` | `d2d1346820d2353ed820311a33e040fec0a25317` |

Labels:

- `C1:0D60 PrintGlyphAndMarkWindowRedraw`

Evidence:

- `notes/text-window-rendering-primitives-c1078d-c10d7c.md`

### `src/c1/c1_0d7c_format_decimal_digits_to8960.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:0D7C..C1:0F40` | 452 | `FormatDecimalDigitsTo8960` | `b3f74bf406e93d84687c0dce165af67b7d7086b4` |

Labels:

- `C1:0D7C FormatDecimalDigitsTo8960`

Evidence:

- `notes/text-window-rendering-primitives-c1078d-c10d7c.md`

### `src/c1/c1_0f40_clear_window_content_by_focus_index.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:0F40..C1:134B` | 1035 | `ClearWindowContentByFocusIndex` | `a9c171e13b632ecf8e3ca9167cfa397d8d194f48` |

Labels:

- `C1:0F40 ClearWindowContentByFocusIndex`

Evidence:

- `notes/text-entry-record-builder-neighbors-c10f40-c11887.md`

### `src/c1/c1_134b_setup_text_display_with_wallet_status.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:134B..C1:138D` | 66 | `SetupTextDisplayWithWalletStatus` | `75e608219197f4ff0a38791e627a0556fb3d37b3` |

Labels:

- `C1:134B SetupTextDisplayWithWalletStatus`

Evidence:

- `notes/text-entry-record-builder-neighbors-c10f40-c11887.md`

### `src/c1/c1_138d_count_text_entry_chain_records_local.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:138D..C1:13D1` | 68 | `CountTextEntryChainRecordsLocal` | `0d61705ee6b873277d92142874ce3ff5ef73eeb3` |

Labels:

- `C1:138D CountTextEntryChainRecordsLocal`

Evidence:

- `notes/text-entry-record-builder-neighbors-c10f40-c11887.md`
- `notes/active-text-entry-chain-layout-c451fa.md`

### `src/c1/c1_13d1_install_text_entry_record.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:13D1..C1:14B1` | 224 | `InstallTextEntryRecord` | `5d00f83b53f4c08cafe6dfd35643e18492a1b386` |

Labels:

- `C1:13D1 InstallTextEntryRecord`

Evidence:

- `notes/text-entry-builder-c113d1-89d4.md`
- `notes/text-entry-record-builder-neighbors-c10f40-c11887.md`

### `src/c1/c1_14b1_create_text_entry_record_with_display_metadata.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:14B1..C1:153B` | 138 | `CreateTextEntryRecordWithDisplayMetadata` | `267968eab530f55a5b34b9eb3e77351d77090d07` |

Labels:

- `C1:14B1 CreateTextEntryRecordWithDisplayMetadata`

Evidence:

- `notes/text-entry-record-builder-neighbors-c10f40-c11887.md`

### `src/c1/c1_153b_create_typed_text_entry_record.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:153B..C1:1596` | 91 | `CreateTypedTextEntryRecord` | `3cac37d3c656fa9b395a02f9e23edcfc6ccdb807` |

Labels:

- `C1:153B CreateTypedTextEntryRecord`

Evidence:

- `notes/text-entry-record-builder-neighbors-c10f40-c11887.md`

### `src/c1/c1_1596_create_typed_text_entry_record_with_extra_byte.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:1596..C1:15F4` | 94 | `CreateTypedTextEntryRecordWithExtraByte` | `65694f3d023f56170aab36a79335e3e25fdb6670` |

Labels:

- `C1:1596 CreateTypedTextEntryRecordWithExtraByte`

Evidence:

- `notes/text-entry-record-builder-neighbors-c10f40-c11887.md`

### `src/c1/c1_15f4_create_typed_text_entry_record_direct.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:15F4..C1:17E2` | 494 | `CreateTypedTextEntryRecordDirect` | `b01d0b0ae86d74ed7fea2df84b3bb422573827fe` |

Labels:

- `C1:15F4 CreateTypedTextEntryRecordDirect`

Evidence:

- `notes/text-entry-record-builder-neighbors-c10f40-c11887.md`
- `notes/short-text-staging-buffer-9c9f.md`

### `src/c1/c1_17e2_measure_bounded_string_length.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:17E2..C1:180D` | 43 | `MeasureBoundedStringLength` | `5b7f97f7e39817b87ed8d9f08c8a4b1fe43ca36c` |

Labels:

- `C1:17E2 MeasureBoundedStringLength`

Evidence:

- `notes/text-window-rendering-primitives-c1078d-c10d7c.md`

### `src/c1/c1_180d_layout_active_text_entries_and_refresh.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:180D..C1:181B` | 14 | `LayoutActiveTextEntriesAndRefresh` | `f4c8b10b0f3fdfd2f60c3e601fe700bb363e672f` |

Labels:

- `C1:180D LayoutActiveTextEntriesAndRefresh`

Evidence:

- `notes/text-window-rendering-primitives-c1078d-c10d7c.md`

### `src/c1/c1_181b_select_active_text_entry_by_y.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:181B..C1:1887` | 108 | `SelectActiveTextEntryByY` | `ab32bfec56edffff8337b9f424c2898e7ef6153c` |

Labels:

- `C1:181B SelectActiveTextEntryByY`

Evidence:

- `notes/text-entry-record-builder-neighbors-c10f40-c11887.md`
- `notes/active-text-entry-chain-layout-c451fa.md`

### `src/c1/c1_1887_select_active_text_entry_by_a.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:1887..C1:1F8A` | 1795 | `SelectActiveTextEntryByA` | `679eb3c74881bc2412200686d839125d1edc8e2e` |

Labels:

- `C1:1887 SelectActiveTextEntryByA`

Evidence:

- `notes/text-entry-record-builder-neighbors-c10f40-c11887.md`
- `notes/active-text-entry-chain-layout-c451fa.md`
- `notes/text-command-family-1a-menus.md`

### `src/c1/c1_1f8a_clear_active_selection_prompt_scratch.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:1F8A..C1:1FBC` | 50 | `ClearActiveSelectionPromptScratch` | `f79cffb41852d058d90e0de82f82c4361174e6ce` |

Labels:

- `C1:1F8A ClearActiveSelectionPromptScratch`

Evidence:

- `notes/character-selection-prompt-cluster-c11f8a-c1242e.md`

### `src/c1/c1_1fbc_read_selection_prompt_candidate_byte.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:1FBC..C1:1FD4` | 24 | `ReadSelectionPromptCandidateByte` | `a8b1d5a249e38c749ecd16d73893c04ceb87d5bf` |

Labels:

- `C1:1FBC ReadSelectionPromptCandidateByte`

Evidence:

- `notes/bank-c1-working-name-proposals.md`

### `src/c1/c1_1fd4_is_selection_prompt_candidate_eligible.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:1FD4..C1:2012` | 62 | `IsSelectionPromptCandidateEligible` | `c2af7f1c0e7e0a97f7800b4f3f7d20258e7850e7` |

Labels:

- `C1:1FD4 IsSelectionPromptCandidateEligible`

Evidence:

- `notes/character-selection-prompt-cluster-c11f8a-c1242e.md`

### `src/c1/c1_2012_find_next_selection_prompt_candidate.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:2012..C1:2070` | 94 | `FindNextSelectionPromptCandidate` | `c705d06ac195a83310541455bc1a62390e1d700c` |

Labels:

- `C1:2012 FindNextSelectionPromptCandidate`

Evidence:

- `notes/character-selection-prompt-cluster-c11f8a-c1242e.md`

### `src/c1/c1_2070_find_previous_selection_prompt_candidate.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:2070..C1:20D6` | 102 | `FindPreviousSelectionPromptCandidate` | `ccc4f32808b89e38887ccb560fd5e7d7bd29d037` |

Labels:

- `C1:2070 FindPreviousSelectionPromptCandidate`

Evidence:

- `notes/character-selection-prompt-cluster-c11f8a-c1242e.md`

### `src/c1/c1_20d6_refresh_selection_prompt_candidate_text.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:20D6..C1:21B8` | 226 | `RefreshSelectionPromptCandidateText` | `9371f6ee3b662fecf4820559d0bae5840b340bfb` |

Labels:

- `C1:20D6 RefreshSelectionPromptCandidateText`

Evidence:

- `notes/character-selection-prompt-cluster-c11f8a-c1242e.md`

### `src/c1/c1_21b8_run_two_list_character_selection_prompt.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:21B8..C1:2362` | 426 | `RunTwoListCharacterSelectionPrompt` | `e868071c905abad0d9920f6e00cc8deb581c0c6b` |

Labels:

- `C1:21B8 RunTwoListCharacterSelectionPrompt`

Evidence:

- `notes/character-selection-prompt-cluster-c11f8a-c1242e.md`

### `src/c1/c1_2362_run_simple_side_selection_prompt.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:2362..C1:242E` | 204 | `RunSimpleSideSelectionPrompt` | `aeea32d272e4a8c391b93ac2b272aecf77d91396` |

Labels:

- `C1:2362 RunSimpleSideSelectionPrompt`

Evidence:

- `notes/character-selection-prompt-cluster-c11f8a-c1242e.md`

### `src/c1/c1_2bf3_print_debug_menu_title_words_with_ticks.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:2BF3..C1:2C36` | 67 | `PrintDebugMenuTitleWordsWithTicks` | `9bc16ff667923e1658a45458734657e8b44b58d3` |

Labels:

- `C1:2BF3 PrintDebugMenuTitleWordsWithTicks`

Evidence:

- `notes/debug-menu-window-tick-helpers-c12bf3-c12d17.md`

### `src/c1/c1_2c36_print_debug_menu_fixed_word_groups.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:2C36..C1:2CCC` | 150 | `PrintDebugMenuFixedWordGroups` | `0b905a67c7b92430ff52bd56e506895d83792470` |

Labels:

- `C1:2C36 PrintDebugMenuFixedWordGroups`

Evidence:

- `notes/debug-menu-window-tick-helpers-c12bf3-c12d17.md`

### `src/c1/c1_2ccc_format_debug_decimal_five_digits.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:2CCC..C1:2D17` | 75 | `FormatDebugDecimalFiveDigits` | `52098afd72d74552ea4ae40d380412d549e3b443` |

Labels:

- `C1:2CCC FormatDebugDecimalFiveDigits`

Evidence:

- `notes/debug-menu-window-tick-helpers-c12bf3-c12d17.md`

### `src/c1/c1_2d17_toggle_debug_meter_display_overlay.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:2D17..C1:2DD5` | 190 | `ToggleDebugMeterDisplayOverlay` | `e8cd50df20d614f0206b11b36c98ff95b4886cc2` |
| `C1:2DD5..C1:2E42` | 109 | `WindowTick` | `f1b1f57676da97746d6ad2874a09299c700e3153` |
| `C1:2E42..C1:2E63` | 33 | `LightWindowTick` | `3ca74265da363a4ea1e83c8216ee9996ad1e06b1` |
| `C1:2E63..C1:3187` | 804 | `DebugMenuSelectionDispatcher` | `f5d5a87d9c084a76d57e77208c76b8ab8f875169` |

Labels:

- `C1:2D17 ToggleDebugMeterDisplayOverlay`
- `C1:2DD5 WindowTick`
- `C1:2E42 LightWindowTick`
- `C1:2E63 DebugMenuSelectionDispatcher`

Evidence:

- `notes/debug-menu-window-tick-helpers-c12bf3-c12d17.md`
- `notes/text-command-1f41-special-event-dispatch-c1befc.md`

### `src/c1/c1_3187_resolve_primary_front_interaction_output.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:3187..C1:323B` | 180 | `ResolvePrimaryFrontInteractionOutput` | `492d69d0f7dd1882bcbdcec3c82deb342ffdd24b` |

Labels:

- `C1:3187 ResolvePrimaryFrontInteractionOutput`

Evidence:

- `notes/interaction-result-consumers.md`
- `notes/front-interaction-flow.md`

### `src/c1/c1_323b_resolve_secondary_facing_interaction_output.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:323B..C1:339E` | 355 | `ResolveSecondaryFacingInteractionOutput` | `f4f1a42f4e4914ff8f022d341b542e2b53a30ca7` |

Labels:

- `C1:323B ResolveSecondaryFacingInteractionOutput`

Evidence:

- `notes/interaction-result-consumers.md`
- `notes/front-interaction-flow.md`

### `src/c1/c1_339e_build_check_menu_entries_wrapper.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:339E..C1:33A7` | 9 | `BuildCheckMenuEntriesWrapper` | `e34f8f780c8fb99b738b7b01f7490fabff092049` |

Labels:

- `C1:339E BuildCheckMenuEntriesWrapper`

Evidence:

- `notes/open-menu-prelude-helpers-c1339e-c133b0.md`

### `src/c1/c1_33a7_build_open_menu_entries_wrapper.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:33A7..C1:33B0` | 9 | `BuildOpenMenuEntriesWrapper` | `19ec07343b65fa276bac468e6d569704a5634977` |

Labels:

- `C1:33A7 BuildOpenMenuEntriesWrapper`

Evidence:

- `notes/open-menu-prelude-helpers-c1339e-c133b0.md`

### `src/c1/c1_33b0_rebuild_open_menu_text_entry_records.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:33B0..C1:34A7` | 247 | `RebuildOpenMenuTextEntryRecords` | `9aff1b5763d6163e9649602e2df17c93dc624a36` |
| `C1:34A7..C1:3C32` | 1931 | `RunOpenMenuSelectionLoop` | `4bc8533c902fcc13e3fe3adf191595d35a74e06d` |
| `C1:3C32..C1:3CA1` | 111 | `HandlePlayerCheckingObject` | `3d3c5840276b1b45b3e0ba255a8a7077a17c04b6` |
| `C1:3CA1..C1:4012` | 881 | `OpenMenuButtonAndDebugMenuHelpers` | `8f04ad2eca0bf19f1b3deb61339957ef6fdbee08` |
| `C1:4012..C1:4049` | 55 | `AdvanceNameEntryLetterBoxPointer` | `4917ad3719bf72f9712c594e57d2f5637a6aead5` |
| `C1:4049..C1:4070` | 39 | `RetreatNameEntryLetterBoxPointer` | `6ce130df2f0e252a2f820e3c86a5a4be662bf950` |
| `C1:4070..C1:4103` | 147 | `ReadNameEntryLetterBoxPointer` | `1298bf44b0f71ad2f5478e651da40951e8632aa6` |

Labels:

- `C1:33B0 RebuildOpenMenuTextEntryRecords`
- `C1:34A7 RunOpenMenuSelectionLoop`
- `C1:3C32 HandlePlayerCheckingObject`
- `C1:3CA1 OpenMenuButtonAndDebugMenuHelpers`
- `C1:4012 AdvanceNameEntryLetterBoxPointer`
- `C1:4049 RetreatNameEntryLetterBoxPointer`
- `C1:4070 ReadNameEntryLetterBoxPointer`

Evidence:

- `notes/open-menu-prelude-helpers-c1339e-c133b0.md`
- `notes/interaction-result-consumers.md`
- `refs/earthbound-disasm-legacy/Earthbound Decomp/EB/Routine_Macros_EB.asm`

### `src/c1/c1_4103_build_text_command24_bit_jump_target.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:4103..C1:41D0` | 205 | `BuildTextCommand24BitJumpTarget` | `bac5ef8186135b1541d8674d5aec72a7304170e4` |

Labels:

- `C1:4103 BuildTextCommand24BitJumpTarget`

Evidence:

- `notes/text-command-0a-24bit-jump.md`

### `src/c1/c1_41d0_handle_text_command09_jump_multi.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:41D0..C1:4265` | 149 | `HandleTextCommand09JumpMulti` | `c85e53f17c21d90c57cb68f115cdc6025ed65dee` |

Labels:

- `C1:41D0 HandleTextCommand09JumpMulti`

Evidence:

- `notes/text-command-09-jump-multi.md`
- `notes/text-command-0a-24bit-jump.md`

### `src/c1/c1_4265_handle_text_command04_set_event_flag.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:4265..C1:42AD` | 72 | `HandleTextCommand04SetEventFlag` | `d94dead8106d8668d5e5f33a8b698966845d6cf9` |

Labels:

- `C1:4265 HandleTextCommand04SetEventFlag`

Evidence:

- `notes/text-command-04-set-event-flag.md`
- `notes/deferred-text-byte-queue-97ba-97ca.md`

### `src/c1/c1_42ad_handle_text_command05_clear_event_flag.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:42AD..C1:42F5` | 72 | `HandleTextCommand05ClearEventFlag` | `0e76518285a4fb80938b3fbe9667460198eb08b5` |

Labels:

- `C1:42AD HandleTextCommand05ClearEventFlag`

Evidence:

- `notes/text-command-05-clear-event-flag.md`
- `notes/deferred-text-byte-queue-97ba-97ca.md`

### `src/c1/c1_42f5_handle_text_command06_jump_if_flag_set.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:42F5..C1:435F` | 106 | `HandleTextCommand06JumpIfFlagSet` | `10e6288e84d6ff1b42bf65774299ea23bcb957f8` |

Labels:

- `C1:42F5 HandleTextCommand06JumpIfFlagSet`

Evidence:

- `notes/text-command-06-jump-if-flag-set.md`
- `notes/text-command-0a-24bit-jump.md`

### `src/c1/c1_435f_handle_text_command07_check_event_flag.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:435F..C1:43D6` | 119 | `HandleTextCommand07CheckEventFlag` | `143f89292ea9db3d081837decc7e5d82a6a913b1` |

Labels:

- `C1:435F HandleTextCommand07CheckEventFlag`

Evidence:

- `notes/text-command-07-check-event-flag.md`
- `notes/deferred-text-byte-queue-97ba-97ca.md`

### `src/c1/c1_43d6_build_call_text_far_pointer_and_dispatch.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:43D6..C1:44A3` | 205 | `BuildCallTextFarPointerAndDispatch` | `7dd9dad5af1dff00cc9a46faddd66676c59a9a32` |
| `C1:44A3..C1:4509` | 102 | `CreateNumberSelectorFromTextCommand` | `49aa7402a748d7cab4e971eb10b92456b7708c23` |
| `C1:4509..C1:4558` | 79 | `HandleTextCommand18ForceTextAlignment` | `60af5ae3ddda7f18211c5ad3850c222bd4acc56e` |

Labels:

- `C1:43D6 BuildCallTextFarPointerAndDispatch`
- `C1:44A3 CreateNumberSelectorFromTextCommand`
- `C1:4509 HandleTextCommand18ForceTextAlignment`

Evidence:

- `notes/text-command-08-call-text.md`
- `notes/text-command-family-18-windows-and-selection.md`
- `refs/earthbound-disasm-legacy/Earthbound Decomp/EB/Routine_Macros_EB.asm`

### `src/c1/c1_4558_handle_text_command0_btest_workmem_true.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:4558..C1:4591` | 57 | `HandleTextCommand0BTestWorkmemTrue` | `8e13a68e48efb2ae7b5ceb24ea65f365868c8af9` |

Labels:

- `C1:4558 HandleTextCommand0BTestWorkmemTrue`

Evidence:

- `notes/interaction-context-and-event-flags.md`

### `src/c1/c1_4591_handle_text_command0_ctest_workmem_false.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:4591..C1:45EF` | 94 | `HandleTextCommand0CTestWorkmemFalse` | `03ea9491c913ed147dcf7abb39402a8989c8a695` |

Labels:

- `C1:4591 HandleTextCommand0CTestWorkmemFalse`

Evidence:

- `notes/text-command-0c-parameterized-test-if-workmem-false.md`
- `notes/deferred-text-byte-queue-97ba-97ca.md`

### `src/c1/c1_45ef_handle_text_command0_dcopy_to_argmem.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:45EF..C1:461A` | 43 | `HandleTextCommand0DCopyToArgmem` | `3006d8346fa4571bb8f76d5c365e8e115f531711` |

Labels:

- `C1:45EF HandleTextCommand0DCopyToArgmem`

Evidence:

- `notes/interaction-context-and-event-flags.md`

### `src/c1/c1_461a_handle_text_command0_estore_to_argmem.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:461A..C1:463B` | 33 | `HandleTextCommand0EStoreToArgmem` | `b0fe64b89ba6ae9ca0d1fad8d04480aeeba958d7` |
| `C1:463B..C1:467D` | 66 | `BuildTextQueueSelector0` | `43ab107b7ab21c092bf3b39f9e96e506d22c1744` |
| `C1:467D..C1:46BF` | 66 | `BuildTextQueueSelector1` | `b5c78f6b24591bfdb300c60bc063ab3e35bb6323` |
| `C1:46BF..C1:4751` | 146 | `PrintItemNameTextCommandFamily` | `298bb760f196804ace1164774374f2bf2c8b64e5` |
| `C1:4751..C1:47A0` | 79 | `HandleTextCommand4751` | `40097ffa2241b7299a3d9196e159252f3ee67bbf` |
| `C1:47A0..C1:47AB` | 11 | `SetEventFlagFromTextArgument` | `322dafdd11611a982179b94054026c527e3f4f52` |
| `C1:47AB..C1:4819` | 110 | `CheckEventFlagFromTextArgument` | `10119f405add4ee3a9027b920fbbd5c69c6e873c` |

Labels:

- `C1:461A HandleTextCommand0EStoreToArgmem`
- `C1:463B BuildTextQueueSelector0`
- `C1:467D BuildTextQueueSelector1`
- `C1:46BF PrintItemNameTextCommandFamily`
- `C1:4751 HandleTextCommand4751`
- `C1:47A0 SetEventFlagFromTextArgument`
- `C1:47AB CheckEventFlagFromTextArgument`

Evidence:

- `notes/text-command-0e-parameterized-store-to-argmem.md`
- `notes/text-command-family-1a-menus.md`
- `notes/jeff-repair-item-name-bridge.md`
- `refs/earthbound-disasm-legacy/Earthbound Decomp/EB/Routine_Macros_EB.asm`

### `src/c1/c1_4819_read_statistic_selector_string_character.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:4819..C1:488C` | 115 | `ReadStatisticSelectorStringCharacter` | `5de06195f4ce3d8b56eafee9dd08089bfd637fd9` |
| `C1:488C..C1:48AC` | 32 | `PrintStatTextCommandHelper` | `ec94628354d6809dcb20598a72a3941d99a7f8a9` |

Labels:

- `C1:4819 ReadStatisticSelectorStringCharacter`
- `C1:488C PrintStatTextCommandHelper`

Evidence:

- `notes/statistic-selector-family-c4550f-c3ee7a.md`
- `notes/text-command-family-19-data-and-substitution.md`

### `src/c1/c1_48ac_test_current_item_compact_category.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:48AC..C1:48E9` | 61 | `TestCurrentItemCompactCategory` | `40ade1d6624db8f19f964826793ba4ae968d5e5f` |
| `C1:48E9..C1:494A` | 97 | `HandleTextCommand1D08` | `78cf3c3d90144385b12c62bd973153cb014325ac` |
| `C1:494A..C1:49B6` | 108 | `HandleTextCommand1D09` | `8bea8f634a6c2231364e6d52ca037ed0e15c761f` |
| `C1:49B6..C1:4A03` | 77 | `RecoverHpPercentTextCommand` | `e8328805e3627353702543da34e80693d168cd08` |
| `C1:4A03..C1:4A50` | 77 | `DepleteHpPercentTextCommand` | `647307b4ec40f2b585f98914bc8e5b161b4fcfbc` |
| `C1:4A50..C1:4A9D` | 77 | `RecoverHpAmountTextCommand` | `4e962343b7d1ad5f2879a0a30815c18b13aad144` |
| `C1:4A9D..C1:4AEA` | 77 | `DepleteHpAmountTextCommand` | `3a7c53156aff8f9d4c014f1ea60e93795cd3c577` |
| `C1:4AEA..C1:4B37` | 77 | `RecoverPpPercentTextCommand` | `b9bc046b098d39fe0c1ec17aef6d0423d13d7f59` |
| `C1:4B37..C1:4B84` | 77 | `DepletePpPercentTextCommand` | `8bb4b7ee7e043b5f09fafa3bf317e8293b283230` |
| `C1:4B84..C1:4BD1` | 77 | `RecoverPpAmountTextCommand` | `dd3458e166c27d757bc0a51d35cde5034257c224` |
| `C1:4BD1..C1:4C1E` | 77 | `DepletePpAmountTextCommand` | `3cc24d5b253004883dd213f800300e12367c7dc9` |
| `C1:4C1E..C1:4C86` | 104 | `GiveItemToCharacterTextCommand` | `ad0f2a0acdf15d98c63e35a37f4d6a39eb7d93c9` |
| `C1:4C86..C1:4CEE` | 104 | `TakeItemFromCharacterTextCommand` | `8043b2709c8f8448ffe2d20988a2bd9fab63b396` |

Labels:

- `C1:48AC TestCurrentItemCompactCategory`
- `C1:48E9 HandleTextCommand1D08`
- `C1:494A HandleTextCommand1D09`
- `C1:49B6 RecoverHpPercentTextCommand`
- `C1:4A03 DepleteHpPercentTextCommand`
- `C1:4A50 RecoverHpAmountTextCommand`
- `C1:4A9D DepleteHpAmountTextCommand`
- `C1:4AEA RecoverPpPercentTextCommand`
- `C1:4B37 DepletePpPercentTextCommand`
- `C1:4B84 RecoverPpAmountTextCommand`
- `C1:4BD1 DepletePpAmountTextCommand`
- `C1:4C1E GiveItemToCharacterTextCommand`
- `C1:4C86 TakeItemFromCharacterTextCommand`

Evidence:

- `notes/item-category-classifier-c19ee6.md`
- `notes/text-command-family-1d-inventory-money.md`
- `notes/text-command-family-1e-stat-recovery.md`
- `notes/hp-pp-adjust-helper-quartet-c18f0e-c19010.md`
- `notes/inventory-slot-search-removal-helper-c18e5b-c18ead.md`

### `src/c1/c1_4cee_find_party_member_with_inventory_room_for_text_command.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:4CEE..C1:4D24` | 54 | `FindPartyMemberWithInventoryRoomForTextCommand` | `f36d639bddde69284e0da8bb773f11bfd834c416` |
| `C1:4D24..C1:4D93` | 111 | `FindPartyMemberWithoutItemForTextCommand` | `cb4d89d7ec6ba15b246640c0fb1cc97bdf6122d9` |

Labels:

- `C1:4CEE FindPartyMemberWithInventoryRoomForTextCommand`
- `C1:4D24 FindPartyMemberWithoutItemForTextCommand`

Evidence:

- `notes/party-inventory-room-search-c456e4-c4572b.md`
- `notes/text-command-family-1d-inventory-money.md`

### `src/c1/c1_4d93_find_party_member_with_item_for_text_command.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:4D93..C1:4DFB` | 104 | `FindPartyMemberWithItemForTextCommand` | `bad440bd0e550b2d7f31ead3cbf385901da4782c` |
| `C1:4DFB..C1:4E8C` | 145 | `UseItemOnCharacterTextCommand` | `9449a6e1c0e657b2e28069d1b8959b687d5c098c` |
| `C1:4E8C..C1:4EAB` | 31 | `TeleportToPresetLocationTextCommand` | `3f57cd479ae53820373f7cf031a7046ce809cd4e` |

Labels:

- `C1:4D93 FindPartyMemberWithItemForTextCommand`
- `C1:4DFB UseItemOnCharacterTextCommand`
- `C1:4E8C TeleportToPresetLocationTextCommand`

Evidence:

- `notes/party-item-possession-search-c45637-c45683.md`
- `notes/text-command-family-1d-inventory-money.md`
- `refs/earthbound-disasm-legacy/Earthbound Decomp/EB/Routine_Macros_EB.asm`

### `src/c1/c1_4eab_handle_text_command10_parameterized_pause.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:4EAB..C1:4EB5` | 10 | `HandleTextCommand10ParameterizedPause` | `ae6238a2c4b96ac36d8d47abae767d32e44c190c` |
| `C1:4EB5..C1:4EF8` | 67 | `DisplayShopMenuTextCommand` | `14ef5774a6ab4b39475644a6e86fac8684bb66cd` |
| `C1:4EF8..C1:4F33` | 59 | `GetBuyPriceOfItemTextCommand` | `a5495a73ed95ac7e0916e1bcd02105cb199e4397` |
| `C1:4F33..C1:4F6F` | 60 | `GetSellPriceOfItemTextCommand` | `3d41940f9e44cfda48a5d61f4d3631084ded9ece` |
| `C1:4F6F..C1:4FD7` | 104 | `CheckDirectItemUseCompatibilityTextCommand` | `a2c9addf21f99862df5a72b2b055d0fa4a7cf963` |
| `C1:4FD7..C1:5007` | 48 | `PrintCharacterNameTextCommand` | `446063525e631aa8a12b2799b7d0d35cd8ab32cf` |
| `C1:5007..C1:506F` | 104 | `GetCharacterStatusByteTextCommand` | `be0ed4ee55e3e1d3b258421ce5b6d45897f2d513` |
| `C1:506F..C1:50E4` | 117 | `InflictStatusTextCommand` | `c645299910c0348eb62ecf923d85a1f85430cc6b` |
| `C1:50E4..C1:516B` | 135 | `CharacterHasAilmentTextCommand` | `a83e9faed141164c7264571a5ae653123d8bd471` |
| `C1:516B..C1:51FC` | 145 | `LoadSpecialTextSelector` | `b02ea389a9748f377311bbfe0b591bcffb783edd` |
| `C1:51FC..C1:528D` | 145 | `LoadSpecialForJumpMultiTextSelector` | `113d4e5e1e7774bec51e8a7ac081703369cc503c` |
| `C1:528D..C1:5384` | 247 | `CompareQueuedValueAgainstTextRegisterCommand` | `73f6470d3da3cc22522809f036abb501d61de13f` |
| `C1:5384..C1:53AF` | 43 | `GetExperienceNeededToLevelTextCommand` | `423d9cfde3c1bf19f9ab792613d44232d9ad0b0f` |
| `C1:53AF..C1:5494` | 229 | `PrintNumberTextCommand` | `e3bc5e8f583e17370252c060d0a31c9c7b959681` |
| `C1:5494..C1:549E` | 10 | `WaitForTextPromptOrInputGateTextCommand` | `d8bba368fbdbdda7a92e2c81953cd11ec02b42ec` |
| `C1:549E..C1:5529` | 139 | `DisplayInventoryMenuTextCommand` | `1cf5f651dd06b8c47fed36f9758b022a063a1b83` |
| `C1:5529..C1:554E` | 37 | `RunWindowRelativeSelectionNoCancelTextCommand` | `cdd4a761d614da4ed17b3457526b0e54e43cfc36` |
| `C1:554E..C1:5573` | 37 | `RunWindowRelativeSelectionTextCommand` | `0b04037c2f81cb6de5a54eab87761c167cade0e4` |
| `C1:5573..C1:5659` | 230 | `PrintMoneyAmountTextCommand` | `f1e265cb1adf83dc1975ce1e1e7cc6b50c12a887` |
| `C1:5659..C1:56DB` | 130 | `GiveItemToCharacterBTextCommand` | `93af579a93a30ed61c67fb66d79cf6859eef22dd` |
| `C1:56DB..C1:575D` | 130 | `RemoveInventoryItemBySlotTextCommand` | `8fdb83c5cdcbf75809873c2fead0827f5fe021da` |

Labels:

- `C1:4EAB HandleTextCommand10ParameterizedPause`
- `C1:4EB5 DisplayShopMenuTextCommand`
- `C1:4EF8 GetBuyPriceOfItemTextCommand`
- `C1:4F33 GetSellPriceOfItemTextCommand`
- `C1:4F6F CheckDirectItemUseCompatibilityTextCommand`
- `C1:4FD7 PrintCharacterNameTextCommand`
- `C1:5007 GetCharacterStatusByteTextCommand`
- `C1:506F InflictStatusTextCommand`
- `C1:50E4 CharacterHasAilmentTextCommand`
- `C1:516B LoadSpecialTextSelector`
- `C1:51FC LoadSpecialForJumpMultiTextSelector`
- `C1:528D CompareQueuedValueAgainstTextRegisterCommand`
- `C1:5384 GetExperienceNeededToLevelTextCommand`
- `C1:53AF PrintNumberTextCommand`
- `C1:5494 WaitForTextPromptOrInputGateTextCommand`
- `C1:549E DisplayInventoryMenuTextCommand`
- `C1:5529 RunWindowRelativeSelectionNoCancelTextCommand`
- `C1:554E RunWindowRelativeSelectionTextCommand`
- `C1:5573 PrintMoneyAmountTextCommand`
- `C1:5659 GiveItemToCharacterBTextCommand`
- `C1:56DB RemoveInventoryItemBySlotTextCommand`

Evidence:

- `notes/text-command-10-parameterized-pause.md`
- `notes/text-command-family-1a-menus.md`
- `notes/jeff-repair-item-name-bridge.md`
- `notes/text-command-family-19-data-and-substitution.md`
- `notes/text-command-family-18-windows-and-selection.md`
- `notes/text-command-family-1d-inventory-money.md`
- `refs/earthbound-disasm-legacy/Earthbound Decomp/EB/Routine_Macros_EB.asm`

### `src/c1/c1_575d_test_equipped_item_presence_for_text_command.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:575D..C1:57CD` | 112 | `TestEquippedItemPresenceForTextCommand` | `4f1ad477c35ebbc79284450200259db6ac6d6511` |
| `C1:57CD..C1:583D` | 112 | `CheckInventoryItemUsabilityTextCommand` | `044817eff849b1f5b1ed9a6dbaff8f2062b437e4` |
| `C1:583D..C1:58A5` | 104 | `CheckDeferredItemUseCompatibilityTextCommand` | `bff659506598a914bff43864ed6585876398067c` |
| `C1:58A5..C1:58FE` | 89 | `StoreInventoryItemWithEscargoTextCommand` | `93b83cde42a397d82793d48797820e6a2083a9bb` |
| `C1:58FE..C1:597F` | 129 | `WithdrawEscargoItemToInventoryTextCommand` | `9063e311502748ac8903a590e5ad4cfa9227a1dc` |
| `C1:597F..C1:59F9` | 122 | `ReadCharacterInventorySlotItemTextCommand` | `50e3006dc8625f81896e44e9860f7b79383d9454` |
| `C1:59F9..C1:5B0E` | 277 | `HaveEnoughMoneyTextCommand` | `386ceef5f4ece3fcdae1342763d9b02aedd65581` |
| `C1:5B0E..C1:5B46` | 56 | `ReadEscargoStorageItemTextCommand` | `0d6f0c580f299322ec61117ea701cbd2a625b6f9` |
| `C1:5B46..C1:5BA7` | 97 | `RunStatusWindowDisplayTextCommand` | `007461cc3e51da78b8a51d8283abaf12bfcc6c5c` |
| `C1:5BA7..C1:5BCA` | 35 | `PrintVerticalTextStringCommand` | `d9b0b378acf918ea9dbecc01cc33cce75a0a5f2a` |
| `C1:5BCA..C1:5C36` | 108 | `PutValueInArgmemTextCommand` | `6bfaa36dbce3de2fd12d334f2542f0e9889ce722` |
| `C1:5C36..C1:5C58` | 34 | `GetLoadedStringCountForWindowTextCommand` | `30cfa0dbc19b00070208cc9d66ff9a4686febe57` |
| `C1:5C58..C1:5C85` | 45 | `RunTextCommand1F71PartyUtility` | `df819a21bfdf08a70832eb0b9da4035623144972` |
| `C1:5C85..C1:5D6B` | 230 | `AddToAtmTextCommand` | `67d04f343a134028e66e72871fbd3383ef0cceac` |
| `C1:5D6B..C1:5E5C` | 241 | `TakeFromAtmTextCommand` | `0dc21ec19fa57cb125cebc9aa89fe5ef936f1402` |
| `C1:5E5C..C1:5F71` | 277 | `HaveEnoughMoneyInAtmTextCommand` | `03b72e7de6bc87d7b5f3079339ce26e4a819c962` |
| `C1:5F71..C1:5F91` | 32 | `AddToWalletTextCommand` | `06ab27af25e416cb257cba86786615bc3aa63e2c` |
| `C1:5F91..C1:5FF7` | 102 | `TakeFromWalletTextCommand` | `13107de1be8730c8277c581de9b67e83d811f757` |
| `C1:5FF7..C1:6080` | 137 | `QueueDeliveryOrPickupItemTextCommand` | `6500880ad0f9f0a8c19919b7a60cece658bbaaf0` |
| `C1:6080..C1:6124` | 164 | `ReadDeliveryOrPickupItemInfoTextCommand` | `3cd8ea5a1c2440c855293e2433648601b0ead445` |
| `C1:6124..C1:6143` | 31 | `AddItemToEscargoStorageTextCommand` | `bdc6e36a3401aa51d258beae3166ac81e0e0a928` |
| `C1:6143..C1:6172` | 47 | `ClassifyFoodItemTextCommand` | `6e078d10155c2979725369a9b2df5de6416ebd1d` |
| `C1:6172..C1:61D1` | 95 | `HaveXPartyMembersTextCommand` | `e6b6592f433d13fa4c9d48fbb1dea4802ea1bb23` |
| `C1:61D1..C1:61F0` | 31 | `PrintPsiNameTextCommand` | `e445e8a9ef6e3e78aab81d9cc89f4d1bcb76d6fc` |
| `C1:61F0..C1:621F` | 47 | `GenerateRandomNumberTextCommand` | `ccabe5f531ad34f9fd13c3d38a9d2e583d436a29` |

Labels:

- `C1:575D TestEquippedItemPresenceForTextCommand`
- `C1:57CD CheckInventoryItemUsabilityTextCommand`
- `C1:583D CheckDeferredItemUseCompatibilityTextCommand`
- `C1:58A5 StoreInventoryItemWithEscargoTextCommand`
- `C1:58FE WithdrawEscargoItemToInventoryTextCommand`
- `C1:597F ReadCharacterInventorySlotItemTextCommand`
- `C1:59F9 HaveEnoughMoneyTextCommand`
- `C1:5B0E ReadEscargoStorageItemTextCommand`
- `C1:5B46 RunStatusWindowDisplayTextCommand`
- `C1:5BA7 PrintVerticalTextStringCommand`
- `C1:5BCA PutValueInArgmemTextCommand`
- `C1:5C36 GetLoadedStringCountForWindowTextCommand`
- `C1:5C58 RunTextCommand1F71PartyUtility`
- `C1:5C85 AddToAtmTextCommand`
- `C1:5D6B TakeFromAtmTextCommand`
- `C1:5E5C HaveEnoughMoneyInAtmTextCommand`
- `C1:5F71 AddToWalletTextCommand`
- `C1:5F91 TakeFromWalletTextCommand`
- `C1:5FF7 QueueDeliveryOrPickupItemTextCommand`
- `C1:6080 ReadDeliveryOrPickupItemInfoTextCommand`
- `C1:6124 AddItemToEscargoStorageTextCommand`
- `C1:6143 ClassifyFoodItemTextCommand`
- `C1:6172 HaveXPartyMembersTextCommand`
- `C1:61D1 PrintPsiNameTextCommand`
- `C1:61F0 GenerateRandomNumberTextCommand`

Evidence:

- `notes/text-command-family-1d-inventory-money.md`
- `notes/text-command-family-19-data-and-substitution.md`
- `notes/text-command-family-18-windows-and-selection.md`
- `notes/jeff-repair-item-name-bridge.md`
- `notes/pending-item-queue-984b.md`
- `refs/earthbound-disasm-legacy/Earthbound Decomp/EB/Routine_Macros_EB.asm`

### `src/c1/c1_621f_finalize_text_command1_fc0_jump_multi2_target.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:621F..C1:6308` | 233 | `FinalizeTextCommand1FC0JumpMulti2Target` | `dec417db3adbea6a304dbc3e3a483e6586323d4b` |
| `C1:6308..C1:63A7` | 159 | `HandleTextCommand1FC0JumpMulti2` | `bba541810b16400960d8eebf79fbed34b288c8fa` |
| `C1:63A7..C1:63FD` | 86 | `RunJeffRepairBrokenItemCallback` | `7ba6cb0798f5bfda9d13e6992d83080e84299d3c` |
| `C1:63FD..C1:646E` | 113 | `HandleTextCommand1F13` | `fdd54ea4620fc60be4a31b1b8511d6a0c29b1542` |
| `C1:646E..C1:6490` | 34 | `HandleTextCommand1F14` | `4617c276119a05b80763829d46657918aea88c0f` |
| `C1:6490..C1:6509` | 121 | `HandleTextCommand1F16` | `5dcae591fe20b2d082176f017ea17fc91169173f` |
| `C1:6509..C1:6582` | 121 | `HandleTextCommand1F17` | `1863083430932568b4860bf69be451f9675f59b6` |
| `C1:6582..C1:65AA` | 40 | `HandleTextCommand1F18` | `9a38c1325119b0c7703fae4516554677e3a9d6e4` |
| `C1:65AA..C1:65D2` | 40 | `HandleTextCommand1F19` | `a279227f6d52a6c94ec6c5a45d333c5e4df7dec4` |
| `C1:65D2..C1:662A` | 88 | `HandleTextCommand1F1A` | `20c4b81a83691849ea6baa5535addd0122741a16` |
| `C1:662A..C1:666D` | 67 | `HandleTextCommand1F1B` | `0ec42e57d2f50c88d0d864f65ead906a4a80d307` |
| `C1:666D..C1:66DD` | 112 | `HandleTextCommand1F1C` | `9a10e4c1632976138eaeec04c62ba2aa300a019f` |
| `C1:66DD..C1:66FE` | 33 | `HandleTextCommand1F1D` | `4d4676f5378ece39b999f9f107907d2f2311e526` |
| `C1:66FE..C1:6744` | 70 | `HandleTextCommand1FE1` | `6a2987cdf978ae0d2e7db4e1317acec420459f30` |
| `C1:6744..C1:67D6` | 146 | `HandleTextCommand1F15` | `8c4a6a0eda7c75cd0df0cc017e88bd655f917d3b` |
| `C1:67D6..C1:683B` | 101 | `HandleTextCommand1F1E` | `ea0d4fa9dbf649ec27b16fd2c4995a94be6cffb1` |
| `C1:683B..C1:68A0` | 101 | `HandleTextCommand1F1F` | `09af5a44c3a2a54d89b7c105515d0f1ac44629ed` |
| `C1:68A0..C1:6947` | 167 | `ResolveFacingDirectionCommand22` | `57a04bf50dc8e7248837e5720b5b8e13d2187b44` |
| `C1:6947..C1:69F7` | 176 | `ResolveFacingDirectionCommand23` | `a26f8be6f9e8cb5135c02f258184a0d9ee92984c` |
| `C1:69F7..C1:6A01` | 10 | `HandleTextCommand1F62` | `d0e3fd6e8de1db53d883b520fbd00f4f45c58840` |
| `C1:6A01..C1:6A7B` | 122 | `SetCharacterLevelTextCommand` | `a4b74e27f2a8a8729aa6aa417d36a16504df289c` |
| `C1:6A7B..C1:6B2B` | 176 | `ResolveFacingDirectionCommand24` | `5ebc6362d654ca62a13927cce8d840eeeede1e98` |
| `C1:6B2B..C1:6BA4` | 121 | `HandleTextCommand1FE4` | `117c38f4a709b26c663838c9c390c7a3d8c63df7` |
| `C1:6BA4..C1:6BAF` | 11 | `HandleTextCommand1FE5` | `94f3325d68cc7942df05d27e05b3593b2f33e487` |
| `C1:6BAF..C1:6BF2` | 67 | `HandleTextCommand1FE6` | `b2f806abb0b36ff3f7612e571dc8e095e428de8e` |
| `C1:6BF2..C1:6C35` | 67 | `HandleTextCommand1FE7` | `de98594d95cb6f6f5eef2186a733894293342e86` |
| `C1:6C35..C1:6C40` | 11 | `HandleTextCommand1FE8` | `0e707cc278161c13eeb54d0fb8c9c91fdb046bad` |
| `C1:6C40..C1:6C83` | 67 | `HandleTextCommand1FE9` | `bdfad62c431f22ef3cdb9a11e469c3ca3f673ca4` |
| `C1:6C83..C1:6CC6` | 67 | `HandleTextCommand1FEA` | `a7c9eee9c6e6ecee8e4805fbf02cf209a3266e5a` |
| `C1:6CC6..C1:6D14` | 78 | `HandleTextCommand1FEB` | `6b5dab10786b4606c243446b3ff333a61e7b1781` |
| `C1:6D14..C1:6D62` | 78 | `HandleTextCommand1FEC` | `056b7667a1cd5264e9f623525b2e94a6cd1fa001` |
| `C1:6D62..C1:6DA5` | 67 | `HandleTextCommand1FEE` | `df02c248f1e18da09648b17b50649d79dececc6a` |
| `C1:6DA5..C1:6DE8` | 67 | `HandleTextCommand1FEF` | `78efab13258c2e115498d1578c39d3eb92cd91c0` |
| `C1:6DE8..C1:6EBF` | 215 | `HandleTextCommand1F63` | `ad1d3a5cc7b6dc947d564e5d82a27066fe46da54` |
| `C1:6EBF..C1:6F2F` | 112 | `HandleTextCommand1FF1` | `7d3565b771ac9dc531bdee87f83395cba759bc34` |
| `C1:6F2F..C1:6F9F` | 112 | `HandleTextCommand1FF2` | `b93d30d4e71e76701c9ad230a46b11ab738bf833` |
| `C1:6F9F..C1:6FD1` | 50 | `ClassifyCondimentItemTextCommand` | `d64a2ecba2496d4cca7415d272d1d374be3dcee8` |
| `C1:6FD1..C1:7058` | 135 | `HandleTextCommand1F23` | `e7cbdc89b19e75d81306a1adb7879234172bd311` |
| `C1:7058..C1:711C` | 196 | `CheckEscargoStorageStatusTextCommand` | `c527d2cb8566909a03812a4fb04a90664e1dc932` |
| `C1:711C..C1:7233` | 279 | `HandleTextCommand1F66` | `6bc6b5f2c99f7980652cb462af29b5e81ed76943` |
| `C1:7233..C1:7254` | 33 | `HandleTextCommand1F67` | `d082c2b4ac311dd044a950390087ae82b1927504` |
| `C1:7254..C1:7274` | 32 | `HandleTextCommand1F04` | `1f6599798409b090e6b9b4008d155e84e9a5eafb` |

Labels:

- `C1:621F FinalizeTextCommand1FC0JumpMulti2Target`
- `C1:6308 HandleTextCommand1FC0JumpMulti2`
- `C1:63A7 RunJeffRepairBrokenItemCallback`
- `C1:63FD HandleTextCommand1F13`
- `C1:646E HandleTextCommand1F14`
- `C1:6490 HandleTextCommand1F16`
- `C1:6509 HandleTextCommand1F17`
- `C1:6582 HandleTextCommand1F18`
- `C1:65AA HandleTextCommand1F19`
- `C1:65D2 HandleTextCommand1F1A`
- `C1:662A HandleTextCommand1F1B`
- `C1:666D HandleTextCommand1F1C`
- `C1:66DD HandleTextCommand1F1D`
- `C1:66FE HandleTextCommand1FE1`
- `C1:6744 HandleTextCommand1F15`
- `C1:67D6 HandleTextCommand1F1E`
- `C1:683B HandleTextCommand1F1F`
- `C1:68A0 ResolveFacingDirectionCommand22`
- `C1:6947 ResolveFacingDirectionCommand23`
- `C1:69F7 HandleTextCommand1F62`
- `C1:6A01 SetCharacterLevelTextCommand`
- `C1:6A7B ResolveFacingDirectionCommand24`
- `C1:6B2B HandleTextCommand1FE4`
- `C1:6BA4 HandleTextCommand1FE5`
- `C1:6BAF HandleTextCommand1FE6`
- `C1:6BF2 HandleTextCommand1FE7`
- `C1:6C35 HandleTextCommand1FE8`
- `C1:6C40 HandleTextCommand1FE9`
- `C1:6C83 HandleTextCommand1FEA`
- `C1:6CC6 HandleTextCommand1FEB`
- `C1:6D14 HandleTextCommand1FEC`
- `C1:6D62 HandleTextCommand1FEE`
- `C1:6DA5 HandleTextCommand1FEF`
- `C1:6DE8 HandleTextCommand1F63`
- `C1:6EBF HandleTextCommand1FF1`
- `C1:6F2F HandleTextCommand1FF2`
- `C1:6F9F ClassifyCondimentItemTextCommand`
- `C1:6FD1 HandleTextCommand1F23`
- `C1:7058 CheckEscargoStorageStatusTextCommand`
- `C1:711C HandleTextCommand1F66`
- `C1:7233 HandleTextCommand1F67`
- `C1:7254 HandleTextCommand1F04`

Evidence:

- `notes/text-command-1f-c0-jump-multi2-c1621f.md`
- `notes/text-command-family-1f-deferred-callbacks.md`
- `notes/text-command-family-19-data-and-substitution.md`
- `notes/text-command-family-1e-stat-recovery.md`
- `notes/text-command-family-1d-inventory-money.md`
- `notes/jeff-repair-item-name-bridge.md`
- `refs/earthbound-disasm-legacy/Earthbound Decomp/EB/Routine_Macros_EB.asm`

### `src/c1/c1_7274_stage_bank_deposit_accumulator_text_value.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:7274..C1:72BC` | 72 | `StageBankDepositAccumulatorTextValue` | `ce5394d8ecb47f9222508acbbc9f14f09881080d` |
| `C1:72BC..C1:72DA` | 30 | `HandleTextCommand1F40` | `748ea40329fe4f9c1288a6be6f5205a54489096c` |
| `C1:72DA..C1:7304` | 42 | `HandleTextCommand1F41` | `74b2eaed42833a9d6a64355a7dea259a7fa66ca8` |
| `C1:7304..C1:7325` | 33 | `HandleTextCommand1FD2` | `c2d8e862998f1b0e9b30975320f7db4155db6bb1` |
| `C1:7325..C1:737D` | 88 | `HandleTextCommand1FF3` | `c875931af5a9f0703b5301f36b2ef57f876096b7` |
| `C1:737D..C1:73C0` | 67 | `HandleTextCommand1FF4` | `0f0878f91c22bd202f2ec48693859f2b32b1155e` |
| `C1:73C0..C1:741F` | 95 | `StageBattleVisualEffectResultTextCommand` | `079313941f86866d076f1b475be641527b8ff10b` |
| `C1:741F..C1:7440` | 33 | `HandleTextCommand1F07` | `428e4a3f87ab86d2e572730d428a09bc726ecd5d` |

Labels:

- `C1:7274 StageBankDepositAccumulatorTextValue`
- `C1:72BC HandleTextCommand1F40`
- `C1:72DA HandleTextCommand1F41`
- `C1:7304 HandleTextCommand1FD2`
- `C1:7325 HandleTextCommand1FF3`
- `C1:737D HandleTextCommand1FF4`
- `C1:73C0 StageBattleVisualEffectResultTextCommand`
- `C1:741F HandleTextCommand1F07`

Evidence:

- `notes/bank-deposit-accumulator-98b9-98bb.md`
- `notes/text-command-family-1d-inventory-money.md`
- `notes/text-command-family-1f-deferred-callbacks.md`
- `notes/text-command-1f41-special-event-dispatch-c1befc.md`
- `notes/timed-event-callback-family-bank01.md`
- `notes/c3-battle-visual-effect-dispatch-source-contract-f981.md`
- `refs/earthbound-disasm-legacy/Earthbound Decomp/EB/Routine_Macros_EB.asm`
- `refs/community-earthbound-docs/Control_codes.txt`

### `src/c1/c1_7440_timed_delivery_row_selector_callback.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:7440..C1:744B` | 11 | `TimedDeliveryRowSelectorCallback` | `91c2ad7427f986e1ba33a67b755c7bd5ecb45e14` |
| `C1:744B..C1:7523` | 216 | `GiveExperienceTextCommand` | `4bb48717ef53c28ee668f0d277578f37ec23ba9d` |
| `C1:7523..C1:7584` | 97 | `BoostIqTextCommand` | `5f4cd0bf0a5a87441d1bb32a2edf0ddda7e3329a` |
| `C1:7584..C1:75E5` | 97 | `BoostGutsTextCommand` | `c72796038bab631a44d9410976a706770068649c` |
| `C1:75E5..C1:7646` | 97 | `BoostSpeedTextCommand` | `70b3a6d608e91157040f49f8eaf119f7be57e29e` |
| `C1:7646..C1:76A7` | 97 | `BoostVitalityTextCommand` | `0773b5a6f5e78eb14270df25a496488ce0d0b6e1` |
| `C1:76A7..C1:7708` | 97 | `BoostLuckTextCommand` | `fc77528d24318f56475b6d0171b087c193670bad` |

Labels:

- `C1:7440 TimedDeliveryRowSelectorCallback`
- `C1:744B GiveExperienceTextCommand`
- `C1:7523 BoostIqTextCommand`
- `C1:7584 BoostGutsTextCommand`
- `C1:75E5 BoostSpeedTextCommand`
- `C1:7646 BoostVitalityTextCommand`
- `C1:76A7 BoostLuckTextCommand`

Evidence:

- `notes/timed-event-slot-block-7440-and-c20abc.md`
- `notes/timed-delivery-row-index-command-1f-d3.md`
- `notes/timed-event-callback-family-bank01.md`
- `notes/text-command-family-1e-stat-recovery.md`
- `notes/equipped-item-derived-cache-family-c21857-c21e03.md`
- `refs/community-earthbound-docs/Control_codes.txt`
- `refs/earthbound-disasm-legacy/Earthbound Decomp/EB/Routine_Macros_EB.asm`

### `src/c1/c1_7708_classify_equipped_item_offensive_defensive.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:7708..C1:776A` | 98 | `ClassifyEquippedItemOffensiveDefensive` | `af363d52373033bbd26ccbef1e04013951e25f0f` |
| `C1:776A..C1:7796` | 44 | `StageStatisticSelectorValueTextCommand` | `3074c1ce39b59a18cc1b90ff9c613948ecf43815` |

Labels:

- `C1:7708 ClassifyEquippedItemOffensiveDefensive`
- `C1:776A StageStatisticSelectorValueTextCommand`

Evidence:

- `notes/offensive-defensive-item-check-c17708.md`
- `notes/text-command-family-1d-inventory-money.md`
- `notes/statistic-selector-family-c4550f-c3ee7a.md`
- `notes/text-command-family-19-data-and-substitution.md`
- `refs/community-earthbound-docs/Control_codes.txt`

### `src/c1/c1_7796_finalize_loaded_string_with_companion_pointer.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:7796..C1:7889` | 243 | `FinalizeLoadedStringWithCompanionPointer` | `db39cf8e55731f1eb17a100e0a48df28dcf8467a` |

Labels:

- `C1:7796 FinalizeLoadedStringWithCompanionPointer`

Evidence:

- `notes/text-command-load-string-pointer-c17796-c17889.md`
- `notes/text-command-family-19-data-and-substitution.md`
- `refs/earthbound-disasm-legacy/Earthbound Decomp/EB/Routine_Macros_EB.asm`

### `src/c1/c1_7889_continue_loaded_string_inline_collector.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:7889..C1:78F7` | 110 | `ContinueLoadedStringInlineCollector` | `a6512489cbf220df1dcbaaaa7137e7a8ef71b4de` |

Labels:

- `C1:7889 ContinueLoadedStringInlineCollector`

Evidence:

- `notes/text-command-load-string-pointer-c17796-c17889.md`
- `notes/text-command-family-19-data-and-substitution.md`
- `refs/earthbound-disasm-legacy/Earthbound Decomp/EB/Routine_Macros_EB.asm`

### `src/c1/c1_78f7_start_loaded_string_inline_collector.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:78F7..C1:7AE3` | 492 | `StartLoadedStringInlineCollector` | `857a2bc4962c79a994f641c03dfba6236cc87f93` |

Labels:

- `C1:78F7 StartLoadedStringInlineCollector`

Evidence:

- `notes/text-command-load-string-pointer-c17796-c17889.md`
- `notes/text-command-family-19-data-and-substitution.md`
- `refs/earthbound-disasm-legacy/Earthbound Decomp/EB/Routine_Macros_EB.asm`

### `src/c1/c1_7ae3_load_display_text_pointer_substitution_slot.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:7AE3..C1:7AF3` | 16 | `LoadDisplayTextPointerSubstitutionSlot` | `46f16391ed49a2aed4e71284ad3261e1740c3426` |

Labels:

- `C1:7AE3 LoadDisplayTextPointerSubstitutionSlot`

Evidence:

- `notes/class2-c1-display-text-substitution-handler-7af3.md`

### `src/c1/c1_7af3_load_display_text_byte_substitution_slot.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:7AF3..C1:7B0D` | 26 | `LoadDisplayTextByteSubstitutionSlot` | `95e5856f6ac87fdcc1a403f590a31289b8920d39` |

Labels:

- `C1:7AF3 LoadDisplayTextByteSubstitutionSlot`

Evidence:

- `notes/class2-c1-display-text-substitution-handler-7af3.md`

### `src/c1/c1_7b0d_load_display_text_mushroomized_selector_byte.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:7B0D..C1:7B56` | 73 | `LoadDisplayTextMushroomizedSelectorByte` | `333943af757b553092fac7f33c0fad5ee9001486` |

Labels:

- `C1:7B0D LoadDisplayTextMushroomizedSelectorByte`

Evidence:

- `notes/class2-c1-display-text-substitution-handler-7af3.md`

### `src/c1/c1_7b56_dispatch_display_text_dynamic_source_selector.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:7B56..C1:866D` | 2839 | `DispatchDisplayTextDynamicSourceSelector` | `11e2e2fb0cad350be15d0acf3005c15905d5d0ee` |

Labels:

- `C1:7B56 DispatchDisplayTextDynamicSourceSelector`

Evidence:

- `notes/display-text-dynamic-source-selector-dispatch-c17b56-c1866d.md`
- `notes/text-command-family-1a-menus.md`
- `notes/class2-c1-display-text-substitution-handler-7af3.md`

### `src/c1/c1_866d_initialize_managed_text_event_slot_front.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:866D..C1:869D` | 48 | `InitializeManagedTextEventSlotFront` | `4cbf6d189f9481ff6ece6c1128d9cf3917785a8f` |

Labels:

- `C1:866D InitializeManagedTextEventSlotFront`

Evidence:

- `notes/bank-c1-working-name-proposals.md`

### `src/c1/c1_869d_apply_active_managed_text_event_slot_snapshot.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:869D..C1:86B1` | 20 | `ApplyActiveManagedTextEventSlotSnapshot` | `994d598162289c5c6d5abbf369266b602de4deb1` |

Labels:

- `C1:869D ApplyActiveManagedTextEventSlotSnapshot`

Evidence:

- `notes/bank-c1-working-name-proposals.md`

### `src/c1/c1_91f8_withdraw_pending_item_to_inventory.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:91F8..C1:9216` | 30 | `WithdrawPendingItemToInventory` | `0cbe7a9e670945056b57189c07d600950ba0e009` |

Labels:

- `C1:91F8 WithdrawPendingItemToInventory`

Evidence:

- `notes/bank-c1-working-name-proposals.md`

### `src/c1/c1_9216_print_item_name_from_configuration_table.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:9216..C1:9249` | 51 | `PrintItemNameFromConfigurationTable` | `0e80da8de6afd0e20cb30c4ae4d70f30791b69d1` |

Labels:

- `C1:9216 PrintItemNameFromConfigurationTable`

Evidence:

- `notes/text-window-rendering-primitives-c1078d-c10d7c.md`

### `src/c1/c1_9b4e_build_equipment_comparison_markers_for_item.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:9B4E..C1:9B79` | 43 | `BuildEquipmentComparisonMarkersForItem` | `0bdf4a12841e97436ae88d34af2018907ccc5ea2` |

Labels:

- `C1:9B4E BuildEquipmentComparisonMarkersForItem`

Evidence:

- `notes/equipment-comparison-markers-9a1d.md`

### `src/c1/c1_a778_refresh_selected_character_equipment_display.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:A778..C1:A795` | 29 | `RefreshSelectedCharacterEquipmentDisplay` | `461c87932697ae13de762edceca15e00dc17f30c` |

Labels:

- `C1:A778 RefreshSelectedCharacterEquipmentDisplay`

Evidence:

- `notes/bank-c1-working-name-proposals.md`

### `src/c1/c1_ac4a_build_battle_attacker_name_buffer.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:AC4A..C1:AC9B` | 81 | `BuildBattleAttackerNameBuffer` | `4029d4d0db585f58a71bb574c1d37b38ddcbffc2` |

Labels:

- `C1:AC4A BuildBattleAttackerNameBuffer`

Evidence:

- `notes/battle-text-context-buffer-family-c1ac4a-ad42.md`
- `notes/battle-choice-text-family-c1b2ec-b997.md`

### `src/c1/c1_ac9b_get_battle_attacker_name_buffer_base.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:AC9B..C1:ACA1` | 6 | `GetBattleAttackerNameBufferBase` | `e5eecb34b2d04d492702c9d3a604823f8f33e4b7` |

Labels:

- `C1:AC9B GetBattleAttackerNameBufferBase`

Evidence:

- `notes/battle-text-context-buffer-family-c1ac4a-ad42.md`

### `src/c1/c1_aca1_build_battle_target_name_buffer.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:ACA1..C1:ACF2` | 81 | `BuildBattleTargetNameBuffer` | `3ebf541a990da4e46cf0a0fdde4afdf7510b7a27` |

Labels:

- `C1:ACA1 BuildBattleTargetNameBuffer`

Evidence:

- `notes/battle-text-context-buffer-family-c1ac4a-ad42.md`
- `notes/battle-choice-text-family-c1b2ec-b997.md`

### `src/c1/c1_acf2_get_battle_target_name_buffer_base.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:ACF2..C1:ACF8` | 6 | `GetBattleTargetNameBufferBase` | `fd547842b75297d0da7419a95b271200e7d70d8a` |

Labels:

- `C1:ACF2 GetBattleTargetNameBufferBase`

Evidence:

- `notes/battle-text-context-buffer-family-c1ac4a-ad42.md`

### `src/c1/c1_acf8_stage_battle_text_substitution_byte.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:ACF8..C1:AD02` | 10 | `StageBattleTextSubstitutionByte` | `72e72eb17175b873da1837029d2fb3237bbbdf2f` |

Labels:

- `C1:ACF8 StageBattleTextSubstitutionByte`

Evidence:

- `notes/battle-text-context-buffer-family-c1ac4a-ad42.md`
- `notes/class2-c1acf8-substitution-byte-family.md`

### `src/c1/c1_ad02_read_battle_text_substitution_byte.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:AD02..C1:AD0A` | 8 | `ReadBattleTextSubstitutionByte` | `da9946e6589ad8d9a3e97c8f62954ba17ab5f5e8` |

Labels:

- `C1:AD02 ReadBattleTextSubstitutionByte`

Evidence:

- `notes/battle-text-context-buffer-family-c1ac4a-ad42.md`
- `notes/class2-c1acf8-substitution-byte-family.md`

### `src/c1/c1_ad0a_stage_battle_text_substitution_pointer.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:AD0A..C1:AD26` | 28 | `StageBattleTextSubstitutionPointer` | `78aaaa34af0f0b508671a42833600dbd6eb93818` |

Labels:

- `C1:AD0A StageBattleTextSubstitutionPointer`

Evidence:

- `notes/battle-text-context-buffer-family-c1ac4a-ad42.md`

### `src/c1/c1_ad26_load_battle_text_substitution_pointer.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:AD26..C1:AD42` | 28 | `LoadBattleTextSubstitutionPointer` | `17e1629a0fa1f3f489e66107d50571c7bce19454` |

Labels:

- `C1:AD26 LoadBattleTextSubstitutionPointer`

Evidence:

- `notes/battle-text-context-buffer-family-c1ac4a-ad42.md`

### `src/c1/c1_ad42_get_front_interaction_result_class.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:AD42..C1:AD7D` | 59 | `GetFrontInteractionResultClass` | `1b6a47e2372ec3ee54feb02569913222798a73df` |

Labels:

- `C1:AD42 GetFrontInteractionResultClass`

Evidence:

- `notes/battle-text-context-buffer-family-c1ac4a-ad42.md`
- `notes/interaction-result-consumers.md`
- `notes/interaction-result-classes.md`

### `src/c1/c1_ad7d_read_overworld_position_context_byte.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:AD7D..C1:ADB4` | 55 | `ReadOverworldPositionContextByte` | `13a238f618edddd2dbeae85a1bd936f1f9e11bd8` |

Labels:

- `C1:AD7D ReadOverworldPositionContextByte`

Evidence:

- `notes/overworld-position-context-byte-c1ad7d.md`

### `src/c1/c1_dd3b_redirect_show_hppp_windows.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:DD3B..C1:DD41` | 6 | `RedirectShowHpppWindows` | `779e396c38703329e8bbd6d9b35276a61eec6c6d` |

Labels:

- `C1:DD3B RedirectShowHpppWindows`

Evidence:

- `notes/battle-text-entry-family-c1dc1c-dd7c.md`

### `src/c1/c1_dd41_redirect_hide_hppp_windows.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:DD41..C1:DD47` | 6 | `RedirectHideHpppWindows` | `71b34d46f6003d9213098e913e2fd01d9cefbfe4` |

Labels:

- `C1:DD41 RedirectHideHpppWindows`

Evidence:

- `notes/battle-text-entry-family-c1dc1c-dd7c.md`

### `src/c1/c1_dd47_redirect_create_window.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:DD47..C1:DD4D` | 6 | `RedirectCreateWindow` | `6f2699556c09f7541dd350944a41027fa073910d` |

Labels:

- `C1:DD47 RedirectCreateWindow`

Evidence:

- `notes/battle-text-entry-family-c1dc1c-dd7c.md`

### `src/c1/c1_dd4d_redirect_set_window_focus.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:DD4D..C1:DD53` | 6 | `RedirectSetWindowFocus` | `b2cb18b4ae8caf1260614a94dd43f3fe981d80c1` |

Labels:

- `C1:DD4D RedirectSetWindowFocus`

Evidence:

- `notes/battle-text-entry-family-c1dc1c-dd7c.md`

### `src/c1/c1_dd53_redirect_text_entry_helper0_fa3.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:DD53..C1:DD59` | 6 | `RedirectTextEntryHelper0FA3` | `3df60d84e743f988b4ad26be6001efd7c50f05a8` |

Labels:

- `C1:DD53 RedirectTextEntryHelper0FA3`

Evidence:

- `notes/battle-text-entry-family-c1dc1c-dd7c.md`

### `src/c1/c1_dd59_redirect_close_focus_window.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:DD59..C1:DD5F` | 6 | `RedirectCloseFocusWindow` | `e3dbc0ed43c864ff2ef2e151a8281ceb3f5bbba6` |

Labels:

- `C1:DD59 RedirectCloseFocusWindow`

Evidence:

- `notes/battle-text-entry-family-c1dc1c-dd7c.md`

### `src/c1/c1_dd5f_battle_display_close_and_sync_wait.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:DD5F..C1:DD70` | 17 | `BattleDisplayCloseAndSyncWait` | `b5ea12cdf7add591a34247f922b426dcad829d87` |

Labels:

- `C1:DD5F BattleDisplayCloseAndSyncWait`

Evidence:

- `notes/battle-text-entry-family-c1dc1c-dd7c.md`
- `notes/text-command-family-18-windows-and-selection.md`

### `src/c1/c1_dd70_redirect_build_battle_attacker_name_buffer.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:DD70..C1:DD76` | 6 | `RedirectBuildBattleAttackerNameBuffer` | `60665b618a3c2a8b2e183a46d8ae8867e9cfd142` |

Labels:

- `C1:DD70 RedirectBuildBattleAttackerNameBuffer`

Evidence:

- `notes/battle-text-entry-family-c1dc1c-dd7c.md`

### `src/c1/c1_dd76_redirect_build_battle_target_name_buffer.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:DD76..C1:DD7C` | 6 | `RedirectBuildBattleTargetNameBuffer` | `bd5cd95ee85cf5cfc5c7da61b0adbd3a66c160c4` |

Labels:

- `C1:DD76 RedirectBuildBattleTargetNameBuffer`

Evidence:

- `notes/battle-text-entry-family-c1dc1c-dd7c.md`

### `src/c1/c1_dd7c_redirect_stage_battle_text_substitution_byte.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:DD7C..C1:DD82` | 6 | `RedirectStageBattleTextSubstitutionByte` | `7cbfc4e4e84372d7afd1fd0bf4d2f3ad888719a7` |

Labels:

- `C1:DD7C RedirectStageBattleTextSubstitutionByte`

Evidence:

- `notes/battle-text-entry-family-c1dc1c-dd7c.md`

### `src/c1/c1_dd82_stage_battle_text_pointer_substitution_only.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:DD82..C1:DD9F` | 29 | `StageBattleTextPointerSubstitutionOnly` | `e71f8ee11bf3ee2e1984b98f1cc7de26e995acf6` |

Labels:

- `C1:DD82 StageBattleTextPointerSubstitutionOnly`

Evidence:

- `notes/battle-text-entry-tail-dd82-dd9f.md`
- `notes/battle-text-context-buffer-family-c1ac4a-ad42.md`

### `src/c1/c1_e48d_render_single_text_input_option_row_scoped.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:E48D..C1:E4BE` | 49 | `RenderSingleTextInputOptionRowScoped` | `0d6c39d2aa2a0636ab8b3d6fed86df0c977899e4` |

Labels:

- `C1:E48D RenderSingleTextInputOptionRowScoped`

Evidence:

- `notes/text-input-dialog-option-helpers-c1e48d-c1e4be.md`

### `src/c1/c1_ff2c_update_lead_entity_type_redraw_flag.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:FF2C..C1:FF6B` | 63 | `UpdateLeadEntityTypeRedrawFlag` | `df0b233c5cd5cf81e2b716b2a341000b4d400e3b` |

Labels:

- `C1:FF2C UpdateLeadEntityTypeRedrawFlag`

Evidence:

- `notes/file-select-tail-helpers-c1ff2c-ff6b-ff99.md`

### `src/c1/c1_ff6b_run_file_select_session.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:FF6B..C1:FF99` | 46 | `RunFileSelectSession` | `74a658f2c5fbdcff227873b796deff7a413d5559` |

Labels:

- `C1:FF6B RunFileSelectSession`

Evidence:

- `notes/bank-c1-working-name-proposals.md`

### `src/c1/c1_242e_dispatch_character_selection_prompt_mode.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:242E..C1:2BF3` | 1989 | `DispatchCharacterSelectionPromptMode` | `f4ec423087f9830f6ec26f2eb75bb00d6c40f88a` |

Labels:

- `C1:242E DispatchCharacterSelectionPromptMode`

Evidence:

- `notes/character-selection-prompt-cluster-c11f8a-c1242e.md`
- `notes/character-selection-prompt-dispatch-c1242e-c12bf3.md`

### `src/c1/c1_86b1_execute_nested_text_pointer.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:86B1..C1:87CC` | 283 | `ExecuteNestedTextPointer` | `2e7f0c5152c905a14c61c664a4e850661d94fb15` |

Labels:

- `C1:86B1 ExecuteNestedTextPointer`

Evidence:

- `notes/text-command-08-call-text.md:24 (Working Names)`
- `working-name metadata: status=working-name, confidence=proposed, tags=script, text`
- `notes/nested-text-pointer-and-callback-invoker-c186b1-c18b2c.md (Source promotion)`

### `src/c1/c1_87cc_invoke_text_engine_callback_low_word.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:87CC..C1:8B2C` | 864 | `InvokeTextEngineCallbackLowWord` | `f4714904318998cea84cc24052ee8e03afd1457e` |

Labels:

- `C1:87CC InvokeTextEngineCallbackLowWord`

Evidence:

- `notes/timed-event-callback-invoker-c187cc.md:15 (Working Names)`
- `working-name metadata: status=working-name, confidence=proposed, tags=text`
- `notes/nested-text-pointer-and-callback-invoker-c186b1-c18b2c.md (Source promotion)`

### `src/c1/c1_8b2c_insert_item_into_first_empty_inventory_slot.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:8B2C..C1:8BC6` | 154 | `InsertItemIntoFirstEmptyInventorySlot` | `3f1f8d255c40fd24f559eb20fb28360c8737697f` |

Labels:

- `C1:8B2C InsertItemIntoFirstEmptyInventorySlot`

Evidence:

- `notes/inventory-slot-insertion-helper-c18bc6.md`
- `notes/text-command-family-1d-inventory-money.md`
- `notes/teddy-bear-and-egg-item-cleanup-branches.md`

### `src/c1/c1_8bc6_insert_item_into_character_inventory.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:8BC6..C1:8C27` | 97 | `InsertItemIntoCharacterInventory` | `bbf5bd015ef316cd1c07e283bc807658d1144ad4` |

Labels:

- `C1:8BC6 InsertItemIntoCharacterInventory`

Evidence:

- `notes/inventory-slot-insertion-helper-c18bc6.md`
- `notes/text-command-family-1d-inventory-money.md`
- `notes/teddy-bear-and-egg-item-cleanup-branches.md`

### `src/c1/c1_8c27_remove_item_from_character_inventory_slot.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:8C27..C1:8E5B` | 564 | `RemoveItemFromCharacterInventorySlot` | `45b0a412abe0b59eae3a71e9e8076e4af4648743` |

Labels:

- `C1:8C27 RemoveItemFromCharacterInventorySlot`

Evidence:

- `notes/inventory-slot-removal-helper-c18c27.md`
- `notes/text-command-family-1d-inventory-money.md`
- `notes/teddy-bear-and-egg-item-cleanup-branches.md`
- `notes/equipment-slot-subtype-dispatch-c19066-c4577d.md`

### `src/c1/c1_8e5b_search_and_remove_item_from_character_inventory.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:8E5B..C1:8EAD` | 82 | `SearchAndRemoveItemFromCharacterInventory` | `e68b13b7369a7f3dab1efa57784d7e6f8df88499` |

Labels:

- `C1:8E5B SearchAndRemoveItemFromCharacterInventory`

Evidence:

- `notes/inventory-slot-search-removal-helper-c18e5b-c18ead.md`
- `notes/text-command-family-1d-inventory-money.md`

### `src/c1/c1_8ead_search_and_remove_item_from_active_inventories.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:8EAD..C1:8F0E` | 97 | `SearchAndRemoveItemFromActiveInventories` | `6f89fdec770c5f7801bf2fb98cd7c364ff3d9bb6` |

Labels:

- `C1:8EAD SearchAndRemoveItemFromActiveInventories`

Evidence:

- `notes/inventory-slot-search-removal-helper-c18e5b-c18ead.md`
- `notes/text-command-family-1d-inventory-money.md`

### `src/c1/c1_8f0e_deplete_hp_for_character_or_active_party.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:8F0E..C1:8F64` | 86 | `DepleteHpForCharacterOrActiveParty` | `22dfcf1ead6ace358f6005ebe61fad226bf50e02` |

Labels:

- `C1:8F0E DepleteHpForCharacterOrActiveParty`

Evidence:

- `notes/hp-pp-adjust-helper-quartet-c18f0e-c19010.md`
- `notes/text-command-family-1e-stat-recovery.md`
- `notes/c3-hp-pp-source-contract-quartet-ec1f-ee13.md`

### `src/c1/c1_8f64_recover_hp_for_character_or_active_party.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:8F64..C1:8FBA` | 86 | `RecoverHpForCharacterOrActiveParty` | `5b15128cb98cdce62a69a37d4224ef02cc8dd09e` |

Labels:

- `C1:8F64 RecoverHpForCharacterOrActiveParty`

Evidence:

- `notes/hp-pp-adjust-helper-quartet-c18f0e-c19010.md`
- `notes/text-command-family-1e-stat-recovery.md`
- `notes/c3-hp-pp-source-contract-quartet-ec1f-ee13.md`

### `src/c1/c1_8fba_deplete_pp_for_character_or_active_party.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:8FBA..C1:9010` | 86 | `DepletePpForCharacterOrActiveParty` | `d3bdf43fbe5ab289745d3e6e31e6b4ddd84c9d2c` |

Labels:

- `C1:8FBA DepletePpForCharacterOrActiveParty`

Evidence:

- `notes/hp-pp-adjust-helper-quartet-c18f0e-c19010.md`
- `notes/text-command-family-1e-stat-recovery.md`
- `notes/c3-hp-pp-source-contract-quartet-ec1f-ee13.md`

### `src/c1/c1_9010_recover_pp_for_character_or_active_party.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:9010..C1:9066` | 86 | `RecoverPpForCharacterOrActiveParty` | `3d09b08ffb112276dc7c5e9d4a2c2f4f12081874` |

Labels:

- `C1:9010 RecoverPpForCharacterOrActiveParty`

Evidence:

- `notes/hp-pp-adjust-helper-quartet-c18f0e-c19010.md`
- `notes/text-command-family-1e-stat-recovery.md`
- `notes/c3-hp-pp-source-contract-quartet-ec1f-ee13.md`

### `src/c1/c1_9066_dispatch_equipped_slot_subtype_update.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:9066..C1:90E6` | 128 | `DispatchEquippedSlotSubtypeUpdate` | `c0f098541c22a494cab3c7844f1d42796a6cb007` |

Labels:

- `C1:9066 DispatchEquippedSlotSubtypeUpdate`

Evidence:

- `notes/equipment-slot-subtype-dispatch-c19066-c4577d.md`
- `notes/inventory-slot-removal-helper-c18c27.md`
- `notes/equipment-preview-and-derived-state-cluster.md`

### `src/c1/c1_90e6_read_active_overworld_registry_type_code.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:90E6..C1:90F1` | 11 | `ReadActiveOverworldRegistryTypeCode` | `19f126bdb17fdbcd93c5499c672a142189676ba0` |
| `C1:90F1..C1:913D` | 76 | `CheckEscargoStorageQueueFull` | `3f20c7145aa34a5a9dfa5bfece81f8fed04bb7b3` |

Labels:

- `C1:90E6 ReadActiveOverworldRegistryTypeCode`
- `C1:90F1 CheckEscargoStorageQueueFull`

Evidence:

- `notes/overworld-registry-accessor-c190e6.md`
- `notes/text-command-family-1d-inventory-money.md`
- `notes/pending-item-queue-984b.md`

### `src/c1/c1_913d_enqueue_pending_item_id.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:913D..C1:9183` | 70 | `EnqueuePendingItemId` | `9af3ab076ac6e99e388dead6e486d0b73fb6f0d7` |
| `C1:9183..C1:91B0` | 45 | `StoreInventorySlotItemInPendingQueue` | `ac39cee06d4ec3949dcfbae0733354e16d08e1d5` |

Labels:

- `C1:913D EnqueuePendingItemId`
- `C1:9183 StoreInventorySlotItemInPendingQueue`

Evidence:

- `notes/pending-item-queue-984b.md`
- `notes/text-command-family-1d-inventory-money.md`
- `notes/inventory-slot-insertion-helper-c18bc6.md`
- `notes/inventory-slot-removal-helper-c18c27.md`

### `src/c1/c1_91b0_remove_pending_item_id_at_index.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:91B0..C1:91F8` | 72 | `RemovePendingItemIdAtIndex` | `46579dd1adcd2f5dbac68c24ee5a85bd58522aa8` |

Labels:

- `C1:91B0 RemovePendingItemIdAtIndex`

Evidence:

- `notes/pending-item-queue-984b.md`
- `notes/text-command-family-1d-inventory-money.md`

### `src/c1/c1_9249_print_statistic_selector_value.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:9249..C1:931B` | 210 | `PrintStatisticSelectorValue` | `1669edfe8918c7a9120997d3dec4fb1c8b7c7c59` |

Labels:

- `C1:9249 PrintStatisticSelectorValue`

Evidence:

- `notes/statistic-selector-family-c4550f-c3ee7a.md`
- `notes/text-command-family-19-data-and-substitution.md`

### `src/c1/c1_931b_print_psi_or_small_dynamic_label.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:931B..C1:93E7` | 204 | `PrintPsiOrSmallDynamicLabel` | `fcbaef42a7c8e720fb9a92e5c1d1966a8ba9b3b4` |

Labels:

- `C1:931B PrintPsiOrSmallDynamicLabel`

Evidence:

- `notes/item-psi-name-display-and-target-prompt-c19216-c19437.md`
- `notes/statistic-selector-family-c4550f-c3ee7a.md`

### `src/c1/c1_93e7_open_target_selection_prompt_label.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:93E7..C1:9437` | 80 | `OpenTargetSelectionPromptLabel` | `57e6955ccb173ca6352827716cc8cf3a76bda97b` |

Labels:

- `C1:93E7 OpenTargetSelectionPromptLabel`

Evidence:

- `notes/item-psi-name-display-and-target-prompt-c19216-c19437.md`
- `notes/c3-window-lifecycle-source-contract-e4ef-e6f7.md`

### `src/c1/c1_9437_close_target_selection_prompt_label.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:9437..C1:9441` | 10 | `CloseTargetSelectionPromptLabel` | `fc0d8724f97ce3f6065512986d8d456c570d5898` |
| `C1:9441..C1:952F` | 238 | `BuildPhoneContactSelectionMenu` | `b4f8c0dbc15e1f14aa21644d2e282e2d2aebdfe7` |
| `C1:952F..C1:98DE` | 943 | `RenderCharacterStatusWindowBlock` | `ad3bf621c7b287fdc6ed80ed4f7d8bf025c5315d` |
| `C1:98DE..C1:9A11` | 307 | `RenderCharacterInventoryOrEquipmentRows` | `ab093612a0707200da5a4e6f9bccc22f51ef53d7` |

Labels:

- `C1:9437 CloseTargetSelectionPromptLabel`
- `C1:9441 BuildPhoneContactSelectionMenu`
- `C1:952F RenderCharacterStatusWindowBlock`
- `C1:98DE RenderCharacterInventoryOrEquipmentRows`

Evidence:

- `notes/item-psi-name-display-and-target-prompt-c19216-c19437.md`
- `notes/text-command-family-1a-menus.md`
- `notes/text-command-family-18-windows-and-selection.md`
- `notes/equipment-menu-display-fringe-c19a11-c19f29.md`
- `notes/battle-item-action-selection-c1ce85-c1cfc6.md`
- `notes/open-menu-prelude-helpers-c1339e-c133b0.md`

### `src/c1/c1_9a11_run_selection_helper_with_temporary_focus.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:9A11..C1:9A43` | 50 | `RunSelectionHelperWithTemporaryFocus` | `b5dadb4f7171a3378de50120d95f3c18d3298410` |
| `C1:9A43..C1:9B4E` | 267 | `BuildEscargoStorageSelectionMenu` | `f051ff83e706225b9401347b020ec3ae288e2818` |

Labels:

- `C1:9A11 RunSelectionHelperWithTemporaryFocus`
- `C1:9A43 BuildEscargoStorageSelectionMenu`

Evidence:

- `notes/equipment-menu-display-fringe-c19a11-c19f29.md`
- `notes/text-command-family-1a-menus.md`
- `notes/pending-item-queue-984b.md`
- `notes/text-command-family-1d-inventory-money.md`

### `src/c1/c1_9b79_resolve_equipped_slot_for_item_subtype.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:9B79..C1:9CDD` | 356 | `ResolveEquippedSlotForItemSubtype` | `e36e3d0a720f69fc97c43e4f25f44bb58e65b505` |

Labels:

- `C1:9B79 ResolveEquippedSlotForItemSubtype`

Evidence:

- `notes/item-byte-19-packed-class-and-slot.md`
- `notes/equipment-comparison-markers-9a1d.md`
- `notes/equipment-slot-subtype-dispatch-c19066-c4577d.md`
- `notes/item-category-classifier-c19ee6.md`

### `src/c1/c1_9cdd_initialize_equipment_comparison_markers_default.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:9CDD..C1:9D49` | 108 | `InitializeEquipmentComparisonMarkersDefault` | `1b930ab0b502ee264c76a0c525f85f86bdf0c3b4` |

Labels:

- `C1:9CDD InitializeEquipmentComparisonMarkersDefault`

Evidence:

- `notes/equipment-comparison-markers-9a1d.md`
- `notes/equipment-menu-display-fringe-c19a11-c19f29.md`
- `notes/equipment-preview-and-derived-state-cluster.md`

### `src/c1/c1_9d49_prepare_equipment_menu_status_display.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:9D49..C1:9DB5` | 108 | `PrepareEquipmentMenuStatusDisplay` | `b6aa1a32446d62d81e40f246b1f90953171c6b54` |
| `C1:9DB5..C1:9EE6` | 305 | `RunShopItemSelectionMenu` | `65777b424de5107aa6e3715ed9e3c33b00c130a0` |

Labels:

- `C1:9D49 PrepareEquipmentMenuStatusDisplay`
- `C1:9DB5 RunShopItemSelectionMenu`

Evidence:

- `notes/equipment-menu-display-fringe-c19a11-c19f29.md`
- `notes/text-command-family-1a-menus.md`

### `src/c1/c1_9ee6_classify_item_compact_category.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:9EE6..C1:9F29` | 67 | `ClassifyItemCompactCategory` | `741379a1b5240e62d07424ed2ec51c95dc1f7667` |

Labels:

- `C1:9EE6 ClassifyItemCompactCategory`

Evidence:

- `notes/item-category-classifier-c19ee6.md`
- `notes/item-byte-19-packed-class-and-slot.md`

### `src/c1/c1_9f29_render_selected_character_equipment_list.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:9F29..C1:A1D8` | 687 | `RenderSelectedCharacterEquipmentList` | `e68c89da31a1842699356bfb6febe527a0f69155` |

Labels:

- `C1:9F29 RenderSelectedCharacterEquipmentList`

Evidence:

- `notes/equipment-menu-display-fringe-c19a11-c19f29.md`
- `notes/equipment-menu-top-level-flow-c1a778-c1aa5d.md`

### `src/c1/c1_a1d8_render_equipment_preview_status.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:A1D8..C1:A778` | 1440 | `RenderEquipmentPreviewStatus` | `2284e7fb9261354a0e49cdf59fef6a01fa31eb82` |

Labels:

- `C1:A1D8 RenderEquipmentPreviewStatus`

Evidence:

- `notes/equipment-preview-slot-block-9cd0-9cd6.md`
- `notes/equipment-preview-and-derived-state-cluster.md`
- `notes/equipment-menu-top-level-flow-c1a778-c1aa5d.md`

### `src/c1/c1_a795_run_character_equipment_slot_selection_loop.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:A795..C1:AA18` | 643 | `RunCharacterEquipmentSlotSelectionLoop` | `d2543bee81533ecfec36076714a0767a78487d71` |
| `C1:AA18..C1:AA5D` | 69 | `RefreshWalletOrStatusDisplay` | `dfca3ad0e4003e7c2ad0afa7d0d5793b259a4bd5` |

Labels:

- `C1:A795 RunCharacterEquipmentSlotSelectionLoop`
- `C1:AA18 RefreshWalletOrStatusDisplay`

Evidence:

- `notes/equipment-menu-top-level-flow-c1a778-c1aa5d.md`
- `notes/equipment-preview-slot-block-9cd0-9cd6.md`
- `notes/text-entry-record-builder-neighbors-c10f40-c11887.md`

### `src/c1/c1_aa5d_run_party_equipment_menu_controller.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:AA5D..C1:AAFA` | 157 | `RunPartyEquipmentMenuController` | `39660688753fade3c4e91a4e8cd4f170b9cb3f52` |
| `C1:AAFA..C1:AC00` | 262 | `RunTeleportDestinationSelectionMenu` | `243d50c1821a2f6a6246c7dfbdf8090e36b1c35d` |
| `C1:AC00..C1:AC4A` | 74 | `OpenPhoneContactSelectionMenu` | `9a21bef1b71cef109f366bd3868a402503ea2b58` |

Labels:

- `C1:AA5D RunPartyEquipmentMenuController`
- `C1:AAFA RunTeleportDestinationSelectionMenu`
- `C1:AC00 OpenPhoneContactSelectionMenu`

Evidence:

- `notes/equipment-menu-top-level-flow-c1a778-c1aa5d.md`
- `notes/text-command-family-1a-menus.md`
- `notes/teleport-menu-wrapper-c1bb71-bcab.md`

### `src/c1/c1_d08b_compute_level_up_stat_growth_delta.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:D08B..C1:D109` | 126 | `ComputeLevelUpStatGrowthDelta` | `c19ae582d2e8b40e41bdd97a3bb49735ac5b36ad` |

Labels:

- `C1:D08B ComputeLevelUpStatGrowthDelta`

Evidence:

- `notes/level-up-stat-growth-helper-c1d08b.md`
- `notes/bank-c1-subsystem-and-symbol-synthesis.md`

### `src/c1/c1_d109_level_up_character_and_refresh_derived_stats.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:D109..C1:D15B` | 82 | `LevelUpCharacterAndRefreshDerivedStats` | `400957bef9b3380b8f10e4b8764db181920325de` |
| `C1:D15B..C1:D204` | 169 | `BuildLevelUpTargetNameAndAnnouncement` | `08feee56facb0ca270912bd305af35769db4482e` |
| `C1:D204..C1:D28C` | 136 | `PrintOffenseGainMessage` | `1dbadf077f76083ddc016a4b1ddbe99e73e1b369` |
| `C1:D28C..C1:D31B` | 143 | `PrintDefenseGainMessage` | `b119dd55a3d05b25e7db251a8ee70f930d1e3ebf` |
| `C1:D31B..C1:D3A5` | 138 | `PrintSpeedGainMessage` | `825dfa6efa252bc2266947a959d83e3430a69bed` |
| `C1:D3A5..C1:D48D` | 232 | `PrintGutsGainMessage` | `99cb433c75d95f9771b68e9e36dcd1c8419bfcb6` |
| `C1:D48D..C1:D575` | 232 | `PrintVitalityGainMessage` | `308007c4176c372f9b49ab4f9e9d6d070f9c263f` |
| `C1:D575..C1:D606` | 145 | `PrintIqGainMessage` | `1b095b2f8cf83118e28c3ae1dd3a21218db02d46` |
| `C1:D606..C1:D695` | 143 | `PrintLuckGainMessage` | `336c271b892bb62ef5aec39482f5c3570116b66e` |
| `C1:D695..C1:D76D` | 216 | `PrintMaximumHpGainMessage` | `f1efe27123f6c5b4e18a73c94961aa7db63f31fb` |
| `C1:D76D..C1:DC1C` | 1199 | `PrintMaximumPpGainMessage` | `6cb867697ba2b233e26b7d536192565d21fef484` |

Labels:

- `C1:D109 LevelUpCharacterAndRefreshDerivedStats`
- `C1:D15B BuildLevelUpTargetNameAndAnnouncement`
- `C1:D204 PrintOffenseGainMessage`
- `C1:D28C PrintDefenseGainMessage`
- `C1:D31B PrintSpeedGainMessage`
- `C1:D3A5 PrintGutsGainMessage`
- `C1:D48D PrintVitalityGainMessage`
- `C1:D575 PrintIqGainMessage`
- `C1:D606 PrintLuckGainMessage`
- `C1:D695 PrintMaximumHpGainMessage`
- `C1:D76D PrintMaximumPpGainMessage`

Evidence:

- `notes/level-up-stat-growth-helper-c1d08b.md`
- `notes/level-up-stat-gain-text-family-c1d15b-d76d.md`
- `notes/equipped-item-derived-cache-family-c21857-c21e03.md`

### `src/c1/c1_f616_open_or_refresh_sound_setting_selection.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:F616..C1:F6E3` | 205 | `OpenOrRefreshSoundSettingSelection` | `4c0e3ca0b2e1192a309c66c0e07987b8e01a007d` |
| `C1:F6E3..C1:F805` | 290 | `OpenOrRefreshWindowFlavourSelection` | `5ae532eac699b39b75742810cecde1af88d62637` |
| `C1:F805..C1:FF2C` | 1831 | `RunFileSelectMenuLoop` | `f68ed6d9ad4d8e6582ed1556c6707592287f8781` |

Labels:

- `C1:F616 OpenOrRefreshSoundSettingSelection`
- `C1:F6E3 OpenOrRefreshWindowFlavourSelection`
- `C1:F805 RunFileSelectMenuLoop`

Evidence:

- `notes/file-select-setup-option-menus-c1f497-c1f616.md`
- `notes/file-select-tail-helpers-c1ff2c-ff6b-ff99.md`
- `notes/bank-c1-subsystem-and-symbol-synthesis.md`

### `src/c1/c1_adb4_determine_battle_targetting.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:ADB4..C1:AF73` | 447 | `DetermineBattleTargetting` | `8e589024423e667d1007dc6773df3988180259b7` |
| `C1:AF73..C1:B2EC` | 889 | `UseItemBattleOrFieldBridge` | `40065bc53d409c3029247381bffb219c595fc0d1` |
| `C1:B2EC..C1:B450` | 356 | `BuildBattleActionChoiceTextFromActionRow` | `5c52331ef997d33e360c06279945e37a23384529` |
| `C1:B450..C1:B5B6` | 358 | `BuildBattleActionTargetChoiceText` | `d6f115e69976ce1859832b5f51b60674cbaeb222` |

Labels:

- `C1:ADB4 DetermineBattleTargetting`
- `C1:AF73 UseItemBattleOrFieldBridge`
- `C1:B2EC BuildBattleActionChoiceTextFromActionRow`
- `C1:B450 BuildBattleActionTargetChoiceText`

Evidence:

- `notes/battle-targetting-resolver-c1adb4-af50.md`
- `notes/battle-choice-text-family-c1b2ec-b997.md`
- `refs/ebsrc-main/ebsrc-main/src/battle/determine_targetting.asm`

### `src/c1/c1_e4be_build_text_input_option_strip.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:E4BE..C1:E57F` | 193 | `BuildTextInputOptionStrip` | `7426d4b9416bc277bd8fd45c240cd8bcb7d48ab4` |
| `C1:E57F..C1:EAA6` | 1319 | `RunTextInputDialog` | `41bf4f8864ba32de89f40fa4083321722517bc06` |
| `C1:EAA6..C1:EAD6` | 48 | `RunNameEntrySpecialEventPrelude` | `3f74ca626aa550f7c180a1d726691bc2332c068d` |

Labels:

- `C1:E4BE BuildTextInputOptionStrip`
- `C1:E57F RunTextInputDialog`
- `C1:EAA6 RunNameEntrySpecialEventPrelude`

Evidence:

- `notes/text-input-dialog-option-helpers-c1e48d-c1e4be.md`
- `notes/text-command-1f41-special-event-dispatch-c1befc.md`
- `notes/naming-buffer-commit-family-c1ead6-c4d065.md`

### `src/c1/c1_b5b6_open_battle_psi_user_selection.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:B5B6..C1:B7C6` | 528 | `OpenBattlePsiUserSelection` | `704a82cfe4e003a1aac32bc0f20a6f9e98285d5f` |
| `C1:B7C6..C1:B850` | 138 | `WriteSelectedPsiActionIntoBattleSelection` | `e9463580b235440b652bd6f74114b546fa7d09a0` |
| `C1:B850..C1:B997` | 327 | `BuildPsiSelectionSnapshotAndText` | `23c8e0020105a913bef2e9b1619e934d44d0ddd7` |
| `C1:B997..C1:BB06` | 367 | `DisplayBattlePsiActionText` | `2b54bb2cba242a31ceeb9dd8ec1e85936d8fb588` |
| `C1:BB06..C1:BB71` | 107 | `FinalizeBattlePsiSelectionState` | `e667bdb77e632cca3830defe343bb7d4572c6736` |

Labels:

- `C1:B5B6 OpenBattlePsiUserSelection`
- `C1:B7C6 WriteSelectedPsiActionIntoBattleSelection`
- `C1:B850 BuildPsiSelectionSnapshotAndText`
- `C1:B997 DisplayBattlePsiActionText`
- `C1:BB06 FinalizeBattlePsiSelectionState`

Evidence:

- `notes/battle-psi-user-selection-front-end-c1b5b6-b7c6.md`
- `notes/battle-choice-text-family-c1b2ec-b997.md`
- `notes/battle-selection-snapshot-export-c2b930.md`
- `refs/ebsrc-main/ebsrc-main/src/battle/battle_psi_menu_redirect.asm`

### `src/c1/c1_dd9f_display_current_action_table_text_mode1.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:DD9F..C1:DDC6` | 39 | `DisplayCurrentActionTableTextMode1` | `a9879a38e5db08e289f00b1f9a86e7e87b77dbde` |
| `C1:DDC6..C1:DDCC` | 6 | `RedirectRemoveItemFromInventory` | `743ed81a7a6c0ea3e5edf27d0fa61e88053cbae8` |
| `C1:DDCC..C1:DDD3` | 7 | `RedirectC43573Helper` | `4b07ecc854b3055fdcc37bc5d77efcf3f301723d` |
| `C1:DDD3..C1:DDDA` | 7 | `RedirectC3E6F8Helper` | `d9600aaa137db6f3baeff6607287316297274796` |
| `C1:DDDA..C1:E1A2` | 968 | `BuildSelectionMenuSetupAndRedirects` | `03d89ab8b09d779bd5f2374ca21895ee90e1d48a` |

Labels:

- `C1:DD9F DisplayCurrentActionTableTextMode1`
- `C1:DDC6 RedirectRemoveItemFromInventory`
- `C1:DDCC RedirectC43573Helper`
- `C1:DDD3 RedirectC3E6F8Helper`
- `C1:DDDA BuildSelectionMenuSetupAndRedirects`

Evidence:

- `notes/battle-text-entry-tail-dd82-dd9f.md`
- `notes/battle-text-display-mode-latch-964d.md`
- `notes/class2-battle-text-cluster-overview.md`
- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank01.asm`

### `src/c1/c1_c452_build_shared_battle_psi_entry_list.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:C452..C1:C853` | 1025 | `BuildSharedBattlePsiEntryList` | `d20480c57b57ec18a2c4214a28a0e1181bf4e743` |

Labels:

- `C1:C452 BuildSharedBattlePsiEntryList`

Evidence:

- `notes/battle-psi-category-list-family-c1caf5-c1cb7f.md`
- `notes/battle-psi-menu-metadata-family-c1c853-c1c8bc.md`
- `notes/battle-psi-menu-table-helpers-c1c046-c1c165.md`

### `src/c1/c1_cb7f_has_battle_psi_category_entries.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:CB7F..C1:CBCD` | 78 | `HasBattlePsiCategoryEntries` | `1fdd43b98efc8236a21f4da561b5e90cdbb5d701` |
| `C1:CBCD..C1:CC39` | 108 | `OpenBattlePsiCategorySelectionStage` | `37fae7b1b6ca5aa1060c38c43ca7f2badcffebce` |
| `C1:CC39..C1:CE73` | 570 | `OpenBattlePsiMenuController` | `819912fdfc41a54e21b3f69b2e248271d6ba3832` |
| `C1:CE73..C1:CE85` | 18 | `ExitBattlePsiMenuController` | `20cc790394e1688b62e69dbbeb54e7d053b01b0b` |

Labels:

- `C1:CB7F HasBattlePsiCategoryEntries`
- `C1:CBCD OpenBattlePsiCategorySelectionStage`
- `C1:CC39 OpenBattlePsiMenuController`
- `C1:CE73 ExitBattlePsiMenuController`

Evidence:

- `notes/battle-psi-category-list-family-c1caf5-c1cb7f.md`
- `notes/battle-psi-menu-controller-c1cc39-ce73.md`
- `notes/battle-psi-menu-metadata-family-c1c853-c1c8bc.md`

### `src/c1/c1_c165_current_character_knows_psi.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:C165..C1:C1BA` | 85 | `CurrentCharacterKnowsPsi` | `f11827bbc8da6a5b0d115db3cdd617be4608123e` |
| `C1:C1BA..C1:C32A` | 368 | `HasPsiEntryForCategoryMask` | `758001c9a2195821626e669458ed2ba4b98d7354` |
| `C1:C32A..C1:C367` | 61 | `CanCharacterOpenPsiLane` | `013a33abfbfa891a254d0420e3185d7da4c12a5a` |
| `C1:C367..C1:C373` | 12 | `CheckBattlePsiUserEligibility` | `0beaa6480bba1cdca0cee8cdfec532e90f9fa79f` |
| `C1:C373..C1:C3B6` | 67 | `FindFirstEligibleBattlePsiUser` | `6555c87973344a223f234f329cf9de1a5fcb2756` |
| `C1:C3B6..C1:C403` | 77 | `CountEligibleBattlePsiUsers` | `5ae233d962c6fc84d12cdf504e7b85e8edf24180` |
| `C1:C403..C1:C452` | 79 | `PrintPsiFamilyName` | `1c3fb1d96c905babadfc7484b0869e74fedc007c` |

Labels:

- `C1:C165 CurrentCharacterKnowsPsi`
- `C1:C1BA HasPsiEntryForCategoryMask`
- `C1:C32A CanCharacterOpenPsiLane`
- `C1:C367 CheckBattlePsiUserEligibility`
- `C1:C373 FindFirstEligibleBattlePsiUser`
- `C1:C3B6 CountEligibleBattlePsiUsers`
- `C1:C403 PrintPsiFamilyName`

Evidence:

- `notes/battle-psi-menu-table-helpers-c1c046-c1c165.md`
- `notes/battle-psi-category-list-family-c1caf5-c1cb7f.md`
- `notes/battle-psi-user-selection-front-end-c1b5b6-b7c6.md`

### `src/c1/c1_ecd1_preview_packed_high_byte_window_flavour.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:ECD1..C1:ECDC` | 11 | `PreviewPackedHighByteWindowFlavour` | `2951aa977a0aa1cb9f6ed50d69506ef23cae88d6` |
| `C1:ECDC..C1:ED5B` | 127 | `ShowCorruptSaveFilesNotice` | `27bed1e2ebbd09287ed92e5c118a88b403645fde` |
| `C1:ED5B..C1:F03E` | 739 | `OpenFileSelectSlotChoiceMenu` | `02d62dfd86cac19117160dfe9dfff2d2e032d300` |
| `C1:F03E..C1:F06B` | 45 | `RunFileSelectSlotChoiceAndPreview` | `d3a5f2e0832fe303254a73befad1fd526d5104c1` |
| `C1:F06B..C1:F07E` | 19 | `ReturnSelectedSaveSlotAfterChecksum` | `2d10148b8406ebd2d125c97aa5656b63d3cbca3c` |

Labels:

- `C1:ECD1 PreviewPackedHighByteWindowFlavour`
- `C1:ECDC ShowCorruptSaveFilesNotice`
- `C1:ED5B OpenFileSelectSlotChoiceMenu`
- `C1:F03E RunFileSelectSlotChoiceAndPreview`
- `C1:F06B ReturnSelectedSaveSlotAfterChecksum`

Evidence:

- `notes/file-select-window-flavour-refresh-c1ec8f-ecd1.md`
- `notes/file-select-action-copy-delete-menus-c1f07e-f14f-f2a8.md`
- `notes/bank-c1-subsystem-and-symbol-synthesis.md`

### `src/c1/c1_e1a2_null_far_callback.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:E1A2..C1:E1A5` | 3 | `NullFarCallback` | `dde45a04b5b3b55e35ad5a3f8beb6e613f9c033a` |
| `C1:E1A5..C1:E47F` | 730 | `RunEnemySelectMode` | `a872859d2ccc02dd7ad4ebb2c19a0e990283cefb` |
| `C1:E47F..C1:E48D` | 14 | `ExitEnemySelectMode` | `dc8c1a91ac87e17cfa7c708e7525bb066b122baf` |

Labels:

- `C1:E1A2 NullFarCallback`
- `C1:E1A5 RunEnemySelectMode`
- `C1:E47F ExitEnemySelectMode`

Evidence:

- `notes/bank-c1-null-hook-c1e1a2.md`
- `notes/bank-c1-subsystem-and-symbol-synthesis.md`
- `notes/c2-battle-sprite-render-and-palette-tail-c2eee7-c2ff9a.md`

### `src/c1/c1_bcab_execute_teleport_destination.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:BCAB..C1:BE4D` | 418 | `ExecuteTeleportDestination` | `3da60042e21366210e48769cd6300f8a2ffa3ba9` |
| `C1:BE4D..C1:BEC6` | 121 | `AttemptHomesicknessResult` | `7f53c04bc8c4caba8c0f743dcab7145d7333de46` |
| `C1:BEC6..C1:BEFC` | 54 | `RunGetOffBicycleMessageAndExit` | `be21167fe08c01990bbce209dd0b49a837a54e42` |

Labels:

- `C1:BCAB ExecuteTeleportDestination`
- `C1:BE4D AttemptHomesicknessResult`
- `C1:BEC6 RunGetOffBicycleMessageAndExit`

Evidence:

- `notes/teleport-menu-wrapper-c1bb71-bcab.md`
- `notes/text-command-1f41-special-event-dispatch-c1befc.md`
- `notes/bicycle-transition-and-party-registry-c03c25-c03f1e.md`

### `src/c1/c1_ead6_run_naming_buffer_commit_flow.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:EAD6..C1:EC04` | 302 | `RunNamingBufferCommitFlow` | `87c07981b1ecd8cd57003dfd4556083859c8435e` |
| `C1:EC04..C1:EC8F` | 139 | `CommitNamingBufferFieldWithPreview` | `b9efbf37f3a1a83a94b031450324d1633a130458` |

Labels:

- `C1:EAD6 RunNamingBufferCommitFlow`
- `C1:EC04 CommitNamingBufferFieldWithPreview`

Evidence:

- `notes/naming-buffer-commit-family-c1ead6-c4d065.md`
- `notes/early-naming-buffers-9819-9829.md`
- `notes/text-input-dialog-option-helpers-c1e48d-c1e4be.md`

### `src/c1/c1_f497_open_or_refresh_text_speed_selection.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:F497..C1:F568` | 209 | `OpenOrRefreshTextSpeedSelection` | `1a4c4548ee202516578c64a0b0d235931fc13307` |
| `C1:F568..C1:F616` | 174 | `OpenSoundSettingMenu` | `fe9dbb293f60b8f11fbc339b035f9273fa902120` |

Labels:

- `C1:F497 OpenOrRefreshTextSpeedSelection`
- `C1:F568 OpenSoundSettingMenu`

Evidence:

- `notes/file-select-setup-option-menus-c1f497-c1f616.md`
- `notes/bank-c1-subsystem-and-symbol-synthesis.md`
- `notes/frontier-scout-2026-04-26.md`

### `src/c1/c1_f14f_open_copy_destination_menu.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:F14F..C1:F2A8` | 345 | `OpenCopyDestinationMenu` | `1dcebb151f16eee4ae936196a008486d2a8800a4` |

Labels:

- `C1:F14F OpenCopyDestinationMenu`

Evidence:

- `notes/file-select-action-copy-delete-menus-c1f07e-f14f-f2a8.md`
- `notes/bank-c1-subsystem-and-symbol-synthesis.md`
- `notes/frontier-scout-2026-04-26.md`

### `src/c1/c1_f07e_open_file_select_action_menu.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:F07E..C1:F14F` | 209 | `OpenFileSelectActionMenu` | `d7fd6582a82f85188188d1d62cf19e4fc2f920b5` |

Labels:

- `C1:F07E OpenFileSelectActionMenu`

Evidence:

- `notes/file-select-action-copy-delete-menus-c1f07e-f14f-f2a8.md`
- `notes/bank-c1-subsystem-and-symbol-synthesis.md`
- `notes/frontier-scout-2026-04-26.md`

### `src/c1/c1_ec8f_preview_window_flavour_and_redraw.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:EC8F..C1:ECD1` | 66 | `PreviewWindowFlavourAndRedraw` | `e790803938226d41ecfa7543f41701ea60d6ad72` |

Labels:

- `C1:EC8F PreviewWindowFlavourAndRedraw`

Evidence:

- `notes/file-select-window-flavour-refresh-c1ec8f-ecd1.md`
- `notes/file-select-setup-option-menus-c1f497-c1f616.md`
- `notes/bank-c1-subsystem-and-symbol-synthesis.md`

### `src/c1/c1_f2a8_open_delete_file_confirmation_menu.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:F2A8..C1:F3C2` | 282 | `OpenDeleteFileConfirmationMenu` | `29e74a35c877116958b42dc26a264e13257874e4` |
| `C1:F3C2..C1:F497` | 213 | `OpenTextSpeedMenu` | `38f85a0b3f55c4146d62ff58e5151c1697671dca` |

Labels:

- `C1:F2A8 OpenDeleteFileConfirmationMenu`
- `C1:F3C2 OpenTextSpeedMenu`

Evidence:

- `notes/file-select-action-copy-delete-menus-c1f07e-f14f-f2a8.md`
- `notes/file-select-setup-option-menus-c1f497-c1f616.md`
- `notes/bank-c1-subsystem-and-symbol-synthesis.md`
- `notes/bank-ef-reference-frontier.md`

### `src/c1/c1_c8bc_format_battle_psi_menu_entry_row.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:C8BC..C1:CA06` | 330 | `FormatBattlePsiMenuEntryRow` | `0c1ed2f533f2727acd4553ab09c0ef9e63c0083b` |

Labels:

- `C1:C8BC FormatBattlePsiMenuEntryRow`

Evidence:

- `notes/battle-psi-menu-metadata-family-c1c853-c1c8bc.md`
- `notes/battle-psi-name-builder-family-c1c8bc-ca06-c3f112-f124.md`
- `notes/battle-psi-ability-table-d58a50.md`

### `src/c1/c1_befc_dispatch_text_command1_f41_special_event.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:BEFC..C1:C046` | 330 | `DispatchTextCommand1F41SpecialEvent` | `0a39edb1ea8b6457e4b0fac14965c016d5ac86af` |

Labels:

- `C1:BEFC DispatchTextCommand1F41SpecialEvent`

Evidence:

- `notes/text-command-1f41-special-event-dispatch-c1befc.md`
- `notes/text-command-family-1f-deferred-callbacks.md`
- `notes/town-map-selection-rendering-c4d274-c4d744.md`

### `src/c1/c1_c046_refresh_psi_menu_cursor_category.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:C046..C1:C165` | 287 | `RefreshPsiMenuCursorCategory` | `3264bae8372b69c77154ec9f7f911739c703e19f` |

Labels:

- `C1:C046 RefreshPsiMenuCursorCategory`

Evidence:

- `notes/battle-psi-menu-table-helpers-c1c046-c1c165.md`
- `notes/battle-psi-menu-metadata-family-c1c853-c1c8bc.md`
- `notes/battle-psi-category-list-family-c1caf5-c1cb7f.md`

### `src/c1/c1_bb71_open_field_psi_destination_menu.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:BB71..C1:BCAB` | 314 | `OpenFieldPsiDestinationMenu` | `227411a4ca092b17623f226d434b7d902dc67b71` |

Labels:

- `C1:BB71 OpenFieldPsiDestinationMenu`

Evidence:

- `notes/teleport-menu-wrapper-c1bb71-bcab.md`
- `notes/battle-psi-user-selection-front-end-c1b5b6-b7c6.md`
- `notes/text-command-family-1a-menus.md`

### `src/c1/c1_ce85_resolve_selected_battle_item_action.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:CE85..C1:CFC6` | 321 | `ResolveSelectedBattleItemAction` | `af04c2b9affd01fa0c7d273181f7a483d326fb11` |

Labels:

- `C1:CE85 ResolveSelectedBattleItemAction`

Evidence:

- `notes/battle-item-action-selection-c1ce85-c1cfc6.md`
- `notes/battle-targetting-resolver-c1adb4-af50.md`
- `notes/item-slot-helper-pair-c3e977-c3ee14.md`

### `src/c1/c1_c853_resolve_battle_psi_targeting_metadata.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:C853..C1:C8BC` | 105 | `ResolveBattlePsiTargetingMetadata` | `05e500a36fc92e7e4672509d9cbb547a357b8ff9` |

Labels:

- `C1:C853 ResolveBattlePsiTargetingMetadata`

Evidence:

- `notes/battle-psi-menu-metadata-family-c1c853-c1c8bc.md`
- `notes/battle-psi-ability-table-d58a50.md`

### `src/c1/c1_ca06_build_psi_rank_name.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:CA06..C1:CA72` | 108 | `BuildPsiRankName` | `0fda80ebe3a50ae6b0f274247df4b3ecb01eafe8` |

Labels:

- `C1:CA06 BuildPsiRankName`

Evidence:

- `notes/battle-psi-name-builder-family-c1c8bc-ca06-c3f112-f124.md`
- `notes/battle-psi-ability-table-d58a50.md`

### `src/c1/c1_ca72_refresh_battle_psi_selection.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:CA72..C1:CAF5` | 131 | `RefreshBattlePsiSelection` | `c22a65232f46f1dfde357c7e2539758c2781d558` |

Labels:

- `C1:CA72 RefreshBattlePsiSelection`

Evidence:

- `notes/battle-psi-menu-metadata-family-c1c853-c1c8bc.md`
- `notes/battle-psi-category-list-family-c1caf5-c1cb7f.md`

### `src/c1/c1_caf5_build_battle_psi_category_entry_list.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:CAF5..C1:CB7F` | 138 | `BuildBattlePsiCategoryEntryList` | `64b28a9934a429c8cb44a118d2602200cf46a35b` |

Labels:

- `C1:CAF5 BuildBattlePsiCategoryEntryList`

Evidence:

- `notes/battle-psi-category-list-family-c1caf5-c1cb7f.md`
- `notes/battle-psi-menu-controller-c1cc39-ce73.md`

### `src/c1/c1_cfc6_open_battle_item_selection_loop.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:CFC6..C1:D038` | 114 | `OpenBattleItemSelectionLoop` | `fd19c1f73ce02069c0b3195d385bdc60b0046606` |

Labels:

- `C1:CFC6 OpenBattleItemSelectionLoop`

Evidence:

- `notes/battle-item-action-selection-c1ce85-c1cfc6.md`
- `notes/item-slot-helper-pair-c3e977-c3ee14.md`

### `src/c1/c1_d038_map_broken_item_to_repaired_item.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:D038..C1:D08B` | 83 | `MapBrokenItemToRepairedItem` | `474851964a7cc48b08527829cd2571a6e36873bc` |

Labels:

- `C1:D038 MapBrokenItemToRepairedItem`

Evidence:

- `notes/c3-jeff-repair-source-contract-f1ec.md`
- `notes/jeff-repair-item-name-bridge.md`

### `src/c1/c1_dc1c_display_battle_text_from_pointer.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:DC1C..C1:DC66` | 74 | `DisplayBattleTextFromPointer` | `708b0501ec877e0cbaed78234ecd782025186920` |

Labels:

- `C1:DC1C DisplayBattleTextFromPointer`

Evidence:

- `notes/battle-text-entry-family-c1dc1c-dd7c.md`
- `notes/direct-callers-c1-dc1c.md`

### `src/c1/c1_dc66_display_battle_text_with_substitution_payload.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:DC66..C1:DCCB` | 101 | `DisplayBattleTextWithSubstitutionPayload` | `950a389f2300186ef1fd2a4ec9755a615bfa2255` |

Labels:

- `C1:DC66 DisplayBattleTextWithSubstitutionPayload`

Evidence:

- `notes/battle-text-entry-family-c1dc1c-dd7c.md`
- `notes/class2-concrete-battle-text-call-paths.md`

### `src/c1/c1_dccb_initialize_party_battle_start_state.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:DCCB..C1:DD3B` | 112 | `InitializePartyBattleStartState` | `3ae598fa0583ec8e169fc1db8cc0ffc797fdea2d` |

Labels:

- `C1:DCCB InitializePartyBattleStartState`

Evidence:

- `notes/battle-text-entry-family-c1dc1c-dd7c.md`
- `notes/class2-battle-text-dispatch-stack.md`

### `src/c1/c1_ff99_compute_centered_text_layout_metric.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C1:FF99..C1:FFD3` | 58 | `ComputeCenteredTextLayoutMetric` | `62e27f3297d9b5a6a04b244093c1a8728e0ce066` |
| `C1:FFD3..C1:FFEF` | 28 | `ComputeBankC1ChecksumTail` | `38d13798765274b47d90632bcf5093c252f5e4b7` |
| `C1:FFEF..C1:10000` | 17 | `BankC1ChecksumConstantAndPadding` | `9381be87378c73e548ad79cc377cd0da932d4ef3` |

Labels:

- `C1:FF99 ComputeCenteredTextLayoutMetric`
- `C1:FFD3 ComputeBankC1ChecksumTail`
- `C1:FFEF BankC1ChecksumConstantAndPadding`

Evidence:

- `notes/file-select-tail-helpers-c1ff2c-ff6b-ff99.md`
- `notes/bank-c1-subsystem-and-symbol-synthesis.md`

## Notes

The scaffold preserves intentional source-adjacent data gaps from the manifest and validates each protected span against the original ROM bytes.
