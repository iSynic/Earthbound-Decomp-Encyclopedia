# Class2 Late Normalization And Odor Family C29051 C29254

This note captures the strongest current local model for the late `D5:7B68` action-entry slice around `C2:9051`, `C2:90C6`, `C2:916E`, and `C2:9254`.

See also [class2-d57b68-battle-action-table-match.md](notes/class2-d57b68-battle-action-table-match.md).
See also [class2-d57b68-early-entry-name-crosswalk.md](notes/class2-d57b68-early-entry-name-crosswalk.md).
See also [class2-affliction-apply-helper-724a.md](notes/class2-affliction-apply-helper-724a.md).
See also [class2-battler-affliction-crosswalk.md](notes/class2-battler-affliction-crosswalk.md).
See also [class2-battle-text-cluster-overview.md](notes/class2-battle-text-cluster-overview.md).
See also [c2-late-normalization-odor-runtime-polish.md](notes/c2-late-normalization-odor-runtime-polish.md).

## Working Names

- `C2:9051` = `QueuedBattlerStatShieldNormalizationCallback`
- `C2:90C6` = `RunBattlerNormalizationActionWrapper`
- `C2:916E` = `RunDiamondizeAction`
- `C2:9254` = `RunOdorOffenseReductionAction`
- `C2:AF1F` = `SnapshotRestoreBattlerNormalizationContext`

## Main result

This late slice is no longer best treated as one muddy `90xx` blob.

The safest current local split is:

- `C2:9051` = queued battler stat-and-shield normalization callback
- `C2:90C6` = special normalization or return-to-original-form wrapper that can schedule `9051`
- `C2:916E` = one-target diamondize action
- `C2:9254` = one-target or all-target odor or stinky-gas offense-reduction action

That is a materially better model than the earlier vague "scenario/controller" wording.

## `C2:9051` is the queued normalization callback

`C2:9051` is not a live `D5:7B68` action row. It is the callback pointer that `C2:90C6` installs through `C2:40A4`.

Its body now reads cleanly:

- copies battler bytes `+0x32..+0x36` into live bytes `+0x26/+0x28/+0x2A/+0x2C/+0x2E`
- that is: `base_offense/base_defense/base_speed/base_guts/base_luck` back into `offense/defense/speed/guts/luck`
- clears battler `+0x23` and `+0x25`, which line up with `afflictions[6]` and `shield_hp`
- then dispatches text `EF:7123` through `C1:DC1C`

So the healthiest local name is a queued battler normalization callback, not a generic late controller.

## `C2:90C6` is the front-end normalization wrapper

`C2:90C6` is a real live second-pointer target from `D5:7B68`.

Current table anchors:

- entry `247` -> `C2:90C6` -> item-use style text at `EF:8E27`
- entry `248` -> `C2:90C6` -> pale-gray-light text at `EF:8D9F`

Its body has two layers.

First, if `$AA12` is nonzero, it scans battler rows at `$9FAC` and looks for a live row with:

- `+0x0C != 0`
- `+0x0E == 0`
- row id `+0x00 == 4`

For the first such row it:

- clears `$AA12`
- passes the row pointer and `$AA14` into `C2:AF1F`
- clears row `+0x04`
- prints `EF:7142`, the "returned to original form" text block

Then, regardless of whether that front-end cleanup happened, it:

- runs `C2:6E00`, the all-active battler target-mask builder now labeled in
  source as `MaskSet_BuildActiveCandidates`
- runs `C2:70E4`, the current-mask pruner for flagged battlers
- queues callback `C2:9051` through `C2:40A4`
- clears `$A96C/$A96E`

The safest current interpretation is:

- `C2:90C6` is a special battler normalization wrapper that can also force a return-to-original-form cleanup before the queued stat-and-shield normalization completes

I am still keeping the exact symbolic reference export cautious. The local body is much stronger now, but the precise reference name is not yet pinned.

## `C2:AF1F` is a snapshot-restore helper for that front-end path

`C2:AF1F` is pointer-heavy, but its role is healthier than before.

The routine takes two pointer pairs through direct-page slots and repeatedly reads fields from both sources at offsets like `+0x11`, `+0x13`, `+0x15`, `+0x17`, and `+0x19`, caching them into local temporaries.

Used from `C2:90C6`, the best current read is:

