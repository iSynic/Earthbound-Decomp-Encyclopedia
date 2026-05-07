# C8 byte-equivalence validation

This report assembles scratch Asar translations of C8 pilot modules into clean ROM copies at their original `org` addresses, then compares the protected byte ranges against the original ROM.

- status: `OK`
- mode: `combined-scaffold`
- modules: `11`
- non-OK modules: `0`
- mismatches: `0`

## Modules

| Status | Source Path | Range | Size | Mismatches | Generated ASM |
| --- | --- | --- | ---: | ---: | --- |
| `OK` | `src/c8/text_e02twsn0.asm` | `C8:0000..C8:2105` | 8453 | 0 | `build/c8-byte-equivalence/bank-c8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/c8/text_e10four1.asm` | `C8:2105..C8:41DE` | 8409 | 0 | `build/c8-byte-equivalence/bank-c8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/c8/text_enews.asm` | `C8:41DE..C8:6279` | 8347 | 0 | `build/c8-byte-equivalence/bank-c8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/c8/text_ebgmess.asm` | `C8:6279..C8:7F23` | 7338 | 0 | `build/c8-byte-equivalence/bank-c8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/c8/text_bank_c8_gap_1_alignmentgap.asm` | `C8:7F23..C8:8000` | 221 | 0 | `build/c8-byte-equivalence/bank-c8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/c8/text_eevent2.asm` | `C8:8000..C8:9E1B` | 7707 | 0 | `build/c8-byte-equivalence/bank-c8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/c8/text_e11sums.asm` | `C8:9E1B..C8:BC2D` | 7698 | 0 | `build/c8-byte-equivalence/bank-c8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/c8/text_bank_c8_gap_2_nonlocaledataisland.asm` | `C8:BC2D..C8:D9ED` | 7616 | 0 | `build/c8-byte-equivalence/bank-c8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/c8/text_e05thrk.asm` | `C8:D9ED..C8:F77D` | 7568 | 0 | `build/c8-byte-equivalence/bank-c8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/c8/text_ebattle6.asm` | `C8:F77D..C8:FFF3` | 2166 | 0 | `build/c8-byte-equivalence/bank-c8-helper-scaffold.byte-equivalence.asar.asm` |
| `OK` | `src/c8/text_bank_c8_gap_3_tailpadding.asm` | `C8:FFF3..C8:10000` | 13 | 0 | `build/c8-byte-equivalence/bank-c8-helper-scaffold.byte-equivalence.asar.asm` |
