# Map Object Bundle Contract

This contract is the portable placed-object view over the current map-object work.
It combines the visual role contract, movement/actionscript pointer join, map sector
position, event flag, and text pointer fields into one row per placed NPC object.

## Summary

- placed objects: `1582`
- NPC config rows: `1584`
- unplaced NPC config rows: `2`
- sectors with objects: `627`
- objects with event flags: `868`
- objects with primary text pointers: `1314`
- objects with secondary text pointers: `250`
- objects without present behavior script files in refs: `21`

## Visual Role Resolution

| Resolution | Objects |
| --- | ---: |
| `full_animation_role_contract` | 732 |
| `rom_runtime_slot_contract` | 850 |

## Behavior Source Status

| Status | Objects |
| --- | ---: |
| `script_file_missing` | 21 |
| `script_file_present` | 1561 |

## Behavior Buckets

| Bucket | Objects |
| --- | ---: |
| `physics_callback_movement` | 737 |
| `task_backed_actionscript` | 660 |
| `script_loop_or_wait` | 151 |
| `unresolved_pointer_target` | 21 |
| `event_actionscript_payload` | 13 |

## Top Sectors By Object Count

| Sector | Objects | Top sprites | Behavior buckets |
| --- | ---: | --- | --- |
| `39,31` | 21 | OVERWORLD_SPRITE::ZOMBIE_GLUED_TO_FLOOR (7), OVERWORLD_SPRITE::ZOMBIE_LYING_DOWN (5), OVERWORLD_SPRITE::URBAN_ZOMBIE (3) | physics_callback_movement (15), task_backed_actionscript (6) |
| `23,30` | 18 | OVERWORLD_SPRITE::MONKEY (4), SPRITE_GROUP_DR_ANDONUTS (2), SPRITE_GROUP_TESSIE_WATCHER (2) | physics_callback_movement (15), task_backed_actionscript (3) |
| `10,9` | 15 | OVERWORLD_SPRITE::LIL_TENDA (10), SPRITE_GROUP_SIGN (1), SPRITE_GROUP_LIL_TALKING_STONE (1) | physics_callback_movement (7), task_backed_actionscript (7), script_loop_or_wait (1) |
| `29,1` | 14 | SPRITE_GROUP_MR_SATURN (4), OVERWORLD_SPRITE::GIFT_BOX (4), SPRITE_GROUP_MINER (1) | physics_callback_movement (9), script_loop_or_wait (3), task_backed_actionscript (2) |
| `1,29` | 12 | OVERWORLD_SPRITE::MOM (2), SPRITE_GROUP_FRANK (2), SPRITE_GROUP_DRAPES_CLOSED (1) | task_backed_actionscript (9), physics_callback_movement (2), script_loop_or_wait (1) |
| `35,21` | 12 | OVERWORLD_SPRITE::BUS_STOP_SIGN (2), OVERWORLD_SPRITE::HOTEL_SIGN (1), OVERWORLD_SPRITE::SCUZZY_GUY (1) | physics_callback_movement (7), task_backed_actionscript (3), script_loop_or_wait (1) |
| `16,6` | 11 | OVERWORLD_SPRITE::HAPPY_TURBAN_GUY (2), OVERWORLD_SPRITE::MUSTACHE_ARAB_TURBAN_GUY (2), SPRITE_GROUP_PREET_PROOT_GUY (2) | task_backed_actionscript (8), physics_callback_movement (2), unresolved_pointer_target (1) |
| `13,2` | 10 | OVERWORLD_SPRITE::UNKNOWN (4), SPRITE_GROUP_TESSIE_WATCHER (2), OVERWORLD_SPRITE::INVISIBLE_2 (1) | physics_callback_movement (5), task_backed_actionscript (3), script_loop_or_wait (2) |
| `37,14` | 10 | SPRITE_GROUP_DIRT_SCOOPER (2), SPRITE_GROUP_MAGIC_TART_STAND (1), OVERWORLD_SPRITE::I_LOVE_QOWGA_SHIRT_GUY (1) | task_backed_actionscript (6), physics_callback_movement (3), unresolved_pointer_target (1) |
| `0,8` | 9 | OVERWORLD_SPRITE::POLICE_BARRIER (2), SPRITE_GROUP_COP_IN_SUNGLASSES (2), OVERWORLD_SPRITE::METEOR (1) | physics_callback_movement (6), task_backed_actionscript (3) |
| `7,30` | 9 | OVERWORLD_SPRITE::GIFT_BOX (7), OVERWORLD_SPRITE::ORANGE_HAIRED_NERD_KID (1), OVERWORLD_SPRITE::I_LOVE_QOWGA_SHIRT_GUY (1) | physics_callback_movement (7), task_backed_actionscript (2) |
| `15,10` | 9 | SPRITE_GROUP_CHARRED_HUMAN (1), SPRITE_GROUP_EVERDRED_LYING_DOWN (1), SPRITE_GROUP_BRUNETTE_SHOPPING_LADY (1) | task_backed_actionscript (6), physics_callback_movement (3) |
| `23,23` | 9 | SPRITE_GROUP_RUNAWAY_FIVE_BASS_PLAYER (1), SPRITE_GROUP_LUCKY (1), SPRITE_GROUP_CLUMSY_ROBOT (1) | task_backed_actionscript (7), physics_callback_movement (2) |
| `33,26` | 9 | SPRITE_GROUP_FAT_GUY_IN_RED_SUIT (1), SPRITE_GROUP_BLONDE_LADY_RED_DRESS (1), SPRITE_GROUP_BLONDE_SHOPPING_LADY (1) | task_backed_actionscript (9) |
| `36,26` | 9 | SPRITE_GROUP_HOTEL_ATTENDANT (2), SPRITE_GROUP_TELEPHONE (1), SPRITE_GROUP_YOUNG_BLONDE_GUY_IN_BLUE (1) | task_backed_actionscript (5), physics_callback_movement (3), script_loop_or_wait (1) |
| `5,30` | 8 | SPRITE_GROUP_BLONDE_LADY_RED_DRESS (1), SPRITE_GROUP_BLONDE_GUY_IN_SUIT (1), OVERWORLD_SPRITE::ATM_MACHINE (1) | task_backed_actionscript (6), physics_callback_movement (2) |
| `8,30` | 8 | OVERWORLD_SPRITE::INSANE_CULTIST (2), OVERWORLD_SPRITE::ATM_MACHINE (1), SPRITE_GROUP_NERDY_REDHEAD (1) | physics_callback_movement (4), task_backed_actionscript (3), script_loop_or_wait (1) |
| `9,30` | 8 | OVERWORLD_SPRITE::INSANE_CULTIST (8) | physics_callback_movement (4), task_backed_actionscript (2), script_loop_or_wait (2) |
| `22,12` | 8 | SPRITE_GROUP_MR_SATURN (2), OVERWORLD_SPRITE::MR_SATURN_BALL_AND_CHAIN (2), SPRITE_GROUP_JAR_OF_FLY_HONEY (2) | physics_callback_movement (5), script_loop_or_wait (2), task_backed_actionscript (1) |
| `25,21` | 8 | OVERWORLD_SPRITE::BIG_SMILE_LADY (2), OVERWORLD_SPRITE::JUKEBOX (1), SPRITE_GROUP_JACKIE (1) | task_backed_actionscript (6), physics_callback_movement (2) |

## Unplaced NPC Config Rows

| NPC ID | Sprite | Movement | Behavior |
| ---: | --- | ---: | --- |
| 0 | `SPRITE_GROUP_NESS` | 10 | `physics_callback_movement` |
| 1311 | `OVERWORLD_SPRITE::NONE` | 0 | `debug_cursor_loop` |

## Machine-Readable Data

The JSON file records `objects` with stable `map_object.NNNN` IDs and nested
`visual`, `behavior`, `interaction`, `classification`, `sector`, and `position` fields.
Behavior entries include the movement ID, ebsrc label, decoded C4 pointer-table
target address, source status, and expected ref script file when the local script
file is missing.
The behavior rows intentionally store compact movement IDs and source status; detailed
event macro and C3-reference profiles remain in `notes/map-movement-usage-contract.json`.
It also includes per-sector summaries and unplaced NPC config rows.

- JSON: `notes/map-object-bundles.json`
- generator: `tools/build_map_object_bundle_contract.py`
