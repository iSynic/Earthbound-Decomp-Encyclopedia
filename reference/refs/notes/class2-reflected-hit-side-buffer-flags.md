# Class2 Reflected Hit Side Buffer Flags

This note captures the current best interpretation of `$5E77` and `$5E78` inside the reflected-hit rebuild family.

See also `notes/class2-reflected-hit-context-rebuild.md`.
See also `notes/class2-reflected-hit-text-context.md`.

## Current strongest claim

`$5E77` and `$5E78` do not look like persistent battle state. They now read much more like short-lived per-side "extra token was appended to this rebuilt buffer" flags.

That is still an inference, but it fits the local write and read pattern much better than alternatives like "buffer valid" or "side active."

## Why they look short-lived

The write/read footprint is very small.

Observed local behavior:

- `C2:3BCF` begins by clearing `$5E77`
- `C2:3D05` begins by clearing `$5E78`
- only a few routines in the surrounding battle-text family write them back to `1`
- bank `C3` has paired readers at `C3:E773` and `C3:E78F`
- broader subsystem init also clears both flags along with nearby transient text or state bytes

That shape is a strong fit for transient one-shot formatting flags rather than for durable gameplay state.

## Where `C2:3BCF` sets `$5E77`

Inside `C2:3BCF`, the flag is set only on a narrow branch:

- the row in `$A970` must satisfy the special branch through byte `+0x0E == 1`
- the local append length gate in `$16` must still be zero
- selected-row byte `+0x0B` must equal `1`
- helper `C2:B66A` fed by row byte `+0x4C` must not report `2`

Only then does `C2:3BCF`:

- append byte `0x50` into the rebuilt buffer
- append a second byte shaped like `0x70 + row[+0x0B]`
- set `$5E77 = 1`

The important point is that the flag is set right next to a tiny optional append block.

That makes `$5E77` look much more like "the first-side rebuilt buffer carries an extra side token" than like a general state flag.

## Where the companion side likely behaves the same way

The exact mirrored write to `$5E78` is not inside `C2:3D05` itself, but the surrounding family strongly suggests the same pattern on the companion side:

- `C2:3D05` clears `$5E78` at entry
- the only direct set we found nearby is in the companion battle-text family at `C2:BDA9`
- bank `C3` reads `$5E78` in the same paired way that it reads `$5E77`

So the safest current interpretation is that `$5E78` is the second-side companion flag for the same optional-token mechanism.

## Why the `C3:E773` / `C3:E78F` readers matter

The best evidence against a generic "buffer valid" reading comes from the paired readers in bank `C3`.

Current safest local read:

- `C3:E773` clears `$5E77`, then checks whether `$5E77` had been set
- if it had not been set, it falls through toward the companion side and related id checks through `$9658/$965A`
- if the side flag had been set, it uses descriptor-derived data and then dispatches a short helper through `C4:47FB`

`C3:E78F` does the same for `$5E78`.

That is a much better fit for "consume an optional side token or side-specific suffix" than for "is this buffer initialized?"

## What the flags probably gate

The safest current working model is:

- `A983` and `A99E` are the per-side rebuilt output buffers
- most of their content is rebuilt unconditionally from descriptor and side context
- `$5E77` and `$5E78` indicate whether a special side-specific extra token was appended during that rebuild
- later bank-`C3` code checks those flags to decide whether it needs to run a companion formatting or rendering step for that extra token

I am deliberately not claiming whether the extra token is a name suffix, target marker, party-position marker, or something else. The local evidence is stronger on the existence of the optional token than on its final user-facing meaning.

## Why this sharpens the reflected-hit story

This helps because it narrows what the reflection rebuild is really doing.

The swap path is not merely rebuilding two opaque buffers. It is rebuilding two side-specific text-context buffers, and those buffers can carry optional side-specific appended tokens tracked by `$5E77/$5E78`.

That is a much more concrete statement than our earlier "some mixed text/state layer" model.

## Current safest takeaway

The safest current takeaway is:

- `$5E77` and `$5E78` are best read as transient per-side optional-token flags
- `C2:3BCF` sets `$5E77` right when it appends a tiny extra byte pair to the first-side rebuilt buffer
- the companion family likely does the same for `$5E78` on the second side
- those appended bytes now look more like battle text control tokens than raw printable suffix bytes
- bank `C3` consumes those flags as part of a later side-specific token-resolution step
- the strongest current local read is that this late resolution can select the article fragment `"The "` versus `"the "` based on `@`-style capitalization context before continuing into a row-position-aware battle text family near `C4:54F0`

That makes the rebuilt `A983` / `A99E` buffers look more like structured side-text buffers than generic scratch space.

## Follow-up note

See also [class2-reflected-hit-side-token-consumers.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-reflected-hit-side-token-consumers.md) for the tighter bank-`C3` interpretation.
See also [class2-row-position-text-cluster-c454f0.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-row-position-text-cluster-c454f0.md) for the row-position text anchor right after `C4:51FA`.

## Best next target

The best next move is to identify what the paired helper data at `C2:0998` and `C2:099C` actually encodes, because that should finally tell us what those side-token cases mean in player-visible terms.
