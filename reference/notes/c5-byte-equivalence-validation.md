# C5 byte-equivalence validation

This report assembles an existing durable Asar source-bank scaffold into a clean ROM copy, then compares the protected byte ranges against the original ROM.

- status: `OK`
- mode: `durable-scaffold`
- modules: `9`
- non-OK modules: `0`
- mismatches: `0`

## Modules

| Status | Source Path | Range | Size | Mismatches | Generated ASM |
| --- | --- | --- | ---: | ---: | --- |
| `OK` | `src/c5/text_eshop0.asm` | `C5:0000..C5:3711` | 14097 | 0 | `src/c5/bank_c5_helpers_asar.asm` |
| `OK` | `src/c5/text_eexplgds.asm` | `C5:3711..C5:6DF3` | 14050 | 0 | `src/c5/bank_c5_helpers_asar.asm` |
| `OK` | `src/c5/text_e13skrb.asm` | `C5:6DF3..C5:7E1C` | 4137 | 0 | `src/c5/bank_c5_helpers_asar.asm` |
| `OK` | `src/c5/text_e17past.asm` | `C5:7E1C..C5:7FC1` | 421 | 0 | `src/c5/bank_c5_helpers_asar.asm` |
| `OK` | `src/c5/text_bank_c5_gap_1_alignmentgap.asm` | `C5:7FC1..C5:8000` | 63 | 0 | `src/c5/bank_c5_helpers_asar.asm` |
| `OK` | `src/c5/text_edebug.asm` | `C5:8000..C5:B3BA` | 13242 | 0 | `src/c5/bank_c5_helpers_asar.asm` |
| `OK` | `src/c5/text_eshop1.asm` | `C5:B3BA..C5:E5BC` | 12802 | 0 | `src/c5/bank_c5_helpers_asar.asm` |
| `OK` | `src/c5/text_eevent0.asm` | `C5:E5BC..C5:FFEC` | 6704 | 0 | `src/c5/bank_c5_helpers_asar.asm` |
| `OK` | `src/c5/text_bank_c5_gap_2_tailpadding.asm` | `C5:FFEC..C5:10000` | 20 | 0 | `src/c5/bank_c5_helpers_asar.asm` |
