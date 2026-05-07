# Audio Independent Oracle Capture Packet

Status: representative independent-emulator capture jobs are packaged for external inputs; current playback/export behavior is preserved.

## Summary

- packet jobs: `16`
- missing representative captures: `16`
- all-track missing independent captures: `190`
- near-oracle pass count: `190`
- phases: `{'independent-duration-uncertainty-coverage': 4, 'independent-probe-source-coverage': 5, 'independent-representative-core': 7}`
- uncertainty counts: `{'active_preview_classification_pending': 1, 'finite_transition_review_pending': 2, 'loop_point_metadata_pending': 2, 'non_zero_control_semantics_pending': 3, 'pcm_trim_usable_sequence_intent_open': 2, 'zero_runtime_probe_pending': 6}`
- accepted oracles: `['mesen2', 'bsnes_higan', 'mednafen']`
- WAV policy: `32000 Hz`, `2` channels, `16` bits, at least `30.0` seconds
- release-quality playback claim ready: `False`

## Phase Batches

| Phase | Jobs | Tracks |
| --- | ---: | --- |
| `independent-representative-core` | 7 | `[1, 17, 32, 46, 171, 173, 175]` |
| `independent-duration-uncertainty-coverage` | 4 | `[10, 8, 5, 12]` |
| `independent-probe-source-coverage` | 5 | `[25, 115, 123, 135, 161]` |

## Capture Jobs

| Order | Track | Name | Phase | Primary uncertainty | Planned seconds | Metadata output |
| ---: | ---: | --- | --- | --- | ---: | --- |
| 1 | 001 | `GAS_STATION` | `independent-representative-core` | `zero_runtime_probe_pending` | `30.0` | `build/audio/oracle-comparison-all-tracks/track-001-gas_station/reference-capture.json` |
| 2 | 017 | `MONOTOLI_BUILDING` | `independent-representative-core` | `non_zero_control_semantics_pending` | `30.0` | `build/audio/oracle-comparison-all-tracks/track-017-monotoli_building/reference-capture.json` |
| 3 | 032 | `GIANT_STEP` | `independent-representative-core` | `zero_runtime_probe_pending` | `21.003219` | `build/audio/oracle-comparison-all-tracks/track-032-giant_step/reference-capture.json` |
| 4 | 046 | `ONETT` | `independent-representative-core` | `non_zero_control_semantics_pending` | `30.0` | `build/audio/oracle-comparison-all-tracks/track-046-onett/reference-capture.json` |
| 5 | 171 | `WINTERS_INTRO` | `independent-representative-core` | `zero_runtime_probe_pending` | `30.0` | `build/audio/oracle-comparison-all-tracks/track-171-winters_intro/reference-capture.json` |
| 6 | 173 | `GOOD_MORNING_MOONSIDE` | `independent-representative-core` | `zero_runtime_probe_pending` | `30.0` | `build/audio/oracle-comparison-all-tracks/track-173-good_morning_moonside/reference-capture.json` |
| 7 | 175 | `TITLE_SCREEN` | `independent-representative-core` | `zero_runtime_probe_pending` | `13.774594` | `build/audio/oracle-comparison-all-tracks/track-175-title_screen/reference-capture.json` |
| 8 | 010 | `WHAT_THE_HECK` | `independent-duration-uncertainty-coverage` | `active_preview_classification_pending` | `30.0` | `build/audio/oracle-comparison-all-tracks/track-010-what_the_heck/reference-capture.json` |
| 9 | 008 | `BATTLE_SWIRL1` | `independent-duration-uncertainty-coverage` | `finite_transition_review_pending` | `4.036187` | `build/audio/oracle-comparison-all-tracks/track-008-battle_swirl1/reference-capture.json` |
| 10 | 005 | `YOU_WON1` | `independent-duration-uncertainty-coverage` | `loop_point_metadata_pending` | `120.0` | `build/audio/oracle-comparison-all-tracks/track-005-you_won1/reference-capture.json` |
| 11 | 012 | `YOU_WON2` | `independent-duration-uncertainty-coverage` | `pcm_trim_usable_sequence_intent_open` | `3.390938` | `build/audio/oracle-comparison-all-tracks/track-012-you_won2/reference-capture.json` |
| 12 | 025 | `CHAOS_THEATRE` | `independent-probe-source-coverage` | `zero_runtime_probe_pending` | `30.0` | `build/audio/oracle-comparison-all-tracks/track-025-chaos_theatre/reference-capture.json` |
| 13 | 115 | `PHONE_CALL` | `independent-probe-source-coverage` | `loop_point_metadata_pending` | `120.0` | `build/audio/oracle-comparison-all-tracks/track-115-phone_call/reference-capture.json` |
| 14 | 123 | `SOMEONE_JOINS` | `independent-probe-source-coverage` | `finite_transition_review_pending` | `2.624125` | `build/audio/oracle-comparison-all-tracks/track-123-someone_joins/reference-capture.json` |
| 15 | 135 | `TELEPORT_IN` | `independent-probe-source-coverage` | `pcm_trim_usable_sequence_intent_open` | `4.744781` | `build/audio/oracle-comparison-all-tracks/track-135-teleport_in/reference-capture.json` |
| 16 | 161 | `SOUNDSTONE_RECORDING_LILLIPUT_STEPS` | `independent-probe-source-coverage` | `non_zero_control_semantics_pending` | `3.840281` | `build/audio/oracle-comparison-all-tracks/track-161-soundstone_recording_lilliput_steps/reference-capture.json` |

