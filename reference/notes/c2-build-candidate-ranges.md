# C2 build-candidate byte ranges

This manifest records source slices promoted into the reusable source-bank scaffold pipeline.

## Summary

- ranges: `233`
- total bytes: `65536`
- source bytes: `65536`
- data gap bytes: `0`

## Ranges

| Level | Source Path | Range | Span Bytes | Source Bytes | Data Gap Bytes | SHA-1 |
| --- | --- | --- | ---: | ---: | ---: | --- |
| `build-candidate` | `src/c2/c2_3b66_expand_battle_text_context_template.asm` | `C2:3B66..C2:3BCF` | 105 | 105 | 0 | `6675b052cdcad4ef4a19e595c4d76027a36bb8d9` |
| `build-candidate` | `src/c2/c2_3bcf_build_battle_attacker_text_context.asm` | `C2:3BCF..C2:3D05` | 310 | 310 | 0 | `3c2503b7ce63be657e1f00cbe2f3a74d7d6359d6` |
| `build-candidate` | `src/c2/c2_7680_display_enemy_death_text.asm` | `C2:7680..C2:77CA` | 330 | 330 | 0 | `d5300c4ae8a5bbfe33b9776f3bf39f383232bb90` |
| `build-candidate` | `src/c2/c2_3d05_build_battle_target_text_context.asm` | `C2:3D05..C2:40A4` | 927 | 927 | 0 | `2675308b9fb4fea353357dd65b039f2472b0d2e4` |
| `build-candidate` | `src/c2/c2_40a4_apply_battle_action_second_pointer_payload.asm` | `C2:40A4..C2:41DC` | 312 | 312 | 0 | `5ebe676f42019ccee61be571963826ee1745891e` |
| `build-candidate` | `src/c2/c2_41dc_build_stealable_item_candidate_list.asm` | `C2:41DC..C2:4316` | 314 | 314 | 0 | `59c553a31ec75c1aa78823924d7f6cabc873a12a` |
| `build-candidate` | `src/c2/c2_4316_select_stealable_item_candidate.asm` | `C2:4316..C2:4348` | 50 | 50 | 0 | `10e5c70abce5b7ca58fedddfa6e299e71f296445` |
| `build-candidate` | `src/c2/c2_4348_is_pending_steal_item_still_stealable.asm` | `C2:4348..C2:437E` | 54 | 54 | 0 | `41385bbadc0087440e747af3b6e4513202bf9c0e` |
| `build-candidate` | `src/c2/c2_4434_pick_random_battler_from_front_back_rows.asm` | `C2:4434..C2:4477` | 67 | 67 | 0 | `641e45a2ba5791621e230a8a22d2c1d4e229c7ed` |
| `build-candidate` | `src/c2/c2_437e_apply_pending_stolen_item_slot_if_still_valid.asm` | `C2:437E..C2:4434` | 182 | 182 | 0 | `6eb8312e9ce40d1c9d2460c0f87a1f4187334c59` |
| `build-candidate` | `src/c2/c2_4477_build_class2_derived_action_code.asm` | `C2:4477..C2:4703` | 652 | 652 | 0 | `90375f81c83d98af7a84d7c0c17545a07f86bb9b` |
| `build-candidate` | `src/c2/c2_4703_dispatch_class2_derived_action.asm` | `C2:4703..C2:4958` | 597 | 597 | 0 | `c6e8ea62d33f37c25c892e0e829aa8bcf6acf859` |
| `build-candidate` | `src/c2/c2_4958_populate_candidate_pool_from_six_sources.asm` | `C2:4958..C2:4A8A` | 306 | 306 | 0 | `ed785bb609e5fde164454f33167ffd8d12bddcee` |
| `build-candidate` | `src/c2/c2_4f00_display_battle_encounter_text.asm` | `C2:4F03..C2:4F52` | 79 | 79 | 0 | `634310e6d353555b7f5a8cc1933c6081fb04c8d7` |
| `build-candidate` | `src/c2/c2_6e77_mask_set_remove_active_typed_candidates.asm` | `C2:6E77..C2:6EF8` | 129 | 129 | 0 | `57e74200edc7ed8e40261c790393e6d0664f8b06` |
| `build-candidate` | `src/c2/c2_6c82_mask_set_build_phase1_candidates.asm` | `C2:6C82..C2:6E77` | 501 | 501 | 0 | `8cd6869b5f0940bfae17892d230f225b59290a49` |
| `build-candidate` | `src/c2/c2_6bfb_mask_set_build_active_typed_candidates.asm` | `C2:6BFB..C2:6C82` | 135 | 135 | 0 | `ba0a435960dca30be0282b1087d12b9fe3533159` |
| `build-candidate` | `src/c2/c2_6ef8_mask_set_find_first_match_in_range.asm` | `C2:6EF8..C2:6FDC` | 228 | 228 | 0 | `0b83af9b6038720da1ceed83a8bf9a635cdaca49` |
| `build-candidate` | `src/c2/c2_6fdc_mask_set_add_bit.asm` | `C2:6FDC..C2:7029` | 77 | 77 | 0 | `39324f95ded7b3cb72caedf786b54461de729cdd` |
| `build-candidate` | `src/c2/c2_7089_mask_set_clear_bit.asm` | `C2:7089..C2:70E4` | 91 | 91 | 0 | `48b5a1cca09f89908f3be95510946f19b5687128` |
| `build-candidate` | `src/c2/c2_70e4_mask_set_prune_flagged_candidates.asm` | `C2:70E4..C2:724A` | 358 | 358 | 0 | `3277f7e8e4c35c91764c85713b97556e02885f62` |
| `build-candidate` | `src/c2/c2_7029_mask_set_test_bit.asm` | `C2:7029..C2:7089` | 96 | 96 | 0 | `669babe12074d5683714f5389cccc6ca6e7af917` |
| `build-candidate` | `src/c2/c2_724a_apply_battler_affliction_subgroup_value.asm` | `C2:724A..C2:7294` | 74 | 74 | 0 | `e1d44cd6346f1fc8cc38e6b1bb1e91b650692be2` |
| `build-candidate` | `src/c2/c2_7294_apply_battler_hp_recovery_feedback.asm` | `C2:7294..C2:7318` | 132 | 132 | 0 | `b3546d2012e23968620fe24ff3d23b7a4d9db08c` |
| `build-candidate` | `src/c2/c2_7318_apply_battler_pp_recovery_feedback.asm` | `C2:7318..C2:7397` | 127 | 127 | 0 | `d79f829cab66d44e051b8bf57425424fa4964d1e` |
| `build-candidate` | `src/c2/c2_7397_install_battler_heavy_recovery_reset.asm` | `C2:7397..C2:7550` | 441 | 441 | 0 | `58d49e3b90a757a77ff0e4495117ec8753136ec6` |
| `build-candidate` | `src/c2/c2_7550_start_selected_battler_collapse_affliction_path.asm` | `C2:7550..C2:7680` | 304 | 304 | 0 | `342b96f687b5344f6c7d17a59192e9090cd4cb1c` |
| `build-candidate` | `src/c2/c2_77ca_run_class2_late_selected_row_controller.asm` | `C2:77CA..C2:7CFD` | 1331 | 1331 | 0 | `7bfe872cadd3ae89d80b704a41e635cf9b145ed3` |
| `build-candidate` | `src/c2/c2_7cfd_check_selected_battler_default_text_blocker.asm` | `C2:7CFD..C2:7D28` | 43 | 43 | 0 | `b77bee558175265bb1b6e701c682c69c7f6b612a` |
| `build-candidate` | `src/c2/c2_7d28_apply_bounded_offense_increase.asm` | `C2:7D28..C2:7D82` | 90 | 90 | 0 | `bd676368956360c38af19afcc5a9c4abbb5ee471` |
| `build-candidate` | `src/c2/c2_7d82_apply_bounded_defense_increase.asm` | `C2:7D82..C2:7DDC` | 90 | 90 | 0 | `18d94f65668cfe8b5557a86aaf10107d1aea55cb` |
| `build-candidate` | `src/c2/c2_7e33_apply_bounded_defense_decrease.asm` | `C2:7E33..C2:7E8A` | 87 | 87 | 0 | `27152828b8df1c2cb1e2242b5127a4f84a4b58c7` |
| `build-candidate` | `src/c2/c2_7ddc_apply_bounded_offense_decrease.asm` | `C2:7DDC..C2:7E33` | 87 | 87 | 0 | `a378d3811bcc8d14ac9d703e30b8026311ef5ff0` |
| `build-candidate` | `src/c2/c2_8bbe_run_mushroomize_status_action.asm` | `C2:8BBE..C2:8BFD` | 63 | 63 | 0 | `946232c6e3ea753816fa50c03f4f902d7e183922` |
| `build-candidate` | `src/c2/c2_8bfd_run_possess_status_action.asm` | `C2:8BFD..C2:8C69` | 108 | 108 | 0 | `90860fa5edd6cb68270e10122be7b0dad134de20` |
| `build-candidate` | `src/c2/c2_8c69_run_crying_status_action.asm` | `C2:8C69..C2:8CB8` | 79 | 79 | 0 | `dfeb5fd9be9aa277d29517f06a0a7d5f4d7132d5` |
| `build-candidate` | `src/c2/c2_8cb8_run_immobilized_status_action.asm` | `C2:8CB8..C2:8CF1` | 57 | 57 | 0 | `827b08d890c6a7e3f31f476ec5062ff850c756a2` |
| `build-candidate` | `src/c2/c2_8cf1_run_solidified_status_action.asm` | `C2:8CF1..C2:8D3A` | 73 | 73 | 0 | `dc47c04c7d412e22c04121e0ebcf24b52de4c377` |
| `build-candidate` | `src/c2/c2_8d3a_run_strange_status_wrapper_action.asm` | `C2:8D3A..C2:8D5A` | 32 | 32 | 0 | `4122c65e988849897a72db2dc2e9e7ccbe63f6c9` |
| `build-candidate` | `src/c2/c2_8d5a_run_concentration_seal_action.asm` | `C2:8D5A..C2:8DBB` | 97 | 97 | 0 | `a5d857d7ca96aea0ac016b717bec50ddfb6b4e67` |
| `build-candidate` | `src/c2/c2_8dbb_run_direct_strange_status_action.asm` | `C2:8DBB..C2:8E42` | 135 | 135 | 0 | `11d0beee9e422b1ee02d97d8c233bd7b831f69fc` |
| `build-candidate` | `src/c2/c2_8e42_run_pp_reduction_action.asm` | `C2:8E42..C2:8EAE` | 108 | 108 | 0 | `16729eeeac6184ede9ded6343550c252286458a2` |
| `build-candidate` | `src/c2/c2_8eae_run_guts_reduction_action.asm` | `C2:8EAE..C2:8F21` | 115 | 115 | 0 | `d4f3c55e76efb1f2027ca3b0f9012df472b89323` |
| `build-candidate` | `src/c2/c2_8f21_run_offense_defense_reduction_action.asm` | `C2:8F21..C2:8F97` | 118 | 118 | 0 | `9305b3e203ddff0fd724b9e53f10e457d55c8270` |
| `build-candidate` | `src/c2/c2_8f97_run_poison_on_hit_physical_action.asm` | `C2:8F97..C2:8FF9` | 98 | 98 | 0 | `cf20c8351bd302b9f2b7f1f70ad572ee38cd091e` |
| `build-candidate` | `src/c2/c2_8ff9_run_double_bash_action.asm` | `C2:8FF9..C2:900B` | 18 | 18 | 0 | `0e647a1fd0dee3462d3d3c36ecab7c066db80013` |
| `build-candidate` | `src/c2/c2_900b_run_fire_damage_action_wrapper.asm` | `C2:900B..C2:902C` | 33 | 33 | 0 | `88d0c87988cf91ef90e06a3b2227ec844e8bab2f` |
| `build-candidate` | `src/c2/c2_902c_run_all_target_physical_flavor_wrapper.asm` | `C2:902C..C2:9033` | 7 | 7 | 0 | `db8604a72b4d8e251e8249636570d3cefa2722a6` |
| `build-candidate` | `src/c2/c2_9033_run_flavor_only_no_op_tail.asm` | `C2:9033..C2:904E` | 27 | 27 | 0 | `7b32d9c163b7e04e7ba3616f5138de50db4a1c0a` |
| `build-candidate` | `src/c2/c2_904e_run_late_message_only_no_op_tail.asm` | `C2:904E..C2:9051` | 3 | 3 | 0 | `dde45a04b5b3b55e35ad5a3f8beb6e613f9c033a` |
| `build-candidate` | `src/c2/c2_9051_queued_battler_stat_shield_normalization_callback.asm` | `C2:9051..C2:90C6` | 117 | 117 | 0 | `198b3e0d0cf5559f2997fef5f23a7543555f4c63` |
| `build-candidate` | `src/c2/c2_90c6_run_battler_normalization_action_wrapper.asm` | `C2:90C6..C2:916E` | 168 | 168 | 0 | `9e8ba1aea357f7747d01d1887f10506660bd5acb` |
| `build-candidate` | `src/c2/c2_916e_run_diamondize_action.asm` | `C2:916E..C2:9254` | 230 | 230 | 0 | `f81bc108ab9c83d00d541008482d778206e0426c` |
| `build-candidate` | `src/c2/c2_9254_run_odor_offense_reduction_action.asm` | `C2:9254..C2:9298` | 68 | 68 | 0 | `1251a90942e5839fa67116dda09381334cbd9b44` |
| `build-candidate` | `src/c2/c2_9298_run_runaway_five_clumsy_robot_special_event.asm` | `C2:9298..C2:92EE` | 86 | 86 | 0 | `1f9db0f11a97093ebce286f393da2f3bb46a287d` |
| `build-candidate` | `src/c2/c2_92ee_run_master_barf_poo_starstorm_special_event.asm` | `C2:92EE..C2:941D` | 303 | 303 | 0 | `efcd2ac520c0c9b44a61fc405621291630579943` |
| `build-candidate` | `src/c2/c2_941d_check_selected_battler_timed_substate_blocker.asm` | `C2:941D..C2:94CE` | 177 | 177 | 0 | `6d9b79f27fe5f6708cbcdf1bfdf7626937335e6a` |
| `build-candidate` | `src/c2/c2_94ce_tick_selected_battler_timed_substate_cleanup.asm` | `C2:94CE..C2:9516` | 72 | 72 | 0 | `a1fae7de8c785c10576daa725cb9377ae2578891` |
| `build-candidate` | `src/c2/c2_9516_run_psi_rockin_common.asm` | `C2:9516..C2:957A` | 100 | 100 | 0 | `d76d30d3724112b551b8522a48de79fc2f536804` |
| `build-candidate` | `src/c2/c2_957a_run_psi_fire_common.asm` | `C2:957A..C2:95CF` | 85 | 85 | 0 | `48f2bb96a6b57e14ce51fed02cc4081aa77bfa23` |
| `build-candidate` | `src/c2/c2_95cf_run_psi_freeze_common.asm` | `C2:95CF..C2:966B` | 156 | 156 | 0 | `6b59c6d0375cd88f678335c034603aa8b9a79535` |
| `build-candidate` | `src/c2/c2_966b_run_psi_thunder_common.asm` | `C2:966B..C2:97A5` | 314 | 314 | 0 | `0d9f5e748778d3143d1dc61d2eb12101c008fe81` |
| `build-candidate` | `src/c2/c2_97a5_handle_psi_thunder_franklin_badge_reflection.asm` | `C2:97A5..C2:98A1` | 252 | 252 | 0 | `5937eb1b1c25e9639129f54959d12ceaf2d0edfe` |
| `build-candidate` | `src/c2/c2_98a1_gate_selected_battler_for_random_status_action.asm` | `C2:98A1..C2:98DE` | 61 | 61 | 0 | `9bae223b3571b40d107e3b042208a175d4b5ab0c` |
| `build-candidate` | `src/c2/c2_98de_try_apply_strange_status_to_selected_battler.asm` | `C2:98DE..C2:9917` | 57 | 57 | 0 | `8ed0bea029b93277ff58b68ea14e927d81551f63` |
| `build-candidate` | `src/c2/c2_9917_try_apply_numb_status_to_selected_battler.asm` | `C2:9917..C2:9950` | 57 | 57 | 0 | `c31a3d1118810a79e0abaa851b25f3345f906a89` |
| `build-candidate` | `src/c2/c2_9950_try_apply_crying_status_to_selected_battler.asm` | `C2:9950..C2:9987` | 55 | 55 | 0 | `b18161638673f43cd84c98b0eada9b2ea309fa10` |
| `build-candidate` | `src/c2/c2_9987_run_psi_flash_alpha_action.asm` | `C2:9987..C2:99AE` | 39 | 39 | 0 | `01cab99585671b7a4adf2b6559dfb3c05e9529da` |
| `build-candidate` | `src/c2/c2_99ae_run_psi_flash_beta_action.asm` | `C2:99AE..C2:99EF` | 65 | 65 | 0 | `d604c18a2c7debd602a2755471d79814cbd12f0e` |
| `build-candidate` | `src/c2/c2_99ef_run_psi_flash_gamma_action.asm` | `C2:99EF..C2:9A35` | 70 | 70 | 0 | `8a5ad3fe4b1d0a96e77127efa103271e9f1f044b` |
| `build-candidate` | `src/c2/c2_9a35_run_psi_flash_omega_action.asm` | `C2:9A35..C2:9A80` | 75 | 75 | 0 | `4bd0ec815e80f83ccd789fab9cd1a439a6c367c2` |
| `build-candidate` | `src/c2/c2_9a80_run_psi_starstorm_common.asm` | `C2:9A80..C2:9AB8` | 56 | 56 | 0 | `29df3a8b662e85534bbf691a6fa89064f1e12d81` |
| `build-candidate` | `src/c2/c2_9ab8_run_fixed_amount_healing_common.asm` | `C2:9AB8..C2:9AEA` | 50 | 50 | 0 | `d53b621a579d6a9dc21fee2772956d1ddccbb969` |
| `build-candidate` | `src/c2/c2_9aea_try_recover_selected_battler_narrow_affliction.asm` | `C2:9AEA..C2:9B7A` | 144 | 144 | 0 | `5926d7328ae4484f09b2d086b703a8c26005bac5` |
| `build-candidate` | `src/c2/c2_9b7a_try_recover_selected_battler_curative_afflictions.asm` | `C2:9B7A..C2:9C2C` | 178 | 178 | 0 | `20bdcfb02bacf375802829af0e821e18fcba7bdc` |
| `build-candidate` | `src/c2/c2_9c2c_try_recover_selected_battler_broad_afflictions.asm` | `C2:9C2C..C2:9CB8` | 140 | 140 | 0 | `d12f65dd4539f4ea8ee9704011d06abc4619cab5` |
| `build-candidate` | `src/c2/c2_9cb8_try_recover_selected_battler_hard_state.asm` | `C2:9CB8..C2:9E38` | 384 | 384 | 0 | `36a6bf51fa642f754154d112cedd48c64e96a603` |
| `build-candidate` | `src/c2/c2_9e38_run_defense_spray_action.asm` | `C2:9E38..C2:9E7F` | 71 | 71 | 0 | `cf3cbb78aa38cff2a0c2709528cdedc618eac4cf` |
| `build-candidate` | `src/c2/c2_9e7f_run_defense_shower_action.asm` | `C2:9E7F..C2:9F06` | 135 | 135 | 0 | `6e54db4604734b008e639052f6019f7002f01fcb` |
| `build-candidate` | `src/c2/c2_9f06_run_resist_checked_asleep_status_action.asm` | `C2:9F06..C2:9F57` | 81 | 81 | 0 | `2c3c39707711fd09675bb8d45ac7da20a82d4685` |
| `build-candidate` | `src/c2/c2_9f57_run_asleep_status_wrapper_action.asm` | `C2:9F57..C2:A056` | 255 | 255 | 0 | `c6ceeece25e4443155dfa29a62e99698e637352d` |
| `build-candidate` | `src/c2/c2_a056_run_resist_checked_strange_status_action.asm` | `C2:A056..C2:A39D` | 839 | 839 | 0 | `de5405c34feaa413ffec2d6feb52ec416f869a32` |
| `build-candidate` | `src/c2/c2_a39d_try_recover_selected_battler_poison_only.asm` | `C2:A39D..C2:A3D1` | 52 | 52 | 0 | `d3e35e5e835d20bdbcdb32b4988dd3056d268dc0` |
| `build-candidate` | `src/c2/c2_0266_load_default_title_upload_tiles.asm` | `C2:0266..C2:0293` | 45 | 45 | 0 | `5e3b26328f0bac27bfc7411d94e926fcac0dac7b` |
| `build-candidate` | `src/c2/c2_0293_clear_default_title_upload_tiles.asm` | `C2:0293..C2:02AC` | 25 | 25 | 0 | `eef318131a7aaa9c4835c3d601b3c2d7337d8ebd` |
| `build-candidate` | `src/c2/c2_02ac_register_and_upload_window_title_buffer.asm` | `C2:02AC..C2:032B` | 127 | 127 | 0 | `0656b690211665397d2c044febb7150825346872` |
| `build-candidate` | `src/c2/c2_032b_write_window_title_and_upload.asm` | `C2:032B..C2:038B` | 96 | 96 | 0 | `db46622debfb52e1da3b737fba352fd7da0f73fa` |
| `build-candidate` | `src/c2/c2_038b_reset_hp_pp_tilemap_buffers.asm` | `C2:038B..C2:03C3` | 56 | 56 | 0 | `89e677ba14731a7e32ed3d97160d4df6335449c3` |
| `build-candidate` | `src/c2/c2_1628_test_event_flag.asm` | `C2:1628..C2:165E` | 54 | 54 | 0 | `3f48f0ad40712500ccf95077ce8a2e890a0f9564` |
| `build-candidate` | `src/c2/c2_165e_set_or_clear_event_flag.asm` | `C2:165E..C2:16AD` | 79 | 79 | 0 | `53220a016966d48cd8ad4aec6f50714999a232c6` |
| `build-candidate` | `src/c2/c2_26c5_set_current9_c88_flag_and_refresh5_d64.asm` | `C2:26C5..C2:26D0` | 11 | 11 | 0 | `9ad2cd3672dccf845d7227bb1abecc4b6372700a` |
| `build-candidate` | `src/c2/c2_26d0_set_current_interaction_event_flag_and_refresh_target.asm` | `C2:26D0..C2:26E6` | 22 | 22 | 0 | `d6001943eef1f457d973bd27cb509c0525318693` |
| `build-candidate` | `src/c2/c2_26e6_get_current9_c88_flag.asm` | `C2:26E6..C2:26EB` | 5 | 5 | 0 | `6bb9319c041fddf95b8619ec44534145e6f55bc2` |
| `build-candidate` | `src/c2/c2_26eb_test_current_interaction_event_flag.asm` | `C2:26EB..C2:26F0` | 5 | 5 | 0 | `a522b8d45295eb1ff1b746c708022c6d35b77f8b` |
| `build-candidate` | `src/c2/c2_08b8_classify_menu_tile_for_cursor_scan.asm` | `C2:08B8..C2:0912` | 90 | 90 | 0 | `63f5f339197992e1a3bb55d5ef3a92448d714c81` |
| `build-candidate` | `src/c2/c2_0b65_find_next_selectable_menu_cell.asm` | `C2:0B65..C2:0D3F` | 474 | 474 | 0 | `29d1d68f48b4432fc6f3d369026f9811b866e0c9` |
| `build-candidate` | `src/c2/c2_0d3f_split_value_into_three_decimal_digits_at8966.asm` | `C2:0D3F..C2:0F58` | 537 | 537 | 0 | `88642c89553bdf1783ebdb636559e01c7a76ae07` |
| `build-candidate` | `src/c2/c2_0f58_select_hp_pp_roll_delta.asm` | `C2:0F58..C2:0F9A` | 66 | 66 | 0 | `ac08e1b1092be7cad2d3214182b47b611a0d52b5` |
| `build-candidate` | `src/c2/c2_0f9a_clamp_hp_pp_roll_targets_to_live_values.asm` | `C2:0F9A..C2:1034` | 154 | 154 | 0 | `dfbaead209df0faf8ef4750ad2eaffa2af00f662` |
| `build-candidate` | `src/c2/c2_1034_are_all_hp_pp_rollers_settled.asm` | `C2:1034..C2:108C` | 88 | 88 | 0 | `4da4e71558c26297a69bf1ecfe46ef6f0b85d0e0` |
| `build-candidate` | `src/c2/c2_108c_clear_hp_pp_roll_dirty_latch_if_settled.asm` | `C2:108C..C2:109F` | 19 | 19 | 0 | `fcf8deda515dc74abb411851c7e839962b63b289` |
| `build-candidate` | `src/c2/c2_109f_run_hp_pp_roller.asm` | `C2:109F..C2:13AC` | 781 | 781 | 0 | `0f06993a3c14abbc1d3fd8a57dda12bc24abf1c8` |
| `build-candidate` | `src/c2/c2_13ac_update_hp_pp_meter_tiles.asm` | `C2:13AC..C2:1628` | 636 | 636 | 0 | `167bbf981c5a95227f36c94b4ed7c2bcf66336cb` |
| `build-candidate` | `src/c2/c2_16ad_apply_music_state_and_mirror_to5_dd4.asm` | `C2:16AD..C2:16C9` | 28 | 28 | 0 | `b1373f9ed8d43380ce08d0d38136e650466cb932` |
| `build-candidate` | `src/c2/c2_16c9_stop_music_redirect.asm` | `C2:16C9..C2:16D0` | 7 | 7 | 0 | `94b96b3e45fb836b644b6d1d9a0bbfd0cf7e4bfc` |
| `build-candidate` | `src/c2/c2_16d0_play_sound_and_refresh_hp_pp_rollers.asm` | `C2:16D0..C2:16DB` | 11 | 11 | 0 | `af02fee05d436d96660e3d10c4da06b25c7e207f` |
| `build-candidate` | `src/c2/c2_16db_arbitrate_party_overlay_entity_presence.asm` | `C2:16DB..C2:1857` | 380 | 380 | 0 | `02ec6e2667eaa4b7fdf2697024908542cf943941` |
| `build-candidate` | `src/c2/c2_26f0_find_first_party_slot_with_state_one.asm` | `C2:26F0..C2:272F` | 63 | 63 | 0 | `dede487f424f9f87bd8a9ade69084e9c3272a601` |
| `build-candidate` | `src/c2/c2_272f_count_party_slots_not_state_one_or_two.asm` | `C2:272F..C2:277C` | 77 | 77 | 0 | `24db66c2b406299e6c75dd1d29f7b565437d6fcd` |
| `build-candidate` | `src/c2/c2_277c_find_first_party_code_not_state_one_or_two.asm` | `C2:277C..C2:27C8` | 76 | 76 | 0 | `b75723f00256717593fbd01aa76304455c7884b3` |
| `build-candidate` | `src/c2/c2_27c8_mark_party_code_bit_in9839.asm` | `C2:27C8..C2:281D` | 85 | 85 | 0 | `2fd10644f74fcb336e4d3c065f2d71b8a24d1987` |
| `build-candidate` | `src/c2/c2_281d_update_party_overlay_position_clamp.asm` | `C2:281D..C2:28B7` | 154 | 154 | 0 | `2ca72af108a33d167f64537508807b5377370383` |
| `build-candidate` | `src/c2/c2_28b7_clamp_party_overlay_position_delta.asm` | `C2:28B7..C2:28F8` | 65 | 65 | 0 | `aa5f341fcc09ff10d75953686eec4dab5254a8aa` |
| `build-candidate` | `src/c2/c2_28f8_insert_party_overlay_tracked_item_id.asm` | `C2:28F8..C2:29BB` | 195 | 195 | 0 | `da729ab3137cdc755c0cd2ddf557548a0ca54a9e` |
| `build-candidate` | `src/c2/c2_29bb_remove_party_overlay_tracked_item_id.asm` | `C2:29BB..C2:2A2C` | 113 | 113 | 0 | `d6bcb6e9c809c5c1b6408fdc3e9eab2c80959fda` |
| `build-candidate` | `src/c2/c2_2a2c_save_current_game.asm` | `C2:2A2C..C2:2A3A` | 14 | 14 | 0 | `c7715e26ee6b73b8b636cd9a5f29b5aec9b8f230` |
| `build-candidate` | `src/c2/c2_3008_save_and_clear_temporary_party_source_state.asm` | `C2:3008..C2:307B` | 115 | 115 | 0 | `2b8e294be7cffd279bb59519ff56f4bb8f9bd299` |
| `build-candidate` | `src/c2/c2_307b_restore_temporary_party_source_state.asm` | `C2:307B..C2:30F3` | 120 | 120 | 0 | `d4ada9ad5651260b23e3db8e0c2252b6c9f9c830` |
| `build-candidate` | `src/c2/c2_2a3a_transfer_inventory_item_between_characters_maintaining_equipment.asm` | `C2:2A3A..C2:2F38` | 1278 | 1278 | 0 | `1e142ea8b494a379e778e350a61bff1adb2151b4` |
| `build-candidate` | `src/c2/c2_2f38_init_battle_scripted.asm` | `C2:2F38..C2:3008` | 208 | 208 | 0 | `7a8ab80ea0c79773dbad813b61d7139d5b18d263` |
| `build-candidate` | `src/c2/c2_1857_recalculate_character_derived_offense.asm` | `C2:1857..C2:192B` | 212 | 212 | 0 | `c2bd8b2bd0dbe4f751ad168aa8aa0d0fc00d6333` |
| `build-candidate` | `src/c2/c2_192b_recalculate_character_derived_defense.asm` | `C2:192B..C2:1AEB` | 448 | 448 | 0 | `9501f122595666fc4ba7bfe0697384189e93df78` |
| `build-candidate` | `src/c2/c2_1aeb_recalculate_character_derived_speed.asm` | `C2:1AEB..C2:1BA4` | 185 | 185 | 0 | `37dd764ae160be614cb89ce45f88eee16cbe01df` |
| `build-candidate` | `src/c2/c2_1ba4_recalculate_character_derived_guts.asm` | `C2:1BA4..C2:1C5D` | 185 | 185 | 0 | `7b5751c3a2587142dbc3f73d744249c83a637596` |
| `build-candidate` | `src/c2/c2_1c5d_recalculate_character_derived_luck.asm` | `C2:1C5D..C2:1D65` | 264 | 264 | 0 | `f5f1026d1cbc6d0d39a655e9a0cecfeaddf2e8f5` |
| `build-candidate` | `src/c2/c2_1d65_recalculate_character_derived_vitality.asm` | `C2:1D65..C2:1D7D` | 24 | 24 | 0 | `027796a2f4f2f82efce426f7fd5e88842842e7df` |
| `build-candidate` | `src/c2/c2_1d7d_recalculate_character_derived_iq.asm` | `C2:1D7D..C2:1D95` | 24 | 24 | 0 | `cf2e572f30daa3e79bc4706591780649cd1df378` |
| `build-candidate` | `src/c2/c2_1d95_recalculate_character_derived_miss_rate.asm` | `C2:1D95..C2:1E03` | 110 | 110 | 0 | `6829513f839bfe55b1e7395bf81653f2ce3f4678` |
| `build-candidate` | `src/c2/c2_1e03_recalculate_character_derived_resistance_fields.asm` | `C2:1E03..C2:2351` | 1358 | 1358 | 0 | `b84b8ab0df4b2f70014790b9f6a8ededeb310dea` |
| `build-candidate` | `src/c2/c2_2351_find_first_empty_inventory_slot_for_character.asm` | `C2:2351..C2:239D` | 76 | 76 | 0 | `f166eade72056e08ce9cd68f6cea43de7a2ee86f` |
| `build-candidate` | `src/c2/c2_6189_fill_instant_win_tile_buffer_and_upload.asm` | `C2:6189..C2:654C` | 963 | 963 | 0 | `63eccbf106302e2b6715b25eb38a0325e5faf4d2` |
| `build-candidate` | `src/c2/c2_654c_run_magic_butterfly_pp_restore_animation.asm` | `C2:654C..C2:6BFB` | 1711 | 1711 | 0 | `b04f30d032e33b1433746846f8625e7e8877095b` |
| `build-candidate` | `src/c2/c2_b930_export_battle_selection_snapshot.asm` | `C2:B930..C2:BAC5` | 405 | 405 | 0 | `e8ac99dbbd81e27dc4ff56f5563149542fed765a` |
| `build-candidate` | `src/c2/c2_bac5_count_filtered_second_stage_rows.asm` | `C2:BAC5..C2:BB18` | 83 | 83 | 0 | `d7f4d105f7358a9258f50f419a3865eabe5747f5` |
| `build-candidate` | `src/c2/c2_bb18_promote_candidate_to_collapse_affliction_controller.asm` | `C2:BB18..C2:BC5C` | 324 | 324 | 0 | `aa066aac22c9f3595139fb307cea74acaf6d7696` |
| `build-candidate` | `src/c2/c2_bc5c_clear_inactive_candidate_live_slot_transient_fields.asm` | `C2:BC5C..C2:BCB9` | 93 | 93 | 0 | `d4ce119753f5bb79d2047a6cbaec917c80519a53` |
| `build-candidate` | `src/c2/c2_2474_lookup_status_tile_width_or_offset_for_hp_pp_window.asm` | `C2:2474..C2:2562` | 238 | 238 | 0 | `e3190ba56bd21be3cb81e59269e641b5ec69a819` |
| `build-candidate` | `src/c2/c2_23d9_lookup_status_tile_value_for_hp_pp_window.asm` | `C2:23D9..C2:2474` | 155 | 155 | 0 | `75acf3739bfe94580ee762d90a835e3145cfea53` |
| `build-candidate` | `src/c2/c2_cfe5_init_loaded_battle_bg_layer_from_config.asm` | `C2:CFE5..C2:D0AC` | 199 | 199 | 0 | `dbd6c4690b987a8a1081ce4f51d98338a72a9461` |
| `build-candidate` | `src/c2/c2_de0f_dim_loaded_battle_bg_palettes_and_upload.asm` | `C2:DE0F..C2:DE96` | 135 | 135 | 0 | `c898428d9a8ed439eaeb5d92ea573145ebc79bcf` |
| `build-candidate` | `src/c2/c2_de96_restore_loaded_battle_bg_palettes_and_upload.asm` | `C2:DE96..C2:DF2E` | 152 | 152 | 0 | `ce4671d53bdc996c92cb65c97e961311c8c0a330` |
| `build-candidate` | `src/c2/c2_df2e_apply_loaded_battle_bg_palette_step.asm` | `C2:DF2E..C2:E08E` | 352 | 352 | 0 | `5d92c39a03d60fdd5259caa2f4ea80f657d33afc` |
| `build-candidate` | `src/c2/c2_e08e_apply_loaded_battle_bg_palette_step_across_layers.asm` | `C2:E08E..C2:E0E7` | 89 | 89 | 0 | `2ffe50535464173864d02f18eba25780fdcc35a5` |
| `build-candidate` | `src/c2/c2_f09f_find_loaded_battle_sprite_slot_by_id.asm` | `C2:F09F..C2:F0D1` | 50 | 50 | 0 | `3d9a7dc75d91694dac3659f52fe34ed7d365bcfc` |
| `build-candidate` | `src/c2/c2_f0d1_trim_loaded_enemy_sprite_list_to_width_limit.asm` | `C2:F0D1..C2:F121` | 80 | 80 | 0 | `2d9b037c67cd11e10ce5bb11a49aa18985e878dc` |
| `build-candidate` | `src/c2/c2_f8f9_render_and_commit_battle_sprite_rows.asm` | `C2:F8F9..C2:F917` | 30 | 30 | 0 | `c1e9ce0a1c2a123546486ded6c742cd65eefa366` |
| `build-candidate` | `src/c2/c2_f917_build_battle_sprite_row_render_order.asm` | `C2:F917..C2:FADE` | 455 | 455 | 0 | `870c65b75c8f3e33fba1af94334f6e665a17b46f` |
| `build-candidate` | `src/c2/c2_fca6_init_enemy_sprite_color_wave_entry_from_palette.asm` | `C2:FCA6..C2:FD99` | 243 | 243 | 0 | `3baeeb5b7cbf5c692f7f737d2d94a614203fe1c7` |
| `build-candidate` | `src/c2/c2_fd99_advance_enemy_sprite_color_wave_palettes.asm` | `C2:FD99..C2:FEF9` | 352 | 352 | 0 | `3ba9e40ebabf91b5102874cc692b58d403672331` |
| `build-candidate` | `src/c2/c2_fef9_load_or_dim_battle_palette_set.asm` | `C2:FEF9..C2:FF9A` | 161 | 161 | 0 | `7687b0ba8d46738a1579d027b2d431468b75c23c` |
| `build-candidate` | `src/c2/c2_f121_assign_enemy_battle_sprite_rows_and_xpositions.asm` | `C2:F121..C2:F8F9` | 2008 | 2008 | 0 | `2b74be570cc514b7a6510d5ea3ea15562ea85b04` |
| `build-candidate` | `src/c2/c2_a658_run_bomb_common_splash_damage.asm` | `C2:A658..C2:A818` | 448 | 448 | 0 | `eb4789cd52d300df80f283e8458d037bfddd12f2` |
| `build-candidate` | `src/c2/c2_a818_run_bomb_action.asm` | `C2:A818..C2:A821` | 9 | 9 | 0 | `1e9740bf7af493743418af2973c2751fb346be4a` |
| `build-candidate` | `src/c2/c2_eee7_load_battle_group_enemy_sprites.asm` | `C2:EEE7..C2:F09F` | 440 | 440 | 0 | `d90f82284ea4ff97209aa87ff00be53f77e73602` |
| `build-candidate` | `src/c2/c2_a3d1_run_item_side_concentration_seal_action.asm` | `C2:A3D1..C2:A5EC` | 539 | 539 | 0 | `5f95d2e804a71b2204e65bc17dc9594c7ed013f4` |
| `build-candidate` | `src/c2/c2_c14e_run_rainbow_colors_special_event.asm` | `C2:C14E..C2:C37A` | 556 | 556 | 0 | `a65418985434c4a963bae71317844aaf204ada1d` |
| `build-candidate` | `src/c2/c2_e8c4_start_battle_swirl_overlay_and_record_mode.asm` | `C2:E8C4..C2:E9ED` | 297 | 297 | 0 | `5d6f2207f3a55bcb7dfafd7183bdd28752c98eb4` |
| `build-candidate` | `src/c2/c2_b573_apply_battle_luck_increase_consequence.asm` | `C2:B573..C2:B6EB` | 376 | 376 | 0 | `de54a2ec2bb134e608b22be48ed9e8e1f9404398` |
| `build-candidate` | `src/c2/c2_e9ed_clear_battle_swirl_overlay_state.asm` | `C2:E9ED..C2:EACF` | 226 | 226 | 0 | `fe4cda489957d5127f2c7ad2bece54366b91436c` |
| `build-candidate` | `src/c2/c2_03c3_compose_party_member_hp_pp_window_tiles.asm` | `C2:03C3..C2:077D` | 954 | 954 | 0 | `51d7a525a73117a11a2b536c9e08be1735e624c9` |
| `build-candidate` | `src/c2/c2_07e1_clear_party_hp_pp_window_tiles.asm` | `C2:07E1..C2:087C` | 155 | 155 | 0 | `3f05438cf373c96faa99ea073fd8f30a4037311c` |
| `build-candidate` | `src/c2/c2_0a20_snapshot_managed_text_event_slot_state.asm` | `C2:0A20..C2:0ABC` | 156 | 156 | 0 | `a1f8c3ccb4770f87e8f1dbb365315d9cf20d3574` |
| `build-candidate` | `src/c2/c2_0abc_restore_managed_text_event_slot_state.asm` | `C2:0ABC..C2:0B65` | 169 | 169 | 0 | `923b9cf34a4137d9a46284126a9695bda8811c79` |
| `build-candidate` | `src/c2/c2_b342_apply_battle_hp_recovery_consequence.asm` | `C2:B342..C2:B360` | 30 | 30 | 0 | `3fab5a3d5bd1a931451b8871928e9bf1a3bde023` |
| `build-candidate` | `src/c2/c2_b360_apply_battle_pp_recovery_consequence.asm` | `C2:B360..C2:B3D8` | 120 | 120 | 0 | `ba9ca311997ccd806d6bd48cc902f2d663986865` |
| `build-candidate` | `src/c2/c2_b3d8_apply_battle_iq_increase_consequence.asm` | `C2:B3D8..C2:B43F` | 103 | 103 | 0 | `2a5c1699c4bc7ac22158bad798d698462c294e3f` |
| `build-candidate` | `src/c2/c2_b43f_apply_battle_guts_increase_consequence.asm` | `C2:B43F..C2:B4A6` | 103 | 103 | 0 | `89e5065aff0fa13ebbe9dd6bc7eefbcf257af8b6` |
| `build-candidate` | `src/c2/c2_b4a6_apply_battle_speed_increase_consequence.asm` | `C2:B4A6..C2:B50D` | 103 | 103 | 0 | `db300be073dd7cc39ffb44b949be57180cdb13b1` |
| `build-candidate` | `src/c2/c2_b50d_apply_battle_vitality_increase_consequence.asm` | `C2:B50D..C2:B573` | 102 | 102 | 0 | `8c15b9cbf2678a76fe37e4215177655f44aae937` |
| `build-candidate` | `src/c2/c2_c37a_run_final_prayer_stage_transition.asm` | `C2:C37A..C2:C3E2` | 104 | 104 | 0 | `63ceed81816707c83e3031b65029d01b4dc349a7` |
| `build-candidate` | `src/c2/c2_c3e2_apply_final_prayer_damage_step.asm` | `C2:C3E2..C2:C41F` | 61 | 61 | 0 | `30a6c99b0d9e62e6f64f318486b5e3dc13337a8f` |
| `build-candidate` | `src/c2/c2_09a0_close_and_clear_current_window_tilemap.asm` | `C2:09A0..C2:0A20` | 128 | 128 | 0 | `a2ad845571b082dce16a84129d4174f16a0bf18f` |
| `build-candidate` | `src/c2/c2_260d_setup_bracelet_equipment_preview_block.asm` | `C2:260D..C2:2673` | 102 | 102 | 0 | `f4c7796928b376b92c1fd2fd626fa00959aff15e` |
| `build-candidate` | `src/c2/c2_b2e0_dispatch_battle_stat_change_consequence.asm` | `C2:B2E0..C2:B342` | 98 | 98 | 0 | `2adf850f7a2961fe6232bb82314c4cf8c0d1198c` |
| `build-candidate` | `src/c2/c2_2562_setup_weapon_equipment_preview_block.asm` | `C2:2562..C2:25AC` | 74 | 74 | 0 | `bdf83b54a0569478ee8705dce0b2d965772e3f5d` |
| `build-candidate` | `src/c2/c2_25ac_setup_charm_equipment_preview_block.asm` | `C2:25AC..C2:260D` | 97 | 97 | 0 | `28ebcf030315d446aa420aa733a4437c60927ea1` |
| `build-candidate` | `src/c2/c2_2673_setup_headgear_equipment_preview_block.asm` | `C2:2673..C2:26C5` | 82 | 82 | 0 | `cf8033dabde9bafd1722742450b222a03f5a5105` |
| `build-candidate` | `src/c2/c2_b6eb_initialize_enemy_battler_stats_from_enemy_id.asm` | `C2:B6EB..C2:B930` | 581 | 581 | 0 | `62e250a44ea1ce87e12e0dd238301597a4c51e84` |
| `build-candidate` | `src/c2/c2_bcb9_apply_battler_pp_target_loss.asm` | `C2:BCB9..C2:BD13` | 90 | 90 | 0 | `611ed76fd2511c7777a27280c9f1ce88dd4907ee` |
| `build-candidate` | `src/c2/c2_077d_redraw_dirty_party_hp_pp_windows.asm` | `C2:077D..C2:07B6` | 57 | 57 | 0 | `d28488e532e7d132bd37cc1e2e936f1da228783d` |
| `build-candidate` | `src/c2/c2_07b6_mark_and_redraw_party_hp_pp_window.asm` | `C2:07B6..C2:07E1` | 43 | 43 | 0 | `217fcfac31b685fbfc33f5f89c190f31e2ea55c4` |
| `build-candidate` | `src/c2/c2_c572_run_final_prayer_opening_transition.asm` | `C2:C572..C2:C5D1` | 95 | 95 | 0 | `9d5370808e4ee3994e171f8cac9f0a1465f4c95b` |
| `build-candidate` | `src/c2/c2_c5d1_run_final_prayer_damage_phase2.asm` | `C2:C5D1..C2:C5FA` | 41 | 41 | 0 | `e59dafc1562690bf7315ccf383acd5281e339581` |
| `build-candidate` | `src/c2/c2_c623_run_final_prayer_damage_phase4.asm` | `C2:C623..C2:C64C` | 41 | 41 | 0 | `60e6d7313b99dbe9c424a30662ed05c017c117df` |
| `build-candidate` | `src/c2/c2_c5fa_run_final_prayer_damage_phase3.asm` | `C2:C5FA..C2:C623` | 41 | 41 | 0 | `75f644efba902bb2143f891bd28b1748999809d7` |
| `build-candidate` | `src/c2/c2_c64c_run_final_prayer_damage_phase5.asm` | `C2:C64C..C2:C675` | 41 | 41 | 0 | `c9b1a18a4c1ce4818fdd34d55706374c5edef93e` |
| `build-candidate` | `src/c2/c2_c675_run_final_prayer_damage_phase6.asm` | `C2:C675..C2:C69E` | 41 | 41 | 0 | `9f92e9a6e10c43fa6299c812b17b2a0dde7140c9` |
| `build-candidate` | `src/c2/c2_c69e_run_final_prayer_damage_phase7.asm` | `C2:C69E..C2:C6D0` | 50 | 50 | 0 | `904122ef59afcc10946edfde4cb2dd7608f35e6e` |
| `build-candidate` | `src/c2/c2_c6d0_run_final_prayer_narrative_phase8.asm` | `C2:C6D0..C2:C6F0` | 32 | 32 | 0 | `e927376cc80fa997fc95c6c75f0cf57466f114ca` |
| `build-candidate` | `src/c2/c2_087c_refresh_dirty_hp_pp_and_open_text_windows.asm` | `C2:087C..C2:08B8` | 60 | 60 | 0 | `4672e2ffa90fe13791a4b1d26e4b614d36661244` |
| `build-candidate` | `src/c2/c2_a5ec_run_damage_plus_solidification_item_action.asm` | `C2:A5EC..C2:A630` | 68 | 68 | 0 | `23d21ef3b83915e258ef775132e9cde1e36e4f58` |
| `build-candidate` | `src/c2/c2_239d_check_party_overlay_registry_presence.asm` | `C2:239D..C2:23D9` | 60 | 60 | 0 | `6ccc335d8f93cf8d6c0c90e63267801e0be5a1bd` |
| `build-candidate` | `src/c2/c2_fade_reset_enemy_sprite_color_wave_slot.asm` | `C2:FADE..C2:FB35` | 87 | 87 | 0 | `587d68892574c9f96398aaa98ff3af6b87740838` |
| `build-candidate` | `src/c2/c2_fb35_enemy_sprite_color_wave_comparison_helper.asm` | `C2:FB35..C2:FCA6` | 369 | 369 | 0 | `62c3a4aeff7a4ebe2237a8144b17a2bec440259a` |
| `build-candidate` | `src/c2/c2_a630_apply_solidification_status_from_item_action.asm` | `C2:A630..C2:A658` | 40 | 40 | 0 | `a471b85d72bdca251180eae9c2374c32e22e0b95` |
| `build-candidate` | `src/c2/c2_30f3_snapshot_respawn_warp_target_state.asm` | `C2:30F3..C2:3109` | 22 | 22 | 0 | `907ed58d9fa1d060c13ea09a117dbedb846ec6b4` |
| `build-candidate` | `src/c2/c2_eacf_wait_for_battle_effect_step_ready.asm` | `C2:EACF..C2:EAEA` | 27 | 27 | 0 | `93d8938ac585564fef7148b87772c3ad5ae08606` |
| `build-candidate` | `src/c2/c2_eaea_build_battle_sprite_allocation_record.asm` | `C2:EAEA..C2:EEE7` | 1021 | 1021 | 0 | `ddcebdff5ebe85a8df7027e570da4c501521e5d3` |
| `build-candidate` | `src/c2/c2_e6b6_advance_psi_animation_frame_and_palette_state_body.asm` | `C2:E6B6..C2:E8C4` | 526 | 526 | 0 | `e34837d8901574e60780425aca0172e03b14439b` |
| `build-candidate` | `src/c2/c2_a821_run_super_bomb_action.asm` | `C2:A821..C2:A82A` | 9 | 9 | 0 | `2345d8e131f349896847a78ded4e15baa00b53ba` |
| `build-candidate` | `src/c2/c2_a82a_run_solidification_item_action.asm` | `C2:A82A..C2:A86B` | 65 | 65 | 0 | `aa075d307cfe595fcea3bd4283be119d81e78e01` |
| `build-candidate` | `src/c2/c2_a86b_run_random_damage_item_action.asm` | `C2:A86B..C2:A89D` | 50 | 50 | 0 | `835c11d6c075cd8a33e19a029e9e620e5a6e44b6` |
| `build-candidate` | `src/c2/c2_c41f_run_final_prayer_narrative_transition.asm` | `C2:C41F..C2:C572` | 339 | 339 | 0 | `7eccb44161553feb7226bdd2045e6845caad0a89` |
| `build-candidate` | `src/c2/c2_3109_battle_start_ufo_present_fallback_table.asm` | `C2:3109..C2:311B` | 18 | 18 | 0 | `c8b08aa7771c58023987eb637dcbc4dbf4d7059d` |
| `build-candidate` | `src/c2/c2_311b_run_battle_start_present_and_message_controller.asm` | `C2:311B..C2:3B66` | 2635 | 2635 | 0 | `3d21502b50210548ec086cee108e3d29baed6c91` |
| `build-candidate` | `src/c2/c2_4a80_populate_candidate_pool_from_variable_sources.asm` | `C2:4A8A..C2:4F03` | 1145 | 1145 | 0 | `8a7f68f676e009f7bbac2c4278c24c0ae263eae1` |
| `build-candidate` | `src/c2/c2_c6f0_run_final_prayer_finale_opening_sequence.asm` | `C2:C6F0..C2:C8C8` | 472 | 472 | 0 | `c478211b7da9a0b19b80d31f8c4ccffbecefb52b` |
| `build-candidate` | `src/c2/c2_c8c8_load_final_prayer_finale_tilemap_state.asm` | `C2:C8C8..C2:C92D` | 101 | 101 | 0 | `1009db7a1d3f82eb4a54850a63a55b1768736d3f` |
| `build-candidate` | `src/c2/c2_c92d_run_final_prayer_finale_record_player.asm` | `C2:C92D..C2:CFE5` | 1720 | 1720 | 0 | `a2cc4ad68243db8698c60ba418d498cf8704ad54` |
| `build-candidate` | `src/c2/c2_0000_run_enemy_sunstroke_check.asm` | `C2:0000..C2:00B9` | 185 | 185 | 0 | `7484cfe62d6290f05b8f8001f4c2d4449ab0c3b7` |
| `build-candidate` | `src/c2/c2_e6b3_advance_psi_animation_frame_and_palette_state.asm` | `C2:E6B3..C2:E6B6` | 3 | 3 | 0 | `bbe0b447f3ad331c5d2dea6e8427616cbeb3fad3` |
| `build-candidate` | `src/c2/c2_00b9_enemy_sunstroke_check_tail_table.asm` | `C2:00B9..C2:00D1` | 24 | 24 | 0 | `75a9edd41e20424692e7316f41089221943db36d` |
| `build-candidate` | `src/c2/c2_ff9a_check_overworld_position_hash_threshold3_of8.asm` | `C2:FF9A..C2:FFB7` | 29 | 29 | 0 | `01f3eba585197ed867b08215dcb451fdf14fe689` |
| `build-candidate` | `src/c2/c2_ffb7_bank_end_tail_bytes.asm` | `C2:FFB7..C2:10000` | 73 | 73 | 0 | `1c412f0192010672dd5fee00abab964a2d7c4ae0` |
| `build-candidate` | `src/c2/c2_4f52_display_battle_start_status_messages_prelude.asm` | `C2:4F52..C2:5024` | 210 | 210 | 0 | `fd47beb74efa1622b453be654b82dfea4537a867` |
| `build-candidate` | `src/c2/c2_5024_run_battle_start_candidate_controller_front.asm` | `C2:5024..C2:5AFB` | 2775 | 2775 | 0 | `0c1d2a45e872dea11815b6d4dbea0c4a83a68c75` |
| `build-candidate` | `src/c2/c2_5afb_run_battle_start_candidate_controller_back.asm` | `C2:5AFB..C2:6189` | 1678 | 1678 | 0 | `033d92dfe09c64c4776503f6a84f79796712a8cc` |
| `build-candidate` | `src/c2/c2_7eaf_run_hit_resolution_and_status_action_cluster.asm` | `C2:7EAF..C2:8BBE` | 3343 | 3343 | 0 | `dfdbfd2dee94e88503837814120b99558732c6b9` |
| `build-candidate` | `src/c2/c2_7e8a_swap_reflected_hit_battle_text_contexts.asm` | `C2:7E8A..C2:7EAF` | 37 | 37 | 0 | `b6e7b544690f27feb9d7dc08c49c79197b36d686` |
| `build-candidate` | `src/c2/c2_a89d_run_random_damage_and_status_item_action_cluster.asm` | `C2:A89D..C2:AF1F` | 1666 | 1666 | 0 | `ec15972f3bcddaf42126362dd29d9261c2855b77` |
| `build-candidate` | `src/c2/c2_e0e7_clear_battle_visual_flash_state_and_layer_config.asm` | `C2:E0E7..C2:E116` | 47 | 47 | 0 | `e9d3c634cbc793297b67aa4d8584f74f0bcf0d4f` |
| `build-candidate` | `src/c2/c2_e116_run_battle_visual_flash_and_bg_effect_body.asm` | `C2:E116..C2:E6B3` | 1437 | 1437 | 0 | `35130b0d39bacf3bec99b7f6c3ae91fff471cafc` |
| `build-candidate` | `src/c2/c2_bd13_sum_active_enemy_battle_sprite_widths.asm` | `C2:BD13..C2:BE6C` | 345 | 345 | 0 | `bb336f4b4c29e8831a78fd512a6783bad3ca1278` |
| `build-candidate` | `src/c2/c2_be6c_run_call_for_help_enemy_selection_body.asm` | `C2:BE6C..C2:C14E` | 738 | 738 | 0 | `bdd6c46a5469cdb96816503832c804821cfd38a2` |
| `build-candidate` | `src/c2/c2_af1f_snapshot_restore_battler_normalization_context.asm` | `C2:AF1F..C2:B172` | 595 | 595 | 0 | `2ea5b40ff9f3adbfd49c20d4b397a06c02b36754` |
| `build-candidate` | `src/c2/c2_b172_resolve_late_normalization_and_odor_continuation.asm` | `C2:B172..C2:B2E0` | 366 | 366 | 0 | `85149acdd32679cb7a87270a617c28eefabfc82a` |
| `build-candidate` | `src/c2/c2_dae3_prime_layer1_battle_bg_distortion_swap.asm` | `C2:DAE3..C2:DB14` | 49 | 49 | 0 | `9d76ff9f6899f269f75131b221aee5ed4d546d42` |
| `build-candidate` | `src/c2/c2_db14_run_battle_bg_per_frame_update_body.asm` | `C2:DB14..C2:DE0F` | 763 | 763 | 0 | `8a4969e92a2374858f5905a438ee8c7cf2e635a6` |
| `build-candidate` | `src/c2/c2_d0ac_build_battle_letterbox_hdma_table.asm` | `C2:D0AC..C2:D121` | 117 | 117 | 0 | `3c958c36f7fa8bc6692a21249693f7c47c3601ff` |
| `build-candidate` | `src/c2/c2_d121_load_battle_background_main_body.asm` | `C2:D121..C2:DAE3` | 2498 | 2498 | 0 | `798e627a3322494fee1906c710dc10c32d8688c8` |
| `build-candidate` | `src/c2/c2_00d1_window_reset_initial_coordinate_data.asm` | `C2:00D1..C2:0266` | 405 | 405 | 0 | `3b7ab9780392e0bf909597d9b089c155fa7b08ed` |
| `build-candidate` | `src/c2/c2_0912_name_entry_grid_character_offset_table.asm` | `C2:0912..C2:0958` | 70 | 70 | 0 | `6ce618d3151cf264c9f3bff6ba718590ccfd5172` |
| `build-candidate` | `src/c2/c2_0958_menu_or_name_entry_mask_table.asm` | `C2:0958..C2:09A0` | 72 | 72 | 0 | `1576e7ce0b6915b7b2bdbf15c9b82646475d71e6` |

