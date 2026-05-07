# Frontier Scout (2026-04-26): Next High-Leverage Source-Promotion Targets

Scope: identify **preserved** (byte-corridor / protected data-gap) corridors with strong local corroboration (ebsrc include maps, legacy labels, and local notes/contracts) that should be fast to promote into real decoded source or typed assets **before** doing any implementation work. This note does **not** change `src/*` or `build/*`.

Primary inputs read for this scout:

- bank scaffold handoffs: `notes/bank-c1-source-scaffold-handoff.md`, `notes/bank-c2-source-scaffold-handoff.md`, `notes/bank-c4-source-scaffold-handoff.md`
- build-candidate range docs: `notes/c0-build-candidate-ranges.md`, `notes/c2-build-candidate-ranges.md`, `notes/c4-build-candidate-ranges.md`
- ref index: `build/ref-index.json` (plus generated frontier notes like `notes/bank-c3-reference-frontier.md`, `notes/bank-c4-reference-frontier.md`)
- legacy disasm: `refs/earthbound-disasm-legacy/Earthbound Decomp/EB/Routine_Macros_EB.asm`
- ebsrc mapping: `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank03.asm`, `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank04.asm`
- Yoshifanatic-derived handoff context: `notes/yoshifanatic1-c0-c4-handoff-readme.md`, `notes/yoshifanatic1-c0-c4-evidence-snippets.md`
- eb-decompile table corpus: `refs/eb-decompile-4ef92/*` (table-centric; not address-bearing in `ref-index.json`)

## Pick list (highest leverage first)

### 1) C0 ActionScript interpreter + small opcode leaves (dispatcher anchor)

This is the cleanest "promote-first" dispatcher corridor: a bytecode reader, an opcode jump table, and a run of tiny op leaves/wrappers whose behavior and parameter layout are already described in local notes.

Targets (exact protected ranges from `build/c0-build-candidate-ranges.json` / `notes/c0-build-candidate-ranges.md`):

- `C0:9506..C0:9558` `Run_ActionScriptFrame` (`src/c0/c0_9506_run_action_script_frame.asm`)
  - Evidence: `notes/actionscript-dispatch-task-frontier-c08fc2-c09ece.md` (opcode dispatch description + state layout)
- `C0:9558..C0:9ABD` `ScriptOpcodePointerTable` (`src/c0/c0_9558_script_opcode_pointer_table.asm`)
  - Evidence: `notes/actionscript-dispatch-task-frontier-c08fc2-c09ece.md` (calls out `C0:9558` table)
- `C0:9ABD..C0:9AC5` `ScriptOpTargetMutationTable` (`src/c0/c0_9abd_script_op_target_mutation_table.asm`)
- `C0:9AC5..C0:9ACC` `ScriptOp_MutateTarget_AND` (`src/c0/c0_9ac5_script_op_mutate_target_and.asm`)
- `C0:9ACC..C0:9AD3` `ScriptOp_MutateTarget_OR` (`src/c0/c0_9acc_script_op_mutate_target_or.asm`)
- `C0:9AD3..C0:9ADB` `ScriptOp_MutateTarget_ADD` (`src/c0/c0_9ad3_script_op_mutate_target_add.asm`)
- `C0:9ADB..C0:9AF9` `ScriptOp_MutateTarget_EOR` (`src/c0/c0_9adb_script_op_mutate_target_eor.asm`)
- `C0:9AF9..C0:9B09` `EntityScriptVarTablePointers` (`src/c0/c0_9af9_entity_script_var_table_pointers.asm`)
- `C0:9B09..C0:9B0F` `ScriptOp_InitCurrentTaskRecordDefaults` (`src/c0/c0_9b09_script_op_init_current_task_record_defaults.asm`)

Suggested source segments:

- keep the dispatcher + table as a single "interpreter core" segment (`C0:9506..C0:9ABD`) for first promotion (one calling convention, shared state arrays)
- keep the mutate-table + 4 tiny leaves as one segment (`C0:9ABD..C0:9AF9`) once control-flow is rewritten as structured ops

Likely force-width caveats:

- opcode fetch (`[$80],Y`) and table indexing wants **8-bit A** for opcode bytes but **16-bit** for pointer math and slot indices; confirm/standardize entry/exit `M/X` state (prefer `REP #$31` on entry, local `SEP #$20` only around byte reads)
- preserve `Y` as "script PC" across helper calls; any `PHY/PLY` mismatches will be silent but catastrophic

### 2) C0 ActionScript wrapper strip `C0:A841..C0:AAFD` (repeated idioms)

These are repeatable "read N words/bytes then delegate to C4" stubs, already documented with parameter layouts and targets. They should be fast to lift as typed op wrappers without needing the deeper C4 helper fully named first.

