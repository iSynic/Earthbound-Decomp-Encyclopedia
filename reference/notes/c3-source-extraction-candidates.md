# C3 source extraction candidates

Generated from `build/c3-source-data-map.json`. This is the implementation queue for C3 rows that should become ordinary 65816 source before event/actionscript VM work.

## Summary

- schema: `earthbound-decomp.c3-source-extraction-candidates.v1`
- source units: `27`
- include-start source units: `24`
- embedded source units: `3`
- internal source entry labels: `9`
- orphan/source entry labels outside addressed source-helper rows: `2`
- by subsystem: `{'HP PP stat adjustment helpers': 4, 'Jeff repair and PSI menu helpers': 1, 'battle visual effect helpers': 7, 'equipment and battle selector helpers': 3, 'file-select visual transition helper': 1, 'inventory equipment and tracked items': 6, 'window and battle text helpers': 5}`
- by readiness: `{'source-ready': 27}`
- by priority: `{'1': 15, '2': 11, '3': 1}`

## Priority Queue

| Priority | Kind | Address | Size | Subsystem | Name | Readiness | Blocked By |
| ---: | --- | --- | ---: | --- | --- | --- | --- |
| 1 | `include-row` | `C3:E450` | 0x9F | window and battle text helpers | `WindowTickTransferDynamicTileBlock` | `source-ready` |  |
| 1 | `include-row` | `C3:E4EF` | 0x209 | window and battle text helpers | `FindFirstFreeWindowSlot` | `source-ready` |  |
| 1 | `include-row` | `C3:E6F8` | 0x65 | window and battle text helpers | `ClearFocusedPartyHpPpActorAndBlankRow` | `source-ready` |  |
| 1 | `include-row` | `C3:E75D` | 0x86 | window and battle text helpers | `ResolveReflectedHitSideArticleTokens` | `source-ready` |  |
| 1 | `include-row` | `C3:E7E3` | 0x6B | window and battle text helpers | `ClearWindowRegisteredCopyChain` | `source-ready` |  |
| 1 | `embedded-label` | `C3:E977` | 0x29 | inventory equipment and tracked items | `ReadCharacterInventorySlotByte` | `source-ready` |  |
| 1 | `embedded-label` | `C3:E9A0` | 0x57 | inventory equipment and tracked items | `CheckEquippedInventorySlotReference` | `source-ready` |  |
| 1 | `include-row` | `C3:E9F7` | 0xD9 | inventory equipment and tracked items | `CheckEquippedInventoryItemPresence` | `source-ready` |  |
| 1 | `include-row` | `C3:EAD0` | 0x4C | inventory equipment and tracked items | `RefreshEggFamilyLifecycleOnInsert` | `source-ready` |  |
| 1 | `include-row` | `C3:EB1C` | 0xAE | inventory equipment and tracked items | `RefreshEggFamilyLifecycleOnRemove` | `source-ready` |  |
| 1 | `include-row` | `C3:EBCA` | 0x55 | inventory equipment and tracked items | `SyncPartyOverlayTrackedItemFamilyState` | `source-ready` |  |
| 1 | `include-row` | `C3:EC1F` | 0x6C | HP PP stat adjustment helpers | `DepleteCharacterHp` | `source-ready` |  |
| 1 | `include-row` | `C3:EC8B` | 0xA1 | HP PP stat adjustment helpers | `RecoverCharacterHp` | `source-ready` |  |
| 1 | `include-row` | `C3:ED2C` | 0x6C | HP PP stat adjustment helpers | `DepleteCharacterPp` | `source-ready` |  |
| 1 | `include-row` | `C3:ED98` | 0x7C | HP PP stat adjustment helpers | `RecoverCharacterPp` | `source-ready` |  |
| 2 | `include-row` | `C3:EE14` | 0x39 | equipment and battle selector helpers | `CheckItemEquipmentSlotCompatibility` | `source-ready` |  |
| 2 | `include-row` | `C3:EE4D` | 0x2D | equipment and battle selector helpers | `RefreshWorldAndReleaseActiveVisualHandle` | `source-ready` |  |
| 2 | `include-row` | `C3:EE7A` | 0xA9 | equipment and battle selector helpers | `ResolveStatisticSelectorValue` | `source-ready` |  |
| 2 | `include-row` | `C3:F1EC` | 0xC5 | Jeff repair and PSI menu helpers | `TryRepairJeffBrokenInventoryItem` | `source-ready` |  |
| 2 | `include-row` | `C3:F5F9` | 0x84 | battle visual effect helpers | `QueueVisualTileRowsLinear` | `source-ready` |  |
| 2 | `include-row` | `C3:F67D` | 0x88 | battle visual effect helpers | `QueueVisualTileRowsWrapped` | `source-ready` |  |
| 2 | `include-row` | `C3:F705` | 0xF6 | battle visual effect helpers | `QueueVisualTileBlockFromStream` | `source-ready` |  |
| 2 | `include-row` | `C3:F7FB` | 0x1E | battle visual effect helpers | `QueueFixedEfEb3dVisualTileBlock` | `source-ready` |  |
| 2 | `include-row` | `C3:F981` | 0x148 | battle visual effect helpers | `DispatchBattleVisualEffectToken` | `source-ready` |  |
| 2 | `include-row` | `C3:FAC9` | 0x40 | battle visual effect helpers | `DispatchBattleActorVisualEffectToken` | `source-ready` |  |
| 2 | `include-row` | `C3:FB09` | 0x16 | battle visual effect helpers | `CheckCurrentBattleActorVisualFlag` | `source-ready` |  |
| 3 | `embedded-label` | `C3:F3C5` | 0x234 | file-select visual transition helper | `RunFileSelectVisualTransition` | `source-ready` |  |

