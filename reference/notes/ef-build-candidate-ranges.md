# EF build-candidate byte ranges

This manifest records source slices promoted into the reusable source-bank scaffold pipeline.

## Summary

- ranges: `28`
- total bytes: `65536`
- source bytes: `10828`
- data gap bytes: `54708`

## Ranges

| Level | Source Path | Range | Span Bytes | Source Bytes | Data Gap Bytes | SHA-1 |
| --- | --- | --- | ---: | ---: | ---: | --- |
| `build-candidate` | `src/ef/ef_0000_00bb_enemy_flashing_helpers.asm` | `EF:0000..EF:00BB` | 187 | 187 | 0 | `77dd6f3f57c4a6fea5be7aa4af69a2691e32b8c7` |
| `build-candidate` | `src/ef/ef_00bb_0256_battle_overworld_visual_helpers.asm` | `EF:00BB..EF:0256` | 411 | 411 | 0 | `3c3e08e10a1dec3621ddfcfeef514509a9acc646` |
| `build-candidate` | `src/ef/ef_0256_027d_audio_pause_resume_flags.asm` | `EF:0256..EF:027D` | 39 | 39 | 0 | `9a99a99d847f6e82b9f4fa3bcd194daa2f18905d` |
| `build-candidate` | `src/ef/ef_027d_0591_overworld_entity_snapshot_helpers.asm` | `EF:027D..EF:0591` | 788 | 788 | 0 | `45d47823667c42199d00e777f6dc6110314aa187` |
| `build-candidate` | `src/ef/ef_0591_05a9_sram_signature_and_save_block_flags.asm` | `EF:0591..EF:05A9` | 24 | 0 | 24 | `7301afe764d5f3200bbbcab6bc2436e84975ecd4` |
| `build-candidate` | `src/ef/ef_05a9_0c3d_save_sram_helpers.asm` | `EF:05A9..EF:0C3D` | 1684 | 1684 | 0 | `e4fbde63d6b5388fcafd04510977c570aeed2702` |
| `build-candidate` | `src/ef/ef_0c3d_0ca7_front_unknown_tail_helpers.asm` | `EF:0C3D..EF:0CA7` | 106 | 106 | 0 | `1959bd78161c2d3b053fbb4a84349a3adbcdcdfa` |
| `build-candidate` | `src/ef/ef_0ca7_delivery_selector_helper_cluster.asm` | `EF:0CA7..EF:101B` | 884 | 884 | 0 | `67263f36ee80d3155ec61cce95d7194870b8c2d7` |
| `build-candidate` | `src/ef/ef_101b_4a40_map_tileset_sprite_table_data.asm` | `EF:101B..EF:4A40` | 14885 | 0 | 14885 | `6e3c7770032eabf33502d47f18c448999ffb2023` |
| `build-candidate` | `src/ef/ef_4a40_4e20_sound_stone_presentation_table_data.asm` | `EF:4A40..EF:4E20` | 992 | 0 | 992 | `ea78ee3d61cd39ebf81f5ac0793353e61ff7c41e` |
| `build-candidate` | `src/ef/ef_4e20_c51b_text_payload_data.asm` | `EF:4E20..EF:C51B` | 30459 | 0 | 30459 | `1419dd1b8b80745a5a22e78d498fcb67a60547aa` |
| `build-candidate` | `src/ef/ef_c51b_d56f_text_glyph_mask_tables.asm` | `EF:C51B..EF:D56F` | 4180 | 0 | 4180 | `73467ad28329342430e2add59df931780f2e488b` |
| `build-candidate` | `src/ef/ef_d56f_d6d4_debug_sound_menu_helpers.asm` | `EF:D56F..EF:D6D4` | 357 | 357 | 0 | `50ea92d8170a2fe213f113009bd9918f69a04d91` |
| `build-candidate` | `src/ef/ef_d6d4_d8b5_debug_sound_menu_controller.asm` | `EF:D6D4..EF:D8B5` | 481 | 481 | 0 | `7dfefdcb21fdb15ad5774c0b8e05d249a9456610` |
| `build-candidate` | `src/ef/ef_d8b5_d95e_debug_menu_option_strings.asm` | `EF:D8B5..EF:D95E` | 169 | 0 | 169 | `395083f64a645515a8e42c25127744e5764ec74c` |
| `build-candidate` | `src/ef/ef_d95e_dabd_debug_menu_graphics_state_init.asm` | `EF:D95E..EF:DABD` | 351 | 351 | 0 | `593aca35ad4b1bf4127ae9cc2d8ca981b37b8ac8` |
| `build-candidate` | `src/ef/ef_dabd_dcbc_debug_menu_text_number_helpers.asm` | `EF:DABD..EF:DCBC` | 511 | 511 | 0 | `69230efc6b0048c238d040518a61002058c4bc4c` |
| `build-candidate` | `src/ef/ef_dcbc_de1a_debug_check_position_overlay.asm` | `EF:DCBC..EF:DE1A` | 350 | 350 | 0 | `7be9bf793988efca02669a8a91b6ceea495b57bb` |
| `build-candidate` | `src/ef/ef_de1a_df0b_debug_view_character_overlay.asm` | `EF:DE1A..EF:DF0B` | 241 | 241 | 0 | `810ee840a220dbb001b044ad9d1df00b0b7b8895` |
| `build-candidate` | `src/ef/ef_df0b_e175_debug_overlay_tile_helpers.asm` | `EF:DF0B..EF:E175` | 618 | 618 | 0 | `15cd4ce61ad31ea3f03158483c285caf717d41d8` |
| `build-candidate` | `src/ef/ef_e175_eb1d_debug_menu_runtime_helpers.asm` | `EF:E175..EF:EB1D` | 2472 | 2472 | 0 | `622254c8aa62a39311c8331d5a5fc32a1dee77c6` |
| `build-candidate` | `src/ef/ef_eb1d_eb2a_debug_color_math_window_table.asm` | `EF:EB1D..EF:EB2A` | 13 | 0 | 13 | `49c3bca75bbbe59051ec87f6e80fc31946136449` |
| `build-candidate` | `src/ef/ef_eb2a_eb3d_debug_color_math_dma_reset.asm` | `EF:EB2A..EF:EB3D` | 19 | 19 | 0 | `b7703e2d448dca9da5dd3146081d989ae457fc32` |
| `build-candidate` | `src/ef/ef_eb3d_eb5f_debug_cursor_tilemap_data.asm` | `EF:EB3D..EF:EB5F` | 34 | 0 | 34 | `dd51f90c8b6debd5ab65cfcad48a0f1cf3a4fb6a` |
| `build-candidate` | `src/ef/asset_debug_menu_font.asm` | `EF:EB5F..EF:EF70` | 1041 | 1041 | 0 | `7d8195145f270d5d310df09b7c73a32cca868614` |
| `build-candidate` | `src/ef/table_141_data_unknown_efef70_asm.asm` | `EF:EF70..EF:EFB7` | 71 | 0 | 71 | `274b0fc73b39180dd07b1df5e5fd1077c481387d` |
| `build-candidate` | `src/ef/asset_debug_cursor_graphics.asm` | `EF:EFB7..EF:F0D7` | 288 | 288 | 0 | `d4aa5ac9ca83bf8da624ffab3ed1c95d0e85cdd8` |
| `build-candidate` | `src/ef/asset_bank_ef_gap_1_tailpadding.asm` | `EF:F0D7..EF:10000` | 3881 | 0 | 3881 | `8e09b47444551098bd77c1dd73e19f0a9ba0a71f` |

## Source Segments

### `src/ef/ef_0000_00bb_enemy_flashing_helpers.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `EF:0000..EF:00BB` | 187 | `EnemyFlashingHelpers` | `77dd6f3f57c4a6fea5be7aa4af69a2691e32b8c7` |

Labels:

- `EF:0000 EnemyFlashingHelpers`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank2f.asm`
- `refs/ebsrc-main/ebsrc-main/src/battle/enemy_flashing_off.asm`
- `refs/ebsrc-main/ebsrc-main/src/battle/enemy_flashing_on.asm`
- `notes/bank-ef-first-pass.md`
- `notes/ef-readable-source-split-queue.md`
- `notes/ef-front-source-closure-0000-0ca7.md`

### `src/ef/ef_00bb_0256_battle_overworld_visual_helpers.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `EF:00BB..EF:0256` | 411 | `BattleOverworldVisualHelpers` | `3c3e08e10a1dec3621ddfcfeef514509a9acc646` |

Labels:

- `EF:00BB BattleOverworldVisualHelpers`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank2f.asm`
- `notes/bank-ef-first-pass.md`
- `notes/ef-readable-source-split-queue.md`
- `notes/ef-front-source-closure-0000-0ca7.md`

### `src/ef/ef_0256_027d_audio_pause_resume_flags.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `EF:0256..EF:027D` | 39 | `AudioPauseResumeFlags` | `9a99a99d847f6e82b9f4fa3bcd194daa2f18905d` |

Labels:

- `EF:0256 AudioPauseResumeFlags`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank2f.asm`
- `refs/ebsrc-main/ebsrc-main/src/audio/pause_music.asm`
- `refs/ebsrc-main/ebsrc-main/src/audio/resume_music.asm`
- `notes/bank-ef-first-pass.md`
- `notes/ef-readable-source-split-queue.md`
- `notes/ef-front-source-closure-0000-0ca7.md`

### `src/ef/ef_027d_0591_overworld_entity_snapshot_helpers.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `EF:027D..EF:0591` | 788 | `OverworldEntitySnapshotHelpers` | `45d47823667c42199d00e777f6dc6110314aa187` |

Labels:

- `EF:027D OverworldEntitySnapshotHelpers`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank2f.asm`
- `notes/bank-ef-first-pass.md`
- `notes/ef-readable-source-split-queue.md`
- `notes/ef-front-source-closure-0000-0ca7.md`

### `src/ef/ef_0591_05a9_sram_signature_and_save_block_flags.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `EF:0591..EF:05A9` (`24` bytes, SHA-1 `7301afe764d5f3200bbbcab6bc2436e84975ecd4`) `EfSramSignatureAndSaveBlockFlags`

Labels:

- `EF:0591 EfSramSignatureAndSaveBlockFlags`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank2f.asm`
- `refs/ebsrc-main/ebsrc-main/include/symbols/bank2f.inc.asm`
- `notes/bank-ef-first-pass.md`
- `notes/ef-readable-source-split-queue.md`
- `notes/ef-front-source-closure-0000-0ca7.md`

### `src/ef/ef_05a9_0c3d_save_sram_helpers.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `EF:05A9..EF:0C3D` | 1684 | `SaveSramHelperCluster` | `e4fbde63d6b5388fcafd04510977c570aeed2702` |

Labels:

- `EF:05A9 SaveSramHelperCluster`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank2f.asm`
- `refs/ebsrc-main/ebsrc-main/include/symbols/bank2f.inc.asm`
- `notes/bank-ef-first-pass.md`
- `notes/ef-readable-source-split-queue.md`
- `notes/ef-front-source-closure-0000-0ca7.md`

### `src/ef/ef_0c3d_0ca7_front_unknown_tail_helpers.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `EF:0C3D..EF:0CA7` | 106 | `EfFrontUnknownTailHelpers` | `1959bd78161c2d3b053fbb4a84349a3adbcdcdfa` |

Labels:

- `EF:0C3D EfFrontUnknownTailHelpers`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank2f.asm`
- `refs/ebsrc-main/ebsrc-main/include/symbols/bank2f.inc.asm`
- `notes/bank-ef-first-pass.md`
- `notes/ef-readable-source-split-queue.md`
- `notes/ef-front-source-closure-0000-0ca7.md`

### `src/ef/ef_0ca7_delivery_selector_helper_cluster.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `EF:0CA7..EF:101B` | 884 | `DeliverySelectorHelperCluster` | `67263f36ee80d3155ec61cce95d7194870b8c2d7` |

Labels:

- `EF:0CA7 DeliverySelectorHelperCluster`

Evidence:

- `notes/delivery-row-helpers-ef0e67-ef0ead.md`
- `notes/selector-row-config-family-ef0ee8.md`
- `notes/timed-delivery-state-helpers-ef0f60-fdb-ff6.md`
- `notes/ef-readable-source-split-queue.md`

### `src/ef/ef_101b_4a40_map_tileset_sprite_table_data.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `EF:101B..EF:4A40` (`14885` bytes, SHA-1 `6e3c7770032eabf33502d47f18c448999ffb2023`) `EfMapTilesetSpriteTableData`

Labels:

- `EF:101B EfMapTilesetSpriteTableData`

Evidence:

- `notes/bank-ef-first-pass.md`
- `notes/ef-readable-source-split-queue.md`
- `notes/landing-profile-asset-families-ef105b-10ab-11cb-121b.md`

### `src/ef/ef_4a40_4e20_sound_stone_presentation_table_data.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `EF:4A40..EF:4E20` (`992` bytes, SHA-1 `ea78ee3d61cd39ebf81f5ac0793353e61ff7c41e`) `EfSoundStonePresentationTableData`

Labels:

- `EF:4A40 EfSoundStonePresentationTableData`

Evidence:

- `notes/bank-ef-first-pass.md`
- `notes/sound-stone-presentation-data-c4ac57.md`
- `notes/ef-readable-source-split-queue.md`

