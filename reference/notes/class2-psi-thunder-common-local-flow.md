# Class2 PSI Thunder Common Local Flow

This note captures the first local behavior sketch for `C2:966B`, the strongest current candidate for `PSI_THUNDER_COMMON`.

See also `notes/class2-psi-common-helper-candidates.md`.
See also `notes/class2-second-pointer-consumer-40a4.md`.
See also `notes/class2-psi-thunder-reflection-branch.md`.

## Why this helper was the best next target

Among the early PSI families, Thunder had the strongest helper match before this pass:

- the wrappers `C2:9871..9895` pass two parameters instead of one
- the reference `PSI_THUNDER_COMMON` is the only early PSI helper in the compared set with that same two-parameter shape
- the local body at `C2:966B` is much larger than the Fire, Freeze, or Starstorm candidates

This made it the best place to push from "strong crosswalk" into a real local flow description.

## Entry signature still matches Thunder best

The local wrappers feed `C2:966B` like this:

- `C2:9871` / `RunPsiThunderAlpha`: `X = 1`, `A = 0x0078`
- `C2:987D` / `RunPsiThunderBeta`: `X = 2`, `A = 0x0078`
- `C2:9889` / `RunPsiThunderGamma`: `X = 3`, `A = 0x00C8`
- `C2:9895` / `RunPsiThunderOmega`: `X = 4`, `A = 0x00C8`

The local helper immediately stores those two inputs separately:

- `X` goes to local `$1A`
- `A` goes to local `$04`

That still fits the reference reading extremely well: hit-count-like parameter plus damage-like parameter.

## Opening phase: count active targets and derive a success value

The first phase of `C2:966B` walks the 32-entry target mask through `C2:7029`:

- it iterates candidate indices `0..31`
- it counts how many bits are active in local `$18`
- it multiplies that count by `64`
- it clamps the result at `255`
- it stores the clamped result in local `$02`

That aligns closely with the reference `PSI_THUNDER_COMMON`, which counts targeted battlers and derives a `count * 64`, clamped to `255`, before the per-hit loop begins.

## Outer phase: preserve the working target mask and loop by requested hit count

After deriving that clamped value, the local helper:

- snapshots the current target mask from `$A96C/$A96E` into local pairs `$06/$08` and `$12/$14`
- clears a local hit counter in `$18`
- enters the first iteration through the named `C2:985A` requested-hit-count gate
- enters a loop whose tail checks both:
  - whether side `0` still has remaining members through `C2:BAC5(0)`
  - whether side `1` still has remaining members through `C2:BAC5(1)`
- increments the local hit counter after each completed strike
- stops when the completed-hit count reaches the requested hit count in `$1A`

This is a strong local match for the reference Thunder behavior, which attempts repeated strikes but stops early if one side is exhausted.

## Per-hit setup: rebuild and narrow the target selection

The inner per-hit path begins at `C2:96CB` / `RunPsiThunderNextStrike` and does the following in broad shape:

- restores the saved working target mask
- runs a filtering step through `C2:416F`
- exits early if the filtered mask is empty
- restores the filtered mask to `$A96C/$A96E`
- calls `C2:6EF8`, the known mask helper family entry, to choose a surviving target index
- scans again through `C2:7029` to find the selected active bit
- maps that selected bit through `C0:8FF7` with selector `#$004E`
- adds the result to `7E:9FAC` and stores it in `$A972`

The important local conclusion is that Thunder is not just replaying a static effect on a fixed target. It is rebuilding a live target choice inside the 32-entry candidate domain for each strike.

## Success branch: hit presentation, busy wait, and target-side handling

Once the selected target is established, the local helper calls `C2:3D05`, then feeds the derived value in `$02` through `C2:6BB8` / `RollActionChanceGate`.

Current safest interpretation:

- that path behaves like the reference success check for whether a Thunder strike lands
- on success, the helper chooses one of two `EF:` pointers based on whether the damage-like parameter in `$04` is `0x0078` or not
- it dispatches that pointer through `C1:DC1C`
- it then loops on `C2:EACF`, matching the already-documented busy/effect wait path

That is a strong local match for the reference Thunder branch that displays a small-versus-large Thunder presentation, then waits for the current effect to finish before proceeding.

## Success branch: reflection and damage-side helpers

After the busy wait, the local success path continues with a cluster that strongly resembles the reference Thunder post-hit handling:

- it clears selected-row byte `+0x4B`
- it checks selected-row byte `+0x0E` and may enter a special branch only when that byte is zero
- in that branch it uses selected-row byte `+0x10`, then calls `C4:5683`
- if that check succeeds, it dispatches `EF:7160`, sets `$AA96 = 1`, and calls `C2:7E8A`

That is now a stronger local shape match for the reference Franklin Badge reflection logic. The row-byte-plus-one search pattern through `C4:5683`, plus the immediate `$AA96 = 1` write and `C2:7E8A` context-swap helper, line up closely enough that the Franklin Badge interpretation is now the best current working model rather than just a loose thematic guess.

After that, the helper enters a target and damage cluster through `C2:941D`,
`C2:6A44` / `RollRandomAmount`, `C2:8125` /
`ApplyDamageToSelectedTarget`, and `C2:94CE`.

The safest current summary is:

- this cluster behaves like the reference shield/nullify, damage variance, resistance, and cleanup path in broad shape
- I am not yet claiming one-to-one local names for each of those callees

## Failure branch: miss presentation

If the success roll does not pass, the helper takes a different branch:

- it dispatches pointer `EF:8837` through `C1:DC1C`
- it then dispatches pointer `C8:FAF6` through `C1:DC1C`

This strongly resembles the reference Thunder miss branch, which emits two different presentation or text payloads for the miss case.

Source follow-up (2026-05-06): the cross-module Thunder loop edges now have
source labels. The common helper jumps to `DisplayPsiThunderMissPresentation`
for `C2:9821`, `CheckPsiThunderRequestedHitCountOrContinue` for `C2:985A`,
and `ClearPsiThunderTargetMaskAndReturn` for `C2:9863`; the reflection tail
continues the loop through `RunPsiThunderNextStrike` at `C2:96CB`.

## What is now locally solid

The following Thunder claims are now locally solid enough to rely on in notes:

- `C2:966B` is a multi-hit action helper, not a simple one-shot damage wrapper
- it counts active targets up front and derives a clamped `count * 64` value
- it loops over individual strikes up to the requested hit count
- it rebuilds live target selection from the 32-entry mask domain on each strike
- it uses the same busy/effect wait helper `C2:EACF` already tied to battle-style presentation flow
- it has distinct success and failure presentation branches
- it includes a likely Franklin Badge reflection branch with a possession check, reflected-hit marker, and context swap
- its rank wrappers and cross-module loop/tail targets are now named in source

## Current safest takeaway

The safest current takeaway is that `C2:966B` is no longer just the best candidate for `PSI_THUNDER_COMMON`; it now behaves like a real local Thunder-family action implementation in broad control-flow terms, and it is the strongest current reference-backed promotion target for that final symbolic name.

That is an important step because it anchors the broader `D5:7B68 -> C2:40A4` action-table story in an actual decoded battle-action family instead of only table matching.

## Best next target

The best next move is to tighten the remaining helper clusters that are still
raw around Thunder-adjacent presentation or reflected-hit cleanup, now that the
main wrapper and loop-tail boundaries are no longer ambiguous.
