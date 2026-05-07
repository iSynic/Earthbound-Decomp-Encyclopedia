# C2 Final Prayer Runtime Polish

This note records the byte-neutral C2 Final Prayer polish slice. It promotes
the shared transition helpers, repeated damage worker, phase ladder, and finale
opening sequence that implement action-table rows `291..299`.

Primary source modules:

- `src/c2/c2_c37a_run_final_prayer_stage_transition.asm`
- `src/c2/c2_c3e2_apply_final_prayer_damage_step.asm`
- `src/c2/c2_c41f_run_final_prayer_narrative_transition.asm`
- `src/c2/c2_c572_run_final_prayer_opening_transition.asm`
- `src/c2/c2_c5d1_run_final_prayer_damage_phase2.asm`
- `src/c2/c2_c5fa_run_final_prayer_damage_phase3.asm`
- `src/c2/c2_c623_run_final_prayer_damage_phase4.asm`
- `src/c2/c2_c64c_run_final_prayer_damage_phase5.asm`
- `src/c2/c2_c675_run_final_prayer_damage_phase6.asm`
- `src/c2/c2_c69e_run_final_prayer_damage_phase7.asm`
- `src/c2/c2_c6d0_run_final_prayer_narrative_phase8.asm`
- `src/c2/c2_c6f0_run_final_prayer_finale_opening_sequence.asm`

Related evidence notes:

- `notes/class2-final-prayer-family-c2c572-c2c6f0.md`
- `notes/class2-prayer-common-helpers-c2c37a-c2c3e2-c2c41f.md`
- `notes/c2-battle-bg-load-update-runtime-polish.md`
- `notes/c2-battle-overlay-runtime-polish.md`

## Helper Layer

`C2:C37A` is the shared stage transition helper for Final Prayer rows `291..297`.
It captures the caller-staged text pointer, runs display mode transitions,
temporarily disables battle-background frame updates through `$9643`, displays
the prayer text, applies the caller's battle visual selector through `C2:C21F`,
then restores updates and returns through C1 cleanup. The display transitions
now call `C2:69DE` / `WaitForDisplayTransitionBusyClear`, and the trailing
pause calls `C2:69BE` / `WaitFrames`. Its cleanup tail now names
`C1:DD3B` / `RefreshBattlePresentationForSelectedRow` and `C1:DD47` /
`OpenBattleTextWindow`.

The staged text display is now named at the source site as the `C1:DC1C`
direct battle-text pointer ABI.

`C2:C3E2` is the shared prayer damage worker. Input A is the amount. The helper
points `$A972` at battler table root `$A21C`, starts red flash timer
`$AD9E = 0x3C`, marks `$AA8E = 1`, prepares amount text through `C2:6AFD` /
`ApplyTwentyFivePercentVariance`, and forces amount application through
`C2:8125` / `ApplyDamageToSelectedTarget` with X = `0x00FF`.

`C2:C41F` is the late narrative transition helper used by phase 8 and the
finale text blocks. It runs a different display and Sound Stone cue sequence,
pauses battle-background updates, displays the staged text, then replays the
caller-selected melody cue. The narrative helper now uses the same named
`RefreshBattlePresentationForSelectedRow` and `OpenBattleTextWindow` joins as
the stage-transition helper.

The helper now names both its staged `C1:DC1C` dispatch and the direct
`C8:FC2E` Mech-Pokey speech tail used by the adjacent transition body.

## Phase Ladder

The action-table rows form a stable Final Prayer ladder:

| Row | Source | Role | Damage | Next `$A97A` |
| ---: | --- | --- | ---: | ---: |
| 291 | `C2:C572` | opening transition | none | `5` |
| 292 | `C2:C5D1` | damage phase 2 | `0x0032` | `6` |
| 293 | `C2:C5FA` | damage phase 3 | `0x0064` | `7` |
| 294 | `C2:C623` | damage phase 4 | `0x00C8` | `8` |
| 295 | `C2:C64C` | damage phase 5 | `0x0190` | `9` |
| 296 | `C2:C675` | damage phase 6 | `0x0320` | `10` |
| 297 | `C2:C69E` | damage phase 7 | `0x0640` | `11` |
| 298 | `C2:C6D0` | late narrative phase | none | `12` |
| 299 | `C2:C6F0` | finale | finale tiers | varies |

