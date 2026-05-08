# Saved Coordinate Reload Path `C4:C718` / `C0:B967`

This note captures the current best local model for the first strong downstream consumer of the saved snapshot triplet:

- `$98B8`
- `$9D1F`
- `$9D21`

See also [respawn-warp-target-snapshot-helper-c230f3.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/respawn-warp-target-snapshot-helper-c230f3.md).
See also [transition-landing-mode-family-9f3f-9f41.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/transition-landing-mode-family-9f3f-9f41.md).

## Main result

`C4:C718` is the first good local place where the saved coordinate pair stops looking like passive state and starts looking like a real reload target.

The strongest current boundary is:

- `C2:30F3` = tiny snapshot helper
- `C4:C718` = saved-coordinate reload / landing initializer
- `C0:943C` = lower-level generic world-object mark/setup helper reused by many callers
- `C0:DD53 / C0:EA99` = the companion staged destination / landing-mode family built around `$98B8`

So the safest current system-level read is no longer just "maybe respawn." We now have a real downstream reload path that consumes the saved coordinates as a landing position for a broader world re-entry / transition sequence.

## Local consumer proof

`$9D1F / $9D21` have only one direct paired reader:

- `C4:C718`

That routine immediately:

- loads `$9D1F -> $02`
- loads `$9D21 -> $16`
- calls `C0:943C`
- then performs a larger reset / world-side setup chain

So `C4:C718` is the first strong local proof that the saved pair is not just text-engine scratch. It is meant to be turned back into active world placement state.

## Why `C0:943C` is not the specific answer by itself

`C0:943C` turned out to be broader than this subsystem.

It is called from many unrelated places across banks `00`, `01`, `02`, `03`, `04`, and `EF`, and its body just marks or prepares a linked world-object chain through `$0A50 / $0A9E / $10B6`.

So the safest local wording is:

- `C0:943C` is a generic lower-level world-object mark/setup helper
- `C4:C718` is the more specific saved-coordinate reload path built on top of it

That distinction matters, because it keeps us from overpromoting `C0:943C` into a fake "respawn routine" label.

## Single direct caller: `C0:B967`

The one direct caller into `C4:C718` is:

- `C0:B967`

That caller sits in a larger state-reset / transition branch:

- restore current HP/PP shadows for the six active party slots
- call `C0:4FFE`
- if that gate passes, call `C4:C718`
- if `C4:C718` returns nonzero, continue into a follow-up state path

So the current best local read is that `C4:C718` is not a free-standing menu helper or script helper. It is part of an actual world-transition path that tries to re-enter the overworld at the saved coordinate pair.

## What `C4:C718` does with the saved coordinates

After loading `$9D1F / $9D21`, `C4:C718`:

- calls `C0:943C`
- runs additional local setup helpers `C4:C2DE` and `C4:C64D`
- branches on that result
- in the heavy path, performs a larger reset / initialization sequence including:
  - object/state clears
  - coordinate-sensitive helper `C0:19B2`
  - registry/party/object-side refresh work
  - additional world-transition helpers like `C0:64D4`, `C0:6B21`, and `C0:88B1`

So the safest current system-level name is not a narrow "teleport box" helper. It is more like a saved-coordinate landing initializer inside a broader world reload path.

## Where `$98B8` fits

This part is stronger now than it was before.

The clean local bridge is:

- `C2:30F3` writes `$98B8` alongside the saved coordinates
- `C2:ABFB` later reads `$98B8`
- `C2:ABFB -> C0:DD53` stages it into `$9F3F`
- `C0:DD53` also stages caller byte `$1D -> $9F41`
- the larger controller at `C0:EA99` interprets `$9F41` as a landing-mode selector

So the safest current read is no longer just "destination / mode selector" in the abstract. It is:

- `$98B8` = saved destination-selector byte for the broader landing family
- later paired with a landing-mode byte into `$9F3F / $9F41`

What is still open is the exact gameplay naming of those modes and the exact final semantic name of `$9F3F`.

## Safest current interpretation

The safest current layered interpretation is:

- `0x19 26` does not itself perform the respawn or warp
- `C2:30F3` snapshots the current landing coordinates plus a companion selector byte
- `C0:DD53 / C0:EA99` turn that selector into a staged destination / landing-mode family
- `C4:C718`, reached from the larger transition branch at `C0:B967`, is the first strong reload-side consumer of the saved coordinates
- and that reload path is broad enough that the best current system-level wording is "saved coordinate reload / landing initializer" rather than a narrower one-off label

That still leaves the community "set respawn point" wording plausible at high level, but now the local subsystem boundaries are much cleaner.

## Confidence boundaries

### Locally proved

- `C4:C718` is the only direct paired reader of `$9D1F / $9D21`
- `C4:C718` is called directly from `C0:B967`
- `C4:C718` consumes the saved coordinates before a larger world-side reset / initialization chain
- `C0:943C` is generic lower-level world-object setup, not the whole respawn subsystem
- `C2:ABFB -> C0:DD53` stages `$98B8` into `$9F3F / $9F41`

### Reference-backed and locally consistent

- the idea that this broader family participates in post-death respawn or scripted warp landing
- the idea that `$9F3F` is a teleport-destination-style index inside the same family

### Still open

- the exact final name of `$9F3F`
- the exact gameplay names of landing modes `1..5`
- whether the best final system name is closer to respawn target, warp target, or transition checkpoint

## Best next target

The cleanest next move is to stay on the success-side branch of the staged landing family:

- `C0:EB7B -> C0:DD79 -> C0:E897`

That is now the shortest path to deciding how much of this family is specifically named-destination arrival versus general landing finalization.
