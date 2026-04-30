# Audio Oracle Verification Report

Status: all-track near-oracle passed; independent external-emulator gate remains open.

- scope: `all_tracks`
- jobs: `190`
- statuses: `{'audio_equivalent_state_delta': 190}`
- oracle ids: `{'ares_full_change_music_load_apply_all_tracks_reference': 190}`
- oracle kinds: `{'backend_result_summary_import': 190}`

## Gates

- representative oracle gate passed: `True`
- independent emulator gate passed: `False`
- all-track oracle gate passed: `True`
- release-quality playback claim ready: `False`

## Audio Equivalence

- byte-exact WAV matches: `190 / 190`
- header register matches: `190 / 190`
- DSP register matches: `190 / 190`
- full APU RAM matches: `0 / 190`
- minimum normalized PCM correlation: `1.0`
- maximum alignment offset samples: `0`

## APU Region Matches

| Region | Matches |
| --- | ---: |
| `brr_sample_payloads` | 190 / 190 |
| `driver_and_overlay` | 0 / 190 |
| `full_apu_ram` | 0 / 190 |
| `runtime_tables_and_sequences` | 190 / 190 |

## Interpretation

- What this proves: The full snapshot-backed playback corpus has reference captures at the planned paths and every compared job meets the accepted oracle status set. Current ares-managed references produce byte-identical PCM with matching header/DSP state across all rendered tracks.
- Why not final: The current imported references are ares-managed near-oracle/backend-summary captures, not independent bsnes/Mesen/Mednafen captures. Release-quality playback should still wait for an independent external emulator gate or an explicit decision that the ares-managed gate is sufficient.
- Next step: Add an independent external-emulator capture path for a representative subset, then rerun collect/validate/report.

## Tracks

