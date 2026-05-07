# Audio Duration Next Actions Plan

Status: next evidence actions are ranked; current playback/export behavior is preserved.

## Summary

- priority lanes: `7`
- release ready: `False`
- blocking tracks: `171`
- independent representative jobs: `16`
- nonzero control probe jobs: `7`
- zero runtime probe jobs: `19`
- finite-transition tracks: `5`
- loop-point tracks: `5`
- residual public-exact blockers: `2`
- PCM-trim sequence-intent tracks: `5`

## Priority Lanes

| Rank | Lane | Status | Why first | Counts |
| ---: | --- | --- | --- | --- |
| 1 | `independent_oracle_representative_capture` | `external_captures_missing` | Release-quality playback claims are blocked even though the all-track near-oracle gate is green; the representative external-emulator campaign is the smallest independent comparison set. | `{'representative_job_count': 16, 'representative_missing_independent_capture_count': 16, 'all_track_missing_independent_capture_count': 190}` |
| 2 | `nonzero_control_probe_import` | `probe_outputs_missing` | Nonzero control semantics are the largest track-count blocker; the seven probe jobs are the highest-leverage way to reduce the 155-track uncertainty lane. | `{'blocker_track_count': 155, 'probe_job_count': 7, 'source_candidate_record_count': 56, 'blocker_tracks_without_source_candidate_count': 146}` |
| 3 | `zero_runtime_probe_import` | `probe_outputs_missing` | The 0x00 lane has exact one-job-per-track coverage, so it can produce clean finite/loop/preview follow-up buckets once runtime effect proofs are imported. | `{'blocker_track_count': 19, 'probe_job_count': 19, 'reader_pc_target_count': 10, 'runtime_zero_read_count': 5931}` |
| 4 | `finite_transition_tail_classification` | `runtime_tail_classification_pending` | Five candidate finite ends all have nonzero PCM after the candidate end; three remain active through the diagnostic render boundary and need transition/stinger evidence before exact finite export. | `{'track_count': 5, 'nonzero_after_candidate_end_count': 5, 'active_through_render_boundary_count': 3}` |
| 5 | `loop_point_or_hold_classification` | `exact_loop_metadata_missing` | All five loop/held candidates are active through the diagnostic render boundary, but exact intro/start/end loop fields are still placeholders. | `{'track_count': 5, 'active_through_render_boundary_count': 5, 'missing_exact_loop_field_count': 20}` |
| 6 | `residual_public_exact_blockers` | `two_public_exact_blockers_remaining` | The residual lane isolates the only public-exact blockers not already covered by control, finite-tail, loop-tail, or oracle campaign work. | `{'record_count': 8, 'public_exact_blocked_count': 2}` |
| 7 | `pcm_trim_sequence_intent_review` | `semantic_promotion_open_public_exact_ready` | Five PCM-trim tracks are already public-exact ready from PCM evidence; reviewing sequence intent prevents those usable exports from being confused with sequence-derived semantic promotion. | `{'pcm_trim_sequence_intent_open_count': 5, 'public_exact_allowed_count': 6}` |

## Post-Completion Validation

- `python tools/build_audio_duration_readiness_rollup.py`
- `python tools/validate_audio_duration_readiness_rollup.py`
- `python tools/build_audio_duration_next_actions_plan.py`
- `python tools/validate_audio_duration_next_actions_plan.py`
- `python tools/build_audio_oracle_source_regeneration_plan.py`
- `python tools/validate_audio_oracle_source_regeneration_plan.py`
- `python tools/validate_audio_export_plan.py`
- `python tools/validate_audio_duration_uncertainty_register.py`
- `python tools/validate_audio_oracle_verification_report.py manifests/audio-oracle-verification-report-all-tracks.json --require-representative-pass`
- `git diff --check`

## Decision Policy

- This plan ranks evidence collection and validation only; it does not change playback or export behavior.
- Promotion remains blocked in every lane until source reports are refreshed by imported evidence.
- Independent external-emulator captures are the first release-quality comparison gate even though near-oracle equivalence passes.
- Nonzero and zero probe outputs must be collected under ignored build/audio paths before they can affect duration uncertainty.
- Finite and loop candidates need runtime/oracle classification before exact-duration or exact-loop public export claims.
- Residual public-exact blockers are tracked separately from PCM-trim tracks that are already usable by PCM evidence.

## Remaining Uncertainty

- Independent external-emulator representative captures remain missing for all 16 queued jobs.
- Nonzero control semantics remain the largest track-count blocker: 155 tracks, with seven representative probe jobs.
- Zero runtime semantics have exact blocker coverage: 19 tracks and 19 probe jobs.
- Five finite-transition candidates and five loop/held candidates still need runtime/oracle classification.
- `NONE` and `WHAT_THE_HECK` remain the residual public-exact blockers.
- Five PCM-trim tracks are public-exact ready from PCM evidence, but sequence-intent promotion remains open.