Targets:

- `C0:A841..C0:A84C` `Script_PlaySoundEffectParameter` (`src/c0/c0_a841_script_play_sound_effect_parameter.asm`)
- `C0:A88D..C0:A8A0` `ScriptWrapper_C46E4F_ReadWordByte` (`src/c0/c0_a88d_script_wrapper_c46_e4_f_read_word_byte.asm`)
- `C0:A977..C0:A98B` `Movement_LoadBattleBg` (`src/c0/c0_a977_movement_load_battle_bg.asm`)
- `C0:AA3F..C0:AA6E` `Script_SetVisualSetupBytesByMode` (`src/c0/c0_aa3f_script_set_visual_setup_bytes_by_mode.asm`)
- `C0:AAD5..C0:AAFD` `Script_CountdownThenJumpTarget` (`src/c0/c0_aad5_script_countdown_then_jump_target.asm`)

Evidence:

- `notes/actionscript-wrapper-strip-c0a841-c0aafd.md` (parameter layouts + called C4 helpers)
- `notes/actionscript-dispatch-task-frontier-c08fc2-c09ece.md` (ties wrappers back into interpreter ABI)

Likely force-width caveats:

- wrappers often interleave `byte, word, word` payloads; be explicit about which reads are `A8` vs `A16`
- keep "script stream pointer" and "current slot" convention consistent with the interpreter (`[$80],Y` reader; slot-indexed WRAM arrays)

### 3) C2 HP/PP window + menu selection helpers (tight, reference-correlated code)

These are small, well-bounded helpers with strong local note coverage and both ebsrc + legacy label corroboration (per `build/ref-index.json`).

Targets (each is currently preserved-bytes in the C2 scaffold; promote into decoded source modules next):

- `C2:038B..C2:03C3` `ResetHpPpTilemapBuffers` (`src/c2/c2_038b_reset_hp_pp_tilemap_buffers.asm`)
- `C2:077D..C2:07B6` `RedrawDirtyPartyHpPpWindows` (`src/c2/c2_077d_redraw_dirty_party_hp_pp_windows.asm`)
- `C2:07B6..C2:07E1` `MarkAndRedrawPartyHpPpWindow` (`src/c2/c2_07b6_mark_and_redraw_party_hp_pp_window.asm`)
- `C2:087C..C2:08B8` `RefreshDirtyHpPpAndOpenTextWindows` (`src/c2/c2_087c_refresh_dirty_hp_pp_and_open_text_windows.asm`)
- `C2:08B8..C2:0958` `ClassifyMenuTileForCursorScan` (`src/c2/c2_08b8_classify_menu_tile_for_cursor_scan.asm`)
- `C2:0B65..C2:0D3F` `FindNextSelectableMenuCell` (`src/c2/c2_0b65_find_next_selectable_menu_cell.asm`)

Evidence:

- `notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md` (working names + context)

Likely force-width caveats:

- tilemap values / masks are byte-granular; cursor scan often wants **A8** for classification/masks but **XY16** for index math
- HP/PP window refresh paths often have "call with M/X fixed" expectations; treat entry/exit flags as part of the ABI

### 4) C2 managed text/timed-event snapshot + restore (clean state ABI)

These are compact state marshaling helpers, ideal to promote early because they define a stable cross-subsystem ABI.

- `C2:0A20..C2:0ABC` `SnapshotManagedTextEventSlotState` (`src/c2/c2_0a20_snapshot_managed_text_event_slot_state.asm`)
- `C2:0ABC..C2:0B65` `RestoreManagedTextEventSlotState` (`src/c2/c2_0abc_restore_managed_text_event_slot_state.asm`)

Evidence:

- `notes/timed-event-slot-block-7440-and-c20abc.md` (working names + slot structure)

Likely force-width caveats:

- routines often copy mixed byte/word fields; lock `M/X` at entry and do explicit `SEP/REP` only at field boundaries to avoid mis-sized stores

### 5) C2 battle background load + palette effect corridor (big win, well-noted)

The `C2:CFE5..C2:E0E7` corridor is large but already consolidated into a few named entry points, with a dedicated note describing the subsystem slice. This should pay off quickly because it's heavily reused and has visible behavior.

