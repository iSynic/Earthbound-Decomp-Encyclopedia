# C3 source emission plan

Generated from the source-ready C3 extraction queue. This is the module/file plan that maps documented C3 helpers to source prototypes, generated Asar companions, and durable byte-equivalence validation work items.

## Summary

- schema: `earthbound-decomp.c3-source-emission-plan.v1`
- modules: `7`
- source units: `27`
- source-ready queue units: `27`
- prototype module: `src/c3/inventory_equipment_tracked_items.asm`
- prototype modules present: `['src/c3/window_text_helpers.asm', 'src/c3/inventory_equipment_tracked_items.asm', 'src/c3/hp_pp_adjustment_helpers.asm', 'src/c3/equipment_battle_selector_helpers.asm', 'src/c3/jeff_repair_psi_helpers.asm', 'src/c3/file_select_visual_transition_helper.asm', 'src/c3/battle_visual_effect_helpers.asm']`
- by phase: `{'build-candidate': 7}`
- by artifact status: `{'prototype-file-present': 7}`
- by prototype level: `{'build-candidate': 7}`

## Module Queue

| Phase | Status | Level | Source Path | Range | Units | Subsystem | Strategy |
| --- | --- | --- | --- | --- | ---: | --- | --- |
| `build-candidate` | `prototype-file-present` | `build-candidate` | `src/c3/window_text_helpers.asm` | `C3:E450..C3:E84E` | 5 | window and battle text helpers | emit as annotated 65816 source with internal callable labels preserved |
| `build-candidate` | `prototype-file-present` | `build-candidate` | `src/c3/inventory_equipment_tracked_items.asm` | `C3:E977..C3:EC1F` | 6 | inventory equipment and tracked items | emit first prototype module; covers embedded split slices, ordinary helpers, and timed-item table contracts |
| `build-candidate` | `prototype-file-present` | `build-candidate` | `src/c3/hp_pp_adjustment_helpers.asm` | `C3:EC1F..C3:EE14` | 4 | HP PP stat adjustment helpers | emit as small arithmetic helper quartet sharing the Y/direct-amount contract |
| `build-candidate` | `prototype-file-present` | `build-candidate` | `src/c3/equipment_battle_selector_helpers.asm` | `C3:EE14..C3:EF23` | 3 | equipment and battle selector helpers | emit as selector/refresh helpers with external C1/C4 table contracts referenced |
| `build-candidate` | `prototype-file-present` | `build-candidate` | `src/c3/jeff_repair_psi_helpers.asm` | `C3:F1EC..C3:F2B1` | 1 | Jeff repair and PSI menu helpers | emit Jeff repair helper with C1:D038 mapper contract kept as an external source dependency |
| `build-candidate` | `prototype-file-present` | `build-candidate` | `src/c3/file_select_visual_transition_helper.asm` | `C3:F3C5..C3:F5F9` | 1 | file-select visual transition helper | emit embedded C3:F3C5 helper as annotated 65816 source while preserving adjacent C3:F2B1..F3C5 tables as data |
| `build-candidate` | `prototype-file-present` | `build-candidate` | `src/c3/battle_visual_effect_helpers.asm` | `C3:F5F9..C3:FB1F` | 7 | battle visual effect helpers | emit transfer/effect dispatch helpers while preserving adjacent C3 effect tables as data |

## Modules

### `src/c3/window_text_helpers.asm`

- subsystem: `window and battle text helpers`
- phase: `build-candidate`
- artifact status: `prototype-file-present`
- prototype level: `build-candidate`
- range: `C3:E450..C3:E84E`
- strategy: emit as annotated 65816 source with internal callable labels preserved
- dependencies: `$8650 window record table`; `$88E0/$88E2 open-window chain heads`; `$88E4 logical-window-to-record map`; `$8958 focused window id`

