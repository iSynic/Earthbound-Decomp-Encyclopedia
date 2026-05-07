# Class2 Solidification Item Action C2A5EC A630

This note captures the strongest current local model for the item-side action entry at `C2:A5EC`, which combines direct damage with a `STATUS_2::SOLIDIFIED` apply attempt through `C2:724A`.

See also [class2-affliction-apply-helper-724a.md](notes/class2-affliction-apply-helper-724a.md).
See also [class2-battler-affliction-crosswalk.md](notes/class2-battler-affliction-crosswalk.md).
See also [class2-d57b68-battle-action-table-match.md](notes/class2-d57b68-battle-action-table-match.md).

## Working Names

- `C2:A5EC` = `RunDamagePlusSolidificationItemAction`
- `C2:A630` = `ApplySolidificationStatusFromItemAction`

## Main result

`C2:A5EC` is the strongest current local candidate for an item-side damage-plus-solidification action.

The body does all of the following in one entry path:

- runs the ordinary target gate through `C2:7CFD`
- runs a success gate through `C2:7CAF` with immediate `0x00FA`
- computes a damage value from `100 - target defense`
- routes that value through `C2:8125` / `ApplyDamageToSelectedTarget`
- then attempts `Y = 4`, `X = 2` through `C2:724A`
- on success, displays `EF:6BEF` = `@{target}'s body solidified!`
- on failure, displays `EF:766E`

That is materially stronger than just saying this is another `724A` caller. It is an action-entry path that combines damage with subgroup-byte `+0x1F = 4`.

## Why `+0x1F = 4` matters here

The current affliction crosswalk already has a strong local mapping for `C2:724A` with `X = 2`, `Y = 4`:

- `X = 2` selects battler affliction byte `+0x1F`
- `Y = 4` is the strongest current fit for `STATUS_2::SOLIDIFIED`
- success text `EF:6BEF` is the familiar solidification text

So the late body at `A5EC` is now a concrete bridge between:

- the battle action table
- direct damage logic
- the `battler::afflictions+2` temporary-status byte
- the solidification player-facing text

## Why this looks item-side

The action-table crosswalk gives a useful local-plus-reference-backed anchor.

`lookup_ref_symbol.py` finds `C2:A5EC` as a live `battle_action_table.yml` entry, and the corresponding entry metadata is:

- action type `item`
- direction `enemy`
- target `one`
- text pointer `C9:7F56`

That `C9:7F56` entry text is also unusually suggestive locally:

- `@{user} lashed ... with {item}!`

That is a much better fit for an item-use strike than for a PSI or generic status spell.

## Strongest reference-backed candidate

The strongest current reference-backed candidate is `BTLACT_HANDBAG_STRAP`.

Why that fit is unusually good:

- the reference `handbag_strap.asm` body is item-side
- it deals damage before applying solidification
- it then applies `STATUS_2::SOLIDIFIED`
- it displays the same solidification text on success and the generic failure text otherwise

That does not prove a final symbolic rename by itself, but the fit is much tighter than a generic "solidify-like" label.

## Relation to nearby helpers

The nearby wrapper at `C2:A552` is now best read as a narrower solidification apply helper:

- it enters directly at `C2:724A`
- on success, displays `EF:6BEF`
- on failure, displays `EF:766E`

But `A552` is not currently pinned as a battle-action-table entry.

`C2:A5EC` is the stronger gameplay-facing anchor because it is a live action entry and includes the surrounding damage or accuracy setup, not just the status write and message tail.

## Current safest interpretation

The safest current interpretation is:

- `C2:A5EC` is a live item-side battle action that deals damage and then attempts solidification through `C2:724A`
- the status write is `battler::afflictions+2 = 4`
- the strongest current reference-backed candidate is `BTLACT_HANDBAG_STRAP`
- the helper at `C2:A630` is the concrete solidification apply branch inside that larger action body

## What is still open

Still open:

- whether `C2:A5EC` should be promoted all the way to the final symbolic name `BTLACT_HANDBAG_STRAP`
- whether the nearby item entries at `C2:A5D1`, `C2:A5DA`, and `C2:A5E3` belong to the same broader item family or are only neighboring non-solidification entries
- whether `C2:A552` is ever reached from another live action-table entry that has not yet been pinned

## Current takeaway

The safest current takeaway is:

- `C2:A5EC` is a real late `D5:7B68` action-table entry
- it combines direct damage with a `STATUS_2::SOLIDIFIED` apply attempt
- it is the strongest current local anchor for an item-side solidification action
- the best current reference-backed candidate is `BTLACT_HANDBAG_STRAP`

## Best next target

The best next move is to trace a few more late `D5:7B68` item entries around `C2:A5D1..A5EC`, so we can decide whether they form a broader status-item cluster or only a loose neighborhood of unrelated item actions.
