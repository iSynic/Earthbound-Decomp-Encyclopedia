# Map Movement Usage Contract

This reference-derived contract joins map object movement IDs to ebsrc event/actionscript pointers.
It is the behavior-side companion to `notes/map-sprite-usage-contract.md`: the sprite contract
answers what a placed NPC looks like, while this contract answers which event/actionscript payload
drives that object's idle loop, physics callback, task startup, or scripted behavior.

## Summary

- NPC config rows: `1584`
- map placements: `1582`
- event script pointer entries: `895`
- event pointer table targets decoded: `895`
- script labels indexed from refs: `971`
- unique movement IDs used by NPC configs: `136`
- unique movement IDs used by placed NPC configs: `135`
- movement IDs resolved to ebsrc script files: `115`
- movement IDs without script-file resolution: `21`
- movement IDs with expected but missing ref script files: `21`
- unique pointer targets used: `136`
- shared pointer targets used: `2`

## Behavior Buckets

| Bucket | Movement IDs |
| --- | ---: |
| `debug_cursor_loop` | 1 |
| `event_actionscript_payload` | 9 |
| `physics_callback_movement` | 16 |
| `script_loop_or_wait` | 61 |
| `task_backed_actionscript` | 28 |
| `unresolved_pointer_target` | 21 |

## Top Movement IDs By Placement Count