| Address | Range | Size | Kind | Name | Labels | Evidence |
| --- | --- | ---: | --- | --- | --- | --- |
| `C3:E450` | `C3:E450..C3:E4EF` | 0x9F | `include-row` | `WindowTickTransferDynamicTileBlock` | `C3:E450` `WindowTickTransferDynamicTileBlock` (entry)<br>`C3:E4CA` `ClearInstantPrinting` (internal-callable-label)<br>`C3:E4D4` `SetInstantPrinting` (internal-callable-label)<br>`C3:E4E0` `TickWindowWithoutInstantPrinting` (internal-callable-label) | `notes/c3-menu-cursor-tile-data-e3f8-e450.md:86`<br>`notes/c3-window-text-source-helper-corridor-e450-e7e3.md:98` |
| `C3:E4EF` | `C3:E4EF..C3:E6F8` | 0x209 | `include-row` | `FindFirstFreeWindowSlot` | `C3:E4EF` `FindFirstFreeWindowSlot` (entry)<br>`C3:E521` `CloseWindowAndReleaseTileState` (internal-callable-label) | `notes/c3-shared-helper-working-name-promotion.md:77`<br>`notes/c3-window-lifecycle-source-contract-e4ef-e6f7.md:7`<br>`notes/c3-window-text-source-helper-corridor-e450-e7e3.md:102` |
| `C3:E6F8` | `C3:E6F8..C3:E75D` | 0x65 | `include-row` | `ClearFocusedPartyHpPpActorAndBlankRow` | `C3:E6F8` `ClearFocusedPartyHpPpActorAndBlankRow` (entry) | `notes/c3-focused-party-hppp-actor-clear-e6f8.md:29` |
| `C3:E75D` | `C3:E75D..C3:E7E3` | 0x86 | `include-row` | `ResolveReflectedHitSideArticleTokens` | `C3:E75D` `ResolveReflectedHitSideArticleTokens` (entry)<br>`C3:E773` `ClearFirstReflectedHitSideArticleTokenFlag` (internal-callable-label)<br>`C3:E78F` `ClearSecondReflectedHitSideArticleTokenFlag` (internal-callable-label) | `notes/c3-window-text-source-helper-corridor-e450-e7e3.md:104`<br>`notes/class2-reflected-hit-side-token-consumers.md:46` |
| `C3:E7E3` | `C3:E7E3..C3:E84E` | 0x6B | `include-row` | `ClearWindowRegisteredCopyChain` | `C3:E7E3` `ClearWindowRegisteredCopyChain` (entry) | `notes/c3-window-and-battle-visual-unknown-tail-e7e3-f981.md:83`<br>`notes/c3-window-text-source-helper-corridor-e450-e7e3.md:105` |

### `src/c3/inventory_equipment_tracked_items.asm`

- subsystem: `inventory equipment and tracked items`
- phase: `build-candidate`
- artifact status: `prototype-file-present`
- prototype level: `build-candidate`
- range: `C3:E977..C3:EC1F`
- strategy: emit first prototype module; covers embedded split slices, ordinary helpers, and timed-item table contracts
- dependencies: `C3:E84E mixed data/source split plan`; `$99F1 character inventory bytes`; `$99FF..$9A02 equipped inventory-slot references`; `D5:F4BB TIMED_ITEM_TRANSFORMATION_TABLE`; `$9F1A tracked-item pulse registry`

