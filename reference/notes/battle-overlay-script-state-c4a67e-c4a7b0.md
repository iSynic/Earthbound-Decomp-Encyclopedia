# Battle Overlay Script State `C4:A67E-C4:A7B0`

## Scope

This small cluster owns the C4 side of the battle overlay or battle-swirl
effect script state rooted at `$AEC2..$AEE6`. It sits after the overlay script
payload data at `C4:A5CE`, `C4:A5FA`, `C4:A626`, and `C4:A652`, and before the
Sound Stone data family now started at `C4:AC57`.

See also [sound-stone-presentation-data-c4ac57.md](notes/sound-stone-presentation-data-c4ac57.md).

The surrounding references line up:

- `C2:DBFE` indexes `C4:A591` during a countdown and transforms its byte values
  into `$AD98`, making it a battle-background/static transition wave table.
- `C2:EA15` begins a battle swirl overlay script and calls `C4:A67E(0)`.
- `C2:EA74` switches to a closing script and also calls `C4:A67E(0)`.
- C3 visual token handlers call `C4:A67E` with fixed-colour overlay modes such
  as `(5, 7)`, `(4, 5)`, and `(2, 4)`.
- `INIT_BATTLE_SCRIPTED` waits in a loop on `UNKNOWN_C2E9C8` while calling
  `C4:A7B0` once per frame.

## Adjacent payload data

`C4:A591` is a 61-byte signed-looking wave/table payload used by the C2 battle
background visual updater. The C2 consumer reads it with `X = #$003C - $AD8C`,
converts the byte around an `#$80` center, and stores the result in `$AD98`.
That makes the table part of the battle background/static transition path
rather than a callable C4 routine.

The four `C4:A5CE/A5FA/A626/A652` blocks are fixed-size overlay script payloads
for the `$AEC2/$AECC` interpreter. Each block is two `#$16`-byte records: a
single nonzero script record followed by a zero record that terminates the
active pointer path.

The C2 selector pair gives their safest current roles:

| address | selected by | current role |
|---|---|---|
| `C4:A5CE` | `C2:EA15`, mode not `1` | opening battle-swirl overlay script, mode 0/default |
| `C4:A5FA` | `C2:EA15`, mode `1` | opening battle-swirl overlay script, mode 1 |
| `C4:A626` | `C2:EA74`, previous mode `0` | closing battle-swirl overlay script, mode 0 |
| `C4:A652` | `C2:EA74`, previous mode nonzero | closing battle-swirl overlay script, nonzero mode |

The opening records share the same payload except for the first word
(`0x003D` vs `0x0064`). The closing records mirror that split and use negative
delta words (`0xFF20`, `0xFF49`, `0xFFFC`, `0xFFFD`) plus `0x8000` sentinel
values in the optional fields.

Source polish: `src/c4/battle_overlay_transition_data.asm` now splits the
combined data corridor into the static transition wave table and the four named
open/close script payload blocks while preserving the byte layout.

2026-05-06 transition-data follow-up: the four local script payloads are now
row-structured as one `#$16`-byte active record followed by one `#$16`-byte
terminator record. The source records line up with the `C4:A7B0` interpreter
fields: delay/count byte, optional X/Y/width/height words, signed deltas, and
delta-step words. The closing records use `$8000` only for the optional
width/height fields, matching the stepper's leave-current-value sentinel check.
The stepper source now also marks the active long-script path, the null-pointer
table-driven frame path, the special-mode ladder, and the cleanup handoff as
separate C4-owned phases.

2026-05-06 transition-record constants follow-up: the same four payload rows
now use named constants for the open/close delay words, initial X/Y seeds,
open-size zero seeds, closing `$8000` size sentinels, signed width/height
deltas, delta-step words, and zero terminator rows. This keeps the C4 table
contract readable without naming the caller-side mode selector beyond the
already-proven open/close mode split.

## Initializer

`C4:A67E` initializes the active overlay state.

Caller A selects an overlay/script mode. Caller X is a flag word:

- bit `1` controls `$AEC6`
- bit `0` controls `$AEC7`
- bit `2` selects `$AEC8 = #$20`; otherwise `$AEC8 = #$1F`
- bit `7` enables the `$AEE4..AEE6` auxiliary mode seed

The routine sets `$AEC2 = 1`, reads a four-byte record from the `CE:DD41` table
using the selected mode, fills `$AEC3..$AEC5`, clears `$AECC/$AECE`, and for
mode zero installs the default script pointer `C4:A5CE`. It also clears
`$AEC9/$AECA`, sets `$AECB = 1`, optionally seeds `$AEE4/AEE5/AEE6`, and calls
`C0:B0AA` to commit the initial overlay/layer state.

## Per-frame interpreter

`C4:A7B0` is the per-frame tick for the active overlay script state.

If `$AEC2` is zero, it returns through the inactive path. Otherwise it decrements
the countdown and, when a record boundary is reached, reads the active long
pointer at `$AECC/$AECE`.

For nonzero records it:

- reloads `$AEC2` from the record delay byte
- reads optional words at record offsets `+2`, `+4`, `+6`, and `+8`, ignoring
  `#$8000` sentinel values
- reads position/delta words at `+0A..+14`
- advances `$AECC/$AECE` by `#$16`
- accumulates the per-frame deltas into `$AED0/$AED2/$AED4/$AED6/$AEDC/$AEDE`
- clamps the overlay size words when the signed deltas would cross zero
- calls `C0:B149`, `C0:B0EF`, and `C0:B047` to apply the resulting window or
  colour-layer state

When the active script pointer is null, it falls back to the table-driven
`$AEC4/$AEC5` phase path. That path uses `CE:DC45` offsets, alternates through
`C0:AE34` and `C0:B0B8`, applies `$AEC6/$AEC7/$AEC8` to the C0 layer helpers,
and advances or decrements the phase counters until the overlay becomes
inactive.

Source polish: `src/c4/battle_overlay_script_state_helpers.asm` and
`src/c4/battle_overlay_script_stepper.asm` now share named contracts for the
flag bits, active/frame/repeat/index bytes, layer/reverse/tile-count controls,
active script pointer, `CE:DD41` script table, `CE:DC45` frame pointer table,
`#$16` record stride, `#$8000` optional-field sentinel, effect position/size
and delta fields, special-mode delay ladder, and the C0 window/offset helper
calls.

2026-05-06 source polish: the initializer source now states the callee-side
ownership boundary explicitly: C2/C3 pass mode and flag words, but C4 owns the
`$AEC2..$AEE6` state layout, the optional local `C4:A5CE` default opening
script pointer, and the handoff to the C0 renderer primer.

2026-05-06 stepper side-effect follow-up: the per-frame source now marks the
size-delta accumulation phase, the width/height zero-crossing clamps, the
zero-size long-script completion path, the `animation parity + 3` frame-tile
selector passed to C0, reverse frame-table walking, and the special-mode
`CE:DD41` reseed before rejoining the table-driven frame path.

## Working Names

- `C4:A591` = `BattleBgStaticTransitionWaveTable`
- `C4:A5CE` = `BattleSwirlOverlayOpenMode0Script`
- `C4:A5FA` = `BattleSwirlOverlayOpenMode1Script`
- `C4:A626` = `BattleSwirlOverlayCloseMode0Script`
- `C4:A652` = `BattleSwirlOverlayCloseModeNonzeroScript`
- `C4:A67E` = `StartBattleOverlayScriptState`
- `C4:A7B0` = `StepBattleOverlayScriptState`

## Confidence boundaries

### Locally proved

- `$AEC2` is the active countdown/liveness byte for the interpreter
- `$AECC/$AECE` is the active long script pointer
- `C2:EA15` and `C2:EA74` choose the four local overlay script payloads by
  opening/closing phase and mode
- `C4:A67E` seeds `$AEC2..$AEE6` and installs script payload pointers
- `C4:A7B0` advances that state once per call and applies it through the C0
  window/colour layer helpers

### Still open

- exact semantic field names for the `#$16`-byte overlay script records
- exact user-facing names for the overlay modes selected through `CE:DD41`
