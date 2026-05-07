# C3 actionscript semantics audit

Generated from `notes/c3-source-data-map.md` via `tools/build_c3_actionscript_semantics_audit.py`. This report is the first semantic frontier for C3 event/actionscript payloads after byte-equivalent source-bank closure.

## Summary

- schema: `earthbound-decomp.c3-actionscript-semantics-audit.v1`
- script rows audited: `181`
- by extraction class: `{'event-bytecode-asset': 41, 'event-bytecode-label': 35, 'event-script-asset': 105}`
- by decode status: `{'complete': 181}`
- native callback contract seeds: `86`
- installed callback target seeds: `17`
- decode bounds: `120` instructions, `0x400` bytes per row unless the source-map row is shorter

## Top opcode and target signals

- top first opcodes: `{'$42 EVENT_CALLROUTINE': 50, '$06 EVENT_PAUSE': 36, '$25 EVENT_SET_PHYSICS_CALLBACK': 24, '$1A EVENT_SHORTCALL': 14, '$0E EVENT_SET_VAR': 9, '$20 EVENT_WRITE_VAR_TO_TEMPVAR': 5, '$3B EVENT_SET_ANIMATION': 5, '$01 EVENT_LOOP': 5, '$23 EVENT_SET_POSITION_CHANGE_CALLBACK': 4, '$28 EVENT_SET_X': 3, '$07 EVENT_START_TASK': 3, '$40 EVENT_SET_Y_VELOCITY': 2}`
- top native callback targets: `{'C0:A4BF': 29, 'C0:A685': 27, 'C0:A4B2': 26, 'C0:A4A8': 23, 'C0:AA6E': 17, 'C4:6E46': 12, 'C0:A65F': 10, 'C4:0015': 8, 'C0:9F82': 7, 'C0:20F1': 7, 'C0:A88D': 6, 'C0:C6B6': 6, 'C0:A864': 5, 'EF:0FF6': 5, 'C0:A82F': 4, 'C0:A841': 4}`
- top installed callback targets: `{'C0:A37A': 17, 'C0:9FC8': 7, 'C0:A360': 5, 'C0:A039': 5, 'C4:8BE1': 4, 'C0:9FF0': 4, 'C4:8C2B': 2, 'C0:9FF1': 2, 'C0:5200': 2, 'C4:8C02': 2, 'C0:A055': 1, 'C0:A0A0': 1, 'C0:A384': 1, 'C0:A26B': 1, 'C0:4D78': 1, 'C0:D7F7': 1}`
- callback semantic groups: `{'current-slot-state': 13, 'movement': 12, 'visual-profile': 10, 'timed-delivery': 9, 'overworld-runtime': 7, 'presentation-render': 7, 'text-presentation': 5, 'neighbor-cache': 5, 'collision': 5, 'proximity-gate': 3, 'event-flag': 2, 'battle-runtime': 2, 'world-state-restore': 2, 'entity-spawn': 1, 'party-facing': 1, 'intro-integrity': 1, 'other': 1}`
- installed callback semantic groups: `{'movement': 7, 'presentation-render': 7, 'overworld-runtime': 2, 'current-slot-state': 1}`
- unknown callback targets: `{}`
- top C3 script targets: `{'C3:AB59': 19, 'C3:A204': 19, 'C3:A111': 7, 'C3:AA38': 5, 'C3:A262': 5, 'C3:A0FE': 5, 'C3:AA1E': 5, 'C3:AB8A': 4, 'C3:A1F3': 4, 'C3:A11E': 4, 'C3:A3B7': 4, 'C3:A09F': 3, 'C3:AB44': 3, 'C3:0295': 3, 'C3:43DB': 3, 'C3:443E': 3}`

## Frontier rows

No syntactic decode frontiers at the current bounds.

## Opcode operand catalog

| Opcode | Name | Byte shape | Semantic fields | Role | Confidence |
| --- | --- | --- | --- | --- | --- |
| `$00` | `EVENT_END` | - | - | `terminal` | `high` |
| `$01` | `EVENT_LOOP` | `byte` | `count` | `loop control` | `high` |
| `$02` | `EVENT_LOOP_END` | - | - | `loop control` | `high` |
| `$03` | `EVENT_LONGJUMP` | `ptr3` | `jump_target` | `terminal` | `high` |
| `$04` | `EVENT_LONGCALL` | `ptr3` | `call_target` | `script call` | `high` |
| `$05` | `EVENT_LONG_RETURN` | - | - | `terminal` | `high` |
| `$06` | `EVENT_PAUSE` | `byte` | `frames` | `state/operand` | `high` |
| `$07` | `EVENT_START_TASK` | `shortptr` | `task_script` | `task control` | `high` |
| `$08` | `EVENT_SET_TICK_CALLBACK` | `ptr3` | `tick_callback` | `callback binding` | `high` |
| `$09` | `EVENT_HALT` | - | - | `terminal` | `high` |
| `$0A` | `EVENT_SHORTCALL_CONDITIONAL` | `shortptr` | `conditional_call_target` | `script call` | `high` |
| `$0B` | `EVENT_SHORTCALL_CONDITIONAL_NOT` | `shortptr` | `inverted_conditional_call_target` | `script call` | `high` |
| `$0C` | `EVENT_END_TASK` | - | - | `terminal` | `high` |
| `$0E` | `EVENT_SET_VAR` | `byte`, `word` | `script_var`, `value_word` | `state/operand` | `high` |
| `$0F` | `EVENT_CLEAR_TICK_CALLBACK` | - | - | `callback binding` | `high` |
| `$10` | `EVENT_SWITCH_JUMP_TEMPVAR` | `wordlist` | `switch_jump_targets` | `branch` | `high` |
| `$11` | `EVENT_SWITCH_CALL_TEMPVAR` | `wordlist` | `switch_call_targets` | `script call` | `high` |
| `$12` | `EVENT_WRITE_BYTE_WRAM` | `word`, `byte` | `wram_addr`, `value_byte` | `state/operand` | `high` |
| `$13` | `EVENT_END_LAST_TASK` | - | - | `task control` | `high` |
| `$14` | `EVENT_BINOP` | `byte`, `byte`, `word` | `script_var`, `operation_byte`, `value_word` | `state/operand` | `high` |
| `$15` | `EVENT_WRITE_WORD_WRAM` | `word`, `word` | `wram_addr`, `value_word` | `state/operand` | `high` |
| `$16` | `EVENT_BREAK_IF_FALSE` | `shortptr` | `break_target` | `branch` | `high` |
| `$17` | `EVENT_BREAK_IF_TRUE` | `shortptr` | `break_target` | `branch` | `high` |
| `$18` | `EVENT_BINOP_WRAM` | `word`, `byte`, `byte` | `wram_addr`, `operation_byte`, `script_var` | `state/operand` | `high` |
| `$19` | `EVENT_SHORTJUMP` | `shortptr` | `jump_target` | `terminal` | `high` |
| `$1A` | `EVENT_SHORTCALL` | `shortptr` | `call_target` | `script call` | `high` |
| `$1B` | `EVENT_SHORT_RETURN` | - | - | `terminal` | `high` |
| `$1C` | `EVENT_SET_ANIMATION_POINTER` | `ptr3` | `animation_pointer` | `state/operand` | `high` |
| `$1D` | `EVENT_WRITE_WORD_TEMPVAR` | `word` | `value_word` | `state/operand` | `high` |
| `$1E` | `EVENT_WRITE_WRAM_TEMPVAR` | `word` | `wram_addr` | `state/operand` | `high` |
| `$1F` | `EVENT_WRITE_TEMPVAR_TO_VAR` | `byte` | `script_var` | `state/operand` | `high` |
| `$20` | `EVENT_WRITE_VAR_TO_TEMPVAR` | `byte` | `script_var` | `state/operand` | `high` |
| `$21` | `EVENT_WRITE_VAR_TO_WAIT_TIMER` | `byte` | `script_var` | `state/operand` | `high` |
| `$22` | `EVENT_SET_DRAW_CALLBACK` | `callbackptr` | `draw_callback` | `callback binding` | `high` |
| `$23` | `EVENT_SET_POSITION_CHANGE_CALLBACK` | `callbackptr` | `position_change_callback` | `callback binding` | `high` |
| `$24` | `EVENT_LOOP_TEMPVAR` | - | - | `loop control` | `high` |
| `$25` | `EVENT_SET_PHYSICS_CALLBACK` | `callbackptr` | `physics_callback` | `callback binding` | `high` |
| `$26` | `EVENT_SET_ANIMATION_FRAME_VAR` | `byte` | `script_var` | `state/operand` | `high` |
| `$27` | `EVENT_BINOP_TEMPVAR` | `byte`, `word` | `operation_byte`, `value_word` | `state/operand` | `high` |
| `$28` | `EVENT_SET_X` | `word` | `x_word` | `state/operand` | `high` |
| `$29` | `EVENT_SET_Y` | `word` | `y_word` | `state/operand` | `high` |
| `$2A` | `EVENT_SET_Z` | `word` | `z_word` | `state/operand` | `high` |
| `$2B` | `EVENT_SET_X_RELATIVE` | `word` | `x_delta_word` | `state/operand` | `high` |
| `$2C` | `EVENT_SET_Y_RELATIVE` | `word` | `y_delta_word` | `state/operand` | `high` |
| `$2D` | `EVENT_SET_Z_RELATIVE` | `word` | `z_delta_word` | `state/operand` | `high` |
| `$2E` | `EVENT_SET_X_VELOCITY_RELATIVE` | `word` | `x_velocity_delta_word` | `state/operand` | `high` |
| `$2F` | `EVENT_SET_Y_VELOCITY_RELATIVE` | `word` | `y_velocity_delta_word` | `state/operand` | `high` |
| `$30` | `EVENT_SET_Z_VELOCITY_RELATIVE` | `word` | `z_velocity_delta_word` | `state/operand` | `high` |
| `$39` | `EVENT_SET_VELOCITIES_ZERO` | - | - | `state/operand` | `high` |
| `$3B` | `EVENT_SET_ANIMATION` | `byte` | `animation_id` | `state/operand` | `high` |
| `$3C` | `EVENT_NEXT_ANIMATION_FRAME` | - | - | `state/operand` | `high` |
| `$3D` | `EVENT_PREV_ANIMATION_FRAME` | - | - | `state/operand` | `high` |
| `$3E` | `EVENT_SKIP_N_ANIMATION_FRAMES` | `byte` | `frame_count` | `state/operand` | `high` |
| `$3F` | `EVENT_SET_X_VELOCITY` | `word` | `x_velocity_word` | `state/operand` | `high` |
| `$40` | `EVENT_SET_Y_VELOCITY` | `word` | `y_velocity_word` | `state/operand` | `high` |
| `$41` | `EVENT_SET_Z_VELOCITY` | `word` | `z_velocity_word` | `state/operand` | `high` |
| `$42` | `EVENT_CALLROUTINE` | `callroutine` | - | `state/operand` | `high` |
| `$43` | `EVENT_SET_PRIORITY` | `byte` | `priority` | `state/operand` | `high` |
| `$44` | `EVENT_WRITE_TEMPVAR_WAITTIMER` | - | - | `state/operand` | `high` |

## Operand value seed catalog

These names are source-pilot readability seeds from recurring decoded C3 actionscript values. Direction-word names are promoted only at callback boundaries where the tempvar or random-choice result reaches the direction/vector runtime helpers.

### Animation IDs

| Value | Name | Decode count | Contract |
| --- | --- | ---: | --- |
| `$00` | `animation_frame0` | 62 | default/first script animation frame selector; often alternated with $01 for pulses |
| `$01` | `animation_frame1` | 32 | alternate/second script animation frame selector; often paired with $00 |
| `$FF` | `animation_hidden_or_off` | 10 | sentinel/off-frame animation selector used by blink or disappearance-style pulses |

### Visual countdown state bytes

| Value | Name | Decode count | Contract |
| --- | --- | ---: | --- |
| `$00` | `visual_state_00` | 12 | visual-state byte $00 stored to current slot $2AF6 by C0:AA6E before the C0:A4C4/C0:A794 visual-profile refresh path; exact profile-frame meaning remains local-unknown |
| `$01` | `visual_state_01` | 1 | visual-state byte $01 stored to current slot $2AF6 by C0:AA6E before the C0:A4C4/C0:A794 visual-profile refresh path; exact profile-frame meaning remains local-unknown |
| `$02` | `visual_state_02` | 15 | visual-state byte $02 stored to current slot $2AF6 by C0:AA6E before the C0:A4C4/C0:A794 visual-profile refresh path; exact profile-frame meaning remains local-unknown |
| `$03` | `visual_state_03` | 1 | visual-state byte $03 stored to current slot $2AF6 by C0:AA6E before the C0:A4C4/C0:A794 visual-profile refresh path; exact profile-frame meaning remains local-unknown |
| `$04` | `visual_state_04` | 16 | visual-state byte $04 stored to current slot $2AF6 by C0:AA6E before the C0:A4C4/C0:A794 visual-profile refresh path; exact profile-frame meaning remains local-unknown |
| `$05` | `visual_state_05` | 1 | visual-state byte $05 stored to current slot $2AF6 by C0:AA6E before the C0:A4C4/C0:A794 visual-profile refresh path; exact profile-frame meaning remains local-unknown |
| `$06` | `visual_state_06` | 19 | visual-state byte $06 stored to current slot $2AF6 by C0:AA6E before the C0:A4C4/C0:A794 visual-profile refresh path; exact profile-frame meaning remains local-unknown |
| `$07` | `visual_state_07` | 1 | visual-state byte $07 stored to current slot $2AF6 by C0:AA6E before the C0:A4C4/C0:A794 visual-profile refresh path; exact profile-frame meaning remains local-unknown |

### Visual countdown seed bytes

| Value | Name | Decode count | Contract |
| --- | --- | ---: | --- |
| `$00` | `visual_countdown_seed_00` | 40 | visual countdown seed byte $00 read by C0:AA6E; zero-visual path writes it raw to $10F2/$2892, existing-visual path doubles it into $10F2 and records the slot in $2896 |
| `$01` | `visual_countdown_seed_01` | 26 | visual countdown seed byte $01 read by C0:AA6E; zero-visual path writes it raw to $10F2/$2892, existing-visual path doubles it into $10F2 and records the slot in $2896 |

### Field $2B32 movement words

| Value | Name | Observed count | Contract |
| --- | --- | ---: | --- |
| `$0040` | `field2b32_step_0040` | 2 | small movement/vector magnitude written to current slot $2B32; boundary-audited through movement/timer consumers |
| `$0060` | `field2b32_step_0060` | 1 | observed movement/vector magnitude written to current slot $2B32; boundary-audited through movement/timer consumers |
| `$0080` | `field2b32_step_0080` | 1 | observed movement/vector magnitude written to current slot $2B32; boundary-audited through movement/timer consumers |
| `$00C0` | `field2b32_step_00c0` | 2 | observed movement/vector magnitude written to current slot $2B32; boundary-audited through movement/timer consumers |
| `$0100` | `field2b32_step_0100` | 12 | standard movement/vector magnitude written to current slot $2B32; boundary-audited through movement/timer consumers |
| `$0140` | `field2b32_step_0140` | 1 | observed movement/vector magnitude written to current slot $2B32; boundary-audited through movement/timer consumers |
| `$0160` | `field2b32_step_0160` | 2 | larger movement/vector magnitude written to current slot $2B32; boundary-audited through movement/timer consumers |
| `$0180` | `field2b32_step_0180` | 2 | observed movement/vector magnitude written to current slot $2B32; boundary-audited through movement/timer consumers |
| `$0200` | `field2b32_step_0200` | 2 | large movement/vector magnitude written to current slot $2B32; boundary-audited through movement/timer consumers |
| `$0280` | `field2b32_step_0280` | 1 | observed movement/vector magnitude written to current slot $2B32; boundary-audited through movement/timer consumers |
| `$0600` | `field2b32_step_0600` | 2 | very large movement/vector magnitude written to current slot $2B32; boundary-audited through movement/timer consumers |

### Field $2B32 movement boundary evidence

`C0:A685` writes the inline `field2b32_word` into current-slot `$2B32`. The C0 movement-vector note shows `C0:C83B` deriving signed vector words from `$2B32`; timer wrappers such as `C0:A6A2`/`C0:A6AD` and direct `C0:CA4E`/`C0:CBD3` calls then consume the active vector or speed scale. The table records decoded C3 `$2B32` writes that reach one of those movement/timer consumers inside the same source-map span.

- boundary-confirmed producers: `11`
- value coverage: `{'$0100': 4, '$0200': 2, '$0180': 2, '$0040': 1, '$0140': 1, '$0080': 1}`
- consumer coverage: `{'C0:C83B': 6, 'C0:A6AD': 5, 'C0:CA4E': 3}`

| Producer | Value | Consumers | Rows |
| --- | --- | --- | --- |
| `C3:9B42` | `$0040 <field2b32_step_0040>` | `C0:C83B InstallScriptMovementVectorFromDirection`, `C0:CA4E SetMovementTaskTimerFromActiveVector` | `C3:9AC7` |
| `C3:A2F7` | `$0100 <field2b32_step_0100>` | `C0:C83B InstallScriptMovementVectorFromDirection`, `C0:CA4E SetMovementTaskTimerFromActiveVector` | `C3:A204 ReleaseCurrentVisualEntityAndEnd`, `C3:A22C Var0AnimationCase0Pulse8FrameOn`, +6 |
| `C3:A3B0` | `$0100 <field2b32_step_0100>` | `C0:C83B InstallScriptMovementVectorFromDirection`, `C0:CA4E SetMovementTaskTimerFromActiveVector` | `C3:A23D Var0AnimationCase2Pulse4Frame`, `C3:A24E Var0AnimationCase3Pulse32Frame`, +5 |
| `C3:A494` | `$0200 <field2b32_step_0200>` | `C0:A6AD Script_SetMovementStateCBD3` | `C3:A381 InitRandomWanderMovementWithCollisionProbe`, `C3:A3A1 InitC40015PulseWithCollisionProbe`, +11 |
| `C3:A4D3` | `$0200 <field2b32_step_0200>` | `C0:A6AD Script_SetMovementStateCBD3` | `C3:A3B7 LoopRandomDirectionMovementWithRandomWait`, `C3:A3C9 ChooseRandomCardinalDirection`, +9 |
| `C3:A553` | `$0100 <field2b32_step_0100>` | `C0:A6AD Script_SetMovementStateCBD3` | `C3:A3E7 SetMovementTimerThenRandomWait`, `C3:A401 InitNpcAttentionPathIfNoCachedNeighbor`, +6 |
| `C3:A5A6` | `$0180 <field2b32_step_0180>` | `C0:A6AD Script_SetMovementStateCBD3` | `C3:A434 LoopNpcAttentionTerrainCollision`, `C3:A448 LoopNpcAttentionHorizontalCollision`, +2 |
| `C3:A5D3` | `$0180 <field2b32_step_0180>` | `C0:A6AD Script_SetMovementStateCBD3` | `C3:A47C ReleaseCurrentVisualEntityTail` |
| `C3:B795` | `$0140 <field2b32_step_0140>` | `C0:C83B InstallScriptMovementVectorFromDirection` | `C3:B70C` |
| `C3:BBA0` | `$0100 <field2b32_step_0100>` | `C0:C83B InstallScriptMovementVectorFromDirection` | `C3:BB73` |
| `C3:CF5C` | `$0080 <field2b32_step_0080>` | `C0:C83B InstallScriptMovementVectorFromDirection` | `C3:CEB9` |

### Direction-class word candidates

| Value | Name | Tempvar decode count | Contract |
| --- | --- | ---: | --- |
| `$0000` | `direction_down` | 3 | down/south-facing direction class word, runtime-backed by C0:A65F/C0:C83B callback-boundary evidence |
| `$0002` | `direction_right` | 3 | right/east-facing direction class word, runtime-backed by C0:A65F/C0:C83B callback-boundary evidence |
| `$0004` | `direction_up` | 6 | up/north-facing direction class word, runtime-backed by C0:A65F/C0:C83B callback-boundary evidence |
| `$0006` | `direction_left` | 6 | left/west-facing direction class word, runtime-backed by C0:A65F/C0:C83B callback-boundary evidence |

### Direction callback boundary evidence

C3 direction-class words are backed by the runtime chain documented around `C0:A65F` and `C0:C83B`: `C0:A65F` stores the active direction/class in `$2AF6[current]` and returns it, while `C0:C83B` stores the direction/mode in `$1A86[current]` and derives signed movement vector words from it. The table below records decoded C3 producers that reach those consumers inside the same source-map span.

- boundary-confirmed producers: `141`
- value coverage: `{'$0004': 63, '$0006': 42, '$0002': 26, '$0000': 25}`
- consumer coverage: `{'C0:A65F': 141, 'C0:C83B': 7}`