| Address | Range | Size | Kind | Name | Labels | Evidence |
| --- | --- | ---: | --- | --- | --- | --- |
| `C3:E977` | `C3:E977..C3:E9A0` | 0x29 | `embedded-label` | `ReadCharacterInventorySlotByte` | `C3:E977` `ReadCharacterInventorySlotByte` (entry) | `notes/c3-e84e-debug-menu-and-embedded-item-helpers-split.md:7`<br>`notes/c3-inventory-equipped-slot-and-egg-refresh-helpers-e977-ebca.md:7`<br>`notes/c3-shared-helper-working-name-promotion.md:79` |
| `C3:E9A0` | `C3:E9A0..C3:E9F7` | 0x57 | `embedded-label` | `CheckEquippedInventorySlotReference` | `C3:E9A0` `CheckEquippedInventorySlotReference` (entry) | `notes/c3-e84e-debug-menu-and-embedded-item-helpers-split.md:8`<br>`notes/c3-inventory-equipped-slot-and-egg-refresh-helpers-e977-ebca.md:8`<br>`notes/c3-shared-helper-working-name-promotion.md:80` |
| `C3:E9F7` | `C3:E9F7..C3:EAD0` | 0xD9 | `include-row` | `CheckEquippedInventoryItemPresence` | `C3:E9F7` `CheckEquippedInventoryItemPresence` (entry) | `notes/c3-inventory-equipped-slot-and-egg-refresh-helpers-e977-ebca.md:9`<br>`notes/c3-shared-helper-working-name-promotion.md:81` |
| `C3:EAD0` | `C3:EAD0..C3:EB1C` | 0x4C | `include-row` | `RefreshEggFamilyLifecycleOnInsert` | `C3:EAD0` `RefreshEggFamilyLifecycleOnInsert` (entry) | `notes/c3-inventory-equipped-slot-and-egg-refresh-helpers-e977-ebca.md:10`<br>`notes/c3-shared-helper-working-name-promotion.md:82` |
| `C3:EB1C` | `C3:EB1C..C3:EBCA` | 0xAE | `include-row` | `RefreshEggFamilyLifecycleOnRemove` | `C3:EB1C` `RefreshEggFamilyLifecycleOnRemove` (entry) | `notes/c3-inventory-equipped-slot-and-egg-refresh-helpers-e977-ebca.md:11`<br>`notes/c3-shared-helper-working-name-promotion.md:83` |
| `C3:EBCA` | `C3:EBCA..C3:EC1F` | 0x55 | `include-row` | `SyncPartyOverlayTrackedItemFamilyState` | `C3:EBCA` `SyncPartyOverlayTrackedItemFamilyState` (entry) | `notes/c3-inventory-equipped-slot-and-egg-refresh-helpers-e977-ebca.md:12`<br>`notes/c3-shared-helper-working-name-promotion.md:84`<br>`notes/c3-tracked-item-sync-source-contract-ebca.md:7` |

### `src/c3/hp_pp_adjustment_helpers.asm`

- subsystem: `HP PP stat adjustment helpers`
- phase: `build-candidate`
- artifact status: `prototype-file-present`
- prototype level: `build-candidate`
- range: `C3:EC1F..C3:EE14`
- strategy: emit as small arithmetic helper quartet sharing the Y/direct-amount contract
- dependencies: `$99D8 max HP/PP fields`; `$9A15 current HP/PP fields`; `$9A19 HP-present paired marker`

| Address | Range | Size | Kind | Name | Labels | Evidence |
| --- | --- | ---: | --- | --- | --- | --- |
| `C3:EC1F` | `C3:EC1F..C3:EC8B` | 0x6C | `include-row` | `DepleteCharacterHp` | `C3:EC1F` `DepleteCharacterHp` (entry) | `notes/c3-hp-pp-source-contract-quartet-ec1f-ee13.md:7`<br>`notes/c3-shared-helper-working-name-promotion.md:85` |
| `C3:EC8B` | `C3:EC8B..C3:ED2C` | 0xA1 | `include-row` | `RecoverCharacterHp` | `C3:EC8B` `RecoverCharacterHp` (entry) | `notes/c3-hp-pp-source-contract-quartet-ec1f-ee13.md:8`<br>`notes/c3-shared-helper-working-name-promotion.md:86` |
| `C3:ED2C` | `C3:ED2C..C3:ED98` | 0x6C | `include-row` | `DepleteCharacterPp` | `C3:ED2C` `DepleteCharacterPp` (entry) | `notes/c3-hp-pp-source-contract-quartet-ec1f-ee13.md:9`<br>`notes/c3-shared-helper-working-name-promotion.md:87` |
| `C3:ED98` | `C3:ED98..C3:EE14` | 0x7C | `include-row` | `RecoverCharacterPp` | `C3:ED98` `RecoverCharacterPp` (entry) | `notes/c3-hp-pp-source-contract-quartet-ec1f-ee13.md:10`<br>`notes/c3-shared-helper-working-name-promotion.md:88` |

### `src/c3/equipment_battle_selector_helpers.asm`

