# C2 Battle Overlay Runtime Polish

This note records the byte-neutral C2 battle overlay polish slice. It promotes
the swirl/overlay latch, script selectors, clear/reset helpers, and busy
predicate adjacent to the PSI animation tick.

Primary source modules:

- `src/c2/c2_e8c4_start_battle_swirl_overlay_and_record_mode.asm`
- `src/c2/c2_e9ed_clear_battle_swirl_overlay_state.asm`
- `src/c2/c2_e9ed_clear_battle_overlay_and_reset_layer_effects.asm`
- `src/c2/c2_ea15_begin_battle_swirl_overlay_script.asm`
- `src/c2/c2_ea74_switch_battle_swirl_overlay_to_closing_script.asm`

Related evidence notes:

- `notes/c2-psi-swirl-overlay-tail-c2e6b3-c2ea74.md`
- `notes/c2-psi-animation-runtime-polish.md`
- `notes/battle-visual-asset-contracts.md`

## Overlay Latch

`C2:E8C4` is the compact overlay latch:

- incoming A is forwarded to the C4 visual helper at `C4:A67E`
- incoming Y is recorded as `$AECA`

The embedded `C2:E8E0` wrapper builds a full overlay profile:

- chooses sound and layer parameters from `$4DBC`
- applies an alternate profile when `$4A8C >= 0x01C0`
- calls the `E8C4` latch with `Y = 0x1E`
- writes overlay duration byte `$AEC8`
- clears `$AECB`

The embedded `C2:E9C8` helper is a busy-style predicate over `$AEC2/$AECA`.

## Clear And Script Selectors

The decoded `C2:E9ED..EACF` source contains the overlay clear/open/close/final
clear bodies.

`C2:E9ED`:

- clears active overlay latch `$AEC2`
- calls `C0:AE34` with `$AEC9 + 3`
- calls `C0:B01A(0, 0, 0)`
- calls `C0:B047(0)`

`C2:EA15`:

- records opening mode in `$AEEF`
- calls `C4:A67E(0)`
- sets `$AEC8 = 0x13`
- chooses opening script pointer `$AECC/$AECE`:
  - mode `2`: `C3:F819`
  - mode `1`: `C4:A5FA`
  - otherwise: `C4:A5CE`

`C2:EA74`:

- calls `C4:A67E(0)`
- sets `$AEC8 = 0x13`
- chooses closing script pointer `$AECC/$AECE` from previous `$AEEF`:
  - nonzero: `C4:A652`
  - zero: `C4:A626`

`C2:EAAA`:

- clears `$AEC2`
- clears `$AECC/$AECE`
- calls `C0:AE34(3)`
- calls `C0:B047(0)`

## Scaffold Note

The working-name corridor files for `C2:E9ED`, `C2:EA15`, and `C2:EA74` remain
in place. This pass documents their promoted behavior while leaving scaffold
structure unchanged. The decoded implementation lives in
`c2_e9ed_clear_battle_swirl_overlay_state.asm`.

## Decomp Value

This slice closes the local runtime story around the battle overlay tail:

- `$AECA` is now documented as the recorded overlay mode/timer byte
- `$AEEF` is the open-mode byte used by the close selector
- `$AEC8` is a duration or script timer byte used by both open and close paths
- `$AECC/$AECE` are the active overlay script pointer pair
- `$AEC2` is the active overlay latch cleared by both reset helpers

The matching C4 interpreter side is now source-polished as well: the
`C4:A591..A67E` data corridor is split into the static wave table plus the four
open/close script payload blocks, and `C4:A67E/A7B0` share named contracts for
the `$AEC2..$AEE6` state record, script/frame tables, record stride/sentinel
fields, and C0 window/offset helper calls.

## Remaining Soft Spots

- final user-facing names for the `$4DBC` overlay profile values
- whether a later scaffold cleanup should replace the three corridor files with
  split decoded source units
