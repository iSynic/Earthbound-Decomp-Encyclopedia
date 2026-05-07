# Class2 Strange Status Family C28D3A C28DBB C2A056

This note captures the strongest current local model for the strange-status late action family rooted at `C2:8D3A`, `C2:8DBB`, and `C2:A056`.

See also [class2-affliction-apply-helper-724a.md](notes/class2-affliction-apply-helper-724a.md).
See also [class2-battler-affliction-crosswalk.md](notes/class2-battler-affliction-crosswalk.md).
See also [class2-d57b68-early-entry-name-crosswalk.md](notes/class2-d57b68-early-entry-name-crosswalk.md).

## Working Names

- `C2:8D3A` = `RunStrangeStatusWrapperAction`
- `C2:8DBB` = `RunDirectStrangeStatusAction`
- `C2:A056` = `RunResistCheckedStrangeStatusAction`

## Main result

These helpers now read as a real strange-status action family over battler affliction subgroup byte `+0x20`.

Current safest local split:

- `C2:A056` -> strongest current local strange-status apply body with one extra target-side resist-style gate
- `C2:8D3A` -> thin wrapper that reuses `C2:A056`
- `C2:8DBB` -> direct strange-status sibling without the extra resist-style gate

All of the successful apply paths converge on:

- `X = 3`
- `Y = 1`
- `C2:724A`
- success text `EF:6C3A`
- failure text `EF:766E`

That is a strong local fit for:

- `battler::afflictions+3 = 1`
- strange

## `C2:A056`

`C2:A056` is the clearest body in the family.

Locally it does all of the following:

- gates through `C2:7CFD`
- reads target byte `row + 0x3B`
- passes that byte through `C2:6BB8` / `RollActionChanceGate`
- only continues on success of that extra target-side gate
- then sets `Y = 1`, `X = 3`
- applies that pair through `C2:724A`
- on success, displays `EF:6C3A`
- on failure, displays `EF:766E`

`EF:6C3A` is the local strange message group:

- `@{target} felt ... strange`

That makes `C2:A056` the strongest current local anchor for `battler::afflictions+3 = 1`.

The extra `row + 0x3B -> C2:6BB8` / `RollActionChanceGate` path is especially useful, because it matches the broad shape of a resist-style variant rather than a plain status writer.

In the action table, the strongest current live anchor is:

- entry `0x003A` (`58`) -> enemy / one / psi / cost `10` -> text `EF:8543` -> second pointer `C2:A056`

That makes `BTLACT_BRAINSHOCK_A` the strongest current reference-backed candidate for the canonical PSI use of this body, because the reference routine is also a one-target PSI action that applies `STATUS_3::STRANGE` with an extra resist check before calling the shared status inflicter.

## `C2:8D3A`

`C2:8D3A` is a trivial wrapper:

- `REP #$31`
- `JSL C2:A056`
- `RTL`

In other words, it does not define a new effect body of its own. It reuses the same strange-status logic as `C2:A056`.

Current live table anchors:

- entry `0x0054` (`84`) -> enemy / one / other / text `EF:9D81`
- entry `0x00CF` (`207`) -> enemy / one / other / text `EF:83A8`

Those two reused rows are useful because they show the family is not limited to one PSI slot. The same strange-status body is being reused by at least two other one-target `other` actions with different attack flavor text.

## `C2:8DBB`

`C2:8DBB` is the direct sibling without the extra target-side `row + 0x3B` gate.

Locally it does all of the following:

- gates through `C2:7CFD`
- sets `Y = 1`, `X = 3`
- applies that pair through `C2:724A`
- on success, displays `EF:6C3A`
- on failure, displays `EF:766E`

That is still the same strange-status write:

- `battler::afflictions+3 = 1`

Current live table anchor:

- entry `0x0056` (`86`) -> party / none / other / text `EF:9DBD`

So the safest current local read is that `C2:8DBB` is a generic strange-status one-target sibling, while `C2:A056` is the stronger resist-checked or PSI-style branch.

## Why this matters

This closes the last open subgroup in the currently exposed battler-affliction block.

The local action-table anchors are now much healthier:

- `+0x1E` -> mushroomized / possessed through `C2:8BBE / 8BFD`
- `+0x1F` -> crying / immobilized / solidified through `C2:8C69 / 8CB8 / 8CF1`
- `+0x20` -> strange through `C2:A056 / 8D3A / 8DBB`
- `+0x21` -> concentration or PSI-seal through `C2:8D5A / A3D1`

That means the late `D5:7B68` slice now has concrete local action families for all of the currently exposed non-primary battler-affliction groups.

## Strongest current interpretation

The safest current interpretation is:

- `C2:A056` is the canonical strange-status apply body in this family, and `BTLACT_BRAINSHOCK_A` is its strongest current reference-backed PSI candidate
- `C2:8D3A` is just a wrapper that reuses `C2:A056`
- `C2:8DBB` is a sibling strange-status body without the extra resist-style gate
- all three locally anchor `battler::afflictions+3 = 1` as strange

## What is still open

Still open:

- the exact local symbolic names for entries `84`, `86`, and `207`
- whether `C2:8DBB` best matches reference `BTLACT_FEELSTRANGE`, `BTLACT_PRAY_RENDING_SOUND`, or another generic strange-inflict action
- the exact human-facing meaning of target byte `row + 0x3B`

## Best next target

The best next move is to keep grouping the neighboring late `D5:7B68` entries by concrete status family, especially the mixed enemy or party `other` rows around `0x0056..0x0058`, now that the strange-status side is no longer soft.
