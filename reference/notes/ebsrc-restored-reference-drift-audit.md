# ebsrc Restored Reference Drift Audit

Status: restored `refs/ebsrc-main` was rechecked against the current local semantic/source state.

## Summary

- banks audited: `['C0', 'C1', 'C2', 'C3', 'C4', 'EF']`
- restored ebsrc unknown entries: `1062`
- ebsrc unknown entries superseded by local source classification/name: `1062`
- locally covered ebsrc unknowns with possible name-polish follow-up: `0`
- reference review candidates: `0`
- semantic posture: `local source classifications, source names, and semantic manifests are ahead of restored ebsrc UNKNOWN coverage for audited priority banks`

## Interpretation

- Restored ebsrc is again a strong reference for include order, constants, labels, and historical naming.
- For audited priority banks, local readable-source closure and generated semantic contracts remain the source of truth.
- Do not bulk-import ebsrc UNKNOWN names; keep local semantic labels when they are more descriptive and byte-equivalent.
- Use ebsrc semantic names as corroboration only after exact-address and role-compatibility checks.

## Bank Summary

| Bank | ebsrc includes | ebsrc unknowns | Local supersedes unknown | Name polish | Review candidates | ebsrc semantic corroboration |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `C0` | 666 | 387 | 387 | 0 | 0 | 157 |
| `C1` | 427 | 145 | 145 | 0 | 0 | 253 |
| `C2` | 406 | 86 | 86 | 0 | 0 | 165 |
| `C3` | 1087 | 58 | 58 | 0 | 0 | 174 |
| `C4` | 566 | 325 | 325 | 0 | 0 | 104 |
| `EF` | 164 | 61 | 61 | 0 | 0 | 33 |

## Bank C0

- status counts: `{'ebsrc_semantic_name_corroborates_local_source': 157, 'ebsrc_semantic_unaddressed_reference': 68, 'local_source_classification_supersedes_ebsrc_unknown': 387, 'local_source_covers_reference_entry': 38, 'reference_support_entry': 16}`
- ebsrc map summary: `{'includes': 666, 'exact_spans': 570, 'promoted_exact_spans': 568, 'promotion_candidates': 2, 'open_entries': 80, 'latest_promoted_end': 'C0:F41E'}`

### Best Local-Supersedes-ebsrc Examples

| Start | ebsrc include | Local semantic name | Status | Action |
| --- | --- | --- | --- | --- |
| `C0:0E16` | `unknown/C0/C00E16.asm` | `Upload_VerticalMovementMapStrip` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `C0:0FCB` | `unknown/C0/C00FCB.asm` | `Upload_HorizontalMovementMapStrip` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `C0:1181` | `unknown/C0/C01181.asm` | `Upload_AuxiliaryMovementMapStrip` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `C0:122A` | `unknown/C0/C0122A.asm` | `upload_auxiliary_movement_map_strip` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `C0:1731` | `unknown/C0/C01731.asm` | `update_runtime_scroll_shadows_and_incremental_refresh` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `C0:17EA` | `unknown/C0/C017EA.asm` | `AccumulateOverworldCameraStep` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `C0:19E2` | `unknown/C0/C019E2.asm` | `Refresh_MapStripsAroundCamera` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `C0:1A63` | `unknown/C0/C01A63.asm` | `Refresh_MapStripVia0E16_FarWrapper` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| ... | ... | ... | ... | 12 more |

### Name-Polish Candidates

| Start | ebsrc include | Local semantic name | Status | Action |
| --- | --- | --- | --- | --- |

### Review Candidates

| Start | ebsrc include | Local semantic name | Status | Action |
| --- | --- | --- | --- | --- |

## Bank C1

- status counts: `{'ebsrc_semantic_name_corroborates_local_source': 253, 'ebsrc_semantic_unaddressed_reference': 11, 'local_source_classification_supersedes_ebsrc_unknown': 145, 'local_source_covers_reference_entry': 6, 'reference_support_entry': 12}`
- ebsrc map summary: `{'includes': 427, 'exact_spans': 399, 'promoted_exact_spans': 399, 'promotion_candidates': 0, 'open_entries': 16, 'latest_promoted_end': 'C1:FFEF'}`

### Best Local-Supersedes-ebsrc Examples