## Source Segments

### `src/c2/c2_3b66_expand_battle_text_context_template.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:3B66..C2:3BCF` | 105 | `ExpandBattleTextContextTemplate` | `6675b052cdcad4ef4a19e595c4d76027a36bb8d9` |

Labels:

- `C2:3B66 ExpandBattleTextContextTemplate`

Evidence:

- `notes/class2-reflected-hit-context-rebuild.md`
- `notes/class2-battle-text-cluster-overview.md`

### `src/c2/c2_3bcf_build_battle_attacker_text_context.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:3BCF..C2:3D05` | 310 | `BuildBattleAttackerTextContext` | `3c2503b7ce63be657e1f00cbe2f3a74d7d6359d6` |

Labels:

- `C2:3BCF BuildBattleAttackerTextContext`

Evidence:

- `notes/class2-concrete-battle-text-call-paths.md`
- `notes/class2-reflected-hit-context-rebuild.md`
- `notes/battle-text-context-buffer-family-c1ac4a-ad42.md`

### `src/c2/c2_7680_display_enemy_death_text.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:7680..C2:77CA` | 330 | `DisplayEnemyDeathText` | `d5300c4ae8a5bbfe33b9776f3bf39f383232bb90` |

Labels:

- `C2:7680 DisplayEnemyDeathText`

