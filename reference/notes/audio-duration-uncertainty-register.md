# Audio Duration Uncertainty Register

Status: duration/export uncertainty is joined across export policy, sequence triage, zero/nonzero probe results, and oracle gates.

## Summary

- tracks: `192`
- primary uncertainty: `{'active_preview_classification_pending': 1, 'finite_transition_review_pending': 5, 'loop_point_metadata_pending': 5, 'measurement_missing': 1, 'no_duration_uncertainty_for_current_export': 1, 'non_zero_control_semantics_pending': 155, 'pcm_trim_usable_sequence_intent_open': 5, 'zero_runtime_probe_pending': 19}`
- export classes: `{'finite_or_transition_review_candidate': 27, 'finite_trim_candidate': 20, 'loop_or_held_candidate': 63, 'skip_no_audio': 1, 'unknown_active_preview': 80, 'unmeasured_or_missing': 1}`
- zero probe statuses: `{'not_in_zero_probe_lane': 173, 'pending': 19}`
- zero probe blockers: `{'active_preview_classification': 7, 'ef_return_stack_model': 15, 'finite_transition_review': 10, 'loop_point_metadata': 2, 'zero_runtime_effect_proof': 19}`
- nonzero probe statuses: `{'pending': 7}`
- nonzero probe blockers: `{'earthbound_variant_ff_effect': 1, 'ef_call_return_effect': 3, 'non_zero_control_semantics_pending': 7, 'timing_toggle_effect': 3}`
- public exact-duration tracks now: `21`
- sequence promotion allowed: `False`

## Release Gates

- all-track near-oracle passed: `True`
- independent emulator gate passed: `False`
- release-quality playback claim ready: `False`
- release gate blocker: `independent_emulator_gate_pending`

## Priority Lanes

| Lane | Tracks | Recommended work |
| --- | ---: | --- |
| `zero_runtime_probe_pending` | 19 | run the 19 generated zero-runtime probe jobs, then collect and validate results |
| `non_zero_control_semantics_pending` | 155 | run the 7 nonzero control probe jobs, starting with the 0x0957 FF/FE/EF mix |
| `loop_point_metadata_pending` | 5 | extract loop entry/exit evidence before exact loop export |

## Decision Policy

- Zero-probe evidence can reduce sequence uncertainty only after individual results validate.
- Sequence-derived public exact-duration promotion remains blocked when sequence command promotion is false.
- Loop-point metadata and active-preview classification remain separate work even after a 0x00 effect is understood.
- Independent emulator comparison remains a release confidence gate, not a prerequisite for local diagnostics.

## Track Register Sample

