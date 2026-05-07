# Audio FF Variant Review

Status: FF variant candidates grouped; EarthBound-local proof is required because stock N-SPC marks VCMD FF invalid.

## Summary

- candidate packs: `0`
- candidate tracks: `0`
- promotion classes: `{}`
- promotion-class tracks: `{}`
- semantic status: `stock_n_spc_ff_invalid_earthbound_variant_proof_required`
- FF semantic status: `contradicted_by_stock_n_spc_pending_earthbound_variant_proof`
- FF exact-duration promotion allowed: `False`

## Promotion Rules

- No record in this review has unpromoted control blockers; those stay in the blocked lane.
- Stock N-SPC marks VCMD FF invalid; FF can only be promoted after EarthBound runtime/disassembly evidence contradicts that baseline.
- Finite/transition review tracks still need track-context review even when FF is confirmed.
- Loop/held candidates with FF still require loop-point or hold/fade interpretation before release exactness.

## Candidates

| Pack | ROM range | Tracks | Export classes | FF candidates | EF edges | Promotion class |
| ---: | --- | --- | --- | ---: | ---: | --- |

## Findings

- The N-SPC pivot moves normal finite-end review to 0x00; FF is now a variant/unreachable review lane.
- The promoted command-semantics manifest currently blocks FF exact-duration promotion unless runtime effect evidence is present.
- The static SPC700 driver dispatch frontier identifies a likely FF dispatch target at 0x1A81, but stock N-SPC marks VCMD FF invalid and EarthBound's runtime effect is still unpromoted.
- The SPC700 FF target review marks 0x1A81 as data-like under static byte profiling, so live PC/index tracing is required before any FF promotion.
- Candidate packs mix finite trims, finite/transition reviews, unknown active previews, and loop/held tracks, so FF confirmation alone is necessary but not sufficient for public exact exports.
- Tracks whose export class is finite_trim_candidate can use FF as sequence corroboration for existing PCM silence evidence once the driver dispatch is named.
- Loop/held packs with FF likely need intro/body loop modeling rather than simple finite-end promotion.

## Next Work

- inspect or trace the SPC700 target 0x1A81 and record whether EarthBound gives FF a variant-specific effect or leaves it invalid/unreachable
- keep finite promotion centered on 0x00 terminator/end-of-subroutine proof unless FF is locally proven
- keep loop_or_held_candidate records in the loop-point lane even if a local terminator is confirmed