## Source Units

### `C3:E450` `WindowTickTransferDynamicTileBlock`

- include: `unknown/C3/C3E450.asm`
- unit kind: `include-row`
- size: `0x9F`
- subsystem: `window and battle text helpers`
- priority: `1`
- readiness: `source-ready`
- notes: Window/text helper corridor has caller and state evidence.; Internal entry labels should stay in the same source unit.

| Internal Address | Offset | Name |
| --- | ---: | --- |
| `C3:E4CA` | `+0x7A` | `ClearInstantPrinting` |
| `C3:E4D4` | `+0x84` | `SetInstantPrinting` |
| `C3:E4E0` | `+0x90` | `TickWindowWithoutInstantPrinting` |

### `C3:E4EF` `FindFirstFreeWindowSlot`

- include: `unknown/C3/C3E4EF.asm`
- unit kind: `include-row`
- size: `0x209`
- subsystem: `window and battle text helpers`
- priority: `1`
- readiness: `source-ready`
- notes: Window/text helper corridor has caller and state evidence.; Internal entry labels should stay in the same source unit.; Window lifecycle source contract keeps C3:E4EF and internal C3:E521 in one source unit.

| Internal Address | Offset | Name |
| --- | ---: | --- |
| `C3:E521` | `+0x32` | `CloseWindowAndReleaseTileState` |

### `C3:E6F8` `ClearFocusedPartyHpPpActorAndBlankRow`

- include: `unknown/C3/C3E6F8.asm`
- unit kind: `include-row`
- size: `0x65`
- subsystem: `window and battle text helpers`
- priority: `1`
- readiness: `source-ready`
- notes: Window/text helper corridor has caller and state evidence.

### `C3:E75D` `ResolveReflectedHitSideArticleTokens`

- include: `unknown/C3/C3E75D.asm`
- unit kind: `include-row`
- size: `0x86`
- subsystem: `window and battle text helpers`
- priority: `1`
- readiness: `source-ready`
- notes: Window/text helper corridor has caller and state evidence.; Internal entry labels should stay in the same source unit.

| Internal Address | Offset | Name |
| --- | ---: | --- |
| `C3:E773` | `+0x16` | `ClearFirstReflectedHitSideArticleTokenFlag` |
| `C3:E78F` | `+0x32` | `ClearSecondReflectedHitSideArticleTokenFlag` |

### `C3:E7E3` `ClearWindowRegisteredCopyChain`

- include: `unknown/C3/C3E7E3.asm`
- unit kind: `include-row`
- size: `0x6B`
- subsystem: `window and battle text helpers`
- priority: `1`
- readiness: `source-ready`
- notes: Window/text helper corridor has caller and state evidence.

### `C3:E977` `ReadCharacterInventorySlotByte`

- include: `data/unknown/C3E84E.asm#embedded`
- unit kind: `embedded-label`
- size: `0x29`
- subsystem: `inventory equipment and tracked items`
- priority: `1`
- readiness: `source-ready`
- containing include: `data/unknown/C3E84E.asm`
- notes: Inventory/equipment contract is now corrected around equipped inventory-slot references.; Mixed-row split plan provides standalone source-helper slice boundaries.; Contained by `data/unknown/C3E84E.asm` at `C3:E84E`.

