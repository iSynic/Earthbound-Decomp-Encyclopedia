# C6 byte-equivalence validation

This report assembles an existing durable Asar source-bank scaffold into a clean ROM copy, then compares the protected byte ranges against the original ROM.

- status: `OK`
- mode: `durable-scaffold`
- modules: `9`
- non-OK modules: `0`
- mismatches: `0`

## Modules

| Status | Source Path | Range | Size | Mismatches | Generated ASM |
| --- | --- | --- | ---: | ---: | --- |
| `OK` | `src/c6/text_e09dsrt.asm` | `C6:0000..C6:2D30` | 11568 | 0 | `src/c6/bank_c6_helpers_asar.asm` |
| `OK` | `src/c6/text_eshop3.asm` | `C6:2D30..C6:59C9` | 11417 | 0 | `src/c6/bank_c6_helpers_asar.asm` |
| `OK` | `src/c6/text_e01onet2.asm` | `C6:59C9..C6:7EEC` | 9507 | 0 | `src/c6/bank_c6_helpers_asar.asm` |
| `OK` | `src/c6/text_bank_c6_gap_1_alignmentgap.asm` | `C6:7EEC..C6:8000` | 276 | 0 | `src/c6/bank_c6_helpers_asar.asm` |
| `OK` | `src/c6/text_eglobal.asm` | `C6:8000..C6:A9F9` | 10745 | 0 | `src/c6/bank_c6_helpers_asar.asm` |
| `OK` | `src/c6/text_e06wins.asm` | `C6:A9F9..C6:D19C` | 10147 | 0 | `src/c6/bank_c6_helpers_asar.asm` |
| `OK` | `src/c6/text_e10four0.asm` | `C6:D19C..C6:F8D9` | 10045 | 0 | `src/c6/bank_c6_helpers_asar.asm` |
| `OK` | `src/c6/text_egoods3.asm` | `C6:F8D9..C6:FFE3` | 1802 | 0 | `src/c6/bank_c6_helpers_asar.asm` |
| `OK` | `src/c6/text_bank_c6_gap_2_tailpadding.asm` | `C6:FFE3..C6:10000` | 29 | 0 | `src/c6/bank_c6_helpers_asar.asm` |
