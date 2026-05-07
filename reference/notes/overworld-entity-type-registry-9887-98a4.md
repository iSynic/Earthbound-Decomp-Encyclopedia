# Overworld Entity Type Registry `$9887..$98A4`

This note captures the current ROM-first model for the small registry RAM block used by the overworld visual/frame-selector and child-entity families.

See also [visual-frame-selector-update-family-c4-62ff.md](notes/visual-frame-selector-update-family-c4-62ff.md).
See also [child-entity-spawn-c4b3d0-c40de8.md](notes/child-entity-spawn-c4b3d0-c40de8.md).
See also [party-overlay-arbitration-c216db-c3ebca.md](notes/party-overlay-arbitration-c216db-c3ebca.md).

## Main result

The `$9887..$98A4` block is now best read as a small parallel-array registry that maps stable overworld type codes onto live entity slots. The strongest new correction is that this registry sits on top of a broader primary source array at `$986F`, not a mushroomized-only byte family.

The strongest current layout is:

| address | size | current read |
|---|---|---|
| `$9887` | word | small mode / formation index |
| `$9889` | word | constant slot-base value `#$0018` |
| `$988B` | byte[6] | sorted active type codes |
| `$9891` | byte[6] | per-entry `(entity_slot - 0x18)` byte |
| `$9897` | word[6] | live entity slot indices |
| `$98A3` | byte | active entry count |
| `$98A4` | byte | active party-member count in the registry (count of leading codes `1..4`) |

This is materially stronger than the older vague "small registry family" wording.

## Why `$986F` is now broader than the older mushroomized wording

A later reconciliation pass tightened the source side enough to promote a broader description.

The safest current read is:

- `$986F` = authoritative six-slot source array of active overworld entity type codes
- `$988B/$9891/$9897/$98A3` = derived registry/index layer built from that source

The stronger local proof now comes from three distinct writer or mutator families:

- `C2:4C80..4CD2` bulk-writes party codes `1..4` into `$986F[0..3]` from a party-membership bitmask and then stores the resulting party-count to `$98A4`
- `EF:E1E0..E217` clears `$986F` and reinserts party codes through `C2:28F8` during overworld/entity init
- `C2:182A/182D` removes non-party codes `0x10` and `0x11` through `C2:29BB`

So the array itself is not best described as mushroomized-only. Party codes `1..4` sort first; NPC/effect-style codes `>= 5` can follow in the same six-slot source family.

A useful refinement from the later `C2:16DB` pass is that party-side changes do in fact trigger a broader overlay-arbitration family rather than a mushroomized-only write path. The strongest current local fit is that `C2:16DB` arbitrates whether overlay entity types `0x10/0x11` should remain present when the leading party-range portion changes, while `C3:EBCA` handles the companion overlay-state sync. That strengthens the broader-registry reading without overpromoting the exact identity of those overlay entities.

## Why `$9889` is not a count

The local write pattern is unusually clean here.

The init path writes `#$0018` to `$9889`, and later insertion arithmetic uses that constant as the slot-base when deriving the byte written into `$9891`.

So the safest current read is:

- `$9889` is a fixed slot-base constant
- it is not an active-entry count

## Why `$98A4` can now be named more concretely

`$98A4` no longer needs to stay at the vague "boundary index" level.

Two independent local paths agree:

- the bank-`00` scan around `C0:32F0..3318` walks `$986F` while entries remain in the party-code range below `5`, then stores the resulting count-like index to `$98A4`
- the bulk party writer around `C2:4C80..4CD2` stores the number of party codes written directly to `$98A4`

So the safest current read is: `$98A4` is the active party-member count in the source/registry family, specifically the count of leading `$986F` entries whose values are in the `1..4` party range.

That still explains why older notes saw it as a boundary index: mechanically, it is the boundary between leading party codes and later non-party codes. But the semantic role is clearer now than before.

## Why `$98A3` still looks count-like

The insert/remove paths both support the count role directly.

- insertion increments `$98A3`
- removal decrements `$98A3`
- later loops treat it as the active-entry bound