### `src/ef/ef_4e20_c51b_text_payload_data.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `EF:4E20..EF:4E38` (`24` bytes, SHA-1 `a38fb2b85cb816804013896b3190cf035712a451`) `EExplPsiMsgExplPsiHissatsuAlfa`
- `EF:4E38..EF:4E51` (`25` bytes, SHA-1 `f670133c5279693e2a340de17f09698fffdc97f1`) `EExplPsiMsgExplPsiHissatsuBeta`
- `EF:4E51..EF:4E6A` (`25` bytes, SHA-1 `e833f10e54861e18528aa466fb2322fe91d7e3ef`) `EExplPsiMsgExplPsiHissatsuGamma`
- `EF:4E6A..EF:4E83` (`25` bytes, SHA-1 `54d1dce5f8dc4970e180177b0c2d5e2c720a875b`) `EExplPsiMsgExplPsiHissatsuOmega`
- `EF:4E83..EF:4E99` (`22` bytes, SHA-1 `7bee6e901f11396ff73966f08f1aabe73bfd8f4c`) `EExplPsiMsgExplPsiFireAlfa`
- `EF:4E99..EF:4EB0` (`23` bytes, SHA-1 `5fbf5b6573e5e0f7343777f8ff86696267b99f9e`) `EExplPsiMsgExplPsiFireBeta`
- `EF:4EB0..EF:4EC7` (`23` bytes, SHA-1 `c5188cf1a223c059e41d5d7c045ead92c86dc87a`) `EExplPsiMsgExplPsiFireGamma`
- `EF:4EC7..EF:4EDE` (`23` bytes, SHA-1 `a9f83ac47f88ed95cd9c1a7c2f86fbac720f5d6c`) `EExplPsiMsgExplPsiFireOmega`
- `EF:4EDE..EF:4F06` (`40` bytes, SHA-1 `287050333550079e3b04ba4f82430416cc335619`) `EExplPsiMsgExplPsiFreezAlfa`
- `EF:4F06..EF:4F2E` (`40` bytes, SHA-1 `cf65c6e67805d8c33f7ee48f308fc137ad854914`) `EExplPsiMsgExplPsiFreezBeta`
- `EF:4F2E..EF:4F56` (`40` bytes, SHA-1 `7d9d47ab81b4fe564baaf2175801c5ba0a0b1e86`) `EExplPsiMsgExplPsiFreezGamma`
- `EF:4F56..EF:4F7E` (`40` bytes, SHA-1 `8787262214b9abf471d901d973590ec18faea2fa`) `EExplPsiMsgExplPsiFreezOmega`
- `EF:4F7E..EF:4FA6` (`40` bytes, SHA-1 `59145d2e6c2654b81e2016d1d72aca8af696ea28`) `EExplPsiMsgExplPsiThunderAlfa`
- `EF:4FA6..EF:4FDC` (`54` bytes, SHA-1 `a1ea91256935bd297e3af2ca66ca97b53ea14590`) `EExplPsiMsgExplPsiThunderBeta`
- `EF:4FDC..EF:5013` (`55` bytes, SHA-1 `5e2bf0d467d2dea5b108f7b84c505b1deeb62b14`) `EExplPsiMsgExplPsiThunderGamma`
- `EF:5013..EF:5049` (`54` bytes, SHA-1 `d981aac242c9ae506eda0d79eed9ec90554ebcb8`) `EExplPsiMsgExplPsiThunderOmega`
- `EF:5049..EF:506B` (`34` bytes, SHA-1 `e181e76e79ed169246e1228277acfac373709e18`) `EExplPsiMsgExplPsiFlashAlfa`
- `EF:506B..EF:50AF` (`68` bytes, SHA-1 `c511f3ebbcdf50ec2568e54a34d8c715c1d946fc`) `EExplPsiMsgExplPsiFlashBeta`
- `EF:50AF..EF:50E1` (`50` bytes, SHA-1 `ee66bf811739ff09b7d229eb101fed6a112c3d43`) `EExplPsiMsgExplPsiFlashGamma`
- `EF:50E1..EF:5131` (`80` bytes, SHA-1 `4e31853c9bc5f24c38dbfdbe0c60fae797fd918c`) `EExplPsiMsgExplPsiFlashOmega`
- `EF:5131..EF:5152` (`33` bytes, SHA-1 `23d72142d013945ee9994a2768d136ce245661e6`) `EExplPsiMsgExplPsiStarstomAlfa`
- `EF:5152..EF:5173` (`33` bytes, SHA-1 `68341b6cf833504b28f26e30604c909b9749a411`) `EExplPsiMsgExplPsiStarstormOmega`
- `EF:5173..EF:5189` (`22` bytes, SHA-1 `e8743125db5eca94d2e3029409fcbd131cda2e32`) `EExplPsiMsgExplPsiLifeupAlfa`
- `EF:5189..EF:519F` (`22` bytes, SHA-1 `b6a47eb58c5e6060a28c84895fbc36bb57c39da7`) `EExplPsiMsgExplPsiLifeupBeta`
- `EF:519F..EF:51BB` (`28` bytes, SHA-1 `d548417645da9f9d88f5d1e8ac07cc854ca7c5d4`) `EExplPsiMsgExplPsiLifeupGamma`
- `EF:51BB..EF:51CF` (`20` bytes, SHA-1 `bca86248000b10ef0e1aa027f01f6512e7df403f`) `EExplPsiMsgExplPsiLifeupOmega`
- `EF:51CF..EF:51F0` (`33` bytes, SHA-1 `794b1189a6b6053ed91fb81a7db847c9624d90bf`) `EExplPsiMsgExplPsiHealingAlfa`
- `EF:51F0..EF:5239` (`73` bytes, SHA-1 `e7edc47883f33ec729257c582a4aa705922d9f9f`) `EExplPsiMsgExplPsiHealingBeta`
- `EF:5239..EF:52A5` (`108` bytes, SHA-1 `a6c1cb70d1bc5bf3d3b4fa6e8a4c859051618928`) `EExplPsiMsgExplPsiHealingGamma`
- `EF:52A5..EF:5301` (`92` bytes, SHA-1 `974bb03fab94d4f89202e725c89421eb00e47e56`) `EExplPsiMsgExplPsiHealingOmega`
- `EF:5301..EF:5361` (`96` bytes, SHA-1 `428bd4268b1ff79667baff37d37f1db8e9e35c04`) `EExplPsiMsgExplPsiShieldAlfa`
- `EF:5361..EF:53C0` (`95` bytes, SHA-1 `0d7a35becb531ebba0dd358ac50f76e82e367646`) `EExplPsiMsgExplPsiShieldSigma`
- `EF:53C0..EF:5428` (`104` bytes, SHA-1 `32eb6a514f042beacd54df4e47c29ddb6155cb59`) `EExplPsiMsgExplPsiShieldBeta`
- `EF:5428..EF:548F` (`103` bytes, SHA-1 `6205a1c33ed5a362491ea1973ef9685954aaeb81`) `EExplPsiMsgExplPsiShieldOmega`
- `EF:548F..EF:54E6` (`87` bytes, SHA-1 `5970e8a6411aca74c19e39d4b44bb5072025c63f`) `EExplPsiMsgExplPsiPShieldAlfa`
- `EF:54E6..EF:553C` (`86` bytes, SHA-1 `0ac0f3490e0bc6f5fe449911aa8a7c2c3ee3ec33`) `EExplPsiMsgExplPsiPShieldSigma`
- `EF:553C..EF:55A0` (`100` bytes, SHA-1 `ba73f490c30f7367771bd56b2112bb949ca35e0b`) `EExplPsiMsgExplPsiPShieldBeta`
- `EF:55A0..EF:5603` (`99` bytes, SHA-1 `6df9ab6f483f3f3dffa11f8c77738b871573f739`) `EExplPsiMsgExplPsiPShieldOmega`
- `EF:5603..EF:562E` (`43` bytes, SHA-1 `d9ce08f63e395aff6189be56902da24cc64164d3`) `EExplPsiMsgExplPsiOffenseUpAlfa`
- `EF:562E..EF:5658` (`42` bytes, SHA-1 `d3216f9065649673acd933df58c924d0da5d898e`) `EExplPsiMsgExplPsiOffenseUpOmega`
- `EF:5658..EF:5687` (`47` bytes, SHA-1 `2cfc44ea15c93321cbba28dcf8dfda1918a18dbc`) `EExplPsiMsgExplPsiDefenseDownAlfa`
- `EF:5687..EF:56B9` (`50` bytes, SHA-1 `bbda87750913e850293fe13241492bbf8f4ec6cb`) `EExplPsiMsgExplPsiDefenseDownOmega`
- `EF:56B9..EF:56D0` (`23` bytes, SHA-1 `3ac89ee08743f75cd0045e781526ff85728f23b1`) `EExplPsiMsgExplPsiSaiminAlfa`
- `EF:56D0..EF:56EB` (`27` bytes, SHA-1 `c7b0f8a5fa604801426f0951fc980b67c8eed206`) `EExplPsiMsgExplPsiSaiminOmega`
- `EF:56EB..EF:5712` (`39` bytes, SHA-1 `0a6d6bd6edb65dad931b549854b8677e44d5cda7`) `EExplPsiMsgExplPsiPMagnetAlfa`
- `EF:5712..EF:5739` (`39` bytes, SHA-1 `023f6278c3460f0154959e83df94b124dec9cae3`) `EExplPsiMsgExplPsiPMagnetOmega`
- `EF:5739..EF:574E` (`21` bytes, SHA-1 `5ae3fed5f18ef201010f257d4dffcdb8fb817cab`) `EExplPsiMsgExplPsiParalysisAlfa`
- `EF:574E..EF:5766` (`24` bytes, SHA-1 `f7e15b4a12ed4e4881d1a163e3506ba120160e66`) `EExplPsiMsgExplPsiParalysisOmega`
- `EF:5766..EF:5777` (`17` bytes, SHA-1 `1768e57987a6003881709f19d5fd133332cb0fe4`) `EExplPsiMsgExplPsiBrainShockAlfa`
- `EF:5777..EF:578B` (`20` bytes, SHA-1 `f164a5cdd85dec4598bc2302df21178641c3b1b6`) `EExplPsiMsgExplPsiBrainShockOmega`
- `EF:578B..EF:57AE` (`35` bytes, SHA-1 `f26105ad8e2676e8168b6f2e471283d62e509d0f`) `EExplPsiMsgExplPsiTeleportAlfa`
- `EF:57AE..EF:57EB` (`61` bytes, SHA-1 `50084c9c20016b063075417279c20989059920f8`) `EExplPsiMsgExplPsiTeleportBeta`
- `EF:57EB..EF:5864` (`121` bytes, SHA-1 `db47c6279541f1f16b227f0c5676e6138617d7c5`) `E16DkfdMsgDkfdFireBoss`
- `EF:5864..EF:58C7` (`99` bytes, SHA-1 `e569e91e0b350487f3f7fae5e60841e9bc233f84`) `E16DkfdMsgDkfdDosei`
- `EF:58C7..EF:5917` (`80` bytes, SHA-1 `f7d629446948af3aa2a9012624644fc9008a2ea4`) `E16DkfdMsgDkfdSkywalker`
- `EF:5917..EF:5A3E` (`295` bytes, SHA-1 `12829213f428ae1469048cfad932e99f91c98566`) `E16DkfdMsgDkfdOldman`
- `EF:5A3E..EF:5A81` (`67` bytes, SHA-1 `cbbe74672c5d7f936f1424ebb13f217de2da1e46`) `E16DkfdMsgDkfdGumiA`
- `EF:5A81..EF:5AB5` (`52` bytes, SHA-1 `f1fb268fefbab5ef344dfb839d7336af2bdebedd`) `E16DkfdBranchDkfdGumiAEnd`
- `EF:5AB5..EF:5AED` (`56` bytes, SHA-1 `90470d7bebaa062c27a121bc7b3e7ae3c22e830e`) `E16DkfdMsgDkfdGumiAReceive`
- `EF:5AED..EF:5B97` (`170` bytes, SHA-1 `0c6afb40b3510d754905984778fd2de59bb56cfd`) `E16DkfdMsgDkfdGumiBoss`
- `EF:5B97..EF:5BC8` (`49` bytes, SHA-1 `0d50e9a485c393fb20e29b6a47f24ad5e2933b65`) `E16DkfdBranchDkfdGumiBossAfter`
- `EF:5BC8..EF:5BE6` (`30` bytes, SHA-1 `4bce2b9d4714b5dc5211beaae437870f96235320`) `E16DkfdBranchDkfdGumiBossEnd`
- `EF:5BE6..EF:5C46` (`96` bytes, SHA-1 `13aea68e448ddd415bb85955f511f35284392be3`) `E16DkfdMsgDkfdGumiC`
- `EF:5C46..EF:5C98` (`82` bytes, SHA-1 `774527d2e9e640e0d11655101375d0b211318010`) `E16DkfdBranchDkfdGumiCEnd`
- `EF:5C98..EF:5CE4` (`76` bytes, SHA-1 `d3b36270aafcaa29e0d52a24500ae032faa44950`) `E16DkfdMsgDkfdGumiD`
- `EF:5CE4..EF:5D16` (`50` bytes, SHA-1 `d40491156fa7bd61e2fc70f3756c41a4b43b77f7`) `E16DkfdBranchDkfdGumiDEnd`
- `EF:5D16..EF:5DF8` (`226` bytes, SHA-1 `2570571d979432a292ab595cac59201c9c692b4a`) `E16DkfdMsgDkfdGumiE`
- `EF:5DF8..EF:5E94` (`156` bytes, SHA-1 `affb31e3bc4b6e7ece79840cc70d8c9671518564`) `E16DkfdBranchDkfdGumiEB`
- `EF:5E94..EF:5F31` (`157` bytes, SHA-1 `ff5b5876c4003c1df1aea7e6f55a58fafb69790f`) `E16DkfdMsgDkfdGumiF`
- `EF:5F31..EF:5F7D` (`76` bytes, SHA-1 `2762742d55c235f57f9de8964655338a9225437c`) `E16DkfdBranchDkfdGumiFEnd`
- `EF:5F7D..EF:5FDF` (`98` bytes, SHA-1 `b298ee2195696f3603d06db21dc55f4ba78ea5b6`) `E16DkfdMsgDkfdGumiG`
- `EF:5FDF..EF:6038` (`89` bytes, SHA-1 `abc2c1057271185956f66fcb2f810912b1767a10`) `E16DkfdMsgDkfdGumiH`
- `EF:6038..EF:6049` (`17` bytes, SHA-1 `51020c10f25bdfd87e70e979b346bb24bf79f5e6`) `E16DkfdBranchDkfdGumiHEnd`
- `EF:6049..EF:604F` (`6` bytes, SHA-1 `4afb7afefc564bcddc4abfd5d4417ae901f3dea6`) `E16DkfdMsgDkfdGumiI`
- `EF:604F..EF:6084` (`53` bytes, SHA-1 `5051af522ca393bae97368c935cb6a60063c5b80`) `E16DkfdMsgDkfdGumiK`
- `EF:6084..EF:60C5` (`65` bytes, SHA-1 `f3fd2c9be250efe0f9ddc7e97875eac4b9507cf2`) `E16DkfdMsgDkfdGumiL`
- `EF:60C5..EF:60F2` (`45` bytes, SHA-1 `5f2079d73770196ba6acf436dd1e0adcde2e827e`) `E16DkfdBranchDkfdGumiLEnd`
- `EF:60F2..EF:610C` (`26` bytes, SHA-1 `39fc3cbde7196648906058a376b92c049d5179eb`) `E16DkfdMsgDkfdBirdPhone`
- `EF:610C..EF:610D` (`1` bytes, SHA-1 `c4ea21bb365bbeeaf5f2c654883e56d11e43c44e`) `E16DkfdMsgDkfdGumiDoorReceive`
- `EF:610D..EF:6132` (`37` bytes, SHA-1 `0463085e2f577d3d1cc30fdbe25f0a0035f3df04`) `E16DkfdMsgReadDkfdGumi1`
- `EF:6132..EF:6157` (`37` bytes, SHA-1 `19bed1a61fc27da303674feff457a00ad9c9dec0`) `E16DkfdMsgReadDkfdGumi2`
- `EF:6157..EF:617B` (`36` bytes, SHA-1 `5a41db8792f2536667dc716db5c9609bf246e99b`) `E16DkfdMsgReadDkfdGumi3`
- `EF:617B..EF:61CB` (`80` bytes, SHA-1 `da74bf4837d835f35c8392823ddca7d808527bf0`) `E07GpftMsgGpftMinigeppuA`
- `EF:61CB..EF:61F3` (`40` bytes, SHA-1 `3657f94c718579ddd4093d427802d4891423d0cb`) `E07GpftBranchGpftMinigeppuANo`
- `EF:61F3..EF:6247` (`84` bytes, SHA-1 `57b3b9da330662d997190724d162e19c7aeee51d`) `E07GpftBranchGpftMinigeppuAYesno`
- `EF:6247..EF:6276` (`47` bytes, SHA-1 `47c62007c7f03acae75713d555acd691b684c170`) `E07GpftBranchGpftMinigeppuAYes`
- `EF:6276..EF:62B1` (`59` bytes, SHA-1 `6f8d426d582b9f665fb00e0480e8a02c825115a2`) `E07GpftMsgGpftMinigeppuB`
- `EF:62B1..EF:62F5` (`68` bytes, SHA-1 `3e5e944dbef71d7e463f6bb113e8af46e1dde202`) `E07GpftMsgGpftMinigeppuC`
- `EF:62F5..EF:63B5` (`192` bytes, SHA-1 `b90a67f25cd296ce4f7f236374f0754b51ff49d3`) `E07GpftMsgGpftMinigeppuD`
- `EF:63B5..EF:6400` (`75` bytes, SHA-1 `fa63b4b1afe17f70b99ac2bfbb3862cb667e4dda`) `E07GpftMsgGpftMinigeppuE`
- `EF:6400..EF:6419` (`25` bytes, SHA-1 `7a2bd68efacbee6baeac1f3e75ac76a2166eebc3`) `E07GpftMsgGpftDoseiA`
- `EF:6419..EF:6446` (`45` bytes, SHA-1 `727fc54a31e79c6d1b9826d21fdaf77d0282fe9b`) `E07GpftMsgGpftDoseiB`
- `EF:6446..EF:6569` (`291` bytes, SHA-1 `51f35d49c6ef43dabe4752487df1643c655a839c`) `E07GpftMsgGpftGeppu`
- `EF:6569..EF:66CA` (`353` bytes, SHA-1 `e71073b1379886ecae801e7b6530d43290859c77`) `E07GpftBranchGpftGeppuMain`
- `EF:66CA..EF:679A` (`208` bytes, SHA-1 `afe47cd14d80b3371d5c69c4aaf836ac2935ae44`) `E07GpftBranchGpftGeppuDead`
- `EF:679A..EF:6814` (`122` bytes, SHA-1 `2b28e39da9a6352398297aea70751cbbcd2177f3`) `E07GpftMsgGpftMlkyBoss`
- `EF:6814..EF:681A` (`6` bytes, SHA-1 `c92bb3cf7b16f3d28984700c8193935b4ff93423`) `E07GpftMsgGpftHakamori`
- `EF:681A..EF:6874` (`90` bytes, SHA-1 `896ec0d5d9f9e3e67790a13144f0a5f8cbf3dc53`) `E07GpftMsgThrkBossGrave`
- `EF:6874..EF:68D7` (`99` bytes, SHA-1 `edc673f28ab405744a3716e6bfdb60f2bac239d7`) `E07GpftBranchThrkBossGraveHave`
- `EF:68D7..EF:6954` (`125` bytes, SHA-1 `cb6bf282d65903b98517d5a2cf31b2fdb1f23c37`) `E07GpftMsgThrkBossGraveDie`
- `EF:6954..EF:69A1` (`77` bytes, SHA-1 `9ec02392bd5354a6e592f0186a961e5a1ed9e2ed`) `E07GpftBranchThrkBossGraveDieHave`
- `EF:69A1..EF:69BA` (`25` bytes, SHA-1 `33973d8aedbab180bc8c1d16f85be38becd9dfe7`) `EBattle5MsgBtlHpMaxRecovered`
- `EF:69BA..EF:69D2` (`24` bytes, SHA-1 `dee68da43f55467846a4643c14bd193aefad587d`) `EBattle5MsgBtlHpRecoveredAmount`
- `EF:69D2..EF:69EA` (`24` bytes, SHA-1 `178a8e52dbf9278e6a66f1bfc8b5e4d7dbc5065c`) `EBattle5MsgBtlPpRecoveredAmount`
- `EF:69EA..EF:69FF` (`21` bytes, SHA-1 `cbca03e002672de1af2ce08e0476abeb1818a953`) `EBattle5MsgBtlCheckOffenseAmount`
- `EF:69FF..EF:6A0D` (`14` bytes, SHA-1 `fb730cb9ad258a3376ee011615e57a6bb17319b9`) `EBattle5MsgBtlCheckDefenseAmount`
- `EF:6A0D..EF:6A24` (`23` bytes, SHA-1 `eaf532c68b3a87d9980a1732fc70a81627fc6cfd`) `EBattle5MsgBtlCheckAntiFire`
- `EF:6A24..EF:6A3C` (`24` bytes, SHA-1 `7bfa471b99fc69bf48792fe2102e215cc0abbcb2`) `EBattle5MsgBtlCheckAntiFreeze`
- `EF:6A3C..EF:6A54` (`24` bytes, SHA-1 `91e70fea8be98342875e635db61652bc75aac0ed`) `EBattle5MsgBtlCheckAntiFlash`
- `EF:6A54..EF:6A6C` (`24` bytes, SHA-1 `384312931078402facd3a775d197d37e6c2221cf`) `EBattle5MsgBtlCheckAntiParalysis`
- `EF:6A6C..EF:6A7F` (`19` bytes, SHA-1 `d35c8d638a6133af56367bfee05a00320394e969`) `EBattle5MsgBtlCheckBrainLevel0`
- `EF:6A7F..EF:6A99` (`26` bytes, SHA-1 `10763eb9cfd6b86fa000114461c0c0859e3a50ea`) `EBattle5MsgBtlCheckBrainLevel3`
- `EF:6A99..EF:6AB3` (`26` bytes, SHA-1 `bfaaec9540a8b30f2c7e48a7f999f357c1f45096`) `EBattle5MsgBtlMetamorphoseOk`
- `EF:6AB3..EF:6AC7` (`20` bytes, SHA-1 `d19194f31d229b82f858043b7526f136277ae4ab`) `EBattle5MsgBtlMetamorphoseFailed`
- `EF:6AC7..EF:6AE0` (`25` bytes, SHA-1 `1d28c385166c187b0eb36d3ad118adb8a44c2326`) `EBattle5MsgBtlDiamondized`
- `EF:6AE0..EF:6AFB` (`27` bytes, SHA-1 `77937f95269e6421b86b3d4693c44fd3843f5b7b`) `EBattle5MsgBtlParalysisInflicted`
- `EF:6AFB..EF:6B18` (`29` bytes, SHA-1 `3b3d3f415dce645e7699370021264b3c224e9266`) `EBattle5MsgBtlFeelingSickInflicted`
- `EF:6B18..EF:6B2F` (`23` bytes, SHA-1 `7812336a84bc28904a7bf104c7ec344f21c5819e`) `EBattle5MsgBtlPoisonInflicted`
- `EF:6B2F..EF:6B43` (`20` bytes, SHA-1 `07f8d05a02270dac2f4a6eaea27be633c7798cb8`) `EBattle5MsgBtlColdInflicted`
- `EF:6B43..EF:6B81` (`62` bytes, SHA-1 `df0b94b393a88f6993dcd766cc4571838b2a3e3e`) `EBattle5ObjectPronounSubtext`
- `EF:6B81..EF:6B98` (`23` bytes, SHA-1 `4fcd80b96a9421b4bc45dc0779d89f3291b6067c`) `EBattle5MsgBtlMushroomizedInflicted`
- `EF:6B98..EF:6BBB` (`35` bytes, SHA-1 `7ee966d54e30ac40a94c86441c2bec3492b67809`) `EBattle5MsgBtlPossessedInflicted`
- `EF:6BBB..EF:6BD3` (`24` bytes, SHA-1 `23f88af6a7604cc91dc3d3fa158a34a220fe16b7`) `EBattle5MsgBtlCryingInflicted`
- `EF:6BD3..EF:6BEF` (`28` bytes, SHA-1 `55c4d2930e8e056ca4cab10bbec98f0ab236360f`) `EBattle5MsgBtlImmobilizedInflicted`
- `EF:6BEF..EF:6C0B` (`28` bytes, SHA-1 `766017a093540d57429f454b420db0739f65a303`) `EBattle5MsgBtlSolidificationInflicted`
- `EF:6C0B..EF:6C3A` (`47` bytes, SHA-1 `30a911438fa0c874b4da136accd54ef893390ac5`) `EBattle5MsgBtlPsiSealInflicted`
- `EF:6C3A..EF:6C55` (`27` bytes, SHA-1 `af8d51b31d83087c92c0d9710c2f57976aa45e70`) `EBattle5MsgBtlStrangeInflicted`
- `EF:6C55..EF:6C6B` (`22` bytes, SHA-1 `4d5790f342b2e74a3d9baf1f2c69c44a5cf6e2a9`) `EBattle5MsgBtlAsleepInflicted`
- `EF:6C6B..EF:6C84` (`25` bytes, SHA-1 `5239e087feae40fca6e73094ad08a3a9a2700cd9`) `EBattle5MsgBtlIncapacitated`
- `EF:6C84..EF:6CC7` (`67` bytes, SHA-1 `9b17266ec30e32ad1633dbb3b8c70c20733d827f`) `EBattle5MsgSysNpcDeadFlyingMan`
- `EF:6CC7..EF:6CD0` (`9` bytes, SHA-1 `37c8b56b3e68d1f01245bd27c582578e20d4bb89`) `EBattle5FlyingManDeadBranchB`
- `EF:6CD0..EF:6CD9` (`9` bytes, SHA-1 `bac11a5d8dcd2becc5f3140ec40663275ff9fa96`) `EBattle5FlyingManDeadBranchC`
- `EF:6CD9..EF:6CE2` (`9` bytes, SHA-1 `e1ffb352ec6abd1b6e69f11fe10897371f250eca`) `EBattle5FlyingManDeadBranchD`
- `EF:6CE2..EF:6CEB` (`9` bytes, SHA-1 `0411f98368826c3c274b91e869979bd29b8c5894`) `EBattle5FlyingManDeadBranchE`
- `EF:6CEB..EF:6CFC` (`17` bytes, SHA-1 `8fabdceb9b80f856e60384c13517ca1e8f3538c7`) `EBattle5FlyingManRemovePartyMemberHelper`
- `EF:6CFC..EF:6D0A` (`14` bytes, SHA-1 `b28f114fc77d50a7abbd9735595c14530428c793`) `EBattle5FlyingManRemoveBranch2`
- `EF:6D0A..EF:6D18` (`14` bytes, SHA-1 `6803c77f9e4feb6a50f7126724d278419fa264e2`) `EBattle5FlyingManRemoveBranch3`
- `EF:6D18..EF:6D26` (`14` bytes, SHA-1 `32c251725020ca643d2e22839b21b6f579bd6f6c`) `EBattle5FlyingManRemoveBranch4`
- `EF:6D26..EF:6D2A` (`4` bytes, SHA-1 `f287881dd67b925df1531e0762bcc1b47a69fff1`) `EBattle5FlyingManRemoveBranch5`
- `EF:6D2A..EF:6D4C` (`34` bytes, SHA-1 `66e3b4d004b2cbe67b60093cc87a2587dad3e20d`) `EBattle5MsgSysNpcDeadTeddyBear`
- `EF:6D4C..EF:6D71` (`37` bytes, SHA-1 `1caf43c69b75eee750489f0cf121dd2e218876da`) `EBattle5MsgSysNpcDeadSuperPlushBear`
- `EF:6D71..EF:6D83` (`18` bytes, SHA-1 `fecde504825e2393a05568e18875e785481531f5`) `EBattle5MsgBtlEnemyDefeated`
- `EF:6D83..EF:6D96` (`19` bytes, SHA-1 `527d33a59d9804279c66b0a7cd83b4236874de51`) `EBattle5MsgBtlEnemyStoppedMoving`
- `EF:6D96..EF:6DA7` (`17` bytes, SHA-1 `ea833438b4ed642747c0190a152671889d2e2381`) `EBattle5MsgBtlEnemyBecameTame`
- `EF:6DA7..EF:6DB8` (`17` bytes, SHA-1 `c078f6115a03dcfc7e65035cb6ce43093994f26d`) `EBattle5MsgBtlEnemyDisappeared`
- `EF:6DB8..EF:6DD8` (`32` bytes, SHA-1 `135dd0b094f3e417766e94fc01ab38a4b98310b9`) `EBattle5MsgBtlEnemyMeltedAway`
- `EF:6DD8..EF:6DF0` (`24` bytes, SHA-1 `dd7e896c37e93caed82eeab43f111efc68324687`) `EBattle5MsgBtlEnemyBrokeIntoPieces`
- `EF:6DF0..EF:6E03` (`19` bytes, SHA-1 `0e8ac92ab6aaa62cfad2aa56ed8eed1af8fd76d1`) `EBattle5MsgBtlEnemyDestroyed`
- `EF:6E03..EF:6E19` (`22` bytes, SHA-1 `280ed6e4bf9525875d970089ca8a196f521a4446`) `EBattle5MsgBtlEnemyScrapped`
- `EF:6E19..EF:6E31` (`24` bytes, SHA-1 `954a4b24573c031af08645cd4eee93c55180f3d5`) `EBattle5MsgBtlEnemyReturnedToNormal`
- `EF:6E31..EF:6E4A` (`25` bytes, SHA-1 `b28bef70d6b861992262429f24ef463357850bfc`) `EBattle5MsgBtlEnemyReturnedToDust`
- `EF:6E4A..EF:6E67` (`29` bytes, SHA-1 `c6d274d913564c37c09cb02eb8a519422febc47c`) `EBattle5MsgBtlDiamondizedRecovered`
- `EF:6E67..EF:6E81` (`26` bytes, SHA-1 `d5c28bd7008e59e91d35fd8a238dfdab161bdce3`) `EBattle5MsgBtlParalysisRecovered`
- `EF:6E81..EF:6E97` (`22` bytes, SHA-1 `e4343b886d04ec9a5eb0807d4e98ad3d4a4f31db`) `EBattle5MsgBtlFeelingSickRecovered`
- `EF:6E97..EF:6EBC` (`37` bytes, SHA-1 `8c2836a58ae92c87ef94de7c948cb53687f7b637`) `EBattle5MsgBtlPoisonRemoved`
- `EF:6EBC..EF:6ED1` (`21` bytes, SHA-1 `42a2c1124dfdb1a894a49009bc0997dab13a340d`) `EBattle5MsgBtlColdRecovered`
- `EF:6ED1..EF:6EED` (`28` bytes, SHA-1 `34c08afa2f8f82674324e5b33f79aabb288b0794`) `EBattle5MsgBtlCryingRecovered`
- `EF:6EED..EF:6F0B` (`30` bytes, SHA-1 `7759e6d88ccd2107724e2effd474691264519a54`) `EBattle5MsgBtlImmobilizedRecovered`
- `EF:6F0B..EF:6F1E` (`19` bytes, SHA-1 `b9d1f92448dc963887cae2234364d16da454de28`) `EBattle5MsgBtlFrozenCanMove`
- `EF:6F1E..EF:6F38` (`26` bytes, SHA-1 `2115437f9f27384c25780b921af73ab04ad771ef`) `EBattle5MsgBtlStrangeRecovered`
- `EF:6F38..EF:6F54` (`28` bytes, SHA-1 `04314f2ae74e84c31b2b19944056b5b006e9aac9`) `EBattle5MsgBtlSunstrokeCured`
- `EF:6F54..EF:6F64` (`16` bytes, SHA-1 `7a0edecaff603fff5fbea3ab9a2c116a2abf63ba`) `EBattle5MsgBtlAsleepRecovered`
- `EF:6F64..EF:6F7C` (`24` bytes, SHA-1 `e835c44f305cf081f18da12269b343050e2048a8`) `EBattle5MsgBtlPsiSealRecovered`
- `EF:6F7C..EF:6F8E` (`18` bytes, SHA-1 `6c4ae3818b87052c84ba3a39b27e14c33bb92d44`) `EBattle5MsgBtlRevived`
- `EF:6F8E..EF:6F9A` (`12` bytes, SHA-1 `21ed1025a46bdab04851bccf116953f8bbeb000a`) `EBattle5MsgBtlReviveFailed`
- `EF:6F9A..EF:6FBD` (`35` bytes, SHA-1 `32b9f94859cc1256432748a68c7afd7904e57bfb`) `EBattle5MsgBtlShieldInstalled`
- `EF:6FBD..EF:6FD3` (`22` bytes, SHA-1 `75d0bac14ab6514e2ea88b25e1500ef00dbe9695`) `EBattle5MsgBtlShieldStrengthened`
- `EF:6FD3..EF:6FF4` (`33` bytes, SHA-1 `436ff24c2b098518d72aea4b6e92c7ae016598e4`) `EBattle5MsgBtlPowerShieldInstalled`
- `EF:6FF4..EF:700C` (`24` bytes, SHA-1 `91688e4579bfd0a98d936abb9eeb605696421bdb`) `EBattle5MsgBtlPowerShieldStrengthened`
- `EF:700C..EF:7032` (`38` bytes, SHA-1 `8e09d7147d7b1d6f5812c470721b0cf2a891391a`) `EBattle5MsgBtlPsychicShieldInstalled`
- `EF:7032..EF:7050` (`30` bytes, SHA-1 `95e260b622016c2efeadc2209d43bf3512c25816`) `EBattle5MsgBtlPsychicShieldStrengthened`
- `EF:7050..EF:707A` (`42` bytes, SHA-1 `ef9940bdeff8772e33413e1128347df7677d3049`) `EBattle5MsgBtlPsychicPowerShieldInstalled`
- `EF:707A..EF:7099` (`31` bytes, SHA-1 `b696662c257fbd2ce9510ea7933052b89d4fbf38`) `EBattle5MsgBtlPsychicPowerShieldStrengthened`
- `EF:7099..EF:70B1` (`24` bytes, SHA-1 `454c896efa3a20c3a15ce78eaf78527172fd73b1`) `EBattle5MsgBtlShieldExpired`
- `EF:70B1..EF:70D2` (`33` bytes, SHA-1 `e49767fe7e0ce9f98ca65b69ae3603fdb1521eb3`) `EBattle5MsgBtlPowerShieldReflectsAttack`
- `EF:70D2..EF:70FA` (`40` bytes, SHA-1 `1b955d8041a0b0aaf2eea5aa7d690e99a1ba285b`) `EBattle5MsgBtlPsychicPowerShieldReflectsPsiName`
- `EF:70FA..EF:7123` (`41` bytes, SHA-1 `03c5e8c29fe5f19b590afe6a060faa5889e44487`) `EBattle5MsgBtlPsychicShieldNullifiesPsiName`
- `EF:7123..EF:7142` (`31` bytes, SHA-1 `a3f610416e889477be5df78079b1d761d75480f8`) `EBattle5MsgBtlNeutralizeResult`
- `EF:7142..EF:7160` (`30` bytes, SHA-1 `146cd7f37e71519b0d2004be040ff876becb3cef`) `EBattle5MsgBtlNeutralizeMetamorph`
- `EF:7160..EF:7186` (`38` bytes, SHA-1 `594e1e727b025bec9e212a9aaadb94b68870fb34`) `EBattle5MsgBtlFranklinBadgeReflectsThunder`
- `EF:7186..EF:7192` (`12` bytes, SHA-1 `2084a70d00b0f28717b31a940e08dc392efd030a`) `EBattle4MsgBtlDiamondizedCannotMove`
- `EF:7192..EF:71B4` (`34` bytes, SHA-1 `ee123464ea5ef423e62887b3e7b8c0a900faf0a2`) `EBattle4MsgBtlParalysisCannotMove`
- `EF:71B4..EF:71CC` (`24` bytes, SHA-1 `56d7f2996d8139565c7d2080a335d91d2d2991c8`) `EBattle4MsgBtlNauseaCannotMove`
- `EF:71CC..EF:71DF` (`19` bytes, SHA-1 `936f8a6a64fe4a23f442f9c3bcaeeec34560b8c9`) `EBattle4MsgBtlPoisonStatus`
- `EF:71DF..EF:71F6` (`23` bytes, SHA-1 `414a41a2205d2aa0ede68bf9b4e640fa50158380`) `EBattle4MsgBtlAsleepStatus`
- `EF:71F6..EF:720C` (`22` bytes, SHA-1 `0991dca0b9526a694996eaedc929fd64a5cce488`) `EBattle4MsgBtlImmobilizedStatus`
- `EF:720C..EF:721E` (`18` bytes, SHA-1 `f88e28c612efd7475a9884c83b7096db8155978d`) `EBattle4MsgBtlPsiSealStatus`
- `EF:721E..EF:7221` (`3` bytes, SHA-1 `9a9dd4fc9529f0d0f21e55e79186969738ff5347`) `EBattle4PsiSealPlayerSideSoundBranch`
- `EF:7221..EF:7249` (`40` bytes, SHA-1 `dcfb9f7c3024d3ae05efc7ed93620eab47123ab9`) `EBattle4PsiSealResultText`
- `EF:7249..EF:725A` (`17` bytes, SHA-1 `e1e8b5c5040f3d970649b4b145463eaf03a3f380`) `EBattle4MsgBtlGuardOn`
- `EF:725A..EF:727F` (`37` bytes, SHA-1 `d358286d973116af553ce1a0f035ad1d45ab27ce`) `EBattle4MsgBtlFlyHoneyMindLost`
- `EF:727F..EF:72A0` (`33` bytes, SHA-1 `6bb0689abc8567d99a0b15ab932c3a0bf765117c`) `EBattle4MsgBtlHomesickRandom`
- `EF:72A0..EF:72B9` (`25` bytes, SHA-1 `e82ec910c7592d8d35e0390774f11d0b1f322757`) `EBattle4MsgBtlHomesickThoughtMom`
- `EF:72B9..EF:72DB` (`34` bytes, SHA-1 `2d9e60b39dd3262f51e1440eaca477ff6fb3fc0a`) `EBattle4MsgBtlHomesickCravingFood`
- `EF:72DB..EF:72F6` (`27` bytes, SHA-1 `34003ffbe658ce975f6ccf063e23d3fed6328071`) `EBattle4MsgBtlHomesickLostMotivation`
- `EF:72F6..EF:72F7` (`1` bytes, SHA-1 `c4ea21bb365bbeeaf5f2c654883e56d11e43c44e`) `EBattle4MsgBtlRunawayFiveBreakIn`
- `EF:72F7..EF:733D` (`70` bytes, SHA-1 `d196be4d816335a0625788e2688c097ac7643009`) `EBattle4MsgBtlRunawayFiveBreakInFailed`
- `EF:733D..EF:7415` (`216` bytes, SHA-1 `cbac0b9bda5afd16cfeb868e2ab0cca1e264a1f4`) `EBattle4MsgBtlRunawayFiveBreakInSucceeded`
- `EF:7415..EF:743B` (`38` bytes, SHA-1 `81313c365a179948200316a3ecdbd5af3b80cef3`) `EBattle4MsgBtlPooBreakIn`
- `EF:743B..EF:745F` (`36` bytes, SHA-1 `0c94d0a4d445894725aaefaee75c40ff2e9d39c1`) `EBattle4MsgBtlPooStarstormReveal`
- `EF:745F..EF:749D` (`62` bytes, SHA-1 `727799622495458a59d956ae265b52e126ff9e17`) `EBattle4MsgBtlPokeyTalkRandom`
- `EF:749D..EF:74B0` (`19` bytes, SHA-1 `6ff4d647c88229bd1f60ddf0a4bafd728e9b1e5b`) `EBattle4MsgBtlPokeyPlayedDead`
- `EF:74B0..EF:74C9` (`25` bytes, SHA-1 `62861e3d1b1b19fb77a2b8518e14ea9199f0343e`) `EBattle4MsgBtlPokeyPretendedCry`
- `EF:74C9..EF:74E6` (`29` bytes, SHA-1 `f993d969d77773f68e357daa1c19e75e0a99d69a`) `EBattle4MsgBtlPokeyApologized`
- `EF:74E6..EF:74FA` (`20` bytes, SHA-1 `e750f9faef3fc1bcf8ef9378a88b5f4778b47499`) `EBattle4MsgBtlPokeyThoughtToSelf`
- `EF:74FA..EF:7514` (`26` bytes, SHA-1 `4f14bd39c5448b7f9124ef6ac3f0700332d004f9`) `EBattle4MsgBtlPokeyActedInnocent`
- `EF:7514..EF:7530` (`28` bytes, SHA-1 `b7989bfe3e2065c2c0ef97b711ccf26d4706496f`) `EBattle4MsgBtlPokeySmiledSincerely`
- `EF:7530..EF:7548` (`24` bytes, SHA-1 `5929c9017c057517713d38a6ee897b3d29ff2915`) `EBattle4MsgBtlPokeyComplained`
- `EF:7548..EF:7569` (`33` bytes, SHA-1 `da8410480a860a2f8541bc06c10e87107d9bc134`) `EBattle4MsgBtlPokeyEdgedCloser`
- `EF:7569..EF:7579` (`16` bytes, SHA-1 `a5c0a43b5021b7c9d03729377bf61d1f51c06acb`) `EBattle4MsgBtlMyDogHowling`
- `EF:7579..EF:7591` (`24` bytes, SHA-1 `fe848981a1676bc95dc4b02c8262e536d9e6f80c`) `EBattle4MsgBtlPickeyTalk`
- `EF:7591..EF:7593` (`2` bytes, SHA-1 `0ca623e2855f2c75c842ad302fe820e41b4d197d`) `EBattle4MsgBtlTonyTalk`
- `EF:7593..EF:75AB` (`24` bytes, SHA-1 `d751fe2f17af56e2dc089f3204a9d23240a8ddf9`) `EBattle4MsgBtlBalmonTalk`
- `EF:75AB..EF:75C2` (`23` bytes, SHA-1 `3a053f08b2ec79049925f079d8b40170757597b4`) `EBattle4MsgBtlDamageAmount`
- `EF:75C2..EF:75D9` (`23` bytes, SHA-1 `edfab9740fc98f70467246c48b24749140cb7442`) `EBattle4MsgBtlMortalDamageAmount`
- `EF:75D9..EF:75F0` (`23` bytes, SHA-1 `3a053f08b2ec79049925f079d8b40170757597b4`) `EBattle4MsgBtlSmashDamageAmount`
- `EF:75F0..EF:7607` (`23` bytes, SHA-1 `edfab9740fc98f70467246c48b24749140cb7442`) `EBattle4MsgBtlMortalSmashDamageAmount`
- `EF:7607..EF:7624` (`29` bytes, SHA-1 `806a7ef398d67cb517fa40d0c53b297828f651d4`) `EBattle4MsgBtlDamageToDeathAmount`
- `EF:7624..EF:7630` (`12` bytes, SHA-1 `4ea6c0dfa6c448606b728bd676b9541a300edcc8`) `EBattle4MsgBtlSmashPlayer`
- `EF:7630..EF:763C` (`12` bytes, SHA-1 `d6e222f2f3092a8dbb1df396ebb3a8e82b71ff61`) `EBattle4MsgBtlSmashMonster`
- `EF:763C..EF:7655` (`25` bytes, SHA-1 `2f17677a234132a95abbcfc211c405e544cf70fc`) `EBattle4MsgBtlShootDodged`
- `EF:7655..EF:766E` (`25` bytes, SHA-1 `2f17677a234132a95abbcfc211c405e544cf70fc`) `EBattle4MsgBtlBashDodged`
- `EF:766E..EF:7682` (`20` bytes, SHA-1 `6097e90c945e2f040dfd0fac365f206f0fe77d8d`) `EBattle4MsgBtlStatusNoEffect`
- `EF:7682..EF:7696` (`20` bytes, SHA-1 `6097e90c945e2f040dfd0fac365f206f0fe77d8d`) `EBattle4AdjacentNoEffectText`
- `EF:7696..EF:76B3` (`29` bytes, SHA-1 `e4113ef4fa47015dc03660c723c49ae26e239e23`) `EBattle4MsgBtlNoVisibleEffect`
- `EF:76B3..EF:76C7` (`20` bytes, SHA-1 `6097e90c945e2f040dfd0fac365f206f0fe77d8d`) `EBattle4MsgBtlNoEffectVariantC`
- `EF:76C7..EF:76D8` (`17` bytes, SHA-1 `1110635d12eaf03417de5aa31df997cab60c78a3`) `EBattle4MsgBtlMissPhysical`
- `EF:76D8..EF:76FD` (`37` bytes, SHA-1 `033b47d37cc1f9de69b043c95cb3c5397bf50dd1`) `EBattle4MsgBtlMissShoot`
- `EF:76FD..EF:7710` (`19` bytes, SHA-1 `d96d3e5e48371da5b741502fdc4f7a176cbd001a`) `EBattle4MsgBtlTargetNotExist`
- `EF:7710..EF:7729` (`25` bytes, SHA-1 `3cbd6bb358b9f9607b00e49444509e19f0afa236`) `EBattle4MsgBtlHpSuckSelfDrain`
- `EF:7729..EF:773F` (`22` bytes, SHA-1 `f8dba4e9c54f6f73c48303350ff61ab1c781e140`) `EBattle4MsgBtlHpSuckAmount`
- `EF:773F..EF:7755` (`22` bytes, SHA-1 `6232b10ccb1d72f3eadde7a851e2688209a5c83a`) `EBattle4MsgBtlPpDrainAmount`
- `EF:7755..EF:7768` (`19` bytes, SHA-1 `97622bb4a3f2a58999cb73e624a6e6dd4a2bfe67`) `EBattle4MsgBtlPpDrainTarget`
- `EF:7768..EF:7787` (`31` bytes, SHA-1 `210944d8fe14331b7fab9ff513e052ec49376722`) `EBattle4MsgBtlStrangeDamage`
- `EF:7787..EF:77B1` (`42` bytes, SHA-1 `9b8f7fc7618de1531e7d1434952a808da5777b06`) `EBattle4MsgBtlPoisonDamage`
- `EF:77B1..EF:77DB` (`42` bytes, SHA-1 `e1107c8d05e467a473077d1c58c466c9a116e071`) `EBattle4MsgBtlSunstrokeDamage`
- `EF:77DB..EF:77FD` (`34` bytes, SHA-1 `128d1011da049119cb9abfd21c65fa7cfec2bab4`) `EBattle4MsgBtlColdDamage`
- `EF:77FD..EF:7810` (`19` bytes, SHA-1 `bf11a9604ab664ba99d8259cf9a94fd91e386065`) `EBattle8MsgBtlCallForHelpEnemyJoined`
- `EF:7810..EF:7824` (`20` bytes, SHA-1 `bc9c731025178de4aa8c5dd234c7df273376bf43`) `EBattle8MsgBtlCallForHelpSeedSprouted`
- `EF:7824..EF:7830` (`12` bytes, SHA-1 `37eb2ca0de50d3f88b762f3cefb361d0d5f08cae`) `EBattle8MsgBtlCallForHelpNoOneCame`
- `EF:7830..EF:7843` (`19` bytes, SHA-1 `0a637d9c7d18747424692410bf1e652aaff3533e`) `EBattle8MsgBtlCallForHelpSeedNoSprout`
- `EF:7843..EF:7858` (`21` bytes, SHA-1 `52dfe17ffa36d7b426f1aa12d86779148c6094ad`) `EBattle8MsgBtlTimeStopReturn`
- `EF:7858..EF:7866` (`14` bytes, SHA-1 `4d5a11d42293acfb56e1cf0d8374921883580b28`) `EBattle8MsgBtlAppearAttacked`
- `EF:7866..EF:7879` (`19` bytes, SHA-1 `a2a870ec7ee0273ca58ff0fbabc06ce35724819d`) `EBattle8MsgBtlAppearBlockedWay`
- `EF:7879..EF:788B` (`18` bytes, SHA-1 `601418a2ba5572f9579db119b2a2ae80bc99014b`) `EBattle8MsgBtlAppearCameAfterYou`
- `EF:788B..EF:789C` (`17` bytes, SHA-1 `5e7a280e02b5f6f0df4c30b2ed5064150d20ba32`) `EBattle8MsgBtlAppearTrappedYou`
- `EF:789C..EF:78AB` (`15` bytes, SHA-1 `f6eeb8fa2be831dc6287125509ba6b3cdfd6a6f1`) `EBattle8MsgBtlFinalEncounter4`
- `EF:78AB..EF:78B8` (`13` bytes, SHA-1 `278a3e4ed17a269f7ffc5ccee8e587fe2b5ba6fe`) `EBattle8MsgBtlFinalEncounter5`
- `EF:78B8..EF:78C7` (`15` bytes, SHA-1 `f05800508c53134fc535d6cd050404dae1eef43f`) `EBattle8MsgBtlFinalEncounter6`
- `EF:78C7..EF:78D8` (`17` bytes, SHA-1 `2080ccac7302058d749a169170a56a1ebb9bdfb2`) `EBattle8MsgBtlFinalEncounter7`
- `EF:78D8..EF:78F7` (`31` bytes, SHA-1 `26ee97fbd73c9c60ab94c8163458502711d6a0b3`) `EBattle8MsgBtlSurpriseOpeningPlayer`
- `EF:78F7..EF:790B` (`20` bytes, SHA-1 `90c7110d1d12d06be949f877d90c179117defef6`) `EBattle8MsgBtlSurpriseOpeningMonster`
- `EF:790B..EF:792B` (`32` bytes, SHA-1 `411101a02bc0b8a6fe05ac3ac40abea3ba061f6f`) `EBattle8GroupActorOpeningHelper`
- `EF:792B..EF:792E` (`3` bytes, SHA-1 `4a27df79273058f0219426b59dd2b8b9f2b7d78c`) `EBattle8GroupActorOpeningSingular`
- `EF:792E..EF:793C` (`14` bytes, SHA-1 `ee4e526a2a39700402be4dad3ef1a53cfcde90ee`) `EBattle8GroupActorOpeningCohort`
- `EF:793C..EF:794B` (`15` bytes, SHA-1 `575504d3e9b534fc31e2c3ed57f5a5ef06814f23`) `EBattle8GroupActorOpeningCohorts`
- `EF:794B..EF:796C` (`33` bytes, SHA-1 `19c340b43361fe13f2bcb709b89643f229c6236b`) `EBattle8GroupActorFinalHelper`
- `EF:796C..EF:7970` (`4` bytes, SHA-1 `56025a7a5d5a8ee1a1c68a2f5b88491a8d4e5976`) `EBattle8GroupActorFinalSingular`
- `EF:7970..EF:797F` (`15` bytes, SHA-1 `5c3eb0d5485504b3e04a52ec3da5d24b7bd36567`) `EBattle8GroupActorFinalCohort`
- `EF:797F..EF:798F` (`16` bytes, SHA-1 `4f96cd2005bdb1ee1cd918cb471cff574f07aa8d`) `EBattle8GroupActorFinalCohorts`
- `EF:798F..EF:79B1` (`34` bytes, SHA-1 `382d187af964992ccb3bc63695695030b0d277fe`) `EBattle8GroupActorSurpriseHelper`
- `EF:79B1..EF:79B6` (`5` bytes, SHA-1 `a10ad7f83b45f191f7dd962fa5ba655b21cc0a66`) `EBattle8GroupActorPossessiveSingular`
- `EF:79B6..EF:79C6` (`16` bytes, SHA-1 `1cbb5a4d47444c21001efd34672b4d656c444f4f`) `EBattle8GroupActorPossessiveCohort`
- `EF:79C6..EF:79D7` (`17` bytes, SHA-1 `d007527ebf6d4dc0c0c9d48da65c9fd8cfb6bbc8`) `EBattle8GroupActorPossessiveCohorts`
- `EF:79D7..EF:79E6` (`15` bytes, SHA-1 `221d916a6e712021994e7c4684b3a4e4461f3256`) `EBattle8MsgBtlPlayerWin`
- `EF:79E6..EF:79EF` (`9` bytes, SHA-1 `22fde23f6d3e83b620160063961a09dd94fb0224`) `EBattle8PlayerWinEventBranch`
- `EF:79EF..EF:7A0A` (`27` bytes, SHA-1 `b16daf1c08292f4100a4100aacce1e17463db462`) `EBattle8PlayerWinExperienceText`
- `EF:7A0A..EF:7A14` (`10` bytes, SHA-1 `a1bd985ecd904e4dc7f4b9196d65bc24312ebb85`) `EBattle8PlayerWinHomesickBranch`
- `EF:7A14..EF:7A28` (`20` bytes, SHA-1 `e05701efbb9a38a5cea8b6cfcbd2c2fd0ff16135`) `EBattle8MsgBtlPlayerWinBoss`
- `EF:7A28..EF:7A4D` (`37` bytes, SHA-1 `4d2e54e69418be3f2b2317a6b4bda0b7ed87a1a8`) `EBattle8MsgBtlPlayerWinForce`
- `EF:7A4D..EF:7A66` (`25` bytes, SHA-1 `672a4fbbe3b373a33f71987733c859a721c6a601`) `EBattle8MsgBtlMonsterWin`
- `EF:7A66..EF:7A7D` (`23` bytes, SHA-1 `984036287db549d282f5beff29201f2d2b9ca871`) `EBattle8MsgBtlLevelUp`
- `EF:7A7D..EF:7A97` (`26` bytes, SHA-1 `ec77fa82818ea8cecc7c4834eeabfd2c57885a80`) `EBattle8MsgBtlLevelOffenseUp`
- `EF:7A97..EF:7AB1` (`26` bytes, SHA-1 `9d2dc4ed5905762d1a852394c42a29488fd25c44`) `EBattle8MsgBtlLevelDefenseUp`
- `EF:7AB1..EF:7AC9` (`24` bytes, SHA-1 `39b68910ac9dd7206a5bee0f0e8f633911b62986`) `EBattle8MsgBtlLevelSpeedUp`
- `EF:7AC9..EF:7AE0` (`23` bytes, SHA-1 `4a7050baace11ee1ea47ee40d14fb3d7b638b6dc`) `EBattle8MsgBtlLevelGutsUp`
- `EF:7AE0..EF:7AFB` (`27` bytes, SHA-1 `df79e167961329b312903fb495c4f9be48264ce9`) `EBattle8MsgBtlLevelVitalityUp`
- `EF:7AFB..EF:7B11` (`22` bytes, SHA-1 `3bd4ef6250187c7e7ddce8351afe96909c3aaa0a`) `EBattle8MsgBtlLevelIqUp`
- `EF:7B11..EF:7B28` (`23` bytes, SHA-1 `ef0f8019e02b166fe0aba14ad12df591443834e7`) `EBattle8MsgBtlLevelLuckUp`
- `EF:7B28..EF:7B46` (`30` bytes, SHA-1 `ecb58cf466d840e103faca3c57ebf8972fd1d725`) `EBattle8MsgBtlLevelMaxHpUp`
- `EF:7B46..EF:7B64` (`30` bytes, SHA-1 `f319f6186d7ebe34933682c772778e6b1100214e`) `EBattle8MsgBtlLevelMaxPpUp`
- `EF:7B64..EF:7B77` (`19` bytes, SHA-1 `b9e211e8574e37ce78c2d391d2b43777f2eb3ff3`) `EBattle8MsgBtlLearnPsi`
- `EF:7B77..EF:7B83` (`12` bytes, SHA-1 `b6be0ba66868c82cafdd691ac712705f421cd14f`) `EBattle8ByteSubstitutionPsiNameText`
- `EF:7B83..EF:7B85` (`2` bytes, SHA-1 `d13061bfe442388f8bf8b53be38aa80ed585e8b5`) `EBattle8PointerSubstitutionIntroState`
- `EF:7B85..EF:7BA0` (`27` bytes, SHA-1 `0b507165fcb107b37b9f7d92fdf7728fb2dff65a`) `EBattle8PointerSubstitutionSweetBranch`
- `EF:7BA0..EF:7BA2` (`2` bytes, SHA-1 `d13061bfe442388f8bf8b53be38aa80ed585e8b5`) `EBattle8PointerSubstitutionBranch2State`
- `EF:7BA2..EF:7BBF` (`29` bytes, SHA-1 `4a8f6b390ce34f65d348108205b2f550d4323e90`) `EBattle8PointerSubstitutionTearsBranch`
- `EF:7BBF..EF:7BC1` (`2` bytes, SHA-1 `d13061bfe442388f8bf8b53be38aa80ed585e8b5`) `EBattle8PointerSubstitutionBranch3State`
- `EF:7BC1..EF:7BDF` (`30` bytes, SHA-1 `20ff702f734c16985cdf2024350476ddbae5485a`) `EBattle8PointerSubstitutionOhBabyBranch`
- `EF:7BDF..EF:7C42` (`99` bytes, SHA-1 `ac0008afdd533cbce642a6a974fdc139a6e12e2e`) `EBattle8MsgBtlPresentByteSubstitution`
- `EF:7C42..EF:7C73` (`49` bytes, SHA-1 `9883fd43ae25bfc47c43f439c44c7f9b697743ab`) `EBattle8PresentRecipientDeadText`
- `EF:7C73..EF:7C89` (`22` bytes, SHA-1 `8a967e4efbdbc4b30f8ce9df0b7383b475aafb7b`) `EBattle8PresentInventoryFullText`
- `EF:7C89..EF:7CB4` (`43` bytes, SHA-1 `6c65899112a80c79c027fd860a338bc055828858`) `EBattle8PresentThrowAwayPrompt`
- `EF:7CB4..EF:7CED` (`57` bytes, SHA-1 `cdf2ec69a05a549e316427fe56a0ce913d6853ba`) `EBattle8PresentAbandonPrompt`
- `EF:7CED..EF:7CF8` (`11` bytes, SHA-1 `fc32170687965f02c20effcc7bc3d9882392ae4b`) `EBattle8PresentAbandonRetryText`
- `EF:7CF8..EF:7D0F` (`23` bytes, SHA-1 `2049a2c4eb026d5a9e973d3a2c55b9b559cf1fd4`) `EBattle8PresentAbandonConfirmedText`
- `EF:7D0F..EF:7D83` (`116` bytes, SHA-1 `e03d93926ccfc1c23b3e4432788f9c8b83303541`) `EBattle8PresentDropSelectionPrompt`
- `EF:7D83..EF:7DBE` (`59` bytes, SHA-1 `de1a1a6d3283e8ab312a1f6c10c88035bb0d8796`) `EBattle8PresentDropConfirmedText`
- `EF:7DBE..EF:7DD5` (`23` bytes, SHA-1 `8b1dce22187c4631cb6f88b5cb74df4b81b50070`) `EBattle8PresentDropForbiddenText`
- `EF:7DD5..EF:7E25` (`80` bytes, SHA-1 `dafcd39be3495506595588a2d98ec0bee797af4f`) `EBattle8MsgBtlCheckPresentGetByteSubstitution`
- `EF:7E25..EF:7E3E` (`25` bytes, SHA-1 `326d9aa5613a268a7cf091c729ebce805764c396`) `EBattle2MsgBtlPpDown`
- `EF:7E3E..EF:7E55` (`23` bytes, SHA-1 `62b508e63eb223b99d8b88f4ced5c3d19c6ec3bf`) `EBattle2MsgBtlOkoru`
- `EF:7E55..EF:7E70` (`27` bytes, SHA-1 `ad403c9d5c62af3b63a0c2073426d080edae4595`) `EBattle2MsgBtlKitanaiKotoba`
- `EF:7E70..EF:7E88` (`24` bytes, SHA-1 `d4cc7c09fd548f062cece1a70ac73fd9964ef968`) `EBattle2MsgBtlSuibun`
- `EF:7E88..EF:7EAC` (`36` bytes, SHA-1 `7adc1d09fead93fcb2723913006fbb6a7583ebd4`) `EBattle2MsgBtlEnergy`
- `EF:7EAC..EF:7ED5` (`41` bytes, SHA-1 `0bb466bd8007c342c6a9297891c822d2673299ed`) `EBattle2MsgBtlDokuKamituki`
- `EF:7ED5..EF:7F02` (`45` bytes, SHA-1 `5d6e6f3b90307c29703ea2ea2a8b9269e44b7d37`) `EBattle2MsgBtlYoroMissile`
- `EF:7F02..EF:7F1E` (`28` bytes, SHA-1 `598fb84e36c1c4e781b7776dd6819c825c857d4f`) `EBattle2MsgBtlMultiAttack`
- `EF:7F1E..EF:7F32` (`20` bytes, SHA-1 `52fa387f2cbecca8ff2195b8de671309037c6804`) `EBattle2MsgBtlMigamae`
- `EF:7F32..EF:7F5A` (`40` bytes, SHA-1 `85f388be8449a78fd1d47b3faec59d47cf1a0f99`) `EBattle2MsgBtlFireball`
- `EF:7F5A..EF:7F7B` (`33` bytes, SHA-1 `b0142cf7c5087b89a62952b0991c1bd0dbd913fb`) `EBattle2MsgBtlGekitotu`
- `EF:7F7B..EF:7F9A` (`31` bytes, SHA-1 `a357002a69f1b46b6a76a7e9b3055c7bb0c77775`) `EBattle2MsgBtlKarate`
- `EF:7F9A..EF:7FC3` (`41` bytes, SHA-1 `75819d5a006c32395c7a2a2cc2bacff2436c788e`) `EBattle2MsgBtlTomoe`
- `EF:7FC3..EF:7FE0` (`29` bytes, SHA-1 `69f0796dc2b04c37be3fb915a1eda2ddb512dbc1`) `EBattle2MsgBtlBousou`
- `EF:7FE0..EF:7FFC` (`28` bytes, SHA-1 `3e2a4bdea4fc98b6be491c43db53802c41bde675`) `EBattle2MsgBtlKnife`
- `EF:7FFC..EF:8010` (`20` bytes, SHA-1 `5cd8bbe977488af7d4e836905a40f20d2543df07`) `EBattle2MsgBtlTossin`
- `EF:8010..EF:8026` (`22` bytes, SHA-1 `8425ae9463d5386f41bf5748ea3474b581fccdfd`) `EBattle2MsgBtlKamituki`
- `EF:8026..EF:804B` (`37` bytes, SHA-1 `f923668a1fc483512cc1b511ed685041e859caf3`) `EBattle2MsgBtlHikkaki`
- `EF:804B..EF:806D` (`34` bytes, SHA-1 `003a2d6cffe3fa65dd03c9665a3e70afdddc4ff1`) `EBattle2MsgBtlSippo`
- `EF:806D..EF:808D` (`32` bytes, SHA-1 `c683c425d77fd742eacc25e674d6f856cad46a72`) `EBattle2MsgBtlNoshikakari`
- `EF:808D..EF:80AC` (`31` bytes, SHA-1 `1d59a71f4c62e68ddf8b5529ee3d7a0c81c4b84a`) `EBattle2MsgBtlKamibukuro`
- `EF:80AC..EF:80C4` (`24` bytes, SHA-1 `68c5e94a8b1ecc6ec2ddac6e066621481fe6f4fe`) `EBattle2MsgBtlKonbou`
- `EF:80C4..EF:80E4` (`32` bytes, SHA-1 `be3cd61d6d790466e389c8d4a19deb52b8a4eda4`) `EBattle2MsgBtlTatumaki`
- `EF:80E4..EF:8109` (`37` bytes, SHA-1 `b3f9f938dce38896c987ec9240ded077a1bfdfbf`) `EBattle2MsgBtlWater`
- `EF:8109..EF:812B` (`34` bytes, SHA-1 `53867573d3ca72ac82a92a2691f1b2c1a0dc6a19`) `EBattle2MsgBtlFutekiSmile`
- `EF:812B..EF:814F` (`36` bytes, SHA-1 `e74b9c9ae63002c1db3ea7abf8cb17562ba686c6`) `EBattle2MsgBtlLoudSmile`
- `EF:814F..EF:8167` (`24` bytes, SHA-1 `1406b3b5c44491ee07f0035ec553474792d6a55f`) `EBattle2MsgBtlNijiriyoru`
- `EF:8167..EF:8186` (`31` bytes, SHA-1 `a6d127caa5d9da57e9250b5ff7efdb2c9a62ff2a`) `EBattle2MsgBtlTubuyaki1`
- `EF:8186..EF:81A5` (`31` bytes, SHA-1 `b72d3a435ff08c08ca000b008f4655333c269777`) `EBattle2MsgBtlTubuyaki2`
- `EF:81A5..EF:81C4` (`31` bytes, SHA-1 `e01da5c379b716391ea472922d569164ca7fc4a1`) `EBattle2MsgBtlTubuyaki3`
- `EF:81C4..EF:81D7` (`19` bytes, SHA-1 `c0fbd669a88ec949c2a21f88712018535491f99f`) `EBattle2MsgBtlKorobu`
- `EF:81D7..EF:81F1` (`26` bytes, SHA-1 `04b5000c1073ded928bc32f09a02e8652c54b772`) `EBattle2MsgBtlBootto`
- `EF:81F1..EF:8211` (`32` bytes, SHA-1 `4d2f2d2fc803360d542ab15691cb06621dc22e4e`) `EBattle2MsgBtlJyouki`
- `EF:8211..EF:8226` (`21` bytes, SHA-1 `fe763552f4afd02d5177d51edaee3b5686d705a0`) `EBattle2MsgBtlYoroyoro`
- `EF:8226..EF:8239` (`19` bytes, SHA-1 `796343d6f46509bee0764b341f85ab8e7d5e6951`) `EBattle2MsgBtlFurafura`
- `EF:8239..EF:825C` (`35` bytes, SHA-1 `55e8e7100f0546551f76ae0bc38ae504856ef4ed`) `EBattle2MsgBtlNitanita`
- `EF:825C..EF:8281` (`37` bytes, SHA-1 `9d1dfffbada6fb639a91c9ecda304fe52b8166af`) `EBattle2MsgBtlKokyuu`
- `EF:8281..EF:8299` (`24` bytes, SHA-1 `62a5b594ee81fff4b5989ab508d8cc00ec85c4aa`) `EBattle2MsgBtlAisatu`
- `EF:8299..EF:82BC` (`35` bytes, SHA-1 `9109b3c215aa6a5088aba3ad48e560a0e137f7b5`) `EBattle2MsgBtlUnari`
- `EF:82BC..EF:82D7` (`27` bytes, SHA-1 `4c0bde06d175c46ede6731980022ae937b9fe071`) `EBattle2MsgBtlKachikachi`
- `EF:82D7..EF:82F7` (`32` bytes, SHA-1 `5a3f46d35b42a7e4d4ba283dbe852b6cff01a407`) `EBattle2MsgBtlMabusiiHikari`
- `EF:82F7..EF:8317` (`32` bytes, SHA-1 `814782bd0c0fc50f71212577f6c07e33213a2e78`) `EBattle2MsgBtlBiribiri`
- `EF:8317..EF:833E` (`39` bytes, SHA-1 `05b7ffcb0b2d759a14805f3e8b751620a039b0f2`) `EBattle2MsgBtlKafun`
- `EF:833E..EF:835C` (`30` bytes, SHA-1 `f6dbe8e72962065aba0cb517f1b989878f798f5b`) `EBattle2MsgBtlColdHand`
- `EF:835C..EF:838A` (`46` bytes, SHA-1 `7b8d12313f204b74ba26d24358487f2eb82246a2`) `EBattle2MsgBtlPoisonBreath`
- `EF:838A..EF:83A8` (`30` bytes, SHA-1 `dc29ae79032986a73eca082ce7a40b7576c899e3`) `EBattle2MsgBtlHaikiGas`
- `EF:83A8..EF:83CA` (`34` bytes, SHA-1 `c34824f9fbb92f396328cd17f130aabe04b5ba49`) `EBattle2MsgBtlLaughHen`
- `EF:83CA..EF:83ED` (`35` bytes, SHA-1 `df48a364ea3ae15bff4a6c36865fb6bcb59d006c`) `EBattle2MsgBtlFue`
- `EF:83ED..EF:8413` (`38` bytes, SHA-1 `01f9156f8793463283afb295e0e2d387291bf972`) `EBattle2MsgBtlJumpToFace`
- `EF:8413..EF:843F` (`44` bytes, SHA-1 `bde83f459bf6244484edc67955bd6654773055be`) `EBattle2MsgBtlChouOnpa`
- `EF:843F..EF:8444` (`5` bytes, SHA-1 `d296611446d215d359e8c7664e0a30f31aa7b62e`) `EBattle0MsgAtStartAsleep`
- `EF:8444..EF:8445` (`1` bytes, SHA-1 `c4ea21bb365bbeeaf5f2c654883e56d11e43c44e`) `EBattle0MsgAtStartPsiSeal`
- `EF:8445..EF:845D` (`24` bytes, SHA-1 `290b309cbe7864982914515bbac8838cfec3ec00`) `EBattle0MsgAtStartStrange`
- `EF:845D..EF:8477` (`26` bytes, SHA-1 `b9cc80704b48261d7854d1582bd91cdb057d291d`) `EBattle0MsgRandomActStrange`
- `EF:8477..EF:848C` (`21` bytes, SHA-1 `e8df4e1a416a16e883880dddfb6f8cfea9620e20`) `EBattle0MsgRandomActMushroom`
- `EF:848C..EF:84A7` (`27` bytes, SHA-1 `e99323f03a7fecbf7430c1c5a4705be0f63e7bbe`) `EBattle1MsgBtlAttack`
- `EF:84A7..EF:84B6` (`15` bytes, SHA-1 `9c57f551049dbfdfe3f3e70588767d34b4dee5ee`) `EBattle1AttackPlayerSideBranch`
- `EF:84B6..EF:84C6` (`16` bytes, SHA-1 `6b8d415e3a2eb1313177e37f9276f39cf41b329c`) `EBattle1MsgBtlShoot`
- `EF:84C6..EF:84D4` (`14` bytes, SHA-1 `ae67ec66f07eb13a1bf5563e47b2d5d48d2a43fa`) `EBattle1MsgBtlGuard`
- `EF:84D4..EF:84F3` (`31` bytes, SHA-1 `a2324897cf11d3b03a6e89ccc07526c64949a6ab`) `EBattle1MsgBtlMetamorphose`
- `EF:84F3..EF:8511` (`30` bytes, SHA-1 `9aa5ecf35c8d1a4c6ed04410e38632dd3b3d20d9`) `EBattle1MsgBtlPlayerFlee`
- `EF:8511..EF:8530` (`31` bytes, SHA-1 `56bab7d7ebab3e80fc4e8caa0360e928e87ecfce`) `EBattle1MsgBtlPlayerFleeFailed`
- `EF:8530..EF:8543` (`19` bytes, SHA-1 `2e0e634a37bc7bb6b511a9912f101bfe9d4e2a08`) `EBattle1MsgBtlCheck`
- `EF:8543..EF:8568` (`37` bytes, SHA-1 `3c0205881fd711e75811d00d23d8eab375519aca`) `EBattle1MsgBtlPsi`
- `EF:8568..EF:857E` (`22` bytes, SHA-1 `eddea2b0a407599f67da715136320d0ad7df8434`) `EBattle1PsiPlayerSideBranch`
- `EF:857E..EF:864C` (`206` bytes, SHA-1 `ec707732de843dd8d0abe6f92b98fa0caf3e9b26`) `EBattle1PsiAnimationDispatch`
- `EF:864C..EF:866E` (`34` bytes, SHA-1 `ce2b90bbf03460d92795d3b257fcfebde934203c`) `EBattle1PsiEffectBranch1`
- `EF:866E..EF:8698` (`42` bytes, SHA-1 `218694e33ef698d221e4b70f886ec82f1d58b57b`) `EBattle1PsiEffectBranch2`
- `EF:8698..EF:86E2` (`74` bytes, SHA-1 `c8afd6c2732a2b05a59bb99d89bf0b318ccdab11`) `EBattle1PsiEffectBranch3`
- `EF:86E2..EF:874A` (`104` bytes, SHA-1 `ed5a9e5453145ff58972590b0c6a5129a226b296`) `EBattle1PsiEffectBranch4`
- `EF:874A..EF:875F` (`21` bytes, SHA-1 `77ef427c60e6f4661fe595a64c11ac1309fa0f17`) `EBattle1PsiEffectBranch5`
- `EF:875F..EF:8777` (`24` bytes, SHA-1 `0863376914292a310452e1f6d5cf9c8ec002fd25`) `EBattle1PsiEffectBranch6`
- `EF:8777..EF:878F` (`24` bytes, SHA-1 `8f0729f6aa5bf3250cc0316104003b2595dbf930`) `EBattle1PsiEffectBranch7`
- `EF:878F..EF:87AC` (`29` bytes, SHA-1 `9b91884c0ce8e8e378914cc23732e19f891535a0`) `EBattle1PsiEffectBranch8`
- `EF:87AC..EF:87C3` (`23` bytes, SHA-1 `6f9bf3f6f55d99837f9ddfb68e0df8d1de7d666c`) `EBattle1PsiEffectBranch9`
- `EF:87C3..EF:87DA` (`23` bytes, SHA-1 `eec8d005cba50856630e74edb227c1bf4ccfa251`) `EBattle1PsiEffectBranch10`
- `EF:87DA..EF:87F4` (`26` bytes, SHA-1 `6d54b1dfd7f86685bb26e0c7b5b3baa2f2311f5e`) `EBattle1PsiEffectBranch11`
- `EF:87F4..EF:8813` (`31` bytes, SHA-1 `076c405486c2f25ca4213396771efb5a162a1405`) `EBattle1PsiEffectBranch12`
- `EF:8813..EF:8814` (`1` bytes, SHA-1 `c4ea21bb365bbeeaf5f2c654883e56d11e43c44e`) `EBattle1PsiEffectBranch13`
- `EF:8814..EF:8823` (`15` bytes, SHA-1 `bacf80ef562971b5da5160d6dc5f1207a5a7e9f1`) `EBattle1MsgBtlThunderSmall`
- `EF:8823..EF:8837` (`20` bytes, SHA-1 `70e485664a175f6e96d22f420a2e64f0a19a7167`) `EBattle1MsgBtlThunderLarge`
- `EF:8837..EF:883D` (`6` bytes, SHA-1 `d578438044de353967285000e232ed6a3197dc6c`) `EBattle1MsgBtlThunderMissSound`
- `EF:883D..EF:8847` (`10` bytes, SHA-1 `f597df942fb9d6040573b05ffb6159cf8c203fe0`) `EBattle1PsiEffectBranch17`
- `EF:8847..EF:8851` (`10` bytes, SHA-1 `385acbf80d92ba740dfe7e2237138c14cb7af3fd`) `EBattle1PsiEffectBranch18`
- `EF:8851..EF:8868` (`23` bytes, SHA-1 `6466f9e55d028c83a18fcb91c353b5ab3348d8d9`) `EBattle1PsiEffectBranch19`
- `EF:8868..EF:8882` (`26` bytes, SHA-1 `23ff0c9a6d5f0785db34a8ee10a6becb17a4be31`) `EBattle1PsiEffectBranch20`
- `EF:8882..EF:88B8` (`54` bytes, SHA-1 `5c8f7e904dd0d302133cbe80c0d67499ecf8bfeb`) `EBattle1PsiEffectBranch21`
- `EF:88B8..EF:88E9` (`49` bytes, SHA-1 `6a15a90a432ef6f937a5fda1438af7fe230491b9`) `EBattle1PsiEffectBranch22`
- `EF:88E9..EF:88EC` (`3` bytes, SHA-1 `d683592bd8f0f4027832289929db6c4b17d8c1d8`) `EBattle1PsiEffectBranch23`
- `EF:88EC..EF:88F6` (`10` bytes, SHA-1 `d41331b297de5b85c40c27fec7922ca2c210bc82`) `EBattle1PsiEffectBranch31`
- `EF:88F6..EF:8900` (`10` bytes, SHA-1 `d41331b297de5b85c40c27fec7922ca2c210bc82`) `EBattle1PsiEffectBranch32`
- `EF:8900..EF:890A` (`10` bytes, SHA-1 `1d2de306edf4d102fd1e949a6f1a45552d0ead43`) `EBattle1PsiEffectBranch33`
- `EF:890A..EF:8914` (`10` bytes, SHA-1 `1d2de306edf4d102fd1e949a6f1a45552d0ead43`) `EBattle1PsiEffectBranch34`
- `EF:8914..EF:891E` (`10` bytes, SHA-1 `31138bbb7086ac62a11e26c82af0f29f57d34ee5`) `EBattle1PsiEffectBranch35`
- `EF:891E..EF:8928` (`10` bytes, SHA-1 `31138bbb7086ac62a11e26c82af0f29f57d34ee5`) `EBattle1PsiEffectBranch36`
- `EF:8928..EF:8932` (`10` bytes, SHA-1 `b345262ccbc40a82c3bf346b6dac5d39c51cd634`) `EBattle1PsiEffectBranch37`
- `EF:8932..EF:893C` (`10` bytes, SHA-1 `b345262ccbc40a82c3bf346b6dac5d39c51cd634`) `EBattle1PsiEffectBranch38`
- `EF:893C..EF:894C` (`16` bytes, SHA-1 `d0af558122f28e371aa5675c3dba7b576dab985d`) `EBattle1PsiEffectBranch41`
- `EF:894C..EF:895C` (`16` bytes, SHA-1 `84be21126a203362bced7549ed0899ddf8d4f760`) `EBattle1PsiEffectBranch42`
- `EF:895C..EF:896C` (`16` bytes, SHA-1 `3c40e5f79fb9ddf9520e5f9de17c78066105b0f7`) `EBattle1PsiEffectBranch43`
- `EF:896C..EF:897C` (`16` bytes, SHA-1 `c3317246f9f2e20b90a313b5c210562340583e90`) `EBattle1PsiEffectBranch44`
- `EF:897C..EF:898C` (`16` bytes, SHA-1 `be771ab8a27e5cd0a91a66896b20e7598d0c56b4`) `EBattle1PsiEffectBranch45`
- `EF:898C..EF:899C` (`16` bytes, SHA-1 `54efcb0927a24fcb20d757fe916f53fed32146ff`) `EBattle1PsiEffectBranch46`
- `EF:899C..EF:89AC` (`16` bytes, SHA-1 `dcc52620ced6474867a1bc52e9c368f2fa9bbed7`) `EBattle1PsiEffectBranch47`
- `EF:89AC..EF:89BC` (`16` bytes, SHA-1 `05a5c2915048697e801c8fb55fbed9b7575503b3`) `EBattle1PsiEffectBranch48`
- `EF:89BC..EF:89CE` (`18` bytes, SHA-1 `731b1615df090f21f79e7faef34ff2905d213bff`) `EBattle1PsiEffectBranch49`
- `EF:89CE..EF:89E0` (`18` bytes, SHA-1 `c14cb7a4b9b698376aec8d772ebe8cc2fcb90366`) `EBattle1PsiEffectBranch50`
- `EF:89E0..EF:89FE` (`30` bytes, SHA-1 `8afe90ada4dfe0b5def823aeba59fd3ad4a62b83`) `EBattle1MsgBtlPray`
- `EF:89FE..EF:8A18` (`26` bytes, SHA-1 `82516287de48a79fcc57c207a112334b7dc1e5d8`) `EBattle3MsgBtlJihibiki`
- `EF:8A18..EF:8A33` (`27` bytes, SHA-1 `b9cf25d951570548a9173205917a1e124c8e642e`) `EBattle3MsgBtlOsaetsuke`
- `EF:8A33..EF:8A52` (`31` bytes, SHA-1 `a9a6f80fa14e823657269b9d4b31ddfe73be7fff`) `EBattle3MsgBtlCurseWord`
- `EF:8A52..EF:8A6F` (`29` bytes, SHA-1 `4f91dc6da094af749a6e9d11f864a1ccc7385948`) `EBattle3MsgBtlJimi`
- `EF:8A6F..EF:8A8C` (`29` bytes, SHA-1 `b2d6de625aaec60f0c0a5fb3cd8960d9c86747cf`) `EBattle3MsgBtlPenki`
- `EF:8A8C..EF:8AA3` (`23` bytes, SHA-1 `fa89bcca9563639b4ab17e070bae0b505eabd87d`) `EBattle3MsgBtlNaguriKakari`
- `EF:8AA3..EF:8AC2` (`31` bytes, SHA-1 `7958bb3b03bfff1342284529767b16d6d187dbe7`) `EBattle3MsgBtlClaw`
- `EF:8AC2..EF:8ADD` (`27` bytes, SHA-1 `a91b11f0930f7946017719b45d7c40719d76d48f`) `EBattle3MsgBtlKuchibashi`
- `EF:8ADD..EF:8AF8` (`27` bytes, SHA-1 `9ce620a6a7cc254e98e62faaf3ec46964da1f001`) `EBattle3MsgBtlTsuno`
- `EF:8AF8..EF:8B11` (`25` bytes, SHA-1 `58b5a0c797894b84c4be5351b86664266a1de1df`) `EBattle3MsgBtlPunch`
- `EF:8B11..EF:8B2F` (`30` bytes, SHA-1 `78e6dd2a297ed89f0a39f966d95223e77084482c`) `EBattle3MsgBtlPumpkin`
- `EF:8B2F..EF:8B4A` (`27` bytes, SHA-1 `69d3dc47622dba92d8559a1b40437d128d75454f`) `EBattle3MsgBtlBeam`
- `EF:8B4A..EF:8B65` (`27` bytes, SHA-1 `bd4124fb9b77641746a3257a196d127f749d5266`) `EBattle3MsgBtlYari`
- `EF:8B65..EF:8B89` (`36` bytes, SHA-1 `9c048f1c73a7b16c2d40bb4b3cf6c4d796cd908a`) `EBattle3MsgBtlFumitsuke`
- `EF:8B89..EF:8BA8` (`31` bytes, SHA-1 `5417a382c51d8e4d0e5747665d0ebc805e87047e`) `EBattle3MsgBtlFurafuupu`
- `EF:8BA8..EF:8BC0` (`24` bytes, SHA-1 `3f23d1e935b11d01c3a5f0fd7c5ac3584f024507`) `EBattle3MsgBtlTaiatari`
- `EF:8BC0..EF:8BE8` (`40` bytes, SHA-1 `a5a34cf8340e55b1a1c0e3a907e0c1035772c0aa`) `EBattle3MsgBtlSkateboard`
- `EF:8BE8..EF:8BFB` (`19` bytes, SHA-1 `ae517ccac21dfd6f14940ad00e0afc12c3ae1dbd`) `EBattle3MsgBtlKamitsukiDiamond`
- `EF:8BFB..EF:8C1D` (`34` bytes, SHA-1 `8f38bb4bfe94c040267c40727b8865266ea1db9a`) `EBattle3MsgBtlKudamaki`
- `EF:8C1D..EF:8C3A` (`29` bytes, SHA-1 `501f385ddfdc187cbae2cad0900521f642b4aae2`) `EBattle3MsgBtlSekkyou`
- `EF:8C3A..EF:8C58` (`30` bytes, SHA-1 `c7e3eb9c98f5d814edd59d5b3bb46a3e5aa97cc5`) `EBattle3MsgBtlShikaritsuke`
- `EF:8C58..EF:8C75` (`29` bytes, SHA-1 `9b42d558d2e655d77fae4bad4cfd20e53ba2a43c`) `EBattle3MsgBtlBadSmell`
- `EF:8C75..EF:8C92` (`29` bytes, SHA-1 `b4982e8d6381eb7f10748d19f888653b69d8d4a9`) `EBattle3MsgBtlLoudVoice`
- `EF:8C92..EF:8CAC` (`26` bytes, SHA-1 `30917200a7b1000f96d516272cec8facb90f1cfc`) `EBattle3MsgBtlOtakebi`
- `EF:8CAC..EF:8CC7` (`27` bytes, SHA-1 `a6e12ad62550dfe21bbdefa92948f39f72b61d17`) `EBattle3MsgBtlFakeDead`
- `EF:8CC7..EF:8CDD` (`22` bytes, SHA-1 `c053dea2b746d7465ec36b4cbda8e7fde606dae4`) `EBattle3MsgBtlYudan`
- `EF:8CDD..EF:8CFB` (`30` bytes, SHA-1 `566d7352fc35a8042bbff3e69ded5685d144bdad`) `EBattle3MsgBtlYudan1`
- `EF:8CFB..EF:8D17` (`28` bytes, SHA-1 `a7e7834f9eb926f03d26dae91032cab9fe910ea2`) `EBattle3MsgBtlYudan2`
- `EF:8D17..EF:8D2F` (`24` bytes, SHA-1 `ffa8ca67550206b698c7d354dc445011b1c436fe`) `EBattle3MsgBtlYudan3`
- `EF:8D2F..EF:8D4C` (`29` bytes, SHA-1 `2a6d2c8d426340e2668e23b7004c71851b2038e4`) `EBattle3MsgBtlYudan4`
- `EF:8D4C..EF:8D72` (`38` bytes, SHA-1 `b8360b3a6defa5ef388b5156d8d5ffe4c99fe053`) `EBattle3MsgBtlYudanLifeup`
- `EF:8D72..EF:8D9F` (`45` bytes, SHA-1 `bfe6951299f51a254f8fc2c8a7ad342a71ee7849`) `EBattle3MsgBtlNebieBeam`
- `EF:8D9F..EF:8DC1` (`34` bytes, SHA-1 `f4ec5f481aa20e8c37e63a06f35875137d5091a2`) `EBattle3MsgBtlNeutralizeSparkle`
- `EF:8DC1..EF:8DDE` (`29` bytes, SHA-1 `937dfc5ae9d58e40fc26e3abf8c21d78635a4cb7`) `EBattle3MsgBtlMakitsuki`
- `EF:8DDE..EF:8E27` (`73` bytes, SHA-1 `a2be184479ff15037a0869f1ce3735092130949d`) `EBattle3MsgBtlToDiamondDog`
- `EF:8E27..EF:8E3C` (`21` bytes, SHA-1 `ed6bb71d52ce16b2c70f35a67f0f207f0b83571e`) `EBattle3MsgBtlWarpNear`
- `EF:8E3C..EF:8E5E` (`34` bytes, SHA-1 `8dd727c3912f31d6a832803481482da02856bb65`) `EBattle3MsgBtlAntipsi`
- `EF:8E5E..EF:8E7E` (`32` bytes, SHA-1 `cb9e63f7d89c72e768b383127b4fa45d1e1babb7`) `EBattle3MsgBtlHpsuck`
- `EF:8E7E..EF:8E9E` (`32` bytes, SHA-1 `416aeaab8b0876ccc0dd67be014af23b5e05f153`) `EBattle3MsgBtlHpsucksp`
- `EF:8E9E..EF:8EBE` (`32` bytes, SHA-1 `aac956c87de5ca8f08c162acb29102248e1e6ca9`) `EBattle3MsgBtlShieldkill`
- `EF:8EBE..EF:8EE2` (`36` bytes, SHA-1 `e1dbb11052439787f5983da25167064d3bbbe743`) `EBattle3MsgBtlBadSmellGas`
- `EF:8EE2..EF:8F17` (`53` bytes, SHA-1 `9d095da1f28789d8c787cfc7241d78a97b832eff`) `EBattle3MsgBtlLightning`
- `EF:8F17..EF:8F4A` (`51` bytes, SHA-1 `833abb473eaaedd8995dcddb89018c082eb03c8c`) `EBattle3MsgBtlLightningB`
- `EF:8F4A..EF:8F91` (`71` bytes, SHA-1 `886d431e469f10d4a3febb85630f90affcbdfa12`) `EBattle3MsgBtlLightningC`
- `EF:8F91..EF:8FAD` (`28` bytes, SHA-1 `9281e687823201e0c4448a95e648ee7cb050705f`) `EBattle3MsgBtlGyiyyig3`
- `EF:8FAD..EF:8FC9` (`28` bytes, SHA-1 `85565ca69ac505eba7758a22fb37a12eb0c52c73`) `EBattle9SubSorezoreHelper`
- `EF:8FC9..EF:8FCB` (`2` bytes, SHA-1 `4fce485363574d7c53f9f57541e8ca8e5547ca3e`) `EBattle9BranchSorezoreEnd`
- `EF:8FCB..EF:8FE4` (`25` bytes, SHA-1 `c38cfb4e78b4b7becd09aa6f89758a5da605112f`) `EBattle9MsgFmonMoonA`
- `EF:8FE4..EF:9003` (`31` bytes, SHA-1 `c304db5699c9b0354d4e9dfc937712456cc5b022`) `EBattle9MsgFmonMoonB`
- `EF:9003..EF:9022` (`31` bytes, SHA-1 `8cd064f06e194706d2f5e83df5e2e5856125e662`) `EBattle9MsgFmonMoonB2`
- `EF:9022..EF:9041` (`31` bytes, SHA-1 `13972fd4c49638f84c6dacf9af9d73684aaf0a9c`) `EBattle9MsgFmonMoonC`
- `EF:9041..EF:9060` (`31` bytes, SHA-1 `dce7701bc60980c9a3c122989b8adb8bc5380786`) `EBattle9MsgFmonPyraAA`
- `EF:9060..EF:907F` (`31` bytes, SHA-1 `e8c17004311bf72e64fefb7ba9070b6fb3bd3f84`) `EBattle9MsgFmonPyraAB`
- `EF:907F..EF:909E` (`31` bytes, SHA-1 `956edb5ee5ef7ded7861cb538998a858e3e4c24f`) `EBattle9MsgFmonPyraAC`
- `EF:909E..EF:90BD` (`31` bytes, SHA-1 `ed376cb9bbcca2fb3368a5c9339688df8602c136`) `EBattle9MsgFmonPyraAD`
- `EF:90BD..EF:90DC` (`31` bytes, SHA-1 `484c78017457ae7074e5284f941fd04f0de693c4`) `EBattle9MsgFmonPyraAE`
- `EF:90DC..EF:90F9` (`29` bytes, SHA-1 `7861af5351db2579422044cdb40272325f5ce72c`) `EBattle9MsgFmonPyraAF`
- `EF:90F9..EF:9118` (`31` bytes, SHA-1 `a4863329f6fbe984984ddbfd9e83cdad044cf531`) `EBattle9MsgFmonPyraAG`
- `EF:9118..EF:9137` (`31` bytes, SHA-1 `41cf3f6628b17355784680bee25d6c21645a552e`) `EBattle9MsgFmonPyraAH`
- `EF:9137..EF:9156` (`31` bytes, SHA-1 `1afc8860c48cd15d61b69432c57c05d0c1baad1a`) `EBattle9MsgFmonPyraAI`
- `EF:9156..EF:9175` (`31` bytes, SHA-1 `65f97bb7bce387d3f08033ed92303a23b297866f`) `EBattle9MsgFmonPyraAJ`
- `EF:9175..EF:9194` (`31` bytes, SHA-1 `9cefc0675df7e868d7b03fe9a25b014af2609281`) `EBattle9MsgFmonPyraAK`
- `EF:9194..EF:91B3` (`31` bytes, SHA-1 `8f26f4addbc1bd47d8477ea3d1f47278e098d633`) `EBattle9MsgFmonPyraAL`
- `EF:91B3..EF:91D2` (`31` bytes, SHA-1 `262501c913e8458e7556e5b83105693793845789`) `EBattle9MsgFmonPyraAM`
- `EF:91D2..EF:91F1` (`31` bytes, SHA-1 `c75b54a7ca63939f5c974b0c52b11ea2d7dafd64`) `EBattle9MsgFmonPyraAN`
- `EF:91F1..EF:9210` (`31` bytes, SHA-1 `60ba4558cf89731322edd63f94ac9b50ae53b74d`) `EBattle9MsgFmonPyraAO`
- `EF:9210..EF:922F` (`31` bytes, SHA-1 `7761d652ae6a5b92be2269760ff25ec4379faeba`) `EBattle9MsgFmonPyraAP`
- `EF:922F..EF:924E` (`31` bytes, SHA-1 `3dbd41343a9b165b8d7180da4804eb4cb29a47a0`) `EBattle9MsgFmonPyraAQ`
- `EF:924E..EF:926D` (`31` bytes, SHA-1 `2ebc7c757a0baa868ff139438ab7f5364c35d79e`) `EBattle9MsgFmonPyraBA`
- `EF:926D..EF:928C` (`31` bytes, SHA-1 `aea4093eb19f7cefd5bf3164c9adf5522530376b`) `EBattle9MsgFmonPyraBB`
- `EF:928C..EF:92AB` (`31` bytes, SHA-1 `8cebe9fbe07c4307227d4f342485c2dd163cb29e`) `EBattle9MsgFmonPyraBC`
- `EF:92AB..EF:92CA` (`31` bytes, SHA-1 `c1f6fd356c890496b066f62a4a01b893cc9c06be`) `EBattle9MsgFmonPyraBD`
- `EF:92CA..EF:92E9` (`31` bytes, SHA-1 `99bc7f88df3f898cb37ea840d4516534c284a413`) `EBattle9MsgFmonPyraBE`
- `EF:92E9..EF:9308` (`31` bytes, SHA-1 `92702d492224f3ef0ce443c19c27b1859f8d96dd`) `EBattle9MsgFmonPyraBF`
- `EF:9308..EF:9327` (`31` bytes, SHA-1 `271df4f18cbe770f4d239fcd32b8443da1d0b468`) `EBattle9MsgFmonPyraBG`
- `EF:9327..EF:9346` (`31` bytes, SHA-1 `6ebe77996708dec675a7366d5b93512318faf360`) `EBattle9MsgFmonPyraBH`
- `EF:9346..EF:9365` (`31` bytes, SHA-1 `3c592975cc6025e1c61759b7f9a5a9fa20521a5b`) `EBattle9MsgFmonPyraBI`
- `EF:9365..EF:9384` (`31` bytes, SHA-1 `3dfe4fc6c9f2998337a731f040770719574a24fe`) `EBattle9MsgFmonBrickAA`
- `EF:9384..EF:93A3` (`31` bytes, SHA-1 `815cf57d88c0abbb5de7b6c074ea6ebcb730499e`) `EBattle9MsgFmonBrickAB`
- `EF:93A3..EF:93C2` (`31` bytes, SHA-1 `1fa670e775cb500bcaed55394840bcf8717bef83`) `EBattle9MsgFmonBrickBA`
- `EF:93C2..EF:93E1` (`31` bytes, SHA-1 `0ba76b461380516d7ea8325da30c4c8eb51e7645`) `EBattle9MsgFmonBrickBB`
- `EF:93E1..EF:9400` (`31` bytes, SHA-1 `a2082d742be870c306f1c0135df29947a82c549b`) `EBattle9MsgFmonBrickCA`
- `EF:9400..EF:941F` (`31` bytes, SHA-1 `f3d5d78b11c0464af283742409b5d6476f103ae5`) `EBattle9MsgFmonBrickCB`
- `EF:941F..EF:9448` (`41` bytes, SHA-1 `2a7854d77988c48c20b9697fb68685e0c9c0130f`) `EBattle9MsgFmonStoneBoss`
- `EF:9448..EF:9467` (`31` bytes, SHA-1 `316cc125d02314e085bd6671a824cc815d954230`) `EBattle9MsgFmonPyraBoss`
- `EF:9467..EF:9486` (`31` bytes, SHA-1 `be526fe81e108312ed7c4684cb9c01b3bd5b63d5`) `EBattle9MsgFmonKraken2A`
- `EF:9486..EF:94A5` (`31` bytes, SHA-1 `b8145bbfecb61c2a9cf90dda65a5f5cde0161317`) `EBattle9MsgFmonKraken2B`
- `EF:94A5..EF:94C4` (`31` bytes, SHA-1 `70ac0ebd90c5586c45ecaf4e81deaf856673347f`) `EBattle9MsgFmonKraken2C`
- `EF:94C4..EF:94E3` (`31` bytes, SHA-1 `639b9364ee7c4f7392fc117d2e8ab9975a05301e`) `EBattle9MsgFmonHieroglyphA`
- `EF:94E3..EF:9502` (`31` bytes, SHA-1 `9b12e0cecc8e13a1f3f49f462928cc22a595a86b`) `EBattle9MsgFmonHieroglyphB`
- `EF:9502..EF:952E` (`44` bytes, SHA-1 `c08e46e25732d2e11186f5502c6a88b877690c75`) `EBattle9MsgFmonBossGrave`
- `EF:952E..EF:95A3` (`117` bytes, SHA-1 `14df05fbff9167b7233af8d918b7c231cc2959fc`) `EBattle9MsgGrfdPola`
- `EF:95A3..EF:96D3` (`304` bytes, SHA-1 `6ea08a2240fdabe884c3ebf7b0dc1dbc4b42e0f4`) `EBattle9BranchGrfdPolaTmp`
- `EF:96D3..EF:970F` (`60` bytes, SHA-1 `30a952fc63655186cc26b4ff26b0a03d3375b0e6`) `EBattle9BranchGrfdPolaItemfull`
- `EF:970F..EF:9737` (`40` bytes, SHA-1 `ea0e9d939eadfa78e0248849e59830af373c4c98`) `EBattle9BranchGrfdPola1`
- `EF:9737..EF:976B` (`52` bytes, SHA-1 `89db592d733f389422caf3a29c029fc9bfb782ec`) `EBattle9BranchGrfdPolaLater`
- `EF:976B..EF:9785` (`26` bytes, SHA-1 `805a459f38b1e7fe7dce3a79fa1dba509f243c23`) `EBattle9BranchGrfdPolaLaterYes`
- `EF:9785..EF:97A2` (`29` bytes, SHA-1 `b6f2027ae4e5933a540807f6e1ae5035321d4134`) `EBattle9MsgGrfdSignpostA`
- `EF:97A2..EF:981C` (`122` bytes, SHA-1 `7154f507558fb405c979067d55d4c5a5ade1fe54`) `EBattle9MsgGrfdLlptBoss`
- `EF:981C..EF:9822` (`6` bytes, SHA-1 `63a71570d82e222296584eb406e25b15c69faea6`) `EBattle9MsgGrfdKinokoGirl`
- `EF:9822..EF:9857` (`53` bytes, SHA-1 `0ae3548be10c4e96fb62bd2fb0ea5997ecf873e8`) `EBattle9MsgGrfdShintoA`
- `EF:9857..EF:98AD` (`86` bytes, SHA-1 `1eb1a3ae22b8b1aa17805372eda1416ab472947c`) `EBattle9MsgGrfdSysmsgGuts`
- `EF:98AD..EF:98D3` (`38` bytes, SHA-1 `6c7bc6e5ca266f2258abd0f1f35f7a24a7530c5f`) `EBattle9BranchGrfdSysmsgGutsNo`
- `EF:98D3..EF:9A47` (`372` bytes, SHA-1 `6a0319d43accf6cea67e3862755fd7426b532ebc`) `EBattle9BranchGrfdSysmsgGutsYes`
- `EF:9A47..EF:9A5E` (`23` bytes, SHA-1 `7fe8f42c7c345fdfcea3f55550c80633365e5a15`) `EBattle1MsgBtlNakama0`
- `EF:9A5E..EF:9A7E` (`32` bytes, SHA-1 `6694a9b335a04365eb5aa8098f32cd0c28d66dd7`) `EBattle1MsgBtlTanemaki0`
- `EF:9A7E..EF:9A9E` (`32` bytes, SHA-1 `9a5428ade7470f09753d284f96e51504db9c376d`) `EBattle1MsgBtlExplosion`
- `EF:9A9E..EF:9ABB` (`29` bytes, SHA-1 `8c79314e616171db1ba717a09283e86594aec79a`) `EBattle1MsgBtlBurn`
- `EF:9ABB..EF:9AE8` (`45` bytes, SHA-1 `c722f88a4a989c9637522e8b2a3d17529e1948cd`) `EBattle1MsgBtlGoods`
- `EF:9AE8..EF:9B02` (`26` bytes, SHA-1 `94a69dc8ea08bb7bf36d4b4a931976282328c727`) `EBattle1BranchBtlGoodsFailed`
- `EF:9B02..EF:9B20` (`30` bytes, SHA-1 `9d9b6d9c2684d81f5e58d8254948dbabe3ae5621`) `EBattle1MsgBtlTimestop`
- `EF:9B20..EF:9B43` (`35` bytes, SHA-1 `0aed63df96b0077e8dad772a85bf7fd38c2fe8fa`) `EBattle1MsgBtlManazashi`
- `EF:9B43..EF:9B73` (`48` bytes, SHA-1 `2472974b8f9e2fd98dbd7bbbd4e2f7fd529f0eb1`) `EBattle1MsgBtlKaidenpa`
- `EF:9B73..EF:9B96` (`35` bytes, SHA-1 `4c85a69637c49f35bdb855400ee38b4b4e978b17`) `EBattle1MsgBtlYoroKaidenpa`
- `EF:9B96..EF:9BC3` (`45` bytes, SHA-1 `ceee98d6c167ddd47b7470fef837fb167aa986f5`) `EBattle1MsgBtlGeppuIki`
- `EF:9BC3..EF:9BE6` (`35` bytes, SHA-1 `daa0033fc10a78ef6777cd0cf6a22d750b0ac2f5`) `EBattle1MsgBtlDokubari`
- `EF:9BE6..EF:9C02` (`28` bytes, SHA-1 `c24516dfae2433534c5e8302bc919a7073393b77`) `EBattle1MsgBtlDeathKiss`
- `EF:9C02..EF:9C30` (`46` bytes, SHA-1 `8f13ee7b6bff533f1869ac782e0754c8e7dfd859`) `EBattle1MsgBtlTumetaiIki`
- `EF:9C30..EF:9C51` (`33` bytes, SHA-1 `4d7482ad028bc7753889aad44fc4c0f4e7cf5906`) `EBattle1MsgBtlHoushi`
- `EF:9C51..EF:9C7E` (`45` bytes, SHA-1 `5c5ae37d604b20ca7d6052bc3410d12e65c4ac99`) `EBattle1MsgBtlTorituki`
- `EF:9C7E..EF:9CAD` (`47` bytes, SHA-1 `d5cafc61a45adef93bc56554c26fc1e80b4a2577`) `EBattle1MsgBtlYoiKaori`
- `EF:9CAD..EF:9CD1` (`36` bytes, SHA-1 `7cc73f6604b6c2623532742c45eb6b8cfebf878c`) `EBattle1MsgBtlKabiHousi`
- `EF:9CD1..EF:9CF1` (`32` bytes, SHA-1 `88d4c30ffa9e11278a24af9ad87470877f24d8e9`) `EBattle1MsgBtlShibari`
- `EF:9CF1..EF:9D14` (`35` bytes, SHA-1 `37ffb8a2fac5906083a9bacb8c13b97ef7e5dae0`) `EBattle1MsgBtlNeneki`
- `EF:9D14..EF:9D3E` (`42` bytes, SHA-1 `8ff51ebb6e98575faa74c86033bf59eaf623b40a`) `EBattle1MsgBtlHaemitu`
- `EF:9D3E..EF:9D62` (`36` bytes, SHA-1 `ea59178d860f252b7da70ffb5d9f12f2ab0fa540`) `EBattle1MsgBtlOshiriIto`
- `EF:9D62..EF:9D81` (`31` bytes, SHA-1 `d774995c70bc4289b6e3f63ebcc0c137d9f97f7d`) `EBattle1MsgBtlKowaiKotoba`
- `EF:9D81..EF:9DA1` (`32` bytes, SHA-1 `c0580c0112d4f9d9faa4300202a78339cd46331c`) `EBattle1MsgBtlAyashiKoto`
- `EF:9DA1..EF:9DBD` (`28` bytes, SHA-1 `cea81260269969217b4d542b8f841cfe155cf986`) `EBattle1MsgBtlFuuin`
- `EF:9DBD..EF:9DDA` (`29` bytes, SHA-1 `53d8d20887b69388012b92bb30b0f3e2f9319e93`) `EBattle1MsgBtlTachibaThink`
- `EF:9DDA..EF:9E05` (`43` bytes, SHA-1 `88c576ad7d6763a1ef94ce9a0f40a32f88dcfad1`) `EBattle1MsgBtlKogeppuIki`
- `EF:9E05..EF:9E22` (`29` bytes, SHA-1 `0fac325e4c81396bbc36ed9cfef32afe93a07f05`) `EBattle1MsgBtlTyphoon`
- `EF:9E22..EF:9E47` (`37` bytes, SHA-1 `0af8075d8d380fcd1919ab78c0a2788e65e9eba5`) `EBattle1MsgBtlCoffee`
- `EF:9E47..EF:9E69` (`34` bytes, SHA-1 `a44e10fe8085e7b4a3c995ef7fc3182a391e807e`) `EBattle1MsgBtlMusic`
- `EF:9E69..EF:9E92` (`41` bytes, SHA-1 `f51bb224643d0f2e5e3106b0b13499bac6ea1d88`) `EBattle1MsgBtlSyoukaEki`
- `EF:9E92..EF:9EB4` (`34` bytes, SHA-1 `dfd4284c849c8695219a6beb4c0c3ff37eb2fb20`) `EBattle1MsgBtlKaminari`
- `EF:9EB4..EF:9ED7` (`35` bytes, SHA-1 `8958f89db69495bad9bb558817ebaa0b1523be82`) `EBattle1MsgBtlFire`
- `EF:9ED7..EF:9EF4` (`29` bytes, SHA-1 `bb9edb85dd80363a4f4d86a1b13a26bc8d15d907`) `EBattle1MsgBtlFireBreath`
- `EF:9EF4..EF:9F9F` (`171` bytes, SHA-1 `be821dbacac76baa97aa4e8d8488f2b99b4e77de`) `EGoods2MsgBtlEscapeMouse`
- `EF:9F9F..EF:9FE2` (`67` bytes, SHA-1 `dcbcc6b6beff39146c2e1f297fb6a8e0e83ad448`) `EGoods2BranchMouseNotDungeon`
- `EF:9FE2..EF:A002` (`32` bytes, SHA-1 `3db4c29e585499780330bef22379d31d89603065`) `EGoods2BranchMouseCantUse`
- `EF:A002..EF:A029` (`39` bytes, SHA-1 `8f8b62322c41a5a7bb48fbbc1b46d884c5152585`) `EGoods2BranchBtlEscapeMousePizza`
- `EF:A029..EF:A07E` (`85` bytes, SHA-1 `b13b27c6d6981e5e59c0c21d658773e98deb4c15`) `EGoods2BranchBtlEscapeMouseKanban`
- `EF:A07E..EF:A0B7` (`57` bytes, SHA-1 `fc37b4cf034a1a3e5ecb49b2e6c3588d3ef6f7bb`) `EGoods2BranchBtlEscapeMouseEscargo`
- `EF:A0B7..EF:A0DC` (`37` bytes, SHA-1 `ac7c3cc18de03208637026da1d7ab93a06712587`) `EGoods2BranchBtlEscapeMouseCapsule`
- `EF:A0DC..EF:A2AB` (`463` bytes, SHA-1 `9e8e54461ae0b2afd11003fbe9c93773dea4132d`) `EGoods2MsgBtlHiero`
- `EF:A2AB..EF:A2B5` (`10` bytes, SHA-1 `746cccf13625d978840dc86f11e0d9e156bcc4ca`) `EGoods2MsgBtlTownMap`
- `EF:A2B5..EF:A2C9` (`20` bytes, SHA-1 `d24354573cfc8d5171e55c57d2ba2d907deaa66f`) `EGoods2BranchTownMapNg`
- `EF:A2C9..EF:A2D5` (`12` bytes, SHA-1 `16da9d264bfec7f719429a66fd991ce23355990e`) `EGoods2MsgOnetTabigoya`
- `EF:A2D5..EF:A2D6` (`1` bytes, SHA-1 `c4ea21bb365bbeeaf5f2c654883e56d11e43c44e`) `EGoods2BranchOnetTabigoyaEnd`
- `EF:A2D6..EF:A2FA` (`36` bytes, SHA-1 `8c143343e807a77d4db7ab725345d2cca0ad491a`) `EGoods2MsgOnetTabigoyaReceive`
- `EF:A2FA..EF:A37A` (`128` bytes, SHA-1 `f6451930cdd148157b9d721702cd030ed42c8315`) `TextUnknownEfa2faMonsterOffEventPayload`
- `EF:A37A..EF:A3B6` (`60` bytes, SHA-1 `10c466fda240e424b349d311bf6fd86c31be27a0`) `CommandWindowText`
- `EF:A3B6..EF:A459` (`163` bytes, SHA-1 `c2a8a80c125f8f3ec4e8cdc13da0b68ba59bab19`) `StatusWindowText`
- `EF:A459..EF:A460` (`7` bytes, SHA-1 `98b234d1e6c672086af5bec751ccf2b653822503`) `StatusWindowUnknownOpenTail`
- `EF:A460..EF:A4E3` (`131` bytes, SHA-1 `b30ef3e0f03bfaecbfe7796865d70aea0de84269`) `NameInputWindowSelectionLayout0`
- `EF:A4E3..EF:A566` (`131` bytes, SHA-1 `1a8b23bf683b613191e4d0b1cd49fcd10c4d7711`) `NameInputWindowSelectionLayout1`
- `EF:A566..EF:A5E9` (`131` bytes, SHA-1 `b30ef3e0f03bfaecbfe7796865d70aea0de84269`) `NameInputWindowSelectionLayout2`
- `EF:A5E9..EF:A66C` (`131` bytes, SHA-1 `1a8b23bf683b613191e4d0b1cd49fcd10c4d7711`) `NameInputWindowSelectionLayout3`
- `EF:A66C..EF:A6A7` (`59` bytes, SHA-1 `c35b88c957876a9a45f6f30aed6cb3243c8def3d`) `NameInputWindowSelectionLayout4`
- `EF:A6A7..EF:A6EB` (`68` bytes, SHA-1 `7641b11de4780c6b6722df547518253ecdd4f51c`) `NameInputWindowSelectionLayout5`
- `EF:A6EB..EF:A6EC` (`1` bytes, SHA-1 `c4ea21bb365bbeeaf5f2c654883e56d11e43c44e`) `TextUnknown7EndBlockPayload`
- `EF:A6EC..EF:C51B` (`7727` bytes, SHA-1 `c591fb7eb6bc3f65a7c4e467fdf4dbc151ae4eed`) `TextDebugUnknownMenu2`

