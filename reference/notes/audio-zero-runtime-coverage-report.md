# Audio Zero Runtime Coverage Report

Status: 0x00 runtime coverage is mapped; probe outputs are still pending and current export behavior is preserved.

## Summary

- blocker tracks: `19`
- probe jobs: `19`
- job track coverage exact: `True`
- candidate packs: `10`
- runtime zero reads: `5931`
- reader PC targets: `10`
- export classes: `{'finite_or_transition_review_candidate': 10, 'loop_or_held_candidate': 2, 'unknown_active_preview': 7}`
- trace focus jobs: `{'prove_zero_effect_but_loop_points_remain_required': 2, 'prove_zero_effect_then_classify_active_preview': 5, 'prove_zero_end_effect_then_review_finite_candidate': 1, 'trace_zero_reader_with_ef_stack_state': 11}`
- pack contexts: `{'needs_ef_return_stack_model': 11, 'zero_phrase_end_candidate_runtime_pending': 8}`
- post-proof actions: `{'classify_active_preview_before_exact_export': 7, 'decode_loop_points_before_exact_export': 2, 'review_observed_silence_as_finite_or_transition': 10}`
- pre-promotion blockers: `{'ef_return_stack_model': 15, 'zero_runtime_effect_proof': 19}`
- sequence promotion allowed: `False`

## Reader PC Targets

| Reader PC | Read count | Driver offset | Role |
| --- | ---: | --- | --- |
| `0x2DB0` | 957 | `0x28B0` | sequence_control_byte_reader_candidate |
| `0x2DDA` | 955 | `0x28DA` | sequence_control_byte_reader_candidate |
| `0x2DF8` | 955 | `0x28F8` | sequence_control_byte_reader_candidate |
| `0x2E3D` | 952 | `0x293D` | sequence_control_byte_reader_candidate |
| `0x0957` | 114 | `0x0457` | sequence_control_byte_reader_candidate |
| `0x0B8A` | 84 | `0x068A` | sequence_control_byte_reader_candidate |
| `0x0847` | 73 | `0x0347` | sequence_control_byte_reader_candidate |
| `0x0782` | 8 | `0x0282` | sequence_control_byte_reader_candidate |
| `0x07A6` | 8 | `0x02A6` | sequence_control_byte_reader_candidate |
| `0x0D12` | 1 | `0x0812` | sequence_control_byte_reader_candidate |

## Probe Jobs

| Track | Name | Export class | Trace focus | Post-proof action | Reader PCs | Promotion allowed |
| ---: | --- | --- | --- | --- | ---: | --- |
| 001 | `GAS_STATION` | `unknown_active_preview` | `trace_zero_reader_with_ef_stack_state` | `classify_active_preview_before_exact_export` | 10 | `False` |
| 025 | `CHAOS_THEATRE` | `unknown_active_preview` | `prove_zero_effect_then_classify_active_preview` | `classify_active_preview_before_exact_export` | 10 | `False` |
| 032 | `GIANT_STEP` | `finite_or_transition_review_candidate` | `trace_zero_reader_with_ef_stack_state` | `review_observed_silence_as_finite_or_transition` | 10 | `False` |
| 033 | `LILLIPUT_STEPS` | `finite_or_transition_review_candidate` | `trace_zero_reader_with_ef_stack_state` | `review_observed_silence_as_finite_or_transition` | 10 | `False` |
| 034 | `MILKY_WELL` | `finite_or_transition_review_candidate` | `trace_zero_reader_with_ef_stack_state` | `review_observed_silence_as_finite_or_transition` | 10 | `False` |
| 035 | `RAINY_CIRCLE` | `finite_or_transition_review_candidate` | `trace_zero_reader_with_ef_stack_state` | `review_observed_silence_as_finite_or_transition` | 10 | `False` |
| 036 | `MAGNET_HILL` | `finite_or_transition_review_candidate` | `trace_zero_reader_with_ef_stack_state` | `review_observed_silence_as_finite_or_transition` | 10 | `False` |
| 037 | `PINK_CLOUD` | `finite_or_transition_review_candidate` | `trace_zero_reader_with_ef_stack_state` | `review_observed_silence_as_finite_or_transition` | 10 | `False` |
| 038 | `LUMINE_HALL` | `finite_or_transition_review_candidate` | `trace_zero_reader_with_ef_stack_state` | `review_observed_silence_as_finite_or_transition` | 10 | `False` |
| 039 | `FIRE_SPRING` | `finite_or_transition_review_candidate` | `trace_zero_reader_with_ef_stack_state` | `review_observed_silence_as_finite_or_transition` | 10 | `False` |
| 085 | `BULLDOZER` | `unknown_active_preview` | `prove_zero_effect_then_classify_active_preview` | `classify_active_preview_before_exact_export` | 10 | `False` |
| 094 | `GOOD_FRIENDS_BAD_FRIENDS` | `unknown_active_preview` | `prove_zero_effect_then_classify_active_preview` | `classify_active_preview_before_exact_export` | 10 | `False` |
| 120 | `HOTEL_OF_THE_LIVING_DEAD` | `unknown_active_preview` | `prove_zero_effect_but_loop_points_remain_required` | `classify_active_preview_before_exact_export` | 10 | `False` |
| 143 | `LEAVING_MAGICANT` | `unknown_active_preview` | `prove_zero_effect_then_classify_active_preview` | `classify_active_preview_before_exact_export` | 10 | `False` |
| 157 | `ATTRACT_MODE` | `unknown_active_preview` | `prove_zero_effect_then_classify_active_preview` | `classify_active_preview_before_exact_export` | 10 | `False` |
| 171 | `WINTERS_INTRO` | `loop_or_held_candidate` | `trace_zero_reader_with_ef_stack_state` | `decode_loop_points_before_exact_export` | 10 | `False` |
| 173 | `GOOD_MORNING_MOONSIDE` | `loop_or_held_candidate` | `prove_zero_effect_but_loop_points_remain_required` | `decode_loop_points_before_exact_export` | 10 | `False` |
| 174 | `GAS_STATION_2` | `finite_or_transition_review_candidate` | `trace_zero_reader_with_ef_stack_state` | `review_observed_silence_as_finite_or_transition` | 10 | `False` |
| 175 | `TITLE_SCREEN` | `finite_or_transition_review_candidate` | `prove_zero_end_effect_then_review_finite_candidate` | `review_observed_silence_as_finite_or_transition` | 10 | `False` |

## Coverage Policy

- This report maps every current 0x00 runtime blocker to a probe job; it does not run the harness.
- Every job targets the same 10 reader PCs so EF-return and true-end semantics can be observed consistently.
- Promotion stays blocked until imported probe outputs classify 0x00 effects and refresh the duration uncertainty register.
- Post-proof actions remain lane-specific: active preview classification, finite/transition review, or exact loop metadata work.

## Remaining Uncertainty

- All 19 zero-runtime blockers have probe jobs, but no imported runtime classifications yet.
- 15 jobs still need EF-return stack modeling evidence before exact duration can be considered.
- The 10 finite/transition post-proof jobs still need finite-ending review after 0x00 effect proof.
