# Class2 Prayer Common Helpers C2C37A C2C3E2 C2C41F

This note captures the strongest current local model for the shared helper layer under the late Final Prayer action family.

See also [class2-final-prayer-family-c2c572-c2c6f0.md](notes/class2-final-prayer-family-c2c572-c2c6f0.md).

## Working Names

- `C2:C37A` = `RunFinalPrayerStageTransition`
- `C2:C3E2` = `ApplyFinalPrayerDamageStep`
- `C2:C41F` = `RunFinalPrayerNarrativeTransition`

## Main result

The late prayer rows are no longer best read as nine unrelated bodies.

Their shared helpers now split into three practical roles:

- `C2:C37A` = opening or mid-prayer stage transition helper
- `C2:C3E2` = prayer damage step helper
- `C2:C41F` = late prayer narrative transition helper

The exact final symbolic names can still stay one notch cautious, but the roles are much healthier now than plain `UNKNOWN_C2C37A` or `UNKNOWN_C2C41F`.

## `C2:C37A` is the shared opening or mid-prayer stage transition helper

Pinned callers are exactly the first seven prayer rows:

- `C2:C572` / `RunFinalPrayerOpeningTransition`
- `C2:C5D1` / `RunFinalPrayerDamagePhase2`
- `C2:C5FA` / `RunFinalPrayerDamagePhase3`
- `C2:C623` / `RunFinalPrayerDamagePhase4`
- `C2:C64C` / `RunFinalPrayerDamagePhase5`
- `C2:C675` / `RunFinalPrayerDamagePhase6`
- `C2:C69E` / `RunFinalPrayerDamagePhase7`

Its local body does the same broad sequence every time:

- preserves the incoming `X` and `A` parameters
- copies the current text pointer from direct-page `$22/$24`
- switches battle-display mode through `C0:887A`
- waits for the display-transition busy byte to clear through `C2:69DE` /
  `WaitForDisplayTransitionBusyClear`
- clears `$9643` and `$5DD4`
- runs `C1:DD5F`
- displays the caller-selected text through `C1:DC1C`
- switches display mode again through `C0:887A`
- routes the incoming `A/X` pair through `C2:C21F` /
  `ApplyFinalPrayerBattleVisualSelector`
- restores `$9643 = 1`
- runs `C1:DD3B` / `RefreshBattlePresentationForSelectedRow` and
  `C1:DD47` / `OpenBattleTextWindow`
- waits `0x3C` through `C2:69BE` / `WaitFrames`

So the safest current local read is:

- `C2:C37A` is the common prayer-stage transition and display helper for the early or mid Final Prayer rows

## `C2:C3E2` is the prayer damage step helper

Pinned callers are exactly the damage-bearing prayer rows:

- `C2:C5D1` / `RunFinalPrayerDamagePhase2`
- `C2:C5FA` / `RunFinalPrayerDamagePhase3`
- `C2:C623` / `RunFinalPrayerDamagePhase4`
- `C2:C64C` / `RunFinalPrayerDamagePhase5`
- `C2:C675` / `RunFinalPrayerDamagePhase6`
- `C2:C69E` / `RunFinalPrayerDamagePhase7`
- and the four repeated finale steps inside `C2:C6F0`

Its body is much more focused than the transition helpers:

- stores the incoming amount
- waits `0x3C`
- points `$A972` at the battler table root `A21C`
- calls `C2:3D05`
- writes `$AD9E = 0x3C`
- writes `$AA8E = 1`
- passes the stored amount into `C2:6AFD` / `ApplyTwentyFivePercentVariance`
- then forces the actual amount application through `C2:8125` /
  `ApplyDamageToSelectedTarget` with `X = 0x00FF`
- waits another `0x3C`

That makes the healthiest current local role:

- `C2:C3E2` is the common prayer-damage worker, matching the later `GIYGAS_HURT_PRAYER` role from `ebsrc`

## `C2:C41F` is the late prayer narrative transition helper

Pinned callers are only the late prayer rows:

- `C2:C6D0` / `RunFinalPrayerNarrativePhase8`
- the four staged text blocks inside `C2:C6F0`

Its body is a different presentation path from `C2:C37A`:

- preserves the incoming text selector in `Y`
- copies the current text pointer from `$22/$24`
- switches display mode through `C0:887A`
- calls `C0:AC0C` with literal `2`
- waits for the display-transition busy byte to clear through `C2:69DE` /
  `WaitForDisplayTransitionBusyClear`
- clears `$9643`
- runs `C1:DD5F`
- writes byte `$001A = 4`
- plays or stages `0x00BF` through `C4:FBBD`
- reopens display mode through `C0:886C`
- displays the caller-selected text through `C1:DC1C`
- restores `$9643 = 1`
- performs another short wait and mode switch
- runs `C1:DD3B` / `RefreshBattlePresentationForSelectedRow` and
  `C1:DD47` / `OpenBattleTextWindow`
- writes byte `$001A = 0x17`
- plays the caller-selected cue through `C4:FBBD`
- reopens display mode again and returns

So the safest current local read is:

- `C2:C41F` is the late prayer narrative transition helper used by the phase-8 and finale prayer text blocks

## Current takeaway

The common helper layer is now in a usable state:

- `C2:C37A` handles the early and middle prayer stage transitions
- `C2:C3E2` handles the repeated prayer damage applications
- `C2:C41F` handles the late-stage prayer narrative transitions
- rows `291..299` now call those three helpers by source-facing contract names,
  so the phase ladder reads as transition, damage, and narrative composition
  rather than raw local-address plumbing

## What is still open

Still open:

- the exact display or sound meaning of the literal writes to `$001A`
- the exact healthiest final names for `C0:887A` and `C0:886C` in this prayer-specific context
- whether `C2:3D05` in this lane should be described as focus-target setup, target-context setup, or something slightly broader
