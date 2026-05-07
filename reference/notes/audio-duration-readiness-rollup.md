# Audio Duration Readiness Rollup

Status: exact-duration readiness remains blocked; current playback/export behavior is preserved.

## Summary

- tracks: `192`
- public exact duration tracks: `21`
- blocking tracks: `171`
- primary uncertainty counts: `{'active_preview_classification_pending': 1, 'finite_transition_review_pending': 5, 'loop_point_metadata_pending': 5, 'measurement_missing': 1, 'no_duration_uncertainty_for_current_export': 1, 'non_zero_control_semantics_pending': 155, 'pcm_trim_usable_sequence_intent_open': 5, 'zero_runtime_probe_pending': 19}`
- near oracle passed: `True`
- independent oracle passed: `False`
- independent oracle representative missing: `16`
- finite tail records: `5`
- loop tail records: `5`
- probe campaign jobs: `26`
- nonzero coverage probe jobs: `7`
- nonzero blocker tracks without source candidate: `146`
- zero coverage probe jobs: `19`
- zero runtime reader PC targets: `10`
- zero/EF frontier candidate packs: `10`
- FD/FE frontier runtime reads: `6`
- FF review runtime reads: `10`
- residual uncertainty records: `8`
- residual public exact blocked: `2`
- release ready: `False`

## Gates

| Gate | Passed | Details |
| --- | --- | --- |
| `public_exact_duration_gate` | `False` | `{'public_exact_duration_track_count': 21, 'track_count': 192, 'blocking_track_count': 171}` |
| `finite_ending_tail_gate` | `False` | `{'records': 5, 'tail_classification_counts': {'active_through_render_boundary': 3, 'post_candidate_tail_nonzero': 2}, 'active_through_render_boundary_count': 3, 'nonzero_after_candidate_end_count': 5}` |
| `loop_point_tail_gate` | `False` | `{'records': 5, 'tail_classification_counts': {'active_through_diagnostic_render_boundary': 5}, 'missing_exact_loop_field_count': 20, 'active_through_render_boundary_count': 5}` |
| `near_oracle_gate` | `True` | `{'status_counts': {'audio_equivalent_state_delta': 190}}` |
| `independent_oracle_gate` | `False` | `{'independent_capture_count': 0, 'missing_independent_capture_count': 190, 'representative_campaign_job_count': 16, 'representative_missing_independent_capture_count': 16}` |
| `sequence_promotion_gate` | `False` | `{'uncertainty_register_allows_sequence_promotion': False, 'probe_campaign_allows_sequence_promotion': False}` |
| `nonzero_control_coverage_gate` | `False` | `{'blocker_track_count': 155, 'probe_job_count': 7, 'source_candidate_record_count': 56, 'unique_source_candidate_track_count': 10, 'blocker_tracks_without_source_candidate_count': 146}` |
| `zero_runtime_coverage_gate` | `False` | `{'blocker_track_count': 19, 'probe_job_count': 19, 'job_track_coverage_exact': True, 'reader_pc_target_count': 10, 'runtime_zero_read_count': 5931, 'pre_promotion_blocker_counts': {'ef_return_stack_model': 15, 'zero_runtime_effect_proof': 19}}` |
| `residual_uncertainty_coverage_gate` | `False` | `{'record_count': 8, 'public_exact_allowed_count': 6, 'public_exact_blocked_count': 2, 'pcm_trim_sequence_intent_open_count': 5, 'primary_uncertainty_counts': {'active_preview_classification_pending': 1, 'measurement_missing': 1, 'no_duration_uncertainty_for_current_export': 1, 'pcm_trim_usable_sequence_intent_open': 5}}` |

## Blocker Lanes

| Lane | Blocking count | Current contract | Next action |
| --- | ---: | --- | --- |
| `non_zero_control_semantics` | 155 | `audio-probe-campaign-plan` | run/import nonzero control probe evidence and refresh duration uncertainty |
| `zero_runtime_probe` | 19 | `audio-zero-runtime-probe-plan` | run/import 0x00 runtime probe evidence and refresh duration uncertainty |
| `finite_transition_review` | 5 | `audio-finite-ending-tail-metrics` | classify true finite endings versus transition/stinger policy |
| `loop_point_metadata` | 5 | `audio-loop-point-tail-metrics` | collect exact loop points or held-policy/no-exact-loop classification |
| `independent_oracle` | 190 | `audio-independent-oracle-campaign-plan` | import external emulator reference captures for representative campaign first |

## Decision Policy

- This rollup is diagnostic only and does not promote sequence-derived durations or exact loop exports.
- Near-oracle equivalence is treated separately from independent external-emulator capture.
- Independent oracle coverage records the representative campaign gap before all-track capture expansion.
- Finite and loop tail metrics prove current diagnostic activity patterns, not final exact-duration policy.
- Nonzero control coverage maps representative probe anchors but does not replace imported runtime probe outputs.
- Zero runtime coverage maps every current zero blocker to a probe job but still requires imported runtime classifications.
- Residual uncertainty coverage keeps PCM-trim public readiness separate from sequence-intent promotion.
- Source-backed zero/EF, FD/FE, and FF frontiers identify proof targets but do not promote exact duration.
- Release-quality exact-duration readiness requires public exact duration coverage plus independent oracle and lane-specific runtime evidence.

## Remaining Uncertainty

- Non-zero control semantics remains the largest track-level exact-duration blocker.
- Independent external-emulator capture remains the release-quality oracle blocker.
- Finite and loop tail metrics are now normalized evidence, but neither lane is promotion-ready without runtime classification.
