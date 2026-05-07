# C3 byte-equivalence validation

This report assembles an existing durable Asar source-bank scaffold into a clean ROM copy, then compares the protected byte ranges against the original ROM.

- status: `OK`
- mode: `durable-scaffold`
- modules: `1`
- non-OK modules: `0`
- mismatches: `0`

## Modules

| Status | Source Path | Range | Size | Mismatches | Generated ASM |
| --- | --- | --- | ---: | ---: | --- |
| `OK` | `src/c3/bank_c3_event_scripts_source_pilot.asar.asm` | `C3:0000..C3:E450` | 58448 | 0 | `src/c3/bank_c3_event_scripts_source_pilot.asar.asm` |
