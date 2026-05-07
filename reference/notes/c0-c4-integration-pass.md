# C0-C4 Integration Pass

This is the current front door for banks `C0` through `C4` after the C4
frontier closure pass. It is meant to connect the per-bank archaeology notes,
machine-readable names, and data contracts into one working map.

## Current artifact set

| Artifact | Purpose |
| --- | --- |
| `build/working-names-c0-c4.json` | Machine-readable working-name manifest for `C0`-`C4`. |
| `build/labels/working-names-c0-c1-c2-c3-c4.tsv` | Reviewable address/name/evidence table for import or diffing. |
| `build/labels/working-names-c0-c1-c2-c3-c4.ca65.inc` | ca65 constants for source experiments. |
| `build/labels/working-names-c0-c1-c2-c3-c4.asar.inc` | Asar constants for patch experiments. |
| `build/labels/working-names-c0-c1-c2-c3-c4.sym` | Debugger symbol file. |
| `build/data-contracts-c0-c4.json` | Machine-readable WRAM/ROM table contract manifest. |
| `notes/data-contracts-c0-c4.md` | Human-readable version of the data-contract manifest. |
| `notes/bank-c0-working-name-proposals.md` through `notes/bank-c4-working-name-proposals.md` | Bank-scoped review lists. |

## Summary

Working-name manifest:

| Bank | Entries |
| --- | ---: |
| `C0` | 503 |
| `C1` | 171 |
| `C2` | 211 |
| `C3` | 163 |
| `C4` | 351 |

Total entries: `1399`.

Confidence split:

| Confidence | Entries |
| --- | ---: |
| `proposed` | 1335 |
| `corroborated` | 64 |

Data-contract manifest:

| Domain | Contracts |
| --- | ---: |
| `rom-table` | 26 |
| `wram-overlay` | 1 |
| `wram-root` | 5 |

Total contracts: `32`; total fields: `329`.

## Integration fix made in this pass

`C1:E48D` had two promoted working names:

- `RenderTextInputRowScoped`
- `RenderSingleTextInputOptionRowScoped`

The second name is more specific and is backed by
`notes/text-input-dialog-option-helpers-c1e48d-c1e4be.md`, so the subsystem
synthesis note now uses `RenderSingleTextInputOptionRowScoped`. This removed
the duplicate-label conflict and allowed the C0-C4 label bundle to emit cleanly.

## Cross-bank system map

### Overworld entity and movement runtime

Primary banks: `C0`, `C3`, `C4`.

- `C0` owns the live entity/task runtime, collision probes, pathing helpers,
  staged-movement callers, scroll/timing services, and interaction flow.
- `C3` supplies script payloads, movement parameter tables, and menu/visual data
  that C0/C2 consumers index.
- `C4` supplies many visual/runtime helpers that C0 calls into: current-slot
  wrappers, staged movement pulse generation, window-mask HDMA, visual records,
  file-select/town-map helpers, and transition support.

Useful contract anchors:

- `INPUT_DIRECTION_PERMISSION_MASK_TABLE`
- `INTERACTION_PROBE_DIRECTION_X_OFFSETS`
- `INTERACTION_PROBE_DIRECTION_Y_OFFSETS`
- `MAP_ENTITY_PLACEMENT_DIRECTION_PARAM_TABLE`
- `MOVEMENT_OCTANT_TO_PULSE_SELECTOR_TABLE`
- `MOVEMENT_OCTANT_SIGNED_UNIT_DELTA_TABLE`

### Text, windows, menus, and naming

Primary banks: `C1`, `C4`, with C0/C2 callers.

- `C1` owns the text engine, text command VM, menu wrappers, battle text entry,
  file-select menus, and naming/text-input front end.
- `C4` owns lower-level text tile staging, glyph/tile upload helpers, window
  palette/color math, active-window tile placement, and naming-buffer helpers.
- Several C1 UI flows call C4 rendering helpers rather than owning the pixel
  side directly.

Useful contract anchors:

- `TITLE_NAME_BUFFER_CURSOR_TILE_RUN`
- `BLINKING_TRIANGLE_WAIT_FRAME_TILES`
- `BLANK_COMMON_TILE_SOURCE_BLOCK`
- `WH_WINDOW_SPAN_RADIUS_RAMP_TABLE`

### Battle engine and battle visuals

Primary banks: `C1`, `C2`, `C3`, plus C4 visual helpers.

- `C1` handles battle-facing text, target prompts, PSI/item/equipment menus,
  battle text entry, and some UI snapshots.
- `C2` owns battle action resolution, status/stat/resource effects, HP/PP
  windows, sprite/palette operations, battle background state, and visual tails.
- `C3` supplies fixed battle visual data tables and script/data payloads.
- `C4` contributes battle overlay script state and coffee/tea or landing-style
  visual transfer helpers.

Useful contract anchors:

- `BATTLERS_TABLE`
- `BATTLE_SELECTION_SNAPSHOT`
- `BATTLE_ACTION_TABLE`
- `PSI_ABILITY_TABLE`
- `ENEMY_CONFIGURATION_TABLE`
- `LOADED_BG_DATA_LAYER1`
- `LOADED_BG_DATA_LAYER2`
- `BATTLE_VISUAL_GRAPHICS_SOURCE_STRIP_OFFSETS`
- `BATTLE_VISUAL_OAM_TILE_INDEX_GRID`
- `BATTLE_PALETTE_SET_ROWS`
- `BATTLE_VISUAL_TOKEN_23_TO_2D_COLOUR_TRIPLES`
- `BATTLE_VISUAL_TOKEN_31_TO_35_COLOUR_TRIPLES`

### Inventory, equipment, party state, and item effects

Primary banks: `C1`, `C2`, `C3`, `C4`.

- `C1` owns most UI-front helpers for inventory, equipment, PSI, and item names.
- `C2` owns item effect resolution and battle action consequences.
- `C3` supplies some item-slot helper and script-facing support.
- `C4` contributes party-state reset, search helpers, tracked-item pulse slots,
  and visual/overlay arbitration.

Useful contract anchors:

- `GAME_STATE`
- `PARTY_CHARACTERS`
- `ITEM_CONFIGURATION_TABLE`
- `BATTLE_ACTION_TABLE`

### Landing, coffee/tea, flyover, sanctuary, and file-select displays

Primary banks: `C0`, `C3`, `C4`, with some C1 menu support.

- C0 contains the landing assembly and HDMA/PPU staging callers.
- C4 contains landing palette interpolation, coffee/tea tile rendering, flyover
  text scene dispatch, Sound Stone presentation data, Your Sanctuary display
  helpers, file-select entity scripts, and town-map selection rendering.
- C3 contributes visual tables and script payloads.

Useful contract anchors:

- `BLANK_COMMON_TILE_SOURCE_BLOCK`
- `BATTLE_PALETTE_SET_ROWS`
- `YOUR_SANCTUARY_LOCATION_COORDINATE_TABLE`

## Confidence boundaries

This integration pass means the naming and contract artifacts are internally
consistent enough to export and diff. It does not mean every proposed name is
final. The `proposed` confidence level is intentionally common: most names are
local, descriptive labels with direct evidence, not upstream/community-approved
symbol names.

The most valuable next refinements are:

- turn high-traffic `proposed` names into `corroborated` names when the same
  contract is independently proven in multiple notes
- split large visual data blobs into stricter table contracts
- add table-value examples to the handoff package for any symbol that may be
  hard to trust from the name alone
- compare our generated label bundle against ebsrc's current symbol includes
  before attempting upstream-style patches