| Start | ebsrc include | Local semantic name | Status | Action |
| --- | --- | --- | --- | --- |
| `C1:0000` | `unknown/C1/C10000.asm` | `RunTextDisplaySetupWrapper` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `C1:0004` | `unknown/C1/C10004.asm` | `ProcessTextboxDataFromCallerPointer` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `C1:004E` | `unknown/C1/C1004E.asm` | `PumpTextWaitFrame` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `C1:008E` | `unknown/C1/C1008E.asm` | `CloseAndDrainAllWindows` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `C1:00D6` | `unknown/C1/C100D6.asm` | `WaitTextTicks` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `C1:00FE` | `unknown/C1/C100FE.asm` | `WaitForTextPromptOrInputGate` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `C1:02D0` | `unknown/C1/C102D0.asm` | `WaitForTextStateFlag9641` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `C1:078D` | `unknown/C1/C1078D.asm` | `InitializeTextWindowTilemapStaging` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| ... | ... | ... | ... | 12 more |

### Name-Polish Candidates

| Start | ebsrc include | Local semantic name | Status | Action |
| --- | --- | --- | --- | --- |

### Review Candidates

| Start | ebsrc include | Local semantic name | Status | Action |
| --- | --- | --- | --- | --- |

## Bank C2

- status counts: `{'ebsrc_semantic_name_corroborates_local_source': 165, 'ebsrc_semantic_unaddressed_reference': 101, 'local_source_classification_supersedes_ebsrc_unknown': 86, 'local_source_covers_reference_entry': 39, 'reference_support_entry': 15}`
- ebsrc map summary: `{'includes': 406, 'exact_spans': 288, 'promoted_exact_spans': 288, 'promotion_candidates': 0, 'open_entries': 103, 'latest_promoted_end': 'C2:FFB7'}`

### Best Local-Supersedes-ebsrc Examples

| Start | ebsrc include | Local semantic name | Status | Action |
| --- | --- | --- | --- | --- |
| `C2:00B9` | `data/unknown/C200B9.asm` | `EnemySunstrokeCheckTailTable` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `C2:00D9` | `unknown/C2/C200D9.asm` | `window_reset_initial_coordinate_data` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `C2:0266` | `unknown/C2/C20266.asm` | `LoadDefaultTitleUploadTiles` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `C2:0293` | `unknown/C2/C20293.asm` | `ClearDefaultTitleUploadTiles` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `C2:02AC` | `unknown/C2/C202AC.asm` | `RegisterAndUploadWindowTitleBuffer` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `C2:038B` | `unknown/C2/C2038B.asm` | `ResetHpPpTilemapBuffers` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `C2:077D` | `unknown/C2/C2077D.asm` | `RedrawDirtyPartyHpPpWindows` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `C2:07B6` | `unknown/C2/C207B6.asm` | `MarkAndRedrawPartyHpPpWindow` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| ... | ... | ... | ... | 12 more |

### Name-Polish Candidates

| Start | ebsrc include | Local semantic name | Status | Action |
| --- | --- | --- | --- | --- |

### Review Candidates

| Start | ebsrc include | Local semantic name | Status | Action |
| --- | --- | --- | --- | --- |

## Bank C3

- status counts: `{'ebsrc_semantic_name_corroborates_local_source': 174, 'ebsrc_semantic_unaddressed_reference': 14, 'local_source_classification_supersedes_ebsrc_unknown': 58, 'local_source_covers_reference_entry': 827, 'reference_support_entry': 14}`
- ebsrc map summary: `{'includes': 1087, 'exact_spans': 1058, 'promoted_exact_spans': 1058, 'promotion_candidates': 0, 'open_entries': 15, 'latest_promoted_end': 'C3:FDBD'}`

### Best Local-Supersedes-ebsrc Examples

| Start | ebsrc include | Local semantic name | Status | Action |
| --- | --- | --- | --- | --- |
| `C3:0188` | `data/unknown/C30188.asm` | `C30188RawData` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `C3:9FF2` | `data/unknown/C39FF2.asm` | `IntroMovementPatternPointerTable` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `C3:A010` | `data/unknown/C3A010.asm` | `IntroMovementPattern09Loop` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `C3:A01B` | `data/unknown/C3A01B.asm` | `IntroMovementPattern08Loop` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `C3:A026` | `data/unknown/C3A026.asm` | `IntroMovementPatternFFLoop` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `C3:A02D` | `data/unknown/C3A02D.asm` | `IntroMovementPattern08LoopAlt` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `C3:A038` | `data/unknown/C3A038.asm` | `IntroMovementPattern04Loop` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `C3:DFE8` | `data/unknown/C3DFE8.asm` | `C3DFE8RawData` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| ... | ... | ... | ... | 12 more |

