# ebsrc Knowns Integration Candidates

Status: restored ebsrc knowns are classified for curated integration; local source semantics remain primary.

## Summary

- banks audited: `['C0', 'C1', 'C2', 'C3', 'C4', 'EF']`
- candidates: `8392`
- source rename default: `do_not_rename_when_local_name_is_more_specific`
- first curated adoption policy: `apply only high-confidence exact symbols, table names, constants, and fields after local role/byte-equivalence review`
- ebsrc symbols already integrated in local source: `220`

## How to Read This Repo Against ebsrc

Local semantic names remain the primary source of truth for C-port work. Exact-address restored ebsrc names are compatibility navigation: when a source-visible alias is safe, the source keeps the local primary label and adds an ebsrc alias; when a name is weaker, conflicting, unaddressed, or macro-only, this manifest keeps it in the crosswalk instead of changing source labels.

## Candidate Classes

| Class | Count | Action |
| --- | ---: | --- |
| `adopt_constant_or_field_name` | 4257 | use as contract/comment vocabulary when touching the related semantic builder |
| `adopt_exact_symbol` | 0 | consider a reviewed source label promotion while preserving old address-prefixed aliases |
| `adopt_table_name` | 0 | use as table-name corroboration when local role and byte range already agree |
| `blocked_unaddressed_or_payload_only` | 660 | keep as reference-only until there is exact local source or reader-path evidence |
| `keep_local_supersedes` | 1833 | keep local semantic name/classification primary; cite ebsrc as corroborating reference |
| `macro_vocab_reference` | 1396 | feed into event/text/actionscript decoder vocabulary only after local opcode proof |
| `manual_review` | 246 | review address, role, and naming superiority before any source/doc adoption |

## Community Alignment Statuses

| Status | Count | Action |
| --- | ---: | --- |
| `blocked_conflict_or_unproven` | 765 | keep out of source until conflict, placeholder, or behavioral proof gap is resolved |
| `docs_crosswalk_only` | 6989 | document as vocabulary or navigation reference, without source aliasing |
| `local_primary_stronger` | 418 | keep local C-port semantic name primary; use the crosswalk for ebsrc lookup |
| `source_alias_integrated` | 220 | ebsrc name is already searchable in source as a primary label or alias |
| `source_alias_ready` | 0 | safe source-visible compatibility alias candidate; preserve local primary name |

## Lane Counts

| Lane | Count |
| --- | ---: |
| `audio-spc700` | 322 |
| `bank-c0` | 473 |
| `bank-c1` | 184 |
| `bank-c2` | 120 |
| `bank-c3` | 43 |
| `bank-ef` | 86 |
| `battle-runtime` | 290 |
| `data-records` | 230 |
| `event-actionscript` | 886 |
| `macro-vocabulary` | 510 |
| `map-data` | 13 |
| `overworld-runtime` | 199 |
| `ppu-window-presentation` | 478 |
| `shared-constants` | 3700 |
| `shared-struct-fields` | 557 |
| `text-vm` | 301 |

## Source-Integrated ebsrc Symbols

These exact-address ebsrc names are already present in local source as primary labels or compatibility aliases.

