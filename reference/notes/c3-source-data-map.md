# C3 source/data extraction map

Generated from the ebsrc bankconfig include order plus local working-name, script-payload, and data-contract manifests. This is the C3 split front door: it says which addressed includes should become 65816 source, which should stay script/data assets, and which already have structured table contracts.

## Summary

- schema: `earthbound-decomp.c3-source-data-map.v1`
- addressed include rows: `193`
- working labels: `172` (`89` internal or named-include labels)
- script payload labels: `84` (`47` internal labels)
- data-contract labels: `36` (`12` internal labels)
- working-named addressed rows: `83`
- script payload include-start rows: `37`
- contract-backed include-start rows: `24`
- by extraction class: `{'contract-backed-data': 20, 'contract-backed-data-prefix': 3, 'effect-script-asset': 1, 'event-bytecode-asset': 14, 'event-bytecode-label': 16, 'event-script-asset': 105, 'mixed-data-script-row': 1, 'mixed-data-source-row': 2, 'movement-pattern-data': 6, 'null-stub': 1, 'source-helper': 24}`
- supplemental by extraction class: `{'contract-backed-data': 12, 'event-bytecode-asset': 27, 'event-bytecode-label': 19, 'movement-pattern-data': 1, 'source-adjacent-data': 15, 'source-helper': 14, 'working-label': 1}`
- script decode status: `{'complete': 30, 'not-applicable': 7}`

## Extraction Classes

| Class | Meaning |
| --- | --- |
| `source-helper` | Ordinary 65816 helper candidate for source extraction. |
| `event-script-asset`, `event-bytecode-asset`, `event-bytecode-label` | Event/actionscript bytecode; export as script assets first. |
| `movement-pattern-data`, `effect-script-asset` | VM-adjacent payloads, but not event bytecode. |
| `contract-backed-data` | Structured ROM table with a data-contract entry. |
| `contract-backed-data-prefix` | Include starts with a structured leading contract and a remaining tail that still needs splitting or preservation. |
| `mixed-data-source-row` | Addressed data include that contains embedded ordinary source-helper labels and should be split before source emission. |
| `mixed-data-script-row` | Addressed data include that contains embedded event/actionscript labels and should be split before script emission. |
| `raw-or-named-data`, `source-adjacent-data`, `data-or-helper-frontier` | Data/include starts that are documented but may need later consumer polishing. |
| `null-stub` | Explicit null/padding stub; preserve, but keep out of source-helper worklists. |

## Addressed Include Rows

