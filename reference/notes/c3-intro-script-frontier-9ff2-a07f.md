# C3 intro script frontier 9FF2-A07F

## Reference context

This pass covers the first unnoted C3 unknown include cluster from `notes/bank-c3-reference-frontier.md`:

- `C3:9FF2` `data/unknown/C39FF2.asm`
- `C3:A010` `data/unknown/C3A010.asm`
- `C3:A01B` `data/unknown/C3A01B.asm`
- `C3:A026` `data/unknown/C3A026.asm`
- `C3:A02D` `data/unknown/C3A02D.asm`
- `C3:A038` `data/unknown/C3A038.asm`

In `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank03.asm`, this cluster appears immediately before `data/events/scripts/001.asm`, `data/events/scripts/002.asm`, and `data/events/C3A07F.asm`.

The legacy disassembly supplies better labels around the actual script bodies:

- `C3:A043`: `Script0001_IntroCutsceneCameraPan`
- `C3:A04E`: `DATA_C3A04E`
- `C3:A052`: `DATA_C3A052`
- `C3:A05E`: `Script0002_UnknownScript`, with a legacy comment saying it runs in the intro cutscene and may be a sprite script.
- `C3:A076`: `DATA_C3A076`

## Data cluster

`C3:9FF2` is not event bytecode. It is a 15-entry little-endian pointer table into the short records that follow:

```text
C3:9FF2: A010 A010 A010 A01B A026 A026 A026 A02D
C3:A002: A02D A026 A010 A026 A026 A010 A038
```

The following unknown includes are compact records rather than standalone event scripts. Decoding them as event bytecode produces misleading `EVENT_LOOP_END` / `EVENT_END` fragments because the record format is not the event VM format.

```text
C3:A010: 02 00 01 09 02 01 01 09 03 10 A0
C3:A01B: 02 00 01 08 02 01 01 08 03 1B A0
C3:A026: 02 00 01 FF 03 26 A0
C3:A02D: 02 00 01 08 02 01 01 08 03 2D A0
C3:A038: 02 00 01 04 02 01 01 04 03 38 A0
```

The self-pointers at the end of each record strongly suggest loopable movement/animation pattern data. For now these should be treated as intro movement-pattern records rather than event scripts.

## Script 001

`C3:A043` is the intro camera-pan gate. In the verified ROM it contains:

```text
C3:A043  42 D3 FF C1          EVENT_CALLROUTINE $C1:FFD3 <ComputeBankC1ChecksumTail>
C3:A047  0A 4E A0             EVENT_SHORTCALL_CONDITIONAL $C3:A04E <DATA_C3A04E>
C3:A04A  42 00 01 C3          EVENT_CALLROUTINE $C3:0100
C3:A04E  08 00 52 C0          EVENT_SET_TICK_CALLBACK $C0:5200 <Tick_OverworldPlayerPositionAndCallbacks>
C3:A052  01 06                EVENT_LOOP $06
C3:A054  06 C8                EVENT_PAUSE $C8
C3:A056  02                   EVENT_LOOP_END
C3:A057  42 00 00 C2          EVENT_CALLROUTINE $C2:0000 <RunEnemySunstrokeCheck>
C3:A05B  19 52 A0             EVENT_SHORTJUMP $C3:A052 <DATA_C3A052>
```

`C3:0100` is not indexed as an addressed ebsrc symbol, but the bank layout puts named `system/display_antipiracy_screen.asm` before `C3:0188`. The shape here matches an intro gate: run a C1 check, conditionally continue to the camera-pan tick loop, otherwise call the C3 system routine at `$C3:0100`.

## Script 002

`C3:A05E` installs an intro object/sprite setup:

```text
C3:A05E  23 39 A0             EVENT_SET_POSITION_CHANGE_CALLBACK $C0:A039 <ReturnFromPositionChangeCallback_NoProjection>
C3:A061  25 6B A2             EVENT_SET_PHYSICS_CALLBACK $C0:A26B <PhysicsCallback_TargetContextCompareAndProject>
C3:A064  3B 00                EVENT_SET_ANIMATION $00
C3:A066  42 AA 3D C0          EVENT_CALLROUTINE $C0:3DAA <Sync_CurrentSlotToPartyCharacterRecord>
C3:A06A  42 F0 4E C0          EVENT_CALLROUTINE $C0:4EF0 <Restore_CurrentSlotFromSnapshotRecord>
C3:A06E  42 DA A6 C0          EVENT_CALLROUTINE $C0:A6DA <ClearCurrentSlotNeighborCache>
C3:A072  08 78 4D C0          EVENT_SET_TICK_CALLBACK $C0:4D78 <Tick_Event2SnapshotObjectReconcile>
C3:A076  42 E3 A6 C0          EVENT_CALLROUTINE $C0:A6E3 <WatchAndRefreshCompanionVisualPhase>
C3:A07A  06 01                EVENT_PAUSE $01
C3:A07C  19 76 A0             EVENT_SHORTJUMP $C3:A076 <DATA_C3A076>
```

This is not a generic movement pulse preset. It binds C0 projection/physics/tick callbacks, synchronizes the current slot with a party-character record, restores a snapshot, and then loops companion visual refresh once per frame. That agrees with the legacy note that script 002 runs during the intro cutscene as a sprite/object script.

`C3:A07F` is a one-byte halt script:

```text
C3:A07F  09                   EVENT_HALT
```

## Working Names

- `C3:9FF2` = `IntroMovementPatternPointerTable`
- `C3:A010` = `IntroMovementPattern09Loop`
- `C3:A01B` = `IntroMovementPattern08Loop`
- `C3:A026` = `IntroMovementPatternFFLoop`
- `C3:A02D` = `IntroMovementPattern08LoopAlt`
- `C3:A038` = `IntroMovementPattern04Loop`
- `C3:A043` = `IntroCutsceneCameraPanGate`
- `C3:A04E` = `StartIntroCameraPanTickLoop`
- `C3:A052` = `LoopIntroCameraPanWaitAndC2Step`
- `C3:A05E` = `IntroCutsceneSpriteObjectSetup`
- `C3:A076` = `LoopIntroCompanionVisualRefresh`
- `C3:A07F` = `HaltEventScript`

## Remaining questions

- The record format for `C3:A010` through `C3:A038` needs a dedicated movement-pattern decoder. The self-referential pointer tails are clear, but field semantics are not yet pinned down.
- `C3:0100` should be tied to the named anti-piracy system include with byte-level evidence from the earlier bank03 system region.
- The exact semantics of `C1:FFD3` and `C2:0000` belong to their bank-local notes; this C3 pass only establishes their use in the intro script flow.
