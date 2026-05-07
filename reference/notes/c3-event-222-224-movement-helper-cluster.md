# C3 event 222-224 movement helper cluster

## Reference context

This is the first C3 reference-first seam after the C0-C2 closure pass. The starting frontier came from:

```powershell
python tools\build_ref_bank_report.py C3 --output notes\bank-c3-reference-frontier.md --limit 160
python tools\lookup_ref_context.py C3:0295 C3:AA38 C3:AB44 C3:AB59 C3:AB8A C3:A09F C3:A262 C3:AFA3
```

High-value refs:

- `refs/ebsrc-main/ebsrc-main/src/data/events/C30295.asm`
- `refs/ebsrc-main/ebsrc-main/src/data/events/scripts/222.asm`
- `refs/ebsrc-main/ebsrc-main/src/data/events/scripts/223.asm`
- `refs/ebsrc-main/ebsrc-main/src/data/events/scripts/224.asm`
- `refs/ebsrc-main/ebsrc-main/src/data/events/C3AA38.asm`
- `refs/ebsrc-main/ebsrc-main/src/data/events/C3AB44.asm`
- `refs/ebsrc-main/ebsrc-main/src/data/events/C3AB59.asm`
- `refs/ebsrc-main/ebsrc-main/src/data/events/C3AB8A.asm`
- `refs/ebsrc-main/ebsrc-main/src/data/events/C3A09F.asm`
- `refs/ebsrc-main/ebsrc-main/src/data/events/C3A262.asm`
- `refs/ebsrc-main/ebsrc-main/src/data/events/C3AFA3.asm`
- `refs/earthbound-disasm-legacy/Earthbound Decomp/EB/Routine_Macros_EB.asm`

`ebsrc-main` gives readable macro expansions for this region, and the legacy disassembly corroborates several raw byte labels such as `DATA_C3A262`, `DATA_C3AB44`, and `DATA_C3AB59`.

## Local decode

`tools/decode_event_script.py` confirms that these are event/actionscript bytecode streams, not 65816 routines.

`C3:0295`:

```text
C3:0295  1A 38 AA             EVENT_SHORTCALL $C3:AA38 <InitActionScriptMovementState>
C3:0298  42 6E AA C0 06 00    EVENT_CALLROUTINE $C0:AA6E <Script_ApplyCurrentSlotVisualCountdownState>, $06, $00
C3:029E  42 85 A6 C0 00 01    EVENT_CALLROUTINE $C0:A685 <Script_SetCurrentSlotField2B32>, $00, $01
C3:02A4  0E 05 01 00          EVENT_SET_VAR $05, $0001
C3:02A8  1A 59 AB             EVENT_SHORTCALL $C3:AB59 <WaitForActiveEntityMovementToFinish>
C3:02AB  1B                   EVENT_SHORT_RETURN
```

`C3:AA38`:

```text
C3:AA38  25 7A A3             EVENT_SET_PHYSICS_CALLBACK $C0:A37A <UpdatePosition_WhenNoNeighbor_WithSpriteRefresh_CurrentSlot>
C3:AA3B  3B 00                EVENT_SET_ANIMATION $00
C3:AA3D  07 11 A1             EVENT_START_TASK $C3:A111 <DATA_C3A111>
C3:AA40  39                   EVENT_SET_VELOCITIES_ZERO
C3:AA41  0E 04 00 00          EVENT_SET_VAR $04, $0000
C3:AA45  1B                   EVENT_SHORT_RETURN
```

`C3:AB44`:

```text
C3:AB44  42 DB 6A C4          EVENT_CALLROUTINE $C4:6ADB <UNKNOWN_C46ADB>
C3:AB48  42 44 70 C4          EVENT_CALLROUTINE $C4:7044 <UNKNOWN_C47044>
C3:AB4C  42 0A 6B C4          EVENT_CALLROUTINE $C4:6B0A <UNKNOWN_C46B0A>
C3:AB50  42 5F A6 C0          EVENT_CALLROUTINE $C0:A65F <SetCurrentSlotDirectionClassIfActive>
C3:AB54  42 BF A4 C0          EVENT_CALLROUTINE $C0:A4BF <RefreshCurrentSlotVisualProfile_Mode0>
C3:AB58  1B                   EVENT_SHORT_RETURN
```

