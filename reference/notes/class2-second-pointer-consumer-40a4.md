# Class2 Second Pointer Consumer 40A4

This note captures the current ROM-first model for `C2:40A4`, the consumer reached by the second pointer fetched from `D5:7B68` through descriptor field `+0x4E`.

See also `notes/class2-descriptor-field-4e-and-d57b68.md`.
See also `notes/class2-late-controller-path-77ca.md`.
See also `notes/class2-d57b68-battle-action-table-match.md`.
See also [class2-concentration-seal-family-c28d5a-c2a3d1.md](notes/class2-concentration-seal-family-c28d5a-c2a3d1.md).

## Working Names

- `C2:40A4` = `ApplyBattleActionSecondPointerPayload`
- `C2:EACF` = `WaitForBattleEffectStepReady`

## Why this routine matters

The `D5:7B68` work established that each selected late-phase action-set entry carries two pointers:

- one dispatched through `C1:DC1C`
- one dispatched through `C2:40A4`

This routine therefore determines whether that second pointer is just data, an animation payload, or a real behavior entry.

## Current local shape of `C2:40A4`

Current safest reading from the local bytes:

- the caller provides a 32-bit pointer in working registers that `40A4` copies into local pair `$06/$08`
- `40A4` loops through a helper at `C2:EACF` until that helper reports completion or readiness
- it then runs two bit-driven iteration passes
- the first pass walks 8 entries rooted at `$A21C`
- the second pass walks all 32 candidate rows rooted at `$9FAC`
- each pass uses `C2:7029`, the known bit-test helper from the class-`2` mask family
- for each bit that passes the test, it calls `C2:3D05` to install the current target or row context
- if the fixed caller-provided pointer in `$06/$08` is nonzero, it writes that
  same pair to the current action-payload pointer slots `$00BC/$00BE` and
  dispatches through `C0:9279`

The strongest purely local interpretation is now narrower and better: `40A4` does not stream a bit-packed pointer payload. It iterates the bit-selected targets from the current action word, installs per-target context through `3D05`, and then applies one fixed second-pointer payload through `C0:9279` once per selected entry.

Source polish: `src/c2/c2_40a4_apply_battle_action_second_pointer_payload.asm`
now names `$00BC/$00BE` as `CurrentActionPayloadPointerLo/Bank` and names
`C4:A08D` as the special-case table consulted by the sibling mask-prune helper.
That keeps the consumer's payload slots distinct from the battle-text pointer
ABI used by `C1:DC1C` and `C1:DD9F`.

## `C2:EACF` looks like a wait-or-busy helper

The side reference gives a useful clue for the helper that `40A4` polls first. In both `psi_thunder_common.asm` and the battle main routine, the reference project calls `UNKNOWN_C2EACF` in a loop, ticking the window system between calls, and only continues once the helper returns zero.

That matches the local `40A4` shape well: its opening loop now reads best as "wait until the current battle effect or presentation phase is no longer busy, then start the bit-driven action application pass." See `notes/class2-busy-helper-eacf-and-window-setup.md` for the focused state-flow pass.

## Why this no longer looks like plain animation data

Several local facts push this away from a pure animation-table interpretation:

- it uses the same bit-test helper family as the class-`2` selection masks
- it iterates selected entries rather than just streaming bytes linearly
- it performs one 8-entry pass and one 32-entry pass, which looks much more like target-set application than like graphics streaming
- it conditionally dispatches through `C0:9279`, which already behaves like a target or action dispatcher rather than a graphics loader
- it is called from the late selected-row controller immediately after the paired `D5:7B68` message pointer is dispatched

That makes `40A4` look more like a target-iteration behavior executor or action applicator than a visual-only helper.

## Strong reference-backed clue from the ebsrc side project

The `ebsrc` side reference gives one especially useful clue:

- `C2:40A4` is used from battle code
- `pray.asm` passes it a named `BTLACT_DEFENSE_DOWN_A` pointer
- `ko_target.asm` also routes a locally built pointer into `C2:40A4`

This is not ROM proof by itself, but it is strong evidence that `40A4` consumes battle-action payload pointers.

## Structural match between `D5:7B68` and the battle action table

The same side reference strengthens the interpretation even more.

Its battle action table entries are laid out as:

- one direction byte
- one target byte
- one type byte
- one cost byte
- one message pointer
- one action pointer

That is not just the same high-level shape we now see locally at `D5:7B68`; the first local entries also line up by value and order. For example:

- local index `0x0004` is `(0, 1, 1, 0)` with pointers `EF:848C` and `C2:859F`, which fits the reference `BASH` slot
- local index `0x000A` is `(0, 4, 3, 10)` with shared PSI-style message pointer `EF:8543`, which fits the reference `PSI_ROCKIN_ALPHA` slot
- local index `0x000E` is `(0, 3, 3, 6)`, which fits the reference `PSI_FIRE_ALPHA` slot
- local index `0x0012` is `(0, 1, 3, 4)`, which fits the reference `PSI_FREEZE_ALPHA` slot

This is the strongest current cross-check that `D5:7B68` is not just any paired-pointer table. It now looks very likely to be the same battle action descriptor family, or a directly corresponding table in the same format.

## Concrete target examples fit the action-wrapper reading

A few second-pointer targets strengthen the action reading from local bytes alone:

- `C2:9556..9571` form the early all-target PSI wrapper quartet over `C2:9516`
- `C2:95AB..95C6` form the early row-target PSI wrapper quartet over `C2:957A`
- `C2:9647..9662` form the early one-target PSI wrapper quartet over `C2:95CF`
- `C2:9871..9895` form the early Thunder wrapper quartet over the larger two-parameter helper `C2:966B`
- `C2:A821` is another compact wrapper over a nearby shared helper
- `C2:8D5A` and `C2:A3D1` now form a focused concentration or PSI-seal apply family, each converging on a `+0x21 = 4` write and `EF:6C0B` through the wrappers at `C2:8D82` and `C2:A3E9`

These look like action-entry routines with parameter variation, not like static data blobs. They also make the second-pointer side of `D5:7B68` look much more like a real battle-action handler table than a generic paired-pointer payload family.

## Current safest interpretation

The safest current interpretation is:

- `C2:40A4` consumes the second pointer from a `D5:7B68` action-set entry
- it treats that pointer like a bit-driven action payload rather than a passive blob
- it tests entry bits, applies per-entry filtering, and dispatches resulting work through `C0:9279`
- the best current reference-backed guess is that this is battle-action execution or battle-action-style payload handling

That is a stronger and more useful statement than the earlier "companion behavior pointer" wording.

## What is still unresolved

Still open:

- the exact payload format consumed by `C2:40A4`
- the exact relationship between the `1B9E` flag and the now-better-understood `AEC2/AECC/AECE` fixed-stride effect-step state polled by `C2:EACF`
- whether `C0:9279` is being used here as a generic effect dispatcher, target dispatcher, or scripted action trampoline in battle-specific form
- how widely the direction or target metadata are consumed locally outside the late selected-row path, even though the byte layout now strongly matches battle-action attributes

## Runtime proof lane

The Phase 2 Mesen runner now treats `C2:40A4` as the missing wrapper, not as
the same thing as downstream `C0:9279` payload dispatch. The three static
callsites are:

- `C2:79D1`, from the late selected-row controller after it derives the
  selected row's second action pointer
- `C2:915C`, from the battler-normalization wrapper after it builds and prunes
  the active battler mask
- `C2:AF0D`, from the random-damage/status item tail after it builds its
  selected payload pointer and target mask

Current save 5 and save 7 probes reach target-mask and text-context neighbors
(`C2:4703`, `C2:3E32`, `C2:416F`, `C2:3D05`) plus direct `C0:9279` payload
dispatches to targets such as `C2:859F`, `C2:8651`, `C2:8740`, and `C2:9033`.
Those `C0:9279` hits return through `C2:5D3D`, so the runner classifies them
as `c2_battle_start_candidate_direct_dispatch`, not `C2:40A4` loop dispatch.
They do not hit `C2:40A4` or those three static pre-call sites. The runner now
captures `$A970/$A972` active row pointers, `$A96C/$A96E` target masks,
`$00BC/$00BE` payload dispatch pointers, and the `$1B9E/$AEC2/$AECC/$AECE`
busy gate when the right fixture lands.

## Current safest takeaway

The safest current takeaway is:

- `D5:7B68` now looks very likely to be a battle action descriptor table rather than a generic pointer table
- its first four bytes strongly match direction, target, type, and cost metadata
- its first pointer behaves like a message or presentation pointer
- its second pointer behaves like a battle-action payload pointer consumed by `C2:40A4`
- `C2:40A4` itself looks like a bit-driven per-target action applicator that dispatches one fixed second-pointer payload through known controller helpers once per selected entry

That gives the late selected-row controller a much clearer gameplay-facing shape.

## Best next target

- See `notes/class2-busy-helper-eacf-and-window-setup.md` for the new busy-state and effect-step pass. The best next move is to map a few concrete `D5:7B68` entries all the way to named `BTLACT_*` behavior in the reference project, or tighten what `C0:B149` is doing with the loaded effect-step state, so the action-set table can be described with less hedging.