| Producer | Source | Values | Consumers | Rows |
| --- | --- | --- | --- | --- |
| `C3:9B4C` | `C0:9F82 choices` | `$0000 <direction_down>`, `$0002 <direction_right>`, `$0004 <direction_up>`, `$0006 <direction_left>` | `C0:A65F SetCurrentSlotDirectionClassIfActive`, `C0:C83B InstallScriptMovementVectorFromDirection` | `C3:9AC7` |
| `C3:A301` | `C0:9F82 choices` | `$0000 <direction_down>`, `$0002 <direction_right>`, `$0004 <direction_up>`, `$0006 <direction_left>` | `C0:A65F SetCurrentSlotDirectionClassIfActive`, `C0:C83B InstallScriptMovementVectorFromDirection` | `C3:A204 ReleaseCurrentVisualEntityAndEnd`, `C3:A22C Var0AnimationCase0Pulse8FrameOn`, +6 |
| `C3:A3C9` | `C0:9F82 choices` | `$0000 <direction_down>`, `$0002 <direction_right>`, `$0004 <direction_up>`, `$0006 <direction_left>` | `C0:A65F SetCurrentSlotDirectionClassIfActive`, `C0:C83B InstallScriptMovementVectorFromDirection` | `C3:A234 Var0AnimationCase1Pulse8FrameOff`, `C3:A23D Var0AnimationCase2Pulse4Frame`, +8 |
| `C3:ABAC` | `C0:9F82 choices` | `$0000 <direction_down>`, `$0002 <direction_right>`, `$0004 <direction_up>`, `$0006 <direction_left>` | `C0:A65F SetCurrentSlotDirectionClassIfActive`, `C0:C83B InstallScriptMovementVectorFromDirection` | `C3:AB9E` |
| `C3:B79B` | `EVENT_WRITE_WORD_TEMPVAR` | `$0004 <direction_up>` | `C0:A65F SetCurrentSlotDirectionClassIfActive`, `C0:C83B InstallScriptMovementVectorFromDirection` | `C3:B70C` |
| `C3:B7A8` | `EVENT_WRITE_WORD_TEMPVAR` | `$0002 <direction_right>` | `C0:A65F SetCurrentSlotDirectionClassIfActive`, `C0:C83B InstallScriptMovementVectorFromDirection` | `C3:B70C` |
| `C3:CF62` | `EVENT_WRITE_WORD_TEMPVAR` | `$0004 <direction_up>` | `C0:A65F SetCurrentSlotDirectionClassIfActive`, `C0:C83B InstallScriptMovementVectorFromDirection` | `C3:CEB9` |
| `C3:0426` | `EVENT_WRITE_WORD_TEMPVAR` | `$0006 <direction_left>` | `C0:A65F SetCurrentSlotDirectionClassIfActive` | `C3:0295 MoveActiveEntityLeftToScriptVarsAndWait` |
| `C3:1F13` | `EVENT_WRITE_WORD_TEMPVAR` | `$0004 <direction_up>` | `C0:A65F SetCurrentSlotDirectionClassIfActive` | `C3:1EEF` |
| `C3:1F44` | `EVENT_WRITE_WORD_TEMPVAR` | `$0004 <direction_up>` | `C0:A65F SetCurrentSlotDirectionClassIfActive` | `C3:1EEF` |
| `C3:1F75` | `EVENT_WRITE_WORD_TEMPVAR` | `$0004 <direction_up>` | `C0:A65F SetCurrentSlotDirectionClassIfActive` | `C3:1EEF` |
| `C3:1FA6` | `EVENT_WRITE_WORD_TEMPVAR` | `$0004 <direction_up>` | `C0:A65F SetCurrentSlotDirectionClassIfActive` | `C3:1EEF` |
| `C3:225A` | `EVENT_WRITE_WORD_TEMPVAR` | `$0002 <direction_right>` | `C0:A65F SetCurrentSlotDirectionClassIfActive` | `C3:2138` |
| `C3:2271` | `EVENT_WRITE_WORD_TEMPVAR` | `$0000 <direction_down>` | `C0:A65F SetCurrentSlotDirectionClassIfActive` | `C3:2138` |
| `C3:2288` | `EVENT_WRITE_WORD_TEMPVAR` | `$0006 <direction_left>` | `C0:A65F SetCurrentSlotDirectionClassIfActive` | `C3:2138` |
| `C3:2D0E` | `EVENT_WRITE_WORD_TEMPVAR` | `$0004 <direction_up>` | `C0:A65F SetCurrentSlotDirectionClassIfActive` | `C3:2CD2` |
| `C3:2D2B` | `EVENT_WRITE_WORD_TEMPVAR` | `$0006 <direction_left>` | `C0:A65F SetCurrentSlotDirectionClassIfActive` | `C3:2CD2` |
| `C3:2D39` | `EVENT_WRITE_WORD_TEMPVAR` | `$0004 <direction_up>` | `C0:A65F SetCurrentSlotDirectionClassIfActive` | `C3:2CD2` |
| `C3:2D59` | `EVENT_WRITE_WORD_TEMPVAR` | `$0006 <direction_left>` | `C0:A65F SetCurrentSlotDirectionClassIfActive` | `C3:2CD2` |
| `C3:2D66` | `EVENT_WRITE_WORD_TEMPVAR` | `$0004 <direction_up>` | `C0:A65F SetCurrentSlotDirectionClassIfActive` | `C3:2CD2` |
| `C3:2D83` | `EVENT_WRITE_WORD_TEMPVAR` | `$0006 <direction_left>` | `C0:A65F SetCurrentSlotDirectionClassIfActive` | `C3:2CD2` |
| `C3:2D90` | `EVENT_WRITE_WORD_TEMPVAR` | `$0004 <direction_up>` | `C0:A65F SetCurrentSlotDirectionClassIfActive` | `C3:2CD2` |
| `C3:2DA7` | `EVENT_WRITE_WORD_TEMPVAR` | `$0006 <direction_left>` | `C0:A65F SetCurrentSlotDirectionClassIfActive` | `C3:2CD2` |
| `C3:2DB4` | `EVENT_WRITE_WORD_TEMPVAR` | `$0000 <direction_down>` | `C0:A65F SetCurrentSlotDirectionClassIfActive` | `C3:2CD2` |
| `C3:2DC1` | `EVENT_WRITE_WORD_TEMPVAR` | `$0002 <direction_right>` | `C0:A65F SetCurrentSlotDirectionClassIfActive` | `C3:2CD2` |
| `C3:2DCE` | `EVENT_WRITE_WORD_TEMPVAR` | `$0004 <direction_up>` | `C0:A65F SetCurrentSlotDirectionClassIfActive` | `C3:2CD2` |
| `C3:2DDB` | `EVENT_WRITE_WORD_TEMPVAR` | `$0006 <direction_left>` | `C0:A65F SetCurrentSlotDirectionClassIfActive` | `C3:2CD2` |
| `C3:2DE8` | `EVENT_WRITE_WORD_TEMPVAR` | `$0004 <direction_up>` | `C0:A65F SetCurrentSlotDirectionClassIfActive` | `C3:2CD2` |
| `C3:34DF` | `EVENT_WRITE_WORD_TEMPVAR` | `$0002 <direction_right>` | `C0:A65F SetCurrentSlotDirectionClassIfActive` | `C3:33DD` |
| `C3:3C58` | `C0:9F82 choices` | `$0000 <direction_down>`, `$0002 <direction_right>`, `$0004 <direction_up>`, `$0006 <direction_left>` | `C0:A65F SetCurrentSlotDirectionClassIfActive` | `C3:3C1D` |
| `C3:3DE9` | `EVENT_WRITE_WORD_TEMPVAR` | `$0004 <direction_up>` | `C0:A65F SetCurrentSlotDirectionClassIfActive` | `C3:3DBE` |
| `...` | `summary` | - | - | `110` additional boundary-confirmed producer(s) in JSON output |

## Native callback contract seed

| Target | Preferred name | Group | Calls | Arg bytes | Args | Contract | Status |
| --- | --- | --- | ---: | ---: | --- | --- | --- |
| `C0:A4BF` | `RefreshCurrentSlotVisualProfile_Mode0` | `visual-profile` | 29 | 0 | `-` | force current slot visual profile refresh | `byte-count-known` |
| `C0:A685` | `Script_SetCurrentSlotField2B32` | `current-slot-state` | 27 | 2 | `field2b32_word` | read one script word and store it to current slot field $2B32 | `byte-count-known` |
| `C0:A4B2` | `RefreshCurrentSlotVisualProfile_Mode1IfAligned` | `visual-profile` | 26 | 0 | `-` | refresh current slot alternate visual profile when alignment allows | `byte-count-known` |
| `C0:A4A8` | `RefreshCurrentSlotVisualProfile_Mode0IfAligned` | `visual-profile` | 23 | 0 | `-` | refresh current slot visual profile when alignment allows | `byte-count-known` |
| `C0:AA6E` | `Script_ApplyCurrentSlotVisualCountdownState` | `visual-profile` | 17 | 2 | `visual_state_byte, countdown_byte` | read countdown/state bytes and apply current slot visual countdown state | `byte-count-known` |
| `C4:6E46` | `SetYieldToTextLatch9641` | `text-presentation` | 12 | 0 | `-` | set the yield-to-text latch used by event presentation handoff | `byte-count-known` |
| `C0:A65F` | `SetCurrentSlotDirectionClassIfActive` | `movement` | 10 | 0 | `-` | copy the tempvar direction/class into the current slot when the slot is active | `byte-count-known` |
| `C4:0015` | `ClearCurrentSlot10f2RefreshVisualAndCheckLiveArea` | `visual-profile` | 8 | 0 | `-` | clear current slot $10F2, refresh visual state, and test live-area status | `byte-count-known` |
| `C0:9F82` | `ChooseRandomScriptWord` | `overworld-runtime` | 7 | 0 | `choice_count_byte, choice_words[]` | read an inline choice count followed by that many words, choose one at random, and leave it in the tempvar/result latch | `byte-count-known` |
| `C0:20F1` | `ScriptRelease_CurrentEntityVisualState` | `visual-profile` | 7 | 0 | `-` | release the current entity/visual slot state at the end of a script-controlled actor sequence | `byte-count-known` |
| `C0:A88D` | `ActionScript_QueueTextPointer` | `text-presentation` | 6 | 4 | `text_pointer_low_word, text_pointer_bank_word` | read two script words as text pointer pieces and queue text record type #$0008 | `byte-count-known` |
| `C0:C6B6` | `CheckCurrentSlotInsideLiveAreaWindow` | `proximity-gate` | 6 | 0 | `-` | test whether the current slot is inside the live-area/window bounds used by event scripts | `byte-count-known` |
| `C0:A864` | `Script_CopyRegistrySlotAnchorToCurrentSlot_ReadByte` | `current-slot-state` | 5 | 1 | `registry_slot_byte` | read one script byte and copy that registry slot anchor to current slot state | `byte-count-known` |
| `EF:0FF6` | `ResetDeliveryArrivalState` | `timed-delivery` | 5 | 0 | `-` | clear transient arrival state and restore/reset delivery controller latch | `byte-count-known` |
| `C0:A82F` | `DisableCurrentSlotNeighborCache` | `neighbor-cache` | 4 | 0 | `-` | write #$8000 sentinel to current slot neighbor cache $289E | `byte-count-known` |
| `C0:A841` | `Script_PlaySoundEffectParameter` | `text-presentation` | 4 | 2 | `sound_effect_id_word` | read one script word as a sound/effect id and play it through C0:ABE0 | `byte-count-known` |
| `C0:A943` | `ActionScript_GetPositionOfPartyMember` | `current-slot-state` | 4 | 1 | `party_member_selector_byte` | read one party-member selector byte and copy that member position into script state | `byte-count-known` |
| `C0:A68B` | `StoreAInCurrentSlotField2B32` | `current-slot-state` | 4 | 0 | `-` | store the accumulator value into current slot movement/visual field $2B32 | `byte-count-known` |
| `C0:D98F` | `Export_CurrentSlotAttentionTarget` | `current-slot-state` | 4 | 0 | `-` | export the current slot attention target into the script-visible cached target fields | `byte-count-known` |
| `C4:6C87` | `RestoreCurrentSlotAnchorFromCachedTarget` | `current-slot-state` | 4 | 0 | `-` | restore the current slot anchor from the cached target position fields | `byte-count-known` |
| `C0:A84C` | `ActionScript_TestEventFlag_ReadWord` | `event-flag` | 3 | 2 | `event_flag_word` | read one script word and test it through C2:1628 | `byte-count-known` |
| `C0:A8C6` | `StepCurrentSlotTowardCachedTarget` | `movement` | 3 | 0 | `-` | step current slot toward cached target through C4:7143 and report arrival | `byte-count-known` |
| `C0:C7DB` | `UpdateCurrentSlotFootprintMask` | `collision` | 3 | 0 | `-` | refresh the current slot footprint/collision mask after position or visual-state changes | `byte-count-known` |
| `C2:0000` | `RunEnemySunstrokeCheck` | `battle-runtime` | 3 | 0 | `-` | battle-runtime sunstroke/special controller helper; C3 intro use remains unusual | `byte-count-known` |
| `C0:A6DA` | `ClearCurrentSlotNeighborCache` | `neighbor-cache` | 3 | 0 | `-` | write #$FFFF to current slot neighbor cache $289E | `byte-count-known` |
| `C0:C83B` | `InstallScriptMovementVectorFromDirection` | `movement` | 3 | 0 | `-` | install current-slot movement vector words from the script direction and speed state | `byte-count-known` |
| `C0:CA4E` | `SetMovementTaskTimerFromActiveVector` | `movement` | 3 | 0 | `-` | derive the movement task timer from the active movement vector and cache it for script waits | `byte-count-known` |
| `C4:6ADB` | `ComputeCurrentSlotTargetDirectionOctant` | `movement` | 3 | 0 | `-` | compute the direction octant from the current slot toward its cached target | `byte-count-known` |
| `C4:7044` | `ProjectAngleIntoCurrentSlotVectorWords` | `movement` | 3 | 0 | `-` | project the active angle into current-slot movement vector words | `byte-count-known` |
| `C4:6B0A` | `RoundAngleToOctantAndCacheCurrentSlot` | `movement` | 3 | 0 | `-` | round the active angle to a direction octant and cache it on the current slot | `byte-count-known` |
| `C4:7B77` | `LoadIndexedWindowGfxAndReadVariantByte` | `text-presentation` | 2 | 0 | `-` | load indexed window graphics and return the selected variant byte to the script | `byte-count-known` |
| `C0:A691` | `GetCurrentSlotField2B32` | `current-slot-state` | 2 | 0 | `-` | return current slot movement/visual field $2B32 for script-side tests | `byte-count-known` |
| `EF:0F60` | `CheckDeliveryServiceReadyForArrival` | `timed-delivery` | 2 | 0 | `-` | test delivery/service readiness against busy state and controller latches | `byte-count-known` |
| `EF:0DFA` | `QueueCurrentDeliveryPointer2` | `timed-delivery` | 2 | 0 | `-` | queue current delivery row pointer 2 as deferred queue type #$000A | `byte-count-known` |
| `C4:6EF8` | `CheckCurrentSlotWithinPlayerProximityThreshold` | `proximity-gate` | 2 | 0 | `-` | test the current slot anchor against the player proximity threshold | `byte-count-known` |
| `C0:A959` | `FacePoseDescriptorSlotTowardCurrentSlot_ReadWord` | `presentation-render` | 2 | 2 | `pose_descriptor_id_word` | read one pose-descriptor id word, resolve that slot, and face it toward the current slot | `byte-count-known` |
| `C0:A98B` | `SpawnEntityAtCurrentSlotAnchor_ReadTwoWords` | `entity-spawn` | 2 | 4 | `sprite_pose_descriptor_word, entity_script_id_word` | read a sprite-pose descriptor index and entity script id, then spawn an entity at the current slot anchor through C01E49 | `byte-count-known` |
| `C0:A679` | `Script_SetCurrentSlotSurfaceFlags` | `current-slot-state` | 2 | 1 | `surface_flags_byte` | read one surface-flags byte and store it to current slot field $2BAA | `byte-count-known` |
| `C4:0023` | `StoreLowNibble1a42ToCurrentScriptField1372` | `presentation-render` | 2 | 0 | `-` | copy the low nibble of display/script latch $1A42 into current script field $1372 | `byte-count-known` |
| `C0:A6E3` | `WatchAndRefreshCompanionVisualPhase` | `visual-profile` | 2 | 0 | `-` | poll companion visual state and refresh the current slot phase while the watcher remains active | `byte-count-known` |
| `C4:7269` | `ClassifyCurrentSlotAgainstAreaBounds` | `current-slot-state` | 2 | 0 | `-` | classify the current slot against the active area-bounds rectangle and return the result in the tempvar | `byte-count-known` |
| `C0:6478` | `Update_CurrentSlotNeighborCache_Priority` | `neighbor-cache` | 2 | 0 | `-` | refresh current slot neighbor-cache priority before attention/collision routing | `byte-count-known` |
| `C0:D5B0` | `Gate_NpcAttentionCoordinatorFromScript` | `overworld-runtime` | 2 | 0 | `-` | start or advance the NPC-attention coordinator and return whether the script should keep waiting | `byte-count-known` |
| `C0:A8DC` | `StepCurrentSlotTowardCachedTarget_NoFacingRefresh` | `movement` | 2 | 0 | `-` | step current slot toward cached target without refreshing the current slot facing selector, and report arrival | `byte-count-known` |
| `C4:6E74` | `CheckStagedPositionWithinPlayerProximityThreshold` | `proximity-gate` | 2 | 0 | `-` | test staged position against the player proximity threshold | `byte-count-known` |
| `C4:8B3B` | `MakePartyLookAtActiveEntityCallback` | `party-facing` | 2 | 0 | `-` | make party members face or track the active entity | `byte-count-known` |
| `C0:A907` | `ActionScript_PrepareNewEntityAtTeleportDestination` | `overworld-runtime` | 2 | 1 | `teleport_destination_selector_byte` | read one teleport-destination selector byte and prepare a new entity at that destination | `byte-count-known` |
| `C0:9FBB` | `ActionScript_FadeOutWrapper` | `presentation-render` | 2 | 2 | `fadeout_effect_word` | read one fade-out effect word and pass it to C0:887A | `byte-count-known` |
| `C0:A838` | `MarkCurrentSlotCollisionStateFFFF` | `collision` | 1 | 0 | `-` | mark the current slot collision/neighbor state with the #$FFFF sentinel | `byte-count-known` |
| `C4:7A9E` | `LoadCurrentEntityIndexedWindowGfxToVram` | `text-presentation` | 1 | 0 | `-` | load the current entity's indexed window graphics variant into VRAM | `byte-count-known` |
| `C4:800B` | `UndrawFlyoverTextAndRestoreWorldDisplay` | `world-state-restore` | 1 | 0 | `-` | restore world display state after flyover/text presentation | `byte-count-known` |
| `C4:68B5` | `TestValueLeftOfCurrentAnchorX` | `presentation-render` | 1 | 0 | `-` | compare a staged value against the current anchor X and report whether it is left of the anchor | `byte-count-known` |
| `C4:68DC` | `TestValueAboveCurrentAnchorY` | `presentation-render` | 1 | 0 | `-` | compare a staged value against the current anchor Y and report whether it is above the anchor | `byte-count-known` |
| `EF:0CA7` | `CheckCurrentDeliveryRetryThreshold` | `timed-delivery` | 1 | 0 | `-` | increment current row retry counter and compare against delivery record word 2 | `byte-count-known` |
| `EF:0D23` | `GetCurrentDeliveryRetryWait` | `timed-delivery` | 1 | 0 | `-` | return current delivery row retry-wait word 3 | `byte-count-known` |
| `C2:FF9A` | `CheckOverworldPositionHashThreshold3Of8` | `battle-runtime` | 1 | 0 | `-` | test the overworld position hash against the 3-of-8 threshold used by encounter/battle gating | `byte-count-known` |
| `C0:C19B` | `CopyPathToLane_FromPartyMemberRequest` | `overworld-runtime` | 1 | 0 | `-` | copy a party-member path request into the active movement lane | `byte-count-known` |
| `EF:0FDB` | `BeginDeliverySuccessArrivalState` | `timed-delivery` | 1 | 0 | `-` | arm success-side delivery arrival state and presentation side effects | `byte-count-known` |
| `EF:0D8D` | `QueueCurrentDeliveryPointer1` | `timed-delivery` | 1 | 0 | `-` | queue current delivery row pointer 1 as immediate queue type #$0008 | `byte-count-known` |
| `C0:C251` | `CopyPathToLane_FromCurrentEntityRequestReverse` | `overworld-runtime` | 1 | 0 | `-` | copy the current entity path request into the active movement lane in reverse order | `byte-count-known` |
| `EF:0E8A` | `GetCurrentDeliveryExitSpeed` | `timed-delivery` | 1 | 0 | `-` | return current delivery row exit-speed word 9 | `byte-count-known` |
| `EF:0E67` | `GetCurrentDeliveryEnterSpeed` | `timed-delivery` | 1 | 0 | `-` | return current delivery row enter-speed word 8 | `byte-count-known` |
| `C4:ECE7` | `IsEntityStillOnCastScreen` | `presentation-render` | 1 | 0 | `-` | test whether the current entity remains on the cast-screen presentation viewport | `byte-count-known` |
| `C0:D15C` | `HasUsableOverlapNeighborContext` | `neighbor-cache` | 1 | 0 | `-` | test whether the current overlap/neighbor context can drive a scripted movement decision | `byte-count-known` |
| `C4:681A` | `QueueCurrentVisualTypeMovementScript` | `visual-profile` | 1 | 0 | `-` | queue the movement script associated with the current slot visual type | `byte-count-known` |
| `C4:6914` | `GetCurrentVisualTypeRecordByte03` | `visual-profile` | 1 | 0 | `-` | return byte $03 from the current visual-type record | `byte-count-known` |
| `C4:6957` | `UpdateCurrentSlotFrameSelector` | `visual-profile` | 1 | 0 | `-` | update the current slot frame selector from visual-type animation state | `byte-count-known` |
| `C1:FFD3` | `ComputeBankC1ChecksumTail` | `intro-integrity` | 1 | 0 | `-` | bank-local checksum/integrity tail used by intro control flow | `byte-count-known` |
| `C3:0100` | `DisplayAntiPiracyScreen` | `other` | 1 | 0 | `-` | display the anti-piracy screen and terminate the script path | `byte-count-known` |
| `C0:3DAA` | `Sync_CurrentSlotToPartyCharacterRecord` | `current-slot-state` | 1 | 0 | `-` | sync current slot position/state into the matching party character record | `byte-count-known` |
| `C0:4EF0` | `Restore_CurrentSlotFromSnapshotRecord` | `current-slot-state` | 1 | 0 | `-` | restore the current slot position/state from its saved snapshot record | `byte-count-known` |
| `C0:5E76` | `Update_CurrentSlotCollisionCache` | `collision` | 1 | 4 | `collision_probe_mode_byte, neighbor_cache_callback_long` | refresh current slot collision cache using one script mode byte and a long neighbor-cache callback pointer | `byte-count-known` |
| `C0:A964` | `SetCurrentSlotAreaBoundsFromRadii_ReadTwoWords` | `movement` | 1 | 4 | `radius_x_word, radius_y_word` | read X/Y radius words and build an area-bounds rectangle around the current slot | `byte-count-known` |
| `C0:A6B8` | `GetCurrentSlotHasNoCachedNeighborFlag` | `neighbor-cache` | 1 | 0 | `-` | test whether the current slot has no cached neighbor/attention target | `byte-count-known` |
| `C0:5E82` | `Update_CurrentSlotCollisionCache_WithTerrainCompatibility` | `collision` | 1 | 0 | `-` | refresh current slot collision cache using terrain-compatibility rules | `byte-count-known` |
| `C0:5ECE` | `Update_CurrentSlotCollisionCache_FromHorizontalEdges` | `collision` | 1 | 0 | `-` | refresh current slot collision cache from horizontal edge probes | `byte-count-known` |
| `C0:D59B` | `Check_NpcAttentionCoordinatorActive` | `overworld-runtime` | 1 | 0 | `-` | test whether the NPC-attention coordinator is still active for the current script actor | `byte-count-known` |
| `C4:6B37` | `RotateDirectionOctantHalfTurn` | `movement` | 1 | 0 | `-` | rotate the current direction octant by a half turn | `byte-count-known` |
| `C0:A8D1` | `StepCurrentSlotTowardCachedTarget_WithHalfTurnFacing` | `movement` | 1 | 0 | `-` | step current slot toward cached target, applying the C4:7143 half-turn facing postprocess | `byte-count-known` |
| `C0:A857` | `ActionScript_SetOrClearEventFlag_ReadWordPreserveMode` | `event-flag` | 1 | 2 | `event_flag_word` | preserve incoming mode in X, read one script word, and call C2:165E | `byte-count-known` |
| `C4:7333` | `ReadActiveOverworldRegistryCount` | `overworld-runtime` | 1 | 0 | `-` | read the active overworld registry count used by landing/profile scripts | `byte-count-known` |
| `C4:6C45` | `SnapshotCurrentSlotAnchorToStagedPosition` | `current-slot-state` | 1 | 0 | `-` | copy the current slot anchor position into the staged position fields used by movement callbacks | `byte-count-known` |
| `C0:A94E` | `FaceVisualTypeSlotTowardCurrentSlot_ReadWord` | `presentation-render` | 1 | 2 | `visual_type_id_word` | read one visual-type id word, resolve that slot, and face it toward the current slot | `byte-count-known` |
| `C0:A86F` | `Script_CopyPoseDescriptorSlotAnchorToCurrentSlot_ReadWord` | `current-slot-state` | 1 | 2 | `pose_descriptor_slot_word` | read one script word and copy that pose-descriptor slot anchor to current slot state | `byte-count-known` |
| `C0:A651` | `Script_SetDirectionClassAndField1A86` | `movement` | 1 | 1 | `direction_class_byte` | read one direction/visual class byte, apply it when active, and store it to current slot field $1A86 | `byte-count-known` |
| `C0:9451` | `RestoreSavedCoordinateState` | `world-state-restore` | 1 | 0 | `-` | restore saved coordinate/world state after transitions or script presentation | `byte-count-known` |