### Name-Polish Candidates

| Start | ebsrc include | Local semantic name | Status | Action |
| --- | --- | --- | --- | --- |

### Review Candidates

| Start | ebsrc include | Local semantic name | Status | Action |
| --- | --- | --- | --- | --- |

## Bank C4

- status counts: `{'ebsrc_semantic_name_corroborates_local_source': 104, 'ebsrc_semantic_unaddressed_reference': 53, 'local_source_classification_supersedes_ebsrc_unknown': 325, 'local_source_covers_reference_entry': 67, 'reference_support_entry': 17}`
- ebsrc map summary: `{'includes': 566, 'exact_spans': 485, 'promoted_exact_spans': 485, 'promotion_candidates': 0, 'open_entries': 64, 'latest_promoted_end': 'C4:FD4B'}`

### Best Local-Supersedes-ebsrc Examples

| Start | ebsrc include | Local semantic name | Status | Action |
| --- | --- | --- | --- | --- |
| `C4:0000` | `unknown/C4/C40000.asm` | `WriteAtoInidisp` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `C4:0009` | `unknown/C4/C40009.asm` | `RestoreInidispFromDisplayShadow` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `C4:0015` | `unknown/C4/C40015.asm` | `ClearCurrentSlot10f2RefreshVisualAndCheckLiveArea` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `C4:0023` | `unknown/C4/C40023.asm` | `StoreLowNibble1a42ToCurrentScriptField1372` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `C4:002F` | `unknown/C4/C4002F.asm` | `SubmitTwoTextTileStripTransfers` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `C4:0085` | `unknown/C4/C40085.asm` | `ClaimTextTileBitsetSlot` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `C4:0B51` | `unknown/C4/C40B51.asm` | `SetupSystemErrorScreenDisplay` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `C4:0B75` | `unknown/C4/C40B75.asm` | `RenderSystemErrorScreenAndHalt` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| ... | ... | ... | ... | 12 more |

### Name-Polish Candidates

| Start | ebsrc include | Local semantic name | Status | Action |
| --- | --- | --- | --- | --- |

### Review Candidates

| Start | ebsrc include | Local semantic name | Status | Action |
| --- | --- | --- | --- | --- |

## Bank EF

- status counts: `{'ebsrc_semantic_name_corroborates_local_source': 33, 'ebsrc_semantic_unaddressed_reference': 49, 'local_source_classification_supersedes_ebsrc_unknown': 61, 'local_source_covers_reference_entry': 6, 'reference_support_entry': 15}`
- ebsrc map summary: `{'includes': 164, 'exact_spans': 94, 'promoted_exact_spans': 94, 'promotion_candidates': 0, 'open_entries': 55, 'latest_promoted_end': 'EF:F5BD'}`

### Best Local-Supersedes-ebsrc Examples

| Start | ebsrc include | Local semantic name | Status | Action |
| --- | --- | --- | --- | --- |
| `EF:00BB` | `unknown/EF/EF00BB.asm` | `BattleOverworldVisualHelpers` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `EF:00E6` | `unknown/EF/EF00E6.asm` | `0256_battle_overworld_visual_helpers` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `EF:0115` | `unknown/EF/EF0115.asm` | `0256_battle_overworld_visual_helpers` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `EF:016F` | `unknown/EF/EF016F.asm` | `0256_battle_overworld_visual_helpers` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `EF:01D2` | `unknown/EF/EF01D2.asm` | `0256_battle_overworld_visual_helpers` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `EF:0262` | `unknown/EF/EF0262.asm` | `027d_audio_pause_resume_flags` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `EF:027D` | `unknown/EF/EF027D.asm` | `OverworldEntitySnapshotHelpers` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| `EF:02C4` | `unknown/EF/EF02C4.asm` | `0591_overworld_entity_snapshot_helpers` | `local_source_classification_supersedes_ebsrc_unknown` | keep local source classification/name; use ebsrc address/path only as corroboration |
| ... | ... | ... | ... | 12 more |

### Name-Polish Candidates

| Start | ebsrc include | Local semantic name | Status | Action |
| --- | --- | --- | --- | --- |

### Review Candidates

| Start | ebsrc include | Local semantic name | Status | Action |
| --- | --- | --- | --- | --- |