- `C2:CFE5..C2:D0AC` `InitLoadedBattleBgLayerFromConfig` (`src/c2/c2_cfe5_init_loaded_battle_bg_layer_from_config.asm`)
- `C2:D0AC..C2:DAE3` `BuildBattleLetterboxHdmaTable` (`src/c2/c2_d0ac_build_battle_letterbox_hdma_table.asm`)
- `C2:DAE3..C2:DE0F` `PrimeLayer1BattleBgDistortionSwap` (`src/c2/c2_dae3_prime_layer1_battle_bg_distortion_swap.asm`)
- `C2:DE96..C2:DF2E` `RestoreLoadedBattleBgPalettesAndUpload` (`src/c2/c2_de96_restore_loaded_battle_bg_palettes_and_upload.asm`)
- `C2:DF2E..C2:E08E` `ApplyLoadedBattleBgPaletteStep` (`src/c2/c2_df2e_apply_loaded_battle_bg_palette_step.asm`)
- `C2:E08E..C2:E0E7` `ApplyLoadedBattleBgPaletteStepAcrossLayers` (`src/c2/c2_e08e_apply_loaded_battle_bg_palette_step_across_layers.asm`)

Evidence:

- `notes/c2-battlebg-load-and-palette-effect-corridor-c2cfe5-c2e0e7.md`

Likely force-width caveats:

- HDMA tables + PPU register staging is byte-oriented; keep "register writes" clearly separated from 16-bit pointer math
- shared scratch across entry points: treat any DP scratch as part of the calling convention until proven otherwise

### 6) C4 event script pointer table + payload islands (preserved data, strong reference structure)

These are preserved data gaps with unusually strong external structure (ebsrc script pointer tables + event fragments). They're good candidates to promote into typed script assets without touching engine code first.

- `C4:00D4..C4:0B51` `EventScriptPointerTable` (`src/c4/event_script_pointer_table.asm`)
  - Evidence: `refs/ebsrc-main/ebsrc-main/src/data/events/script_pointers.asm`, `notes/ebsrc-bank-c4-map.md`
- `C4:0BD4..C4:1DB6` `EarlyEventOverlayDataPayloads` (`src/c4/early_event_overlay_data_payloads.asm`)
- `C4:2172..C4:23DC` `EventScriptPayloads2172To23dc` (`src/c4/event_script_payloads_2172_23dc.asm`)
  - Evidence: `refs/ebsrc-main/ebsrc-main/src/data/events/scripts/787.asm`, `refs/ebsrc-main/ebsrc-main/src/data/events/scripts/860.asm`
- `C4:279F..C4:283F` `EventScriptPayloads279fTo283f` (`src/c4/event_script_payloads_279f_283f.asm`)
  - Evidence: `refs/ebsrc-main/ebsrc-main/src/data/events/scripts/859.asm`

Suggested source segments:

- first promote the pointer table into a typed "script id -> pointer" manifest (even if payload decode stays raw)
- then promote each payload island as a script asset bundle keyed by the pointer table entries that land in that island

### 7) C4 entity footprint + visual profile tables (typed table win)

The `C4:2A1F..C4:30EC` block is preserved as a single data corridor but has enough corroboration to split into typed tables incrementally.

- `C4:2A1F..C4:30EC` `EntityFootprintVisualProfileTables` (`src/c4/entity_footprint_visual_profile_tables.asm`)
  - Evidence: `notes/ebsrc-bank-c4-map.md`, plus legacy data labels (e.g. `DATA_C42A1F` in `refs/earthbound-disasm-legacy/.../Routine_Macros_EB.asm`)

Suggested source segments:

- promote each table start already implied by legacy labels (`DATA_C42A1F`, `DATA_C42A41`, `DATA_C42A63`, ...) as separate typed arrays
- annotate row stride + meaning only when consumer callsites in C0/C4 prove it (avoid premature semantics)

## Notes on reference availability

- The ebsrc include maps (`refs/ebsrc-main/.../bank03.asm`, `bank04.asm`) are present and referenced throughout `build/ref-index.json`, but a number of per-address include files referenced by those maps are **not** present in this local snapshot (e.g. `unknown/C3/C3E4EF.asm`, `unknown/C4/C47501.asm`). This scout therefore treats ebsrc's bankconfig include *rows* as corroboration even when the included leaf file is missing locally.

### 8) C1 file-select submenu bodies (`C1:F07E..FF2C`) (fast wins, already well modeled)

These are still **data-only protected spans** in the C1 scaffold, but they have unusually strong local behavioral notes and clean call boundaries. They should be quick to promote into decoded source (and then stable symbol contracts) with minimal cross-bank dependency.

Targets (protected spans; current `notes/c1-build-candidate-ranges.md` classification is “data-only protected span”):

- `C1:F07E..C1:F14F` `OpenFileSelectActionMenu` (`src/c1/c1_f07e_open_file_select_action_menu.asm`)
  - Evidence: `notes/file-select-action-copy-delete-menus-c1f07e-f14f-f2a8.md`, `notes/bank-c1-subsystem-and-symbol-synthesis.md`
