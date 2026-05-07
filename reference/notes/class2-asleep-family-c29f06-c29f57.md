# Class2 Asleep Family C29F06 C29F57

This note captures the strongest current local model for the asleep-status late action family rooted at `C2:9F06` and wrapper `C2:9F57`.

See also [class2-affliction-apply-helper-724a.md](notes/class2-affliction-apply-helper-724a.md).
See also [class2-battler-affliction-crosswalk.md](notes/class2-battler-affliction-crosswalk.md).
See also [class2-d57b68-early-entry-name-crosswalk.md](notes/class2-d57b68-early-entry-name-crosswalk.md).

## Working Names

- `C2:9F06` = `RunResistCheckedAsleepStatusAction`
- `C2:9F57` = `RunAsleepStatusWrapperAction`

## Main result

`C2:9F06` now reads as a real asleep-status apply body over battler affliction subgroup byte `+0x1F`, and `C2:9F57` is just a wrapper that reuses it.

Current safest local split:

- `C2:9F06` -> all-target asleep-status apply body with one extra target-side gate through `row + 0x3C -> C2:6BB8` / `RollActionChanceGate`
- `C2:9F57` -> thin wrapper that reuses `C2:9F06`

The successful apply path is:

- `X = 2`
- `Y = 1`
- `C2:724A`
- success text `EF:6C55`
- failure text `EF:766E`

That is a strong local fit for:

- `battler::afflictions+2 = 1`
- asleep

## `C2:9F06`

Locally `C2:9F06` does all of the following:

- gates through `C2:7CFD`
- reads target byte `row + 0x3C`
- passes that byte through `C2:6BB8` / `RollActionChanceGate`
- only continues on success of that extra target-side gate
- then sets `Y = 1`, `X = 2`
- applies that pair through `C2:724A`
- on success, displays `EF:6C55`
- on failure, displays `EF:766E`

`EF:6C55` is the local asleep success text:

- `@{target} fell asleep!`

That makes `C2:9F06` the strongest current late-table anchor for `battler::afflictions+2 = 1`.

## `C2:9F57`

`C2:9F57` is only:

- `REP #$31`
- `JSL C2:9F06`
- `RTL`

So it does not define a separate effect body. It just reuses the same asleep-status logic.

Current live table anchors for this family:

- entry `0x0035` (`53`) -> enemy / all / psi / cost `18` -> text `EF:8543` -> second pointer `C2:9F57`
- entry `0x005A` (`90`) -> enemy / all / other / text `EF:9E47` -> second pointer `C2:9F57`

Those reused rows show the family is not limited to one action flavor. The same all-target asleep apply body is reused by at least one PSI row and one `other` row.

## Why this matters

This closes another gap in the currently exposed temporary-status subgroup.

The late `D5:7B68` action table now has concrete local anchors for the whole `+0x1F` ladder:

- `+0x1F = 1` -> asleep through `C2:9F06 / 9F57`
- `+0x1F = 2` -> crying through `C2:8C69 / 8DFC`
- `+0x1F = 3` -> immobilized or could-not-move through `C2:8CB8`
- `+0x1F = 4` -> solidified through `C2:8CF1 / A5EC`

That makes the temporary-status subgroup much less piecemeal than it was before this pass.

## Strongest current interpretation

The safest current interpretation is:

- `C2:9F06` is a real all-target asleep-status apply body over `battler::afflictions+2 = 1`
- `C2:9F57` is only a wrapper over that same body
- the extra `row + 0x3C -> C2:6BB8` / `RollActionChanceGate` path makes the family look more like a gated or resist-checked variant than a plain unconditional status writer

## What is still open

Still open:

- the exact reference-side names for entries `53` and `90`
- whether entry `53` is best matched to a PSI-side sleep family or another all-target ailment family with reused generic PSI-intro text
- the exact semantic meaning of target byte `row + 0x3C`

## Best next target

The best next move is to keep outward on the neighboring numeric-effect routines like `C2:8E42`, because the affliction side of this late table is now getting close to a full local map.
