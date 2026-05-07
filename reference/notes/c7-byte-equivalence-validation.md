# C7 byte-equivalence validation

This report assembles an existing durable Asar source-bank scaffold into a clean ROM copy, then compares the protected byte ranges against the original ROM.

- status: `OK`
- mode: `durable-scaffold`
- modules: `11`
- non-OK modules: `0`
- mismatches: `0`

## Modules

| Status | Source Path | Range | Size | Mismatches | Generated ASM |
| --- | --- | --- | ---: | ---: | --- |
| `OK` | `src/c7/text_ehint.asm` | `C7:0000..C7:2709` | 9993 | 0 | `src/c7/bank_c7_helpers_asar.asm` |
| `OK` | `src/c7/text_e01onet1.asm` | `C7:2709..C7:4BA9` | 9376 | 0 | `src/c7/bank_c7_helpers_asar.asm` |
| `OK` | `src/c7/text_e01onet0.asm` | `C7:4BA9..C7:6F20` | 9079 | 0 | `src/c7/bank_c7_helpers_asar.asm` |
| `OK` | `src/c7/text_e18mgkt.asm` | `C7:6F20..C7:7DCE` | 3758 | 0 | `src/c7/bank_c7_helpers_asar.asm` |
| `OK` | `src/c7/text_egoods4.asm` | `C7:7DCE..C7:7F00` | 306 | 0 | `src/c7/bank_c7_helpers_asar.asm` |
| `OK` | `src/c7/text_bank_c7_gap_1_alignmentgap.asm` | `C7:7F00..C7:8000` | 256 | 0 | `src/c7/bank_c7_helpers_asar.asm` |
| `OK` | `src/c7/text_eevent1.asm` | `C7:8000..C7:A2F7` | 8951 | 0 | `src/c7/bank_c7_helpers_asar.asm` |
| `OK` | `src/c7/text_eevent4.asm` | `C7:A2F7..C7:C588` | 8849 | 0 | `src/c7/bank_c7_helpers_asar.asm` |
| `OK` | `src/c7/text_esystem.asm` | `C7:C588..C7:E797` | 8719 | 0 | `src/c7/bank_c7_helpers_asar.asm` |
| `OK` | `src/c7/text_e08dosei.asm` | `C7:E797..C7:FF40` | 6057 | 0 | `src/c7/bank_c7_helpers_asar.asm` |
| `OK` | `src/c7/text_bank_c7_gap_2_tailpadding.asm` | `C7:FF40..C7:10000` | 192 | 0 | `src/c7/bank_c7_helpers_asar.asm` |
