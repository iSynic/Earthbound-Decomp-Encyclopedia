# CoilSnake Format Experiments

This note summarizes payload-free non-script format probes.
Generated projects, image assets, and rebuilt ROMs remain under ignored `build/coilsnake/`.

## Summary

- Experiments: `6`
- Missing expected reports: `0`
- Experiment root: `build/coilsnake/edit-experiments`

| Experiment | Family | Source | Replacement | Comparison base | Changed bytes | Changed span | Evidence |
| --- | --- | --- | --- | --- | ---: | --- | --- |
| `font0-width5-probe` | `ui-font` | `Fonts/0_widths.yml` | - | `build/coilsnake/baseline-rebuild.sfc` | `1` | `0x0F60DC` (`CF:60DC`)..`0x0F60DD` (`CF:60DD`) | `diff-confirmed` |
| `bg-data-distortion1-probe` | `battle-visual` | `bg_data_table.yml` | - | `build/coilsnake/baseline-rebuild.sfc` | `1` | `0x0ADCD0` (`CA:DCD0`)..`0x0ADCD1` (`CA:DCD1`) | `diff-confirmed` |
| `town-map-first-icon-x-probe` | `ui-town-map` | `TownMaps/icon_positions.yml` | - | `build/coilsnake/baseline-rebuild.sfc` | `1` | `0x2011A4` (`E0:11A4`)..`0x2011A5` (`E0:11A5`) | `diff-confirmed` |
| `windowgraphics-windows1-copy-probe` | `ui-window-graphics` | `WindowGraphics/Windows1_0.png` | `WindowGraphics/Windows1_1.png` | `build/coilsnake/baseline-rebuild.sfc` | `27` | `0x201FCB` (`E0:1FCB`)..`0x202000` (`E0:2000`) | `diff-confirmed` |
| `battlesprite-001-copy-probe` | `battle-sprite` | `BattleSprites/001.png` | `BattleSprites/002.png` | `build/coilsnake/baseline-rebuild.sfc` | `121244` | `0x00EBF3` (`C0:EBF3`)..`0x2F11C8` (`EF:11C8`) | `diff-confirmed` |
| `tileset00-fts-nibble-probe` | `map-tileset` | `Tilesets/00.fts` | - | `build/coilsnake/baseline-rebuild.sfc` | `21693` | `0x188F7B` (`D8:8F7B`)..`0x2F10B8` (`EF:10B8`) | `diff-confirmed` |

## Interpretation

- These probes show whether CoilSnake format-facing fields lower to fixed rebuilt-ROM bytes or broader compiler rewrites.
- A one-byte diff proves edit locality in the CoilSnake baseline rebuild; runtime naming still needs local source or asset-contract correlation.
- Broad multi-run diffs are compiler/repacking evidence, not direct runtime ownership claims.