| Target | Lane | Reference | ebsrc Name | Local Name | Reason |
| --- | --- | --- | --- | --- | --- |
| `C0:19E2` | `overworld-runtime` | `overworld/reload_map.asm` | `RELOAD_MAP` | `Refresh_MapStripsAroundCamera` | restored ebsrc semantic name is already present in the local source module |
| `C0:1A63` | `overworld-runtime` | `overworld/initialize_map.asm` | `INITIALIZE_MAP` | `Refresh_MapStripVia0E16_FarWrapper` | restored ebsrc semantic name is already present in the local source module |
| `C0:1A69` | `overworld-runtime` | `overworld/initialize_misc_object_data.asm` | `INITIALIZE_MISC_OBJECT_DATA` | `Reset_EntitySlotStateTables` | restored ebsrc semantic name is already present in the local source module |
| `C0:1C11` | `bank-c0` | `system/alloc_sprite_mem.asm` | `ALLOC_SPRITE_MEM` | `Rewrite_VisualMemoryReservations4A00` | restored ebsrc semantic name is already present in the local source module |
| `C0:1E49` | `overworld-runtime` | `overworld/create_entity.asm` | `CREATE_ENTITY` | `Initialize_EntityWithSpritePose` | restored ebsrc semantic name is already present in the local source module |
| `C0:3C5E` | `overworld-runtime` | `overworld/get_on_bicycle.asm` | `GET_ON_BICYCLE` | `Get_OnBicycle` | restored ebsrc semantic name is already present in the local source module |
| `C0:404F` | `overworld-runtime` | `overworld/map_input_to_direction.asm` | `MAP_INPUT_TO_DIRECTION` | `MapInputToDirection` | restored ebsrc semantic name is already present in the local source module |
| `C0:4279` | `overworld-runtime` | `overworld/find_nearby_checkable_tpt_entry.asm` | `FIND_NEARBY_CHECKABLE_TPT_ENTRY` | `Resolve_InteractableAlongFacingTarget` | restored ebsrc semantic name is already present in the local source module |
| `C0:4452` | `overworld-runtime` | `overworld/find_nearby_talkable_tpt_entry.asm` | `FIND_NEARBY_TALKABLE_TPT_ENTRY` | `Resolve_FrontInteractionTarget` | restored ebsrc semantic name is already present in the local source module |
| `C0:5FF6` | `overworld-runtime` | `overworld/npc_collision_check.asm` | `NPC_COLLISION_CHECK` | `Find_OverlappingEntitySlot` | restored ebsrc semantic name is already present in the local source module |
| `C0:6B21` | `overworld-runtime` | `overworld/spawn_buzz_buzz.asm` | `SPAWN_BUZZ_BUZZ` | `RunPostTransitionScriptHookAndSelectorPass` | restored ebsrc semantic name is already present in the local source module |
| `C0:6BFF` | `overworld-runtime` | `overworld/door_transition.asm` | `DOOR_TRANSITION` | `RunDeferredScriptPointerAndRefreshTransitionState` | restored ebsrc semantic name is already present in the local source module |
| `C0:75DD` | `overworld-runtime` | `overworld/process_queued_interactions.asm` | `PROCESS_QUEUED_INTERACTIONS` | `Consume_MovementRecordQueue` | restored ebsrc semantic name is already present in the local source module |
| `C0:841B` | `bank-c0` | `system/read_joypad.asm` | `READ_JOYPAD` | `Advance_InputPlaybackStream` | restored ebsrc semantic name is already present in the local source module |
| `C0:8501` | `bank-c0` | `system/process_sfx_queue.asm` | `PROCESS_SFX_QUEUE` | `Nmi_ServiceAudioQueue` | restored ebsrc semantic name is already present in the local source module |
| `C0:8518` | `bank-c0` | `system/execute_irq_callback.asm` | `EXECUTE_IRQ_CALLBACK` | `Frame_CallbackDispatcher` | restored ebsrc semantic name is already present in the local source module |
| `C0:851B` | `bank-c0` | `system/default_irq_callback.asm` | `DEFAULT_IRQ_CALLBACK` | `Frame_CallbackReturn` | restored ebsrc semantic name is already present in the local source module |
| `C0:851C` | `bank-c0` | `system/set_irq_callback.asm` | `SET_IRQ_CALLBACK` | `Set_FrameCallbackPtr` | restored ebsrc semantic name is already present in the local source module |
| `C0:8522` | `bank-c0` | `system/reset_irq_callback.asm` | `RESET_IRQ_CALLBACK` | `Reset_FrameCallbackToDefault` | restored ebsrc semantic name is already present in the local source module |
| `C0:8616` | `bank-c0` | `system/transfer_to_vram.asm` | `TRANSFER_TO_VRAM` | `QueueVramTransfer_FromDpSource` | restored ebsrc semantic name is already present in the local source module |
| `C0:8D92` | `bank-c0` | `system/set_oam_size.asm` | `SET_OAM_SIZE` | `Update_ObselRegisterFromQueue` | restored ebsrc semantic name is already present in the local source module |
| `C0:8D9E` | `bank-c0` | `system/set_bg1_vram_location.asm` | `SET_BG1_VRAM_LOCATION` | `Update_Bg1ScreenBaseRegistersFromQueue` | restored ebsrc semantic name is already present in the local source module |
| `C0:8DDE` | `bank-c0` | `system/set_bg2_vram_location.asm` | `SET_BG2_VRAM_LOCATION` | `Update_Bg2ScreenBaseRegistersFromQueue` | restored ebsrc semantic name is already present in the local source module |
| `C0:8E1C` | `bank-c0` | `system/set_bg3_vram_location.asm` | `SET_BG3_VRAM_LOCATION` | `Update_Bg3ScreenBaseRegistersFromQueue` | restored ebsrc semantic name is already present in the local source module |
| `C0:8E5C` | `bank-c0` | `system/set_bg4_vram_location.asm` | `SET_BG4_VRAM_LOCATION` | `Update_Bg4ScreenBaseRegistersFromQueue` | restored ebsrc semantic name is already present in the local source module |
| `C0:8FF7` | `bank-c0` | `system/math/mult168.asm` | `MULT168` | `Multiply16By8_ViaHardwareRegisters` | restored ebsrc semantic name is already present in the local source module |
| `C0:9032` | `bank-c0` | `system/math/mult16.asm` | `MULT16` | `Multiply16By16_ViaHardwareRegisters` | restored ebsrc semantic name is already present in the local source module |
| `C0:9321` | `overworld-runtime` | `overworld/init_entity.asm` | `INIT_ENTITY` | `Init_DelayedActionState` | restored ebsrc semantic name is already present in the local source module |
| `C0:9F82` | `overworld-runtime` | `overworld/actionscript/choose_random.asm` | `CHOOSE_RANDOM` | `ChooseRandomScriptWord` | restored ebsrc semantic name is already present in the local source module |
| `C0:A60B` | `map-data` | `data/sprite_direction_mapping_4_direction.asm` | `SPRITE_DIRECTION_MAPPING_4_DIRECTION` | `VisualProfileDirectionOffsetTable` | restored ebsrc semantic name is already present in the local source module |
| `C0:A623` | `map-data` | `data/sprite_direction_mapping_8_direction.asm` | `SPRITE_DIRECTION_MAPPING_8_DIRECTION` | `VisualProfileSecondaryOffsetTable` | restored ebsrc semantic name is already present in the local source module |
| `C0:A651` | `overworld-runtime` | `overworld/actionscript/set_direction8.asm` | `SET_DIRECTION8` | `Script_SetDirectionClassAndField1A86` | restored ebsrc semantic name is already present in the local source module |
| `C0:A65F` | `overworld-runtime` | `overworld/actionscript/set_direction.asm` | `SET_DIRECTION` | `SetCurrentSlotDirectionClassIfActive` | restored ebsrc semantic name is already present in the local source module |
| `C0:A679` | `overworld-runtime` | `overworld/actionscript/set_surface_flags.asm` | `SET_SURFACE_FLAGS` | `Script_SetCurrentSlotDisplayControlBits` | restored ebsrc semantic name is already present in the local source module |
| `C0:A8F7` | `overworld-runtime` | `overworld/actionscript/prepare_new_entity_at_self.asm` | `ACTIONSCRIPT_PREPARE_NEW_ENTITY_AT_SELF` | `ActionScript_PrepareNewEntityAtSelf` | restored ebsrc semantic name is already present in the local source module |
| `C0:A8FF` | `overworld-runtime` | `overworld/actionscript/prepare_new_entity_at_party_leader.asm` | `ACTIONSCRIPT_PREPARE_NEW_ENTITY_AT_PARTY_LEADER` | `ActionScript_PrepareNewEntityAtPartyLeader` | restored ebsrc semantic name is already present in the local source module |
| `C0:A907` | `overworld-runtime` | `overworld/actionscript/prepare_new_entity_at_teleport_destination.asm` | `ACTIONSCRIPT_PREPARE_NEW_ENTITY_AT_TELEPORT_DESTINATION` | `ActionScript_PrepareNewEntityAtTeleportDestination` | restored ebsrc semantic name is already present in the local source module |
| `C0:A912` | `overworld-runtime` | `overworld/actionscript/prepare_new_entity.asm` | `ACTIONSCRIPT_PREPARE_NEW_ENTITY` | `ActionScript_PrepareNewEntity` | restored ebsrc semantic name is already present in the local source module |
| `C0:A943` | `overworld-runtime` | `overworld/actionscript/get_position_of_party_member.asm` | `ACTIONSCRIPT_GET_POSITION_OF_PARTY_MEMBER` | `ActionScript_GetPositionOfPartyMember` | restored ebsrc semantic name is already present in the local source module |
| `C0:AA07` | `overworld-runtime` | `overworld/actionscript/fade_out_with_mosaic.asm` | `FADE_OUT_WITH_MOSAIC` | `ActionScript_FadeOutWithMosaic` | restored ebsrc semantic name is already present in the local source module |

