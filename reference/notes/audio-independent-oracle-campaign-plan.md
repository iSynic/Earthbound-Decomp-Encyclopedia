# Audio Independent Oracle Campaign Plan

Status: independent external-emulator representative capture campaign is ready; current playback/export behavior remains unchanged.

## Gate State

- all-track near-oracle passed: `True`
- independent emulator gate passed: `False`
- release-quality playback claim ready: `False`
- near-oracle pass count: `190 / 190`
- independent captures: `0 / 190`
- missing independent captures: `190`
- representative campaign jobs: `16`
- representative primary uncertainty counts: `{'active_preview_classification_pending': 1, 'finite_transition_review_pending': 2, 'loop_point_metadata_pending': 2, 'non_zero_control_semantics_pending': 3, 'pcm_trim_usable_sequence_intent_open': 2, 'zero_runtime_probe_pending': 6}`
- diagnostic focus counts: `{'active_through_preview_or_loop_candidate': 9, 'finite_tail_or_transition_end': 4, 'general_playback_equivalence': 3}`

## Campaign Policy

- This plan selects a bounded representative subset for independent external-emulator capture.
- The campaign does not change playback/export behavior and cannot promote sequence-derived exact durations.
- External emulator captures are ROM-derived generated evidence and must stay under ignored build/audio paths.
- Passing this representative campaign is evidence for the independent gate; all-track independent capture remains a separate expansion decision.

## Capture Contract

- accepted oracles: `['mesen2', 'bsnes_higan', 'mednafen']`
- required importer: `tools/import_audio_oracle_reference_capture.py`
- required independent flag: `True`
- minimum metadata fields: `['oracle_id', 'oracle_kind', 'independent_emulator_capture', 'emulator_version', 'capture_command', 'audio_settings', 'source_spc_sha1', 'reference_wav_sha1', 'render_sample_rate', 'channels', 'bits_per_sample', 'duration_seconds']`

## Representative Jobs

| Order | Phase | Track | Name | Focus | Primary uncertainty | Reason |
| ---: | --- | ---: | --- | --- | --- | --- |
| 1 | `independent-representative-core` | 001 | `GAS_STATION` | `active_through_preview_or_loop_candidate` | `zero_runtime_probe_pending` | zero-runtime baseline and active-preview uncertainty anchor |
| 2 | `independent-representative-core` | 017 | `MONOTOLI_BUILDING` | `active_through_preview_or_loop_candidate` | `non_zero_control_semantics_pending` | first non-zero control-semantics source candidate |
| 3 | `independent-representative-core` | 032 | `GIANT_STEP` | `finite_tail_or_transition_end` | `zero_runtime_probe_pending` | finite/transition candidate with zero-runtime uncertainty |
| 4 | `independent-representative-core` | 046 | `ONETT` | `active_through_preview_or_loop_candidate` | `non_zero_control_semantics_pending` | long-standing ONETT renderer/oracle smoke anchor |
| 5 | `independent-representative-core` | 171 | `WINTERS_INTRO` | `active_through_preview_or_loop_candidate` | `zero_runtime_probe_pending` | loop/held preview track with zero-runtime evidence still pending |
| 6 | `independent-representative-core` | 173 | `GOOD_MORNING_MOONSIDE` | `active_through_preview_or_loop_candidate` | `zero_runtime_probe_pending` | loop/held preview track with zero-runtime evidence still pending |
| 7 | `independent-representative-core` | 175 | `TITLE_SCREEN` | `general_playback_equivalence` | `zero_runtime_probe_pending` | finite title-screen transition candidate from zero-runtime lane |
| 8 | `independent-duration-uncertainty-coverage` | 010 | `WHAT_THE_HECK` | `general_playback_equivalence` | `active_preview_classification_pending` | coverage for active_preview_classification_pending with general_playback_equivalence oracle focus |
| 9 | `independent-duration-uncertainty-coverage` | 008 | `BATTLE_SWIRL1` | `finite_tail_or_transition_end` | `finite_transition_review_pending` | coverage for finite_transition_review_pending with finite_tail_or_transition_end oracle focus |
| 10 | `independent-duration-uncertainty-coverage` | 005 | `YOU_WON1` | `active_through_preview_or_loop_candidate` | `loop_point_metadata_pending` | coverage for loop_point_metadata_pending with active_through_preview_or_loop_candidate oracle focus |
| 11 | `independent-duration-uncertainty-coverage` | 012 | `YOU_WON2` | `active_through_preview_or_loop_candidate` | `pcm_trim_usable_sequence_intent_open` | coverage for pcm_trim_usable_sequence_intent_open with active_through_preview_or_loop_candidate oracle focus |
| 12 | `independent-probe-source-coverage` | 025 | `CHAOS_THEATRE` | `active_through_preview_or_loop_candidate` | `zero_runtime_probe_pending` | coverage for zero_runtime_probe_pending with active_through_preview_or_loop_candidate oracle focus |
| 13 | `independent-probe-source-coverage` | 115 | `PHONE_CALL` | `general_playback_equivalence` | `loop_point_metadata_pending` | coverage for loop_point_metadata_pending with general_playback_equivalence oracle focus |
| 14 | `independent-probe-source-coverage` | 123 | `SOMEONE_JOINS` | `finite_tail_or_transition_end` | `finite_transition_review_pending` | coverage for finite_transition_review_pending with finite_tail_or_transition_end oracle focus |
| 15 | `independent-probe-source-coverage` | 135 | `TELEPORT_IN` | `active_through_preview_or_loop_candidate` | `pcm_trim_usable_sequence_intent_open` | coverage for pcm_trim_usable_sequence_intent_open with active_through_preview_or_loop_candidate oracle focus |
| 16 | `independent-probe-source-coverage` | 161 | `SOUNDSTONE_RECORDING_LILLIPUT_STEPS` | `finite_tail_or_transition_end` | `non_zero_control_semantics_pending` | coverage for non_zero_control_semantics_pending with finite_tail_or_transition_end oracle focus |

