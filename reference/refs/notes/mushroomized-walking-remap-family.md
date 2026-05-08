# Mushroomized Walking Remap Family

This note captures the current ROM-first model for the overworld mushroomized-walking data family around `$986F`, `$988B`, `$9891`, `$9897`, `$9A0B`, `$98A3`, and `$98A4`.

See also [mushroomized-walking-builders-34de-37d0.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/mushroomized-walking-builders-34de-37d0.md).
See also [class2-cc19-20-eshop2-single-use.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-cc19-20-eshop2-single-use.md).
See also [class2-c1-display-text-substitution-handler-7af3.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-c1-display-text-substitution-handler-7af3.md).
See also [party-overlay-arbitration-c216db-c3ebca.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/party-overlay-arbitration-c216db-c3ebca.md).

## Main result

The strongest current read is that the mushroomized-walking subsystem is not just one remap byte and one flag.

It now looks much more like a six-entry controller family with a real downstream overlay or presentation side:

- `$986F` supplies the source entry codes
- `$988B` keeps the active codes in an ordered list
- `$98A3` is the active-entry count
- `$98A4` is the active party-member count, which also acts as the boundary after the leading `1..4` party codes
- `$9891`, `$9897`, and `$9A0B` carry per-entry selector / payload state for downstream movement or overlay logic
- `$0B8E/$0BCA` and `$0B16/$0B52` hold per-entry anchor and draw-coordinate state

That is materially stronger than the earlier generic "mushroomized state byte" wording.

## Why `$98A4` still mechanically looks index-like

The clearest writer is still the bank-`00` path around `C0:32F0..3318`.

That code:

- initializes `Y = 0`
- scans the six-entry byte family at `$986F + Y`
- continues while the current entry is in the small nonzero range below `5`
- stops on the first `0` or `>= 5` entry
- then does `TYA` and stores that byte into `$98A4`

So `$98A4` is very unlikely to be an arbitrary mode flag. It is much more naturally explained as the resulting scan index or boundary. A later bulk writer at `C2:4C80..4CD2` also stores the number of party codes written directly into `$98A4`, which is why the stronger mainline read is now "active party-member count" rather than only "scan boundary."

## Why `$98A3` now looks firmly count-like

The builder paths make the count role much stronger than before.

- `C0:34D6` copies `$98A3` into a loop bound while rebuilding the exported entry rows.
- `C0:369B` increments `$98A3` each time a new active mushroomized entry is inserted.
- `C0:37D0` special-cases the `count == 1` case.
- `C0:3A24` clears `$98A3` before rebuilding the whole family from `$986F`.

So `$98A3` is now best treated as the active-entry count, not just a vague companion control byte.

## Stronger local role for `$988B`

A later pass tightened the output side of the family.

`C0:369B` inserts one source byte from `$986F` into the ordered list at `$988B`, shifting the existing rows downward first. `C0:34D6` then uses `$988B` as the basis for its sort key and exports the sorted result to later buffers.

So `$988B` now looks like an ordered active-entry code list, not a generic scratch array.

## Why `$988B` is now better read as a derived layer

The registry-reconcile pass tightened the source/output split enough to name it more directly.

- `C2:28F8` inserts into `$986F` and then calls `C0:369B` to mirror the same code into `$988B`
- `C2:29BB` removes from `$986F` and then runs the matching derived-layer removal path
- `C0:3A24` clears `$988B` and rebuilds the derived layer from `$986F` during full reset

So the safest current read is that `$986F` is the authoritative source array while `$988B` is the ordered runtime lookup layer built from it. That makes the older mushroomized-only wording too narrow for `$986F` itself, while keeping the higher-level mushroomized controller story intact.

## Stronger local role for `$9891`, `$9897`, and `$9A0B`

The exact field names are not final yet, but the family shape is much clearer.

- `$9891 + slot` is a mapped selector byte used with the `#$005F` helper.
- `$9897 + 2*slot` is a per-entry word payload reused across insert, sort, export, and later per-entry refresh.
- `$9A0B[mapped selector]` is a per-selector byte payload that gets seeded, carried forward, and written back during the builder passes.

That makes these three addresses look like one coordinated payload family rather than unrelated remap scratch.

## Why this now looks richer than a simple direction swap

The builder and refresh paths do more than swap one input for another.

The local bank-`00` family:

- rebuilds all active entries from `$986F`
- keeps them in a sorted controller order
- exports byte and word side buffers into `7E:97F5+...`
- maintains anchor and draw-position tables at `$0B8E/$0BCA` and `$0B16/$0B52`
- refreshes per-entry state from live player position via `$9877/$987B`
- feeds those derived draw coordinates into later sprite / overlay placement code

So the safest current read is that this is a small mushroomized movement controller with companion presentation state, not a trivial direct-remap table.

## Why the reference names are now more plausible

The quarantined `ebsrc` tree exports these globals in the same neighborhood:

- `ENTITY_MUSHROOMIZED_OVERLAY_PTRS`
- `ENTITY_MUSHROOMIZED_NEXT_UPDATE_FRAMES`
- `ENTITY_MUSHROOMIZED_SPRITEMAPS`
- `MUSHROOMIZATION_TIMER`
- `MUSHROOMIZATION_MODIFIER`
- `MUSHROOMIZED_WALKING_FLAG`

I do not yet have a clean local one-to-one proof for every address, so those names should stay reference-backed rather than fully promoted.

But the local controller shape now makes them much more plausible than before.

## Why this still helps the clinic script

The lone exposed text use of `0x19 0x20` is still `C9:1A91` in `MSG_SUB_GRFD_KINOKOGIRL`, and that text command still loads `$98A4` through `C1:7B0D`.

That fit is better now than it was earlier:

- the clinic script is probably not reading a generic flag
- it is much more likely exposing the current party-count / boundary byte from the broader controller family
- and it preserves/restores that byte while it scans party members for the mushroomized ailment

So the clinic path now fits naturally with the stronger controller model.

## Current safest interpretation

The safest interpretation is:

- `$986F` is a six-entry source-code array for the broader active overworld entity-type family, not a mushroomized-only array
- `$988B` is the derived ordered active-entry code list rebuilt from that source
- `$98A3` is the active-entry count in the derived layer
- `$98A4` is the active party-member count, and mechanically also the boundary after the leading `1..4` party codes
- `$9891`, `$9897`, and `$9A0B` are the coordinated per-entry selector / payload state used by later movement or overlay code
- the mushroomized overlay/controller subsystem is built on top of this family, but the family itself is broader than mushroomized walking alone

## Caution

Two cautions still matter.

- The exact player-facing meaning of the per-entry payload trio is not fully pinned yet. They still might be best described as overlay pointers, next-update frames, spritemap selectors, or a nearby equivalent.
- The arbitration side is now better understood than before: [party-overlay-arbitration-c216db-c3ebca.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/party-overlay-arbitration-c216db-c3ebca.md) is the strongest current local fit for `C2:16DB` / `C3:EBCA`. But the specific identity of the overlay entity types `0x10/0x11` is still a little softer than the arbitration role itself, so the overlay-level "mushroomized" name should stay attached to the upper entity interpretation rather than forced onto every helper in the family.

## Best next target

The best next move is now narrower: decode `C4:8F98` or tighten the overlay entity class behind `0x10/0x11`, because the main remaining question is no longer whether `C2:16DB` is broader. The remaining question is whether the overlay entities it arbitrates are exclusively mushroomized or part of a slightly broader walking-overlay class.
