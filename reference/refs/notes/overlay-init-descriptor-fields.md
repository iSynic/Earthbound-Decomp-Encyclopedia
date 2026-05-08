# Overlay Init Descriptor Fields

This note captures the current best local field map for the visual-state write path that seeds `2A06`, `2A42`, `2A7E`, `2ABA`, `29CA`, and `2CD6`.

See also [sprite-pose-descriptor-cache-2a06-2cd6.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/sprite-pose-descriptor-cache-2a06-2cd6.md).
See also [mushroomized-overlay-gate-words.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/mushroomized-overlay-gate-words.md).
See also [mushroomized-overlay-animation-scripts.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/mushroomized-overlay-animation-scripts.md).

## Main correction

A useful correction finally landed.

The fields `2A06`, `29CA`, `2A42`, `2A7E`, `2ABA`, and `2CD6` are not best explained as a tiny overlay-only descriptor cache. The local write path shows that they are populated from a richer sprite-pose descriptor family.

Two sources are involved:

- a pose descriptor at `[$23:$25]`
- the long-pointer table at `EF:133F`, indexed by `$2B`

The strongest current local read is:

- `2ABA` = pose descriptor byte `+0`, used as a per-frame piece count
- `2A7E` = pose descriptor byte `+1`, shifted left once, used as the frame-record stride
- `2A42` = pose descriptor byte `+8`, used as the bank byte for the actual frame-record data
- `2CD6` = the selected pose-table index (`$2B`)
- `2A06` = bank byte of the selected pose descriptor record
- `29CA` = low-word pointer to the descriptor's frame-word list at offset `+9`

## Why `2A42` still reads as frame-data bank

At `C0:A4C4+` and `C0:A794+`:

- the code loads a word from the cached list pointed to by `2A06/29CA`
- then copies `2A42` into the far-pointer bank byte
- then calls the draw helper `C0:A56E`

That still makes `2A42` the bank byte for the final frame-record data being rendered.

The new piece is simply that this bank byte comes from pose descriptor offset `+8` explicitly.

## Why `2ABA` now looks like a real count field

At `C0:A4C4+` and `C0:A794+`:

- `LDA $2ABA,Y`
- `STA $00`
- after each draw helper call, `DEC $00`
- the loop stops when the counter reaches zero

The local write path now ties that back to pose descriptor byte `+0`, which makes the count-like role much firmer.

## Why `2A7E` now reads as a structural stride field

At `C0:A4C4+` and `C0:A794+`:

- `LDA $2A7E,Y`
- `STA $0092`
- the code advances the frame-data pointer by `$0092` after each emitted piece

The write path reads pose descriptor byte `+1`, zero-extends it, shifts it left once, and stores it to `2A7E`.

So the safest current read is:

- `2A7E` is the per-piece frame-record stride, encoded in the pose descriptor as a smaller byte-sized value

That is more fundamental than the earlier ripple-specific wording.

## Why `2A06` and `29CA` now have a cleaner explanation

The write path uses `$2B` to index the long-pointer table at `EF:133F`, then:

- stores the selected index to `2CD6`
- stores the descriptor bank byte to `2A06`
- stores the descriptor low word plus `9` to `29CA`

The `+9` bias now makes sense: sampled pose descriptors have an 8-byte header plus a bank byte before the directional frame-word list begins.

So the safest current statement is:

- `2A06/29CA` cache the pose descriptor's frame-word list pointer, not a generic overlay script pointer

## Correction to earlier wording

Two earlier phrases should be treated as superseded.

- `2CD6` is better read as a sprite-pose table index than a generic overlay-family index.
- `2A06` is better read as the pose descriptor bank byte than as the bank byte of the final frame data.

The draw-side observations still stand, but the source-layer interpretation is now cleaner.

## What still remains open

A few descriptor bytes still need names.

- bytes `+2..+7` of the pose descriptor are not fully pinned yet
- neighboring arrays like `2B6E`, `3366`, `33A2`, `33DE`, and `1A4A` clearly receive more of this cached header/state
- the later overlay animation channels still need to be described as consumers of this broader pose cache, not as the whole cache itself

## Best next target

The best next move is to tighten pose descriptor bytes `+2..+7` and the neighboring cached arrays they seed. That should let us connect the generic pose-descriptor cache to the overlay-specific branches without blurring those two layers together.