Evidence:

- `notes/class2-concrete-battle-text-call-paths.md`
- `notes/class2-enemy-text-pointer-consumers.md`
- `notes/class2-battle-text-cluster-overview.md`

### `src/c2/c2_3d05_build_battle_target_text_context.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:3D05..C2:40A4` | 927 | `BuildBattleTargetTextContext` | `2675308b9fb4fea353357dd65b039f2472b0d2e4` |

Labels:

- `C2:3D05 BuildBattleTargetTextContext`

Evidence:

- `notes/class2-reflected-hit-context-rebuild.md`
- `notes/class2-reflected-hit-text-context.md`
- `notes/class2-concrete-battle-text-call-paths.md`
- `notes/battle-text-context-buffer-family-c1ac4a-ad42.md`

### `src/c2/c2_40a4_apply_battle_action_second_pointer_payload.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:40A4..C2:416F` | 203 | `ApplyBattleActionSecondPointerPayload` | `2c4bd5fb86417c05726cc6d8e68f66546e08ce33` |
| `C2:416F..C2:41DC` | 109 | `FilterBattleActionTargetMaskByRowState` | `05fcc4876ca14a8df1f3c5c638a3cd663c7d33fc` |

Labels:

- `C2:40A4 ApplyBattleActionSecondPointerPayload`
- `C2:416F FilterBattleActionTargetMaskByRowState`

Evidence:

- `notes/class2-second-pointer-consumer-40a4.md`
- `notes/class2-d57b68-battle-action-table-match.md`
- `notes/class2-psi-thunder-common-local-flow.md`
- `notes/class2-handoff-4477-4703.md`

### `src/c2/c2_41dc_build_stealable_item_candidate_list.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:41DC..C2:4316` | 314 | `BuildStealableItemCandidateList` | `59c553a31ec75c1aa78823924d7f6cabc873a12a` |

Labels:

- `C2:41DC BuildStealableItemCandidateList`

Evidence:

- `notes/c2-steal-and-target-selection-helpers-c241dc-c24434.md`
- `notes/class2-d57b68-battle-action-table-match.md`

### `src/c2/c2_4316_select_stealable_item_candidate.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:4316..C2:4348` | 50 | `SelectStealableItemCandidate` | `10e5c70abce5b7ca58fedddfa6e299e71f296445` |

Labels:

- `C2:4316 SelectStealableItemCandidate`

Evidence:

- `notes/c2-steal-and-target-selection-helpers-c241dc-c24434.md`
- `refs/ebsrc-main/ebsrc-main/src/battle/select_stealable_item.asm`

### `src/c2/c2_4348_is_pending_steal_item_still_stealable.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:4348..C2:437E` | 54 | `IsPendingStealItemStillStealable` | `41385bbadc0087440e747af3b6e4513202bf9c0e` |

Labels:

- `C2:4348 IsPendingStealItemStillStealable`

Evidence:

