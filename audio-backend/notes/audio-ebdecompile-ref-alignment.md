# Audio eb-decompile Reference Alignment

Status: direct song-file payload alignment built; in-engine sub-song alignment remains separate work.

## Summary

- songs.yml entries: `191`
- direct ref song files: `171`
- direct ref payload matches: `169`
- contract sequence-pack matches: `169`
- song-reference entries: `5`
- in-engine entries: `15`
- alignment statuses: `{'in_engine_subsong_reference': 15, 'no_matching_contract_sequence_block': 2, 'payload_matches_contract_sequence_block': 169, 'song_references_another_track': 5}`

## First 80 Tracks

| Track | Name | Contract sequence pack | Ref song pack | Status | Ref file |
| ---: | --- | ---: | --- | --- | --- |
| `1` | GAS_STATION | `1` | `0x01` | `no_matching_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/01/song-01.ebm` |
| `2` | NAMING_SCREEN | `4` | `0x04` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/04/song-02.ebm` |
| `3` | SETUP_SCREEN | `4` | `0x04` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/04/song-03.ebm` |
| `4` | NONE2 | `None` | `in-engine` | `in_engine_subsong_reference` | `` |
| `5` | YOU_WON1 | `None` | `in-engine` | `in_engine_subsong_reference` | `` |
| `6` | LEVEL_UP | `None` | `in-engine` | `in_engine_subsong_reference` | `` |
| `7` | YOU_LOSE | `6` | `0x06` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/06/song-07.ebm` |
| `8` | BATTLE_SWIRL1 | `None` | `in-engine` | `in_engine_subsong_reference` | `` |
| `9` | BATTLE_SWIRL2 | `None` | `in-engine` | `in_engine_subsong_reference` | `` |
| `10` | WHAT_THE_HECK | `None` | `None` | `song_references_another_track` | `` |
| `11` | NEW_FRIEND | `None` | `in-engine` | `in_engine_subsong_reference` | `` |
| `12` | YOU_WON2 | `None` | `in-engine` | `in_engine_subsong_reference` | `` |
| `13` | TELEPORT_OUT | `None` | `in-engine` | `in_engine_subsong_reference` | `` |
| `14` | TELEPORT_FAIL | `None` | `in-engine` | `in_engine_subsong_reference` | `` |
| `15` | FALLING_UNDERGROUND | `7` | `0x07` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/07/song-0F.ebm` |
| `16` | DR_ANDONUTS_LAB | `9` | `0x09` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/09/song-10.ebm` |
| `17` | MONOTOLI_BUILDING | `10` | `0x0A` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/0A/song-11.ebm` |
| `18` | SLOPPY_HOUSE | `11` | `0x0B` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/0B/song-12.ebm` |
| `19` | NEIGHBOURS_HOUSE | `12` | `0x0C` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/0C/song-13.ebm` |
| `20` | ARCADE | `13` | `0x0D` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/0D/song-14.ebm` |
| `21` | POKEYS_HOUSE | `14` | `0x0E` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/0E/song-15.ebm` |
| `22` | HOSPITAL | `15` | `0x0F` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/0F/song-16.ebm` |
| `23` | NESSS_HOUSE | `16` | `0x10` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/10/song-17.ebm` |
| `24` | PAULAS_THEME | `17` | `0x11` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/11/song-18.ebm` |
| `25` | CHAOS_THEATRE | `18` | `0x12` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/12/song-19.ebm` |
| `26` | HOTEL | `19` | `0x13` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/13/song-1A.ebm` |
| `27` | GOOD_MORNING | `19` | `0x13` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/13/song-1B.ebm` |
| `28` | DEPARTMENT_STORE | `20` | `0x14` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/14/song-1C.ebm` |
| `29` | ONETT_AT_NIGHT_1 | `22` | `0x16` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/16/song-1D.ebm` |
| `30` | YOUR_SANCTUARY_1 | `23` | `0x17` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/17/song-1E.ebm` |
| `31` | YOUR_SANCTUARY_2 | `23` | `0x17` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/17/song-1F.ebm` |
| `32` | GIANT_STEP | `25` | `0x19` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/19/song-20.ebm` |
| `33` | LILLIPUT_STEPS | `25` | `0x19` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/19/song-21.ebm` |
| `34` | MILKY_WELL | `25` | `0x19` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/19/song-22.ebm` |
| `35` | RAINY_CIRCLE | `25` | `0x19` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/19/song-23.ebm` |
| `36` | MAGNET_HILL | `25` | `0x19` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/19/song-24.ebm` |
| `37` | PINK_CLOUD | `25` | `0x19` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/19/song-25.ebm` |
| `38` | LUMINE_HALL | `25` | `0x19` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/19/song-26.ebm` |
| `39` | FIRE_SPRING | `25` | `0x19` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/19/song-27.ebm` |
| `40` | NEAR_A_BOSS | `26` | `0x1A` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/1A/song-28.ebm` |
| `41` | ALIEN_INVESTIGATION | `28` | `0x1C` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/1C/song-29.ebm` |
| `42` | FIRE_SPRINGS_HALL | `29` | `0x1D` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/1D/song-2A.ebm` |
| `43` | BELCH_BASE | `30` | `0x1E` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/1E/song-2B.ebm` |
| `44` | ZOMBIE_THREED | `31` | `0x1F` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/1F/song-2C.ebm` |
| `45` | SPOOKY_CAVE | `32` | `0x20` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/20/song-2D.ebm` |
| `46` | ONETT | `34` | `None` | `song_references_another_track` | `` |
| `47` | FOURSIDE | `36` | `0x24` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/24/song-2F.ebm` |
| `48` | SATURN_VALLEY | `38` | `0x26` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/26/song-30.ebm` |
| `49` | MONKEY_CAVES | `39` | `0x27` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/27/song-31.ebm` |
| `50` | MOONSIDE | `41` | `0x29` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/29/song-32.ebm` |
| `51` | DUSTY_DUNES_DESERT | `43` | `0x2B` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/2B/song-33.ebm` |
| `52` | PEACEFUL_REST_VALLEY | `45` | `0x2D` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/2D/song-34.ebm` |
| `53` | ZOMBIE_THREED2 | `46` | `0x2E` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/2E/song-35.ebm` |
| `54` | WINTERS | `48` | `0x30` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/30/song-36.ebm` |
| `55` | CAVE_NEAR_A_BOSS | `49` | `0x31` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/31/song-37.ebm` |
| `56` | SUMMERS | `51` | `0x33` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/33/song-38.ebm` |
| `57` | JACKIES_CAFE | `53` | `0x35` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/35/song-39.ebm` |
| `58` | SAILING_TO_SCARABA | `55` | `0x37` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/37/song-3A.ebm` |
| `59` | DALAAM | `57` | `0x39` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/39/song-3B.ebm` |
| `60` | MU_TRAINING | `59` | `0x3B` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/3B/song-3C.ebm` |
| `61` | BAZAAR | `61` | `0x3D` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/3D/song-3D.ebm` |
| `62` | SCARABA_DESERT | `62` | `0x3E` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/3E/song-3E.ebm` |
| `63` | PYRAMID | `63` | `0x3F` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/3F/song-3F.ebm` |
| `64` | DEEP_DARKNESS | `65` | `0x41` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/41/song-40.ebm` |
| `65` | TENDA_VILLAGE | `67` | `0x43` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/43/song-41.ebm` |
| `66` | WELCOME_HOME | `68` | `0x44` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/44/song-42.ebm` |
| `67` | SEA_OF_EDEN | `69` | `0x45` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/45/song-43.ebm` |
| `68` | LOST_UNDERWORLD | `71` | `0x47` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/47/song-44.ebm` |
| `69` | FIRST_STEP_BACK | `73` | `0x49` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/49/song-45.ebm` |
| `70` | SECOND_STEP_BACK | `75` | `0x4B` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/4B/song-46.ebm` |
| `71` | THE_PLACE | `77` | `0x4D` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/4D/song-47.ebm` |
| `72` | GIYGAS_AWAKENS | `77` | `0x4D` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/4D/song-48.ebm` |
| `73` | GIYGAS_PHASE2 | `79` | `0x4F` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/4F/song-49.ebm` |
| `74` | GIYGAS_WEAKENED2 | `81` | `0x51` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/51/song-4A.ebm` |
| `75` | GIYGAS_DEATH2 | `83` | `0x53` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/53/song-4B.ebm` |
| `76` | RUNAWAY5_CONCERT_1 | `85` | `0x55` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/55/song-4C.ebm` |
| `77` | RUNAWAY5_TOUR_BUS | `86` | `0x56` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/56/song-4D.ebm` |
| `78` | RUNAWAY5_CONCERT_2 | `87` | `0x57` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/57/song-4E.ebm` |
| `79` | POWER | `88` | `0x58` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/58/song-4F.ebm` |
| `80` | VENUS_CONCERT | `90` | `0x5A` | `payload_matches_contract_sequence_block` | `refs/eb-decompile-4ef92/Music/Packs/5A/song-50.ebm` |

## Findings

- Direct eb-decompile song files include a 4-byte load header followed by the sequence payload.
- Matching direct song files corroborate our LOAD_SPC700_DATA block extraction, destination, and payload hashing.
- In-engine songs are sub-song references inside pack 1 driver/runtime data rather than one file per top-level sequence pack, so they need a separate sub-song alignment pass.
- Song-to-reference entries intentionally reuse another track's song data and should be resolved before exact export planning treats them as independent sequences.

## Next Work

- resolve in-engine song files against pack 1's runtime sequence area
- use direct payload matches to seed future focused pack reports automatically
- feed song-to-reference reuse into exact-duration export planning
