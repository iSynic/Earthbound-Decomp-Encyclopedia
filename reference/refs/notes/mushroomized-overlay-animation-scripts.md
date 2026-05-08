# Mushroomized Overlay Animation Scripts

This note captures the local role of `C0:AD56` and the bank-`C4` script tables used by the overlay callers.

See also [mushroomized-overlay-gate-words.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/mushroomized-overlay-gate-words.md).
See also [mushroomized-overlay-redirect-c08c58.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/mushroomized-overlay-redirect-c08c58.md).
See also [mushroomized-walking-builders-34de-37d0.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/mushroomized-walking-builders-34de-37d0.md).

## Main result

`C0:AD56` is a tiny animation-script interpreter for the entity-overlay records.

The four per-entity script-pointer/timer pairs in bank `00` are:

- `$301E/$305A`
- `$30D2/$310E`
- `$2F6A/$2FA6`
- `$2EB6/$2EF2`

Those pointers are seeded from bank-`C4` tables:

- `C4:0EF0`
- `C4:0F04`
- `C4:0EB0`
- `C4:0EE4`

The useful new result is that these four scripts line up exactly with the `ebsrc` entity-overlay families:

- `C4:0EB0` = `ENTITY_OVERLAY_SWEATING`
- `C4:0EE4` = `ENTITY_OVERLAY_MUSHROOMIZED`
- `C4:0EF0` = `ENTITY_OVERLAY_RIPPLE`
- `C4:0F04` = `ENTITY_OVERLAY_BIG_RIPPLE`

So the mushroomized controller notes were slightly too narrow: this local display path is really feeding the broader entity-overlay system, and the mushroomized overlay is one of the four channels in that shared family.

## `C0:AD56` script format

The local interpreter shape is simple and useful.

Input:

- `A` = base address of the per-entity current-payload slot
- `$02/$03` = current script pointer
- `X` is derived from the entity index in `$88`

The script opcodes decode as:

- `0x0001, value`
  - store `value` into the per-entity current-payload slot
  - continue scanning the script
- `0x0002, delay`
  - return with `Y = delay`
  - return with `A = next script pointer`
- `0x0003, target`
  - set the current script pointer base to `target`
  - restart scanning from that address

That makes the timer side in the callers much clearer:

- if the timer is zero, call `C0:AD56`
- store returned script pointer back into the per-entity pointer slot
- store returned delay into the paired timer slot
- decrement the timer each update
- use the current payload word for the draw record

## Top-level animation tables

The four bank-`C4` top-level tables have clean loop shapes.

### `C4:0EB0` = sweating

This cycles through the payload words:

- `0E42` for 8 ticks
- `0E4C` for 8 ticks
- `0000` for 16 ticks
- `0E56` for 8 ticks
- `0E60` for 8 ticks
- `0000` for 16 ticks
- then loops back to `0EB0`

This matches `ebsrc`'s `ENTITY_OVERLAY_SWEATING` exactly.

### `C4:0EE4` = mushroomized

This is a very small loop:

- `0E6A` for 255 ticks
- then loop back to `0EE4`

This matches `ENTITY_OVERLAY_MUSHROOMIZED` exactly.

### `C4:0EF0` = small ripple

This loops between two payloads:

- `0E74` for 12 ticks
- `0E7E` for 12 ticks
- then loop back to `0EF0`

This matches `ENTITY_OVERLAY_RIPPLE` exactly.

### `C4:0F04` = big ripple

This also loops between two payloads:

- `0E88` for 12 ticks
- `0E9C` for 12 ticks
- then loop back to `0F04`

This matches `ENTITY_OVERLAY_BIG_RIPPLE` exactly.

## What the payload words are

The payload words written by the scripts are addresses in the small `C4:0E42..0EAE` block.

Examples:

- `0E42`, `0E4C`, `0E56`, `0E60`
- `0E6A`, `0E74`, `0E7E`
- `0E88`, `0E9C`

The `ebsrc` cross-check makes these much less mysterious. They are overlay frame records with this shape:

- relative Y byte
- tile/attribute word
- relative X byte
- attribute byte

So the current payload word in the local bank-`00` channels is a pointer to an overlay frame descriptor, not just a raw tile id.

## How this fits the callers

The caller family now reads coherently.

- `C0:AC89` uses `$301E/$305A/$3096` and therefore drives the small-ripple channel.
- `C0:ACBA` uses `$30D2/$310E/$314A` and therefore drives the big-ripple channel.
- `C0:ACFF` uses `$2F6A/$2FA6/$2FE2` and therefore drives the sweating channel.
- `C0:AD3F` uses `$2EB6/$2EF2/$2F2E` and therefore drives the mushroomized channel.

The paired gate note [mushroomized-overlay-gate-words.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/mushroomized-overlay-gate-words.md) now narrows the conditions that enable those channels.

So the broader local path is better described as an entity-overlay update/display family, with mushroomized handling as one branch inside it.

## Local gating picture from `C0:AC59+`

The gate logic is now useful enough to summarize.

First branch family:

- if `$2BAA & #$000C == 0`, no ripple-style overlay is emitted
- if `$2BAA & #$000C == #$0004`, the code skips the ripple pair and jumps straight to the sweating/mushroomized pair
- otherwise it chooses between:
  - small ripple when `$2A7E == #$0040`
  - big ripple for the other non-`#0004` nonzero cases in that branch

Second branch family:

- if `$2E7A == 0`, neither sweating nor mushroomized is emitted
- if `$2E7A` has bit `15` set, the sweating channel is active, but only for entities `>= $002E`
- if `$2E7A & #$4000` is set, the mushroomized channel is active, also only for entities `>= $002E`

I am still keeping the semantic names of `$2A7E`, `$2BAA`, and `$2E7A` cautious, but the overlay-channel selection itself is now much less ambiguous.

## Safest current interpretation

The safest interpretation is:

- the local bank-`00` code is driving the shared entity-overlay system
- the four active overlay channels here are ripple, big ripple, sweating, and mushroomized
- the mushroomized controller work we traced earlier is plugged into that same overlay/display machinery
- the mushroomized-specific overlay channel is the `2EB6/2EF2/2F2E -> C4:0EE4` family

This pushes the subsystem even closer to the reference-family names around overlay pointers / update frames / spritemaps.

## Best next target

The best next move is to tighten the overlay-initialization descriptor that writes `$2A7E/$2ABA/$2A42`, because the overlay families and their gate bits are now identified and the remaining ambiguity is mostly in the structured source data.
