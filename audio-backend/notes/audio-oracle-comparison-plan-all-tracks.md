# Audio Oracle Comparison Plan

Status: oracle comparison contract ready; reference capture runner pending.

- scope: `all_tracks`
- jobs: `190`
- source playback manifest: `build/audio/c0ab06-change-music-fusion-render-jobs-all/playback-export-manifest.json`
- generated output root: `build/audio/oracle-comparison-all-tracks`

## Reference Oracles

| Oracle | Status | Role | Integration policy |
| --- | --- | --- | --- |
| `ares` | `runner_pending` | permissive accuracy-first in-process/out-of-tree reference capture runner | preferred first implementation target because the project already has local ares harnesses |
| `mesen2_or_bsnes_higan_or_mednafen` | `optional_runner_pending` | external emulator validation oracle | use to corroborate ares/libgme output, not as a required app dependency |

## Comparison Policy

- SPC exactness: compare signatures, header registers, selected APU RAM region hashes, and DSP register snapshots where the reference exposes them
- PCM exactness: do not require byte-perfect PCM across independent renderers before alignment/timing has been characterized
- first gate: all representative jobs produce reference captures and classify as pass, audio_equivalent_state_delta, explained_timing_offset, or investigated_mismatch
- promotion gate: expand the same comparison contract from representative_tracks to all_tracks after the runner is stable
- PCM thresholds: `{'sample_rate': 32000, 'channels': 2, 'bits_per_sample': 16, 'minimum_seconds': 30.0, 'minimum_normalized_correlation_after_alignment': 0.98, 'maximum_leading_silence_delta_samples': 4096}`

## Workflow

1. Build or refresh this plan with `python tools/build_audio_oracle_comparison_plan.py`.
2. Capture a planned track with the reference emulator as SPC plus 32 kHz stereo WAV.
3. Import that capture with `python tools/import_audio_oracle_reference_capture.py --track-id <id> --spc <capture.spc> --wav <capture.wav> --oracle-id <emulator>`.
4. Collect comparison records with `python tools/collect_audio_oracle_comparison_results.py`.
5. Validate the gate with `python tools/validate_audio_oracle_comparison_summary.py`; add `--require-compared` only when the reference capture set should be complete.
6. After the representative gate is stable, regenerate with `--all-tracks` and use the same import/collect/validate flow.

Current ares-managed near-oracle result: full CHANGE_MUSIC/load-apply captures for the representative set classify `20 / 20` as `audio_equivalent_state_delta`: PCM output is byte-identical/zero-offset equivalent while full APU RAM differs in non-audio-affecting regions, with matching header registers and DSP registers.

## Release Gates

- Reference captures must be generated locally from a user-provided ROM.
- Reference SPC/WAV/PCM outputs must stay under ignored build/audio paths.
- Each mismatch must be classified as timing offset, renderer difference, snapshot-state difference, or unknown.
- Representative-track oracle comparison must pass before claiming release-quality audio playback/export.
- All-track oracle comparison should pass before claiming fully validated audio reconstruction.

## Jobs

