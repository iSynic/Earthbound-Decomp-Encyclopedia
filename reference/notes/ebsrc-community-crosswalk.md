# ebsrc Community Crosswalk

Status: alias-first community navigation is generated from exact-address restored ebsrc references while local C-port semantic names remain primary.

## How to Read This Repo Against ebsrc

When a local name is stronger, source keeps that local primary name. Safe exact-address ebsrc names are added as compatibility aliases such as `EBSRC_NAME = LocalPrimaryName`; otherwise the ebsrc name stays in this crosswalk as searchable provenance. Macro vocabulary, placeholders, and unaddressed payload names are reference-only until local opcode or reader-path evidence exists.

## Status Counts

| Status | Count | Meaning |
| --- | ---: | --- |
| `blocked_conflict_or_unproven` | 765 | keep out of source until conflict, placeholder, or behavioral proof gap is resolved |
| `docs_crosswalk_only` | 6989 | document as vocabulary or navigation reference, without source aliasing |
| `local_primary_stronger` | 418 | keep local C-port semantic name primary; use the crosswalk for ebsrc lookup |
| `source_alias_integrated` | 220 | ebsrc name is already searchable in source as a primary label or alias |
| `source_alias_ready` | 0 | safe source-visible compatibility alias candidate; preserve local primary name |

## Source Alias Integrated