`C3:AB59`:

```text
C3:AB59  1A 44 AB             EVENT_SHORTCALL $C3:AB44 <RefreshActiveEntityDirectionAndVisualProfile>
C3:AB5C  06 01                EVENT_PAUSE $01
C3:AB5E  42 DC A8 C0          EVENT_CALLROUTINE $C0:A8DC <StepCurrentSlotTowardCachedTarget_NoFacingRefresh>
C3:AB62  0A 5C AB             EVENT_SHORTCALL_CONDITIONAL $C3:AB5C <DATA_C3AB5C>
C3:AB65  39                   EVENT_SET_VELOCITIES_ZERO
C3:AB66  1B                   EVENT_SHORT_RETURN
```

`C3:AB8A`:

```text
C3:AB8A  06 01                EVENT_PAUSE $01
C3:AB8C  42 74 6E C4          EVENT_CALLROUTINE $C4:6E74 <CheckStagedPositionWithinPlayerProximityThreshold>
C3:AB90  0A 8A AB             EVENT_SHORTCALL_CONDITIONAL $C3:AB8A <WaitUntilPlayerLeavesActiveArea>
C3:AB93  1B                   EVENT_SHORT_RETURN
```

`C3:A09F`:

```text
C3:A09F  06 08                EVENT_PAUSE $08
C3:A0A1  3B 01                EVENT_SET_ANIMATION $01
C3:A0A3  42 B2 A4 C0          EVENT_CALLROUTINE $C0:A4B2 <RefreshCurrentSlotVisualProfile_Mode1IfAligned>
C3:A0A7  06 08                EVENT_PAUSE $08
C3:A0A9  3B 00                EVENT_SET_ANIMATION $00
C3:A0AB  42 A8 A4 C0          EVENT_CALLROUTINE $C0:A4A8 <RefreshCurrentSlotVisualProfile_Mode0IfAligned>
C3:A0AF  19 9F A0             EVENT_SHORTJUMP $C3:A09F <LoopActiveEntityWalkAnimationPulse>
```

`C3:A262`:

```text
C3:A262  42 DA A6 C0          EVENT_CALLROUTINE $C0:A6DA <ClearCurrentSlotNeighborCache>
C3:A266  42 76 5E C0 F1 A6 64 C0 EVENT_CALLROUTINE $C0:5E76 <Update_CurrentSlotCollisionCache>, $F1, $A6, $64, $C0
C3:A26E  19 66 A2             EVENT_SHORTJUMP $C3:A266 <DATA_C3A266>
```

`C3:AFA3`:

```text
C3:AFA3  42 3B 8B C4          EVENT_CALLROUTINE $C4:8B3B
C3:AFA7  06 03                EVENT_PAUSE $03
C3:AFA9  19 A3 AF             EVENT_SHORTJUMP $C3:AFA3 <LoopPartyLooksAtActiveEntity>
```

## Script family

`EVENT_221`, `EVENT_222`, `EVENT_223`, and `EVENT_224` are the hidden entries inside the old raw `C3:0188..0295` include:

- `C3:0188..0195`: 13-byte prefix/data island before the first known event entry.
- `C3:0195`: `EVENT_221`, matching `refs/ebsrc-main/ebsrc-main/src/data/events/scripts/221.asm`.
- `C3:0235`: `EVENT_222`, matching `refs/ebsrc-main/ebsrc-main/src/data/events/scripts/222.asm`.
- `C3:024A`: `EVENT_223`, matching `refs/ebsrc-main/ebsrc-main/src/data/events/scripts/223.asm`.
- `C3:0260`: `EVENT_224`, matching `refs/ebsrc-main/ebsrc-main/src/data/events/scripts/224.asm`.

The anchor for `EVENT_221` is the byte-exact `EVENT_TEST_EVENT_FLAG EVENT_FLAG::FLG_POLA` expansion at `C3:0195`:

```text
C3:0195  42 4C A8 C0 0C 00    EVENT_CALLROUTINE $C0:A84C, $0C, $00
C3:019B  0B AA A2             EVENT_SHORTCALL_CONDITIONAL_NOT $C3:A2AA
C3:019E  42 4C A8 C0 0D 00    EVENT_CALLROUTINE $C0:A84C, $0D, $00
C3:01A4  0A AA A2             EVENT_SHORTCALL_CONDITIONAL $C3:A2AA
```

`EVENT_222`, `EVENT_223`, and `EVENT_224` are the immediate callers of `C3:0295` in `ebsrc-main`.

- `EVENT_222` writes `PENDING_INTERACTIONS = 1`, sets `ACTIONSCRIPT_VARS::V6 = $1B10`, sets `V7 = $0188`, calls `C3:0295`, yields to text, then halts.
- `EVENT_223` positions the entity at `$1FE8,$0068`, sets `V6/V7` to `$1F18,$0068`, calls `C3:0295`, yields to text, then halts.
- `EVENT_224` positions the entity at `$1DD0,$00D8`, sets `V6/V7` to `$1D80,$00D8`, calls `C3:0295`, then does an additional right-facing/text/wait/reset sequence before yielding and halting.

That caller shape makes `C3:0295` a reusable "active entity moves left toward the current script target variables and waits for movement completion" helper. It should not be named after only one scene.

## Interpretation

`C3:AA38` is the setup prologue: physics callback, idle animation, recurring task, zero velocity, and a cleared action variable.

`C3:AB44` refreshes the current entity's derived direction and visual/movement profile from C4/C0 helper calls. The key C4 target is now documented as `C4:7044 = ProjectAngleIntoCurrentSlotVectorWords`.

`C3:AB59` waits in one-frame increments until `C0:A8DC` reports that the movement wrapper has finished, then zeros velocity.

`C3:AB8A` is the same "pause, test, conditional self-call" shape as a wait loop. The `ebsrc-main` macro names the call as `EVENT_TEST_PLAYER_IN_AREA`, so this is a wait-until-player-leaves-area helper.

`C3:A09F`, `C3:A262`, and `C3:AFA3` are looping tasks used by nearby movement scripts: animation pulse, collision cache refresh, and party-look-at-active-entity behavior.

## Working Names

- `C3:0295` = `MoveActiveEntityLeftToScriptVarsAndWait`
- `C3:0195` = `Event221PaulaFatherFarewellSequence`
- `C3:0235` = `Event222PaulaDoorExitMovementScript`
- `C3:024A` = `Event223PaulaPorchExitMovementScript`
- `C3:0260` = `Event224PaulaReturnMovementScript`
- `C3:AA38` = `InitActionScriptMovementState`
- `C3:AB44` = `RefreshActiveEntityDirectionAndVisualProfile`
- `C3:AB59` = `WaitForActiveEntityMovementToFinish`
- `C3:AB8A` = `WaitUntilPlayerLeavesActiveArea`
- `C3:A09F` = `LoopActiveEntityWalkAnimationPulse`
- `C3:A262` = `LoopActiveEntityCollisionProbeRefresh`
- `C3:AFA3` = `LoopPartyLooksAtActiveEntity`

## Remaining questions

- The 13-byte prefix at `C3:0188..0195` still needs a direct consumer or source annotation. It is now bounded by the `EVENT_221` byte signature, but it should remain a small preserved prefix until its exact role is known.
- `C4:6E74` and `C4:8B3B` are currently named through `ebsrc-main` macros but still need local C4 documentation before their names become more than ref-corroborated behavior. The adjacent `C4:7044`, `C4:7143`, and `C4:72A8` movement-vector helpers are now covered in `notes/movement-target-bounds-and-vector-refresh-c46ef8-c47369.md`.
- `C3:A111` is the local target for the setup task started by `C3:AA38`; the broader `C3:A0D8`/`C3:A111` movement-task family should be the next neighboring C3 seam.
