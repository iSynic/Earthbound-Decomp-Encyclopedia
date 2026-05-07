# Audio Loop/Hold Classification Packet

Status: loop/held candidates are packaged for exact loop-point or held-policy classification; current playback/export behavior is preserved.

## Summary

- packet jobs: `5`
- tracks: `[5, 6, 115, 183, 184]`
- tail classifications: `{'active_through_diagnostic_render_boundary': 5}`
- diagnostic focus counts: `{'active_through_preview_or_loop_candidate': 4, 'general_playback_equivalence': 1}`
- primary sample pack counts: `{'5': 5}`
- missing exact loop fields: `20`
- active through render boundary: `5`
- pending evidence: `5`
- ready evidence: `0`
- blocking reasons: `{'held_or_sample_loop_policy_unresolved': 5, 'missing_intro_samples': 5, 'missing_loop_end_sample': 5, 'missing_loop_start_sample': 5, 'missing_measured_by': 5, 'placeholder_loop_points_pending': 5}`
- accepted evidence statuses: `['exact_loop_points_available', 'held_policy_no_exact_loop_points', 'unresolved_loop_or_hold_policy']`

## Diagnostic Batches

| Diagnostic focus | Jobs | Tracks |
| --- | ---: | --- |
| `active_through_preview_or_loop_candidate` | 4 | `[5, 6, 183, 184]` |
| `general_playback_equivalence` | 1 | `[115]` |

## Classification Jobs

| Order | Track | Name | Diagnostic focus | Last nonzero frame | Silent frames at render end | Audit status |
| ---: | ---: | --- | --- | ---: | ---: | --- |
| 1 | 005 | `YOU_WON1` | `active_through_preview_or_loop_candidate` | 959999 | 0 | `pending_loop_evidence` |
| 2 | 006 | `LEVEL_UP` | `active_through_preview_or_loop_candidate` | 959999 | 0 | `pending_loop_evidence` |
| 3 | 115 | `PHONE_CALL` | `general_playback_equivalence` | 959998 | 1 | `pending_loop_evidence` |
| 4 | 183 | `SUDDEN_VICTORY` | `active_through_preview_or_loop_candidate` | 959999 | 0 | `pending_loop_evidence` |
| 5 | 184 | `YOU_WON3` | `active_through_preview_or_loop_candidate` | 959999 | 0 | `pending_loop_evidence` |

## Validation After Evidence

- `python tools/validate_audio_loop_hold_classification_packet.py`
- `python tools/run_audio_loop_point_evidence_plan.py --mode audit-current-export`
- `python tools/validate_audio_loop_point_evidence_run_summary.py`
- `python tools/build_audio_loop_point_tail_metrics.py`
- `python tools/validate_audio_loop_point_tail_metrics.py`
- `python tools/validate_audio_loop_point_evidence_plan.py`
- `python tools/validate_audio_export_plan.py`
- `python tools/validate_audio_duration_uncertainty_register.py`
- `python tools/build_audio_duration_readiness_rollup.py`
- `python tools/validate_audio_duration_readiness_rollup.py`

## Classification Policy

- This packet is diagnostic only and preserves current playback/export behavior.
- Activity through the diagnostic render boundary supports loop/held prioritization but does not prove exact loop points.
- Public loop export remains loop-count-plus-fade preview until exact loop points or a held-policy classification are validated.
- Exact loop metadata requires sample-accurate intro_samples, loop_start_sample, loop_end_sample, and measured_by evidence.
- A held_policy_no_exact_loop_points classification can be valid while still keeping public exact loop export blocked.
- Sequence command promotion remains separate from this loop/hold packet.

## Remaining Uncertainty

- All five loop/held candidates still need explicit runtime/oracle classification.
- All five are active through the 30-second diagnostic render boundary.
- Exact public loop metadata remains blocked by 20 missing intro/start/end/measured_by fields.
