# Class2 Persistent Status Action Pair C28BBE C28BFD

This note captures the strongest current local model for the two neighboring `D5:7B68` action entries at `C2:8BBE` and `C2:8BFD`.

See also [class2-affliction-apply-helper-724a.md](notes/class2-affliction-apply-helper-724a.md).
See also [class2-battler-affliction-crosswalk.md](notes/class2-battler-affliction-crosswalk.md).
See also [class2-d57b68-battle-action-table-match.md](notes/class2-d57b68-battle-action-table-match.md).

## Working Names

- `C2:8BBE` = `RunMushroomizeStatusAction`
- `C2:8BFD` = `RunPossessStatusAction`

## Main result

`C2:8BBE` and `C2:8BFD` are the strongest current late-table anchors for the persistent hard-heal subgroup byte at battler affliction offset `+0x1E`.

Locally:

- `C2:8BBE` gates the target through `C2:7CFD`, then applies `Y = 1`, `X = 1` through `C2:724A`, and on success displays `EF:6B81`
- `C2:8BFD` gates the target through `C2:7CFD`, checks target row byte `+0x0E`, then applies `Y = 2`, `X = 1` through `C2:724A`, and on success displays `EF:6B98`
- both fall back through `EF:766E` on failure

That makes them the strongest current local action-entry pair for:

- `battler::afflictions+1 = 1`
- `battler::afflictions+1 = 2`

## Why the pair is strong

The two entries are adjacent in the late `D5:7B68` table and both share the same structural shape:

- enemy direction
- one target
- action type `other`
- direct status apply through `C2:724A`
- success text through `C1:DC1C`
- failure through the generic did-not-work text

The important difference is the applied value and the success text.

### `C2:8BBE`

The success branch is:

- `Y = 1`, `X = 1`
- `C2:724A`
- `EF:6B81`

That matches the current local mapping for:

- affliction subgroup byte `+0x1E`
- value `1`
- mushroomized-style text

### `C2:8BFD`

The success branch is:

- ensure target row byte `+0x0E` is still zero
- `Y = 2`, `X = 1`
- `C2:724A`
- `EF:6B98`

That matches the current local mapping for:

- affliction subgroup byte `+0x1E`
- value `2`
- possessed-style text

It also does a little extra setup after success through the `A18C/A18D/A18F` side path, which fits the idea that possession has extra companion behavior beyond the raw status write.

## Action-table context

The decompile-side battle action table gives a useful structural anchor:

- entry `75` -> code `C2:8BBE` -> direction `enemy`, target `one`, action type `other`, text pointer `EF:9C30`
- entry `76` -> code `C2:8BFD` -> direction `enemy`, target `one`, action type `other`, text pointer `EF:9C51`

Those two entry texts are also compatible with the local effect family:

- `EF:9C30` looks like a spore-scattering attack text
- `EF:9C51` looks like a possession-oriented frightening or ghostly attack text

## Strongest reference-backed candidates

The strongest current reference-backed candidates are:

- `C2:8BBE` -> `BTLACT_MUSHROOMIZE`
- `C2:8BFD` -> `BTLACT_POSSESS`

Why that fit is strong:

- reference `mushroomize.asm` writes `STATUS_1::MUSHROOMIZED = 1`
- reference `possess.asm` writes `STATUS_1::POSSESSED = 2`
- those values exactly match the local `Y = 1` and `Y = 2` writes through `X = 1`
- the local success texts match the same player-facing effects unusually well

I am still keeping the final exported names one notch cautious because the exact late-table slot numbering still comes from the side reference, but the behavioral fit is now very strong.

## What is not yet proved

Still open:

- whether `C2:8BBE` and `C2:8BFD` should be promoted all the way to those final symbolic names in every note
- the exact meaning of target row byte `+0x0E` in the extra possession gate
- how the neighboring late-table entries at `C2:8C69`, `C2:8CB8`, and `C2:8CF1` partition the temporary-status side around crying, immobilized, and similar states

## Current takeaway

The safest current takeaway is:

- `C2:8BBE` and `C2:8BFD` are real late `D5:7B68` action-table entries
- both apply battler affliction subgroup `+0x1E`
- local value `1` is now strongly anchored to mushroomized at the action-entry level
- local value `2` is now strongly anchored to possessed at the action-entry level
- together they make the `STATUS_1` subgroup much stronger than a reader-side or helper-side inference alone

## Best next target

The best next move is to decode the neighboring late entries at `C2:8C69`, `C2:8CB8`, and `C2:8CF1`, because those look like the next temporary-status action cluster beside this persistent-status pair.
