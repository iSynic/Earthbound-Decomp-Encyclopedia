# Class2 Post-Selection Controller Phases

This note captures the first ROM-first pass over the controller that runs after the heavy `C2:5540` path promotes a row into `$A970` and `$A972`.

See also `notes/class2-second-stage-selector-a970.md`.
See also `notes/class2-end-to-end-gate-path-5540.md`.
See also `notes/class2-005e-record-domain.md`.
See also [battle-action-stat-change-family-c2b2e0-b5d7.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/battle-action-stat-change-family-c2b2e0-b5d7.md).
See also [battle-affliction-recovery-family-c29aea-a39d.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/battle-affliction-recovery-family-c29aea-a39d.md).

## Why this cluster matters

This is the point where the descriptor-backed selection work becomes a real active-row controller.

The strongest current result is that the post-selection logic is not one opaque routine. It breaks into at least four sibling phases:

- `C2:7294`, a parameterized feedback helper
- `C2:7318`, a second parameterized feedback helper using a different row field pair
- `C2:7397`, a heavy recovery/reset installer that battle-side curative helpers also reuse as their top revival-grade path
- `C2:7550`, the main post-selection controller entry used by the `99xx` timed state family

## `C2:7294` looks like a parameterized feedback helper

Direct callers include `C2:A0BB`, `A0CB`, `A0DB`, `AC3A`, `AC4D`, `AC64`, `B35A`, and `B390`, all of which load `$A972` as the active row and supply a computed value in `X` first.

Current safest reading:

- the routine requires selected-row byte `+0x0C == 1`
- it immediately returns if row byte `+0x1D == 1` is already set, except for a fallback script case
- otherwise it combines the caller's `X` value with row word `+0x13`, normalizes through helper `C2:7126`, and compares the result against row word `+0x15`
- if the comparison fails, it dispatches hardcoded script `EF:69A1` through `C1:DC1C`
- if the comparison passes, it dispatches hardcoded script `EF:69BA` through `C1:DC66` with a parameter built from the caller's input value
- if row byte `+0x1D == 1`, it instead dispatches hardcoded script `EF:7696`

That makes `7294` read best as a range-sensitive feedback helper rather than a general state transition.

## `C2:7318` is the sibling feedback helper using `+0x19/+0x1B`

Direct callers include `C2:A0EB`, `A0FB`, `AC77`, `B372`, and `B3A4`. These callers are structurally very similar to the `7294` callers but feed `7318` instead.

Current safest reading:

- it requires row byte `+0x0C == 1`
- it returns immediately when row byte `+0x1D == 1`
- otherwise it uses row words `+0x19` and `+0x1B`, clamps a derived value through helper `C2:7191`, and dispatches hardcoded script `EF:69D2` through `C1:DC66`

That makes `7318` look like the second axis or alternate-threshold sibling to `7294`, not a completely different subsystem.

A later battle-side pass found that these same two helpers are reused directly by the battle consequence dispatcher at `C2:B2E0`, where selectors `0`, `1`, and `2` wrap `7294`, `7318`, and the chained `7294 + 7318` pair respectively. See also [battle-action-stat-change-family-c2b2e0-b5d7.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/battle-action-stat-change-family-c2b2e0-b5d7.md).
See also [battle-affliction-recovery-family-c29aea-a39d.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/battle-affliction-recovery-family-c29aea-a39d.md).

## `C2:7397` looks like a heavy recovery/reset installer

Direct callers include `C2:9C9D`, `9CD2`, and `AC95`. One of the clearest call sites is `AC95`, which only reaches `7397` when the active selected row in `$A972` has byte `+0x1D == 1`, then passes row word `+0x15` in `X`.

Current safest reading:

- it first dispatches hardcoded script `EF:6F7C`
  - decompile text resolves this as `@{target} was revived!`
- it clears selected-row bytes `+0x1D` through `+0x23` and clears row word `+0x04`
- it sets row byte `+0x0D = 1`
- when row bytes `+0x0E` and `+0x0F` are both zero, it updates paired `9A15` and `9A13` tables through selector `#$005F` using ids stored at row `+0x10`
- it clears row byte `+0x4B` across all 32 candidate rows, then marks the selected row's `+0x4B` byte
- it runs two 16-step initialization loops through `C2:FAD8`, `C2:FB35`, and `C2:69BE`, keyed by selected-row byte `+0x43`

That makes `7397` look broader than a simple controller-phase installer. The older controller note still holds structurally, but the now-pinned `EF:6F7C` text and the battle-side calls from `9CB8` show that this helper is also reused as a heavy recovery or revival-grade reset path over the selected row. See also [battle-affliction-recovery-family-c29aea-a39d.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/battle-affliction-recovery-family-c29aea-a39d.md).

## `C2:7550` looks like the main post-selection controller entry