## Installed callback target signal

| Target | Preferred name | Group | Installs | Contract |
| --- | --- | --- | ---: | --- |
| `C0:A37A` | `UpdatePosition_WhenNoNeighbor_WithSpriteRefresh_CurrentSlot` | `movement` | 17 | current-slot entry that reloads the active slot and joins the no-neighbor sprite-refresh updater |
| `C0:9FC8` | `Integrate_XYVelocityOnly` | `movement` | 7 | integrate fractional/current-slot XY velocity into world X/Y position |
| `C0:A360` | `UpdatePosition_WhenNoNeighbor_WithSpriteRefresh` | `movement` | 5 | per-frame no-neighbor position updater that integrates movement and refreshes footprint state |
| `C0:A039` | `ReturnFromPositionChangeCallback_NoProjection` | `presentation-render` | 5 | passive position-change callback entry that returns without screen projection |
| `C4:8BE1` | `SimpleScreenPositionCallback` | `presentation-render` | 4 | tick callback that keeps the active entity at a simple screen-projected position |
| `C0:9FF0` | `ReturnFromPhysicsCallback_NoMovement` | `movement` | 4 | passive physics callback entry that returns without integrating movement |
| `C4:8C2B` | `CentreScreenOnEntityCallback` | `presentation-render` | 2 | tick callback that centers the screen around the active entity |
| `C0:9FF1` | `Integrate_XYAndZVelocity_WithSpriteRefresh` | `movement` | 2 | integrate XY and Z velocity, then refresh the current-slot footprint/sprite mask |
| `C0:5200` | `Tick_OverworldPlayerPositionAndCallbacks` | `overworld-runtime` | 2 | normal overworld tick callback for player/object position and registered callbacks |
| `C4:8C02` | `SimpleScreenPositionCallbackOffset` | `presentation-render` | 2 | tick callback that keeps the active entity at a simple screen-projected position with offset handling |
| `C0:A055` | `ProjectWorldToScreen_FromCamera39` | `presentation-render` | 1 | project current slot world X/Y through camera $39/$3B |
| `C0:A0A0` | `ProjectWorldToScreen_FromCamera39AndHeight` | `presentation-render` | 1 | project current slot world X/Y through camera $39/$3B and subtract height from screen Y |
| `C0:A384` | `UpdatePosition_WhenNoNeighbor` | `movement` | 1 | per-frame no-neighbor position updater that integrates movement without the footprint refresh tail |
| `C0:A26B` | `PhysicsCallback_TargetContextCompareAndProject` | `movement` | 1 | physics callback that compares current slot in active target context and otherwise falls back to camera projection |
| `C0:4D78` | `Tick_Event2SnapshotObjectReconcile` | `overworld-runtime` | 1 | intro/event snapshot tick callback that reconciles object state against saved coordinates |
| `C0:D7F7` | `Consume_CurrentSlotAttentionPath` | `current-slot-state` | 1 | consume the current slot attention path into live movement target state |
| `C0:A03A` | `ProjectWorldToScreen_FromCamera31AndHeight` | `presentation-render` | 1 | project current slot world coordinates through camera $31 and height state into screen coordinates |

## Full script inventory