- `notes/c2-steal-and-target-selection-helpers-c241dc-c24434.md`
- `notes/class2-d57b68-battle-action-table-match.md`

### `src/c2/c2_4434_pick_random_battler_from_front_back_rows.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:4434..C2:4477` | 67 | `PickRandomBattlerFromFrontBackRows` | `641e45a2ba5791621e230a8a22d2c1d4e229c7ed` |

Labels:

- `C2:4434 PickRandomBattlerFromFrontBackRows`

Evidence:

- `notes/c2-steal-and-target-selection-helpers-c241dc-c24434.md`
- `refs/ebsrc-main/ebsrc-main/src/battle/choose_target.asm`

### `src/c2/c2_437e_apply_pending_stolen_item_slot_if_still_valid.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:437E..C2:4434` | 182 | `ApplyPendingStolenItemSlotIfStillValid` | `6eb8312e9ce40d1c9d2460c0f87a1f4187334c59` |

Labels:

- `C2:437E ApplyPendingStolenItemSlotIfStillValid`

Evidence:

- `notes/c2-steal-and-target-selection-helpers-c241dc-c24434.md`
- `notes/class2-d57b68-battle-action-table-match.md`

### `src/c2/c2_4477_build_class2_derived_action_code.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:4477..C2:4703` | 652 | `BuildClass2DerivedActionCode` | `90375f81c83d98af7a84d7c0c17545a07f86bb9b` |

Labels:

- `C2:4477 BuildClass2DerivedActionCode`

Evidence:

- `notes/class2-handoff-4477-4703.md`
- `notes/class2-candidate-population-and-ranking.md`
- `notes/class2-mask-helper-family.md`

### `src/c2/c2_4703_dispatch_class2_derived_action.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:4703..C2:4821` | 286 | `DispatchClass2DerivedAction` | `aa9a16538f982aa85684d52d66d8cbc9f8f1e719` |
| `C2:4821..C2:4958` | 311 | `InitializeClass2CandidateVisualState` | `20bc9195e8470edef30f5b4aa2c053040e5fbc58` |

Labels:

- `C2:4703 DispatchClass2DerivedAction`
- `C2:4821 InitializeClass2CandidateVisualState`

Evidence:

- `notes/class2-handoff-4477-4703.md`
- `notes/class2-candidate-population-and-ranking.md`
- `notes/class2-mask-helper-family.md`
- `notes/c2-battle-sprite-render-and-palette-tail-c2eee7-c2ff9a.md`

### `src/c2/c2_4958_populate_candidate_pool_from_six_sources.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:4958..C2:4A8A` | 306 | `PopulateCandidatePoolFromSixSources` | `ed785bb609e5fde164454f33167ffd8d12bddcee` |

Labels:

- `C2:4958 PopulateCandidatePoolFromSixSources`

Evidence:

- `notes/class2-candidate-population-and-ranking.md`
- `notes/class2-source-families-986f-9f8a.md`
- `notes/c2-battle-sprite-render-and-palette-tail-c2eee7-c2ff9a.md`

### `src/c2/c2_4f00_display_battle_encounter_text.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:4F03..C2:4F52` | 79 | `DisplayBattleEncounterText` | `634310e6d353555b7f5a8cc1933c6081fb04c8d7` |

Labels:

- `C2:4F03 DisplayBattleEncounterText`

Evidence:

- `notes/class2-candidate-population-and-ranking.md`
- `notes/class2-concrete-battle-text-call-paths.md`
- `boundary repaired from unsafe C2:4F00 split`

### `src/c2/c2_6e77_mask_set_remove_active_typed_candidates.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:6E77..C2:6EF8` | 129 | `MaskSet_RemoveActiveTypedCandidates` | `57e74200edc7ed8e40261c790393e6d0664f8b06` |

Labels:

- `C2:6E77 MaskSet_RemoveActiveTypedCandidates`

Evidence:

- `notes/class2-mask-helper-family.md`
- `notes/class2-handoff-4477-4703.md`

### `src/c2/c2_6c82_mask_set_build_phase1_candidates.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:6C82..C2:6D04` | 130 | `MaskSet_BuildPhase1Candidates` | `dff94669b62b4eafd5aa336890c647f0a025afb1` |
| `C2:6D04..C2:6E77` | 371 | `MaskSet_BuildMetadataMatchedCandidates` | `1801ff7362b625a13cdb33b2932543a843c24533` |

Labels:

- `C2:6C82 MaskSet_BuildPhase1Candidates`
- `C2:6D04 MaskSet_BuildMetadataMatchedCandidates`

Evidence:

- `notes/class2-mask-helper-family.md`
- `notes/class2-handoff-4477-4703.md`

### `src/c2/c2_6bfb_mask_set_build_active_typed_candidates.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:6BFB..C2:6C82` | 135 | `MaskSet_BuildActiveTypedCandidates` | `ba0a435960dca30be0282b1087d12b9fe3533159` |

Labels:

- `C2:6BFB MaskSet_BuildActiveTypedCandidates`

Evidence:

- `notes/class2-mask-helper-family.md`
- `notes/class2-handoff-4477-4703.md`

### `src/c2/c2_6ef8_mask_set_find_first_match_in_range.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:6EF8..C2:6FDC` | 228 | `MaskSet_FindFirstMatchInRange` | `0b83af9b6038720da1ceed83a8bf9a635cdaca49` |

Labels:

- `C2:6EF8 MaskSet_FindFirstMatchInRange`

Evidence:

- `notes/class2-mask-helper-family.md`
- `notes/class2-handoff-4477-4703.md`

### `src/c2/c2_6fdc_mask_set_add_bit.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:6FDC..C2:7029` | 77 | `MaskSet_AddBit` | `39324f95ded7b3cb72caedf786b54461de729cdd` |

Labels:

- `C2:6FDC MaskSet_AddBit`

Evidence:

- `notes/class2-mask-helper-family.md`
- `notes/class2-handoff-4477-4703.md`

### `src/c2/c2_7089_mask_set_clear_bit.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:7089..C2:70E4` | 91 | `MaskSet_ClearBit` | `48b5a1cca09f89908f3be95510946f19b5687128` |

Labels:

- `C2:7089 MaskSet_ClearBit`

Evidence:

- `notes/class2-mask-helper-family.md`
- `notes/class2-handoff-4477-4703.md`

### `src/c2/c2_70e4_mask_set_prune_flagged_candidates.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:70E4..C2:724A` | 358 | `MaskSet_PruneFlaggedCandidates` | `3277f7e8e4c35c91764c85713b97556e02885f62` |

Labels:

- `C2:70E4 MaskSet_PruneFlaggedCandidates`

Evidence:

- `notes/class2-mask-helper-family.md`
- `notes/class2-handoff-4477-4703.md`
- `notes/class2-post-selection-controller-phases.md`

### `src/c2/c2_7029_mask_set_test_bit.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:7029..C2:7089` | 96 | `MaskSet_TestBit` | `669babe12074d5683714f5389cccc6ca6e7af917` |

Labels:

- `C2:7029 MaskSet_TestBit`

Evidence:

- `notes/class2-mask-helper-family.md`
- `notes/class2-handoff-4477-4703.md`

### `src/c2/c2_724a_apply_battler_affliction_subgroup_value.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:724A..C2:7294` | 74 | `ApplyBattlerAfflictionSubgroupValue` | `e1d44cd6346f1fc8cc38e6b1bb1e91b650692be2` |

Labels:

- `C2:724A ApplyBattlerAfflictionSubgroupValue`

Evidence:

- `notes/class2-affliction-apply-helper-724a.md`
- `notes/class2-battler-affliction-crosswalk.md`
- `notes/class2-psi-flash-common-local-flow.md`

### `src/c2/c2_7294_apply_battler_hp_recovery_feedback.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:7294..C2:7318` | 132 | `ApplyBattlerHpRecoveryFeedback` | `b3546d2012e23968620fe24ff3d23b7a4d9db08c` |

Labels:

- `C2:7294 ApplyBattlerHpRecoveryFeedback`

Evidence:

- `notes/class2-healing-amount-family-c29ab8-c29ae1.md`
- `notes/class2-post-selection-controller-phases.md`
- `notes/battle-action-stat-change-family-c2b2e0-b5d7.md`

### `src/c2/c2_7318_apply_battler_pp_recovery_feedback.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:7318..C2:7397` | 127 | `ApplyBattlerPpRecoveryFeedback` | `d79f829cab66d44e051b8bf57425424fa4964d1e` |

Labels:

- `C2:7318 ApplyBattlerPpRecoveryFeedback`

Evidence:

- `notes/class2-post-selection-controller-phases.md`
- `notes/battle-action-stat-change-family-c2b2e0-b5d7.md`

### `src/c2/c2_7397_install_battler_heavy_recovery_reset.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:7397..C2:7550` | 441 | `InstallBattlerHeavyRecoveryReset` | `58d49e3b90a757a77ff0e4495117ec8753136ec6` |

Labels:

- `C2:7397 InstallBattlerHeavyRecoveryReset`

Evidence:

- `notes/class2-post-selection-controller-phases.md`
- `notes/battle-affliction-recovery-family-c29aea-a39d.md`
- `notes/class2-second-stage-selector-a970.md`

### `src/c2/c2_7550_start_selected_battler_collapse_affliction_path.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:7550..C2:7680` | 304 | `StartSelectedBattlerCollapseAfflictionPath` | `342b96f687b5344f6c7d17a59192e9090cd4cb1c` |

Labels:

- `C2:7550 StartSelectedBattlerCollapseAfflictionPath`

Evidence:

- `notes/class2-post-selection-controller-phases.md`
- `notes/class2-slot-fields-and-transition-start.md`
- `notes/class2-psi-flash-common-local-flow.md`

### `src/c2/c2_77ca_run_class2_late_selected_row_controller.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:77CA..C2:7C96` | 1228 | `RunClass2LateSelectedRowController` | `20ffa0148ddbb7ac99aae477100fcf147c012521` |
| `C2:7C96..C2:7CAF` | 25 | `RollSelectedRowThresholdGate` | `78e0ef2c4f58ea20772a5f03d47046434c4ce07c` |
| `C2:7CAF..C2:7CFD` | 78 | `RollSelectedVsActiveRowOffsetGate` | `eaa669b3ef02a6e66ddcc9b2d70b2a55ef7d7865` |

Labels:

- `C2:77CA RunClass2LateSelectedRowController`
- `C2:7C96 RollSelectedRowThresholdGate`
- `C2:7CAF RollSelectedVsActiveRowOffsetGate`

Evidence:

- `notes/class2-late-controller-path-77ca.md`
- `notes/class2-post-selection-controller-phases.md`
- `notes/class2-descriptor-field-4e-and-d57b68.md`

### `src/c2/c2_7cfd_check_selected_battler_default_text_blocker.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:7CFD..C2:7D28` | 43 | `CheckSelectedBattlerDefaultTextBlocker` | `b77bee558175265bb1b6e701c682c69c7f6b612a` |

Labels:

- `C2:7CFD CheckSelectedBattlerDefaultTextBlocker`

Evidence:

- `notes/class2-state-machine-99xx.md`
- `notes/class2-slot-fields-and-transition-start.md`

### `src/c2/c2_7d28_apply_bounded_offense_increase.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:7D28..C2:7D82` | 90 | `ApplyBoundedOffenseIncrease` | `bd676368956360c38af19afcc5a9c4abbb5ee471` |

Labels:

- `C2:7D28 ApplyBoundedOffenseIncrease`

Evidence:

- `notes/class2-bounded-offense-defense-helpers-c27d28-c27e33.md`
- `notes/class2-late-stat-and-resource-family-c28e42-c29e38.md`

### `src/c2/c2_7d82_apply_bounded_defense_increase.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:7D82..C2:7DDC` | 90 | `ApplyBoundedDefenseIncrease` | `18d94f65668cfe8b5557a86aaf10107d1aea55cb` |

Labels:

- `C2:7D82 ApplyBoundedDefenseIncrease`

Evidence:

- `notes/class2-bounded-offense-defense-helpers-c27d28-c27e33.md`
- `notes/class2-late-stat-and-resource-family-c28e42-c29e38.md`

### `src/c2/c2_7e33_apply_bounded_defense_decrease.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:7E33..C2:7E8A` | 87 | `ApplyBoundedDefenseDecrease` | `27152828b8df1c2cb1e2242b5127a4f84a4b58c7` |

Labels:

- `C2:7E33 ApplyBoundedDefenseDecrease`

Evidence:

- `notes/class2-bounded-offense-defense-helpers-c27d28-c27e33.md`
- `notes/class2-late-stat-and-resource-family-c28e42-c29e38.md`

### `src/c2/c2_7ddc_apply_bounded_offense_decrease.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:7DDC..C2:7E33` | 87 | `ApplyBoundedOffenseDecrease` | `a378d3811bcc8d14ac9d703e30b8026311ef5ff0` |

Labels:

- `C2:7DDC ApplyBoundedOffenseDecrease`

Evidence:

- `notes/class2-bounded-offense-defense-helpers-c27d28-c27e33.md`
- `notes/class2-late-stat-and-resource-family-c28e42-c29e38.md`
- `notes/class2-late-normalization-and-odor-family-c29051-c29254.md`

### `src/c2/c2_8bbe_run_mushroomize_status_action.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:8BBE..C2:8BFD` | 63 | `RunMushroomizeStatusAction` | `946232c6e3ea753816fa50c03f4f902d7e183922` |

Labels:

- `C2:8BBE RunMushroomizeStatusAction`

Evidence:

- `notes/class2-persistent-status-action-pair-c28bbe-c28bfd.md`
- `notes/class2-affliction-apply-helper-724a.md`

### `src/c2/c2_8bfd_run_possess_status_action.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:8BFD..C2:8C69` | 108 | `RunPossessStatusAction` | `90860fa5edd6cb68270e10122be7b0dad134de20` |

Labels:

- `C2:8BFD RunPossessStatusAction`

Evidence:

- `notes/class2-persistent-status-action-pair-c28bbe-c28bfd.md`
- `notes/class2-affliction-apply-helper-724a.md`

### `src/c2/c2_8c69_run_crying_status_action.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:8C69..C2:8CB8` | 79 | `RunCryingStatusAction` | `dfeb5fd9be9aa277d29517f06a0a7d5f4d7132d5` |

Labels:

- `C2:8C69 RunCryingStatusAction`

Evidence:

- `notes/class2-temporary-status-action-cluster-c28c69-c28cb8-c28cf1.md`
- `notes/class2-affliction-apply-helper-724a.md`

### `src/c2/c2_8cb8_run_immobilized_status_action.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:8CB8..C2:8CF1` | 57 | `RunImmobilizedStatusAction` | `827b08d890c6a7e3f31f476ec5062ff850c756a2` |

Labels:

- `C2:8CB8 RunImmobilizedStatusAction`

Evidence:

- `notes/class2-temporary-status-action-cluster-c28c69-c28cb8-c28cf1.md`
- `notes/class2-affliction-apply-helper-724a.md`

### `src/c2/c2_8cf1_run_solidified_status_action.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:8CF1..C2:8D3A` | 73 | `RunSolidifiedStatusAction` | `dc47c04c7d412e22c04121e0ebcf24b52de4c377` |

Labels:

- `C2:8CF1 RunSolidifiedStatusAction`

Evidence:

- `notes/class2-temporary-status-action-cluster-c28c69-c28cb8-c28cf1.md`
- `notes/class2-affliction-apply-helper-724a.md`

### `src/c2/c2_8d3a_run_strange_status_wrapper_action.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:8D3A..C2:8D41` | 7 | `RunStrangeStatusWrapperAction` | `37664291fa35b7991fd82860a8e218e7fed66777` |
| `C2:8D41..C2:8D5A` | 25 | `CheckTargetField2eThresholdGate` | `d24d3a33435cf659db8242778a553ddab56037a0` |

Labels:

- `C2:8D3A RunStrangeStatusWrapperAction`
- `C2:8D41 CheckTargetField2eThresholdGate`

Evidence:

- `notes/class2-strange-status-family-c28d3a-c28dbb-c2a056.md`

### `src/c2/c2_8d5a_run_concentration_seal_action.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:8D5A..C2:8DBB` | 97 | `RunConcentrationSealAction` | `a5d857d7ca96aea0ac016b717bec50ddfb6b4e67` |

Labels:

- `C2:8D5A RunConcentrationSealAction`

Evidence:

- `notes/class2-concentration-seal-family-c28d5a-c2a3d1.md`
- `notes/class2-affliction-apply-helper-724a.md`

### `src/c2/c2_8dbb_run_direct_strange_status_action.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:8DBB..C2:8E42` | 135 | `RunDirectStrangeStatusAction` | `11d0beee9e422b1ee02d97d8c233bd7b831f69fc` |

Labels:

- `C2:8DBB RunDirectStrangeStatusAction`

Evidence:

- `notes/class2-strange-status-family-c28d3a-c28dbb-c2a056.md`
- `notes/class2-affliction-apply-helper-724a.md`

### `src/c2/c2_8e42_run_pp_reduction_action.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:8E42..C2:8EAE` | 108 | `RunPpReductionAction` | `16729eeeac6184ede9ded6343550c252286458a2` |

Labels:

- `C2:8E42 RunPpReductionAction`

Evidence:

- `notes/class2-late-stat-and-resource-family-c28e42-c29e38.md`

### `src/c2/c2_8eae_run_guts_reduction_action.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:8EAE..C2:8F21` | 115 | `RunGutsReductionAction` | `d4f3c55e76efb1f2027ca3b0f9012df472b89323` |

Labels:

- `C2:8EAE RunGutsReductionAction`

Evidence:

- `notes/class2-late-stat-and-resource-family-c28e42-c29e38.md`

### `src/c2/c2_8f21_run_offense_defense_reduction_action.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:8F21..C2:8F97` | 118 | `RunOffenseDefenseReductionAction` | `9305b3e203ddff0fd724b9e53f10e457d55c8270` |

Labels:

- `C2:8F21 RunOffenseDefenseReductionAction`

Evidence:

- `notes/class2-late-stat-and-resource-family-c28e42-c29e38.md`

### `src/c2/c2_8f97_run_poison_on_hit_physical_action.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:8F97..C2:8FF9` | 98 | `RunPoisonOnHitPhysicalAction` | `cf20c8351bd302b9f2b7f1f70ad572ee38cd091e` |

Labels:

- `C2:8F97 RunPoisonOnHitPhysicalAction`

Evidence:

- `notes/class2-late-physical-special-family-c28f97-c2900b.md`
- `notes/class2-affliction-apply-helper-724a.md`

### `src/c2/c2_8ff9_run_double_bash_action.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:8FF9..C2:9004` | 11 | `RunDoubleBashAction` | `97d575853a3e20b994656e5759c467c8a11c22e1` |
| `C2:9004..C2:900B` | 7 | `RunSingleBashWrapperAction` | `abbd362e58e62ed5f54bd13ca81cc0c92e36ef23` |

Labels:

- `C2:8FF9 RunDoubleBashAction`
- `C2:9004 RunSingleBashWrapperAction`

Evidence:

- `notes/class2-late-physical-special-family-c28f97-c2900b.md`

### `src/c2/c2_900b_run_fire_damage_action_wrapper.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:900B..C2:902C` | 33 | `RunFireDamageActionWrapper` | `88d0c87988cf91ef90e06a3b2227ec844e8bab2f` |

Labels:

- `C2:900B RunFireDamageActionWrapper`

Evidence:

- `notes/class2-late-physical-special-family-c28f97-c2900b.md`

### `src/c2/c2_902c_run_all_target_physical_flavor_wrapper.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:902C..C2:9033` | 7 | `RunAllTargetPhysicalFlavorWrapper` | `db8604a72b4d8e251e8249636570d3cefa2722a6` |

Labels:

- `C2:902C RunAllTargetPhysicalFlavorWrapper`

Evidence:

- `notes/class2-late-physical-special-family-c28f97-c2900b.md`

