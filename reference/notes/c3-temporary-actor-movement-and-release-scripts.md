# C3 temporary actor movement and release scripts

## Purpose

This note follows the C3 action-script movement seam beyond the pulse presets into the temporary actor scripts that combine C0 movement callbacks, collision/neighbor-cache tasks, random direction selection, NPC attention coordination, and current-entity release.

References:

- `refs/ebsrc-main/ebsrc-main/src/data/events/C343DB.asm`
- `refs/ebsrc-main/ebsrc-main/src/data/events/C3A15E.asm`
- `refs/ebsrc-main/ebsrc-main/src/data/events/C3A17B.asm`
- `refs/ebsrc-main/ebsrc-main/src/data/events/C3A18F.asm`
- `refs/ebsrc-main/ebsrc-main/src/data/events/C3A1F3.asm`
- `refs/ebsrc-main/ebsrc-main/src/data/events/C3A20E.asm`
- `refs/ebsrc-main/ebsrc-main/src/data/events/C3A401.asm`
- `notes/c3-actionscript-movement-pulse-presets-a0b2-ab26.md`
- `notes/c3-c0-callback-binding-correction.md`
- `notes/entity-overlap-neighbor-cache-c05ece-c064d3.md`
- `notes/movement-vector-script-runtime-c0c83b-c0d195.md`
- `notes/npc-attention-path-coordinator-c0d19b-c0d98f.md`

## Decoder/tooling note

This pass also tightened `tools/decode_event_script.py` for this script class:

- added no-argument callroutine knowledge for the C0/C2/C4/EF helpers used by these event scripts
- added opcode `0x43` as `EVENT_SET_PRIORITY`
- added opcode `0x44` as `EVENT_WRITE_TEMPVAR_WAITTIMER`
- made `C0:9F82` consume and print its inline random-choice word list

That makes wandering scripts like `C3:A3B7` decode as a clean random direction / random duration loop instead of falling through into the inline data as bogus opcodes.

## Timed-delivery cleanup task

`C3:43DB` is the small task started by the timed-delivery departure path. It pulses animation `1` only while `V4` is true, always restores animation `0`, checks `C0:C6B6`, and loops while the current slot is still inside the live-area window.

When the slot leaves that live-area window, it runs the timed-delivery teardown helper `EF:0FF6`, yields to text through the C4 event helper, and jumps to the shared current-entity release tail at `C3:A204`.

That makes it a timed-delivery departure cleanup/pulse task rather than an ordinary idle pulse.

## C40015-gated pulse and release loops

The neighboring `A15E..A209` scripts are small temporary-actor pulse loops that end through the shared release tail once `C4:0015` stops taking the loop branch.

- `C3:A15E` starts with `C4:0023`, gates animation `1` on `V4`, then loops on `C4:0015` until it jumps to `C3:A204`.
- `C3:A17B` and `C3:A18F` are simpler slow/fast versions of the same `animation 1 -> C0:A4B2 -> C4:0015` loop.
- `C3:A1F3` is the 16-frame version used by the confirmation-screen walking-character path and other temporary scripts.
- `C3:A204` calls `C0:20F1` and ends.
- `C3:A209` is the tiny four-frame delay before the same release tail.

The exact meaning of `C4:0015` and `C4:0023` still belongs to a later C4 pass, but the C3-side role is clear: pulse a temporary actor until the C4 condition ends, then release the current visual entity.

## Var0 animation phase loop

`C3:A20E` is a `V0`-selected animation loop used by the NPC attention setup family. It starts from animation `0`, refreshes profile mode `0`, reads `V0`, and dispatches one of five short animation cases:

- `C3:A22C`: eight-frame animation-1 half followed by the fallthrough animation-0 half at `C3:A234`
- `C3:A234`: eight-frame animation-0 half
- `C3:A23D`: four-frame animation-1 / animation-0 pulse
- `C3:A24E`: thirty-two-frame animation-1 / animation-0 pulse
- `C3:A25F`: sixteen-frame idle wait

After each selected case, it checks `C0:C6B6`; once the current slot is outside the live-area window, it jumps to `C3:A47C`, the current-entity release tail.

## Random wandering setup and loop

`C3:A381` installs the `C0:A360` no-neighbor physics callback, starts the `C3:A111` walk-pulse task, starts the `C3:A262` collision-probe refresh task, refreshes the visual profile, sets current-slot field `2B32` through `C0:A685($00,$01)`, seeds wrapper parameters through `C0:A964($08,$00,$08,$00)`, and jumps into `C3:A3B7`.

`C3:A3A1` is the shorter sibling that installs the same physics callback, starts the `C3:A15E` pulse loop plus the `C3:A262` collision-probe refresh task, refreshes the visual profile, sets `C0:A685($00,$01)`, and returns.

`C3:A3B7` is a random wandering loop:

1. clear `V4`
2. ask `C4:7269` (`ClassifyCurrentSlotAgainstAreaBounds`) whether to choose from the normal cardinal direction list
3. if true, choose one of `0, 2, 4, 6`
4. otherwise subtract one from the existing tempvar
5. install the chosen direction through `C0:A65F` and `C0:C83B`
6. choose a movement distance/count from `8, 16`
7. call `C0:CA4E` to derive the active task timer
8. stop velocity, set `V4 = 1`, choose a wait timer from `30, 60, 90, 120`, and loop

So the safest C3-side name is a random direction movement loop with a random wait, not a scene-specific actor name.

`C3:A3C9` is the inline cardinal-direction picker used by that loop.

## NPC attention / neighbor-cache family

`C3:A401` is the common initializer for the nearby attention/neighbor-cache scripts. It sets a passive `C0:9FF0` physics callback, clears one C0 state through `C0:A6DA`, waits one frame, and calls `C0:A6B8`.

If the current slot has no cached neighbor flag, it installs tick callback `C0:D7F7`, switches physics to `C0:A360`, sets animation `0`, refreshes the visual profile, clears `V0`, and starts the `C3:A20E` animation-phase task. Otherwise it returns without starting that loop.

`C3:A426` and `C3:A42D` are the two public wrappers:

- `C3:A426` starts the terrain-compatibility collision loop at `C3:A434`.
- `C3:A42D` starts the horizontal-edge collision loop at `C3:A448`.

Both loops update the priority neighbor cache through `C0:6478`, update a current-slot collision cache, and call `C0:D5B0` until the coordinator lets them fall into the finish/release path at `C3:A45C`.

`C3:A45C` waits for `C0:D59B` to report the coordinator inactive, stops the actor, restores the passive physics callback, sets `V0 = 1`, blinks animation `FF/00` three times, and releases the current visual entity through `C3:A47C`.

## Working Names

- `C3:43DB` = `LoopTimedDeliveryDeparturePulseUntilOffscreen`
- `C3:43E8` = `TimedDeliveryDeparturePulseAnimation0Half`
- `C3:A15E` = `LoopC40015Var4GatedPulseUntilRelease`
- `C3:A17B` = `LoopC40015SlowPulseUntilRelease`
- `C3:A18F` = `LoopC40015FastPulseUntilRelease`
- `C3:A1F3` = `LoopC40015Pulse16FrameUntilRelease`
- `C3:A204` = `ReleaseCurrentVisualEntityAndEnd`
- `C3:A209` = `DelayThenReleaseCurrentVisualEntity`
- `C3:A20E` = `LoopVar0SelectedAnimationUntilOffscreen`
- `C3:A22C` = `Var0AnimationCase0Pulse8FrameOn`
- `C3:A234` = `Var0AnimationCase1Pulse8FrameOff`
- `C3:A23D` = `Var0AnimationCase2Pulse4Frame`
- `C3:A24E` = `Var0AnimationCase3Pulse32Frame`
- `C3:A25F` = `Var0AnimationCase4Wait16Frame`
- `C3:A381` = `InitRandomWanderMovementWithCollisionProbe`
- `C3:A3A1` = `InitC40015PulseWithCollisionProbe`
- `C3:A3B7` = `LoopRandomDirectionMovementWithRandomWait`
- `C3:A3C9` = `ChooseRandomCardinalDirection`
- `C3:A3D6` = `ApplyRandomDirectionAndMovementTimer`
- `C3:A3E7` = `SetMovementTimerThenRandomWait`
- `C3:A401` = `InitNpcAttentionPathIfNoCachedNeighbor`
- `C3:A426` = `StartNpcAttentionTerrainCollisionLoop`
- `C3:A42D` = `StartNpcAttentionHorizontalCollisionLoop`
- `C3:A434` = `LoopNpcAttentionTerrainCollision`
- `C3:A448` = `LoopNpcAttentionHorizontalCollision`
- `C3:A45C` = `FinishNpcAttentionAndReleaseActor`
- `C3:A47C` = `ReleaseCurrentVisualEntityTail`
- `C3:A2AA` = `TrafficLightWaitUntilOffscreenAndRelease`

## Remaining questions

- `C4:0015` and `C4:0023` are only named here by their C3-side effects. `C4:6E46` is now pinned by ebsrc's `EVENT_YIELD_TO_TEXT` macro and documented in `notes/current-slot-position-staging-c46b8d-c46d4b.md`. `C4:7269` now has a local C4 contract in `notes/movement-target-bounds-and-vector-refresh-c46ef8-c47369.md`: it classifies the current slot against bounds seeded by `C4:7225`.
- `C3:A401` and its wrappers are named through the documented C0 NPC attention coordinator. That is stronger than a pure ref name, but the exact gameplay-facing family may tighten when the surrounding event ids `004..022` are promoted.