## Remaining Exact/Table Adoption Batch

These are review-ready exact source/table candidates only. An empty table means this pass either integrated or rejected the safe source-facing batch.

| Target | Lane | Reference | ebsrc Name | Local Name | Reason |
| --- | --- | --- | --- | --- | --- |

## Constants And Field Vocabulary

These restored ebsrc names are vocabulary inputs for semantic contracts and comments, not bulk source-renaming targets.

| Target | Lane | Reference | ebsrc Name | Local Name | Reason |
| --- | --- | --- | --- | --- | --- |
| `NO_EFFECT` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `NO_EFFECT` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `USE_NO_EFFECT` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `USE_NO_EFFECT` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `ACTION_002` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `ACTION_002` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `ACTION_003` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `ACTION_003` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `BASH` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `BASH` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `SHOOT` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `SHOOT` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `SPY` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `SPY` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PRAY` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PRAY` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `GUARD` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `GUARD` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `ACTION_009` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `ACTION_009` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_ROCKIN_ALPHA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_ROCKIN_ALPHA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_ROCKIN_BETA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_ROCKIN_BETA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_ROCKIN_GAMMA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_ROCKIN_GAMMA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_ROCKIN_OMEGA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_ROCKIN_OMEGA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_FIRE_ALPHA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_FIRE_ALPHA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_FIRE_BETA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_FIRE_BETA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_FIRE_GAMMA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_FIRE_GAMMA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_FIRE_OMEGA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_FIRE_OMEGA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_FREEZE_ALPHA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_FREEZE_ALPHA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_FREEZE_BETA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_FREEZE_BETA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_FREEZE_GAMMA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_FREEZE_GAMMA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_FREEZE_OMEGA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_FREEZE_OMEGA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_THUNDER_ALPHA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_THUNDER_ALPHA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_THUNDER_BETA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_THUNDER_BETA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_THUNDER_GAMMA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_THUNDER_GAMMA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_THUNDER_OMEGA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_THUNDER_OMEGA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_FLASH_ALPHA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_FLASH_ALPHA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_FLASH_BETA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_FLASH_BETA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_FLASH_GAMMA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_FLASH_GAMMA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_FLASH_OMEGA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_FLASH_OMEGA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_STARSTORM_ALPHA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_STARSTORM_ALPHA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_STARSTORM_OMEGA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_STARSTORM_OMEGA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_LIFEUP_ALPHA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_LIFEUP_ALPHA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_LIFEUP_BETA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_LIFEUP_BETA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_LIFEUP_GAMMA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_LIFEUP_GAMMA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_LIFEUP_OMEGA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_LIFEUP_OMEGA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_HEALING_ALPHA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_HEALING_ALPHA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_HEALING_BETA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_HEALING_BETA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_HEALING_GAMMA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_HEALING_GAMMA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_HEALING_OMEGA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_HEALING_OMEGA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |

