# Audio 0x00 Terminator Review

Status: N-SPC-family 0x00 terminator candidates grouped; EarthBound end-vs-return proof is still pending.

## Summary

- candidate packs: `10`
- candidate tracks: `19`
- promotion classes: `{'zero_runtime_effect_pending': 10}`
- post-zero-proof track actions: `{'classify_active_preview_before_exact_export': 7, 'decode_loop_points_before_exact_export': 2, 'review_observed_silence_as_finite_or_transition': 10}`
- pre-promotion blockers by track: `{'ef_return_stack_model': 15, 'zero_runtime_effect_proof': 19}`
- zero semantic status: `pending_earthbound_zero_control_effect_proof`
- zero exact-duration promotion allowed: `False`

## Track Action Triage

| Action | Tracks |
| --- | ---: |
| `classify_active_preview_before_exact_export` | 7 |
| `decode_loop_points_before_exact_export` | 2 |
| `review_observed_silence_as_finite_or_transition` | 10 |

| Blocker | Tracks |
| --- | ---: |
| `ef_return_stack_model` | 15 |
| `zero_runtime_effect_proof` | 19 |

## Candidates

| Pack | ROM range | Tracks | Export classes | 0x00 candidates | EF edges | Promotion class |
| ---: | --- | --- | --- | ---: | ---: | --- |
| `25` | `EC:E101..EC:EB51` | `[32, 33, 34, 35, 36, 37, 38, 39]` | `{'finite_or_transition_review_candidate': 8}` | 32 | 44 | `zero_runtime_effect_pending` |
| `1` | `E6:0000..E6:45D8` | `[1, 174]` | `{'unknown_active_preview': 1, 'finite_or_transition_review_candidate': 1}` | 2 | 9 | `zero_runtime_effect_pending` |
| `163` | `EE:0A8B..EE:0FB2` | `[175]` | `{'finite_or_transition_review_candidate': 1}` | 2 | 4 | `zero_runtime_effect_pending` |
| `148` | `EE:3A7D..EE:3E9C` | `[143]` | `{'unknown_active_preview': 1}` | 5 | 12 | `zero_runtime_effect_pending` |
| `160` | `EE:4ADF..EE:4EEA` | `[171]` | `{'loop_or_held_candidate': 1}` | 4 | 20 | `zero_runtime_effect_pending` |
| `154` | `EB:E9E4..EB:FE22` | `[157]` | `{'unknown_active_preview': 1}` | 4 | 6 | `zero_runtime_effect_pending` |
| `107` | `EC:4592..EC:6700` | `[94]` | `{'unknown_active_preview': 1}` | 4 | 3 | `zero_runtime_effect_pending` |
| `136` | `EE:0000..EE:0554` | `[120, 173]` | `{'unknown_active_preview': 1, 'loop_or_held_candidate': 1}` | 5 | 0 | `zero_runtime_effect_pending` |
| `18` | `E2:FC88..E2:FFFD` | `[25]` | `{'unknown_active_preview': 1}` | 3 | 0 | `zero_runtime_effect_pending` |
| `96` | `CF:FF38..CF:FFF9` | `[85]` | `{'unknown_active_preview': 1}` | 1 | 0 | `zero_runtime_effect_pending` |

## Promotion Rules

- 0x00 is the N-SPC-family phrase termination/end-of-subroutine candidate, not automatic public exact-duration proof.
- EF context must distinguish subroutine return from true phrase/song end.
- Finite trim candidates may use 0x00 as corroboration only after EarthBound-local effect proof.
- Loop/held candidates remain preview exports until loop entry/exit semantics are decoded.

## Findings

- The focused 0x00 lane replaces the former FF-centered terminator review for N-SPC-family evidence.
- Candidate records include offsets, counts, hashes inherited from the walk frontier, and derived statuses only.
- No candidate is promoted for public sequence exact-duration export until local EarthBound effect proof is added.

## Next Work

- trace or disassemble EarthBound 0x00 handling and record end-vs-EF-return behavior
- join 0x00 observations with EF call-stack context for finite candidate packs
- feed confirmed finite/return semantics back into audio-export-plan duration_semantics
