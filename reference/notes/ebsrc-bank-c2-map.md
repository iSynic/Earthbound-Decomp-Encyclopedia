# ebsrc Bank C2 Reference Map

Generated from ebsrc bankconfig include order, ebsrc bank symbols, and local source-bank build-candidate spans.

## Summary

- includes: `406`
- exact spans: `288`
- promoted exact spans: `288`
- promotion candidates: `0`
- open/unresolved entries: `103`
- latest promoted end: `C2:FFB7`

## Current Open Frontier

| Start | End | Size | Status | Include | ebsrc Symbol | Local Name | Kind |
| --- | --- | ---: | --- | --- | --- | --- | --- |
| C2:FFB7 |  | 73 | `exact` | `battle/actions/pray_rending_sound.asm` | `` | `` | `named-code` |
|  |  | 0 | `open` | `battle/actions/pray.asm` | `` | `` | `named-code` |
|  |  | 0 | `open` | `battle/copy_mirror_data.asm` | `COPY_MIRROR_DATA` | `` | `named-code` |
|  |  | 0 | `open` | `battle/actions/mirror.asm` | `` | `` | `named-code` |
|  |  | 0 | `open` | `battle/apply_condiment.asm` | `` | `` | `named-code` |
|  |  | 0 | `open` | `battle/eat_food.asm` | `EAT_FOOD` | `` | `named-code` |
|  |  | 0 | `open` | `battle/calc_psi_damage_modifiers.asm` | `` | `` | `named-code` |
|  | C2:B66A | -18838 | `exact` | `battle/calc_psi_resistance_modifiers.asm` | `` | `` | `named-code` |

## Current Exact Frontier Candidates

| Start | End | Size | Include | ebsrc Symbol | Local Name | Kind |
| --- | --- | ---: | --- | --- | --- | --- |

## Candidate Backlog

| Start | End | Size | Include | ebsrc Symbol | Local Name | Kind |
| --- | --- | ---: | --- | --- | --- | --- |

## Include Map