So `$98A3` remains the authoritative active-entry count.

## Why `$9891` is a real third parallel array

The registry is no longer just "codes plus slot words."

The insertion and removal paths shift and maintain:

- `$988B`
- `$9897`
- `$9891`

in parallel.

The inserted `$9891` byte is derived as `(slot - 0x18)`, which makes it a compact slot-offset companion field rather than a second id.

So the safest current read is:

- `$988B` = sorted type codes
- `$9897` = live slot indices
- `$9891` = compact per-entry slot-offset byte

## How the registry is used

The registry is now a good fit for the resolver family in bank `C4`.

- `C4:608C` special-cases `A = #$00FF` to return the fixed slot-base at `$9889`, otherwise scans `$988B` and returns the matching live entity slot from `$9897`
- `C4:6397` iterates the active registry entries and broadcasts frame-selector updates across matching entities
- `C4:B4FE/B519` use the same registry-backed lookup to spawn or clear attached child entities
- `C0:3E25`, `C0:3E5A`, `C0:3E9D`, and `C0:3EC3` form a predecessor/order helper family over `$988B/$9897`, used by nearby movement/update paths to compare the current entry against the preceding registry entry and update a per-slot gap/order bit.
- `C0:3F1E` fans the current transition snapshot out to every active registry-backed live entity by copying `$9877/$987B/$987F/$9881` into slot arrays like `$0B8E/$0BCA/$2AF6/$2BAA`.

`C4:608C` also looks broader than the older mushroomized wording: it handles both leading party codes and later non-party codes through the same `$988B/$9897` lookup path.

The important structural refinement is that `$988B` is a derived lookup layer, not the primary truth. Inserts keep `$988B/$9891/$9897` synchronized incrementally, while broader rebuild paths can reconstruct that layer from `$986F`.

So the current best read is: this registry lets higher-level systems target overworld entities by stable type code instead of by volatile live slot index, while `$986F` remains the broader authoritative source array beneath it.

## Local lifecycle

The broad local lifecycle now looks like:

- init clears the arrays and seeds `$9889 = #$0018`
- bulk party-side writers can populate `$986F` directly and seed `$98A4` from the number of leading party entries
- insertion keeps the entries sorted by type code, fills `$988B/$9897/$9891`, and increments `$98A3`
- removal shifts the same arrays left, decrements `$98A3`, and preserves some departing entity world-position state before despawn
- full-reset paths clear the derived layer and rebuild it from `$986F`, which is why `$986F` now reads as the primary source while `$988B` is the runtime lookup copy

That is a genuine registry/cache workflow, not just a scratch list.

## `C3:E012` cross-check

A useful supporting clue is the stride-8 ROM table at `C3:E012`.

The strongest current local read is:

- it is indexed by `(type_code - 1)`
- offset `+6` behaves like a base entity-slot field during registry insertion/setup

This makes the registry look even more like a type-to-slot system, though the exact meanings of the other fields in that table should stay a little cautious.

## What remains open

A few parts still need care.

- `$9887` is definitely a small mode/formation-like selector, but its exact gameplay-visible meaning is still open.
- the exact player-visible meaning of the non-party codes in `$986F` beyond the currently observed `0x10/0x11` range still needs more local naming work.
- the exact meaning of the payload side beyond `$9891/$9897` remains open in the neighboring visual/overlay notes.

## Best current interpretation

The safest current read is:

- `$988B/$9891/$9897/$98A3` form a six-entry overworld entity-type registry
- `$9889 = #$0018` is the fixed live-slot base used by that registry
- bank-`C4` frame-selector and child-entity systems use this registry to target live entities by stable type code

## Confidence

- `$9889` as constant slot-base `#$0018`: high confidence
- `$988B/$9897/$9891` as parallel registry arrays: high confidence
- `$98A3` as active-entry count: high confidence
- `$98A4` as active party-member count / party-code boundary: high confidence
- exact gameplay-visible meaning of `$9887`: still cautious