Labels:

- `EF:4E20 EExplPsiMsgExplPsiHissatsuAlfa`
- `EF:4E38 EExplPsiMsgExplPsiHissatsuBeta`
- `EF:4E51 EExplPsiMsgExplPsiHissatsuGamma`
- `EF:4E6A EExplPsiMsgExplPsiHissatsuOmega`
- `EF:4E83 EExplPsiMsgExplPsiFireAlfa`
- `EF:4E99 EExplPsiMsgExplPsiFireBeta`
- `EF:4EB0 EExplPsiMsgExplPsiFireGamma`
- `EF:4EC7 EExplPsiMsgExplPsiFireOmega`
- `EF:4EDE EExplPsiMsgExplPsiFreezAlfa`
- `EF:4F06 EExplPsiMsgExplPsiFreezBeta`
- `EF:4F2E EExplPsiMsgExplPsiFreezGamma`
- `EF:4F56 EExplPsiMsgExplPsiFreezOmega`
- `EF:4F7E EExplPsiMsgExplPsiThunderAlfa`
- `EF:4FA6 EExplPsiMsgExplPsiThunderBeta`
- `EF:4FDC EExplPsiMsgExplPsiThunderGamma`
- `EF:5013 EExplPsiMsgExplPsiThunderOmega`
- `EF:5049 EExplPsiMsgExplPsiFlashAlfa`
- `EF:506B EExplPsiMsgExplPsiFlashBeta`
- `EF:50AF EExplPsiMsgExplPsiFlashGamma`
- `EF:50E1 EExplPsiMsgExplPsiFlashOmega`
- `EF:5131 EExplPsiMsgExplPsiStarstomAlfa`
- `EF:5152 EExplPsiMsgExplPsiStarstormOmega`
- `EF:5173 EExplPsiMsgExplPsiLifeupAlfa`
- `EF:5189 EExplPsiMsgExplPsiLifeupBeta`
- `EF:519F EExplPsiMsgExplPsiLifeupGamma`
- `EF:51BB EExplPsiMsgExplPsiLifeupOmega`
- `EF:51CF EExplPsiMsgExplPsiHealingAlfa`
- `EF:51F0 EExplPsiMsgExplPsiHealingBeta`
- `EF:5239 EExplPsiMsgExplPsiHealingGamma`
- `EF:52A5 EExplPsiMsgExplPsiHealingOmega`
- `EF:5301 EExplPsiMsgExplPsiShieldAlfa`
- `EF:5361 EExplPsiMsgExplPsiShieldSigma`
- `EF:53C0 EExplPsiMsgExplPsiShieldBeta`
- `EF:5428 EExplPsiMsgExplPsiShieldOmega`
- `EF:548F EExplPsiMsgExplPsiPShieldAlfa`
- `EF:54E6 EExplPsiMsgExplPsiPShieldSigma`
- `EF:553C EExplPsiMsgExplPsiPShieldBeta`
- `EF:55A0 EExplPsiMsgExplPsiPShieldOmega`
- `EF:5603 EExplPsiMsgExplPsiOffenseUpAlfa`
- `EF:562E EExplPsiMsgExplPsiOffenseUpOmega`
- `EF:5658 EExplPsiMsgExplPsiDefenseDownAlfa`
- `EF:5687 EExplPsiMsgExplPsiDefenseDownOmega`
- `EF:56B9 EExplPsiMsgExplPsiSaiminAlfa`
- `EF:56D0 EExplPsiMsgExplPsiSaiminOmega`
- `EF:56EB EExplPsiMsgExplPsiPMagnetAlfa`
- `EF:5712 EExplPsiMsgExplPsiPMagnetOmega`
- `EF:5739 EExplPsiMsgExplPsiParalysisAlfa`
- `EF:574E EExplPsiMsgExplPsiParalysisOmega`
- `EF:5766 EExplPsiMsgExplPsiBrainShockAlfa`
- `EF:5777 EExplPsiMsgExplPsiBrainShockOmega`
- `EF:578B EExplPsiMsgExplPsiTeleportAlfa`
- `EF:57AE EExplPsiMsgExplPsiTeleportBeta`
- `EF:57EB E16DkfdMsgDkfdFireBoss`
- `EF:5864 E16DkfdMsgDkfdDosei`
- `EF:58C7 E16DkfdMsgDkfdSkywalker`
- `EF:5917 E16DkfdMsgDkfdOldman`
- `EF:5A3E E16DkfdMsgDkfdGumiA`
- `EF:5A81 E16DkfdBranchDkfdGumiAEnd`
- `EF:5AB5 E16DkfdMsgDkfdGumiAReceive`
- `EF:5AED E16DkfdMsgDkfdGumiBoss`
- `EF:5B97 E16DkfdBranchDkfdGumiBossAfter`
- `EF:5BC8 E16DkfdBranchDkfdGumiBossEnd`
- `EF:5BE6 E16DkfdMsgDkfdGumiC`
- `EF:5C46 E16DkfdBranchDkfdGumiCEnd`
- `EF:5C98 E16DkfdMsgDkfdGumiD`
- `EF:5CE4 E16DkfdBranchDkfdGumiDEnd`
- `EF:5D16 E16DkfdMsgDkfdGumiE`
- `EF:5DF8 E16DkfdBranchDkfdGumiEB`
- `EF:5E94 E16DkfdMsgDkfdGumiF`
- `EF:5F31 E16DkfdBranchDkfdGumiFEnd`
- `EF:5F7D E16DkfdMsgDkfdGumiG`
- `EF:5FDF E16DkfdMsgDkfdGumiH`
- `EF:6038 E16DkfdBranchDkfdGumiHEnd`
- `EF:6049 E16DkfdMsgDkfdGumiI`
- `EF:604F E16DkfdMsgDkfdGumiK`
- `EF:6084 E16DkfdMsgDkfdGumiL`
- `EF:60C5 E16DkfdBranchDkfdGumiLEnd`
- `EF:60F2 E16DkfdMsgDkfdBirdPhone`
- `EF:610C E16DkfdMsgDkfdGumiDoorReceive`
- `EF:610D E16DkfdMsgReadDkfdGumi1`
- `EF:6132 E16DkfdMsgReadDkfdGumi2`
- `EF:6157 E16DkfdMsgReadDkfdGumi3`
- `EF:617B E07GpftMsgGpftMinigeppuA`
- `EF:61CB E07GpftBranchGpftMinigeppuANo`
- `EF:61F3 E07GpftBranchGpftMinigeppuAYesno`
- `EF:6247 E07GpftBranchGpftMinigeppuAYes`
- `EF:6276 E07GpftMsgGpftMinigeppuB`
- `EF:62B1 E07GpftMsgGpftMinigeppuC`
- `EF:62F5 E07GpftMsgGpftMinigeppuD`
- `EF:63B5 E07GpftMsgGpftMinigeppuE`
- `EF:6400 E07GpftMsgGpftDoseiA`
- `EF:6419 E07GpftMsgGpftDoseiB`
- `EF:6446 E07GpftMsgGpftGeppu`
- `EF:6569 E07GpftBranchGpftGeppuMain`
- `EF:66CA E07GpftBranchGpftGeppuDead`
- `EF:679A E07GpftMsgGpftMlkyBoss`
- `EF:6814 E07GpftMsgGpftHakamori`
- `EF:681A E07GpftMsgThrkBossGrave`
- `EF:6874 E07GpftBranchThrkBossGraveHave`
- `EF:68D7 E07GpftMsgThrkBossGraveDie`
- `EF:6954 E07GpftBranchThrkBossGraveDieHave`
- `EF:69A1 EBattle5MsgBtlHpMaxRecovered`
- `EF:69BA EBattle5MsgBtlHpRecoveredAmount`
- `EF:69D2 EBattle5MsgBtlPpRecoveredAmount`
- `EF:69EA EBattle5MsgBtlCheckOffenseAmount`
- `EF:69FF EBattle5MsgBtlCheckDefenseAmount`
- `EF:6A0D EBattle5MsgBtlCheckAntiFire`
- `EF:6A24 EBattle5MsgBtlCheckAntiFreeze`
- `EF:6A3C EBattle5MsgBtlCheckAntiFlash`
- `EF:6A54 EBattle5MsgBtlCheckAntiParalysis`
- `EF:6A6C EBattle5MsgBtlCheckBrainLevel0`
- `EF:6A7F EBattle5MsgBtlCheckBrainLevel3`
- `EF:6A99 EBattle5MsgBtlMetamorphoseOk`
- `EF:6AB3 EBattle5MsgBtlMetamorphoseFailed`
- `EF:6AC7 EBattle5MsgBtlDiamondized`
- `EF:6AE0 EBattle5MsgBtlParalysisInflicted`
- `EF:6AFB EBattle5MsgBtlFeelingSickInflicted`
- `EF:6B18 EBattle5MsgBtlPoisonInflicted`
- `EF:6B2F EBattle5MsgBtlColdInflicted`
- `EF:6B43 EBattle5ObjectPronounSubtext`
- `EF:6B81 EBattle5MsgBtlMushroomizedInflicted`
- `EF:6B98 EBattle5MsgBtlPossessedInflicted`
- `EF:6BBB EBattle5MsgBtlCryingInflicted`
- `EF:6BD3 EBattle5MsgBtlImmobilizedInflicted`
- `EF:6BEF EBattle5MsgBtlSolidificationInflicted`
- `EF:6C0B EBattle5MsgBtlPsiSealInflicted`
- `EF:6C3A EBattle5MsgBtlStrangeInflicted`
- `EF:6C55 EBattle5MsgBtlAsleepInflicted`
- `EF:6C6B EBattle5MsgBtlIncapacitated`
- `EF:6C84 EBattle5MsgSysNpcDeadFlyingMan`
- `EF:6CC7 EBattle5FlyingManDeadBranchB`
- `EF:6CD0 EBattle5FlyingManDeadBranchC`
- `EF:6CD9 EBattle5FlyingManDeadBranchD`
- `EF:6CE2 EBattle5FlyingManDeadBranchE`
- `EF:6CEB EBattle5FlyingManRemovePartyMemberHelper`
- `EF:6CFC EBattle5FlyingManRemoveBranch2`
- `EF:6D0A EBattle5FlyingManRemoveBranch3`
- `EF:6D18 EBattle5FlyingManRemoveBranch4`
- `EF:6D26 EBattle5FlyingManRemoveBranch5`
- `EF:6D2A EBattle5MsgSysNpcDeadTeddyBear`
- `EF:6D4C EBattle5MsgSysNpcDeadSuperPlushBear`
- `EF:6D71 EBattle5MsgBtlEnemyDefeated`
- `EF:6D83 EBattle5MsgBtlEnemyStoppedMoving`
- `EF:6D96 EBattle5MsgBtlEnemyBecameTame`
- `EF:6DA7 EBattle5MsgBtlEnemyDisappeared`
- `EF:6DB8 EBattle5MsgBtlEnemyMeltedAway`
- `EF:6DD8 EBattle5MsgBtlEnemyBrokeIntoPieces`
- `EF:6DF0 EBattle5MsgBtlEnemyDestroyed`
- `EF:6E03 EBattle5MsgBtlEnemyScrapped`
- `EF:6E19 EBattle5MsgBtlEnemyReturnedToNormal`
- `EF:6E31 EBattle5MsgBtlEnemyReturnedToDust`
- `EF:6E4A EBattle5MsgBtlDiamondizedRecovered`
- `EF:6E67 EBattle5MsgBtlParalysisRecovered`
- `EF:6E81 EBattle5MsgBtlFeelingSickRecovered`
- `EF:6E97 EBattle5MsgBtlPoisonRemoved`
- `EF:6EBC EBattle5MsgBtlColdRecovered`
- `EF:6ED1 EBattle5MsgBtlCryingRecovered`
- `EF:6EED EBattle5MsgBtlImmobilizedRecovered`
- `EF:6F0B EBattle5MsgBtlFrozenCanMove`
- `EF:6F1E EBattle5MsgBtlStrangeRecovered`
- `EF:6F38 EBattle5MsgBtlSunstrokeCured`
- `EF:6F54 EBattle5MsgBtlAsleepRecovered`
- `EF:6F64 EBattle5MsgBtlPsiSealRecovered`
- `EF:6F7C EBattle5MsgBtlRevived`
- `EF:6F8E EBattle5MsgBtlReviveFailed`
- `EF:6F9A EBattle5MsgBtlShieldInstalled`
- `EF:6FBD EBattle5MsgBtlShieldStrengthened`
- `EF:6FD3 EBattle5MsgBtlPowerShieldInstalled`
- `EF:6FF4 EBattle5MsgBtlPowerShieldStrengthened`
- `EF:700C EBattle5MsgBtlPsychicShieldInstalled`
- `EF:7032 EBattle5MsgBtlPsychicShieldStrengthened`
- `EF:7050 EBattle5MsgBtlPsychicPowerShieldInstalled`
- `EF:707A EBattle5MsgBtlPsychicPowerShieldStrengthened`
- `EF:7099 EBattle5MsgBtlShieldExpired`
- `EF:70B1 EBattle5MsgBtlPowerShieldReflectsAttack`
- `EF:70D2 EBattle5MsgBtlPsychicPowerShieldReflectsPsiName`
- `EF:70FA EBattle5MsgBtlPsychicShieldNullifiesPsiName`
- `EF:7123 EBattle5MsgBtlNeutralizeResult`
- `EF:7142 EBattle5MsgBtlNeutralizeMetamorph`
- `EF:7160 EBattle5MsgBtlFranklinBadgeReflectsThunder`
- `EF:7186 EBattle4MsgBtlDiamondizedCannotMove`
- `EF:7192 EBattle4MsgBtlParalysisCannotMove`
- `EF:71B4 EBattle4MsgBtlNauseaCannotMove`
- `EF:71CC EBattle4MsgBtlPoisonStatus`
- `EF:71DF EBattle4MsgBtlAsleepStatus`
- `EF:71F6 EBattle4MsgBtlImmobilizedStatus`
- `EF:720C EBattle4MsgBtlPsiSealStatus`
- `EF:721E EBattle4PsiSealPlayerSideSoundBranch`
- `EF:7221 EBattle4PsiSealResultText`
- `EF:7249 EBattle4MsgBtlGuardOn`
- `EF:725A EBattle4MsgBtlFlyHoneyMindLost`
- `EF:727F EBattle4MsgBtlHomesickRandom`
- `EF:72A0 EBattle4MsgBtlHomesickThoughtMom`
- `EF:72B9 EBattle4MsgBtlHomesickCravingFood`
- `EF:72DB EBattle4MsgBtlHomesickLostMotivation`
- `EF:72F6 EBattle4MsgBtlRunawayFiveBreakIn`
- `EF:72F7 EBattle4MsgBtlRunawayFiveBreakInFailed`
- `EF:733D EBattle4MsgBtlRunawayFiveBreakInSucceeded`
- `EF:7415 EBattle4MsgBtlPooBreakIn`
- `EF:743B EBattle4MsgBtlPooStarstormReveal`
- `EF:745F EBattle4MsgBtlPokeyTalkRandom`
- `EF:749D EBattle4MsgBtlPokeyPlayedDead`
- `EF:74B0 EBattle4MsgBtlPokeyPretendedCry`
- `EF:74C9 EBattle4MsgBtlPokeyApologized`
- `EF:74E6 EBattle4MsgBtlPokeyThoughtToSelf`
- `EF:74FA EBattle4MsgBtlPokeyActedInnocent`
- `EF:7514 EBattle4MsgBtlPokeySmiledSincerely`
- `EF:7530 EBattle4MsgBtlPokeyComplained`
- `EF:7548 EBattle4MsgBtlPokeyEdgedCloser`
- `EF:7569 EBattle4MsgBtlMyDogHowling`
- `EF:7579 EBattle4MsgBtlPickeyTalk`
- `EF:7591 EBattle4MsgBtlTonyTalk`
- `EF:7593 EBattle4MsgBtlBalmonTalk`
- `EF:75AB EBattle4MsgBtlDamageAmount`
- `EF:75C2 EBattle4MsgBtlMortalDamageAmount`
- `EF:75D9 EBattle4MsgBtlSmashDamageAmount`
- `EF:75F0 EBattle4MsgBtlMortalSmashDamageAmount`
- `EF:7607 EBattle4MsgBtlDamageToDeathAmount`
- `EF:7624 EBattle4MsgBtlSmashPlayer`
- `EF:7630 EBattle4MsgBtlSmashMonster`
- `EF:763C EBattle4MsgBtlShootDodged`
- `EF:7655 EBattle4MsgBtlBashDodged`
- `EF:766E EBattle4MsgBtlStatusNoEffect`
- `EF:7682 EBattle4AdjacentNoEffectText`
- `EF:7696 EBattle4MsgBtlNoVisibleEffect`
- `EF:76B3 EBattle4MsgBtlNoEffectVariantC`
- `EF:76C7 EBattle4MsgBtlMissPhysical`
- `EF:76D8 EBattle4MsgBtlMissShoot`
- `EF:76FD EBattle4MsgBtlTargetNotExist`
- `EF:7710 EBattle4MsgBtlHpSuckSelfDrain`
- `EF:7729 EBattle4MsgBtlHpSuckAmount`
- `EF:773F EBattle4MsgBtlPpDrainAmount`
- `EF:7755 EBattle4MsgBtlPpDrainTarget`
- `EF:7768 EBattle4MsgBtlStrangeDamage`
- `EF:7787 EBattle4MsgBtlPoisonDamage`
- `EF:77B1 EBattle4MsgBtlSunstrokeDamage`
- `EF:77DB EBattle4MsgBtlColdDamage`
- `EF:77FD EBattle8MsgBtlCallForHelpEnemyJoined`
- `EF:7810 EBattle8MsgBtlCallForHelpSeedSprouted`
- `EF:7824 EBattle8MsgBtlCallForHelpNoOneCame`
- `EF:7830 EBattle8MsgBtlCallForHelpSeedNoSprout`
- `EF:7843 EBattle8MsgBtlTimeStopReturn`
- `EF:7858 EBattle8MsgBtlAppearAttacked`
- `EF:7866 EBattle8MsgBtlAppearBlockedWay`
- `EF:7879 EBattle8MsgBtlAppearCameAfterYou`
- `EF:788B EBattle8MsgBtlAppearTrappedYou`
- `EF:789C EBattle8MsgBtlFinalEncounter4`
- `EF:78AB EBattle8MsgBtlFinalEncounter5`
- `EF:78B8 EBattle8MsgBtlFinalEncounter6`
- `EF:78C7 EBattle8MsgBtlFinalEncounter7`
- `EF:78D8 EBattle8MsgBtlSurpriseOpeningPlayer`
- `EF:78F7 EBattle8MsgBtlSurpriseOpeningMonster`
- `EF:790B EBattle8GroupActorOpeningHelper`
- `EF:792B EBattle8GroupActorOpeningSingular`
- `EF:792E EBattle8GroupActorOpeningCohort`
- `EF:793C EBattle8GroupActorOpeningCohorts`
- `EF:794B EBattle8GroupActorFinalHelper`
- `EF:796C EBattle8GroupActorFinalSingular`
- `EF:7970 EBattle8GroupActorFinalCohort`
- `EF:797F EBattle8GroupActorFinalCohorts`
- `EF:798F EBattle8GroupActorSurpriseHelper`
- `EF:79B1 EBattle8GroupActorPossessiveSingular`
- `EF:79B6 EBattle8GroupActorPossessiveCohort`
- `EF:79C6 EBattle8GroupActorPossessiveCohorts`
- `EF:79D7 EBattle8MsgBtlPlayerWin`
- `EF:79E6 EBattle8PlayerWinEventBranch`
- `EF:79EF EBattle8PlayerWinExperienceText`
- `EF:7A0A EBattle8PlayerWinHomesickBranch`
- `EF:7A14 EBattle8MsgBtlPlayerWinBoss`
- `EF:7A28 EBattle8MsgBtlPlayerWinForce`
- `EF:7A4D EBattle8MsgBtlMonsterWin`
- `EF:7A66 EBattle8MsgBtlLevelUp`
- `EF:7A7D EBattle8MsgBtlLevelOffenseUp`
- `EF:7A97 EBattle8MsgBtlLevelDefenseUp`
- `EF:7AB1 EBattle8MsgBtlLevelSpeedUp`
- `EF:7AC9 EBattle8MsgBtlLevelGutsUp`
- `EF:7AE0 EBattle8MsgBtlLevelVitalityUp`
- `EF:7AFB EBattle8MsgBtlLevelIqUp`
- `EF:7B11 EBattle8MsgBtlLevelLuckUp`
- `EF:7B28 EBattle8MsgBtlLevelMaxHpUp`
- `EF:7B46 EBattle8MsgBtlLevelMaxPpUp`
- `EF:7B64 EBattle8MsgBtlLearnPsi`
- `EF:7B77 EBattle8ByteSubstitutionPsiNameText`
- `EF:7B83 EBattle8PointerSubstitutionIntroState`
- `EF:7B85 EBattle8PointerSubstitutionSweetBranch`
- `EF:7BA0 EBattle8PointerSubstitutionBranch2State`
- `EF:7BA2 EBattle8PointerSubstitutionTearsBranch`
- `EF:7BBF EBattle8PointerSubstitutionBranch3State`
- `EF:7BC1 EBattle8PointerSubstitutionOhBabyBranch`
- `EF:7BDF EBattle8MsgBtlPresentByteSubstitution`
- `EF:7C42 EBattle8PresentRecipientDeadText`
- `EF:7C73 EBattle8PresentInventoryFullText`
- `EF:7C89 EBattle8PresentThrowAwayPrompt`
- `EF:7CB4 EBattle8PresentAbandonPrompt`
- `EF:7CED EBattle8PresentAbandonRetryText`
- `EF:7CF8 EBattle8PresentAbandonConfirmedText`
- `EF:7D0F EBattle8PresentDropSelectionPrompt`
- `EF:7D83 EBattle8PresentDropConfirmedText`
- `EF:7DBE EBattle8PresentDropForbiddenText`
- `EF:7DD5 EBattle8MsgBtlCheckPresentGetByteSubstitution`
- `EF:7E25 EBattle2MsgBtlPpDown`
- `EF:7E3E EBattle2MsgBtlOkoru`
- `EF:7E55 EBattle2MsgBtlKitanaiKotoba`
- `EF:7E70 EBattle2MsgBtlSuibun`
- `EF:7E88 EBattle2MsgBtlEnergy`
- `EF:7EAC EBattle2MsgBtlDokuKamituki`
- `EF:7ED5 EBattle2MsgBtlYoroMissile`
- `EF:7F02 EBattle2MsgBtlMultiAttack`
- `EF:7F1E EBattle2MsgBtlMigamae`
- `EF:7F32 EBattle2MsgBtlFireball`
- `EF:7F5A EBattle2MsgBtlGekitotu`
- `EF:7F7B EBattle2MsgBtlKarate`
- `EF:7F9A EBattle2MsgBtlTomoe`
- `EF:7FC3 EBattle2MsgBtlBousou`
- `EF:7FE0 EBattle2MsgBtlKnife`
- `EF:7FFC EBattle2MsgBtlTossin`
- `EF:8010 EBattle2MsgBtlKamituki`
- `EF:8026 EBattle2MsgBtlHikkaki`
- `EF:804B EBattle2MsgBtlSippo`
- `EF:806D EBattle2MsgBtlNoshikakari`
- `EF:808D EBattle2MsgBtlKamibukuro`
- `EF:80AC EBattle2MsgBtlKonbou`
- `EF:80C4 EBattle2MsgBtlTatumaki`
- `EF:80E4 EBattle2MsgBtlWater`
- `EF:8109 EBattle2MsgBtlFutekiSmile`
- `EF:812B EBattle2MsgBtlLoudSmile`
- `EF:814F EBattle2MsgBtlNijiriyoru`
- `EF:8167 EBattle2MsgBtlTubuyaki1`
- `EF:8186 EBattle2MsgBtlTubuyaki2`
- `EF:81A5 EBattle2MsgBtlTubuyaki3`
- `EF:81C4 EBattle2MsgBtlKorobu`
- `EF:81D7 EBattle2MsgBtlBootto`
- `EF:81F1 EBattle2MsgBtlJyouki`
- `EF:8211 EBattle2MsgBtlYoroyoro`
- `EF:8226 EBattle2MsgBtlFurafura`
- `EF:8239 EBattle2MsgBtlNitanita`
- `EF:825C EBattle2MsgBtlKokyuu`
- `EF:8281 EBattle2MsgBtlAisatu`
- `EF:8299 EBattle2MsgBtlUnari`
- `EF:82BC EBattle2MsgBtlKachikachi`
- `EF:82D7 EBattle2MsgBtlMabusiiHikari`
- `EF:82F7 EBattle2MsgBtlBiribiri`
- `EF:8317 EBattle2MsgBtlKafun`
- `EF:833E EBattle2MsgBtlColdHand`
- `EF:835C EBattle2MsgBtlPoisonBreath`
- `EF:838A EBattle2MsgBtlHaikiGas`
- `EF:83A8 EBattle2MsgBtlLaughHen`
- `EF:83CA EBattle2MsgBtlFue`
- `EF:83ED EBattle2MsgBtlJumpToFace`
- `EF:8413 EBattle2MsgBtlChouOnpa`
- `EF:843F EBattle0MsgAtStartAsleep`
- `EF:8444 EBattle0MsgAtStartPsiSeal`
- `EF:8445 EBattle0MsgAtStartStrange`
- `EF:845D EBattle0MsgRandomActStrange`
- `EF:8477 EBattle0MsgRandomActMushroom`
- `EF:848C EBattle1MsgBtlAttack`
- `EF:84A7 EBattle1AttackPlayerSideBranch`
- `EF:84B6 EBattle1MsgBtlShoot`
- `EF:84C6 EBattle1MsgBtlGuard`
- `EF:84D4 EBattle1MsgBtlMetamorphose`
- `EF:84F3 EBattle1MsgBtlPlayerFlee`
- `EF:8511 EBattle1MsgBtlPlayerFleeFailed`
- `EF:8530 EBattle1MsgBtlCheck`
- `EF:8543 EBattle1MsgBtlPsi`
- `EF:8568 EBattle1PsiPlayerSideBranch`
- `EF:857E EBattle1PsiAnimationDispatch`
- `EF:864C EBattle1PsiEffectBranch1`
- `EF:866E EBattle1PsiEffectBranch2`
- `EF:8698 EBattle1PsiEffectBranch3`
- `EF:86E2 EBattle1PsiEffectBranch4`
- `EF:874A EBattle1PsiEffectBranch5`
- `EF:875F EBattle1PsiEffectBranch6`
- `EF:8777 EBattle1PsiEffectBranch7`
- `EF:878F EBattle1PsiEffectBranch8`
- `EF:87AC EBattle1PsiEffectBranch9`
- `EF:87C3 EBattle1PsiEffectBranch10`
- `EF:87DA EBattle1PsiEffectBranch11`
- `EF:87F4 EBattle1PsiEffectBranch12`
- `EF:8813 EBattle1PsiEffectBranch13`
- `EF:8814 EBattle1MsgBtlThunderSmall`
- `EF:8823 EBattle1MsgBtlThunderLarge`
- `EF:8837 EBattle1MsgBtlThunderMissSound`
- `EF:883D EBattle1PsiEffectBranch17`
- `EF:8847 EBattle1PsiEffectBranch18`
- `EF:8851 EBattle1PsiEffectBranch19`
- `EF:8868 EBattle1PsiEffectBranch20`
- `EF:8882 EBattle1PsiEffectBranch21`
- `EF:88B8 EBattle1PsiEffectBranch22`
- `EF:88E9 EBattle1PsiEffectBranch23`
- `EF:88EC EBattle1PsiEffectBranch31`
- `EF:88F6 EBattle1PsiEffectBranch32`
- `EF:8900 EBattle1PsiEffectBranch33`
- `EF:890A EBattle1PsiEffectBranch34`
- `EF:8914 EBattle1PsiEffectBranch35`
- `EF:891E EBattle1PsiEffectBranch36`
- `EF:8928 EBattle1PsiEffectBranch37`
- `EF:8932 EBattle1PsiEffectBranch38`
- `EF:893C EBattle1PsiEffectBranch41`
- `EF:894C EBattle1PsiEffectBranch42`
- `EF:895C EBattle1PsiEffectBranch43`
- `EF:896C EBattle1PsiEffectBranch44`
- `EF:897C EBattle1PsiEffectBranch45`
- `EF:898C EBattle1PsiEffectBranch46`
- `EF:899C EBattle1PsiEffectBranch47`
- `EF:89AC EBattle1PsiEffectBranch48`
- `EF:89BC EBattle1PsiEffectBranch49`
- `EF:89CE EBattle1PsiEffectBranch50`
- `EF:89E0 EBattle1MsgBtlPray`
- `EF:89FE EBattle3MsgBtlJihibiki`
- `EF:8A18 EBattle3MsgBtlOsaetsuke`
- `EF:8A33 EBattle3MsgBtlCurseWord`
- `EF:8A52 EBattle3MsgBtlJimi`
- `EF:8A6F EBattle3MsgBtlPenki`
- `EF:8A8C EBattle3MsgBtlNaguriKakari`
- `EF:8AA3 EBattle3MsgBtlClaw`
- `EF:8AC2 EBattle3MsgBtlKuchibashi`
- `EF:8ADD EBattle3MsgBtlTsuno`
- `EF:8AF8 EBattle3MsgBtlPunch`
- `EF:8B11 EBattle3MsgBtlPumpkin`
- `EF:8B2F EBattle3MsgBtlBeam`
- `EF:8B4A EBattle3MsgBtlYari`
- `EF:8B65 EBattle3MsgBtlFumitsuke`
- `EF:8B89 EBattle3MsgBtlFurafuupu`
- `EF:8BA8 EBattle3MsgBtlTaiatari`
- `EF:8BC0 EBattle3MsgBtlSkateboard`
- `EF:8BE8 EBattle3MsgBtlKamitsukiDiamond`
- `EF:8BFB EBattle3MsgBtlKudamaki`
- `EF:8C1D EBattle3MsgBtlSekkyou`
- `EF:8C3A EBattle3MsgBtlShikaritsuke`
- `EF:8C58 EBattle3MsgBtlBadSmell`
- `EF:8C75 EBattle3MsgBtlLoudVoice`
- `EF:8C92 EBattle3MsgBtlOtakebi`
- `EF:8CAC EBattle3MsgBtlFakeDead`
- `EF:8CC7 EBattle3MsgBtlYudan`
- `EF:8CDD EBattle3MsgBtlYudan1`
- `EF:8CFB EBattle3MsgBtlYudan2`
- `EF:8D17 EBattle3MsgBtlYudan3`
- `EF:8D2F EBattle3MsgBtlYudan4`
- `EF:8D4C EBattle3MsgBtlYudanLifeup`
- `EF:8D72 EBattle3MsgBtlNebieBeam`
- `EF:8D9F EBattle3MsgBtlNeutralizeSparkle`
- `EF:8DC1 EBattle3MsgBtlMakitsuki`
- `EF:8DDE EBattle3MsgBtlToDiamondDog`
- `EF:8E27 EBattle3MsgBtlWarpNear`
- `EF:8E3C EBattle3MsgBtlAntipsi`
- `EF:8E5E EBattle3MsgBtlHpsuck`
- `EF:8E7E EBattle3MsgBtlHpsucksp`
- `EF:8E9E EBattle3MsgBtlShieldkill`
- `EF:8EBE EBattle3MsgBtlBadSmellGas`
- `EF:8EE2 EBattle3MsgBtlLightning`
- `EF:8F17 EBattle3MsgBtlLightningB`
- `EF:8F4A EBattle3MsgBtlLightningC`
- `EF:8F91 EBattle3MsgBtlGyiyyig3`
- `EF:8FAD EBattle9SubSorezoreHelper`
- `EF:8FC9 EBattle9BranchSorezoreEnd`
- `EF:8FCB EBattle9MsgFmonMoonA`
- `EF:8FE4 EBattle9MsgFmonMoonB`
- `EF:9003 EBattle9MsgFmonMoonB2`
- `EF:9022 EBattle9MsgFmonMoonC`
- `EF:9041 EBattle9MsgFmonPyraAA`
- `EF:9060 EBattle9MsgFmonPyraAB`
- `EF:907F EBattle9MsgFmonPyraAC`
- `EF:909E EBattle9MsgFmonPyraAD`
- `EF:90BD EBattle9MsgFmonPyraAE`
- `EF:90DC EBattle9MsgFmonPyraAF`
- `EF:90F9 EBattle9MsgFmonPyraAG`
- `EF:9118 EBattle9MsgFmonPyraAH`
- `EF:9137 EBattle9MsgFmonPyraAI`
- `EF:9156 EBattle9MsgFmonPyraAJ`
- `EF:9175 EBattle9MsgFmonPyraAK`
- `EF:9194 EBattle9MsgFmonPyraAL`
- `EF:91B3 EBattle9MsgFmonPyraAM`
- `EF:91D2 EBattle9MsgFmonPyraAN`
- `EF:91F1 EBattle9MsgFmonPyraAO`
- `EF:9210 EBattle9MsgFmonPyraAP`
- `EF:922F EBattle9MsgFmonPyraAQ`
- `EF:924E EBattle9MsgFmonPyraBA`
- `EF:926D EBattle9MsgFmonPyraBB`
- `EF:928C EBattle9MsgFmonPyraBC`
- `EF:92AB EBattle9MsgFmonPyraBD`
- `EF:92CA EBattle9MsgFmonPyraBE`
- `EF:92E9 EBattle9MsgFmonPyraBF`
- `EF:9308 EBattle9MsgFmonPyraBG`
- `EF:9327 EBattle9MsgFmonPyraBH`
- `EF:9346 EBattle9MsgFmonPyraBI`
- `EF:9365 EBattle9MsgFmonBrickAA`
- `EF:9384 EBattle9MsgFmonBrickAB`
- `EF:93A3 EBattle9MsgFmonBrickBA`
- `EF:93C2 EBattle9MsgFmonBrickBB`
- `EF:93E1 EBattle9MsgFmonBrickCA`
- `EF:9400 EBattle9MsgFmonBrickCB`
- `EF:941F EBattle9MsgFmonStoneBoss`
- `EF:9448 EBattle9MsgFmonPyraBoss`
- `EF:9467 EBattle9MsgFmonKraken2A`
- `EF:9486 EBattle9MsgFmonKraken2B`
- `EF:94A5 EBattle9MsgFmonKraken2C`
- `EF:94C4 EBattle9MsgFmonHieroglyphA`
- `EF:94E3 EBattle9MsgFmonHieroglyphB`
- `EF:9502 EBattle9MsgFmonBossGrave`
- `EF:952E EBattle9MsgGrfdPola`
- `EF:95A3 EBattle9BranchGrfdPolaTmp`
- `EF:96D3 EBattle9BranchGrfdPolaItemfull`
- `EF:970F EBattle9BranchGrfdPola1`
- `EF:9737 EBattle9BranchGrfdPolaLater`
- `EF:976B EBattle9BranchGrfdPolaLaterYes`
- `EF:9785 EBattle9MsgGrfdSignpostA`
- `EF:97A2 EBattle9MsgGrfdLlptBoss`
- `EF:981C EBattle9MsgGrfdKinokoGirl`
- `EF:9822 EBattle9MsgGrfdShintoA`
- `EF:9857 EBattle9MsgGrfdSysmsgGuts`
- `EF:98AD EBattle9BranchGrfdSysmsgGutsNo`
- `EF:98D3 EBattle9BranchGrfdSysmsgGutsYes`
- `EF:9A47 EBattle1MsgBtlNakama0`
- `EF:9A5E EBattle1MsgBtlTanemaki0`
- `EF:9A7E EBattle1MsgBtlExplosion`
- `EF:9A9E EBattle1MsgBtlBurn`
- `EF:9ABB EBattle1MsgBtlGoods`
- `EF:9AE8 EBattle1BranchBtlGoodsFailed`
- `EF:9B02 EBattle1MsgBtlTimestop`
- `EF:9B20 EBattle1MsgBtlManazashi`
- `EF:9B43 EBattle1MsgBtlKaidenpa`
- `EF:9B73 EBattle1MsgBtlYoroKaidenpa`
- `EF:9B96 EBattle1MsgBtlGeppuIki`
- `EF:9BC3 EBattle1MsgBtlDokubari`
- `EF:9BE6 EBattle1MsgBtlDeathKiss`
- `EF:9C02 EBattle1MsgBtlTumetaiIki`
- `EF:9C30 EBattle1MsgBtlHoushi`
- `EF:9C51 EBattle1MsgBtlTorituki`
- `EF:9C7E EBattle1MsgBtlYoiKaori`
- `EF:9CAD EBattle1MsgBtlKabiHousi`
- `EF:9CD1 EBattle1MsgBtlShibari`
- `EF:9CF1 EBattle1MsgBtlNeneki`
- `EF:9D14 EBattle1MsgBtlHaemitu`
- `EF:9D3E EBattle1MsgBtlOshiriIto`
- `EF:9D62 EBattle1MsgBtlKowaiKotoba`
- `EF:9D81 EBattle1MsgBtlAyashiKoto`
- `EF:9DA1 EBattle1MsgBtlFuuin`
- `EF:9DBD EBattle1MsgBtlTachibaThink`
- `EF:9DDA EBattle1MsgBtlKogeppuIki`
- `EF:9E05 EBattle1MsgBtlTyphoon`
- `EF:9E22 EBattle1MsgBtlCoffee`
- `EF:9E47 EBattle1MsgBtlMusic`
- `EF:9E69 EBattle1MsgBtlSyoukaEki`
- `EF:9E92 EBattle1MsgBtlKaminari`
- `EF:9EB4 EBattle1MsgBtlFire`
- `EF:9ED7 EBattle1MsgBtlFireBreath`
- `EF:9EF4 EGoods2MsgBtlEscapeMouse`
- `EF:9F9F EGoods2BranchMouseNotDungeon`
- `EF:9FE2 EGoods2BranchMouseCantUse`
- `EF:A002 EGoods2BranchBtlEscapeMousePizza`
- `EF:A029 EGoods2BranchBtlEscapeMouseKanban`
- `EF:A07E EGoods2BranchBtlEscapeMouseEscargo`
- `EF:A0B7 EGoods2BranchBtlEscapeMouseCapsule`
- `EF:A0DC EGoods2MsgBtlHiero`
- `EF:A2AB EGoods2MsgBtlTownMap`
- `EF:A2B5 EGoods2BranchTownMapNg`
- `EF:A2C9 EGoods2MsgOnetTabigoya`
- `EF:A2D5 EGoods2BranchOnetTabigoyaEnd`
- `EF:A2D6 EGoods2MsgOnetTabigoyaReceive`
- `EF:A2FA TextUnknownEfa2faMonsterOffEventPayload`
- `EF:A37A CommandWindowText`
- `EF:A3B6 StatusWindowText`
- `EF:A459 StatusWindowUnknownOpenTail`
- `EF:A460 NameInputWindowSelectionLayout0`
- `EF:A4E3 NameInputWindowSelectionLayout1`
- `EF:A566 NameInputWindowSelectionLayout2`
- `EF:A5E9 NameInputWindowSelectionLayout3`
- `EF:A66C NameInputWindowSelectionLayout4`
- `EF:A6A7 NameInputWindowSelectionLayout5`
- `EF:A6EB TextUnknown7EndBlockPayload`
- `EF:A6EC TextDebugUnknownMenu2`