| Address | Size | Include | Class | Name / Contract | Decode |
| --- | ---: | --- | --- | --- | --- |
| `C3:0188` | 0x10D | `data/unknown/C30188.asm` | `mixed-data-script-row` |  |  |
| `C3:0295` | 0x6F6 | `data/events/C30295.asm` | `event-bytecode-asset` | `MoveActiveEntityLeftToScriptVarsAndWait` | `complete` |
| `C3:098B` | 0x94 | `data/events/C3098B.asm` | `event-script-asset` |  |  |
| `C3:0A1F` | 0x236 | `data/events/C30A1F.asm` | `event-script-asset` |  |  |
| `C3:0C55` | 0x12 | `data/events/C30C55.asm` | `event-script-asset` |  |  |
| `C3:0C67` | 0x10C6 | `data/events/C30C67.asm` | `event-script-asset` |  |  |
| `C3:1D2D` | 0x22 | `data/events/C31D2D.asm` | `event-script-asset` |  |  |
| `C3:1D4F` | 0xA5 | `data/events/C31D4F.asm` | `event-script-asset` |  |  |
| `C3:1DF4` | 0x39 | `data/events/C31DF4.asm` | `event-script-asset` |  |  |
| `C3:1E2D` | 0x94 | `data/events/C31E2D.asm` | `event-script-asset` |  |  |
| `C3:1EC1` | 0x17 | `data/events/C31EC1.asm` | `event-script-asset` |  |  |
| `C3:1ED8` | 0x17 | `data/events/C31ED8.asm` | `event-script-asset` |  |  |
| `C3:1EEF` | 0x249 | `data/events/C31EEF.asm` | `event-script-asset` |  |  |
| `C3:2138` | 0xB9A | `data/events/C32138.asm` | `event-script-asset` |  |  |
| `C3:2CD2` | 0x6C7 | `data/events/C32CD2.asm` | `event-script-asset` |  |  |
| `C3:3399` | 0x11 | `data/events/C33399.asm` | `event-script-asset` |  |  |
| `C3:33AA` | 0x11 | `data/events/C333AA.asm` | `event-script-asset` |  |  |
| `C3:33BB` | 0x11 | `data/events/C333BB.asm` | `event-script-asset` |  |  |
| `C3:33CC` | 0x11 | `data/events/C333CC.asm` | `event-script-asset` |  |  |
| `C3:33DD` | 0x16C | `data/events/C333DD.asm` | `event-script-asset` |  |  |
| `C3:3549` | 0x6B2 | `data/events/C33549.asm` | `event-script-asset` |  |  |
| `C3:3BFB` | 0x1D | `data/events/C33BFB.asm` | `event-script-asset` |  |  |
| `C3:3C18` | 0x5 | `data/events/C33C18.asm` | `event-script-asset` |  |  |
| `C3:3C1D` | 0x1A1 | `data/events/C33C1D.asm` | `event-script-asset` |  |  |
| `C3:3DBE` | 0x5D4 | `data/events/C33DBE.asm` | `event-script-asset` |  |  |
| `C3:4392` | 0x1C | `data/events/C34392.asm` | `event-script-asset` |  |  |
| `C3:43AE` | 0x2D | `data/events/C343AE.asm` | `event-script-asset` |  |  |
| `C3:43DB` | 0x4E9 | `data/events/C343DB.asm` | `event-bytecode-label` | `LoopTimedDeliveryDeparturePulseUntilOffscreen` | `complete` |
| `C3:48C4` | 0xA0 | `data/events/C348C4.asm` | `event-script-asset` |  |  |
| `C3:4964` | 0xFD | `data/events/C34964.asm` | `event-script-asset` |  |  |
| `C3:4A61` | 0x101 | `data/events/C34A61.asm` | `event-script-asset` |  |  |
| `C3:4B62` | 0x1D7 | `data/events/C34B62.asm` | `event-script-asset` |  |  |
| `C3:4D39` | 0x13A | `data/events/C34D39.asm` | `event-script-asset` |  |  |
| `C3:4E73` | 0x1118 | `data/events/C34E73.asm` | `event-script-asset` |  |  |
| `C3:5F8B` | 0x2B | `data/events/C35F8B.asm` | `event-script-asset` |  |  |
| `C3:5FB6` | 0x17 | `data/events/C35FB6.asm` | `event-script-asset` |  |  |
| `C3:5FCD` | 0x2F3 | `data/events/C35FCD.asm` | `event-script-asset` |  |  |
| `C3:62C0` | 0x574 | `data/events/C362C0.asm` | `event-script-asset` |  |  |
| `C3:6834` | 0x20A | `data/events/C36834.asm` | `event-script-asset` |  |  |
| `C3:6A3E` | 0x3 | `data/events/C36A3E.asm` | `event-script-asset` |  |  |
| `C3:6A41` | 0x173 | `data/events/C36A41.asm` | `event-script-asset` |  |  |
| `C3:6BB4` | 0x36 | `data/events/C36BB4.asm` | `event-script-asset` |  |  |
| `C3:6BEA` | 0x12E | `data/events/C36BEA.asm` | `event-script-asset` |  |  |
| `C3:6D18` | 0x129 | `data/events/C36D18.asm` | `event-script-asset` |  |  |
| `C3:6E41` | 0x5F8 | `data/events/C36E41.asm` | `event-script-asset` |  |  |
| `C3:7439` | 0x10C | `data/events/C37439.asm` | `event-script-asset` |  |  |
| `C3:7545` | 0x14 | `data/events/C37545.asm` | `event-script-asset` |  |  |
| `C3:7559` | 0x523 | `data/events/C37559.asm` | `event-script-asset` |  |  |
| `C3:7A7C` | 0x8E1 | `data/events/C37A7C.asm` | `event-script-asset` |  |  |
| `C3:835D` | 0x5F | `data/events/C3835D.asm` | `event-script-asset` |  |  |
| `C3:83BC` | 0x5BC | `data/events/C383BC.asm` | `event-script-asset` |  |  |
| `C3:8978` | 0x26 | `data/events/C38978.asm` | `event-script-asset` |  |  |
| `C3:899E` | 0x1129 | `data/events/C3899E.asm` | `event-script-asset` |  |  |
| `C3:9AC7` | 0x33A | `data/events/C39AC7.asm` | `event-script-asset` |  |  |
| `C3:9E01` | 0x1F1 | `data/events/C39E01.asm` | `event-script-asset` |  |  |
| `C3:9FF2` | 0x1E | `data/unknown/C39FF2.asm` | `movement-pattern-data` | `IntroMovementPatternPointerTable` | `not-applicable` |
| `C3:A010` | 0xB | `data/unknown/C3A010.asm` | `movement-pattern-data` | `IntroMovementPattern09Loop` | `not-applicable` |
| `C3:A01B` | 0xB | `data/unknown/C3A01B.asm` | `movement-pattern-data` | `IntroMovementPattern08Loop` | `not-applicable` |
| `C3:A026` | 0x7 | `data/unknown/C3A026.asm` | `movement-pattern-data` | `IntroMovementPatternFFLoop` | `not-applicable` |
| `C3:A02D` | 0xB | `data/unknown/C3A02D.asm` | `movement-pattern-data` | `IntroMovementPattern08LoopAlt` | `not-applicable` |
| `C3:A038` | 0x47 | `data/unknown/C3A038.asm` | `movement-pattern-data` | `IntroMovementPattern04Loop` | `not-applicable` |
| `C3:A07F` | 0x20 | `data/events/C3A07F.asm` | `event-bytecode-asset` | `HaltEventScript` | `complete` |
| `C3:A09F` | 0x13 | `data/events/C3A09F.asm` | `event-bytecode-label` | `LoopActiveEntityWalkAnimationPulse` | `complete` |
| `C3:A0B2` | 0x13 | `data/events/C3A0B2.asm` | `event-bytecode-label` | `LoopActiveEntityWalkPulse24Frame` | `complete` |
| `C3:A0C5` | 0x13 | `data/events/C3A0C5.asm` | `event-bytecode-label` | `LoopActiveEntityWalkPulse12Frame` | `complete` |
| `C3:A0D8` | 0x56 | `data/events/C3A0D8.asm` | `event-bytecode-label` | `LoopActiveEntityWalkPulse9FrameConditional` | `complete` |
| `C3:A12E` | 0x30 | `data/events/C3A12E.asm` | `event-bytecode-label` | `LoopActiveEntityWalkPulseVar4Countdown` | `complete` |
| `C3:A15E` | 0x1D | `data/events/C3A15E.asm` | `event-bytecode-label` | `LoopC40015Var4GatedPulseUntilRelease` | `complete` |
| `C3:A17B` | 0x14 | `data/events/C3A17B.asm` | `event-bytecode-label` | `LoopC40015SlowPulseUntilRelease` | `complete` |
| `C3:A18F` | 0x14 | `data/events/C3A18F.asm` | `event-bytecode-label` | `LoopC40015FastPulseUntilRelease` | `complete` |
| `C3:A1A3` | 0x14 | `data/events/C3A1A3.asm` | `event-script-asset` |  |  |
| `C3:A1B7` | 0x14 | `data/events/C3A1B7.asm` | `event-script-asset` |  |  |
| `C3:A1CB` | 0x14 | `data/events/C3A1CB.asm` | `event-script-asset` |  |  |
| `C3:A1DF` | 0x14 | `data/events/C3A1DF.asm` | `event-bytecode-label` | `LoopActiveEntityWalkPulse2FrameC40015Branch` | `complete` |
| `C3:A1F3` | 0x16 | `data/events/C3A1F3.asm` | `event-bytecode-label` | `LoopC40015Pulse16FrameUntilRelease` | `complete` |
| `C3:A209` | 0x5 | `data/events/C3A209.asm` | `event-bytecode-asset` | `DelayThenReleaseCurrentVisualEntity` | `complete` |
| `C3:A20E` | 0x54 | `data/events/C3A20E.asm` | `event-bytecode-label` | `LoopVar0SelectedAnimationUntilOffscreen` | `complete` |
| `C3:A262` | 0xF | `data/events/C3A262.asm` | `event-bytecode-label` | `LoopActiveEntityCollisionProbeRefresh` | `complete` |
| `C3:A271` | 0x1 | `data/events/C3A271.asm` | `event-script-asset` |  |  |
| `C3:A272` | 0x18F | `data/events/C3A272.asm` | `event-script-asset` |  |  |
| `C3:A401` | 0x61D | `data/events/C3A401.asm` | `event-bytecode-asset` | `InitNpcAttentionPathIfNoCachedNeighbor` | `complete` |
| `C3:AA1E` | 0xD | `data/events/C3AA1E.asm` | `event-script-asset` |  |  |
| `C3:AA2B` | 0xD | `data/events/C3AA2B.asm` | `event-script-asset` |  |  |
| `C3:AA38` | 0xE | `data/events/C3AA38.asm` | `event-bytecode-asset` | `InitActionScriptMovementState` | `complete` |
| `C3:AA46` | 0x14 | `data/events/C3AA46.asm` | `event-bytecode-asset` | `InitMovementPreset40_00Pulse24Frame` | `complete` |
| `C3:AA5A` | 0x14 | `data/events/C3AA5A.asm` | `event-bytecode-asset` | `InitMovementPreset00_01Pulse12Frame` | `complete` |
| `C3:AA6E` | 0x14 | `data/events/C3AA6E.asm` | `event-bytecode-asset` | `InitMovementPreset60_01Pulse9Frame` | `complete` |
| `C3:AA82` | 0x14 | `data/events/C3AA82.asm` | `event-bytecode-asset` | `InitMovementPreset00_02Pulse6Frame` | `complete` |
| `C3:AA96` | 0x14 | `data/events/C3AA96.asm` | `event-bytecode-asset` | `InitMovementPreset00_06Pulse2Frame` | `complete` |
| `C3:AAAA` | 0xE | `data/events/C3AAAA.asm` | `event-bytecode-asset` | `InitMovementPresetVar4Countdown` | `complete` |
| `C3:AAB8` | 0xA | `data/events/C3AAB8.asm` | `event-script-asset` |  |  |
| `C3:AAC2` | 0x14 | `data/events/C3AAC2.asm` | `event-script-asset` |  |  |
| `C3:AAD6` | 0x14 | `data/events/C3AAD6.asm` | `event-script-asset` |  |  |
| `C3:AAEA` | 0x14 | `data/events/C3AAEA.asm` | `event-script-asset` |  |  |
| `C3:AAFE` | 0x14 | `data/events/C3AAFE.asm` | `event-script-asset` |  |  |
| `C3:AB12` | 0x14 | `data/events/C3AB12.asm` | `event-bytecode-asset` | `InitMovementPreset00_06C40015Branch` | `complete` |
| `C3:AB26` | 0x11 | `data/events/C3AB26.asm` | `event-bytecode-asset` | `InitAlternatePhysicsVar4WalkPulse` | `complete` |
| `C3:AB37` | 0xD | `data/events/C3AB37.asm` | `event-script-asset` |  |  |
| `C3:AB44` | 0x15 | `data/events/C3AB44.asm` | `event-bytecode-asset` | `RefreshActiveEntityDirectionAndVisualProfile` | `complete` |
| `C3:AB59` | 0xE | `data/events/C3AB59.asm` | `event-bytecode-label` | `WaitForActiveEntityMovementToFinish` | `complete` |
| `C3:AB67` | 0x23 | `data/events/C3AB67.asm` | `event-script-asset` |  |  |
| `C3:AB8A` | 0xA | `data/events/C3AB8A.asm` | `event-bytecode-label` | `WaitUntilPlayerLeavesActiveArea` | `complete` |
| `C3:AB94` | 0xA | `data/events/C3AB94.asm` | `event-script-asset` |  |  |
| `C3:AB9E` | 0x42 | `data/events/C3AB9E.asm` | `event-script-asset` |  |  |
| `C3:ABE0` | 0x3C3 | `data/events/C3ABE0.asm` | `event-script-asset` |  |  |
| `C3:AFA3` | 0x113 | `data/events/C3AFA3.asm` | `event-bytecode-label` | `LoopPartyLooksAtActiveEntity` | `complete` |
| `C3:B0B6` | 0x37B | `data/events/C3B0B6.asm` | `event-script-asset` |  |  |
| `C3:B431` | 0x2DB | `data/events/C3B431.asm` | `event-script-asset` |  |  |
| `C3:B70C` | 0x397 | `data/events/C3B70C.asm` | `event-script-asset` |  |  |
| `C3:BAA3` | 0x21 | `data/events/C3BAA3.asm` | `event-script-asset` |  |  |
| `C3:BAC4` | 0x13 | `data/events/C3BAC4.asm` | `event-script-asset` |  |  |
| `C3:BAD7` | 0x85 | `data/events/C3BAD7.asm` | `event-script-asset` |  |  |
| `C3:BB5C` | 0x17 | `data/events/C3BB5C.asm` | `event-script-asset` |  |  |
| `C3:BB73` | 0x190 | `data/events/C3BB73.asm` | `event-script-asset` |  |  |
| `C3:BD03` | 0x1A1 | `data/events/C3BD03.asm` | `event-script-asset` |  |  |
| `C3:BEA4` | 0x30 | `data/events/C3BEA4.asm` | `event-script-asset` |  |  |
| `C3:BED4` | 0x26F | `data/events/C3BED4.asm` | `event-script-asset` |  |  |
| `C3:C143` | 0x9D | `data/events/C3C143.asm` | `event-script-asset` |  |  |
| `C3:C1E0` | 0x2F | `data/events/C3C1E0.asm` | `event-script-asset` |  |  |
| `C3:C20F` | 0x18 | `data/events/C3C20F.asm` | `event-script-asset` |  |  |
| `C3:C227` | 0x136 | `data/events/C3C227.asm` | `event-script-asset` |  |  |
| `C3:C35D` | 0x4B3 | `data/events/C3C35D.asm` | `event-script-asset` |  |  |
| `C3:C810` | 0xA | `data/events/C3C810.asm` | `event-script-asset` |  |  |
| `C3:C81A` | 0xA | `data/events/C3C81A.asm` | `event-script-asset` |  |  |
| `C3:C824` | 0x4D | `data/events/C3C824.asm` | `event-script-asset` |  |  |
| `C3:C871` | 0x8C | `data/events/C3C871.asm` | `event-script-asset` |  |  |
| `C3:C8FD` | 0xF | `data/events/C3C8FD.asm` | `event-script-asset` |  |  |
| `C3:C90C` | 0x42 | `data/events/C3C90C.asm` | `event-script-asset` |  |  |
| `C3:C94E` | 0x2D6 | `data/events/C3C94E.asm` | `event-script-asset` |  |  |
| `C3:CC24` | 0x38 | `data/events/C3CC24.asm` | `event-script-asset` |  |  |
| `C3:CC5C` | 0x38 | `data/events/C3CC5C.asm` | `event-script-asset` |  |  |
| `C3:CC94` | 0x14 | `data/events/C3CC94.asm` | `event-script-asset` |  |  |
| `C3:CCA8` | 0x1FA | `data/events/C3CCA8.asm` | `event-script-asset` |  |  |
| `C3:CEA2` | 0x17 | `data/events/C3CEA2.asm` | `event-script-asset` |  |  |
| `C3:CEB9` | 0x1EB | `data/events/C3CEB9.asm` | `event-script-asset` |  |  |
| `C3:D0A4` | 0x86F | `data/events/C3D0A4.asm` | `event-script-asset` |  |  |
| `C3:D913` | 0x267 | `data/events/C3D913.asm` | `event-script-asset` |  |  |
| `C3:DB7A` | 0x61 | `data/events/C3DB7A.asm` | `event-script-asset` |  |  |
| `C3:DBDB` | 0x3B5 | `data/events/C3DBDB.asm` | `event-script-asset` |  |  |
| `C3:DF90` | 0x25 | `data/events/C3DF90.asm` | `event-script-asset` |  |  |
| `C3:DFB5` | 0x1F | `data/events/C3DFB5.asm` | `event-script-asset` |  |  |
| `C3:DFD4` | 0x14 | `data/events/C3DFD4.asm` | `event-script-asset` |  |  |
| `C3:DFE8` | 0x160 | `data/unknown/C3DFE8.asm` | `contract-backed-data-prefix` | `PATHFINDING_TILE_CONTEXT_GATE_TABLE` |  |
| `C3:E148` | 0x10 | `data/unknown/C3E148.asm` | `contract-backed-data` | `InteractionProbeDirectionXOffsetTable / INTERACTION_PROBE_DIRECTION_X_OFFSETS` |  |
| `C3:E158` | 0x10 | `data/unknown/C3E158.asm` | `contract-backed-data` | `InteractionProbeDirectionYOffsetTable / INTERACTION_PROBE_DIRECTION_Y_OFFSETS` |  |
| `C3:E168` | 0x70 | `data/unknown/C3E168.asm` | `contract-backed-data-prefix` | `INTERACTION_RESULT_FACING_REMAP_TABLE` |  |
| `C3:E1D8` | 0x8 | `data/unknown/C3E1D8.asm` | `contract-backed-data` | `MapEntityPlacementDirectionParamTable / MAP_ENTITY_PLACEMENT_DIRECTION_PARAM_TABLE` |  |
| `C3:E1E0` | 0x20 | `data/unknown/C3E1E0.asm` | `contract-backed-data` | `MapEntityPlacementDirectionParamTable_Page1 / MAP_ENTITY_PLACEMENT_DIRECTION_PARAM_TABLE_PAGE1` |  |
| `C3:E200` | 0x8 | `data/unknown/C3E200.asm` | `contract-backed-data` | `StagedMovementPrimaryDirectionParamTable / STAGED_MOVEMENT_PRIMARY_DIRECTION_PARAM_TABLE` |  |
| `C3:E208` | 0x8 | `data/unknown/C3E208.asm` | `contract-backed-data` | `StagedMovementAlternateDirectionParamTable / STAGED_MOVEMENT_ALTERNATE_DIRECTION_PARAM_TABLE` |  |
| `C3:E210` | 0x8 | `data/unknown/C3E210.asm` | `contract-backed-data` | `StagedMovementSubtileOffsetSetA_X / STAGED_MOVEMENT_SUBTILE_OFFSET_SET_A_X` |  |
| `C3:E218` | 0x8 | `data/unknown/C3E218.asm` | `contract-backed-data` | `StagedMovementSubtileOffsetSetA_Y / STAGED_MOVEMENT_SUBTILE_OFFSET_SET_A_Y` |  |
| `C3:E220` | 0x8 | `data/unknown/C3E220.asm` | `contract-backed-data` | `StagedMovementSubtileOffsetSetB_X / STAGED_MOVEMENT_SUBTILE_OFFSET_SET_B_X` |  |
| `C3:E228` | 0x8 | `data/unknown/C3E228.asm` | `contract-backed-data` | `StagedMovementSubtileOffsetSetB_Y / STAGED_MOVEMENT_SUBTILE_OFFSET_SET_B_Y` |  |
| `C3:E230` | 0x10 | `data/unknown/C3E230.asm` | `contract-backed-data` | `DoorCandidateDirectionOffsetX / DOOR_CANDIDATE_DIRECTION_OFFSET_X` |  |
| `C3:E240` | 0x1B8 | `data/unknown/C3E240.asm` | `contract-backed-data-prefix` | `DoorCandidateDirectionOffsetY / DOOR_CANDIDATE_DIRECTION_OFFSET_Y` |  |
| `C3:E3F8` | 0x16 | `data/unknown/C3E3F8.asm` | `contract-backed-data` | `MenuCursorTilePrefixTable / MENU_CURSOR_TILE_PREFIX_TABLE` |  |
| `C3:E40E` | 0xE | `data/unknown/C3E40E.asm` | `contract-backed-data` | `TitleNameBufferCursorTileRun / TITLE_NAME_BUFFER_CURSOR_TILE_RUN` |  |
| `C3:E41C` | 0x30 | `data/unknown/C3E41C.asm` | `contract-backed-data` | `BlinkingTriangleWaitFrame0Tiles / BLINKING_TRIANGLE_WAIT_FRAME_TILES` |  |
| `C3:E44C` | 0x4 | `data/unknown/C3E44C.asm` | `contract-backed-data` | `WindowTickTransferPreludeData / WINDOW_TICK_TRANSFER_PRELUDE_WORDS` |  |
| `C3:E450` | 0x9F | `unknown/C3/C3E450.asm` | `source-helper` | `WindowTickTransferDynamicTileBlock` |  |
| `C3:E4EF` | 0x209 | `unknown/C3/C3E4EF.asm` | `source-helper` | `FindFirstFreeWindowSlot` |  |
| `C3:E6F8` | 0x65 | `unknown/C3/C3E6F8.asm` | `source-helper` | `ClearFocusedPartyHpPpActorAndBlankRow` |  |
| `C3:E75D` | 0x86 | `unknown/C3/C3E75D.asm` | `source-helper` | `ResolveReflectedHitSideArticleTokens` |  |
| `C3:E7E3` | 0x6B | `unknown/C3/C3E7E3.asm` | `source-helper` | `ClearWindowRegisteredCopyChain` |  |
| `C3:E84E` | 0x1A9 | `data/unknown/C3E84E.asm` | `mixed-data-source-row` |  |  |
| `C3:E9F7` | 0xD9 | `unknown/C3/C3E9F7.asm` | `source-helper` | `CheckEquippedInventoryItemPresence` |  |
| `C3:EAD0` | 0x4C | `unknown/C3/C3EAD0.asm` | `source-helper` | `RefreshEggFamilyLifecycleOnInsert` |  |
| `C3:EB1C` | 0xAE | `unknown/C3/C3EB1C.asm` | `source-helper` | `RefreshEggFamilyLifecycleOnRemove` |  |
| `C3:EBCA` | 0x55 | `unknown/C3/C3EBCA.asm` | `source-helper` | `SyncPartyOverlayTrackedItemFamilyState` |  |
| `C3:EC1F` | 0x6C | `unknown/C3/C3EC1F.asm` | `source-helper` | `DepleteCharacterHp` |  |
| `C3:EC8B` | 0xA1 | `unknown/C3/C3EC8B.asm` | `source-helper` | `RecoverCharacterHp` |  |
| `C3:ED2C` | 0x6C | `unknown/C3/C3ED2C.asm` | `source-helper` | `DepleteCharacterPp` |  |
| `C3:ED98` | 0x7C | `unknown/C3/C3ED98.asm` | `source-helper` | `RecoverCharacterPp` |  |
| `C3:EE14` | 0x39 | `unknown/C3/C3EE14.asm` | `source-helper` | `CheckItemEquipmentSlotCompatibility` |  |
| `C3:EE4D` | 0x2D | `unknown/C3/C3EE4D.asm` | `source-helper` | `RefreshWorldAndReleaseActiveVisualHandle` |  |
| `C3:EE7A` | 0xA9 | `unknown/C3/C3EE7A.asm` | `source-helper` | `ResolveStatisticSelectorValue` |  |
| `C3:EF23` | 0x3 | `misc/null/C3EF23.asm` | `null-stub` |  |  |
| `C3:EF26` | 0x18A | `data/unknown/C3EF26.asm` | `contract-backed-data` | `BattlePsiMenuSelectorGroupTable / BATTLE_PSI_MENU_SELECTOR_GROUP_TABLE` |  |
| `C3:F0B0` | 0x13C | `data/unknown/C3F0B0.asm` | `contract-backed-data` | `BattlePsiKnownStateGateTable / BATTLE_PSI_KNOWN_STATE_GATE_TABLE` |  |
| `C3:F1EC` | 0xC5 | `unknown/C3/C3F1EC.asm` | `source-helper` | `TryRepairJeffBrokenInventoryItem` |  |
| `C3:F2B1` | 0x348 | `data/unknown/C3F2B1.asm` | `mixed-data-source-row` | `LevelUpStatGrowthVarianceTable / LEVEL_UP_STAT_GROWTH_VARIANCE_TABLE` |  |
| `C3:F5F9` | 0x84 | `unknown/C3/C3F5F9.asm` | `source-helper` | `QueueVisualTileRowsLinear` |  |
| `C3:F67D` | 0x88 | `unknown/C3/C3F67D.asm` | `source-helper` | `QueueVisualTileRowsWrapped` |  |
| `C3:F705` | 0xF6 | `unknown/C3/C3F705.asm` | `source-helper` | `QueueVisualTileBlockFromStream` |  |
| `C3:F7FB` | 0x1E | `unknown/C3/C3F7FB.asm` | `source-helper` | `QueueFixedEfEb3dVisualTileBlock` |  |
| `C3:F819` | 0x58 | `data/unknown/C3F819.asm` | `effect-script-asset` | `BattleSwirlOverlayMode2Script` | `not-applicable` |
| `C3:F871` | 0x40 | `data/unknown/C3F871.asm` | `contract-backed-data` | `BattleVisualGraphicsSourceStripOffsets / BATTLE_VISUAL_GRAPHICS_SOURCE_STRIP_OFFSETS` |  |
| `C3:F8B1` | 0x40 | `data/unknown/C3F8B1.asm` | `contract-backed-data` | `BattleVisualOamTileIndexGrid / BATTLE_VISUAL_OAM_TILE_INDEX_GRID` |  |
| `C3:F8F1` | 0x90 | `data/unknown/C3F8F1.asm` | `contract-backed-data` | `BattlePaletteSetRows / BATTLE_PALETTE_SET_ROWS` |  |
| `C3:F981` | 0x148 | `unknown/C3/C3F981.asm` | `source-helper` | `DispatchBattleVisualEffectToken` |  |
| `C3:FAC9` | 0x40 | `unknown/C3/C3FAC9.asm` | `source-helper` | `DispatchBattleActorVisualEffectToken` |  |
| `C3:FB09` | 0x16 | `unknown/C3/C3FB09.asm` | `source-helper` | `CheckCurrentBattleActorVisualFlag` |  |

