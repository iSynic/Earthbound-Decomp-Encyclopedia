# Battle Affliction Recovery Family `C2:9AEA..A39D`

This note captures the current best local model for the battle-side affliction recovery helper ladder centered on `C2:9AEA`.

See also [battle-action-stat-change-family-c2b2e0-b5d7.md](notes/battle-action-stat-change-family-c2b2e0-b5d7.md).
See also [class2-battler-affliction-crosswalk.md](notes/class2-battler-affliction-crosswalk.md).
See also [class2-post-selection-controller-phases.md](notes/class2-post-selection-controller-phases.md).

## Working Names

- `C2:9AEA` = `TryRecoverSelectedBattlerNarrowAffliction`
- `C2:9B7A` = `TryRecoverSelectedBattlerCurativeAfflictions`
- `C2:9C2C` = `TryRecoverSelectedBattlerBroadAfflictions`
- `C2:9CB8` = `TryRecoverSelectedBattlerHardState`
- `C2:A39D` = `TryRecoverSelectedBattlerPoisonOnly`

## Main result

The helpers at `C2:9AEA`, `C2:9B7A`, `C2:9C2C`, `C2:9CB8`, and `C2:A39D` are not generic battle tails.

They now read best as a small battle-side affliction recovery ladder:

- `C2:9AEA`
  - narrow recovery helper for cold, sunstroke, and asleep-style status
- `C2:9B7A`
  - broader recovery helper for poison, nausea-like sickness, crying, and strange-style status, with fallback to `9AEA`
- `C2:9C2C`
  - still broader recovery helper for diamondized and paralyzed or numbed states, with fallback to `9B7A`
- `C2:9CB8`
  - top-level revival or hardest-incapacitation wrapper over `9C2C`, with a direct `7397` recovery path when row byte `+0x1D == 1`
- `C2:A39D`
  - narrow poison-only item-side cure wrapper

So the tails hanging off `C2:B2E0` are now much less anonymous:

- selector `9 -> C2:9AEA` belongs to the narrow affliction-recovery side
- selector `0x0A -> C2:A39D` belongs to the poison-only item-side side

## `C2:9AEA`: narrow affliction recovery

`C2:9AEA` checks active row `$A972` against the affliction region rooted at `+0x1D`.

Current local behavior:

- if row byte `+0x1D == 7`
  - clear that byte
  - display `EF:6EBC`
  - `@{target} got over the cold!`
- else if row byte `+0x1D == 6`
  - clear that byte
  - display `EF:6F38`
  - `@{target}'s sunstroke was cured!`
- else if row byte `+0x1F == 1`
  - clear that byte
  - display `EF:6F54`
  - `@{target} woke up!`
- else
  - display `EF:7696`
  - `@It had no visible effect on {target}!`

So `9AEA` is best treated as the narrow curative helper for cold, sunstroke, and asleep-style status.

## `C2:9B7A`: broader curative sibling with fallback to `9AEA`

`C2:9B7A` clearly extends the same family.

Current local behavior:

- if row byte `+0x1D == 5`
  - clear that byte
  - display `EF:6E97`
  - `@The poison was removed from {target}'s body!`
- else if row byte `+0x1D == 4`
  - clear that byte
  - display `EF:6E81`
  - `@{target} felt much better!`
- else if row byte `+0x1F == 2`
  - clear that byte
  - display `EF:6ED1`
  - `@{target} finally stopped crying...`
- else if row byte `+0x20 == 1`
  - clear that byte
  - display `EF:6F1E`
  - `@{target} went back to normal!`
- else
  - recurse to `C2:9AEA`

That makes `9B7A` best treated as the broader curative sibling that handles poison, nausea-like sickness, crying, and strange-style status before falling back to the narrower `9AEA` set.

## `C2:9C2C`: still broader recovery helper

`C2:9C2C` extends the same ladder again.

The strongest locally pinned branches are:

- if row byte `+0x1D == 3`
  - clear that byte
  - display `EF:6E67`
  - `@{target}'s numbness is gone!`
- else if row byte `+0x1D == 2`
  - clear that byte
  - display `EF:6E4A`
  - `@{target}'s body returned to normal!`
- else
  - defer to `C2:9B7A`

There is also a harder `+0x1D == 1` branch in the middle of `9C2C`, but the disassembly there is still not as clean as the surrounding branches. The strongest safe statement is:

- it does not behave like a simple text-only clear branch
- it calls `C2:6BB8`
- it then routes through `C2:7397` on success-path behavior
- that makes it look like the hardest recovery case in this ladder, likely a heavier body-state or solidification-style recovery rather than an ordinary one-byte status clear

So `9C2C` is best treated as the broader mobility or body-state recovery helper, with a still-slightly-soft hardest branch.

## `C2:9CB8`: top-level hard-state wrapper

`C2:9CB8` is a short wrapper above `9C2C`.

Current local behavior:

- if row byte `+0x1D == 1`
  - load row word `+0x15`
  - route directly through `C2:7397`
- else
  - call `C2:9C2C`

That is strong evidence that value `1` in row byte `+0x1D` is the hardest recovery case in this family. `7397` itself opens by dispatching `EF:6F7C`, which the decompile text resolves as `@{target} was revived!`, then clears bytes `+0x1D..+0x23` and reseeds later row state. So the healthiest current read is that `9CB8` is the top-level revival or hardest-incapacitation recovery wrapper in this ladder, not just another ordinary status clear.

