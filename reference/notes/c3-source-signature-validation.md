# C3 source signature validation

This report walks address-prefixed labels in `src/c3` prototypes and compares the annotated instruction mnemonic stream against decoded ROM bytes at the same C3 addresses. It is a byte-equivalence precursor, not an assembler.

- status: `OK`
- modules: `7`
- instruction lines checked: `1947`
- labels checked: `175`
- errors: `0`
- warnings: `0`

## Modules

| Status | Source Path | Instructions | Labels | Errors | Warnings |
| --- | --- | ---: | ---: | ---: | ---: |
| `OK` | `src/c3/window_text_helpers.asm` | 467 | 48 | 0 | 0 |
| `OK` | `src/c3/inventory_equipment_tracked_items.asm` | 338 | 36 | 0 | 0 |
| `OK` | `src/c3/hp_pp_adjustment_helpers.asm` | 238 | 14 | 0 | 0 |
| `OK` | `src/c3/equipment_battle_selector_helpers.asm` | 138 | 11 | 0 | 0 |
| `OK` | `src/c3/jeff_repair_psi_helpers.asm` | 94 | 8 | 0 | 0 |
| `OK` | `src/c3/file_select_visual_transition_helper.asm` | 227 | 25 | 0 | 0 |
| `OK` | `src/c3/battle_visual_effect_helpers.asm` | 445 | 33 | 0 | 0 |
