# Audio Oracle Source Evidence Preflight

Status: oracle comparison collection is blocked in this workspace by missing ignored source/reference artifacts; playback/export behavior is preserved.

## Summary

- jobs: `190`
- collector-ready jobs: `0`
- missing-source blocked jobs: `190`
- source SPC present: `0`
- source render WAV present: `0`
- reference SPC present: `0`
- reference WAV present: `0`
- capture metadata present: `0`
- comparison results present: `0`
- representative jobs: `16`
- blocking reasons: `{'missing_capture_metadata': 190, 'missing_comparison_result': 190, 'missing_reference_spc': 190, 'missing_reference_wav': 190, 'missing_source_render_wav': 190, 'missing_source_spc': 190}`
- near-oracle gates: representative `True`, all-track `True`
- independent gate passed: `False`

## Collector Status Batches

| Status | Jobs | First tracks |
| --- | ---: | --- |
| `collector_blocked_missing_source_evidence` | 190 | `[1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]` |

## Representative Handoff Tracks

| Track | Name | Phase | Primary uncertainty | Collector status |
| ---: | --- | --- | --- | --- |
| 001 | `GAS_STATION` | `independent-representative-core` | `zero_runtime_probe_pending` | `collector_blocked_missing_source_evidence` |
| 005 | `YOU_WON1` | `independent-duration-uncertainty-coverage` | `loop_point_metadata_pending` | `collector_blocked_missing_source_evidence` |
| 008 | `BATTLE_SWIRL1` | `independent-duration-uncertainty-coverage` | `finite_transition_review_pending` | `collector_blocked_missing_source_evidence` |
| 010 | `WHAT_THE_HECK` | `independent-duration-uncertainty-coverage` | `active_preview_classification_pending` | `collector_blocked_missing_source_evidence` |
| 012 | `YOU_WON2` | `independent-duration-uncertainty-coverage` | `pcm_trim_usable_sequence_intent_open` | `collector_blocked_missing_source_evidence` |
| 017 | `MONOTOLI_BUILDING` | `independent-representative-core` | `non_zero_control_semantics_pending` | `collector_blocked_missing_source_evidence` |
| 025 | `CHAOS_THEATRE` | `independent-probe-source-coverage` | `zero_runtime_probe_pending` | `collector_blocked_missing_source_evidence` |
| 032 | `GIANT_STEP` | `independent-representative-core` | `zero_runtime_probe_pending` | `collector_blocked_missing_source_evidence` |
| 046 | `ONETT` | `independent-representative-core` | `non_zero_control_semantics_pending` | `collector_blocked_missing_source_evidence` |
| 115 | `PHONE_CALL` | `independent-probe-source-coverage` | `loop_point_metadata_pending` | `collector_blocked_missing_source_evidence` |
| 123 | `SOMEONE_JOINS` | `independent-probe-source-coverage` | `finite_transition_review_pending` | `collector_blocked_missing_source_evidence` |
| 135 | `TELEPORT_IN` | `independent-probe-source-coverage` | `pcm_trim_usable_sequence_intent_open` | `collector_blocked_missing_source_evidence` |
| 161 | `SOUNDSTONE_RECORDING_LILLIPUT_STEPS` | `independent-probe-source-coverage` | `non_zero_control_semantics_pending` | `collector_blocked_missing_source_evidence` |
| 171 | `WINTERS_INTRO` | `independent-representative-core` | `zero_runtime_probe_pending` | `collector_blocked_missing_source_evidence` |
| 173 | `GOOD_MORNING_MOONSIDE` | `independent-representative-core` | `zero_runtime_probe_pending` | `collector_blocked_missing_source_evidence` |
| 175 | `TITLE_SCREEN` | `independent-representative-core` | `zero_runtime_probe_pending` | `collector_blocked_missing_source_evidence` |

## Validation

- `python tools/build_audio_oracle_source_evidence_preflight.py`
- `python tools/validate_audio_oracle_source_evidence_preflight.py`
- `python tools/validate_audio_oracle_comparison_plan.py manifests/audio-oracle-comparison-plan-all-tracks.json --allow-missing-source-outputs`
- `python tools/validate_audio_oracle_verification_report.py manifests/audio-oracle-verification-report-all-tracks.json --require-representative-pass`
- `python tools/validate_audio_independent_oracle_handoff_matrix.py`
- `python tools/validate_audio_independent_oracle_capture_packet.py`
- `python tools/build_audio_oracle_source_regeneration_plan.py`
- `python tools/validate_audio_oracle_source_regeneration_plan.py`

## Preflight Policy

- This report audits local ignored oracle evidence paths only; it does not collect or compare audio.
- Source SPC/WAV artifacts and external reference SPC/WAV artifacts are generated evidence under build/audio.
- The all-track verification report can remain green while this collector preflight is blocked in a clean workspace.
- Run source render/capture generation before collecting oracle comparison summaries from this plan.
- This preflight cannot promote playback, exact durations, loop metadata, or release-quality claims.

## Remaining Uncertainty

- The committed all-track oracle report remains green from existing verification evidence.
- The local collect-summary path needs regenerated source SPC/WAV evidence before it can validate in this workspace.
- Independent emulator release-quality evidence still requires the 16 representative external captures.
