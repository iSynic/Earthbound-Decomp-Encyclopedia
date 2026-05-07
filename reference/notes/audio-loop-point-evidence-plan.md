# Audio Loop Point Evidence Plan

Status: loop-point evidence plan is ready; current loop-count/fade preview behavior remains unchanged.

## Summary

- jobs: `5`
- tracks: `['LEVEL_UP', 'PHONE_CALL', 'SUDDEN_VICTORY', 'YOU_WON1', 'YOU_WON3']`
- primary sample packs: `{'5': 5}`
- no dedicated sequence pack: `5`
- diagnostic focus counts: `{'active_through_preview_or_loop_candidate': 4, 'general_playback_equivalence': 1}`
- preview policy: `2` loops plus `5.0` second fade
- promotion allowed by plan: `False`
- public exact loop export ready: `False`

## Decision Policy

- Current playback/export behavior stays loop-count-plus-fade preview until loop or hold evidence is explicit.
- These five tracks are not blocked by broad sequence-pack command promotion; they share primary sample pack 5 with no dedicated sequence pack.
- Exact loop export requires sample-accurate intro, loop start, loop end, and measured_by evidence.
- A held/SFX classification is valid evidence only if it keeps public exact loop export blocked or defines a separate held-policy export.

## Jobs

| Order | Track | Name | Primary pack | Oracle focus | Loop evidence status | Missing fields |
| ---: | ---: | --- | ---: | --- | --- | --- |
| 1 | `005` | `YOU_WON1` | `5` | `active_through_preview_or_loop_candidate` | `placeholder_only_exact_loop_points_pending` | `['intro_samples', 'loop_start_sample', 'loop_end_sample', 'measured_by']` |
| 2 | `006` | `LEVEL_UP` | `5` | `active_through_preview_or_loop_candidate` | `placeholder_only_exact_loop_points_pending` | `['intro_samples', 'loop_start_sample', 'loop_end_sample', 'measured_by']` |
| 3 | `115` | `PHONE_CALL` | `5` | `general_playback_equivalence` | `placeholder_only_exact_loop_points_pending` | `['intro_samples', 'loop_start_sample', 'loop_end_sample', 'measured_by']` |
| 4 | `183` | `SUDDEN_VICTORY` | `5` | `active_through_preview_or_loop_candidate` | `placeholder_only_exact_loop_points_pending` | `['intro_samples', 'loop_start_sample', 'loop_end_sample', 'measured_by']` |
| 5 | `184` | `YOU_WON3` | `5` | `active_through_preview_or_loop_candidate` | `placeholder_only_exact_loop_points_pending` | `['intro_samples', 'loop_start_sample', 'loop_end_sample', 'measured_by']` |

## Accepted Evidence Statuses

- `exact_loop_points_available`
- `held_policy_no_exact_loop_points`
- `unresolved_loop_or_hold_policy`

## Post Evidence Validation

- `python tools/run_audio_loop_point_evidence_plan.py --mode audit-current-export`
- `python tools/validate_audio_loop_point_evidence_run_summary.py`
- `python tools/validate_audio_loop_point_evidence_plan.py`
- `python tools/validate_audio_export_plan.py`
- `python tools/validate_audio_duration_uncertainty_register.py`
