# Action-script/event wrapper strip (`C0:A841-C0:AAFD`)

## Scope

`C0:A841-C0:AAFD` is a compact wrapper band between the current-entity
movement helpers and `LOAD_SPC700_DATA` at `C0:AB06`. Most entries consume
one to three action-script parameters with `EB_ReadScriptParameterByte`
(`C0:9D86`) or `EB_ReadScriptParameterWord` (`C0:9D94`), preserve the current
entity slot in `$94` where needed, and tail-call longer helpers in banks C2 or
C4.

The legacy disassembly and ebsrc symbols corroborate the local starts:
`UNKNOWN_C0A841`, `UNKNOWN_C0A84C`, `UNKNOWN_C0A857`, the C4 wrapper run,
the `ACTIONSCRIPT_PREPARE_NEW_ENTITY*` entries, `MOVEMENT_LOAD_BATTLEBG`,
`ACTIONSCRIPT_FADE_OUT_WITH_MOSAIC`, and the final timer/slot helpers at
`C0:AA6E-C0:AAFD`.

## C2/C4 parameter wrappers

- `C0:A841` reads one word and calls `C0:ABE0`, then returns. `C0:ABE0`
  queues a nonzero A value in the `$1AC2` sound/effect command ring via
  `$00CA`, toggles `$1ACA`, and treats zero specially by writing `$57` to
  `APUPort3`.
- `C0:A84C` reads one word and calls `C2:1628`.
- `C0:A857` preserves incoming A in X, reads one word into A, then calls
  `C2:165E`.
- `C0:A864`, `C0:A86F`, `C0:A87A`, `C0:A88D`, `C0:A8A0`, and `C0:A8B3`
  are byte/word or two-word wrappers around C4 helpers:
  `C4:6C9B`, `C4:6CC7`, `C4:6CF5`, `C4:6E4F`, `C4:66F0`, and `C4:6C5E`.
  The `C4:6B8D..6D4B` targets are now mapped in
  [current-slot-position-staging-c46b8d-c46d4b.md](notes/current-slot-position-staging-c46b8d-c46d4b.md): they copy resolved entity positions into the current slot's cached target, staged words, or live anchor.
- `C0:A8C6`, `C0:A8D1`, and `C0:A8DC` call `C4:7143` with fixed A/X
  modes: `(0,0)`, `(1,0)`, and `(0,1)`.
- `C0:A8E7` and `C0:A8EF` call `C4:72A8` with fixed A modes `0` and `1`.
- `C0:A88D` is ebsrc's `EVENT_QUEUE_TEXT` wrapper. It reads the inline text pointer pieces and passes them to `C4:6E4F`, which enqueues record type `8` through `C0:64E3`.

## Entity/new-object and position wrappers

- `C0:A8F7`, `C0:A8FF`, `C0:A907`, and `C0:A912` align with the ebsrc
  `ACTIONSCRIPT_PREPARE_NEW_ENTITY_AT_SELF`,
  `ACTIONSCRIPT_PREPARE_NEW_ENTITY_AT_PARTY_LEADER`,
  `ACTIONSCRIPT_PREPARE_NEW_ENTITY_AT_TELEPORT_DESTINATION`, and
  `ACTIONSCRIPT_PREPARE_NEW_ENTITY` symbol order. Locally they call
  `C4:6DAD` with mode `0` or `1`, `C4:6DE5` with one byte parameter, and
  `C4:6E37` with two word parameters plus one byte parameter.
- `C0:A92D` reads one word and calls `C4:6B8D`, setting the current slot's cached target to a `$2C9A` visual-type slot's position.
- `C0:A938` reads one word and calls `C4:6BBB`, setting the current slot's cached target to a `$2CD6` pose-descriptor slot's position.
- `C0:A943` reads one byte and calls `C4:6BE9`; ebsrc symbol order places
  `ACTIONSCRIPT_GET_POSITION_OF_PARTY_MEMBER` here. Locally this resolves a party/registry code and writes the selected position into the current cached target.
- `C0:A94E` reads one word and calls `C4:6984`.
- `C0:A959` reads one word and calls `C4:69F1`.
- `C0:A964` reads two words and calls `C4:7225`.
- `C0:A977` reads two words and calls `C4:7370`; symbol order places
  `MOVEMENT_LOAD_BATTLEBG` at this entry.

## Three-word effect wrappers

The next run consistently reads two or three word parameters, shuffles them
through stack/X/Y, and delegates to C4 helpers:

- `C0:A98B` -> `C4:6534`
- `C0:A99F` -> `C4:ECAD`
- `C0:A9B3` -> `C4:EBAD`
- `C0:A9CF` -> `C4:EC05`
- `C0:A9EB` -> `C4:EC52`
- `C0:AA07` -> `C0:8814`; symbol order identifies this as
  `ACTIONSCRIPT_FADE_OUT_WITH_MOSAIC`.
- `C0:AA23` -> `C4:7765`

## Slot refresh, small constants, and countdown fields