Evidence:

- `notes/bank-ef-first-pass.md`
- `notes/ef-runtime-semantic-polish-plan.md`
- `notes/c2-ef-battle-text-contract-workahead.md`
- `notes/ef-battle-text-payload-runtime-polish.md`

### `src/ef/ef_c51b_d56f_text_glyph_mask_tables.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `EF:C51B..EF:CD1B` (`2048` bytes, SHA-1 `c05d069ecc05fe0ddc3cea5509e32ec384c3465e`) `TextGlyphMergeMaskTable`
- `EF:CD1B..EF:D51B` (`2048` bytes, SHA-1 `b468bd09266de57cf450958f7ab63c87af089b6b`) `TextGlyphCarryMaskTable`
- `EF:D51B..EF:D56F` (`84` bytes, SHA-1 `a074bb0fafeff51b2f0ba603e53fe79c4c23e7f7`) `DebugSoundMenuOptionAndVersionStrings`

Labels:

- `EF:C51B TextGlyphMergeMaskTable`
- `EF:CD1B TextGlyphCarryMaskTable`
- `EF:D51B DebugSoundMenuOptionAndVersionStrings`
- `EF:D56F EfTextGlyphMaskTablesEnd`

Evidence:

- `notes/bank-ef-first-pass.md`
- `notes/text-token-glyph-run-stager-c44b3a-c44e61.md`
- `notes/ef-readable-source-split-queue.md`

