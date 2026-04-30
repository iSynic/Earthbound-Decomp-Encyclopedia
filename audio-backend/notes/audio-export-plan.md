# Audio Export Plan

Status: export policy ready; exact loop points and some sequence-level duration semantics remain open.

- tracks: `192`
- export classes: `{'unmeasured_or_missing': 1, 'unknown_active_preview': 80, 'skip_no_audio': 1, 'loop_or_held_candidate': 63, 'finite_or_transition_review_candidate': 27, 'finite_trim_candidate': 20}`
- export statuses: `{'blocked_or_skip_until_measured': 1, 'preview_only': 80, 'ready': 1, 'preview_policy_ready_exact_loop_pending': 63, 'review_needed_before_public_exact_export': 27, 'usable_with_pcm_silence_evidence': 20}`
- recommended modes: `{'do_not_public_export': 1, 'diagnostic_preview': 80, 'skip': 1, 'loop_count_plus_fade_preview': 63, 'trim_candidate_after_manual_or_sequence_review': 27, 'trim_to_observed_end': 20}`
- tracks needing sequence semantics: `170`

## Playback Confidence

- all-track near-oracle passed: `True`
- independent emulator gate passed: `False`
- release-quality playback claim ready: `False`

## Defaults

- sample format: `32000` Hz, `2` channels, `16` bits
- loop preview: `2` loops plus `5.0` second fade
- finite trim policy: trim after the last sample above the silence threshold; keep no extra generated silence

## Release Gates

- Finite trim candidates are usable where sustained trailing silence is observed, but sequence semantics can still refine exact musical intent.
- Loop or held candidates must use an explicit loop-count/fade preview until loop points are decoded.
- Unknown active previews are not exact exports.
- Independent external-emulator playback validation remains optional for development but open for public release confidence.
- Generated WAV/SPC/audio outputs remain local ignored artifacts derived from a user-provided ROM.

## Tracks