## Samples By Class

### `adopt_exact_symbol`

| Target | Lane | Reference | ebsrc Name | Local Name | Reason |
| --- | --- | --- | --- | --- | --- |

### `adopt_constant_or_field_name`

| Target | Lane | Reference | ebsrc Name | Local Name | Reason |
| --- | --- | --- | --- | --- | --- |
| `NO_EFFECT` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `NO_EFFECT` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `USE_NO_EFFECT` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `USE_NO_EFFECT` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `ACTION_002` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `ACTION_002` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `ACTION_003` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `ACTION_003` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `BASH` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `BASH` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `SHOOT` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `SHOOT` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `SPY` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `SPY` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PRAY` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PRAY` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `GUARD` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `GUARD` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `ACTION_009` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `ACTION_009` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_ROCKIN_ALPHA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_ROCKIN_ALPHA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_ROCKIN_BETA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_ROCKIN_BETA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_ROCKIN_GAMMA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_ROCKIN_GAMMA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_ROCKIN_OMEGA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_ROCKIN_OMEGA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_FIRE_ALPHA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_FIRE_ALPHA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_FIRE_BETA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_FIRE_BETA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_FIRE_GAMMA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_FIRE_GAMMA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_FIRE_OMEGA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_FIRE_OMEGA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_FREEZE_ALPHA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_FREEZE_ALPHA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |
| `PSI_FREEZE_BETA` | `shared-constants` | `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm` | `PSI_FREEZE_BETA` | `` | restored ebsrc constant/enum vocabulary can improve local semantic contracts |

### `adopt_table_name`

| Target | Lane | Reference | ebsrc Name | Local Name | Reason |
| --- | --- | --- | --- | --- | --- |

