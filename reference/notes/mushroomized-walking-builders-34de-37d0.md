# Mushroomized Walking Builders 34DE 369B 37D0

This note captures the stronger local model for the bank-`00` mushroomized-walking builder family centered on `C0:34D6`, `C0:369B`, `C0:39E5`, `C0:3A24`, and the downstream consumers `C0:A254`, `C0:8C58`, and `C0:AD56`.

See also [mushroomized-walking-remap-family.md](notes/mushroomized-walking-remap-family.md).
See also [mushroomized-overlay-redirect-c08c58.md](notes/mushroomized-overlay-redirect-c08c58.md).
See also [mushroomized-overlay-animation-scripts.md](notes/mushroomized-overlay-animation-scripts.md).
See also [class2-cc19-20-eshop2-single-use.md](notes/class2-cc19-20-eshop2-single-use.md).

## Working Names

- `C0:2C3E` = `RefreshSpecialTraversalModeState`
- `C0:2C83` = `ResetMushroomizedWalking`
- `C0:2C89` = `MushroomizationMovementSwap`
- `C0:34D6` = `SortAndExport_MushroomizedWalkingEntries`
- `C0:369B` = `Insert_MushroomizedWalkingActiveEntry`
- `C0:37D0` = `AppendMushroomizedEntryAndRefreshController`
- `C0:39E5` = `RefreshMushroomizedEntryTargetPositions`
- `C0:3A24` = `Rebuild_MushroomizedWalkingController`

## Main result

The mushroomized-walking subsystem no longer looks like a bare direction-swap table.

The strongest current local read is that bank `00` is maintaining a small controller for up to six active mushroomized movement entries plus companion overlay or presentation state:

- `C0:3A24` clears and rebuilds the whole family
- `C0:369B` inserts one active entry into the ordered working set
- `C0:34D6` re-sorts and exports compact per-entry state to later movement / overlay consumers
- `C0:39E5` refreshes per-entry target-position state from live player position, but now looks broader than a mushroomized-only helper
- `C0:A254` converts those per-entry anchor positions into on-screen draw coordinates
- `C0:8C58` enqueues the resulting visual records into the broader display pipeline
- `C0:AD56` advances the small overlay-animation scripts that supply the current visual payload words

So the local structure is now better described as a mushroomized movement-controller family with ordered active entries and companion presentation state, not just an isolated remap-byte table.

## `C0:3A24` looks like the full rebuild entry

The bytes at `C0:3A24` do a clean subsystem reset and rebuild:

- clear `$98A4` and `$98A3`
- clear six byte slots at `7E:988B+N`
- clear six word slots at `7E:9897+2*N`
- clear the paired byte buffers at `7E:97F5+0x96+N` and `7E:97F5+0x9C+N`
- set `$5D7E = 1` while rebuilding
- walk the six-entry source family at `$986F`
- call `C0:369B` for each nonzero entry
- clear `$5D7E` again after the rebuild loop

That is a much stronger shape than a one-off table mutator. It is a proper rebuild path for the whole mushroomized controller state.

## `C0:369B` looks like insert-one-active-entry

The input to `C0:369B` is one byte from the six-entry `$986F` family.

Locally it does four distinct jobs:

1. find the insertion point against the current ordered byte list at `$988B`
2. shift the existing entry arrays downward to make room
3. increment the active-entry count at `$98A3`
4. derive per-entry selector/payload state from `DATA_C3E012`, `$0A62`, `$987D`, and the table rooted at `$5156`

The inserted entry byte itself is stored to `$988B + slot`.

That means `$988B` now looks much more like an ordered active-entry code list than a generic scratch buffer.

## `C0:34D6` looks like export-and-sort

`C0:34D6` starts from the current active-entry count in `$98A3`, preloads one mapped byte per entry through `$9891 -> #$005F -> $9A0B`, builds sort keys, bubble-sorts the working rows, and then exports the result back out.

The important part is the shape of those sort rows:

- key in local temp `+$1A`
- companion word from `$9897`
- companion byte from `$9891`