- `C1:F14F..C1:F2A8` `OpenCopyDestinationMenu` (`src/c1/c1_f14f_open_copy_destination_menu.asm`)
  - Evidence: `notes/file-select-action-copy-delete-menus-c1f07e-f14f-f2a8.md`, `notes/bank-c1-subsystem-and-symbol-synthesis.md`
- `C1:F2A8..C1:F497` `OpenDeleteFileConfirmationMenu` (`src/c1/c1_f2a8_open_delete_file_confirmation_menu.asm`)
  - Evidence: `notes/file-select-action-copy-delete-menus-c1f07e-f14f-f2a8.md`, `notes/bank-c1-subsystem-and-symbol-synthesis.md`
- `C1:F497..C1:F616` `OpenOrRefreshTextSpeedSelection` (`src/c1/c1_f497_open_or_refresh_text_speed_selection.asm`)
  - Evidence: `notes/file-select-setup-option-menus-c1f497-c1f616.md`, `notes/bank-c1-subsystem-and-symbol-synthesis.md`
- `C1:F616..C1:FF2C` `OpenOrRefreshSoundSettingSelection` (`src/c1/c1_f616_open_or_refresh_sound_setting_selection.asm`)
  - Evidence: `notes/file-select-setup-option-menus-c1f497-c1f616.md`, `notes/bank-c1-subsystem-and-symbol-synthesis.md`

Suggested source segments:

- Promote the “action menu triad” as one contiguous semantic slice (`C1:F07E..C1:F497`), since the three bodies share the same menu builder/selection skeleton and the EF save-slot tail calls.
- Promote the “setup menu dual” as one contiguous semantic slice (`C1:F497..C1:FF2C`) since both wrappers are structurally identical except for the state byte and menu builder target.

Likely force-width caveats:

- Both setup wrappers are explicitly dual-mode (`A==0` run selection vs `A!=0` refresh-only); keep call ABI (argument register + expected `M/X`) stable across both branches.
- Menu-render loops tend to be mixed-width (byte state like `$98B6/$98B7` and window id bytes vs 16-bit pointer/stride math); avoid relying on implicit `SEP/REP` state inherited from callers.

### 9) EF save-slot helpers called by C1 file-select (`EF:0A4D`, `EF:0BFA`, `EF:0C15`) (best anchors to split EF first)

Bank EF is currently an asset-style coarse scaffold (`EF:0000..EF:EB5F` is one preserved corridor), so the highest-leverage source-promotion move is to carve out the small save-slot helpers that C1 already calls with stable semantics.

Targets (entry points are strongly corroborated by local C1 notes + legacy disasm labels):

- `EF:0A4D` `label_EF0A4D` (called from C1 setup menu wrappers when a committed selection updates save-file setup state)
  - Evidence: `notes/file-select-setup-option-menus-c1f497-c1f616.md`, `refs/earthbound-disasm-legacy/Earthbound Decomp/EB/Routine_Macros_EB.asm` (label + code), `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank2f.asm` (save/system include context; local leaf files missing)
  - Proposed label (provisional, keep file-select context): `CommitFileSelectSetupStateToSaveSlot`
- `EF:0BFA` `label_EF0BFA` (delete-file operation for the selected slot)
  - Evidence: `notes/file-select-action-copy-delete-menus-c1f07e-f14f-f2a8.md`, `refs/earthbound-disasm-legacy/Earthbound Decomp/EB/Routine_Macros_EB.asm` (label + code), `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank2f.asm`
  - Proposed label: `EraseSaveSlot`
- `EF:0C15` `label_EF0C15` (copy-file operation: `(currentSlot-1, destSlot-1)` from C1)
  - Evidence: `notes/file-select-action-copy-delete-menus-c1f07e-f14f-f2a8.md`, `refs/earthbound-disasm-legacy/Earthbound Decomp/EB/Routine_Macros_EB.asm` (label + code), `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank2f.asm`
  - Proposed label: `CopySaveSlot`

Suggested source segments:

- First split EF into a “save helpers strip” around `EF:0A4D..EF:0C15` (and the immediately-adjacent helper calls they trampoline into), so C1’s file-select contracts no longer depend on the monolithic `EF:0000..EF:EB5F` preserved span.

Likely force-width caveats:

- Each entry point begins with `REP #$31` + a small DP stack frame and then does `ASL`-based slot math; keep `A` as the slot index and avoid accidental `SEP` before the `ASL/TAX/TAY` setup.
- The helpers trampoline into other EF-local routines (e.g. `label_EF088F`, `label_EF05A9`, `label_EF06A2`); treat those as part of the “first split” set to avoid splitting only the thunk while leaving the real worker buried.
