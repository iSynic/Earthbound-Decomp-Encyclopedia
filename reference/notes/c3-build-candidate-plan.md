# C3 build-candidate hardening plan

Generated from the C3 source-emission plan and current `src/c3` prototype artifacts. This tracks the gap between annotated source prototypes and build-candidate source that can enter a byte-equivalence harness.

## Summary

- modules: `7`
- annotated asm modules: `0`
- build candidate modules: `7`
- open ended modules: `0`
- signature clean modules: `7`
- symbolic operand lines: `602`
- unresolved symbol lines: `0`
- local control flow edges: `200`

## Module Queue

| Blockers | Signature | Level | Asm Contract | Source Path | Range | Instr. | Symbolic | Unresolved | Raw Ext. | Recommendation |
| ---: | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| 0 | `OK` | `build-candidate` | `pilot-ready` | `src/c3/equipment_battle_selector_helpers.asm` | `C3:EE14..C3:EF23` | 138 | 29 | 0 | 0 | ready for first real assembler byte-equivalence pilot |
| 0 | `OK` | `build-candidate` | `pilot-ready` | `src/c3/jeff_repair_psi_helpers.asm` | `C3:F1EC..C3:F2B1` | 94 | 39 | 0 | 0 | ready for first real assembler byte-equivalence pilot |
| 0 | `OK` | `build-candidate` | `pilot-ready` | `src/c3/hp_pp_adjustment_helpers.asm` | `C3:EC1F..C3:EE14` | 238 | 62 | 0 | 0 | ready for first real assembler byte-equivalence pilot |
| 0 | `OK` | `build-candidate` | `pilot-ready` | `src/c3/inventory_equipment_tracked_items.asm` | `C3:E977..C3:EC1F` | 338 | 84 | 0 | 0 | ready for first real assembler byte-equivalence pilot |
| 0 | `OK` | `build-candidate` | `pilot-ready` | `src/c3/file_select_visual_transition_helper.asm` | `C3:F3C5..C3:F5F9` | 227 | 96 | 0 | 0 | ready for first real assembler byte-equivalence pilot |
| 0 | `OK` | `build-candidate` | `pilot-ready` | `src/c3/battle_visual_effect_helpers.asm` | `C3:F5F9..C3:FB1F` | 445 | 114 | 0 | 0 | ready for first real assembler byte-equivalence pilot |
| 0 | `OK` | `build-candidate` | `pilot-ready` | `src/c3/window_text_helpers.asm` | `C3:E450..C3:E84E` | 467 | 178 | 0 | 0 | ready for first real assembler byte-equivalence pilot |

## Blockers

### `src/c3/equipment_battle_selector_helpers.asm`

- none

### `src/c3/jeff_repair_psi_helpers.asm`

- none

### `src/c3/hp_pp_adjustment_helpers.asm`

- none

### `src/c3/inventory_equipment_tracked_items.asm`

- none

### `src/c3/file_select_visual_transition_helper.asm`

- none

### `src/c3/battle_visual_effect_helpers.asm`

- none

### `src/c3/window_text_helpers.asm`

- none