The sort key is not a plain copy of the entry byte.

It starts from `$988B`, then adds priority bands:

- values `>= 5` get pushed upward by `+$0300`
- some lower values get `+$0100` depending on the `99DC` class reached through `$9897 -> $0E9A -> #$005F -> $99DC`

So the active entry order is meaningful controller state, not just input order.

After sorting, the routine exports:

- byte-sized values to `7E:97F5+0x96+N`
- word entries back to `$9897 + 2*N`
- byte-sized values to `7E:97F5+0x9C+N`
- mapped byte values back into the `$9A0B` family
- a reverse slot map at `$0F8A`

It then copies the first word in `$9897` to `$9889` and calls `C0:32EC`, `C0:2C3E`, and `C4:7F87`.

That is much closer to refresh controller exports for downstream movement / overlay code than to swap directions in place.

## Source Polish Follow-Up

The 2026-05-06 C0 source polish pass added local source anchors for the merged
post-`SPAWN_VERTICAL` tail entries: `C0:2C3E` refreshes the special traversal
mode state and can restore the leader from bicycle mode, `C0:2C83` clears the
mushroomized-walking latch, and `C0:2C89` is the reference-named movement swap
body used by the player stepper when `$5DA0` is active. The same pass also
named `C0:34D6`'s call into `C0:2C3E`.

## `C0:39E5` looks like shared per-entry target-position refresh

`C0:39E5` walks the current active-entry list at `$988B`, takes the paired word from `$9897`, snapshots live player position from `$9877/$987B` into per-entry word tables at `$0B8E/$0BCA`, and calls `C0:A254` for each entry.

The stronger current boundary is that this is probably not mushroomized-specific by itself. It still fits the builder family we mapped here, but the newer bank-`C0` scene and interaction work suggests `C0:39E5` is a broader shared staged-position sync helper that this subsystem reuses.

## `C0:A254` turns anchor positions into draw coordinates

The downstream consumer at `C0:A254` is very clean:

- load per-entry anchor X from `$0B8E + 2*slot`
- subtract `#$0031`
- store the result to `$0B16 + 2*slot`
- load per-entry anchor Y from `$0BCA + 2*slot`
- subtract `#$0033`
- store the result to `$0B52 + 2*slot`

That is strong evidence that:

- `$0B8E/$0BCA` are anchor or world-position-like coordinates
- `$0B16/$0B52` are derived on-screen or draw-position coordinates

The later consumers support that read.

- `C0:A26B+` compares `$0B16/$0B52` and the anchor tables for ordering and proximity decisions.
- `C0:AC89+`, `C0:ACBA+`, `C0:ACFF+`, and `C0:AD3F+` feed `$0B16/$0B52` directly into `C0:8C58`, which behaves like a display-record enqueue helper.

So this downstream path pushes the subsystem strongly toward an overlay or presentation interpretation, not just a hidden movement remap.

## `C0:8C58` looks like the generic draw-record redirector

The body at `C0:8C58` is small but very informative.

It pushes caller `X` and `A`, selects one of four buckets from `$2400`, and appends a four-word record to that bucket.

The stored fields are effectively:

- caller `A`
- caller `X`
- caller `Y`
- caller `$000B`

In the overlay call sites, that reads naturally as:

- a per-entry visual payload or frame-like word in `A`
- draw X in `X`
- draw Y in `Y`
- a companion attribute or selector in `$000B`

So the mushroomized controller is clearly feeding a broader display pipeline, not just modifying invisible movement state.

## `C0:AD56` is the overlay-animation script interpreter

The caller families around `C0:AC89`, `C0:ACBA`, `C0:ACFF`, and `C0:AD3F` do not use static payloads.

They maintain per-entity script-pointer/timer pairs:

- `$301E/$305A`
- `$30D2/$310E`
- `$2F6A/$2FA6`
- `$2EB6/$2EF2`

Those pointers are seeded from bank-`C4` tables:

- `C4:0EF0`
- `C4:0F04`
- `C4:0EB0`
- `C4:0EE4`