| # | Start | End | Size | Status | Promoted | Include | ebsrc Symbol | Local Name |
| ---: | --- | --- | ---: | --- | --- | --- | --- | --- |
| 0 |  |  | 0 | `support` |  | `eventmacros.asm` | `` | `` |
| 1 |  |  | 0 | `support` |  | `common.asm` | `` | `` |
| 2 |  |  | 0 | `support` |  | `config.asm` | `` | `` |
| 3 |  |  | 0 | `support` |  | `structs.asm` | `` | `` |
| 4 |  |  | 0 | `support` |  | `symbols/bank00.inc.asm` | `` | `` |
| 5 |  |  | 0 | `support` |  | `symbols/bank01.inc.asm` | `` | `` |
| 6 |  |  | 0 | `support` |  | `symbols/bank02.inc.asm` | `` | `` |
| 7 |  |  | 0 | `support` |  | `symbols/bank03.inc.asm` | `` | `` |
| 8 |  |  | 0 | `support` |  | `symbols/bank04.inc.asm` | `` | `` |
| 9 |  |  | 0 | `support` |  | `symbols/bank2f.inc.asm` | `` | `` |
| 10 |  |  | 0 | `support` |  | `symbols/battle_bgs.inc.asm` | `` | `` |
| 11 |  |  | 0 | `support` |  | `symbols/battle_sprites.inc.asm` | `` | `` |
| 12 |  |  | 0 | `support` |  | `symbols/globals.inc.asm` | `` | `` |
| 13 |  |  | 0 | `support` |  | `symbols/misc.inc.asm` | `` | `` |
| 14 |  |  | 0 | `support` |  | `symbols/text.inc.asm` | `` | `` |
| 15 |  |  | 0 | `open` |  | `overworld/inflict_sunstroke_check.asm` | `INFLICT_SUNSTROKE_CHECK` | `` |
| 16 | C2:00B9 | C2:00D1 | 24 | `exact` | yes | `data/unknown/C200B9.asm` | `UNKNOWN_C200B9` | `` |
| 17 | C2:00D9 | C2:0266 | 397 | `exact` | yes | `unknown/C2/C200D9.asm` | `UNKNOWN_C200D9` | `` |
| 18 | C2:0266 | C2:0293 | 45 | `exact` | yes | `unknown/C2/C20266.asm` | `UNKNOWN_C20266` | `LoadDefaultTitleUploadTiles` |
| 19 | C2:0293 | C2:02AC | 25 | `exact` | yes | `unknown/C2/C20293.asm` | `UNKNOWN_C20293` | `ClearDefaultTitleUploadTiles` |
| 20 | C2:02AC | C2:032B | 127 | `exact` | yes | `unknown/C2/C202AC.asm` | `` | `RegisterAndUploadWindowTitleBuffer` |
| 21 | C2:032B | C2:038B | 96 | `exact` | yes | `text/set_window_title.asm` | `SET_WINDOW_TITLE` | `WriteWindowTitleAndUpload` |
| 22 | C2:038B | C2:03C3 | 56 | `exact` | yes | `unknown/C2/C2038B.asm` | `UNKNOWN_C2038B` | `ResetHpPpTilemapBuffers` |
| 23 | C2:03C3 | C2:077D | 954 | `exact` | yes | `text/hp_pp_window/draw.asm` | `` | `ComposePartyMemberHpPpWindowTiles` |
| 24 | C2:077D | C2:07B6 | 57 | `exact` | yes | `unknown/C2/C2077D.asm` | `` | `RedrawDirtyPartyHpPpWindows` |
| 25 | C2:07B6 | C2:07E1 | 43 | `exact` | yes | `unknown/C2/C207B6.asm` | `UNKNOWN_C207B6` | `MarkAndRedrawPartyHpPpWindow` |
| 26 | C2:07E1 | C2:087C | 155 | `exact` | yes | `text/hp_pp_window/undraw.asm` | `` | `ClearPartyHpPpWindowTiles` |
| 27 | C2:087C | C2:08B8 | 60 | `exact` | yes | `unknown/C2/C2087C.asm` | `UNKNOWN_C2087C` | `RefreshDirtyHpPpAndOpenTextWindows` |
| 28 | C2:08B8 | C2:0912 | 90 | `exact` | yes | `unknown/C2/C208B8.asm` | `UNKNOWN_C208B8` | `ClassifyMenuTileForCursorScan` |
| 29 | C2:0912 | C2:0958 | 70 | `exact` | yes | `data/text/name_entry_grid_character_offset_table.asm` | `NAME_ENTRY_GRID_CHARACTER_OFFSET_TABLE` | `` |
| 30 | C2:0958 | C2:09A0 | 72 | `exact` | yes | `data/unknown/C20958.asm` | `UNKNOWN_C20958` | `MenuOrNameEntryMaskTable` |
| 31 | C2:09A0 | C2:0A20 | 128 | `exact` | yes | `data/text/the.asm` | `UNKNOWN_C209A0` | `CloseAndClearCurrentWindowTilemap` |
| 32 | C2:09A0 | C2:0A20 | 128 | `exact` | yes | `unknown/C2/C209A0.asm` | `UNKNOWN_C209A0` | `CloseAndClearCurrentWindowTilemap` |
| 33 | C2:0A20 | C2:0ABC | 156 | `exact` | yes | `unknown/C2/C20A20.asm` | `UNKNOWN_C20A20` | `SnapshotManagedTextEventSlotState` |
| 34 | C2:0ABC | C2:0B65 | 169 | `exact` | yes | `unknown/C2/C20ABC.asm` | `UNKNOWN_C20ABC` | `RestoreManagedTextEventSlotState` |
| 35 | C2:0B65 | C2:0D3F | 474 | `exact` | yes | `unknown/C2/C20B65.asm` | `UNKNOWN_C20B65` | `FindNextSelectableMenuCell` |
| 36 | C2:0D3F | C2:0F58 | 537 | `exact` | yes | `text/hp_pp_window/separate_decimal_digits.asm` | `UNKNOWN_C20D3F` | `SplitValueIntoThreeDecimalDigitsAt8966` |
| 37 | C2:0F58 | C2:0F9A | 66 | `exact` | yes | `text/hp_pp_window/fill_tile_buffer_x.asm` | `` | `SelectHpPpRollDelta` |
| 38 | C2:0F9A | C2:1034 | 154 | `exact` | yes | `text/hp_pp_window/fill_tile_buffer.asm` | `` | `ClampHpPpRollTargetsToLiveValues` |
| 39 | C2:1034 | C2:108C | 88 | `exact` | yes | `text/hp_pp_window/fill_character_hp_tile_buffer.asm` | `UNKNOWN_C21034` | `AreAllHpPpRollersSettled` |
| 40 | C2:108C | C2:109F | 19 | `exact` | yes | `text/hp_pp_window/fill_character_pp_tile_buffer.asm` | `UNKNOWN_C2108C` | `ClearHpPpRollDirtyLatchIfSettled` |
| 41 | C2:0F58 | C2:0F9A | 66 | `exact` | yes | `unknown/C2/C20F58.asm` | `` | `SelectHpPpRollDelta` |
| 42 | C2:0F9A | C2:1034 | 154 | `exact` | yes | `misc/reset_hppp_rolling.asm` | `RESET_HPPP_ROLLING` | `ClampHpPpRollTargetsToLiveValues` |
| 43 | C2:1034 | C2:108C | 88 | `exact` | yes | `unknown/C2/C21034.asm` | `UNKNOWN_C21034` | `AreAllHpPpRollersSettled` |
| 44 | C2:108C | C2:109F | 19 | `exact` | yes | `unknown/C2/C2108C.asm` | `UNKNOWN_C2108C` | `ClearHpPpRollDirtyLatchIfSettled` |
| 45 | C2:109F | C2:13AC | 781 | `exact` | yes | `misc/hp_pp_roller.asm` | `HP_PP_ROLLER` | `` |
| 46 | C2:13AC | C2:1628 | 636 | `exact` | yes | `text/update_hppp_meter_tiles.asm` | `UPDATE_HPPP_METER_TILES` | `` |
| 47 | C2:1628 | C2:165E | 54 | `exact` | yes | `text/get_event_flag.asm` | `GET_EVENT_FLAG` | `TestEventFlag` |
| 48 | C2:165E | C2:16AD | 79 | `exact` | yes | `text/set_event_flag.asm` | `SET_EVENT_FLAG` | `SetOrClearEventFlag` |
| 49 | C2:16AD | C2:16C9 | 28 | `exact` | yes | `unknown/C2/C216AD.asm` | `UNKNOWN_C216AD` | `ApplyMusicTrackAndSyncMirror` |
| 50 | C2:16C9 | C2:16D0 | 7 | `exact` | yes | `audio/stop_music_redirect.asm` | `` | `StopMusicRedirect` |
| 51 | C2:16D0 | C2:16DB | 11 | `exact` | yes | `audio/play_sound_and_unknown.asm` | `PLAY_SOUND_AND_UNKNOWN` | `PlaySoundAndTickLightWindow` |
| 52 | C2:16DB | C2:1857 | 380 | `exact` | yes | `unknown/C2/C216DB.asm` | `UNKNOWN_C216DB` | `ArbitratePartyOverlayEntityPresence` |
| 53 | C2:1857 | C2:192B | 212 | `exact` | yes | `misc/recalc_character_postmath_offense.asm` | `RECALC_CHARACTER_POSTMATH_OFFENSE` | `RecalculateCharacterDerivedOffense` |
| 54 | C2:192B | C2:1AEB | 448 | `exact` | yes | `misc/recalc_character_postmath_defense.asm` | `RECALC_CHARACTER_POSTMATH_DEFENSE` | `RecalculateCharacterDerivedDefense` |
| 55 | C2:1AEB | C2:1BA4 | 185 | `exact` | yes | `misc/recalc_character_postmath_speed.asm` | `RECALC_CHARACTER_POSTMATH_SPEED` | `RecalculateCharacterDerivedSpeed` |
| 56 | C2:1BA4 | C2:1C5D | 185 | `exact` | yes | `misc/recalc_character_postmath_guts.asm` | `RECALC_CHARACTER_POSTMATH_GUTS` | `RecalculateCharacterDerivedGuts` |
| 57 | C2:1C5D | C2:1D65 | 264 | `exact` | yes | `misc/recalc_character_postmath_luck.asm` | `RECALC_CHARACTER_POSTMATH_LUCK` | `RecalculateCharacterDerivedLuck` |
| 58 | C2:1D65 | C2:1D7D | 24 | `exact` | yes | `misc/recalc_character_postmath_vitality.asm` | `RECALC_CHARACTER_POSTMATH_VITALITY` | `RecalculateCharacterDerivedVitality` |
| 59 | C2:1D7D | C2:1D95 | 24 | `exact` | yes | `misc/recalc_character_postmath_iq.asm` | `RECALC_CHARACTER_POSTMATH_IQ` | `RecalculateCharacterDerivedIq` |
| 60 | C2:1D95 | C2:1E03 | 110 | `exact` | yes | `battle/recalc_character_miss_rate.asm` | `RECALC_CHARACTER_MISS_RATE` | `RecalculateCharacterDerivedMissRate` |
| 61 | C2:1E03 | C2:2351 | 1358 | `exact` | yes | `battle/calc_resistances.asm` | `CALC_RESISTANCES` | `RecalculateCharacterDerivedResistanceFields` |
| 62 | C2:2351 | C2:239D | 76 | `exact` | yes | `misc/increase_wallet_balance.asm` | `UNKNOWN_C22351` | `FindFirstEmptyInventorySlotForCharacter` |
| 63 | C2:239D | C2:23D9 | 60 | `exact` | yes | `misc/decrease_wallet_balance.asm` | `UNKNOWN_C2239D` | `CheckPartyOverlayRegistryPresence` |
| 64 | C2:23D9 | C2:2474 | 155 | `exact` | yes | `text/get_party_character_name.asm` | `UNKNOWN_C223D9` | `LookupStatusTileValueForHpPpWindow` |
| 65 | C2:2351 | C2:239D | 76 | `exact` | yes | `unknown/C2/C22351.asm` | `UNKNOWN_C22351` | `FindFirstEmptyInventorySlotForCharacter` |
| 66 | C2:239D | C2:23D9 | 60 | `exact` | yes | `unknown/C2/C2239D.asm` | `UNKNOWN_C2239D` | `CheckPartyOverlayRegistryPresence` |
| 67 | C2:23D9 | C2:2474 | 155 | `exact` | yes | `unknown/C2/C223D9.asm` | `UNKNOWN_C223D9` | `LookupStatusTileValueForHpPpWindow` |
| 68 | C2:2474 | C2:2562 | 238 | `exact` | yes | `unknown/C2/C22474.asm` | `UNKNOWN_C22474` | `LookupStatusTileWidthOrOffsetForHpPpWindow` |
| 69 | C2:2562 | C2:25AC | 74 | `exact` | yes | `inventory/get_item_subtype.asm` | `UNKNOWN_C22562` | `SetupWeaponEquipmentPreviewBlock` |
| 70 | C2:25AC | C2:260D | 97 | `exact` | yes | `inventory/get_item_subtype2.asm` | `UNKNOWN_C225AC` | `SetupCharmEquipmentPreviewBlock` |
| 71 | C2:2562 | C2:25AC | 74 | `exact` | yes | `unknown/C2/C22562.asm` | `UNKNOWN_C22562` | `SetupWeaponEquipmentPreviewBlock` |
| 72 | C2:25AC | C2:260D | 97 | `exact` | yes | `unknown/C2/C225AC.asm` | `UNKNOWN_C225AC` | `SetupCharmEquipmentPreviewBlock` |
| 73 | C2:260D | C2:2673 | 102 | `exact` | yes | `unknown/C2/C2260D.asm` | `UNKNOWN_C2260D` | `SetupBraceletEquipmentPreviewBlock` |
| 74 | C2:2673 | C2:26C5 | 82 | `exact` | yes | `unknown/C2/C22673.asm` | `UNKNOWN_C22673` | `SetupHeadgearEquipmentPreviewBlock` |
| 75 | C2:26C5 | C2:26D0 | 11 | `exact` | yes | `unknown/C2/C226C5.asm` | `UNKNOWN_C226C5` | `SetCurrent9C88FlagAndRefresh5D64` |
| 76 | C2:26E6 | C2:26EB | 5 | `exact` | yes | `unknown/C2/C226E6.asm` | `UNKNOWN_C226E6` | `GetCurrent9C88Flag` |
| 77 | C2:26F0 | C2:272F | 63 | `exact` | yes | `unknown/C2/C226F0.asm` | `UNKNOWN_C226F0` | `FindFirstPartySlotWithStateOne` |
| 78 | C2:272F | C2:277C | 77 | `exact` | yes | `unknown/C2/C2272F.asm` | `UNKNOWN_C2272F` | `CountPartySlotsNotStateOneOrTwo` |
| 79 | C2:277C | C2:27C8 | 76 | `exact` | yes | `unknown/C2/C2277C.asm` | `UNKNOWN_C2277C` | `FindFirstPartyCodeNotStateOneOrTwo` |
| 80 | C2:27C8 | C2:281D | 85 | `exact` | yes | `misc/learn_special_psi.asm` | `LEARN_SPECIAL_PSI` | `` |
| 81 | C2:281D | C2:28B7 | 154 | `exact` | yes | `misc/atm_deposit.asm` | `` | `` |
| 82 | C2:28B7 | C2:28F8 | 65 | `exact` | yes | `misc/atm_withdraw.asm` | `` | `` |
| 83 | C2:28F8 | C2:29BB | 195 | `exact` | yes | `misc/party_add_char.asm` | `` | `` |
| 84 | C2:29BB | C2:2A2C | 113 | `exact` | yes | `misc/party_remove_char.asm` | `` | `RemovePartyOverlayTrackedItemId` |
| 85 | C2:2A2C | C2:2A3A | 14 | `exact` | yes | `misc/save_game.asm` | `` | `SaveCurrentGame` |
| 86 | C2:2A3A | C2:2F38 | 1278 | `exact` | yes | `unknown/C2/C22A3A.asm` | `UNKNOWN_C22A3A` | `TransferInventoryItemBetweenCharactersMaintainingEquipment` |
| 87 | C2:2F38 | C2:3008 | 208 | `exact` | yes | `battle/init_scripted.asm` | `` | `InitBattleScripted` |
| 88 | C2:3008 | C2:307B | 115 | `exact` | yes | `unknown/C2/C23008.asm` | `UNKNOWN_C23008` | `SaveAndClearTemporaryPartySourceState` |
| 89 | C2:307B | C2:30F3 | 120 | `exact` | yes | `unknown/C2/C2307B.asm` | `UNKNOWN_C2307B` | `RestoreTemporaryPartySourceState` |
| 90 | C2:30F3 | C2:3109 | 22 | `exact` | yes | `misc/set_teleport_box_destination.asm` | `SET_TELEPORT_BOX_DESTINATION` | `SnapshotRespawnWarpTargetState` |
| 91 | C2:3109 | C2:311B | 18 | `exact` | yes | `data/battle/consolation_item_table.asm` | `CONSOLATION_ITEM_TABLE` | `BattleStartUfoPresentFallbackTable` |
| 92 | C2:311B | C2:3B66 | 2635 | `exact` | yes | `battle/menu_handler.asm` | `` | `` |
| 93 | C2:3B66 | C2:3BCF | 105 | `exact` | yes | `text/copy_enemy_name.asm` | `` | `ExpandBattleTextContextTemplate` |
| 94 | C2:3BCF | C2:3D05 | 310 | `exact` | yes | `text/fix_attacker_name.asm` | `FIX_ATTACKER_NAME` | `BuildBattleAttackerTextContext` |
| 95 | C2:3D05 | C2:40A4 | 927 | `exact` | yes | `text/fix_target_name.asm` | `FIX_TARGET_NAME` | `BuildBattleTargetTextContext` |
| 96 | C2:3E32 | C2:3E8A | 88 | `exact` | yes | `unknown/C2/C23E32.asm` | `UNKNOWN_C23E32` | `` |
| 97 | C2:3E8A |  | 0 | `open` |  | `unknown/C2/C23E8A.asm` | `UNKNOWN_C23E8A` | `` |
| 98 |  |  | 0 | `open` |  | `battle/find_targettable_npc.asm` | `FIND_TARGETTABLE_NPC` | `` |
| 99 |  |  | 0 | `open` |  | `battle/get_shield_targetting.asm` | `GET_SHIELD_TARGETTING` | `` |
| 100 |  |  | 0 | `open` |  | `battle/feeling_strange_retargetting.asm` | `` | `` |
| 101 | C2:40A4 | C2:416F | 203 | `exact` | yes | `unknown/C2/C240A4.asm` | `UNKNOWN_C240A4` | `ApplyBattleActionSecondPointerPayload` |
| 102 | C2:416F | C2:41DC | 109 | `exact` | yes | `battle/remove_status_untargettable_targets.asm` | `REMOVE_STATUS_UNTARGETTABLE_TARGETS` | `` |
| 103 | C2:41DC | C2:4316 | 314 | `exact` | yes | `battle/find_stealable_items.asm` | `` | `BuildStealableItemCandidateList` |
| 104 | C2:4316 | C2:4348 | 50 | `exact` | yes | `battle/select_stealable_item.asm` | `SELECT_STEALABLE_ITEM` | `SelectStealableItemCandidate` |
| 105 | C2:4348 | C2:437E | 54 | `exact` | yes | `unknown/C2/C24348.asm` | `UNKNOWN_C24348` | `IsPendingStealItemStillStealable` |
| 106 | C2:437E | C2:4434 | 182 | `exact` | yes | `unknown/C2/C2437E.asm` | `UNKNOWN_C2437E` | `ApplyPendingStolenItemSlotIfStillValid` |
| 107 | C2:4434 | C2:4477 | 67 | `exact` | yes | `unknown/C2/C24434.asm` | `UNKNOWN_C24434` | `PickRandomBattlerFromFrontBackRows` |
| 108 | C2:4477 | C2:4703 | 652 | `exact` | yes | `battle/choose_target.asm` | `CHOOSE_TARGET` | `BuildClass2DerivedActionCode` |
| 109 | C2:4703 | C2:4821 | 286 | `exact` | yes | `unknown/C2/C24703.asm` | `UNKNOWN_C24703` | `DispatchClass2DerivedAction` |
| 110 | C2:4821 | C2:4958 | 311 | `exact` | yes | `battle/main_battle_routine.asm` | `` | `` |
| 111 | C2:6189 | C2:654C | 963 | `exact` | yes | `unknown/C2/C26189.asm` | `` | `FillInstantWinTileBufferAndUpload` |
| 112 | C2:654C | C2:6BFB | 1711 | `exact` | yes | `battle/instant_win_handler.asm` | `UNKNOWN_C2654C` | `RunMagicButterflyPpRestoreAnimation` |
| 113 | C2:654C | C2:6BFB | 1711 | `exact` | yes | `unknown/C2/C2654C.asm` | `UNKNOWN_C2654C` | `RunMagicButterflyPpRestoreAnimation` |
| 114 | C2:6BFB | C2:6C82 | 135 | `exact` | yes | `battle/instant_win_check.asm` | `INSTANT_WIN_CHECK` | `MaskSet_BuildActiveTypedBattlers` |
| 115 | C2:6C82 | C2:6D04 | 130 | `exact` | yes | `battle/get_battle_action_type.asm` | `` | `MaskSet_BuildPhase1Battlers` |
| 116 | C2:6D04 | C2:6E77 | 371 | `exact` | yes | `battle/get_enemy_type.asm` | `` | `` |
| 117 | C2:6E77 | C2:6EF8 | 129 | `exact` | yes | `system/wait.asm` | `` | `MaskSet_RemoveActiveTypedBattlers` |
| 118 | C2:69DE |  | 0 | `open` |  | `unknown/C2/C269DE.asm` | `` | `` |
| 119 |  |  | 0 | `open` |  | `system/math/rand_long.asm` | `` | `` |
| 120 |  |  | 0 | `open` |  | `system/math/truncate_16_to_8.asm` | `` | `` |
| 121 |  |  | 0 | `open` |  | `system/math/rand_limit.asm` | `` | `` |
| 122 |  |  | 0 | `open` |  | `battle/50_percent_variance.asm` | `` | `` |
| 123 |  |  | 0 | `open` |  | `battle/25_percent_variance.asm` | `` | `` |
| 124 |  |  | 0 | `open` |  | `battle/success_255.asm` | `` | `` |
| 125 |  |  | 0 | `open` |  | `battle/success_500.asm` | `` | `` |
| 126 |  |  | 0 | `open` |  | `battle/target_allies.asm` | `TARGET_ALLIES` | `` |
| 127 |  |  | 0 | `open` |  | `battle/target_all_enemies.asm` | `TARGET_ALL_ENEMIES` | `` |
| 128 |  |  | 0 | `open` |  | `battle/target_row.asm` | `TARGET_ROW` | `` |
| 129 |  |  | 0 | `open` |  | `battle/target_all.asm` | `TARGET_ALL` | `` |
| 130 |  |  | 0 | `open` |  | `battle/remove_npc_targetting.asm` | `REMOVE_NPC_TARGETTING` | `` |
| 131 |  |  | 0 | `open` |  | `battle/random_targetting.asm` | `RANDOM_TARGETTING` | `` |
| 132 |  |  | 0 | `open` |  | `battle/target_battler.asm` | `TARGET_BATTLER` | `` |
| 133 |  |  | 0 | `open` |  | `battle/is_char_targetted.asm` | `IS_CHAR_TARGETTED` | `` |
| 134 |  |  | 0 | `open` |  | `battle/remove_target.asm` | `REMOVE_TARGET` | `` |
| 135 |  |  | 0 | `open` |  | `battle/remove_dead_targetting.asm` | `` | `` |
| 136 |  |  | 0 | `open` |  | `battle/set_hp.asm` | `` | `` |
| 137 |  |  | 0 | `open` |  | `battle/set_pp.asm` | `` | `` |
| 138 |  |  | 0 | `open` |  | `battle/reduce_hp.asm` | `` | `` |
| 139 |  |  | 0 | `open` |  | `battle/reduce_pp.asm` | `` | `` |
| 140 |  |  | 0 | `open` |  | `battle/inflict_status.asm` | `` | `` |
| 141 |  |  | 0 | `open` |  | `battle/recover_hp.asm` | `` | `` |
| 142 |  |  | 0 | `open` |  | `battle/recover_pp.asm` | `` | `` |
| 143 |  |  | 0 | `open` |  | `battle/revive_target.asm` | `` | `` |
| 144 |  |  | 0 | `open` |  | `battle/ko_target.asm` | `KO_TARGET` | `` |
| 145 |  |  | 0 | `open` |  | `battle/success_luck80.asm` | `` | `` |
| 146 |  |  | 0 | `open` |  | `battle/success_speed.asm` | `` | `` |
| 147 |  |  | 0 | `open` |  | `battle/fail_attack_on_npcs.asm` | `` | `` |
| 148 |  |  | 0 | `open` |  | `battle/increase_offense_16th.asm` | `` | `` |
| 149 |  |  | 0 | `open` |  | `battle/increase_defense_16th.asm` | `` | `` |
| 150 |  |  | 0 | `open` |  | `battle/decrease_offense_16th.asm` | `` | `` |
| 151 |  |  | 0 | `open` |  | `battle/decrease_defense_16th.asm` | `` | `` |
| 152 |  |  | 0 | `open` |  | `battle/swap_attacker_with_target.asm` | `` | `` |
| 153 |  |  | 0 | `open` |  | `battle/calc_damage.asm` | `` | `` |
| 154 |  |  | 0 | `open` |  | `battle/calc_damage_reduction.asm` | `` | `` |
| 155 |  |  | 0 | `open` |  | `battle/miss_calc.asm` | `` | `` |
| 156 |  |  | 0 | `open` |  | `battle/smaaaash.asm` | `` | `` |
| 157 |  |  | 0 | `open` |  | `battle/determine_dodge.asm` | `` | `` |
| 158 |  |  | 0 | `open` |  | `battle/actions/level_2_attack.asm` | `` | `` |
| 159 |  |  | 0 | `open` |  | `battle/heal_strangeness.asm` | `` | `` |
| 160 |  |  | 0 | `open` |  | `battle/actions/bash.asm` | `` | `` |
| 161 |  |  | 0 | `open` |  | `battle/actions/level_4_attack.asm` | `` | `` |
| 162 |  |  | 0 | `open` |  | `battle/actions/level_3_attack.asm` | `` | `` |
| 163 |  |  | 0 | `open` |  | `battle/actions/level_1_attack.asm` | `` | `` |
| 164 |  |  | 0 | `open` |  | `battle/actions/shoot.asm` | `` | `` |
| 165 |  |  | 0 | `open` |  | `battle/actions/spy.asm` | `` | `` |
| 166 |  |  | 0 | `open` |  | `battle/actions/null01.asm` | `` | `` |
| 167 |  |  | 0 | `open` |  | `battle/actions/steal.asm` | `` | `` |
| 168 |  |  | 0 | `open` |  | `battle/actions/freeze_time.asm` | `` | `` |
| 169 |  |  | 0 | `open` |  | `battle/actions/diamondize.asm` | `` | `` |
| 170 |  |  | 0 | `open` |  | `battle/actions/paralyze.asm` | `` | `` |
| 171 |  |  | 0 | `open` |  | `battle/actions/nauseate.asm` | `` | `` |
| 172 |  |  | 0 | `open` |  | `battle/actions/poison.asm` | `` | `` |
| 173 |  |  | 0 | `open` |  | `battle/actions/cold.asm` | `` | `` |
| 174 |  |  | 0 | `open` |  | `battle/actions/mushroomize.asm` | `` | `` |
| 175 |  |  | 0 | `open` |  | `battle/actions/possess.asm` | `` | `` |
| 176 |  |  | 0 | `open` |  | `battle/actions/crying.asm` | `` | `` |
| 177 |  |  | 0 | `open` |  | `battle/actions/immobilize.asm` | `` | `` |
| 178 |  |  | 0 | `open` |  | `battle/actions/solidify.asm` | `` | `` |
| 179 |  |  | 0 | `open` |  | `battle/actions/brainshock_alpha_redirect.asm` | `` | `` |
| 180 |  |  | 0 | `open` |  | `battle/success_luck40.asm` | `` | `` |
| 181 |  |  | 0 | `open` |  | `battle/actions/distract.asm` | `` | `` |
| 182 |  |  | 0 | `open` |  | `battle/actions/feel_strange.asm` | `` | `` |
| 183 |  |  | 0 | `open` |  | `battle/actions/crying2.asm` | `` | `` |
| 184 |  |  | 0 | `open` |  | `battle/actions/hypnosis_alpha_redirect.asm` | `` | `` |
| 185 |  |  | 0 | `open` |  | `battle/actions/reduce_pp.asm` | `` | `` |
| 186 |  |  | 0 | `open` |  | `battle/actions/cut_guts.asm` | `` | `` |
| 187 |  |  | 0 | `open` |  | `battle/actions/reduce_offense_defense.asm` | `` | `` |
| 188 |  |  | 0 | `open` |  | `battle/actions/level_2_attack_poison.asm` | `` | `` |
| 189 |  |  | 0 | `open` |  | `battle/actions/bash_twice.asm` | `` | `` |
| 190 |  |  | 0 | `open` |  | `battle/actions/null01_redirect.asm` | `` | `` |
| 191 |  |  | 0 | `open` |  | `battle/actions/350_fire_damage.asm` | `` | `` |
| 192 |  |  | 0 | `open` |  | `battle/actions/level_3_attack_copy.asm` | `` | `` |
| 193 |  |  | 0 | `open` |  | `battle/actions/null02.asm` | `` | `` |
| 194 |  |  | 0 | `open` |  | `battle/actions/null03.asm` | `` | `` |
| 195 |  |  | 0 | `open` |  | `battle/actions/null04.asm` | `` | `` |
| 196 |  |  | 0 | `open` |  | `battle/actions/null05.asm` | `` | `` |
| 197 |  |  | 0 | `open` |  | `battle/actions/null06.asm` | `` | `` |
| 198 |  |  | 0 | `open` |  | `battle/actions/null07.asm` | `` | `` |
| 199 |  |  | 0 | `open` |  | `battle/actions/null08.asm` | `` | `` |
| 200 |  |  | 0 | `open` |  | `battle/actions/null09.asm` | `` | `` |
| 201 |  |  | 0 | `open` |  | `battle/actions/null10.asm` | `` | `` |
| 202 |  |  | 0 | `open` |  | `battle/actions/null11.asm` | `` | `` |
| 203 |  |  | 0 | `open` |  | `battle/actions/neutralize.asm` | `` | `` |
| 204 | C2:90C6 | C2:916E | 168 | `exact` | yes | `unknown/C2/C290C6.asm` | `UNKNOWN_C290C6` | `RunBattlerNormalizationActionWrapper` |
| 205 | C2:916E | C2:9254 | 230 | `exact` | yes | `battle/actions/level_2_attack_diamondize.asm` | `` | `RunDiamondizeAction` |
| 206 | C2:9254 | C2:9298 | 68 | `exact` | yes | `battle/actions/reduce_offense.asm` | `` | `RunOdorOffenseReductionAction` |
| 207 | C2:9298 | C2:92EE | 86 | `exact` | yes | `battle/actions/clumsy_robot_death.asm` | `` | `RunRunawayFiveClumsyRobotSpecialEvent` |
| 208 | C2:92EE | C2:941D | 303 | `exact` | yes | `battle/actions/enemy_extend.asm` | `` | `RunMasterBarfPooStarstormSpecialEvent` |
| 209 | C2:941D | C2:94CE | 177 | `exact` | yes | `battle/actions/master_barf_death.asm` | `` | `CheckSelectedBattlerTimedSubstateBlocker` |
| 210 | C2:94CE | C2:9516 | 72 | `exact` | yes | `battle/psi_shield_nullify.asm` | `` | `TickSelectedBattlerTimedSubstateCleanup` |
| 211 | C2:9516 | C2:9556 | 64 | `exact` | yes | `battle/weaken_shield.asm` | `` | `RunPsiRockinCommon` |
| 212 | C2:9556 | C2:955F | 9 | `exact` | yes | `battle/actions/psi_rockin_common.asm` | `` | `` |
| 213 | C2:955F | C2:9568 | 9 | `exact` | yes | `battle/actions/psi_rockin_alpha.asm` | `` | `` |
| 214 | C2:9568 | C2:9571 | 9 | `exact` | yes | `battle/actions/psi_rockin_beta.asm` | `` | `` |
| 215 | C2:9571 | C2:957A | 9 | `exact` | yes | `battle/actions/psi_rockin_gamma.asm` | `` | `` |
| 216 | C2:957A | C2:95AB | 49 | `exact` | yes | `battle/actions/psi_rockin_omega.asm` | `` | `RunPsiFireCommon` |
| 217 | C2:95AB | C2:95B4 | 9 | `exact` | yes | `battle/actions/psi_fire_common.asm` | `` | `` |
| 218 | C2:95B4 | C2:95BD | 9 | `exact` | yes | `battle/actions/psi_fire_alpha.asm` | `` | `` |
| 219 | C2:95BD | C2:95C6 | 9 | `exact` | yes | `battle/actions/psi_fire_beta.asm` | `` | `` |
| 220 | C2:95C6 | C2:95CF | 9 | `exact` | yes | `battle/actions/psi_fire_gamma.asm` | `` | `` |
| 221 | C2:95CF | C2:9647 | 120 | `exact` | yes | `battle/actions/psi_fire_omega.asm` | `` | `RunPsiFreezeCommon` |
| 222 | C2:9647 | C2:9650 | 9 | `exact` | yes | `battle/actions/psi_freeze_common.asm` | `` | `` |
| 223 | C2:9650 | C2:9659 | 9 | `exact` | yes | `battle/actions/psi_freeze_alpha.asm` | `` | `` |
| 224 | C2:9659 | C2:9662 | 9 | `exact` | yes | `battle/actions/psi_freeze_beta.asm` | `` | `` |
| 225 | C2:9662 | C2:966B | 9 | `exact` | yes | `battle/actions/psi_freeze_gamma.asm` | `` | `` |
| 226 | C2:966B | C2:97A5 | 314 | `exact` | yes | `battle/actions/psi_freeze_omega.asm` | `` | `RunPsiThunderCommon` |
| 227 | C2:97A5 | C2:98A1 | 252 | `exact` | yes | `battle/actions/psi_thunder_common.asm` | `` | `` |
| 228 | C2:98A1 | C2:98DE | 61 | `exact` | yes | `battle/actions/psi_thunder_alpha.asm` | `` | `GateSelectedBattlerForRandomStatusAction` |
| 229 | C2:98DE | C2:9917 | 57 | `exact` | yes | `battle/actions/psi_thunder_beta.asm` | `` | `TryApplyStrangeStatusToSelectedBattler` |
| 230 | C2:9917 | C2:9950 | 57 | `exact` | yes | `battle/actions/psi_thunder_gamma.asm` | `` | `TryApplyNumbStatusToSelectedBattler` |
| 231 | C2:9950 | C2:9987 | 55 | `exact` | yes | `battle/actions/psi_thunder_omega.asm` | `` | `TryApplyCryingStatusToSelectedBattler` |
| 232 | C2:9987 | C2:99AE | 39 | `exact` | yes | `battle/actions/psi_flash_immunity_test.asm` | `` | `RunPsiFlashAlphaAction` |
| 233 | C2:99AE | C2:99EF | 65 | `exact` | yes | `battle/actions/psi_flash_feeling_strange.asm` | `` | `RunPsiFlashBetaAction` |
| 234 | C2:99EF | C2:9A35 | 70 | `exact` | yes | `battle/actions/psi_flash_paralysis.asm` | `` | `RunPsiFlashGammaAction` |
| 235 | C2:9A35 | C2:9A80 | 75 | `exact` | yes | `battle/actions/psi_flash_crying.asm` | `` | `RunPsiFlashOmegaAction` |
| 236 | C2:9A80 | C2:9AA6 | 38 | `exact` | yes | `battle/actions/psi_flash_alpha.asm` | `` | `RunPsiStarstormCommon` |
| 237 | C2:9AA6 | C2:9AAF | 9 | `exact` | yes | `battle/actions/psi_flash_beta.asm` | `` | `` |
| 238 | C2:9AAF | C2:9AB8 | 9 | `exact` | yes | `battle/actions/psi_flash_gamma.asm` | `` | `` |
| 239 | C2:9AB8 | C2:9AC6 | 14 | `exact` | yes | `battle/actions/psi_flash_omega.asm` | `` | `RunFixedAmountHealingCommon` |
| 240 | C2:9AC6 | C2:9ACF | 9 | `exact` | yes | `battle/actions/psi_starstorm_common.asm` | `` | `RunLifeupAlphaHealingAction` |
| 241 | C2:9ACF | C2:9AD8 | 9 | `exact` | yes | `battle/actions/psi_starstorm_alpha.asm` | `` | `RunLifeupBetaHealingAction` |
| 242 | C2:9AD8 | C2:9AE1 | 9 | `exact` | yes | `battle/actions/psi_starstorm_omega.asm` | `` | `RunLifeupGammaHealingAction` |
| 243 | C2:9AE1 | C2:9AEA | 9 | `exact` | yes | `battle/actions/lifeup_common.asm` | `` | `RunLifeupOmegaHealingAction` |
| 244 | C2:9AEA | C2:9B7A | 144 | `exact` | yes | `battle/actions/lifeup_alpha.asm` | `` | `TryRecoverSelectedBattlerNarrowAffliction` |
| 245 | C2:9B7A | C2:9C2C | 178 | `exact` | yes | `battle/actions/lifeup_beta.asm` | `` | `TryRecoverSelectedBattlerCurativeAfflictions` |
| 246 | C2:9C2C | C2:9CB8 | 140 | `exact` | yes | `battle/actions/lifeup_gamma.asm` | `` | `TryRecoverSelectedBattlerBroadAfflictions` |
| 247 | C2:9CB8 | C2:9E38 | 384 | `exact` | yes | `battle/actions/lifeup_omega.asm` | `` | `TryRecoverSelectedBattlerHardState` |
| 248 | C2:9E38 | C2:9E7F | 71 | `exact` | yes | `battle/actions/healing_alpha.asm` | `` | `` |
| 249 | C2:9E7F | C2:9F06 | 135 | `exact` | yes | `battle/actions/healing_beta.asm` | `` | `` |
| 250 | C2:9F06 | C2:9F57 | 81 | `exact` | yes | `battle/actions/healing_gamma.asm` | `` | `RunResistCheckedAsleepStatusAction` |
| 251 | C2:9F57 | C2:A056 | 255 | `exact` | yes | `battle/actions/healing_omega.asm` | `` | `RunAsleepStatusWrapperAction` |
| 252 | C2:A056 | C2:A39D | 839 | `exact` | yes | `battle/actions/shield_common.asm` | `` | `RunResistCheckedStrangeStatusAction` |
| 253 | C2:A39D | C2:A3D1 | 52 | `exact` | yes | `battle/actions/shield_alpha.asm` | `` | `TryRecoverSelectedBattlerPoisonOnly` |
| 254 | C2:A3D1 | C2:A5EC | 539 | `exact` | yes | `battle/actions/shield_alpha_redirect.asm` | `` | `RunItemSideConcentrationSealAction` |
| 255 | C2:A5EC | C2:A630 | 68 | `exact` | yes | `battle/actions/shield_beta.asm` | `` | `RunDamagePlusSolidificationItemAction` |
| 256 | C2:A630 | C2:A658 | 40 | `exact` | yes | `battle/actions/shield_beta_redirect.asm` | `` | `ApplySolidificationStatusFromItemAction` |
| 257 | C2:A658 | C2:A818 | 448 | `exact` | yes | `battle/actions/psi_shield_alpha.asm` | `` | `RunBombCommonSplashDamage` |
| 258 | C2:A818 | C2:A821 | 9 | `exact` | yes | `battle/actions/psi_shield_alpha_redirect.asm` | `` | `RunBombAction` |
| 259 | C2:A821 | C2:A82A | 9 | `exact` | yes | `battle/actions/psi_shield_beta.asm` | `` | `RunSuperBombAction` |
| 260 | C2:A82A | C2:A86B | 65 | `exact` | yes | `battle/actions/psi_shield_beta_redirect.asm` | `` | `` |
| 261 | C2:A86B | C2:A89D | 50 | `exact` | yes | `battle/actions/offense_up_alpha.asm` | `` | `` |
| 262 | C2:A89D | C2:AF1F | 1666 | `exact` | yes | `battle/actions/offense_up_alpha_redirect.asm` | `` | `` |
| 263 | C2:AF1F | C2:B172 | 595 | `exact` | yes | `battle/actions/defense_down_alpha.asm` | `` | `SnapshotRestoreBattlerNormalizationContext` |
| 264 | C2:B172 | C2:B2E0 | 366 | `exact` | yes | `battle/actions/defense_down_alpha_redirect.asm` | `` | `` |
| 265 | C2:B2E0 | C2:B342 | 98 | `exact` | yes | `battle/actions/hypnosis_alpha.asm` | `` | `DispatchBattleStatChangeConsequence` |
| 266 | C2:B342 | C2:B360 | 30 | `exact` | yes | `battle/actions/hypnosis_alpha_redirect_copy.asm` | `` | `ApplyBattleHpRecoveryConsequence` |
| 267 | C2:B360 | C2:B3D8 | 120 | `exact` | yes | `battle/actions/magnet_alpha.asm` | `` | `ApplyBattlePpRecoveryConsequence` |
| 268 | C2:B3D8 | C2:B43F | 103 | `exact` | yes | `battle/actions/magnet_omega.asm` | `` | `ApplyBattleIqIncreaseConsequence` |
| 269 | C2:B43F | C2:B4A6 | 103 | `exact` | yes | `battle/actions/paralysis_alpha.asm` | `` | `ApplyBattleGutsIncreaseConsequence` |
| 270 | C2:B4A6 | C2:B50D | 103 | `exact` | yes | `battle/actions/paralysis_alpha_redirect.asm` | `` | `ApplyBattleSpeedIncreaseConsequence` |
| 271 | C2:B50D | C2:B573 | 102 | `exact` | yes | `battle/actions/brainshock_alpha.asm` | `` | `ApplyBattleVitalityIncreaseConsequence` |
| 272 | C2:B573 | C2:B6EB | 376 | `exact` | yes | `battle/actions/brainshock_alpha_redirect_copy.asm` | `` | `ApplyBattleLuckIncreaseConsequence` |
| 273 | C2:B6EB | C2:B930 | 581 | `exact` | yes | `battle/actions/hp_recovery_1d4.asm` | `` | `InitializeEnemyBattlerStatsFromEnemyId` |
| 274 | C2:B930 | C2:BAC5 | 405 | `exact` | yes | `battle/actions/hp_recovery_50.asm` | `` | `ExportBattleSelectionSnapshot` |
| 275 | C2:BAC5 | C2:BB18 | 83 | `exact` | yes | `battle/actions/hp_recovery_200.asm` | `` | `CountFilteredSecondStageRows` |
| 276 | C2:BB18 | C2:BC5C | 324 | `exact` | yes | `battle/actions/pp_recovery_20.asm` | `` | `PromoteCandidateToCollapseAfflictionController` |
| 277 | C2:BC5C | C2:BCB9 | 93 | `exact` | yes | `battle/actions/pp_recovery_80.asm` | `` | `ClearInactiveCandidateLiveSlotTransientFields` |
| 278 | C2:BCB9 | C2:BD13 | 90 | `exact` | yes | `battle/actions/iq_up_1d4.asm` | `UNKNOWN_C2BCB9` | `ApplyBattlerPpTargetLoss` |
| 279 | C2:BD13 | C2:BE6C | 345 | `exact` | yes | `battle/actions/guts_up_1d4.asm` | `` | `SumActiveEnemyBattleSpriteWidths` |
| 280 | C2:BE6C | C2:C14E | 738 | `exact` | yes | `battle/actions/speed_up_1d4.asm` | `` | `` |
| 281 | C2:C14E | C2:C37A | 556 | `exact` | yes | `battle/actions/vitality_up_1d4.asm` | `` | `RunRainbowColorsSpecialEvent` |
| 282 | C2:C37A | C2:C3E2 | 104 | `exact` | yes | `battle/actions/luck_up_1d4.asm` | `` | `RunFinalPrayerStageTransition` |
| 283 | C2:C3E2 | C2:C41F | 61 | `exact` | yes | `battle/actions/hp_recovery_300.asm` | `` | `ApplyFinalPrayerDamageStep` |
| 284 | C2:C41F | C2:C572 | 339 | `exact` | yes | `battle/actions/random_stat_up_1d4.asm` | `` | `RunFinalPrayerNarrativeTransition` |
| 285 | C2:C572 | C2:C5D1 | 95 | `exact` | yes | `battle/actions/hp_recovery_10.asm` | `` | `RunFinalPrayerOpeningTransition` |
| 286 | C2:C5D1 | C2:C5FA | 41 | `exact` | yes | `battle/actions/hp_recovery_100.asm` | `` | `RunFinalPrayerDamagePhase2` |
| 287 | C2:C5FA | C2:C623 | 41 | `exact` | yes | `battle/actions/hp_recovery_10000.asm` | `` | `RunFinalPrayerDamagePhase3` |
| 288 | C2:C623 | C2:C64C | 41 | `exact` | yes | `battle/actions/heal_poison.asm` | `HEAL_POISON` | `RunFinalPrayerDamagePhase4` |
| 289 | C2:C64C | C2:C675 | 41 | `exact` | yes | `battle/actions/counter_psi.asm` | `` | `RunFinalPrayerDamagePhase5` |
| 290 | C2:C675 | C2:C69E | 41 | `exact` | yes | `battle/actions/shield_killer.asm` | `` | `RunFinalPrayerDamagePhase6` |
| 291 | C2:C69E | C2:C6D0 | 50 | `exact` | yes | `battle/actions/hp_sucker.asm` | `` | `RunFinalPrayerDamagePhase7` |
| 292 | C2:C6D0 | C2:C6F0 | 32 | `exact` | yes | `battle/actions/hungry_hp_sucker.asm` | `` | `RunFinalPrayerNarrativePhase8` |
| 293 | C2:C6F0 | C2:C8C8 | 472 | `exact` | yes | `battle/actions/mummy_wrap.asm` | `` | `RunFinalPrayerFinale` |
| 294 | C2:C8C8 | C2:C92D | 101 | `exact` | yes | `battle/actions/bottle_rocket_common.asm` | `` | `` |
| 295 | C2:C92D | C2:CFE5 | 1720 | `exact` | yes | `battle/actions/bottle_rocket.asm` | `` | `` |
| 296 | C2:CFE5 | C2:D0AC | 199 | `exact` | yes | `battle/actions/big_bottle_rocket.asm` | `UNKNOWN_C2CFE5` | `InitLoadedBattleBgLayerFromConfig` |
| 297 | C2:D0AC | C2:D121 | 117 | `exact` | yes | `battle/actions/multi_bottle_rocket.asm` | `UNKNOWN_C2D0AC` | `BuildBattleLetterboxHdmaTable` |
| 298 | C2:D121 | C2:DAE3 | 2498 | `exact` | yes | `battle/actions/handbag_strap.asm` | `` | `` |
| 299 | C2:DAE3 | C2:DB14 | 49 | `exact` | yes | `battle/actions/bomb_common.asm` | `UNKNOWN_C2DAE3` | `PrimeLayer1BattleBgDistortionSwap` |
| 300 | C2:DB14 | C2:DE0F | 763 | `exact` | yes | `battle/actions/bomb.asm` | `UNKNOWN_C2DB14` | `` |
| 301 | C2:DE0F | C2:DE96 | 135 | `exact` | yes | `battle/actions/super_bomb.asm` | `UNKNOWN_C2DE0F` | `DimLoadedBattleBgPalettesAndUpload` |
| 302 | C2:DE96 | C2:DF2E | 152 | `exact` | yes | `battle/actions/solidify_2.asm` | `UNKNOWN_C2DE96` | `RestoreLoadedBattleBgPalettesAndUpload` |
| 303 | C2:DF2E | C2:E08E | 352 | `exact` | yes | `battle/actions/yogurt_dispenser.asm` | `` | `ApplyLoadedBattleBgPaletteStep` |
| 304 | C2:E08E | C2:E0E7 | 89 | `exact` | yes | `battle/actions/snake.asm` | `` | `ApplyLoadedBattleBgPaletteStepAcrossLayers` |
| 305 | C2:E0E7 | C2:E116 | 47 | `exact` | yes | `battle/actions/inflict_solidification.asm` | `UNKNOWN_C2E0E7` | `ClearBattleVisualFlashStateAndLayerConfig` |
| 306 | C2:E116 | C2:E6B3 | 1437 | `exact` | yes | `battle/actions/inflict_poison.asm` | `` | `` |
| 307 | C2:E6B3 | C2:E6B6 | 3 | `exact` | yes | `battle/actions/bag_of_dragonite.asm` | `UNKNOWN_C2E6B3` | `AdvancePsiAnimationFrameAndPaletteState` |
| 308 | C2:E6B6 | C2:E8C4 | 526 | `exact` | yes | `battle/actions/insect_spray_common.asm` | `UNKNOWN_C2E6B6` | `AdvancePsiAnimationFrameAndPaletteStateBody` |
| 309 | C2:E8C4 | C2:E9ED | 297 | `exact` | yes | `battle/actions/insecticide_spray.asm` | `UNKNOWN_C2E8C4` | `StartBattleSwirlOverlayAndRecordMode` |
| 310 | C2:E9ED | C2:EACF | 226 | `exact` | yes | `battle/actions/xterminator_spray.asm` | `UNKNOWN_C2E9ED` | `ClearBattleOverlayAndResetLayerEffects` |
| 311 | C2:EACF | C2:EAEA | 27 | `exact` | yes | `battle/actions/rust_promoter_common.asm` | `UNKNOWN_C2EACF` | `WaitForBattleEffectStepReady` |
| 312 | C2:EAEA | C2:EEE7 | 1021 | `exact` | yes | `battle/actions/rust_promoter.asm` | `` | `` |
| 313 | C2:EEE7 | C2:F09F | 440 | `exact` | yes | `battle/actions/rust_promoter_dx.asm` | `UNKNOWN_C2EEE7` | `LoadBattleGroupEnemySprites` |
| 314 | C2:F09F | C2:F0D1 | 50 | `exact` | yes | `battle/actions/sudden_guts_pill.asm` | `` | `FindLoadedBattleSpriteSlotById` |
| 315 | C2:F0D1 | C2:F121 | 80 | `exact` | yes | `battle/actions/defense_spray.asm` | `UNKNOWN_C2F0D1` | `TrimLoadedEnemySpriteListToWidthLimit` |
| 316 | C2:F121 | C2:F8F9 | 2008 | `exact` | yes | `battle/actions/defense_shower.asm` | `UNKNOWN_C2F121` | `AssignEnemyBattleSpriteRowsAndXPositions` |
| 317 | C2:F8F9 | C2:F917 | 30 | `exact` | yes | `battle/boss_battle_check.asm` | `UNKNOWN_C2F8F9` | `RenderAndCommitBattleSpriteRows` |
| 318 | C2:F917 | C2:FADE | 455 | `exact` | yes | `battle/actions/teleport_box.asm` | `UNKNOWN_C2F917` | `BuildBattleSpriteRowRenderOrder` |
| 319 | C2:FADE | C2:FB35 | 87 | `exact` | yes | `battle/actions/pray_subtle.asm` | `UNKNOWN_C2FADE` | `ResetEnemySpriteColorWaveSlot` |
| 320 | C2:FB35 | C2:FCA6 | 369 | `exact` | yes | `battle/actions/pray_warm.asm` | `UNKNOWN_C2FB35` | `` |
| 321 | C2:FCA6 | C2:FD99 | 243 | `exact` | yes | `battle/actions/pray_golden.asm` | `UNKNOWN_C2FCA6` | `InitEnemySpriteColorWaveEntryFromPalette` |
| 322 | C2:FD99 | C2:FEF9 | 352 | `exact` | yes | `battle/actions/pray_mysterious.asm` | `UNKNOWN_C2FD99` | `AdvanceEnemySpriteColorWavePalettes` |
| 323 | C2:FEF9 | C2:FF9A | 161 | `exact` | yes | `battle/actions/pray_rainbow.asm` | `UNKNOWN_C2FEF9` | `LoadOrDimBattlePaletteSet` |
| 324 | C2:FF9A | C2:FFB7 | 29 | `exact` | yes | `battle/actions/pray_aroma.asm` | `UNKNOWN_C2FF9A` | `CheckOverworldPositionHashThreshold3Of8` |
| 325 | C2:FFB7 |  | 73 | `exact` | yes | `battle/actions/pray_rending_sound.asm` | `` | `` |
| 326 |  |  | 0 | `open` |  | `battle/actions/pray.asm` | `` | `` |
| 327 |  |  | 0 | `open` |  | `battle/copy_mirror_data.asm` | `COPY_MIRROR_DATA` | `` |
| 328 |  |  | 0 | `open` |  | `battle/actions/mirror.asm` | `` | `` |
| 329 |  |  | 0 | `open` |  | `battle/apply_condiment.asm` | `` | `` |
| 330 |  |  | 0 | `open` |  | `battle/eat_food.asm` | `EAT_FOOD` | `` |
| 331 |  |  | 0 | `open` |  | `battle/calc_psi_damage_modifiers.asm` | `` | `` |
| 332 |  | C2:B66A | -18838 | `exact` | yes | `battle/calc_psi_resistance_modifiers.asm` | `` | `` |
| 333 | C2:B66A |  | 0 | `open` |  | `unknown/C2/C2B66A.asm` | `UNKNOWN_C2B66A` | `` |
| 334 |  |  | 0 | `open` |  | `battle/init_enemy_stats.asm` | `BATTLE_INIT_ENEMY_STATS` | `` |
| 335 |  |  | 0 | `open` |  | `battle/init_player_stats.asm` | `BATTLE_INIT_PLAYER_STATS` | `` |
| 336 |  |  | 0 | `open` |  | `battle/count_chars.asm` | `COUNT_CHARS` | `` |
| 337 |  |  | 0 | `open` |  | `battle/check_dead_players.asm` | `CHECK_DEAD_PLAYERS` | `` |
| 338 |  |  | 0 | `open` |  | `battle/reset_post_battle_stats.asm` | `RESET_POST_BATTLE_STATS` | `` |
| 339 | C2:BCB9 | C2:BD13 | 90 | `exact` | yes | `unknown/C2/C2BCB9.asm` | `UNKNOWN_C2BCB9` | `ApplyBattlerPpTargetLoss` |
| 340 | C2:BD13 | C2:BE6C | 345 | `exact` | yes | `battle/lose_hp_status.asm` | `LOSE_HP_STATUS` | `SumActiveEnemyBattleSpriteWidths` |
| 341 | C2:BD13 | C2:BE6C | 345 | `exact` | yes | `unknown/C2/C2BD13.asm` | `` | `SumActiveEnemyBattleSpriteWidths` |
| 342 | C2:BE6C | C2:C14E | 738 | `exact` | yes | `battle/call_for_help_common.asm` | `` | `` |
| 343 | C2:C14E | C2:C37A | 556 | `exact` | yes | `battle/actions/sow_seeds.asm` | `` | `RunRainbowColorsSpecialEvent` |
| 344 | C2:C37A | C2:C3E2 | 104 | `exact` | yes | `battle/actions/call_for_help.asm` | `` | `RunFinalPrayerStageTransition` |
| 345 | C2:C3E2 | C2:C41F | 61 | `exact` | yes | `battle/actions/rainbow_of_colours.asm` | `` | `ApplyFinalPrayerDamageStep` |
| 346 | C2:C41F | C2:C572 | 339 | `exact` | yes | `battle/actions/fly_honey.asm` | `` | `RunFinalPrayerNarrativeTransition` |
| 347 | C2:C21F | C2:C32C | 269 | `exact` | yes | `unknown/C2/C2C21F.asm` | `` | `` |
| 348 | C2:C32C | C2:C37A | 78 | `exact` | yes | `unknown/C2/C2C32C.asm` | `` | `` |
| 349 | C2:C37A | C2:C3E2 | 104 | `exact` | yes | `unknown/C2/C2C37A.asm` | `` | `RunFinalPrayerStageTransition` |
| 350 | C2:C3E2 | C2:C41F | 61 | `exact` | yes | `battle/giygas_hurt_prayer.asm` | `` | `ApplyFinalPrayerDamageStep` |
| 351 | C2:C41F | C2:C572 | 339 | `exact` | yes | `unknown/C2/C2C41F.asm` | `` | `RunFinalPrayerNarrativeTransition` |
| 352 | C2:C572 | C2:C5D1 | 95 | `exact` | yes | `battle/actions/pokey_speech_1.asm` | `` | `RunFinalPrayerOpeningTransition` |
| 353 | C2:C5D1 | C2:C5FA | 41 | `exact` | yes | `battle/actions/null12.asm` | `` | `RunFinalPrayerDamagePhase2` |
| 354 | C2:C5FA | C2:C623 | 41 | `exact` | yes | `battle/actions/pokey_speech_2.asm` | `` | `RunFinalPrayerDamagePhase3` |
| 355 | C2:C623 | C2:C64C | 41 | `exact` | yes | `battle/actions/giygas_prayer_1.asm` | `` | `RunFinalPrayerDamagePhase4` |
| 356 | C2:C64C | C2:C675 | 41 | `exact` | yes | `battle/actions/giygas_prayer_2.asm` | `` | `RunFinalPrayerDamagePhase5` |
| 357 | C2:C675 | C2:C69E | 41 | `exact` | yes | `battle/actions/giygas_prayer_3.asm` | `` | `RunFinalPrayerDamagePhase6` |
| 358 | C2:C69E | C2:C6D0 | 50 | `exact` | yes | `battle/actions/giygas_prayer_4.asm` | `` | `RunFinalPrayerDamagePhase7` |
| 359 | C2:C6D0 | C2:C6F0 | 32 | `exact` | yes | `battle/actions/giygas_prayer_5.asm` | `` | `RunFinalPrayerNarrativePhase8` |
| 360 | C2:C6F0 | C2:C8C8 | 472 | `exact` | yes | `battle/actions/giygas_prayer_6.asm` | `` | `RunFinalPrayerFinale` |
| 361 | C2:C8C8 | C2:C92D | 101 | `exact` | yes | `battle/actions/giygas_prayer_7.asm` | `` | `` |
| 362 | C2:C92D | C2:CFE5 | 1720 | `exact` | yes | `battle/actions/giygas_prayer_8.asm` | `` | `` |
| 363 | C2:CFE5 | C2:D0AC | 199 | `exact` | yes | `battle/actions/giygas_prayer_9.asm` | `UNKNOWN_C2CFE5` | `InitLoadedBattleBgLayerFromConfig` |
| 364 | C2:D0AC | C2:D121 | 117 | `exact` | yes | `battle/load_enemy_battle_sprites.asm` | `UNKNOWN_C2D0AC` | `BuildBattleLetterboxHdmaTable` |
| 365 | C2:D121 | C2:DAE3 | 2498 | `exact` | yes | `misc/battlebgs/generate_frame.asm` | `` | `` |
| 366 | C2:CFE5 | C2:D0AC | 199 | `exact` | yes | `unknown/C2/C2CFE5.asm` | `UNKNOWN_C2CFE5` | `InitLoadedBattleBgLayerFromConfig` |
| 367 | C2:D0AC | C2:D121 | 117 | `exact` | yes | `unknown/C2/C2D0AC.asm` | `UNKNOWN_C2D0AC` | `BuildBattleLetterboxHdmaTable` |
| 368 | C2:D121 | C2:DAE3 | 2498 | `exact` | yes | `battle/load_battlebg.asm` | `` | `` |
| 369 | C2:DAE3 | C2:DB14 | 49 | `exact` | yes | `unknown/C2/C2DAE3.asm` | `UNKNOWN_C2DAE3` | `PrimeLayer1BattleBgDistortionSwap` |
| 370 | C2:DB14 | C2:DE0F | 763 | `exact` | yes | `unknown/C2/C2DB14.asm` | `UNKNOWN_C2DB14` | `` |
| 371 | C2:DB3F | C2:DE0F | 720 | `exact` | yes | `unknown/C2/C2DB3F.asm` | `UNKNOWN_C2DB3F` | `` |
| 372 | C2:DE0F | C2:DE96 | 135 | `exact` | yes | `unknown/C2/C2DE0F.asm` | `UNKNOWN_C2DE0F` | `DimLoadedBattleBgPalettesAndUpload` |
| 373 | C2:DE96 | C2:DF2E | 152 | `exact` | yes | `unknown/C2/C2DE96.asm` | `UNKNOWN_C2DE96` | `RestoreLoadedBattleBgPalettesAndUpload` |
| 374 | C2:DF2E | C2:E08E | 352 | `exact` | yes | `unknown/C2/C2DF2E.asm` | `` | `ApplyLoadedBattleBgPaletteStep` |
| 375 | C2:E08E | C2:E0E7 | 89 | `exact` | yes | `unknown/C2/C2E08E.asm` | `` | `ApplyLoadedBattleBgPaletteStepAcrossLayers` |
| 376 | C2:E0E7 | C2:E116 | 47 | `exact` | yes | `unknown/C2/C2E0E7.asm` | `UNKNOWN_C2E0E7` | `ClearBattleVisualFlashStateAndLayerConfig` |
| 377 | C2:E116 | C2:E6B3 | 1437 | `exact` | yes | `battle/show_psi_animation.asm` | `SHOW_PSI_ANIMATION` | `` |
| 378 | C2:E6B3 | C2:E6B6 | 3 | `exact` | yes | `unknown/C2/C2E6B3.asm` | `UNKNOWN_C2E6B3` | `AdvancePsiAnimationFrameAndPaletteState` |
| 379 | C2:E8C4 | C2:E9ED | 297 | `exact` | yes | `unknown/C2/C2E8C4.asm` | `UNKNOWN_C2E8C4` | `StartBattleSwirlOverlayAndRecordMode` |
| 380 | C2:E9ED | C2:EACF | 226 | `exact` | yes | `overworld/battle_swirl_sequence.asm` | `UNKNOWN_C2E9ED` | `ClearBattleOverlayAndResetLayerEffects` |
| 381 | C2:E9C8 | C2:E9ED | 37 | `exact` | yes | `unknown/C2/C2E9C8.asm` | `UNKNOWN_C2E9C8` | `` |
| 382 | C2:E9ED | C2:EACF | 226 | `exact` | yes | `unknown/C2/C2E9ED.asm` | `UNKNOWN_C2E9ED` | `ClearBattleOverlayAndResetLayerEffects` |
| 383 | C2:EA15 | C2:EA74 | 95 | `exact` | yes | `unknown/C2/C2EA15.asm` | `UNKNOWN_C2EA15` | `BeginBattleSwirlOverlayScript` |
| 384 | C2:EA74 | C2:EAAA | 54 | `exact` | yes | `unknown/C2/C2EA74.asm` | `UNKNOWN_C2EA74` | `SwitchBattleSwirlOverlayToClosingScript` |
| 385 | C2:EAAA | C2:EACF | 37 | `exact` | yes | `unknown/C2/C2EAAA.asm` | `UNKNOWN_C2EAAA` | `` |
| 386 | C2:EACF | C2:EAEA | 27 | `exact` | yes | `unknown/C2/C2EACF.asm` | `UNKNOWN_C2EACF` | `WaitForBattleEffectStepReady` |
| 387 | C2:EAEA | C2:EEE7 | 1021 | `exact` | yes | `battle/load_battle_sprite.asm` | `` | `` |
| 388 | C2:EEE7 | C2:F09F | 440 | `exact` | yes | `unknown/C2/C2EEE7.asm` | `UNKNOWN_C2EEE7` | `LoadBattleGroupEnemySprites` |
| 389 | C2:F09F | C2:F0D1 | 50 | `exact` | yes | `battle/get_battle_sprite_width.asm` | `` | `FindLoadedBattleSpriteSlotById` |
| 390 | C2:F0D1 | C2:F121 | 80 | `exact` | yes | `battle/get_battle_sprite_height.asm` | `UNKNOWN_C2F0D1` | `TrimLoadedEnemySpriteListToWidthLimit` |
| 391 | C2:F09F | C2:F0D1 | 50 | `exact` | yes | `unknown/C2/C2F09F.asm` | `` | `FindLoadedBattleSpriteSlotById` |
| 392 | C2:F0D1 | C2:F121 | 80 | `exact` | yes | `unknown/C2/C2F0D1.asm` | `UNKNOWN_C2F0D1` | `TrimLoadedEnemySpriteListToWidthLimit` |
| 393 | C2:F121 | C2:F8F9 | 2008 | `exact` | yes | `unknown/C2/C2F121.asm` | `UNKNOWN_C2F121` | `AssignEnemyBattleSpriteRowsAndXPositions` |
| 394 | C2:F8F9 | C2:F917 | 30 | `exact` | yes | `battle/render_battle_sprite_row.asm` | `UNKNOWN_C2F8F9` | `RenderAndCommitBattleSpriteRows` |
| 395 | C2:F8F9 | C2:F917 | 30 | `exact` | yes | `unknown/C2/C2F8F9.asm` | `UNKNOWN_C2F8F9` | `RenderAndCommitBattleSpriteRows` |
| 396 | C2:F917 | C2:FADE | 455 | `exact` | yes | `unknown/C2/C2F917.asm` | `UNKNOWN_C2F917` | `BuildBattleSpriteRowRenderOrder` |
| 397 | C2:FAD2 | C2:FAD8 | 6 | `exact` | yes | `unknown/C2/C2FAD2.asm` | `UNKNOWN_C2FAD2` | `` |
| 398 | C2:FAD8 | C2:FADE | 6 | `exact` | yes | `unknown/C2/C2FAD8.asm` | `UNKNOWN_C2FAD8` | `` |
| 399 | C2:FADE | C2:FB35 | 87 | `exact` | yes | `unknown/C2/C2FADE.asm` | `UNKNOWN_C2FADE` | `ResetEnemySpriteColorWaveSlot` |
| 400 | C2:FB35 | C2:FCA6 | 369 | `exact` | yes | `unknown/C2/C2FB35.asm` | `UNKNOWN_C2FB35` | `` |
| 401 | C2:FCA6 | C2:FD99 | 243 | `exact` | yes | `unknown/C2/C2FCA6.asm` | `UNKNOWN_C2FCA6` | `InitEnemySpriteColorWaveEntryFromPalette` |
| 402 | C2:FD99 | C2:FEF9 | 352 | `exact` | yes | `unknown/C2/C2FD99.asm` | `UNKNOWN_C2FD99` | `AdvanceEnemySpriteColorWavePalettes` |
| 403 | C2:FEF9 | C2:FF9A | 161 | `exact` | yes | `unknown/C2/C2FEF9.asm` | `UNKNOWN_C2FEF9` | `LoadOrDimBattlePaletteSet` |
| 404 | C2:FF9A | C2:FFB7 | 29 | `exact` | yes | `unknown/C2/C2FF9A.asm` | `UNKNOWN_C2FF9A` | `CheckOverworldPositionHashThreshold3Of8` |
| 405 | C2:FFB7 |  | 73 | `exact` | yes | `data/events/scripts/000.asm` | `` | `` |
