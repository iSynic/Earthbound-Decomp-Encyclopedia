# ebsrc Bank C0 Reference Map

Generated from ebsrc bankconfig include order, ebsrc bank symbols, and local source-bank build-candidate spans.

## Summary

- includes: `666`
- exact spans: `570`
- promoted exact spans: `568`
- promotion candidates: `2`
- open/unresolved entries: `80`
- latest promoted end: `C0:F41E`

## Current Open Frontier

| Start | End | Size | Status | Include | ebsrc Symbol | Local Name | Kind |
| --- | --- | ---: | --- | --- | --- | --- | --- |
| C0:F41E | C0:10000 | 3042 | `exact` | `intro/gas_station.asm` | `GAS_STATION` | `FrameCallback_ProcessCommandStream` | `named-code` |
| C0:10000 |  | 0 | `open` | `intro/load_gas_station_flash_palette.asm` | `LOAD_GAS_STATION_FLASH_PALETTE` | `` | `named-code` |
| C0:10000 |  | 0 | `open` | `intro/load_gas_station_palette.asm` | `LOAD_GAS_STATION_PALETTE` | `` | `named-code` |
| C0:10000 |  | 0 | `open` | `ending/credits_scroll_frame.asm` | `` | `` | `named-include` |

## Current Exact Frontier Candidates

| Start | End | Size | Include | ebsrc Symbol | Local Name | Kind |
| --- | --- | ---: | --- | --- | --- | --- |

## Candidate Backlog

| Start | End | Size | Include | ebsrc Symbol | Local Name | Kind |
| --- | --- | ---: | --- | --- | --- | --- |
| C0:222B | C0:255C | 817 | `unknown/C0/C0222B.asm` | `UNKNOWN_C0222B` | `` | `unknown-code` |
| C0:8B19 | C0:8B8E | 117 | `unknown/C0/C08B19.asm` | `UNKNOWN_C08B19` | `` | `unknown-code` |

## Include Map