| Address | Name | Class | Decode | Instr. | First opcode | Callroutines | Installed callbacks | C3 targets |
| --- | --- | --- | --- | ---: | --- | --- | --- | --- |
| `C3:0195` | `Event221PaulaFatherFarewellSequence` | `event-bytecode-asset` | `complete` | 44 | `$42 EVENT_CALLROUTINE` | `C0:A84C`, `C0:A82F`, `C0:A838`, `C0:AA6E`, +6 | `C0:A360` | `C3:A2AA`, `C3:AA38`, `C3:AB8A`, `C3:AFA3`, +5 |
| `C3:0235` | `Event222PaulaDoorExitMovementScript` | `event-bytecode-asset` | `complete` | 6 | `$15 EVENT_WRITE_WORD_WRAM` | `C4:6E46` | - | `C3:0295` |
| `C3:024A` | `Event223PaulaPorchExitMovementScript` | `event-bytecode-asset` | `complete` | 7 | `$28 EVENT_SET_X` | `C4:6E46` | - | `C3:0295` |
| `C3:0260` | `Event224PaulaReturnMovementScript` | `event-bytecode-asset` | `complete` | 15 | `$28 EVENT_SET_X` | `C0:AA6E`, `C4:6E46` | - | `C3:0295`, `C3:AB59` |
| `C3:0295` | `MoveActiveEntityLeftToScriptVarsAndWait` | `event-bytecode-asset` | `complete` | 6 | `$1A EVENT_SHORTCALL` | `C0:AA6E`, `C0:A685` | - | `C3:AA38`, `C3:AB59` |
| `C3:098B` | `WaitMovementThenYieldHalt` | `event-script-asset` | `complete` | 3 | `$1A EVENT_SHORTCALL` | `C4:6E46` | - | `C3:AB59` |
| `C3:0A1F` | `ShortZBounceTask` | `event-script-asset` | `complete` | 8 | `$41 EVENT_SET_Z_VELOCITY` | - | - | - |
| `C3:0C55` | `InitMovementPresetField2B32AndRefreshVisual` | `event-script-asset` | `complete` | 5 | `$1A EVENT_SHORTCALL` | `C0:A685`, `C0:A4BF` | - | `C3:AA2B` |
| `C3:0C67` | `LoopLongCoordinatePatrolRoute` | `event-script-asset` | `complete` | 36 | `$06 EVENT_PAUSE` | - | - | `C3:AB59`, `C3:0C67` |
| `C3:1D2D` | `LoopVar4TimedAnimationPulse` | `event-script-asset` | `complete` | 11 | `$20 EVENT_WRITE_VAR_TO_TEMPVAR` | `C0:A4B2`, `C0:A4A8` | - | `C3:1D4A`, `C3:1D2D` |
| `C3:1D4F` | `InitVar4TimedAnimationPulseMovement` | `event-script-asset` | `complete` | 7 | `$25 EVENT_SET_PHYSICS_CALLBACK` | `C0:A4BF` | `C0:A37A` | `C3:1D2D` |
| `C3:1DF4` | `Event357_RegistryAnchorMovementPrep` | `event-script-asset` | `complete` | 11 | `$42 EVENT_CALLROUTINE` | `C0:A864` | `C0:9FC8`, `C4:8C2B` | `C3:1E14`, `C3:AB59`, `C3:1E0C` |
| `C3:1E2D` | `InitPartyMemberMovementWithBrightnessTask` | `event-script-asset` | `complete` | 11 | `$25 EVENT_SET_PHYSICS_CALLBACK` | `C0:A943` | `C0:9FC8`, `C4:8C2B` | `C3:1E4D`, `C3:AB59`, `C3:1E45` |
| `C3:1EC1` | `RunRightwardStepPulseHelper` | `event-script-asset` | `complete` | 10 | `$06 EVENT_PAUSE` | `C0:A4B2`, `C0:A4A8` | - | - |
| `C3:1ED8` | `RunLeftwardStepPulseHelper` | `event-script-asset` | `complete` | 10 | `$06 EVENT_PAUSE` | `C0:A4B2`, `C0:A4A8` | - | - |
| `C3:1EEF` | `RunTStageDanceStepPattern` | `event-script-asset` | `complete` | 73 | `$3F EVENT_SET_X_VELOCITY` | `C0:AA6E`, `C0:A65F`, `C0:A4A8` | - | `C3:2138` |
| `C3:2138` | `RunTStageAnimationStepPair` | `event-script-asset` | `complete` | 7 | `$3B EVENT_SET_ANIMATION` | `C0:A4A8`, `C0:A4B2` | - | - |
| `C3:2CD2` | `LoopStageActorVerticalBounce` | `event-script-asset` | `complete` | 14 | `$40 EVENT_SET_Y_VELOCITY` | - | - | `C3:2CD2` |
| `C3:3399` | `PulseDownFacingVisualCountdown` | `event-script-asset` | `complete` | 5 | `$42 EVENT_CALLROUTINE` | `C0:AA6E` | - | - |
| `C3:33AA` | `PulseUpFacingVisualCountdown` | `event-script-asset` | `complete` | 5 | `$42 EVENT_CALLROUTINE` | `C0:AA6E` | - | - |
| `C3:33BB` | `PulseLeftFacingVisualCountdown` | `event-script-asset` | `complete` | 5 | `$42 EVENT_CALLROUTINE` | `C0:AA6E` | - | - |
| `C3:33CC` | `PulseRightFacingVisualCountdown` | `event-script-asset` | `complete` | 5 | `$42 EVENT_CALLROUTINE` | `C0:AA6E` | - | - |
| `C3:33DD` | `RunStageFacingVisualPulsePattern` | `event-script-asset` | `complete` | 19 | `$1A EVENT_SHORTCALL` | `C0:AA6E` | - | `C3:3399` |
| `C3:3549` | `LoopVisualCountdownRandomWaitTask` | `event-script-asset` | `complete` | 11 | `$42 EVENT_CALLROUTINE` | `C0:AA6E`, `C0:9F82` | - | `C3:3549` |
| `C3:3BFB` | `RunWindowGfxVariantLoaderPrologue` | `event-script-asset` | `complete` | 9 | `$3B EVENT_SET_ANIMATION` | `C4:7A9E`, `C4:7B77` | `C0:9FC8` | `C3:3C18`, `C3:3C08` |
| `C3:3C18` | `UndrawFlyoverTextAndReturn` | `event-script-asset` | `complete` | 2 | `$42 EVENT_CALLROUTINE` | `C4:800B` | - | - |
| `C3:3C1D` | `RunWindowGfxVariantLoop` | `event-script-asset` | `complete` | 8 | `$20 EVENT_WRITE_VAR_TO_TEMPVAR` | `C4:7B77` | - | `C3:3C2F` |
| `C3:3DBE` | `LoopEvent465_466Field2B32PulseTask` | `event-script-asset` | `complete` | 8 | `$01 EVENT_LOOP` | `C0:A691`, `C0:A68B` | - | - |
| `C3:4392` | `RunLeftwardBoundsReleasePath` | `event-script-asset` | `complete` | 9 | `$07 EVENT_START_TASK` | `C0:AA6E` | - | `C3:43AE`, `C3:A204` |
| `C3:43AE` | `LoopWatchBoundsForLeftwardRelease` | `event-script-asset` | `complete` | 14 | `$06 EVENT_PAUSE` | `C4:68B5`, `C4:68DC` | - | `C3:43C4`, `C3:43D8`, `C3:43AE`, `C3:A204` |
| `C3:43DB` | `LoopTimedDeliveryDeparturePulseUntilOffscreen` | `event-bytecode-label` | `complete` | 13 | `$06 EVENT_PAUSE` | `C0:A4B2`, `C0:A4A8`, `C0:C6B6`, `EF:0FF6`, +1 | - | `C3:43E8`, `C3:43DB`, `C3:A204` |
| `C3:43E8` | `TimedDeliveryDeparturePulseAnimation0Half` | `event-bytecode-asset` | `complete` | 8 | `$06 EVENT_PAUSE` | `C0:A4A8`, `C0:C6B6`, `EF:0FF6`, `C4:6E46` | - | `C3:43DB`, `C3:A204` |
| `C3:443E` | `TimedDeliveryRetryWaitLoop` | `event-bytecode-asset` | `complete` | 9 | `$42 EVENT_CALLROUTINE` | `EF:0CA7`, `EF:0D23`, `EF:0F60` | - | `C3:447D`, `C3:4457`, `C3:443E` |
| `C3:444D` | `TimedDeliveryReadinessGate` | `event-bytecode-asset` | `complete` | 3 | `$42 EVENT_CALLROUTINE` | `EF:0F60` | - | `C3:4457`, `C3:443E` |
| `C3:4457` | `TimedDeliverySuccessGateAndPresentationSetup` | `event-bytecode-asset` | `complete` | 11 | `$42 EVENT_CALLROUTINE` | `C2:FF9A`, `C0:C19B`, `EF:0FDB`, `EF:0D8D` | - | `C3:447D`, `C3:443E`, `C3:447A`, `C3:4488`, +1 |
| `C3:447A` | `StartTimedDeliveryArrivalMovementTask` | `event-bytecode-label` | `complete` | 4 | `$1A EVENT_SHORTCALL` | `EF:0FF6`, `EF:0DFA` | - | `C3:44DE`, `C3:A204` |
| `C3:447D` | `TimedDeliveryFailureTeardown` | `event-bytecode-asset` | `complete` | 3 | `$42 EVENT_CALLROUTINE` | `EF:0FF6`, `EF:0DFA` | - | `C3:A204` |
| `C3:4488` | `PrepareTimedDeliveryActorForPresentation` | `event-bytecode-asset` | `complete` | 11 | `$3B EVENT_SET_ANIMATION` | `C0:A4BF`, `C4:6EF8` | - | `C3:A09F`, `C3:44A7`, `C3:4499` |
| `C3:4499` | `WaitTimedDeliveryActorPresentationPrep` | `event-bytecode-label` | `complete` | 6 | `$06 EVENT_PAUSE` | `C4:6EF8` | - | `C3:44A7`, `C3:4499` |
| `C3:44A7` | `ReturnFromTimedDeliveryActorPrep` | `event-bytecode-label` | `complete` | 1 | `$1B EVENT_SHORT_RETURN` | - | - | - |
| `C3:44A8` | `RunTimedDeliveryDepartureMovement` | `event-bytecode-asset` | `complete` | 15 | `$39 EVENT_SET_VELOCITIES_ZERO` | `C0:C251`, `EF:0E8A`, `C0:A68B`, `C0:D98F`, +1 | - | `C3:43DB`, `C3:44D2`, `C3:AB59`, `C3:44C1` |
| `C3:44C1` | `LoopTimedDeliveryDepartureMovement` | `event-bytecode-label` | `complete` | 5 | `$42 EVENT_CALLROUTINE` | `C0:D98F`, `C4:6C87` | - | `C3:44D2`, `C3:AB59`, `C3:44C1` |
| `C3:44D2` | `FinishTimedDeliveryDepartureAndYieldText` | `event-bytecode-label` | `complete` | 4 | `$39 EVENT_SET_VELOCITIES_ZERO` | `EF:0FF6`, `C4:6E46` | - | `C3:A204` |
| `C3:44DE` | `RunTimedDeliveryArrivalMovement` | `event-bytecode-asset` | `complete` | 9 | `$42 EVENT_CALLROUTINE` | `EF:0E67`, `C0:A68B`, `C0:D98F`, `C4:6C87` | - | `C3:44FF`, `C3:AB59`, `C3:44EE` |
| `C3:44EE` | `LoopTimedDeliveryArrivalMovement` | `event-bytecode-label` | `complete` | 5 | `$42 EVENT_CALLROUTINE` | `C0:D98F`, `C4:6C87` | - | `C3:44FF`, `C3:AB59`, `C3:44EE` |
| `C3:44FF` | `HoldTimedDeliveryArrivalCompletion` | `event-bytecode-label` | `complete` | 3 | `$0E EVENT_SET_VAR` | - | - | `C3:44FF` |
| `C3:48C4` | `PlayDownRightLeftDownFacingGesture` | `event-script-asset` | `complete` | 19 | `$1D EVENT_WRITE_WORD_TEMPVAR` | `C0:A65F`, `C0:A4BF` | - | - |
| `C3:4964` | `LoopReadScriptWords0201Task` | `event-script-asset` | `complete` | 4 | `$42 EVENT_CALLROUTINE` | `C0:A959` | - | `C3:4964` |
| `C3:4A61` | `LoopReadScriptWord01Task` | `event-script-asset` | `complete` | 3 | `$42 EVENT_CALLROUTINE` | `C0:A959` | - | `C3:4A61` |
| `C3:4B62` | `PlayDirectionCountdownCompassCycle` | `event-script-asset` | `complete` | 25 | `$42 EVENT_CALLROUTINE` | `C0:AA6E` | - | - |
| `C3:4D39` | `RunFallingBouncePresentation` | `event-script-asset` | `complete` | 13 | `$2A EVENT_SET_Z` | `C0:A841`, `C4:6E46` | - | `C3:AB26` |
| `C3:4E73` | `InitSimpleScreenPositionIntroActor` | `event-script-asset` | `complete` | 6 | `$42 EVENT_CALLROUTINE` | `C0:A864` | `C0:A039`, `C0:9FC8`, `C4:8BE1` | - |
| `C3:5F8B` | `LoopCastScreenActorRefreshGateTask` | `event-script-asset` | `complete` | 15 | `$21 EVENT_WRITE_VAR_TO_WAIT_TIMER` | `C0:A4B2`, `C4:ECE7`, `C0:A4A8` | - | `C3:5F98`, `C3:5FB3`, `C3:5FAC`, `C3:5F8B`, +1 |
| `C3:5FB6` | `InitFlatCastScreenActorWithRefreshTask` | `event-script-asset` | `complete` | 9 | `$21 EVENT_WRITE_VAR_TO_WAIT_TIMER` | - | `C0:A055`, `C0:9FC8` | `C3:5F8B` |
| `C3:5FCD` | `InitDepthCastScreenActorWithRefreshTask` | `event-script-asset` | `complete` | 8 | `$0E EVENT_SET_VAR` | - | `C0:A0A0`, `C0:9FF1` | `C3:5F8B` |
| `C3:62C0` | `RunCastScreenFacingPulseCycle` | `event-script-asset` | `complete` | 9 | `$42 EVENT_CALLROUTINE` | `C0:AA6E` | - | - |
| `C3:6834` | `SpawnKingThenReleaseCurrentVisualEntity` | `event-script-asset` | `complete` | 2 | `$42 EVENT_CALLROUTINE` | `C0:A98B` | - | `C3:A204` |
| `C3:6A3E` | `ReleaseCurrentVisualEntityFromCastPath` | `event-script-asset` | `complete` | 1 | `$19 EVENT_SHORTJUMP` | - | - | `C3:A204` |
| `C3:6A41` | `PrepareObscuredVehiclePathActor` | `event-script-asset` | `complete` | 7 | `$25 EVENT_SET_PHYSICS_CALLBACK` | `C0:A679` | `C0:A384` | `C3:A1F3`, `C3:A262` |
| `C3:6BB4` | `LoopVar3VerticalBounce` | `event-script-asset` | `complete` | 7 | `$20 EVENT_WRITE_VAR_TO_TEMPVAR` | - | - | `C3:6BC1`, `C3:6BB4` |
| `C3:6BEA` | `EndBeforeBoogyTentEyeLiveAreaGate` | `event-script-asset` | `complete` | 1 | `$00 EVENT_END` | - | - | - |
| `C3:6D18` | `LoopWaitForUsableOverlapNeighborContext` | `event-script-asset` | `complete` | 6 | `$06 EVENT_PAUSE` | `C0:D15C`, `C4:681A` | - | `C3:6D18`, `C3:9E01` |
| `C3:6E41` | `LoopVisualTypeFrameSelectorTask` | `event-script-asset` | `complete` | 5 | `$42 EVENT_CALLROUTINE` | `C4:0023`, `C4:6914`, `C4:6957` | - | `C3:6E45` |
| `C3:7439` | `PrepareAlignedMovementToY1616` | `event-script-asset` | `complete` | 9 | `$25 EVENT_SET_PHYSICS_CALLBACK` | `C0:C7DB`, `C0:A4A8`, `C0:A685` | `C0:A37A` | - |
| `C3:7545` | `RunRightLeftFacingPulsePair` | `event-script-asset` | `complete` | 7 | `$01 EVENT_LOOP` | `C0:AA6E` | - | - |
| `C3:7559` | `RunLeftRightFacingPulsePair` | `event-script-asset` | `complete` | 7 | `$01 EVENT_LOOP` | `C0:AA6E` | - | - |
| `C3:7A7C` | `InitStationaryVar4PulseAndReturn` | `event-script-asset` | `complete` | 6 | `$25 EVENT_SET_PHYSICS_CALLBACK` | - | `C0:A37A` | `C3:A15E` |
| `C3:835D` | `SwitchAnimPortFlagsFromTempvar` | `event-script-asset` | `complete` | 2 | `$10 EVENT_SWITCH_JUMP_TEMPVAR` | - | - | `C3:8370`, `C3:8383`, `C3:8396`, `C3:83A9` |
| `C3:83BC` | `ChooseRandomFacingCycleStepCount` | `event-script-asset` | `complete` | 2 | `$42 EVENT_CALLROUTINE` | `C0:9F82` | - | - |
| `C3:8978` | `LoopAnimPortDirectionFromVar4` | `event-script-asset` | `complete` | 6 | `$20 EVENT_WRITE_VAR_TO_TEMPVAR` | `C0:A84C` | - | `C3:8992`, `C3:898C`, `C3:8995` |
| `C3:899E` | `LoopAnimPortBlinkAnimation` | `event-script-asset` | `complete` | 11 | `$3B EVENT_SET_ANIMATION` | `C0:A4A8`, `C0:A4B2` | - | `C3:899E` |
| `C3:9AC7` | `PrepareBattleSwirlFootprintVisualReturn` | `event-script-asset` | `complete` | 7 | `$25 EVENT_SET_PHYSICS_CALLBACK` | `C0:C7DB`, `C0:A4BF` | `C0:9FF0` | `C3:9ABB` |
| `C3:9E01` | `WaitUntilNoBattleSwirlOrEnemyTouch` | `event-script-asset` | `complete` | 5 | `$1E EVENT_WRITE_WRAM_TEMPVAR` | - | - | `C3:9E0E` |
| `C3:A043` | `IntroCutsceneCameraPanGate` | `event-bytecode-asset` | `complete` | 9 | `$42 EVENT_CALLROUTINE` | `C1:FFD3`, `C3:0100`, `C2:0000` | `C0:5200` | `C3:A04E`, `C3:0100`, `C3:A052` |
| `C3:A04E` | `StartIntroCameraPanTickLoop` | `event-bytecode-label` | `complete` | 6 | `$08 EVENT_SET_TICK_CALLBACK` | `C2:0000` | `C0:5200` | `C3:A052` |
| `C3:A052` | `LoopIntroCameraPanWaitAndC2Step` | `event-bytecode-label` | `complete` | 5 | `$01 EVENT_LOOP` | `C2:0000` | - | `C3:A052` |
| `C3:A05E` | `IntroCutsceneSpriteObjectSetup` | `event-bytecode-asset` | `complete` | 10 | `$23 EVENT_SET_POSITION_CHANGE_CALLBACK` | `C0:3DAA`, `C0:4EF0`, `C0:A6DA`, `C0:A6E3` | `C0:A039`, `C0:A26B`, `C0:4D78` | `C3:A076` |
| `C3:A076` | `LoopIntroCompanionVisualRefresh` | `event-bytecode-label` | `complete` | 3 | `$42 EVENT_CALLROUTINE` | `C0:A6E3` | - | `C3:A076` |
| `C3:A07F` | `HaltEventScript` | `event-bytecode-asset` | `complete` | 1 | `$09 EVENT_HALT` | - | - | - |
| `C3:A09F` | `LoopActiveEntityWalkAnimationPulse` | `event-bytecode-label` | `complete` | 7 | `$06 EVENT_PAUSE` | `C0:A4B2`, `C0:A4A8` | - | `C3:A09F` |
| `C3:A0B2` | `LoopActiveEntityWalkPulse24Frame` | `event-bytecode-label` | `complete` | 7 | `$06 EVENT_PAUSE` | `C0:A4B2`, `C0:A4A8` | - | `C3:A0B2` |
| `C3:A0C5` | `LoopActiveEntityWalkPulse12Frame` | `event-bytecode-label` | `complete` | 7 | `$06 EVENT_PAUSE` | `C0:A4B2`, `C0:A4A8` | - | `C3:A0C5` |
| `C3:A0D8` | `LoopActiveEntityWalkPulse9FrameConditional` | `event-bytecode-label` | `complete` | 32 | `$06 EVENT_PAUSE` | `C0:A4B2`, `C0:A4A8` | - | `C3:A0D8`, `C3:A0EB`, `C3:A0FE`, `C3:A11E`, +1 |
| `C3:A0EB` | `LoopActiveEntityWalkPulse6FrameConditional` | `event-bytecode-label` | `complete` | 25 | `$06 EVENT_PAUSE` | `C0:A4B2`, `C0:A4A8` | - | `C3:A0EB`, `C3:A0FE`, `C3:A11E`, `C3:A111` |
| `C3:A0FE` | `LoopActiveEntityWalkPulse2FrameConditional` | `event-bytecode-label` | `complete` | 18 | `$06 EVENT_PAUSE` | `C0:A4B2`, `C0:A4A8` | - | `C3:A0FE`, `C3:A11E`, `C3:A111` |
| `C3:A111` | `LoopActiveEntityWalkPulseVar4Gate` | `event-bytecode-label` | `complete` | 11 | `$06 EVENT_PAUSE` | `C0:A4B2`, `C0:A4A8` | - | `C3:A11E`, `C3:A111` |
| `C3:A12E` | `LoopActiveEntityWalkPulseVar4Countdown` | `event-bytecode-label` | `complete` | 19 | `$20 EVENT_WRITE_VAR_TO_TEMPVAR` | `C0:A4B2`, `C0:A4A8` | - | `C3:A159`, `C3:A12E` |
| `C3:A15E` | `LoopC40015Var4GatedPulseUntilRelease` | `event-bytecode-label` | `complete` | 10 | `$42 EVENT_CALLROUTINE` | `C4:0023`, `C0:A4B2`, `C4:0015` | - | `C3:A16F`, `C3:A162`, `C3:A204` |
| `C3:A17B` | `LoopC40015SlowPulseUntilRelease` | `event-bytecode-label` | `complete` | 7 | `$06 EVENT_PAUSE` | `C0:A4B2`, `C4:0015` | - | `C3:A17B`, `C3:A204` |
| `C3:A18F` | `LoopC40015FastPulseUntilRelease` | `event-bytecode-label` | `complete` | 7 | `$06 EVENT_PAUSE` | `C0:A4B2`, `C4:0015` | - | `C3:A18F`, `C3:A204` |
| `C3:A1A3` | `LoopC40015Pulse12FrameUntilRelease` | `event-script-asset` | `complete` | 7 | `$06 EVENT_PAUSE` | `C0:A4B2`, `C4:0015` | - | `C3:A1A3`, `C3:A204` |
| `C3:A1B7` | `LoopC40015Pulse9FrameUntilRelease` | `event-script-asset` | `complete` | 7 | `$06 EVENT_PAUSE` | `C0:A4B2`, `C4:0015` | - | `C3:A1B7`, `C3:A204` |
| `C3:A1CB` | `LoopC40015Pulse6FrameUntilRelease` | `event-script-asset` | `complete` | 7 | `$06 EVENT_PAUSE` | `C0:A4B2`, `C4:0015` | - | `C3:A1CB`, `C3:A204` |
| `C3:A1DF` | `LoopActiveEntityWalkPulse2FrameC40015Branch` | `event-bytecode-label` | `complete` | 7 | `$06 EVENT_PAUSE` | `C0:A4B2`, `C4:0015` | - | `C3:A0FE`, `C3:A204` |
| `C3:A1F3` | `LoopC40015Pulse16FrameUntilRelease` | `event-bytecode-label` | `complete` | 8 | `$06 EVENT_PAUSE` | `C0:A4B2`, `C4:0015`, `C0:20F1` | - | `C3:A1F3` |
| `C3:A204` | `ReleaseCurrentVisualEntityAndEnd` | `event-bytecode-asset` | `complete` | 2 | `$42 EVENT_CALLROUTINE` | `C0:20F1` | - | - |
| `C3:A209` | `DelayThenReleaseCurrentVisualEntity` | `event-bytecode-asset` | `complete` | 2 | `$06 EVENT_PAUSE` | - | - | `C3:A204` |
| `C3:A20E` | `LoopVar0SelectedAnimationUntilOffscreen` | `event-bytecode-label` | `complete` | 7 | `$3B EVENT_SET_ANIMATION` | `C0:A4A8`, `C0:C6B6` | - | `C3:A22C`, `C3:A234`, `C3:A23D`, `C3:A24E`, +3 |
| `C3:A22C` | `Var0AnimationCase0Pulse8FrameOn` | `event-bytecode-asset` | `complete` | 7 | `$06 EVENT_PAUSE` | `C0:A4B2`, `C0:A4A8` | - | - |
| `C3:A234` | `Var0AnimationCase1Pulse8FrameOff` | `event-bytecode-asset` | `complete` | 4 | `$06 EVENT_PAUSE` | `C0:A4A8` | - | - |
| `C3:A23D` | `Var0AnimationCase2Pulse4Frame` | `event-bytecode-asset` | `complete` | 7 | `$06 EVENT_PAUSE` | `C0:A4B2`, `C0:A4A8` | - | - |
| `C3:A24E` | `Var0AnimationCase3Pulse32Frame` | `event-bytecode-asset` | `complete` | 7 | `$06 EVENT_PAUSE` | `C0:A4B2`, `C0:A4A8` | - | - |
| `C3:A25F` | `Var0AnimationCase4Wait16Frame` | `event-bytecode-asset` | `complete` | 2 | `$06 EVENT_PAUSE` | - | - | - |
| `C3:A262` | `LoopActiveEntityCollisionProbeRefresh` | `event-bytecode-label` | `complete` | 3 | `$42 EVENT_CALLROUTINE` | `C0:A6DA`, `C0:5E76` | - | `C3:A266` |
| `C3:A271` | `EndCurrentEventTask` | `event-script-asset` | `complete` | 1 | `$0C EVENT_END_TASK` | - | - | - |
| `C3:A272` | `EndPreviousTaskThenDirectionFollowerPath` | `event-script-asset` | `complete` | 1 | `$0C EVENT_END_TASK` | - | - | - |
| `C3:A2AA` | `TrafficLightWaitUntilOffscreenAndRelease` | `event-bytecode-asset` | `complete` | 10 | `$25 EVENT_SET_PHYSICS_CALLBACK` | `C0:C7DB`, `C0:A4BF`, `C0:C6B6`, `C0:20F1` | `C0:9FF0` | `C3:A2B8` |
| `C3:A381` | `InitRandomWanderMovementWithCollisionProbe` | `event-bytecode-asset` | `complete` | 8 | `$25 EVENT_SET_PHYSICS_CALLBACK` | `C0:A4BF`, `C0:A685`, `C0:A964` | `C0:A360` | `C3:A111`, `C3:A262`, `C3:A3B7` |
| `C3:A3A1` | `InitC40015PulseWithCollisionProbe` | `event-bytecode-asset` | `complete` | 7 | `$25 EVENT_SET_PHYSICS_CALLBACK` | `C0:A4BF`, `C0:A685` | `C0:A360` | `C3:A15E`, `C3:A262` |
| `C3:A3B7` | `LoopRandomDirectionMovementWithRandomWait` | `event-bytecode-label` | `complete` | 5 | `$0E EVENT_SET_VAR` | `C4:7269` | - | `C3:A3C9`, `C3:A3D6` |
| `C3:A3C9` | `ChooseRandomCardinalDirection` | `event-bytecode-asset` | `complete` | 10 | `$42 EVENT_CALLROUTINE` | `C0:9F82`, `C0:A65F`, `C0:C83B`, `C0:CA4E` | - | `C3:A3B7` |
| `C3:A3D6` | `ApplyRandomDirectionAndMovementTimer` | `event-bytecode-asset` | `complete` | 9 | `$42 EVENT_CALLROUTINE` | `C0:A65F`, `C0:C83B`, `C0:9F82`, `C0:CA4E` | - | `C3:A3B7` |
| `C3:A3E7` | `SetMovementTimerThenRandomWait` | `event-bytecode-asset` | `complete` | 6 | `$42 EVENT_CALLROUTINE` | `C0:CA4E`, `C0:9F82` | - | `C3:A3B7` |
| `C3:A401` | `InitNpcAttentionPathIfNoCachedNeighbor` | `event-bytecode-asset` | `complete` | 12 | `$25 EVENT_SET_PHYSICS_CALLBACK` | `C0:A6DA`, `C0:A6B8`, `C0:A4BF` | `C0:9FF0`, `C0:D7F7`, `C0:A360` | `C3:A425`, `C3:A20E` |
| `C3:A426` | `StartNpcAttentionTerrainCollisionLoop` | `event-bytecode-label` | `complete` | 3 | `$1A EVENT_SHORTCALL` | - | - | `C3:A401`, `C3:A434` |
| `C3:A42D` | `StartNpcAttentionHorizontalCollisionLoop` | `event-bytecode-label` | `complete` | 3 | `$1A EVENT_SHORTCALL` | - | - | `C3:A401`, `C3:A448` |
| `C3:A434` | `LoopNpcAttentionTerrainCollision` | `event-bytecode-label` | `complete` | 6 | `$42 EVENT_CALLROUTINE` | `C0:6478`, `C0:5E82`, `C0:D5B0` | - | `C3:A45C`, `C3:A434` |
| `C3:A448` | `LoopNpcAttentionHorizontalCollision` | `event-bytecode-label` | `complete` | 6 | `$42 EVENT_CALLROUTINE` | `C0:6478`, `C0:5ECE`, `C0:D5B0` | - | `C3:A45C`, `C3:A448` |
| `C3:A45C` | `FinishNpcAttentionAndReleaseActor` | `event-bytecode-label` | `complete` | 16 | `$06 EVENT_PAUSE` | `C0:D59B`, `C0:20F1` | `C0:9FF0` | `C3:A45C` |
| `C3:A47C` | `ReleaseCurrentVisualEntityTail` | `event-bytecode-asset` | `complete` | 2 | `$42 EVENT_CALLROUTINE` | `C0:20F1` | - | - |
| `C3:AA1E` | `ApplyTempDirectionAndRefreshMovementVector` | `event-script-asset` | `complete` | 4 | `$42 EVENT_CALLROUTINE` | `C0:A65F`, `C0:C83B`, `C0:A4BF` | - | - |
| `C3:AA2B` | `InitMovementWithDefaultPhysicsPulseAndCollisionProbe` | `event-script-asset` | `complete` | 6 | `$25 EVENT_SET_PHYSICS_CALLBACK` | - | `C0:A360` | `C3:A1F3`, `C3:A262` |
| `C3:AA38` | `InitActionScriptMovementState` | `event-bytecode-asset` | `complete` | 6 | `$25 EVENT_SET_PHYSICS_CALLBACK` | - | `C0:A37A` | `C3:A111` |
| `C3:AA46` | `InitMovementPreset40_00Pulse24Frame` | `event-bytecode-asset` | `complete` | 7 | `$25 EVENT_SET_PHYSICS_CALLBACK` | `C0:A4BF`, `C0:A685` | `C0:A37A` | `C3:A0B2` |
| `C3:AA5A` | `InitMovementPreset00_01Pulse12Frame` | `event-bytecode-asset` | `complete` | 7 | `$25 EVENT_SET_PHYSICS_CALLBACK` | `C0:A4BF`, `C0:A685` | `C0:A37A` | `C3:A0C5` |
| `C3:AA6E` | `InitMovementPreset60_01Pulse9Frame` | `event-bytecode-asset` | `complete` | 7 | `$25 EVENT_SET_PHYSICS_CALLBACK` | `C0:A4BF`, `C0:A685` | `C0:A37A` | `C3:A0D8` |
| `C3:AA82` | `InitMovementPreset00_02Pulse6Frame` | `event-bytecode-asset` | `complete` | 7 | `$25 EVENT_SET_PHYSICS_CALLBACK` | `C0:A4BF`, `C0:A685` | `C0:A37A` | `C3:A0EB` |
| `C3:AA96` | `InitMovementPreset00_06Pulse2Frame` | `event-bytecode-asset` | `complete` | 7 | `$25 EVENT_SET_PHYSICS_CALLBACK` | `C0:A4BF`, `C0:A685` | `C0:A37A` | `C3:A0FE` |
| `C3:AAAA` | `InitMovementPresetVar4Countdown` | `event-bytecode-asset` | `complete` | 6 | `$25 EVENT_SET_PHYSICS_CALLBACK` | - | `C0:A37A` | `C3:A12E` |
| `C3:AAB8` | `InitMovementPresetC40015Pulse16Frame` | `event-script-asset` | `complete` | 5 | `$25 EVENT_SET_PHYSICS_CALLBACK` | - | `C0:A37A` | `C3:A1F3` |
| `C3:AAC2` | `InitMovementPreset40_00C40015FastPulse` | `event-script-asset` | `complete` | 7 | `$25 EVENT_SET_PHYSICS_CALLBACK` | `C0:A4BF`, `C0:A685` | `C0:A37A` | `C3:A18F` |
| `C3:AAD6` | `InitMovementPreset00_01C40015Pulse12Frame` | `event-script-asset` | `complete` | 7 | `$25 EVENT_SET_PHYSICS_CALLBACK` | `C0:A4BF`, `C0:A685` | `C0:A37A` | `C3:A1A3` |
| `C3:AAEA` | `InitMovementPreset60_01C40015Pulse9Frame` | `event-script-asset` | `complete` | 7 | `$25 EVENT_SET_PHYSICS_CALLBACK` | `C0:A4BF`, `C0:A685` | `C0:A37A` | `C3:A1B7` |
| `C3:AAFE` | `InitMovementPreset00_02C40015Pulse6Frame` | `event-script-asset` | `complete` | 7 | `$25 EVENT_SET_PHYSICS_CALLBACK` | `C0:A4BF`, `C0:A685` | `C0:A37A` | `C3:A1CB` |
| `C3:AB12` | `InitMovementPreset00_06C40015Branch` | `event-bytecode-asset` | `complete` | 7 | `$25 EVENT_SET_PHYSICS_CALLBACK` | `C0:A4BF`, `C0:A685` | `C0:A37A` | `C3:A1DF` |
| `C3:AB26` | `InitAlternatePhysicsVar4WalkPulse` | `event-bytecode-asset` | `complete` | 7 | `$23 EVENT_SET_POSITION_CHANGE_CALLBACK` | - | `C0:A03A`, `C0:9FF1` | `C3:A111` |
| `C3:AB37` | `InitSimpleScreenPositionMovementCallbacks` | `event-script-asset` | `complete` | 5 | `$23 EVENT_SET_POSITION_CHANGE_CALLBACK` | - | `C0:A039`, `C0:A37A`, `C4:8BE1` | - |
| `C3:AB44` | `RefreshActiveEntityDirectionAndVisualProfile` | `event-bytecode-asset` | `complete` | 6 | `$42 EVENT_CALLROUTINE` | `C4:6ADB`, `C4:7044`, `C4:6B0A`, `C0:A65F`, +1 | - | - |
| `C3:AB59` | `WaitForActiveEntityMovementToFinish` | `event-bytecode-label` | `complete` | 6 | `$1A EVENT_SHORTCALL` | `C0:A8DC` | - | `C3:AB44`, `C3:AB5C` |
| `C3:AB67` | `MoveCurrentSlotAwayFromTargetVector` | `event-script-asset` | `complete` | 11 | `$42 EVENT_CALLROUTINE` | `C4:6ADB`, `C4:7044`, `C4:6B0A`, `C4:6B37`, +3 | - | `C3:AB7F` |
| `C3:AB8A` | `WaitUntilPlayerLeavesActiveArea` | `event-bytecode-label` | `complete` | 4 | `$06 EVENT_PAUSE` | `C4:6E74` | - | `C3:AB8A` |
| `C3:AB94` | `WaitUntilPlayerEntersActiveArea` | `event-script-asset` | `complete` | 4 | `$06 EVENT_PAUSE` | `C4:6E74` | - | `C3:AB94` |
| `C3:AB9E` | `LoopRandomWanderInsideActiveArea` | `event-script-asset` | `complete` | 4 | `$42 EVENT_CALLROUTINE` | `C4:7269` | - | `C3:ABAC`, `C3:ABB9` |
| `C3:ABE0` | `WaitUntilWram0028LowByteSet` | `event-script-asset` | `complete` | 5 | `$06 EVENT_PAUSE` | - | - | `C3:ABE0` |
| `C3:AFA3` | `LoopPartyLooksAtActiveEntity` | `event-bytecode-label` | `complete` | 3 | `$42 EVENT_CALLROUTINE` | `C4:8B3B` | - | `C3:AFA3` |
| `C3:B0B6` | `LoopField2B32VerticalOscillation` | `event-script-asset` | `complete` | 19 | `$01 EVENT_LOOP` | `C0:A691`, `C0:A68B` | - | `C3:B0C7` |
| `C3:B431` | `LoopWaitInsideLiveAreaThenRelease` | `event-script-asset` | `complete` | 6 | `$06 EVENT_PAUSE` | `C0:C6B6`, `C0:A857`, `C0:20F1` | - | `C3:B431` |
| `C3:B70C` | `RunFaceTargetShakeByRegistryCount` | `event-script-asset` | `complete` | 27 | `$23 EVENT_SET_POSITION_CHANGE_CALLBACK` | `C0:A685`, `C4:6ADB`, `C4:7044`, `C4:6B0A`, +3 | `C0:A039`, `C0:9FC8`, `C4:8BE1` | `C3:B737` |
| `C3:BAA3` | `RunTunnelGhostOneTextLoop` | `event-script-asset` | `complete` | 9 | `$42 EVENT_CALLROUTINE` | `C0:A82F`, `C0:A88D`, `C0:A943`, `C0:A8C6` | - | `C3:BB5C`, `C3:BB73`, `C3:BAB5` |
| `C3:BAC4` | `RunTunnelGhostWarpTextHalt` | `event-script-asset` | `complete` | 5 | `$42 EVENT_CALLROUTINE` | `C0:A82F`, `C0:A88D` | - | `C3:BB5C`, `C3:BB73` |
| `C3:BAD7` | `RunTunnelGhostThreedWarpTextHalt` | `event-script-asset` | `complete` | 5 | `$42 EVENT_CALLROUTINE` | `C0:A82F`, `C0:A88D` | - | `C3:BB5C`, `C3:BB73` |
| `C3:BB5C` | `PrepareTunnelGhostActiveAreaWindow` | `event-script-asset` | `complete` | 7 | `$1A EVENT_SHORTCALL` | `C0:A4BF`, `C4:6C45` | - | `C3:AAB8`, `C3:AB8A` |
| `C3:BB73` | `TrackPartyMemberForTunnelGhost` | `event-script-asset` | `complete` | 9 | `$0E EVENT_SET_VAR` | `C0:A943`, `C0:A685`, `C0:A8C6` | - | `C3:AB44`, `C3:BB85` |
| `C3:BD03` | `PrepareTunnelGhostAreaWaitAndMovement` | `event-script-asset` | `complete` | 4 | `$1A EVENT_SHORTCALL` | `C0:A4BF` | - | `C3:AAB8`, `C3:AB8A` |
| `C3:BEA4` | `RunDoorCloseTempFlagTextHandoff` | `event-script-asset` | `complete` | 13 | `$0E EVENT_SET_VAR` | `C0:A685`, `C0:AA6E`, `C4:6E46` | - | `C3:AA1E`, `C3:AB59` |
| `C3:BED4` | `RunDoorCloseTempFlagMovementReset` | `event-script-asset` | `complete` | 7 | `$0E EVENT_SET_VAR` | `C0:A685` | - | `C3:AB59` |
| `C3:C143` | `RunStaggeredDoorCloseMovement` | `event-script-asset` | `complete` | 11 | `$28 EVENT_SET_X` | `C0:A685`, `C0:A841` | - | `C3:AA38`, `C3:AA1E` |
| `C3:C1E0` | `RunPositionDoorCloseOpeningPath` | `event-script-asset` | `complete` | 14 | `$1A EVENT_SHORTCALL` | `C0:A685`, `C0:A65F`, `C0:A4BF` | - | `C3:AA38`, `C3:C227`, `C3:AA1E`, `C3:AB59` |
| `C3:C20F` | `RunPositionDoorCloseSoundPath` | `event-script-asset` | `complete` | 6 | `$0E EVENT_SET_VAR` | `C0:A685`, `C0:A841` | - | `C3:AB59` |
| `C3:C227` | `LoopMakePartyLookAtActiveEntity` | `event-script-asset` | `complete` | 4 | `$42 EVENT_CALLROUTINE` | `C4:8B3B`, `C0:A94E` | - | `C3:C227` |
| `C3:C35D` | `InitLeftFacingTempFlagMovementTo15F0_16E8` | `event-script-asset` | `complete` | 15 | `$1A EVENT_SHORTCALL` | `C0:A65F`, `C0:A4BF`, `C0:A84C`, `C0:A685` | - | `C3:AA38`, `C3:C36F`, `C3:AB59` |
| `C3:C810` | `LoopTeleportDestinationOffsetLeft` | `event-script-asset` | `complete` | 3 | `$14 EVENT_BINOP` | - | - | `C3:C810` |
| `C3:C81A` | `LoopTeleportDestinationOffsetRight` | `event-script-asset` | `complete` | 3 | `$14 EVENT_BINOP` | - | - | `C3:C81A` |
| `C3:C824` | `LoopTeleportDestinationOffsetJitter` | `event-script-asset` | `complete` | 35 | `$06 EVENT_PAUSE` | - | - | `C3:C824` |
| `C3:C871` | `LoopTeleportDestinationPausePulse` | `event-script-asset` | `complete` | 26 | `$06 EVENT_PAUSE` | - | - | `C3:C871` |
| `C3:C8FD` | `PrepareTeleportDestinationC3` | `event-script-asset` | `complete` | 4 | `$1A EVENT_SHORTCALL` | `C0:A907`, `C4:6E46` | - | `C3:C94E`, `C3:A204` |
| `C3:C90C` | `RunTeleportDestinationLeftRiseFadeHelper` | `event-script-asset` | `complete` | 21 | `$42 EVENT_CALLROUTINE` | `C0:A864`, `C0:A4BF`, `C0:A685`, `C0:9FBB` | `C4:8C02` | `C3:AB26`, `C3:AA1E`, `C3:ABE0` |
| `C3:C94E` | `RunTeleportDestinationRiseFadeHelper` | `event-script-asset` | `complete` | 21 | `$42 EVENT_CALLROUTINE` | `C0:A864`, `C0:A4BF`, `C0:A685`, `C0:9FBB` | `C4:8C02` | `C3:AB26`, `C3:AA1E`, `C3:ABE0` |
| `C3:CC24` | `RunTeleportFlyoverCoordinatePathA` | `event-script-asset` | `complete` | 16 | `$0E EVENT_SET_VAR` | - | - | `C3:AB59` |
| `C3:CC5C` | `RunTeleportFlyoverCoordinatePathB` | `event-script-asset` | `complete` | 16 | `$0E EVENT_SET_VAR` | - | - | `C3:AB59` |
| `C3:CC94` | `RunTeleportFlyoverOffsetPulseBursts` | `event-script-asset` | `complete` | 10 | `$07 EVENT_START_TASK` | - | - | `C3:C824` |
| `C3:CCA8` | `LoopTeleportFlyoverVerticalBob` | `event-script-asset` | `complete` | 5 | `$2C EVENT_SET_Y_RELATIVE` | - | - | `C3:CCA8` |
| `C3:CEA2` | `LoopSpawnSkyRunnerElectricEffect` | `event-script-asset` | `complete` | 8 | `$06 EVENT_PAUSE` | `C0:A98B` | - | `C3:CEA2` |
| `C3:CEB9` | `LoopSkyRunnerElectricEffectRise` | `event-script-asset` | `complete` | 4 | `$42 EVENT_CALLROUTINE` | `C0:A86F` | - | `C3:CEB9` |
| `C3:D0A4` | `RunFourDirectionVisualCountdownReturn` | `event-script-asset` | `complete` | 9 | `$42 EVENT_CALLROUTINE` | `C0:AA6E` | - | - |
| `C3:D913` | `RunBusTunnelDesertRightTextHalt` | `event-script-asset` | `complete` | 2 | `$42 EVENT_CALLROUTINE` | `C0:A88D` | - | - |
| `C3:DB7A` | `RunBusTunnelBridgeRightTextHandoff` | `event-script-asset` | `complete` | 9 | `$1A EVENT_SHORTCALL` | `C0:A685`, `C0:A907`, `C0:A88D` | - | `C3:DBE0`, `C3:AB59` |
| `C3:DBDB` | `CopyAnchorThenPrepareObscuredSimplePositionActor` | `event-script-asset` | `complete` | 7 | `$42 EVENT_CALLROUTINE` | `C0:A864`, `C0:A679` | `C0:A039`, `C0:9FC8`, `C4:8BE1` | - |
| `C3:DF90` | `RunRightwardLiveAreaTextYieldPath` | `event-script-asset` | `complete` | 11 | `$07 EVENT_START_TASK` | `C0:A651`, `C0:A4BF`, `C0:C6B6`, `C0:20F1`, +2 | - | `C3:DFB5`, `C3:DF9F` |
| `C3:DFB5` | `LoopRandomBounceOrDownwardWaitTask` | `event-script-asset` | `complete` | 5 | `$42 EVENT_CALLROUTINE` | `C0:9F82` | - | `C3:DFD4`, `C3:DFE4` |
| `C3:DFD4` | `ChooseDownwardVelocityAndWaitTimer` | `event-script-asset` | `complete` | 4 | `$40 EVENT_SET_Y_VELOCITY` | `C0:9F82` | - | `C3:DFB5` |

