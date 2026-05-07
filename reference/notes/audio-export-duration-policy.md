# Audio Export Duration Policy

Status: duration policy ready; exact finite lengths and loop points are not yet measured.

- tracks: `192`
- duration classes: `{'unknown_candidate': 104, 'no_audio_no_key_on': 1, 'finite_candidate': 29, 'looping_candidate': 58}`
- exact-duration statuses: `{'needs_sequence_or_runtime_analysis': 104, 'not_applicable': 1, 'needs_driver_end_or_silence_detection': 29, 'needs_loop_point_detection': 58}`

## Policy

- finite tracks: Export to the first confirmed driver end, stop command, or sustained digital silence boundary, then trim tail silence according to measured samples.
- looping tracks: Do not pretend a looped cue has a finite exact length. Store loop start/end metadata; preview/export WAVs should use an explicit loop-count and fade policy.
- unknown tracks: Keep 30-second diagnostic previews out of release claims until sequence semantics or runtime measurement classifies the track.
- recommended loop preview: `{'loops': 2, 'fade_seconds': 5.0, 'minimum_intro_seconds': 0.0}`

## Release Gates

- Every rendered public export must declare finite, looping, no-audio, or unknown duration class.
- Finite exports must have a measured end sample or an explained silence threshold.
- Looping exports must include loop metadata or explicitly state the chosen loop-count/fade preview policy.
- The current 30-second renders remain diagnostic previews until this policy is measured per track.
- Exact-length claims require sequence/runtime evidence, not only track-name heuristics.

## Tracks

