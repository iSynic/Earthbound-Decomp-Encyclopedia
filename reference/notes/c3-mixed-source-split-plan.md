# C3 mixed data/source split plan

Generated from `build/c3-source-data-map.json`. This file is the mechanical carving plan for addressed data includes that contain embedded ordinary 65816 source helpers.

## Summary

- schema: `earthbound-decomp.c3-mixed-source-split-plan.v1`
- mixed rows: `2`
- total slices: `5`
- source-helper slices: `3`
- source-helper addresses: `['C3:E977', 'C3:E9A0', 'C3:F3C5']`

## Rows

### `C3:E84E` `data/unknown/C3E84E.asm`

- range: `C3:E84E..C3:E9F7`
- size: `0x1A9`

| Slice | Range | Size | Kind | Name | Extraction Expectation |
| --- | --- | ---: | --- | --- | --- |
| `C3:E84E` | `C3:E84E..C3:E977` | `0x129` | `leading-data` | `C3E84E_LeadingData` | preserve as data before embedded source-helper labels |
| `C3:E977` | `C3:E977..C3:E9A0` | `0x29` | `source-helper` | `ReadCharacterInventorySlotByte` | emit as standalone ordinary 65816 source helper from mixed include row |
| `C3:E9A0` | `C3:E9A0..C3:E9F7` | `0x57` | `source-helper` | `CheckEquippedInventorySlotReference` | emit as standalone ordinary 65816 source helper from mixed include row |

### `C3:F2B1` `data/unknown/C3F2B1.asm`

- range: `C3:F2B1..C3:F5F9`
- size: `0x348`

| Slice | Range | Size | Kind | Name | Extraction Expectation |
| --- | --- | ---: | --- | --- | --- |
| `C3:F2B1` | `C3:F2B1..C3:F3C5` | `0x114` | `leading-data` | `C3F2B1_LeadingData` | preserve as data before embedded source-helper labels |
| `C3:F3C5` | `C3:F3C5..C3:F5F9` | `0x234` | `source-helper` | `RunFileSelectVisualTransition` | emit as standalone ordinary 65816 source helper from mixed include row |
