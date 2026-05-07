# C3 to C0 callback binding correction

## Summary

`EVENT_SET_DRAW_CALLBACK`, `EVENT_SET_POSITION_CHANGE_CALLBACK`, and `EVENT_SET_PHYSICS_CALLBACK` store low-word callback operands. In C3 scripts, those operands commonly refer back to C0 callback routines, not to same-bank C3 labels.

This matters because the first version of `tools/decode_event_script.py` formatted every two-byte script pointer as bank-local. That was right for `EVENT_SHORTCALL`/`EVENT_SHORTJUMP`, but wrong for callback opcodes.

## Corrected local decodes

`C3:AA38` installs the current-slot C0 position update/sprite refresh callback:

```text
C3:AA38  25 7A A3             EVENT_SET_PHYSICS_CALLBACK $C0:A37A <UpdatePosition_WhenNoNeighbor_WithSpriteRefresh_CurrentSlot>
C3:AA3B  3B 00                EVENT_SET_ANIMATION $00
C3:AA3D  07 11 A1             EVENT_START_TASK $C3:A111 <LoopActiveEntityWalkPulseVar4Gate>
C3:AA40  39                   EVENT_SET_VELOCITIES_ZERO
C3:AA41  0E 04 00 00          EVENT_SET_VAR $04, $0000
C3:AA45  1B                   EVENT_SHORT_RETURN
```

`C3:AB26` installs an alternate projection callback and a velocity integration callback:

```text
C3:AB26  23 3A A0             EVENT_SET_POSITION_CHANGE_CALLBACK $C0:A03A <ProjectWorldToScreen_FromCamera31AndHeight>
C3:AB29  25 F1 9F             EVENT_SET_PHYSICS_CALLBACK $C0:9FF1 <Integrate_XYAndZVelocity_WithSpriteRefresh>
C3:AB2C  3B 00                EVENT_SET_ANIMATION $00
C3:AB2E  07 11 A1             EVENT_START_TASK $C3:A111 <LoopActiveEntityWalkPulseVar4Gate>
C3:AB31  39                   EVENT_SET_VELOCITIES_ZERO
C3:AB32  0E 04 00 00          EVENT_SET_VAR $04, $0000
C3:AB36  1B                   EVENT_SHORT_RETURN
```

`C3:A381` uses the same pattern for the `C0:A360` no-neighbor position updater:

```text
C3:A381  25 60 A3             EVENT_SET_PHYSICS_CALLBACK $C0:A360 <UpdatePosition_WhenNoNeighbor_WithSpriteRefresh>
C3:A384  3B 00                EVENT_SET_ANIMATION $00
C3:A386  07 11 A1             EVENT_START_TASK $C3:A111 <LoopActiveEntityWalkPulseVar4Gate>
C3:A389  07 62 A2             EVENT_START_TASK $C3:A262 <LoopActiveEntityCollisionProbeRefresh>
C3:A38C  42 BF A4 C0          EVENT_CALLROUTINE $C0:A4BF <RefreshCurrentSlotVisualProfile_Mode0>
C3:A390  42 85 A6 C0 00 01    EVENT_CALLROUTINE $C0:A685 <Script_SetCurrentSlotField2B32>, $00, $01
C3:A396  42 64 A9 C0 08 00 08 00 EVENT_CALLROUTINE $C0:A964 <SetCurrentSlotAreaBoundsFromRadii_ReadTwoWords>, $08, $00, $08, $00
C3:A39E  19 B7 A3             EVENT_SHORTJUMP $C3:A3B7 <LoopRandomDirectionMovementWithRandomWait>
```

## Cross-bank contract

This clarifies the C3/C0 boundary:

- C3 event scripts choose script-local tasks, animation pulses, and setup parameters.
- C3 callback opcodes install C0 low-word callbacks into the active entity/task runtime.
- C0 owns the callback implementations: projection, velocity integration, position update, and sprite refresh.

The C0 names are already present in `build/working-names-c0-c3.json`, so this note is evidence for the binding contract rather than a new callback naming pass.

## Decoder change

`tools/decode_event_script.py` now treats opcodes `0x22`, `0x23`, and `0x25` as `callbackptr` operands and formats them as C0 addresses. `EVENT_SHORTCALL`, `EVENT_SHORTJUMP`, and conditional short calls remain bank-local.

## Remaining questions

- `C3:A3B7` and `C3:A3C9` are adjacent C3 script helpers used by `C3:A381`; they touch `C4:7269` and `C0:9F82` and need a separate script-helper pass before naming.
- `C0:A685` and `C0:A964` field/argument semantics are still intentionally literal in C3 notes until the current-slot field contract is tighter.