### `src/ef/ef_d56f_d6d4_debug_sound_menu_helpers.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `EF:D56F..EF:D6D4` | 357 | `DebugSoundMenuHelpers` | `50ea92d8170a2fe213f113009bd9918f69a04d91` |

Labels:

- `EF:D56F DebugSoundMenuHelpers`

Evidence:

- `notes/debug-menu-reachability-c0-c1-ef.md`
- `notes/bank-ef-first-pass.md`
- `notes/ef-readable-source-split-queue.md`
- `notes/ef-debug-sound-menu-prefix-d56f-d6d4.md`

### `src/ef/ef_d6d4_d8b5_debug_sound_menu_controller.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `EF:D6D4..EF:D8B5` | 481 | `DebugSoundMenuController` | `7dfefdcb21fdb15ad5774c0b8e05d249a9456610` |

Labels:

- `EF:D6D4 DebugSoundMenuController`

Evidence:

- `notes/debug-menu-reachability-c0-c1-ef.md`
- `notes/bank-ef-first-pass.md`
- `notes/ef-readable-source-split-queue.md`
- `notes/ef-debug-menu-controller-and-loader-d6d4-dabd.md`

### `src/ef/ef_d8b5_d95e_debug_menu_option_strings.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `EF:D8B5..EF:D8D6` (`33` bytes, SHA-1 `31f10c69f697cd6178e14aa801da883b4de1ab06`) `DebugMenuRomVersionLine`
- `EF:D8D6..EF:D8E7` (`17` bytes, SHA-1 `54027409a40418b5a91e5793a72fa75ac21d2805`) `DebugMenuTitleLine`
- `EF:D8E7..EF:D8F8` (`17` bytes, SHA-1 `8714bb0f8399aae4c8cd9b0ef4df85f30b88e7f8`) `DebugMenuGameOptionLine`
- `EF:D8F8..EF:D909` (`17` bytes, SHA-1 `50f324cf9e0de6003fc1acbed9c5542b1e55269f`) `DebugMenuViewMapOptionLine`
- `EF:D909..EF:D91A` (`17` bytes, SHA-1 `9ea121b47ef4e6e294e8aaea57f74f5608cb9eb5`) `DebugMenuViewCharacterOptionLine`
- `EF:D91A..EF:D92B` (`17` bytes, SHA-1 `556050c750b230f7d3134b68e1f2fc9fa1b04d21`) `DebugMenuViewAttributeOptionLine`
- `EF:D92B..EF:D93C` (`17` bytes, SHA-1 `8b14a4a5b3008e82adf9c014d8fc8a0a79cf71d7`) `DebugMenuShowBattleOptionLine`
- `EF:D93C..EF:D94D` (`17` bytes, SHA-1 `43ac03ef4d7f4d2dbe2b04d994e4036379f2e2d3`) `DebugMenuCheckPositionOptionLine`
- `EF:D94D..EF:D95E` (`17` bytes, SHA-1 `ae778a0e72072a3c27cffff20f866148c1c5fae3`) `DebugMenuSoundModeOptionLine`

