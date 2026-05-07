# Audio Finite Ending Evidence Plan

Status: finite-ending evidence plan is ready; current review-needed export behavior remains unchanged.

## Summary

- jobs: `5`
- tracks: `['BATTLE_SWIRL1', 'BATTLE_SWIRL2', 'NEW_FRIEND', 'SOMEONE_JOINS', 'BATTLE_SWIRL4']`
- export classes: `{'finite_or_transition_review_candidate': 5}`
- recommended modes: `{'trim_candidate_after_manual_or_sequence_review': 5}`
- diagnostic focus counts: `{'active_through_preview_or_loop_candidate': 2, 'finite_tail_or_transition_end': 2, 'general_playback_equivalence': 1}`
- finite gap statuses: `{'finite_tail_review_pending': 5}`
- nonzero after candidate end: `5`
- promotion allowed by plan: `False`
- public exact finite export ready: `False`

## Decision Policy

- Current playback/export behavior stays review-needed trim candidate until tail evidence is explicit.
- Trailing PCM silence measurement alone does not promote these tracks to public exact finite exports.
- A true finite ending requires candidate-end sample evidence plus post-boundary silence/idle state.
- A transition/stinger classification is valid evidence only if public exact finite export remains blocked or gets a separate policy.

## Jobs

| Order | Track | Name | Oracle focus | Evidence status | Candidate end frame | Last nonzero frame | Tail seconds | Nonzero after end |
| ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `008` | `BATTLE_SWIRL1` | `finite_tail_or_transition_end` | `finite_tail_review_pending` | `129158` | `140984` | `0.369563` | `True` |
| 2 | `009` | `BATTLE_SWIRL2` | `general_playback_equivalence` | `finite_tail_review_pending` | `131027` | `959997` | `25.905313` | `True` |
| 3 | `011` | `NEW_FRIEND` | `active_through_preview_or_loop_candidate` | `finite_tail_review_pending` | `253126` | `959999` | `22.089781` | `True` |
| 4 | `123` | `SOMEONE_JOINS` | `finite_tail_or_transition_end` | `finite_tail_review_pending` | `83972` | `113116` | `0.91075` | `True` |
| 5 | `176` | `BATTLE_SWIRL4` | `active_through_preview_or_loop_candidate` | `finite_tail_review_pending` | `170468` | `959999` | `24.672844` | `True` |

## Accepted Evidence Statuses

- `true_finite_end`
- `transition_or_stinger_policy`
- `unresolved_finite_boundary`

## Post Evidence Validation

- `python tools/run_audio_finite_ending_evidence_plan.py --mode audit-current-export`
- `python tools/validate_audio_finite_ending_evidence_run_summary.py`
- `python tools/validate_audio_finite_ending_evidence_plan.py`
- `python tools/validate_audio_export_plan.py`
- `python tools/validate_audio_duration_uncertainty_register.py`

## Remaining Uncertainty

- The five tracks still need explicit true-ending versus transition/stinger classification.
- Current diagnostic render metrics show nonzero PCM after the candidate finite end for every selected track.
- Public exact finite export remains blocked until runtime/oracle tail evidence is imported and validated.