## Validation After Imports

- `python tools/validate_audio_independent_oracle_capture_packet.py`
- `python tools/build_audio_independent_oracle_handoff_matrix.py`
- `python tools/validate_audio_independent_oracle_handoff_matrix.py`
- `python tools/build_audio_oracle_source_evidence_preflight.py`
- `python tools/validate_audio_oracle_source_evidence_preflight.py`
- `python tools/run_audio_independent_oracle_campaign.py --mode audit-existing-captures`
- `python tools/validate_audio_independent_oracle_campaign_run_summary.py`
- `python tools/collect_audio_oracle_comparison_results.py --plan manifests/audio-oracle-comparison-plan-all-tracks.json --summary build/audio/oracle-comparison-all-tracks/oracle-comparison-summary.json`
- `python tools/validate_audio_oracle_comparison_summary.py build/audio/oracle-comparison-all-tracks/oracle-comparison-summary.json --require-compared`
- `python tools/build_audio_oracle_verification_report.py --summary build/audio/oracle-comparison-all-tracks/oracle-comparison-summary.json --json manifests/audio-oracle-verification-report-all-tracks.json --markdown notes/audio-oracle-verification-report-all-tracks.md`
- `python tools/validate_audio_oracle_verification_report.py manifests/audio-oracle-verification-report-all-tracks.json --require-representative-pass`
- `python tools/build_audio_independent_oracle_coverage_report.py`
- `python tools/validate_audio_independent_oracle_coverage_report.py`
- `python tools/build_audio_duration_readiness_rollup.py`
- `python tools/validate_audio_duration_readiness_rollup.py`

## Capture Packet Policy

- This packet is an operator checklist for external independent-emulator captures; it does not run an emulator.
- External SPC/WAV capture artifacts are generated evidence and must stay under ignored build/audio paths.
- Each imported capture must identify mesen2, bsnes/higan, or mednafen and set independent_emulator_capture=true.
- The importer must preserve planned source_spc.sha1 in capture metadata before comparison results are collected.
- Any mismatch must be explained before release-quality playback can be claimed.
- This packet cannot promote exact durations, sequence semantics, or public loop metadata by itself.

## Remaining Uncertainty

- All 16 representative captures still require external independent-emulator SPC/WAV inputs.
- All imported captures must pass per-track reference capture validation before comparison summaries are refreshed.
- Release-quality playback remains blocked until the independent emulator gate passes after report refresh.