Labels:

- `EF:D8B5 DebugMenuRomVersionLine`
- `EF:D8D6 DebugMenuTitleLine`
- `EF:D8E7 DebugMenuGameOptionLine`
- `EF:D8F8 DebugMenuViewMapOptionLine`
- `EF:D909 DebugMenuViewCharacterOptionLine`
- `EF:D91A DebugMenuViewAttributeOptionLine`
- `EF:D92B DebugMenuShowBattleOptionLine`
- `EF:D93C DebugMenuCheckPositionOptionLine`
- `EF:D94D DebugMenuSoundModeOptionLine`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/data/debug/menu_option_strings.asm`
- `refs/EB-M2-Listing-v1/US/bank2F.txt`
- `notes/debug-menu-reachability-c0-c1-ef.md`
- `notes/bank-ef-first-pass.md`
- `notes/ef-debug-menu-controller-and-loader-d6d4-dabd.md`

### `src/ef/ef_d95e_dabd_debug_menu_graphics_state_init.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `EF:D95E..EF:DABD` | 351 | `DebugMenuGraphicsAndStateInit` | `593aca35ad4b1bf4127ae9cc2d8ca981b37b8ac8` |

Labels:

- `EF:D95E DebugMenuGraphicsAndStateInit`

Evidence:

- `notes/debug-menu-reachability-c0-c1-ef.md`
- `notes/bank-ef-first-pass.md`
- `notes/ef-readable-source-split-queue.md`
- `notes/ef-debug-menu-controller-and-loader-d6d4-dabd.md`