### `src/c2/c2_9033_run_flavor_only_no_op_tail.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:9033..C2:9036` | 3 | `RunFlavorOnlyNoOpTail` | `dde45a04b5b3b55e35ad5a3f8beb6e613f9c033a` |
| `C2:9036..C2:9039` | 3 | `RunFlavorOnlyNoOpTail_9036` | `dde45a04b5b3b55e35ad5a3f8beb6e613f9c033a` |
| `C2:9039..C2:903C` | 3 | `RunFlavorOnlyNoOpTail_9039` | `dde45a04b5b3b55e35ad5a3f8beb6e613f9c033a` |
| `C2:903C..C2:903F` | 3 | `RunFlavorOnlyNoOpTail_903C` | `dde45a04b5b3b55e35ad5a3f8beb6e613f9c033a` |
| `C2:903F..C2:9042` | 3 | `RunFlavorOnlyNoOpTail_903F` | `dde45a04b5b3b55e35ad5a3f8beb6e613f9c033a` |
| `C2:9042..C2:9045` | 3 | `RunFlavorOnlyNoOpTail_9042` | `dde45a04b5b3b55e35ad5a3f8beb6e613f9c033a` |
| `C2:9045..C2:9048` | 3 | `RunFlavorOnlyNoOpTail_9045` | `dde45a04b5b3b55e35ad5a3f8beb6e613f9c033a` |
| `C2:9048..C2:904B` | 3 | `RunFlavorOnlyNoOpTail_9048` | `dde45a04b5b3b55e35ad5a3f8beb6e613f9c033a` |
| `C2:904B..C2:904E` | 3 | `RunFlavorOnlyNoOpTail_904B` | `dde45a04b5b3b55e35ad5a3f8beb6e613f9c033a` |

Labels:

- `C2:9033 RunFlavorOnlyNoOpTail`
- `C2:9036 RunFlavorOnlyNoOpTail_9036`
- `C2:9039 RunFlavorOnlyNoOpTail_9039`
- `C2:903C RunFlavorOnlyNoOpTail_903C`
- `C2:903F RunFlavorOnlyNoOpTail_903F`
- `C2:9042 RunFlavorOnlyNoOpTail_9042`
- `C2:9045 RunFlavorOnlyNoOpTail_9045`
- `C2:9048 RunFlavorOnlyNoOpTail_9048`
- `C2:904B RunFlavorOnlyNoOpTail_904B`

Evidence:

- `notes/class2-late-flavor-tail-c2902c-c2904e.md`

### `src/c2/c2_904e_run_late_message_only_no_op_tail.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:904E..C2:9051` | 3 | `RunLateMessageOnlyNoOpTail` | `dde45a04b5b3b55e35ad5a3f8beb6e613f9c033a` |

Labels:

- `C2:904E RunLateMessageOnlyNoOpTail`

Evidence:

- `notes/class2-late-flavor-tail-c2902c-c2904e.md`

### `src/c2/c2_9051_queued_battler_stat_shield_normalization_callback.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:9051..C2:90C6` | 117 | `QueuedBattlerStatShieldNormalizationCallback` | `198b3e0d0cf5559f2997fef5f23a7543555f4c63` |

Labels:

- `C2:9051 QueuedBattlerStatShieldNormalizationCallback`

Evidence:

- `notes/class2-late-normalization-and-odor-family-c29051-c29254.md`

### `src/c2/c2_90c6_run_battler_normalization_action_wrapper.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:90C6..C2:916E` | 168 | `RunBattlerNormalizationActionWrapper` | `9e8ba1aea357f7747d01d1887f10506660bd5acb` |

Labels:

- `C2:90C6 RunBattlerNormalizationActionWrapper`

Evidence:

- `notes/class2-late-normalization-and-odor-family-c29051-c29254.md`

### `src/c2/c2_916e_run_diamondize_action.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:916E..C2:9254` | 230 | `RunDiamondizeAction` | `f81bc108ab9c83d00d541008482d778206e0426c` |

Labels:

- `C2:916E RunDiamondizeAction`

Evidence:

- `notes/class2-late-normalization-and-odor-family-c29051-c29254.md`
- `notes/class2-affliction-apply-helper-724a.md`

### `src/c2/c2_9254_run_odor_offense_reduction_action.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:9254..C2:9298` | 68 | `RunOdorOffenseReductionAction` | `1251a90942e5839fa67116dda09381334cbd9b44` |

Labels:

- `C2:9254 RunOdorOffenseReductionAction`

Evidence:

- `notes/class2-late-normalization-and-odor-family-c29051-c29254.md`

### `src/c2/c2_9298_run_runaway_five_clumsy_robot_special_event.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:9298..C2:92EE` | 86 | `RunRunawayFiveClumsyRobotSpecialEvent` | `1f9db0f11a97093ebce286f393da2f3bb46a287d` |

Labels:

- `C2:9298 RunRunawayFiveClumsyRobotSpecialEvent`

Evidence:

- `notes/class2-special-event-results-c29298-c2c14e.md`

### `src/c2/c2_92ee_run_master_barf_poo_starstorm_special_event.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:92EE..C2:941D` | 303 | `RunMasterBarfPooStarstormSpecialEvent` | `efcd2ac520c0c9b44a61fc405621291630579943` |

Labels:

- `C2:92EE RunMasterBarfPooStarstormSpecialEvent`

Evidence:

- `notes/class2-special-event-results-c29298-c2c14e.md`

### `src/c2/c2_941d_check_selected_battler_timed_substate_blocker.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:941D..C2:94CE` | 177 | `CheckSelectedBattlerTimedSubstateBlocker` | `6d9b79f27fe5f6708cbcdf1bfdf7626937335e6a` |

Labels:

- `C2:941D CheckSelectedBattlerTimedSubstateBlocker`

Evidence:

- `notes/class2-psi-shield-post-hit-aa96.md`
- `notes/class2-psi-thunder-reflection-branch.md`

### `src/c2/c2_94ce_tick_selected_battler_timed_substate_cleanup.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:94CE..C2:9516` | 72 | `TickSelectedBattlerTimedSubstateCleanup` | `a1fae7de8c785c10576daa725cb9377ae2578891` |

Labels:

- `C2:94CE TickSelectedBattlerTimedSubstateCleanup`

Evidence:

- `notes/class2-psi-shield-post-hit-aa96.md`
- `notes/class2-psi-thunder-reflection-branch.md`

### `src/c2/c2_9516_run_psi_rockin_common.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:9516..C2:9556` | 64 | `RunPsiRockinCommon` | `378917eb45e85486f9a1a5dafc739d613f17b254` |
| `C2:9556..C2:955F` | 9 | `RunPsiRockinAlphaWrapper` | `812a6619b156c6c88f568854ec61f714a4cfd697` |
| `C2:955F..C2:9568` | 9 | `RunPsiRockinBetaWrapper` | `22358ab4bb6b91c59db729bb897cc32a332306c7` |
| `C2:9568..C2:9571` | 9 | `RunPsiRockinGammaWrapper` | `72359558f2bf6c2353f8dfe6469f05b821a06268` |
| `C2:9571..C2:957A` | 9 | `RunPsiRockinOmegaWrapper` | `85ba5a0d6ff4def908b7265a0db27e4c32492b3c` |

Labels:

- `C2:9516 RunPsiRockinCommon`
- `C2:9556 RunPsiRockinAlphaWrapper`
- `C2:955F RunPsiRockinBetaWrapper`
- `C2:9568 RunPsiRockinGammaWrapper`
- `C2:9571 RunPsiRockinOmegaWrapper`

Evidence:

- `notes/class2-psi-action-wrapper-local-verification.md`

### `src/c2/c2_957a_run_psi_fire_common.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:957A..C2:95AB` | 49 | `RunPsiFireCommon` | `8d18a278d08c6123299ced40606889c76cbb3711` |
| `C2:95AB..C2:95B4` | 9 | `RunPsiFireAlphaWrapper` | `ff8dbdbec814fa7a98919f414f00e2ef22c845a7` |
| `C2:95B4..C2:95BD` | 9 | `RunPsiFireBetaWrapper` | `f869969b4418f7f1d648f19906de65080aa8a59d` |
| `C2:95BD..C2:95C6` | 9 | `RunPsiFireGammaWrapper` | `1583ba851b7688b394eca8ccc90284f33310d822` |
| `C2:95C6..C2:95CF` | 9 | `RunPsiFireOmegaWrapper` | `613c5ad9a11dc3b73b53e0b6b51e7f310393f93c` |

Labels:

- `C2:957A RunPsiFireCommon`
- `C2:95AB RunPsiFireAlphaWrapper`
- `C2:95B4 RunPsiFireBetaWrapper`
- `C2:95BD RunPsiFireGammaWrapper`
- `C2:95C6 RunPsiFireOmegaWrapper`

Evidence:

- `notes/class2-psi-action-wrapper-local-verification.md`

### `src/c2/c2_95cf_run_psi_freeze_common.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:95CF..C2:9647` | 120 | `RunPsiFreezeCommon` | `baaf713cb7ff9365d53701aa53131598aea0a6a4` |
| `C2:9647..C2:9650` | 9 | `RunPsiFreezeAlphaWrapper` | `330933ca7b770ad6ba7c909eac9e9c4f9c8ddfb1` |
| `C2:9650..C2:9659` | 9 | `RunPsiFreezeBetaWrapper` | `961d8237ddb685d5ae33db1e85beac864516a786` |
| `C2:9659..C2:9662` | 9 | `RunPsiFreezeGammaWrapper` | `d4bb439188923473d73760444de77833e55a5de5` |
| `C2:9662..C2:966B` | 9 | `RunPsiFreezeOmegaWrapper` | `83ad3f7895169c662a0b0c9f62e90d248ff3429b` |

Labels:

- `C2:95CF RunPsiFreezeCommon`
- `C2:9647 RunPsiFreezeAlphaWrapper`
- `C2:9650 RunPsiFreezeBetaWrapper`
- `C2:9659 RunPsiFreezeGammaWrapper`
- `C2:9662 RunPsiFreezeOmegaWrapper`

Evidence:

- `notes/class2-psi-action-wrapper-local-verification.md`

### `src/c2/c2_966b_run_psi_thunder_common.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:966B..C2:97A5` | 314 | `RunPsiThunderCommon` | `0d9f5e748778d3143d1dc61d2eb12101c008fe81` |

Labels:

- `C2:966B RunPsiThunderCommon`

Evidence:

- `notes/class2-psi-thunder-common-local-flow.md`
- `notes/class2-psi-action-wrapper-local-verification.md`

### `src/c2/c2_97a5_handle_psi_thunder_franklin_badge_reflection.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:97A5..C2:98A1` | 252 | `HandlePsiThunderFranklinBadgeReflection` | `5937eb1b1c25e9639129f54959d12ceaf2d0edfe` |

Labels:

- `C2:97A5 HandlePsiThunderFranklinBadgeReflection`

Evidence:

- `notes/class2-psi-thunder-reflection-branch.md`
- `notes/class2-psi-thunder-common-local-flow.md`

### `src/c2/c2_98a1_gate_selected_battler_for_random_status_action.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:98A1..C2:98DE` | 61 | `GateSelectedBattlerForRandomStatusAction` | `9bae223b3571b40d107e3b042208a175d4b5ab0c` |

Labels:

- `C2:98A1 GateSelectedBattlerForRandomStatusAction`

Evidence:

- `notes/class2-psi-flash-common-local-flow.md`

### `src/c2/c2_98de_try_apply_strange_status_to_selected_battler.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:98DE..C2:9917` | 57 | `TryApplyStrangeStatusToSelectedBattler` | `8ed0bea029b93277ff58b68ea14e927d81551f63` |

Labels:

- `C2:98DE TryApplyStrangeStatusToSelectedBattler`

Evidence:

- `notes/class2-psi-flash-common-local-flow.md`
- `notes/class2-affliction-apply-helper-724a.md`

### `src/c2/c2_9917_try_apply_numb_status_to_selected_battler.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:9917..C2:9950` | 57 | `TryApplyNumbStatusToSelectedBattler` | `c31a3d1118810a79e0abaa851b25f3345f906a89` |

Labels:

- `C2:9917 TryApplyNumbStatusToSelectedBattler`

Evidence:

- `notes/class2-psi-flash-common-local-flow.md`
- `notes/class2-affliction-apply-helper-724a.md`

### `src/c2/c2_9950_try_apply_crying_status_to_selected_battler.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:9950..C2:9987` | 55 | `TryApplyCryingStatusToSelectedBattler` | `b18161638673f43cd84c98b0eada9b2ea309fa10` |

Labels:

- `C2:9950 TryApplyCryingStatusToSelectedBattler`

Evidence:

- `notes/class2-psi-flash-common-local-flow.md`
- `notes/class2-affliction-apply-helper-724a.md`

### `src/c2/c2_9987_run_psi_flash_alpha_action.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:9987..C2:99AE` | 39 | `RunPsiFlashAlphaAction` | `01cab99585671b7a4adf2b6559dfb3c05e9529da` |

Labels:

- `C2:9987 RunPsiFlashAlphaAction`

Evidence:

- `notes/class2-psi-flash-common-local-flow.md`

### `src/c2/c2_99ae_run_psi_flash_beta_action.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:99AE..C2:99EF` | 65 | `RunPsiFlashBetaAction` | `d604c18a2c7debd602a2755471d79814cbd12f0e` |

Labels:

- `C2:99AE RunPsiFlashBetaAction`

Evidence:

- `notes/class2-psi-flash-common-local-flow.md`

### `src/c2/c2_99ef_run_psi_flash_gamma_action.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:99EF..C2:9A35` | 70 | `RunPsiFlashGammaAction` | `8a5ad3fe4b1d0a96e77127efa103271e9f1f044b` |

Labels:

- `C2:99EF RunPsiFlashGammaAction`

Evidence:

- `notes/class2-psi-flash-common-local-flow.md`

### `src/c2/c2_9a35_run_psi_flash_omega_action.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:9A35..C2:9A80` | 75 | `RunPsiFlashOmegaAction` | `4bd0ec815e80f83ccd789fab9cd1a439a6c367c2` |

Labels:

- `C2:9A35 RunPsiFlashOmegaAction`

Evidence:

- `notes/class2-psi-flash-common-local-flow.md`

### `src/c2/c2_9a80_run_psi_starstorm_common.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:9A80..C2:9AA6` | 38 | `RunPsiStarstormCommon` | `846038724a7f9138388576955e086b84048d451d` |
| `C2:9AA6..C2:9AAF` | 9 | `RunPsiStarstormAlphaWrapper` | `c55d010791f70d5bd0c06ae1e1a1074764b81cad` |
| `C2:9AAF..C2:9AB8` | 9 | `RunPsiStarstormOmegaWrapper` | `ea2b873589dd809f17da2a505234cc15eff9f1e1` |

Labels:

- `C2:9A80 RunPsiStarstormCommon`
- `C2:9AA6 RunPsiStarstormAlphaWrapper`
- `C2:9AAF RunPsiStarstormOmegaWrapper`

Evidence:

- `notes/class2-psi-action-wrapper-local-verification.md`

### `src/c2/c2_9ab8_run_fixed_amount_healing_common.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:9AB8..C2:9AC6` | 14 | `RunFixedAmountHealingCommon` | `2dfda4d24b5af41d945a63e00cbc6052098c5ab5` |
| `C2:9AC6..C2:9ACF` | 9 | `RunLifeupAlphaHealingAction` | `7960ca8c51c8050744d0b594929e1e3f21cedc8f` |
| `C2:9ACF..C2:9AD8` | 9 | `RunLifeupBetaHealingAction` | `0c3e1373adde8a99475bfe06a20fbf6f30fc86e2` |
| `C2:9AD8..C2:9AE1` | 9 | `RunLifeupGammaHealingAction` | `b6fbd143365b9707787c26ebe96e34b8e9c3dbcc` |
| `C2:9AE1..C2:9AEA` | 9 | `RunLifeupOmegaHealingAction` | `276a820a59b4cb3cba4c0ab2fab36dc3f82f2bab` |

Labels:

- `C2:9AB8 RunFixedAmountHealingCommon`
- `C2:9AC6 RunLifeupAlphaHealingAction`
- `C2:9ACF RunLifeupBetaHealingAction`
- `C2:9AD8 RunLifeupGammaHealingAction`
- `C2:9AE1 RunLifeupOmegaHealingAction`

Evidence:

- `notes/class2-healing-amount-family-c29ab8-c29ae1.md`

### `src/c2/c2_9aea_try_recover_selected_battler_narrow_affliction.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:9AEA..C2:9B7A` | 144 | `TryRecoverSelectedBattlerNarrowAffliction` | `5926d7328ae4484f09b2d086b703a8c26005bac5` |

Labels:

- `C2:9AEA TryRecoverSelectedBattlerNarrowAffliction`

Evidence:

- `notes/battle-affliction-recovery-family-c29aea-a39d.md`
- `notes/class2-healing-amount-family-c29ab8-c29ae1.md`

### `src/c2/c2_9b7a_try_recover_selected_battler_curative_afflictions.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:9B7A..C2:9C2C` | 178 | `TryRecoverSelectedBattlerCurativeAfflictions` | `20bdcfb02bacf375802829af0e821e18fcba7bdc` |

Labels:

- `C2:9B7A TryRecoverSelectedBattlerCurativeAfflictions`

Evidence:

- `notes/battle-affliction-recovery-family-c29aea-a39d.md`

### `src/c2/c2_9c2c_try_recover_selected_battler_broad_afflictions.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:9C2C..C2:9CB8` | 140 | `TryRecoverSelectedBattlerBroadAfflictions` | `d12f65dd4539f4ea8ee9704011d06abc4619cab5` |

Labels:

- `C2:9C2C TryRecoverSelectedBattlerBroadAfflictions`

Evidence:

- `notes/battle-affliction-recovery-family-c29aea-a39d.md`

### `src/c2/c2_9cb8_try_recover_selected_battler_hard_state.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:9CB8..C2:9E38` | 384 | `TryRecoverSelectedBattlerHardState` | `36a6bf51fa642f754154d112cedd48c64e96a603` |

Labels:

- `C2:9CB8 TryRecoverSelectedBattlerHardState`

Evidence:

- `notes/battle-affliction-recovery-family-c29aea-a39d.md`

### `src/c2/c2_9e38_run_defense_spray_action.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:9E38..C2:9E7F` | 71 | `RunDefenseSprayAction` | `cf3cbb78aa38cff2a0c2709528cdedc618eac4cf` |

Labels:

- `C2:9E38 RunDefenseSprayAction`

Evidence:

- `notes/class2-late-stat-and-resource-family-c28e42-c29e38.md`

### `src/c2/c2_9e7f_run_defense_shower_action.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:9E7F..C2:9F06` | 135 | `RunDefenseShowerAction` | `6e54db4604734b008e639052f6019f7002f01fcb` |

Labels:

- `C2:9E7F RunDefenseShowerAction`

Evidence:

- `notes/class2-late-stat-and-resource-family-c28e42-c29e38.md`

### `src/c2/c2_9f06_run_resist_checked_asleep_status_action.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:9F06..C2:9F57` | 81 | `RunResistCheckedAsleepStatusAction` | `2c3c39707711fd09675bb8d45ac7da20a82d4685` |

Labels:

- `C2:9F06 RunResistCheckedAsleepStatusAction`

Evidence:

- `notes/class2-asleep-family-c29f06-c29f57.md`

### `src/c2/c2_9f57_run_asleep_status_wrapper_action.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:9F57..C2:A056` | 255 | `RunAsleepStatusWrapperAction` | `c6ceeece25e4443155dfa29a62e99698e637352d` |

Labels:

- `C2:9F57 RunAsleepStatusWrapperAction`

Evidence:

- `notes/class2-asleep-family-c29f06-c29f57.md`

### `src/c2/c2_a056_run_resist_checked_strange_status_action.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:A056..C2:A39D` | 839 | `RunResistCheckedStrangeStatusAction` | `de5405c34feaa413ffec2d6feb52ec416f869a32` |

Labels:

- `C2:A056 RunResistCheckedStrangeStatusAction`

Evidence:

- `notes/class2-strange-status-family-c28d3a-c28dbb-c2a056.md`

### `src/c2/c2_a39d_try_recover_selected_battler_poison_only.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:A39D..C2:A3D1` | 52 | `TryRecoverSelectedBattlerPoisonOnly` | `d3e35e5e835d20bdbcdb32b4988dd3056d268dc0` |

Labels:

- `C2:A39D TryRecoverSelectedBattlerPoisonOnly`

Evidence:

- `notes/battle-affliction-recovery-family-c29aea-a39d.md`

### `src/c2/c2_0266_load_default_title_upload_tiles.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:0266..C2:0293` | 45 | `LoadDefaultTitleUploadTiles` | `5e3b26328f0bac27bfc7411d94e926fcac0dac7b` |

Labels:

- `C2:0266 LoadDefaultTitleUploadTiles`

Evidence:

- `notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md`

