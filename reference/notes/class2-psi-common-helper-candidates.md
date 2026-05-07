# Class2 PSI Common Helper Candidates

This note captures the current best mapping between early local PSI-family shared helpers in bank `C2` and the corresponding named `*_COMMON` routines in the quarantined `ebsrc` reference tree.

See also `notes/class2-psi-action-wrapper-local-verification.md`.
See also `notes/class2-d57b68-early-entry-name-crosswalk.md`.

## Working Names

- `C2:9516` = `RunPsiRockinCommon`
- `C2:957A` = `RunPsiFireCommon`
- `C2:95CF` = `RunPsiFreezeCommon`
- `C2:966B` = `RunPsiThunderCommon`
- `C2:9A80` = `RunPsiStarstormCommon`

## Current best helper-family mapping

The strongest current mapping is:

- local `C2:9516` -> strongest reference-backed fit for `PSI_ROCKIN_COMMON`
- local `C2:957A` -> strongest reference-backed fit for `PSI_FIRE_COMMON`
- local `C2:95CF` -> strongest reference-backed fit for `PSI_FREEZE_COMMON`
- local `C2:966B` -> strongest reference-backed fit for `PSI_THUNDER_COMMON`
- local `C2:9A80` -> strongest reference-backed fit for `PSI_STARSTORM_COMMON`

This is still not framed as a pure local proof of every final symbolic name, but it is now materially stronger than a simple table-order guess. The local wrapper quartets, parameter signatures, and family-specific control-flow differences all line up with the reference common-helper split.

## Why the mapping is strong

Three things line up at once:

- the `D5:7B68` action-table order matches the reference battle action order
- the early local action entries form the expected per-rank wrapper families
- the argument signatures and some family-specific control-flow traits line up with the reference `*_COMMON` routines unusually well

## Rockin helper candidate: `C2:9516`

Local wrapper evidence:

- `C2:9556..9571` are four single-parameter wrappers that load `A` with rank-scaled values and call `C2:9516`

Reference comparison:

- `BTLACT_PSI_ROCKIN_A/B/G/O` all call `PSI_ROCKIN_COMMON` with a single damage-like parameter in `A`
- `PSI_ROCKIN_COMMON` has a family-specific extra branch for a dodge or no-effect path before weakening shield

Useful local clue:

- `C2:9516` is the only early helper in this cluster that includes an extra message-dispatch-looking path through `C1:DC1C` with hardcoded pointer `EF:766E`, which fits the idea that Rockin has a special text path when the attack is avoided or ineffective

That makes `C2:9516` a strong local candidate for `PSI_ROCKIN_COMMON`.

## Fire helper candidate: `C2:957A`

Local wrapper evidence:

- `C2:95AB..95C6` are four single-parameter wrappers that load `A` and call `C2:957A`

Reference comparison:

- `BTLACT_PSI_FIRE_A/B/G/O` all call `PSI_FIRE_COMMON` with one damage-like parameter in `A`
- `PSI_FIRE_COMMON` is simpler than Freeze and Thunder: it nullifies shield, applies variance, applies fire resistance, then weakens shield

Useful local clue:

- `C2:957A` has the same one-parameter family shape and lacks the extra up-front target guard that appears in the Freeze candidate

That makes `C2:957A` the strongest current candidate for `PSI_FIRE_COMMON`.

## Freeze helper candidate: `C2:95CF`

Local wrapper evidence:

- `C2:9647..9662` are four single-parameter wrappers that load `A` and call `C2:95CF`

Reference comparison:

- `BTLACT_PSI_FREEZE_A/B/G/O` all call `PSI_FREEZE_COMMON` with one damage-like parameter in `A`
- `PSI_FREEZE_COMMON` is notably richer than Fire because it first runs an NPC or invalid-target failure guard, then later includes a chance-based solidify-status branch and a separate message path

Useful local clue:

- `C2:95CF` begins with an extra call to `C2:7CFD` before its target-selection work, unlike the Fire candidate
- that extra front-end guard is exactly the sort of family-specific difference we would expect between Fire and Freeze from the reference code

That makes `C2:95CF` a strong local candidate for `PSI_FREEZE_COMMON`.

## Thunder helper candidate: `C2:966B`

Local wrapper evidence:

- `C2:9871..9895` load both `X` and `A` before calling `C2:966B`
- the wrappers vary `X` as `1, 2, 3, 4` and `A` as `0x0078, 0x0078, 0x00C8, 0x00C8`

Reference comparison:

- `BTLACT_PSI_THUNDER_A/B/G/O` call `PSI_THUNDER_COMMON` with two parameters: hit-count-like input and damage-like input
- `PSI_THUNDER_COMMON` is the only early PSI helper in the reference set with this two-parameter shape and a much larger control-flow body

Useful local clue:

- `C2:966B` is also visibly much larger than the Fire and Freeze candidates and immediately stores both incoming parameters into working state
- its opening loop walks the 32-entry selection mask through `C2:7029`, counts active entries, and derives a clamped follow-up value before entering the larger body

That target-counting front end is exactly the sort of extra machinery we would expect for the Thunder family and makes this the strongest helper match in the whole cluster. `C2:966B` is very likely the local `PSI_THUNDER_COMMON` implementation.

## Starstorm helper candidate: `C2:9A80`

Local wrapper evidence:

- `C2:9AA6` and `C2:9AAF` are two single-parameter wrappers that load `A` and call `C2:9A80`

Reference comparison:

- `BTLACT_PSI_STARSTORM_A/O` both call `PSI_STARSTORM_COMMON` with one damage-like parameter in `A`
- `PSI_STARSTORM_COMMON` is structurally closer to Fire than to Thunder: shield nullify, variance, full resist damage, weaken shield

Useful local clue:

- `C2:9A80` has the same compact one-parameter shape as we would expect for the two-rank Starstorm family

That makes `C2:9A80` a strong local candidate for `PSI_STARSTORM_COMMON`.

## Current safest takeaway

The safest current takeaway is:

- the early local PSI action families now have strong shared-helper identities, not just wrapper-family identities
- `C2:9516`, `957A`, `95CF`, `966B`, and `9A80` are best treated as the local Rockin, Fire, Freeze, Thunder, and Starstorm common helpers, with the final symbolic names still carried as reference-backed promotions rather than pure local proofs
- `C2:966B` remains the strongest match of the group because its two-parameter signature and multi-hit flow uniquely match Thunder
- `C2:957A` and `C2:95CF` are also strong because the local structural difference between them mirrors the Fire versus Freeze split in the reference tree
- this gives us a much healthier naming bridge for the `D5:7B68` second-pointer families without pretending every inner helper callee is fully solved already

## Best next target

The best next move is to decode one shared helper locally enough to describe its real behavior flow. `C2:966B` is the best candidate because the Thunder match is strongest and its extra control flow should expose more of the battle-action execution machinery behind `C2:40A4`.
