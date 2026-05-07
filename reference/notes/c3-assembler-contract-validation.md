# C3 assembler contract validation

This report checks the assembler-facing contract for C3 source prototypes. It does not prove byte-equivalent assembly; it verifies that pilot-ready files have defined local symbols and named external control-flow targets while the source signature/range harness protects ROM bytes separately.

- status: `OK`
- modules: `7`
- pilot-ready modules: `7`
- instruction lines: `1947`
- symbolic operand lines: `602`
- unresolved symbol lines: `0`
- raw external control-flow edges: `0`
- errors: `0`
- warnings: `0`

## Modules

| Status | Contract | Source Path | Symbols | Labels | Symbolic | Unresolved | Raw External Edges | Errors | Warnings |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `OK` | `pilot-ready` | `src/c3/window_text_helpers.asm` | 73 | 48 | 178 | 0 | 0 | 0 | 0 |
| `OK` | `pilot-ready` | `src/c3/inventory_equipment_tracked_items.asm` | 18 | 35 | 84 | 0 | 0 | 0 | 0 |
| `OK` | `pilot-ready` | `src/c3/hp_pp_adjustment_helpers.asm` | 10 | 14 | 62 | 0 | 0 | 0 | 0 |
| `OK` | `pilot-ready` | `src/c3/equipment_battle_selector_helpers.asm` | 19 | 11 | 29 | 0 | 0 | 0 | 0 |
| `OK` | `pilot-ready` | `src/c3/jeff_repair_psi_helpers.asm` | 20 | 8 | 39 | 0 | 0 | 0 | 0 |
| `OK` | `pilot-ready` | `src/c3/file_select_visual_transition_helper.asm` | 37 | 25 | 96 | 0 | 0 | 0 | 0 |
| `OK` | `pilot-ready` | `src/c3/battle_visual_effect_helpers.asm` | 24 | 33 | 114 | 0 | 0 | 0 | 0 |
