# Audio Independent Oracle Coverage Report

Status: near-oracle coverage is all-track green; independent external-emulator captures remain pending.

## Summary

- oracle jobs: `190`
- near-oracle pass count: `190`
- status counts: `{'audio_equivalent_state_delta': 190}`
- independent captures: `0`
- missing independent captures: `190`
- representative campaign jobs: `16`
- representative missing independent captures: `16`
- phase jobs: `{'independent-duration-uncertainty-coverage': 4, 'independent-probe-source-coverage': 5, 'independent-representative-core': 7}`
- representative uncertainty counts: `{'active_preview_classification_pending': 1, 'finite_transition_review_pending': 2, 'loop_point_metadata_pending': 2, 'non_zero_control_semantics_pending': 3, 'pcm_trim_usable_sequence_intent_open': 2, 'zero_runtime_probe_pending': 6}`
- all-track near oracle passed: `True`
- independent emulator gate passed: `False`
- release-quality playback claim ready: `False`

## Representative Campaign

| Order | Track | Name | Phase | Primary uncertainty | Focus | Independent capture |
| ---: | ---: | --- | --- | --- | --- | --- |
| 1 | 001 | `GAS_STATION` | `independent-representative-core` | `zero_runtime_probe_pending` | `active_through_preview_or_loop_candidate` | `False` |
| 2 | 017 | `MONOTOLI_BUILDING` | `independent-representative-core` | `non_zero_control_semantics_pending` | `active_through_preview_or_loop_candidate` | `False` |
| 3 | 032 | `GIANT_STEP` | `independent-representative-core` | `zero_runtime_probe_pending` | `finite_tail_or_transition_end` | `False` |
| 4 | 046 | `ONETT` | `independent-representative-core` | `non_zero_control_semantics_pending` | `active_through_preview_or_loop_candidate` | `False` |
| 5 | 171 | `WINTERS_INTRO` | `independent-representative-core` | `zero_runtime_probe_pending` | `active_through_preview_or_loop_candidate` | `False` |
| 6 | 173 | `GOOD_MORNING_MOONSIDE` | `independent-representative-core` | `zero_runtime_probe_pending` | `active_through_preview_or_loop_candidate` | `False` |
| 7 | 175 | `TITLE_SCREEN` | `independent-representative-core` | `zero_runtime_probe_pending` | `general_playback_equivalence` | `False` |
| 8 | 010 | `WHAT_THE_HECK` | `independent-duration-uncertainty-coverage` | `active_preview_classification_pending` | `general_playback_equivalence` | `False` |
| 9 | 008 | `BATTLE_SWIRL1` | `independent-duration-uncertainty-coverage` | `finite_transition_review_pending` | `finite_tail_or_transition_end` | `False` |
| 10 | 005 | `YOU_WON1` | `independent-duration-uncertainty-coverage` | `loop_point_metadata_pending` | `active_through_preview_or_loop_candidate` | `False` |
| 11 | 012 | `YOU_WON2` | `independent-duration-uncertainty-coverage` | `pcm_trim_usable_sequence_intent_open` | `active_through_preview_or_loop_candidate` | `False` |
| 12 | 025 | `CHAOS_THEATRE` | `independent-probe-source-coverage` | `zero_runtime_probe_pending` | `active_through_preview_or_loop_candidate` | `False` |
| 13 | 115 | `PHONE_CALL` | `independent-probe-source-coverage` | `loop_point_metadata_pending` | `general_playback_equivalence` | `False` |
| 14 | 123 | `SOMEONE_JOINS` | `independent-probe-source-coverage` | `finite_transition_review_pending` | `finite_tail_or_transition_end` | `False` |
| 15 | 135 | `TELEPORT_IN` | `independent-probe-source-coverage` | `pcm_trim_usable_sequence_intent_open` | `active_through_preview_or_loop_candidate` | `False` |
| 16 | 161 | `SOUNDSTONE_RECORDING_LILLIPUT_STEPS` | `independent-probe-source-coverage` | `non_zero_control_semantics_pending` | `finite_tail_or_transition_end` | `False` |

## Capture Policy

- Near-oracle equivalence is already all-track green but is not independent external-emulator evidence.
- Representative campaign capture should be completed before expanding to all-track independent capture.
- Accepted independent captures must use mesen2, bsnes/higan, or mednafen metadata and pass import validation.
- This report does not change playback/export behavior and cannot promote release-quality playback claims.

## Remaining Uncertainty

- All 16 representative campaign captures are still missing independent external-emulator evidence.
- All 190 all-track oracle jobs are missing independent capture metadata.
- Release-quality playback claims remain blocked until independent captures are imported and validated.