| # | Start | End | Size | Status | Promoted | Include | ebsrc Symbol | Local Name |
| ---: | --- | --- | ---: | --- | --- | --- | --- | --- |
| 0 |  |  | 0 | `support` |  | `common.asm` | `` | `` |
| 1 |  |  | 0 | `support` |  | `config.asm` | `` | `` |
| 2 |  |  | 0 | `support` |  | `eventmacros.asm` | `` | `` |
| 3 |  |  | 0 | `support` |  | `structs.asm` | `` | `` |
| 4 |  |  | 0 | `support` |  | `symbols/bank00.inc.asm` | `` | `` |
| 5 |  |  | 0 | `support` |  | `symbols/bank01.inc.asm` | `` | `` |
| 6 |  |  | 0 | `support` |  | `symbols/bank02.inc.asm` | `` | `` |
| 7 |  |  | 0 | `support` |  | `symbols/bank03.inc.asm` | `` | `` |
| 8 |  |  | 0 | `support` |  | `symbols/bank04.inc.asm` | `` | `` |
| 9 |  |  | 0 | `support` |  | `symbols/bank2f.inc.asm` | `` | `` |
| 10 |  |  | 0 | `support` |  | `symbols/doors.inc.asm` | `` | `` |
| 11 |  |  | 0 | `support` |  | `symbols/globals.inc.asm` | `` | `` |
| 12 |  |  | 0 | `support` |  | `symbols/map.inc.asm` | `` | `` |
| 13 |  |  | 0 | `support` |  | `symbols/misc.inc.asm` | `` | `` |
| 14 |  |  | 0 | `support` |  | `symbols/sram.inc.asm` | `` | `` |
| 15 |  |  | 0 | `support` |  | `symbols/text.inc.asm` | `` | `` |
| 16 |  |  | 0 | `open` |  | `overworld/actionscript/clear_entity_draw_sorting_table.asm` | `` | `` |
| 17 |  |  | 0 | `open` |  | `overworld/setup_vram.asm` | `OVERWORLD_SETUP_VRAM` | `` |
| 18 |  |  | 0 | `open` |  | `overworld/initialize.asm` | `OVERWORLD_INITIALIZE` | `` |
| 19 |  |  | 0 | `open` |  | `system/load_tileset_anim.asm` | `` | `` |
| 20 |  |  | 0 | `open` |  | `system/animate_tileset.asm` | `ANIMATE_TILESET` | `` |
| 21 |  |  | 0 | `open` |  | `system/load_palette_anim.asm` | `` | `` |
| 22 |  |  | 0 | `open` |  | `system/animate_palette.asm` | `ANIMATE_PALETTE` | `` |
| 23 | C0:035B |  | 0 | `open` |  | `unused/C0035B.asm` | `UNUSED_C0035B` | `` |
| 24 |  |  | 0 | `open` |  | `system/get_colour_average.asm` | `` | `` |
| 25 |  |  | 0 | `open` |  | `overworld/adjust_single_colour.asm` | `` | `` |
| 26 |  |  | 0 | `open` |  | `overworld/adjust_sprite_palettes_by_average.asm` | `ADJUST_SPRITE_PALETTES_BY_AVERAGE` | `` |
| 27 |  |  | 0 | `open` |  | `overworld/prepare_average_for_sprite_palettes.asm` | `PREPARE_AVERAGE_FOR_SPRITE_PALETTES` | `` |
| 28 |  |  | 0 | `open` |  | `overworld/load_tile_collision.asm` | `` | `` |
| 29 |  |  | 0 | `open` |  | `overworld/replace_block.asm` | `` | `` |
| 30 |  |  | 0 | `open` |  | `overworld/load_map_block_event_changes.asm` | `LOAD_MAP_BLOCK_EVENT_CHANGES` | `` |
| 31 |  |  | 0 | `open` |  | `overworld/load_special_sprite_palette.asm` | `LOAD_SPECIAL_SPRITE_PALETTE` | `` |
| 32 |  |  | 0 | `open` |  | `overworld/load_map_palette.asm` | `` | `` |
| 33 |  |  | 0 | `open` |  | `overworld/load_map_at_sector.asm` | `` | `` |
| 34 |  |  | 0 | `open` |  | `overworld/load_sector_attributes.asm` | `` | `` |
| 35 |  |  | 0 | `open` |  | `overworld/load_map_row.asm` | `` | `` |
| 36 |  |  | 0 | `open` |  | `overworld/load_map_column.asm` | `` | `` |
| 37 |  |  | 0 | `open` |  | `overworld/load_collision_row.asm` | `` | `` |
| 38 |  |  | 0 | `open` |  | `overworld/load_collision_column.asm` | `` | `` |
| 39 | C0:0E16 | C0:0FCB | 437 | `exact` | yes | `unknown/C0/C00E16.asm` | `` | `Upload_VerticalMovementMapStrip` |
| 40 | C0:0FCB | C0:1181 | 438 | `exact` | yes | `unknown/C0/C00FCB.asm` | `` | `Upload_HorizontalMovementMapStrip` |
| 41 | C0:1181 | C0:1558 | 983 | `exact` | yes | `unknown/C0/C01181.asm` | `` | `Upload_AuxiliaryMovementMapStrip` |
| 42 | C0:122A |  | 0 | `open` |  | `unknown/C0/C0122A.asm` | `` | `` |
| 43 |  |  | 0 | `open` |  | `overworld/reload_map_at_position.asm` | `RELOAD_MAP_AT_POSITION` | `` |
| 44 |  |  | 0 | `open` |  | `overworld/load_map_at_position.asm` | `LOAD_MAP_AT_POSITION` | `` |
| 45 |  |  | 0 | `open` |  | `overworld/refresh_map_at_position.asm` | `` | `` |
| 46 | C0:1731 | C0:17EA | 185 | `exact` | yes | `unknown/C0/C01731.asm` | `UNKNOWN_C01731` | `` |
| 47 | C0:17EA | C0:19E2 | 504 | `exact` | yes | `unknown/C0/C017EA.asm` | `UNKNOWN_C017EA` | `AccumulateOverworldCameraStep` |
| 48 | C0:19E2 | C0:1A63 | 129 | `exact` | yes | `overworld/reload_map.asm` | `UNKNOWN_C019E2` | `Refresh_MapStripsAroundCamera` |
| 49 | C0:1A63 | C0:1A69 | 6 | `exact` | yes | `overworld/initialize_map.asm` | `UNKNOWN_C01A63` | `Refresh_MapStripVia0E16_FarWrapper` |
| 50 | C0:19E2 | C0:1A63 | 129 | `exact` | yes | `unknown/C0/C019E2.asm` | `UNKNOWN_C019E2` | `Refresh_MapStripsAroundCamera` |
| 51 | C0:1A63 | C0:1A69 | 6 | `exact` | yes | `unknown/C0/C01A63.asm` | `UNKNOWN_C01A63` | `Refresh_MapStripVia0E16_FarWrapper` |
| 52 | C0:1A69 | C0:1A86 | 29 | `exact` | yes | `overworld/initialize_misc_object_data.asm` | `INITIALIZE_MISC_OBJECT_DATA` | `Reset_EntitySlotStateTables` |
| 53 | C0:1A86 | C0:1A9D | 23 | `exact` | yes | `unknown/C0/C01A86.asm` | `UNKNOWN_C01A86` | `Reset_EntityBytePool467E` |
| 54 | C0:1A9D | C0:1B15 | 120 | `exact` | yes | `overworld/find_free_space_7E4682.asm` | `` | `Find_FreeEntityBytePoolRun467E` |
| 55 | C0:1B15 | C0:1B96 | 129 | `exact` | yes | `unknown/C0/C01B15.asm` | `UNKNOWN_C01B15` | `Release_EntityBytePoolRun467E` |
| 56 | C0:1B96 | C0:1C11 | 123 | `exact` | yes | `unknown/C0/C01B96.asm` | `UNKNOWN_C01B96` | `Reserve_VisualMemorySpan4A00` |
| 57 | C0:1C11 | C0:1C52 | 65 | `exact` | yes | `system/alloc_sprite_mem.asm` | `ALLOC_SPRITE_MEM` | `Rewrite_VisualMemoryReservations4A00` |
| 58 | C0:1C52 | C0:1CA8 | 86 | `exact` | yes | `unknown/C0/C01C52.asm` | `UNKNOWN_C01C52` | `ReserveAndUpload_EntityVisualTiles` |
| 59 | C0:1D38 | C0:1DED | 181 | `exact` | yes | `unknown/C0/C01D38.asm` | `` | `Build_EntityVisualRecords467E` |
| 60 | C0:1DED | C0:1E49 | 92 | `exact` | yes | `unknown/C0/C01DED.asm` | `` | `Read_SpritePoseVisualDescriptor` |
| 61 | C0:1E49 | C0:20F1 | 680 | `exact` | yes | `overworld/create_entity.asm` | `CREATE_ENTITY` | `Initialize_EntityWithSpritePose` |
| 62 | C0:20F1 | C0:2140 | 79 | `exact` | yes | `unknown/C0/C020F1.asm` | `UNKNOWN_C020F1` | `ScriptRelease_CurrentEntityVisualState` |
| 63 | C0:2140 | C0:2291 | 337 | `exact` | yes | `unknown/C0/C02140.asm` | `UNKNOWN_C02140` | `Release_EntitySlotAndVisualState` |
| 64 | C0:2194 | C0:21E6 | 82 | `exact` | yes | `unknown/C0/C02194.asm` | `UNKNOWN_C02194` | `` |
| 65 | C0:21E6 | C0:222B | 69 | `exact` | yes | `unknown/C0/C021E6.asm` | `UNKNOWN_C021E6` | `` |
| 66 | C0:222B | C0:255C | 817 | `exact` |  | `unknown/C0/C0222B.asm` | `UNKNOWN_C0222B` | `` |
| 67 | C0:255C | C0:25CF | 115 | `exact` | yes | `unknown/C0/C0255C.asm` | `UNKNOWN_C0255C` | `Run_VerticalCompanionSpawnProducer` |
| 68 | C0:25CF | C0:263D | 110 | `exact` | yes | `unknown/C0/C025CF.asm` | `UNKNOWN_C025CF` | `Run_HorizontalCompanionSpawnProducer` |
| 69 | C0:263D | C0:2668 | 43 | `exact` | yes | `unknown/C0/C0263D.asm` | `UNKNOWN_C0263D` | `Lookup_PlacementTileWord_D01880` |
| 70 | C0:2668 | C0:28E7 | 639 | `exact` | yes | `unknown/C0/C02668.asm` | `` | `Resolve_SpawnProbeCandidateList` |
| 71 | C0:28E7 | C0:2957 | 112 | `exact` | yes | `overworld/spawn_horizontal.asm` | `SPAWN_HORIZONTAL` | `TryPlaceSpawnCandidateFromListEntry` |
| 72 | C0:2957 | C0:2A50 | 249 | `exact` | yes | `overworld/spawn_vertical.asm` | `SPAWN_VERTICAL` | `InitializeSpawnedCandidateEntitySlot` |
| 73 | C0:2C3E |  | 0 | `open` |  | `unknown/C0/C02C3E.asm` | `UNKNOWN_C02C3E` | `RefreshSpecialTraversalModeState` |
| 74 |  |  | 0 | `open` |  | `overworld/reset_mushroomized_walking.asm` | `RESET_MUSHROOMIZED_WALKING` | `` |
| 75 |  |  | 0 | `open` |  | `overworld/mushroomization_movement_swap.asm` | `` | `` |
| 76 | C0:2D29 |  | 0 | `open` |  | `unknown/C0/C02D29.asm` | `UNKNOWN_C02D29` | `ResetOverworldPartyRuntimeState` |
| 77 |  |  | 0 | `open` |  | `overworld/adjust_position_horizontal.asm` | `` | `` |
| 78 |  |  | 0 | `open` |  | `overworld/adjust_position_vertical.asm` | `` | `` |
| 79 | C0:329F | C0:34D6 | 567 | `exact` | yes | `unknown/C0/C0329F.asm` | `UNKNOWN_C0329F` | `Clear_CharacterAfflictionBytes` |
| 80 | C0:32EC |  | 0 | `open` |  | `unknown/C0/C032EC.asm` | `UNKNOWN_C032EC` | `` |
| 81 |  |  | 0 | `open` |  | `overworld/update_party.asm` | `UPDATE_PARTY` | `` |
| 82 | C0:369B | C0:37D0 | 309 | `exact` | yes | `unknown/C0/C0369B.asm` | `UNKNOWN_C0369B` | `Insert_MushroomizedWalkingActiveEntry` |
| 83 | C0:3903 | C0:39E5 | 226 | `exact` | yes | `unknown/C0/C03903.asm` | `UNKNOWN_C03903` | `` |
| 84 | C0:39E5 | C0:3A24 | 63 | `exact` | yes | `unknown/C0/C039E5.asm` | `UNKNOWN_C039E5` | `RefreshMushroomizedEntryTargetPositions` |
| 85 | C0:3A24 | C0:3A94 | 112 | `exact` | yes | `unknown/C0/C03A24.asm` | `UNKNOWN_C03A24` | `Rebuild_MushroomizedWalkingController` |
| 86 | C0:3A94 | C0:3C25 | 401 | `exact` | yes | `unknown/C0/C03A94.asm` | `UNKNOWN_C03A94` | `RefreshPositionDerivedVisualContextClass` |
| 87 | C0:3C25 | C0:3C4B | 38 | `exact` | yes | `unknown/C0/C03C25.asm` | `` | `Refresh_DestinationContextIfPositionChanged` |
| 88 | C0:3C4B | C0:3C5E | 19 | `exact` | yes | `unknown/C0/C03C4B.asm` | `UNKNOWN_C03C4B` | `Probe_CurrentPositionHighCollisionBits` |
| 89 | C0:3C5E | C0:3CFD | 159 | `exact` | yes | `overworld/get_on_bicycle.asm` | `GET_ON_BICYCLE` | `Get_OnBicycle` |
| 90 | C0:3CFD | C0:3DAA | 173 | `exact` | yes | `unknown/C0/C03CFD.asm` | `UNKNOWN_C03CFD` | `Restore_LeaderEntityFromBicycleMode` |
| 91 | C0:3DAA | C0:3E25 | 123 | `exact` | yes | `unknown/C0/C03DAA.asm` | `UNKNOWN_C03DAA` | `Sync_CurrentSlotToPartyCharacterRecord` |
| 92 | C0:3E25 | C0:3E5A | 53 | `exact` | yes | `unknown/C0/C03E25.asm` | `UNKNOWN_C03E25` | `Get_PreviousRegistryTypeCode` |
| 93 | C0:3E5A | C0:3E9D | 67 | `exact` | yes | `unknown/C0/C03E5A.asm` | `` | `Get_PreviousRegistryObjectOrderByte` |
| 94 | C0:3E9D | C0:3EC3 | 38 | `exact` | yes | `unknown/C0/C03E9D.asm` | `UNKNOWN_C03E9D` | `Measure_PreviousRegistryOrderDelta` |
| 95 | C0:3EC3 | C0:3F1E | 91 | `exact` | yes | `unknown/C0/C03EC3.asm` | `UNKNOWN_C03EC3` | `Advance_RegistryOrderAndUpdateGapFlag` |
| 96 | C0:3F1E | C0:3FA9 | 139 | `exact` | yes | `unknown/C0/C03F1E.asm` | `UNKNOWN_C03F1E` | `Apply_TransitionSnapshotToRegistryEntities` |
| 97 | C0:3FA9 | C0:402B | 130 | `exact` | yes | `unknown/C0/C03FA9.asm` | `UNKNOWN_C03FA9` | `Refresh_PostTransitionEntityPlacement` |
| 98 | C0:402B | C0:4049 | 30 | `exact` | yes | `system/center_screen.asm` | `UNKNOWN_C0402B` | `Install_AnimationScriptFromCallerPointer` |
| 99 | C0:402B | C0:4049 | 30 | `exact` | yes | `unknown/C0/C0402B.asm` | `UNKNOWN_C0402B` | `Install_AnimationScriptFromCallerPointer` |
| 100 | C0:4049 | C0:404F | 6 | `exact` | yes | `unknown/C0/C04049.asm` | `UNKNOWN_C04049` | `Clear_AnimationScriptCountdown` |
| 101 | C0:404F | C0:4116 | 199 | `exact` | yes | `overworld/map_input_to_direction.asm` | `MAP_INPUT_TO_DIRECTION` | `MapInputToDirection` |
| 102 | C0:4116 | C0:41E3 | 205 | `exact` | yes | `unknown/C0/C04116.asm` | `` | `Probe_InteractableInFacingDirection` |
| 103 | C0:41E3 | C0:4279 | 150 | `exact` | yes | `unknown/C0/C041E3.asm` | `` | `Probe_InteractableAlongFacing` |
| 104 | C0:4279 | C0:42EF | 118 | `exact` | yes | `overworld/find_nearby_checkable_tpt_entry.asm` | `FIND_NEARBY_CHECKABLE_TPT_ENTRY` | `Resolve_InteractableAlongFacingTarget` |
| 105 | C0:42C2 | C0:42EF | 45 | `exact` | yes | `unknown/C0/C042C2.asm` | `UNKNOWN_C042C2` | `` |
| 106 | C0:42EF | C0:43BC | 205 | `exact` | yes | `unknown/C0/C042EF.asm` | `` | `Probe_FrontInteractionFacing` |
| 107 | C0:43BC | C0:4452 | 150 | `exact` | yes | `unknown/C0/C043BC.asm` | `` | `Resolve_InteractionFacingRotation` |
| 108 | C0:4452 | C0:449B | 73 | `exact` | yes | `overworld/find_nearby_talkable_tpt_entry.asm` | `FIND_NEARBY_TALKABLE_TPT_ENTRY` | `Resolve_FrontInteractionTarget` |
| 109 | C0:449B | C0:476D | 722 | `exact` | yes | `unknown/C0/C0449B.asm` | `` | `Step_PlayerFromDirectionalInput` |
| 110 | C0:476D | C0:47CF | 98 | `exact` | yes | `unknown/C0/C0476D.asm` | `` | `Sync_PlayerGlobalsFromActiveSlot` |
| 111 | C0:47CF | C0:48D3 | 260 | `exact` | yes | `unknown/C0/C047CF.asm` | `` | `Step_ScriptedMode0C` |
| 112 | C0:48D3 | C0:4A7B | 424 | `exact` | yes | `unknown/C0/C048D3.asm` | `` | `Step_BicycleTraversalMode` |
| 113 | C0:4A7B | C0:4A88 | 13 | `exact` | yes | `unknown/C0/C04A7B.asm` | `UNKNOWN_C04A7B` | `Restore_TemporaryMovementMode` |
| 114 | C0:4A88 | C0:4AAD | 37 | `exact` | yes | `unknown/C0/C04A88.asm` | `UNKNOWN_C04A88` | `Enter_TemporaryPartyFacingRefreshMode` |
| 115 | C0:4AAD | C0:4B53 | 166 | `exact` | yes | `unknown/C0/C04AAD.asm` | `` | `Tick_TemporaryPartyFacingRefreshMode` |
| 116 | C0:4B53 | C0:4C45 | 242 | `exact` | yes | `unknown/C0/C04B53.asm` | `` | `Dispatch_TemporaryMovementMode98A5` |
| 117 | C0:4C45 | C0:4D78 | 307 | `exact` | yes | `unknown/C0/C04C45.asm` | `UNKNOWN_C04C45` | `Commit_PlayerPositionSnapshotTick` |
| 118 | C0:4D78 | C0:4EF0 | 376 | `exact` | yes | `unknown/C0/C04D78.asm` | `UNKNOWN_C04D78` | `Tick_Event2SnapshotObjectReconcile` |
| 119 | C0:4EF0 | C0:4F60 | 112 | `exact` | yes | `unknown/C0/C04EF0.asm` | `UNKNOWN_C04EF0` | `Restore_CurrentSlotFromSnapshotRecord` |
| 120 | C0:4F47 | C0:4F60 | 25 | `exact` | yes | `unknown/C0/C04F47.asm` | `UNKNOWN_C04F47` | `` |
| 121 | C0:4F60 | C0:4F9F | 63 | `exact` | yes | `unknown/C0/C04F60.asm` | `` | `Queue_PartyObjectConditionDecayCallback` |
| 122 | C0:4F9F | C0:4FFE | 95 | `exact` | yes | `unknown/C0/C04F9F.asm` | `` | `Update_PartyObjectConditionThresholdLatch` |
| 123 | C0:4FFE | C0:5200 | 514 | `exact` | yes | `unknown/C0/C04FFE.asm` | `UNKNOWN_C04FFE` | `Process_PartyObjectConditionDecayGate` |
| 124 | C0:5200 | C0:5238 | 56 | `exact` | yes | `unknown/C0/C05200.asm` | `UNKNOWN_C05200` | `Tick_OverworldPlayerPositionAndCallbacks` |
| 125 | C0:5238 | C0:52D4 | 156 | `exact` | yes | `battle/init_common.asm` | `` | `Tick_LandingProfileStepSequencerIfActive` |
| 126 | C0:52D4 | C0:546B | 407 | `exact` | yes | `unknown/C0/C052D4.asm` | `UNKNOWN_C052D4` | `Seed_PartyTrailSnapshotRing` |
| 127 | C0:546B | C0:54C9 | 94 | `exact` | yes | `unknown/C0/C0546B.asm` | `UNKNOWN_C0546B` | `Sum_ActivePartyLevels` |
| 128 | C0:54C9 | C0:5503 | 58 | `exact` | yes | `unknown/C0/C054C9.asm` | `` | `Read_CollisionByteAndLatchBit10Coord` |
| 129 | C0:5503 | C0:559C | 153 | `exact` | yes | `unknown/C0/C05503.asm` | `` | `OR_CollisionHorizontalEdgeA` |
| 130 | C0:559C | C0:5639 | 157 | `exact` | yes | `unknown/C0/C0559C.asm` | `` | `OR_CollisionHorizontalEdgeB` |
| 131 | C0:5639 | C0:56D0 | 151 | `exact` | yes | `unknown/C0/C05639.asm` | `` | `OR_CollisionVerticalEdgeA` |
| 132 | C0:56D0 | C0:5769 | 153 | `exact` | yes | `unknown/C0/C056D0.asm` | `` | `OR_CollisionVerticalEdgeB` |
| 133 | C0:5769 | C0:57E8 | 127 | `exact` | yes | `unknown/C0/C05769.asm` | `` | `Probe_SurfaceMaskCollisionSamples` |
| 134 | C0:57E8 | C0:583C | 84 | `exact` | yes | `unknown/C0/C057E8.asm` | `` | `Resolve_SurfaceMask0007` |
| 135 | C0:583C | C0:5890 | 84 | `exact` | yes | `unknown/C0/C0583C.asm` | `` | `Resolve_SurfaceMask0038` |
| 136 | C0:5890 | C0:59EF | 351 | `exact` | yes | `unknown/C0/C05890.asm` | `` | `Resolve_SurfaceMask0009` |
| 137 | C0:59EF | C0:5B4E | 351 | `exact` | yes | `unknown/C0/C059EF.asm` | `` | `Resolve_SurfaceMask0024` |
| 138 | C0:5B4E | C0:5B7B | 45 | `exact` | yes | `unknown/C0/C05B4E.asm` | `` | `Validate_SingleSurfaceModeAgainstMask` |
| 139 | C0:5B7B | C0:5CD7 | 348 | `exact` | yes | `unknown/C0/C05B7B.asm` | `UNKNOWN_C05B7B` | `Resolve_MovementSurfaceCollision` |
| 140 | C0:5CD7 | C0:5D8B | 180 | `exact` | yes | `unknown/C0/C05CD7.asm` | `UNKNOWN_C05CD7` | `Probe_FootprintCollisionEdges` |
| 141 | C0:5D8B | C0:5DE7 | 92 | `exact` | yes | `unknown/C0/C05D8B.asm` | `UNKNOWN_C05D8B` | `Probe_FullFootprintCollision` |
| 142 | C0:5DE7 | C0:5E3B | 84 | `exact` | yes | `unknown/C0/C05DE7.asm` | `UNKNOWN_C05DE7` | `Classify_EntityTerrainCompatibility` |
| 143 | C0:5E3B | C0:5E76 | 59 | `exact` | yes | `unknown/C0/C05E3B.asm` | `` | `Update_SlotCollisionCache` |
| 144 | C0:5E76 | C0:5E82 | 12 | `exact` | yes | `unknown/C0/C05E76.asm` | `UNKNOWN_C05E76` | `Update_CurrentSlotCollisionCache` |
| 145 | C0:5E82 | C0:5ECE | 76 | `exact` | yes | `unknown/C0/C05E82.asm` | `UNKNOWN_C05E82` | `Update_CurrentSlotCollisionCache_WithTerrainCompatibility` |
| 146 | C0:5ECE | C0:5F33 | 101 | `exact` | yes | `unknown/C0/C05ECE.asm` | `UNKNOWN_C05ECE` | `Update_CurrentSlotCollisionCache_FromHorizontalEdges` |
| 147 | C0:5F33 | C0:5F82 | 79 | `exact` | yes | `unknown/C0/C05F33.asm` | `UNKNOWN_C05F33` | `Probe_FootprintVerticalEdges` |
| 148 | C0:5F82 | C0:5FD1 | 79 | `exact` | yes | `unknown/C0/C05F82.asm` | `UNKNOWN_C05F82` | `Probe_FootprintHorizontalEdges` |
| 149 | C0:5FD1 | C0:5FF6 | 37 | `exact` | yes | `unknown/C0/C05FD1.asm` | `` | `Read_CenteredCollisionTile` |
| 150 | C0:5FF6 | C0:613C | 326 | `exact` | yes | `overworld/npc_collision_check.asm` | `NPC_COLLISION_CHECK` | `Find_OverlappingEntitySlot` |
| 151 | C0:613C | C0:6267 | 299 | `exact` | yes | `unknown/C0/C0613C.asm` | `UNKNOWN_C0613C` | `Update_SlotNeighborCache_BroadScan` |
| 152 | C0:6267 | C0:6478 | 529 | `exact` | yes | `unknown/C0/C06267.asm` | `UNKNOWN_C06267` | `Update_SlotNeighborCache_PriorityScan` |
| 153 | C0:6478 | C0:64A6 | 46 | `exact` | yes | `unknown/C0/C06478.asm` | `UNKNOWN_C06478` | `Update_CurrentSlotNeighborCache_Priority` |
| 154 | C0:64A6 | C0:64E3 | 61 | `exact` | yes | `unknown/C0/C064A6.asm` | `UNKNOWN_C064A6` | `Update_CurrentSlotNeighborCache_Broad` |
| 155 | C0:64D4 | C0:64E3 | 15 | `exact` | yes | `unknown/C0/C064D4.asm` | `UNKNOWN_C064D4` | `` |
| 156 | C0:64E3 | C0:65C2 | 223 | `exact` | yes | `unknown/C0/C064E3.asm` | `UNKNOWN_C064E3` | `Enqueue_MovementRecord` |
| 157 | C0:6537 | C0:654E | 23 | `exact` | yes | `unknown/C0/C06537.asm` | `UNKNOWN_C06537` | `` |
| 158 | C0:654E | C0:6578 | 42 | `exact` | yes | `unknown/C0/C0654E.asm` | `UNKNOWN_C0654E` | `` |
| 159 | C0:6578 | C0:65A3 | 43 | `exact` | yes | `unknown/C0/C06578.asm` | `UNKNOWN_C06578` | `` |
| 160 | C0:65A3 | C0:65C2 | 31 | `exact` | yes | `unknown/C0/C065A3.asm` | `UNKNOWN_C065A3` | `` |
| 161 | C0:65C2 | C0:69F7 | 1077 | `exact` | yes | `unknown/C0/C065C2.asm` | `UNKNOWN_C065C2` | `Probe_Type6DoorCandidate` |
| 162 | C0:69F7 | C0:6A07 | 16 | `exact` | yes | `overworld/screen_transition.asm` | `UNKNOWN_C069F7` | `Get_CurrentPositionMusicOrAreaId` |
| 163 | C0:6A07 | C0:6A1B | 20 | `exact` | yes | `overworld/get_screen_transition_sound_effect.asm` | `UNKNOWN_C06A07` | `Apply_CurrentPositionMusicOrAreaId` |
| 164 | C0:68F4 | C0:69AF | 187 | `exact` | yes | `unknown/C0/C068F4.asm` | `UNKNOWN_C068F4` | `` |
| 165 | C0:69AF |  | 0 | `open` |  | `unknown/C0/C069AF.asm` | `UNKNOWN_C069AF` | `` |
| 166 |  |  | 0 | `open` |  | `overworld/change_music_5DD6.asm` | `CHANGE_MUSIC_5DD6` | `` |
| 167 | C0:69F7 | C0:6A07 | 16 | `exact` | yes | `unknown/C0/C069F7.asm` | `UNKNOWN_C069F7` | `Get_CurrentPositionMusicOrAreaId` |
| 168 | C0:6A07 | C0:6A1B | 20 | `exact` | yes | `unknown/C0/C06A07.asm` | `UNKNOWN_C06A07` | `Apply_CurrentPositionMusicOrAreaId` |
| 169 | C0:6A1B | C0:6A8B | 112 | `exact` | yes | `unknown/C0/C06A1B.asm` | `` | `MovementTriggerType0_QueueDoorDestination` |
| 170 | C0:6A8B | C0:6A8E | 3 | `exact` | yes | `unknown/C0/C06A8B.asm` | `` | `MovementTriggerType5Or7_NoOp` |
| 171 | C0:6A8E | C0:6A91 | 3 | `exact` | yes | `unknown/C0/C06A8E.asm` | `` | `MovementTriggerType6_NoOp` |
| 172 | C0:6A91 | C0:6ACA | 57 | `exact` | yes | `unknown/C0/C06A91.asm` | `` | `MovementTriggerType1_SetState07Or08` |
| 173 | C0:6ACA | C0:6B21 | 87 | `exact` | yes | `unknown/C0/C06ACA.asm` | `` | `MovementTriggerType2_QueueDoorTransition` |
| 174 | C0:6B21 | C0:6B3D | 28 | `exact` | yes | `overworld/spawn_buzz_buzz.asm` | `SPAWN_BUZZ_BUZZ` | `RunPostTransitionScriptHookAndSelectorPass` |
| 175 | C0:6B3D | C0:6BFF | 194 | `exact` | yes | `unknown/C0/C06B3D.asm` | `UNKNOWN_C06B3D` | `PreserveDeferredScriptPointersAcrossTransition` |
| 176 | C0:6BFF | C0:6E1A | 539 | `exact` | yes | `overworld/door_transition.asm` | `` | `RunDeferredScriptPointerAndRefreshTransitionState` |
| 177 | C0:6E02 | C0:6E1A | 24 | `exact` | yes | `data/unknown/C06E02.asm` | `UNKNOWN_C06E02` | `` |
| 178 | C0:6E1A | C0:6E2C | 18 | `exact` | yes | `unknown/C0/C06E1A.asm` | `UNKNOWN_C06E1A` | `Reset_StagedMovementState` |
| 179 | C0:6E2C | C0:6E4A | 30 | `exact` | yes | `unknown/C0/C06E2C.asm` | `UNKNOWN_C06E2C` | `TimerCallback_CommitStagedPosition_State0C` |
| 180 | C0:6E4A | C0:6E6E | 36 | `exact` | yes | `unknown/C0/C06E4A.asm` | `UNKNOWN_C06E4A` | `TimerCallback_CommitStagedPosition_ClearMotion` |
| 181 | C0:6E6E | C0:6F68 | 250 | `exact` | yes | `unknown/C0/C06E6E.asm` | `` | `MovementTriggerType3_QueueOffsetStep` |
| 182 | C0:6F82 | C0:6FED | 107 | `exact` | yes | `unknown/C0/C06F82.asm` | `UNKNOWN_C06F82` | `TimerCallback_WaitForStagedY_State0D` |
| 183 | C0:6FED | C0:705F | 114 | `exact` | yes | `unknown/C0/C06FED.asm` | `UNKNOWN_C06FED` | `TimerCallback_WaitForStagedY_ClearMotion` |
| 184 | C0:705F | C0:70CB | 108 | `exact` | yes | `unknown/C0/C0705F.asm` | `` | `Select_StagedMovementFacing` |
| 185 | C0:70CB | C0:7180 | 181 | `exact` | yes | `unknown/C0/C070CB.asm` | `` | `Queue_StagedMovementFromGridCoords` |
| 186 | C0:7180 | C0:71D1 | 81 | `exact` | yes | `overworld/disable_hotspot.asm` | `DISABLE_HOTSPOT` | `Arm_StagedMovementTimerFromTable48E6B` |
| 187 | C0:71D1 | C0:73C0 | 495 | `exact` | yes | `overworld/reload_hotspots.asm` | `RELOAD_HOTSPOTS` | `Arm_StagedMovementTimerFromDirectionTables` |
| 188 | C0:73C0 | C0:7477 | 183 | `exact` | yes | `overworld/activate_hotspot.asm` | `UNKNOWN_C073C0` | `Check_MovementBoundaryTrigger` |
| 189 | C0:73C0 | C0:7477 | 183 | `exact` | yes | `unknown/C0/C073C0.asm` | `UNKNOWN_C073C0` | `Check_MovementBoundaryTrigger` |
| 190 | C0:7477 | C0:7526 | 175 | `exact` | yes | `unknown/C0/C07477.asm` | `UNKNOWN_C07477` | `Lookup_MovementTriggerType` |
| 191 | C0:7526 | C0:75DD | 183 | `exact` | yes | `unknown/C0/C07526.asm` | `UNKNOWN_C07526` | `Dispatch_MovementHelperFromLookup` |
| 192 | C0:75DD | C0:778A | 429 | `exact` | yes | `overworld/process_queued_interactions.asm` | `PROCESS_QUEUED_INTERACTIONS` | `Consume_MovementRecordQueue` |
| 193 | C0:769C | C0:76C8 | 44 | `exact` | yes | `unknown/C0/C0769C.asm` | `UNKNOWN_C0769C` | `` |
| 194 | C0:76C8 | C0:7716 | 78 | `exact` | yes | `unknown/C0/C076C8.asm` | `UNKNOWN_C076C8` | `` |
| 195 | C0:7716 | C0:777A | 100 | `exact` | yes | `unknown/C0/C07716.asm` | `UNKNOWN_C07716` | `` |
| 196 | C0:777A | C0:778A | 16 | `exact` | yes | `unknown/C0/C0777A.asm` | `UNKNOWN_C0777A` | `` |
| 197 | C0:778A | C0:780F | 133 | `exact` | yes | `unknown/C0/C0778A.asm` | `UNKNOWN_C0778A` | `Update_CurrentSlotOrbitOffsetFromLeader` |
| 198 | C0:780F | C0:7994 | 389 | `exact` | yes | `unknown/C0/C0780F.asm` | `UNKNOWN_C0780F` | `ResolveVisualSelectorRowToPoseIndex` |
| 199 | C0:79EC | C0:7A31 | 69 | `exact` | yes | `unknown/C0/C079EC.asm` | `UNKNOWN_C079EC` | `` |
| 200 | C0:7A31 | C0:7B52 | 289 | `exact` | yes | `unknown/C0/C07A31.asm` | `UNKNOWN_C07A31` | `Set_SlotOverlayFlag4000IfRequested` |
| 201 | C0:7A56 | C0:7B52 | 252 | `exact` | yes | `unknown/C0/C07A56.asm` | `UNKNOWN_C07A56` | `` |
| 202 | C0:7B52 | C0:8180 | 1582 | `exact` | yes | `unknown/C0/C07B52.asm` | `UNKNOWN_C07B52` | `Refresh_VisibleEntityScreenPositions` |
| 203 | C0:7C5B |  | 0 | `open` |  | `unknown/C0/C07C5B.asm` | `UNKNOWN_C07C5B` | `` |
| 204 |  |  | 0 | `open` |  | `system/strcat.asm` | `STRCAT` | `` |
| 205 |  |  | 0 | `open` |  | `system/reset.asm` | `RESET` | `` |
| 206 |  |  | 0 | `open` |  | `system/reset_vector.asm` | `RESET_VECTOR` | `` |
| 207 |  |  | 0 | `open` |  | `system/nmi_vector.asm` | `NMI_VECTOR` | `` |
| 208 |  |  | 0 | `open` |  | `system/irq_vector.asm` | `IRQ_VECTOR` | `` |
| 209 |  |  | 0 | `open` |  | `system/irq_nmi.asm` | `` | `` |
| 210 |  |  | 0 | `open` |  | `system/test_sram_size.asm` | `TEST_SRAM_SIZE` | `` |
| 211 | C0:83B8 | C0:83C1 | 9 | `exact` | yes | `unknown/C0/C083B8.asm` | `UNKNOWN_C083B8` | `Clear_InputPlaybackOrRecordStream` |
| 212 | C0:83C1 | C0:83E3 | 34 | `exact` | yes | `unknown/C0/C083C1.asm` | `UNKNOWN_C083C1` | `Start_InputRecordStream` |
| 213 | C0:83E3 | C0:841B | 56 | `exact` | yes | `unknown/C0/C083E3.asm` | `UNKNOWN_C083E3` | `Install_InputPlaybackStream` |
| 214 | C0:841B | C0:8456 | 59 | `exact` | yes | `system/read_joypad.asm` | `` | `Advance_InputPlaybackStream` |
| 215 | C0:8456 | C0:8496 | 64 | `exact` | yes | `unknown/C0/C08456.asm` | `` | `Advance_InputRecordStream` |
| 216 | C0:8496 | C0:8501 | 107 | `exact` | yes | `unknown/C0/C08496.asm` | `` | `Poll_FrameInputAndStreams` |
| 217 | C0:8501 | C0:8518 | 23 | `exact` | yes | `system/process_sfx_queue.asm` | `` | `Nmi_ServiceAudioQueue` |
| 218 | C0:8518 | C0:851B | 3 | `exact` | yes | `system/execute_irq_callback.asm` | `` | `Frame_CallbackDispatcher` |
| 219 | C0:851B | C0:851C | 1 | `exact` | yes | `system/default_irq_callback.asm` | `` | `Frame_CallbackReturn` |
| 220 | C0:851C | C0:8522 | 6 | `exact` | yes | `system/set_irq_callback.asm` | `SET_IRQ_CALLBACK` | `Set_FrameCallbackPtr` |
| 221 | C0:8522 | C0:8529 | 7 | `exact` | yes | `system/reset_irq_callback.asm` | `RESET_IRQ_CALLBACK` | `Reset_FrameCallbackToDefault` |
| 222 | C0:8529 | C0:8573 | 74 | `exact` | yes | `unknown/C0/C08529.asm` | `UNKNOWN_C08529` | `Copy_RecordBlockAndSetTransferFlag` |
| 223 | C0:856B | C0:8573 | 8 | `exact` | yes | `unknown/C0/C0856B.asm` | `UNKNOWN_C0856B` | `` |
| 224 | C0:8573 | C0:8616 | 163 | `exact` | yes | `unknown/C0/C08573.asm` | `UNKNOWN_C08573` | `Submit_TransferDescriptorList` |
| 225 | C0:8616 | C0:8643 | 45 | `exact` | yes | `system/transfer_to_vram.asm` | `TRANSFER_TO_VRAM` | `QueueVramTransfer_FromDpSource` |
| 226 | C0:8643 | C0:865F | 28 | `exact` | yes | `system/prepare_vram_copy.asm` | `PREPARE_VRAM_COPY` | `SubmitQueuedOrImmediateVramTransfer` |
| 227 | C0:865F | C0:8756 | 247 | `exact` | yes | `system/copy_to_vram_redirect.asm` | `` | `Submit_TransferDescriptorOrImmediateDma` |
| 228 | C0:8756 | C0:878B | 53 | `exact` | yes | `system/copy_to_vram.asm` | `` | `Wait_OneFrameAndPollInput` |
| 229 | C0:878B | C0:87AB | 32 | `exact` | yes | `system/sbrk.asm` | `UNKNOWN_C0878B` | `Wait_Frames_CountA` |
| 230 | C0:87AB | C0:886C | 193 | `exact` | yes | `system/enable_nmi_joypad.asm` | `ENABLE_NMI_JOYPAD` | `Update_DisplayNibble10From0D` |
| 231 | C0:8726 | C0:8744 | 30 | `exact` | yes | `unknown/C0/C08726.asm` | `UNKNOWN_C08726` | `` |
| 232 | C0:8744 |  | 0 | `open` |  | `unknown/C0/C08744.asm` | `UNKNOWN_C08744` | `` |
| 233 |  |  | 0 | `open` |  | `system/wait_until_next_frame.asm` | `WAIT_UNTIL_NEXT_FRAME` | `` |
| 234 | C0:878B | C0:87AB | 32 | `exact` | yes | `unknown/C0/C0878B.asm` | `UNKNOWN_C0878B` | `Wait_Frames_CountA` |
| 235 | C0:87AB | C0:886C | 193 | `exact` | yes | `system/set_inidisp_far.asm` | `SET_INIDISP_FAR` | `Update_DisplayNibble10From0D` |
| 236 | C0:886C | C0:887A | 14 | `exact` | yes | `system/set_inidisp.asm` | `` | `Set_DisplayWaitCounter` |
| 237 | C0:887A | C0:888B | 17 | `exact` | yes | `unknown/C0/C087AB_redirect.asm` | `` | `Set_NegatedDisplayWaitCounter` |
| 238 | C0:87AB | C0:886C | 193 | `exact` | yes | `unknown/C0/C087AB.asm` | `` | `Update_DisplayNibble10From0D` |
| 239 | C0:886C | C0:887A | 14 | `exact` | yes | `system/fade_in_with_mosaic.asm` | `FADE_IN_WITH_MOSAIC` | `Set_DisplayWaitCounter` |
| 240 | C0:887A | C0:888B | 17 | `exact` | yes | `system/fade_out_with_mosaic.asm` | `FADE_OUT_WITH_MOSAIC` | `Set_NegatedDisplayWaitCounter` |
| 241 | C0:888B | C0:88A5 | 26 | `exact` | yes | `system/fade_in.asm` | `UNKNOWN_C0888B` | `Run_DisplayWaitLoopUntilCounterClear` |
| 242 | C0:88A5 | C0:8B20 | 635 | `exact` | yes | `system/fade_out.asm` | `UNKNOWN_C088A5` | `Swap_DisplayFlag0B` |
| 243 | C0:888B | C0:88A5 | 26 | `exact` | yes | `unknown/C0/C0888B.asm` | `UNKNOWN_C0888B` | `Run_DisplayWaitLoopUntilCounterClear` |
| 244 | C0:88A5 | C0:8B20 | 635 | `exact` | yes | `unknown/C0/C088A5.asm` | `UNKNOWN_C088A5` | `Swap_DisplayFlag0B` |
| 245 | C0:8B20 | C0:8B8E | 110 | `exact` | yes | `system/oam_clear.asm` | `OAM_CLEAR` | `PublishRuntimeScrollShadowsToNmiBuffers` |
| 246 | C0:8B19 | C0:8B8E | 117 | `exact` |  | `unknown/C0/C08B19.asm` | `UNKNOWN_C08B19` | `` |
| 247 | C0:8B8E | C0:8C53 | 197 | `exact` | yes | `unknown/C0/C08B8E.asm` | `` | `Drain_DisplayRendererUpdateQueues` |
| 248 | C0:8C53 | C0:8C54 | 1 | `exact` | yes | `unknown/C0/C08C53.asm` | `` | `DisplayQueue_NoOpHook` |
| 249 | C0:8C54 | C0:8C58 | 4 | `exact` | yes | `unknown/C0/C08C54.asm` | `` | `Enqueue_DisplayRecord_FarWrapper` |
| 250 | C0:8C58 | C0:8CD5 | 125 | `exact` | yes | `unknown/C0/C08C58.asm` | `` | `Enqueue_DisplayRendererUpdateRecord` |
| 251 | C0:8CD5 | C0:8D79 | 164 | `exact` | yes | `data/C08C58_jumps.asm` | `UNKNOWN_C08CD5` | `Apply_DisplayRendererQueueRecord` |
| 252 | C0:8C6D | C0:8C87 | 26 | `exact` | yes | `unknown/C0/C08C6D.asm` | `` | `` |
| 253 | C0:8C87 | C0:8CA1 | 26 | `exact` | yes | `unknown/C0/C08C87.asm` | `UNKNOWN_C08C87` | `` |
| 254 | C0:8CA1 | C0:8CBB | 26 | `exact` | yes | `unknown/C0/C08CA1.asm` | `UNKNOWN_C08CA1` | `` |
| 255 | C0:8CBB | C0:8CD5 | 26 | `exact` | yes | `unknown/C0/C08CBB.asm` | `UNKNOWN_C08CBB` | `` |
| 256 | C0:8CD5 | C0:8D79 | 164 | `exact` | yes | `unknown/C0/C08CD5.asm` | `UNKNOWN_C08CD5` | `Apply_DisplayRendererQueueRecord` |
| 257 | C0:8D79 | C0:8D92 | 25 | `exact` | yes | `unknown/C0/C08D79.asm` | `UNKNOWN_C08D79` | `Update_BgModeRegisterFromQueue` |
| 258 | C0:8D92 | C0:8D9E | 12 | `exact` | yes | `system/set_oam_size.asm` | `SET_OAM_SIZE` | `Update_ObselRegisterFromQueue` |
| 259 | C0:8D9E | C0:8DDE | 64 | `exact` | yes | `system/set_bg1_vram_location.asm` | `SET_BG1_VRAM_LOCATION` | `Update_Bg1ScreenBaseRegistersFromQueue` |
| 260 | C0:8DDE | C0:8E1C | 62 | `exact` | yes | `system/set_bg2_vram_location.asm` | `SET_BG2_VRAM_LOCATION` | `Update_Bg2ScreenBaseRegistersFromQueue` |
| 261 | C0:8E1C | C0:8E5C | 64 | `exact` | yes | `system/set_bg3_vram_location.asm` | `SET_BG3_VRAM_LOCATION` | `Update_Bg3ScreenBaseRegistersFromQueue` |
| 262 | C0:8E5C | C0:8ED2 | 118 | `exact` | yes | `system/set_bg4_vram_location.asm` | `SET_BG4_VRAM_LOCATION` | `Update_Bg4ScreenBaseRegistersFromQueue` |
| 263 | C0:8ED2 | C0:8FC2 | 240 | `exact` | yes | `system/math/rand.asm` | `RAND` | `CopyWordsFromLongSource` |
| 264 | C0:8FC2 | C0:8FE6 | 36 | `exact` | yes | `system/memcpy16.asm` | `UNKNOWN_C08FC2` | `VRAMPortTripleTable_Tail` |
| 265 | C0:8FE6 | C0:8FF7 | 17 | `exact` | yes | `system/memcpy24.asm` | `MEMCPY24` | `Multiply8x8_ViaHardwareRegisters` |
| 266 | C0:8FF7 | C0:9032 | 59 | `exact` | yes | `system/memset16.asm` | `MEMSET16` | `Multiply16By8_ViaHardwareRegisters` |
| 267 | C0:9032 | C0:915B | 297 | `exact` | yes | `system/memset24.asm` | `MEMSET24` | `Multiply16By16_ViaHardwareRegisters` |
| 268 | C0:915B | C0:9279 | 286 | `exact` | yes | `system/strlen.asm` | `STRLEN` | `NormalizeFixedPointDivisionResult` |
| 269 | C0:9279 | C0:927C | 3 | `exact` | yes | `system/strcmp.asm` | `UNKNOWN_C09279` | `Dispatch_DelayedActionTarget` |
| 270 | C0:927C | C0:9321 | 165 | `exact` | yes | `system/setjmp.asm` | `UNKNOWN_C0927C` | `Init_DelayedActionPools` |
| 271 | C0:9321 | C0:941E | 253 | `exact` | yes | `system/longjmp.asm` | `LONGJMP` | `Init_DelayedActionState` |
| 272 | C0:941E | C0:943C | 30 | `exact` | yes | `system/wait_dma_finished.asm` | `WAIT_DMA_FINISHED` | `Init_TaskRecordScriptState` |
| 273 | C0:943C | C0:94AA | 110 | `exact` | yes | `data/palette_dma_parameters.asm` | `UNKNOWN_C0943C` | `MarkWorldObjectChainForSetup` |
| 274 | C0:94AA | C0:9506 | 92 | `exact` | yes | `data/dma_table.asm` | `` | `Process_ActiveTaskSlots` |
| 275 | C0:8FC2 | C0:8FE6 | 36 | `exact` | yes | `data/unknown/C08FC2.asm` | `UNKNOWN_C08FC2` | `VRAMPortTripleTable_Tail` |
| 276 | C0:8FE6 | C0:8FF7 | 17 | `exact` | yes | `system/math/mult8.asm` | `MULT8` | `Multiply8x8_ViaHardwareRegisters` |
| 277 | C0:8FF7 | C0:9032 | 59 | `exact` | yes | `system/math/mult168.asm` | `MULT168` | `Multiply16By8_ViaHardwareRegisters` |
| 278 | C0:9032 | C0:915B | 297 | `exact` | yes | `system/math/mult16.asm` | `MULT16` | `Multiply16By16_ViaHardwareRegisters` |
| 279 | C0:915B | C0:9279 | 286 | `exact` | yes | `system/math/mult32.asm` | `MULT32` | `NormalizeFixedPointDivisionResult` |
| 280 | C0:9279 | C0:927C | 3 | `exact` | yes | `system/math/division8.asm` | `UNKNOWN_C09279` | `Dispatch_DelayedActionTarget` |
| 281 | C0:927C | C0:9321 | 165 | `exact` | yes | `system/math/division16.asm` | `UNKNOWN_C0927C` | `Init_DelayedActionPools` |
| 282 | C0:9321 | C0:941E | 253 | `exact` | yes | `system/math/division32.asm` | `DIVISION32` | `Init_DelayedActionState` |
| 283 | C0:941E | C0:943C | 30 | `exact` | yes | `system/math/division8s.asm` | `DIVISION8S` | `Init_TaskRecordScriptState` |
| 284 | C0:943C | C0:94AA | 110 | `exact` | yes | `system/math/division16s.asm` | `UNKNOWN_C0943C` | `MarkWorldObjectChainForSetup` |
| 285 | C0:94AA | C0:9506 | 92 | `exact` | yes | `system/math/division32s.asm` | `DIVISION32S` | `Process_ActiveTaskSlots` |
| 286 | C0:9506 | C0:9558 | 82 | `exact` | yes | `system/math/modulus8s.asm` | `MODULUS8S` | `Run_ActionScriptFrame` |
| 287 | C0:9558 | C0:9ABD | 1381 | `exact` | yes | `system/math/modulus16s.asm` | `MODULUS16S` | `ScriptOpcodePointerTable` |
| 288 | C0:9ABD | C0:9AC5 | 8 | `exact` | yes | `system/math/modulus32s.asm` | `UNKNOWN_C09ABD` | `ScriptOpTargetMutationTable` |
| 289 | C0:9AC5 | C0:9ACC | 7 | `exact` | yes | `system/math/modulus8.asm` | `UNKNOWN_C09AC5` | `ScriptOp_MutateTarget_AND` |
| 290 | C0:9ACC | C0:9AD3 | 7 | `exact` | yes | `system/math/modulus16.asm` | `UNKNOWN_C09ACC` | `ScriptOp_MutateTarget_OR` |
| 291 | C0:9AD3 | C0:9ADB | 8 | `exact` | yes | `system/math/modulus32.asm` | `UNKNOWN_C09AD3` | `ScriptOp_MutateTarget_ADD` |
| 292 | C0:9ADB | C0:9AF9 | 30 | `exact` | yes | `system/math/asl16.asm` | `UNKNOWN_C09ADB` | `ScriptOp_MutateTarget_EOR` |
| 293 | C0:9AF9 | C0:9B09 | 16 | `exact` | yes | `system/math/asl32.asm` | `ASL32` | `EntityScriptVarTablePointers` |
| 294 | C0:9B09 | C0:9B0F | 6 | `exact` | yes | `system/math/asr8.asm` | `ASR8` | `ScriptOp_InitCurrentTaskRecordDefaults` |
| 295 | C0:9B0F | C0:9B1F | 16 | `exact` | yes | `system/math/asr16.asm` | `ASR16` | `ScriptOp_WriteImmediateByteToAddress` |
| 296 | C0:9B1F | C0:9B2C | 13 | `exact` | yes | `system/math/asr32.asm` | `ASR32` | `ScriptOp_WriteImmediateWordToAddress` |
| 297 | C0:9279 | C0:927C | 3 | `exact` | yes | `unknown/C0/C09279.asm` | `UNKNOWN_C09279` | `Dispatch_DelayedActionTarget` |
| 298 | C0:927C | C0:9321 | 165 | `exact` | yes | `unknown/C0/C0927C.asm` | `UNKNOWN_C0927C` | `Init_DelayedActionPools` |
| 299 | C0:9321 | C0:941E | 253 | `exact` | yes | `overworld/init_entity.asm` | `INIT_ENTITY` | `Init_DelayedActionState` |
| 300 | C0:943C | C0:94AA | 110 | `exact` | yes | `unknown/C0/C0943C.asm` | `UNKNOWN_C0943C` | `MarkWorldObjectChainForSetup` |
| 301 | C0:9451 |  | 0 | `open` |  | `unknown/C0/C09451.asm` | `UNKNOWN_C09451` | `` |
| 302 |  |  | 0 | `open` |  | `overworld/actionscript/run_actionscript_frame.asm` | `RUN_ACTIONSCRIPT_FRAME` | `` |
| 303 | C0:94D0 | C0:9506 | 54 | `exact` | yes | `unknown/C0/C094D0.asm` | `` | `` |
| 304 | C0:9506 | C0:9558 | 82 | `exact` | yes | `unknown/C0/C09506.asm` | `` | `Run_ActionScriptFrame` |
| 305 | C0:9558 | C0:9ABD | 1381 | `exact` | yes | `data/movement_control_codes_pointer_table.asm` | `` | `ScriptOpcodePointerTable` |
| 306 | C0:9ABD | C0:9AC5 | 8 | `exact` | yes | `overworld/actionscript/script/00.asm` | `UNKNOWN_C09ABD` | `ScriptOpTargetMutationTable` |
| 307 | C0:9AC5 | C0:9ACC | 7 | `exact` | yes | `overworld/actionscript/script/01.asm` | `UNKNOWN_C09AC5` | `ScriptOp_MutateTarget_AND` |
| 308 | C0:9ACC | C0:9AD3 | 7 | `exact` | yes | `overworld/actionscript/script/24.asm` | `UNKNOWN_C09ACC` | `ScriptOp_MutateTarget_OR` |
| 309 | C0:9AD3 | C0:9ADB | 8 | `exact` | yes | `overworld/actionscript/script/02.asm` | `UNKNOWN_C09AD3` | `ScriptOp_MutateTarget_ADD` |
| 310 | C0:9ADB | C0:9AF9 | 30 | `exact` | yes | `overworld/actionscript/script/19.asm` | `UNKNOWN_C09ADB` | `ScriptOp_MutateTarget_EOR` |
| 311 | C0:9AF9 | C0:9B09 | 16 | `exact` | yes | `overworld/actionscript/script/03.asm` | `` | `EntityScriptVarTablePointers` |
| 312 | C0:9B09 | C0:9B0F | 6 | `exact` | yes | `overworld/actionscript/script/1A.asm` | `` | `ScriptOp_InitCurrentTaskRecordDefaults` |
| 313 | C0:9B0F | C0:9B1F | 16 | `exact` | yes | `overworld/actionscript/script/1B.asm` | `` | `ScriptOp_WriteImmediateByteToAddress` |
| 314 | C0:9B1F | C0:9B2C | 13 | `exact` | yes | `overworld/actionscript/script/04.asm` | `` | `ScriptOp_WriteImmediateWordToAddress` |
| 315 | C0:9B2C | C0:9B44 | 24 | `exact` | yes | `overworld/actionscript/script/05.asm` | `` | `ScriptOp_BranchIfScratchZeroAndReturn` |
| 316 | C0:9B44 | C0:9B4D | 9 | `exact` | yes | `overworld/actionscript/script/06.asm` | `` | `ScriptOp_BranchIfScratchNonzeroAndReturn` |
| 317 | C0:9B4D | C0:9B61 | 20 | `exact` | yes | `overworld/actionscript/script/3B_45.asm` | `` | `ScriptOp_InstallFarDataPointer` |
| 318 | C0:9B61 | C0:9B6B | 10 | `exact` | yes | `overworld/actionscript/script/28.asm` | `` | `ScriptOp_LoadScratchImmediateWord` |
| 319 | C0:9B6B | C0:9B79 | 14 | `exact` | yes | `overworld/actionscript/script/29.asm` | `` | `ScriptOp_LoadScratchFromAddress` |
| 320 | C0:9B79 | C0:9B91 | 24 | `exact` | yes | `overworld/actionscript/script/2A.asm` | `` | `ScriptOp_StoreScratchToEntityVar` |
| 321 | C0:9B91 | C0:9BA9 | 24 | `exact` | yes | `overworld/actionscript/script/3F_49.asm` | `` | `ScriptOp_LoadScratchFromEntityVar` |
| 322 | C0:9BA9 | C0:9BB4 | 11 | `exact` | yes | `overworld/actionscript/script/40_4A.asm` | `` | `ScriptOp_CopyScratchToWaitCounterIfNonzero` |
| 323 | C0:9BB4 | C0:9BCC | 24 | `exact` | yes | `overworld/actionscript/script/41_4B.asm` | `` | `ScriptOp_LoadWaitCounterFromEntityVar` |
| 324 | C0:9BCC | C0:9BE4 | 24 | `exact` | yes | `overworld/actionscript/script/2E.asm` | `` | `ScriptOp_LoadTaskField10F2FromEntityVar` |
| 325 | C0:9BE4 | C0:9BEE | 10 | `exact` | yes | `overworld/actionscript/script/2F.asm` | `` | `ScriptOp_InstallTaskCallback11E2` |
| 326 | C0:9BEE | C0:9BF8 | 10 | `exact` | yes | `overworld/actionscript/script/30.asm` | `` | `ScriptOp_InstallTaskCallback11A6` |
| 327 | C0:9BF8 | C0:9C02 | 10 | `exact` | yes | `overworld/actionscript/script/31.asm` | `` | `ScriptOp_InstallTaskCallback121E` |
| 328 | C0:9C02 | C0:9C57 | 85 | `exact` | yes | `overworld/actionscript/script/32.asm` | `` | `Alloc_TaskSlotOrFail` |
| 329 | C0:9C57 | C0:9C73 | 28 | `exact` | yes | `overworld/actionscript/script/33.asm` | `` | `Link_TaskSlotIntoActiveList` |
| 330 | C0:9C73 | C0:9C8F | 28 | `exact` | yes | `overworld/actionscript/script/34.asm` | `` | `Detach_TaskSlotLink` |
| 331 | C0:9C8F | C0:9C99 | 10 | `exact` | yes | `overworld/actionscript/script/35.asm` | `` | `Push_TaskSlotToFreeList` |
| 332 | C0:9C99 | C0:9CD7 | 62 | `exact` | yes | `overworld/actionscript/script/36.asm` | `` | `Restore_TaskRecordChain` |
| 333 | C0:9CD7 | C0:9D03 | 44 | `exact` | yes | `overworld/actionscript/script/2B.asm` | `UNKNOWN_C09CD7` | `Compact_TaskSlotFreeList` |
| 334 | C0:9D03 | C0:9D12 | 15 | `exact` | yes | `overworld/actionscript/script/2C.asm` | `` | `Pop_TaskRecordFromFreeList` |
| 335 | C0:9D12 | C0:9D1F | 13 | `exact` | yes | `overworld/actionscript/script/2D.asm` | `` | `Push_TaskRecordToFreeList` |
| 336 | C0:9D1F | C0:9D3E | 31 | `exact` | yes | `overworld/actionscript/script/37.asm` | `` | `Unlink_TaskRecordFromSlotChain` |
| 337 | C0:9D3E | C0:9D60 | 34 | `exact` | yes | `overworld/actionscript/script/38.asm` | `` | `Find_TaskRecordPredecessor` |
| 338 | C0:9D60 | C0:9D78 | 24 | `exact` | yes | `overworld/actionscript/script/39.asm` | `UNKNOWN_C09D60` | `Count_RecordLinksUntilY` |
| 339 | C0:9907 |  | 0 | `open` |  | `unknown/C0/C09907.asm` | `UNKNOWN_C09907` | `` |
| 340 |  |  | 0 | `open` |  | `overworld/actionscript/script/3A.asm` | `` | `` |
| 341 |  |  | 0 | `open` |  | `overworld/actionscript/script/43.asm` | `` | `` |
| 342 |  |  | 0 | `open` |  | `overworld/actionscript/script/42_4C.asm` | `` | `` |
| 343 |  |  | 0 | `open` |  | `overworld/actionscript/script/0A.asm` | `` | `` |
| 344 |  |  | 0 | `open` |  | `overworld/actionscript/script/0B.asm` | `` | `` |
| 345 |  |  | 0 | `open` |  | `overworld/actionscript/script/10.asm` | `` | `` |
| 346 |  |  | 0 | `open` |  | `overworld/actionscript/script/11.asm` | `` | `` |
| 347 |  |  | 0 | `open` |  | `overworld/actionscript/script/0C.asm` | `` | `` |
| 348 |  |  | 0 | `open` |  | `overworld/actionscript/script/07.asm` | `` | `` |
| 349 |  |  | 0 | `open` |  | `overworld/actionscript/script/13.asm` | `` | `` |
| 350 |  |  | 0 | `open` |  | `overworld/actionscript/script/08.asm` | `` | `` |
| 351 |  |  | 0 | `open` |  | `overworld/actionscript/script/09.asm` | `` | `` |
| 352 |  |  | 0 | `open` |  | `overworld/actionscript/script/3C_46.asm` | `` | `` |
| 353 |  |  | 0 | `open` |  | `overworld/actionscript/script/3D_47.asm` | `` | `` |
| 354 |  |  | 0 | `open` |  | `overworld/actionscript/script/3E_48.asm` | `` | `` |
| 355 |  |  | 0 | `open` |  | `overworld/actionscript/script/18.asm` | `` | `` |
| 356 |  |  | 0 | `open` |  | `overworld/actionscript/script/14.asm` | `` | `` |
| 357 |  |  | 0 | `open` |  | `overworld/actionscript/script/27.asm` | `` | `` |
| 358 |  |  | 0 | `open` |  | `overworld/actionscript/script/0D.asm` | `` | `` |
| 359 | C0:9ABD | C0:9AC5 | 8 | `exact` | yes | `data/unknown/C09ABD.asm` | `UNKNOWN_C09ABD` | `ScriptOpTargetMutationTable` |
| 360 | C0:9AC5 | C0:9ACC | 7 | `exact` | yes | `unknown/C0/C09AC5.asm` | `UNKNOWN_C09AC5` | `ScriptOp_MutateTarget_AND` |
| 361 | C0:9ACC | C0:9AD3 | 7 | `exact` | yes | `unknown/C0/C09ACC.asm` | `UNKNOWN_C09ACC` | `ScriptOp_MutateTarget_OR` |
| 362 | C0:9AD3 | C0:9ADB | 8 | `exact` | yes | `unknown/C0/C09AD3.asm` | `UNKNOWN_C09AD3` | `ScriptOp_MutateTarget_ADD` |
| 363 | C0:9ADB | C0:9AF9 | 30 | `exact` | yes | `unknown/C0/C09ADB.asm` | `UNKNOWN_C09ADB` | `ScriptOp_MutateTarget_EOR` |
| 364 | C0:9AF9 | C0:9B09 | 16 | `exact` | yes | `overworld/actionscript/script/0E.asm` | `` | `EntityScriptVarTablePointers` |
| 365 | C0:9B09 | C0:9B0F | 6 | `exact` | yes | `data/events/entity_script_var_tables.asm` | `` | `ScriptOp_InitCurrentTaskRecordDefaults` |
| 366 | C0:9B0F | C0:9B1F | 16 | `exact` | yes | `overworld/actionscript/script/0F.asm` | `` | `ScriptOp_WriteImmediateByteToAddress` |
| 367 | C0:9B1F | C0:9B2C | 13 | `exact` | yes | `overworld/actionscript/script/12.asm` | `` | `ScriptOp_WriteImmediateWordToAddress` |
| 368 | C0:9B2C | C0:9B44 | 24 | `exact` | yes | `overworld/actionscript/script/15.asm` | `` | `ScriptOp_BranchIfScratchZeroAndReturn` |
| 369 | C0:9B44 | C0:9B4D | 9 | `exact` | yes | `overworld/actionscript/script/16.asm` | `` | `ScriptOp_BranchIfScratchNonzeroAndReturn` |
| 370 | C0:9B4D | C0:9B61 | 20 | `exact` | yes | `overworld/actionscript/script/17.asm` | `` | `ScriptOp_InstallFarDataPointer` |
| 371 | C0:9B61 | C0:9B6B | 10 | `exact` | yes | `overworld/actionscript/script/1C.asm` | `` | `ScriptOp_LoadScratchImmediateWord` |
| 372 | C0:9B6B | C0:9B79 | 14 | `exact` | yes | `overworld/actionscript/script/1D.asm` | `` | `ScriptOp_LoadScratchFromAddress` |
| 373 | C0:9B79 | C0:9B91 | 24 | `exact` | yes | `overworld/actionscript/script/1E.asm` | `` | `ScriptOp_StoreScratchToEntityVar` |
| 374 | C0:9B91 | C0:9BA9 | 24 | `exact` | yes | `overworld/actionscript/script/1F.asm` | `` | `ScriptOp_LoadScratchFromEntityVar` |
| 375 | C0:9BA9 | C0:9BB4 | 11 | `exact` | yes | `overworld/actionscript/script/20.asm` | `` | `ScriptOp_CopyScratchToWaitCounterIfNonzero` |
| 376 | C0:9BB4 | C0:9BCC | 24 | `exact` | yes | `overworld/actionscript/script/44.asm` | `` | `ScriptOp_LoadWaitCounterFromEntityVar` |
| 377 | C0:9BCC | C0:9BE4 | 24 | `exact` | yes | `overworld/actionscript/script/21.asm` | `` | `ScriptOp_LoadTaskField10F2FromEntityVar` |
| 378 | C0:9BE4 | C0:9BEE | 10 | `exact` | yes | `overworld/actionscript/script/26.asm` | `` | `ScriptOp_InstallTaskCallback11E2` |
| 379 | C0:9BEE | C0:9BF8 | 10 | `exact` | yes | `overworld/actionscript/script/22.asm` | `` | `ScriptOp_InstallTaskCallback11A6` |
| 380 | C0:9BF8 | C0:9C02 | 10 | `exact` | yes | `overworld/actionscript/script/23.asm` | `` | `ScriptOp_InstallTaskCallback121E` |
| 381 | C0:9C02 | C0:9C57 | 85 | `exact` | yes | `overworld/actionscript/script/25.asm` | `` | `Alloc_TaskSlotOrFail` |
| 382 | C0:9C02 | C0:9C57 | 85 | `exact` | yes | `unknown/C0/C09C02.asm` | `` | `Alloc_TaskSlotOrFail` |
| 383 | C0:9C35 | C0:9C3B | 6 | `exact` | yes | `unknown/C0/C09C35.asm` | `UNKNOWN_C09C35` | `` |
| 384 | C0:9C3B | C0:9C57 | 28 | `exact` | yes | `unknown/C0/C09C3B.asm` | `` | `` |
| 385 | C0:9C57 | C0:9C73 | 28 | `exact` | yes | `unknown/C0/C09C57.asm` | `` | `Link_TaskSlotIntoActiveList` |
| 386 | C0:9C73 | C0:9C8F | 28 | `exact` | yes | `unknown/C0/C09C73.asm` | `` | `Detach_TaskSlotLink` |
| 387 | C0:9C8F | C0:9C99 | 10 | `exact` | yes | `unknown/C0/C09C8F.asm` | `` | `Push_TaskSlotToFreeList` |
| 388 | C0:9C99 | C0:9CD7 | 62 | `exact` | yes | `unknown/C0/C09C99.asm` | `` | `Restore_TaskRecordChain` |
| 389 | C0:9CB5 | C0:9CD7 | 34 | `exact` | yes | `unknown/C0/C09CB5.asm` | `` | `` |
| 390 | C0:9CD7 | C0:9D03 | 44 | `exact` | yes | `unknown/C0/C09CD7.asm` | `UNKNOWN_C09CD7` | `Compact_TaskSlotFreeList` |
| 391 | C0:9D03 | C0:9D12 | 15 | `exact` | yes | `unknown/C0/C09D03.asm` | `` | `Pop_TaskRecordFromFreeList` |
| 392 | C0:9D12 | C0:9D1F | 13 | `exact` | yes | `unknown/C0/C09D12.asm` | `` | `Push_TaskRecordToFreeList` |
| 393 | C0:9D1F | C0:9D3E | 31 | `exact` | yes | `unknown/C0/C09D1F.asm` | `` | `Unlink_TaskRecordFromSlotChain` |
| 394 | C0:9D3E | C0:9D60 | 34 | `exact` | yes | `unknown/C0/C09D3E.asm` | `` | `Find_TaskRecordPredecessor` |
| 395 | C0:9D60 | C0:9D78 | 24 | `exact` | yes | `unknown/C0/C09D60.asm` | `UNKNOWN_C09D60` | `Count_RecordLinksUntilY` |
| 396 | C0:9D78 | C0:9DA1 | 41 | `exact` | yes | `unknown/C0/C09D78.asm` | `UNKNOWN_C09D78` | `Select_NthTaskRecordInA` |
| 397 | C0:9DA1 | C0:9DAE | 13 | `exact` | yes | `overworld/actionscript/script/read8.asm` | `` | `Init_TaskRecordDefaults` |
| 398 | C0:9DAE | C0:9E0A | 92 | `exact` | yes | `overworld/actionscript/script/read8_copy.asm` | `UNKNOWN_C09DAE` | `Script_CreateTask_DefaultSlotRange` |
| 399 | C0:9E0A | C0:9E18 | 14 | `exact` | yes | `overworld/actionscript/script/read16.asm` | `` | `Script_CreateTask_WithSlotRange` |
| 400 | C0:9E18 | C0:9E25 | 13 | `exact` | yes | `overworld/actionscript/script/read16_copy.asm` | `` | `Script_CreateTask_OneSlotRange` |
| 401 | C0:9E25 | C0:9E3B | 22 | `exact` | yes | `overworld/actionscript/jump_to_loaded_movement_pointer.asm` | `` | `Script_RecreateTaskInOneSlotRange` |
| 402 | C0:9E3B | C0:9E71 | 54 | `exact` | yes | `overworld/actionscript/clear_sprite_tick_callback.asm` | `` | `Script_CreateTask_AbsolutePosition` |
| 403 | C0:9DAE | C0:9E0A | 92 | `exact` | yes | `unknown/C0/C09DAE.asm` | `UNKNOWN_C09DAE` | `Script_CreateTask_DefaultSlotRange` |
| 404 | C0:9E71 | C0:9E79 | 8 | `exact` | yes | `unknown/C0/C09E71.asm` | `UNKNOWN_C09E71` | `Script_SetupTaskPath92F5` |
| 405 | C0:9E79 | C0:9E8E | 21 | `exact` | yes | `unknown/C0/C09E79.asm` | `` | `Script_ReleaseTaskFromEntityVar` |
| 406 | C0:9E98 | C0:9EAC | 20 | `exact` | yes | `unknown/C0/C09E98.asm` | `UNKNOWN_C09E98` | `Script_ReleaseAllOtherTasks` |
| 407 | C0:9EAC | C0:9ECE | 34 | `exact` | yes | `unknown/C0/C09EAC.asm` | `UNKNOWN_C09EAC` | `Script_ReleaseTasksByStateExceptCurrent` |
| 408 | C0:9ECE | C0:9EFF | 49 | `exact` | yes | `unknown/C0/C09ECE.asm` | `UNKNOWN_C09ECE` | `Script_SetupTaskWithThreeParameters` |
| 409 | C0:9EFF | C0:9F08 | 9 | `exact` | yes | `unknown/C0/C09EFF.asm` | `UNKNOWN_C09EFF` | `Resolve_ActiveSlotPositionContext` |
| 410 | C0:9F3B | C0:9F43 | 8 | `exact` | yes | `unknown/C0/C09F3B.asm` | `UNKNOWN_C09F3B` | `Freeze_AllActiveTasksExceptMarked` |
| 411 | C0:9F71 | C0:9F82 | 17 | `exact` | yes | `unknown/C0/C09F71.asm` | `UNKNOWN_C09F71` | `Restore_TaskFlagsFromFreezeSnapshot` |
| 412 | C0:9F82 | C0:9FA8 | 38 | `exact` | yes | `overworld/actionscript/choose_random.asm` | `CHOOSE_RANDOM` | `ChooseRandomScriptWord` |
| 413 | C0:9FA8 | C0:9FAE | 6 | `exact` | yes | `unknown/C0/C09FA8.asm` | `UNKNOWN_C09FA8` | `ChooseRandomScriptByte` |
| 414 | C0:9FAE | C0:9FBB | 13 | `exact` | yes | `overworld/actionscript/fade_in.asm` | `FADE_IN` | `ActionScript_FadeInWrapper` |
| 415 | C0:9FBB | C0:9FC8 | 13 | `exact` | yes | `overworld/actionscript/fade_out.asm` | `FADE_OUT` | `ActionScript_FadeOutWrapper` |
| 416 | C0:9FAE | C0:9FBB | 13 | `exact` | yes | `unknown/C0/C09FAE.asm` | `` | `ActionScript_FadeInWrapper` |
| 417 | C0:9FF1 | C0:A00C | 27 | `exact` | yes | `unknown/C0/C09FF1.asm` | `UNKNOWN_C09FF1` | `Integrate_XYAndZVelocity_WithSpriteRefresh` |
| 418 | C0:A00C | C0:A023 | 23 | `exact` | yes | `unknown/C0/C0A00C.asm` | `UNKNOWN_C0A00C` | `Integrate_XYAndZVelocity` |
| 419 | C0:A023 | C0:A03A | 23 | `exact` | yes | `unknown/C0/C0A023.asm` | `` | `ProjectWorldToScreen_FromCamera31` |
| 420 | C0:A03A | C0:A055 | 27 | `exact` | yes | `unknown/C0/C0A03A.asm` | `UNKNOWN_C0A03A` | `ProjectWorldToScreen_FromCamera31AndHeight` |
| 421 | C0:A055 | C0:A06C | 23 | `exact` | yes | `unknown/C0/C0A055.asm` | `UNKNOWN_C0A055` | `ProjectWorldToScreen_FromCamera39` |
| 422 | C0:A06C | C0:A089 | 29 | `exact` | yes | `unknown/C0/C0A06C.asm` | `UNKNOWN_C0A06C` | `ProjectWorldToScreen_DirectCamera39Event` |
| 423 | C0:A089 | C0:A0A0 | 23 | `exact` | yes | `unknown/C0/C0A089.asm` | `UNKNOWN_C0A089` | `AddCamera39ToWorldPosition` |
| 424 | C0:A0A0 | C0:A0BB | 27 | `exact` | yes | `unknown/C0/C0A0A0.asm` | `UNKNOWN_C0A0A0` | `ProjectWorldToScreen_FromCamera39AndHeight` |
| 425 | C0:A0BB | C0:A0CA | 15 | `exact` | yes | `unknown/C0/C0A0BB.asm` | `UNKNOWN_C0A0BB` | `ProjectWorldToScreen_CopyWorld` |
| 426 | C0:A0CA | C0:A0E3 | 25 | `exact` | yes | `unknown/C0/C0A0CA.asm` | `` | `Run_TaskDataCallbackByIndex` |
| 427 | C0:A0E3 | C0:A0FA | 23 | `exact` | yes | `unknown/C0/C0A0E3.asm` | `` | `Run_CurrentTaskDataCallback` |
| 428 | C0:A0FA | C0:A152 | 88 | `exact` | yes | `unknown/C0/C0A0FA.asm` | `UNKNOWN_C0A0FA` | `Draw_TaskDataRecordAtIndex` |
| 429 | C0:A152 | C0:A156 | 4 | `exact` | yes | `system/check_hardware.asm` | `CHECK_HARDWARE` | `Lookup_CachedMapPropertyNibble_Far` |
| 430 | C0:A156 | C0:A1AE | 88 | `exact` | yes | `unknown/C0/C0A156_redirect.asm` | `` | `Lookup_CachedMapPropertyNibble` |
| 431 | C0:A156 | C0:A1AE | 88 | `exact` | yes | `unknown/C0/C0A156.asm` | `` | `Lookup_CachedMapPropertyNibble` |
| 432 | C0:A1AE | C0:A1CE | 32 | `exact` | yes | `data/unknown/C0A1AE.asm` | `` | `CachedMapPropertyShiftDispatchTable` |
| 433 | C0:A1CE | C0:A1D0 | 2 | `exact` | yes | `unknown/C0/C0A1CE.asm` | `UNKNOWN_C0A1CE` | `SelectPackedMapPropertyBits0` |
| 434 | C0:A1F2 | C0:A20C | 26 | `exact` | yes | `unknown/C0/C0A1F2.asm` | `UNKNOWN_C0A1F2` | `Copy_MapBufferPageToWorkBuffer` |
| 435 | C0:A20C | C0:A21C | 16 | `exact` | yes | `data/unknown/C0A20C.asm` | `UNKNOWN_C0A20C` | `MapBufferPageSourcePointerTable` |
| 436 | C0:A21C | C0:A230 | 20 | `exact` | yes | `unknown/C0/C0A21C.asm` | `UNKNOWN_C0A21C` | `FindActiveTaskByField2C9A` |
| 437 | C0:A230 | C0:A254 | 36 | `exact` | yes | `unknown/C0/C0A230.asm` | `UNKNOWN_C0A230` | `AddLinkedSlotPositionToCurrentProjection` |
| 438 | C0:A254 | C0:A26B | 23 | `exact` | yes | `unknown/C0/C0A254.asm` | `UNKNOWN_C0A254` | `ProjectSlotWorldPositionFromCamera31` |
| 439 | C0:A26B | C0:A2AB | 64 | `exact` | yes | `unknown/C0/C0A26B.asm` | `UNKNOWN_C0A26B` | `PhysicsCallback_TargetComparisonAndProjection` |
| 440 | C0:A2AB | C0:A2B7 | 12 | `exact` | yes | `data/unknown/C0A2AB.asm` | `UNKNOWN_C0A2AB` | `PhysicsCallbackDistanceThresholdTableA` |
| 441 | C0:A2B7 | C0:A2E1 | 42 | `exact` | yes | `unknown/C0/C0A2B7.asm` | `UNKNOWN_C0A2B7` | `CompareProjectedXThenYDistanceThreshold` |
| 442 | C0:A2E1 | C0:A30B | 42 | `exact` | yes | `unknown/C0/C0A2E1.asm` | `UNKNOWN_C0A2E1` | `CompareProjectedYThenXDistanceThreshold` |
| 443 | C0:A30B | C0:A317 | 12 | `exact` | yes | `data/unknown/C0A30B.asm` | `UNKNOWN_C0A30B` | `PhysicsCallbackDistanceThresholdTableB` |
| 444 | C0:A317 | C0:A350 | 57 | `exact` | yes | `unknown/C0/C0A317.asm` | `UNKNOWN_C0A317` | `CompareWorldXDistanceAndNormalizeDelta` |
| 445 | C0:A350 | C0:A360 | 16 | `exact` | yes | `data/unknown/C0A350.asm` | `` | `PhysicsCallbackComparisonDispatchTable` |
| 446 | C0:A360 | C0:A37A | 26 | `exact` | yes | `unknown/C0/C0A360.asm` | `UNKNOWN_C0A360` | `UpdatePosition_WhenNoNeighbor_WithSpriteRefresh` |
| 447 | C0:A384 | C0:A39E | 26 | `exact` | yes | `unknown/C0/C0A384.asm` | `UNKNOWN_C0A384` | `UpdatePosition_WhenNoNeighbor` |
| 448 | C0:A3A4 | C0:A443 | 159 | `exact` | yes | `unknown/C0/C0A3A4.asm` | `` | `Build_DisplayRecordFromCurrentTaskData` |
| 449 | C0:A443 | C0:A48F | 76 | `exact` | yes | `unknown/C0/C0A443.asm` | `` | `RefreshCurrentSlotProfileIfCompositeKeyChanged` |
| 450 | C0:A56E | C0:A60B | 157 | `exact` | yes | `unknown/C0/C0A56E.asm` | `UNKNOWN_C0A56E` | `Generate_RenderDmaStripDescriptors` |
| 451 | C0:A60B | C0:A623 | 24 | `exact` | yes | `data/sprite_direction_mapping_4_direction.asm` | `SPRITE_DIRECTION_MAPPING_4_DIRECTION` | `VisualProfileDirectionOffsetTable` |
| 452 | C0:A623 | C0:A643 | 32 | `exact` | yes | `data/sprite_direction_mapping_8_direction.asm` | `SPRITE_DIRECTION_MAPPING_8_DIRECTION` | `VisualProfileSecondaryOffsetTable` |
| 453 | C0:A643 | C0:A651 | 14 | `exact` | yes | `system/math/rand_0_3.asm` | `UNKNOWN_C0A643` | `Script_SetDirectionClassAndField2C9A` |
| 454 | C0:A651 | C0:A65F | 14 | `exact` | yes | `system/math/rand_0_7.asm` | `RAND_0_7` | `Script_SetDirectionClassAndField1A86` |
| 455 | C0:A643 | C0:A651 | 14 | `exact` | yes | `unknown/C0/C0A643.asm` | `UNKNOWN_C0A643` | `Script_SetDirectionClassAndField2C9A` |
| 456 | C0:A651 | C0:A65F | 14 | `exact` | yes | `overworld/actionscript/set_direction8.asm` | `SET_DIRECTION8` | `Script_SetDirectionClassAndField1A86` |
| 457 | C0:A65F | C0:A66D | 14 | `exact` | yes | `overworld/actionscript/set_direction.asm` | `SET_DIRECTION` | `SetCurrentSlotDirectionClassIfActive` |
| 458 | C0:A66D | C0:A673 | 6 | `exact` | yes | `unknown/C0/C0A66D.asm` | `UNKNOWN_C0A66D` | `SetCurrentSlotDirectionClass` |
| 459 | C0:A673 | C0:A679 | 6 | `exact` | yes | `unknown/C0/C0A673.asm` | `UNKNOWN_C0A673` | `GetCurrentSlotDirectionClass` |
| 460 | C0:A679 | C0:A685 | 12 | `exact` | yes | `overworld/actionscript/set_surface_flags.asm` | `SET_SURFACE_FLAGS` | `Script_SetCurrentSlotDisplayControlBits` |
| 461 | C0:A685 | C0:A68B | 6 | `exact` | yes | `unknown/C0/C0A685.asm` | `UNKNOWN_C0A685` | `Script_SetCurrentSlotField2B32` |
| 462 | C0:A691 | C0:A697 | 6 | `exact` | yes | `unknown/C0/C0A691.asm` | `UNKNOWN_C0A691` | `GetCurrentSlotField2B32` |
| 463 | C0:A697 | C0:A6A2 | 11 | `exact` | yes | `unknown/C0/C0A697.asm` | `UNKNOWN_C0A697` | `Script_SetMovementStateC83B` |
| 464 | C0:A6A2 | C0:A6AD | 11 | `exact` | yes | `unknown/C0/C0A6A2.asm` | `UNKNOWN_C0A6A2` | `Script_SetMovementStateCA4E` |
| 465 | C0:A6AD | C0:A6B8 | 11 | `exact` | yes | `unknown/C0/C0A6AD.asm` | `UNKNOWN_C0A6AD` | `Script_SetMovementStateCBD3` |
| 466 | C0:A6B8 | C0:A6C5 | 13 | `exact` | yes | `unknown/C0/C0A6B8.asm` | `UNKNOWN_C0A6B8` | `GetCurrentSlotHasNoCachedNeighborFlag` |
| 467 | C0:A6C5 | C0:A6CB | 6 | `exact` | yes | `unknown/C0/C0A6C5.asm` | `UNKNOWN_C0A6C5` | `GetCurrentSlotCollisionFlags28DA` |
| 468 | C0:A6CB | C0:A6E3 | 24 | `exact` | yes | `unknown/C0/C0A6CB.asm` | `UNKNOWN_C0A6CB` | `GetCurrentSlotActivityState2C5E` |
| 469 | C0:A6E3 | C0:A6F7 | 20 | `exact` | yes | `overworld/actionscript/disable_current_entity_collision.asm` | `UNKNOWN_C0A6E3` | `WatchAndRefreshCompanionVisualPhase` |
| 470 | C0:A6F7 | C0:A750 | 89 | `exact` | yes | `overworld/actionscript/clear_current_entity_collision.asm` | `CLEAR_CURRENT_ENTITY_COLLISION` | `RefreshCompanionVisualOnSignatureChange` |
| 471 | C0:A6E3 | C0:A6F7 | 20 | `exact` | yes | `unknown/C0/C0A6E3.asm` | `UNKNOWN_C0A6E3` | `WatchAndRefreshCompanionVisualPhase` |
| 472 | C0:A780 | C0:A78F | 15 | `exact` | yes | `unknown/C0/C0A780.asm` | `UNKNOWN_C0A780` | `RefreshCompanionVisualProfileForEntry` |
| 473 | C0:A794 | C0:A841 | 173 | `exact` | yes | `unknown/C0/C0A794.asm` | `` | `RefreshCompanionVisualProfile_PhaseBiased` |
| 474 | C0:A841 | C0:A84C | 11 | `exact` | yes | `overworld/actionscript/disable_current_entity_collision2.asm` | `UNKNOWN_C0A841` | `Script_PlaySoundEffectParameter` |
| 475 | C0:A84C | C0:A857 | 11 | `exact` | yes | `overworld/actionscript/clear_current_entity_collision2.asm` | `UNKNOWN_C0A84C` | `ScriptWrapper_C21628_ReadWord` |
| 476 | C0:A841 | C0:A84C | 11 | `exact` | yes | `unknown/C0/C0A841.asm` | `UNKNOWN_C0A841` | `Script_PlaySoundEffectParameter` |
| 477 | C0:A84C | C0:A857 | 11 | `exact` | yes | `unknown/C0/C0A84C.asm` | `UNKNOWN_C0A84C` | `ScriptWrapper_C21628_ReadWord` |
| 478 | C0:A857 | C0:A864 | 13 | `exact` | yes | `unknown/C0/C0A857.asm` | `UNKNOWN_C0A857` | `ScriptWrapper_C2165E_ReadWordPreserveMode` |
| 479 | C0:A864 | C0:A86F | 11 | `exact` | yes | `unknown/C0/C0A864.asm` | `UNKNOWN_C0A864` | `Script_CopyRegistrySlotAnchorToCurrentSlot_ReadByte` |
| 480 | C0:A86F | C0:A87A | 11 | `exact` | yes | `unknown/C0/C0A86F.asm` | `UNKNOWN_C0A86F` | `Script_CopyPoseDescriptorSlotAnchorToCurrentSlot_ReadWord` |
| 481 | C0:A87A | C0:A88D | 19 | `exact` | yes | `unknown/C0/C0A87A.asm` | `UNKNOWN_C0A87A` | `Script_SetCameraRelativeAnchor_ReadTwoWords` |
| 482 | C0:A88D | C0:A8A0 | 19 | `exact` | yes | `unknown/C0/C0A88D.asm` | `UNKNOWN_C0A88D` | `ActionScript_QueueTextPointer` |
| 483 | C0:A8A0 | C0:A8B3 | 19 | `exact` | yes | `unknown/C0/C0A8A0.asm` | `UNKNOWN_C0A8A0` | `ScriptWrapper_C466F0_ReadWordByte` |
| 484 | C0:A8B3 | C0:A8C6 | 19 | `exact` | yes | `unknown/C0/C0A8B3.asm` | `UNKNOWN_C0A8B3` | `Script_SetStagedPositionOffset_ReadTwoWords` |
| 485 | C0:A8C6 | C0:A8D1 | 11 | `exact` | yes | `unknown/C0/C0A8C6.asm` | `UNKNOWN_C0A8C6` | `ScriptWrapper_C47143_Mode00` |
| 486 | C0:A8D1 | C0:A8DC | 11 | `exact` | yes | `unknown/C0/C0A8D1.asm` | `UNKNOWN_C0A8D1` | `ScriptWrapper_C47143_Mode10` |
| 487 | C0:A8DC | C0:A8E7 | 11 | `exact` | yes | `unknown/C0/C0A8DC.asm` | `UNKNOWN_C0A8DC` | `ScriptWrapper_C47143_Mode01` |
| 488 | C0:A8E7 | C0:A8EF | 8 | `exact` | yes | `unknown/C0/C0A8E7.asm` | `UNKNOWN_C0A8E7` | `ScriptWrapper_C472A8_Mode0` |
| 489 | C0:A8EF | C0:A8F7 | 8 | `exact` | yes | `unknown/C0/C0A8EF.asm` | `UNKNOWN_C0A8EF` | `ScriptWrapper_C472A8_Mode1` |
| 490 | C0:A8F7 | C0:A8FF | 8 | `exact` | yes | `overworld/actionscript/prepare_new_entity_at_self.asm` | `ACTIONSCRIPT_PREPARE_NEW_ENTITY_AT_SELF` | `ActionScript_PrepareNewEntityAtSelf` |
| 491 | C0:A8FF | C0:A907 | 8 | `exact` | yes | `overworld/actionscript/prepare_new_entity_at_party_leader.asm` | `ACTIONSCRIPT_PREPARE_NEW_ENTITY_AT_PARTY_LEADER` | `ActionScript_PrepareNewEntityAtPartyLeader` |
| 492 | C0:A907 | C0:A912 | 11 | `exact` | yes | `overworld/actionscript/prepare_new_entity_at_teleport_destination.asm` | `ACTIONSCRIPT_PREPARE_NEW_ENTITY_AT_TELEPORT_DESTINATION` | `ActionScript_PrepareNewEntityAtTeleportDestination` |
| 493 | C0:A912 | C0:A92D | 27 | `exact` | yes | `overworld/actionscript/prepare_new_entity.asm` | `ACTIONSCRIPT_PREPARE_NEW_ENTITY` | `ActionScript_PrepareNewEntity` |
| 494 | C0:A92D | C0:A938 | 11 | `exact` | yes | `unknown/C0/C0A92D.asm` | `UNKNOWN_C0A92D` | `Script_SetTargetToVisualTypeSlotPosition_ReadWord` |
| 495 | C0:A938 | C0:A943 | 11 | `exact` | yes | `unknown/C0/C0A938.asm` | `UNKNOWN_C0A938` | `Script_SetTargetToPoseDescriptorSlotPosition_ReadWord` |
| 496 | C0:A943 | C0:A94E | 11 | `exact` | yes | `overworld/actionscript/get_position_of_party_member.asm` | `ACTIONSCRIPT_GET_POSITION_OF_PARTY_MEMBER` | `ActionScript_GetPositionOfPartyMember` |
| 497 | C0:A94E | C0:A959 | 11 | `exact` | yes | `unknown/C0/C0A94E.asm` | `UNKNOWN_C0A94E` | `ScriptWrapper_C46984_ReadWord` |
| 498 | C0:A959 | C0:A964 | 11 | `exact` | yes | `unknown/C0/C0A959.asm` | `UNKNOWN_C0A959` | `ScriptWrapper_C469F1_ReadWord` |
| 499 | C0:A964 | C0:A977 | 19 | `exact` | yes | `unknown/C0/C0A964.asm` | `UNKNOWN_C0A964` | `ScriptWrapper_C47225_ReadTwoWords` |
| 500 | C0:A977 | C0:A98B | 20 | `exact` | yes | `battle/load_battlebg_movement.asm` | `` | `Movement_LoadBattleBg` |
| 501 | C0:A98B | C0:A99F | 20 | `exact` | yes | `unknown/C0/C0A98B.asm` | `UNKNOWN_C0A98B` | `ScriptWrapper_C46534_ReadThreeWords` |
| 502 | C0:A99F | C0:A9B3 | 20 | `exact` | yes | `unknown/C0/C0A99F.asm` | `UNKNOWN_C0A99F` | `ScriptWrapper_C4ECAD_ReadThreeWords` |
| 503 | C0:A9B3 | C0:A9CF | 28 | `exact` | yes | `unknown/C0/C0A9B3.asm` | `UNKNOWN_C0A9B3` | `ScriptWrapper_C4EBAD_ReadThreeWords` |
| 504 | C0:A9CF | C0:A9EB | 28 | `exact` | yes | `unknown/C0/C0A9CF.asm` | `UNKNOWN_C0A9CF` | `ScriptWrapper_C4EC05_ReadThreeWords` |
| 505 | C0:A9EB | C0:AA07 | 28 | `exact` | yes | `unknown/C0/C0A9EB.asm` | `UNKNOWN_C0A9EB` | `ScriptWrapper_C4EC52_ReadThreeWords` |
| 506 | C0:AA07 | C0:AA23 | 28 | `exact` | yes | `overworld/actionscript/fade_out_with_mosaic.asm` | `FADE_OUT_WITH_MOSAIC` | `ActionScript_FadeOutWithMosaic` |
| 507 | C0:AA23 | C0:AA3F | 28 | `exact` | yes | `unknown/C0/C0AA23.asm` | `UNKNOWN_C0AA23` | `ScriptWrapper_C47765_ReadTwoWords` |
| 508 | C0:AA3F | C0:AA6E | 47 | `exact` | yes | `unknown/C0/C0AA3F.asm` | `UNKNOWN_C0AA3F` | `Script_SetVisualSetupBytesByMode` |
| 509 | C0:AA6E | C0:AAA8 | 58 | `exact` | yes | `unknown/C0/C0AA6E.asm` | `UNKNOWN_C0AA6E` | `Script_ApplyCurrentSlotVisualCountdownState` |
| 510 | C0:AAAC | C0:AAB1 | 5 | `exact` | yes | `unknown/C0/C0AAAC.asm` | `UNKNOWN_C0AAAC` | `Script_RefreshCurrentSlotVisualProfile` |
| 511 | C0:AAB5 | C0:AACD | 24 | `exact` | yes | `unknown/C0/C0AAB5.asm` | `UNKNOWN_C0AAB5` | `ScriptWrapper_C497C0_ReadWordByteByte` |
| 512 | C0:AACD | C0:AAD1 | 4 | `exact` | yes | `unknown/C0/C0AACD.asm` | `UNKNOWN_C0AACD` | `ReturnX0002` |
| 513 | C0:AAD1 | C0:AAD5 | 4 | `exact` | yes | `unknown/C0/C0AAD1.asm` | `UNKNOWN_C0AAD1` | `ReturnX0004` |
| 514 | C0:AAD5 | C0:AAFD | 40 | `exact` | yes | `unknown/C0/C0AAD5.asm` | `UNKNOWN_C0AAD5` | `Script_CountdownThenJumpTarget` |
| 515 | C0:AAFD | C0:AB06 | 9 | `exact` | yes | `unknown/C0/C0AAFD.asm` | `UNKNOWN_C0AAFD` | `Script_ClearFrameCountdown` |
| 516 | C0:AB06 | C0:ABA8 | 162 | `exact` | yes | `audio/load_spc700_data.asm` | `LOAD_SPC700_DATA` | `LoadSpc700DataStream` |
| 517 | C0:ABA8 | C0:ABBD | 21 | `exact` | yes | `audio/wait_for_spc700.asm` | `` | `WaitForSpcReadyAndResetApuPorts` |
| 518 | C0:ABBD | C0:ABC6 | 9 | `exact` | yes | `unknown/C0/C0ABBD.asm` | `UNKNOWN_C0ABBD` | `SendApuPort0CommandByte` |
| 519 | C0:ABC6 | C0:ABE0 | 26 | `exact` | yes | `audio/stop_music.asm` | `STOP_MUSIC` | `StopMusicAndLatchNoTrack` |
| 520 | C0:ABE0 | C0:AC0C | 44 | `exact` | yes | `audio/play_sound.asm` | `PLAY_SOUND` | `QueueSoundEffectOrPlayApuPort3Cue` |
| 521 | C0:AC0C | C0:AC20 | 20 | `exact` | yes | `unknown/C0/C0AC0C.asm` | `UNKNOWN_C0AC0C` | `ToggleAndSendApuPort1Command` |
| 522 | C0:AC20 | C0:AC3A | 26 | `exact` | yes | `unknown/C0/C0AC20.asm` | `UNKNOWN_C0AC20` | `ReadApuPort0Byte` |
| 523 | C0:AC3A | C0:AC43 | 9 | `exact` | yes | `data/stereo_mono_data.asm` | `UNKNOWN_C0AC3A` | `SendApuPort2Byte` |
| 524 | C0:AC3A | C0:AC43 | 9 | `exact` | yes | `unknown/C0/C0AC3A.asm` | `UNKNOWN_C0AC3A` | `SendApuPort2Byte` |
| 525 | C0:AC43 | C0:AC68 | 37 | `exact` | yes | `unknown/C0/C0AC43.asm` | `UNKNOWN_C0AC43` | `SelectAndEmitBattleBgTransferDescriptors` |
| 526 | C0:AD56 | C0:AD8A | 52 | `exact` | yes | `unknown/C0/C0AD56.asm` | `` | `ExpandBattleBgTransferDescriptorStream` |
| 527 | C0:AD8A | C0:AD9F | 21 | `exact` | yes | `data/events/scripts/786.asm` | `EVENT_786` | `Event786_CurrentSlotOrbitScript` |
| 528 | C0:AD9F | C0:ADB2 | 19 | `exact` | yes | `unknown/C0/C0AD9F.asm` | `` | `WriteVramAddressFrom3B3C` |
| 529 | C0:ADB2 | C0:AE16 | 100 | `exact` | yes | `misc/battlebgs/do_battlebg_dma.asm` | `DO_BATTLEBG_DMA` | `ConfigureBattleBgDmaChannel` |
| 530 | C0:AE16 | C0:AE1D | 7 | `exact` | yes | `data/dma_flags.asm` | `DMA_FLAGS` | `DmaChannelFlagTable` |
| 531 | C0:AE1D | C0:AE26 | 9 | `exact` | yes | `data/dma_target_registers.asm` | `` | `BattleBgDmaBbusRegisterTable` |
| 532 | C0:AE26 | C0:AE34 | 14 | `exact` | yes | `data/unknown/C0AE26.asm` | `` | `BattleBgDmaSourceDescriptorTemplates` |
| 533 | C0:AE2D | C0:AE34 | 7 | `exact` | yes | `data/unknown/C0AE2D.asm` | `` | `` |
| 534 | C0:AE34 | C0:AE44 | 16 | `exact` | yes | `unknown/C0/C0AE34.asm` | `UNKNOWN_C0AE34` | `ClearPendingDmaChannelBit` |
| 535 | C0:AE44 | C0:AFCD | 393 | `exact` | yes | `data/unknown/C0AE44.asm` | `UNKNOWN_C0AE44` | `InverseDmaChannelMaskTable` |
| 536 | C0:AFCD | C0:B01A | 77 | `exact` | yes | `misc/battlebgs/load_bg_offset_parameters.asm` | `UNKNOWN_C0AFCD` | `ApplyBattleBgColourMathPreset` |
| 537 | C0:B01A | C0:B039 | 31 | `exact` | yes | `misc/battlebgs/load_bg_offset_parameters2.asm` | `LOAD_BG_OFFSET_PARAMETERS2` | `SetFixedColourRgbComponents` |
| 538 | C0:B039 | C0:B047 | 14 | `exact` | yes | `misc/battlebgs/prepare_bg_offset_tables.asm` | `PREPARE_BG_OFFSET_TABLES` | `SetColourAddSubModeRegisters` |
| 539 | C0:AFCD | C0:B01A | 77 | `exact` | yes | `unknown/C0/C0AFCD.asm` | `UNKNOWN_C0AFCD` | `ApplyBattleBgColourMathPreset` |
| 540 | C0:AFF1 |  | 0 | `open` |  | `data/unknown/C0AFF1.asm` | `UNKNOWN_C0AFF1` | `` |
| 541 |  |  | 0 | `open` |  | `system/set_coldata.asm` | `SET_COLDATA` | `` |
| 542 |  |  | 0 | `open` |  | `system/set_colour_addsub_mode.asm` | `SET_COLOUR_ADDSUB_MODE` | `` |
| 543 |  |  | 0 | `open` |  | `system/set_window_mask.asm` | `SET_WINDOW_MASK` | `` |
| 544 | C0:B0A6 | C0:B0AA | 4 | `exact` | yes | `data/unknown/C0B0A6.asm` | `UNKNOWN_C0B0A6` | `WindowMaskNibbleLookupTable` |
| 545 | C0:B0AA | C0:B0B8 | 14 | `exact` | yes | `unknown/C0/C0B0AA.asm` | `UNKNOWN_C0B0AA` | `ResetWindowLeftPositions` |
| 546 | C0:B0B8 | C0:B0EF | 55 | `exact` | yes | `unknown/C0/C0B0B8.asm` | `UNKNOWN_C0B0B8` | `ConfigureWindowPositionDmaFromSource` |
| 547 | C0:B0EF | C0:B149 | 90 | `exact` | yes | `unknown/C0/C0B0EF.asm` | `UNKNOWN_C0B0EF` | `BuildAndConfigureWindowPositionDmaDescriptor` |
| 548 | C0:B149 | C0:B2FF | 438 | `exact` | yes | `unknown/C0/C0B149.asm` | `UNKNOWN_C0B149` | `BuildBattleBgOffsetEffectTable3FD0` |
| 549 | C0:B2FF | C0:B65F | 864 | `exact` | yes | `data/unknown/C0B2FF.asm` | `UNKNOWN_C0B2FF` | `BattleBgOffsetClampLookupTable` |
| 550 | C0:B3FF |  | 0 | `open` |  | `data/unknown/C0B3FF.asm` | `UNKNOWN_C0B3FF` | `` |
| 551 |  |  | 0 | `open` |  | `system/math/cosine_sine.asm` | `COSINE_SINE` | `` |
| 552 |  |  | 0 | `open` |  | `data/sine_table.asm` | `` | `` |
| 553 |  |  | 0 | `open` |  | `system/file_select_init.asm` | `` | `` |
| 554 | C0:B65F | C0:B67F | 32 | `exact` | yes | `unknown/C0/C0B65F.asm` | `UNKNOWN_C0B65F` | `SeedPlayerOverworldStartPosition` |
| 555 | C0:B67F | C0:B967 | 744 | `exact` | yes | `unknown/C0/C0B67F.asm` | `` | `InitializeIntroOverworldScene` |
| 556 | C0:B967 | C0:B9BC | 85 | `exact` | yes | `battle/init_overworld.asm` | `` | `TrySavedCoordinateReloadLanding` |
| 557 | C0:B9BC | C0:BA35 | 121 | `exact` | yes | `system/main.asm` | `` | `SnapshotPartyPositionsToPathGridRecords` |
| 558 | C0:BA35 | C0:BC74 | 575 | `exact` | yes | `system/game_init.asm` | `GAME_INIT` | `BuildPathfindingOccupancyAndCandidateBuffers` |
| 559 | C0:B9BC | C0:BA35 | 121 | `exact` | yes | `unknown/C0/C0B9BC.asm` | `` | `SnapshotPartyPositionsToPathGridRecords` |
| 560 | C0:BA35 | C0:BC74 | 575 | `exact` | yes | `unknown/C0/C0BA35.asm` | `` | `BuildPathfindingOccupancyAndCandidateBuffers` |
| 561 | C0:BC74 | C0:BD96 | 290 | `exact` | yes | `misc/find_path_to_party.asm` | `FIND_PATH_TO_PARTY` | `FindPathToParty` |
| 562 | C0:BD96 | C0:BF72 | 476 | `exact` | yes | `unknown/C0/C0BD96.asm` | `UNKNOWN_C0BD96` | `BuildPathRequestToPartyMemberAndApplyStep` |
| 563 | C0:BF72 | C0:C0B4 | 322 | `exact` | yes | `unknown/C0/C0BF72.asm` | `UNKNOWN_C0BF72` | `BuildPathRequestToCurrentEntity` |
| 564 | C0:C0B4 | C0:C19B | 231 | `exact` | yes | `unknown/C0/C0C0B4.asm` | `UNKNOWN_C0C0B4` | `CopyPathToLane_FromPartyPath` |
| 565 | C0:C19B | C0:C251 | 182 | `exact` | yes | `unknown/C0/C0C19B.asm` | `UNKNOWN_C0C19B` | `CopyPathToLane_FromPartyMemberRequest` |
| 566 | C0:C251 | C0:C30C | 187 | `exact` | yes | `unknown/C0/C0C251.asm` | `UNKNOWN_C0C251` | `CopyPathToLane_FromCurrentEntityRequestReverse` |
| 567 | C0:C30C | C0:C353 | 71 | `exact` | yes | `unknown/C0/C0C30C.asm` | `UNKNOWN_C0C30C` | `RefreshCurrentSlotProfileFromField2C9A` |
| 568 | C0:C353 | C0:C35D | 10 | `exact` | yes | `unknown/C0/C0C353.asm` | `UNKNOWN_C0C353` | `RefreshCurrentSlotProfileFromField2C9A_Current` |
| 569 | C0:C35D | C0:C363 | 6 | `exact` | yes | `unknown/C0/C0C35D.asm` | `UNKNOWN_C0C35D` | `GetPlayerContext9885` |
| 570 | C0:C363 | C0:C3F9 | 150 | `exact` | yes | `unknown/C0/C0C363.asm` | `UNKNOWN_C0C363` | `GetPlayerDistanceBucketWide` |
| 571 | C0:C3F9 | C0:C48F | 150 | `exact` | yes | `unknown/C0/C0C3F9.asm` | `UNKNOWN_C0C3F9` | `GetPlayerDistanceBucketTight` |
| 572 | C0:C48F | C0:C4AF | 32 | `exact` | yes | `unknown/C0/C0C48F.asm` | `UNKNOWN_C0C48F` | `GateWidePlayerDistanceBucket` |
| 573 | C0:C4AF | C0:C4CF | 32 | `exact` | yes | `unknown/C0/C0C4AF.asm` | `UNKNOWN_C0C4AF` | `GateTightPlayerDistanceBucket` |
| 574 | C0:C4CF | C0:C4F7 | 40 | `exact` | yes | `data/unknown/C0C4CF.asm` | `UNKNOWN_C0C4CF` | `PlayerDirectionRemapTable` |
| 575 | C0:C4F7 | C0:C524 | 45 | `exact` | yes | `data/map/opposite_directions.asm` | `` | `GetDirectionFromPlayerToEntity` |
| 576 | C0:C524 | C0:C608 | 228 | `exact` | yes | `overworld/get_direction_from_player_to_entity.asm` | `UNKNOWN_C0C524` | `CheckCurrentSlotDirectionEncounterGate` |
| 577 | C0:C524 | C0:C608 | 228 | `exact` | yes | `unknown/C0/C0C524.asm` | `UNKNOWN_C0C524` | `CheckCurrentSlotDirectionEncounterGate` |
| 578 | C0:C608 | C0:C615 | 13 | `exact` | yes | `overworld/get_opposite_direction_from_player_to_entity.asm` | `GET_OPPOSITE_DIRECTION_FROM_PLAYER_TO_ENTITY` | `GetOppositeDirectionFromPlayerToEntity` |
| 579 | C0:C615 | C0:C62B | 22 | `exact` | yes | `unknown/C0/C0C615.asm` | `UNKNOWN_C0C615` | `GetGatedOppositeOrDirectPlayerEntityDirection` |
| 580 | C0:C62B | C0:C682 | 87 | `exact` | yes | `unknown/C0/C0C62B.asm` | `UNKNOWN_C0C62B` | `GetGatedEntityPositionDirectionFlag` |
| 581 | C0:C682 | C0:C69E | 28 | `exact` | yes | `overworld/actionscript/get_direction_rotated_clockwise.asm` | `GET_DIRECTION_ROTATED_CLOCKWISE` | `RotateDirectionByCurrentSlotClass` |
| 582 | C0:C69E | C0:C6B6 | 24 | `exact` | yes | `overworld/actionscript/get_direction_turned_randomly_left_or_right.asm` | `GET_DIRECTION_TURNED_RANDOMLY_LEFT_OR_RIGHT` | `GetDirectionTurnedRandomlyLeftOrRight` |
| 583 | C0:C6B6 | C0:C711 | 91 | `exact` | yes | `unknown/C0/C0C6B6.asm` | `UNKNOWN_C0C6B6` | `CheckCurrentSlotInsideLiveAreaWindow` |
| 584 | C0:C711 | C0:C760 | 79 | `exact` | yes | `unknown/C0/C0C711.asm` | `UNKNOWN_C0C711` | `CheckCurrentSlotDirectionAdjustedGridAlignment` |
| 585 | C0:C760 | C0:C7AC | 76 | `exact` | yes | `unknown/C0/C0C760.asm` | `UNKNOWN_C0C760` | `CheckDirectionAdjustedGridAlignment` |
| 586 | C0:C7AC | C0:C7DB | 47 | `exact` | yes | `unknown/C0/C0C7AC.asm` | `UNKNOWN_C0C7AC` | `RefreshCurrentSlotFootprintMaskFromCachedPosition` |
| 587 | C0:C7DB | C0:C808 | 45 | `exact` | yes | `unknown/C0/C0C7DB.asm` | `UNKNOWN_C0C7DB` | `UpdateCurrentSlotFootprintMask` |
| 588 | C0:C808 | C0:C83B | 51 | `exact` | yes | `unknown/C0/C0C808.asm` | `UNKNOWN_C0C808` | `UpdateCurrentSlotFootprintMaskWithHeightOffset` |
| 589 | C0:C83B | C0:CA4E | 531 | `exact` | yes | `unknown/C0/C0C83B.asm` | `UNKNOWN_C0C83B` | `InstallScriptMovementVectorFromDirection` |
| 590 | C0:CA4E | C0:CBD3 | 389 | `exact` | yes | `unknown/C0/C0CA4E.asm` | `UNKNOWN_C0CA4E` | `SetMovementTaskTimerFromActiveVector` |
| 591 | C0:CBD3 | C0:CC11 | 62 | `exact` | yes | `unknown/C0/C0CBD3.asm` | `UNKNOWN_C0CBD3` | `SetMovementTaskTimerFromSpeedScale` |
| 592 | C0:CC11 | C0:CCCC | 187 | `exact` | yes | `unknown/C0/C0CC11.asm` | `UNKNOWN_C0CC11` | `SetMovementTaskTimerFromCachedTarget` |
| 593 | C0:CCCC | C0:CD50 | 132 | `exact` | yes | `unknown/C0/C0CCCC.asm` | `UNKNOWN_C0CCCC` | `InitializeArcMovementTargetState` |
| 594 | C0:CD50 | C0:CEBE | 366 | `exact` | yes | `unknown/C0/C0CD50.asm` | `UNKNOWN_C0CD50` | `AdvanceArcMovementVectorFromPhase` |
| 595 | C0:CEBE | C0:CF97 | 217 | `exact` | yes | `unknown/C0/C0CEBE.asm` | `UNKNOWN_C0CEBE` | `TurnArcPhaseTowardTargetAngle` |
| 596 | C0:CF58 | C0:CF97 | 63 | `exact` | yes | `data/unknown/C0CF58.asm` | `UNKNOWN_C0CF58` | `` |
| 597 | C0:CF97 | C0:D0D9 | 322 | `exact` | yes | `unknown/C0/C0CF97.asm` | `` | `FindNearbyCollisionMapTarget` |
| 598 | C0:D0D9 | C0:D0E6 | 13 | `exact` | yes | `unknown/C0/C0D0D9.asm` | `UNKNOWN_C0D0D9` | `FindNearbyRoamingCollisionTarget` |
| 599 | C0:D0E6 | C0:D15C | 118 | `exact` | yes | `unknown/C0/C0D0E6.asm` | `UNKNOWN_C0D0E6` | `MoveOrSnapSlotTowardCachedPlayerTarget` |
| 600 | C0:D15C | C0:D195 | 57 | `exact` | yes | `unknown/C0/C0D15C.asm` | `UNKNOWN_C0D15C` | `HasUsableOverlapNeighborContext` |
| 601 | C0:D195 | C0:D19B | 6 | `exact` | yes | `unknown/C0/C0D195.asm` | `UNKNOWN_C0D195` | `ReturnFalse_MovementPredicate` |
| 602 | C0:D19B | C0:D323 | 392 | `exact` | yes | `unknown/C0/C0D19B.asm` | `UNKNOWN_C0D19B` | `Prepare_NpcAttentionPathSet` |
| 603 | C0:D4DE | C0:D59B | 189 | `exact` | yes | `unknown/C0/C0D4DE.asm` | `UNKNOWN_C0D4DE` | `Prepare_RandomizedNpcAttentionCandidates` |
| 604 | C0:D59B | C0:D5B0 | 21 | `exact` | yes | `unknown/C0/C0D59B.asm` | `UNKNOWN_C0D59B` | `Check_NpcAttentionCoordinatorActive` |
| 605 | C0:D5B0 | C0:D77F | 463 | `exact` | yes | `unknown/C0/C0D5B0.asm` | `UNKNOWN_C0D5B0` | `Gate_NpcAttentionCoordinatorFromScript` |
| 606 | C0:D77F | C0:D7B3 | 52 | `exact` | yes | `unknown/C0/C0D77F.asm` | `UNKNOWN_C0D77F` | `MarkOtherSlotsAttentionLocked` |
| 607 | C0:D7B3 | C0:D7C7 | 20 | `exact` | yes | `unknown/C0/C0D7B3.asm` | `UNKNOWN_C0D7B3` | `Save_CurrentSlotAttentionPosition` |
| 608 | C0:D7C7 | C0:D7E0 | 25 | `exact` | yes | `unknown/C0/C0D7C7.asm` | `UNKNOWN_C0D7C7` | `Restore_CurrentSlotAttentionPosition` |
| 609 | C0:D7E0 | C0:D7F7 | 23 | `exact` | yes | `unknown/C0/C0D7E0.asm` | `UNKNOWN_C0D7E0` | `Normalize_CurrentSlotAttentionState` |
| 610 | C0:D7F7 | C0:D98F | 408 | `exact` | yes | `unknown/C0/C0D7F7.asm` | `UNKNOWN_C0D7F7` | `Consume_CurrentSlotAttentionPath` |
| 611 | C0:D98F | C0:DB0F | 384 | `exact` | yes | `unknown/C0/C0D98F.asm` | `UNKNOWN_C0D98F` | `Export_CurrentSlotAttentionTarget` |
| 612 | C0:DA31 | C0:DB0F | 222 | `exact` | yes | `unknown/C0/C0DA31.asm` | `` | `` |
| 613 | C0:DB0F | C0:DBE6 | 215 | `exact` | yes | `unknown/C0/C0DB0F.asm` | `` | `Dispatch_ActiveTaskSlots` |
| 614 | C0:DBE6 | C0:DC38 | 82 | `exact` | yes | `overworld/schedule_overworld_task.asm` | `SCHEDULE_OVERWORLD_TASK` | `Queue_DelayedActionTimer` |
| 615 | C0:DC38 | C0:DC4E | 22 | `exact` | yes | `unknown/C0/C0DC38.asm` | `UNKNOWN_C0DC38` | `Clear_DelayedActionTimerSlot` |
| 616 | C0:DC4E | C0:DD0F | 193 | `exact` | yes | `overworld/process_overworld_tasks.asm` | `` | `FrameCallback_ProcessDelayedActions` |
| 617 | C0:DD0F | C0:DD2C | 29 | `exact` | yes | `overworld/load_dad_phone.asm` | `LOAD_DAD_PHONE` | `WaitForFramePumpIdle` |
| 618 | C0:DD0F | C0:DD2C | 29 | `exact` | yes | `unknown/C0/C0DD0F.asm` | `` | `WaitForFramePumpIdle` |
| 619 | C0:DD2C | C0:DD53 | 39 | `exact` | yes | `unknown/C0/C0DD2C.asm` | `UNKNOWN_C0DD2C` | `WaitFramePumpCountA` |
| 620 | C0:DD53 | C0:DD79 | 38 | `exact` | yes | `overworld/set_teleport_state.asm` | `SET_TELEPORT_STATE` | `SetTeleportStateSelectors` |
| 621 | C0:DD79 | C0:DE16 | 157 | `exact` | yes | `unknown/C0/C0DD79.asm` | `UNKNOWN_C0DD79` | `PrepareTeleportDestinationState` |
| 622 | C0:DE16 | C0:DE46 | 48 | `exact` | yes | `unknown/C0/C0DE16.asm` | `` | `FreezeTeleportTransitionObjects` |
| 623 | C0:DE46 | C0:DE7C | 54 | `exact` | yes | `unknown/C0/C0DE46.asm` | `` | `InitializeTeleportTransitionObjectsAndVectors` |
| 624 | C0:DE7C | C0:DED9 | 93 | `exact` | yes | `unknown/C0/C0DE7C.asm` | `` | `UnfreezeTeleportTransitionObjects` |
| 625 | C0:DED9 | C0:DF22 | 73 | `exact` | yes | `unknown/C0/C0DED9.asm` | `` | `ProbeTeleportTwoPointFootprintCollision` |
| 626 | C0:DF22 | C0:E196 | 628 | `exact` | yes | `unknown/C0/C0DF22.asm` | `` | `UpdateTeleportDirectionVectorState` |
| 627 | C0:E196 | C0:E214 | 126 | `exact` | yes | `unknown/C0/C0E196.asm` | `` | `SnapshotTeleportPlayerStateToRing` |
| 628 | C0:E214 | C0:E254 | 64 | `exact` | yes | `unknown/C0/C0E214.asm` | `` | `AdvanceTeleportObjectSnapshotRingCursor` |
| 629 | C0:E254 | C0:E28F | 59 | `exact` | yes | `unknown/C0/C0E254.asm` | `` | `UpdateTeleportTransitionObjectCadence` |
| 630 | C0:E28F | C0:E3C1 | 306 | `exact` | yes | `unknown/C0/C0E28F.asm` | `UNKNOWN_C0E28F` | `TickTeleportStraightMovementCallback` |
| 631 | C0:E3C1 | C0:E44D | 140 | `exact` | yes | `unknown/C0/C0E3C1.asm` | `UNKNOWN_C0E3C1` | `RestoreTeleportObjectFromSnapshotRing` |
| 632 | C0:E44D | C0:E48A | 61 | `exact` | yes | `unknown/C0/C0E44D.asm` | `` | `ApplyTeleportBetaManualSteering` |
| 633 | C0:E48A | C0:E516 | 140 | `exact` | yes | `unknown/C0/C0E48A.asm` | `` | `SeedTeleportPostSuccessDriftVector` |
| 634 | C0:E516 | C0:E674 | 350 | `exact` | yes | `unknown/C0/C0E516.asm` | `UNKNOWN_C0E516` | `TickTeleportCurvedMovementCallback` |
| 635 | C0:E674 | C0:E6FE | 138 | `exact` | yes | `unknown/C0/C0E674.asm` | `UNKNOWN_C0E674` | `TickTeleportPostSuccessDriftCallback` |
| 636 | C0:E6FE | C0:E776 | 120 | `exact` | yes | `unknown/C0/C0E6FE.asm` | `UNKNOWN_C0E6FE` | `RestoreTeleportExitObjectFromSnapshotRing` |
| 637 | C0:E776 | C0:E815 | 159 | `exact` | yes | `unknown/C0/C0E776.asm` | `UNKNOWN_C0E776` | `TickTeleportStraightExitCallback` |
| 638 | C0:E815 | C0:E897 | 130 | `exact` | yes | `unknown/C0/C0E815.asm` | `` | `SetupTeleportSuccessfulArrival` |
| 639 | C0:E897 | C0:E979 | 226 | `exact` | yes | `unknown/C0/C0E897.asm` | `` | `FinalizeTeleportArrivalOrFailure` |
| 640 | C0:E979 | C0:E97C | 3 | `exact` | yes | `unknown/C0/C0E979.asm` | `UNKNOWN_C0E979` | `TeleportNoOpCallback` |
| 641 | C0:E97C | C0:E9BA | 62 | `exact` | yes | `unknown/C0/C0E97C.asm` | `UNKNOWN_C0E97C` | `RefreshTeleportCurrentSlotPose` |
| 642 | C0:E9BA | C0:EA3E | 132 | `exact` | yes | `unknown/C0/C0E9BA.asm` | `` | `HoldTeleportFailureState` |
| 643 | C0:EA3E | C0:EA68 | 42 | `exact` | yes | `misc/teleport_freezeobjects.asm` | `TELEPORT_FREEZEOBJECTS` | `SuppressInteractionsForTeleportSlots` |
| 644 | C0:EA68 | C0:EA99 | 49 | `exact` | yes | `misc/teleport_freezeobjects2.asm` | `` | `EnsureTeleportSlotInteractionSuppression` |
| 645 | C0:EA99 | C0:EBE0 | 327 | `exact` | yes | `misc/teleport_mainloop.asm` | `TELEPORT_MAINLOOP` | `TeleportMainloopStateMachine` |
| 646 | C0:EBE0 | C0:EC77 | 151 | `exact` | yes | `unknown/C0/C0EBE0.asm` | `UNKNOWN_C0EBE0` | `Load_TitleLogoGraphicsAndTilemap` |
| 647 | C0:EC77 | C0:ECB7 | 64 | `exact` | yes | `unknown/C0/C0EC77.asm` | `UNKNOWN_C0EC77` | `Load_TitleScreenLetterOrGlowPalettes` |
| 648 | C0:ECB7 | C0:ED14 | 93 | `exact` | yes | `unknown/C0/C0ECB7.asm` | `UNKNOWN_C0ECB7` | `Load_TitleScreenBackgroundPalettes` |
| 649 | C0:ED14 | C0:ED39 | 37 | `exact` | yes | `unknown/C0/C0ED14.asm` | `UNKNOWN_C0ED14` | `Install_TitlePaletteFillFF` |
| 650 | C0:ED39 | C0:ED5C | 35 | `exact` | yes | `unknown/C0/C0ED39.asm` | `UNKNOWN_C0ED39` | `Install_TitlePaletteFill00` |
| 651 | C0:ED5C | C0:EDD1 | 117 | `exact` | yes | `unknown/C0/C0ED5C.asm` | `UNKNOWN_C0ED5C` | `Build_TitleScreenSkippedAnimationPaletteState` |
| 652 | C0:EDD1 | C0:EDDA | 9 | `exact` | yes | `unknown/C0/C0EDD1.asm` | `UNKNOWN_C0EDD1` | `Set_TitleScreenControlState2` |
| 653 | C0:EDDA | C0:EE47 | 109 | `exact` | yes | `unknown/C0/C0EDDA.asm` | `UNKNOWN_C0EDDA` | `Advance_TitleScreenPaletteFrame` |
| 654 | C0:EE47 | C0:EE53 | 12 | `exact` | yes | `unknown/C0/C0EE47.asm` | `UNKNOWN_C0EE47` | `Set_DisplayMode13` |
| 655 | C0:EE53 | C0:EFE1 | 398 | `exact` | yes | `unknown/C0/C0EE53.asm` | `UNKNOWN_C0EE53` | `Clear_CurrentTitleObjectHiddenFlag` |
| 656 | C0:EFE1 | C0:F1D2 | 497 | `exact` | yes | `intro/logo_screen_load.asm` | `` | `WaitFramesWithIntroCancel` |
| 657 | C0:EFE1 | C0:F1D2 | 497 | `exact` | yes | `unknown/C0/C0EFE1.asm` | `` | `WaitFramesWithIntroCancel` |
| 658 | C0:F1D2 | C0:F21E | 76 | `exact` | yes | `intro/logo_screen.asm` | `LOGO_SCREEN` | `RunIntroTimedPaletteFadeTail` |
| 659 | C0:F21E | C0:F41E | 512 | `exact` | yes | `intro/gas_station_load.asm` | `` | `RunGasStationIntroScreenLoop` |
| 660 | C0:F1D2 | C0:F21E | 76 | `exact` | yes | `unknown/C0/C0F1D2.asm` | `` | `RunIntroTimedPaletteFadeTail` |
| 661 | C0:F21E | C0:F41E | 512 | `exact` | yes | `unknown/C0/C0F21E.asm` | `` | `RunGasStationIntroScreenLoop` |
| 662 | C0:F41E | C0:10000 | 3042 | `exact` | yes | `intro/gas_station.asm` | `GAS_STATION` | `FrameCallback_ProcessCommandStream` |
| 663 | C0:10000 |  | 0 | `open` |  | `intro/load_gas_station_flash_palette.asm` | `LOAD_GAS_STATION_FLASH_PALETTE` | `` |
| 664 | C0:10000 |  | 0 | `open` |  | `intro/load_gas_station_palette.asm` | `LOAD_GAS_STATION_PALETTE` | `` |
| 665 | C0:10000 |  | 0 | `open` |  | `ending/credits_scroll_frame.asm` | `` | `` |