### `src/ef/ef_dabd_dcbc_debug_menu_text_number_helpers.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `EF:DABD..EF:DCBC` | 511 | `DebugMenuTextAndNumberHelpers` | `69230efc6b0048c238d040518a61002058c4bc4c` |

Labels:

- `EF:DABD DebugMenuTextAndNumberHelpers`

Evidence:

- `notes/debug-menu-reachability-c0-c1-ef.md`
- `notes/bank-ef-first-pass.md`
- `notes/ef-readable-source-split-queue.md`
- `notes/ef-debug-menu-runtime-closure-dabd-eb5f.md`

### `src/ef/ef_dcbc_de1a_debug_check_position_overlay.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `EF:DCBC..EF:DE1A` | 350 | `DebugCheckPositionOverlayWriter` | `7be9bf793988efca02669a8a91b6ceea495b57bb` |

Labels:

- `EF:DCBC DebugCheckPositionOverlayWriter`

Evidence:

- `notes/debug-menu-reachability-c0-c1-ef.md`
- `notes/bank-ef-first-pass.md`
- `notes/ef-readable-source-split-queue.md`
- `notes/ef-debug-menu-runtime-closure-dabd-eb5f.md`

### `src/ef/ef_de1a_df0b_debug_view_character_overlay.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `EF:DE1A..EF:DF0B` | 241 | `DebugViewCharacterOverlayWriter` | `810ee840a220dbb001b044ad9d1df00b0b7b8895` |

