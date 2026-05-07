# Audio Oracle Source Regeneration Plan

Status: source evidence regeneration is planned; current playback/export behavior is preserved.

## Summary

- stages: `6`
- current collector-ready jobs: `0`
- current source-blocked jobs: `190`
- current source SPCs present: `0`
- current source render WAVs present: `0`
- all-track oracle jobs: `190`
- representative capture jobs: `16`
- expected source SPCs after regeneration: `190`
- expected source render WAVs after regeneration: `190`

## Stages

| Rank | Stage | Purpose | Commands |
| ---: | --- | --- | ---: |
| 1 | `preflight_current_gap` | Confirm whether the oracle collector is blocked by missing local source/reference artifacts before regeneration. | 2 |
| 2 | `all_track_fusion_source_spc` | Regenerate all-track fused CHANGE_MUSIC/C0:AB06 last-key-on source SPC snapshots under ignored build/audio. | 2 |
| 3 | `spc_index_and_renderer_jobs` | Index the regenerated SPC snapshots and build the all-track libgme/snes_spc renderer job queue. | 3 |
| 4 | `libgme_render_and_metrics` | Render source WAVs from regenerated SPC snapshots, collect backend statuses, and refresh render metrics. | 6 |
| 5 | `playback_oracle_plan_refresh` | Rebuild committed metadata that points to the regenerated source SPC/WAV evidence. | 6 |
| 6 | `reference_capture_and_collection` | After source evidence exists, import independent external-emulator captures and collect comparison results. | 6 |

## Representative Handoff Tracks

| Order | Track | Name | Phase | Primary uncertainty |
| ---: | ---: | --- | --- | --- |
| 1 | 001 | `GAS_STATION` | `independent-representative-core` | `zero_runtime_probe_pending` |
| 2 | 017 | `MONOTOLI_BUILDING` | `independent-representative-core` | `non_zero_control_semantics_pending` |
| 3 | 032 | `GIANT_STEP` | `independent-representative-core` | `zero_runtime_probe_pending` |
| 4 | 046 | `ONETT` | `independent-representative-core` | `non_zero_control_semantics_pending` |
| 5 | 171 | `WINTERS_INTRO` | `independent-representative-core` | `zero_runtime_probe_pending` |
| 6 | 173 | `GOOD_MORNING_MOONSIDE` | `independent-representative-core` | `zero_runtime_probe_pending` |
| 7 | 175 | `TITLE_SCREEN` | `independent-representative-core` | `zero_runtime_probe_pending` |
| 8 | 010 | `WHAT_THE_HECK` | `independent-duration-uncertainty-coverage` | `active_preview_classification_pending` |
| 9 | 008 | `BATTLE_SWIRL1` | `independent-duration-uncertainty-coverage` | `finite_transition_review_pending` |
| 10 | 005 | `YOU_WON1` | `independent-duration-uncertainty-coverage` | `loop_point_metadata_pending` |
| 11 | 012 | `YOU_WON2` | `independent-duration-uncertainty-coverage` | `pcm_trim_usable_sequence_intent_open` |
| 12 | 025 | `CHAOS_THEATRE` | `independent-probe-source-coverage` | `zero_runtime_probe_pending` |
| 13 | 115 | `PHONE_CALL` | `independent-probe-source-coverage` | `loop_point_metadata_pending` |
| 14 | 123 | `SOMEONE_JOINS` | `independent-probe-source-coverage` | `finite_transition_review_pending` |
| 15 | 135 | `TELEPORT_IN` | `independent-probe-source-coverage` | `pcm_trim_usable_sequence_intent_open` |
| 16 | 161 | `SOUNDSTONE_RECORDING_LILLIPUT_STEPS` | `independent-probe-source-coverage` | `non_zero_control_semantics_pending` |

## Validation

- `python tools/build_audio_oracle_source_regeneration_plan.py`
- `python tools/validate_audio_oracle_source_regeneration_plan.py`
- `python tools/validate_audio_oracle_source_evidence_preflight.py`
- `python tools/validate_audio_oracle_comparison_plan.py manifests/audio-oracle-comparison-plan-all-tracks.json --allow-missing-source-outputs`
- `python tools/validate_audio_oracle_verification_report.py manifests/audio-oracle-verification-report-all-tracks.json --require-representative-pass`
- `python tools/validate_audio_independent_oracle_handoff_matrix.py`
- `python tools/validate_audio_independent_oracle_capture_packet.py`
- `python tools/validate_audio_duration_next_actions_plan.py`
- `git diff --check`

## Policy

- This plan regenerates ignored local source evidence and committed diagnostics only; it does not change playback/export behavior.
- All generated SPC/WAV/backend outputs remain under ignored build/audio paths and must not be distributed.
- The source regeneration lane must complete before collecting oracle comparison summaries in a clean workspace.
- Independent external-emulator captures remain a separate operator-provided evidence step after source SPC/WAV evidence exists.
- Exact durations, loop metadata, and release-quality playback claims remain blocked until their existing gates pass.

## Remaining Uncertainty

- The source SPC/WAV regeneration chain needs a user-provided ROM and local libgme harness build.
- Independent emulator captures are still external inputs after the source evidence layer exists.
- Exact duration, loop, finite-ending, and control-semantics gates remain unchanged.