| Target | Lane | ebsrc Path | ebsrc Name | Local Primary | Confidence | Action |
| --- | --- | --- | --- | --- | --- | --- |
| `C0:19E2` | `overworld-runtime` | `overworld/reload_map.asm` | `RELOAD_MAP` | `Refresh_MapStripsAroundCamera` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:1A63` | `overworld-runtime` | `overworld/initialize_map.asm` | `INITIALIZE_MAP` | `Refresh_MapStripVia0E16_FarWrapper` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:1A69` | `overworld-runtime` | `overworld/initialize_misc_object_data.asm` | `INITIALIZE_MISC_OBJECT_DATA` | `Reset_EntitySlotStateTables` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:1C11` | `bank-c0` | `system/alloc_sprite_mem.asm` | `ALLOC_SPRITE_MEM` | `Rewrite_VisualMemoryReservations4A00` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:1E49` | `overworld-runtime` | `overworld/create_entity.asm` | `CREATE_ENTITY` | `Initialize_EntityWithSpritePose` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:3C5E` | `overworld-runtime` | `overworld/get_on_bicycle.asm` | `GET_ON_BICYCLE` | `Get_OnBicycle` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:404F` | `overworld-runtime` | `overworld/map_input_to_direction.asm` | `MAP_INPUT_TO_DIRECTION` | `MapInputToDirection` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:4279` | `overworld-runtime` | `overworld/find_nearby_checkable_tpt_entry.asm` | `FIND_NEARBY_CHECKABLE_TPT_ENTRY` | `Resolve_InteractableAlongFacingTarget` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:4452` | `overworld-runtime` | `overworld/find_nearby_talkable_tpt_entry.asm` | `FIND_NEARBY_TALKABLE_TPT_ENTRY` | `Resolve_FrontInteractionTarget` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:5FF6` | `overworld-runtime` | `overworld/npc_collision_check.asm` | `NPC_COLLISION_CHECK` | `Find_OverlappingEntitySlot` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:6B21` | `overworld-runtime` | `overworld/spawn_buzz_buzz.asm` | `SPAWN_BUZZ_BUZZ` | `RunPostTransitionScriptHookAndSelectorPass` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:6BFF` | `overworld-runtime` | `overworld/door_transition.asm` | `DOOR_TRANSITION` | `RunDeferredScriptPointerAndRefreshTransitionState` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:75DD` | `overworld-runtime` | `overworld/process_queued_interactions.asm` | `PROCESS_QUEUED_INTERACTIONS` | `Consume_MovementRecordQueue` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:841B` | `bank-c0` | `system/read_joypad.asm` | `READ_JOYPAD` | `Advance_InputPlaybackStream` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:8501` | `bank-c0` | `system/process_sfx_queue.asm` | `PROCESS_SFX_QUEUE` | `Nmi_ServiceAudioQueue` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:8518` | `bank-c0` | `system/execute_irq_callback.asm` | `EXECUTE_IRQ_CALLBACK` | `Frame_CallbackDispatcher` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:851B` | `bank-c0` | `system/default_irq_callback.asm` | `DEFAULT_IRQ_CALLBACK` | `Frame_CallbackReturn` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:851C` | `bank-c0` | `system/set_irq_callback.asm` | `SET_IRQ_CALLBACK` | `Set_FrameCallbackPtr` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:8522` | `bank-c0` | `system/reset_irq_callback.asm` | `RESET_IRQ_CALLBACK` | `Reset_FrameCallbackToDefault` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:8616` | `bank-c0` | `system/transfer_to_vram.asm` | `TRANSFER_TO_VRAM` | `QueueVramTransfer_FromDpSource` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:8D92` | `bank-c0` | `system/set_oam_size.asm` | `SET_OAM_SIZE` | `Update_ObselRegisterFromQueue` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:8D9E` | `bank-c0` | `system/set_bg1_vram_location.asm` | `SET_BG1_VRAM_LOCATION` | `Update_Bg1ScreenBaseRegistersFromQueue` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:8DDE` | `bank-c0` | `system/set_bg2_vram_location.asm` | `SET_BG2_VRAM_LOCATION` | `Update_Bg2ScreenBaseRegistersFromQueue` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:8E1C` | `bank-c0` | `system/set_bg3_vram_location.asm` | `SET_BG3_VRAM_LOCATION` | `Update_Bg3ScreenBaseRegistersFromQueue` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:8E5C` | `bank-c0` | `system/set_bg4_vram_location.asm` | `SET_BG4_VRAM_LOCATION` | `Update_Bg4ScreenBaseRegistersFromQueue` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:8FF7` | `bank-c0` | `system/math/mult168.asm` | `MULT168` | `Multiply16By8_ViaHardwareRegisters` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:9032` | `bank-c0` | `system/math/mult16.asm` | `MULT16` | `Multiply16By16_ViaHardwareRegisters` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:9321` | `overworld-runtime` | `overworld/init_entity.asm` | `INIT_ENTITY` | `Init_DelayedActionState` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:9F82` | `overworld-runtime` | `overworld/actionscript/choose_random.asm` | `CHOOSE_RANDOM` | `ChooseRandomScriptWord` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:A60B` | `map-data` | `data/sprite_direction_mapping_4_direction.asm` | `SPRITE_DIRECTION_MAPPING_4_DIRECTION` | `VisualProfileDirectionOffsetTable` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:A623` | `map-data` | `data/sprite_direction_mapping_8_direction.asm` | `SPRITE_DIRECTION_MAPPING_8_DIRECTION` | `VisualProfileSecondaryOffsetTable` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:A651` | `overworld-runtime` | `overworld/actionscript/set_direction8.asm` | `SET_DIRECTION8` | `Script_SetDirectionClassAndField1A86` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:A65F` | `overworld-runtime` | `overworld/actionscript/set_direction.asm` | `SET_DIRECTION` | `SetCurrentSlotDirectionClassIfActive` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:A679` | `overworld-runtime` | `overworld/actionscript/set_surface_flags.asm` | `SET_SURFACE_FLAGS` | `Script_SetCurrentSlotDisplayControlBits` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:A8F7` | `overworld-runtime` | `overworld/actionscript/prepare_new_entity_at_self.asm` | `ACTIONSCRIPT_PREPARE_NEW_ENTITY_AT_SELF` | `ActionScript_PrepareNewEntityAtSelf` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:A8FF` | `overworld-runtime` | `overworld/actionscript/prepare_new_entity_at_party_leader.asm` | `ACTIONSCRIPT_PREPARE_NEW_ENTITY_AT_PARTY_LEADER` | `ActionScript_PrepareNewEntityAtPartyLeader` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:A907` | `overworld-runtime` | `overworld/actionscript/prepare_new_entity_at_teleport_destination.asm` | `ACTIONSCRIPT_PREPARE_NEW_ENTITY_AT_TELEPORT_DESTINATION` | `ActionScript_PrepareNewEntityAtTeleportDestination` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:A912` | `overworld-runtime` | `overworld/actionscript/prepare_new_entity.asm` | `ACTIONSCRIPT_PREPARE_NEW_ENTITY` | `ActionScript_PrepareNewEntity` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:A943` | `overworld-runtime` | `overworld/actionscript/get_position_of_party_member.asm` | `ACTIONSCRIPT_GET_POSITION_OF_PARTY_MEMBER` | `ActionScript_GetPositionOfPartyMember` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:AA07` | `overworld-runtime` | `overworld/actionscript/fade_out_with_mosaic.asm` | `FADE_OUT_WITH_MOSAIC` | `ActionScript_FadeOutWithMosaic` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:AB06` | `audio-spc700` | `audio/load_spc700_data.asm` | `LOAD_SPC700_DATA` | `LoadSpc700DataStream` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:ABA8` | `audio-spc700` | `audio/wait_for_spc700.asm` | `WAIT_FOR_SPC700` | `WaitForSpcReadyAndResetApuPorts` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:ABC6` | `audio-spc700` | `audio/stop_music.asm` | `STOP_MUSIC` | `StopMusicAndLatchNoTrack` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:ABE0` | `audio-spc700` | `audio/play_sound.asm` | `PLAY_SOUND` | `QueueSoundEffectOrPlayApuPort3Cue` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:ADB2` | `battle-runtime` | `misc/battlebgs/do_battlebg_dma.asm` | `DO_BATTLEBG_DMA` | `ConfigureBattleBgDmaChannel` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:AE16` | `data-records` | `data/dma_flags.asm` | `DMA_FLAGS` | `DmaChannelFlagTable` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:AE1D` | `data-records` | `data/dma_target_registers.asm` | `DMA_TARGET_REGISTERS` | `BattleBgDmaBbusRegisterTable` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:BC74` | `bank-c0` | `misc/find_path_to_party.asm` | `FIND_PATH_TO_PARTY` | `FindPathToParty` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:C608` | `overworld-runtime` | `overworld/get_opposite_direction_from_player_to_entity.asm` | `GET_OPPOSITE_DIRECTION_FROM_PLAYER_TO_ENTITY` | `GetOppositeDirectionFromPlayerToEntity` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:C682` | `overworld-runtime` | `overworld/actionscript/get_direction_rotated_clockwise.asm` | `GET_DIRECTION_ROTATED_CLOCKWISE` | `RotateDirectionByCurrentSlotClass` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:C69E` | `overworld-runtime` | `overworld/actionscript/get_direction_turned_randomly_left_or_right.asm` | `GET_DIRECTION_TURNED_RANDOMLY_LEFT_OR_RIGHT` | `GetDirectionTurnedRandomlyLeftOrRight` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:DBE6` | `overworld-runtime` | `overworld/schedule_overworld_task.asm` | `SCHEDULE_OVERWORLD_TASK` | `Queue_DelayedActionTimer` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:DC4E` | `overworld-runtime` | `overworld/process_overworld_tasks.asm` | `PROCESS_OVERWORLD_TASKS` | `FrameCallback_ProcessDelayedActions` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:DD53` | `overworld-runtime` | `overworld/set_teleport_state.asm` | `SET_TELEPORT_STATE` | `SetTeleportStateSelectors` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:EA3E` | `bank-c0` | `misc/teleport_freezeobjects.asm` | `TELEPORT_FREEZEOBJECTS` | `SuppressInteractionsForTeleportSlots` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:EA68` | `bank-c0` | `misc/teleport_freezeobjects2.asm` | `TELEPORT_FREEZEOBJECTS2` | `EnsureTeleportSlotInteractionSuppression` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:EA99` | `bank-c0` | `misc/teleport_mainloop.asm` | `TELEPORT_MAINLOOP` | `TeleportMainloopStateMachine` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:F21E` | `bank-c0` | `intro/gas_station_load.asm` | `GAS_STATION_LOAD` | `RunGasStationIntroScreenLoop` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C1:0166` | `text-vm` | `text/ccs/halt.asm` | `HALT` | `RunTextHaltControlWorker` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C1:0301` | `text-vm` | `text/get_active_window_address.asm` | `GET_ACTIVE_WINDOW_ADDRESS` | `GetActiveInteractionContextRecord` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C1:2DD5` | `text-vm` | `text/window_tick.asm` | `WINDOW_TICK` | `C12DD5_WindowTick` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C1:2E63` | `bank-c1` | `system/debug/y_button_menu.asm` | `DEBUG_Y_BUTTON_MENU` | `C12E63_DebugMenuSelectionDispatcher` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C1:3187` | `overworld-runtime` | `overworld/talk_to.asm` | `TALK_TO` | `ResolvePrimaryFrontInteractionOutput` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C1:323B` | `overworld-runtime` | `overworld/check.asm` | `CHECK` | `ResolveSecondaryFacingInteractionOutput` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C1:34A7` | `overworld-runtime` | `overworld/open_menu.asm` | `OPEN_MENU` | `C134A7_RunOpenMenuSelectionLoop` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C1:3C32` | `text-vm` | `text/open_hppp_display.asm` | `OPEN_HPPP_DISPLAY` | `C13C32_HandlePlayerCheckingObject` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C1:3CA1` | `overworld-runtime` | `overworld/show_town_map.asm` | `SHOW_TOWN_MAP` | `OpenHpppDisplay` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C1:4012` | `overworld-runtime` | `overworld/debug/y_button_flag.asm` | `DEBUG_Y_BUTTON_FLAG` | `C14012_AdvanceNameEntryLetterBoxPointer` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C1:4049` | `overworld-runtime` | `overworld/debug/y_button_guide.asm` | `DEBUG_Y_BUTTON_GUIDE` | `C14049_RetreatNameEntryLetterBoxPointer` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C1:4070` | `overworld-runtime` | `overworld/debug/set_char_level.asm` | `DEBUG_SET_CHAR_LEVEL` | `C14070_ReadNameEntryLetterBoxPointer` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C1:597F` | `text-vm` | `text/ccs/show_character_inventory.asm` | `SHOW_CHARACTER_INVENTORY` | `C1597F_ReadCharacterInventorySlotItemTextCommand` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C1:6308` | `text-vm` | `text/ccs/jump_multi2.asm` | `JUMP_MULTI2` | `C16308_HandleTextCommand1FC0JumpMulti2` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C1:6A01` | `text-vm` | `text/ccs/set_character_level.asm` | `SET_CHARACTER_LEVEL` | `C16A01_SetCharacterLevelTextCommand` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C1:6F9F` | `text-vm` | `text/ccs/test_item_is_condiment.asm` | `TEST_ITEM_IS_CONDIMENT` | `C16F9F_ClassifyCondimentItemTextCommand` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C1:6FD1` | `text-vm` | `text/ccs/trigger_battle.asm` | `TRIGGER_BATTLE` | `C16FD1_InitScriptedBattleTextCommand` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C1:78F7` | `text-vm` | `text/ccs/load_string.asm` | `LOAD_STRING` | `StartLoadedStringInlineCollector` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C1:86B1` | `text-vm` | `text/display_text.asm` | `DISPLAY_TEXT` | `ExecuteNestedTextPointer` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C1:913D` | `bank-c1` | `misc/escargo_express_store.asm` | `ESCARGO_EXPRESS_STORE` | `EnqueuePendingItemId` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C1:9183` | `bank-c1` | `misc/escargo_express_move.asm` | `ESCARGO_EXPRESS_MOVE` | `StoreInventorySlotItemInPendingQueue` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C1:98DE` | `bank-c1` | `misc/inventory_get_item_name.asm` | `INVENTORY_GET_ITEM_NAME` | `C198DE_RenderCharacterInventoryOrEquipmentRows` | `exact_address_alias_or_primary_already_present` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |

## Source Alias Ready

These exact-address entries are safe candidates for source-visible compatibility aliases. A non-empty table is a backlog for the alias applier or manual review.

| Target | Lane | ebsrc Path | ebsrc Name | Local Primary | Confidence | Action |
| --- | --- | --- | --- | --- | --- | --- |

## Crosswalk Samples By Lane

| Target | Lane | ebsrc Path | ebsrc Name | Local Primary | Confidence | Action |
| --- | --- | --- | --- | --- | --- | --- |
| `` | `bank-c0` | `common.asm` | `COMMON` | `` | `conflict_unproven_or_placeholder_reference` | keep as reference-only until there is exact local source or reader-path evidence |
| `` | `map-data` | `symbols/map.inc.asm` | `MAP.INC` | `` | `conflict_unproven_or_placeholder_reference` | keep as reference-only until there is exact local source or reader-path evidence |
| `` | `text-vm` | `symbols/text.inc.asm` | `TEXT.INC` | `` | `conflict_unproven_or_placeholder_reference` | keep as reference-only until there is exact local source or reader-path evidence |
| `` | `overworld-runtime` | `overworld/actionscript/clear_entity_draw_sorting_table.asm` | `CLEAR_ENTITY_DRAW_SORTING_TABLE` | `` | `source_symbol_collision_elsewhere_docs_crosswalk` | keep as reference-only until there is exact local source or reader-path evidence |
| `` | `ppu-window-presentation` | `system/load_tileset_anim.asm` | `LOAD_TILESET_ANIM` | `` | `source_symbol_collision_elsewhere_docs_crosswalk` | keep as reference-only until there is exact local source or reader-path evidence |
| `C0:5238` | `battle-runtime` | `battle/init_common.asm` | `INIT_COMMON` | `Tick_LandingProfileStepSequencerIfActive` | `exact_address_local_name_more_specific_docs_crosswalk` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:6E02` | `data-records` | `data/unknown/C06E02.asm` | `` | `C06E02_DeferredTransitionStateTemplate` | `reference_vocabulary_or_payload_without_source_alias_target` | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `C0:AD8A` | `event-actionscript` | `data/events/scripts/786.asm` | `EVENT_786` | `Event786_CurrentSlotOrbitScript` | `reference_vocabulary_or_payload_without_source_alias_target` | feed into event/text/actionscript decoder vocabulary only after local opcode proof |
| `` | `bank-c1` | `common.asm` | `COMMON` | `` | `conflict_unproven_or_placeholder_reference` | keep as reference-only until there is exact local source or reader-path evidence |
| `` | `bank-c2` | `eventmacros.asm` | `EVENTMACROS` | `` | `conflict_unproven_or_placeholder_reference` | keep as reference-only until there is exact local source or reader-path evidence |
| `` | `bank-c3` | `eventmacros.asm` | `EVENTMACROS` | `` | `conflict_unproven_or_placeholder_reference` | keep as reference-only until there is exact local source or reader-path evidence |
| `` | `audio-spc700` | `symbols/audiopacks.inc.asm` | `AUDIOPACKS.INC` | `` | `conflict_unproven_or_placeholder_reference` | keep as reference-only until there is exact local source or reader-path evidence |
| `` | `bank-ef` | `common.asm` | `COMMON` | `` | `conflict_unproven_or_placeholder_reference` | keep as reference-only until there is exact local source or reader-path evidence |
| `NO_EFFECT` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `NO_EFFECT` | `` | `reference_vocabulary_or_payload_without_source_alias_target` | use as contract/comment vocabulary when touching the related semantic builder |
| `fraction` | `shared-struct-fields` | `refs/ebsrc-main/ebsrc-main/include/structs.asm` | `fraction` | `` | `reference_vocabulary_or_payload_without_source_alias_target` | use as contract/comment vocabulary when touching the related semantic builder |
| `EVENT_END` | `macro-vocabulary` | `refs/ebsrc-main/ebsrc-main/include/eventmacros.asm` | `EVENT_END` | `` | `reference_vocabulary_or_payload_without_source_alias_target` | feed into event/text/actionscript decoder vocabulary only after local opcode proof |

## Guardrails

- Do not rename local semantic labels away from their C-port-oriented names.
- Add source aliases only for exact-address, role-compatible ebsrc names.
- Keep ebsrc `UNKNOWN`, generic payload, and macro-only names in docs until local proof exists.
- Run byte-equivalence for every bank touched by source-visible aliases.