## Supplemental Labels

These labels are not address-bearing include starts in the reference bankconfig. They are still important: most are internal event labels, named-source include entry points, or table sublabels needed by source comments.

| Address | Class | Source | Name / Contract | Decode |
| --- | --- | --- | --- | --- |
| `C3:0100` | `source-helper` | `working-name` | `DisplayAntiPiracyScreen` |  |
| `C3:0142` | `source-helper` | `working-name` | `DisplayFaultyGamePakScreen` |  |
| `C3:0195` | `event-bytecode-asset` | `script-payload` | `Event221PaulaFatherFarewellSequence` | `limit` |
| `C3:0235` | `event-bytecode-asset` | `script-payload` | `Event222PaulaDoorExitMovementScript` | `complete` |
| `C3:024A` | `event-bytecode-asset` | `script-payload` | `Event223PaulaPorchExitMovementScript` | `complete` |
| `C3:0260` | `event-bytecode-asset` | `script-payload` | `Event224PaulaReturnMovementScript` | `complete` |
| `C3:43E8` | `event-bytecode-asset` | `script-payload` | `TimedDeliveryDeparturePulseAnimation0Half` | `complete` |
| `C3:443E` | `event-bytecode-asset` | `script-payload` | `TimedDeliveryRetryWaitLoop` | `complete` |
| `C3:444D` | `event-bytecode-asset` | `script-payload` | `TimedDeliveryReadinessGate` | `complete` |
| `C3:4457` | `event-bytecode-asset` | `script-payload` | `TimedDeliverySuccessGateAndPresentationSetup` | `complete` |
| `C3:447A` | `event-bytecode-label` | `script-payload` | `StartTimedDeliveryArrivalMovementTask` | `complete` |
| `C3:447D` | `event-bytecode-asset` | `script-payload` | `TimedDeliveryFailureTeardown` | `complete` |
| `C3:4488` | `event-bytecode-asset` | `script-payload` | `PrepareTimedDeliveryActorForPresentation` | `complete` |
| `C3:4499` | `event-bytecode-label` | `script-payload` | `WaitTimedDeliveryActorPresentationPrep` | `complete` |
| `C3:44A7` | `event-bytecode-label` | `script-payload` | `ReturnFromTimedDeliveryActorPrep` | `complete` |
| `C3:44A8` | `event-bytecode-asset` | `script-payload` | `RunTimedDeliveryDepartureMovement` | `complete` |
| `C3:44C1` | `event-bytecode-label` | `script-payload` | `LoopTimedDeliveryDepartureMovement` | `complete` |
| `C3:44D2` | `event-bytecode-label` | `script-payload` | `FinishTimedDeliveryDepartureAndYieldText` | `complete` |
| `C3:44DE` | `event-bytecode-asset` | `script-payload` | `RunTimedDeliveryArrivalMovement` | `complete` |
| `C3:44EE` | `event-bytecode-label` | `script-payload` | `LoopTimedDeliveryArrivalMovement` | `complete` |
| `C3:44FF` | `event-bytecode-label` | `script-payload` | `HoldTimedDeliveryArrivalCompletion` | `complete` |
| `C3:A043` | `event-bytecode-asset` | `script-payload` | `IntroCutsceneCameraPanGate` | `complete` |
| `C3:A04E` | `event-bytecode-label` | `script-payload` | `StartIntroCameraPanTickLoop` | `complete` |
| `C3:A052` | `event-bytecode-label` | `script-payload` | `LoopIntroCameraPanWaitAndC2Step` | `complete` |
| `C3:A05E` | `event-bytecode-asset` | `script-payload` | `IntroCutsceneSpriteObjectSetup` | `complete` |
| `C3:A076` | `event-bytecode-label` | `script-payload` | `LoopIntroCompanionVisualRefresh` | `complete` |
| `C3:A0EB` | `event-bytecode-label` | `script-payload` | `LoopActiveEntityWalkPulse6FrameConditional` | `complete` |
| `C3:A0FE` | `event-bytecode-label` | `script-payload` | `LoopActiveEntityWalkPulse2FrameConditional` | `complete` |
| `C3:A111` | `event-bytecode-label` | `script-payload` | `LoopActiveEntityWalkPulseVar4Gate` | `complete` |
| `C3:A204` | `event-bytecode-asset` | `script-payload` | `ReleaseCurrentVisualEntityAndEnd` | `complete` |
| `C3:A22C` | `event-bytecode-asset` | `script-payload` | `Var0AnimationCase0Pulse8FrameOn` | `complete` |
| `C3:A234` | `event-bytecode-asset` | `script-payload` | `Var0AnimationCase1Pulse8FrameOff` | `complete` |
| `C3:A23D` | `event-bytecode-asset` | `script-payload` | `Var0AnimationCase2Pulse4Frame` | `complete` |
| `C3:A24E` | `event-bytecode-asset` | `script-payload` | `Var0AnimationCase3Pulse32Frame` | `complete` |
| `C3:A25F` | `event-bytecode-asset` | `script-payload` | `Var0AnimationCase4Wait16Frame` | `complete` |
| `C3:A2AA` | `event-bytecode-asset` | `script-payload` | `TrafficLightWaitUntilOffscreenAndRelease` | `complete` |
| `C3:A381` | `event-bytecode-asset` | `script-payload` | `InitRandomWanderMovementWithCollisionProbe` | `complete` |
| `C3:A3A1` | `event-bytecode-asset` | `script-payload` | `InitC40015PulseWithCollisionProbe` | `complete` |
| `C3:A3B7` | `event-bytecode-label` | `script-payload` | `LoopRandomDirectionMovementWithRandomWait` | `complete` |
| `C3:A3C9` | `event-bytecode-asset` | `script-payload` | `ChooseRandomCardinalDirection` | `complete` |
| `C3:A3D6` | `event-bytecode-asset` | `script-payload` | `ApplyRandomDirectionAndMovementTimer` | `complete` |
| `C3:A3E7` | `event-bytecode-asset` | `script-payload` | `SetMovementTimerThenRandomWait` | `complete` |
| `C3:A426` | `event-bytecode-label` | `script-payload` | `StartNpcAttentionTerrainCollisionLoop` | `complete` |
| `C3:A42D` | `event-bytecode-label` | `script-payload` | `StartNpcAttentionHorizontalCollisionLoop` | `complete` |
| `C3:A434` | `event-bytecode-label` | `script-payload` | `LoopNpcAttentionTerrainCollision` | `complete` |
| `C3:A448` | `event-bytecode-label` | `script-payload` | `LoopNpcAttentionHorizontalCollision` | `complete` |
| `C3:A45C` | `event-bytecode-label` | `script-payload` | `FinishNpcAttentionAndReleaseActor` | `complete` |
| `C3:A47C` | `event-bytecode-asset` | `script-payload` | `ReleaseCurrentVisualEntityTail` | `complete` |
| `C3:E12C` | `contract-backed-data` | `data-contract` | `InputDirectionPermissionMaskTable` |  |
| `C3:E406` | `contract-backed-data` | `data-contract` | `AnimatedMenuCursorPointRightTiles` |  |
| `C3:E416` | `contract-backed-data` | `data-contract` | `BlinkingTriangleBaseTiles` |  |
| `C3:E424` | `source-adjacent-data` | `working-name` | `BlinkingTriangleWaitFrame1Tiles` |  |
| `C3:E42C` | `source-adjacent-data` | `working-name` | `BlinkingTriangleWaitFrame2Tiles` |  |
| `C3:E434` | `source-adjacent-data` | `working-name` | `BlinkingTriangleWaitFrame3Tiles` |  |
| `C3:E43C` | `contract-backed-data` | `data-contract` | `BlinkingTriangleWaitFramePointerTable` |  |
| `C3:E4CA` | `source-helper` | `working-name` | `ClearInstantPrinting` |  |
| `C3:E4D4` | `source-helper` | `working-name` | `SetInstantPrinting` |  |
| `C3:E4E0` | `source-helper` | `working-name` | `TickWindowWithoutInstantPrinting` |  |
| `C3:E521` | `source-helper` | `working-name` | `CloseWindowAndReleaseTileState` |  |
| `C3:E773` | `source-helper` | `working-name` | `ClearFirstReflectedHitSideArticleTokenFlag` |  |
| `C3:E78F` | `source-helper` | `working-name` | `ClearSecondReflectedHitSideArticleTokenFlag` |  |
| `C3:E977` | `source-helper` | `working-name` | `ReadCharacterInventorySlotByte` |  |
| `C3:E9A0` | `source-helper` | `working-name` | `CheckEquippedInventorySlotReference` |  |
| `C3:F016` | `contract-backed-data` | `data-contract` | `BattlePsiMenuGroupSliceCountTable` |  |
| `C3:F054` | `contract-backed-data` | `data-contract` | `BattleTextControlToken50To7fMetadataTable` |  |
| `C3:F112` | `contract-backed-data` | `data-contract` | `BattlePsiRankSuffixTable` |  |
| `C3:F11C` | `contract-backed-data` | `data-contract` | `BattlePsiMenuEntryFixedTail` |  |
| `C3:F124` | `contract-backed-data` | `data-contract` | `BattlePsiMenuEntryRowTable` |  |
| `C3:F2B5` | `contract-backed-data` | `data-contract` | `VisualSelectorPoseRowTable` |  |
| `C3:F3C5` | `source-helper` | `working-name` | `RunFileSelectVisualTransition` |  |
| `C3:F879` | `source-adjacent-data` | `working-name` | `BattleVisualGraphicsSourceStripOffsetsPage1` |  |
| `C3:F881` | `source-adjacent-data` | `working-name` | `BattleVisualGraphicsSourceStripOffsetsPage2` |  |
| `C3:F889` | `source-adjacent-data` | `working-name` | `BattleVisualGraphicsSourceStripOffsetsPage3` |  |
| `C3:F891` | `source-adjacent-data` | `working-name` | `BattleVisualGraphicsSourceStripOffsetsPage4` |  |
| `C3:F899` | `source-adjacent-data` | `working-name` | `BattleVisualGraphicsSourceStripOffsetsPage5` |  |
| `C3:F8A1` | `source-adjacent-data` | `working-name` | `BattleVisualGraphicsSourceStripOffsetsPage6` |  |
| `C3:F8A9` | `source-adjacent-data` | `working-name` | `BattleVisualGraphicsSourceStripOffsetsPage7` |  |
| `C3:F8C1` | `source-adjacent-data` | `working-name` | `BattleVisualOamTileIndexGridRow1` |  |
| `C3:F8D1` | `source-adjacent-data` | `working-name` | `BattleVisualOamTileIndexGridRow2` |  |
| `C3:F8E1` | `source-adjacent-data` | `working-name` | `BattleVisualOamTileIndexGridRow3` |  |
| `C3:F911` | `source-adjacent-data` | `working-name` | `BattlePaletteSetRow1` |  |
| `C3:F931` | `source-adjacent-data` | `working-name` | `BattlePaletteSetRow2` |  |
| `C3:F951` | `contract-backed-data` | `data-contract` | `BattleVisualToken23To2dColourTriples` |  |
| `C3:F972` | `contract-backed-data` | `data-contract` | `BattleVisualToken31To35ColourTriples` |  |
| `C3:F9A2` | `source-helper` | `working-name` | `ApplyBattleVisualToken23To2dColourEffect` |  |
| `C3:FA4A` | `source-helper` | `working-name` | `ApplyBattleVisualToken31To35ColourEffect` |  |
| `C3:FAC7` | `source-helper` | `working-name` | `ReturnFromBattleVisualEffectTokenDispatch` |  |
| `C3:FB1F` | `working-label` | `working-name` | `DATA_C3FB1F` |  |
| `C3:FDBD` | `movement-pattern-data` | `script-payload` | `DeliveryPlaceholderSpriteTable` | `not-applicable` |