## `C2:A39D`: poison-only item-side helper

The entry at `C2:A39D`, which is what `C2:B5DF` actually calls, is much narrower.

Its behavior is simple:

- check active row byte `+0x1D`
- if it equals `5`
  - clear that byte
  - display `EF:6E97`
  - `@The poison was removed from {target}'s body!`
- otherwise
  - do nothing visible

So `A39D` is best treated as a poison-only item-side cure helper, not as another generic stat or consequence routine.

## Relation to the battler affliction crosswalk

This family lines up well with the already-mapped affliction region in [class2-battler-affliction-crosswalk.md](notes/class2-battler-affliction-crosswalk.md).

The safest current split is:

- row byte `+0x1D`
  - now looks like the main one-byte ailment enum for unconscious, diamondized, paralyzed, nauseous, poisoned, sunstroke, and cold or sniffling states
- row byte `+0x1F`
  - includes asleep-style and crying-style subgroup values
- row byte `+0x20`
  - includes strange-style subgroup value `1`

That is strong local evidence that this helper ladder is operating directly over the live battler-affliction block, not over some unrelated status scratch.

## Promoted `+0x1D` ailment-value map

The local cure texts now line up cleanly enough with the reference ailment list to promote a real value map for row byte `+0x1D` in this family.

Safest current map:

- `1` = unconscious
- `2` = diamondized
- `3` = paralyzed or numbed
- `4` = nauseous
- `5` = poisoned
- `6` = sunstroke
- `7` = cold or sniffling

Why this is now strong enough to promote:

- `1 -> 9CB8 -> 7397 -> EF:6F7C`
  - `@{target} was revived!`
- `2 -> 9C2C -> EF:6E4A`
  - `@{target}'s body returned to normal!`
  - reference Healing text explicitly says this tier cures being diamondized
- `3 -> 9C2C -> EF:6E67`
  - `@{target}'s numbness is gone!`
  - reference Healing text explicitly says this tier cures paralysis
- `4 -> 9B7A -> EF:6E81`
  - `@{target} felt much better!`
  - reference ailment list names value `4` as nauseous
- `5 -> 9B7A/A39D -> EF:6E97`
  - `@The poison was removed from {target}'s body!`
- `6 -> 9AEA -> EF:6F38`
  - `@{target}'s sunstroke was cured!`
- `7 -> 9AEA -> EF:6EBC`
  - `@{target} got over the cold!`
  - reference ailment list names value `7` as sniffling

That makes `+0x1D` look much less like a vague subgroup byte. In this recovery family it behaves like the main one-byte ailment enum for the unconscious / diamondized / numbness / nausea / poison / sunstroke / cold set.

## Relation to the battle action table

The reference battle action table gives a useful supporting cross-check.

Reference-backed and locally consistent action-table observations:

- `C2:9AEA`, `C2:9B7A`, `C2:9C2C`, and `C2:9CB8` appear as a sequence of four one-target party PSI actions with PP costs `5`, `8`, `20`, and `38`
- the same code addresses are also reused by one-target party item actions
- `C2:A39D` appears only as an item-side one-target party action

That strongly supports the local read that these are the battle-side curative or healing-status helpers, with `A39D` as a narrower poison-only item helper.

A stronger reference-backed cross-check is now available too: the four PSI-side entries using `9AEA`, `9B7A`, `9C2C`, and `9CB8` have PP costs `5`, `8`, `20`, and `38`, which line up exactly with the usual `Healing alpha / beta / gamma / omega` progression while the local behavior widens from narrow status cure to broad recovery to revival-grade handling. So the safest current wording is:

- `9AEA` = strongest reference-backed candidate for `Healing alpha`
- `9B7A` = strongest reference-backed candidate for `Healing beta`
- `9C2C` = strongest reference-backed candidate for `Healing gamma`
- `9CB8` = strongest reference-backed candidate for `Healing omega`

I am still keeping those as reference-backed final names rather than replacing the local behavioral names outright in the top summary.

## Current safest interpretation

The safest current interpretation is:

- `9AEA .. 9CB8` form a progressively broader battle-side affliction recovery ladder
- each higher helper handles additional status families, then falls back into the lower helper
- `A39D` is a narrow poison-only item-side cure helper
- the `C2:B2E0` dispatcher uses only the narrowest and most item-like ends of that ladder as its tail selectors

## Confidence

- `9AEA` as narrow cold/sunstroke/sleep recovery helper: high confidence
- `9B7A` as broader poison/sickness/crying/strange recovery helper with fallback to `9AEA`: high confidence
- `9C2C` as broader diamondized/paralyzed recovery helper with fallback to `9B7A`: high confidence
- `9CB8` as top-level revival or hardest-incapacitation wrapper over `9C2C`: moderate-to-high confidence
- `A39D` as poison-only item-side cure helper: high confidence
- `9AEA/9B7A/9C2C/9CB8` as reference-backed `Healing alpha/beta/gamma/omega`: moderate-to-high confidence
- promoted `+0x1D` value map `1..7` as unconscious/diamondized/paralyzed/nauseous/poisoned/sunstroke/cold`: moderate-to-high confidence

## What is still open

- the exact one-to-one action-name mapping for the four PSI-side entries in this ladder
- how far this `+0x1D` ailment map should be promoted outside the curative family, since the selected-row controller at `C2:7550` also writes `+0x1D = 1` in a broader non-curative setup path
