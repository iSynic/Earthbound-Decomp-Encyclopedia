# CoilSnake Phase 2C Promotion Assessment

This note decides which Phase 2C CoilSnake results are ready for local contract promotion.
It is intentionally stricter than the raw diff classification: a small CoilSnake-rebuild diff is not promoted unless it also lines up with local original-ROM contracts.

## Summary

- `authoring-lowering-only`: `2`
- `defer-original-runtime-promotion`: `4`
- `promote-to-local-contract`: `2`

## Decisions

| Experiment | Behavior | Assessment | Changed span | Action |
| --- | --- | --- | --- | --- |
| `ccscript-body-command-byte-probe` | `script-lowering` | `authoring-lowering-only` | `0x3896F6 (F8:96F6)..0x3896F7 (F8:96F7)` | `keep-as-oracle-evidence` |
| `ccscript-rom-goto-label-probe` | `script-lowering` | `authoring-lowering-only` | `0x050001 (C5:0001)..0x050003 (C5:0003)` | `keep-as-oracle-evidence` |
| `font0-width5-probe` | `fixed-byte` | `defer-original-runtime-promotion` | `0x0F60DC (CF:60DC)..0x0F60DD (CF:60DD)` | `record-as-rebuilt-layout-evidence` |
| `bg-data-distortion1-probe` | `fixed-byte` | `promote-to-local-contract` | `0x0ADCD0 (CA:DCD0)..0x0ADCD1 (CA:DCD1)` | `promote-runtime-correlated-field` |
| `town-map-first-icon-x-probe` | `fixed-byte` | `defer-original-runtime-promotion` | `0x2011A4 (E0:11A4)..0x2011A5 (E0:11A5)` | `record-as-rebuilt-layout-evidence` |
| `windowgraphics-windows1-copy-probe` | `bounded-insertion` | `promote-to-local-contract` | `0x201FCB (E0:1FCB)..0x202000 (E0:2000)` | `promote-bounded-insertion-evidence` |
| `battlesprite-001-copy-probe` | `broad-repack` | `defer-original-runtime-promotion` | `0x00EBF3 (C0:EBF3)..0x2F11C8 (EF:11C8)` | `keep-as-compiler-behavior-constraint` |
| `tileset00-fts-nibble-probe` | `broad-repack` | `defer-original-runtime-promotion` | `0x188F7B (D8:8F7B)..0x2F10B8 (EF:10B8)` | `keep-as-compiler-behavior-constraint` |

## Local Reads

### `ccscript-body-command-byte-probe`

- assessment: `authoring-lowering-only`
- local result: CCScript body argument lowering is isolated in the scriptdump rebuild, but text VM semantics remain owned by local C1 parser/handler evidence.
- local docs: `notes/coilsnake-ccscript-experiments.md`, `notes/text-script-assets-frontier.md`

### `ccscript-rom-goto-label-probe`

- assessment: `authoring-lowering-only`
- local result: CCScript label reference lowering is isolated in the scriptdump rebuild, but it is not a runtime command semantic.
- local docs: `notes/coilsnake-ccscript-experiments.md`, `notes/text-script-assets-frontier.md`

### `font0-width5-probe`

- assessment: `defer-original-runtime-promotion`
- local result: The CoilSnake rebuild byte lands at CF:60DC, which is inside the original ROM's CF event-music/table corridor rather than the checked E0/E1 font metric ranges.
- local docs: `notes/font-bundle-contracts.md`, `notes/ui-font-town-map-asset-contracts.md`

### `bg-data-distortion1-probe`

- assessment: `promote-to-local-contract`
- local result: The byte lands at CA:DCD0, inside the original CA battle-background config table. Relative to CA:DCA1, this is row 2 offset +0x2F overall / row offset +0x0D, matching the first distortion reference slot documented for BG_DATA_TABLE rows.
- local docs: `notes/battle-background-scene-bundles.md`, `notes/battle-visual-asset-contracts.md`

### `town-map-first-icon-x-probe`

- assessment: `defer-original-runtime-promotion`
- local result: The CoilSnake rebuild byte lands at E0:11A4, which is inside the original ROM's compressed SRAM template range, while original town-map icon placement records live in E1:F4A9..E1:F581.
- local docs: `notes/town-map-selection-rendering-c4d274-c4d744.md`, `notes/ui-font-town-map-asset-contracts.md`

### `windowgraphics-windows1-copy-probe`

- assessment: `promote-to-local-contract`
- local result: The bounded changed span E0:1FCB..E0:2000 sits inside the original text-window palette-block contract E0:1FC8..E0:2188.
- local docs: `notes/text-window-skin-bundle-contracts.md`, `notes/ui-font-town-map-asset-contracts.md`

### `battlesprite-001-copy-probe`

- assessment: `defer-original-runtime-promotion`
- local result: The broad changed span reflects compression/repacking behavior across many ROM regions, so it should constrain editor/tool expectations rather than name a stable runtime field.
- local docs: `notes/battle-sprite-bundle-contracts.md`

### `tileset00-fts-nibble-probe`

- assessment: `defer-original-runtime-promotion`
- local result: The broad changed span reflects tileset compression/repacking behavior, so it should constrain editor/tool expectations rather than name a stable runtime field.
- local docs: `notes/map-tileset-bundles.md`