### `C3:E9A0` `CheckEquippedInventorySlotReference`

- include: `data/unknown/C3E84E.asm#embedded`
- unit kind: `embedded-label`
- size: `0x57`
- subsystem: `inventory equipment and tracked items`
- priority: `1`
- readiness: `source-ready`
- containing include: `data/unknown/C3E84E.asm`
- notes: Inventory/equipment contract is now corrected around equipped inventory-slot references.; Mixed-row split plan provides standalone source-helper slice boundaries.; Contained by `data/unknown/C3E84E.asm` at `C3:E84E`.

### `C3:E9F7` `CheckEquippedInventoryItemPresence`

- include: `unknown/C3/C3E9F7.asm`
- unit kind: `include-row`
- size: `0xD9`
- subsystem: `inventory equipment and tracked items`
- priority: `1`
- readiness: `source-ready`
- notes: Inventory/equipment contract is now corrected around equipped inventory-slot references.

### `C3:EAD0` `RefreshEggFamilyLifecycleOnInsert`

- include: `unknown/C3/C3EAD0.asm`
- unit kind: `include-row`
- size: `0x4C`
- subsystem: `inventory equipment and tracked items`
- priority: `1`
- readiness: `source-ready`
- notes: Inventory/equipment contract is now corrected around equipped inventory-slot references.

### `C3:EB1C` `RefreshEggFamilyLifecycleOnRemove`

- include: `unknown/C3/C3EB1C.asm`
- unit kind: `include-row`
- size: `0xAE`
- subsystem: `inventory equipment and tracked items`
- priority: `1`
- readiness: `source-ready`
- notes: Inventory/equipment contract is now corrected around equipped inventory-slot references.

### `C3:EBCA` `SyncPartyOverlayTrackedItemFamilyState`

- include: `unknown/C3/C3EBCA.asm`
- unit kind: `include-row`
- size: `0x55`
- subsystem: `inventory equipment and tracked items`
- priority: `1`
- readiness: `source-ready`
- notes: Inventory/equipment contract is now corrected around equipped inventory-slot references.; Tracked-item sync source contract closes the D5:F4BB accumulator-width caveat.

### `C3:EC1F` `DepleteCharacterHp`

- include: `unknown/C3/C3EC1F.asm`
- unit kind: `include-row`
- size: `0x6C`
- subsystem: `HP PP stat adjustment helpers`
- priority: `1`
- readiness: `source-ready`
- notes: HP/PP adjustment quartet shares one direct/dynamic amount contract.

### `C3:EC8B` `RecoverCharacterHp`

- include: `unknown/C3/C3EC8B.asm`
- unit kind: `include-row`
- size: `0xA1`
- subsystem: `HP PP stat adjustment helpers`
- priority: `1`
- readiness: `source-ready`
- notes: HP/PP adjustment quartet shares one direct/dynamic amount contract.

### `C3:ED2C` `DepleteCharacterPp`

- include: `unknown/C3/C3ED2C.asm`
- unit kind: `include-row`
- size: `0x6C`
- subsystem: `HP PP stat adjustment helpers`
- priority: `1`
- readiness: `source-ready`
- notes: HP/PP adjustment quartet shares one direct/dynamic amount contract.

### `C3:ED98` `RecoverCharacterPp`

- include: `unknown/C3/C3ED98.asm`
- unit kind: `include-row`
- size: `0x7C`
- subsystem: `HP PP stat adjustment helpers`
- priority: `1`
- readiness: `source-ready`
- notes: HP/PP adjustment quartet shares one direct/dynamic amount contract.

### `C3:EE14` `CheckItemEquipmentSlotCompatibility`

- include: `unknown/C3/C3EE14.asm`
- unit kind: `include-row`
- size: `0x39`
- subsystem: `equipment and battle selector helpers`
- priority: `2`
- readiness: `source-ready`
- notes: Equipment/statistic selector helpers now have source-contract notes.

### `C3:EE4D` `RefreshWorldAndReleaseActiveVisualHandle`

- include: `unknown/C3/C3EE4D.asm`
- unit kind: `include-row`
- size: `0x2D`
- subsystem: `equipment and battle selector helpers`
- priority: `2`
- readiness: `source-ready`
- notes: Equipment/statistic selector helpers now have source-contract notes.

### `C3:EE7A` `ResolveStatisticSelectorValue`

- include: `unknown/C3/C3EE7A.asm`
- unit kind: `include-row`
- size: `0xA9`
- subsystem: `equipment and battle selector helpers`
- priority: `2`
- readiness: `source-ready`
- notes: Equipment/statistic selector helpers now have source-contract notes.

