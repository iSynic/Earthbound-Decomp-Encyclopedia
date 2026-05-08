# Class2 Second-Stage Selector A970

This note captures the current ROM-first model for the second-stage selector around `$A970`, `C2:BAC5`, and `C2:BB18`.

See also `notes/class2-end-to-end-gate-path-5540.md`.

## Why this cluster matters

This is the point where the heavier `C2:5540` path stops looking like pure descriptor gating and starts looking like a real ongoing controller.

The strongest current result is that this cluster promotes a chosen candidate row into active working state rooted at `$A970` and the surrounding `A9xx` fields.

## `C2:BAC5` looks like a filtered row-count helper

Current safest reading:

- input in `A` selects a row-state value to test
- the routine scans the 32 candidate rows at `9FAC + 0x4E * n`
- it requires row `+0x0C` to be nonzero
- it requires row `+0x0E` to match the requested state value
- it also checks row `+0x1D` and increments a count only for a narrow allowed subset
- it returns that count in `A`

That makes `BAC5` read best as a filtered candidate-row count helper, not as a dispatcher.

## `C2:BB18` looks like the candidate-to-controller promoter

Current safest reading:

- input in `A` selects a candidate index or candidate-row ordinal
- the routine maps that selection into a concrete row at `9FAC + 0x4E * n`
- it copies multiple candidate-side bytes into working families rooted near `99CE`, `9FC3`, and the `A9xx` block
- one important guard in this promoter now reads more clearly: a branch excludes candidate class byte `9FC9 == 1` before one `+0x1D = 1` promotion path
- if the chosen row is not already in a conflicting state, it writes the chosen row pointer to `$A972` and the chosen row base to `$A970`
- it sets row byte `+0x1D = 1`, clears row bytes `+0x1E` through `+0x23`, then triggers follow-up helpers including `C2:3D05`, `C1:DD47`, and immediate script feedback through `C1:DC1C`

The important behavioral point is no longer just generic controller promotion. In light of the battler-layout correction and the `C2:7550` startup path, `BB18` now looks much more like the promoter into an active selected-battler collapse or affliction-handling path than like a neutral controller-state installer.

## `$A970` and `$A972` look like active-row anchors

Current safest reading:

- `$A970` holds the base address of the currently selected candidate row in the `9FAC + 0x4E * n` family
- `$A972` is a closely related companion pointer or cached row anchor used by the follow-up controller helpers

Many later `5540`-side paths immediately read from `$A970`, then branch on row-local fields like `+1D`, `+1E`, `+1F`, `+20`, and `+23`.

That makes `$A970` the best current marker for the active selected battler row under control. The newer collapse-side evidence also suggests this is not just a neutral controller anchor: at least some of these promoted rows are being driven into specific affliction or collapse handling immediately after selection.

The follow-up trace in `notes/class2-post-selection-controller-phases.md` now makes those branches more concrete: `C2:7294` and `C2:7318` read best as sibling parameterized feedback helpers, `C2:7397` reads like an activation or reset installer for the selected row, and `C2:7550` reads like the main post-selection controller entry that seeds row-local phase bytes and dispatches a descriptor-backed pointer from record `+0x31`.
 The late follow-up note at `notes/class2-late-controller-path-77ca.md` further strengthens `+0x0E` as a major phase byte and `+0x4B` as a per-row active marker.

## How this changes the 5540 story

With this cluster in place, the heavier path now reads in three phases:

1. candidate scan and scoring
2. candidate promotion into active `$A970` row state
3. ongoing controller behavior over that promoted row

That is a much stronger subsystem model than simply saying the path "keeps going after the gate."

## Relation to the existing class-2 notes

This selector layer fits cleanly with the existing findings:

- `BAC5` matches the idea that the `5540` path performs best-candidate style filtering before deeper behavior
- `BB18` explains how the winning row becomes the active object for later `44xx`, `47xx`, `6Axx`, and `72xx/73xx` helper families
- `$A970` now looks like the working bridge between descriptor-backed candidate rows and the heavier interaction controller

## What is still unresolved

Still open:

- the exact semantic split among row fields `+1D`, `+1E`, `+1F`, `+20`, and `+23`, now that `+1D` is increasingly pointing at battler affliction or collapse state instead of a generic controller flag
- what role the companion pointer `$A972` plays relative to `$A970`
- whether `C1:DD47` and `C1:DD53` are best understood as script setup, object refresh, or controller-phase transition helpers

## Current safest takeaway

The safest current takeaway is:

- `BAC5` counts rows that satisfy a filtered state test
- `BB18` promotes one of those rows into active controller state
- `$A970` is the best current marker for the selected active row

That means the heavy `5540` path now has a clear mid-level shape: it scores candidate descriptors, chooses a row, promotes it, then runs a controller over that promoted row.

## Best next target

- See `notes/class2-post-selection-controller-phases.md` for the first controller-phase pass. The best next move is to tighten the remaining row-local phase meanings, especially `+0E`, `+0F`, `+10`, `+1E`, and the 32-row marker at `+4B`, so the selected-row controller can be named from end-to-end behavior instead of just from entry and setup.
