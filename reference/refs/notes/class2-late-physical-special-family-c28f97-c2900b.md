# Class2 Late Physical Special Family C28F97 C2900B

This note captures the strongest current local model for the late `D5:7B68` action-entry slice around `C2:8F97`, `C2:8FF9`, and `C2:900B`.

See also [class2-d57b68-battle-action-table-match.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-d57b68-battle-action-table-match.md).
See also [class2-d57b68-early-entry-name-crosswalk.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-d57b68-early-entry-name-crosswalk.md).
See also [class2-affliction-apply-helper-724a.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-affliction-apply-helper-724a.md).
See also [class2-battler-affliction-crosswalk.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-battler-affliction-crosswalk.md).

## Main result

This late-table seam is no longer best treated as one anonymous cluster.

The safest current split is:

- `C2:8F97` = strongest current local fit for a level-2 physical poison attack
- `C2:8FF9` = `DOUBLE_BASH`
- `C2:900B` = one-target fire-damage or flaming-fireball action

Those three neighbors sit next to each other in the table, but their bodies are structurally different enough that they should not be collapsed into one generic "enemy physical" note.

## `C2:8F97` is the poison-on-hit physical side

`C2:8F97` now has a much healthier local read than before.

The body:

- gates through the ordinary target and hit chain at `C2:7CFD`, `C2:82F8`, `C2:83F8`, and `C2:84AD`
- if the final dodge-style check fails, prints `EF:7655`
- otherwise runs the standard physical-on-hit pair `C2:8523 / C2:856B`
- then calls `C2:724A` with `X = 0`, `Y = 5`
- on success prints `EF:6B18`

That last step is the key bridge. `C2:724A` is now our grouped affliction apply-or-upgrade helper, and `X = 0`, `Y = 5` writes primary affliction byte `+0x1D = 5`, which is the currently anchored poison side.

The entry text for the live table row fits that body unusually well:

- entry `100` -> `C2:8F97` -> `EF:7EAC`
- `EF:7EAC` reads as an enemy attacking with poison fangs

Together with the quarantined reference file `level_2_attack_poison.asm`, this is now the strongest current local-plus-reference-backed fit for `BTLACT_LEVEL_2_ATK_POISON`.

## `C2:8FF9` is the double-bash wrapper

`C2:8FF9` is now the cleanest member of this slice.

Its body is just:

- `JSL C2859F`
- `JSL C2859F`
- `RTL`

That is exactly the shape we would expect for a pure double-hit wrapper over the already-anchored bash family at `C2:859F`.

The live action-table row is also a clean fit:

- entry `102` -> `C2:8FF9` -> `EF:7F02`
- `EF:7F02` reads as an enemy attacking continuously

The quarantined reference file `bash_twice.asm` is an exact structural match, so this one is strong enough to promote:

- `C2:8FF9` = `BTLACT_DOUBLE_BASH`

## `C2:900B` is the fire-damage side

`C2:900B` is not another status writer and not another physical wrapper.

The body:

- seeds literal `0x015E` (`350`) into `C2:6AFD`
- stores the resulting amount in local DP state
- reads current target row byte `+0x3A`
- uses that byte as the index argument for `C2:8125`
- lets `C2:8125` drive the actual damage application and display-side follow-through

The live row and message text fit a fire-damage interpretation much better than a generic special attack label:

- entry `104` -> `C2:900B` -> `EF:7F32`
- `EF:7F32` reads as an enemy spewing a flaming fireball

So the safest current local name is:

- one-target fire-damage or flaming-fireball action

There is a useful reference-side cross-check here too: the literal `350` lines up with the quarantined `BTLACT_350_FIRE_DAMAGE` helper. I am still keeping the final symbolic name for `C2:900B` slightly cautious, because the local body is a full action wrapper over `C2:8125`, not just the tiny standalone damage helper exported in that reference file.

## Action-table anchors

The useful late-table anchors for this slice are:

- entry `100` -> `C2:8F97` -> enemy one-target piercing-physical -> poison-fangs text
- entry `102` -> `C2:8FF9` -> enemy one-target physical -> attack-continuously text
- entry `104` -> `C2:900B` -> enemy one-target other -> flaming-fireball text

That gives us one clean poison-on-hit physical action, one clean double-bash wrapper, and one clean fire-damage special action in immediate sequence.

## Current safest interpretation

The safest current interpretation is:

- `C2:8F97` is the late poison-on-hit physical action and strongest current fit for `BTLACT_LEVEL_2_ATK_POISON`
- `C2:8FF9` is the exact `BTLACT_DOUBLE_BASH` wrapper over `C2:859F`
- `C2:900B` is a real one-target fire-damage wrapper keyed by the target-side `+0x3A` byte and flavored by the flaming-fireball text family

## What is still open

Still open:

- whether `C2:8F97` should be promoted all the way from strongest-fit wording to the final reference export name
- the exact human-facing meaning of target row byte `+0x3A` in the `C2:900B` path
- whether `C2:900B` matches a named reference export more cleanly in a later action-file lane

## Current takeaway

The safest current takeaway is:

- this late-table neighborhood is now substantially less anonymous
- `8F97` is poison-on-hit physical
- `8FF9` is exact double bash
- `900B` is a fire-damage special action rather than another status family