## Post Capture Validation

- `python tools/run_audio_independent_oracle_campaign.py --limit 1 --mode dry-run-plan`
- `python tools/validate_audio_independent_oracle_campaign_run_summary.py`
- `python tools/run_audio_independent_oracle_campaign.py --limit 1 --mode audit-existing-captures`
- `python tools/validate_audio_independent_oracle_campaign_run_summary.py`
- `python tools/run_audio_independent_oracle_campaign.py --mode audit-existing-captures`
- `python tools/validate_audio_independent_oracle_campaign_run_summary.py`
- `python tools/validate_audio_oracle_reference_capture.py --plan manifests/audio-oracle-comparison-plan-all-tracks.json --track-id 1 --allow-missing`
- `python tools/validate_audio_oracle_comparison_plan.py manifests/audio-oracle-comparison-plan-all-tracks.json --allow-missing-source-outputs`
- `python tools/collect_audio_oracle_comparison_results.py --plan manifests/audio-oracle-comparison-plan-all-tracks.json --summary build/audio/oracle-comparison-all-tracks/oracle-comparison-summary.json`
- `python tools/validate_audio_oracle_comparison_summary.py build/audio/oracle-comparison-all-tracks/oracle-comparison-summary.json --require-compared`
- `python tools/build_audio_oracle_verification_report.py --summary build/audio/oracle-comparison-all-tracks/oracle-comparison-summary.json --json manifests/audio-oracle-verification-report-all-tracks.json --markdown notes/audio-oracle-verification-report-all-tracks.md`
- `python tools/validate_audio_oracle_verification_report.py manifests/audio-oracle-verification-report-all-tracks.json --require-representative-pass`
- `python tools/build_audio_duration_uncertainty_register.py`
- `python tools/validate_audio_duration_uncertainty_register.py`

## Remaining Uncertainty

- The campaign closes only the representative independent-emulator evidence gap after real captures are imported.
- Non-zero control semantics, zero-runtime proof, loop-point metadata, finite-transition review, and measurement gaps remain governed by the duration uncertainty register.
- All-track independent capture can be staged after the representative campaign proves the external capture/import path.
