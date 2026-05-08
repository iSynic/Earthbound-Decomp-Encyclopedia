# Mushroomized Overlay Gate Words

This note captures the current best local model for the gate/state words around `2A7E`, `2ABA`, `2BAA`, and `2E7A`.

See also [sprite-pose-descriptor-cache-2a06-2cd6.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/sprite-pose-descriptor-cache-2a06-2cd6.md).
See also [overlay-init-descriptor-fields.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/overlay-init-descriptor-fields.md).
See also [mushroomized-overlay-animation-scripts.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/mushroomized-overlay-animation-scripts.md).

## Main result

The useful correction here is that `2A7E` and `2ABA` are now better understood as pose-descriptor cache fields, while `2BAA` and `2E7A` still read best as local gate/state words in the overlay consumers.

The strongest current local read is:

- `2A7E` = pose descriptor byte `+1`, shifted left once, used as the frame-record stride
- `2ABA` = pose descriptor byte `+0`, used as a piece count
- `2BAA` = ripple-branch draw-options word in the local readers
- `2E7A` = late-channel enable word for sweating and mushroomized

So the earlier wording that treated `2A7E` as a pure ripple subtype selector was too narrow.

## `2A7E` is structurally a stride field

The clearest local role is still in the draw helpers:

- `C0:A4C4+` and `C0:A794+` load `2A7E` into the per-piece step register
- after each emitted piece, the code advances the frame-data pointer by that amount

The write path now ties that directly to pose descriptor byte `+1`, shifted left once before storage.

So the safest current statement is:

- `2A7E` is a structural frame-record stride field

The ripple branch still compares it against `#$0040`, but that now looks like a specific descriptor value being tested, not the whole semantic meaning of the field.

## `2ABA` now looks clearly count-like

At `C0:A4C4+` and `C0:A794+`:

- `LDA $2ABA,Y`
- `STA $00`
- the helper decrements `$00` after each draw piece
- the loop stops when it reaches zero

The write path now ties that back to pose descriptor byte `+0` explicitly.

So the safest current read is:

- `2ABA` is a piece-count field cached from the pose descriptor

## `2BAA` still reads like a ripple draw-options word

The local readers still make this useful.

At `C0:AC59+`:

- `LDA $2BAA,X`
- `AND #$000C`
- zero skips the ripple-style branch entirely
- `#$0004` skips straight to the sweating/mushroomized pair
- the remaining case enters the ripple pair

At `C0:A3B4+`, `C0:A4C4+`, and `C0:A794+`:

- lower bits affect sprite-attribute handling
- bits `2/3` control extra draw passes

So the safest current statement is still:

- `2BAA` is a compact local draw-options word for this visual branch family

## `2E7A` still reads like the sweating/mushroomized enable field

The setup and display readers still line up well.

- the builder clears `2E7A[slot]`
- later descriptor conditions OR in `#$8000` and `#$4000`
- the display side uses bit `15` for the sweating channel and bit `14` for the mushroomized channel

So the safest current read is still:

- `2E7A` is a compact enable field for the sweating and mushroomized overlay channels

## Safest synthesis

The safest synthesis now is:

- `2A7E` and `2ABA` are generic pose-descriptor cache fields
- `2BAA` and `2E7A` are overlay-consumer gate/state words layered on top of that broader cache

That is a better fit than treating all four words as one flat overlay-only descriptor.

## Best next target

The best next move is to map pose descriptor bytes `+2..+7` and the neighboring cached arrays they seed. That should expose how the generic pose cache hands off into the ripple, sweating, and mushroomized overlay branches.