## Source Extraction Slices

These are the addressed rows currently classified as `source-helper`. They are the C3 rows most suitable for ordinary 65816 source extraction before deeper VM work.

| Address | Include | Working Name | Expectation |
| --- | --- | --- | --- |
| `C3:E450` | `unknown/C3/C3E450.asm` | `WindowTickTransferDynamicTileBlock` | ordinary 65816 helper candidate for source extraction |
| `C3:E4EF` | `unknown/C3/C3E4EF.asm` | `FindFirstFreeWindowSlot` | ordinary 65816 helper candidate for source extraction |
| `C3:E6F8` | `unknown/C3/C3E6F8.asm` | `ClearFocusedPartyHpPpActorAndBlankRow` | ordinary 65816 helper candidate for source extraction |
| `C3:E75D` | `unknown/C3/C3E75D.asm` | `ResolveReflectedHitSideArticleTokens` | ordinary 65816 helper candidate for source extraction |
| `C3:E7E3` | `unknown/C3/C3E7E3.asm` | `ClearWindowRegisteredCopyChain` | ordinary 65816 helper candidate for source extraction |
| `C3:E9F7` | `unknown/C3/C3E9F7.asm` | `CheckEquippedInventoryItemPresence` | ordinary 65816 helper candidate for source extraction |
| `C3:EAD0` | `unknown/C3/C3EAD0.asm` | `RefreshEggFamilyLifecycleOnInsert` | ordinary 65816 helper candidate for source extraction |
| `C3:EB1C` | `unknown/C3/C3EB1C.asm` | `RefreshEggFamilyLifecycleOnRemove` | ordinary 65816 helper candidate for source extraction |
| `C3:EBCA` | `unknown/C3/C3EBCA.asm` | `SyncPartyOverlayTrackedItemFamilyState` | ordinary 65816 helper candidate for source extraction |
| `C3:EC1F` | `unknown/C3/C3EC1F.asm` | `DepleteCharacterHp` | ordinary 65816 helper candidate for source extraction |
| `C3:EC8B` | `unknown/C3/C3EC8B.asm` | `RecoverCharacterHp` | ordinary 65816 helper candidate for source extraction |
| `C3:ED2C` | `unknown/C3/C3ED2C.asm` | `DepleteCharacterPp` | ordinary 65816 helper candidate for source extraction |
| `C3:ED98` | `unknown/C3/C3ED98.asm` | `RecoverCharacterPp` | ordinary 65816 helper candidate for source extraction |
| `C3:EE14` | `unknown/C3/C3EE14.asm` | `CheckItemEquipmentSlotCompatibility` | ordinary 65816 helper candidate for source extraction |
| `C3:EE4D` | `unknown/C3/C3EE4D.asm` | `RefreshWorldAndReleaseActiveVisualHandle` | ordinary 65816 helper candidate for source extraction |
| `C3:EE7A` | `unknown/C3/C3EE7A.asm` | `ResolveStatisticSelectorValue` | ordinary 65816 helper candidate for source extraction |
| `C3:F1EC` | `unknown/C3/C3F1EC.asm` | `TryRepairJeffBrokenInventoryItem` | ordinary 65816 helper candidate for source extraction |
| `C3:F5F9` | `unknown/C3/C3F5F9.asm` | `QueueVisualTileRowsLinear` | ordinary 65816 helper candidate for source extraction |
| `C3:F67D` | `unknown/C3/C3F67D.asm` | `QueueVisualTileRowsWrapped` | ordinary 65816 helper candidate for source extraction |
| `C3:F705` | `unknown/C3/C3F705.asm` | `QueueVisualTileBlockFromStream` | ordinary 65816 helper candidate for source extraction |
| `C3:F7FB` | `unknown/C3/C3F7FB.asm` | `QueueFixedEfEb3dVisualTileBlock` | ordinary 65816 helper candidate for source extraction |
| `C3:F981` | `unknown/C3/C3F981.asm` | `DispatchBattleVisualEffectToken` | ordinary 65816 helper candidate for source extraction |
| `C3:FAC9` | `unknown/C3/C3FAC9.asm` | `DispatchBattleActorVisualEffectToken` | ordinary 65816 helper candidate for source extraction |
| `C3:FB09` | `unknown/C3/C3FB09.asm` | `CheckCurrentBattleActorVisualFlag` | ordinary 65816 helper candidate for source extraction |

