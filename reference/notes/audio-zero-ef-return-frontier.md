# Audio 0x00/EF Return Frontier

Status: 0x00 candidates are grouped by EF context; runtime proof is still required.

## Summary

- candidate packs: `10`
- sampled 0x00 walks: `35`
- sampled 0x00 walk classes: `{'end_vs_ef_return_ambiguous': 3, 'phrase_or_song_end_candidate_pending_runtime_proof': 32}`
- pack context classes: `{'needs_ef_return_stack_model': 3, 'zero_phrase_end_candidate_runtime_pending': 7}`
- trace focus packs: `{'prove_zero_effect_but_loop_points_remain_required': 1, 'prove_zero_effect_then_classify_active_preview': 5, 'prove_zero_end_effect_then_review_finite_candidate': 1, 'trace_zero_reader_with_ef_stack_state': 3}`
- post-zero-proof track actions: `{'classify_active_preview_before_exact_export': 7, 'decode_loop_points_before_exact_export': 2, 'review_observed_silence_as_finite_or_transition': 10}`
- runtime 0x00 reads: `5931`
- runtime 0x00 reader PCs: `10`
- sequence promotion allowed: `False`

## Runtime Probe Plan

| Reader PC | 0x00 reads | Driver offset | Required observation |
| --- | ---: | --- | --- |
| `0x2DB0` | 957 | `0x28B0` | record command pointer, EF stack/return state, voice slot, and post-read branch/effect for 0x00 |
| `0x2DDA` | 955 | `0x28DA` | record command pointer, EF stack/return state, voice slot, and post-read branch/effect for 0x00 |
| `0x2DF8` | 955 | `0x28F8` | record command pointer, EF stack/return state, voice slot, and post-read branch/effect for 0x00 |
| `0x2E3D` | 952 | `0x293D` | record command pointer, EF stack/return state, voice slot, and post-read branch/effect for 0x00 |
| `0x0957` | 114 | `0x0457` | record command pointer, EF stack/return state, voice slot, and post-read branch/effect for 0x00 |
| `0x0B8A` | 84 | `0x068A` | record command pointer, EF stack/return state, voice slot, and post-read branch/effect for 0x00 |
| `0x0847` | 73 | `0x0347` | record command pointer, EF stack/return state, voice slot, and post-read branch/effect for 0x00 |
| `0x0782` | 8 | `0x0282` | record command pointer, EF stack/return state, voice slot, and post-read branch/effect for 0x00 |

## Packs

| Pack | Tracks | Export classes | 0x00 candidates | EF edges | Context | Trace focus | Sampled walk classes |
| ---: | --- | --- | ---: | ---: | --- | --- | --- |
| `25` | `[32, 33, 34, 35, 36, 37, 38, 39]` | `{'finite_or_transition_review_candidate': 8}` | 32 | 44 | `needs_ef_return_stack_model` | `trace_zero_reader_with_ef_stack_state` | `{'end_vs_ef_return_ambiguous': 1, 'phrase_or_song_end_candidate_pending_runtime_proof': 15}` |
| `1` | `[1, 174]` | `{'unknown_active_preview': 1, 'finite_or_transition_review_candidate': 1}` | 2 | 9 | `needs_ef_return_stack_model` | `trace_zero_reader_with_ef_stack_state` | `{'end_vs_ef_return_ambiguous': 1}` |
| `163` | `[175]` | `{'finite_or_transition_review_candidate': 1}` | 2 | 4 | `zero_phrase_end_candidate_runtime_pending` | `prove_zero_end_effect_then_review_finite_candidate` | `{'phrase_or_song_end_candidate_pending_runtime_proof': 1}` |
| `148` | `[143]` | `{'unknown_active_preview': 1}` | 5 | 12 | `zero_phrase_end_candidate_runtime_pending` | `prove_zero_effect_then_classify_active_preview` | `{'phrase_or_song_end_candidate_pending_runtime_proof': 2}` |
| `160` | `[171]` | `{'loop_or_held_candidate': 1}` | 4 | 20 | `needs_ef_return_stack_model` | `trace_zero_reader_with_ef_stack_state` | `{'end_vs_ef_return_ambiguous': 1, 'phrase_or_song_end_candidate_pending_runtime_proof': 1}` |
| `154` | `[157]` | `{'unknown_active_preview': 1}` | 4 | 6 | `zero_phrase_end_candidate_runtime_pending` | `prove_zero_effect_then_classify_active_preview` | `{'phrase_or_song_end_candidate_pending_runtime_proof': 1}` |
| `107` | `[94]` | `{'unknown_active_preview': 1}` | 4 | 3 | `zero_phrase_end_candidate_runtime_pending` | `prove_zero_effect_then_classify_active_preview` | `{'phrase_or_song_end_candidate_pending_runtime_proof': 3}` |
| `136` | `[120, 173]` | `{'unknown_active_preview': 1, 'loop_or_held_candidate': 1}` | 5 | 0 | `zero_phrase_end_candidate_runtime_pending` | `prove_zero_effect_but_loop_points_remain_required` | `{'phrase_or_song_end_candidate_pending_runtime_proof': 5}` |
| `18` | `[25]` | `{'unknown_active_preview': 1}` | 3 | 0 | `zero_phrase_end_candidate_runtime_pending` | `prove_zero_effect_then_classify_active_preview` | `{'phrase_or_song_end_candidate_pending_runtime_proof': 3}` |
| `96` | `[85]` | `{'unknown_active_preview': 1}` | 1 | 0 | `zero_phrase_end_candidate_runtime_pending` | `prove_zero_effect_then_classify_active_preview` | `{'phrase_or_song_end_candidate_pending_runtime_proof': 1}` |

## Promotion Policy

- Static 0x00 context can prioritize work, but cannot decide exact end-vs-return semantics alone.
- A 0x00 on a path with an EF call edge remains ambiguous until the EF return stack model is proven.
- A 0x00 on a path without an EF call edge is an end candidate, but still needs EarthBound runtime/disassembly proof before public exact export.
- The source-backed 0x00 reader shows loop/return and pattern-control paths; runtime proof must capture which path each candidate takes.
- No record in this frontier directly promotes sequence exact-duration exports.

## Findings

- The new frontier identifies which 0x00 candidates need an EF return stack model first.
- Runtime 0x00 reader evidence is currently taken from the dispatch/control-reader manifests; older traces may report zero reads until regenerated with the widened harness contract.
- Source-effect evidence now provides the exact voice-reader, pattern-reader, and EF state slots that the runtime proof must capture.
- Pack-level export promotion remains blocked even for phrase-end-looking candidates.

## Next Work

- regenerate targeted ares traces for the 0x00 review packs using the widened zero-control trace contract
- decode reader PCs that observe 0x00 and record end-vs-return state transitions
- promote only packs whose 0x00 end proof agrees with EF context and track policy