### `macro_vocab_reference`

| Target | Lane | Reference | ebsrc Name | Local Name | Reason |
| --- | --- | --- | --- | --- | --- |
| `C0:AD8A` | `event-actionscript` | `data/events/scripts/786.asm` | `EVENT_786` | `Event786_CurrentSlotOrbitScript` | event script label/macro vocabulary reference; no behavior claim from ebsrc alone |
| `C2:FFB7` | `event-actionscript` | `data/events/scripts/000.asm` | `EVENT_000` | `C2FFB7_BankEndTailBytes` | event script label/macro vocabulary reference; no behavior claim from ebsrc alone |
| `C3:0295` | `event-actionscript` | `data/events/scripts/221.asm` | `EVENT_221` | `MoveActiveEntityLeftToScriptVarsAndWait` | event script label/macro vocabulary reference; no behavior claim from ebsrc alone |
| `C3:098B` | `event-actionscript` | `data/events/scripts/222.asm` | `EVENT_222` | `C3098B_MoveActiveEntityLeftToScriptVarsAndWaitEnd` | event script label/macro vocabulary reference; no behavior claim from ebsrc alone |
| `C3:0A1F` | `event-actionscript` | `data/events/scripts/223.asm` | `EVENT_223` | `C30A1F_C3098BEventScriptEnd` | event script label/macro vocabulary reference; no behavior claim from ebsrc alone |
| `C3:0C55` | `event-actionscript` | `data/events/scripts/224.asm` | `EVENT_224` | `C30C55_C30A1FEventScriptEnd` | event script label/macro vocabulary reference; no behavior claim from ebsrc alone |
| `C3:098B` | `event-actionscript` | `data/events/scripts/225+226+227.asm` | `225+226+227` | `C3098B_MoveActiveEntityLeftToScriptVarsAndWaitEnd` | event script label/macro vocabulary reference; no behavior claim from ebsrc alone |
| `C3:0A1F` | `event-actionscript` | `data/events/scripts/228.asm` | `EVENT_228` | `C30A1F_C3098BEventScriptEnd` | event script label/macro vocabulary reference; no behavior claim from ebsrc alone |
| `C3:0C55` | `event-actionscript` | `data/events/scripts/229.asm` | `EVENT_229` | `C30C55_C30A1FEventScriptEnd` | event script label/macro vocabulary reference; no behavior claim from ebsrc alone |
| `C3:0C67` | `event-actionscript` | `data/events/scripts/230.asm` | `EVENT_230` | `C30C67_C30C55EventScriptEnd` | event script label/macro vocabulary reference; no behavior claim from ebsrc alone |
| `C3:1D2D` | `event-actionscript` | `data/events/scripts/231.asm` | `EVENT_231` | `C31D2D_C30C67EventScriptEnd` | event script label/macro vocabulary reference; no behavior claim from ebsrc alone |
| `C3:1D4F` | `event-actionscript` | `data/events/scripts/232.asm` | `EVENT_232` | `C31D4F_C31D2DEventScriptEnd` | event script label/macro vocabulary reference; no behavior claim from ebsrc alone |
| `C3:1DF4` | `event-actionscript` | `data/events/scripts/228+229+230+231+232_common.asm` | `228+229+230+231+232_COMMON` | `C31DF4_C31D4FEventScriptEnd` | event script label/macro vocabulary reference; no behavior claim from ebsrc alone |
| `C3:1E2D` | `event-actionscript` | `data/events/scripts/233+234+235+236+237.asm` | `233+234+235+236+237` | `C31E2D_C31DF4EventScriptEnd` | event script label/macro vocabulary reference; no behavior claim from ebsrc alone |
| `C3:1EC1` | `event-actionscript` | `data/events/scripts/238.asm` | `EVENT_238` | `C31EC1_C31E2DEventScriptEnd` | event script label/macro vocabulary reference; no behavior claim from ebsrc alone |
| `C3:1ED8` | `event-actionscript` | `data/events/scripts/239.asm` | `EVENT_239` | `C31ED8_C31EC1EventScriptEnd` | event script label/macro vocabulary reference; no behavior claim from ebsrc alone |
| `C3:1EEF` | `event-actionscript` | `data/events/scripts/240.asm` | `EVENT_240` | `C31EEF_C31ED8EventScriptEnd` | event script label/macro vocabulary reference; no behavior claim from ebsrc alone |
| `C3:2138` | `event-actionscript` | `data/events/scripts/241.asm` | `EVENT_241` | `C32138_C31EEFEventScriptEnd` | event script label/macro vocabulary reference; no behavior claim from ebsrc alone |
| `C3:2CD2` | `event-actionscript` | `data/events/scripts/242+243.asm` | `242+243` | `C32CD2_C32138EventScriptEnd` | event script label/macro vocabulary reference; no behavior claim from ebsrc alone |
| `C3:3399` | `event-actionscript` | `data/events/scripts/244.asm` | `EVENT_244` | `C33399_C32CD2EventScriptEnd` | event script label/macro vocabulary reference; no behavior claim from ebsrc alone |

