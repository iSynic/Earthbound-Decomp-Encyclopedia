# ED byte-equivalence validation

This report assembles an existing durable Asar source-bank scaffold into a clean ROM copy, then compares the protected byte ranges against the original ROM.

- status: `OK`
- mode: `durable-scaffold`
- modules: `37`
- non-OK modules: `0`
- mismatches: `0`

## Modules

| Status | Source Path | Range | Size | Mismatches | Generated ASM |
| --- | --- | --- | ---: | ---: | --- |
| `OK` | `src/ed/asset_audio_pack_121.asm` | `ED:0000..ED:0A07` | 2567 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
| `OK` | `src/ed/asset_audio_pack_87.asm` | `ED:0A07..ED:1406` | 2559 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
| `OK` | `src/ed/asset_audio_pack_132.asm` | `ED:1406..ED:1DFF` | 2553 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
| `OK` | `src/ed/asset_audio_pack_116.asm` | `ED:1DFF..ED:27F7` | 2552 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
| `OK` | `src/ed/asset_audio_pack_34.asm` | `ED:27F7..ED:3195` | 2462 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
| `OK` | `src/ed/asset_audio_pack_119.asm` | `ED:3195..ED:3A9C` | 2311 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
| `OK` | `src/ed/asset_audio_pack_141.asm` | `ED:3A9C..ED:436B` | 2255 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
| `OK` | `src/ed/asset_audio_pack_48.asm` | `ED:436B..ED:4BA7` | 2108 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
| `OK` | `src/ed/asset_audio_pack_39.asm` | `ED:4BA7..ED:53DF` | 2104 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
| `OK` | `src/ed/asset_audio_pack_150.asm` | `ED:53DF..ED:5C01` | 2082 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
| `OK` | `src/ed/asset_audio_pack_120.asm` | `ED:5C01..ED:6409` | 2056 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
| `OK` | `src/ed/asset_audio_pack_38.asm` | `ED:6409..ED:6C06` | 2045 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
| `OK` | `src/ed/asset_audio_pack_161.asm` | `ED:6C06..ED:73E2` | 2012 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
| `OK` | `src/ed/asset_audio_pack_68.asm` | `ED:73E2..ED:7BB6` | 2004 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
| `OK` | `src/ed/asset_audio_pack_104.asm` | `ED:7BB6..ED:8389` | 2003 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
| `OK` | `src/ed/asset_audio_pack_90.asm` | `ED:8389..ED:8B21` | 1944 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
| `OK` | `src/ed/asset_audio_pack_86.asm` | `ED:8B21..ED:91AF` | 1678 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
| `OK` | `src/ed/asset_audio_pack_100.asm` | `ED:91AF..ED:9824` | 1653 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
| `OK` | `src/ed/asset_audio_pack_26.asm` | `ED:9824..ED:9E93` | 1647 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
| `OK` | `src/ed/asset_audio_pack_43.asm` | `ED:9E93..ED:A4D7` | 1604 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
| `OK` | `src/ed/asset_audio_pack_162.asm` | `ED:A4D7..ED:AB12` | 1595 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
| `OK` | `src/ed/asset_audio_pack_85.asm` | `ED:AB12..ED:B136` | 1572 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
| `OK` | `src/ed/asset_audio_pack_99.asm` | `ED:B136..ED:B753` | 1565 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
| `OK` | `src/ed/asset_audio_pack_28.asm` | `ED:B753..ED:BD60` | 1549 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
| `OK` | `src/ed/asset_audio_pack_10.asm` | `ED:BD60..ED:C36C` | 1548 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
| `OK` | `src/ed/asset_audio_pack_117.asm` | `ED:C36C..ED:C96E` | 1538 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
| `OK` | `src/ed/asset_audio_pack_77.asm` | `ED:C96E..ED:CF55` | 1511 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
| `OK` | `src/ed/asset_audio_pack_19.asm` | `ED:CF55..ED:D539` | 1508 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
| `OK` | `src/ed/asset_audio_pack_57.asm` | `ED:D539..ED:DAFD` | 1476 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
| `OK` | `src/ed/asset_audio_pack_14.asm` | `ED:DAFD..ED:E0AE` | 1457 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
| `OK` | `src/ed/asset_audio_pack_158.asm` | `ED:E0AE..ED:E65C` | 1454 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
| `OK` | `src/ed/asset_audio_pack_30.asm` | `ED:E65C..ED:EBF4` | 1432 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
| `OK` | `src/ed/asset_audio_pack_134.asm` | `ED:EBF4..ED:F183` | 1423 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
| `OK` | `src/ed/asset_audio_pack_113.asm` | `ED:F183..ED:F710` | 1421 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
| `OK` | `src/ed/asset_audio_pack_146.asm` | `ED:F710..ED:FC9C` | 1420 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
| `OK` | `src/ed/asset_audio_pack_29.asm` | `ED:FC9C..ED:FFFE` | 866 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
| `OK` | `src/ed/asset_bank_ed_gap_1_tailpadding.asm` | `ED:FFFE..ED:10000` | 2 | 0 | `src/ed/bank_ed_helpers_asar.asm` |
