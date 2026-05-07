# C9 byte-equivalence validation

This report assembles an existing durable Asar source-bank scaffold into a clean ROM copy, then compares the protected byte ranges against the original ROM.

- status: `OK`
- mode: `durable-scaffold`
- modules: `16`
- non-OK modules: `0`
- mismatches: `0`

## Modules

| Status | Source Path | Range | Size | Mismatches | Generated ASM |
| --- | --- | --- | ---: | ---: | --- |
| `OK` | `src/c9/text_eshop2.asm` | `C9:0000..C9:1C3A` | 7226 | 0 | `src/c9/bank_c9_helpers_asar.asm` |
| `OK` | `src/c9/text_eevent3.asm` | `C9:1C3A..C9:3853` | 7193 | 0 | `src/c9/bank_c9_helpers_asar.asm` |
| `OK` | `src/c9/text_e02twsn2.asm` | `C9:3853..C9:53BF` | 7020 | 0 | `src/c9/bank_c9_helpers_asar.asm` |
| `OK` | `src/c9/text_e02twsn1.asm` | `C9:53BF..C9:6D10` | 6481 | 0 | `src/c9/bank_c9_helpers_asar.asm` |
| `OK` | `src/c9/text_e19moon.asm` | `C9:6D10..C9:7B6B` | 3675 | 0 | `src/c9/bank_c9_helpers_asar.asm` |
| `OK` | `src/c9/text_egoods0.asm` | `C9:7B6B..C9:7FB3` | 1096 | 0 | `src/c9/bank_c9_helpers_asar.asm` |
| `OK` | `src/c9/text_bank_c9_gap_1_alignmentgap.asm` | `C9:7FB3..C9:8000` | 77 | 0 | `src/c9/bank_c9_helpers_asar.asm` |
| `OK` | `src/c9/text_e03happy.asm` | `C9:8000..C9:992F` | 6447 | 0 | `src/c9/bank_c9_helpers_asar.asm` |
| `OK` | `src/c9/text_unknown_c9992f.asm` | `C9:992F..C9:B226` | 6391 | 0 | `src/c9/bank_c9_helpers_asar.asm` |
| `OK` | `src/c9/text_eevent5.asm` | `C9:B226..C9:C991` | 5995 | 0 | `src/c9/bank_c9_helpers_asar.asm` |
| `OK` | `src/c9/text_e12rama.asm` | `C9:C991..C9:D6F8` | 3431 | 0 | `src/c9/bank_c9_helpers_asar.asm` |
| `OK` | `src/c9/text_e15gumi.asm` | `C9:D6F8..C9:E37E` | 3206 | 0 | `src/c9/bank_c9_helpers_asar.asm` |
| `OK` | `src/c9/text_e14makyo.asm` | `C9:E37E..C9:EE2F` | 2737 | 0 | `src/c9/bank_c9_helpers_asar.asm` |
| `OK` | `src/c9/text_ebattle7.asm` | `C9:EE2F..C9:F897` | 2664 | 0 | `src/c9/bank_c9_helpers_asar.asm` |
| `OK` | `src/c9/text_egoods1.asm` | `C9:F897..C9:FF2F` | 1688 | 0 | `src/c9/bank_c9_helpers_asar.asm` |
| `OK` | `src/c9/text_bank_c9_gap_2_tailpadding.asm` | `C9:FF2F..C9:10000` | 209 | 0 | `src/c9/bank_c9_helpers_asar.asm` |