### `src/c2/c2_0293_clear_default_title_upload_tiles.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:0293..C2:02AC` | 25 | `ClearDefaultTitleUploadTiles` | `eef318131a7aaa9c4835c3d601b3c2d7337d8ebd` |

Labels:

- `C2:0293 ClearDefaultTitleUploadTiles`

Evidence:

- `notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md`

### `src/c2/c2_02ac_register_and_upload_window_title_buffer.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:02AC..C2:032B` | 127 | `RegisterAndUploadWindowTitleBuffer` | `0656b690211665397d2c044febb7150825346872` |

Labels:

- `C2:02AC RegisterAndUploadWindowTitleBuffer`

Evidence:

- `notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md`

### `src/c2/c2_032b_write_window_title_and_upload.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:032B..C2:038B` | 96 | `WriteWindowTitleAndUpload` | `db46622debfb52e1da3b737fba352fd7da0f73fa` |

Labels:

- `C2:032B WriteWindowTitleAndUpload`

Evidence:

- `notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md`

### `src/c2/c2_038b_reset_hp_pp_tilemap_buffers.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:038B..C2:03C3` | 56 | `ResetHpPpTilemapBuffers` | `89e677ba14731a7e32ed3d97160d4df6335449c3` |

Labels:

- `C2:038B ResetHpPpTilemapBuffers`

Evidence:

- `notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md`

### `src/c2/c2_1628_test_event_flag.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:1628..C2:165E` | 54 | `TestEventFlag` | `3f48f0ad40712500ccf95077ce8a2e890a0f9564` |

Labels:

- `C2:1628 TestEventFlag`

Evidence:

- `notes/text-command-07-check-event-flag.md`

### `src/c2/c2_165e_set_or_clear_event_flag.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:165E..C2:16AD` | 79 | `SetOrClearEventFlag` | `53220a016966d48cd8ad4aec6f50714999a232c6` |

Labels:

- `C2:165E SetOrClearEventFlag`

Evidence:

- `notes/text-command-04-set-event-flag.md`
- `notes/text-command-05-clear-event-flag.md`

### `src/c2/c2_26c5_set_current9_c88_flag_and_refresh5_d64.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:26C5..C2:26D0` | 11 | `SetCurrent9C88FlagAndRefresh5D64` | `9ad2cd3672dccf845d7227bb1abecc4b6372700a` |

Labels:

- `C2:26C5 SetCurrent9C88FlagAndRefresh5D64`

Evidence:

- `notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md`

### `src/c2/c2_26d0_set_current_interaction_event_flag_and_refresh_target.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:26D0..C2:26E6` | 22 | `SetCurrentInteractionEventFlagAndRefreshTarget` | `d6001943eef1f457d973bd27cb509c0525318693` |

Labels:

- `C2:26D0 SetCurrentInteractionEventFlagAndRefreshTarget`

Evidence:

- `notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md`

### `src/c2/c2_26e6_get_current9_c88_flag.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:26E6..C2:26EB` | 5 | `GetCurrent9C88Flag` | `6bb9319c041fddf95b8619ec44534145e6f55bc2` |

Labels:

- `C2:26E6 GetCurrent9C88Flag`

Evidence:

- `notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md`

### `src/c2/c2_26eb_test_current_interaction_event_flag.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:26EB..C2:26F0` | 5 | `TestCurrentInteractionEventFlag` | `a522b8d45295eb1ff1b746c708022c6d35b77f8b` |

Labels:

- `C2:26EB TestCurrentInteractionEventFlag`

Evidence:

- `notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md`

### `src/c2/c2_08b8_classify_menu_tile_for_cursor_scan.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:08B8..C2:0912` | 90 | `ClassifyMenuTileForCursorScan` | `63f5f339197992e1a3bb55d5ef3a92448d714c81` |

Labels:

- `C2:08B8 ClassifyMenuTileForCursorScan`

Evidence:

- `notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md`

### `src/c2/c2_0b65_find_next_selectable_menu_cell.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:0B65..C2:0D3F` | 474 | `FindNextSelectableMenuCell` | `29d1d68f48b4432fc6f3d369026f9811b866e0c9` |

Labels:

- `C2:0B65 FindNextSelectableMenuCell`

Evidence:

- `notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md`

### `src/c2/c2_0d3f_split_value_into_three_decimal_digits_at8966.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:0D3F..C2:0F58` | 537 | `SplitValueIntoThreeDecimalDigitsAt8966` | `88642c89553bdf1783ebdb636559e01c7a76ae07` |

Labels:

- `C2:0D3F SplitValueIntoThreeDecimalDigitsAt8966`

Evidence:

- `notes/c2-symbol-only-stragglers-c200d1-c20d3f.md`
- `notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md`

### `src/c2/c2_0f58_select_hp_pp_roll_delta.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:0F58..C2:0F9A` | 66 | `SelectHpPpRollDelta` | `ac08e1b1092be7cad2d3214182b47b611a0d52b5` |

Labels:

- `C2:0F58 SelectHpPpRollDelta`

Evidence:

- `notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md`

### `src/c2/c2_0f9a_clamp_hp_pp_roll_targets_to_live_values.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:0F9A..C2:1034` | 154 | `ClampHpPpRollTargetsToLiveValues` | `dfbaead209df0faf8ef4750ad2eaffa2af00f662` |

Labels:

- `C2:0F9A ClampHpPpRollTargetsToLiveValues`

Evidence:

- `notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md`

### `src/c2/c2_1034_are_all_hp_pp_rollers_settled.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:1034..C2:108C` | 88 | `AreAllHpPpRollersSettled` | `4da4e71558c26297a69bf1ecfe46ef6f0b85d0e0` |

Labels:

- `C2:1034 AreAllHpPpRollersSettled`

Evidence:

- `notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md`

### `src/c2/c2_108c_clear_hp_pp_roll_dirty_latch_if_settled.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:108C..C2:109F` | 19 | `ClearHpPpRollDirtyLatchIfSettled` | `fcf8deda515dc74abb411851c7e839962b63b289` |

Labels:

- `C2:108C ClearHpPpRollDirtyLatchIfSettled`

Evidence:

- `notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md`

### `src/c2/c2_109f_run_hp_pp_roller.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:109F..C2:13AC` | 781 | `RunHpPpRoller` | `0f06993a3c14abbc1d3fd8a57dda12bc24abf1c8` |

Labels:

- `C2:109F RunHpPpRoller`

Evidence:

- `notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md`
- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank02.asm`

### `src/c2/c2_13ac_update_hp_pp_meter_tiles.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:13AC..C2:1628` | 636 | `UpdateHpPpMeterTiles` | `167bbf981c5a95227f36c94b4ed7c2bcf66336cb` |

Labels:

- `C2:13AC UpdateHpPpMeterTiles`

Evidence:

- `notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md`
- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank02.asm`

### `src/c2/c2_16ad_apply_music_state_and_mirror_to5_dd4.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:16AD..C2:16C9` | 28 | `ApplyMusicStateAndMirrorTo5DD4` | `b1373f9ed8d43380ce08d0d38136e650466cb932` |

Labels:

- `C2:16AD ApplyMusicStateAndMirrorTo5DD4`

Evidence:

- `notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md`
- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank02.asm`

### `src/c2/c2_16c9_stop_music_redirect.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:16C9..C2:16D0` | 7 | `StopMusicRedirect` | `94b96b3e45fb836b644b6d1d9a0bbfd0cf7e4bfc` |

Labels:

- `C2:16C9 StopMusicRedirect`

Evidence:

- `notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md`
- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank02.asm`

### `src/c2/c2_16d0_play_sound_and_refresh_hp_pp_rollers.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:16D0..C2:16DB` | 11 | `PlaySoundAndRefreshHpPpRollers` | `af02fee05d436d96660e3d10c4da06b25c7e207f` |

Labels:

- `C2:16D0 PlaySoundAndRefreshHpPpRollers`

Evidence:

- `notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md`
- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank02.asm`

### `src/c2/c2_16db_arbitrate_party_overlay_entity_presence.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:16DB..C2:1857` | 380 | `ArbitratePartyOverlayEntityPresence` | `02ec6e2667eaa4b7fdf2697024908542cf943941` |

Labels:

- `C2:16DB ArbitratePartyOverlayEntityPresence`

Evidence:

- `notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md`
- `notes/party-overlay-arbitration-c216db-c3ebca.md`
- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank02.asm`

### `src/c2/c2_26f0_find_first_party_slot_with_state_one.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:26F0..C2:272F` | 63 | `FindFirstPartySlotWithStateOne` | `dede487f424f9f87bd8a9ade69084e9c3272a601` |

Labels:

- `C2:26F0 FindFirstPartySlotWithStateOne`

Evidence:

- `notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md`

### `src/c2/c2_272f_count_party_slots_not_state_one_or_two.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:272F..C2:277C` | 77 | `CountPartySlotsNotStateOneOrTwo` | `24db66c2b406299e6c75dd1d29f7b565437d6fcd` |

Labels:

- `C2:272F CountPartySlotsNotStateOneOrTwo`

Evidence:

- `notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md`

### `src/c2/c2_277c_find_first_party_code_not_state_one_or_two.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:277C..C2:27C8` | 76 | `FindFirstPartyCodeNotStateOneOrTwo` | `b75723f00256717593fbd01aa76304455c7884b3` |

Labels:

- `C2:277C FindFirstPartyCodeNotStateOneOrTwo`

Evidence:

- `notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md`

### `src/c2/c2_27c8_mark_party_code_bit_in9839.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:27C8..C2:281D` | 85 | `MarkPartyCodeBitIn9839` | `2fd10644f74fcb336e4d3c065f2d71b8a24d1987` |

Labels:

- `C2:27C8 MarkPartyCodeBitIn9839`

Evidence:

- `notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md`
- `notes/party-overlay-arbitration-c216db-c3ebca.md`

### `src/c2/c2_281d_update_party_overlay_position_clamp.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:281D..C2:28B7` | 154 | `UpdatePartyOverlayPositionClamp` | `2ca72af108a33d167f64537508807b5377370383` |

Labels:

- `C2:281D UpdatePartyOverlayPositionClamp`

Evidence:

- `notes/party-overlay-arbitration-c216db-c3ebca.md`

### `src/c2/c2_28b7_clamp_party_overlay_position_delta.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:28B7..C2:28F8` | 65 | `ClampPartyOverlayPositionDelta` | `aa5f341fcc09ff10d75953686eec4dab5254a8aa` |

Labels:

- `C2:28B7 ClampPartyOverlayPositionDelta`

Evidence:

- `notes/party-overlay-arbitration-c216db-c3ebca.md`

### `src/c2/c2_28f8_insert_party_overlay_tracked_item_id.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:28F8..C2:29BB` | 195 | `InsertPartyOverlayTrackedItemId` | `da729ab3137cdc755c0cd2ddf557548a0ca54a9e` |

Labels:

- `C2:28F8 InsertPartyOverlayTrackedItemId`

Evidence:

- `notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md`
- `notes/party-overlay-arbitration-c216db-c3ebca.md`

### `src/c2/c2_29bb_remove_party_overlay_tracked_item_id.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:29BB..C2:2A2C` | 113 | `RemovePartyOverlayTrackedItemId` | `d6bcb6e9c809c5c1b6408fdc3e9eab2c80959fda` |

Labels:

- `C2:29BB RemovePartyOverlayTrackedItemId`

Evidence:

- `notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md`
- `notes/party-overlay-arbitration-c216db-c3ebca.md`

### `src/c2/c2_2a2c_save_current_game.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:2A2C..C2:2A3A` | 14 | `SaveCurrentGame` | `c7715e26ee6b73b8b636cd9a5f29b5aec9b8f230` |

Labels:

- `C2:2A2C SaveCurrentGame`

Evidence:

- `notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md`
- `notes/text-command-family-1f-deferred-callbacks.md`

### `src/c2/c2_3008_save_and_clear_temporary_party_source_state.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:3008..C2:307B` | 115 | `SaveAndClearTemporaryPartySourceState` | `2b8e294be7cffd279bb59519ff56f4bb8f9bd299` |

Labels:

- `C2:3008 SaveAndClearTemporaryPartySourceState`

Evidence:

- `notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md`

### `src/c2/c2_307b_restore_temporary_party_source_state.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:307B..C2:30F3` | 120 | `RestoreTemporaryPartySourceState` | `d4ada9ad5651260b23e3db8e0c2252b6c9f9c830` |

Labels:

- `C2:307B RestoreTemporaryPartySourceState`

Evidence:

- `notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md`

### `src/c2/c2_2a3a_transfer_inventory_item_between_characters_maintaining_equipment.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:2A3A..C2:2F38` | 1278 | `TransferInventoryItemBetweenCharactersMaintainingEquipment` | `1e142ea8b494a379e778e350a61bff1adb2151b4` |

Labels:

- `C2:2A3A TransferInventoryItemBetweenCharactersMaintainingEquipment`

Evidence:

- `notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md`
- `notes/inventory-slot-insertion-helper-c18bc6.md`
- `notes/equipment-slot-subtype-dispatch-c19066-c4577d.md`

### `src/c2/c2_2f38_init_battle_scripted.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:2F38..C2:3008` | 208 | `InitBattleScripted` | `7a8ab80ea0c79773dbad813b61d7139d5b18d263` |

Labels:

