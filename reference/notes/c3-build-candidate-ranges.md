# C3 build-candidate byte ranges

This manifest records ROM byte ranges for C3 helper modules that are being prepared for build-candidate promotion. It is a byte-equivalence precursor: it pins source-emission metadata to a concrete ROM slice before assembler integration.

## Summary

- ranges: `7`
- total bytes: `4553`
- source bytes: `4193`
- data gap bytes: `360`

## Ranges

| Level | Source Path | Range | Span Bytes | Source Bytes | Data Gap Bytes | SHA-1 |
| --- | --- | --- | ---: | ---: | ---: | --- |
| `build-candidate` | `src/c3/window_text_helpers.asm` | `C3:E450..C3:E84E` | 1022 | 1022 | 0 | `cf5ed3d3fae1e6adbd71e07feeee7419b5cf8207` |
| `build-candidate` | `src/c3/inventory_equipment_tracked_items.asm` | `C3:E977..C3:EC1F` | 680 | 680 | 0 | `5faf2c4d221e21edfa75e8aa5ce59031eca5b8c7` |
| `build-candidate` | `src/c3/hp_pp_adjustment_helpers.asm` | `C3:EC1F..C3:EE14` | 501 | 501 | 0 | `010b248a397746426cb6846d75c2170b2e12c265` |
| `build-candidate` | `src/c3/equipment_battle_selector_helpers.asm` | `C3:EE14..C3:EF23` | 271 | 271 | 0 | `715d3d673026fff3c5f799264f2962425bcf4ab3` |
| `build-candidate` | `src/c3/jeff_repair_psi_helpers.asm` | `C3:F1EC..C3:F2B1` | 197 | 197 | 0 | `78d0a226bf94c9d95e0a52a8c176d10d84e2a66c` |
| `build-candidate` | `src/c3/file_select_visual_transition_helper.asm` | `C3:F3C5..C3:F5F9` | 564 | 564 | 0 | `e7a7bab265c12acac5539c574e204b99338d2c31` |
| `build-candidate` | `src/c3/battle_visual_effect_helpers.asm` | `C3:F5F9..C3:FB1F` | 1318 | 958 | 360 | `3164d2a491b0fe7e790fb85ef0266ae2df073f98` |

## Source Segments

### `src/c3/window_text_helpers.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C3:E450..C3:E4EF` | 159 | `WindowTickTransferDynamicTileBlock` | `272aa3aff41aa7a21d787e6b5a479bf7a0776dff` |
| `C3:E4EF..C3:E6F8` | 521 | `FindFirstFreeWindowSlot` | `a16f0e5c50d8f15fb7e880786103676c39c88eb2` |
| `C3:E6F8..C3:E75D` | 101 | `ClearFocusedPartyHpPpActorAndBlankRow` | `a0eea0ae022b2016ca4c0a5f8e69365306addbc5` |
| `C3:E75D..C3:E7E3` | 134 | `ResolveReflectedHitSideArticleTokens` | `c941a39d04f86a3f74a6906e9af6750467d46397` |
| `C3:E7E3..C3:E84E` | 107 | `ClearWindowRegisteredCopyChain` | `80bcc70bdd0ba8135eeb9e51c1faadcc0c0bc052` |

### `src/c3/inventory_equipment_tracked_items.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C3:E977..C3:E9A0` | 41 | `ReadCharacterInventorySlotByte` | `518c22bc2e33bca2447f094a79a4d8d1c3e85c1f` |
| `C3:E9A0..C3:E9F7` | 87 | `CheckEquippedInventorySlotReference` | `e4e5818f5c3ffe09eaf055a11eb8c61c1b1f2b98` |
| `C3:E9F7..C3:EAD0` | 217 | `CheckEquippedInventoryItemPresence` | `2b0c924b0e5bdde6126f78f9671d75d5426344ee` |
| `C3:EAD0..C3:EB1C` | 76 | `RefreshEggFamilyLifecycleOnInsert` | `687b1fdc6270bdcdc4f69ba373ccc8c1789e0a1e` |
| `C3:EB1C..C3:EBCA` | 174 | `RefreshEggFamilyLifecycleOnRemove` | `8028c61b67c2e04087e2209c028a69a5ba88ccf2` |
| `C3:EBCA..C3:EC1F` | 85 | `SyncPartyOverlayTrackedItemFamilyState` | `d32d690d7ee3d057e5851329d30f1926994660db` |

### `src/c3/hp_pp_adjustment_helpers.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C3:EC1F..C3:EC8B` | 108 | `DepleteCharacterHp` | `c895f05cec449f0f1c431a49bc18d365780abd33` |
| `C3:EC8B..C3:ED2C` | 161 | `RecoverCharacterHp` | `dd06e768f1031811d8a30bb0f754ef956436362a` |
| `C3:ED2C..C3:ED98` | 108 | `DepleteCharacterPp` | `554efd5dc2cde686b6d0b4c4b737cc3b551abfe7` |
| `C3:ED98..C3:EE14` | 124 | `RecoverCharacterPp` | `5c97b005d6e4a6472956aaa48017cf8c4a6cf429` |