The reference cross-check now makes the top-level mapping clear:

- `0EF0` = small ripple
- `0F04` = big ripple
- `0EB0` = sweating
- `0EE4` = mushroomized

So the broader local family is really the shared entity-overlay system, and the mushroomized overlay is the `2EB6/2EF2/2F2E -> C4:0EE4` channel inside it.

## Stronger local readings for the main WRAM fields

The strongest current ROM-first readings are:

- `$986F` = six-entry source code family for mushroomized walking
- `$988B` = ordered active-entry code list derived from `$986F`
- `$98A3` = active-entry count
- `$98A4` = selected or boundary index derived elsewhere from the `$986F` scan
- `$9891` = per-entry mapped selector byte used with the `#$005F` helper
- `$9897` = per-entry word payload used as a downstream controller / overlay key
- `$9A0B` = per-selector byte payload reused during export and refresh
- `$0B8E/$0BCA` = per-entry anchor positions
- `$0B16/$0B52` = per-entry derived draw coordinates

The exact player-facing names of `$9891`, `$9897`, and `$9A0B` are still not final, but they are clearly part of one controller family rather than unrelated scratch bytes.

## Why the reference names are now more plausible

The quarantined `ebsrc` tree exports these globals in the same neighborhood:

- `ENTITY_MUSHROOMIZED_OVERLAY_PTRS`
- `ENTITY_MUSHROOMIZED_NEXT_UPDATE_FRAMES`
- `ENTITY_MUSHROOMIZED_SPRITEMAPS`
- `MUSHROOMIZATION_TIMER`
- `MUSHROOMIZATION_MODIFIER`
- `MUSHROOMIZED_WALKING_FLAG`

I do not yet have a clean local address-for-address proof that `$9891/$9897/$9A0B` map exactly onto those names.

But the local builder behavior now makes that family much more plausible than it was before: we clearly have an active-entry controller, a small count, a rebuild pass, per-entry payload words, per-entry mapped bytes, later live-position refresh, draw-coordinate conversion, a display enqueue path, and per-channel overlay animation scripts.

So the safest wording is:

- the reference names are strong support for the subsystem identity
- the exact one-to-one field mapping should still stay tentative until one more local consumer family is decoded

## What `C0:37D0` contributes

The `C0:37D0` region is where the local picture becomes visibly controller-like.

This path handles the special count-`1` case differently from the multi-entry case, seeds `$9A0B` for a new or appended entry, pulls a pair of words from the `$5156` family, indexes `DATA_C3E012`, writes position-like offsets to `$0B16/$0B52`, updates `$9889`, and then runs the same `C0:32EC -> C0:34D6` refresh chain.

So the best current read is that `C0:37D0` is not a trivial append helper. It is the bridge from new active mushroomized entry exists into rebuild the controller outputs and downstream live state.

## Current safest interpretation

The safest interpretation now is:

- the mushroomized-walking subsystem is a six-entry active controller
- `$986F` supplies the source entry codes
- `$988B` keeps those active codes in a sorted controller order
- `$98A3` is the active-entry count
- `$9891`, `$9897`, and `$9A0B` carry the per-entry selector / payload state needed by downstream movement or overlay logic
- the family maintains live anchor and draw-position tables at `$0B8E/$0BCA` and `$0B16/$0B52`
- the draw positions and animated visual payloads are then enqueued through `C0:8C58` into the broader display pipeline
- the broader overlay family includes ripple, big ripple, sweating, and mushroomized channels
- the mushroomized channel is one branch within that shared overlay system

## Caution

Two cautions still matter.

- I have not yet pinned the exact semantic meanings of the gate words `$2A7E`, `$2BAA`, and `$2E7A`.
- `$98A4` is still best left as a selected or boundary index, not a final symbolic name.

## Best next target

The best next move is to tighten `$2A7E`, `$2BAA`, and `$2E7A`, because the overlay families are now identified and the remaining ambiguity is mostly in the state words that turn those channels on.
