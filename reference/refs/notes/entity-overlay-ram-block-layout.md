# Entity Overlay RAM Block Layout

This note captures the current best structural read for the contiguous `0x3C`-stride visual-state block around `2A06..2CD6`.

See also [sprite-pose-descriptor-cache-2a06-2cd6.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/sprite-pose-descriptor-cache-2a06-2cd6.md).
See also [overlay-init-descriptor-fields.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/overlay-init-descriptor-fields.md).
See also [mushroomized-overlay-animation-scripts.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/mushroomized-overlay-animation-scripts.md).

## Main result

One part of the earlier observation still holds, and one part needs correction.

The part that still holds:

- the addresses `2A06, 2A42, 2A7E, 2ABA, 2AF6, 2B32, 2B6E, 2BAA, 2BE6, 2C22, 2C5E, 2C9A, 2CD6` are spaced exactly `0x3C` bytes apart
- that is exactly one `MAX_ENTITIES * 2` word-array stride
- so this is still very likely a real shared per-entity visual-state block

The part that now needs correction:

- the old one-to-one crosswalk to `ebsrc`'s `ENTITY_*_OVERLAY_*` arrays is too aggressive to keep as-is

Local writes now show that `2A06`, `29CA`, `2A42`, `2A7E`, `2ABA`, and `2CD6` are populated from a sprite-pose descriptor cache path, not from a tiny overlay-only record.

## Exact spacing check

Each adjacent pair differs by `0x3C`:

- `2A06 -> 2A42`
- `2A42 -> 2A7E`
- `2A7E -> 2ABA`
- `2ABA -> 2AF6`
- `2AF6 -> 2B32`
- `2B32 -> 2B6E`
- `2B6E -> 2BAA`
- `2BAA -> 2BE6`
- `2BE6 -> 2C22`
- `2C22 -> 2C5E`
- `2C5E -> 2C9A`
- `2C9A -> 2CD6`

That structural observation still looks solid.

## What local writes now prove

The write block documented in [sprite-pose-descriptor-cache-2a06-2cd6.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/sprite-pose-descriptor-cache-2a06-2cd6.md) shows that at least the leading arrays in this block are seeded from sprite-pose descriptor data:

- `2ABA` gets pose descriptor byte `+0`
- `2A7E` gets pose descriptor byte `+1`, shifted left once
- `2A42` gets pose descriptor byte `+8`
- `2CD6` gets the selected pose-table index `$2B`
- `2A06/29CA` get the cached pointer to the pose descriptor's frame-word list

That means `2A06` is not behaving like a simple overlay-flags word, and `2CD6` is not behaving like a simple overlay-spritemap word.

So the old exact field-name crosswalk should be treated as superseded.

## Safest current interpretation

The safest current statement is:

- `2A06..2CD6` is a real shared per-entity visual-state block
- the leading portion of that block clearly caches sprite-pose descriptor data
- later consumers in the same neighborhood still feed the sweating, mushroomized, ripple, and big-ripple overlay channels
- so the overlay system appears to consume a broader visual/pose cache rather than owning that entire cache outright

That is a cleaner model than the earlier direct overlay-array mapping.

## What remains plausible from the older overlay reading

Some of the older overlay-side observations are still useful.

- the four overlay channels are locally identified
- `2E7A` still behaves like the enable word for the sweating and mushroomized channels
- `2BAA` still behaves like a draw-options word in the ripple branch

So the overlay work was not wasted. The adjustment is that those overlay branches now look like consumers of a wider visual-state/cache block.

## What is now retracted

The exact tentative map from the earlier note should not be treated as current:

- `2A06 = ENTITY_OVERLAY_FLAGS`
- `2A42 = ENTITY_MUSHROOMIZED_OVERLAY_PTRS`
- `2A7E = ENTITY_MUSHROOMIZED_NEXT_UPDATE_FRAMES`
- `2ABA = ENTITY_MUSHROOMIZED_SPRITEMAPS`
- and the rest of that straight-line overlay-array mapping

The block-level spacing observation still stands, but those exact names are no longer the safest local interpretation.

## Best next target

The best next move is to finish mapping pose descriptor bytes `+2..+7` and the neighboring cached arrays they seed. That should tell us where the generic pose cache ends and where the overlay-specific state begins.
