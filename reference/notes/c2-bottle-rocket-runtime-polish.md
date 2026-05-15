# C2 Bottle Rocket Runtime Polish

This note records the byte-neutral source polish pass over the bottle-rocket
common helper and wrappers in the `C2:A3D1..A5EC` item-side source unit.

Primary source module:

- `src/c2/c2_a3d1_run_item_side_concentration_seal_action.asm`

Related evidence:

- `refs/EB-M2-Listing-v1/US/bank02.txt`
- `refs/ebsrc-main/ebsrc-main/src/battle/actions/bottle_rocket_common.asm`
- `refs/ebsrc-main/ebsrc-main/src/battle/actions/bottle_rocket.asm`
- `refs/ebsrc-main/ebsrc-main/src/battle/actions/big_bottle_rocket.asm`
- `refs/ebsrc-main/ebsrc-main/src/battle/actions/multi_bottle_rocket.asm`
- `refs/ebsrc-main/ebsrc-main/include/config.asm`
- `notes/c2-item-bomb-runtime-polish.md`

## Promoted Contracts

`C2:A57A` is the shared `BOTTLE_ROCKET_COMMON` helper. It takes an attempt
count in `A`, loops that many times, and increments a local successful-hit
count for each `C2:7CAF` / `RollSelectedVsActiveRowOffsetGate` success result.

Stable promoted constants:

- hit gate: `100`
- damage per successful hit: `120`
- bottle-rocket wrapper count: `1`
- big-bottle-rocket wrapper count: `5`
- multi-bottle-rocket wrapper count: `20`

After the loop, a zero-hit result emits the shared no-effect script `EF:766E`
through `C1:DC1C`. A nonzero-hit result computes
`successful_hits * 120`, applies `C2:6AFD` /
`ApplyTwentyFivePercentVariance`, and passes the result to `C2:8125` /
`ApplyDamageToSelectedTarget` for the selected-target damage application.

## Wrapper Names

The reference source gives direct names for the three adjacent far wrappers:

- `C2:A5D1` = `BTLACT_BOTTLE_ROCKET`
- `C2:A5DA` = `BTLACT_BIG_BOTTLE_ROCKET`
- `C2:A5E3` = `BTLACT_MULTI_BOTTLE_ROCKET`

The local source now exports matching wrapper aliases while preserving the
existing `BOTTLE_ROCKET_COMMON` entry.

## Phase 2 Trace-Oracles

Bottle rockets are a compact counted damage-family oracle for the Phase 2
damage lane. The useful trace points are the wrapper attempt count, each
speed/offset gate result, the final successful-hit count, `successful_hits *
120`, the 25-percent variance call, and the final `C2:8125` selected-target
damage ABI crossing.

Keep the counted gate separate from shared damage application in downstream
contracts. A zero-hit result is a no-effect text path; a nonzero result is an
amount-preparation path into the common damage spine.

## Remaining Soft Spots

- The surrounding `A3D1..A5EC` unit still contains neighboring item-side
  actions that should stay separate from the bottle-rocket family.
- The damage-type sentinel passed in `X = $00FF` is still named locally rather
  than promoted as a global damage enum.