## Mixed Data Rows

These addressed data includes contain embedded source-helper or event/actionscript labels. Split their leading data/prefix bytes before emitting ordinary source or script assets.

| Address | Include | Embedded Labels | Split Expectation |
| --- | --- | --- | --- |
| `C3:0188` | `data/unknown/C30188.asm` | C3:0195 Event221PaulaFatherFarewellSequence<br>C3:0235 Event222PaulaDoorExitMovementScript<br>C3:024A Event223PaulaPorchExitMovementScript<br>C3:0260 Event224PaulaReturnMovementScript | mixed row: split leading data/prefix bytes from embedded event/actionscript labels C3:0195 Event221PaulaFatherFarewellSequence, C3:0235 Event222PaulaDoorExitMovementScript, C3:024A Event223PaulaPorchExitMovementScript, C3:0260 Event224PaulaReturnMovementScript |
| `C3:E84E` | `data/unknown/C3E84E.asm` | C3:E977 ReadCharacterInventorySlotByte<br>C3:E9A0 CheckEquippedInventorySlotReference | mixed row: split leading data from embedded source-helper labels C3:E977 ReadCharacterInventorySlotByte, C3:E9A0 CheckEquippedInventorySlotReference |
| `C3:F2B1` | `data/unknown/C3F2B1.asm` | C3:F3C5 RunFileSelectVisualTransition | mixed row: split leading data from embedded source-helper labels C3:F3C5 RunFileSelectVisualTransition |

## Follow-up Frontier

Rows below are documented enough to split, but are intentionally not promoted to normal source helpers yet.

| Address | Include | Class | Reason |
| --- | --- | --- | --- |
| _none_ |  |  |  |