## Decode excerpts

### C3:0195 Event221PaulaFatherFarewellSequence

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `42 4C A8 C0 0C 00 0B AA A2 42 4C A8 C0 0D 00 0A`

```text
C3:0195  42 4C A8 C0 0C 00    EVENT_CALLROUTINE $C0:A84C <ActionScript_TestEventFlag_ReadWord>, event_flag_word=$000C
C3:019B  0B AA A2             EVENT_SHORTCALL_CONDITIONAL_NOT inverted_conditional_call_target=$C3:A2AA <TrafficLightWaitUntilOffscreenAndRelease>
C3:019E  42 4C A8 C0 0D 00    EVENT_CALLROUTINE $C0:A84C <ActionScript_TestEventFlag_ReadWord>, event_flag_word=$000D
C3:01A4  0A AA A2             EVENT_SHORTCALL_CONDITIONAL conditional_call_target=$C3:A2AA <TrafficLightWaitUntilOffscreenAndRelease>
C3:01A7  1A 38 AA             EVENT_SHORTCALL call_target=$C3:AA38 <InitActionScriptMovementState>
C3:01AA  3B FF                EVENT_SET_ANIMATION animation_id=$FF <animation_hidden_or_off>
C3:01AC  42 2F A8 C0          EVENT_CALLROUTINE $C0:A82F <DisableCurrentSlotNeighborCache>
C3:01B0  0E 04 01 00          EVENT_SET_VAR script_var=var4, value_word=$0001
C3:01B4  0E 00 90 1A          EVENT_SET_VAR script_var=var0, value_word=$1A90
C3:01B8  0E 01 60 1E          EVENT_SET_VAR script_var=var1, value_word=$1E60
C3:01BC  0E 02 08 00          EVENT_SET_VAR script_var=var2, value_word=$0008
C3:01C0  0E 03 C0 00          EVENT_SET_VAR script_var=var3, value_word=$00C0
C3:01C4  1A 8A AB             EVENT_SHORTCALL call_target=$C3:AB8A <WaitUntilPlayerLeavesActiveArea>
C3:01C7  28 E8 1A             EVENT_SET_X x_word=$1AE8
C3:01CA  29 68 1E             EVENT_SET_Y y_word=$1E68
C3:01CD  3B 00                EVENT_SET_ANIMATION animation_id=$00 <animation_frame0>
; ... 28 more decoded lines in JSON output
```

### C3:0235 Event222PaulaDoorExitMovementScript

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `15 9A 5D 01 00 0E 06 10 1B 0E 07 88 01 1A 95 02`

```text
C3:0235  15 9A 5D 01 00       EVENT_WRITE_WORD_WRAM wram_addr=$5D9A <queue_pending_or_special_state_flag>, value_word=$0001
C3:023A  0E 06 10 1B          EVENT_SET_VAR script_var=var6, value_word=$1B10
C3:023E  0E 07 88 01          EVENT_SET_VAR script_var=var7, value_word=$0188
C3:0242  1A 95 02             EVENT_SHORTCALL call_target=$C3:0295 <MoveActiveEntityLeftToScriptVarsAndWait>
C3:0245  42 46 6E C4          EVENT_CALLROUTINE $C4:6E46 <SetYieldToTextLatch9641>
C3:0249  09                   EVENT_HALT
```

### C3:024A Event223PaulaPorchExitMovementScript

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `28 E8 1F 29 68 00 0E 06 18 1F 0E 07 68 00 1A 95`

```text
C3:024A  28 E8 1F             EVENT_SET_X x_word=$1FE8
C3:024D  29 68 00             EVENT_SET_Y y_word=$0068
C3:0250  0E 06 18 1F          EVENT_SET_VAR script_var=var6, value_word=$1F18
C3:0254  0E 07 68 00          EVENT_SET_VAR script_var=var7, value_word=$0068
C3:0258  1A 95 02             EVENT_SHORTCALL call_target=$C3:0295 <MoveActiveEntityLeftToScriptVarsAndWait>
C3:025B  42 46 6E C4          EVENT_CALLROUTINE $C4:6E46 <SetYieldToTextLatch9641>
C3:025F  09                   EVENT_HALT
```

### C3:0260 Event224PaulaReturnMovementScript

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `28 D0 1D 29 D8 00 0E 06 80 1D 0E 07 D8 00 1A 95`

```text
C3:0260  28 D0 1D             EVENT_SET_X x_word=$1DD0
C3:0263  29 D8 00             EVENT_SET_Y y_word=$00D8
C3:0266  0E 06 80 1D          EVENT_SET_VAR script_var=var6, value_word=$1D80
C3:026A  0E 07 D8 00          EVENT_SET_VAR script_var=var7, value_word=$00D8
C3:026E  1A 95 02             EVENT_SHORTCALL call_target=$C3:0295 <MoveActiveEntityLeftToScriptVarsAndWait>
C3:0271  42 6E AA C0 02 00    EVENT_CALLROUTINE $C0:AA6E <Script_ApplyCurrentSlotVisualCountdownState>, visual_state_byte=$02 <visual_state_02>, countdown_byte=$00 <visual_countdown_seed_00>
C3:0277  42 46 6E C4          EVENT_CALLROUTINE $C4:6E46 <SetYieldToTextLatch9641>
C3:027B  06 01                EVENT_PAUSE frames=$01
C3:027D  15 9A 5D 00 00       EVENT_WRITE_WORD_WRAM wram_addr=$5D9A <queue_pending_or_special_state_flag>, value_word=$0000
C3:0282  0E 06 D0 1D          EVENT_SET_VAR script_var=var6, value_word=$1DD0
C3:0286  1A 59 AB             EVENT_SHORTCALL call_target=$C3:AB59 <WaitForActiveEntityMovementToFinish>
C3:0289  13                   EVENT_END_LAST_TASK
C3:028A  42 6E AA C0 06 00    EVENT_CALLROUTINE $C0:AA6E <Script_ApplyCurrentSlotVisualCountdownState>, visual_state_byte=$06 <visual_state_06>, countdown_byte=$00 <visual_countdown_seed_00>
C3:0290  42 46 6E C4          EVENT_CALLROUTINE $C4:6E46 <SetYieldToTextLatch9641>
C3:0294  09                   EVENT_HALT
```

### C3:0295 MoveActiveEntityLeftToScriptVarsAndWait

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `1A 38 AA 42 6E AA C0 06 00 42 85 A6 C0 00 01 0E`

```text
C3:0295  1A 38 AA             EVENT_SHORTCALL call_target=$C3:AA38 <InitActionScriptMovementState>
C3:0298  42 6E AA C0 06 00    EVENT_CALLROUTINE $C0:AA6E <Script_ApplyCurrentSlotVisualCountdownState>, visual_state_byte=$06 <visual_state_06>, countdown_byte=$00 <visual_countdown_seed_00>
C3:029E  42 85 A6 C0 00 01    EVENT_CALLROUTINE $C0:A685 <Script_SetCurrentSlotField2B32>, field2b32_word=$0100 <field2b32_step_0100>
C3:02A4  0E 05 01 00          EVENT_SET_VAR script_var=var5, value_word=$0001
C3:02A8  1A 59 AB             EVENT_SHORTCALL call_target=$C3:AB59 <WaitForActiveEntityMovementToFinish>
C3:02AB  1B                   EVENT_SHORT_RETURN
```

### C3:43DB LoopTimedDeliveryDeparturePulseUntilOffscreen

- class: `event-bytecode-label`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `06 08 20 04 0B E8 43 3B 01 42 B2 A4 C0 06 08 3B`

```text
C3:43DB  06 08                EVENT_PAUSE frames=$08
C3:43DD  20 04                EVENT_WRITE_VAR_TO_TEMPVAR script_var=var4
C3:43DF  0B E8 43             EVENT_SHORTCALL_CONDITIONAL_NOT inverted_conditional_call_target=$C3:43E8 <TimedDeliveryDeparturePulseAnimation0Half>
C3:43E2  3B 01                EVENT_SET_ANIMATION animation_id=$01 <animation_frame1>
C3:43E4  42 B2 A4 C0          EVENT_CALLROUTINE $C0:A4B2 <RefreshCurrentSlotVisualProfile_Mode1IfAligned>
C3:43E8  06 08                EVENT_PAUSE frames=$08
C3:43EA  3B 00                EVENT_SET_ANIMATION animation_id=$00 <animation_frame0>
C3:43EC  42 A8 A4 C0          EVENT_CALLROUTINE $C0:A4A8 <RefreshCurrentSlotVisualProfile_Mode0IfAligned>
C3:43F0  42 B6 C6 C0          EVENT_CALLROUTINE $C0:C6B6 <CheckCurrentSlotInsideLiveAreaWindow>
C3:43F4  0B DB 43             EVENT_SHORTCALL_CONDITIONAL_NOT inverted_conditional_call_target=$C3:43DB <LoopTimedDeliveryDeparturePulseUntilOffscreen>
C3:43F7  42 F6 0F EF          EVENT_CALLROUTINE $EF:0FF6 <ResetDeliveryArrivalState>
C3:43FB  42 46 6E C4          EVENT_CALLROUTINE $C4:6E46 <SetYieldToTextLatch9641>
C3:43FF  19 04 A2             EVENT_SHORTJUMP jump_target=$C3:A204 <ReleaseCurrentVisualEntityAndEnd>
```

### C3:43E8 TimedDeliveryDeparturePulseAnimation0Half

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `06 08 3B 00 42 A8 A4 C0 42 B6 C6 C0 0B DB 43 42`

```text
C3:43E8  06 08                EVENT_PAUSE frames=$08
C3:43EA  3B 00                EVENT_SET_ANIMATION animation_id=$00 <animation_frame0>
C3:43EC  42 A8 A4 C0          EVENT_CALLROUTINE $C0:A4A8 <RefreshCurrentSlotVisualProfile_Mode0IfAligned>
C3:43F0  42 B6 C6 C0          EVENT_CALLROUTINE $C0:C6B6 <CheckCurrentSlotInsideLiveAreaWindow>
C3:43F4  0B DB 43             EVENT_SHORTCALL_CONDITIONAL_NOT inverted_conditional_call_target=$C3:43DB <LoopTimedDeliveryDeparturePulseUntilOffscreen>
C3:43F7  42 F6 0F EF          EVENT_CALLROUTINE $EF:0FF6 <ResetDeliveryArrivalState>
C3:43FB  42 46 6E C4          EVENT_CALLROUTINE $C4:6E46 <SetYieldToTextLatch9641>
C3:43FF  19 04 A2             EVENT_SHORTJUMP jump_target=$C3:A204 <ReleaseCurrentVisualEntityAndEnd>
```

### C3:443E TimedDeliveryRetryWaitLoop

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `42 A7 0C EF 0A 7D 44 42 23 0D EF 24 06 3C 02 42`

```text
C3:443E  42 A7 0C EF          EVENT_CALLROUTINE $EF:0CA7 <CheckCurrentDeliveryRetryThreshold>
C3:4442  0A 7D 44             EVENT_SHORTCALL_CONDITIONAL conditional_call_target=$C3:447D <TimedDeliveryFailureTeardown>
C3:4445  42 23 0D EF          EVENT_CALLROUTINE $EF:0D23 <GetCurrentDeliveryRetryWait>
C3:4449  24                   EVENT_LOOP_TEMPVAR
C3:444A  06 3C                EVENT_PAUSE frames=$3C
C3:444C  02                   EVENT_LOOP_END
C3:444D  42 60 0F EF          EVENT_CALLROUTINE $EF:0F60 <CheckDeliveryServiceReadyForArrival>
C3:4451  0A 57 44             EVENT_SHORTCALL_CONDITIONAL conditional_call_target=$C3:4457 <TimedDeliverySuccessGateAndPresentationSetup>
C3:4454  19 3E 44             EVENT_SHORTJUMP jump_target=$C3:443E <TimedDeliveryRetryWaitLoop>
```

### C3:444D TimedDeliveryReadinessGate

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `42 60 0F EF 0A 57 44 19 3E 44 42 9A FF C2 0B 7D`

```text
C3:444D  42 60 0F EF          EVENT_CALLROUTINE $EF:0F60 <CheckDeliveryServiceReadyForArrival>
C3:4451  0A 57 44             EVENT_SHORTCALL_CONDITIONAL conditional_call_target=$C3:4457 <TimedDeliverySuccessGateAndPresentationSetup>
C3:4454  19 3E 44             EVENT_SHORTJUMP jump_target=$C3:443E <TimedDeliveryRetryWaitLoop>
```

### C3:4457 TimedDeliverySuccessGateAndPresentationSetup

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `42 9A FF C2 0B 7D 44 20 00 42 9B C1 C0 0B 3E 44`

```text
C3:4457  42 9A FF C2          EVENT_CALLROUTINE $C2:FF9A <CheckOverworldPositionHashThreshold3Of8>
C3:445B  0B 7D 44             EVENT_SHORTCALL_CONDITIONAL_NOT inverted_conditional_call_target=$C3:447D <TimedDeliveryFailureTeardown>
C3:445E  20 00                EVENT_WRITE_VAR_TO_TEMPVAR script_var=var0
C3:4460  42 9B C1 C0          EVENT_CALLROUTINE $C0:C19B <CopyPathToLane_FromPartyMemberRequest>
C3:4464  0B 3E 44             EVENT_SHORTCALL_CONDITIONAL_NOT inverted_conditional_call_target=$C3:443E <TimedDeliveryRetryWaitLoop>
C3:4467  07 7A 44             EVENT_START_TASK task_script=$C3:447A <StartTimedDeliveryArrivalMovementTask>
C3:446A  06 01                EVENT_PAUSE frames=$01
C3:446C  42 DB 0F EF          EVENT_CALLROUTINE $EF:0FDB <BeginDeliverySuccessArrivalState>
C3:4470  1A 88 44             EVENT_SHORTCALL call_target=$C3:4488 <PrepareTimedDeliveryActorForPresentation>
C3:4473  42 8D 0D EF          EVENT_CALLROUTINE $EF:0D8D <QueueCurrentDeliveryPointer1>
C3:4477  19 A8 44             EVENT_SHORTJUMP jump_target=$C3:44A8 <RunTimedDeliveryDepartureMovement>
```

### C3:447A StartTimedDeliveryArrivalMovementTask

- class: `event-bytecode-label`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `1A DE 44 42 F6 0F EF 42 FA 0D EF 19 04 A2 3B 00`

```text
C3:447A  1A DE 44             EVENT_SHORTCALL call_target=$C3:44DE <RunTimedDeliveryArrivalMovement>
C3:447D  42 F6 0F EF          EVENT_CALLROUTINE $EF:0FF6 <ResetDeliveryArrivalState>
C3:4481  42 FA 0D EF          EVENT_CALLROUTINE $EF:0DFA <QueueCurrentDeliveryPointer2>
C3:4485  19 04 A2             EVENT_SHORTJUMP jump_target=$C3:A204 <ReleaseCurrentVisualEntityAndEnd>
```

### C3:447D TimedDeliveryFailureTeardown

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `42 F6 0F EF 42 FA 0D EF 19 04 A2 3B 00 07 9F A0`

```text
C3:447D  42 F6 0F EF          EVENT_CALLROUTINE $EF:0FF6 <ResetDeliveryArrivalState>
C3:4481  42 FA 0D EF          EVENT_CALLROUTINE $EF:0DFA <QueueCurrentDeliveryPointer2>
C3:4485  19 04 A2             EVENT_SHORTJUMP jump_target=$C3:A204 <ReleaseCurrentVisualEntityAndEnd>
```

### C3:4488 PrepareTimedDeliveryActorForPresentation

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `3B 00 07 9F A0 42 BF A4 C0 0E 02 16 00 0E 03 16`

```text
C3:4488  3B 00                EVENT_SET_ANIMATION animation_id=$00 <animation_frame0>
C3:448A  07 9F A0             EVENT_START_TASK task_script=$C3:A09F <LoopActiveEntityWalkAnimationPulse>
C3:448D  42 BF A4 C0          EVENT_CALLROUTINE $C0:A4BF <RefreshCurrentSlotVisualProfile_Mode0>
C3:4491  0E 02 16 00          EVENT_SET_VAR script_var=var2, value_word=$0016
C3:4495  0E 03 16 00          EVENT_SET_VAR script_var=var3, value_word=$0016
C3:4499  06 01                EVENT_PAUSE frames=$01
C3:449B  20 04                EVENT_WRITE_VAR_TO_TEMPVAR script_var=var4
C3:449D  0B A7 44             EVENT_SHORTCALL_CONDITIONAL_NOT inverted_conditional_call_target=$C3:44A7 <ReturnFromTimedDeliveryActorPrep>
C3:44A0  42 F8 6E C4          EVENT_CALLROUTINE $C4:6EF8 <CheckCurrentSlotWithinPlayerProximityThreshold>
C3:44A4  0A 99 44             EVENT_SHORTCALL_CONDITIONAL conditional_call_target=$C3:4499 <WaitTimedDeliveryActorPresentationPrep>
C3:44A7  1B                   EVENT_SHORT_RETURN
```

### C3:4499 WaitTimedDeliveryActorPresentationPrep

- class: `event-bytecode-label`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `06 01 20 04 0B A7 44 42 F8 6E C4 0A 99 44 1B 39`

```text
C3:4499  06 01                EVENT_PAUSE frames=$01
C3:449B  20 04                EVENT_WRITE_VAR_TO_TEMPVAR script_var=var4
C3:449D  0B A7 44             EVENT_SHORTCALL_CONDITIONAL_NOT inverted_conditional_call_target=$C3:44A7 <ReturnFromTimedDeliveryActorPrep>
C3:44A0  42 F8 6E C4          EVENT_CALLROUTINE $C4:6EF8 <CheckCurrentSlotWithinPlayerProximityThreshold>
C3:44A4  0A 99 44             EVENT_SHORTCALL_CONDITIONAL conditional_call_target=$C3:4499 <WaitTimedDeliveryActorPresentationPrep>
C3:44A7  1B                   EVENT_SHORT_RETURN
```

