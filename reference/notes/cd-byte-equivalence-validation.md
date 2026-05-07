# CD byte-equivalence validation

This report assembles scratch Asar translations of CD pilot modules into clean ROM copies at their original `org` addresses, then compares the protected byte ranges against the original ROM.

- status: `OK`
- mode: `combined-scaffold`
- modules: `55`
- non-OK modules: `0`
- mismatches: `0`

## Modules

| Status | Source Path | Range | Size | Mismatches | Generated ASM |
| --- | --- | --- | ---: | ---: | --- |
| `OK` | `src/cd/asset_battle_sprite_107.asm` | `CD:0000..CD:0E26` | 3622 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_64.asm` | `CD:0E26..CD:185C` | 2614 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_40.asm` | `CD:185C..CD:2255` | 2553 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_97.asm` | `CD:2255..CD:2B19` | 2244 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_41.asm` | `CD:2B19..CD:328F` | 1910 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_86.asm` | `CD:328F..CD:3959` | 1738 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_39.asm` | `CD:3959..CD:3F94` | 1595 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_38.asm` | `CD:3F94..CD:45AA` | 1558 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_56.asm` | `CD:45AA..CD:4B4B` | 1441 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_100.asm` | `CD:4B4B..CD:509D` | 1362 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_96.asm` | `CD:509D..CD:55EE` | 1361 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_36.asm` | `CD:55EE..CD:5B3D` | 1359 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_73.asm` | `CD:5B3D..CD:6069` | 1324 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_75.asm` | `CD:6069..CD:6593` | 1322 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_35.asm` | `CD:6593..CD:6AB6` | 1315 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_74.asm` | `CD:6AB6..CD:6FD3` | 1309 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_101.asm` | `CD:6FD3..CD:74DF` | 1292 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_94.asm` | `CD:74DF..CD:79D7` | 1272 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_37.asm` | `CD:79D7..CD:7ECE` | 1271 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_87.asm` | `CD:7ECE..CD:83AA` | 1244 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_13.asm` | `CD:83AA..CD:883F` | 1173 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_104.asm` | `CD:883F..CD:8CCB` | 1164 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_99.asm` | `CD:8CCB..CD:9142` | 1143 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_55.asm` | `CD:9142..CD:958A` | 1096 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_95.asm` | `CD:958A..CD:9984` | 1018 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_105.asm` | `CD:9984..CD:9D65` | 993 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_72.asm` | `CD:9D65..CD:A144` | 991 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_51.asm` | `CD:A144..CD:A51D` | 985 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_22.asm` | `CD:A51D..CD:A8F4` | 983 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_102.asm` | `CD:A8F4..CD:ACBF` | 971 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_84.asm` | `CD:ACBF..CD:B087` | 968 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_67.asm` | `CD:B087..CD:B447` | 960 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_63.asm` | `CD:B447..CD:B802` | 955 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_11.asm` | `CD:B802..CD:BB82` | 896 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_106.asm` | `CD:BB82..CD:BEFF` | 893 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_54.asm` | `CD:BEFF..CD:C27B` | 892 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_14.asm` | `CD:C27B..CD:C5F0` | 885 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_32.asm` | `CD:C5F0..CD:C960` | 880 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_81.asm` | `CD:C960..CD:CCCF` | 879 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_62.asm` | `CD:CCCF..CD:D01D` | 846 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_93.asm` | `CD:D01D..CD:D36A` | 845 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_83.asm` | `CD:D36A..CD:D6A6` | 828 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_34.asm` | `CD:D6A6..CD:D9E1` | 827 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_12.asm` | `CD:D9E1..CD:DD18` | 823 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_60.asm` | `CD:DD18..CD:E04C` | 820 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_71.asm` | `CD:E04C..CD:E37C` | 816 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_10.asm` | `CD:E37C..CD:E6A8` | 812 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_9.asm` | `CD:E6A8..CD:E9D4` | 812 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_28.asm` | `CD:E9D4..CD:ECF7` | 803 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_108.asm` | `CD:ECF7..CD:F018` | 801 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_79.asm` | `CD:F018..CD:F337` | 799 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_27.asm` | `CD:F337..CD:F652` | 795 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_78.asm` | `CD:F652..CD:F95F` | 781 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_30.asm` | `CD:F95F..CD:FC6C` | 781 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/cd/asset_battle_sprite_23.asm` | `CD:FC6C..CD:10000` | 916 | 0 | `build/cd-byte-equivalence/bank-cd-helper-scaffold.byte-equivalence.asar.asm` |
