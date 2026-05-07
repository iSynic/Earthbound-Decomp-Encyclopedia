# EE byte-equivalence validation

This report assembles an existing durable Asar source-bank scaffold into a clean ROM copy, then compares the protected byte ranges against the original ROM.

- status: `OK`
- mode: `durable-scaffold`
- modules: `47`
- non-OK modules: `0`
- mismatches: `0`

## Modules

| Status | Source Path | Range | Size | Mismatches | Generated ASM |
| --- | --- | --- | ---: | ---: | --- |
| `OK` | `src/ee/asset_audio_pack_136.asm` | `EE:0000..EE:0554` | 1364 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_112.asm` | `EE:0554..EE:0A8B` | 1335 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_163.asm` | `EE:0A8B..EE:0FB2` | 1319 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_115.asm` | `EE:0FB2..EE:14D4` | 1314 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_53.asm` | `EE:14D4..EE:19EE` | 1306 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_67.asm` | `EE:19EE..EE:1EFE` | 1296 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_20.asm` | `EE:1EFE..EE:2401` | 1283 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_144.asm` | `EE:2401..EE:28FE` | 1277 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_63.asm` | `EE:28FE..EE:2DCD` | 1231 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_138.asm` | `EE:2DCD..EE:3236` | 1129 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_127.asm` | `EE:3236..EE:365D` | 1063 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_16.asm` | `EE:365D..EE:3A7D` | 1056 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_148.asm` | `EE:3A7D..EE:3E9C` | 1055 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_23.asm` | `EE:3E9C..EE:42BB` | 1055 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_11.asm` | `EE:42BB..EE:46CE` | 1043 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_142.asm` | `EE:46CE..EE:4ADF` | 1041 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_160.asm` | `EE:4ADF..EE:4EEA` | 1035 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_101.asm` | `EE:4EEA..EE:52E6` | 1020 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_103.asm` | `EE:52E6..EE:56DF` | 1017 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_51.asm` | `EE:56DF..EE:5A99` | 954 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_93.asm` | `EE:5A99..EE:5DFA` | 865 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_95.asm` | `EE:5DFA..EE:614C` | 850 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_164.asm` | `EE:614C..EE:648C` | 832 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_151.asm` | `EE:648C..EE:67B7` | 811 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_12.asm` | `EE:67B7..EE:6A85` | 718 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_135.asm` | `EE:6A85..EE:6D36` | 689 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_83.asm` | `EE:6D36..EE:6FDD` | 679 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_88.asm` | `EE:6FDD..EE:7274` | 663 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_31.asm` | `EE:7274..EE:74D7` | 611 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_129.asm` | `EE:74D7..EE:7737` | 608 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_22.asm` | `EE:7737..EE:798E` | 599 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_17.asm` | `EE:798E..EE:7BDF` | 593 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_91.asm` | `EE:7BDF..EE:7E29` | 586 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_81.asm` | `EE:7E29..EE:804D` | 548 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_147.asm` | `EE:804D..EE:826C` | 543 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_152.asm` | `EE:826C..EE:8466` | 506 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_128.asm` | `EE:8466..EE:8638` | 466 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_159.asm` | `EE:8638..EE:87CB` | 403 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_49.asm` | `EE:87CB..EE:894F` | 388 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_9.asm` | `EE:894F..EE:8ACA` | 379 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_69.asm` | `EE:8ACA..EE:8C1E` | 340 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_167.asm` | `EE:8C1E..EE:8D65` | 327 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_130.asm` | `EE:8D65..EE:8EA2` | 317 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_168.asm` | `EE:8EA2..EE:8FD6` | 308 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_137.asm` | `EE:8FD6..EE:90FF` | 297 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_audio_pack_41.asm` | `EE:90FF..EE:9201` | 258 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
| `OK` | `src/ee/asset_bank_ee_gap_1_tailpadding.asm` | `EE:9201..EE:10000` | 28159 | 0 | `src/ee/bank_ee_helpers_asar.asm` |