| Track | Name | Status | Oracle | WAV Exact | Offset | Correlation | DSP Match | Full RAM Match |
| ---: | --- | --- | --- | --- | ---: | ---: | --- | --- |
| `001` | `GAS_STATION` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `002` | `NAMING_SCREEN` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `003` | `SETUP_SCREEN` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `005` | `YOU_WON1` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `006` | `LEVEL_UP` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `007` | `YOU_LOSE` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `008` | `BATTLE_SWIRL1` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `009` | `BATTLE_SWIRL2` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `010` | `WHAT_THE_HECK` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `011` | `NEW_FRIEND` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `012` | `YOU_WON2` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `013` | `TELEPORT_OUT` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `014` | `TELEPORT_FAIL` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `015` | `FALLING_UNDERGROUND` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `016` | `DR_ANDONUTS_LAB` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `017` | `MONOTOLI_BUILDING` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `018` | `SLOPPY_HOUSE` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `019` | `NEIGHBOURS_HOUSE` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `020` | `ARCADE` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `021` | `POKEYS_HOUSE` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `022` | `HOSPITAL` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `023` | `NESSS_HOUSE` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `024` | `PAULAS_THEME` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `025` | `CHAOS_THEATRE` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `026` | `HOTEL` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `027` | `GOOD_MORNING` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `028` | `DEPARTMENT_STORE` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `029` | `ONETT_AT_NIGHT_1` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `030` | `YOUR_SANCTUARY_1` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `031` | `YOUR_SANCTUARY_2` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `032` | `GIANT_STEP` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `033` | `LILLIPUT_STEPS` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `034` | `MILKY_WELL` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `035` | `RAINY_CIRCLE` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `036` | `MAGNET_HILL` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `037` | `PINK_CLOUD` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `038` | `LUMINE_HALL` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `039` | `FIRE_SPRING` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `040` | `NEAR_A_BOSS` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `041` | `ALIEN_INVESTIGATION` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `042` | `FIRE_SPRINGS_HALL` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `043` | `BELCH_BASE` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `044` | `ZOMBIE_THREED` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `045` | `SPOOKY_CAVE` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `046` | `ONETT` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `047` | `FOURSIDE` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `048` | `SATURN_VALLEY` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `049` | `MONKEY_CAVES` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `050` | `MOONSIDE` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `051` | `DUSTY_DUNES_DESERT` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `052` | `PEACEFUL_REST_VALLEY` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `053` | `ZOMBIE_THREED2` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `054` | `WINTERS` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `055` | `CAVE_NEAR_A_BOSS` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `056` | `SUMMERS` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `057` | `JACKIES_CAFE` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `058` | `SAILING_TO_SCARABA` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `059` | `DALAAM` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `060` | `MU_TRAINING` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `061` | `BAZAAR` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `062` | `SCARABA_DESERT` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `063` | `PYRAMID` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `064` | `DEEP_DARKNESS` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `065` | `TENDA_VILLAGE` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `066` | `WELCOME_HOME` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `067` | `SEA_OF_EDEN` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `068` | `LOST_UNDERWORLD` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `069` | `FIRST_STEP_BACK` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `070` | `SECOND_STEP_BACK` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `071` | `THE_PLACE` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `072` | `GIYGAS_AWAKENS` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `073` | `GIYGAS_PHASE2` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `074` | `GIYGAS_WEAKENED2` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `075` | `GIYGAS_DEATH2` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `076` | `RUNAWAY5_CONCERT_1` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `077` | `RUNAWAY5_TOUR_BUS` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `078` | `RUNAWAY5_CONCERT_2` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `079` | `POWER` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `080` | `VENUS_CONCERT` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `081` | `YELLOW_SUBMARINE` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `082` | `BICYCLE` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `083` | `SKY_RUNNER` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `084` | `SKY_RUNNER_FALLING` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `085` | `BULLDOZER` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `086` | `TESSIE` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `087` | `CITY_BUS` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `088` | `FUZZY_PICKLES` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `089` | `DELIVERY` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `090` | `RETURN_TO_YOUR_BODY` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `091` | `PHASE_DISTORTER_TIME_TRAVEL` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `092` | `COFFEE_BREAK` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `093` | `BECAUSE_I_LOVE_YOU` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `094` | `GOOD_FRIENDS_BAD_FRIENDS` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `095` | `SMILES_AND_TEARS` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `096` | `VS_CRANKY_LADY` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `097` | `VS_SPINNING_ROBO` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `098` | `VS_STRUTTIN_EVIL_MUSHROOM` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `099` | `VS_MASTER_BELCH` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `100` | `VS_NEW_AGE_RETRO_HIPPIE` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `101` | `VS_RUNAWAY_DOG` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `102` | `VS_CAVE_BOY` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `103` | `VS_YOUR_SANCTUARY_BOSS` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `104` | `VS_KRAKEN` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `105` | `POKEY_MEANS_BUSINESS` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `106` | `INSIDE_THE_DUNGEON` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `107` | `MEGATON_WALK` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `108` | `SEA_OF_EDEN2` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `109` | `EXPLOSION` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `110` | `SKY_RUNNER_CRASH` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `111` | `MAGIC_CAKE` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `112` | `POKEYS_HOUSE_BUZZ_BUZZ` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `113` | `BUZZ_BUZZ_SWATTED` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `114` | `ONETT_AT_NIGHT_BUZZ_BUZZ` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `115` | `PHONE_CALL` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `116` | `KNOCK_KNOCK_RIGHT` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `117` | `RABBIT_CAVE` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `118` | `ONETT_AT_NIGHT_3` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `119` | `APPLE_OF_ENLIGHTENMENT` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `120` | `HOTEL_OF_THE_LIVING_DEAD` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `121` | `ONETT_INTRO` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `122` | `SUNRISE_ONETT` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `123` | `SOMEONE_JOINS` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `124` | `ENTER_STARMAN_JR` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `125` | `BOARDING_SCHOOL` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `126` | `PHASE_DISTORTER` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `127` | `PHASE_DISTORTER_2` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `128` | `BOY_MEETS_GIRL` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `129` | `HAPPY_THREED` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `130` | `RUNAWAY5_ARE_FREED` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `131` | `FLYING_MAN` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `132` | `ONETT_AT_NIGHT_2` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `133` | `HIDDEN_SONG` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `134` | `YOUR_SANCTUARY_BOSS` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `135` | `TELEPORT_IN` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `136` | `SATURN_VALLEY_CAVE` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `137` | `ELEVATOR_DOWN` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `138` | `ELEVATOR_UP` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `139` | `ELEVATOR_STOP` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `140` | `TOPOLLA_THEATRE` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `141` | `VS_MASTER_BARF` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `142` | `GOING_TO_MAGICANT` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `143` | `LEAVING_MAGICANT` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `144` | `KRAKEN_DEFEATED` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `145` | `STONEHENGE_DESTRUCTION` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `146` | `TESSIE_SIGHTING` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `147` | `METEOR_FALL` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `148` | `VS_STARMAN_JR` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `149` | `RUNAWAY5_HELP_OUT` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `150` | `KNOCK_KNOCK` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `151` | `ONETT_AFTER_METEOR1` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `152` | `ONETT_AFTER_METEOR2` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `153` | `POKEY_THEME` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `154` | `ONETT_AT_NIGHT_BUZZ_BUZZ2` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `155` | `YOUR_SANCTUARY_BOSS2` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `156` | `METEOR_STRIKE` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `157` | `ATTRACT_MODE` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `158` | `NAME_CONFIRMATION` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `159` | `PEACEFUL_REST_VALLEY2` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `160` | `SOUNDSTONE_RECORDING_GIANT_STEP` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `161` | `SOUNDSTONE_RECORDING_LILLIPUT_STEPS` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `162` | `SOUNDSTONE_RECORDING_MILKY_WELL` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `163` | `SOUNDSTONE_RECORDING_RAINY_CIRCLE` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `164` | `SOUNDSTONE_RECORDING_MAGNET_HILL` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `165` | `SOUNDSTONE_RECORDING_PINK_CLOUD` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `166` | `SOUNDSTONE_RECORDING_LUMINE_HALL` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `167` | `SOUNDSTONE_RECORDING_FIRE_SPRING` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `168` | `SOUNDSTONE_BGM` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `169` | `EIGHT_MELODIES` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `170` | `DALAAM_INTRO` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `171` | `WINTERS_INTRO` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `172` | `POKEY_ESCAPES` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `173` | `GOOD_MORNING_MOONSIDE` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `174` | `GAS_STATION_2` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `175` | `TITLE_SCREEN` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `176` | `BATTLE_SWIRL4` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `177` | `POKEY_INTRO` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `178` | `GOOD_MORNING_SCARABA` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `179` | `ROBOTOMY1` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `180` | `POKEY_ESCAPES2` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `181` | `RETURN_TO_YOUR_BODY2` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `182` | `GIYGAS_STATIC` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `183` | `SUDDEN_VICTORY` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `184` | `YOU_WON3` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `185` | `GIYGAS_PHASE3` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `186` | `GIYGAS_PHASE1` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `187` | `GIVE_US_STRENGTH` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `188` | `GOOD_MORNING2` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `189` | `SOUND_STONE` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `190` | `GIYGAS_DEATH` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
| `191` | `GIYGAS_WEAKENED` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_all_tracks_reference` | yes | 0 | 1.0 | yes | no |