| Movement | Target | Address | Bucket | NPC configs | Placements | Top sprites | Source file |
| ---: | --- | --- | --- | ---: | ---: | --- | --- |
| 8 | `EVENT_8` | `C3:A2AA` | `physics_callback_movement` | 393 | 393 | SPRITE_GROUP_SIGN (21), OVERWORLD_SPRITE::ATM_MACHINE (20), OVERWORLD_SPRITE::STREET_SIGN (17) | `refs/ebsrc-main/ebsrc-main/src/data/events/scripts/008.asm` |
| 12 | `EVENT_6_12` | `C3:A2E4` | `task_backed_actionscript` | 253 | 253 | SPRITE_GROUP_SURFER (11), SPRITE_GROUP_YOUNG_BLONDE_GUY_IN_BLUE (7), SPRITE_GROUP_MR_SATURN (7) | `refs/ebsrc-main/ebsrc-main/src/data/events/scripts/006+012.asm` |
| 606 | `EVENT_606` | `C3:6E2D` | `task_backed_actionscript` | 240 | 240 | SPRITE_GROUP_NERDY_REDHEAD (11), SPRITE_GROUP_MR_SATURN (11), SPRITE_GROUP_COP_IN_SUNGLASSES (9) | `refs/ebsrc-main/ebsrc-main/src/data/events/scripts/606.asm` |
| 9 | `EVENT_9` | `C3:A299` | `physics_callback_movement` | 177 | 177 | OVERWORLD_SPRITE::GIFT_BOX (118), OVERWORLD_SPRITE::TRASH_CAN (25), OVERWORLD_SPRITE::DALAAM_PRESENT (21) | `refs/ebsrc-main/ebsrc-main/src/data/events/scripts/009.asm` |
| 10 | `EVENT_10_11` | `C3:A2D3` | `physics_callback_movement` | 144 | 143 | OVERWORLD_SPRITE::MONKEY (24), OVERWORLD_SPRITE::INSANE_CULTIST (13), SPRITE_GROUP_MR_SATURN (6) | `refs/ebsrc-main/ebsrc-main/src/data/events/scripts/010+011.asm` |
| 605 | `EVENT_605` | `C3:6E19` | `task_backed_actionscript` | 108 | 108 | OVERWORLD_SPRITE::DOCTOR (7), OVERWORLD_SPRITE::NURSE (6), SPRITE_GROUP_SORTA_BALD_GUY_IN_SUIT (5) | `refs/ebsrc-main/ebsrc-main/src/data/events/scripts/605.asm` |
| 13 | `EVENT_13` | `C3:A33B` | `script_loop_or_wait` | 41 | 41 | SPRITE_GROUP_MR_SATURN (4), SPRITE_GROUP_CAT (3), OVERWORLD_SPRITE::MONKEY (3) | `refs/ebsrc-main/ebsrc-main/src/data/events/scripts/013.asm` |
| 599 | `EVENT_599` | `C3:6D53` | `script_loop_or_wait` | 27 | 27 | OVERWORLD_SPRITE::GUARDIAN_HIEROGLYPH (15), OVERWORLD_SPRITE::LETHAL_ASP_HIEROGLYPH (9), OVERWORLD_SPRITE::PETRIFIED_ROYAL_GUARD (2) | `refs/ebsrc-main/ebsrc-main/src/data/events/scripts/599.asm` |
| 16 | `EVENT_16` | `C3:A365` | `script_loop_or_wait` | 11 | 11 | OVERWORLD_SPRITE::YELLOW_CLOTHES_BLONDE (2), SPRITE_GROUP_YOUNG_BLONDE_GUY_IN_BLUE (1), SPRITE_GROUP_MR_T (1) | `refs/ebsrc-main/ebsrc-main/src/data/events/scripts/016.asm` |
| 600 | `EVENT_600` | `C3:6D5C` | `task_backed_actionscript` | 10 | 10 | OVERWORLD_SPRITE::GUARDIAN_DIGGER (5), SPRITE_GROUP_SLIMY_PILE (3), OVERWORLD_SPRITE::ROWDY_MOUSE (2) | `refs/ebsrc-main/ebsrc-main/src/data/events/scripts/600.asm` |
| 693 | `EVENT_693` | `C3:83D2` | `physics_callback_movement` | 10 | 10 | SPRITE_GROUP_YOUR_SANCTUARY_BOSS (8), SPRITE_GROUP_SPRING (1), SPRITE_GROUP_FLAME (1) | `refs/ebsrc-main/ebsrc-main/src/data/events/scripts/693.asm` |
| 602 | `EVENT_602` | `C3:6D9F` | `task_backed_actionscript` | 9 | 9 | OVERWORLD_SPRITE::SENTRY_ROBOT (5), SPRITE_GROUP_KRAKEN (3), SPRITE_GROUP_CLUMSY_ROBOT (1) | `refs/ebsrc-main/ebsrc-main/src/data/events/scripts/602.asm` |
| 769 | `EVENT_769` | `C3:9CD7` | `task_backed_actionscript` | 7 | 7 | OVERWORLD_SPRITE::UNDERWATER_NPC (7) | `refs/ebsrc-main/ebsrc-main/src/data/events/scripts/769.asm` |
| 607 | `EVENT_607` | `C3:6E52` | `script_loop_or_wait` | 6 | 6 | OVERWORLD_SPRITE::SCUZZY_GUY (1), OVERWORLD_SPRITE::YELLOW_CLOTHES_BLONDE (1), OVERWORLD_SPRITE::I_LOVE_QOWGA_SHIRT_GUY (1) | `refs/ebsrc-main/ebsrc-main/src/data/events/scripts/607.asm` |
| 80 | `EVENT_80` | `C3:B8E8` | `event_actionscript_payload` | 5 | 5 | OVERWORLD_SPRITE::URBAN_ZOMBIE (2), OVERWORLD_SPRITE::ZOMBIE_POSSESSOR (2), SPRITE_GROUP_ZOMBIE_LADY (1) | `refs/ebsrc-main/ebsrc-main/src/data/events/scripts/080.asm` |
| 784 | `EVENT_784` | `C3:9FBA` | `task_backed_actionscript` | 5 | 5 | OVERWORLD_SPRITE::OVAL_CLOUD (5) | `refs/ebsrc-main/ebsrc-main/src/data/events/scripts/784.asm` |
| 598 | `EVENT_598` | `C3:6D40` | `task_backed_actionscript` | 4 | 4 | OVERWORLD_SPRITE::SKATE_PUNK (2), OVERWORLD_SPRITE::MAD_DUCK (2) | `refs/ebsrc-main/ebsrc-main/src/data/events/scripts/598.asm` |
| 608 | `EVENT_608` | `C3:6E5E` | `script_loop_or_wait` | 4 | 4 | SPRITE_GROUP_TRAVELLING_ENTERTAINER (2), OVERWORLD_SPRITE::SCUZZY_GUY (1), SPRITE_GROUP_DOG (1) | `refs/ebsrc-main/ebsrc-main/src/data/events/scripts/608.asm` |
| 609 | `EVENT_609` | `C3:6E6A` | `script_loop_or_wait` | 4 | 4 | SPRITE_GROUP_DARK_HAIRED_GUY_IN_SUIT (1), OVERWORLD_SPRITE::BLONDE_GUY_IN_BLUE_SUIT (1), SPRITE_GROUP_BLONDE_SHOPPING_LADY (1) | `refs/ebsrc-main/ebsrc-main/src/data/events/scripts/609.asm` |
| 7 | `EVENT_7` | `C3:A287` | `physics_callback_movement` | 3 | 3 | OVERWORLD_SPRITE::INVISIBLE_2 (1), OVERWORLD_SPRITE::DONT_ENTER_SIGN (1), OVERWORLD_SPRITE::SECRET_DOOR_IN_MONOTOLI_BUILDING (1) | `refs/ebsrc-main/ebsrc-main/src/data/events/scripts/007.asm` |

