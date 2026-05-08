# Visual Frame-Selector Update Family (`C4:62FF..C4:6507`)

This note documents the family of routines at `C4:62FF` through `C4:6507` that update entity frame/pose selectors and trigger redraws.

See also [sprite-pose-descriptor-cache-2a06-2cd6.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/sprite-pose-descriptor-cache-2a06-2cd6.md).
See also [child-entity-spawn-c4b3d0-c40de8.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/child-entity-spawn-c4b3d0-c40de8.md).
See also [overworld-entity-type-registry-9887-98a4.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/overworld-entity-type-registry-9887-98a4.md).

## Main result

These routines divide into two subfamilies:

1. frame-selector updaters (`C4:62FF`, `C4:6331`, `C4:6363`, `C4:6397`)
2. world-positioned entity initializers (`C4:64B5`, `C4:6507`)

The first group updates `$2AF6` and triggers redraws when the selected frame value changes. The second group creates or refreshes world-positioned entities, then seeds their initial visual selector state.

## Frame-selector updaters

### `C4:62FF` - update by `$2C9A` match

Locally this path:

1. calls `C4:605A` with `A` as the lookup key
2. `C4:605A` scans entity slots for `$2C9A[slot] == A`
3. if a slot is found and `$2AF6[slot]` differs from the input `X`, it updates `$2AF6[slot]`
4. then it calls `C0:A48F`

So the safest current read is: update the frame selector for the entity whose caller-assigned visual-type id matches the input.

### `C4:6331` - update by `$2CD6` match

This is the sibling path that uses `C4:6028` instead of `C4:605A`.

`C4:6028` scans entity slots for `$2CD6[slot] == A`, and on a successful match the code applies the same `$2AF6` update + redraw sequence.

So the safest current read is: update the frame selector for the entity whose cached pose-table index matches the input.

### `C4:6363` - update by small registry match

This path uses `C4:608C` with an 8-bit input instead of the broader entity-scan helpers above. `C4:608C` now reads more concretely as a lookup over the small parallel registry at `$988B/$9891/$9897/$98A3`; see [overworld-entity-type-registry-9887-98a4.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/overworld-entity-type-registry-9887-98a4.md). The stronger current model is that `$988B` is the derived lookup layer while the broader source family lives at `$986F`.

A useful new local constraint is that `C4:608C` handles the whole registry family uniformly: `A = #$00FF` returns the fixed base at `$9889`, while ordinary codes scan `$988B` and return the matching live slot from `$9897` whether the code is a leading party code or a later non-party code.

If a slot is found and `$2AF6` changes, it updates the selector and then calls `C0:A780` instead of `C0:A48F`.

So the safest current read is: update the frame selector for a registry-selected overworld entity type rather than a general full-scan entity family.

### `C4:6397` - broadcast update over the registry family

This is the heavier sibling. It iterates the same small registry family and pushes a new frame selector to every matching live entry instead of stopping after the first hit. The stronger current registry model now makes that family read much more like a six-entry overworld type registry than an anonymous RAM list.

The safest current read is: broadcast a frame-selector update to multiple related entries in the registry-backed overworld entity family.

## `C0:A48F` vs `C0:A780`

Both look like pose-frame redraw triggers, but they are not the same entry point.

- `C0:A48F` is used by the `$2C9A` and `$2CD6` single-target paths.
- `C0:A780` is used by the registry-backed paths.

The safest current statement is that the two frame-selector families converge on related redraw logic but use different setup/data entry points.

## World-positioned entity initializers

### `C4:64B5`

This path prepares a parameter record, calls `C01E49`, then seeds:

- `$2AF6[new_slot]` from caller-side state
- `$2C9A[new_slot]` from the caller's input selector id

The strongest current read is: initialize a new or newly selected world-positioned entity and assign both its current frame selector and its caller-driven visual-type id.

### `C4:6507`

This is the close sibling that uses the same general setup pattern but targets a caller-selected slot instead of the looser allocation path.

So the safest current read is: forced-slot variant of the same world-positioned initializer family.

## Resolver-key distinction

The useful structural split is:

| resolver | field matched | current read |
|---|---|---|
| `C4:605A` | `$2C9A` | caller-assigned visual-type/effect id |
| `C4:6028` | `$2CD6` | cached pose-table index |
| `C4:608C` | `$988B/$9897` registry | RAM-side overworld type-registry lookup |

That distinction matters because the same pose (`$2CD6`) can plausibly appear under multiple caller-driven visual types (`$2C9A`), and because the registry-backed path can target both leading party codes and later non-party codes through the same `$988B` lookup layer.

## What still remains open

- the exact semantic name of the small registry family used by `C4:608C`
- the exact differences between the `A48F` and `A780` redraw branches
- the format of the caller-side parameter record feeding `C4:64B5` / `C4:6507`

## Best next target

The best next move is to tighten the registry family around `C4:608C` and the associated RAM block, because that should clarify when the single-target update helpers are used versus the broadcast-style update path.
