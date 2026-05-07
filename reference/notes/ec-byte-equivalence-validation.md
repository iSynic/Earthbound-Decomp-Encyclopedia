# EC byte-equivalence validation

This report assembles an existing durable Asar source-bank scaffold into a clean ROM copy, then compares the protected byte ranges against the original ROM.

- status: `OK`
- mode: `durable-scaffold`
- modules: `15`
- non-OK modules: `0`
- mismatches: `0`

## Modules

| Status | Source Path | Range | Size | Mismatches | Generated ASM |
| --- | --- | --- | ---: | ---: | --- |
| `OK` | `src/ec/asset_audio_pack_114.asm` | `EC:0000..EC:23EC` | 9196 | 0 | `src/ec/bank_ec_helpers_asar.asm` |
| `OK` | `src/ec/asset_audio_pack_109.asm` | `EC:23EC..EC:4592` | 8614 | 0 | `src/ec/bank_ec_helpers_asar.asm` |
| `OK` | `src/ec/asset_audio_pack_107.asm` | `EC:4592..EC:6700` | 8558 | 0 | `src/ec/bank_ec_helpers_asar.asm` |
| `OK` | `src/ec/asset_audio_pack_98.asm` | `EC:6700..EC:8864` | 8548 | 0 | `src/ec/bank_ec_helpers_asar.asm` |
| `OK` | `src/ec/asset_audio_pack_165.asm` | `EC:8864..EC:9B76` | 4882 | 0 | `src/ec/bank_ec_helpers_asar.asm` |
| `OK` | `src/ec/asset_audio_pack_62.asm` | `EC:9B76..EC:A7D8` | 3170 | 0 | `src/ec/bank_ec_helpers_asar.asm` |
| `OK` | `src/ec/asset_audio_pack_58.asm` | `EC:A7D8..EC:B38A` | 2994 | 0 | `src/ec/bank_ec_helpers_asar.asm` |
| `OK` | `src/ec/asset_audio_pack_133.asm` | `EC:B38A..EC:BF28` | 2974 | 0 | `src/ec/bank_ec_helpers_asar.asm` |
| `OK` | `src/ec/asset_audio_pack_97.asm` | `EC:BF28..EC:CAA1` | 2937 | 0 | `src/ec/bank_ec_helpers_asar.asm` |
| `OK` | `src/ec/asset_audio_pack_55.asm` | `EC:CAA1..EC:D5D8` | 2871 | 0 | `src/ec/bank_ec_helpers_asar.asm` |
| `OK` | `src/ec/asset_audio_pack_106.asm` | `EC:D5D8..EC:E101` | 2857 | 0 | `src/ec/bank_ec_helpers_asar.asm` |
| `OK` | `src/ec/asset_audio_pack_25.asm` | `EC:E101..EC:EB51` | 2640 | 0 | `src/ec/bank_ec_helpers_asar.asm` |
| `OK` | `src/ec/asset_audio_pack_15.asm` | `EC:EB51..EC:F578` | 2599 | 0 | `src/ec/bank_ec_helpers_asar.asm` |
| `OK` | `src/ec/asset_audio_pack_157.asm` | `EC:F578..EC:FF94` | 2588 | 0 | `src/ec/bank_ec_helpers_asar.asm` |
| `OK` | `src/ec/asset_bank_ec_gap_1_tailpadding.asm` | `EC:FF94..EC:10000` | 108 | 0 | `src/ec/bank_ec_helpers_asar.asm` |