### `keep_local_supersedes`

| Target | Lane | Reference | ebsrc Name | Local Name | Reason |
| --- | --- | --- | --- | --- | --- |
| `C0:0E16` | `bank-c0` | `unknown/C0/C00E16.asm` | `` | `Upload_VerticalMovementMapStrip` | restored ebsrc still marks this span unknown; keep local semantic classification |
| `C0:0FCB` | `bank-c0` | `unknown/C0/C00FCB.asm` | `` | `Upload_HorizontalMovementMapStrip` | restored ebsrc still marks this span unknown; keep local semantic classification |
| `C0:1181` | `bank-c0` | `unknown/C0/C01181.asm` | `` | `Upload_AuxiliaryMovementMapStrip` | restored ebsrc still marks this span unknown; keep local semantic classification |
| `C0:1731` | `bank-c0` | `unknown/C0/C01731.asm` | `` | `` | restored ebsrc still marks this span unknown; keep local semantic classification |
| `C0:17EA` | `bank-c0` | `unknown/C0/C017EA.asm` | `` | `AccumulateOverworldCameraStep` | restored ebsrc still marks this span unknown; keep local semantic classification |
| `C0:19E2` | `overworld-runtime` | `overworld/reload_map.asm` | `RELOAD_MAP` | `Refresh_MapStripsAroundCamera` | restored ebsrc semantic name is already present in the local source module |
| `C0:1A63` | `overworld-runtime` | `overworld/initialize_map.asm` | `INITIALIZE_MAP` | `Refresh_MapStripVia0E16_FarWrapper` | restored ebsrc semantic name is already present in the local source module |
| `C0:19E2` | `bank-c0` | `unknown/C0/C019E2.asm` | `` | `Refresh_MapStripsAroundCamera` | restored ebsrc still marks this span unknown; keep local semantic classification |
| `C0:1A63` | `bank-c0` | `unknown/C0/C01A63.asm` | `` | `Refresh_MapStripVia0E16_FarWrapper` | restored ebsrc still marks this span unknown; keep local semantic classification |
| `C0:1A69` | `overworld-runtime` | `overworld/initialize_misc_object_data.asm` | `INITIALIZE_MISC_OBJECT_DATA` | `Reset_EntitySlotStateTables` | restored ebsrc semantic name is already present in the local source module |
| `C0:1A86` | `bank-c0` | `unknown/C0/C01A86.asm` | `` | `Reset_EntityBytePool467E` | restored ebsrc still marks this span unknown; keep local semantic classification |
| `C0:1A9D` | `overworld-runtime` | `overworld/find_free_space_7E4682.asm` | `FIND_FREE_SPACE_7E4682` | `Find_FreeEntityBytePoolRun467E` | local code name is already more specific; keep as primary and record ebsrc as corroboration |
| `C0:1B15` | `bank-c0` | `unknown/C0/C01B15.asm` | `` | `Release_EntityBytePoolRun467E` | restored ebsrc still marks this span unknown; keep local semantic classification |
| `C0:1B96` | `bank-c0` | `unknown/C0/C01B96.asm` | `` | `Reserve_VisualMemorySpan4A00` | restored ebsrc still marks this span unknown; keep local semantic classification |
| `C0:1C11` | `bank-c0` | `system/alloc_sprite_mem.asm` | `ALLOC_SPRITE_MEM` | `Rewrite_VisualMemoryReservations4A00` | restored ebsrc semantic name is already present in the local source module |
| `C0:1C52` | `bank-c0` | `unknown/C0/C01C52.asm` | `` | `ReserveAndUpload_EntityVisualTiles` | restored ebsrc still marks this span unknown; keep local semantic classification |
| `C0:1D38` | `bank-c0` | `unknown/C0/C01D38.asm` | `` | `Build_EntityVisualRecords467E` | restored ebsrc still marks this span unknown; keep local semantic classification |
| `C0:1DED` | `bank-c0` | `unknown/C0/C01DED.asm` | `` | `Read_SpritePoseVisualDescriptor` | restored ebsrc still marks this span unknown; keep local semantic classification |
| `C0:1E49` | `overworld-runtime` | `overworld/create_entity.asm` | `CREATE_ENTITY` | `Initialize_EntityWithSpritePose` | restored ebsrc semantic name is already present in the local source module |
| `C0:20F1` | `bank-c0` | `unknown/C0/C020F1.asm` | `` | `ScriptRelease_CurrentEntityVisualState` | restored ebsrc still marks this span unknown; keep local semantic classification |