| Track | Name | Policy Class | Export Class | Status | Mode | Duration Seconds | Needs Semantics |
| ---: | --- | --- | --- | --- | --- | ---: | --- |
| `000` | `NONE` | `unknown_candidate` | `unmeasured_or_missing` | `blocked_or_skip_until_measured` | `do_not_public_export` |  | no |
| `001` | `GAS_STATION` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `002` | `NAMING_SCREEN` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `003` | `SETUP_SCREEN` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `004` | `NONE2` | `no_audio_no_key_on` | `skip_no_audio` | `ready` | `skip` | 0.0 | no |
| `005` | `YOU_WON1` | `finite_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 120.0 | yes |
| `006` | `LEVEL_UP` | `finite_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 120.0 | yes |
| `007` | `YOU_LOSE` | `finite_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 120.0 | yes |
| `008` | `BATTLE_SWIRL1` | `looping_candidate` | `finite_or_transition_review_candidate` | `review_needed_before_public_exact_export` | `trim_candidate_after_manual_or_sequence_review` | 4.036187 | yes |
| `009` | `BATTLE_SWIRL2` | `looping_candidate` | `finite_or_transition_review_candidate` | `review_needed_before_public_exact_export` | `trim_candidate_after_manual_or_sequence_review` | 4.094594 | yes |
| `010` | `WHAT_THE_HECK` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `011` | `NEW_FRIEND` | `unknown_candidate` | `finite_or_transition_review_candidate` | `review_needed_before_public_exact_export` | `trim_candidate_after_manual_or_sequence_review` | 7.910188 | yes |
| `012` | `YOU_WON2` | `finite_candidate` | `finite_trim_candidate` | `usable_with_pcm_silence_evidence` | `trim_to_observed_end` | 3.390938 | no |
| `013` | `TELEPORT_OUT` | `finite_candidate` | `finite_trim_candidate` | `usable_with_pcm_silence_evidence` | `trim_to_observed_end` | 10.202156 | no |
| `014` | `TELEPORT_FAIL` | `finite_candidate` | `finite_trim_candidate` | `usable_with_pcm_silence_evidence` | `trim_to_observed_end` | 0.667156 | no |
| `015` | `FALLING_UNDERGROUND` | `finite_candidate` | `finite_trim_candidate` | `usable_with_pcm_silence_evidence` | `trim_to_observed_end` | 6.393813 | no |
| `016` | `DR_ANDONUTS_LAB` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `017` | `MONOTOLI_BUILDING` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `018` | `SLOPPY_HOUSE` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `019` | `NEIGHBOURS_HOUSE` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `020` | `ARCADE` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `021` | `POKEYS_HOUSE` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `022` | `HOSPITAL` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `023` | `NESSS_HOUSE` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `024` | `PAULAS_THEME` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `025` | `CHAOS_THEATRE` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `026` | `HOTEL` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `027` | `GOOD_MORNING` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `028` | `DEPARTMENT_STORE` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `029` | `ONETT_AT_NIGHT_1` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `030` | `YOUR_SANCTUARY_1` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `031` | `YOUR_SANCTUARY_2` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `032` | `GIANT_STEP` | `unknown_candidate` | `finite_or_transition_review_candidate` | `review_needed_before_public_exact_export` | `trim_candidate_after_manual_or_sequence_review` | 21.003219 | yes |
| `033` | `LILLIPUT_STEPS` | `unknown_candidate` | `finite_or_transition_review_candidate` | `review_needed_before_public_exact_export` | `trim_candidate_after_manual_or_sequence_review` | 21.004906 | yes |
| `034` | `MILKY_WELL` | `unknown_candidate` | `finite_or_transition_review_candidate` | `review_needed_before_public_exact_export` | `trim_candidate_after_manual_or_sequence_review` | 21.002375 | yes |
| `035` | `RAINY_CIRCLE` | `unknown_candidate` | `finite_or_transition_review_candidate` | `review_needed_before_public_exact_export` | `trim_candidate_after_manual_or_sequence_review` | 21.001938 | yes |
| `036` | `MAGNET_HILL` | `unknown_candidate` | `finite_or_transition_review_candidate` | `review_needed_before_public_exact_export` | `trim_candidate_after_manual_or_sequence_review` | 21.000875 | yes |
| `037` | `PINK_CLOUD` | `unknown_candidate` | `finite_or_transition_review_candidate` | `review_needed_before_public_exact_export` | `trim_candidate_after_manual_or_sequence_review` | 21.005312 | yes |
| `038` | `LUMINE_HALL` | `unknown_candidate` | `finite_or_transition_review_candidate` | `review_needed_before_public_exact_export` | `trim_candidate_after_manual_or_sequence_review` | 19.2455 | yes |
| `039` | `FIRE_SPRING` | `unknown_candidate` | `finite_or_transition_review_candidate` | `review_needed_before_public_exact_export` | `trim_candidate_after_manual_or_sequence_review` | 21.005406 | yes |
| `040` | `NEAR_A_BOSS` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `041` | `ALIEN_INVESTIGATION` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `042` | `FIRE_SPRINGS_HALL` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `043` | `BELCH_BASE` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `044` | `ZOMBIE_THREED` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `045` | `SPOOKY_CAVE` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `046` | `ONETT` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `047` | `FOURSIDE` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `048` | `SATURN_VALLEY` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `049` | `MONKEY_CAVES` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `050` | `MOONSIDE` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `051` | `DUSTY_DUNES_DESERT` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `052` | `PEACEFUL_REST_VALLEY` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `053` | `ZOMBIE_THREED2` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `054` | `WINTERS` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `055` | `CAVE_NEAR_A_BOSS` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `056` | `SUMMERS` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `057` | `JACKIES_CAFE` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `058` | `SAILING_TO_SCARABA` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `059` | `DALAAM` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `060` | `MU_TRAINING` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `061` | `BAZAAR` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `062` | `SCARABA_DESERT` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `063` | `PYRAMID` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `064` | `DEEP_DARKNESS` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `065` | `TENDA_VILLAGE` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `066` | `WELCOME_HOME` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `067` | `SEA_OF_EDEN` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `068` | `LOST_UNDERWORLD` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `069` | `FIRST_STEP_BACK` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `070` | `SECOND_STEP_BACK` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `071` | `THE_PLACE` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `072` | `GIYGAS_AWAKENS` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `073` | `GIYGAS_PHASE2` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `074` | `GIYGAS_WEAKENED2` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `075` | `GIYGAS_DEATH2` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `076` | `RUNAWAY5_CONCERT_1` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `077` | `RUNAWAY5_TOUR_BUS` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `078` | `RUNAWAY5_CONCERT_2` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `079` | `POWER` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `080` | `VENUS_CONCERT` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `081` | `YELLOW_SUBMARINE` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `082` | `BICYCLE` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `083` | `SKY_RUNNER` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `084` | `SKY_RUNNER_FALLING` | `unknown_candidate` | `finite_or_transition_review_candidate` | `review_needed_before_public_exact_export` | `trim_candidate_after_manual_or_sequence_review` | 7.594875 | yes |
| `085` | `BULLDOZER` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `086` | `TESSIE` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `087` | `CITY_BUS` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `088` | `FUZZY_PICKLES` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `089` | `DELIVERY` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `090` | `RETURN_TO_YOUR_BODY` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `091` | `PHASE_DISTORTER_TIME_TRAVEL` | `unknown_candidate` | `finite_or_transition_review_candidate` | `review_needed_before_public_exact_export` | `trim_candidate_after_manual_or_sequence_review` | 16.832563 | yes |
| `092` | `COFFEE_BREAK` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `093` | `BECAUSE_I_LOVE_YOU` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `094` | `GOOD_FRIENDS_BAD_FRIENDS` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `095` | `SMILES_AND_TEARS` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `096` | `VS_CRANKY_LADY` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `097` | `VS_SPINNING_ROBO` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `098` | `VS_STRUTTIN_EVIL_MUSHROOM` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `099` | `VS_MASTER_BELCH` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `100` | `VS_NEW_AGE_RETRO_HIPPIE` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `101` | `VS_RUNAWAY_DOG` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `102` | `VS_CAVE_BOY` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `103` | `VS_YOUR_SANCTUARY_BOSS` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `104` | `VS_KRAKEN` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `105` | `POKEY_MEANS_BUSINESS` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `106` | `INSIDE_THE_DUNGEON` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `107` | `MEGATON_WALK` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `108` | `SEA_OF_EDEN2` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `109` | `EXPLOSION` | `finite_candidate` | `finite_trim_candidate` | `usable_with_pcm_silence_evidence` | `trim_to_observed_end` | 6.852594 | no |
| `110` | `SKY_RUNNER_CRASH` | `finite_candidate` | `finite_trim_candidate` | `usable_with_pcm_silence_evidence` | `trim_to_observed_end` | 6.014469 | no |
| `111` | `MAGIC_CAKE` | `unknown_candidate` | `finite_or_transition_review_candidate` | `review_needed_before_public_exact_export` | `trim_candidate_after_manual_or_sequence_review` | 5.790375 | yes |
| `112` | `POKEYS_HOUSE_BUZZ_BUZZ` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `113` | `BUZZ_BUZZ_SWATTED` | `finite_candidate` | `finite_trim_candidate` | `usable_with_pcm_silence_evidence` | `trim_to_observed_end` | 2.246594 | no |
| `114` | `ONETT_AT_NIGHT_BUZZ_BUZZ` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `115` | `PHONE_CALL` | `finite_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 120.0 | yes |
| `116` | `KNOCK_KNOCK_RIGHT` | `finite_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 120.0 | yes |
| `117` | `RABBIT_CAVE` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `118` | `ONETT_AT_NIGHT_3` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `119` | `APPLE_OF_ENLIGHTENMENT` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `120` | `HOTEL_OF_THE_LIVING_DEAD` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `121` | `ONETT_INTRO` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `122` | `SUNRISE_ONETT` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `123` | `SOMEONE_JOINS` | `unknown_candidate` | `finite_or_transition_review_candidate` | `review_needed_before_public_exact_export` | `trim_candidate_after_manual_or_sequence_review` | 2.624125 | yes |
| `124` | `ENTER_STARMAN_JR` | `unknown_candidate` | `finite_or_transition_review_candidate` | `review_needed_before_public_exact_export` | `trim_candidate_after_manual_or_sequence_review` | 3.406875 | yes |
| `125` | `BOARDING_SCHOOL` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `126` | `PHASE_DISTORTER` | `unknown_candidate` | `finite_or_transition_review_candidate` | `review_needed_before_public_exact_export` | `trim_candidate_after_manual_or_sequence_review` | 3.56725 | yes |
| `127` | `PHASE_DISTORTER_2` | `unknown_candidate` | `finite_or_transition_review_candidate` | `review_needed_before_public_exact_export` | `trim_candidate_after_manual_or_sequence_review` | 3.553031 | yes |
| `128` | `BOY_MEETS_GIRL` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `129` | `HAPPY_THREED` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `130` | `RUNAWAY5_ARE_FREED` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `131` | `FLYING_MAN` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `132` | `ONETT_AT_NIGHT_2` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `133` | `HIDDEN_SONG` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `134` | `YOUR_SANCTUARY_BOSS` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `135` | `TELEPORT_IN` | `finite_candidate` | `finite_trim_candidate` | `usable_with_pcm_silence_evidence` | `trim_to_observed_end` | 4.744781 | no |
| `136` | `SATURN_VALLEY_CAVE` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `137` | `ELEVATOR_DOWN` | `finite_candidate` | `finite_trim_candidate` | `usable_with_pcm_silence_evidence` | `trim_to_observed_end` | 22.0855 | no |
| `138` | `ELEVATOR_UP` | `finite_candidate` | `finite_trim_candidate` | `usable_with_pcm_silence_evidence` | `trim_to_observed_end` | 22.081906 | no |
| `139` | `ELEVATOR_STOP` | `finite_candidate` | `finite_trim_candidate` | `usable_with_pcm_silence_evidence` | `trim_to_observed_end` | 22.082031 | no |
| `140` | `TOPOLLA_THEATRE` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `141` | `VS_MASTER_BARF` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `142` | `GOING_TO_MAGICANT` | `unknown_candidate` | `finite_or_transition_review_candidate` | `review_needed_before_public_exact_export` | `trim_candidate_after_manual_or_sequence_review` | 11.8845 | yes |
| `143` | `LEAVING_MAGICANT` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `144` | `KRAKEN_DEFEATED` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `145` | `STONEHENGE_DESTRUCTION` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `146` | `TESSIE_SIGHTING` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `147` | `METEOR_FALL` | `finite_candidate` | `finite_trim_candidate` | `usable_with_pcm_silence_evidence` | `trim_to_observed_end` | 18.651344 | no |
| `148` | `VS_STARMAN_JR` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `149` | `RUNAWAY5_HELP_OUT` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `150` | `KNOCK_KNOCK` | `finite_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 120.0 | yes |
| `151` | `ONETT_AFTER_METEOR1` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `152` | `ONETT_AFTER_METEOR2` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `153` | `POKEY_THEME` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `154` | `ONETT_AT_NIGHT_BUZZ_BUZZ2` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `155` | `YOUR_SANCTUARY_BOSS2` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `156` | `METEOR_STRIKE` | `finite_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 120.0 | yes |
| `157` | `ATTRACT_MODE` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `158` | `NAME_CONFIRMATION` | `unknown_candidate` | `finite_or_transition_review_candidate` | `review_needed_before_public_exact_export` | `trim_candidate_after_manual_or_sequence_review` | 6.951906 | yes |
| `159` | `PEACEFUL_REST_VALLEY2` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `160` | `SOUNDSTONE_RECORDING_GIANT_STEP` | `finite_candidate` | `finite_trim_candidate` | `usable_with_pcm_silence_evidence` | `trim_to_observed_end` | 5.1565 | no |
| `161` | `SOUNDSTONE_RECORDING_LILLIPUT_STEPS` | `finite_candidate` | `finite_trim_candidate` | `usable_with_pcm_silence_evidence` | `trim_to_observed_end` | 3.840281 | no |
| `162` | `SOUNDSTONE_RECORDING_MILKY_WELL` | `finite_candidate` | `finite_trim_candidate` | `usable_with_pcm_silence_evidence` | `trim_to_observed_end` | 3.839344 | no |
| `163` | `SOUNDSTONE_RECORDING_RAINY_CIRCLE` | `finite_candidate` | `finite_trim_candidate` | `usable_with_pcm_silence_evidence` | `trim_to_observed_end` | 3.842312 | no |
| `164` | `SOUNDSTONE_RECORDING_MAGNET_HILL` | `finite_candidate` | `finite_trim_candidate` | `usable_with_pcm_silence_evidence` | `trim_to_observed_end` | 3.842375 | no |
| `165` | `SOUNDSTONE_RECORDING_PINK_CLOUD` | `finite_candidate` | `finite_trim_candidate` | `usable_with_pcm_silence_evidence` | `trim_to_observed_end` | 3.837813 | no |
| `166` | `SOUNDSTONE_RECORDING_LUMINE_HALL` | `finite_candidate` | `finite_trim_candidate` | `usable_with_pcm_silence_evidence` | `trim_to_observed_end` | 3.839313 | no |
| `167` | `SOUNDSTONE_RECORDING_FIRE_SPRING` | `finite_candidate` | `finite_trim_candidate` | `usable_with_pcm_silence_evidence` | `trim_to_observed_end` | 3.467531 | no |
| `168` | `SOUNDSTONE_BGM` | `unknown_candidate` | `finite_or_transition_review_candidate` | `review_needed_before_public_exact_export` | `trim_candidate_after_manual_or_sequence_review` | 7.255187 | yes |
| `169` | `EIGHT_MELODIES` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `170` | `DALAAM_INTRO` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `171` | `WINTERS_INTRO` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `172` | `POKEY_ESCAPES` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `173` | `GOOD_MORNING_MOONSIDE` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `174` | `GAS_STATION_2` | `unknown_candidate` | `finite_or_transition_review_candidate` | `review_needed_before_public_exact_export` | `trim_candidate_after_manual_or_sequence_review` | 13.578563 | yes |
| `175` | `TITLE_SCREEN` | `looping_candidate` | `finite_or_transition_review_candidate` | `review_needed_before_public_exact_export` | `trim_candidate_after_manual_or_sequence_review` | 13.774594 | yes |
| `176` | `BATTLE_SWIRL4` | `looping_candidate` | `finite_or_transition_review_candidate` | `review_needed_before_public_exact_export` | `trim_candidate_after_manual_or_sequence_review` | 5.327125 | yes |
| `177` | `POKEY_INTRO` | `unknown_candidate` | `finite_or_transition_review_candidate` | `review_needed_before_public_exact_export` | `trim_candidate_after_manual_or_sequence_review` | 3.760531 | yes |
| `178` | `GOOD_MORNING_SCARABA` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `179` | `ROBOTOMY1` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `180` | `POKEY_ESCAPES2` | `unknown_candidate` | `finite_or_transition_review_candidate` | `review_needed_before_public_exact_export` | `trim_candidate_after_manual_or_sequence_review` | 7.385187 | yes |
| `181` | `RETURN_TO_YOUR_BODY2` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `182` | `GIYGAS_STATIC` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `183` | `SUDDEN_VICTORY` | `finite_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 120.0 | yes |
| `184` | `YOU_WON3` | `finite_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 120.0 | yes |
| `185` | `GIYGAS_PHASE3` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `186` | `GIYGAS_PHASE1` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `187` | `GIVE_US_STRENGTH` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `188` | `GOOD_MORNING2` | `unknown_candidate` | `unknown_active_preview` | `preview_only` | `diagnostic_preview` | 30.0 | yes |
| `189` | `SOUND_STONE` | `unknown_candidate` | `finite_or_transition_review_candidate` | `review_needed_before_public_exact_export` | `trim_candidate_after_manual_or_sequence_review` | 7.255187 | yes |
| `190` | `GIYGAS_DEATH` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
| `191` | `GIYGAS_WEAKENED` | `looping_candidate` | `loop_or_held_candidate` | `preview_policy_ready_exact_loop_pending` | `loop_count_plus_fade_preview` | 30.0 | yes |