- `AF1F` is a row-snapshot restore or merge helper that applies the `$AA14` staging block back onto the selected battler before the wrapper prints "returned to original form"

That is still body-described rather than fully named, but it is no longer just an opaque pointer helper.

The source body now names the stable tail contracts without trying to over-name
the pointer merge:

- enemy row `+0x5D` as the mirror/metamorphosis success byte
- `$AA12/$AA14/$AA62` as the selected battler id, staging block, and staging
  mode used by the normalization/metamorphosis bridge
- `EF:6A99` / `EF:6AB3` as the metamorphose success/failure scripts
- `C1:DC1C` as the direct battle-text pointer dispatch

Neighbor `C2:B172` now carries the condiment continuation contracts: it uses
`C1:DB33` to find the matching condiment, removes it through the active
inventory helper at `C1:8EAD`, scans the 7-byte `D5:EA77` condiment table, and
emits the C9 spice hit/miss text scripts before returning either the matched
condiment recovery payload or the item-table params fallback.

## `C2:916E` is the one-target diamondize side

`C2:916E` is a separate live `D5:7B68` action row.

Current table anchor:

- entry `228` -> `C2:916E` -> one-target `piercing physical` row with `EF:8BE8`

The local body is now in solid shape:

- gates through the ordinary target checks `7CFD / 82F8 / 83F8 / 84AD`
- runs the normal hit path `8523 / 856B / 7C96`
- calls `C2:724A` with `X = 0`, `Y = 2`
- that anchors battler affliction byte `+0x1D = 2`, our current diamondized value
- zeroes battler bytes `+0x1E..+0x23`
- calls `C2:72AD`
- adjusts `$A974/$A976` by a `B9:A800` table-selected delta and adds row `+0x3D` into `$A978`
- prints `EF:6AC7`, the diamondized text, on success
- fails through `EF:7655`

So `C2:916E` is now a strong local fit for a one-target diamondize action.

## `C2:9254` is the odor or stinky-gas offense-cut family

`C2:9254` is also a separate live `D5:7B68` action row family.

Current table anchors:

- entry `232` -> `C2:9254` -> horrid-odor text at `EF:8C58`
- entry `273` -> `C2:9254` -> stinky-gas text at `EF:8EBE`

Its body is much cleaner now:

- gates through `C2:7CFD`
- snapshots current battler `offense` from row `+0x26`
- calls `C2:7DDC`
- `7DDC` lowers current offense by at least `1`, using the high nibble of the current value when available, then clamps the result to a floor based on roughly three quarters of `base_offense`
- the action then reports the resulting delta through `C1:DC66` using text `C8:F885`

That means `C2:9254` is no longer an anonymous neighboring tail. It is a real odor or stinky-gas offense-reduction family.

## Field-level bridge

Useful battler-field anchors in this slice are now:

- `+0x23` = `afflictions[6]` or shield-group byte
- `+0x25` = `shield_hp`
- `+0x26` = `offense`
- `+0x28` = `defense`
- `+0x2A` = `speed`
- `+0x2C` = `guts`
- `+0x2E` = `luck`
- `+0x32..+0x36` = saved base offense, defense, speed, guts, and luck

That is why the queued `9051` callback is now much better described as normalization rather than generic state work.

## Current safest interpretation

The safest current interpretation is:

- `90C6` is a special battler-normalization action wrapper with an optional return-to-original-form prepass
- `9051` is the queued stat-and-shield normalization callback it installs
- `916E` is a separate one-target diamondize action
- `9254` is a separate odor or stinky-gas offense-cut family

## What is still open

Still open:

- the exact symbolic reference-backed name for `90C6`
- the exact identity of battler id `4` in the `90C6` front-end scan
- a stronger local name for `AF1F` beyond snapshot-restore helper
- the exact human-facing phrasing of `EF:7123`, even though `9051`'s mechanical role is now clear
- a broader symbolic name for the `B172` continuation once the tail after the
  current source-module boundary is promoted

## Current takeaway

The current takeaway is that the late `90xx` strip is not one subsystem.

It contains:

- a queued normalization path (`9051`, fronted by `90C6`)
- a real one-target diamondize action (`916E`)
- a real odor or stinky-gas offense-down family (`9254`)

That makes this area much easier to reason about when we return to the late action table.
