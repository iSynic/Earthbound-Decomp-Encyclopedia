# Audio Finite-Transition Classification Packet

Status: finite-transition candidates are packaged for runtime/oracle tail classification; current playback/export behavior is preserved.

## Summary

- packet jobs: `5`
- tracks: `[8, 9, 11, 123, 176]`
- tail classifications: `{'active_through_render_boundary': 3, 'post_candidate_tail_nonzero': 2}`
- nonzero after candidate end: `5`
- active through render boundary: `3`
- pending evidence: `5`
- ready evidence: `0`
- blocking reasons: `{'finite_tail_review_pending': 5, 'missing_explicit_tail_classification': 5, 'nonzero_pcm_after_candidate_end': 5, 'public_exact_export_blocked': 5, 'sequence_semantics_required': 5}`
- accepted evidence statuses: `['true_finite_end', 'transition_or_stinger_policy', 'unresolved_finite_boundary']`

## Tail Batches

| Tail classification | Jobs | Tracks |
| --- | ---: | --- |
| `post_candidate_tail_nonzero` | 2 | `[8, 123]` |
| `active_through_render_boundary` | 3 | `[9, 11, 176]` |

## Classification Jobs

| Order | Track | Name | Tail classification | Tail seconds | Silent frames at render end | Audit status |
| ---: | ---: | --- | --- | ---: | ---: | --- |
| 1 | 008 | `BATTLE_SWIRL1` | `post_candidate_tail_nonzero` | 0.369563 | 819015 | `pending_finite_ending_evidence` |
| 2 | 009 | `BATTLE_SWIRL2` | `active_through_render_boundary` | 25.905313 | 2 | `pending_finite_ending_evidence` |
| 3 | 011 | `NEW_FRIEND` | `active_through_render_boundary` | 22.089781 | 0 | `pending_finite_ending_evidence` |
| 4 | 123 | `SOMEONE_JOINS` | `post_candidate_tail_nonzero` | 0.91075 | 846883 | `pending_finite_ending_evidence` |
| 5 | 176 | `BATTLE_SWIRL4` | `active_through_render_boundary` | 24.672844 | 0 | `pending_finite_ending_evidence` |

## Validation After Evidence

- `python tools/validate_audio_finite_transition_classification_packet.py`
- `python tools/run_audio_finite_ending_evidence_plan.py --mode audit-current-export`
- `python tools/validate_audio_finite_ending_evidence_run_summary.py`
- `python tools/build_audio_finite_ending_tail_metrics.py`
- `python tools/validate_audio_finite_ending_tail_metrics.py`
- `python tools/validate_audio_finite_ending_evidence_plan.py`
- `python tools/validate_audio_export_plan.py`
- `python tools/validate_audio_duration_uncertainty_register.py`
- `python tools/build_audio_duration_readiness_rollup.py`
- `python tools/validate_audio_duration_readiness_rollup.py`

## Classification Policy

- This packet is diagnostic only and preserves current playback/export behavior.
- Post-candidate PCM activity blocks public exact finite export until explicit runtime/oracle classification is imported.
- Tracks active through the diagnostic render boundary need stronger evidence than candidate-end timing alone.
- Shorter post-candidate tails still need transition/stinger versus true-release classification.
- A transition_or_stinger_policy classification can be valid while still keeping public exact finite export blocked.
- Sequence command promotion remains blocked until separate zero/nonzero control evidence is consumed.

## Remaining Uncertainty

- All five candidate finite endings still need explicit runtime/oracle classification.
- Three tracks are active through the 30-second diagnostic render boundary.
- Two tracks have shorter post-candidate nonzero tails but still need transition/stinger versus true-release evidence.