### `C3:F1EC` `TryRepairJeffBrokenInventoryItem`

- include: `unknown/C3/C3F1EC.asm`
- unit kind: `include-row`
- size: `0xC5`
- subsystem: `Jeff repair and PSI menu helpers`
- priority: `2`
- readiness: `source-ready`
- notes: Jeff repair source contract now pairs this mutating inventory repair helper with C1:D038.

### `C3:F3C5` `RunFileSelectVisualTransition`

- include: `data/unknown/C3F2B1.asm#embedded`
- unit kind: `embedded-label`
- size: `0x234`
- subsystem: `file-select visual transition helper`
- priority: `3`
- readiness: `source-ready`
- containing include: `data/unknown/C3F2B1.asm`
- notes: Mixed-row split plan provides standalone source-helper slice boundaries.; Contained by `data/unknown/C3F2B1.asm` at `C3:F2B1`.

### `C3:F5F9` `QueueVisualTileRowsLinear`

- include: `unknown/C3/C3F5F9.asm`
- unit kind: `include-row`
- size: `0x84`
- subsystem: `battle visual effect helpers`
- priority: `2`
- readiness: `source-ready`
- notes: Battle visual queue/effect helpers are source-ready but depend on adjacent C3 visual tables.

### `C3:F67D` `QueueVisualTileRowsWrapped`

- include: `unknown/C3/C3F67D.asm`
- unit kind: `include-row`
- size: `0x88`
- subsystem: `battle visual effect helpers`
- priority: `2`
- readiness: `source-ready`
- notes: Battle visual queue/effect helpers are source-ready but depend on adjacent C3 visual tables.

### `C3:F705` `QueueVisualTileBlockFromStream`

- include: `unknown/C3/C3F705.asm`
- unit kind: `include-row`
- size: `0xF6`
- subsystem: `battle visual effect helpers`
- priority: `2`
- readiness: `source-ready`
- notes: Battle visual queue/effect helpers are source-ready but depend on adjacent C3 visual tables.

### `C3:F7FB` `QueueFixedEfEb3dVisualTileBlock`

- include: `unknown/C3/C3F7FB.asm`
- unit kind: `include-row`
- size: `0x1E`
- subsystem: `battle visual effect helpers`
- priority: `2`
- readiness: `source-ready`
- notes: Battle visual queue/effect helpers are source-ready but depend on adjacent C3 visual tables.

### `C3:F981` `DispatchBattleVisualEffectToken`

- include: `unknown/C3/C3F981.asm`
- unit kind: `include-row`
- size: `0x148`
- subsystem: `battle visual effect helpers`
- priority: `2`
- readiness: `source-ready`
- notes: Battle visual queue/effect helpers are source-ready but depend on adjacent C3 visual tables.; Battle visual effect dispatch source contract preserves the token colour tables.

| Internal Address | Offset | Name |
| --- | ---: | --- |
| `C3:F9A2` | `+0x21` | `ApplyBattleVisualToken23To2dColourEffect` |
| `C3:FA4A` | `+0xC9` | `ApplyBattleVisualToken31To35ColourEffect` |
| `C3:FAC7` | `+0x146` | `ReturnFromBattleVisualEffectTokenDispatch` |

### `C3:FAC9` `DispatchBattleActorVisualEffectToken`

- include: `unknown/C3/C3FAC9.asm`
- unit kind: `include-row`
- size: `0x40`
- subsystem: `battle visual effect helpers`
- priority: `2`
- readiness: `source-ready`
- notes: Battle visual queue/effect helpers are source-ready but depend on adjacent C3 visual tables.

### `C3:FB09` `CheckCurrentBattleActorVisualFlag`

- include: `unknown/C3/C3FB09.asm`
- unit kind: `include-row`
- size: `0x16`
- subsystem: `battle visual effect helpers`
- priority: `2`
- readiness: `source-ready`
- notes: Battle visual queue/effect helpers are source-ready but depend on adjacent C3 visual tables.

## Orphan Source Labels

These source labels are not currently inside an addressed source-helper row. They need special handling during source carving.

| Address | Subsystem | Name | Reason |
| --- | --- | --- | --- |
| `C3:0100` | system screens | `DisplayAntiPiracyScreen` | system entry point label before the first addressed bank payload include |
| `C3:0142` | system screens | `DisplayFaultyGamePakScreen` | system entry point label before the first addressed bank payload include |