## Shared Pointer Targets

Some movement IDs deliberately point at the same script label. These are aliases in the
NPC config movement field, not duplicate script bodies.

| Target | Movement IDs |
| --- | --- |
| `EVENT_10_11` | `10, 11` |
| `EVENT_6_12` | `6, 12` |

## Unresolved Movement IDs

These movement IDs are used by NPC configs and have decoded C4 pointer-table targets,
but the expected ebsrc script files are absent from the local ref checkout.

| Movement | Target | Address | Expected file | NPC IDs | Top sprites |
| ---: | --- | --- | --- | --- | --- |
| 870 | `EVENT_870` | `C3:9623` | `data/events/scripts/870.asm` | `567` | OVERWORLD_SPRITE::INVISIBLE_2 (1) |
| 871 | `EVENT_871` | `C3:9654` | `data/events/scripts/871.asm` | `709` | OVERWORLD_SPRITE::INVISIBLE_2 (1) |
| 872 | `EVENT_872` | `C3:9685` | `data/events/scripts/872.asm` | `736` | OVERWORLD_SPRITE::INVISIBLE_2 (1) |
| 873 | `EVENT_873` | `C3:96B6` | `data/events/scripts/873.asm` | `568` | OVERWORLD_SPRITE::INVISIBLE_2 (1) |
| 875 | `EVENT_875` | `C3:9718` | `data/events/scripts/875.asm` | `777` | OVERWORLD_SPRITE::INVISIBLE_2 (1) |
| 876 | `EVENT_876` | `C3:9749` | `data/events/scripts/876.asm` | `776` | OVERWORLD_SPRITE::INVISIBLE_2 (1) |
| 877 | `EVENT_877` | `C3:977A` | `data/events/scripts/877.asm` | `981` | OVERWORLD_SPRITE::STREETLIGHT (1) |
| 878 | `EVENT_878` | `C3:97AB` | `data/events/scripts/878.asm` | `913` | OVERWORLD_SPRITE::INVISIBLE_2 (1) |
| 879 | `EVENT_879` | `C3:97DC` | `data/events/scripts/879.asm` | `971` | OVERWORLD_SPRITE::INVISIBLE_2 (1) |
| 880 | `EVENT_880` | `C3:980D` | `data/events/scripts/880.asm` | `935` | OVERWORLD_SPRITE::INVISIBLE_2 (1) |
| 881 | `EVENT_881` | `C3:983E` | `data/events/scripts/881.asm` | `1093` | OVERWORLD_SPRITE::INVISIBLE_2 (1) |
| 882 | `EVENT_882` | `C3:986F` | `data/events/scripts/882.asm` | `1115` | SPRITE_GROUP_PALACE_DECORATIONS (1) |
| 883 | `EVENT_883` | `C3:98A0` | `data/events/scripts/883.asm` | `640` | OVERWORLD_SPRITE::INVISIBLE_2 (1) |
| 884 | `EVENT_884` | `C3:98D1` | `data/events/scripts/884.asm` | `1086` | OVERWORLD_SPRITE::HOTEL_SIGN (1) |
| 885 | `EVENT_885` | `C3:9902` | `data/events/scripts/885.asm` | `1032` | OVERWORLD_SPRITE::INVISIBLE_2 (1) |
| 886 | `EVENT_886` | `C3:9933` | `data/events/scripts/886.asm` | `1078` | SPRITE_GROUP_MAGIC_TART_STAND (1) |
| 887 | `EVENT_887` | `C3:9964` | `data/events/scripts/887.asm` | `1076` | OVERWORLD_SPRITE::INVISIBLE_2 (1) |
| 888 | `EVENT_888` | `C3:9995` | `data/events/scripts/888.asm` | `1157` | SPRITE_GROUP_PREET_PROOT_GUY (1) |
| 889 | `EVENT_889` | `C3:99C6` | `data/events/scripts/889.asm` | `1158` | OVERWORLD_SPRITE::INVISIBLE_2 (1) |
| 890 | `EVENT_890` | `C3:99F7` | `data/events/scripts/890.asm` | `1159` | OVERWORLD_SPRITE::INVISIBLE_2 (1) |
| 891 | `EVENT_891` | `C3:9A28` | `data/events/scripts/891.asm` | `1237` | OVERWORLD_SPRITE::INVISIBLE_2 (1) |

## Machine-Readable Data

The JSON contract records one row per used movement ID with target label, source file, behavior
bucket, NPC/map placement counts, top sprites, event macro profile, referenced C3 labels, and
example NPC config IDs.

- JSON: `notes/map-movement-usage-contract.json`
- generator: `tools/build_map_movement_usage_contract.py`