- `C0:AA3F` uses incoming A as a mode selector, chooses X as either `$0033`
  or `$00B3`, reads three bytes into `$9E37-$9E39`, restores the original
  mode, and calls `C4:2439`. This looks like a small graphics/palette or
  actor-visual setup wrapper keyed by a three-byte inline payload.
- `C0:AA6E` branches on `$0E5E[current_entity_slot]`. In the zero case it
  reads two bytes into `$2AF6[slot]` and `$10F2[slot]`, mirrors the second
  byte to `$2892`, then calls `C0:A4C4` with Y as the current slot. In the
  nonzero case it stores the first byte in `$2AF6[slot]`, doubles the second
  byte into `$10F2[slot]`, stores the slot in `$2896`, and jumps through the
  `C0:A794` profile/refresh helper.
- `C0:AAAC` stores the current slot in `$2896` and jumps through `C0:A794`.
- `C0:AAB5` reads a word, byte, byte triple and calls `C4:97C0` with the word
  in Y, first byte in X, and second byte in A.
- `C0:AACD` and `C0:AAD1` are tiny constant-return entries that set X to
  `$0002` or `$0004`.
- `C0:AAD5` reads a byte count, increments it, reads a word target, and uses
  `($84)+$0C` as a countdown field. If the field is empty it initializes it
  from the incremented count, decrements it, and only when the countdown
  reaches zero stores the target word in `$94`.
- `C0:AAFD` clears the same `($84)+$0C` countdown field.

## Practical decomp notes

This strip is useful as an action-script ABI map: the wrappers describe the
inline parameter layout even when the deeper C4 helper is not fully named yet.
For future lifting, these entries can become small typed script op functions
while the C4 targets remain shared engine helpers. The `AAD5/AAFD` pair also
identifies `($84)+$0C` as a reusable per-script-frame countdown/control field.

## Working Names

- `C0:A841` = `Script_PlaySoundEffectParameter`
- `C0:A84C` = `ScriptWrapper_C21628_ReadWord`
- `C0:A857` = `ScriptWrapper_C2165E_ReadWordPreserveMode`
- `C0:A864` = `Script_CopyRegistrySlotAnchorToCurrentSlot_ReadByte`
- `C0:A86F` = `Script_CopyPoseDescriptorSlotAnchorToCurrentSlot_ReadWord`
- `C0:A87A` = `Script_SetCameraRelativeAnchor_ReadTwoWords`
- `C0:A88D` = `ActionScript_QueueTextPointer`
- `C0:A8A0` = `ScriptWrapper_C466F0_ReadWordByte`
- `C0:A8B3` = `Script_SetStagedPositionOffset_ReadTwoWords`
- `C0:A8C6` = `ScriptWrapper_C47143_Mode00`
- `C0:A8D1` = `ScriptWrapper_C47143_Mode10`
- `C0:A8DC` = `ScriptWrapper_C47143_Mode01`
- `C0:A8E7` = `ScriptWrapper_C472A8_Mode0`
- `C0:A8EF` = `ScriptWrapper_C472A8_Mode1`
- `C0:A8F7` = `ActionScript_PrepareNewEntityAtSelf`
- `C0:A8FF` = `ActionScript_PrepareNewEntityAtPartyLeader`
- `C0:A907` = `ActionScript_PrepareNewEntityAtTeleportDestination`
- `C0:A912` = `ActionScript_PrepareNewEntity`
- `C0:A92D` = `Script_SetTargetToVisualTypeSlotPosition_ReadWord`
- `C0:A938` = `Script_SetTargetToPoseDescriptorSlotPosition_ReadWord`
- `C0:A943` = `ActionScript_GetPositionOfPartyMember`
- `C0:A94E` = `ScriptWrapper_C46984_ReadWord`
- `C0:A959` = `ScriptWrapper_C469F1_ReadWord`
- `C0:A964` = `ScriptWrapper_C47225_ReadTwoWords`
- `C0:A977` = `Movement_LoadBattleBg`
- `C0:A98B` = `ScriptWrapper_C46534_ReadThreeWords`
- `C0:A99F` = `ScriptWrapper_C4ECAD_ReadThreeWords`
- `C0:A9B3` = `ScriptWrapper_C4EBAD_ReadThreeWords`
- `C0:A9CF` = `ScriptWrapper_C4EC05_ReadThreeWords`
- `C0:A9EB` = `ScriptWrapper_C4EC52_ReadThreeWords`
- `C0:AA07` = `ActionScript_FadeOutWithMosaic`
- `C0:AA23` = `ScriptWrapper_C47765_ReadTwoWords`
- `C0:AA3F` = `Script_SetVisualSetupBytesByMode`
- `C0:AA6E` = `Script_ApplyCurrentSlotVisualCountdownState`
- `C0:AAAC` = `Script_RefreshCurrentSlotVisualProfile`
- `C0:AAB5` = `ScriptWrapper_C497C0_ReadWordByteByte`
- `C0:AACD` = `ReturnX0002`
- `C0:AAD1` = `ReturnX0004`
- `C0:AAD5` = `Script_CountdownThenJumpTarget`
- `C0:AAFD` = `Script_ClearFrameCountdown`