The damage rows are regular wrappers around `C2:C37A` followed by `C2:C3E2`.
Phase 8 intentionally skips damage and advances through the late narrative
helper only.

Source follow-up: the phase 1-7 wrappers now call `C2:C37A` as
`RunFinalPrayerStageTransition`, the phase 2-7 and finale damage sites call
`C2:C3E2` as `ApplyFinalPrayerDamageStep`, and the phase 8/finale narrative
sites call `C2:C41F` as `RunFinalPrayerNarrativeTransition`. The opening
transition also names its `C0:ABE0` presentation cue dispatch as
`QueueSoundEffectOrPlayApuPort3Cue`.

Battle-visual selector follow-up: Final Prayer callers now name `C2:C21F` as
`ApplyFinalPrayerBattleVisualSelector`, preserving the existing A/X selector
contract while leaving the less-decoded `C2:C32C` companion raw.

## Finale Opening

`C2:C6F0` interleaves four late narrative text blocks with four larger damage
tiers:

- `0x0C80`
- `0x1900`
- `0x3200`
- `0x6400`

It then runs the Sound Stone/noise table rooted at `C4:A35D`, drives layer-1
battle-background distortion swaps through `C2:DAE3`, starts the final overlay
through `C2:E8C4`, waits on the overlay busy predicate, and hands off into the
terminal battle visual state. Its fixed pauses now use the same
`C2:69BE` / `WaitFrames` helper as the shared prayer damage worker, and its
per-frame presentation loops now call `C1:2DD5` / `WindowTick` by name.
The finale opening also names the initial `C2:0F9A` HP/PP roll-target clamp,
the `C1:DD41` battle-presentation prep, the repeated `C0:ABE0` cue dispatches,
the `C2:F8F9` sprite-row commits, and the `C2:DAE3` layer-1 distortion priming
join by their established source contracts.
The final overlay loop now names `C2:E8C4` as
`StartBattleSwirlOverlayAndRecordMode` and `C2:E9C8` as
`PollBattleTransitionComplete`, matching the adjacent special-event transition
contract.

The finale source now names the four C9 narrative scripts (`C9:F70C`,
`C9:F7BB`, `C9:F804`, `C9:F84D`) and the direct `C8:FF31` Pokey run-away text
dispatched through `C1:DC1C`. The opening prayer follow-up at `C9:F86A` is also
named in the phase-1 source body.

## Decomp Value

This slice turns the Final Prayer area from a set of thematically named action
bodies into a runtime contract:

- rows `291..299` have stable phase roles
- `$A97A` is the phase-progress field for this ladder
- `$9643` is explicitly paused around prayer text presentation
- the shared damage helper is now tied to amount setup, flash timing, and forced
  application
- the phase ladder and finale now call the shared prayer transition, damage,
  and narrative helpers by source-facing contract names instead of raw local
  addresses
- the shared `C2:C21F` battle visual selector is named at the Final Prayer
  callsites that feed it A/X visual parameters
- the finale is connected to battle-background distortion and overlay helpers
- opening and finale cue/sprite/presentation joins now reuse existing
  source-facing presentation contracts instead of raw cross-call addresses
- prayer transition and finale sources now use named C1 battle-presentation
  lifecycle joins instead of raw display/window helper calls
- the terminal overlay wait now names the overlay start and completion poll
  helpers instead of raw `C2:E8C4` / `C2:E9C8` edges

## Remaining Soft Spots

- exact final names for display helpers `C0:887A` and `C0:886C`
- full decoded-source replacement for the remaining `C2:C6F0..CFE5` corridor
- final names for the C4 finale sound and distortion timing tables
