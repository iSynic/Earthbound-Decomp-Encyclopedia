# Class2 Temporary Status Action Cluster C28C69 C28CB8 C28CF1

This note captures the strongest current local model for the neighboring late `D5:7B68` action entries rooted at `C2:8C69`, `C2:8CB8`, and `C2:8CF1`.

See also [class2-affliction-apply-helper-724a.md](notes/class2-affliction-apply-helper-724a.md).
See also [class2-battler-affliction-crosswalk.md](notes/class2-battler-affliction-crosswalk.md).
See also [class2-persistent-status-action-pair-c28bbe-c28bfd.md](notes/class2-persistent-status-action-pair-c28bbe-c28bfd.md).

## Working Names

- `C2:8C69` = `RunCryingStatusAction`
- `C2:8CB8` = `RunImmobilizedStatusAction`
- `C2:8CF1` = `RunSolidifiedStatusAction`

## Main result

These three neighboring late action entries now read as a real temporary-status cluster over battler affliction subgroup byte `+0x1F`.

Current safest local split:

- `C2:8C69` -> strong local crying action
- `C2:8CB8` -> strong local immobilized or could-not-move action family
- `C2:8CF1` -> strong local solidification action

All three live in the same late enemy-side one-target `other` stretch of the action table, and all three converge on subgroup byte `+0x1F` through `C2:724A` or its immediately adjacent helper shape.

## Action-table context

The current late-table bridge is:

- entry `78` -> `C2:8C69` -> enemy / one / other / text `EF:9CAD`
- entries `79..82` -> `C2:8CB8` -> enemy / one / other / texts `EF:9CD1`, `EF:9CF1`, `EF:9D14`, `EF:9D3E`
- entry `83` -> `C2:8CF1` -> enemy / one / other / text `EF:9D62`
- entry `87` -> `C2:8DFC` -> enemy / all / other / text `EF:9DDA`

That already suggests a themed local cluster rather than unrelated isolated actions.

## `C2:8C69`

`C2:8C69` is now much cleaner than it was before the DP or state-tracing pass.

Locally it does all of the following:

- gates through `C2:7CFD`
- performs one extra target-side gate through `row + 0x39 -> C2:6BB8` /
  `RollActionChanceGate`
- then sets `Y = 2`, `X = 2`
- applies that pair through `C2:724A`
- on success, displays `EF:6BBB`
- on failure, displays `EF:766E`

That is a strong local fit for:

- `battler::afflictions+2 = 2`
- crying

The reference `BTLACT_CRYING2` body is also a strong reference-backed match, because it writes `STATUS_2::CRYING` with the same one-target enemy-action shape and uses the same crying message group.

## `C2:8CB8`

`C2:8CB8` is also clean.

Locally it does all of the following:

- applies `Y = 3`, `X = 2` through `C2:724A`
- on success, displays `EF:6BD3`
- on failure, displays `EF:766E`

That is the best current local fit for:

- `battler::afflictions+2 = 3`
- the could-not-move or immobilized subgroup value

This entry is reused by multiple neighboring late-table records (`79..82`), which suggests a small family of different action texts that converge on the same immobilized effect body.

## `C2:8CF1`

`C2:8CF1` is clean too.

Locally it:

- gates through `C2:7CFD`
- runs an additional success gate through `C2:7C96`
- applies `Y = 4`, `X = 2` through `C2:724A`
- on success, displays `EF:6BEF`
- on failure, displays `EF:766E`

That is the strongest local fit for:

- `battler::afflictions+2 = 4`
- solidification

Compared with the item-side solidification anchor at `C2:A5EC`, this gives us a second independent action-entry anchor for the same temporary-status value, but on the enemy `other` side rather than the item side.

## Why this matters

This cluster materially improves the late-table picture.

We no longer just have one concentration family and one item-side solidification action. The late table now has multiple concrete affliction families:

- persistent hard-heal statuses at `+0x1E` through `C2:8BBE / 8BFD`
- temporary statuses at `+0x1F` through `C2:8C69 / 8CB8 / 8CF1`
- concentration or PSI-seal at `+0x21` through `C2:8D5A / A3D1`

That makes the late `D5:7B68` region read much more like a real grouped status-action slice of the battle action table, not just a pile of disconnected tail routines.

## Strongest current interpretation

The safest current interpretation is:

- `C2:8C69`, `C2:8CB8`, `C2:8CF1`, and now `C2:8DFC` form a temporary-status late action cluster over `battler::afflictions+2`
- `C2:8C69` and `C2:8DFC` strongly anchor the crying value `2`, with `BTLACT_CRYING2` as the strongest current reference-backed candidate for the one-target body
- `C2:8CB8` strongly anchors the immobilized or could-not-move value `3`
- `C2:8CF1` strongly anchors the solidified value `4`

## What is still open

Still open:

- exact reference-side action names for entries `78..83`
- whether the repeated `C2:8CB8` entry texts correspond to different thematic attacks sharing one immobilize effect body, or a narrower family such as multiple spray or mucus attacks
- whether the extra `row + 0x39 -> C2:6BB8` / `RollActionChanceGate` path in `C2:8C69` has a more specific semantic meaning than a general extra eligibility check

## Current takeaway

The safest current takeaway is:

- the late `D5:7B68` table now has a real temporary-status action cluster
- `C2:8C69`, `C2:8CB8`, and `C2:8CF1` are strong anchors for `+0x1F = 2`, `+0x1F = 3`, and `+0x1F = 4`
- together with the persistent-status pair and the concentration family, this gives the late table a much clearer affliction-action layout

## Best next target

The best next move is to continue outward from `C2:8CB8`'s repeated entry texts and see whether those later records can be grouped by concrete attack flavor, now that the crying side is no longer the weak point in this cluster.
