# Class2 PSI Action Wrapper Local Verification

This note records the first direct local byte-level verification for the early PSI action families reached through `D5:7B68`.

See also `notes/class2-d57b68-early-entry-name-crosswalk.md`.
See also `notes/class2-second-pointer-consumer-40a4.md`.
See also `notes/class2-psi-common-helper-candidates.md`.

## Why this note matters

The action-table crosswalk already made it very likely that early `D5:7B68` entries map to battle action families like Rockin, Fire, Freeze, and Thunder.

The useful next question is whether the local `C2:` handlers themselves look like the thin per-rank wrappers that the `ebsrc` reference project uses. For several families, the answer is yes.

## Rockin family is locally consistent with wrapper stubs

At `C2:9556` the local bytes decode as a repeated pattern:

- `C2:9556`: load `A = 0x0050`, `JSR C2:9516`, `RTL`
- `C2:955F`: load `A = 0x00B4`, `JSR C2:9516`, `RTL`
- `C2:9568`: load `A = 0x0140`, `JSR C2:9516`, `RTL`
- `C2:9571`: load `A = 0x0280`, `JSR C2:9516`, `RTL`

That is exactly the shape we would expect for `PSI_ROCKIN_ALPHA/BETA/GAMMA/OMEGA` wrappers over one shared helper.

## Fire family is locally consistent with wrapper stubs

At `C2:95AB` the same pattern appears with a different shared helper:

- `C2:95AB`: load `A = 0x0050`, `JSR C2:957A`, `RTL`
- `C2:95B4`: load `A = 0x00A0`, `JSR C2:957A`, `RTL`
- `C2:95BD`: load `A = 0x00F0`, `JSR C2:957A`, `RTL`
- `C2:95C6`: load `A = 0x0140`, `JSR C2:957A`, `RTL`

That is a very clean local match for a `PSI_FIRE_*` wrapper family.

## Freeze family is locally consistent with wrapper stubs

At `C2:9647` the local bytes again form a tight wrapper run:

- `C2:9647`: load `A = 0x00B4`, `JSR C2:95CF`, `RTL`
- `C2:9650`: load `A = 0x0168`, `JSR C2:95CF`, `RTL`
- `C2:9659`: load `A = 0x021C`, `JSR C2:95CF`, `RTL`
- `C2:9662`: load `A = 0x02D0`, `JSR C2:95CF`, `RTL`

That is again exactly the wrapper shape we would expect from `PSI_FREEZE_ALPHA/BETA/GAMMA/OMEGA`.

## Thunder family is locally consistent with wrapper stubs

At `C2:9871` the pattern is slightly richer but still clearly wrapper-based:

- `C2:9871`: load `X = 1`, `A = 0x0078`, `JSR C2:966B`, `RTL`
- `C2:987D`: load `X = 2`, `A = 0x0078`, `JSR C2:966B`, `RTL`
- `C2:9889`: load `X = 3`, `A = 0x00C8`, `JSR C2:966B`, `RTL`
- `C2:9895`: load `X = 4`, `A = 0x00C8`, `JSR C2:966B`, `RTL`

This fits the reference pattern for `PSI_THUNDER_*` well, because Thunder varies by both hit-count-like and damage-like parameters.

## Starstorm family is locally consistent with wrapper stubs

At `C2:9AA6` the two-entry Starstorm family is also clean:

- `C2:9AA6`: load `A = 0x0168`, `JSR C2:9A80`, `RTL`
- `C2:9AAF`: load `A = 0x02D0`, `JSR C2:9A80`, `RTL`

That matches the expected `PSI_STARSTORM_ALPHA/OMEGA` two-rank family very well.

## Flash family now has a real local branch map

The Flash run at `C2:9987`, `99AE`, `99EF`, and `9A35` is still more complex than the tiny one-jump quartets, but it is no longer just an unresolved oddball.

The shared local shape is now clear:

- gate through `C2:7CFD`
- gate through `C2:98A1`
- sample `C0:8E9A & 7`
- branch into a status or collapse ladder built from:
  - `C2:7550`
  - `C2:9917`
  - `C2:98DE`
  - `C2:9950`
- finish through `C2:94CE`

The concrete texts behind those three smaller helpers are now pinned too:

- `C2:9917` -> numbness text `EF:6AE0`
- `C2:98DE` -> strange text `EF:6C3A`
- `C2:9950` -> crying text `EF:6BBB`

So Flash is no longer best described as "still needs deeper local decoding." It now has a real local tier ladder, documented in `notes/class2-psi-flash-common-local-flow.md`.

## Current safest takeaway

The safest current takeaway is:

- the local ROM now directly supports the early-entry action-family crosswalk, not just the reference table order
- Rockin, Fire, Freeze, Thunder, and Starstorm all have clear local wrapper-family shapes
- those wrapper families now converge on strong shared-helper identities in bank `C2`:
  - Rockin -> `C2:9516`
  - Fire -> `C2:957A`
  - Freeze -> `C2:95CF`
  - Thunder -> `C2:966B`
  - Starstorm -> `C2:9A80`
- Flash is now locally mapped as a real random status ladder, even though its tier logic is broader than the tiny wrapper quartets

This materially strengthens the local case that `D5:7B68` is feeding genuine battle action handlers rather than only generic script or presentation pointers.

## Best next target

The best next move is to decode one shared helper directly, probably `C2:957A`, `C2:95CF`, or `C2:966B`. That should turn one of these families from a strong wrapper-based inference into a locally verified action implementation.
