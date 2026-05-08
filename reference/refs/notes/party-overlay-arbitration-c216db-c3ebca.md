# Party Overlay Arbitration `C2:16DB` / `C3:EBCA`

This note captures the current local read of the side-effect family around `C2:16DB`, the nearby presence check at `C2:239D`, and the companion updater `C3:EBCA`.

See also [mushroomized-walking-remap-family.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/mushroomized-walking-remap-family.md).
See also [overworld-entity-type-registry-9887-98a4.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/overworld-entity-type-registry-9887-98a4.md).

## Main result

The safest current read is:

- `C2:16DB` is broader than a mushroomized-only hook
- it is best read as a party-composition-driven overlay arbitration helper
- `C3:EBCA` is its companion overlay-state updater
- the managed overlay entity types still look likely to be the mushroomized walking overlays, but that identity belongs to the overlay-entity layer, not to the arbitration mechanism itself

So the old binary question "is `C2:16DB` mushroomized or general?" now has a cleaner answer: the invocation and arbitration layer is general across party composition changes, while the specific overlay entities being inserted or removed may still be mushroomized-specific.

## Why `C2:16DB` now looks broader than mushroomized-only

The strongest current local constraint is the caller pattern.

The party-code insertion and removal helpers call `C2:16DB` for the leading party-code range, not only for a separately proved mushroomized-status gate:

- `C2:28F8` insertion path calls `C2:16DB` for party codes `1..4`
- `C2:29BB` removal path calls `C2:16DB` for party codes `1..4`
- those same call sites skip the helper for later non-party codes

That is a much better fit for a party-composition overlay arbitration helper than for a narrowly mushroomized-status-specific callback.

## `C2:239D`

`C2:239D` now has a good local role as a small registry presence check.

The safest current read is:

- input: a type code in `A`
- behavior: scan the active source family rooted at `$986F`
- return: the matching code if found, `0` if absent

That role fits very naturally beside `C2:16DB`: once the helper decides what overlay type should exist, `C2:239D` answers whether that type is already present in the live source family.

## `C2:16DB`

The current best local model is that `C2:16DB` is an arbitration pass over the party-facing portion of the active type registry.

The safest current summary is:

- it iterates the leading party-range entries from `$986F`, bounded by `$98A4`
- it uses per-party state rooted in the `$99CE/$99F1` family while doing that pass
- its post-loop decision can remove or preserve overlay entity types `0x10` and `0x11` through the standard registry mutators
- it does not look like the routine that directly owns `$9891/$9897/$9A0B`

So `C2:16DB` is best treated as a registry-arbitration helper that decides whether the overlay entity types should be present, not as the downstream visual-state builder itself.

## `C3:EBCA`

The companion helper `C3:EBCA` is now best read as the state-sync half of the same higher-level family.

The safest current read is:

- it is called immediately after the party-side `C2:16DB` updates
- it works more on overlay-state/timing/update data than on the registry-source decision itself
- it sits naturally on the "keep the overlay entities' state coherent" side of the split, while `C2:16DB` sits on the "should the overlay entities exist right now?" side

That division is much healthier than the older model where both routines were just one unresolved blob.

## Overlay entity types `0x10` and `0x11`

The currently observed non-party codes `0x10` and `0x11` remain the key bridge back to the mushroomized notes.

The safest current read is:

- `C2:16DB` arbitrates the presence of overlay entity types `0x10` and `0x11`
- those types are still strong candidates for the mushroomized walking overlay entities
- but that specific identity is still one step short of fully local proof

So the mushroomized label should currently stay attached to the overlay-entity interpretation, not to the registry-arbitration helper itself.

## What I am not promoting yet

A few potentially useful leads from the wider pass are still being left out of the mainline model for now:

- any claim that depends on a conflicting reinterpretation of `D5:5000 + 0x19`
- stronger naming for the overlay entity class beyond "likely mushroomized walking overlay"
- firmer semantic names for the deeper `C3:EBCA` tables and `C4:8F98` until their local consumers are tighter

## Best current interpretation

The safest current interpretation is:

- `$986F` is the broader active overworld entity-type source array
- `C2:16DB` arbitrates whether overlay entity types `0x10/0x11` should be present when the party-facing portion changes
- `C3:EBCA` is the companion overlay-state sync/update pass
- the specific overlay entity identities are still likely mushroomized, but that part remains a little more cautious than the arbitration role itself

## Confidence

- `C2:16DB` as broader party-composition overlay arbitration: medium-high confidence
- `C2:239D` as registry presence check: medium-high confidence
- `C3:EBCA` as companion overlay-state updater: medium confidence
- `0x10/0x11` as specifically mushroomized overlay entities: medium confidence, still partly reference-backed