### C3:44A7 ReturnFromTimedDeliveryActorPrep

- class: `event-bytecode-label`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `1B 39 06 01 13 13 07 DB 43 20 00 42 51 C2 C0 0B`

```text
C3:44A7  1B                   EVENT_SHORT_RETURN
```

### C3:44A8 RunTimedDeliveryDepartureMovement

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `39 06 01 13 13 07 DB 43 20 00 42 51 C2 C0 0B D2`

```text
C3:44A8  39                   EVENT_SET_VELOCITIES_ZERO
C3:44A9  06 01                EVENT_PAUSE frames=$01
C3:44AB  13                   EVENT_END_LAST_TASK
C3:44AC  13                   EVENT_END_LAST_TASK
C3:44AD  07 DB 43             EVENT_START_TASK task_script=$C3:43DB <LoopTimedDeliveryDeparturePulseUntilOffscreen>
C3:44B0  20 00                EVENT_WRITE_VAR_TO_TEMPVAR script_var=var0
C3:44B2  42 51 C2 C0          EVENT_CALLROUTINE $C0:C251 <CopyPathToLane_FromCurrentEntityRequestReverse>
C3:44B6  0B D2 44             EVENT_SHORTCALL_CONDITIONAL_NOT inverted_conditional_call_target=$C3:44D2 <FinishTimedDeliveryDepartureAndYieldText>
C3:44B9  42 8A 0E EF          EVENT_CALLROUTINE $EF:0E8A <GetCurrentDeliveryExitSpeed>
C3:44BD  42 8B A6 C0          EVENT_CALLROUTINE $C0:A68B <StoreAInCurrentSlotField2B32>
C3:44C1  42 8F D9 C0          EVENT_CALLROUTINE $C0:D98F <Export_CurrentSlotAttentionTarget>
C3:44C5  0A D2 44             EVENT_SHORTCALL_CONDITIONAL conditional_call_target=$C3:44D2 <FinishTimedDeliveryDepartureAndYieldText>
C3:44C8  1A 59 AB             EVENT_SHORTCALL call_target=$C3:AB59 <WaitForActiveEntityMovementToFinish>
C3:44CB  42 87 6C C4          EVENT_CALLROUTINE $C4:6C87 <RestoreCurrentSlotAnchorFromCachedTarget>
C3:44CF  19 C1 44             EVENT_SHORTJUMP jump_target=$C3:44C1 <LoopTimedDeliveryDepartureMovement>
```

### C3:44C1 LoopTimedDeliveryDepartureMovement

- class: `event-bytecode-label`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `42 8F D9 C0 0A D2 44 1A 59 AB 42 87 6C C4 19 C1`

```text
C3:44C1  42 8F D9 C0          EVENT_CALLROUTINE $C0:D98F <Export_CurrentSlotAttentionTarget>
C3:44C5  0A D2 44             EVENT_SHORTCALL_CONDITIONAL conditional_call_target=$C3:44D2 <FinishTimedDeliveryDepartureAndYieldText>
C3:44C8  1A 59 AB             EVENT_SHORTCALL call_target=$C3:AB59 <WaitForActiveEntityMovementToFinish>
C3:44CB  42 87 6C C4          EVENT_CALLROUTINE $C4:6C87 <RestoreCurrentSlotAnchorFromCachedTarget>
C3:44CF  19 C1 44             EVENT_SHORTJUMP jump_target=$C3:44C1 <LoopTimedDeliveryDepartureMovement>
```

### C3:44D2 FinishTimedDeliveryDepartureAndYieldText

- class: `event-bytecode-label`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `39 42 F6 0F EF 42 46 6E C4 19 04 A2 42 67 0E EF`

```text
C3:44D2  39                   EVENT_SET_VELOCITIES_ZERO
C3:44D3  42 F6 0F EF          EVENT_CALLROUTINE $EF:0FF6 <ResetDeliveryArrivalState>
C3:44D7  42 46 6E C4          EVENT_CALLROUTINE $C4:6E46 <SetYieldToTextLatch9641>
C3:44DB  19 04 A2             EVENT_SHORTJUMP jump_target=$C3:A204 <ReleaseCurrentVisualEntityAndEnd>
```

### C3:44DE RunTimedDeliveryArrivalMovement

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `42 67 0E EF 42 8B A6 C0 0E 05 03 00 0E 04 00 00`

```text
C3:44DE  42 67 0E EF          EVENT_CALLROUTINE $EF:0E67 <GetCurrentDeliveryEnterSpeed>
C3:44E2  42 8B A6 C0          EVENT_CALLROUTINE $C0:A68B <StoreAInCurrentSlotField2B32>
C3:44E6  0E 05 03 00          EVENT_SET_VAR script_var=var5, value_word=$0003
C3:44EA  0E 04 00 00          EVENT_SET_VAR script_var=var4, value_word=$0000
C3:44EE  42 8F D9 C0          EVENT_CALLROUTINE $C0:D98F <Export_CurrentSlotAttentionTarget>
C3:44F2  0A FF 44             EVENT_SHORTCALL_CONDITIONAL conditional_call_target=$C3:44FF <HoldTimedDeliveryArrivalCompletion>
C3:44F5  1A 59 AB             EVENT_SHORTCALL call_target=$C3:AB59 <WaitForActiveEntityMovementToFinish>
C3:44F8  42 87 6C C4          EVENT_CALLROUTINE $C4:6C87 <RestoreCurrentSlotAnchorFromCachedTarget>
C3:44FC  19 EE 44             EVENT_SHORTJUMP jump_target=$C3:44EE <LoopTimedDeliveryArrivalMovement>
```

### C3:44EE LoopTimedDeliveryArrivalMovement

- class: `event-bytecode-label`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `42 8F D9 C0 0A FF 44 1A 59 AB 42 87 6C C4 19 EE`

```text
C3:44EE  42 8F D9 C0          EVENT_CALLROUTINE $C0:D98F <Export_CurrentSlotAttentionTarget>
C3:44F2  0A FF 44             EVENT_SHORTCALL_CONDITIONAL conditional_call_target=$C3:44FF <HoldTimedDeliveryArrivalCompletion>
C3:44F5  1A 59 AB             EVENT_SHORTCALL call_target=$C3:AB59 <WaitForActiveEntityMovementToFinish>
C3:44F8  42 87 6C C4          EVENT_CALLROUTINE $C4:6C87 <RestoreCurrentSlotAnchorFromCachedTarget>
C3:44FC  19 EE 44             EVENT_SHORTJUMP jump_target=$C3:44EE <LoopTimedDeliveryArrivalMovement>
```

### C3:44FF HoldTimedDeliveryArrivalCompletion

- class: `event-bytecode-label`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `0E 04 01 00 06 F0 19 FF 44 42 64 A8 C0 FF 25 C8`

```text
C3:44FF  0E 04 01 00          EVENT_SET_VAR script_var=var4, value_word=$0001
C3:4503  06 F0                EVENT_PAUSE frames=$F0
C3:4505  19 FF 44             EVENT_SHORTJUMP jump_target=$C3:44FF <HoldTimedDeliveryArrivalCompletion>
```

### C3:A043 IntroCutsceneCameraPanGate

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `42 D3 FF C1 0A 4E A0 42 00 01 C3 08 00 52 C0 01`

```text
C3:A043  42 D3 FF C1          EVENT_CALLROUTINE $C1:FFD3 <ComputeBankC1ChecksumTail>
C3:A047  0A 4E A0             EVENT_SHORTCALL_CONDITIONAL conditional_call_target=$C3:A04E <StartIntroCameraPanTickLoop>
C3:A04A  42 00 01 C3          EVENT_CALLROUTINE $C3:0100 <DisplayAntiPiracyScreen>
C3:A04E  08 00 52 C0          EVENT_SET_TICK_CALLBACK tick_callback=$C0:5200 <Tick_OverworldPlayerPositionAndCallbacks>
C3:A052  01 06                EVENT_LOOP count=$06
C3:A054  06 C8                EVENT_PAUSE frames=$C8
C3:A056  02                   EVENT_LOOP_END
C3:A057  42 00 00 C2          EVENT_CALLROUTINE $C2:0000 <RunEnemySunstrokeCheck>
C3:A05B  19 52 A0             EVENT_SHORTJUMP jump_target=$C3:A052 <LoopIntroCameraPanWaitAndC2Step>
```

### C3:A04E StartIntroCameraPanTickLoop

- class: `event-bytecode-label`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `08 00 52 C0 01 06 06 C8 02 42 00 00 C2 19 52 A0`

```text
C3:A04E  08 00 52 C0          EVENT_SET_TICK_CALLBACK tick_callback=$C0:5200 <Tick_OverworldPlayerPositionAndCallbacks>
C3:A052  01 06                EVENT_LOOP count=$06
C3:A054  06 C8                EVENT_PAUSE frames=$C8
C3:A056  02                   EVENT_LOOP_END
C3:A057  42 00 00 C2          EVENT_CALLROUTINE $C2:0000 <RunEnemySunstrokeCheck>
C3:A05B  19 52 A0             EVENT_SHORTJUMP jump_target=$C3:A052 <LoopIntroCameraPanWaitAndC2Step>
```

### C3:A052 LoopIntroCameraPanWaitAndC2Step

- class: `event-bytecode-label`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `01 06 06 C8 02 42 00 00 C2 19 52 A0 23 39 A0 25`

```text
C3:A052  01 06                EVENT_LOOP count=$06
C3:A054  06 C8                EVENT_PAUSE frames=$C8
C3:A056  02                   EVENT_LOOP_END
C3:A057  42 00 00 C2          EVENT_CALLROUTINE $C2:0000 <RunEnemySunstrokeCheck>
C3:A05B  19 52 A0             EVENT_SHORTJUMP jump_target=$C3:A052 <LoopIntroCameraPanWaitAndC2Step>
```

### C3:A05E IntroCutsceneSpriteObjectSetup

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `23 39 A0 25 6B A2 3B 00 42 AA 3D C0 42 F0 4E C0`

```text
C3:A05E  23 39 A0             EVENT_SET_POSITION_CHANGE_CALLBACK position_change_callback=$C0:A039 <ReturnFromPositionChangeCallback_NoProjection>
C3:A061  25 6B A2             EVENT_SET_PHYSICS_CALLBACK physics_callback=$C0:A26B <PhysicsCallback_TargetContextCompareAndProject>
C3:A064  3B 00                EVENT_SET_ANIMATION animation_id=$00 <animation_frame0>
C3:A066  42 AA 3D C0          EVENT_CALLROUTINE $C0:3DAA <Sync_CurrentSlotToPartyCharacterRecord>
C3:A06A  42 F0 4E C0          EVENT_CALLROUTINE $C0:4EF0 <Restore_CurrentSlotFromSnapshotRecord>
C3:A06E  42 DA A6 C0          EVENT_CALLROUTINE $C0:A6DA <ClearCurrentSlotNeighborCache>
C3:A072  08 78 4D C0          EVENT_SET_TICK_CALLBACK tick_callback=$C0:4D78 <Tick_Event2SnapshotObjectReconcile>
C3:A076  42 E3 A6 C0          EVENT_CALLROUTINE $C0:A6E3 <WatchAndRefreshCompanionVisualPhase>
C3:A07A  06 01                EVENT_PAUSE frames=$01
C3:A07C  19 76 A0             EVENT_SHORTJUMP jump_target=$C3:A076 <LoopIntroCompanionVisualRefresh>
```

### C3:A076 LoopIntroCompanionVisualRefresh

- class: `event-bytecode-label`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `42 E3 A6 C0 06 01 19 76 A0 09 23 39 A0 25 6B A2`

```text
C3:A076  42 E3 A6 C0          EVENT_CALLROUTINE $C0:A6E3 <WatchAndRefreshCompanionVisualPhase>
C3:A07A  06 01                EVENT_PAUSE frames=$01
C3:A07C  19 76 A0             EVENT_SHORTJUMP jump_target=$C3:A076 <LoopIntroCompanionVisualRefresh>
```

### C3:A07F HaltEventScript

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `09 23 39 A0 25 6B A2 3B 00 42 7D 02 EF 08 1E 03`

```text
C3:A07F  09                   EVENT_HALT
```

### C3:A09F LoopActiveEntityWalkAnimationPulse

- class: `event-bytecode-label`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `06 08 3B 01 42 B2 A4 C0 06 08 3B 00 42 A8 A4 C0`

```text
C3:A09F  06 08                EVENT_PAUSE frames=$08
C3:A0A1  3B 01                EVENT_SET_ANIMATION animation_id=$01 <animation_frame1>
C3:A0A3  42 B2 A4 C0          EVENT_CALLROUTINE $C0:A4B2 <RefreshCurrentSlotVisualProfile_Mode1IfAligned>
C3:A0A7  06 08                EVENT_PAUSE frames=$08
C3:A0A9  3B 00                EVENT_SET_ANIMATION animation_id=$00 <animation_frame0>
C3:A0AB  42 A8 A4 C0          EVENT_CALLROUTINE $C0:A4A8 <RefreshCurrentSlotVisualProfile_Mode0IfAligned>
C3:A0AF  19 9F A0             EVENT_SHORTJUMP jump_target=$C3:A09F <LoopActiveEntityWalkAnimationPulse>
```

### C3:A0B2 LoopActiveEntityWalkPulse24Frame

- class: `event-bytecode-label`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `06 18 3B 01 42 B2 A4 C0 06 18 3B 00 42 A8 A4 C0`

```text
C3:A0B2  06 18                EVENT_PAUSE frames=$18
C3:A0B4  3B 01                EVENT_SET_ANIMATION animation_id=$01 <animation_frame1>
C3:A0B6  42 B2 A4 C0          EVENT_CALLROUTINE $C0:A4B2 <RefreshCurrentSlotVisualProfile_Mode1IfAligned>
C3:A0BA  06 18                EVENT_PAUSE frames=$18
C3:A0BC  3B 00                EVENT_SET_ANIMATION animation_id=$00 <animation_frame0>
C3:A0BE  42 A8 A4 C0          EVENT_CALLROUTINE $C0:A4A8 <RefreshCurrentSlotVisualProfile_Mode0IfAligned>
C3:A0C2  19 B2 A0             EVENT_SHORTJUMP jump_target=$C3:A0B2 <LoopActiveEntityWalkPulse24Frame>
```

### C3:A0C5 LoopActiveEntityWalkPulse12Frame

- class: `event-bytecode-label`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `06 0C 3B 01 42 B2 A4 C0 06 0C 3B 00 42 A8 A4 C0`

```text
C3:A0C5  06 0C                EVENT_PAUSE frames=$0C
C3:A0C7  3B 01                EVENT_SET_ANIMATION animation_id=$01 <animation_frame1>
C3:A0C9  42 B2 A4 C0          EVENT_CALLROUTINE $C0:A4B2 <RefreshCurrentSlotVisualProfile_Mode1IfAligned>
C3:A0CD  06 0C                EVENT_PAUSE frames=$0C
C3:A0CF  3B 00                EVENT_SET_ANIMATION animation_id=$00 <animation_frame0>
C3:A0D1  42 A8 A4 C0          EVENT_CALLROUTINE $C0:A4A8 <RefreshCurrentSlotVisualProfile_Mode0IfAligned>
C3:A0D5  19 C5 A0             EVENT_SHORTJUMP jump_target=$C3:A0C5 <LoopActiveEntityWalkPulse12Frame>
```

### C3:A0D8 LoopActiveEntityWalkPulse9FrameConditional

- class: `event-bytecode-label`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `06 09 3B 01 42 B2 A4 C0 06 09 3B 00 42 A8 A4 C0`

```text
C3:A0D8  06 09                EVENT_PAUSE frames=$09
C3:A0DA  3B 01                EVENT_SET_ANIMATION animation_id=$01 <animation_frame1>
C3:A0DC  42 B2 A4 C0          EVENT_CALLROUTINE $C0:A4B2 <RefreshCurrentSlotVisualProfile_Mode1IfAligned>
C3:A0E0  06 09                EVENT_PAUSE frames=$09
C3:A0E2  3B 00                EVENT_SET_ANIMATION animation_id=$00 <animation_frame0>
C3:A0E4  42 A8 A4 C0          EVENT_CALLROUTINE $C0:A4A8 <RefreshCurrentSlotVisualProfile_Mode0IfAligned>
C3:A0E8  0B D8 A0             EVENT_SHORTCALL_CONDITIONAL_NOT inverted_conditional_call_target=$C3:A0D8 <LoopActiveEntityWalkPulse9FrameConditional>
C3:A0EB  06 06                EVENT_PAUSE frames=$06
C3:A0ED  3B 01                EVENT_SET_ANIMATION animation_id=$01 <animation_frame1>
C3:A0EF  42 B2 A4 C0          EVENT_CALLROUTINE $C0:A4B2 <RefreshCurrentSlotVisualProfile_Mode1IfAligned>
C3:A0F3  06 06                EVENT_PAUSE frames=$06
C3:A0F5  3B 00                EVENT_SET_ANIMATION animation_id=$00 <animation_frame0>
C3:A0F7  42 A8 A4 C0          EVENT_CALLROUTINE $C0:A4A8 <RefreshCurrentSlotVisualProfile_Mode0IfAligned>
C3:A0FB  0B EB A0             EVENT_SHORTCALL_CONDITIONAL_NOT inverted_conditional_call_target=$C3:A0EB <LoopActiveEntityWalkPulse6FrameConditional>
C3:A0FE  06 02                EVENT_PAUSE frames=$02
C3:A100  3B 01                EVENT_SET_ANIMATION animation_id=$01 <animation_frame1>
; ... 16 more decoded lines in JSON output
```

### C3:A0EB LoopActiveEntityWalkPulse6FrameConditional

- class: `event-bytecode-label`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `06 06 3B 01 42 B2 A4 C0 06 06 3B 00 42 A8 A4 C0`

```text
C3:A0EB  06 06                EVENT_PAUSE frames=$06
C3:A0ED  3B 01                EVENT_SET_ANIMATION animation_id=$01 <animation_frame1>
C3:A0EF  42 B2 A4 C0          EVENT_CALLROUTINE $C0:A4B2 <RefreshCurrentSlotVisualProfile_Mode1IfAligned>
C3:A0F3  06 06                EVENT_PAUSE frames=$06
C3:A0F5  3B 00                EVENT_SET_ANIMATION animation_id=$00 <animation_frame0>
C3:A0F7  42 A8 A4 C0          EVENT_CALLROUTINE $C0:A4A8 <RefreshCurrentSlotVisualProfile_Mode0IfAligned>
C3:A0FB  0B EB A0             EVENT_SHORTCALL_CONDITIONAL_NOT inverted_conditional_call_target=$C3:A0EB <LoopActiveEntityWalkPulse6FrameConditional>
C3:A0FE  06 02                EVENT_PAUSE frames=$02
C3:A100  3B 01                EVENT_SET_ANIMATION animation_id=$01 <animation_frame1>
C3:A102  42 B2 A4 C0          EVENT_CALLROUTINE $C0:A4B2 <RefreshCurrentSlotVisualProfile_Mode1IfAligned>
C3:A106  06 02                EVENT_PAUSE frames=$02
C3:A108  3B 00                EVENT_SET_ANIMATION animation_id=$00 <animation_frame0>
C3:A10A  42 A8 A4 C0          EVENT_CALLROUTINE $C0:A4A8 <RefreshCurrentSlotVisualProfile_Mode0IfAligned>
C3:A10E  0B FE A0             EVENT_SHORTCALL_CONDITIONAL_NOT inverted_conditional_call_target=$C3:A0FE <LoopActiveEntityWalkPulse2FrameConditional>
C3:A111  06 08                EVENT_PAUSE frames=$08
C3:A113  20 04                EVENT_WRITE_VAR_TO_TEMPVAR script_var=var4
; ... 9 more decoded lines in JSON output
```

### C3:A0FE LoopActiveEntityWalkPulse2FrameConditional

- class: `event-bytecode-label`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `06 02 3B 01 42 B2 A4 C0 06 02 3B 00 42 A8 A4 C0`

```text
C3:A0FE  06 02                EVENT_PAUSE frames=$02
C3:A100  3B 01                EVENT_SET_ANIMATION animation_id=$01 <animation_frame1>
C3:A102  42 B2 A4 C0          EVENT_CALLROUTINE $C0:A4B2 <RefreshCurrentSlotVisualProfile_Mode1IfAligned>
C3:A106  06 02                EVENT_PAUSE frames=$02
C3:A108  3B 00                EVENT_SET_ANIMATION animation_id=$00 <animation_frame0>
C3:A10A  42 A8 A4 C0          EVENT_CALLROUTINE $C0:A4A8 <RefreshCurrentSlotVisualProfile_Mode0IfAligned>
C3:A10E  0B FE A0             EVENT_SHORTCALL_CONDITIONAL_NOT inverted_conditional_call_target=$C3:A0FE <LoopActiveEntityWalkPulse2FrameConditional>
C3:A111  06 08                EVENT_PAUSE frames=$08
C3:A113  20 04                EVENT_WRITE_VAR_TO_TEMPVAR script_var=var4
C3:A115  0B 1E A1             EVENT_SHORTCALL_CONDITIONAL_NOT inverted_conditional_call_target=$C3:A11E <LoopActiveEntityWalkPulseVar4Gate_OffHalf>
C3:A118  3B 01                EVENT_SET_ANIMATION animation_id=$01 <animation_frame1>
C3:A11A  42 B2 A4 C0          EVENT_CALLROUTINE $C0:A4B2 <RefreshCurrentSlotVisualProfile_Mode1IfAligned>
C3:A11E  06 08                EVENT_PAUSE frames=$08
C3:A120  20 04                EVENT_WRITE_VAR_TO_TEMPVAR script_var=var4
C3:A122  0B 11 A1             EVENT_SHORTCALL_CONDITIONAL_NOT inverted_conditional_call_target=$C3:A111 <LoopActiveEntityWalkPulseVar4Gate>
C3:A125  3B 00                EVENT_SET_ANIMATION animation_id=$00 <animation_frame0>
; ... 2 more decoded lines in JSON output
```

### C3:A111 LoopActiveEntityWalkPulseVar4Gate

- class: `event-bytecode-label`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `06 08 20 04 0B 1E A1 3B 01 42 B2 A4 C0 06 08 20`

