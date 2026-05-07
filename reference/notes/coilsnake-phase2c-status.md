# CoilSnake Phase 2C Status

This note closes the current CoilSnake format-behavior pass with payload-free classifications.
Generated projects, image assets, CCScript dumps, and rebuilt ROMs remain under ignored `build/coilsnake/`.

## Summary

- Scriptdump roundtrip: `compiler-normalized-roundtrip`
- Scriptdump changed bytes: `511398` across `30055` runs
- Scriptdump changed span: `0x03FD8D (C3:FD8D)..0x38A10C (F8:A10C)`
- Classified experiments: `8`

Behavior counts:

- `bounded-insertion`: `1`
- `broad-repack`: `2`
- `fixed-byte`: `3`
- `script-lowering`: `2`

Promotion lanes:

- `authoring-lowering-only`: `2`
- `candidate-local-contract-update`: `4`
- `defer-runtime-promotion`: `2`

## Experiment Classification

| Experiment | Kind | Family | Behavior | Promotion lane | Changed bytes | Runs | Changed span |
| --- | --- | --- | --- | --- | ---: | ---: | --- |
| `ccscript-body-command-byte-probe` | `ccscript` | `text-script` | `script-lowering` | `authoring-lowering-only` | `1` | `1` | `0x3896F6 (F8:96F6)..0x3896F7 (F8:96F7)` |
| `ccscript-rom-goto-label-probe` | `ccscript` | `text-script` | `script-lowering` | `authoring-lowering-only` | `2` | `1` | `0x050001 (C5:0001)..0x050003 (C5:0003)` |
| `font0-width5-probe` | `format` | `ui-font` | `fixed-byte` | `candidate-local-contract-update` | `1` | `1` | `0x0F60DC (CF:60DC)..0x0F60DD (CF:60DD)` |
| `bg-data-distortion1-probe` | `format` | `battle-visual` | `fixed-byte` | `candidate-local-contract-update` | `1` | `1` | `0x0ADCD0 (CA:DCD0)..0x0ADCD1 (CA:DCD1)` |
| `town-map-first-icon-x-probe` | `format` | `ui-town-map` | `fixed-byte` | `candidate-local-contract-update` | `1` | `1` | `0x2011A4 (E0:11A4)..0x2011A5 (E0:11A5)` |
| `windowgraphics-windows1-copy-probe` | `format` | `ui-window-graphics` | `bounded-insertion` | `candidate-local-contract-update` | `27` | `7` | `0x201FCB (E0:1FCB)..0x202000 (E0:2000)` |
| `battlesprite-001-copy-probe` | `format` | `battle-sprite` | `broad-repack` | `defer-runtime-promotion` | `121244` | `5766` | `0x00EBF3 (C0:EBF3)..0x2F11C8 (EF:11C8)` |
| `tileset00-fts-nibble-probe` | `format` | `map-tileset` | `broad-repack` | `defer-runtime-promotion` | `21693` | `957` | `0x188F7B (D8:8F7B)..0x2F10B8 (EF:10B8)` |

## Remaining Actions

- `ready`: promote fixed-byte and bounded-insertion probes only where existing local callers/contracts already support the address.
- `ready`: keep broad-repack probes as editor/compiler behavior constraints until a narrower diff or pointer walk exists.
- `satisfied-by-policy`: avoid treating full scriptdump roundtrip output as byte-stable runtime proof.

## Interpretation

- `fixed-byte` and `bounded-insertion` probes can support local contract updates when existing source or asset notes already explain the address.
- `broad-repack` probes prove CoilSnake accepts and compiles the edit, but the changed spans are compiler/recompression behavior rather than stable runtime fields.
- `script-lowering` probes prove authoring/compiler behavior and must be joined back to local text VM evidence before naming runtime commands.
