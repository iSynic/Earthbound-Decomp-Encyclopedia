# ebsrc Bank C1 Reference Map

Generated from ebsrc bankconfig include order, ebsrc bank symbols, and local source-bank build-candidate spans.

## Summary

- includes: `427`
- exact spans: `399`
- promoted exact spans: `399`
- promotion candidates: `0`
- open/unresolved entries: `16`
- latest promoted end: `C1:FFEF`

## Current Open Frontier

| Start | End | Size | Status | Include | ebsrc Symbol | Local Name | Kind |
| --- | --- | ---: | --- | --- | --- | --- | --- |

## Current Exact Frontier Candidates

| Start | End | Size | Include | ebsrc Symbol | Local Name | Kind |
| --- | --- | ---: | --- | --- | --- | --- |

## Candidate Backlog

| Start | End | Size | Include | ebsrc Symbol | Local Name | Kind |
| --- | --- | ---: | --- | --- | --- | --- |

## Include Map

| # | Start | End | Size | Status | Promoted | Include | ebsrc Symbol | Local Name |
| ---: | --- | --- | ---: | --- | --- | --- | --- | --- |
| 0 |  |  | 0 | `support` |  | `common.asm` | `` | `` |
| 1 |  |  | 0 | `support` |  | `config.asm` | `` | `` |
| 2 |  |  | 0 | `support` |  | `structs.asm` | `` | `` |
| 3 |  |  | 0 | `support` |  | `symbols/bank00.inc.asm` | `` | `` |
| 4 |  |  | 0 | `support` |  | `symbols/bank01.inc.asm` | `` | `` |
| 5 |  |  | 0 | `support` |  | `symbols/bank02.inc.asm` | `` | `` |
| 6 |  |  | 0 | `support` |  | `symbols/bank03.inc.asm` | `` | `` |
| 7 |  |  | 0 | `support` |  | `symbols/bank04.inc.asm` | `` | `` |
| 8 |  |  | 0 | `support` |  | `symbols/bank2f.inc.asm` | `` | `` |
| 9 |  |  | 0 | `support` |  | `symbols/globals.inc.asm` | `` | `` |
| 10 |  |  | 0 | `support` |  | `symbols/misc.inc.asm` | `` | `` |
| 11 |  |  | 0 | `support` |  | `symbols/text.inc.asm` | `` | `` |
| 12 | C1:0000 | C1:0004 | 4 | `exact` | yes | `unknown/C1/C10000.asm` | `UNKNOWN_C10000` | `RunTextDisplaySetupWrapper` |
| 13 | C1:0004 | C1:004E | 74 | `exact` | yes | `unknown/C1/C10004.asm` | `UNKNOWN_C10004` | `ProcessTextboxDataFromCallerPointer` |
| 14 | C1:004E | C1:008E | 64 | `exact` | yes | `text/enable_blinking_triangle.asm` | `UNKNOWN_C1004E` | `PumpTextWaitFrame` |
| 15 | C1:008E | C1:00D6 | 72 | `exact` | yes | `text/clear_blinking_prompt.asm` | `` | `CloseAndDrainAllWindows` |
| 16 | C1:00D6 | C1:00FE | 40 | `exact` | yes | `text/get_blinking_prompt.asm` | `` | `WaitTextTicks` |
| 17 | C1:00FE | C1:0166 | 104 | `exact` | yes | `text/set_text_sound_mode.asm` | `` | `WaitForTextPromptOrInputGate` |
| 18 | C1:004E | C1:008E | 64 | `exact` | yes | `unknown/C1/C1004E.asm` | `UNKNOWN_C1004E` | `PumpTextWaitFrame` |
| 19 | C1:008E | C1:00D6 | 72 | `exact` | yes | `text/get_window_focus.asm` | `` | `CloseAndDrainAllWindows` |
| 20 | C1:00D6 | C1:00FE | 40 | `exact` | yes | `text/set_window_focus.asm` | `` | `WaitTextTicks` |
| 21 | C1:00FE | C1:0166 | 104 | `exact` | yes | `text/close_focus_window.asm` | `` | `WaitForTextPromptOrInputGate` |
| 22 | C1:008E | C1:00D6 | 72 | `exact` | yes | `unknown/C1/C1008E.asm` | `` | `CloseAndDrainAllWindows` |
| 23 | C1:00D6 | C1:00FE | 40 | `exact` | yes | `text/lock_input.asm` | `` | `WaitTextTicks` |
| 24 | C1:00FE | C1:0166 | 104 | `exact` | yes | `text/unlock_input.asm` | `` | `WaitForTextPromptOrInputGate` |
| 25 | C1:00D6 | C1:00FE | 40 | `exact` | yes | `unknown/C1/C100D6.asm` | `` | `WaitTextTicks` |
| 26 | C1:00FE | C1:0166 | 104 | `exact` | yes | `unknown/C1/C100FE.asm` | `` | `WaitForTextPromptOrInputGate` |
| 27 | C1:0166 | C1:02D0 | 362 | `exact` | yes | `text/ccs/halt.asm` | `` | `RunTextHaltControlWorker` |
| 28 | C1:02D0 | C1:0301 | 49 | `exact` | yes | `unknown/C1/C102D0.asm` | `` | `WaitForTextStateFlag9641` |
| 29 | C1:0301 | C1:042E | 301 | `exact` | yes | `text/get_active_window_address.asm` | `` | `GetActiveInteractionContextRecord` |
| 30 | C1:042E | C1:045D | 47 | `exact` | yes | `text/transfer_active_mem_storage.asm` | `` | `IncrementCurrentTextContextWorkmem` |
| 31 | C1:045D | C1:0489 | 44 | `exact` | yes | `text/transfer_storage_mem_active.asm` | `` | `InstallPrimaryInteractionContextPointer` |
| 32 | C1:0489 | C1:04B5 | 44 | `exact` | yes | `text/get_argument_memory.asm` | `` | `InstallSecondaryInteractionContextPointer` |
| 33 | C1:04B5 | C1:078D | 728 | `exact` | yes | `text/get_secondary_memory.asm` | `` | `GetCurrentTextContextLineState` |
| 34 | C1:078D | C1:07AF | 34 | `exact` | yes | `text/get_working_memory.asm` | `` | `InitializeTextWindowTilemapStaging` |
| 35 | C1:07AF | C1:0A85 | 726 | `exact` | yes | `text/increment_secondary_memory.asm` | `UNKNOWN_C107AF` | `BuildWindowTilemapFromDescriptor` |
| 36 | C1:0A85 | C1:0BA1 | 284 | `exact` | yes | `text/set_secondary_memory.asm` | `` | `WriteGlyphToWindowDescriptorBuffer` |
| 37 | C1:0BA1 | C1:0BFE | 93 | `exact` | yes | `text/set_working_memory.asm` | `` | `PrintGlyphToActiveWindow` |
| 38 | C1:0BFE | C1:0C49 | 75 | `exact` | yes | `text/set_argument_memory.asm` | `UNKNOWN_C10BFE` | `CreatePointerBackedTextEntryRecord` |
| 39 | C1:0C49 | C1:0C55 | 12 | `exact` | yes | `text/get_text_x.asm` | `` | `CountTextEntryChainRecords` |
| 40 | C1:0C55 | C1:0D60 | 267 | `exact` | yes | `text/get_text_y.asm` | `UNKNOWN_C10C55` | `FormatNumberFromCallerPointer` |
| 41 | C1:0D60 | C1:0D7C | 28 | `exact` | yes | `text/create_window.asm` | `` | `PrintGlyphAndMarkWindowRedraw` |
| 42 | C1:078D | C1:07AF | 34 | `exact` | yes | `unknown/C1/C1078D.asm` | `` | `InitializeTextWindowTilemapStaging` |
| 43 | C1:07AF | C1:0A85 | 726 | `exact` | yes | `unknown/C1/C107AF.asm` | `UNKNOWN_C107AF` | `BuildWindowTilemapFromDescriptor` |
| 44 | C1:0A85 | C1:0BA1 | 284 | `exact` | yes | `text/show_hppp_windows.asm` | `` | `WriteGlyphToWindowDescriptorBuffer` |
| 45 | C1:0BA1 | C1:0BFE | 93 | `exact` | yes | `text/hide_hppp_windows.asm` | `` | `PrintGlyphToActiveWindow` |
| 46 | C1:0A85 | C1:0BA1 | 284 | `exact` | yes | `unknown/C1/C10A85.asm` | `` | `WriteGlyphToWindowDescriptorBuffer` |
| 47 | C1:0BA1 | C1:0BFE | 93 | `exact` | yes | `unknown/C1/C10BA1.asm` | `` | `PrintGlyphToActiveWindow` |
| 48 | C1:0BFE | C1:0C49 | 75 | `exact` | yes | `text/ccs/clear_line.asm` | `UNKNOWN_C10BFE` | `CreatePointerBackedTextEntryRecord` |
| 49 | C1:0C49 | C1:0C55 | 12 | `exact` | yes | `unknown/C1/C1008E_redirect.asm` | `` | `CountTextEntryChainRecords` |
| 50 | C1:0BFE | C1:0C49 | 75 | `exact` | yes | `unknown/C1/C10BFE.asm` | `UNKNOWN_C10BFE` | `CreatePointerBackedTextEntryRecord` |
| 51 | C1:0C49 | C1:0C55 | 12 | `exact` | yes | `unknown/C1/C1138D_redirect.asm` | `` | `CountTextEntryChainRecords` |
| 52 | C1:0C55 | C1:0D60 | 267 | `exact` | yes | `unknown/C1/C117E2_redirect.asm` | `UNKNOWN_C10C55` | `FormatNumberFromCallerPointer` |
| 53 | C1:0C55 | C1:0D60 | 267 | `exact` | yes | `unknown/C1/C10C55.asm` | `UNKNOWN_C10C55` | `FormatNumberFromCallerPointer` |
| 54 | C1:0D60 | C1:0D7C | 28 | `exact` | yes | `unknown/C4/C438A5_redirect.asm` | `` | `PrintGlyphAndMarkWindowRedraw` |
| 55 | C1:0D7C | C1:0F40 | 452 | `exact` | yes | `text/print_newline_redirect.asm` | `` | `FormatDecimalDigitsTo8960` |
| 56 | C1:0F40 | C1:134B | 1035 | `exact` | yes | `unknown/C1/C10BA1_redirect.asm` | `` | `ClearWindowContentByFocusIndex` |
| 57 | C1:134B | C1:138D | 66 | `exact` | yes | `text/print_letter_redirect.asm` | `` | `SetupTextDisplayWithWalletStatus` |
| 58 | C1:138D | C1:13D1 | 68 | `exact` | yes | `text/print_string_redirect.asm` | `` | `CountTextEntryChainRecordsLocal` |
| 59 | C1:13D1 | C1:14B1 | 224 | `exact` | yes | `unknown/C4/C437B8_redirect.asm` | `` | `InstallTextEntryRecord` |
| 60 | C1:14B1 | C1:153B | 138 | `exact` | yes | `text/print_letter.asm` | `` | `CreateTextEntryRecordWithDisplayMetadata` |
| 61 | C1:0D60 | C1:0D7C | 28 | `exact` | yes | `unknown/C1/C10D60.asm` | `` | `PrintGlyphAndMarkWindowRedraw` |
| 62 | C1:0D7C | C1:0F40 | 452 | `exact` | yes | `unknown/C1/C10D7C.asm` | `` | `FormatDecimalDigitsTo8960` |
| 63 | C1:0F40 | C1:134B | 1035 | `exact` | yes | `text/print_number.asm` | `` | `ClearWindowContentByFocusIndex` |
| 64 | C1:0EB4 | C1:0EE3 | 47 | `exact` | yes | `unknown/C1/C10EB4.asm` | `` | `` |
| 65 | C1:0EE3 |  | 0 | `open` |  | `unknown/C1/C10EE3.asm` | `` | `` |
| 66 |  |  | 0 | `open` |  | `text/print_string.asm` | `` | `` |
| 67 | C1:0F40 | C1:134B | 1035 | `exact` | yes | `unknown/C1/C10F40.asm` | `` | `ClearWindowContentByFocusIndex` |
| 68 | C1:0FA3 |  | 0 | `open` |  | `unknown/C1/C10FA3.asm` | `` | `` |
| 69 |  |  | 0 | `open` |  | `text/change_current_window_font.asm` | `` | `` |
| 70 | C1:0FEA |  | 0 | `open` |  | `unknown/C1/C10FEA.asm` | `` | `` |
| 71 |  |  | 0 | `open` |  | `text/num_select_prompt.asm` | `` | `` |
| 72 | C1:134B | C1:138D | 66 | `exact` | yes | `unknown/C1/C1134B.asm` | `` | `SetupTextDisplayWithWalletStatus` |
| 73 | C1:1354 | C1:1383 | 47 | `exact` | yes | `unknown/C1/C11354.asm` | `` | `` |
| 74 | C1:1383 | C1:138D | 10 | `exact` | yes | `unknown/C1/C11383.asm` | `` | `` |
| 75 | C1:138D | C1:13D1 | 68 | `exact` | yes | `unknown/C1/C1138D.asm` | `` | `CountTextEntryChainRecordsLocal` |
| 76 | C1:13D1 | C1:14B1 | 224 | `exact` | yes | `unknown/C1/C113D1.asm` | `` | `InstallTextEntryRecord` |
| 77 | C1:14B1 | C1:153B | 138 | `exact` | yes | `unknown/C1/C114B1.asm` | `` | `CreateTextEntryRecordWithDisplayMetadata` |
| 78 | C1:153B | C1:1596 | 91 | `exact` | yes | `unknown/C1/C1153B.asm` | `` | `CreateTypedTextEntryRecord` |
| 79 | C1:1596 | C1:15F4 | 94 | `exact` | yes | `unknown/C1/C11596.asm` | `` | `CreateTypedTextEntryRecordWithExtraByte` |
| 80 | C1:15F4 | C1:17E2 | 494 | `exact` | yes | `unknown/C1/C115F4.asm` | `` | `CreateTypedTextEntryRecordDirect` |
| 81 | C1:17E2 | C1:180D | 43 | `exact` | yes | `text/print_menu_items.asm` | `` | `MeasureBoundedStringLength` |
| 82 | C1:17E2 | C1:180D | 43 | `exact` | yes | `unknown/C1/C117E2.asm` | `` | `MeasureBoundedStringLength` |
| 83 | C1:180D | C1:181B | 14 | `exact` | yes | `unknown/C1/C1180D.asm` | `` | `LayoutActiveTextEntriesAndRefresh` |
| 84 | C1:181B | C1:1887 | 108 | `exact` | yes | `unknown/C1/C1181B.asm` | `` | `SelectActiveTextEntryByY` |
| 85 | C1:1887 | C1:1F8A | 1795 | `exact` | yes | `unknown/C1/C11887.asm` | `` | `SelectActiveTextEntryByA` |
| 86 | C1:1F8A | C1:1FBC | 50 | `exact` | yes | `text/move_cursor.asm` | `MOVE_CURSOR` | `ClearActiveSelectionPromptScratch` |
| 87 | C1:1FBC | C1:1FD4 | 24 | `exact` | yes | `text/selection_menu.asm` | `` | `ReadSelectionPromptCandidateByte` |
| 88 | C1:1F5A | C1:1F8A | 48 | `exact` | yes | `unknown/C1/C11F5A.asm` | `` | `` |
| 89 | C1:1F8A | C1:1FBC | 50 | `exact` | yes | `unknown/C1/C11F8A.asm` | `` | `ClearActiveSelectionPromptScratch` |
| 90 | C1:1FBC | C1:1FD4 | 24 | `exact` | yes | `unknown/C1/C11FBC.asm` | `` | `ReadSelectionPromptCandidateByte` |
| 91 | C1:1FD4 | C1:2012 | 62 | `exact` | yes | `unknown/C1/C11FD4.asm` | `` | `IsSelectionPromptCandidateEligible` |
| 92 | C1:2012 | C1:2070 | 94 | `exact` | yes | `unknown/C1/C12012.asm` | `` | `FindNextSelectionPromptCandidate` |
| 93 | C1:2070 | C1:20D6 | 102 | `exact` | yes | `unknown/C1/C12070.asm` | `` | `FindPreviousSelectionPromptCandidate` |
| 94 | C1:20D6 | C1:21B8 | 226 | `exact` | yes | `unknown/C1/C120D6.asm` | `` | `RefreshSelectionPromptCandidateText` |
| 95 | C1:21B8 | C1:2362 | 426 | `exact` | yes | `unknown/C1/C121B8.asm` | `` | `RunTwoListCharacterSelectionPrompt` |
| 96 | C1:2362 | C1:242E | 204 | `exact` | yes | `unknown/C1/C12362.asm` | `` | `RunSimpleSideSelectionPrompt` |
| 97 | C1:242E | C1:2BF3 | 1989 | `exact` | yes | `unknown/C1/C1242E.asm` | `` | `DispatchCharacterSelectionPromptMode` |
| 98 | C1:244C |  | 0 | `open` |  | `unknown/C1/C1244C.asm` | `` | `` |
| 99 |  |  | 0 | `open` |  | `text/character_select_prompt.asm` | `` | `` |
| 100 | C1:2BD5 | C1:2BF3 | 30 | `exact` | yes | `unknown/C1/C12BD5.asm` | `` | `` |
| 101 | C1:2BF3 | C1:2C36 | 67 | `exact` | yes | `unknown/C1/C12BF3.asm` | `UNKNOWN_C12BF3` | `PrintDebugMenuTitleWordsWithTicks` |
| 102 | C1:2C36 | C1:2CCC | 150 | `exact` | yes | `unknown/C1/C12C36.asm` | `UNKNOWN_C12C36` | `PrintDebugMenuFixedWordGroups` |
| 103 | C1:2CCC | C1:2D17 | 75 | `exact` | yes | `unknown/C1/C12CCC.asm` | `` | `FormatDebugDecimalFiveDigits` |
| 104 | C1:2D17 | C1:2DD5 | 190 | `exact` | yes | `unknown/C1/C12D17.asm` | `` | `ToggleDebugMeterDisplayOverlay` |
| 105 | C1:2DD5 | C1:2E42 | 109 | `exact` | yes | `text/window_tick.asm` | `WINDOW_TICK` | `` |
| 106 | C1:2E42 | C1:2E63 | 33 | `exact` | yes | `unknown/C1/C12E42.asm` | `UNKNOWN_C12E42` | `` |
| 107 | C1:2E63 | C1:3187 | 804 | `exact` | yes | `system/debug/y_button_menu.asm` | `DEBUG_Y_BUTTON_MENU` | `` |
| 108 | C1:3187 | C1:323B | 180 | `exact` | yes | `overworld/talk_to.asm` | `TALK_TO` | `ResolvePrimaryFrontInteractionOutput` |
| 109 | C1:323B | C1:339E | 355 | `exact` | yes | `overworld/check.asm` | `CHECK` | `ResolveSecondaryFacingInteractionOutput` |
| 110 | C1:339E | C1:33A7 | 9 | `exact` | yes | `unknown/C1/C1339E.asm` | `UNKNOWN_C1339E` | `BuildCheckMenuEntriesWrapper` |
| 111 | C1:33A7 | C1:33B0 | 9 | `exact` | yes | `unknown/C1/C133A7.asm` | `UNKNOWN_C133A7` | `BuildOpenMenuEntriesWrapper` |
| 112 | C1:33B0 | C1:34A7 | 247 | `exact` | yes | `unknown/C1/C133B0.asm` | `` | `RebuildOpenMenuTextEntryRecords` |
| 113 | C1:34A7 | C1:3C32 | 1931 | `exact` | yes | `overworld/open_menu.asm` | `` | `` |
| 114 | C1:3C32 | C1:3CA1 | 111 | `exact` | yes | `text/open_hppp_display.asm` | `OPEN_HPPP_DISPLAY` | `` |
| 115 | C1:3CA1 | C1:4012 | 881 | `exact` | yes | `overworld/show_town_map.asm` | `SHOW_TOWN_MAP` | `OpenHpppDisplay` |
| 116 | C1:4012 | C1:4049 | 55 | `exact` | yes | `overworld/debug/y_button_flag.asm` | `DEBUG_Y_BUTTON_FLAG` | `` |
| 117 | C1:4049 | C1:4070 | 39 | `exact` | yes | `overworld/debug/y_button_guide.asm` | `DEBUG_Y_BUTTON_GUIDE` | `` |
| 118 | C1:4070 | C1:4103 | 147 | `exact` | yes | `overworld/debug/set_char_level.asm` | `DEBUG_SET_CHAR_LEVEL` | `` |
| 119 | C1:4103 | C1:41D0 | 205 | `exact` | yes | `overworld/debug/y_button_goods.asm` | `DEBUG_Y_BUTTON_GOODS` | `BuildTextCommand24BitJumpTarget` |
| 120 | C1:4012 | C1:4049 | 55 | `exact` | yes | `unknown/C1/C14012.asm` | `` | `` |
| 121 | C1:4049 | C1:4070 | 39 | `exact` | yes | `unknown/C1/C14049.asm` | `` | `` |
| 122 | C1:4070 | C1:4103 | 147 | `exact` | yes | `unknown/C1/C14070.asm` | `` | `` |
| 123 | C1:4103 | C1:41D0 | 205 | `exact` | yes | `text/ccs/print_stat.asm` | `` | `BuildTextCommand24BitJumpTarget` |
| 124 | C1:41D0 | C1:4265 | 149 | `exact` | yes | `text/ccs/print_party_or_hint_new_line.asm` | `` | `HandleTextCommand09JumpMulti` |
| 125 | C1:4265 | C1:42AD | 72 | `exact` | yes | `text/ccs/unknown_1C_09.asm` | `` | `HandleTextCommand04SetEventFlag` |
| 126 | C1:42AD | C1:42F5 | 72 | `exact` | yes | `text/ccs/text_effects.asm` | `` | `HandleTextCommand05ClearEventFlag` |
| 127 | C1:42F5 | C1:435F | 106 | `exact` | yes | `text/ccs/jump.asm` | `` | `HandleTextCommand06JumpIfFlagSet` |
| 128 | C1:435F | C1:43D6 | 119 | `exact` | yes | `text/ccs/jump_multi.asm` | `` | `HandleTextCommand07CheckEventFlag` |
| 129 | C1:43D6 | C1:44A3 | 205 | `exact` | yes | `text/ccs/set_event_flag.asm` | `` | `BuildCallTextFarPointerAndDispatch` |
| 130 | C1:44A3 | C1:4509 | 102 | `exact` | yes | `text/ccs/clear_event_flag.asm` | `` | `` |
| 131 | C1:4509 | C1:4558 | 79 | `exact` | yes | `text/ccs/jump_event_flag.asm` | `` | `` |
| 132 | C1:4558 | C1:4591 | 57 | `exact` | yes | `text/ccs/get_event_flag.asm` | `` | `HandleTextCommand0BTestWorkmemTrue` |
| 133 | C1:4591 | C1:45EF | 94 | `exact` | yes | `text/ccs/print_special_graphics.asm` | `` | `HandleTextCommand0CTestWorkmemFalse` |
| 134 | C1:45EF | C1:461A | 43 | `exact` | yes | `text/ccs/open_window.asm` | `` | `HandleTextCommand0DCopyToArgmem` |
| 135 | C1:461A | C1:463B | 33 | `exact` | yes | `text/ccs/switch_to_window.asm` | `` | `HandleTextCommand0EStoreToArgmem` |
| 136 | C1:463B | C1:467D | 66 | `exact` | yes | `text/ccs/call.asm` | `` | `` |
| 137 | C1:467D | C1:46BF | 66 | `exact` | yes | `text/ccs/create_number_selector.asm` | `` | `` |
| 138 | C1:46BF | C1:4751 | 146 | `exact` | yes | `text/ccs/force_text_alignment.asm` | `` | `` |
| 139 | C1:4751 | C1:47A0 | 79 | `exact` | yes | `text/ccs/check_equal.asm` | `` | `` |
| 140 | C1:47A0 | C1:47AB | 11 | `exact` | yes | `text/ccs/check_not_equal.asm` | `` | `` |
| 141 | C1:47AB | C1:4819 | 110 | `exact` | yes | `text/ccs/print_horizontal_strings.asm` | `` | `` |
| 142 | C1:4819 | C1:488C | 115 | `exact` | yes | `text/ccs/copy_to_argmem.asm` | `` | `ReadStatisticSelectorStringCharacter` |
| 143 | C1:488C | C1:48AC | 32 | `exact` | yes | `text/ccs/set_secmem.asm` | `` | `` |
| 144 | C1:48AC | C1:48E9 | 61 | `exact` | yes | `text/ccs/party_selection_menu_uncancellable.asm` | `` | `TestCurrentItemCompactCategory` |
| 145 | C1:48E9 | C1:494A | 97 | `exact` | yes | `text/ccs/party_selection_menu.asm` | `` | `` |
| 146 | C1:494A | C1:49B6 | 108 | `exact` | yes | `text/ccs/print_item_name.asm` | `` | `` |
| 147 | C1:49B6 | C1:4A03 | 77 | `exact` | yes | `text/ccs/print_teleport_destination_name.asm` | `` | `` |
| 148 | C1:4A03 | C1:4A50 | 77 | `exact` | yes | `text/ccs/get_character_number.asm` | `` | `` |
| 149 | C1:4A50 | C1:4A9D | 77 | `exact` | yes | `text/ccs/play_music.asm` | `` | `` |
| 150 | C1:4A9D | C1:4AEA | 77 | `exact` | yes | `text/ccs/stop_music.asm` | `` | `` |
| 151 | C1:4AEA | C1:4B37 | 77 | `exact` | yes | `text/ccs/play_sfx.asm` | `` | `` |
| 152 | C1:4B37 | C1:4B84 | 77 | `exact` | yes | `text/ccs/get_letter_from_character_name.asm` | `` | `` |
| 153 | C1:4B84 | C1:4BD1 | 77 | `exact` | yes | `text/ccs/get_letter_from_stat.asm` | `` | `` |
| 154 | C1:4BD1 | C1:4C1E | 77 | `exact` | yes | `text/ccs/print_character.asm` | `` | `` |
| 155 | C1:4C1E | C1:4C86 | 104 | `exact` | yes | `text/ccs/test_inventory_full.asm` | `` | `` |
| 156 | C1:4C86 | C1:4CEE | 104 | `exact` | yes | `text/ccs/wallet_increase.asm` | `` | `` |
| 157 | C1:4CEE | C1:4D24 | 54 | `exact` | yes | `text/ccs/wallet_decrease.asm` | `` | `FindPartyMemberWithInventoryRoomForTextCommand` |
| 158 | C1:4D24 | C1:4D93 | 111 | `exact` | yes | `text/ccs/recover_hp_by_percent.asm` | `` | `` |
| 159 | C1:4D93 | C1:4DFB | 104 | `exact` | yes | `text/ccs/deplete_hp_by_percent.asm` | `` | `FindPartyMemberWithItemForTextCommand` |
| 160 | C1:4DFB | C1:4E8C | 145 | `exact` | yes | `text/ccs/recover_hp_by_amount.asm` | `` | `` |
| 161 | C1:4E8C | C1:4EAB | 31 | `exact` | yes | `text/ccs/deplete_hp_by_amount.asm` | `` | `` |
| 162 | C1:4EAB | C1:4EB5 | 10 | `exact` | yes | `text/ccs/recover_pp_by_percent.asm` | `` | `HandleTextCommand10ParameterizedPause` |
| 163 | C1:4EB5 | C1:4EF8 | 67 | `exact` | yes | `text/ccs/deplete_pp_by_percent.asm` | `` | `` |
| 164 | C1:4EF8 | C1:4F33 | 59 | `exact` | yes | `text/ccs/recover_pp_by_amount.asm` | `` | `` |
| 165 | C1:4F33 | C1:4F6F | 60 | `exact` | yes | `text/ccs/deplete_pp_by_amount.asm` | `` | `` |
| 166 | C1:4F6F | C1:4FD7 | 104 | `exact` | yes | `text/ccs/give_item_to_character.asm` | `GIVE_ITEM_TO_CHARACTER` | `` |
| 167 | C1:4FD7 | C1:5007 | 48 | `exact` | yes | `text/ccs/take_item_from_character.asm` | `TAKE_ITEM_FROM_CHARACTER` | `` |
| 168 | C1:5007 | C1:506F | 104 | `exact` | yes | `text/ccs/test_inventory_not_full.asm` | `` | `` |
| 169 | C1:506F | C1:50E4 | 117 | `exact` | yes | `text/ccs/test_character_doesnt_have_item.asm` | `` | `` |
| 170 | C1:50E4 | C1:516B | 135 | `exact` | yes | `text/ccs/test_character_has_item.asm` | `` | `` |
| 171 | C1:516B | C1:51FC | 145 | `exact` | yes | `text/ccs/trigger_psi_teleport.asm` | `` | `` |
| 172 | C1:51FC | C1:528D | 145 | `exact` | yes | `text/ccs/trigger_teleport.asm` | `` | `` |
| 173 | C1:528D | C1:5384 | 247 | `exact` | yes | `text/ccs/pause.asm` | `` | `` |
| 174 | C1:5384 | C1:53AF | 43 | `exact` | yes | `text/ccs/display_shop_menu.asm` | `` | `` |
| 175 | C1:53AF | C1:5494 | 229 | `exact` | yes | `text/ccs/get_item_price.asm` | `` | `` |
| 176 | C1:5494 | C1:549E | 10 | `exact` | yes | `text/ccs/get_item_sell_price.asm` | `` | `` |
| 177 | C1:549E | C1:5529 | 139 | `exact` | yes | `text/ccs/test_character_can_equip_item.asm` | `` | `` |
| 178 | C1:5529 | C1:554E | 37 | `exact` | yes | `text/ccs/print_character_name.asm` | `` | `` |
| 179 | C1:554E | C1:5573 | 37 | `exact` | yes | `text/ccs/get_character_status.asm` | `` | `` |
| 180 | C1:5573 | C1:5659 | 230 | `exact` | yes | `text/ccs/inflict_character_status.asm` | `` | `` |
| 181 | C1:5659 | C1:56DB | 130 | `exact` | yes | `text/ccs/test_character_status.asm` | `` | `` |
| 182 | C1:56DB | C1:575D | 130 | `exact` | yes | `text/ccs/get_gender_etc.asm` | `` | `` |
| 183 | C1:575D | C1:57CD | 112 | `exact` | yes | `text/ccs/switch_gender_etc.asm` | `` | `TestEquippedItemPresenceForTextCommand` |
| 184 | C1:57CD | C1:583D | 112 | `exact` | yes | `text/ccs/test_equality.asm` | `` | `` |
| 185 | C1:583D | C1:58A5 | 104 | `exact` | yes | `text/ccs/get_exp_for_next_level.asm` | `` | `` |
| 186 | C1:58A5 | C1:58FE | 89 | `exact` | yes | `text/ccs/print_number.asm` | `` | `` |
| 187 | C1:58FE | C1:597F | 129 | `exact` | yes | `text/ccs/unknown_1F_60.asm` | `` | `` |
| 188 | C1:597F | C1:59F9 | 122 | `exact` | yes | `text/ccs/show_character_inventory.asm` | `` | `` |
| 189 | C1:59F9 | C1:5B0E | 277 | `exact` | yes | `text/ccs/unknown_18_08.asm` | `` | `` |
| 190 | C1:5B0E | C1:5B46 | 56 | `exact` | yes | `text/ccs/unknown_18_09.asm` | `` | `` |
| 191 | C1:5B46 | C1:5BA7 | 97 | `exact` | yes | `text/ccs/print_money_amount.asm` | `` | `` |
| 192 | C1:5BA7 | C1:5BCA | 35 | `exact` | yes | `text/ccs/give_item_to_character_2.asm` | `` | `` |
| 193 | C1:5BCA | C1:5C36 | 108 | `exact` | yes | `text/ccs/take_item_from_character_2.asm` | `` | `` |
| 194 | C1:5C36 | C1:5C58 | 34 | `exact` | yes | `text/ccs/unknown_1D_10.asm` | `` | `` |
| 195 | C1:5C58 | C1:5C85 | 45 | `exact` | yes | `text/ccs/unknown_1D_11.asm` | `` | `` |
| 196 | C1:5C85 | C1:5D6B | 230 | `exact` | yes | `text/ccs/equip_character_from_inventory.asm` | `` | `` |
| 197 | C1:5D6B | C1:5E5C | 241 | `exact` | yes | `text/ccs/unknown_1D_12.asm` | `` | `` |
| 198 | C1:5E5C | C1:5F71 | 277 | `exact` | yes | `text/ccs/unknown_1D_13.asm` | `` | `` |
| 199 | C1:5F71 | C1:5F91 | 32 | `exact` | yes | `text/ccs/get_item_number.asm` | `` | `` |
| 200 | C1:5F91 | C1:5FF7 | 102 | `exact` | yes | `text/ccs/test_has_enough_money.asm` | `` | `` |
| 201 | C1:5FF7 | C1:6080 | 137 | `exact` | yes | `text/ccs/unknown_19_1A.asm` | `` | `` |
| 202 | C1:6080 | C1:6124 | 164 | `exact` | yes | `text/ccs/unknown_18_0D.asm` | `` | `` |
| 203 | C1:6124 | C1:6143 | 31 | `exact` | yes | `text/ccs/print_vertical_strings.asm` | `` | `` |
| 204 | C1:6143 | C1:6172 | 47 | `exact` | yes | `text/ccs/set_argmem.asm` | `` | `` |
| 205 | C1:6172 | C1:61D1 | 95 | `exact` | yes | `text/ccs/unknown_19_1B.asm` | `` | `` |
| 206 | C1:61D1 | C1:61F0 | 31 | `exact` | yes | `text/ccs/learn_special_psi.asm` | `` | `` |
| 207 | C1:61F0 | C1:621F | 47 | `exact` | yes | `text/ccs/atm_increase.asm` | `` | `` |
| 208 | C1:621F | C1:6308 | 233 | `exact` | yes | `text/ccs/atm_decrease.asm` | `` | `FinalizeTextCommand1FC0JumpMulti2Target` |
| 209 | C1:6308 | C1:63A7 | 159 | `exact` | yes | `text/ccs/test_atm_has_enough_money.asm` | `` | `` |
| 210 | C1:63A7 | C1:63FD | 86 | `exact` | yes | `text/ccs/party_member_add.asm` | `` | `` |
| 211 | C1:63FD | C1:646E | 113 | `exact` | yes | `text/ccs/party_member_remove.asm` | `` | `` |
| 212 | C1:5FB1 |  | 0 | `open` |  | `unknown/C1/C15FB1.asm` | `` | `` |
| 213 |  |  | 0 | `open` |  | `text/ccs/unknown_19_1C.asm` | `` | `` |
| 214 |  |  | 0 | `open` |  | `text/ccs/unknown_19_1D.asm` | `` | `` |
| 215 |  |  | 0 | `open` |  | `text/ccs/escargo_express_store.asm` | `` | `` |
| 216 |  |  | 0 | `open` |  | `text/ccs/test_item_is_drink.asm` | `` | `` |
| 217 |  |  | 0 | `open` |  | `text/ccs/test_party_enough_characters.asm` | `` | `` |
| 218 |  |  | 0 | `open` |  | `text/ccs/print_psi_name.asm` | `` | `` |
| 219 |  |  | 0 | `open` |  | `text/ccs/get_random_number.asm` | `` | `` |
| 220 | C1:621F | C1:6308 | 233 | `exact` | yes | `unknown/C1/C1621F.asm` | `` | `FinalizeTextCommand1FC0JumpMulti2Target` |
| 221 | C1:6308 | C1:63A7 | 159 | `exact` | yes | `text/ccs/jump_multi2.asm` | `` | `` |
| 222 | C1:63A7 | C1:63FD | 86 | `exact` | yes | `text/ccs/try_fixing_items.asm` | `` | `` |
| 223 | C1:63FD | C1:646E | 113 | `exact` | yes | `text/ccs/set_character_direction.asm` | `` | `` |
| 224 | C1:646E | C1:6490 | 34 | `exact` | yes | `text/ccs/set_party_direction.asm` | `` | `` |
| 225 | C1:6490 | C1:6509 | 121 | `exact` | yes | `text/ccs/set_tpt_direction.asm` | `` | `` |
| 226 | C1:6509 | C1:6582 | 121 | `exact` | yes | `text/ccs/create_entity_tpt.asm` | `` | `` |
| 227 | C1:6582 | C1:65AA | 40 | `exact` | yes | `text/ccs/dummy_1F_18.asm` | `` | `` |
| 228 | C1:65AA | C1:65D2 | 40 | `exact` | yes | `text/ccs/dummy_1F_19.asm` | `` | `` |
| 229 | C1:65D2 | C1:662A | 88 | `exact` | yes | `text/ccs/create_floating_sprite_at_tpt_entity.asm` | `` | `` |
| 230 | C1:662A | C1:666D | 67 | `exact` | yes | `text/ccs/delete_floating_sprite_at_tpt_entity.asm` | `` | `` |
| 231 | C1:666D | C1:66DD | 112 | `exact` | yes | `text/ccs/create_floating_sprite_at_character.asm` | `` | `` |
| 232 | C1:66DD | C1:66FE | 33 | `exact` | yes | `text/ccs/delete_floating_sprite_at_character.asm` | `` | `` |
| 233 | C1:66FE | C1:6744 | 70 | `exact` | yes | `text/ccs/set_map_palette.asm` | `` | `` |
| 234 | C1:6744 | C1:67D6 | 146 | `exact` | yes | `text/ccs/create_entity_sprite.asm` | `` | `` |
| 235 | C1:67D6 | C1:683B | 101 | `exact` | yes | `text/ccs/delete_entity_tpt.asm` | `` | `` |
| 236 | C1:683B | C1:68A0 | 101 | `exact` | yes | `text/ccs/delete_entity_sprite.asm` | `` | `` |
| 237 | C1:68A0 | C1:6947 | 167 | `exact` | yes | `text/ccs/get_direction_from_character_to_entity.asm` | `` | `` |
| 238 | C1:6947 | C1:69F7 | 176 | `exact` | yes | `text/ccs/get_direction_from_tpt_entity_to_entity.asm` | `` | `` |
| 239 | C1:69F7 | C1:6A01 | 10 | `exact` | yes | `text/ccs/enable_blinking_triangle.asm` | `` | `` |
| 240 | C1:6A01 | C1:6A7B | 122 | `exact` | yes | `text/ccs/set_character_level.asm` | `` | `` |
| 241 | C1:6A7B | C1:6B2B | 176 | `exact` | yes | `text/ccs/get_direction_from_sprite_entity_to_entity.asm` | `` | `` |
| 242 | C1:6B2B | C1:6BA4 | 121 | `exact` | yes | `text/ccs/set_entity_direction_sprite.asm` | `` | `` |
| 243 | C1:6BA4 | C1:6BAF | 11 | `exact` | yes | `text/ccs/set_player_movement_lock.asm` | `` | `` |
| 244 | C1:6BAF | C1:6BF2 | 67 | `exact` | yes | `text/ccs/set_tpt_entity_delay.asm` | `` | `` |
| 245 | C1:6BF2 | C1:6C35 | 67 | `exact` | yes | `text/ccs/unknown_1F_E7.asm` | `` | `` |
| 246 | C1:6C35 | C1:6C40 | 11 | `exact` | yes | `text/ccs/set_player_movement_lock_if_camera_refocused.asm` | `` | `` |
| 247 | C1:6C40 | C1:6C83 | 67 | `exact` | yes | `text/ccs/unknown_1F_E9.asm` | `` | `` |
| 248 | C1:6C83 | C1:6CC6 | 67 | `exact` | yes | `text/ccs/unknown_1F_EA.asm` | `` | `` |
| 249 | C1:6CC6 | C1:6D14 | 78 | `exact` | yes | `text/ccs/set_character_invisibility.asm` | `` | `` |
| 250 | C1:6D14 | C1:6D62 | 78 | `exact` | yes | `text/ccs/set_character_visibility.asm` | `` | `` |
| 251 | C1:6D62 | C1:6DA5 | 67 | `exact` | yes | `text/ccs/teleport_party_to_tpt_entity.asm` | `` | `` |
| 252 | C1:6DA5 | C1:6DE8 | 67 | `exact` | yes | `text/ccs/unknown_1F_EF.asm` | `` | `` |
| 253 | C1:6DE8 | C1:6EBF | 215 | `exact` | yes | `text/ccs/screen_reload_pointer.asm` | `` | `` |
| 254 | C1:6EBF | C1:6F2F | 112 | `exact` | yes | `text/ccs/set_tpt_entity_movement.asm` | `` | `` |
| 255 | C1:6F2F | C1:6F9F | 112 | `exact` | yes | `text/ccs/set_sprite_entity_movement.asm` | `` | `` |
| 256 | C1:6F9F | C1:6FD1 | 50 | `exact` | yes | `text/ccs/test_item_is_condiment.asm` | `` | `` |
| 257 | C1:6FD1 | C1:7058 | 135 | `exact` | yes | `text/ccs/trigger_battle.asm` | `` | `` |
| 258 | C1:7058 | C1:711C | 196 | `exact` | yes | `text/ccs/set_respawn_point.asm` | `` | `` |
| 259 | C1:711C | C1:7233 | 279 | `exact` | yes | `text/ccs/unknown_1D_0C.asm` | `` | `` |
| 260 | C1:7233 | C1:7254 | 33 | `exact` | yes | `text/ccs/activate_hotspot.asm` | `` | `` |
| 261 | C1:7254 | C1:7274 | 32 | `exact` | yes | `text/ccs/deactivate_hotspot.asm` | `` | `` |
| 262 | C1:7274 | C1:72BC | 72 | `exact` | yes | `text/ccs/toggle_text_printing_sound.asm` | `` | `StageBankDepositAccumulatorTextValue` |
| 263 | C1:72BC | C1:72DA | 30 | `exact` | yes | `text/ccs/unknown_1D_24.asm` | `` | `` |
| 264 | C1:72DA | C1:7304 | 42 | `exact` | yes | `text/ccs/unknown_1F_40.asm` | `` | `` |
| 265 | C1:7304 | C1:7325 | 33 | `exact` | yes | `text/ccs/trigger_special_event.asm` | `` | `` |
| 266 | C1:7325 | C1:737D | 88 | `exact` | yes | `text/ccs/trigger_photographer_event.asm` | `` | `` |
| 267 | C1:737D | C1:73C0 | 67 | `exact` | yes | `text/ccs/create_floating_sprite_at_sprite_entity.asm` | `` | `` |
| 268 | C1:73C0 | C1:741F | 95 | `exact` | yes | `text/ccs/delete_floating_sprite_at_sprite_entity.asm` | `` | `` |
| 269 | C1:741F | C1:7440 | 33 | `exact` | yes | `text/ccs/display_battle_animation.asm` | `` | `` |
| 270 | C1:7440 | C1:744B | 11 | `exact` | yes | `text/ccs/set_music_effect.asm` | `` | `TimedDeliveryRowSelectorCallback` |
| 271 | C1:744B | C1:7523 | 216 | `exact` | yes | `text/ccs/trigger_timed_event.asm` | `` | `` |
| 272 | C1:7523 | C1:7584 | 97 | `exact` | yes | `text/ccs/increase_character_experience.asm` | `` | `` |
| 273 | C1:7584 | C1:75E5 | 97 | `exact` | yes | `text/ccs/increase_character_iq.asm` | `` | `` |
| 274 | C1:75E5 | C1:7646 | 97 | `exact` | yes | `text/ccs/increase_character_guts.asm` | `` | `` |
| 275 | C1:7646 | C1:76A7 | 97 | `exact` | yes | `text/ccs/increase_character_speed.asm` | `` | `` |
| 276 | C1:76A7 | C1:7708 | 97 | `exact` | yes | `text/ccs/increase_character_vitality.asm` | `` | `` |
| 277 | C1:7708 | C1:776A | 98 | `exact` | yes | `text/ccs/increase_character_luck.asm` | `` | `ClassifyEquippedItemOffensiveDefensive` |
| 278 | C1:776A | C1:7796 | 44 | `exact` | yes | `text/ccs/unknown_1D_23.asm` | `` | `` |
| 279 | C1:7796 | C1:7889 | 243 | `exact` | yes | `text/ccs/unknown_19_27.asm` | `` | `FinalizeLoadedStringWithCompanionPointer` |
| 280 | C1:7796 | C1:7889 | 243 | `exact` | yes | `unknown/C1/C17796.asm` | `` | `FinalizeLoadedStringWithCompanionPointer` |
| 281 | C1:7889 | C1:78F7 | 110 | `exact` | yes | `unknown/C1/C17889.asm` | `` | `ContinueLoadedStringInlineCollector` |
| 282 | C1:78F7 | C1:7AE3 | 492 | `exact` | yes | `text/ccs/load_string.asm` | `` | `StartLoadedStringInlineCollector` |
| 283 | C1:7AE3 | C1:7AF3 | 16 | `exact` | yes | `text/ccs/tree_18.asm` | `` | `LoadDisplayTextPointerSubstitutionSlot` |
| 284 | C1:7AF3 | C1:7B0D | 26 | `exact` | yes | `text/ccs/tree_19.asm` | `` | `LoadDisplayTextByteSubstitutionSlot` |
| 285 | C1:7B0D | C1:7B56 | 73 | `exact` | yes | `text/ccs/tree_1A.asm` | `` | `LoadDisplayTextMushroomizedSelectorByte` |
| 286 | C1:7B56 | C1:866D | 2839 | `exact` | yes | `text/ccs/tree_1B.asm` | `` | `DispatchDisplayTextDynamicSourceSelector` |
| 287 | C1:866D | C1:869D | 48 | `exact` | yes | `text/ccs/tree_1C.asm` | `` | `InitializeManagedTextEventSlotFront` |
| 288 | C1:869D | C1:86B1 | 20 | `exact` | yes | `text/ccs/tree_1D.asm` | `` | `ApplyActiveManagedTextEventSlotSnapshot` |
| 289 | C1:86B1 | C1:87CC | 283 | `exact` | yes | `text/ccs/tree_1E.asm` | `` | `ExecuteNestedTextPointer` |
| 290 | C1:87CC | C1:8B2C | 864 | `exact` | yes | `text/ccs/tree_1F.asm` | `` | `InvokeTextEngineCallbackLowWord` |
| 291 | C1:866D | C1:869D | 48 | `exact` | yes | `unknown/C1/C1866D.asm` | `` | `InitializeManagedTextEventSlotFront` |
| 292 | C1:869D | C1:86B1 | 20 | `exact` | yes | `unknown/C1/C1869D.asm` | `` | `ApplyActiveManagedTextEventSlotSnapshot` |
| 293 | C1:86B1 | C1:87CC | 283 | `exact` | yes | `text/display_text.asm` | `DISPLAY_TEXT` | `ExecuteNestedTextPointer` |
| 294 | C1:87CC | C1:8B2C | 864 | `exact` | yes | `misc/give_item_to_specific_character.asm` | `` | `InvokeTextEngineCallbackLowWord` |
| 295 | C1:8B2C | C1:8BC6 | 154 | `exact` | yes | `misc/give_item_to_character.asm` | `GIVE_ITEM_TO_CHARACTER` | `InsertItemIntoFirstEmptyInventorySlot` |
| 296 | C1:8BC6 | C1:8C27 | 97 | `exact` | yes | `misc/remove_item_from_inventory.asm` | `` | `InsertItemIntoCharacterInventory` |
| 297 | C1:8C27 | C1:8E5B | 564 | `exact` | yes | `misc/take_item_from_specific_character.asm` | `` | `RemoveItemFromCharacterInventorySlot` |
| 298 | C1:8E5B | C1:8EAD | 82 | `exact` | yes | `misc/take_item_from_character.asm` | `TAKE_ITEM_FROM_CHARACTER` | `SearchAndRemoveItemFromCharacterInventory` |
| 299 | C1:8EAD | C1:8F0E | 97 | `exact` | yes | `misc/reduce_hp_amtpercent.asm` | `` | `SearchAndRemoveItemFromActiveInventories` |
| 300 | C1:8F0E | C1:8F64 | 86 | `exact` | yes | `misc/recover_hp_amtpercent.asm` | `` | `DepleteHpForCharacterOrActiveParty` |
| 301 | C1:8F64 | C1:8FBA | 86 | `exact` | yes | `misc/reduce_pp_amtpercent.asm` | `` | `RecoverHpForCharacterOrActiveParty` |
| 302 | C1:8FBA | C1:9010 | 86 | `exact` | yes | `misc/recover_pp_amtpercent.asm` | `` | `DepletePpForCharacterOrActiveParty` |
| 303 | C1:9010 | C1:9066 | 86 | `exact` | yes | `misc/equip_item.asm` | `` | `RecoverPpForCharacterOrActiveParty` |
| 304 | C1:90E6 | C1:90F1 | 11 | `exact` | yes | `unknown/C1/C190E6.asm` | `` | `ReadActiveOverworldRegistryTypeCode` |
| 305 | C1:90F1 | C1:913D | 76 | `exact` | yes | `unknown/C1/C190F1.asm` | `` | `` |
| 306 | C1:913D | C1:9183 | 70 | `exact` | yes | `misc/escargo_express_store.asm` | `` | `EnqueuePendingItemId` |
| 307 | C1:9183 | C1:91B0 | 45 | `exact` | yes | `misc/escargo_express_move.asm` | `` | `StoreInventorySlotItemInPendingQueue` |
| 308 | C1:91B0 | C1:91F8 | 72 | `exact` | yes | `unknown/C1/C191B0.asm` | `` | `RemovePendingItemIdAtIndex` |
| 309 | C1:91F8 | C1:9216 | 30 | `exact` | yes | `unknown/C1/C191F8.asm` | `` | `WithdrawPendingItemToInventory` |
| 310 | C1:9216 | C1:9249 | 51 | `exact` | yes | `unknown/C1/C19216.asm` | `` | `PrintItemNameFromConfigurationTable` |
| 311 | C1:9249 | C1:931B | 210 | `exact` | yes | `unknown/C1/C19249.asm` | `` | `PrintStatisticSelectorValue` |
| 312 | C1:931B | C1:93E7 | 204 | `exact` | yes | `unknown/C1/C1931B.asm` | `` | `PrintPsiOrSmallDynamicLabel` |
| 313 | C1:93E7 | C1:9437 | 80 | `exact` | yes | `unknown/C1/C193E7.asm` | `` | `OpenTargetSelectionPromptLabel` |
| 314 | C1:9437 | C1:9441 | 10 | `exact` | yes | `unknown/C1/C19437.asm` | `` | `CloseTargetSelectionPromptLabel` |
| 315 | C1:9441 | C1:952F | 238 | `exact` | yes | `unknown/C1/C19441.asm` | `` | `` |
| 316 | C1:952F | C1:98DE | 943 | `exact` | yes | `unknown/C1/C1952F.asm` | `UNKNOWN_C1952F` | `` |
| 317 | C1:98DE | C1:9A11 | 307 | `exact` | yes | `misc/inventory_get_item_name.asm` | `` | `` |
| 318 | C1:9A11 | C1:9A43 | 50 | `exact` | yes | `unknown/C1/C19A11.asm` | `` | `RunSelectionHelperWithTemporaryFocus` |
| 319 | C1:9A43 | C1:9B4E | 267 | `exact` | yes | `unknown/C1/C19A43.asm` | `` | `BuildEscargoStorageSelectionMenu` |
| 320 | C1:9B4E | C1:9B79 | 43 | `exact` | yes | `text/set_hppp_window_mode_item.asm` | `SET_HPPP_WINDOW_MODE_ITEM` | `BuildEquipmentComparisonMarkersForItem` |
| 321 | C1:9CDD | C1:9D49 | 108 | `exact` | yes | `unknown/C1/C19CDD.asm` | `` | `InitializeEquipmentComparisonMarkersDefault` |
| 322 | C1:9D49 | C1:9DB5 | 108 | `exact` | yes | `unknown/C1/C19D49.asm` | `` | `PrepareEquipmentMenuStatusDisplay` |
| 323 | C1:9DB5 | C1:9EE6 | 305 | `exact` | yes | `unknown/C1/C19DB5.asm` | `` | `RunShopItemSelectionMenu` |
| 324 | C1:9EE6 | C1:9F29 | 67 | `exact` | yes | `misc/get_item_type.asm` | `` | `ClassifyItemCompactCategory` |
| 325 | C1:9F29 | C1:A1D8 | 687 | `exact` | yes | `unknown/C1/C19F29.asm` | `` | `RenderSelectedCharacterEquipmentList` |
| 326 | C1:A1D8 | C1:A778 | 1440 | `exact` | yes | `unknown/C1/C1A1D8.asm` | `UNKNOWN_C1A1D8` | `RenderEquipmentPreviewStatus` |
| 327 | C1:A778 | C1:A795 | 29 | `exact` | yes | `unknown/C1/C1A778.asm` | `UNKNOWN_C1A778` | `RefreshSelectedCharacterEquipmentDisplay` |
| 328 | C1:A795 | C1:AA18 | 643 | `exact` | yes | `unknown/C1/C1A795.asm` | `` | `RunCharacterEquipmentSlotSelectionLoop` |
| 329 | C1:AA18 | C1:AA5D | 69 | `exact` | yes | `unknown/C1/C1AA18.asm` | `` | `RefreshWalletOrStatusDisplay` |
| 330 | C1:AA5D | C1:AAFA | 157 | `exact` | yes | `unknown/C1/C1AA5D.asm` | `` | `RunPartyEquipmentMenuController` |
| 331 | C1:AAFA | C1:AC00 | 262 | `exact` | yes | `unknown/C1/C1AAFA.asm` | `` | `RunTeleportDestinationSelectionMenu` |
| 332 | C1:AC00 | C1:AC4A | 74 | `exact` | yes | `unknown/C1/C1AC00.asm` | `` | `OpenPhoneContactSelectionMenu` |
| 333 | C1:AC4A | C1:AC9B | 81 | `exact` | yes | `unknown/C1/C1AC4A.asm` | `` | `BuildBattleAttackerNameBuffer` |
| 334 | C1:AC9B | C1:ACA1 | 6 | `exact` | yes | `battle/return_battle_attacker_address.asm` | `` | `GetBattleAttackerNameBufferBase` |
| 335 | C1:ACA1 | C1:ACF2 | 81 | `exact` | yes | `unknown/C1/C1ACA1.asm` | `` | `BuildBattleTargetNameBuffer` |
| 336 | C1:ACF2 | C1:ACF8 | 6 | `exact` | yes | `battle/return_battle_target_address.asm` | `` | `GetBattleTargetNameBufferBase` |
| 337 | C1:ACF8 | C1:AD02 | 10 | `exact` | yes | `unknown/C1/C1ACF8.asm` | `` | `StageBattleTextSubstitutionByte` |
| 338 | C1:AD02 | C1:AD0A | 8 | `exact` | yes | `unknown/C1/C1AD02.asm` | `` | `ReadBattleTextSubstitutionByte` |
| 339 | C1:AD0A | C1:AD26 | 28 | `exact` | yes | `unknown/C1/C1AD0A.asm` | `` | `StageBattleTextSubstitutionPointer` |
| 340 | C1:AD26 | C1:AD42 | 28 | `exact` | yes | `unknown/C1/C1AD26.asm` | `` | `LoadBattleTextSubstitutionPointer` |
| 341 | C1:AD42 | C1:AD7D | 59 | `exact` | yes | `unknown/C1/C1AD42.asm` | `` | `GetFrontInteractionResultClass` |
| 342 | C1:AD7D | C1:ADB4 | 55 | `exact` | yes | `unknown/C1/C1AD7D.asm` | `` | `ReadOverworldPositionContextByte` |
| 343 | C1:ADB4 | C1:AF73 | 447 | `exact` | yes | `battle/determine_targetting.asm` | `` | `DetermineBattleTargetting` |
| 344 | C1:AF73 | C1:B2EC | 889 | `exact` | yes | `overworld/use_item.asm` | `` | `UseItemBattleOrFieldBridge` |
| 345 | C1:B5B6 | C1:B7C6 | 528 | `exact` | yes | `unknown/C1/C1B5B6.asm` | `` | `OpenBattlePsiUserSelection` |
| 346 | C1:BB06 | C1:BB71 | 107 | `exact` | yes | `unknown/C1/C1BB06.asm` | `UNKNOWN_C1BB06` | `FinalizeBattlePsiSelectionState` |
| 347 | C1:BB71 | C1:BCAB | 314 | `exact` | yes | `unknown/C1/C1BB71.asm` | `` | `OpenFieldPsiDestinationMenu` |
| 348 | C1:BCAB | C1:BE4D | 418 | `exact` | yes | `overworld/teleport.asm` | `` | `ExecuteTeleportDestination` |
| 349 | C1:BE4D | C1:BEC6 | 121 | `exact` | yes | `overworld/attempt_homesickness.asm` | `` | `AttemptHomesicknessResult` |
| 350 | C1:BEC6 | C1:BEFC | 54 | `exact` | yes | `overworld/get_off_bicycle.asm` | `GET_OFF_BICYCLE` | `RunGetOffBicycleMessageAndExit` |
| 351 | C1:BEFC | C1:C046 | 330 | `exact` | yes | `unknown/C1/C1BEFC.asm` | `` | `DispatchTextCommand1F41SpecialEvent` |
| 352 | C1:C046 | C1:C165 | 287 | `exact` | yes | `unknown/C1/C1C046.asm` | `` | `RefreshPsiMenuCursorCategory` |
| 353 | C1:C165 | C1:C1BA | 85 | `exact` | yes | `unknown/C1/C1C165.asm` | `` | `CurrentCharacterKnowsPsi` |
| 354 | C1:C1BA | C1:C32A | 368 | `exact` | yes | `unknown/C1/C1C1BA.asm` | `` | `HasPsiEntryForCategoryMask` |
| 355 | C1:C32A | C1:C367 | 61 | `exact` | yes | `unknown/C1/C1C32A.asm` | `` | `CanCharacterOpenPsiLane` |
| 356 | C1:C367 | C1:C373 | 12 | `exact` | yes | `unknown/C1/C1C367.asm` | `UNKNOWN_C1C367` | `CheckBattlePsiUserEligibility` |
| 357 | C1:C373 | C1:C3B6 | 67 | `exact` | yes | `unknown/C1/C1C373.asm` | `` | `FindFirstEligibleBattlePsiUser` |
| 358 | C1:C3B6 | C1:C403 | 77 | `exact` | yes | `unknown/C1/C1C3B6.asm` | `` | `CountEligibleBattlePsiUsers` |
| 359 | C1:C403 | C1:C452 | 79 | `exact` | yes | `text/get_psi_name.asm` | `` | `PrintPsiFamilyName` |
| 360 | C1:C452 | C1:C853 | 1025 | `exact` | yes | `battle/generate_psi_list.asm` | `` | `BuildSharedBattlePsiEntryList` |
| 361 | C1:C853 | C1:C8BC | 105 | `exact` | yes | `unknown/C1/C1C853.asm` | `UNKNOWN_C1C853` | `ResolveBattlePsiTargetingMetadata` |
| 362 | C1:C8BC | C1:CA06 | 330 | `exact` | yes | `unknown/C1/C1C8BC.asm` | `UNKNOWN_C1C8BC` | `FormatBattlePsiMenuEntryRow` |
| 363 | C1:CA06 | C1:CA72 | 108 | `exact` | yes | `unknown/C1/C1CA06.asm` | `` | `BuildPsiRankName` |
| 364 | C1:CA72 | C1:CAF5 | 131 | `exact` | yes | `unknown/C1/C1CA72.asm` | `` | `RefreshBattlePsiSelection` |
| 365 | C1:CAF5 | C1:CB7F | 138 | `exact` | yes | `unknown/C1/C1CAF5.asm` | `UNKNOWN_C1CAF5` | `BuildBattlePsiCategoryEntryList` |
| 366 | C1:CB7F | C1:CBCD | 78 | `exact` | yes | `unknown/C1/C1CB7F.asm` | `` | `HasBattlePsiCategoryEntries` |
| 367 | C1:CBCD | C1:CC39 | 108 | `exact` | yes | `battle/battle_psi_menu.asm` | `` | `OpenBattlePsiCategorySelectionStage` |
| 368 | C1:CE85 | C1:CFC6 | 321 | `exact` | yes | `unknown/C1/C1CE85.asm` | `` | `ResolveSelectedBattleItemAction` |
| 369 | C1:CFC6 | C1:D038 | 114 | `exact` | yes | `unknown/C1/C1CFC6.asm` | `` | `OpenBattleItemSelectionLoop` |
| 370 | C1:D038 | C1:D08B | 83 | `exact` | yes | `unknown/C1/C1D038.asm` | `` | `MapBrokenItemToRepairedItem` |
| 371 | C1:D08B | C1:D109 | 126 | `exact` | yes | `unknown/C1/C1D08B.asm` | `` | `ComputeLevelUpStatGrowthDelta` |
| 372 | C1:D109 | C1:D15B | 82 | `exact` | yes | `misc/level_up_char.asm` | `` | `LevelUpCharacterAndRefreshDerivedStats` |
| 373 | C1:D15B | C1:D204 | 169 | `exact` | yes | `misc/reset_char_level_one.asm` | `` | `BuildLevelUpTargetNameAndAnnouncement` |
| 374 | C1:D204 | C1:D28C | 136 | `exact` | yes | `misc/gain_exp.asm` | `GAIN_EXP` | `PrintOffenseGainMessage` |
| 375 | C1:D28C | C1:D31B | 143 | `exact` | yes | `misc/find_condiment.asm` | `FIND_CONDIMENT` | `PrintDefenseGainMessage` |
| 376 | C1:D31B | C1:D3A5 | 138 | `exact` | yes | `overworld/show_hp_alert.asm` | `SHOW_HP_ALERT` | `PrintSpeedGainMessage` |
| 377 | C1:D3A5 | C1:D48D | 232 | `exact` | yes | `text/display_in_battle_text.asm` | `DISPLAY_IN_BATTLE_TEXT` | `PrintGutsGainMessage` |
| 378 | C1:D48D | C1:D575 | 232 | `exact` | yes | `text/display_text_wait.asm` | `DISPLAY_TEXT_WAIT` | `PrintVitalityGainMessage` |
| 379 | C1:DCCB | C1:DD3B | 112 | `exact` | yes | `unknown/C1/C1DCCB.asm` | `UNKNOWN_C1DCCB` | `InitializePartyBattleStartState` |
| 380 | C1:DD3B | C1:DD41 | 6 | `exact` | yes | `text/show_hppp_windows_redirect.asm` | `` | `RedirectShowHpppWindows` |
| 381 | C1:DD41 | C1:DD47 | 6 | `exact` | yes | `text/hide_hppp_windows_redirect.asm` | `` | `RedirectHideHpppWindows` |
| 382 | C1:DD47 | C1:DD4D | 6 | `exact` | yes | `text/create_window_redirect.asm` | `` | `RedirectCreateWindow` |
| 383 | C1:DD4D | C1:DD53 | 6 | `exact` | yes | `text/set_window_focus_redirect.asm` | `` | `RedirectSetWindowFocus` |
| 384 | C1:DD53 | C1:DD59 | 6 | `exact` | yes | `unknown/C1/C10FA3_redirect.asm` | `` | `RedirectTextEntryHelper0FA3` |
| 385 | C1:DD59 | C1:DD5F | 6 | `exact` | yes | `text/close_focus_window_redirect.asm` | `` | `RedirectCloseFocusWindow` |
| 386 | C1:DD5F | C1:DD70 | 17 | `exact` | yes | `unknown/C1/C1DD5F.asm` | `UNKNOWN_C1DD5F` | `BattleDisplayCloseAndSyncWait` |
| 387 | C1:DD70 | C1:DD76 | 6 | `exact` | yes | `unknown/C1/C1AC4A_redirect.asm` | `` | `RedirectBuildBattleAttackerNameBuffer` |
| 388 | C1:DD76 | C1:DD7C | 6 | `exact` | yes | `unknown/C1/C1ACA1_redirect.asm` | `` | `RedirectBuildBattleTargetNameBuffer` |
| 389 | C1:DD7C | C1:DD82 | 6 | `exact` | yes | `unknown/C1/C1ACF8_redirect.asm` | `` | `RedirectStageBattleTextSubstitutionByte` |
| 390 | C1:DD82 | C1:DD9F | 29 | `exact` | yes | `unknown/C1/C1DD82.asm` | `UNKNOWN_C1DD82` | `StageBattleTextPointerSubstitutionOnly` |
| 391 | C1:DD9F | C1:DDC6 | 39 | `exact` | yes | `unknown/C1/C1DD9F.asm` | `UNKNOWN_C1DD9F` | `DisplayCurrentActionTableTextMode1` |
| 392 | C1:DDC6 | C1:DDCC | 6 | `exact` | yes | `misc/remove_item_from_inventory_redirect.asm` | `` | `RedirectRemoveItemFromInventory` |
| 393 | C1:DDCC | C1:DDD3 | 7 | `exact` | yes | `unknown/C4/C43573_redirect.asm` | `` | `RedirectC43573Helper` |
| 394 | C1:DDD3 | C1:DDDA | 7 | `exact` | yes | `unknown/C3/C3E6F8_redirect.asm` | `` | `RedirectC3E6F8Helper` |
| 395 | C1:DDDA | C1:E1A2 | 968 | `exact` | yes | `text/selection_menu_setup.asm` | `` | `BuildSelectionMenuSetupAndRedirects` |
| 396 | C1:E1A2 | C1:E1A5 | 3 | `exact` | yes | `text/print_menu_items_redirect.asm` | `` | `NullFarCallback` |
| 397 | C1:E1A5 | C1:E47F | 730 | `exact` | yes | `text/selection_menu_redirect.asm` | `` | `RunEnemySelectMode` |
| 398 | C1:E47F | C1:E48D | 14 | `exact` | yes | `unknown/C1/C1CFC6_redirect.asm` | `` | `ExitEnemySelectMode` |
| 399 | C1:E48D | C1:E4BE | 49 | `exact` | yes | `unknown/C1/C1242E_redirect.asm` | `` | `RenderSingleTextInputOptionRowScoped` |
| 400 | C1:E4BE | C1:E57F | 193 | `exact` | yes | `battle/battle_psi_menu_redirect.asm` | `` | `BuildTextInputOptionStrip` |
| 401 | C1:E57F | C1:EAA6 | 1319 | `exact` | yes | `battle/actions/switch_weapon.asm` | `` | `RunTextInputDialog` |
| 402 | C1:EAA6 | C1:EAD6 | 48 | `exact` | yes | `battle/actions/switch_armor.asm` | `` | `RunNameEntrySpecialEventPrelude` |
| 403 | C1:E1A2 | C1:E1A5 | 3 | `exact` | yes | `misc/null/C1E1A2.asm` | `NULL_C1E1A2` | `NullFarCallback` |
| 404 | C1:E1A5 | C1:E47F | 730 | `exact` | yes | `battle/enemy_select_mode.asm` | `ENEMY_SELECT_MODE` | `RunEnemySelectMode` |
| 405 | C1:E48D | C1:E4BE | 49 | `exact` | yes | `unknown/C1/C1E48D.asm` | `` | `RenderSingleTextInputOptionRowScoped` |
| 406 | C1:E4BE | C1:E57F | 193 | `exact` | yes | `unknown/C1/C1E4BE.asm` | `` | `BuildTextInputOptionStrip` |
| 407 | C1:E57F | C1:EAA6 | 1319 | `exact` | yes | `text/text_input_dialog.asm` | `` | `RunTextInputDialog` |
| 408 | C1:EAA6 | C1:EAD6 | 48 | `exact` | yes | `text/enter_your_name_please.asm` | `ENTER_YOUR_NAME_PLEASE` | `RunNameEntrySpecialEventPrelude` |
| 409 | C1:EAD6 | C1:EC04 | 302 | `exact` | yes | `intro/name_a_character.asm` | `` | `RunNamingBufferCommitFlow` |
| 410 | C1:EC8F | C1:ECD1 | 66 | `exact` | yes | `unknown/C1/C1EC8F.asm` | `UNKNOWN_C1EC8F` | `PreviewWindowFlavourAndRedraw` |
| 411 | C1:ECD1 | C1:ECDC | 11 | `exact` | yes | `unknown/C1/C1ECD1.asm` | `UNKNOWN_C1ECD1` | `PreviewPackedHighByteWindowFlavour` |
| 412 | C1:ECDC | C1:ED5B | 127 | `exact` | yes | `system/saves/corruption_check.asm` | `` | `ShowCorruptSaveFilesNotice` |
| 413 | C1:ED5B | C1:F03E | 739 | `exact` | yes | `intro/file_select_menu.asm` | `` | `OpenFileSelectSlotChoiceMenu` |
| 414 | C1:F07E | C1:F14F | 209 | `exact` | yes | `unknown/C1/C1F07E.asm` | `` | `OpenFileSelectActionMenu` |
| 415 | C1:F14F | C1:F2A8 | 345 | `exact` | yes | `unknown/C1/C1F14F.asm` | `` | `OpenCopyDestinationMenu` |
| 416 | C1:F2A8 | C1:F3C2 | 282 | `exact` | yes | `unknown/C1/C1F2A8.asm` | `` | `OpenDeleteFileConfirmationMenu` |
| 417 | C1:F3C2 | C1:F497 | 213 | `exact` | yes | `intro/file_select/open_text_speed_menu.asm` | `OPEN_TEXT_SPEED_MENU` | `OpenTextSpeedMenu` |
| 418 | C1:F497 | C1:F568 | 209 | `exact` | yes | `unknown/C1/C1F497.asm` | `UNKNOWN_C1F497` | `OpenOrRefreshTextSpeedSelection` |
| 419 | C1:F568 | C1:F616 | 174 | `exact` | yes | `intro/file_select/open_sound_menu.asm` | `` | `OpenSoundSettingMenu` |
| 420 | C1:F616 | C1:F6E3 | 205 | `exact` | yes | `unknown/C1/C1F616.asm` | `` | `OpenOrRefreshSoundSettingSelection` |
| 421 | C1:F6E3 | C1:F805 | 290 | `exact` | yes | `intro/file_select/open_flavour_menu.asm` | `` | `OpenOrRefreshWindowFlavourSelection` |
| 422 | C1:F805 | C1:FF2C | 1831 | `exact` | yes | `intro/file_select_menu_loop.asm` | `` | `RunFileSelectMenuLoop` |
| 423 | C1:FF2C | C1:FF6B | 63 | `exact` | yes | `unknown/C1/C1FF2C.asm` | `` | `UpdateLeadEntityTypeRedrawFlag` |
| 424 | C1:FF6B | C1:FF99 | 46 | `exact` | yes | `unknown/C1/C1FF6B.asm` | `UNKNOWN_C1FF6B` | `RunFileSelectSession` |
| 425 | C1:FF99 | C1:FFD3 | 58 | `exact` | yes | `unknown/C1/C1FF99.asm` | `UNKNOWN_C1FF99` | `ComputeCenteredTextLayoutMetric` |
| 426 | C1:FFD3 | C1:FFEF | 28 | `exact` | yes | `system/antipiracy/sram_check_routine_checksum.asm` | `SRAM_CHECK_ROUTINE_CHECKSUM` | `ComputeBankC1ChecksumTail` |