```text
C3:A111  06 08                EVENT_PAUSE frames=$08
C3:A113  20 04                EVENT_WRITE_VAR_TO_TEMPVAR script_var=var4
C3:A115  0B 1E A1             EVENT_SHORTCALL_CONDITIONAL_NOT inverted_conditional_call_target=$C3:A11E <LoopActiveEntityWalkPulseVar4Gate_OffHalf>
C3:A118  3B 01                EVENT_SET_ANIMATION animation_id=$01 <animation_frame1>
C3:A11A  42 B2 A4 C0          EVENT_CALLROUTINE $C0:A4B2 <RefreshCurrentSlotVisualProfile_Mode1IfAligned>
C3:A11E  06 08                EVENT_PAUSE frames=$08
C3:A120  20 04                EVENT_WRITE_VAR_TO_TEMPVAR script_var=var4
C3:A122  0B 11 A1             EVENT_SHORTCALL_CONDITIONAL_NOT inverted_conditional_call_target=$C3:A111 <LoopActiveEntityWalkPulseVar4Gate>
C3:A125  3B 00                EVENT_SET_ANIMATION animation_id=$00 <animation_frame0>
C3:A127  42 A8 A4 C0          EVENT_CALLROUTINE $C0:A4A8 <RefreshCurrentSlotVisualProfile_Mode0IfAligned>
C3:A12B  19 11 A1             EVENT_SHORTJUMP jump_target=$C3:A111 <LoopActiveEntityWalkPulseVar4Gate>
```

### C3:A12E LoopActiveEntityWalkPulseVar4Countdown

- class: `event-bytecode-label`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `20 04 0A 59 A1 24 06 01 20 04 16 59 A1 02 3B 01`

```text
C3:A12E  20 04                EVENT_WRITE_VAR_TO_TEMPVAR script_var=var4
C3:A130  0A 59 A1             EVENT_SHORTCALL_CONDITIONAL conditional_call_target=$C3:A159 <LoopActiveEntityWalkPulseVar4Countdown_WaitAndRestart>
C3:A133  24                   EVENT_LOOP_TEMPVAR
C3:A134  06 01                EVENT_PAUSE frames=$01
C3:A136  20 04                EVENT_WRITE_VAR_TO_TEMPVAR script_var=var4
C3:A138  16 59 A1             EVENT_BREAK_IF_FALSE break_target=$C3:A159 <LoopActiveEntityWalkPulseVar4Countdown_WaitAndRestart>
C3:A13B  02                   EVENT_LOOP_END
C3:A13C  3B 01                EVENT_SET_ANIMATION animation_id=$01 <animation_frame1>
C3:A13E  42 B2 A4 C0          EVENT_CALLROUTINE $C0:A4B2 <RefreshCurrentSlotVisualProfile_Mode1IfAligned>
C3:A142  20 04                EVENT_WRITE_VAR_TO_TEMPVAR script_var=var4
C3:A144  0A 59 A1             EVENT_SHORTCALL_CONDITIONAL conditional_call_target=$C3:A159 <LoopActiveEntityWalkPulseVar4Countdown_WaitAndRestart>
C3:A147  24                   EVENT_LOOP_TEMPVAR
C3:A148  06 01                EVENT_PAUSE frames=$01
C3:A14A  20 04                EVENT_WRITE_VAR_TO_TEMPVAR script_var=var4
C3:A14C  16 59 A1             EVENT_BREAK_IF_FALSE break_target=$C3:A159 <LoopActiveEntityWalkPulseVar4Countdown_WaitAndRestart>
C3:A14F  02                   EVENT_LOOP_END
; ... 3 more decoded lines in JSON output
```

### C3:A15E LoopC40015Var4GatedPulseUntilRelease

- class: `event-bytecode-label`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `42 23 00 C4 06 08 20 04 0B 6F A1 3B 01 42 B2 A4`

```text
C3:A15E  42 23 00 C4          EVENT_CALLROUTINE $C4:0023 <StoreLowNibble1a42ToCurrentScriptField1372>
C3:A162  06 08                EVENT_PAUSE frames=$08
C3:A164  20 04                EVENT_WRITE_VAR_TO_TEMPVAR script_var=var4
C3:A166  0B 6F A1             EVENT_SHORTCALL_CONDITIONAL_NOT inverted_conditional_call_target=$C3:A16F <LoopC40015Var4GatedPulseUntilRelease_CheckRelease>
C3:A169  3B 01                EVENT_SET_ANIMATION animation_id=$01 <animation_frame1>
C3:A16B  42 B2 A4 C0          EVENT_CALLROUTINE $C0:A4B2 <RefreshCurrentSlotVisualProfile_Mode1IfAligned>
C3:A16F  06 08                EVENT_PAUSE frames=$08
C3:A171  42 15 00 C4          EVENT_CALLROUTINE $C4:0015 <ClearCurrentSlot10f2RefreshVisualAndCheckLiveArea>
C3:A175  0B 62 A1             EVENT_SHORTCALL_CONDITIONAL_NOT inverted_conditional_call_target=$C3:A162 <LoopC40015Var4GatedPulseUntilRelease_Loop>
C3:A178  19 04 A2             EVENT_SHORTJUMP jump_target=$C3:A204 <ReleaseCurrentVisualEntityAndEnd>
```

### C3:A17B LoopC40015SlowPulseUntilRelease

- class: `event-bytecode-label`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `06 18 3B 01 42 B2 A4 C0 06 30 42 15 00 C4 0B 7B`

```text
C3:A17B  06 18                EVENT_PAUSE frames=$18
C3:A17D  3B 01                EVENT_SET_ANIMATION animation_id=$01 <animation_frame1>
C3:A17F  42 B2 A4 C0          EVENT_CALLROUTINE $C0:A4B2 <RefreshCurrentSlotVisualProfile_Mode1IfAligned>
C3:A183  06 30                EVENT_PAUSE frames=$30
C3:A185  42 15 00 C4          EVENT_CALLROUTINE $C4:0015 <ClearCurrentSlot10f2RefreshVisualAndCheckLiveArea>
C3:A189  0B 7B A1             EVENT_SHORTCALL_CONDITIONAL_NOT inverted_conditional_call_target=$C3:A17B <LoopC40015SlowPulseUntilRelease>
C3:A18C  19 04 A2             EVENT_SHORTJUMP jump_target=$C3:A204 <ReleaseCurrentVisualEntityAndEnd>
```

### C3:A18F LoopC40015FastPulseUntilRelease

- class: `event-bytecode-label`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `06 18 3B 01 42 B2 A4 C0 06 18 42 15 00 C4 0B 8F`

```text
C3:A18F  06 18                EVENT_PAUSE frames=$18
C3:A191  3B 01                EVENT_SET_ANIMATION animation_id=$01 <animation_frame1>
C3:A193  42 B2 A4 C0          EVENT_CALLROUTINE $C0:A4B2 <RefreshCurrentSlotVisualProfile_Mode1IfAligned>
C3:A197  06 18                EVENT_PAUSE frames=$18
C3:A199  42 15 00 C4          EVENT_CALLROUTINE $C4:0015 <ClearCurrentSlot10f2RefreshVisualAndCheckLiveArea>
C3:A19D  0B 8F A1             EVENT_SHORTCALL_CONDITIONAL_NOT inverted_conditional_call_target=$C3:A18F <LoopC40015FastPulseUntilRelease>
C3:A1A0  19 04 A2             EVENT_SHORTJUMP jump_target=$C3:A204 <ReleaseCurrentVisualEntityAndEnd>
```

### C3:A1DF LoopActiveEntityWalkPulse2FrameC40015Branch

- class: `event-bytecode-label`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `06 02 3B 01 42 B2 A4 C0 06 02 42 15 00 C4 0B FE`

```text
C3:A1DF  06 02                EVENT_PAUSE frames=$02
C3:A1E1  3B 01                EVENT_SET_ANIMATION animation_id=$01 <animation_frame1>
C3:A1E3  42 B2 A4 C0          EVENT_CALLROUTINE $C0:A4B2 <RefreshCurrentSlotVisualProfile_Mode1IfAligned>
C3:A1E7  06 02                EVENT_PAUSE frames=$02
C3:A1E9  42 15 00 C4          EVENT_CALLROUTINE $C4:0015 <ClearCurrentSlot10f2RefreshVisualAndCheckLiveArea>
C3:A1ED  0B FE A0             EVENT_SHORTCALL_CONDITIONAL_NOT inverted_conditional_call_target=$C3:A0FE <LoopActiveEntityWalkPulse2FrameConditional>
C3:A1F0  19 04 A2             EVENT_SHORTJUMP jump_target=$C3:A204 <ReleaseCurrentVisualEntityAndEnd>
```

### C3:A1F3 LoopC40015Pulse16FrameUntilRelease

- class: `event-bytecode-label`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `06 10 3B 01 42 B2 A4 C0 06 10 42 15 00 C4 0B F3`

```text
C3:A1F3  06 10                EVENT_PAUSE frames=$10
C3:A1F5  3B 01                EVENT_SET_ANIMATION animation_id=$01 <animation_frame1>
C3:A1F7  42 B2 A4 C0          EVENT_CALLROUTINE $C0:A4B2 <RefreshCurrentSlotVisualProfile_Mode1IfAligned>
C3:A1FB  06 10                EVENT_PAUSE frames=$10
C3:A1FD  42 15 00 C4          EVENT_CALLROUTINE $C4:0015 <ClearCurrentSlot10f2RefreshVisualAndCheckLiveArea>
C3:A201  0B F3 A1             EVENT_SHORTCALL_CONDITIONAL_NOT inverted_conditional_call_target=$C3:A1F3 <LoopC40015Pulse16FrameUntilRelease>
C3:A204  42 F1 20 C0          EVENT_CALLROUTINE $C0:20F1 <ScriptRelease_CurrentEntityVisualState>
C3:A208  00                   EVENT_END
```

### C3:A204 ReleaseCurrentVisualEntityAndEnd

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `42 F1 20 C0 00 06 04 19 04 A2 3B 00 42 A8 A4 C0`

```text
C3:A204  42 F1 20 C0          EVENT_CALLROUTINE $C0:20F1 <ScriptRelease_CurrentEntityVisualState>
C3:A208  00                   EVENT_END
```

### C3:A209 DelayThenReleaseCurrentVisualEntity

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `06 04 19 04 A2 3B 00 42 A8 A4 C0 20 00 11 05 2C`

```text
C3:A209  06 04                EVENT_PAUSE frames=$04
C3:A20B  19 04 A2             EVENT_SHORTJUMP jump_target=$C3:A204 <ReleaseCurrentVisualEntityAndEnd>
```

### C3:A20E LoopVar0SelectedAnimationUntilOffscreen

- class: `event-bytecode-label`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `3B 00 42 A8 A4 C0 20 00 11 05 2C A2 34 A2 3D A2`

```text
C3:A20E  3B 00                EVENT_SET_ANIMATION animation_id=$00 <animation_frame0>
C3:A210  42 A8 A4 C0          EVENT_CALLROUTINE $C0:A4A8 <RefreshCurrentSlotVisualProfile_Mode0IfAligned>
C3:A214  20 00                EVENT_WRITE_VAR_TO_TEMPVAR script_var=var0
C3:A216  11 05 2C A2 34 A2 3D A2 4E A2 5F A2 EVENT_SWITCH_CALL_TEMPVAR switch_call_targets=count=5 [$C3:A22C <Var0AnimationCase0Pulse8FrameOn>, $C3:A234 <Var0AnimationCase1Pulse8FrameOff>, $C3:A23D <Var0AnimationCase2Pulse4Frame>, $C3:A24E <Var0AnimationCase3Pulse32Frame>, $C3:A25F <Var0AnimationCase4Wait16Frame>]
C3:A222  42 B6 C6 C0          EVENT_CALLROUTINE $C0:C6B6 <CheckCurrentSlotInsideLiveAreaWindow>
C3:A226  0B 14 A2             EVENT_SHORTCALL_CONDITIONAL_NOT inverted_conditional_call_target=$C3:A214 <LoopVar0SelectedAnimationBody>
C3:A229  19 7C A4             EVENT_SHORTJUMP jump_target=$C3:A47C <ReleaseCurrentVisualEntityTail>
```

### C3:A22C Var0AnimationCase0Pulse8FrameOn

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `06 08 3B 01 42 B2 A4 C0 06 08 3B 00 42 A8 A4 C0`

```text
C3:A22C  06 08                EVENT_PAUSE frames=$08
C3:A22E  3B 01                EVENT_SET_ANIMATION animation_id=$01 <animation_frame1>
C3:A230  42 B2 A4 C0          EVENT_CALLROUTINE $C0:A4B2 <RefreshCurrentSlotVisualProfile_Mode1IfAligned>
C3:A234  06 08                EVENT_PAUSE frames=$08
C3:A236  3B 00                EVENT_SET_ANIMATION animation_id=$00 <animation_frame0>
C3:A238  42 A8 A4 C0          EVENT_CALLROUTINE $C0:A4A8 <RefreshCurrentSlotVisualProfile_Mode0IfAligned>
C3:A23C  1B                   EVENT_SHORT_RETURN
```

### C3:A234 Var0AnimationCase1Pulse8FrameOff

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `06 08 3B 00 42 A8 A4 C0 1B 06 04 3B 01 42 B2 A4`

```text
C3:A234  06 08                EVENT_PAUSE frames=$08
C3:A236  3B 00                EVENT_SET_ANIMATION animation_id=$00 <animation_frame0>
C3:A238  42 A8 A4 C0          EVENT_CALLROUTINE $C0:A4A8 <RefreshCurrentSlotVisualProfile_Mode0IfAligned>
C3:A23C  1B                   EVENT_SHORT_RETURN
```

### C3:A23D Var0AnimationCase2Pulse4Frame

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `06 04 3B 01 42 B2 A4 C0 06 04 3B 00 42 A8 A4 C0`

```text
C3:A23D  06 04                EVENT_PAUSE frames=$04
C3:A23F  3B 01                EVENT_SET_ANIMATION animation_id=$01 <animation_frame1>
C3:A241  42 B2 A4 C0          EVENT_CALLROUTINE $C0:A4B2 <RefreshCurrentSlotVisualProfile_Mode1IfAligned>
C3:A245  06 04                EVENT_PAUSE frames=$04
C3:A247  3B 00                EVENT_SET_ANIMATION animation_id=$00 <animation_frame0>
C3:A249  42 A8 A4 C0          EVENT_CALLROUTINE $C0:A4A8 <RefreshCurrentSlotVisualProfile_Mode0IfAligned>
C3:A24D  1B                   EVENT_SHORT_RETURN
```

### C3:A24E Var0AnimationCase3Pulse32Frame

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `06 20 3B 01 42 B2 A4 C0 06 20 3B 00 42 A8 A4 C0`

```text
C3:A24E  06 20                EVENT_PAUSE frames=$20
C3:A250  3B 01                EVENT_SET_ANIMATION animation_id=$01 <animation_frame1>
C3:A252  42 B2 A4 C0          EVENT_CALLROUTINE $C0:A4B2 <RefreshCurrentSlotVisualProfile_Mode1IfAligned>
C3:A256  06 20                EVENT_PAUSE frames=$20
C3:A258  3B 00                EVENT_SET_ANIMATION animation_id=$00 <animation_frame0>
C3:A25A  42 A8 A4 C0          EVENT_CALLROUTINE $C0:A4A8 <RefreshCurrentSlotVisualProfile_Mode0IfAligned>
C3:A25E  1B                   EVENT_SHORT_RETURN
```

### C3:A25F Var0AnimationCase4Wait16Frame

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `06 10 1B 42 DA A6 C0 42 76 5E C0 F1 A6 64 C0 19`

```text
C3:A25F  06 10                EVENT_PAUSE frames=$10
C3:A261  1B                   EVENT_SHORT_RETURN
```

### C3:A262 LoopActiveEntityCollisionProbeRefresh

- class: `event-bytecode-label`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `42 DA A6 C0 42 76 5E C0 F1 A6 64 C0 19 66 A2 0C`

```text
C3:A262  42 DA A6 C0          EVENT_CALLROUTINE $C0:A6DA <ClearCurrentSlotNeighborCache>
C3:A266  42 76 5E C0 F1 A6 64 C0 EVENT_CALLROUTINE $C0:5E76 <Update_CurrentSlotCollisionCache>, collision_probe_mode_byte=$F1, neighbor_cache_callback_long=$C0:64A6 <Update_CurrentSlotNeighborCache_Broad>
C3:A26E  19 66 A2             EVENT_SHORTJUMP jump_target=$C3:A266 <LoopCollisionProbeRefresh>
```

### C3:A2AA TrafficLightWaitUntilOffscreenAndRelease

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `25 F0 9F 3B 00 39 42 DB C7 C0 42 BF A4 C0 06 08`

```text
C3:A2AA  25 F0 9F             EVENT_SET_PHYSICS_CALLBACK physics_callback=$C0:9FF0 <ReturnFromPhysicsCallback_NoMovement>
C3:A2AD  3B 00                EVENT_SET_ANIMATION animation_id=$00 <animation_frame0>
C3:A2AF  39                   EVENT_SET_VELOCITIES_ZERO
C3:A2B0  42 DB C7 C0          EVENT_CALLROUTINE $C0:C7DB <UpdateCurrentSlotFootprintMask>
C3:A2B4  42 BF A4 C0          EVENT_CALLROUTINE $C0:A4BF <RefreshCurrentSlotVisualProfile_Mode0>
C3:A2B8  06 08                EVENT_PAUSE frames=$08
C3:A2BA  42 B6 C6 C0          EVENT_CALLROUTINE $C0:C6B6 <CheckCurrentSlotInsideLiveAreaWindow>
C3:A2BE  0B B8 A2             EVENT_SHORTCALL_CONDITIONAL_NOT inverted_conditional_call_target=$C3:A2B8 <Event8_Entry2WaitUntilOffscreenRelease>
C3:A2C1  42 F1 20 C0          EVENT_CALLROUTINE $C0:20F1 <ScriptRelease_CurrentEntityVisualState>
C3:A2C5  00                   EVENT_END
```

### C3:A381 InitRandomWanderMovementWithCollisionProbe

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `25 60 A3 3B 00 07 11 A1 07 62 A2 42 BF A4 C0 42`

```text
C3:A381  25 60 A3             EVENT_SET_PHYSICS_CALLBACK physics_callback=$C0:A360 <UpdatePosition_WhenNoNeighbor_WithSpriteRefresh>
C3:A384  3B 00                EVENT_SET_ANIMATION animation_id=$00 <animation_frame0>
C3:A386  07 11 A1             EVENT_START_TASK task_script=$C3:A111 <LoopActiveEntityWalkPulseVar4Gate>
C3:A389  07 62 A2             EVENT_START_TASK task_script=$C3:A262 <LoopActiveEntityCollisionProbeRefresh>
C3:A38C  42 BF A4 C0          EVENT_CALLROUTINE $C0:A4BF <RefreshCurrentSlotVisualProfile_Mode0>
C3:A390  42 85 A6 C0 00 01    EVENT_CALLROUTINE $C0:A685 <Script_SetCurrentSlotField2B32>, field2b32_word=$0100 <field2b32_step_0100>
C3:A396  42 64 A9 C0 08 00 08 00 EVENT_CALLROUTINE $C0:A964 <SetCurrentSlotAreaBoundsFromRadii_ReadTwoWords>, radius_x_word=$0008, radius_y_word=$0008
C3:A39E  19 B7 A3             EVENT_SHORTJUMP jump_target=$C3:A3B7 <LoopRandomDirectionMovementWithRandomWait>
```

### C3:A3A1 InitC40015PulseWithCollisionProbe

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `25 60 A3 3B 00 07 5E A1 07 62 A2 42 BF A4 C0 42`

```text
C3:A3A1  25 60 A3             EVENT_SET_PHYSICS_CALLBACK physics_callback=$C0:A360 <UpdatePosition_WhenNoNeighbor_WithSpriteRefresh>
C3:A3A4  3B 00                EVENT_SET_ANIMATION animation_id=$00 <animation_frame0>
C3:A3A6  07 5E A1             EVENT_START_TASK task_script=$C3:A15E <LoopC40015Var4GatedPulseUntilRelease>
C3:A3A9  07 62 A2             EVENT_START_TASK task_script=$C3:A262 <LoopActiveEntityCollisionProbeRefresh>
C3:A3AC  42 BF A4 C0          EVENT_CALLROUTINE $C0:A4BF <RefreshCurrentSlotVisualProfile_Mode0>
C3:A3B0  42 85 A6 C0 00 01    EVENT_CALLROUTINE $C0:A685 <Script_SetCurrentSlotField2B32>, field2b32_word=$0100 <field2b32_step_0100>
C3:A3B6  1B                   EVENT_SHORT_RETURN
```

### C3:A3B7 LoopRandomDirectionMovementWithRandomWait

- class: `event-bytecode-label`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `0E 04 00 00 42 69 72 C4 0A C9 A3 27 02 FF FF 19`

```text
C3:A3B7  0E 04 00 00          EVENT_SET_VAR script_var=var4, value_word=$0000
C3:A3BB  42 69 72 C4          EVENT_CALLROUTINE $C4:7269 <ClassifyCurrentSlotAgainstAreaBounds>
C3:A3BF  0A C9 A3             EVENT_SHORTCALL_CONDITIONAL conditional_call_target=$C3:A3C9 <ChooseRandomCardinalDirection>
C3:A3C2  27 02 FF FF          EVENT_BINOP_TEMPVAR operation_byte=$02 <ADD>, value_word=$FFFF
C3:A3C6  19 D6 A3             EVENT_SHORTJUMP jump_target=$C3:A3D6 <ApplyRandomDirectionAndMovementTimer>
```

### C3:A3C9 ChooseRandomCardinalDirection

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `42 82 9F C0 04 00 00 02 00 04 00 06 00 42 5F A6`

```text
C3:A3C9  42 82 9F C0 04 00 00 02 00 04 00 06 00 EVENT_CALLROUTINE $C0:9F82 <ChooseRandomScriptWord>, choices=4 [$0000, $0002, $0004, $0006]
C3:A3D6  42 5F A6 C0          EVENT_CALLROUTINE $C0:A65F <SetCurrentSlotDirectionClassIfActive>
C3:A3DA  42 3B C8 C0          EVENT_CALLROUTINE $C0:C83B <InstallScriptMovementVectorFromDirection>
C3:A3DE  42 82 9F C0 02 08 00 10 00 EVENT_CALLROUTINE $C0:9F82 <ChooseRandomScriptWord>, choices=2 [$0008, $0010]
C3:A3E7  42 4E CA C0          EVENT_CALLROUTINE $C0:CA4E <SetMovementTaskTimerFromActiveVector>
C3:A3EB  39                   EVENT_SET_VELOCITIES_ZERO
C3:A3EC  0E 04 01 00          EVENT_SET_VAR script_var=var4, value_word=$0001
C3:A3F0  42 82 9F C0 04 1E 00 3C 00 5A 00 78 00 EVENT_CALLROUTINE $C0:9F82 <ChooseRandomScriptWord>, choices=4 [$001E, $003C, $005A, $0078]
C3:A3FD  44                   EVENT_WRITE_TEMPVAR_WAITTIMER
C3:A3FE  19 B7 A3             EVENT_SHORTJUMP jump_target=$C3:A3B7 <LoopRandomDirectionMovementWithRandomWait>
```

