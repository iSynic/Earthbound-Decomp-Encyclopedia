# Map Milestone Closure

Status: closed for the current contract/research phase.

This milestone turns the map layer from scattered reference exports and ROM
tables into a reproducible set of checked-in contracts. The contracts are
designed for romhack research now and for later extraction/port tooling: they
record IDs, counts, joins, hashes, table ranges, runtime masks, and dependency
relationships without checking in ROM-derived rendered assets.

## Rebuild Command

Regenerate the checked-in map contracts in dependency order:

```powershell
python tools/run_map_contracts.py
```

Useful variants:

```powershell
python tools/run_map_contracts.py --list
python tools/run_map_contracts.py --dry-run
python tools/run_map_contracts.py --start-at map-collision-attribute
python tools/run_map_contracts.py --only map-palette-pointer-table map-fts-palette-variant
python tools/run_map_contracts.py --rom "<path-to-user-rom>"
```

Preview renderers remain separate and opt-in because they write ignored local
outputs under `build/`.

## Closed Contracts

| Layer | Primary Contract | Tool | Closure Status |
| --- | --- | --- | --- |
| NPC visuals | `notes/map-sprite-usage-contract.json` | `tools/build_map_sprite_usage_contract.py` | `1582` placed objects joined to sprite metadata/runtime roles. |
| NPC movement/scripts | `notes/map-movement-usage-contract.json` | `tools/build_map_movement_usage_contract.py` | `136` used movement IDs joined to C4/C3 targets; `21` late refs are known missing files. |
| Placed object rows | `notes/map-object-bundles.json` | `tools/build_map_object_bundle_contract.py` | `1582` placed rows carry position, visual role, behavior target, flags, and text pointers. |
| Sector inventory | `notes/map-sector-bundles.json` | `tools/build_map_sector_bundle_contract.py` | All `1280` sectors carry objects, triggers, doors, hotspots, enemy groups, music, map-change counts, and map-tile hashes. |
| Tileset dependencies | `notes/map-tileset-bundles.json` | `tools/build_map_tileset_bundle_contract.py` | Full `0..31` tileset ID domain mapped; `28` IDs used by sectors and `20` direct `.fts` exports present. |
| `.fts` format | `notes/map-fts-format-audit.json` | `tools/build_map_fts_format_audit.py` | All `20` direct exports share the stable `64/290/96` section shape. |
| Arrangement cells | `notes/map-fts-arrangement-contract.json` | `tools/build_map_fts_arrangement_contract.py` | `20480` records / `327680` cells decoded as 2-byte BG descriptor plus 1-byte collision attribute. |
| Palette variant rows | `notes/map-fts-palette-variant-contract.json` | `tools/build_map_fts_palette_variant_contract.py` | All `168` 290-char rows verified as DA palette variants, with `0` unexplained mismatches. |
| Tile animation runtime | `notes/map-tile-animation-runtime-contract.json` | `tools/build_map_tile_animation_runtime_contract.py` | EF pointer tables and C0 `$43DC` upload records closed for `20` animation IDs. |
| Scene composition | `notes/map-scene-composition-contract.json` | `tools/build_map_scene_composition_contract.py` | All `1280` sectors joined to tileset/palette/feature status; `950` have direct `.fts` contracts. |
| Palette descriptor roles | `notes/map-palette-descriptor-context.json` | `tools/build_map_palette_descriptor_context.py` | Descriptor palettes `2..7` map to DA subpalettes `0..5`; palettes `0..1` are text/common palette space. |
| Palette pointer table | `notes/map-palette-pointer-table-contract.json` | `tools/build_map_palette_pointer_table_contract.py` | DA `32`-entry long-pointer table verified with `32` exact asset matches. |
| Palette script usage | `notes/map-palette-command-usage-contract.json` | `tools/build_map_palette_command_usage_contract.py` | All `33` `CHANGE_MAP_PALETTE` hits join to resolved palette variants. |
| Collision scene context | `notes/map-collision-attribute-context.json` | `tools/build_map_collision_attribute_context.py` | `972800` live-scene cells sampled across `950` direct `.fts` sectors. |
| Collision storage | `notes/map-collision-pointer-contract.json` | `tools/build_map_collision_pointer_contract.py` | `12423 / 12423` D8 pointer entries match `.fts` collision records exactly; `0` bad pointers. |
| Collision runtime bits | `notes/map-collision-runtime-bit-contract.json` | `tools/build_map_collision_runtime_bit_contract.py` | C0 masks, six sample points, and major bit roles promoted from runtime evidence. |

## Major Results

- The placed-object layer is portable: visual identity, behavior targets, event
  flags, text pointers, and map positions are joined in row-per-object form.
- Every world sector has a stable inventory row with object, trigger, door,
  hotspot, enemy, music, map-change, tileset, palette, and map-tile context.
- The direct `.fts` format is split into tile pixels, palette variants, and
  arrangement/collision records.
- Arrangement descriptor words are SNES BG tilemap words. Descriptor palette
  values `2..7` resolve to the six DA map-palette subpalettes.
- The variable 290-character `.fts` rows are palette variants, not tile
  animation scripts.
- Map tile animation is tied to EF graphics/script pointer tables and the C0
  upload-record runtime.
- The `.fts` collision byte is storage-verified against bank D8: all pointer
  entries resolve to the exact 16 collision bytes for the matching metatile.
- Runtime collision masks are now grounded: observed solid/high collision is
  `0x80`, `0x10` is the coordinate-latch/special-surface bit, and `0x04/0x08`
  feed entity terrain compatibility.

## Deferred On Purpose

These are not blockers for closing this milestone; they are the next phase's
edge work.

- Collision low bits `0x01/0x02`: preserved and counted, but still need
  caller-side gameplay labels before they should be named more strongly.
- DA palette metadata words: event flag, event palette selector, sprite
  palette, and flash-effect words are structurally identified, but their full
  runtime behavior should be followed separately.
- Text/common palette space: descriptor palettes `0..1` are identified as
  outside the DA map-palette payload, but preview tooling still treats them as
  overflow/fallback until the common palette source is joined.
- Palette-settings-only tilesets: `10` sector-used tileset IDs have palette
  settings without direct local `.fts` exports.
- Event/actionscript semantics: movement IDs and behavior entrypoints are
  joined to refs, but this milestone does not execute or fully decompile every
  script payload.
- Engine-ready map bundles: the contracts are suitable inputs for a future
  installer/extractor/port pipeline, but no final native map-runtime schema is
  claimed here.

## Next Good Phase

The best next phase is not more map counting. It is either:

- finish the small caller-side collision labels for `0x01/0x02`, then treat map
  collision as semantically closed enough for tooling; or
- move to a broader asset phase and start building engine-ready bundle schemas
  that consume these contracts while preserving the end-user-supplied-ROM model.

For a future port, this milestone is enough to begin designing the map asset
loader boundaries: sectors, tilesets, palette variants, tile animation records,
collision records, placed objects, and behavior pointers are now stable inputs.