- subsystem: `equipment and battle selector helpers`
- phase: `build-candidate`
- artifact status: `prototype-file-present`
- prototype level: `build-candidate`
- range: `C3:EE14..C3:EF23`
- strategy: emit as selector/refresh helpers with external C1/C4 table contracts referenced
- dependencies: `C4:58AB equipment slot mask helper`; `C4:550F statistic selector records`; `$B4A8 active visual/presentation handle`

| Address | Range | Size | Kind | Name | Labels | Evidence |
| --- | --- | ---: | --- | --- | --- | --- |
| `C3:EE14` | `C3:EE14..C3:EE4D` | 0x39 | `include-row` | `CheckItemEquipmentSlotCompatibility` | `C3:EE14` `CheckItemEquipmentSlotCompatibility` (entry) | `notes/c3-equipment-selector-source-contract-ee14-ef22.md:7`<br>`notes/c3-shared-helper-working-name-promotion.md:89` |
| `C3:EE4D` | `C3:EE4D..C3:EE7A` | 0x2D | `include-row` | `RefreshWorldAndReleaseActiveVisualHandle` | `C3:EE4D` `RefreshWorldAndReleaseActiveVisualHandle` (entry) | `notes/c3-equipment-selector-source-contract-ee14-ef22.md:8`<br>`notes/c3-shared-helper-working-name-promotion.md:90` |
| `C3:EE7A` | `C3:EE7A..C3:EF23` | 0xA9 | `include-row` | `ResolveStatisticSelectorValue` | `C3:EE7A` `ResolveStatisticSelectorValue` (entry) | `notes/c3-equipment-selector-source-contract-ee14-ef22.md:9`<br>`notes/c3-shared-helper-working-name-promotion.md:91` |

### `src/c3/jeff_repair_psi_helpers.asm`

- subsystem: `Jeff repair and PSI menu helpers`
- phase: `build-candidate`
- artifact status: `prototype-file-present`
- prototype level: `build-candidate`
- range: `C3:F1EC..C3:F2B1`
- strategy: emit Jeff repair helper with C1:D038 mapper contract kept as an external source dependency
- dependencies: `D5:5000 item configuration table`; `$9AAF Jeff inventory bytes`; `$9AA7 Jeff IQ value`; `C1:D038 MapBrokenItemToRepairedItem`

| Address | Range | Size | Kind | Name | Labels | Evidence |
| --- | --- | ---: | --- | --- | --- | --- |
| `C3:F1EC` | `C3:F1EC..C3:F2B1` | 0xC5 | `include-row` | `TryRepairJeffBrokenInventoryItem` | `C3:F1EC` `TryRepairJeffBrokenInventoryItem` (entry) | `notes/c3-jeff-repair-source-contract-f1ec.md:9`<br>`notes/c3-shared-helper-working-name-promotion.md:98` |

### `src/c3/file_select_visual_transition_helper.asm`

- subsystem: `file-select visual transition helper`
- phase: `build-candidate`
- artifact status: `prototype-file-present`
- prototype level: `build-candidate`
- range: `C3:F3C5..C3:F5F9`
- strategy: emit embedded C3:F3C5 helper as annotated 65816 source while preserving adjacent C3:F2B1..F3C5 tables as data
- dependencies: `C3:F2B1 level-up stat growth variance table`; `C3:F2B5 visual selector pose row table`; `$9F75 transition mode argument latch`; `$9641 file-select/entity-script busy state`

| Address | Range | Size | Kind | Name | Labels | Evidence |
| --- | --- | ---: | --- | --- | --- | --- |
| `C3:F3C5` | `C3:F3C5..C3:F5F9` | 0x234 | `embedded-label` | `RunFileSelectVisualTransition` | `C3:F3C5` `RunFileSelectVisualTransition` (entry) | `notes/c3-battle-visual-data-and-file-select-transition-split.md:57` |

### `src/c3/battle_visual_effect_helpers.asm`

- subsystem: `battle visual effect helpers`
- phase: `build-candidate`
- artifact status: `prototype-file-present`
- prototype level: `build-candidate`
- range: `C3:F5F9..C3:FB1F`
- strategy: emit transfer/effect dispatch helpers while preserving adjacent C3 effect tables as data
- dependencies: `C3:F951 BattleVisualToken23To2dColourTriples`; `C3:F972 BattleVisualToken31To35ColourTriples`; `C3:F819 BattleSwirlOverlayMode2Script`; `EF:EB3D fixed visual tile source`