- `C2:2F38 InitBattleScripted`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank02.asm:162`
- `refs/ebsrc-main/ebsrc-main/src/battle/init_scripted.asm`

### `src/c2/c2_1857_recalculate_character_derived_offense.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:1857..C2:192B` | 212 | `RecalculateCharacterDerivedOffense` | `c2bd8b2bd0dbe4f751ad168aa8aa0d0fc00d6333` |

Labels:

- `C2:1857 RecalculateCharacterDerivedOffense`

Evidence:

- `notes/equipped-item-derived-cache-family-c21857-c21e03.md`

### `src/c2/c2_192b_recalculate_character_derived_defense.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:192B..C2:1AEB` | 448 | `RecalculateCharacterDerivedDefense` | `9501f122595666fc4ba7bfe0697384189e93df78` |

Labels:

- `C2:192B RecalculateCharacterDerivedDefense`

Evidence:

- `notes/equipped-item-derived-cache-family-c21857-c21e03.md`

### `src/c2/c2_1aeb_recalculate_character_derived_speed.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:1AEB..C2:1BA4` | 185 | `RecalculateCharacterDerivedSpeed` | `37dd764ae160be614cb89ce45f88eee16cbe01df` |

Labels:

- `C2:1AEB RecalculateCharacterDerivedSpeed`

Evidence:

- `notes/equipped-item-derived-cache-family-c21857-c21e03.md`

### `src/c2/c2_1ba4_recalculate_character_derived_guts.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:1BA4..C2:1C5D` | 185 | `RecalculateCharacterDerivedGuts` | `7b5751c3a2587142dbc3f73d744249c83a637596` |

Labels:

- `C2:1BA4 RecalculateCharacterDerivedGuts`

Evidence:

- `notes/equipped-item-derived-cache-family-c21857-c21e03.md`

### `src/c2/c2_1c5d_recalculate_character_derived_luck.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:1C5D..C2:1D65` | 264 | `RecalculateCharacterDerivedLuck` | `f5f1026d1cbc6d0d39a655e9a0cecfeaddf2e8f5` |

Labels:

- `C2:1C5D RecalculateCharacterDerivedLuck`

Evidence:

- `notes/equipped-item-derived-cache-family-c21857-c21e03.md`

### `src/c2/c2_1d65_recalculate_character_derived_vitality.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:1D65..C2:1D7D` | 24 | `RecalculateCharacterDerivedVitality` | `027796a2f4f2f82efce426f7fd5e88842842e7df` |

Labels:

- `C2:1D65 RecalculateCharacterDerivedVitality`

Evidence:

- `notes/equipped-item-derived-cache-family-c21857-c21e03.md`

### `src/c2/c2_1d7d_recalculate_character_derived_iq.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:1D7D..C2:1D95` | 24 | `RecalculateCharacterDerivedIq` | `cf2e572f30daa3e79bc4706591780649cd1df378` |

Labels:

- `C2:1D7D RecalculateCharacterDerivedIq`

Evidence:

- `notes/equipped-item-derived-cache-family-c21857-c21e03.md`

### `src/c2/c2_1d95_recalculate_character_derived_miss_rate.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:1D95..C2:1E03` | 110 | `RecalculateCharacterDerivedMissRate` | `6829513f839bfe55b1e7395bf81653f2ce3f4678` |

Labels:

- `C2:1D95 RecalculateCharacterDerivedMissRate`

Evidence:

- `notes/equipped-item-derived-cache-family-c21857-c21e03.md`

### `src/c2/c2_1e03_recalculate_character_derived_resistance_fields.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:1E03..C2:2351` | 1358 | `RecalculateCharacterDerivedResistanceFields` | `b84b8ab0df4b2f70014790b9f6a8ededeb310dea` |

Labels:

- `C2:1E03 RecalculateCharacterDerivedResistanceFields`

Evidence:

- `notes/equipped-item-derived-cache-family-c21857-c21e03.md`

### `src/c2/c2_2351_find_first_empty_inventory_slot_for_character.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:2351..C2:239D` | 76 | `FindFirstEmptyInventorySlotForCharacter` | `f166eade72056e08ce9cd68f6cea43de7a2ee86f` |

Labels:

- `C2:2351 FindFirstEmptyInventorySlotForCharacter`

Evidence:

- `notes/pending-item-queue-984b.md`

### `src/c2/c2_6189_fill_instant_win_tile_buffer_and_upload.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:6189..C2:654C` | 963 | `FillInstantWinTileBufferAndUpload` | `63eccbf106302e2b6715b25eb38a0325e5faf4d2` |

Labels:

- `C2:6189 FillInstantWinTileBufferAndUpload`

Evidence:

- `notes\c2-instant-win-and-magic-butterfly-helpers-c26189-c2654c.md`

### `src/c2/c2_654c_run_magic_butterfly_pp_restore_animation.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:654C..C2:6BFB` | 1711 | `RunMagicButterflyPpRestoreAnimation` | `b04f30d032e33b1433746846f8625e7e8877095b` |

Labels:

- `C2:654C RunMagicButterflyPpRestoreAnimation`

Evidence:

- `notes\c2-instant-win-and-magic-butterfly-helpers-c26189-c2654c.md`

### `src/c2/c2_b930_export_battle_selection_snapshot.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:B930..C2:BAC5` | 405 | `ExportBattleSelectionSnapshot` | `e8ac99dbbd81e27dc4ff56f5563149542fed765a` |

Labels:

- `C2:B930 ExportBattleSelectionSnapshot`

Evidence:

- `notes\battle-selection-snapshot-export-c2b930.md`
- `notes\c2-battle-contract-workahead.md`

### `src/c2/c2_bac5_count_filtered_second_stage_rows.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:BAC5..C2:BB18` | 83 | `CountFilteredSecondStageRows` | `d7f4d105f7358a9258f50f419a3865eabe5747f5` |

Labels:

- `C2:BAC5 CountFilteredSecondStageRows`

Evidence:

- `notes\class2-second-stage-selector-a970.md`
- `notes\c2-battle-contract-workahead.md`

### `src/c2/c2_bb18_promote_candidate_to_collapse_affliction_controller.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:BB18..C2:BC5C` | 324 | `PromoteCandidateToCollapseAfflictionController` | `aa066aac22c9f3595139fb307cea74acaf6d7696` |

Labels:

- `C2:BB18 PromoteCandidateToCollapseAfflictionController`

Evidence:

- `notes\class2-second-stage-selector-a970.md`
- `notes\c2-battle-contract-workahead.md`

### `src/c2/c2_bc5c_clear_inactive_candidate_live_slot_transient_fields.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:BC5C..C2:BCB9` | 93 | `ClearInactiveCandidateLiveSlotTransientFields` | `d4ce119753f5bb79d2047a6cbaec917c80519a53` |

Labels:

- `C2:BC5C ClearInactiveCandidateLiveSlotTransientFields`

Evidence:

- `notes\class2-second-stage-selector-a970.md`
- `notes\c2-battle-contract-workahead.md`

### `src/c2/c2_2474_lookup_status_tile_width_or_offset_for_hp_pp_window.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:2474..C2:2562` | 238 | `LookupStatusTileWidthOrOffsetForHpPpWindow` | `e3190ba56bd21be3cb81e59269e641b5ec69a819` |

Labels:

- `C2:2474 LookupStatusTileWidthOrOffsetForHpPpWindow`

Evidence:

- `notes\c2-party-inventory-status-utility-corridor-c216ad-c2307b.md`

### `src/c2/c2_23d9_lookup_status_tile_value_for_hp_pp_window.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:23D9..C2:2474` | 155 | `LookupStatusTileValueForHpPpWindow` | `75acf3739bfe94580ee762d90a835e3145cfea53` |

Labels:

- `C2:23D9 LookupStatusTileValueForHpPpWindow`

Evidence:

- `notes\c2-party-inventory-status-utility-corridor-c216ad-c2307b.md`

### `src/c2/c2_cfe5_init_loaded_battle_bg_layer_from_config.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:CFE5..C2:D0AC` | 199 | `InitLoadedBattleBgLayerFromConfig` | `dbd6c4690b987a8a1081ce4f51d98338a72a9461` |

Labels:

- `C2:CFE5 InitLoadedBattleBgLayerFromConfig`

Evidence:

- `notes\c2-battlebg-load-and-palette-effect-corridor-c2cfe5-c2e0e7.md`

### `src/c2/c2_de0f_dim_loaded_battle_bg_palettes_and_upload.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:DE0F..C2:DE96` | 135 | `DimLoadedBattleBgPalettesAndUpload` | `c898428d9a8ed439eaeb5d92ea573145ebc79bcf` |

Labels:

- `C2:DE0F DimLoadedBattleBgPalettesAndUpload`

Evidence:

- `notes\c2-battlebg-load-and-palette-effect-corridor-c2cfe5-c2e0e7.md`

### `src/c2/c2_de96_restore_loaded_battle_bg_palettes_and_upload.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:DE96..C2:DF2E` | 152 | `RestoreLoadedBattleBgPalettesAndUpload` | `ce4671d53bdc996c92cb65c97e961311c8c0a330` |

Labels:

- `C2:DE96 RestoreLoadedBattleBgPalettesAndUpload`

Evidence:

- `notes\c2-battlebg-load-and-palette-effect-corridor-c2cfe5-c2e0e7.md`

### `src/c2/c2_df2e_apply_loaded_battle_bg_palette_step.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:DF2E..C2:E08E` | 352 | `ApplyLoadedBattleBgPaletteStep` | `5d92c39a03d60fdd5259caa2f4ea80f657d33afc` |

Labels:

- `C2:DF2E ApplyLoadedBattleBgPaletteStep`

Evidence:

- `notes\c2-battlebg-load-and-palette-effect-corridor-c2cfe5-c2e0e7.md`

### `src/c2/c2_e08e_apply_loaded_battle_bg_palette_step_across_layers.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:E08E..C2:E0E7` | 89 | `ApplyLoadedBattleBgPaletteStepAcrossLayers` | `2ffe50535464173864d02f18eba25780fdcc35a5` |

Labels:

- `C2:E08E ApplyLoadedBattleBgPaletteStepAcrossLayers`

Evidence:

- `notes\c2-battlebg-load-and-palette-effect-corridor-c2cfe5-c2e0e7.md`

### `src/c2/c2_f09f_find_loaded_battle_sprite_slot_by_id.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:F09F..C2:F0D1` | 50 | `FindLoadedBattleSpriteSlotById` | `3d9a7dc75d91694dac3659f52fe34ed7d365bcfc` |

Labels:

- `C2:F09F FindLoadedBattleSpriteSlotById`

Evidence:

- `notes\c2-battle-sprite-render-and-palette-tail-c2eee7-c2ff9a.md`

### `src/c2/c2_f0d1_trim_loaded_enemy_sprite_list_to_width_limit.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:F0D1..C2:F121` | 80 | `TrimLoadedEnemySpriteListToWidthLimit` | `2d9b037c67cd11e10ce5bb11a49aa18985e878dc` |

Labels:

- `C2:F0D1 TrimLoadedEnemySpriteListToWidthLimit`

Evidence:

- `notes\c2-battle-sprite-render-and-palette-tail-c2eee7-c2ff9a.md`

### `src/c2/c2_f8f9_render_and_commit_battle_sprite_rows.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:F8F9..C2:F917` | 30 | `RenderAndCommitBattleSpriteRows` | `c1e9ce0a1c2a123546486ded6c742cd65eefa366` |

Labels:

- `C2:F8F9 RenderAndCommitBattleSpriteRows`

Evidence:

- `notes\c2-battle-sprite-render-and-palette-tail-c2eee7-c2ff9a.md`

### `src/c2/c2_f917_build_battle_sprite_row_render_order.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:F917..C2:FADE` | 455 | `BuildBattleSpriteRowRenderOrder` | `870c65b75c8f3e33fba1af94334f6e665a17b46f` |

Labels:

- `C2:F917 BuildBattleSpriteRowRenderOrder`

Evidence:

- `notes\c2-battle-sprite-render-and-palette-tail-c2eee7-c2ff9a.md`

### `src/c2/c2_fca6_init_enemy_sprite_color_wave_entry_from_palette.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:FCA6..C2:FD99` | 243 | `InitEnemySpriteColorWaveEntryFromPalette` | `3baeeb5b7cbf5c692f7f737d2d94a614203fe1c7` |

Labels:

- `C2:FCA6 InitEnemySpriteColorWaveEntryFromPalette`

Evidence:

- `notes\c2-battle-sprite-render-and-palette-tail-c2eee7-c2ff9a.md`

### `src/c2/c2_fd99_advance_enemy_sprite_color_wave_palettes.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:FD99..C2:FEF9` | 352 | `AdvanceEnemySpriteColorWavePalettes` | `3ba9e40ebabf91b5102874cc692b58d403672331` |

Labels:

- `C2:FD99 AdvanceEnemySpriteColorWavePalettes`

Evidence:

- `notes\c2-battle-sprite-render-and-palette-tail-c2eee7-c2ff9a.md`

### `src/c2/c2_fef9_load_or_dim_battle_palette_set.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:FEF9..C2:FF9A` | 161 | `LoadOrDimBattlePaletteSet` | `7687b0ba8d46738a1579d027b2d431468b75c23c` |

Labels:

- `C2:FEF9 LoadOrDimBattlePaletteSet`

Evidence:

- `notes\c2-battle-sprite-render-and-palette-tail-c2eee7-c2ff9a.md`

### `src/c2/c2_f121_assign_enemy_battle_sprite_rows_and_xpositions.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:F121..C2:F8F9` | 2008 | `AssignEnemyBattleSpriteRowsAndXPositions` | `2b74be570cc514b7a6510d5ea3ea15562ea85b04` |

Labels:

- `C2:F121 AssignEnemyBattleSpriteRowsAndXPositions`

Evidence:

- `notes\c2-battle-sprite-render-and-palette-tail-c2eee7-c2ff9a.md`

### `src/c2/c2_a658_run_bomb_common_splash_damage.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:A658..C2:A818` | 448 | `RunBombCommonSplashDamage` | `eb4789cd52d300df80f283e8458d037bfddd12f2` |

Labels:

- `C2:A658 RunBombCommonSplashDamage`

Evidence:

- `notes\class2-bomb-common-family-c2a658-c2a821.md`

### `src/c2/c2_a818_run_bomb_action.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:A818..C2:A821` | 9 | `RunBombAction` | `1e9740bf7af493743418af2973c2751fb346be4a` |

Labels:

- `C2:A818 RunBombAction`

Evidence:

- `notes\class2-bomb-common-family-c2a658-c2a821.md`

### `src/c2/c2_eee7_load_battle_group_enemy_sprites.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:EEE7..C2:F09F` | 440 | `LoadBattleGroupEnemySprites` | `d90f82284ea4ff97209aa87ff00be53f77e73602` |

Labels:

- `C2:EEE7 LoadBattleGroupEnemySprites`

Evidence:

- `notes/c2-battle-sprite-render-and-palette-tail-c2eee7-c2ff9a.md`

### `src/c2/c2_a3d1_run_item_side_concentration_seal_action.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:A3D1..C2:A5EC` | 539 | `RunItemSideConcentrationSealAction` | `5f95d2e804a71b2204e65bc17dc9594c7ed013f4` |

Labels:

- `C2:A3D1 RunItemSideConcentrationSealAction`

Evidence:

- `notes/class2-concentration-seal-family-c28d5a-c2a3d1.md`

### `src/c2/c2_c14e_run_rainbow_colors_special_event.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:C14E..C2:C37A` | 556 | `RunRainbowColorsSpecialEvent` | `a65418985434c4a963bae71317844aaf204ada1d` |

Labels:

- `C2:C14E RunRainbowColorsSpecialEvent`

Evidence:

- `notes/class2-special-event-results-c29298-c2c14e.md`

### `src/c2/c2_e8c4_start_battle_swirl_overlay_and_record_mode.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:E8C4..C2:E9ED` | 297 | `StartBattleSwirlOverlayAndRecordMode` | `5d6f2207f3a55bcb7dfafd7183bdd28752c98eb4` |

Labels:

- `C2:E8C4 StartBattleSwirlOverlayAndRecordMode`

Evidence:

- `notes/c2-psi-swirl-overlay-tail-c2e6b3-c2ea74.md`

### `src/c2/c2_b573_apply_battle_luck_increase_consequence.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:B573..C2:B6EB` | 376 | `ApplyBattleLuckIncreaseConsequence` | `de54a2ec2bb134e608b22be48ed9e8e1f9404398` |

Labels:

- `C2:B573 ApplyBattleLuckIncreaseConsequence`

Evidence:

- `notes/battle-action-stat-change-family-c2b2e0-b5d7.md`

### `src/c2/c2_e9ed_clear_battle_swirl_overlay_state.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:E9ED..C2:EACF` | 226 | `ClearBattleSwirlOverlayState` | `fe4cda489957d5127f2c7ad2bece54366b91436c` |

Labels:

- `C2:E9ED ClearBattleSwirlOverlayState`

Evidence:

- `notes/c2-psi-swirl-overlay-tail-c2e6b3-c2ea74.md`

### `src/c2/c2_03c3_compose_party_member_hp_pp_window_tiles.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:03C3..C2:077D` | 954 | `ComposePartyMemberHpPpWindowTiles` | `51d7a525a73117a11a2b536c9e08be1735e624c9` |

Labels:

- `C2:03C3 ComposePartyMemberHpPpWindowTiles`

Evidence:

- `notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md`

### `src/c2/c2_07e1_clear_party_hp_pp_window_tiles.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:07E1..C2:087C` | 155 | `ClearPartyHpPpWindowTiles` | `3f05438cf373c96faa99ea073fd8f30a4037311c` |

Labels:

- `C2:07E1 ClearPartyHpPpWindowTiles`

Evidence:

- `notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md`

### `src/c2/c2_0a20_snapshot_managed_text_event_slot_state.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:0A20..C2:0ABC` | 156 | `SnapshotManagedTextEventSlotState` | `a1f8c3ccb4770f87e8f1dbb365315d9cf20d3574` |

Labels:

- `C2:0A20 SnapshotManagedTextEventSlotState`

Evidence:

- `notes/timed-event-slot-block-7440-and-c20abc.md`

### `src/c2/c2_0abc_restore_managed_text_event_slot_state.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:0ABC..C2:0B65` | 169 | `RestoreManagedTextEventSlotState` | `923b9cf34a4137d9a46284126a9695bda8811c79` |

Labels:

- `C2:0ABC RestoreManagedTextEventSlotState`

Evidence:

- `notes/timed-event-slot-block-7440-and-c20abc.md`

### `src/c2/c2_b342_apply_battle_hp_recovery_consequence.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:B342..C2:B360` | 30 | `ApplyBattleHpRecoveryConsequence` | `3fab5a3d5bd1a931451b8871928e9bf1a3bde023` |

Labels:

- `C2:B342 ApplyBattleHpRecoveryConsequence`

Evidence:

- `notes/battle-action-stat-change-family-c2b2e0-b5d7.md`

### `src/c2/c2_b360_apply_battle_pp_recovery_consequence.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:B360..C2:B3D8` | 120 | `ApplyBattlePpRecoveryConsequence` | `ba9ca311997ccd806d6bd48cc902f2d663986865` |

Labels:

- `C2:B360 ApplyBattlePpRecoveryConsequence`

Evidence:

- `notes/battle-action-stat-change-family-c2b2e0-b5d7.md`

### `src/c2/c2_b3d8_apply_battle_iq_increase_consequence.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:B3D8..C2:B43F` | 103 | `ApplyBattleIqIncreaseConsequence` | `2a5c1699c4bc7ac22158bad798d698462c294e3f` |

Labels:

- `C2:B3D8 ApplyBattleIqIncreaseConsequence`

Evidence:

- `notes/battle-action-stat-change-family-c2b2e0-b5d7.md`

### `src/c2/c2_b43f_apply_battle_guts_increase_consequence.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:B43F..C2:B4A6` | 103 | `ApplyBattleGutsIncreaseConsequence` | `89e5065aff0fa13ebbe9dd6bc7eefbcf257af8b6` |

Labels:

- `C2:B43F ApplyBattleGutsIncreaseConsequence`

Evidence:

- `notes/battle-action-stat-change-family-c2b2e0-b5d7.md`

### `src/c2/c2_b4a6_apply_battle_speed_increase_consequence.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:B4A6..C2:B50D` | 103 | `ApplyBattleSpeedIncreaseConsequence` | `db300be073dd7cc39ffb44b949be57180cdb13b1` |

Labels:

- `C2:B4A6 ApplyBattleSpeedIncreaseConsequence`

Evidence:

- `notes/battle-action-stat-change-family-c2b2e0-b5d7.md`

### `src/c2/c2_b50d_apply_battle_vitality_increase_consequence.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:B50D..C2:B573` | 102 | `ApplyBattleVitalityIncreaseConsequence` | `8c15b9cbf2678a76fe37e4215177655f44aae937` |

Labels:

- `C2:B50D ApplyBattleVitalityIncreaseConsequence`

Evidence:

- `notes/battle-action-stat-change-family-c2b2e0-b5d7.md`

### `src/c2/c2_c37a_run_final_prayer_stage_transition.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:C37A..C2:C3E2` | 104 | `RunFinalPrayerStageTransition` | `63ceed81816707c83e3031b65029d01b4dc349a7` |

Labels:

- `C2:C37A RunFinalPrayerStageTransition`

Evidence:

- `notes/class2-prayer-common-helpers-c2c37a-c2c3e2-c2c41f.md`

### `src/c2/c2_c3e2_apply_final_prayer_damage_step.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:C3E2..C2:C41F` | 61 | `ApplyFinalPrayerDamageStep` | `30a6c99b0d9e62e6f64f318486b5e3dc13337a8f` |

Labels:

- `C2:C3E2 ApplyFinalPrayerDamageStep`

Evidence:

- `notes/class2-prayer-common-helpers-c2c37a-c2c3e2-c2c41f.md`

### `src/c2/c2_09a0_close_and_clear_current_window_tilemap.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:09A0..C2:0A20` | 128 | `CloseAndClearCurrentWindowTilemap` | `a2ad845571b082dce16a84129d4174f16a0bf18f` |

Labels:

- `C2:09A0 CloseAndClearCurrentWindowTilemap`

Evidence:

- `notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md`

### `src/c2/c2_260d_setup_bracelet_equipment_preview_block.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:260D..C2:2673` | 102 | `SetupBraceletEquipmentPreviewBlock` | `f4c7796928b376b92c1fd2fd626fa00959aff15e` |

Labels:

- `C2:260D SetupBraceletEquipmentPreviewBlock`

Evidence:

- `notes/equipment-preview-and-derived-state-cluster.md`

### `src/c2/c2_b2e0_dispatch_battle_stat_change_consequence.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:B2E0..C2:B342` | 98 | `DispatchBattleStatChangeConsequence` | `2adf850f7a2961fe6232bb82314c4cf8c0d1198c` |

Labels:

- `C2:B2E0 DispatchBattleStatChangeConsequence`

Evidence:

- `notes/battle-action-stat-change-family-c2b2e0-b5d7.md`

### `src/c2/c2_2562_setup_weapon_equipment_preview_block.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:2562..C2:25AC` | 74 | `SetupWeaponEquipmentPreviewBlock` | `bdf83b54a0569478ee8705dce0b2d965772e3f5d` |

Labels:

- `C2:2562 SetupWeaponEquipmentPreviewBlock`

Evidence:

- `notes/equipment-preview-and-derived-state-cluster.md`

### `src/c2/c2_25ac_setup_charm_equipment_preview_block.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:25AC..C2:260D` | 97 | `SetupCharmEquipmentPreviewBlock` | `28ebcf030315d446aa420aa733a4437c60927ea1` |

Labels:

- `C2:25AC SetupCharmEquipmentPreviewBlock`

Evidence:

- `notes/equipment-preview-and-derived-state-cluster.md`

### `src/c2/c2_2673_setup_headgear_equipment_preview_block.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:2673..C2:26C5` | 82 | `SetupHeadgearEquipmentPreviewBlock` | `cf8033dabde9bafd1722742450b222a03f5a5105` |

Labels:

- `C2:2673 SetupHeadgearEquipmentPreviewBlock`

Evidence:

- `notes/equipment-preview-and-derived-state-cluster.md`

### `src/c2/c2_b6eb_initialize_enemy_battler_stats_from_enemy_id.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:B6EB..C2:B930` | 581 | `InitializeEnemyBattlerStatsFromEnemyId` | `62e250a44ea1ce87e12e0dd238301597a4c51e84` |

Labels:

- `C2:B6EB InitializeEnemyBattlerStatsFromEnemyId`

Evidence:

- `notes/class2-local-enemy-id-to-battler-init-chain.md`

### `src/c2/c2_bcb9_apply_battler_pp_target_loss.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:BCB9..C2:BD13` | 90 | `ApplyBattlerPpTargetLoss` | `611ed76fd2511c7777a27280c9f1ce88dd4907ee` |

Labels:

- `C2:BCB9 ApplyBattlerPpTargetLoss`

Evidence:

- `notes/c2-pp-loss-and-call-for-help-width-helpers-c2bcb9-c2bd13.md`

### `src/c2/c2_077d_redraw_dirty_party_hp_pp_windows.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:077D..C2:07B6` | 57 | `RedrawDirtyPartyHpPpWindows` | `d28488e532e7d132bd37cc1e2e936f1da228783d` |

Labels:

- `C2:077D RedrawDirtyPartyHpPpWindows`

Evidence:

- `notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md`

### `src/c2/c2_07b6_mark_and_redraw_party_hp_pp_window.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:07B6..C2:07E1` | 43 | `MarkAndRedrawPartyHpPpWindow` | `217fcfac31b685fbfc33f5f89c190f31e2ea55c4` |

Labels:

- `C2:07B6 MarkAndRedrawPartyHpPpWindow`

Evidence:

- `notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md`

### `src/c2/c2_c572_run_final_prayer_opening_transition.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:C572..C2:C5D1` | 95 | `RunFinalPrayerOpeningTransition` | `9d5370808e4ee3994e171f8cac9f0a1465f4c95b` |

Labels:

- `C2:C572 RunFinalPrayerOpeningTransition`

Evidence:

- `notes/class2-final-prayer-family-c2c572-c2c6f0.md`

### `src/c2/c2_c5d1_run_final_prayer_damage_phase2.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:C5D1..C2:C5FA` | 41 | `RunFinalPrayerDamagePhase2` | `e59dafc1562690bf7315ccf383acd5281e339581` |

Labels:

- `C2:C5D1 RunFinalPrayerDamagePhase2`

Evidence:

- `notes/class2-final-prayer-family-c2c572-c2c6f0.md`

### `src/c2/c2_c623_run_final_prayer_damage_phase4.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:C623..C2:C64C` | 41 | `RunFinalPrayerDamagePhase4` | `60e6d7313b99dbe9c424a30662ed05c017c117df` |

Labels:

- `C2:C623 RunFinalPrayerDamagePhase4`

Evidence:

- `notes/class2-final-prayer-family-c2c572-c2c6f0.md`

### `src/c2/c2_c5fa_run_final_prayer_damage_phase3.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:C5FA..C2:C623` | 41 | `RunFinalPrayerDamagePhase3` | `75f644efba902bb2143f891bd28b1748999809d7` |

Labels:

- `C2:C5FA RunFinalPrayerDamagePhase3`

Evidence:

- `notes/class2-final-prayer-family-c2c572-c2c6f0.md`

### `src/c2/c2_c64c_run_final_prayer_damage_phase5.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:C64C..C2:C675` | 41 | `RunFinalPrayerDamagePhase5` | `c9b1a18a4c1ce4818fdd34d55706374c5edef93e` |

Labels:

- `C2:C64C RunFinalPrayerDamagePhase5`

Evidence:

- `notes/class2-final-prayer-family-c2c572-c2c6f0.md`

### `src/c2/c2_c675_run_final_prayer_damage_phase6.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:C675..C2:C69E` | 41 | `RunFinalPrayerDamagePhase6` | `9f92e9a6e10c43fa6299c812b17b2a0dde7140c9` |

Labels:

- `C2:C675 RunFinalPrayerDamagePhase6`

Evidence:

- `notes/class2-final-prayer-family-c2c572-c2c6f0.md`

### `src/c2/c2_c69e_run_final_prayer_damage_phase7.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:C69E..C2:C6D0` | 50 | `RunFinalPrayerDamagePhase7` | `904122ef59afcc10946edfde4cb2dd7608f35e6e` |

Labels:

- `C2:C69E RunFinalPrayerDamagePhase7`

Evidence:

- `notes/class2-final-prayer-family-c2c572-c2c6f0.md`

### `src/c2/c2_c6d0_run_final_prayer_narrative_phase8.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:C6D0..C2:C6F0` | 32 | `RunFinalPrayerNarrativePhase8` | `e927376cc80fa997fc95c6c75f0cf57466f114ca` |

Labels:

- `C2:C6D0 RunFinalPrayerNarrativePhase8`

Evidence:

- `notes/class2-final-prayer-family-c2c572-c2c6f0.md`

### `src/c2/c2_087c_refresh_dirty_hp_pp_and_open_text_windows.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:087C..C2:08B8` | 60 | `RefreshDirtyHpPpAndOpenTextWindows` | `4672e2ffa90fe13791a4b1d26e4b614d36661244` |

Labels:

- `C2:087C RefreshDirtyHpPpAndOpenTextWindows`

Evidence:

- `notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md`

### `src/c2/c2_a5ec_run_damage_plus_solidification_item_action.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:A5EC..C2:A630` | 68 | `RunDamagePlusSolidificationItemAction` | `23d21ef3b83915e258ef775132e9cde1e36e4f58` |

Labels:

- `C2:A5EC RunDamagePlusSolidificationItemAction`

Evidence:

- `notes/class2-solidification-item-action-c2a5ec-a630.md`

### `src/c2/c2_239d_check_party_overlay_registry_presence.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:239D..C2:23D9` | 60 | `CheckPartyOverlayRegistryPresence` | `6ccc335d8f93cf8d6c0c90e63267801e0be5a1bd` |

Labels:

- `C2:239D CheckPartyOverlayRegistryPresence`

Evidence:

- `notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md`

### `src/c2/c2_fade_reset_enemy_sprite_color_wave_slot.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:FADE..C2:FB35` | 87 | `ResetEnemySpriteColorWaveSlot` | `587d68892574c9f96398aaa98ff3af6b87740838` |

Labels:

- `C2:FADE ResetEnemySpriteColorWaveSlot`

Evidence:

- `notes/c2-battle-sprite-render-and-palette-tail-c2eee7-c2ff9a.md`

### `src/c2/c2_fb35_enemy_sprite_color_wave_comparison_helper.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:FB35..C2:FCA6` | 369 | `EnemySpriteColorWaveComparisonHelper` | `62c3a4aeff7a4ebe2237a8144b17a2bec440259a` |

Labels:

- `C2:FB35 EnemySpriteColorWaveComparisonHelper`

Evidence:

- `notes/c2-battle-sprite-render-and-palette-tail-c2eee7-c2ff9a.md`

### `src/c2/c2_a630_apply_solidification_status_from_item_action.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:A630..C2:A658` | 40 | `ApplySolidificationStatusFromItemAction` | `a471b85d72bdca251180eae9c2374c32e22e0b95` |

Labels:

- `C2:A630 ApplySolidificationStatusFromItemAction`

Evidence:

- `notes/class2-solidification-item-action-c2a5ec-a630.md`

### `src/c2/c2_30f3_snapshot_respawn_warp_target_state.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:30F3..C2:3109` | 22 | `SnapshotRespawnWarpTargetState` | `907ed58d9fa1d060c13ea09a117dbedb846ec6b4` |

Labels:

- `C2:30F3 SnapshotRespawnWarpTargetState`

Evidence:

- `notes/respawn-warp-target-snapshot-helper-c230f3.md`

### `src/c2/c2_eacf_wait_for_battle_effect_step_ready.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:EACF..C2:EAEA` | 27 | `WaitForBattleEffectStepReady` | `93d8938ac585564fef7148b87772c3ad5ae08606` |

Labels:

- `C2:EACF WaitForBattleEffectStepReady`

Evidence:

- `notes/class2-busy-helper-eacf-and-window-setup.md`

### `src/c2/c2_eaea_build_battle_sprite_allocation_record.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:EAEA..C2:EEE7` | 1021 | `BuildBattleSpriteAllocationRecord` | `ddcebdff5ebe85a8df7027e570da4c501521e5d3` |

Labels:

- `C2:EAEA BuildBattleSpriteAllocationRecord`

Evidence:

- `notes/c2-battle-sprite-render-and-palette-tail-c2eee7-c2ff9a.md`

### `src/c2/c2_e6b6_advance_psi_animation_frame_and_palette_state_body.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:E6B6..C2:E8C4` | 526 | `AdvancePsiAnimationFrameAndPaletteStateBody` | `e34837d8901574e60780425aca0172e03b14439b` |

Labels:

- `C2:E6B6 AdvancePsiAnimationFrameAndPaletteStateBody`

Evidence:

- `notes/c2-psi-swirl-overlay-tail-c2e6b3-c2ea74.md`

### `src/c2/c2_a821_run_super_bomb_action.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:A821..C2:A82A` | 9 | `RunSuperBombAction` | `2345d8e131f349896847a78ded4e15baa00b53ba` |

Labels:

- `C2:A821 RunSuperBombAction`

Evidence:

- `notes/class2-bomb-common-family-c2a658-c2a821.md`

### `src/c2/c2_a82a_run_solidification_item_action.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:A82A..C2:A86B` | 65 | `RunSolidificationItemAction` | `aa075d307cfe595fcea3bd4283be119d81e78e01` |

Labels:

- `C2:A82A RunSolidificationItemAction`

Evidence:

- `notes/class2-bomb-common-family-c2a658-c2a821.md`

### `src/c2/c2_a86b_run_random_damage_item_action.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:A86B..C2:A89D` | 50 | `RunRandomDamageItemAction` | `835c11d6c075cd8a33e19a029e9e620e5a6e44b6` |

Labels:

- `C2:A86B RunRandomDamageItemAction`

Evidence:

- `notes/class2-bomb-common-family-c2a658-c2a821.md`

### `src/c2/c2_c41f_run_final_prayer_narrative_transition.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:C41F..C2:C572` | 339 | `RunFinalPrayerNarrativeTransition` | `7eccb44161553feb7226bdd2045e6845caad0a89` |

Labels:

- `C2:C41F RunFinalPrayerNarrativeTransition`

Evidence:

- `notes/class2-prayer-common-helpers-c2c37a-c2c3e2-c2c41f.md`

### `src/c2/c2_3109_battle_start_ufo_present_fallback_table.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:3109..C2:311B` | 18 | `BattleStartUfoPresentFallbackTable` | `c8b08aa7771c58023987eb637dcbc4dbf4d7059d` |

Labels:

- `C2:3109 BattleStartUfoPresentFallbackTable`

Evidence:

- `notes\class2-battle-start-extra-message-state-4dbc-aa10.md`

### `src/c2/c2_311b_run_battle_start_present_and_message_controller.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:311B..C2:3B66` | 2635 | `RunBattleStartPresentAndMessageController` | `3d21502b50210548ec086cee108e3d29baed6c91` |

Labels:

- `C2:311B RunBattleStartPresentAndMessageController`

Evidence:

- `notes\class2-battle-start-extra-message-state-4dbc-aa10.md`

### `src/c2/c2_4a80_populate_candidate_pool_from_variable_sources.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:4A8A..C2:4F03` | 1145 | `PopulateCandidatePoolFromVariableSources` | `8a7f68f676e009f7bbac2c4278c24c0ae263eae1` |

Labels:

- `C2:4A8A PopulateCandidatePoolFromVariableSources`

Evidence:

- `notes\class2-candidate-population-and-ranking.md`

### `src/c2/c2_c6f0_run_final_prayer_finale_opening_sequence.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:C6F0..C2:C8C8` | 472 | `RunFinalPrayerFinaleOpeningSequence` | `c478211b7da9a0b19b80d31f8c4ccffbecefb52b` |

Labels:

- `C2:C6F0 RunFinalPrayerFinaleOpeningSequence`

Evidence:

- `notes\class2-final-prayer-family-c2c572-c2c6f0.md`

### `src/c2/c2_c8c8_load_final_prayer_finale_tilemap_state.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:C8C8..C2:C92D` | 101 | `LoadFinalPrayerFinaleTilemapState` | `1009db7a1d3f82eb4a54850a63a55b1768736d3f` |

Labels:

- `C2:C8C8 LoadFinalPrayerFinaleTilemapState`

Evidence:

- `notes\class2-final-prayer-family-c2c572-c2c6f0.md`

### `src/c2/c2_c92d_run_final_prayer_finale_record_player.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:C92D..C2:CFE5` | 1720 | `RunFinalPrayerFinaleRecordPlayer` | `a2cc4ad68243db8698c60ba418d498cf8704ad54` |

Labels:

- `C2:C92D RunFinalPrayerFinaleRecordPlayer`

Evidence:

- `notes\class2-final-prayer-family-c2c572-c2c6f0.md`

### `src/c2/c2_0000_run_enemy_sunstroke_check.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:0000..C2:00B9` | 185 | `RunEnemySunstrokeCheck` | `7484cfe62d6290f05b8f8001f4c2d4449ab0c3b7` |

Labels:

- `C2:0000 RunEnemySunstrokeCheck`

Evidence:

- `notes\c2-source-promotion-candidates-workahead.md`

### `src/c2/c2_e6b3_advance_psi_animation_frame_and_palette_state.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:E6B3..C2:E6B6` | 3 | `AdvancePsiAnimationFrameAndPaletteStatePrefix` | `bbe0b447f3ad331c5d2dea6e8427616cbeb3fad3` |

Labels:

- `C2:E6B3 AdvancePsiAnimationFrameAndPaletteStatePrefix`

Evidence:

- `notes\c2-psi-swirl-overlay-tail-c2e6b3-c2ea74.md`

### `src/c2/c2_00b9_enemy_sunstroke_check_tail_table.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:00B9..C2:00D1` | 24 | `EnemySunstrokeCheckTailTable` | `75a9edd41e20424692e7316f41089221943db36d` |

Labels:

- `C2:00B9 EnemySunstrokeCheckTailTable`

Evidence:

- `notes\c2-source-promotion-candidates-workahead.md`

### `src/c2/c2_ff9a_check_overworld_position_hash_threshold3_of8.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:FF9A..C2:FFB7` | 29 | `CheckOverworldPositionHashThreshold3Of8` | `01f3eba585197ed867b08215dcb451fdf14fe689` |

Labels:

- `C2:FF9A CheckOverworldPositionHashThreshold3Of8`

Evidence:

- `notes\c2-battle-sprite-render-and-palette-tail-c2eee7-c2ff9a.md`

### `src/c2/c2_ffb7_bank_end_tail_bytes.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:FFB7..C2:10000` | 73 | `BankEndTailBytes` | `1c412f0192010672dd5fee00abab964a2d7c4ae0` |

Labels:

- `C2:FFB7 BankEndTailBytes`

Evidence:

- `notes\c2-battle-sprite-render-and-palette-tail-c2eee7-c2ff9a.md`

### `src/c2/c2_4f52_display_battle_start_status_messages_prelude.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:4F52..C2:5024` | 210 | `DisplayBattleStartStatusMessagesPrelude` | `fd47beb74efa1622b453be654b82dfea4537a867` |

Labels:

- `C2:4F52 DisplayBattleStartStatusMessagesPrelude`

Evidence:

- `notes\class2-concrete-battle-text-call-paths.md`
- `notes\c2-ef-battle-text-contract-workahead.md`
- `notes\class2-end-to-end-gate-path-5540.md`

### `src/c2/c2_5024_run_battle_start_candidate_controller_front.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:5024..C2:5AFB` | 2775 | `RunBattleStartCandidateControllerFront` | `0c1d2a45e872dea11815b6d4dbea0c4a83a68c75` |

Labels:

- `C2:5024 RunBattleStartCandidateControllerFront`

Evidence:

- `notes\class2-end-to-end-gate-path-5540.md`
- `notes\class2-second-stage-selector-a970.md`
- `notes\class2-post-selection-controller-phases.md`

### `src/c2/c2_5afb_run_battle_start_candidate_controller_back.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:5AFB..C2:6189` | 1678 | `RunBattleStartCandidateControllerBack` | `033d92dfe09c64c4776503f6a84f79796712a8cc` |

Labels:

- `C2:5AFB RunBattleStartCandidateControllerBack`

Evidence:

- `notes\class2-end-to-end-gate-path-5540.md`
- `notes\class2-second-stage-selector-a970.md`
- `notes\class2-post-selection-controller-phases.md`

### `src/c2/c2_7eaf_run_hit_resolution_and_status_action_cluster.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:7EAF..C2:8BBE` | 3343 | `RunHitResolutionAndStatusActionCluster` | `dfdbfd2dee94e88503837814120b99558732c6b9` |

Labels:

- `C2:7EAF RunHitResolutionAndStatusActionCluster`

Evidence:

- `notes\class2-reflected-hit-context-rebuild.md`

### `src/c2/c2_7e8a_swap_reflected_hit_battle_text_contexts.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:7E8A..C2:7EAF` | 37 | `SwapReflectedHitBattleTextContexts` | `b6e7b544690f27feb9d7dc08c49c79197b36d686` |

Labels:

- `C2:7E8A SwapReflectedHitBattleTextContexts`

Evidence:

- `notes\class2-reflected-hit-context-rebuild.md`

### `src/c2/c2_a89d_run_random_damage_and_status_item_action_cluster.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:A89D..C2:AF1F` | 1666 | `RunRandomDamageAndStatusItemActionCluster` | `ec15972f3bcddaf42126362dd29d9261c2855b77` |

Labels:

- `C2:A89D RunRandomDamageAndStatusItemActionCluster`

Evidence:

- `notes\c2-ef-battle-text-contract-workahead.md`
- `notes\class2-late-normalization-and-odor-family-c29051-c29254.md`

### `src/c2/c2_e0e7_clear_battle_visual_flash_state_and_layer_config.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:E0E7..C2:E116` | 47 | `ClearBattleVisualFlashStateAndLayerConfig` | `e9d3c634cbc793297b67aa4d8584f74f0bcf0d4f` |

Labels:

- `C2:E0E7 ClearBattleVisualFlashStateAndLayerConfig`

Evidence:

- `notes\c2-battlebg-load-and-palette-effect-corridor-c2cfe5-c2e0e7.md`

### `src/c2/c2_e116_run_battle_visual_flash_and_bg_effect_body.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:E116..C2:E6B3` | 1437 | `RunBattleVisualFlashAndBgEffectBody` | `35130b0d39bacf3bec99b7f6c3ae91fff471cafc` |

Labels:

- `C2:E116 RunBattleVisualFlashAndBgEffectBody`

Evidence:

- `notes\c2-battlebg-load-and-palette-effect-corridor-c2cfe5-c2e0e7.md`

### `src/c2/c2_bd13_sum_active_enemy_battle_sprite_widths.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:BD13..C2:BE6C` | 345 | `SumActiveEnemyBattleSpriteWidthsAndCallForHelpPrefix` | `bb336f4b4c29e8831a78fd512a6783bad3ca1278` |

Labels:

- `C2:BD13 SumActiveEnemyBattleSpriteWidthsAndCallForHelpPrefix`

Evidence:

- `notes\c2-pp-loss-and-call-for-help-width-helpers-c2bcb9-c2bd13.md`
- `notes\class2-special-event-results-c29298-c2c14e.md`

### `src/c2/c2_be6c_run_call_for_help_enemy_selection_body.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:BE6C..C2:C14E` | 738 | `RunCallForHelpEnemySelectionBody` | `bdd6c46a5469cdb96816503832c804821cfd38a2` |

Labels:

- `C2:BE6C RunCallForHelpEnemySelectionBody`

Evidence:

- `notes\c2-pp-loss-and-call-for-help-width-helpers-c2bcb9-c2bd13.md`
- `notes\class2-special-event-results-c29298-c2c14e.md`

### `src/c2/c2_af1f_snapshot_restore_battler_normalization_context.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:AF1F..C2:B172` | 595 | `SnapshotRestoreBattlerNormalizationContext` | `2ea5b40ff9f3adbfd49c20d4b397a06c02b36754` |

Labels:

- `C2:AF1F SnapshotRestoreBattlerNormalizationContext`

Evidence:

- `notes\class2-late-normalization-and-odor-family-c29051-c29254.md`

### `src/c2/c2_b172_resolve_late_normalization_and_odor_continuation.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:B172..C2:B2E0` | 366 | `ResolveLateNormalizationAndOdorContinuation` | `85149acdd32679cb7a87270a617c28eefabfc82a` |

Labels:

- `C2:B172 ResolveLateNormalizationAndOdorContinuation`

Evidence:

- `notes\class2-late-normalization-and-odor-family-c29051-c29254.md`

### `src/c2/c2_dae3_prime_layer1_battle_bg_distortion_swap.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:DAE3..C2:DB14` | 49 | `PrimeLayer1BattleBgDistortionSwap` | `9d76ff9f6899f269f75131b221aee5ed4d546d42` |

Labels:

- `C2:DAE3 PrimeLayer1BattleBgDistortionSwap`

Evidence:

- `notes\c2-battlebg-load-and-palette-effect-corridor-c2cfe5-c2e0e7.md`

### `src/c2/c2_db14_run_battle_bg_per_frame_update_body.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:DB14..C2:DE0F` | 763 | `RunBattleBgPerFrameUpdateBody` | `8a4969e92a2374858f5905a438ee8c7cf2e635a6` |

Labels:

- `C2:DB14 RunBattleBgPerFrameUpdateBody`

Evidence:

- `notes\c2-battlebg-load-and-palette-effect-corridor-c2cfe5-c2e0e7.md`

### `src/c2/c2_d0ac_build_battle_letterbox_hdma_table.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:D0AC..C2:D121` | 117 | `BuildBattleLetterboxHdmaTable` | `3c958c36f7fa8bc6692a21249693f7c47c3601ff` |

Labels:

- `C2:D0AC BuildBattleLetterboxHdmaTable`

Evidence:

- `notes\c2-battlebg-load-and-palette-effect-corridor-c2cfe5-c2e0e7.md`

### `src/c2/c2_d121_load_battle_background_main_body.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:D121..C2:DAE3` | 2498 | `LoadBattleBackgroundMainBody` | `798e627a3322494fee1906c710dc10c32d8688c8` |

Labels:

- `C2:D121 LoadBattleBackgroundMainBody`

Evidence:

- `refs\ebsrc-main\ebsrc-main\src\battle\load_battlebg.asm`
- `notes\c2-battlebg-load-and-palette-effect-corridor-c2cfe5-c2e0e7.md`

### `src/c2/c2_00d1_window_reset_initial_coordinate_data.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:00D1..C2:0266` | 405 | `WindowInitialCoordinateHeaderAndResetData` | `3b7ab9780392e0bf909597d9b089c155fa7b08ed` |

Labels:

- `C2:00D1 WindowInitialCoordinateHeaderAndResetData`

Evidence:

- `notes\c2-symbol-only-stragglers-c200d1-c20d3f.md`

### `src/c2/c2_0912_name_entry_grid_character_offset_table.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:0912..C2:0958` | 70 | `NameEntryGridCharacterOffsetTable` | `6ce618d3151cf264c9f3bff6ba718590ccfd5172` |

Labels:

- `C2:0912 NameEntryGridCharacterOffsetTable`

Evidence:

- `notes\c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md`

### `src/c2/c2_0958_menu_or_name_entry_mask_table.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C2:0958..C2:09A0` | 72 | `MenuOrNameEntryMaskTable` | `1576e7ce0b6915b7b2bdbf15c9b82646475d71e6` |

Labels:

- `C2:0958 MenuOrNameEntryMaskTable`

Evidence:

- `notes\c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md`

## Notes

The scaffold preserves intentional source-adjacent data gaps from the manifest and validates each protected span against the original ROM bytes.
