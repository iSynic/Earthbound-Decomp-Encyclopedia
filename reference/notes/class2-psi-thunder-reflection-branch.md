# Class2 PSI Thunder Reflection Branch

This note tightens the special-case branch inside local `C2:966B`, the current best candidate for `PSI_THUNDER_COMMON`.

See also `notes/class2-psi-thunder-common-local-flow.md`.
See also `notes/class2-reflected-hit-context-rebuild.md`.
See also `notes/class2-psi-shield-post-hit-aa96.md`.
See also `notes/class2-busy-helper-eacf-and-window-setup.md`.

## Working Names

- `C2:97A5` = `HandlePsiThunderFranklinBadgeReflection`
- `C2:9821` = `DisplayPsiThunderMissPresentation`
- `C2:985A` = `CheckPsiThunderRequestedHitCountOrContinue`
- `C2:9863` = `ClearPsiThunderTargetMaskAndReturn`

## Current strongest claim

The special branch inside local `C2:966B` now looks very likely to be the same Franklin Badge lightning-reflection path described in the `ebsrc` reference Thunder routine.

This is still a cross-checked inference rather than a full local symbolic decode, but the match is now stronger than a vague "reflection-like" description.

## Why the match is stronger now

In the `ebsrc` reference `PSI_THUNDER_COMMON`, the relevant branch does this in broad shape:

- only checks the special case for one side of the battle
- loads `X = 1`
- reads the target row byte, increments it, and passes that into `FIND_ITEM_IN_INVENTORY2`
- if the search succeeds, it displays `MSG_BTL_FRANKLIN_TURN`
- sets `DAMAGE_IS_REFLECTED = 1`
- swaps attacker and target

The local `C2:966B` success branch now matches that structure unusually well.

## Local branch shape at `C2:97A1+`

After the busy wait, the local success path:

- loads the selected row from `$A972`
- clears byte `+0x4B`
- checks byte `+0x0E` and only continues into the special branch when it is zero
- writes `1` to local `$16`
- reads selected-row byte `+0x10`, increments it, and passes that together with the fixed `1` through `C4:5683`
- if that check succeeds, it dispatches `EF:7160` through `C1:DC1C`
- sets `$AA96 = 1`
- calls `C2:7E8A`

The row-byte-plus-one search pattern is the most important new clue. It matches the reference Thunder branch's inventory check shape much more closely than our earlier summary did.

Source follow-up (2026-05-06): the reflection tail now names the miss
presentation, requested-hit-count gate, target-mask cleanup return, and the
back-edge to `C2:96CB` / `RunPsiThunderNextStrike`. The four rank wrappers at
`C2:9871/987D/9889/9895` now call `RunPsiThunderCommon` by name.

## `C4:5683` now reads like an inventory or possession checker

The helper at `C4:5683` strengthens that interpretation.

Current safest local read:

- with ordinary inputs it calls `C4:5637`
- `C4:5637` walks a small bounded list using `C0:8FF7` selector `#$005F`
- it compares byte values against the requested item-like id
- it returns success when a match is found

`C4:5683` also has a special `A == 0xFFFF` entry path that scans repeatedly, which is exactly the kind of behavior we would expect from an inventory or possession search helper rather than from a graphics routine.

That does not prove the exact item identity by itself, but it is a very good fit for the reference branch that searches for the Franklin Badge.

## `C2:7E8A` reads like a reflected-hit context swap helper

The follow-up helper at `C2:7E8A` is also a good local fit for the reflection story.

Current safest local read:

- it swaps `$A970` and `$A972`
- then calls `C2:3BCF`
- then calls `C2:3D05`
- then returns

That is a strong local shape for "swap attacker and target contexts, then rebuild the working battle-selection state for the reflected hit."

I am still leaving the exact symbolic names of `C2:3BCF` and `C2:3D05` open, but the context-swap behavior is clear enough to use as a working description.

## Why `$AA96 = 1` matters

The local branch sets `$AA96 = 1` immediately before calling `C2:7E8A`.

That write lines up well with the broader reflection model because the post-hit cleanup helpers at `C2:941D` and `C2:94CE` check `$AA96` and take different presentation or cleanup paths when it is set.

So `$AA96` now reads best as a reflected-hit or special-resolution marker, not a generic scratch flag.

## Current safest takeaway

The safest current takeaway is:

- the special branch inside local `C2:966B` is very likely the Franklin Badge reflection path from the reference Thunder routine
- `C4:5683` behaves like the needed inventory or possession check helper
- `C2:7E8A` behaves like a reflected-hit context swap and refresh helper
- `$AA96` behaves like a reflected-hit marker consumed by the post-hit cleanup path

That is a materially stronger statement than the earlier "reflection-style special case" wording.

## Best next target

The best next move is to tighten the `$AA96` consumers in `C2:941D` and `C2:94CE`, because that should tell us exactly how the reflected-hit marker changes post-hit text, cleanup, or target-state handling.