| Track | Name | Class | Exact Status | Export Policy | Confidence |
| ---: | --- | --- | --- | --- | --- |
| `000` | `NONE` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `001` | `GAS_STATION` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `002` | `NAMING_SCREEN` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `003` | `SETUP_SCREEN` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `004` | `NONE2` | `no_audio_no_key_on` | `not_applicable` | `skip_render` | observed |
| `005` | `YOU_WON1` | `finite_candidate` | `needs_driver_end_or_silence_detection` | `render_until_driver_end_or_sustained_silence_then_trim_tail` | name_based_candidate |
| `006` | `LEVEL_UP` | `finite_candidate` | `needs_driver_end_or_silence_detection` | `render_until_driver_end_or_sustained_silence_then_trim_tail` | name_based_candidate |
| `007` | `YOU_LOSE` | `finite_candidate` | `needs_driver_end_or_silence_detection` | `render_until_driver_end_or_sustained_silence_then_trim_tail` | name_based_candidate |
| `008` | `BATTLE_SWIRL1` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `009` | `BATTLE_SWIRL2` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `010` | `WHAT_THE_HECK` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `011` | `NEW_FRIEND` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `012` | `YOU_WON2` | `finite_candidate` | `needs_driver_end_or_silence_detection` | `render_until_driver_end_or_sustained_silence_then_trim_tail` | name_based_candidate |
| `013` | `TELEPORT_OUT` | `finite_candidate` | `needs_driver_end_or_silence_detection` | `render_until_driver_end_or_sustained_silence_then_trim_tail` | name_based_candidate |
| `014` | `TELEPORT_FAIL` | `finite_candidate` | `needs_driver_end_or_silence_detection` | `render_until_driver_end_or_sustained_silence_then_trim_tail` | name_based_candidate |
| `015` | `FALLING_UNDERGROUND` | `finite_candidate` | `needs_driver_end_or_silence_detection` | `render_until_driver_end_or_sustained_silence_then_trim_tail` | name_based_candidate |
| `016` | `DR_ANDONUTS_LAB` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `017` | `MONOTOLI_BUILDING` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `018` | `SLOPPY_HOUSE` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `019` | `NEIGHBOURS_HOUSE` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `020` | `ARCADE` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `021` | `POKEYS_HOUSE` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `022` | `HOSPITAL` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `023` | `NESSS_HOUSE` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `024` | `PAULAS_THEME` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `025` | `CHAOS_THEATRE` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `026` | `HOTEL` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `027` | `GOOD_MORNING` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `028` | `DEPARTMENT_STORE` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `029` | `ONETT_AT_NIGHT_1` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `030` | `YOUR_SANCTUARY_1` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `031` | `YOUR_SANCTUARY_2` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `032` | `GIANT_STEP` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `033` | `LILLIPUT_STEPS` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `034` | `MILKY_WELL` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `035` | `RAINY_CIRCLE` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `036` | `MAGNET_HILL` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `037` | `PINK_CLOUD` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `038` | `LUMINE_HALL` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `039` | `FIRE_SPRING` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `040` | `NEAR_A_BOSS` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `041` | `ALIEN_INVESTIGATION` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `042` | `FIRE_SPRINGS_HALL` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `043` | `BELCH_BASE` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `044` | `ZOMBIE_THREED` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `045` | `SPOOKY_CAVE` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `046` | `ONETT` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `047` | `FOURSIDE` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `048` | `SATURN_VALLEY` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `049` | `MONKEY_CAVES` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `050` | `MOONSIDE` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `051` | `DUSTY_DUNES_DESERT` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `052` | `PEACEFUL_REST_VALLEY` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `053` | `ZOMBIE_THREED2` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `054` | `WINTERS` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `055` | `CAVE_NEAR_A_BOSS` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `056` | `SUMMERS` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `057` | `JACKIES_CAFE` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `058` | `SAILING_TO_SCARABA` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `059` | `DALAAM` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `060` | `MU_TRAINING` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `061` | `BAZAAR` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `062` | `SCARABA_DESERT` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `063` | `PYRAMID` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `064` | `DEEP_DARKNESS` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `065` | `TENDA_VILLAGE` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `066` | `WELCOME_HOME` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `067` | `SEA_OF_EDEN` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `068` | `LOST_UNDERWORLD` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `069` | `FIRST_STEP_BACK` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `070` | `SECOND_STEP_BACK` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `071` | `THE_PLACE` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `072` | `GIYGAS_AWAKENS` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `073` | `GIYGAS_PHASE2` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `074` | `GIYGAS_WEAKENED2` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `075` | `GIYGAS_DEATH2` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `076` | `RUNAWAY5_CONCERT_1` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `077` | `RUNAWAY5_TOUR_BUS` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `078` | `RUNAWAY5_CONCERT_2` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `079` | `POWER` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `080` | `VENUS_CONCERT` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `081` | `YELLOW_SUBMARINE` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `082` | `BICYCLE` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `083` | `SKY_RUNNER` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `084` | `SKY_RUNNER_FALLING` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `085` | `BULLDOZER` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `086` | `TESSIE` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `087` | `CITY_BUS` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `088` | `FUZZY_PICKLES` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `089` | `DELIVERY` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `090` | `RETURN_TO_YOUR_BODY` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `091` | `PHASE_DISTORTER_TIME_TRAVEL` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `092` | `COFFEE_BREAK` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `093` | `BECAUSE_I_LOVE_YOU` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `094` | `GOOD_FRIENDS_BAD_FRIENDS` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `095` | `SMILES_AND_TEARS` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `096` | `VS_CRANKY_LADY` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `097` | `VS_SPINNING_ROBO` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `098` | `VS_STRUTTIN_EVIL_MUSHROOM` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `099` | `VS_MASTER_BELCH` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `100` | `VS_NEW_AGE_RETRO_HIPPIE` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `101` | `VS_RUNAWAY_DOG` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `102` | `VS_CAVE_BOY` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `103` | `VS_YOUR_SANCTUARY_BOSS` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `104` | `VS_KRAKEN` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `105` | `POKEY_MEANS_BUSINESS` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `106` | `INSIDE_THE_DUNGEON` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `107` | `MEGATON_WALK` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `108` | `SEA_OF_EDEN2` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `109` | `EXPLOSION` | `finite_candidate` | `needs_driver_end_or_silence_detection` | `render_until_driver_end_or_sustained_silence_then_trim_tail` | name_based_candidate |
| `110` | `SKY_RUNNER_CRASH` | `finite_candidate` | `needs_driver_end_or_silence_detection` | `render_until_driver_end_or_sustained_silence_then_trim_tail` | name_based_candidate |
| `111` | `MAGIC_CAKE` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `112` | `POKEYS_HOUSE_BUZZ_BUZZ` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `113` | `BUZZ_BUZZ_SWATTED` | `finite_candidate` | `needs_driver_end_or_silence_detection` | `render_until_driver_end_or_sustained_silence_then_trim_tail` | name_based_candidate |
| `114` | `ONETT_AT_NIGHT_BUZZ_BUZZ` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `115` | `PHONE_CALL` | `finite_candidate` | `needs_driver_end_or_silence_detection` | `render_until_driver_end_or_sustained_silence_then_trim_tail` | name_based_candidate |
| `116` | `KNOCK_KNOCK_RIGHT` | `finite_candidate` | `needs_driver_end_or_silence_detection` | `render_until_driver_end_or_sustained_silence_then_trim_tail` | name_based_candidate |
| `117` | `RABBIT_CAVE` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `118` | `ONETT_AT_NIGHT_3` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `119` | `APPLE_OF_ENLIGHTENMENT` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `120` | `HOTEL_OF_THE_LIVING_DEAD` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `121` | `ONETT_INTRO` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `122` | `SUNRISE_ONETT` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `123` | `SOMEONE_JOINS` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `124` | `ENTER_STARMAN_JR` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `125` | `BOARDING_SCHOOL` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `126` | `PHASE_DISTORTER` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `127` | `PHASE_DISTORTER_2` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `128` | `BOY_MEETS_GIRL` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `129` | `HAPPY_THREED` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `130` | `RUNAWAY5_ARE_FREED` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `131` | `FLYING_MAN` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `132` | `ONETT_AT_NIGHT_2` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `133` | `HIDDEN_SONG` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `134` | `YOUR_SANCTUARY_BOSS` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `135` | `TELEPORT_IN` | `finite_candidate` | `needs_driver_end_or_silence_detection` | `render_until_driver_end_or_sustained_silence_then_trim_tail` | name_based_candidate |
| `136` | `SATURN_VALLEY_CAVE` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `137` | `ELEVATOR_DOWN` | `finite_candidate` | `needs_driver_end_or_silence_detection` | `render_until_driver_end_or_sustained_silence_then_trim_tail` | name_based_candidate |
| `138` | `ELEVATOR_UP` | `finite_candidate` | `needs_driver_end_or_silence_detection` | `render_until_driver_end_or_sustained_silence_then_trim_tail` | name_based_candidate |
| `139` | `ELEVATOR_STOP` | `finite_candidate` | `needs_driver_end_or_silence_detection` | `render_until_driver_end_or_sustained_silence_then_trim_tail` | name_based_candidate |
| `140` | `TOPOLLA_THEATRE` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `141` | `VS_MASTER_BARF` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `142` | `GOING_TO_MAGICANT` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `143` | `LEAVING_MAGICANT` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `144` | `KRAKEN_DEFEATED` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `145` | `STONEHENGE_DESTRUCTION` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `146` | `TESSIE_SIGHTING` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `147` | `METEOR_FALL` | `finite_candidate` | `needs_driver_end_or_silence_detection` | `render_until_driver_end_or_sustained_silence_then_trim_tail` | name_based_candidate |
| `148` | `VS_STARMAN_JR` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `149` | `RUNAWAY5_HELP_OUT` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `150` | `KNOCK_KNOCK` | `finite_candidate` | `needs_driver_end_or_silence_detection` | `render_until_driver_end_or_sustained_silence_then_trim_tail` | name_based_candidate |
| `151` | `ONETT_AFTER_METEOR1` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `152` | `ONETT_AFTER_METEOR2` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `153` | `POKEY_THEME` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `154` | `ONETT_AT_NIGHT_BUZZ_BUZZ2` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `155` | `YOUR_SANCTUARY_BOSS2` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `156` | `METEOR_STRIKE` | `finite_candidate` | `needs_driver_end_or_silence_detection` | `render_until_driver_end_or_sustained_silence_then_trim_tail` | name_based_candidate |
| `157` | `ATTRACT_MODE` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `158` | `NAME_CONFIRMATION` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `159` | `PEACEFUL_REST_VALLEY2` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `160` | `SOUNDSTONE_RECORDING_GIANT_STEP` | `finite_candidate` | `needs_driver_end_or_silence_detection` | `render_until_driver_end_or_sustained_silence_then_trim_tail` | name_based_candidate |
| `161` | `SOUNDSTONE_RECORDING_LILLIPUT_STEPS` | `finite_candidate` | `needs_driver_end_or_silence_detection` | `render_until_driver_end_or_sustained_silence_then_trim_tail` | name_based_candidate |
| `162` | `SOUNDSTONE_RECORDING_MILKY_WELL` | `finite_candidate` | `needs_driver_end_or_silence_detection` | `render_until_driver_end_or_sustained_silence_then_trim_tail` | name_based_candidate |
| `163` | `SOUNDSTONE_RECORDING_RAINY_CIRCLE` | `finite_candidate` | `needs_driver_end_or_silence_detection` | `render_until_driver_end_or_sustained_silence_then_trim_tail` | name_based_candidate |
| `164` | `SOUNDSTONE_RECORDING_MAGNET_HILL` | `finite_candidate` | `needs_driver_end_or_silence_detection` | `render_until_driver_end_or_sustained_silence_then_trim_tail` | name_based_candidate |
| `165` | `SOUNDSTONE_RECORDING_PINK_CLOUD` | `finite_candidate` | `needs_driver_end_or_silence_detection` | `render_until_driver_end_or_sustained_silence_then_trim_tail` | name_based_candidate |
| `166` | `SOUNDSTONE_RECORDING_LUMINE_HALL` | `finite_candidate` | `needs_driver_end_or_silence_detection` | `render_until_driver_end_or_sustained_silence_then_trim_tail` | name_based_candidate |
| `167` | `SOUNDSTONE_RECORDING_FIRE_SPRING` | `finite_candidate` | `needs_driver_end_or_silence_detection` | `render_until_driver_end_or_sustained_silence_then_trim_tail` | name_based_candidate |
| `168` | `SOUNDSTONE_BGM` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `169` | `EIGHT_MELODIES` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `170` | `DALAAM_INTRO` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `171` | `WINTERS_INTRO` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `172` | `POKEY_ESCAPES` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `173` | `GOOD_MORNING_MOONSIDE` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `174` | `GAS_STATION_2` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `175` | `TITLE_SCREEN` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `176` | `BATTLE_SWIRL4` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `177` | `POKEY_INTRO` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `178` | `GOOD_MORNING_SCARABA` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `179` | `ROBOTOMY1` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `180` | `POKEY_ESCAPES2` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `181` | `RETURN_TO_YOUR_BODY2` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `182` | `GIYGAS_STATIC` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `183` | `SUDDEN_VICTORY` | `finite_candidate` | `needs_driver_end_or_silence_detection` | `render_until_driver_end_or_sustained_silence_then_trim_tail` | name_based_candidate |
| `184` | `YOU_WON3` | `finite_candidate` | `needs_driver_end_or_silence_detection` | `render_until_driver_end_or_sustained_silence_then_trim_tail` | name_based_candidate |
| `185` | `GIYGAS_PHASE3` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `186` | `GIYGAS_PHASE1` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `187` | `GIVE_US_STRENGTH` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `188` | `GOOD_MORNING2` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `189` | `SOUND_STONE` | `unknown_candidate` | `needs_sequence_or_runtime_analysis` | `keep_diagnostic_preview_until_duration_is_measured` | unclassified |
| `190` | `GIYGAS_DEATH` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
| `191` | `GIYGAS_WEAKENED` | `looping_candidate` | `needs_loop_point_detection` | `export_loop_metadata_and_render_intro_plus_two_loops_with_fade_for_preview` | name_based_candidate |