### C3:A3D6 ApplyRandomDirectionAndMovementTimer

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `42 5F A6 C0 42 3B C8 C0 42 82 9F C0 02 08 00 10`

```text
C3:A3D6  42 5F A6 C0          EVENT_CALLROUTINE $C0:A65F <SetCurrentSlotDirectionClassIfActive>
C3:A3DA  42 3B C8 C0          EVENT_CALLROUTINE $C0:C83B <InstallScriptMovementVectorFromDirection>
C3:A3DE  42 82 9F C0 02 08 00 10 00 EVENT_CALLROUTINE $C0:9F82 <ChooseRandomScriptWord>, choices=2 [$0008, $0010]
C3:A3E7  42 4E CA C0          EVENT_CALLROUTINE $C0:CA4E <SetMovementTaskTimerFromActiveVector>
C3:A3EB  39                   EVENT_SET_VELOCITIES_ZERO
C3:A3EC  0E 04 01 00          EVENT_SET_VAR script_var=var4, value_word=$0001
C3:A3F0  42 82 9F C0 04 1E 00 3C 00 5A 00 78 00 EVENT_CALLROUTINE $C0:9F82 <ChooseRandomScriptWord>, choices=4 [$001E, $003C, $005A, $0078]
C3:A3FD  44                   EVENT_WRITE_TEMPVAR_WAITTIMER
C3:A3FE  19 B7 A3             EVENT_SHORTJUMP jump_target=$C3:A3B7 <LoopRandomDirectionMovementWithRandomWait>
```

### C3:A3E7 SetMovementTimerThenRandomWait

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `42 4E CA C0 39 0E 04 01 00 42 82 9F C0 04 1E 00`

```text
C3:A3E7  42 4E CA C0          EVENT_CALLROUTINE $C0:CA4E <SetMovementTaskTimerFromActiveVector>
C3:A3EB  39                   EVENT_SET_VELOCITIES_ZERO
C3:A3EC  0E 04 01 00          EVENT_SET_VAR script_var=var4, value_word=$0001
C3:A3F0  42 82 9F C0 04 1E 00 3C 00 5A 00 78 00 EVENT_CALLROUTINE $C0:9F82 <ChooseRandomScriptWord>, choices=4 [$001E, $003C, $005A, $0078]
C3:A3FD  44                   EVENT_WRITE_TEMPVAR_WAITTIMER
C3:A3FE  19 B7 A3             EVENT_SHORTJUMP jump_target=$C3:A3B7 <LoopRandomDirectionMovementWithRandomWait>
```

### C3:A401 InitNpcAttentionPathIfNoCachedNeighbor

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `25 F0 9F 42 DA A6 C0 06 01 42 B8 A6 C0 0B 25 A4`

```text
C3:A401  25 F0 9F             EVENT_SET_PHYSICS_CALLBACK physics_callback=$C0:9FF0 <ReturnFromPhysicsCallback_NoMovement>
C3:A404  42 DA A6 C0          EVENT_CALLROUTINE $C0:A6DA <ClearCurrentSlotNeighborCache>
C3:A408  06 01                EVENT_PAUSE frames=$01
C3:A40A  42 B8 A6 C0          EVENT_CALLROUTINE $C0:A6B8 <GetCurrentSlotHasNoCachedNeighborFlag>
C3:A40E  0B 25 A4             EVENT_SHORTCALL_CONDITIONAL_NOT inverted_conditional_call_target=$C3:A425 <ReturnFromNpcAttentionNeighborCacheCheck>
C3:A411  08 F7 D7 C0          EVENT_SET_TICK_CALLBACK tick_callback=$C0:D7F7 <Consume_CurrentSlotAttentionPath>
C3:A415  25 60 A3             EVENT_SET_PHYSICS_CALLBACK physics_callback=$C0:A360 <UpdatePosition_WhenNoNeighbor_WithSpriteRefresh>
C3:A418  3B 00                EVENT_SET_ANIMATION animation_id=$00 <animation_frame0>
C3:A41A  42 BF A4 C0          EVENT_CALLROUTINE $C0:A4BF <RefreshCurrentSlotVisualProfile_Mode0>
C3:A41E  0E 00 00 00          EVENT_SET_VAR script_var=var0, value_word=$0000
C3:A422  07 0E A2             EVENT_START_TASK task_script=$C3:A20E <LoopVar0SelectedAnimationUntilOffscreen>
C3:A425  1B                   EVENT_SHORT_RETURN
```

### C3:A426 StartNpcAttentionTerrainCollisionLoop

- class: `event-bytecode-label`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `1A 01 A4 07 34 A4 1B 1A 01 A4 07 48 A4 1B 42 78`

```text
C3:A426  1A 01 A4             EVENT_SHORTCALL call_target=$C3:A401 <InitNpcAttentionPathIfNoCachedNeighbor>
C3:A429  07 34 A4             EVENT_START_TASK task_script=$C3:A434 <LoopNpcAttentionTerrainCollision>
C3:A42C  1B                   EVENT_SHORT_RETURN
```

### C3:A42D StartNpcAttentionHorizontalCollisionLoop

- class: `event-bytecode-label`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `1A 01 A4 07 48 A4 1B 42 78 64 C0 42 82 5E C0 42`

```text
C3:A42D  1A 01 A4             EVENT_SHORTCALL call_target=$C3:A401 <InitNpcAttentionPathIfNoCachedNeighbor>
C3:A430  07 48 A4             EVENT_START_TASK task_script=$C3:A448 <LoopNpcAttentionHorizontalCollision>
C3:A433  1B                   EVENT_SHORT_RETURN
```

### C3:A434 LoopNpcAttentionTerrainCollision

- class: `event-bytecode-label`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `42 78 64 C0 42 82 5E C0 42 B0 D5 C0 0B 5C A4 06`

```text
C3:A434  42 78 64 C0          EVENT_CALLROUTINE $C0:6478 <Update_CurrentSlotNeighborCache_Priority>
C3:A438  42 82 5E C0          EVENT_CALLROUTINE $C0:5E82 <Update_CurrentSlotCollisionCache_WithTerrainCompatibility>
C3:A43C  42 B0 D5 C0          EVENT_CALLROUTINE $C0:D5B0 <Gate_NpcAttentionCoordinatorFromScript>
C3:A440  0B 5C A4             EVENT_SHORTCALL_CONDITIONAL_NOT inverted_conditional_call_target=$C3:A45C <FinishNpcAttentionAndReleaseActor>
C3:A443  06 01                EVENT_PAUSE frames=$01
C3:A445  19 34 A4             EVENT_SHORTJUMP jump_target=$C3:A434 <LoopNpcAttentionTerrainCollision>
```

### C3:A448 LoopNpcAttentionHorizontalCollision

- class: `event-bytecode-label`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `42 78 64 C0 42 CE 5E C0 42 B0 D5 C0 0B 5C A4 06`

```text
C3:A448  42 78 64 C0          EVENT_CALLROUTINE $C0:6478 <Update_CurrentSlotNeighborCache_Priority>
C3:A44C  42 CE 5E C0          EVENT_CALLROUTINE $C0:5ECE <Update_CurrentSlotCollisionCache_FromHorizontalEdges>
C3:A450  42 B0 D5 C0          EVENT_CALLROUTINE $C0:D5B0 <Gate_NpcAttentionCoordinatorFromScript>
C3:A454  0B 5C A4             EVENT_SHORTCALL_CONDITIONAL_NOT inverted_conditional_call_target=$C3:A45C <FinishNpcAttentionAndReleaseActor>
C3:A457  06 01                EVENT_PAUSE frames=$01
C3:A459  19 48 A4             EVENT_SHORTJUMP jump_target=$C3:A448 <LoopNpcAttentionHorizontalCollision>
```

### C3:A45C FinishNpcAttentionAndReleaseActor

- class: `event-bytecode-label`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `06 01 42 9B D5 C0 0B 5C A4 3B 00 39 25 F0 9F 0E`

```text
C3:A45C  06 01                EVENT_PAUSE frames=$01
C3:A45E  42 9B D5 C0          EVENT_CALLROUTINE $C0:D59B <Check_NpcAttentionCoordinatorActive>
C3:A462  0B 5C A4             EVENT_SHORTCALL_CONDITIONAL_NOT inverted_conditional_call_target=$C3:A45C <FinishNpcAttentionAndReleaseActor>
C3:A465  3B 00                EVENT_SET_ANIMATION animation_id=$00 <animation_frame0>
C3:A467  39                   EVENT_SET_VELOCITIES_ZERO
C3:A468  25 F0 9F             EVENT_SET_PHYSICS_CALLBACK physics_callback=$C0:9FF0 <ReturnFromPhysicsCallback_NoMovement>
C3:A46B  0E 00 01 00          EVENT_SET_VAR script_var=var0, value_word=$0001
C3:A46F  06 01                EVENT_PAUSE frames=$01
C3:A471  01 03                EVENT_LOOP count=$03
C3:A473  3B FF                EVENT_SET_ANIMATION animation_id=$FF <animation_hidden_or_off>
C3:A475  06 05                EVENT_PAUSE frames=$05
C3:A477  3B 00                EVENT_SET_ANIMATION animation_id=$00 <animation_frame0>
C3:A479  06 05                EVENT_PAUSE frames=$05
C3:A47B  02                   EVENT_LOOP_END
C3:A47C  42 F1 20 C0          EVENT_CALLROUTINE $C0:20F1 <ScriptRelease_CurrentEntityVisualState>
C3:A480  00                   EVENT_END
```

### C3:A47C ReleaseCurrentVisualEntityTail

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `42 F1 20 C0 00 42 BF A4 C0 3B 00 19 5C A4 1A 26`

```text
C3:A47C  42 F1 20 C0          EVENT_CALLROUTINE $C0:20F1 <ScriptRelease_CurrentEntityVisualState>
C3:A480  00                   EVENT_END
```

### C3:AA38 InitActionScriptMovementState

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `25 7A A3 3B 00 07 11 A1 39 0E 04 00 00 1B 25 7A`

```text
C3:AA38  25 7A A3             EVENT_SET_PHYSICS_CALLBACK physics_callback=$C0:A37A <UpdatePosition_WhenNoNeighbor_WithSpriteRefresh_CurrentSlot>
C3:AA3B  3B 00                EVENT_SET_ANIMATION animation_id=$00 <animation_frame0>
C3:AA3D  07 11 A1             EVENT_START_TASK task_script=$C3:A111 <LoopActiveEntityWalkPulseVar4Gate>
C3:AA40  39                   EVENT_SET_VELOCITIES_ZERO
C3:AA41  0E 04 00 00          EVENT_SET_VAR script_var=var4, value_word=$0000
C3:AA45  1B                   EVENT_SHORT_RETURN
```

### C3:AA46 InitMovementPreset40_00Pulse24Frame

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `25 7A A3 3B 00 07 B2 A0 39 42 BF A4 C0 42 85 A6`

```text
C3:AA46  25 7A A3             EVENT_SET_PHYSICS_CALLBACK physics_callback=$C0:A37A <UpdatePosition_WhenNoNeighbor_WithSpriteRefresh_CurrentSlot>
C3:AA49  3B 00                EVENT_SET_ANIMATION animation_id=$00 <animation_frame0>
C3:AA4B  07 B2 A0             EVENT_START_TASK task_script=$C3:A0B2 <LoopActiveEntityWalkPulse24Frame>
C3:AA4E  39                   EVENT_SET_VELOCITIES_ZERO
C3:AA4F  42 BF A4 C0          EVENT_CALLROUTINE $C0:A4BF <RefreshCurrentSlotVisualProfile_Mode0>
C3:AA53  42 85 A6 C0 40 00    EVENT_CALLROUTINE $C0:A685 <Script_SetCurrentSlotField2B32>, field2b32_word=$0040 <field2b32_step_0040>
C3:AA59  1B                   EVENT_SHORT_RETURN
```

### C3:AA5A InitMovementPreset00_01Pulse12Frame

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `25 7A A3 3B 00 07 C5 A0 39 42 BF A4 C0 42 85 A6`

```text
C3:AA5A  25 7A A3             EVENT_SET_PHYSICS_CALLBACK physics_callback=$C0:A37A <UpdatePosition_WhenNoNeighbor_WithSpriteRefresh_CurrentSlot>
C3:AA5D  3B 00                EVENT_SET_ANIMATION animation_id=$00 <animation_frame0>
C3:AA5F  07 C5 A0             EVENT_START_TASK task_script=$C3:A0C5 <LoopActiveEntityWalkPulse12Frame>
C3:AA62  39                   EVENT_SET_VELOCITIES_ZERO
C3:AA63  42 BF A4 C0          EVENT_CALLROUTINE $C0:A4BF <RefreshCurrentSlotVisualProfile_Mode0>
C3:AA67  42 85 A6 C0 00 01    EVENT_CALLROUTINE $C0:A685 <Script_SetCurrentSlotField2B32>, field2b32_word=$0100 <field2b32_step_0100>
C3:AA6D  1B                   EVENT_SHORT_RETURN
```

### C3:AA6E InitMovementPreset60_01Pulse9Frame

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `25 7A A3 3B 00 07 D8 A0 39 42 BF A4 C0 42 85 A6`

```text
C3:AA6E  25 7A A3             EVENT_SET_PHYSICS_CALLBACK physics_callback=$C0:A37A <UpdatePosition_WhenNoNeighbor_WithSpriteRefresh_CurrentSlot>
C3:AA71  3B 00                EVENT_SET_ANIMATION animation_id=$00 <animation_frame0>
C3:AA73  07 D8 A0             EVENT_START_TASK task_script=$C3:A0D8 <LoopActiveEntityWalkPulse9FrameConditional>
C3:AA76  39                   EVENT_SET_VELOCITIES_ZERO
C3:AA77  42 BF A4 C0          EVENT_CALLROUTINE $C0:A4BF <RefreshCurrentSlotVisualProfile_Mode0>
C3:AA7B  42 85 A6 C0 60 01    EVENT_CALLROUTINE $C0:A685 <Script_SetCurrentSlotField2B32>, field2b32_word=$0160 <field2b32_step_0160>
C3:AA81  1B                   EVENT_SHORT_RETURN
```

### C3:AA82 InitMovementPreset00_02Pulse6Frame

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `25 7A A3 3B 00 07 EB A0 39 42 BF A4 C0 42 85 A6`

```text
C3:AA82  25 7A A3             EVENT_SET_PHYSICS_CALLBACK physics_callback=$C0:A37A <UpdatePosition_WhenNoNeighbor_WithSpriteRefresh_CurrentSlot>
C3:AA85  3B 00                EVENT_SET_ANIMATION animation_id=$00 <animation_frame0>
C3:AA87  07 EB A0             EVENT_START_TASK task_script=$C3:A0EB <LoopActiveEntityWalkPulse6FrameConditional>
C3:AA8A  39                   EVENT_SET_VELOCITIES_ZERO
C3:AA8B  42 BF A4 C0          EVENT_CALLROUTINE $C0:A4BF <RefreshCurrentSlotVisualProfile_Mode0>
C3:AA8F  42 85 A6 C0 00 02    EVENT_CALLROUTINE $C0:A685 <Script_SetCurrentSlotField2B32>, field2b32_word=$0200 <field2b32_step_0200>
C3:AA95  1B                   EVENT_SHORT_RETURN
```

### C3:AA96 InitMovementPreset00_06Pulse2Frame

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `25 7A A3 3B 00 07 FE A0 39 42 BF A4 C0 42 85 A6`

```text
C3:AA96  25 7A A3             EVENT_SET_PHYSICS_CALLBACK physics_callback=$C0:A37A <UpdatePosition_WhenNoNeighbor_WithSpriteRefresh_CurrentSlot>
C3:AA99  3B 00                EVENT_SET_ANIMATION animation_id=$00 <animation_frame0>
C3:AA9B  07 FE A0             EVENT_START_TASK task_script=$C3:A0FE <LoopActiveEntityWalkPulse2FrameConditional>
C3:AA9E  39                   EVENT_SET_VELOCITIES_ZERO
C3:AA9F  42 BF A4 C0          EVENT_CALLROUTINE $C0:A4BF <RefreshCurrentSlotVisualProfile_Mode0>
C3:AAA3  42 85 A6 C0 00 06    EVENT_CALLROUTINE $C0:A685 <Script_SetCurrentSlotField2B32>, field2b32_word=$0600 <field2b32_step_0600>
C3:AAA9  1B                   EVENT_SHORT_RETURN
```

### C3:AAAA InitMovementPresetVar4Countdown

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `25 7A A3 3B 00 07 2E A1 39 0E 04 0C 00 1B 25 7A`

```text
C3:AAAA  25 7A A3             EVENT_SET_PHYSICS_CALLBACK physics_callback=$C0:A37A <UpdatePosition_WhenNoNeighbor_WithSpriteRefresh_CurrentSlot>
C3:AAAD  3B 00                EVENT_SET_ANIMATION animation_id=$00 <animation_frame0>
C3:AAAF  07 2E A1             EVENT_START_TASK task_script=$C3:A12E <LoopActiveEntityWalkPulseVar4Countdown>
C3:AAB2  39                   EVENT_SET_VELOCITIES_ZERO
C3:AAB3  0E 04 0C 00          EVENT_SET_VAR script_var=var4, value_word=$000C
C3:AAB7  1B                   EVENT_SHORT_RETURN
```

### C3:AB12 InitMovementPreset00_06C40015Branch

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `25 7A A3 3B 00 07 DF A1 39 42 BF A4 C0 42 85 A6`

```text
C3:AB12  25 7A A3             EVENT_SET_PHYSICS_CALLBACK physics_callback=$C0:A37A <UpdatePosition_WhenNoNeighbor_WithSpriteRefresh_CurrentSlot>
C3:AB15  3B 00                EVENT_SET_ANIMATION animation_id=$00 <animation_frame0>
C3:AB17  07 DF A1             EVENT_START_TASK task_script=$C3:A1DF <LoopActiveEntityWalkPulse2FrameC40015Branch>
C3:AB1A  39                   EVENT_SET_VELOCITIES_ZERO
C3:AB1B  42 BF A4 C0          EVENT_CALLROUTINE $C0:A4BF <RefreshCurrentSlotVisualProfile_Mode0>
C3:AB1F  42 85 A6 C0 00 06    EVENT_CALLROUTINE $C0:A685 <Script_SetCurrentSlotField2B32>, field2b32_word=$0600 <field2b32_step_0600>
C3:AB25  1B                   EVENT_SHORT_RETURN
```

### C3:AB26 InitAlternatePhysicsVar4WalkPulse

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `23 3A A0 25 F1 9F 3B 00 07 11 A1 39 0E 04 00 00`

```text
C3:AB26  23 3A A0             EVENT_SET_POSITION_CHANGE_CALLBACK position_change_callback=$C0:A03A <ProjectWorldToScreen_FromCamera31AndHeight>
C3:AB29  25 F1 9F             EVENT_SET_PHYSICS_CALLBACK physics_callback=$C0:9FF1 <Integrate_XYAndZVelocity_WithSpriteRefresh>
C3:AB2C  3B 00                EVENT_SET_ANIMATION animation_id=$00 <animation_frame0>
C3:AB2E  07 11 A1             EVENT_START_TASK task_script=$C3:A111 <LoopActiveEntityWalkPulseVar4Gate>
C3:AB31  39                   EVENT_SET_VELOCITIES_ZERO
C3:AB32  0E 04 00 00          EVENT_SET_VAR script_var=var4, value_word=$0000
C3:AB36  1B                   EVENT_SHORT_RETURN
```

### C3:AB44 RefreshActiveEntityDirectionAndVisualProfile

- class: `event-bytecode-asset`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `42 DB 6A C4 42 44 70 C4 42 0A 6B C4 42 5F A6 C0`

```text
C3:AB44  42 DB 6A C4          EVENT_CALLROUTINE $C4:6ADB <ComputeCurrentSlotTargetDirectionOctant>
C3:AB48  42 44 70 C4          EVENT_CALLROUTINE $C4:7044 <ProjectAngleIntoCurrentSlotVectorWords>
C3:AB4C  42 0A 6B C4          EVENT_CALLROUTINE $C4:6B0A <RoundAngleToOctantAndCacheCurrentSlot>
C3:AB50  42 5F A6 C0          EVENT_CALLROUTINE $C0:A65F <SetCurrentSlotDirectionClassIfActive>
C3:AB54  42 BF A4 C0          EVENT_CALLROUTINE $C0:A4BF <RefreshCurrentSlotVisualProfile_Mode0>
C3:AB58  1B                   EVENT_SHORT_RETURN
```

### C3:AB59 WaitForActiveEntityMovementToFinish

- class: `event-bytecode-label`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `1A 44 AB 06 01 42 DC A8 C0 0A 5C AB 39 1B 42 DB`

```text
C3:AB59  1A 44 AB             EVENT_SHORTCALL call_target=$C3:AB44 <RefreshActiveEntityDirectionAndVisualProfile>
C3:AB5C  06 01                EVENT_PAUSE frames=$01
C3:AB5E  42 DC A8 C0          EVENT_CALLROUTINE $C0:A8DC <StepCurrentSlotTowardCachedTarget_NoFacingRefresh>
C3:AB62  0A 5C AB             EVENT_SHORTCALL_CONDITIONAL conditional_call_target=$C3:AB5C <LoopWaitForActiveEntityMovementToFinish>
C3:AB65  39                   EVENT_SET_VELOCITIES_ZERO
C3:AB66  1B                   EVENT_SHORT_RETURN
```

### C3:AB8A WaitUntilPlayerLeavesActiveArea

- class: `event-bytecode-label`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `06 01 42 74 6E C4 0A 8A AB 1B 06 01 42 74 6E C4`

```text
C3:AB8A  06 01                EVENT_PAUSE frames=$01
C3:AB8C  42 74 6E C4          EVENT_CALLROUTINE $C4:6E74 <CheckStagedPositionWithinPlayerProximityThreshold>
C3:AB90  0A 8A AB             EVENT_SHORTCALL_CONDITIONAL conditional_call_target=$C3:AB8A <WaitUntilPlayerLeavesActiveArea>
C3:AB93  1B                   EVENT_SHORT_RETURN
```

### C3:AFA3 LoopPartyLooksAtActiveEntity

- class: `event-bytecode-label`
- decode status: `complete`
- stop reason: terminal/control-flow stop
- raw preview: `42 3B 8B C4 06 03 19 A3 AF 25 7A A3 3B 00 07 7B`

```text
C3:AFA3  42 3B 8B C4          EVENT_CALLROUTINE $C4:8B3B <MakePartyLookAtActiveEntityCallback>
C3:AFA7  06 03                EVENT_PAUSE frames=$03
C3:AFA9  19 A3 AF             EVENT_SHORTJUMP jump_target=$C3:AFA3 <LoopPartyLooksAtActiveEntity>
```
