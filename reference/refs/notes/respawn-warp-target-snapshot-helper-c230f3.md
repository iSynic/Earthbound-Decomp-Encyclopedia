# Respawn / Warp Target Snapshot Helper `C2:30F3`

This note captures the current best local model for the small bank-`C2` helper reached by text command `0x19 26`.

See also [text-command-family-19-data-and-substitution.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-family-19-data-and-substitution.md).
See also [saved-coordinate-reload-path-c4c718-c0b967.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/saved-coordinate-reload-path-c4c718-c0b967.md).
See also [transition-landing-mode-family-9f3f-9f41.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/transition-landing-mode-family-9f3f-9f41.md).

## Main result

`C2:30F3` is not a full respawn routine by itself.

The helper is much smaller and cleaner than the inherited community wording suggests. It simply snapshots:

- one staged byte into `$98B8`
- current X-like coordinate `$9877 -> $9D1F`
- current Y-like coordinate `$987B -> $9D21`

So the safest current local read is now:

- `0x19 26` calls a small transition-landing snapshot helper
- that helper records the current live coordinates and one companion selector byte
- later code interprets that saved state as part of a broader respawn / warp / landing pipeline

## Local helper body

`0x19 26` reaches `C1:7037`, and `C1:7037` does little more than resolve one byte argument and pass it to `C2:30F3`.

`C2:30F3` itself is only:

- `STA $98B8` (8-bit store)
- `LDA $9877 ; STA $9D1F`
- `LDA $987B ; STA $9D21`
- `RTL`

So the helper has exactly three observable side effects.

## What the written state looks like

### `$9D1F / $9D21`

These two words are best read as a saved current-coordinate pair.

Evidence:

- `C2:30F3` copies them directly from the live position words `$9877 / $987B`
- sibling code at `C1:2FB2` and `C1:F847` also copies `$9877 / $987B -> $9D1F / $9D21`
- `C4:C718` later reads `$9D1F / $9D21` together and immediately feeds them into a larger world-side routine through `C0:943C`

So the strongest current read is that `$9D1F / $9D21` are generic saved world coordinates, reused by multiple transition-style flows.

### `$98B8`

`$98B8` is a one-byte companion selector, not part of the coordinate pair itself.

The strongest new local bridge is:

- `C2:ABFB` reads `$98B8`
- then `JSL`s `C0:DD53`
- `C0:DD53` stages low byte `A -> $9F3F`
- and stages caller direct-page byte `$1D -> $9F41`

That means the saved byte is no longer just vaguely transition-adjacent. It is the direct source of the later staged destination selector `$9F3F`; see [transition-landing-mode-family-9f3f-9f41.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/transition-landing-mode-family-9f3f-9f41.md).

So the safest current read is now:

- `$98B8` = saved one-byte landing-destination selector
- later paired with a caller-side landing mode into `$9F3F / $9F41`

## Why the community label is only partly local-proofed

The community docs say `0x19 26`:

- sets the respawn coordinates to the current player position
- and sets the destination of the unused Teleport Box battle action

The local ROM now supports the first half strongly, and it supports the second half more narrowly than before but still not as a direct label on `C2:30F3` itself.

What is locally strong:

- the helper really does snapshot the current coordinate pair
- it really does save one companion byte alongside that snapshot
- that companion byte is later staged into `$9F3F`, which behaves like a destination selector in the landing controller family

What is still only higher-level or reference-backed:

- the exact semantic name of `$98B8`
- whether the saved byte is best called respawn destination id, warp id, or more specifically a teleport-destination-style id
- the exact gameplay system that owns each landing mode around `$9F41`

So the safest current wording is:

- `0x19 26` locally performs a transition landing-target snapshot
- the broader "set respawn point" wording is still plausible at system level
- but `C2:30F3` itself should not be described as the whole respawn routine

## Confidence boundaries

### Locally proved

- `0x19 26 -> C1:7037 -> C2:30F3`
- `C2:30F3` writes `$98B8`, `$9D1F`, and `$9D21`
- `$9D1F / $9D21` are copied directly from `$9877 / $987B`
- sibling code also reuses the same coordinate snapshot pair
- `C4:C718` consumes `$9D1F / $9D21` together as saved world coordinates; see [saved-coordinate-reload-path-c4c718-c0b967.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/saved-coordinate-reload-path-c4c718-c0b967.md)
- `C2:ABFB -> C0:DD53` later stages `$98B8` into `$9F3F`

### Reference-backed and locally consistent

- the higher-level interpretation that this snapshot is used as a respawn or warp landing target
- the possibility that `$98B8` is the destination id for a teleport-style landing flow

### Still open

- the exact combined consumer that interprets `$98B8` together with the saved coordinates
- the exact final semantic label for `$98B8`
- whether there are multiple gameplay systems sharing the same saved coordinate pair

## Best next target

The cleanest next move is to stay on the staged landing family:

- `$98B8 -> C2:ABFB -> C0:DD53 -> $9F3F / $9F41`
- then the success-side branch `C0:EB7B -> C0:DD79 -> C0:E897`

That should decide how narrow or broad the final system name should be.
