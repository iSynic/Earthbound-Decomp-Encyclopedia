# Class2 Reflected Hit Context Rebuild

This note captures the current best local interpretation of `C2:3BCF`, `C2:3D05`, and their caller `C2:7E8A`.

See also `notes/class2-psi-thunder-reflection-branch.md`.
See also `notes/class2-reflected-hit-text-context.md`.
See also `notes/class2-reflected-hit-side-buffer-flags.md`.
See also `notes/class2-psi-shield-post-hit-aa96.md`.

## Current strongest claim

`C2:7E8A` now looks like a reflected-hit context swap helper, and `C2:3BCF` plus `C2:3D05` look like the paired context-rebuild helpers it uses to refresh battle-side working state after the swap.

The safest current description is not "damage logic" or "text logic." These routines look more like attacker-side and target-side battle-context builders that reconstruct working buffers from the swapped selected rows.

## `C2:7E8A` really does look like a swap-and-rebuild helper

The local body of `C2:7E8A` is simple and useful:

- save `$A970`
- copy `$A972` into `$A970`
- restore the saved value into `$A972`
- call `C2:3BCF`
- call `C2:3D05`
- return

That is too direct to be much else. It swaps the two selected-row anchors, then rebuilds the dependent working state.

This fits the reflected-hit model very well: once PSI is reflected, the acting and receiving sides need to trade places for the rest of the hit-resolution machinery.

## `C2:3BCF` and `C2:3D05` are a matched pair

The two routines are structurally very similar.

Shared local traits:

- both clear a one-byte WRAM flag at entry:
  - `C2:3BCF` clears `$5E77`
  - `C2:3D05` clears `$5E78`
- both resolve a `D5:9589` descriptor record from selected-row byte `+0x00` through `C0:8FF7` selector `#$005E`
- both begin by clearing a 0x1C-byte working buffer through `C0:8EFC`:
  - `C2:3BCF` clears buffer `A983`
  - `C2:3D05` clears buffer `A99E`
- both then call the local helper `C2:3B66` to write expanded bytes into that cleared working buffer
- both may append extra bytes based on selected-row fields like `+0x0B`, `+0x0E`, and `+0x4C`
- both finish by calling nearby `C1:DD70`-family helpers

The strongest current read is that these are not arbitrary control-flow twins. They are two sides of the same "rebuild working battle context from selected row plus descriptor" operation.

## `C2:3BCF` looks like the first-side rebuild helper

`C2:3BCF` works from `$A970` and appears to drive the first half of the rebuilt state.

Current safest local clues:

- it resolves the descriptor for the row currently in `$A970`
- it clears and then fills working buffer `A983` via `C0:8EFC` plus `C2:3B66`
- it uses `$5E77` as its local presence or append flag
- in one branch it emits byte `0x50` and a `0x70 + row[+0x0B]` style value into the built data
- it ends through `C1:DD70`

I do not think we have enough yet to say whether this is specifically "attacker text context" or "left-side command context," but it is clearly the first half of the paired rebuild.

## `C2:3D05` looks like the second-side rebuild helper

`C2:3D05` is the companion routine for `$A972`.

Current safest local clues:

- it resolves the descriptor for the row currently in `$A972`
- it clears and then fills working buffer `A99E` via `C0:8EFC` plus `C2:3B66`
- it uses `$5E78` as the companion local presence or append flag
- it stores selected-row byte `+0x00` into `$965A`
- it ends through `C1:DD76`

That makes it the natural companion for the second side of the reflected-hit rebuild.

## `C2:3B66` looks like a small template-expander

The local helper `C2:3B66` is worth calling out because both rebuild routines depend on it.

Current safest read:

- it takes a destination buffer pointer in `A`
- it walks a source byte stream supplied through `$1D/$1F`
- it copies ordinary bytes directly
- it treats value `0xAC` specially by expanding bytes from the `99CE` table family
- it writes the expanded result into the caller's destination buffer
- it null-terminates the result and returns the output length in `Y`

That makes `C2:3B66` look like a compact byte-template expander over pre-cleared output buffers rather than a gameplay-state mutator.

This is a good fit for the idea that `C2:3BCF` and `C2:3D05` are rebuilding compact working command or presentation buffers after the reflected-hit swap.

## Why this matters for the reflected Thunder path

The reflected Thunder path now reads more coherently end to end:

1. `C2:966B` detects the Franklin-Badge-like special case.
2. It displays the reflection text and sets `$AA96 = 1`.
3. It calls `C2:7E8A`.
4. `C2:7E8A` swaps `$A970/$A972`.
5. `C2:3BCF` and `C2:3D05` rebuild the dependent per-side working state from the swapped rows.
6. Later, `C2:94CE` consumes `$AA96` to finish shield weakening and cleanup.

That is a much tighter local model than "reflection branch calls an unknown helper."

## Current safest takeaway

The safest current takeaway is:

- `C2:7E8A` is a reflected-hit swap-and-rebuild helper
- `C2:3BCF` and `C2:3D05` are paired context-rebuild helpers for the two selected-row anchors
- `C2:3B66` is a small template expander used by both rebuild helpers
- the reflected Thunder branch now has a believable local mechanism for rebuilding battle working state after swapping acting and receiving sides

## Best next target

The best next move is to tighten what the rebuilt buffers actually represent, especially:

- what `A983` and `A99E` encode,
- what `$5E77` and `$5E78` mean,
- and what the `C1:DD70` / `C1:DD76` tail calls do with the rebuilt data.

That should let us replace "context rebuild" with something more concrete like command-buffer rebuild, message-context rebuild, or target-state rebuild.