| Track | Name | Source SPC | Comparison result path |
| ---: | --- | --- | --- |
| `001` | `GAS_STATION` | `fusion-track-001-gas_station-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-001-gas_station/oracle-comparison-result.json` |
| `002` | `NAMING_SCREEN` | `fusion-track-002-naming_screen-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-002-naming_screen/oracle-comparison-result.json` |
| `003` | `SETUP_SCREEN` | `fusion-track-003-setup_screen-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-003-setup_screen/oracle-comparison-result.json` |
| `005` | `YOU_WON1` | `fusion-track-005-you_won1-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-005-you_won1/oracle-comparison-result.json` |
| `006` | `LEVEL_UP` | `fusion-track-006-level_up-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-006-level_up/oracle-comparison-result.json` |
| `007` | `YOU_LOSE` | `fusion-track-007-you_lose-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-007-you_lose/oracle-comparison-result.json` |
| `008` | `BATTLE_SWIRL1` | `fusion-track-008-battle_swirl1-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-008-battle_swirl1/oracle-comparison-result.json` |
| `009` | `BATTLE_SWIRL2` | `fusion-track-009-battle_swirl2-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-009-battle_swirl2/oracle-comparison-result.json` |
| `010` | `WHAT_THE_HECK` | `fusion-track-010-what_the_heck-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-010-what_the_heck/oracle-comparison-result.json` |
| `011` | `NEW_FRIEND` | `fusion-track-011-new_friend-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-011-new_friend/oracle-comparison-result.json` |
| `012` | `YOU_WON2` | `fusion-track-012-you_won2-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-012-you_won2/oracle-comparison-result.json` |
| `013` | `TELEPORT_OUT` | `fusion-track-013-teleport_out-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-013-teleport_out/oracle-comparison-result.json` |
| `014` | `TELEPORT_FAIL` | `fusion-track-014-teleport_fail-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-014-teleport_fail/oracle-comparison-result.json` |
| `015` | `FALLING_UNDERGROUND` | `fusion-track-015-falling_underground-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-015-falling_underground/oracle-comparison-result.json` |
| `016` | `DR_ANDONUTS_LAB` | `fusion-track-016-dr_andonuts_lab-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-016-dr_andonuts_lab/oracle-comparison-result.json` |
| `017` | `MONOTOLI_BUILDING` | `fusion-track-017-monotoli_building-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-017-monotoli_building/oracle-comparison-result.json` |
| `018` | `SLOPPY_HOUSE` | `fusion-track-018-sloppy_house-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-018-sloppy_house/oracle-comparison-result.json` |
| `019` | `NEIGHBOURS_HOUSE` | `fusion-track-019-neighbours_house-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-019-neighbours_house/oracle-comparison-result.json` |
| `020` | `ARCADE` | `fusion-track-020-arcade-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-020-arcade/oracle-comparison-result.json` |
| `021` | `POKEYS_HOUSE` | `fusion-track-021-pokeys_house-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-021-pokeys_house/oracle-comparison-result.json` |
| `022` | `HOSPITAL` | `fusion-track-022-hospital-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-022-hospital/oracle-comparison-result.json` |
| `023` | `NESSS_HOUSE` | `fusion-track-023-nesss_house-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-023-nesss_house/oracle-comparison-result.json` |
| `024` | `PAULAS_THEME` | `fusion-track-024-paulas_theme-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-024-paulas_theme/oracle-comparison-result.json` |
| `025` | `CHAOS_THEATRE` | `fusion-track-025-chaos_theatre-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-025-chaos_theatre/oracle-comparison-result.json` |
| `026` | `HOTEL` | `fusion-track-026-hotel-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-026-hotel/oracle-comparison-result.json` |
| `027` | `GOOD_MORNING` | `fusion-track-027-good_morning-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-027-good_morning/oracle-comparison-result.json` |
| `028` | `DEPARTMENT_STORE` | `fusion-track-028-department_store-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-028-department_store/oracle-comparison-result.json` |
| `029` | `ONETT_AT_NIGHT_1` | `fusion-track-029-onett_at_night_1-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-029-onett_at_night_1/oracle-comparison-result.json` |
| `030` | `YOUR_SANCTUARY_1` | `fusion-track-030-your_sanctuary_1-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-030-your_sanctuary_1/oracle-comparison-result.json` |
| `031` | `YOUR_SANCTUARY_2` | `fusion-track-031-your_sanctuary_2-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-031-your_sanctuary_2/oracle-comparison-result.json` |
| `032` | `GIANT_STEP` | `fusion-track-032-giant_step-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-032-giant_step/oracle-comparison-result.json` |
| `033` | `LILLIPUT_STEPS` | `fusion-track-033-lilliput_steps-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-033-lilliput_steps/oracle-comparison-result.json` |
| `034` | `MILKY_WELL` | `fusion-track-034-milky_well-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-034-milky_well/oracle-comparison-result.json` |
| `035` | `RAINY_CIRCLE` | `fusion-track-035-rainy_circle-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-035-rainy_circle/oracle-comparison-result.json` |
| `036` | `MAGNET_HILL` | `fusion-track-036-magnet_hill-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-036-magnet_hill/oracle-comparison-result.json` |
| `037` | `PINK_CLOUD` | `fusion-track-037-pink_cloud-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-037-pink_cloud/oracle-comparison-result.json` |
| `038` | `LUMINE_HALL` | `fusion-track-038-lumine_hall-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-038-lumine_hall/oracle-comparison-result.json` |
| `039` | `FIRE_SPRING` | `fusion-track-039-fire_spring-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-039-fire_spring/oracle-comparison-result.json` |
| `040` | `NEAR_A_BOSS` | `fusion-track-040-near_a_boss-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-040-near_a_boss/oracle-comparison-result.json` |
| `041` | `ALIEN_INVESTIGATION` | `fusion-track-041-alien_investigation-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-041-alien_investigation/oracle-comparison-result.json` |
| `042` | `FIRE_SPRINGS_HALL` | `fusion-track-042-fire_springs_hall-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-042-fire_springs_hall/oracle-comparison-result.json` |
| `043` | `BELCH_BASE` | `fusion-track-043-belch_base-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-043-belch_base/oracle-comparison-result.json` |
| `044` | `ZOMBIE_THREED` | `fusion-track-044-zombie_threed-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-044-zombie_threed/oracle-comparison-result.json` |
| `045` | `SPOOKY_CAVE` | `fusion-track-045-spooky_cave-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-045-spooky_cave/oracle-comparison-result.json` |
| `046` | `ONETT` | `fusion-track-046-onett-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-046-onett/oracle-comparison-result.json` |
| `047` | `FOURSIDE` | `fusion-track-047-fourside-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-047-fourside/oracle-comparison-result.json` |
| `048` | `SATURN_VALLEY` | `fusion-track-048-saturn_valley-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-048-saturn_valley/oracle-comparison-result.json` |
| `049` | `MONKEY_CAVES` | `fusion-track-049-monkey_caves-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-049-monkey_caves/oracle-comparison-result.json` |
| `050` | `MOONSIDE` | `fusion-track-050-moonside-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-050-moonside/oracle-comparison-result.json` |
| `051` | `DUSTY_DUNES_DESERT` | `fusion-track-051-dusty_dunes_desert-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-051-dusty_dunes_desert/oracle-comparison-result.json` |
| `052` | `PEACEFUL_REST_VALLEY` | `fusion-track-052-peaceful_rest_valley-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-052-peaceful_rest_valley/oracle-comparison-result.json` |
| `053` | `ZOMBIE_THREED2` | `fusion-track-053-zombie_threed2-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-053-zombie_threed2/oracle-comparison-result.json` |
| `054` | `WINTERS` | `fusion-track-054-winters-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-054-winters/oracle-comparison-result.json` |
| `055` | `CAVE_NEAR_A_BOSS` | `fusion-track-055-cave_near_a_boss-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-055-cave_near_a_boss/oracle-comparison-result.json` |
| `056` | `SUMMERS` | `fusion-track-056-summers-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-056-summers/oracle-comparison-result.json` |
| `057` | `JACKIES_CAFE` | `fusion-track-057-jackies_cafe-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-057-jackies_cafe/oracle-comparison-result.json` |
| `058` | `SAILING_TO_SCARABA` | `fusion-track-058-sailing_to_scaraba-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-058-sailing_to_scaraba/oracle-comparison-result.json` |
| `059` | `DALAAM` | `fusion-track-059-dalaam-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-059-dalaam/oracle-comparison-result.json` |
| `060` | `MU_TRAINING` | `fusion-track-060-mu_training-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-060-mu_training/oracle-comparison-result.json` |
| `061` | `BAZAAR` | `fusion-track-061-bazaar-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-061-bazaar/oracle-comparison-result.json` |
| `062` | `SCARABA_DESERT` | `fusion-track-062-scaraba_desert-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-062-scaraba_desert/oracle-comparison-result.json` |
| `063` | `PYRAMID` | `fusion-track-063-pyramid-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-063-pyramid/oracle-comparison-result.json` |
| `064` | `DEEP_DARKNESS` | `fusion-track-064-deep_darkness-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-064-deep_darkness/oracle-comparison-result.json` |
| `065` | `TENDA_VILLAGE` | `fusion-track-065-tenda_village-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-065-tenda_village/oracle-comparison-result.json` |
| `066` | `WELCOME_HOME` | `fusion-track-066-welcome_home-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-066-welcome_home/oracle-comparison-result.json` |
| `067` | `SEA_OF_EDEN` | `fusion-track-067-sea_of_eden-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-067-sea_of_eden/oracle-comparison-result.json` |
| `068` | `LOST_UNDERWORLD` | `fusion-track-068-lost_underworld-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-068-lost_underworld/oracle-comparison-result.json` |
| `069` | `FIRST_STEP_BACK` | `fusion-track-069-first_step_back-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-069-first_step_back/oracle-comparison-result.json` |
| `070` | `SECOND_STEP_BACK` | `fusion-track-070-second_step_back-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-070-second_step_back/oracle-comparison-result.json` |
| `071` | `THE_PLACE` | `fusion-track-071-the_place-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-071-the_place/oracle-comparison-result.json` |
| `072` | `GIYGAS_AWAKENS` | `fusion-track-072-giygas_awakens-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-072-giygas_awakens/oracle-comparison-result.json` |
| `073` | `GIYGAS_PHASE2` | `fusion-track-073-giygas_phase2-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-073-giygas_phase2/oracle-comparison-result.json` |
| `074` | `GIYGAS_WEAKENED2` | `fusion-track-074-giygas_weakened2-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-074-giygas_weakened2/oracle-comparison-result.json` |
| `075` | `GIYGAS_DEATH2` | `fusion-track-075-giygas_death2-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-075-giygas_death2/oracle-comparison-result.json` |
| `076` | `RUNAWAY5_CONCERT_1` | `fusion-track-076-runaway5_concert_1-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-076-runaway5_concert_1/oracle-comparison-result.json` |
| `077` | `RUNAWAY5_TOUR_BUS` | `fusion-track-077-runaway5_tour_bus-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-077-runaway5_tour_bus/oracle-comparison-result.json` |
| `078` | `RUNAWAY5_CONCERT_2` | `fusion-track-078-runaway5_concert_2-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-078-runaway5_concert_2/oracle-comparison-result.json` |
| `079` | `POWER` | `fusion-track-079-power-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-079-power/oracle-comparison-result.json` |
| `080` | `VENUS_CONCERT` | `fusion-track-080-venus_concert-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-080-venus_concert/oracle-comparison-result.json` |
| `081` | `YELLOW_SUBMARINE` | `fusion-track-081-yellow_submarine-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-081-yellow_submarine/oracle-comparison-result.json` |
| `082` | `BICYCLE` | `fusion-track-082-bicycle-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-082-bicycle/oracle-comparison-result.json` |
| `083` | `SKY_RUNNER` | `fusion-track-083-sky_runner-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-083-sky_runner/oracle-comparison-result.json` |
| `084` | `SKY_RUNNER_FALLING` | `fusion-track-084-sky_runner_falling-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-084-sky_runner_falling/oracle-comparison-result.json` |
| `085` | `BULLDOZER` | `fusion-track-085-bulldozer-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-085-bulldozer/oracle-comparison-result.json` |
| `086` | `TESSIE` | `fusion-track-086-tessie-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-086-tessie/oracle-comparison-result.json` |
| `087` | `CITY_BUS` | `fusion-track-087-city_bus-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-087-city_bus/oracle-comparison-result.json` |
| `088` | `FUZZY_PICKLES` | `fusion-track-088-fuzzy_pickles-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-088-fuzzy_pickles/oracle-comparison-result.json` |
| `089` | `DELIVERY` | `fusion-track-089-delivery-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-089-delivery/oracle-comparison-result.json` |
| `090` | `RETURN_TO_YOUR_BODY` | `fusion-track-090-return_to_your_body-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-090-return_to_your_body/oracle-comparison-result.json` |
| `091` | `PHASE_DISTORTER_TIME_TRAVEL` | `fusion-track-091-phase_distorter_time_travel-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-091-phase_distorter_time_travel/oracle-comparison-result.json` |
| `092` | `COFFEE_BREAK` | `fusion-track-092-coffee_break-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-092-coffee_break/oracle-comparison-result.json` |
| `093` | `BECAUSE_I_LOVE_YOU` | `fusion-track-093-because_i_love_you-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-093-because_i_love_you/oracle-comparison-result.json` |
| `094` | `GOOD_FRIENDS_BAD_FRIENDS` | `fusion-track-094-good_friends_bad_friends-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-094-good_friends_bad_friends/oracle-comparison-result.json` |
| `095` | `SMILES_AND_TEARS` | `fusion-track-095-smiles_and_tears-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-095-smiles_and_tears/oracle-comparison-result.json` |
| `096` | `VS_CRANKY_LADY` | `fusion-track-096-vs_cranky_lady-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-096-vs_cranky_lady/oracle-comparison-result.json` |
| `097` | `VS_SPINNING_ROBO` | `fusion-track-097-vs_spinning_robo-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-097-vs_spinning_robo/oracle-comparison-result.json` |
| `098` | `VS_STRUTTIN_EVIL_MUSHROOM` | `fusion-track-098-vs_struttin_evil_mushroom-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-098-vs_struttin_evil_mushroom/oracle-comparison-result.json` |
| `099` | `VS_MASTER_BELCH` | `fusion-track-099-vs_master_belch-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-099-vs_master_belch/oracle-comparison-result.json` |
| `100` | `VS_NEW_AGE_RETRO_HIPPIE` | `fusion-track-100-vs_new_age_retro_hippie-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-100-vs_new_age_retro_hippie/oracle-comparison-result.json` |
| `101` | `VS_RUNAWAY_DOG` | `fusion-track-101-vs_runaway_dog-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-101-vs_runaway_dog/oracle-comparison-result.json` |
| `102` | `VS_CAVE_BOY` | `fusion-track-102-vs_cave_boy-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-102-vs_cave_boy/oracle-comparison-result.json` |
| `103` | `VS_YOUR_SANCTUARY_BOSS` | `fusion-track-103-vs_your_sanctuary_boss-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-103-vs_your_sanctuary_boss/oracle-comparison-result.json` |
| `104` | `VS_KRAKEN` | `fusion-track-104-vs_kraken-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-104-vs_kraken/oracle-comparison-result.json` |
| `105` | `POKEY_MEANS_BUSINESS` | `fusion-track-105-pokey_means_business-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-105-pokey_means_business/oracle-comparison-result.json` |
| `106` | `INSIDE_THE_DUNGEON` | `fusion-track-106-inside_the_dungeon-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-106-inside_the_dungeon/oracle-comparison-result.json` |
| `107` | `MEGATON_WALK` | `fusion-track-107-megaton_walk-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-107-megaton_walk/oracle-comparison-result.json` |
| `108` | `SEA_OF_EDEN2` | `fusion-track-108-sea_of_eden2-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-108-sea_of_eden2/oracle-comparison-result.json` |
| `109` | `EXPLOSION` | `fusion-track-109-explosion-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-109-explosion/oracle-comparison-result.json` |
| `110` | `SKY_RUNNER_CRASH` | `fusion-track-110-sky_runner_crash-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-110-sky_runner_crash/oracle-comparison-result.json` |
| `111` | `MAGIC_CAKE` | `fusion-track-111-magic_cake-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-111-magic_cake/oracle-comparison-result.json` |
| `112` | `POKEYS_HOUSE_BUZZ_BUZZ` | `fusion-track-112-pokeys_house_buzz_buzz-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-112-pokeys_house_buzz_buzz/oracle-comparison-result.json` |
| `113` | `BUZZ_BUZZ_SWATTED` | `fusion-track-113-buzz_buzz_swatted-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-113-buzz_buzz_swatted/oracle-comparison-result.json` |
| `114` | `ONETT_AT_NIGHT_BUZZ_BUZZ` | `fusion-track-114-onett_at_night_buzz_buzz-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-114-onett_at_night_buzz_buzz/oracle-comparison-result.json` |
| `115` | `PHONE_CALL` | `fusion-track-115-phone_call-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-115-phone_call/oracle-comparison-result.json` |
| `116` | `KNOCK_KNOCK_RIGHT` | `fusion-track-116-knock_knock_right-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-116-knock_knock_right/oracle-comparison-result.json` |
| `117` | `RABBIT_CAVE` | `fusion-track-117-rabbit_cave-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-117-rabbit_cave/oracle-comparison-result.json` |
| `118` | `ONETT_AT_NIGHT_3` | `fusion-track-118-onett_at_night_3-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-118-onett_at_night_3/oracle-comparison-result.json` |
| `119` | `APPLE_OF_ENLIGHTENMENT` | `fusion-track-119-apple_of_enlightenment-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-119-apple_of_enlightenment/oracle-comparison-result.json` |
| `120` | `HOTEL_OF_THE_LIVING_DEAD` | `fusion-track-120-hotel_of_the_living_dead-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-120-hotel_of_the_living_dead/oracle-comparison-result.json` |
| `121` | `ONETT_INTRO` | `fusion-track-121-onett_intro-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-121-onett_intro/oracle-comparison-result.json` |
| `122` | `SUNRISE_ONETT` | `fusion-track-122-sunrise_onett-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-122-sunrise_onett/oracle-comparison-result.json` |
| `123` | `SOMEONE_JOINS` | `fusion-track-123-someone_joins-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-123-someone_joins/oracle-comparison-result.json` |
| `124` | `ENTER_STARMAN_JR` | `fusion-track-124-enter_starman_jr-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-124-enter_starman_jr/oracle-comparison-result.json` |
| `125` | `BOARDING_SCHOOL` | `fusion-track-125-boarding_school-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-125-boarding_school/oracle-comparison-result.json` |
| `126` | `PHASE_DISTORTER` | `fusion-track-126-phase_distorter-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-126-phase_distorter/oracle-comparison-result.json` |
| `127` | `PHASE_DISTORTER_2` | `fusion-track-127-phase_distorter_2-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-127-phase_distorter_2/oracle-comparison-result.json` |
| `128` | `BOY_MEETS_GIRL` | `fusion-track-128-boy_meets_girl-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-128-boy_meets_girl/oracle-comparison-result.json` |
| `129` | `HAPPY_THREED` | `fusion-track-129-happy_threed-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-129-happy_threed/oracle-comparison-result.json` |
| `130` | `RUNAWAY5_ARE_FREED` | `fusion-track-130-runaway5_are_freed-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-130-runaway5_are_freed/oracle-comparison-result.json` |
| `131` | `FLYING_MAN` | `fusion-track-131-flying_man-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-131-flying_man/oracle-comparison-result.json` |
| `132` | `ONETT_AT_NIGHT_2` | `fusion-track-132-onett_at_night_2-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-132-onett_at_night_2/oracle-comparison-result.json` |
| `133` | `HIDDEN_SONG` | `fusion-track-133-hidden_song-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-133-hidden_song/oracle-comparison-result.json` |
| `134` | `YOUR_SANCTUARY_BOSS` | `fusion-track-134-your_sanctuary_boss-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-134-your_sanctuary_boss/oracle-comparison-result.json` |
| `135` | `TELEPORT_IN` | `fusion-track-135-teleport_in-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-135-teleport_in/oracle-comparison-result.json` |
| `136` | `SATURN_VALLEY_CAVE` | `fusion-track-136-saturn_valley_cave-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-136-saturn_valley_cave/oracle-comparison-result.json` |
| `137` | `ELEVATOR_DOWN` | `fusion-track-137-elevator_down-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-137-elevator_down/oracle-comparison-result.json` |
| `138` | `ELEVATOR_UP` | `fusion-track-138-elevator_up-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-138-elevator_up/oracle-comparison-result.json` |
| `139` | `ELEVATOR_STOP` | `fusion-track-139-elevator_stop-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-139-elevator_stop/oracle-comparison-result.json` |
| `140` | `TOPOLLA_THEATRE` | `fusion-track-140-topolla_theatre-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-140-topolla_theatre/oracle-comparison-result.json` |
| `141` | `VS_MASTER_BARF` | `fusion-track-141-vs_master_barf-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-141-vs_master_barf/oracle-comparison-result.json` |
| `142` | `GOING_TO_MAGICANT` | `fusion-track-142-going_to_magicant-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-142-going_to_magicant/oracle-comparison-result.json` |
| `143` | `LEAVING_MAGICANT` | `fusion-track-143-leaving_magicant-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-143-leaving_magicant/oracle-comparison-result.json` |
| `144` | `KRAKEN_DEFEATED` | `fusion-track-144-kraken_defeated-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-144-kraken_defeated/oracle-comparison-result.json` |
| `145` | `STONEHENGE_DESTRUCTION` | `fusion-track-145-stonehenge_destruction-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-145-stonehenge_destruction/oracle-comparison-result.json` |
| `146` | `TESSIE_SIGHTING` | `fusion-track-146-tessie_sighting-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-146-tessie_sighting/oracle-comparison-result.json` |
| `147` | `METEOR_FALL` | `fusion-track-147-meteor_fall-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-147-meteor_fall/oracle-comparison-result.json` |
| `148` | `VS_STARMAN_JR` | `fusion-track-148-vs_starman_jr-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-148-vs_starman_jr/oracle-comparison-result.json` |
| `149` | `RUNAWAY5_HELP_OUT` | `fusion-track-149-runaway5_help_out-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-149-runaway5_help_out/oracle-comparison-result.json` |
| `150` | `KNOCK_KNOCK` | `fusion-track-150-knock_knock-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-150-knock_knock/oracle-comparison-result.json` |
| `151` | `ONETT_AFTER_METEOR1` | `fusion-track-151-onett_after_meteor1-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-151-onett_after_meteor1/oracle-comparison-result.json` |
| `152` | `ONETT_AFTER_METEOR2` | `fusion-track-152-onett_after_meteor2-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-152-onett_after_meteor2/oracle-comparison-result.json` |
| `153` | `POKEY_THEME` | `fusion-track-153-pokey_theme-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-153-pokey_theme/oracle-comparison-result.json` |
| `154` | `ONETT_AT_NIGHT_BUZZ_BUZZ2` | `fusion-track-154-onett_at_night_buzz_buzz2-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-154-onett_at_night_buzz_buzz2/oracle-comparison-result.json` |
| `155` | `YOUR_SANCTUARY_BOSS2` | `fusion-track-155-your_sanctuary_boss2-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-155-your_sanctuary_boss2/oracle-comparison-result.json` |
| `156` | `METEOR_STRIKE` | `fusion-track-156-meteor_strike-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-156-meteor_strike/oracle-comparison-result.json` |
| `157` | `ATTRACT_MODE` | `fusion-track-157-attract_mode-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-157-attract_mode/oracle-comparison-result.json` |
| `158` | `NAME_CONFIRMATION` | `fusion-track-158-name_confirmation-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-158-name_confirmation/oracle-comparison-result.json` |
| `159` | `PEACEFUL_REST_VALLEY2` | `fusion-track-159-peaceful_rest_valley2-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-159-peaceful_rest_valley2/oracle-comparison-result.json` |
| `160` | `SOUNDSTONE_RECORDING_GIANT_STEP` | `fusion-track-160-soundstone_recording_giant_step-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-160-soundstone_recording_giant_step/oracle-comparison-result.json` |
| `161` | `SOUNDSTONE_RECORDING_LILLIPUT_STEPS` | `fusion-track-161-soundstone_recording_lilliput_steps-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-161-soundstone_recording_lilliput_steps/oracle-comparison-result.json` |
| `162` | `SOUNDSTONE_RECORDING_MILKY_WELL` | `fusion-track-162-soundstone_recording_milky_well-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-162-soundstone_recording_milky_well/oracle-comparison-result.json` |
| `163` | `SOUNDSTONE_RECORDING_RAINY_CIRCLE` | `fusion-track-163-soundstone_recording_rainy_circle-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-163-soundstone_recording_rainy_circle/oracle-comparison-result.json` |
| `164` | `SOUNDSTONE_RECORDING_MAGNET_HILL` | `fusion-track-164-soundstone_recording_magnet_hill-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-164-soundstone_recording_magnet_hill/oracle-comparison-result.json` |
| `165` | `SOUNDSTONE_RECORDING_PINK_CLOUD` | `fusion-track-165-soundstone_recording_pink_cloud-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-165-soundstone_recording_pink_cloud/oracle-comparison-result.json` |
| `166` | `SOUNDSTONE_RECORDING_LUMINE_HALL` | `fusion-track-166-soundstone_recording_lumine_hall-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-166-soundstone_recording_lumine_hall/oracle-comparison-result.json` |
| `167` | `SOUNDSTONE_RECORDING_FIRE_SPRING` | `fusion-track-167-soundstone_recording_fire_spring-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-167-soundstone_recording_fire_spring/oracle-comparison-result.json` |
| `168` | `SOUNDSTONE_BGM` | `fusion-track-168-soundstone_bgm-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-168-soundstone_bgm/oracle-comparison-result.json` |
| `169` | `EIGHT_MELODIES` | `fusion-track-169-eight_melodies-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-169-eight_melodies/oracle-comparison-result.json` |
| `170` | `DALAAM_INTRO` | `fusion-track-170-dalaam_intro-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-170-dalaam_intro/oracle-comparison-result.json` |
| `171` | `WINTERS_INTRO` | `fusion-track-171-winters_intro-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-171-winters_intro/oracle-comparison-result.json` |
| `172` | `POKEY_ESCAPES` | `fusion-track-172-pokey_escapes-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-172-pokey_escapes/oracle-comparison-result.json` |
| `173` | `GOOD_MORNING_MOONSIDE` | `fusion-track-173-good_morning_moonside-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-173-good_morning_moonside/oracle-comparison-result.json` |
| `174` | `GAS_STATION_2` | `fusion-track-174-gas_station_2-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-174-gas_station_2/oracle-comparison-result.json` |
| `175` | `TITLE_SCREEN` | `fusion-track-175-title_screen-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-175-title_screen/oracle-comparison-result.json` |
| `176` | `BATTLE_SWIRL4` | `fusion-track-176-battle_swirl4-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-176-battle_swirl4/oracle-comparison-result.json` |
| `177` | `POKEY_INTRO` | `fusion-track-177-pokey_intro-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-177-pokey_intro/oracle-comparison-result.json` |
| `178` | `GOOD_MORNING_SCARABA` | `fusion-track-178-good_morning_scaraba-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-178-good_morning_scaraba/oracle-comparison-result.json` |
| `179` | `ROBOTOMY1` | `fusion-track-179-robotomy1-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-179-robotomy1/oracle-comparison-result.json` |
| `180` | `POKEY_ESCAPES2` | `fusion-track-180-pokey_escapes2-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-180-pokey_escapes2/oracle-comparison-result.json` |
| `181` | `RETURN_TO_YOUR_BODY2` | `fusion-track-181-return_to_your_body2-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-181-return_to_your_body2/oracle-comparison-result.json` |
| `182` | `GIYGAS_STATIC` | `fusion-track-182-giygas_static-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-182-giygas_static/oracle-comparison-result.json` |
| `183` | `SUDDEN_VICTORY` | `fusion-track-183-sudden_victory-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-183-sudden_victory/oracle-comparison-result.json` |
| `184` | `YOU_WON3` | `fusion-track-184-you_won3-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-184-you_won3/oracle-comparison-result.json` |
| `185` | `GIYGAS_PHASE3` | `fusion-track-185-giygas_phase3-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-185-giygas_phase3/oracle-comparison-result.json` |
| `186` | `GIYGAS_PHASE1` | `fusion-track-186-giygas_phase1-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-186-giygas_phase1/oracle-comparison-result.json` |
| `187` | `GIVE_US_STRENGTH` | `fusion-track-187-give_us_strength-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-187-give_us_strength/oracle-comparison-result.json` |
| `188` | `GOOD_MORNING2` | `fusion-track-188-good_morning2-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-188-good_morning2/oracle-comparison-result.json` |
| `189` | `SOUND_STONE` | `fusion-track-189-sound_stone-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-189-sound_stone/oracle-comparison-result.json` |
| `190` | `GIYGAS_DEATH` | `fusion-track-190-giygas_death-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-190-giygas_death/oracle-comparison-result.json` |
| `191` | `GIYGAS_WEAKENED` | `fusion-track-191-giygas_weakened-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison-all-tracks/track-191-giygas_weakened/oracle-comparison-result.json` |