Direct callers include `C2:599F`, `81F0`, `8259`, `99D8`, `9A1E`, `9A69`, and `A4F1`. The most important callers are `99D8`, `9A1E`, and `9A69`, which confirms that the `99xx` timed state family feeds directly into this routine using `$A972`.

Current safest reading:

- it begins by requiring selected-row byte `+0x0E == 0`; otherwise it jumps into the alternate late handler documented in `notes/class2-late-controller-path-77ca.md`
- it then requires selected-row byte `+0x1E == 2`; otherwise it jumps into a different setup path
- in the `+0x1E == 2` path, it scans six upstream source entries and only keeps entries where the candidate is enabled in `9FB8`, not already marked in `9FBB`, and has neighboring metadata byte `9FCA == 2`
- after that scan, it sets selected-row byte `+0x1D = 1` and clears row bytes `+0x1E` through `+0x23`
- if selected-row byte `+0x0F == 0`, it updates the paired `9A15/9A13` tables for the linked `+0x10` ids, dispatches hardcoded script `EF:6C6B`, and later clears row byte `+0x0C`
- if selected-row byte `+0x0F != 0`, it maps the active `9F8C` id through stride `#$005E`, adds record offset `+0x31`, reads a 32-bit pointer from the `D5:9589` record, dispatches that pointer through `C1:DC1C`, and again later clears row byte `+0x0C`
- after that descriptor-backed dispatch, it either seeds new row-local values from the `983A/983C` family for subtype-like values `0x10` and `0x11`, or it scans all rows for matching subtype values and clears row byte `+0x10` on the matches

The later `77CA` branch now makes an important correction to how these upstream metadata bytes should be read: the startup path here checks `9FCA == 2`, while the late branch excludes `9FC9 == 1`. So the neighboring `9FC9/9FCA` bytes should stay split in the model rather than being collapsed into one vague class flag.

This is no longer best read as a generic controller activation path. The startup branch now fits a collapse or unconscious installer much better: it seeds `+0x1D = 1`, emits either the hardcoded collapse script `EF:6C6B` or descriptor-backed death-style text, and clears battler byte `+0x0C`, which the battler crosswalk already treats as the consciousness-style active gate. It also strengthens the local read that record field `+0x31` is a real pointer payload and that the selected-row controller mixes hardcoded scripts with descriptor-backed script or presentation pointers.

## Working phase model

The safest current phase model is:

1. `$A970/$A972` identify the active selected row
2. `7294` and `7318` provide parameterized feedback based on row-local threshold pairs
3. `7397` installs or resets one selected row as the active controlled row
4. `7550` enters the heavier controller, seeds row-local phase bytes, and dispatches either a hardcoded or descriptor-backed script outcome

That is already a stronger behavioral model than simply saying the `5540` path "keeps going after promotion."

The earlier "pure active flag" reading for selected-row `+0x1D` is no longer the healthiest one here. The `C2:7550` startup branch now aligns much better with the curative-family ailment map: it writes `+0x1D = 1`, emits collapse-side text, and clears battler `+0x0C`. The broader reader set also now helps: party-level scans treat `1` as the only consistently hard-blocked value, while `1` and `2` form the stronger special-handling pair. So the safest current wording is that selected-row `+0x1D` participates in the battler affliction or collapse state family, with value `1` strongly associated with unconscious or collapsed state rather than with a generic controller-active flag.

## What is still unresolved

Still open:

- the exact meaning of row bytes `+0x0D`, `+0x0F`, and `+0x10`, even though `+0x0E` now reads much more strongly as a major phase byte and `+0x4B` as a row-selection marker
- whether the remaining non-curative-looking `+0x1D` uses can all be re-read as battler affliction or collapse handling now that the `7550` startup branch clearly aligns with unconscious or collapsed state
- the finer behavior of the alternate `7550` branches outside the `+0x0E == 0` and `+0x1E == 2` path
- what gameplay meaning the paired feedback scripts `EF:69A1`, `EF:69BA`, `EF:69D2`, `EF:6F7C`, `EF:6C6B`, and `EF:7696` correspond to
- whether helper pair `C2:7126` and `C2:7191` should be understood as range normalization, cursor clamping, or some other coordinate-domain translation

## Current safest takeaway

The safest current takeaway is:

- the post-selection controller is real and phase-structured
- `7294` and `7318` are sibling parameterized feedback helpers
- `7397` installs or resets the selected row into active control state
- `7550` is the main controller entry from the `99xx` timed family and it proves that record `+0x31` is a descriptor-backed pointer payload

That moves the project from "selected row exists" to a concrete model of how that selected row begins doing work.

## Best next target

- See `notes/class2-late-controller-path-77ca.md` for the first late-phase pass. The best next move is to trace descriptor field `+0x4E` and the `D5:7B68` pointer family, or tighten the helper cluster around `C2:3BCF`, `C2:3D05`, and `C2:40A4`, so the late selected-row phase can be named from gameplay behavior instead of just from structure.