| Address | Range | Size | Kind | Name | Labels | Evidence |
| --- | --- | ---: | --- | --- | --- | --- |
| `C3:F5F9` | `C3:F5F9..C3:F67D` | 0x84 | `include-row` | `QueueVisualTileRowsLinear` | `C3:F5F9` `QueueVisualTileRowsLinear` (entry) | `notes/c3-window-and-battle-visual-unknown-tail-e7e3-f981.md:84` |
| `C3:F67D` | `C3:F67D..C3:F705` | 0x88 | `include-row` | `QueueVisualTileRowsWrapped` | `C3:F67D` `QueueVisualTileRowsWrapped` (entry) | `notes/c3-window-and-battle-visual-unknown-tail-e7e3-f981.md:85` |
| `C3:F705` | `C3:F705..C3:F7FB` | 0xF6 | `include-row` | `QueueVisualTileBlockFromStream` | `C3:F705` `QueueVisualTileBlockFromStream` (entry) | `notes/c3-window-and-battle-visual-unknown-tail-e7e3-f981.md:86` |
| `C3:F7FB` | `C3:F7FB..C3:F819` | 0x1E | `include-row` | `QueueFixedEfEb3dVisualTileBlock` | `C3:F7FB` `QueueFixedEfEb3dVisualTileBlock` (entry) | `notes/c3-window-and-battle-visual-unknown-tail-e7e3-f981.md:87` |
| `C3:F981` | `C3:F981..C3:FAC9` | 0x148 | `include-row` | `DispatchBattleVisualEffectToken` | `C3:F981` `DispatchBattleVisualEffectToken` (entry)<br>`C3:F9A2` `ApplyBattleVisualToken23To2dColourEffect` (internal-callable-label)<br>`C3:FA4A` `ApplyBattleVisualToken31To35ColourEffect` (internal-callable-label)<br>`C3:FAC7` `ReturnFromBattleVisualEffectTokenDispatch` (internal-callable-label) | `notes/c3-battle-visual-effect-dispatch-source-contract-f981.md:7`<br>`notes/c3-window-and-battle-visual-unknown-tail-e7e3-f981.md:88` |
| `C3:FAC9` | `C3:FAC9..C3:FB09` | 0x40 | `include-row` | `DispatchBattleActorVisualEffectToken` | `C3:FAC9` `DispatchBattleActorVisualEffectToken` (entry) | `notes/c3-window-and-battle-visual-unknown-tail-e7e3-f981.md:89` |
| `C3:FB09` | `C3:FB09..C3:FB1F` | 0x16 | `include-row` | `CheckCurrentBattleActorVisualFlag` | `C3:FB09` `CheckCurrentBattleActorVisualFlag` (entry) | `notes/c3-window-and-battle-visual-unknown-tail-e7e3-f981.md:90`<br>`refs/earthbound-disasm-legacy/Earthbound Decomp/EB/Routine_Macros_EB.asm:46125` |

## Prototype Status

`src/c3/inventory_equipment_tracked_items.asm` remains the first source-emission prototype and is now a build candidate. It is the best structural test case because it covers:

- embedded source slices from a mixed data/source row
- direct character inventory access
- equipped-slot reference checks
- item-family lifecycle refresh hooks
- one structured external table contract at `D5:F4BB`

`7` planned C3 helper modules now have prototype artifacts at `build-candidate` level: `src/c3/window_text_helpers.asm`, `src/c3/inventory_equipment_tracked_items.asm`, `src/c3/hp_pp_adjustment_helpers.asm`, `src/c3/equipment_battle_selector_helpers.asm`, `src/c3/jeff_repair_psi_helpers.asm`, `src/c3/file_select_visual_transition_helper.asm`, `src/c3/battle_visual_effect_helpers.asm`. The remaining C3 source work is broader build-candidate hardening: keeping the source prototypes, generated `.bytes.asar.asm` companions, durable scaffold, and adjacent visual/script data assets in byte-equivalent lockstep.
