# C2 PSI animation and battle swirl overlay tail

This note covers the remaining unknowns between `SHOW_PSI_ANIMATION`, the battle swirl sequence, and the battle-background loader tail:

- `C2:E6B3`
- `C2:E8C4`
- `C2:E9ED`
- `C2:EA15`
- `C2:EA74`

The reference include map places this cluster immediately after `battle/show_psi_animation.asm` and before `overworld/battle_swirl_sequence.asm`, with known neighbors `C2:E9C8`, `C2:EAAA`, and `C2:EACF`.

## `C2:E6B3` / `C2:E6B6` - advance PSI animation frame and palette state

Suggested working name: `AdvancePsiAnimationFrameAndPaletteState`

Direct caller:

- `C2:DCF9`

The reference chunk starts at `C2:E6B3`, but the decoded bytes show a plausible routine prologue beginning at `C2:E6B6`; `C2:E6B3` appears to be padding or inline data immediately before the callable body. The direct call target found locally is `C2:E6B6`, from the per-frame battle-background update path around `C2:DCF9`.

Observed behavior:

- advances `PSI_ANIMATION_STATE::time_until_next_frame` at `$1B9E`
- reloads the frame hold from `$1B9F` when the timer reaches zero
- if `PSI_ANIMATION_STATE::frames_left` at `$1BA0` is nonzero:
  - copies the current frame pointer at `$1BA1` into VRAM tile ranges rooted at `$5800`
  - uses the same C0 upload helpers and masks/layers as the surrounding battle visual code
  - advances the source frame pointer by `0x0400`
  - decrements the remaining frame count
- advances the PSI palette animation timer at `$1BA9`
- uses the palette range/index/speed fields around `$1BA5..$1BA8`
- copies palette words from the PSI palette source pointer at `$1BAA` into the target palette buffer at `$1BCA`
- uploads palette changes through `C0:856B(0x18)`
- drives enemy-color/alternate-palette timers at `$1BCC` and `$1BCE`, calling the nearby palette helpers `C2:FAD8`, `C2:FB35`, and `C2:FADE`

This is the per-frame PSI visual animator rather than the setup routine. `SHOW_PSI_ANIMATION` prepares the state; this helper consumes it during the battle visual tick.

## `C2:E8C4` - start/retime a battle swirl overlay mode

Suggested working name: `StartBattleSwirlOverlayAndRecordMode`

Direct callers:

- `C2:C24D`
- `C2:C317`
- `C2:C89A`
- `C2:E9A6`

Observed behavior:

- preserves the caller's `Y` value as an overlay mode/timer byte at `$AECA`
- passes the incoming `A` value through to the C4 visual helper at `C4:A67E`

The local callers sit in battle setup, prayer/special visual code, and the nearby swirl wrapper at `C2:E8E0`. That wrapper chooses a sound/effect based on `$4DBC`, updates C0 layer state, calls `C2:E8C4`, stores `$AEC8`, and clears `$AECB`. The byte-level behavior is small, but the call context marks it as a battle swirl/overlay latch.

## `C2:E9ED` - clear overlay state and reset layer effects

Suggested working name: `ClearBattleOverlayAndResetLayerEffects`

Direct callers:

- `C2:61CF`
- `C2:DADD`

Observed behavior:

- clears `$AEC2`
- calls `C0:AE34` with `A = $AEC9 + 3`
- calls `C0:B01A(0, 0, 0)`
- calls `C0:B047(0)`

The caller at `C2:61CF` is in the instant-win setup path, and the caller at `C2:DADD` is at the end of `LOAD_BATTLE_BG`. In both cases this helper resets the battle overlay/layer-effect state after a major battle visual transition.

## `C2:EA15` - begin a battle swirl overlay script

Suggested working name: `BeginBattleSwirlOverlayScript`

Direct callers:

- `C4:9846`
- `C4:DA14`

Observed behavior:

- stores the input mode byte in `$AEEF`
- calls `C4:A67E(0)`
- sets `$AEC8 = 0x13`
- chooses a script/function pointer pair at `$AECC/$AECE`:
  - mode `2`: `C3:F819`
  - mode `1`: `C4:A5FA`
  - otherwise: `C4:A5CE`

The C4 path around `C4:DA14` starts this helper with mode `0`, waits for input/visual progress, then calls `C2:EA74`, polls `C2:EACF` until the overlay is inactive, and finally calls `C2:EAAA`. This makes `C2:EA15` the opening script selector for that overlay sequence.

## `C2:EA74` - switch the battle swirl overlay to its closing script

Suggested working name: `SwitchBattleSwirlOverlayToClosingScript`

Direct caller:

- `C4:DA95`

Observed behavior:

- calls `C4:A67E(0)`
- sets `$AEC8 = 0x13`
- reads the previous mode from `$AEEF`
- chooses the closing pointer pair at `$AECC/$AECE`:
  - nonzero mode: `C4:A652`
  - zero mode: `C4:A626`

Together, `C2:EA15` and `C2:EA74` form the open/close selector pair for the battle swirl overlay scripts. The existing `C2:EACF` latch remains the busy/inactive test for the selected script.

## Working Names

- `C2:E6B3` = `AdvancePsiAnimationFrameAndPaletteState`
- `C2:E6B6` = `AdvancePsiAnimationFrameAndPaletteStateBody`
- `C2:E8C4` = `StartBattleSwirlOverlayAndRecordMode`
- `C2:E9ED` = `ClearBattleOverlayAndResetLayerEffects`
- `C2:EA15` = `BeginBattleSwirlOverlayScript`
- `C2:EA74` = `SwitchBattleSwirlOverlayToClosingScript`
