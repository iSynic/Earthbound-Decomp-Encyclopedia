# C3 actionscript movement pulse presets

## Reference context

This pass follows the `C3:AA38` setup helper from `notes/c3-event-222-224-movement-helper-cluster.md`. That helper starts the task at `C3:A111`; neighboring refs show a small family of animation-pulse task entrypoints and preset installers.

Key refs:

- `refs/ebsrc-main/ebsrc-main/src/data/events/C3A0B2.asm`
- `refs/ebsrc-main/ebsrc-main/src/data/events/C3A0C5.asm`
- `refs/ebsrc-main/ebsrc-main/src/data/events/C3A0D8.asm`
- `refs/ebsrc-main/ebsrc-main/src/data/events/C3A12E.asm`
- `refs/ebsrc-main/ebsrc-main/src/data/events/C3AA46.asm`
- `refs/ebsrc-main/ebsrc-main/src/data/events/C3AA5A.asm`
- `refs/ebsrc-main/ebsrc-main/src/data/events/C3AA6E.asm`
- `refs/ebsrc-main/ebsrc-main/src/data/events/C3AA82.asm`
- `refs/ebsrc-main/ebsrc-main/src/data/events/C3AA96.asm`
- `refs/ebsrc-main/ebsrc-main/src/data/events/C3AAAA.asm`
- `refs/ebsrc-main/ebsrc-main/src/data/events/C3AB12.asm`
- `refs/ebsrc-main/ebsrc-main/src/data/events/C3AB26.asm`
- `refs/earthbound-disasm-legacy/Earthbound Decomp/EB/Routine_Macros_EB.asm`

The legacy disassembly corroborates the byte labels around `DATA_C3A111`/`DATA_C3A11E` and the raw event bytes used by the nearby setup helpers.

## Pulse task shapes

The simplest members repeatedly toggle animation profile `1` and `0`, calling the two C0 visual-profile refresh helpers in between:

```text
C3:A0B2  06 18                EVENT_PAUSE $18
C3:A0B4  3B 01                EVENT_SET_ANIMATION $01
C3:A0B6  42 B2 A4 C0          EVENT_CALLROUTINE $C0:A4B2 <RefreshCurrentSlotVisualProfile_Mode1IfAligned>
C3:A0BA  06 18                EVENT_PAUSE $18
C3:A0BC  3B 00                EVENT_SET_ANIMATION $00
C3:A0BE  42 A8 A4 C0          EVENT_CALLROUTINE $C0:A4A8 <RefreshCurrentSlotVisualProfile_Mode0IfAligned>
C3:A0C2  19 B2 A0             EVENT_SHORTJUMP $C3:A0B2
```

`C3:A0C5` has the same body with `$0C` pauses. `C3:A0D8` contains three conditional variants with `$09`, `$06`, and `$02` pauses; the ebsrc local labels name those as `UNKNOWN_C3A0D8`, `UNKNOWN_C3A0D8_ENTRY1`, and `UNKNOWN_C3A0D8_ENTRY2`.

`C3:A111` is the task entry used by `C3:AA38` and `C3:AB26`. It checks `ACTIONSCRIPT_VARS::V4` before each half of the animation pulse, so callers can gate or suppress the visible frame toggle:

```text
C3:A111  06 08                EVENT_PAUSE $08
C3:A113  20 04                EVENT_WRITE_VAR_TO_TEMPVAR $04
C3:A115  0B 1E A1             EVENT_SHORTCALL_CONDITIONAL_NOT $C3:A11E <DATA_C3A11E>
C3:A118  3B 01                EVENT_SET_ANIMATION $01
C3:A11A  42 B2 A4 C0          EVENT_CALLROUTINE $C0:A4B2 <RefreshCurrentSlotVisualProfile_Mode1IfAligned>
C3:A11E  06 08                EVENT_PAUSE $08
C3:A120  20 04                EVENT_WRITE_VAR_TO_TEMPVAR $04
C3:A122  0B 11 A1             EVENT_SHORTCALL_CONDITIONAL_NOT $C3:A111 <DATA_C3A111>
C3:A125  3B 00                EVENT_SET_ANIMATION $00
C3:A127  42 A8 A4 C0          EVENT_CALLROUTINE $C0:A4A8 <RefreshCurrentSlotVisualProfile_Mode0IfAligned>
C3:A12B  19 11 A1             EVENT_SHORTJUMP $C3:A111 <DATA_C3A111>
```