| Track | Name | Export class | Primary uncertainty | Remaining blockers | Next action |
| ---: | --- | --- | --- | --- | --- |
| `000` | `NONE` | `unmeasured_or_missing` | `measurement_missing` | `[]` | regenerate playback/export duration measurements before export |
| `001` | `GAS_STATION` | `unknown_active_preview` | `zero_runtime_probe_pending` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'active_preview_classification']` | run targeted 0x00 runtime probe jobs and collect validated results |
| `002` | `NAMING_SCREEN` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `003` | `SETUP_SCREEN` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `005` | `YOU_WON1` | `loop_or_held_candidate` | `loop_point_metadata_pending` | `[]` | decode loop entry/exit metadata before public exact loop export |
| `006` | `LEVEL_UP` | `loop_or_held_candidate` | `loop_point_metadata_pending` | `[]` | decode loop entry/exit metadata before public exact loop export |
| `007` | `YOU_LOSE` | `loop_or_held_candidate` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `008` | `BATTLE_SWIRL1` | `finite_or_transition_review_candidate` | `finite_transition_review_pending` | `[]` | review observed tail/silence as finite ending or transition |
| `009` | `BATTLE_SWIRL2` | `finite_or_transition_review_candidate` | `finite_transition_review_pending` | `[]` | review observed tail/silence as finite ending or transition |
| `010` | `WHAT_THE_HECK` | `unknown_active_preview` | `active_preview_classification_pending` | `[]` | classify active preview as finite, held, looping, or unresolved |
| `011` | `NEW_FRIEND` | `finite_or_transition_review_candidate` | `finite_transition_review_pending` | `[]` | review observed tail/silence as finite ending or transition |
| `012` | `YOU_WON2` | `finite_trim_candidate` | `pcm_trim_usable_sequence_intent_open` | `[]` | keep PCM-trim export usable while sequence intent remains advisory |
| `013` | `TELEPORT_OUT` | `finite_trim_candidate` | `pcm_trim_usable_sequence_intent_open` | `[]` | keep PCM-trim export usable while sequence intent remains advisory |
| `014` | `TELEPORT_FAIL` | `finite_trim_candidate` | `pcm_trim_usable_sequence_intent_open` | `[]` | keep PCM-trim export usable while sequence intent remains advisory |
| `015` | `FALLING_UNDERGROUND` | `finite_trim_candidate` | `pcm_trim_usable_sequence_intent_open` | `[]` | keep PCM-trim export usable while sequence intent remains advisory |
| `016` | `DR_ANDONUTS_LAB` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `017` | `MONOTOLI_BUILDING` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `018` | `SLOPPY_HOUSE` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `019` | `NEIGHBOURS_HOUSE` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `020` | `ARCADE` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `021` | `POKEYS_HOUSE` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `022` | `HOSPITAL` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `023` | `NESSS_HOUSE` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `024` | `PAULAS_THEME` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `025` | `CHAOS_THEATRE` | `unknown_active_preview` | `zero_runtime_probe_pending` | `['zero_runtime_effect_proof', 'active_preview_classification']` | run targeted 0x00 runtime probe jobs and collect validated results |
| `026` | `HOTEL` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `027` | `GOOD_MORNING` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `028` | `DEPARTMENT_STORE` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `029` | `ONETT_AT_NIGHT_1` | `loop_or_held_candidate` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `030` | `YOUR_SANCTUARY_1` | `loop_or_held_candidate` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `031` | `YOUR_SANCTUARY_2` | `loop_or_held_candidate` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `032` | `GIANT_STEP` | `finite_or_transition_review_candidate` | `zero_runtime_probe_pending` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'finite_transition_review']` | run targeted 0x00 runtime probe jobs and collect validated results |
| `033` | `LILLIPUT_STEPS` | `finite_or_transition_review_candidate` | `zero_runtime_probe_pending` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'finite_transition_review']` | run targeted 0x00 runtime probe jobs and collect validated results |
| `034` | `MILKY_WELL` | `finite_or_transition_review_candidate` | `zero_runtime_probe_pending` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'finite_transition_review']` | run targeted 0x00 runtime probe jobs and collect validated results |
| `035` | `RAINY_CIRCLE` | `finite_or_transition_review_candidate` | `zero_runtime_probe_pending` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'finite_transition_review']` | run targeted 0x00 runtime probe jobs and collect validated results |
| `036` | `MAGNET_HILL` | `finite_or_transition_review_candidate` | `zero_runtime_probe_pending` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'finite_transition_review']` | run targeted 0x00 runtime probe jobs and collect validated results |
| `037` | `PINK_CLOUD` | `finite_or_transition_review_candidate` | `zero_runtime_probe_pending` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'finite_transition_review']` | run targeted 0x00 runtime probe jobs and collect validated results |
| `038` | `LUMINE_HALL` | `finite_or_transition_review_candidate` | `zero_runtime_probe_pending` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'finite_transition_review']` | run targeted 0x00 runtime probe jobs and collect validated results |
| `039` | `FIRE_SPRING` | `finite_or_transition_review_candidate` | `zero_runtime_probe_pending` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'finite_transition_review']` | run targeted 0x00 runtime probe jobs and collect validated results |
| `040` | `NEAR_A_BOSS` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `041` | `ALIEN_INVESTIGATION` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `042` | `FIRE_SPRINGS_HALL` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `043` | `BELCH_BASE` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `044` | `ZOMBIE_THREED` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `045` | `SPOOKY_CAVE` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `046` | `ONETT` | `loop_or_held_candidate` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `047` | `FOURSIDE` | `loop_or_held_candidate` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `048` | `SATURN_VALLEY` | `loop_or_held_candidate` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `049` | `MONKEY_CAVES` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `050` | `MOONSIDE` | `loop_or_held_candidate` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `051` | `DUSTY_DUNES_DESERT` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `052` | `PEACEFUL_REST_VALLEY` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `053` | `ZOMBIE_THREED2` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `054` | `WINTERS` | `loop_or_held_candidate` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `055` | `CAVE_NEAR_A_BOSS` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `056` | `SUMMERS` | `loop_or_held_candidate` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `057` | `JACKIES_CAFE` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `058` | `SAILING_TO_SCARABA` | `loop_or_held_candidate` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `059` | `DALAAM` | `loop_or_held_candidate` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `060` | `MU_TRAINING` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `061` | `BAZAAR` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `062` | `SCARABA_DESERT` | `loop_or_held_candidate` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `063` | `PYRAMID` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `064` | `DEEP_DARKNESS` | `loop_or_held_candidate` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `065` | `TENDA_VILLAGE` | `loop_or_held_candidate` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `066` | `WELCOME_HOME` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `067` | `SEA_OF_EDEN` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `068` | `LOST_UNDERWORLD` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `069` | `FIRST_STEP_BACK` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `070` | `SECOND_STEP_BACK` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `071` | `THE_PLACE` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `072` | `GIYGAS_AWAKENS` | `loop_or_held_candidate` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `073` | `GIYGAS_PHASE2` | `loop_or_held_candidate` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `074` | `GIYGAS_WEAKENED2` | `loop_or_held_candidate` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `075` | `GIYGAS_DEATH2` | `loop_or_held_candidate` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `076` | `RUNAWAY5_CONCERT_1` | `loop_or_held_candidate` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `077` | `RUNAWAY5_TOUR_BUS` | `loop_or_held_candidate` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `078` | `RUNAWAY5_CONCERT_2` | `loop_or_held_candidate` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `079` | `POWER` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
| `080` | `VENUS_CONCERT` | `unknown_active_preview` | `non_zero_control_semantics_pending` | `[]` | decode FD/FE/FF and related control-flow semantics before exact promotion |
