# Class2 Concentration Seal Family C28D5A C2A3D1

This note captures the strongest current local model for the two live battle-action-table entries that write battler affliction byte `+0x21 = 4` and then display the shared concentration or PSI-seal text at `EF:6C0B`.

See also [class2-battler-affliction-crosswalk.md](notes/class2-battler-affliction-crosswalk.md).
See also [class2-d57b68-battle-action-table-match.md](notes/class2-d57b68-battle-action-table-match.md).
See also [class2-second-pointer-consumer-40a4.md](notes/class2-second-pointer-consumer-40a4.md).

## Working Names

- `C2:8D5A` = `RunConcentrationSealAction`
- `C2:A3D1` = `RunItemSideConcentrationSealAction`

## Main result

The current ROM exposes two live `D5:7B68` action-entry routines that converge on the same effect:

- `C2:8D5A`
- `C2:A3D1`

Both are enemy-direction, one-target action entries in the action table. Their entry records differ in action type and entry text, but both route into the same local effect shape:

- run the ordinary target gating path through `C2:7CFD`
- run a second success or eligibility gate through `C2:8D41`
- if the target's row byte `+0x21` is still zero, write `4`
- dispatch `EF:6C0B` through `C1:DC1C`
- otherwise fall back to `EF:766E`

That makes these two routines the strongest current local family for the `+0x21 = 4` battler-affliction state.

## Why the pairing is strong

The two bodies are structurally parallel.

`C2:8D5A`:

- enters through the action-table wrapper slot at `D5:7B68`
- runs `C2:7CFD`
- runs `C2:8D41`
- computes `target + 0x21`
- if nonzero, jumps to failure text `EF:766E`
- otherwise writes `4` and displays `EF:6C0B`

`C2:A3D1`:

- enters through another action-table wrapper slot at `D5:7B68`
- runs the same `C2:7CFD`
- runs the same `C2:8D41`
- computes `target + 0x21`
- if nonzero, jumps to failure text `EF:766E`
- otherwise writes `4` and displays `EF:6C0B`

The only meaningful difference in the successful branch is the entry text and metadata in the parent `D5:7B68` record.

## Action-table context

The decompile-side action-table crosswalk gives a useful structural match for both entries:

- entry `85` -> code `C2:8D5A` -> direction `enemy`, target `one`, action type `other`, text pointer `EF:9DA1`
- entry `159` -> code `C2:A3D1` -> direction `enemy`, target `one`, action type `item`, text pointer `EF:8E3C`

Those are different action-table identities, but their effect bodies are locally the same concentration or PSI-seal write.

That matters because it shows `+0x21 = 4` is not a one-off quirk of one move. The same state is reused by at least:

- one ordinary enemy-side action entry
- one item-side action entry

## Shared message pointer

The shared success text is `EF:6C0B`.

That script is the familiar concentration or PSI-seal message:

- `@{target} was not able to concentrate!`
- `@{target} was not able to use PSI!`

This is the strongest current local bridge from the `+0x21` affliction byte to the player-facing concentration or PSI-seal state.

## Strongest current interpretation

The safest current interpretation is:

- row byte `+0x21` is `battler::afflictions+4`
- local value `4` is a real concentration or PSI-seal state
- `C2:8D5A` and `C2:A3D1` form a shared local family that applies that state when the target is still clear
- failure text `EF:766E` is the generic "did not work" fallback for an already-occupied or otherwise invalid target state

This lines up unusually well with the `ebsrc` `BTLACT_DISTRACT` body, which also:

- checks whether the target already has a concentration-group status
- writes `STATUS_4::CANT_CONCENTRATE4`
- displays `MSG_BTL_FUUIN_ON`

I am still keeping that final name one notch cautious because the local ROM evidence proves the effect family directly, while the exact exported reference name still comes from the side project.

## What is not yet proved

Still open:

- whether `C2:8D5A` should be promoted all the way to the reference symbolic name `BTLACT_DISTRACT`
- whether entry `159` is a strict item-side clone of the same battle action or only a close sibling
- whether the current ROM ever writes `+0x21 = 1`, or only the `4` side of the concentration-group enum in live action lanes we have traced so far

## Current takeaway

The safest current takeaway is:

- `C2:8D5A` and `C2:A3D1` are a real shared concentration or PSI-seal apply family
- both write battler affliction byte `+0x21 = 4`
- both display `EF:6C0B`
- both fail through `EF:766E`
- together they make the local read of `battler::afflictions+4` much stronger than a single isolated wrapper would

## Best next target

The best next move is to trace a few more `D5:7B68` entries that write battler-affliction bytes directly, so the late action table can be grouped by concrete status families instead of only by PSI wrapper quartets.
