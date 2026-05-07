# E0 byte-equivalence validation

This report assembles scratch Asar translations of E0 pilot modules into clean ROM copies at their original `org` addresses, then compares the protected byte ranges against the original ROM.

- status: `OK`
- mode: `combined-scaffold`
- modules: `16`
- non-OK modules: `0`
- mismatches: `0`

## Modules

| Status | Source Path | Range | Size | Mismatches | Generated ASM |
| --- | --- | --- | ---: | ---: | --- |
| `OK` | `src/e0/asset_text_window_gfx.asm` | `E0:0000..E0:0754` | 1876 | 0 | `build/e0-byte-equivalence/bank-e0-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e0/asset_flavoured_text_gfx.asm` | `E0:0754..E0:07A0` | 76 | 0 | `build/e0-byte-equivalence/bank-e0-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e0/asset_mother2_romaji_font.asm` | `E0:07A0..E0:09B4` | 532 | 0 | `build/e0-byte-equivalence/bank-e0-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e0/asset_compressed_sram.asm` | `E0:09B4..E0:1359` | 2469 | 0 | `build/e0-byte-equivalence/bank-e0-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e0/asset_mrsaturn_font_data.asm` | `E0:1359..E0:13B9` | 96 | 0 | `build/e0-byte-equivalence/bank-e0-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e0/asset_mrsaturn_font_gfx.asm` | `E0:13B9..E0:1FB9` | 3072 | 0 | `build/e0-byte-equivalence/bank-e0-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e0/table_006_data_text_window_properties_asm.asm` | `E0:1FB9..E0:21A8` | 495 | 0 | `build/e0-byte-equivalence/bank-e0-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e0/asset_town_map_onett.asm` | `E0:21A8..E0:4920` | 10104 | 0 | `build/e0-byte-equivalence/bank-e0-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e0/asset_town_map_twoson.asm` | `E0:4920..E0:6721` | 7681 | 0 | `build/e0-byte-equivalence/bank-e0-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e0/asset_town_map_threed.asm` | `E0:6721..E0:8379` | 7256 | 0 | `build/e0-byte-equivalence/bank-e0-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e0/asset_town_map_fourside.asm` | `E0:8379..E0:ADB4` | 10811 | 0 | `build/e0-byte-equivalence/bank-e0-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e0/asset_town_map_scaraba.asm` | `E0:ADB4..E0:C7F1` | 6717 | 0 | `build/e0-byte-equivalence/bank-e0-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e0/asset_town_map_summers.asm` | `E0:C7F1..E0:ED03` | 9490 | 0 | `build/e0-byte-equivalence/bank-e0-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e0/asset_audio_pack_110.asm` | `E0:ED03..E0:FCE1` | 4062 | 0 | `build/e0-byte-equivalence/bank-e0-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e0/asset_audio_pack_6.asm` | `E0:FCE1..E0:FFB3` | 722 | 0 | `build/e0-byte-equivalence/bank-e0-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/e0/asset_bank_e0_gap_1_tailpadding.asm` | `E0:FFB3..E0:10000` | 77 | 0 | `build/e0-byte-equivalence/bank-e0-helper-scaffold.byte-equivalence.asar.asm` |
