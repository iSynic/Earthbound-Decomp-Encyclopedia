# Mushroomized Overlay Redirect C08C58

This note captures the local role of `C0:8C58` in the mushroomized-walking controller path.

See also [mushroomized-overlay-animation-scripts.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/mushroomized-overlay-animation-scripts.md).
See also [mushroomized-walking-builders-34de-37d0.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/mushroomized-walking-builders-34de-37d0.md).

## Main result

`C0:8C58` is not mushroom-specific.

It is a small generic redirector that appends a four-word draw record into one of four display buckets selected by `$2400`.

That matters because the mushroomized controller feeds its derived draw coordinates into this routine, which is strong evidence that the controller has a real visual overlay or presentation side, not just hidden movement state.

## Local body shape

The body at `C0:8C58` is very small:

- `PHX`
- `PHA`
- load bucket selector from `$2400`
- indirect through a four-entry jump table

The four targets are:

- `C0:8C6D`
- `C0:8C87`
- `C0:8CA1`
- `C0:8CBB`

Each target does the same shape against a different base/index pair:

- read current tail index from `$2504`, `$2606`, `$2708`, or `$280A`
- store one word to the first array in that bucket
- `PLA` and store one word to the second array
- store `Y` to the third array
- store `$000B` to the fourth array
- increment the tail index by 2

So `C0:8C58` is best described as a four-bucket draw-record enqueue helper.

## Call convention

The stack behavior makes the call convention much clearer than it first looks.

At entry:

- current `A` is pushed
- current `X` is pushed
- the bucket is selected
- the first target stores the saved `A`
- then `PLA` pulls the saved `X` and stores it
- `Y` is stored directly
- `$000B` is stored as the fourth field

So each enqueued record is effectively:

- field 0 = caller `A`
- field 1 = caller `X`
- field 2 = caller `Y`
- field 3 = caller `$000B`

The exact semantic names of those four fields are not fully pinned yet, but in the mushroomized call sites they read naturally as:

- visual payload or frame-like value in `A`
- draw X in `X`
- draw Y in `Y`
- companion attribute or selector in `$000B`

## Why this matters for the mushroomized path

The mushroomized controller feeds this helper from several `C0:ACxx` paths after first deriving draw coordinates from `$0B16/$0B52`.

The important local pattern is:

- take per-entry draw X from `$0B16`
- take per-entry draw Y from `$0B52`
- load a per-entry visual value from one of the current-payload slots driven by `C0:AD56`
- optionally add a small offset
- call `C0:8C58`

The paired note [mushroomized-overlay-animation-scripts.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/mushroomized-overlay-animation-scripts.md) now shows that those current-payload values come from small looping bank-`C4` animation scripts.

That is strong local evidence that the mushroomized controller is contributing visual draw records, not merely remapping movement decisions.

## Safest current interpretation

The safest interpretation is:

- `C0:8C58` is a generic draw-record redirector / enqueue helper
- the mushroomized controller computes per-entry draw coordinates and per-entry animated visual payloads
- those values are then enqueued through `C0:8C58` into the broader display pipeline

So the most likely next naming direction for `$9891/$9897/$9A0B` is overlay or presentation oriented, not purely movement oriented.

## Best next target

The best next move is to tighten the gating words `$2A7E` and `$2E7A`, because those should expose when the four mushroomized overlay channels are active and whether they correspond to distinct visible pieces of the effect.
