# Audio Independent Oracle Handoff Matrix

Status: representative external-emulator captures are ready for operator handoff; current playback/export behavior is preserved.

## Summary

- handoff jobs: `16`
- ready captures: `0`
- pending captures: `16`
- missing capture metadata: `16`
- all-track missing independent captures: `190`
- near-oracle pass count: `190`
- phase counts: `{'independent-duration-uncertainty-coverage': 4, 'independent-probe-source-coverage': 5, 'independent-representative-core': 7}`
- uncertainty counts: `{'active_preview_classification_pending': 1, 'finite_transition_review_pending': 2, 'loop_point_metadata_pending': 2, 'non_zero_control_semantics_pending': 3, 'pcm_trim_usable_sequence_intent_open': 2, 'zero_runtime_probe_pending': 6}`
- duration buckets: `{'diagnostic_30s': 7, 'long_preview_120s': 2, 'short_finite_candidate': 7}`
- accepted oracles: `['mesen2', 'bsnes_higan', 'mednafen']`
- independent emulator gate passed: `False`
- release-quality playback claim ready: `False`

## Phase Batches

| Phase | Jobs | Tracks |
| --- | ---: | --- |
| `independent-representative-core` | 7 | `[1, 17, 32, 46, 171, 173, 175]` |
| `independent-duration-uncertainty-coverage` | 4 | `[10, 8, 5, 12]` |
| `independent-probe-source-coverage` | 5 | `[25, 115, 123, 135, 161]` |

## Duration Batches

| Duration bucket | Jobs | Tracks |
| --- | ---: | --- |
| `diagnostic_30s` | 7 | `[1, 17, 46, 171, 173, 10, 25]` |
| `short_finite_candidate` | 7 | `[32, 175, 8, 12, 123, 135, 161]` |
| `long_preview_120s` | 2 | `[5, 115]` |

## Handoff Jobs

| Order | Track | Name | Phase | Primary uncertainty | Planned seconds | Audit status | Blocking reason |
| ---: | ---: | --- | --- | --- | ---: | --- | --- |
| 1 | 001 | `GAS_STATION` | `independent-representative-core` | `zero_runtime_probe_pending` | `30.0` | `pending_independent_capture` | `['missing_capture_metadata']` |
| 2 | 017 | `MONOTOLI_BUILDING` | `independent-representative-core` | `non_zero_control_semantics_pending` | `30.0` | `pending_independent_capture` | `['missing_capture_metadata']` |
| 3 | 032 | `GIANT_STEP` | `independent-representative-core` | `zero_runtime_probe_pending` | `21.003219` | `pending_independent_capture` | `['missing_capture_metadata']` |
| 4 | 046 | `ONETT` | `independent-representative-core` | `non_zero_control_semantics_pending` | `30.0` | `pending_independent_capture` | `['missing_capture_metadata']` |
| 5 | 171 | `WINTERS_INTRO` | `independent-representative-core` | `zero_runtime_probe_pending` | `30.0` | `pending_independent_capture` | `['missing_capture_metadata']` |
| 6 | 173 | `GOOD_MORNING_MOONSIDE` | `independent-representative-core` | `zero_runtime_probe_pending` | `30.0` | `pending_independent_capture` | `['missing_capture_metadata']` |
| 7 | 175 | `TITLE_SCREEN` | `independent-representative-core` | `zero_runtime_probe_pending` | `13.774594` | `pending_independent_capture` | `['missing_capture_metadata']` |
| 8 | 010 | `WHAT_THE_HECK` | `independent-duration-uncertainty-coverage` | `active_preview_classification_pending` | `30.0` | `pending_independent_capture` | `['missing_capture_metadata']` |
| 9 | 008 | `BATTLE_SWIRL1` | `independent-duration-uncertainty-coverage` | `finite_transition_review_pending` | `4.036187` | `pending_independent_capture` | `['missing_capture_metadata']` |
| 10 | 005 | `YOU_WON1` | `independent-duration-uncertainty-coverage` | `loop_point_metadata_pending` | `120.0` | `pending_independent_capture` | `['missing_capture_metadata']` |
| 11 | 012 | `YOU_WON2` | `independent-duration-uncertainty-coverage` | `pcm_trim_usable_sequence_intent_open` | `3.390938` | `pending_independent_capture` | `['missing_capture_metadata']` |
| 12 | 025 | `CHAOS_THEATRE` | `independent-probe-source-coverage` | `zero_runtime_probe_pending` | `30.0` | `pending_independent_capture` | `['missing_capture_metadata']` |
| 13 | 115 | `PHONE_CALL` | `independent-probe-source-coverage` | `loop_point_metadata_pending` | `120.0` | `pending_independent_capture` | `['missing_capture_metadata']` |
| 14 | 123 | `SOMEONE_JOINS` | `independent-probe-source-coverage` | `finite_transition_review_pending` | `2.624125` | `pending_independent_capture` | `['missing_capture_metadata']` |
| 15 | 135 | `TELEPORT_IN` | `independent-probe-source-coverage` | `pcm_trim_usable_sequence_intent_open` | `4.744781` | `pending_independent_capture` | `['missing_capture_metadata']` |
| 16 | 161 | `SOUNDSTONE_RECORDING_LILLIPUT_STEPS` | `independent-probe-source-coverage` | `non_zero_control_semantics_pending` | `3.840281` | `pending_independent_capture` | `['missing_capture_metadata']` |

## Validation After Imports

- `python tools/build_audio_independent_oracle_handoff_matrix.py`
- `python tools/validate_audio_independent_oracle_handoff_matrix.py`
- `python tools/build_audio_oracle_source_evidence_preflight.py`
- `python tools/validate_audio_oracle_source_evidence_preflight.py`
- `python tools/run_audio_independent_oracle_campaign.py --mode audit-existing-captures`
- `python tools/validate_audio_independent_oracle_campaign_run_summary.py`
- `python tools/validate_audio_independent_oracle_capture_packet.py`
- `python tools/validate_audio_independent_oracle_coverage_report.py`
- `python tools/collect_audio_oracle_comparison_results.py --plan manifests/audio-oracle-comparison-plan-all-tracks.json --summary build/audio/oracle-comparison-all-tracks/oracle-comparison-summary.json`
- `python tools/validate_audio_oracle_comparison_summary.py build/audio/oracle-comparison-all-tracks/oracle-comparison-summary.json --require-compared`
- `python tools/build_audio_oracle_verification_report.py --summary build/audio/oracle-comparison-all-tracks/oracle-comparison-summary.json --json manifests/audio-oracle-verification-report-all-tracks.json --markdown notes/audio-oracle-verification-report-all-tracks.md`
- `python tools/validate_audio_oracle_verification_report.py manifests/audio-oracle-verification-report-all-tracks.json --require-representative-pass`
- `python tools/build_audio_duration_readiness_rollup.py`
- `python tools/validate_audio_duration_readiness_rollup.py`

## Handoff Policy

- This matrix is an external-capture handoff and audit artifact; it does not run an emulator.
- Every listed capture is still pending because committed evidence has no independent capture metadata.
- Imported captures must remain under ignored build/audio paths and pass per-track reference validation.
- The ares near-oracle gate remains green, but release-quality playback remains blocked until the independent emulator gate passes.
- This matrix cannot promote exact durations, loop metadata, sequence semantics, or playback/export behavior.

## Remaining Uncertainty

- All 16 representative independent captures are still pending external SPC/WAV inputs.
- The all-track near-oracle gate remains green, but it is not independent external-emulator evidence.
- Release-quality playback remains blocked until imported captures refresh the independent emulator gate.