### `blocked_unaddressed_or_payload_only`

| Target | Lane | Reference | ebsrc Name | Local Name | Reason |
| --- | --- | --- | --- | --- | --- |
| `` | `bank-c0` | `common.asm` | `COMMON` | `` | support include; useful as reference but not a local semantic target |
| `` | `bank-c0` | `config.asm` | `CONFIG` | `` | support include; useful as reference but not a local semantic target |
| `` | `bank-c0` | `eventmacros.asm` | `EVENTMACROS` | `` | support include; useful as reference but not a local semantic target |
| `` | `bank-c0` | `structs.asm` | `STRUCTS` | `` | support include; useful as reference but not a local semantic target |
| `` | `bank-c0` | `symbols/bank00.inc.asm` | `BANK00.INC` | `` | support include; useful as reference but not a local semantic target |
| `` | `bank-c0` | `symbols/bank01.inc.asm` | `BANK01.INC` | `` | support include; useful as reference but not a local semantic target |
| `` | `bank-c0` | `symbols/bank02.inc.asm` | `BANK02.INC` | `` | support include; useful as reference but not a local semantic target |
| `` | `bank-c0` | `symbols/bank03.inc.asm` | `BANK03.INC` | `` | support include; useful as reference but not a local semantic target |
| `` | `bank-c0` | `symbols/bank04.inc.asm` | `BANK04.INC` | `` | support include; useful as reference but not a local semantic target |
| `` | `bank-c0` | `symbols/bank2f.inc.asm` | `BANK2F.INC` | `` | support include; useful as reference but not a local semantic target |
| `` | `bank-c0` | `symbols/doors.inc.asm` | `DOORS.INC` | `` | support include; useful as reference but not a local semantic target |
| `` | `bank-c0` | `symbols/globals.inc.asm` | `GLOBALS.INC` | `` | support include; useful as reference but not a local semantic target |
| `` | `map-data` | `symbols/map.inc.asm` | `MAP.INC` | `` | support include; useful as reference but not a local semantic target |
| `` | `bank-c0` | `symbols/misc.inc.asm` | `MISC.INC` | `` | support include; useful as reference but not a local semantic target |
| `` | `bank-c0` | `symbols/sram.inc.asm` | `SRAM.INC` | `` | support include; useful as reference but not a local semantic target |
| `` | `text-vm` | `symbols/text.inc.asm` | `TEXT.INC` | `` | support include; useful as reference but not a local semantic target |
| `` | `overworld-runtime` | `overworld/actionscript/clear_entity_draw_sorting_table.asm` | `CLEAR_ENTITY_DRAW_SORTING_TABLE` | `` | semantic reference is not exact-covered by local source |
| `` | `overworld-runtime` | `overworld/setup_vram.asm` | `OVERWORLD_SETUP_VRAM` | `` | semantic reference is not exact-covered by local source |
| `` | `overworld-runtime` | `overworld/initialize.asm` | `OVERWORLD_INITIALIZE` | `` | semantic reference is not exact-covered by local source |
| `` | `ppu-window-presentation` | `system/load_tileset_anim.asm` | `LOAD_TILESET_ANIM` | `` | semantic reference is not exact-covered by local source |

### `manual_review`

