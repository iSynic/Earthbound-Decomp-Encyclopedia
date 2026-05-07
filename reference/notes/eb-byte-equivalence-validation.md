# EB byte-equivalence validation

This report assembles an existing durable Asar source-bank scaffold into a clean ROM copy, then compares the protected byte ranges against the original ROM.

- status: `OK`
- mode: `durable-scaffold`
- modules: `9`
- non-OK modules: `0`
- mismatches: `0`

## Modules

| Status | Source Path | Range | Size | Mismatches | Generated ASM |
| --- | --- | --- | ---: | ---: | --- |
| `OK` | `src/eb/asset_audio_pack_44.asm` | `EB:0000..EB:29E8` | 10728 | 0 | `src/eb/bank_eb_helpers_asar.asm` |
| `OK` | `src/eb/asset_audio_pack_21.asm` | `EB:29E8..EB:520C` | 10276 | 0 | `src/eb/bank_eb_helpers_asar.asm` |
| `OK` | `src/eb/asset_audio_pack_5.asm` | `EB:520C..EB:78D6` | 9930 | 0 | `src/eb/bank_eb_helpers_asar.asm` |
| `OK` | `src/eb/asset_audio_pack_40.asm` | `EB:78D6..EB:9F8E` | 9912 | 0 | `src/eb/bank_eb_helpers_asar.asm` |
| `OK` | `src/eb/asset_audio_pack_33.asm` | `EB:9F8E..EB:C4E8` | 9562 | 0 | `src/eb/bank_eb_helpers_asar.asm` |
| `OK` | `src/eb/asset_audio_pack_105.asm` | `EB:C4E8..EB:E9E4` | 9468 | 0 | `src/eb/bank_eb_helpers_asar.asm` |
| `OK` | `src/eb/asset_audio_pack_154.asm` | `EB:E9E4..EB:FE22` | 5182 | 0 | `src/eb/bank_eb_helpers_asar.asm` |
| `OK` | `src/eb/asset_audio_pack_13.asm` | `EB:FE22..EB:FFFF` | 477 | 0 | `src/eb/bank_eb_helpers_asar.asm` |
| `OK` | `src/eb/asset_bank_eb_gap_1_tailpadding.asm` | `EB:FFFF..EB:10000` | 1 | 0 | `src/eb/bank_eb_helpers_asar.asm` |