Labels:

- `EF:DE1A DebugViewCharacterOverlayWriter`

Evidence:

- `notes/debug-menu-reachability-c0-c1-ef.md`
- `notes/bank-ef-first-pass.md`
- `notes/ef-readable-source-split-queue.md`
- `notes/ef-debug-menu-runtime-closure-dabd-eb5f.md`

### `src/ef/ef_df0b_e175_debug_overlay_tile_helpers.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `EF:DF0B..EF:E175` | 618 | `DebugOverlayTileHelpers` | `15cd4ce61ad31ea3f03158483c285caf717d41d8` |

Labels:

- `EF:DF0B DebugOverlayTileHelpers`

Evidence:

- `notes/debug-menu-reachability-c0-c1-ef.md`
- `notes/bank-ef-first-pass.md`
- `notes/ef-readable-source-split-queue.md`
- `notes/ef-debug-menu-runtime-closure-dabd-eb5f.md`

### `src/ef/ef_e175_eb1d_debug_menu_runtime_helpers.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `EF:E175..EF:EB1D` | 2472 | `DebugMenuRuntimeAndMapViewHelpers` | `622254c8aa62a39311c8331d5a5fc32a1dee77c6` |

Labels:

- `EF:E175 DebugMenuRuntimeAndMapViewHelpers`

Evidence:

- `notes/debug-menu-reachability-c0-c1-ef.md`
- `notes/bank-ef-first-pass.md`
- `notes/ef-readable-source-split-queue.md`
- `notes/ef-debug-menu-runtime-closure-dabd-eb5f.md`

### `src/ef/ef_eb1d_eb2a_debug_color_math_window_table.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `EF:EB1D..EF:EB2A` (`13` bytes, SHA-1 `49c3bca75bbbe59051ec87f6e80fc31946136449`) `DebugColorMathWindowHdmaTable`

Labels:

- `EF:EB1D DebugColorMathWindowHdmaTable`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank2f.asm`
- `notes/bank-ef-first-pass.md`
- `notes/debug-menu-reachability-c0-c1-ef.md`
- `notes/ef-readable-source-split-queue.md`
- `notes/ef-debug-menu-runtime-closure-dabd-eb5f.md`

### `src/ef/ef_eb2a_eb3d_debug_color_math_dma_reset.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `EF:EB2A..EF:EB3D` | 19 | `DebugColorMathDmaResetHelper` | `b7703e2d448dca9da5dd3146081d989ae457fc32` |

Labels:

- `EF:EB2A DebugColorMathDmaResetHelper`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank2f.asm`
- `notes/bank-ef-first-pass.md`
- `notes/debug-menu-reachability-c0-c1-ef.md`
- `notes/ef-readable-source-split-queue.md`
- `notes/ef-debug-menu-runtime-closure-dabd-eb5f.md`

### `src/ef/ef_eb3d_eb5f_debug_cursor_tilemap_data.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `EF:EB3D..EF:EB5F` (`34` bytes, SHA-1 `dd51f90c8b6debd5ab65cfcad48a0f1cf3a4fb6a`) `DebugCursorTilemapData`

Labels:

- `EF:EB3D DebugCursorTilemapData`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank2f.asm`
- `notes/bank-ef-first-pass.md`
- `notes/debug-menu-reachability-c0-c1-ef.md`
- `notes/ef-readable-source-split-queue.md`
- `notes/ef-debug-menu-runtime-closure-dabd-eb5f.md`

### `src/ef/asset_debug_menu_font.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `EF:EB5F..EF:EF70` | 1041 | `AssetDebugMenuFont` | `7d8195145f270d5d310df09b7c73a32cca868614` |

Labels:

- `EF:EB5F AssetDebugMenuFont`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank2F.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-ef.json`
- `notes/bank-ef-asset-data-map.md`

### `src/ef/table_141_data_unknown_efef70_asm.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `EF:EF70..EF:EF9F` (`47` bytes, SHA-1 `061b137ba2bb0b901659da146a46549fd93913df`) `UnknownEfef70Data`
- `EF:EF9F..EF:EFB7` (`24` bytes, SHA-1 `bc2bc6857fb27664ccb31dabc20ed81f504f429e`) `DebugFontPalette`

Labels:

- `EF:EF70 UnknownEfef70Data`
- `EF:EF9F DebugFontPalette`
- `EF:EFB7 DebugFontPaletteAndUnknownTableEnd`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank2f.asm`
- `refs/EB-M2-Listing-v1/US/bank2F.txt`
- `refs/ebsrc-main/ebsrc-main/src/data/debug/debug_font_palette.asm`
- `notes/bank-ef-first-pass.md`
- `notes/bank-ef-asset-data-map.md`

### `src/ef/asset_debug_cursor_graphics.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `EF:EFB7..EF:F0D7` | 288 | `AssetDebugCursorGraphics` | `d4aa5ac9ca83bf8da624ffab3ed1c95d0e85cdd8` |

Labels:

- `EF:EFB7 AssetDebugCursorGraphics`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank2F.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-ef.json`
- `notes/bank-ef-asset-data-map.md`

### `src/ef/asset_bank_ef_gap_1_tailpadding.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `EF:F0D7..EF:F1BB` (`228` bytes, SHA-1 `12b445e0dbf65060bfc3dd1a0958f2524d48d324`) `UnknownEff0d7ZeroPaddingData`
- `EF:F1BB..EF:F3BB` (`512` bytes, SHA-1 `1e2c1bba7c448f87003ab6b0fcab8db1e9052106`) `UnknownEff1bbLateData`
- `EF:F3BB..EF:F3DB` (`32` bytes, SHA-1 `de5c2e7d4ef51bd9017400589954706aaa3fe48f`) `UnknownVersionString`
- `EF:F3DB..EF:F511` (`310` bytes, SHA-1 `73fe4836b23e2f293057c4fbd72d07ab677aa1de`) `UnusedEff3dbData`
- `EF:F511..EF:F53B` (`42` bytes, SHA-1 `4413bc6dc79f4ca5d8706d508448c47e21e2647e`) `UnusedEff511Data`
- `EF:F53B..EF:F5BB` (`128` bytes, SHA-1 `0ae4f711ef5d6e9d26c611fd2c8c8ac45ecbf9e7`) `UnusedEff53bData`
- `EF:F5BB..EF:F5BD` (`2` bytes, SHA-1 `1e488f170b28a6dd965b53b53a149be60e05b7e1`) `DebugCursorSpritemapPointer`
- `EF:F5BD..EF:F5EB` (`46` bytes, SHA-1 `6bb0e228293b21e97cf3586d88c8e73dddc4a4ab`) `DebugCursorSpritemapEntries`
- `EF:F5EB..EF:10000` (`2581` bytes, SHA-1 `2738019380ee57a09c6901377bf56f13979f7079`) `EfBankTailPadding`

Labels:

- `EF:F0D7 UnknownEff0d7ZeroPaddingData`
- `EF:F1BB UnknownEff1bbLateData`
- `EF:F3BB UnknownVersionString`
- `EF:F3DB UnusedEff3dbData`
- `EF:F511 UnusedEff511Data`
- `EF:F53B UnusedEff53bData`
- `EF:F5BB DebugCursorSpritemapPointer`
- `EF:F5BD DebugCursorSpritemapEntries`
- `EF:F5EB EfBankTailPadding`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank2f.asm`
- `refs/EB-M2-Listing-v1/US/bank2F.txt`
- `notes/bank-ef-first-pass.md`
- `notes/bank-ef-asset-data-map.md`

## Notes

The scaffold preserves intentional source-adjacent data gaps from the manifest and validates each protected span against the original ROM bytes.