| Target | Lane | Reference | ebsrc Name | Local Name | Reason |
| --- | --- | --- | --- | --- | --- |
| `C0:8CD5` | `data-records` | `data/C08C58_jumps.asm` | `` | `Apply_DisplayRendererQueueRecord` | exact-covered semantic include has no non-placeholder ebsrc symbol or table stem |
| `C0:943C` | `data-records` | `data/palette_dma_parameters.asm` | `PALETTE_DMA_PARAMETERS` | `MarkWorldObjectChainForSetup` | named ebsrc data overlaps a non-generic local source name; review before adopting |
| `C0:94AA` | `data-records` | `data/dma_table.asm` | `DMA_TABLE` | `Process_ActiveTaskSlots` | named ebsrc data overlaps a non-generic local source name; review before adopting |
| `C0:9558` | `data-records` | `data/movement_control_codes_pointer_table.asm` | `MOVEMENT_CONTROL_CODES_POINTER_TABLE` | `ScriptOpcodePointerTable` | named ebsrc data overlaps a non-generic local source name; review before adopting |
| `C0:9B09` | `data-records` | `data/events/entity_script_var_tables.asm` | `ENTITY_SCRIPT_VAR_TABLES` | `ScriptOp_InitCurrentTaskRecordDefaults` | named ebsrc data overlaps a non-generic local source name; review before adopting |
| `C0:AC3A` | `data-records` | `data/stereo_mono_data.asm` | `STEREO_MONO_DATA` | `SendApuPort2Byte` | named ebsrc data overlaps a non-generic local source name; review before adopting |
| `C0:C4F7` | `map-data` | `data/map/opposite_directions.asm` | `OPPOSITE_DIRECTIONS` | `GetDirectionFromPlayerToEntity` | named ebsrc data overlaps a non-generic local source name; review before adopting |
| `C1:E1A2` | `bank-c1` | `misc/null/C1E1A2.asm` | `` | `NullFarCallback` | exact-covered semantic include has no non-placeholder ebsrc symbol or table stem |
| `C2:09A0` | `text-vm` | `data/text/the.asm` | `THE` | `CloseAndClearCurrentWindowTilemap` | named ebsrc data overlaps a non-generic local source name; review before adopting |
| `C3:0295` | `data-records` | `data/events/C30295.asm` | `` | `MoveActiveEntityLeftToScriptVarsAndWait` | exact-covered semantic include has no non-placeholder ebsrc symbol or table stem |
| `C3:098B` | `data-records` | `data/events/C3098B.asm` | `` | `C3098B_MoveActiveEntityLeftToScriptVarsAndWaitEnd` | exact-covered semantic include has no non-placeholder ebsrc symbol or table stem |
| `C3:0A1F` | `data-records` | `data/events/C30A1F.asm` | `` | `C30A1F_C3098BEventScriptEnd` | exact-covered semantic include has no non-placeholder ebsrc symbol or table stem |
| `C3:0C55` | `data-records` | `data/events/C30C55.asm` | `` | `C30C55_C30A1FEventScriptEnd` | exact-covered semantic include has no non-placeholder ebsrc symbol or table stem |
| `C3:0C67` | `data-records` | `data/events/C30C67.asm` | `` | `C30C67_C30C55EventScriptEnd` | exact-covered semantic include has no non-placeholder ebsrc symbol or table stem |
| `C3:1D2D` | `data-records` | `data/events/C31D2D.asm` | `` | `C31D2D_C30C67EventScriptEnd` | exact-covered semantic include has no non-placeholder ebsrc symbol or table stem |
| `C3:1D4F` | `data-records` | `data/events/C31D4F.asm` | `` | `C31D4F_C31D2DEventScriptEnd` | exact-covered semantic include has no non-placeholder ebsrc symbol or table stem |
| `C3:1DF4` | `data-records` | `data/events/C31DF4.asm` | `` | `C31DF4_C31D4FEventScriptEnd` | exact-covered semantic include has no non-placeholder ebsrc symbol or table stem |
| `C3:1E2D` | `data-records` | `data/events/C31E2D.asm` | `` | `C31E2D_C31DF4EventScriptEnd` | exact-covered semantic include has no non-placeholder ebsrc symbol or table stem |
| `C3:1EC1` | `data-records` | `data/events/C31EC1.asm` | `` | `C31EC1_C31E2DEventScriptEnd` | exact-covered semantic include has no non-placeholder ebsrc symbol or table stem |
| `C3:1ED8` | `data-records` | `data/events/C31ED8.asm` | `` | `C31ED8_C31EC1EventScriptEnd` | exact-covered semantic include has no non-placeholder ebsrc symbol or table stem |

## Guardrails

- Do not bulk-import restored ebsrc `UNKNOWN` names.
- Keep local names when they are more specific than restored ebsrc names.
- Treat macro names and unaddressed payloads as decoder/reference input, not behavior proof.
- Run bank byte-equivalence checks before committing any source label promotion.
