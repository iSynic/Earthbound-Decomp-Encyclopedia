# Audio Sequence Command Semantics

Status: promoted command semantics are evidence-gated; current checked-in traces do not permit sequence exact-duration promotion.

## Summary

- commands: `5`
- confirmed for exact duration: `0`
- pending: `1`
- blocked or contradicted: `4`
- source-backed VCMD commands: `3`
- zero-control pending commands: `1`
- outside-VCMD-table commands: `1`
- sequence promotion allowed: `False`
- semantic status: `promotions_require_runtime_dispatch_and_effect_evidence`

## Promotion Policy

- Static dispatch-table targets are evidence, not promotion authority.
- N-SPC family semantics are hypotheses for EarthBound, not promotion authority.
- 0x00 is the primary terminator/end-of-subroutine candidate under N-SPC semantics, but needs local EarthBound effect proof before sequence exact-duration promotion.
- FF cannot promote finite exact-duration semantics from the source-backed VCMD table because that table ends at FE; stock N-SPC also marks VCMD 0xFF invalid.
- FD and FE are treated as fast-forward timing toggles under the N-SPC hypothesis, but public exact exports still require local timing/effect proof.
- Loop/held tracks require loop metadata even if a local terminator is later confirmed.

## Commands

| Command | Hypothesis | Source role | Static target | Semantic status | Effect proof | Seq reads | Dispatch hits | Promotion allowed | Next export action |
| --- | --- | --- | ---: | --- | --- | ---: | ---: | --- | --- |
| `0x00` | `phrase_termination_or_end_of_subroutine` | `zero_control_pending` | `None` | `pending_earthbound_zero_control_effect_proof` | `zero_control_pending` | `5931` | `0` | `False` | `keep_public_exact_promotion_blocked` |
| `0xEF` | `subroutine` | `source_backed_vcmd` | `0x0AAC` | `runtime_interpreter_read_observed_dispatch_decode_pending` | `runtime_effect_pending` | `475` | `0` | `False` | `keep_public_exact_promotion_blocked` |
| `0xFD` | `fast_forward_on` | `source_backed_vcmd` | `0x0B7E` | `runtime_interpreter_read_observed_dispatch_decode_pending` | `runtime_effect_pending` | `1` | `0` | `False` | `keep_public_exact_promotion_blocked` |
| `0xFE` | `fast_forward_off` | `source_backed_vcmd` | `0x0B7F` | `runtime_interpreter_read_observed_dispatch_decode_pending` | `runtime_effect_pending` | `5` | `0` | `False` | `keep_public_exact_promotion_blocked` |
| `0xFF` | `invalid_stock_n_spc_vcmd` | `outside_vcmd_table` | `None` | `contradicted_by_stock_n_spc_pending_earthbound_variant_proof` | `outside_vcmd_table` | `12` | `0` | `False` | `keep_public_exact_promotion_blocked` |

## Findings

- The current checked-in evidence does not yet permit sequence-command exact-duration promotion.
- Existing PCM silence evidence may still support finite trim candidates independently of sequence-command promotion.
- The source-backed VCMD table and N-SPC hypothesis both shift exact finite-end work from FF toward 0x00 phrase/VCMD termination evidence.
- Runtime traces now identify control-byte reader PCs, but those reader paths still need effect decoding before this manifest can unblock exact sequence semantics.
- Source-effect facts now name the EF return slots and FD/FE timing state that runtime probes must capture.

## Next Work

- trace or disassemble EarthBound handling of 0x00 phrase/VCMD termination and EF return behavior
- decode the control reader frontier PCs, starting with 0x0957 for FF/FE/EF behavior
- treat FF observations as variant/unreachable evidence unless the reader path proves an EarthBound-specific effect
- decode FD/FE timing behavior before using fast-forward regions for exact loop or finite export decisions