### `src/c3/equipment_battle_selector_helpers.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C3:EE14..C3:EE4D` | 57 | `CheckItemEquipmentSlotCompatibility` | `dcf848ef5b38a9c35d94efa694a069660835ef30` |
| `C3:EE4D..C3:EE7A` | 45 | `RefreshWorldAndReleaseActiveVisualHandle` | `fe8f86d9a41323da252bdd701221abfa41a21b85` |
| `C3:EE7A..C3:EF23` | 169 | `ResolveStatisticSelectorValue` | `25ae1311daa18f4608918c20bec335fdef312c41` |

### `src/c3/jeff_repair_psi_helpers.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C3:F1EC..C3:F2B1` | 197 | `TryRepairJeffBrokenInventoryItem` | `78d0a226bf94c9d95e0a52a8c176d10d84e2a66c` |

### `src/c3/file_select_visual_transition_helper.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C3:F3C5..C3:F5F9` | 564 | `RunFileSelectVisualTransition` | `e7a7bab265c12acac5539c574e204b99338d2c31` |

### `src/c3/battle_visual_effect_helpers.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| `C3:F5F9..C3:F67D` | 132 | `QueueVisualTileRowsLinear` | `bfa86628fb5c85a4c058d51070016e4419357172` |
| `C3:F67D..C3:F705` | 136 | `QueueVisualTileRowsWrapped` | `41fcd4a1c996572c1284aa382241a99debaeff12` |
| `C3:F705..C3:F7FB` | 246 | `QueueVisualTileBlockFromStream` | `a60740040448d593780ddde476bf3312acbdfe76` |
| `C3:F7FB..C3:F819` | 30 | `QueueFixedEfEb3dVisualTileBlock` | `d17491c6e2189f3d9405f9b97345a3c5975c98ed` |
| `C3:F981..C3:FAC9` | 328 | `DispatchBattleVisualEffectToken` | `eaa5fd3f993419a0e055ef3793fbc031f34418be` |
| `C3:FAC9..C3:FB09` | 64 | `DispatchBattleActorVisualEffectToken` | `e7543045832c1f9fe65781892a0ff147be3cc8be` |
| `C3:FB09..C3:FB1F` | 22 | `CheckCurrentBattleActorVisualFlag` | `035e00e211fd3bc84014a18fd6bd9f9da9eba462` |

Data gaps inside protected span:

- `C3:F819..C3:F981` (360 bytes, SHA-1 `93df16de751cde7f7fb95ec2810abfa30cddfe4d`)


## Labels

### `src/c3/window_text_helpers.asm`

- `C3:E450 WindowTickTransferDynamicTileBlock`
- `C3:E4CA ClearInstantPrinting`
- `C3:E4D4 SetInstantPrinting`
- `C3:E4E0 TickWindowWithoutInstantPrinting`
- `C3:E4EF FindFirstFreeWindowSlot`
- `C3:E521 CloseWindowAndReleaseTileState`
- `C3:E6F8 ClearFocusedPartyHpPpActorAndBlankRow`
- `C3:E75D ResolveReflectedHitSideArticleTokens`
- `C3:E773 ClearFirstReflectedHitSideArticleTokenFlag`
- `C3:E78F ClearSecondReflectedHitSideArticleTokenFlag`
- `C3:E7E3 ClearWindowRegisteredCopyChain`

### `src/c3/inventory_equipment_tracked_items.asm`

- `C3:E977 ReadCharacterInventorySlotByte`
- `C3:E9A0 CheckEquippedInventorySlotReference`
- `C3:E9F7 CheckEquippedInventoryItemPresence`
- `C3:EAD0 RefreshEggFamilyLifecycleOnInsert`
- `C3:EB1C RefreshEggFamilyLifecycleOnRemove`
- `C3:EBCA SyncPartyOverlayTrackedItemFamilyState`

### `src/c3/hp_pp_adjustment_helpers.asm`

- `C3:EC1F DepleteCharacterHp`
- `C3:EC8B RecoverCharacterHp`
- `C3:ED2C DepleteCharacterPp`
- `C3:ED98 RecoverCharacterPp`

### `src/c3/equipment_battle_selector_helpers.asm`

- `C3:EE14 CheckItemEquipmentSlotCompatibility`
- `C3:EE4D RefreshWorldAndReleaseActiveVisualHandle`
- `C3:EE7A ResolveStatisticSelectorValue`

### `src/c3/jeff_repair_psi_helpers.asm`

- `C3:F1EC TryRepairJeffBrokenInventoryItem`

### `src/c3/file_select_visual_transition_helper.asm`

- `C3:F3C5 RunFileSelectVisualTransition`

### `src/c3/battle_visual_effect_helpers.asm`

- `C3:F5F9 QueueVisualTileRowsLinear`
- `C3:F67D QueueVisualTileRowsWrapped`
- `C3:F705 QueueVisualTileBlockFromStream`
- `C3:F7FB QueueFixedEfEb3dVisualTileBlock`
- `C3:F981 DispatchBattleVisualEffectToken`
- `C3:F9A2 ApplyBattleVisualToken23To2dColourEffect`
- `C3:FA4A ApplyBattleVisualToken31To35ColourEffect`
- `C3:FAC7 ReturnFromBattleVisualEffectTokenDispatch`
- `C3:FAC9 DispatchBattleActorVisualEffectToken`
- `C3:FB09 CheckCurrentBattleActorVisualFlag`