`C3:A12E` is a longer `V4`-controlled pulse loop. It reads `V4`, loops with one-frame pauses while that value remains true, toggles animation `1`, repeats the same gate, toggles animation `0`, and jumps back to `C3:A12E`.

`C3:A1DF` is a fast two-frame pulse variant that calls `UNKNOWN_C40015` and branches into the `C3:A0FE` fast pulse path when its condition is false.

## Setup presets

The AAxx/ABxx helpers install one of the task entrypoints after setting shared movement state:

- `C3:AA46`: physics `C0:A37A`, animation `0`, task `C3:A0B2`, zero velocity, visual profile `0`, `C0:A685($40,$00)`.
- `C3:AA5A`: same setup, task `C3:A0C5`, `C0:A685($00,$01)`.
- `C3:AA6E`: same setup, task `C3:A0D8`, `C0:A685($60,$01)`.
- `C3:AA82`: same setup, task `C3:A0EB`, `C0:A685($00,$02)`.
- `C3:AA96`: same setup, task `C3:A0FE`, `C0:A685($00,$06)`.
- `C3:AAAA`: same setup, task `C3:A12E`, sets `V4 = $000C`.
- `C3:AB12`: same setup, task `C3:A1DF`, `C0:A685($00,$06)`.
- `C3:AB26`: alternate callbacks `C0:A03A` and `C0:9FF1`, task `C3:A111`, zero velocity, sets `V4 = $0000`.

`C3:AA38` from the previous note belongs to this preset family too: it starts `C3:A111`, zeros velocity, and clears `V4`.

## Interpretation

This cluster is the action/event script equivalent of a movement-preset library. The pulse tasks own how the current entity's animation alternates, while the setup helpers choose a task speed/gate and initialize the movement fields consumed by C0's current-slot visual and movement helpers.

The `C0:A685` parameter pairs are still named conservatively because their exact field-level semantics come from C0 state code, not from C3 alone. The local byte shape is firm; the preset names should stay descriptive until that field pair has a stronger data contract.

## Source-form pilot

This family is now the first C3 event/actionscript source-form pilot:

- generator: `tools/build_c3_event_script_source_pilot.py`
- source: `src/c3/event_scripts/movement_pulse_presets.asar.asm`
- report: `notes/c3-event-script-source-pilot.md`

The pilot covers the pulse task island and matching AAxx/ABxx preset installers as labeled macro assembly. It validates `617` ROM bytes across `27` source/data-map rows while keeping the opaque scaffold corridor untouched until the replacement flow is mature.

## Working Names

- `C3:A0B2` = `LoopActiveEntityWalkPulse24Frame`
- `C3:A0C5` = `LoopActiveEntityWalkPulse12Frame`
- `C3:A0D8` = `LoopActiveEntityWalkPulse9FrameConditional`
- `C3:A0EB` = `LoopActiveEntityWalkPulse6FrameConditional`
- `C3:A0FE` = `LoopActiveEntityWalkPulse2FrameConditional`
- `C3:A111` = `LoopActiveEntityWalkPulseVar4Gate`
- `C3:A12E` = `LoopActiveEntityWalkPulseVar4Countdown`
- `C3:A1DF` = `LoopActiveEntityWalkPulse2FrameC40015Branch`
- `C3:AA46` = `InitMovementPreset40_00Pulse24Frame`
- `C3:AA5A` = `InitMovementPreset00_01Pulse12Frame`
- `C3:AA6E` = `InitMovementPreset60_01Pulse9Frame`
- `C3:AA82` = `InitMovementPreset00_02Pulse6Frame`
- `C3:AA96` = `InitMovementPreset00_06Pulse2Frame`
- `C3:AAAA` = `InitMovementPresetVar4Countdown`
- `C3:AB12` = `InitMovementPreset00_06C40015Branch`
- `C3:AB26` = `InitAlternatePhysicsVar4WalkPulse`

## Remaining questions

- `C0:A37A`, `C0:A03A`, and `C0:9FF1` are callback entrypoints referenced by these presets. They already have local C0 working names; C3 contributes caller/context evidence rather than new callback implementations.
- `UNKNOWN_C40015` is a C4 helper used by `C3:A1DF`; the branch behavior is locally visible, but the helper's semantic name belongs to a later C4 pass.
- The `C0:A685` argument pairs should remain in preset names only as literal parameters until the underlying current-slot fields are named more confidently.
