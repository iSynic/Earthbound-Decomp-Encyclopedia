# Map Object Layer Closure

Date: 2026-04-27

This note closes the current overworld placed-object refinement phase. The goal of
the phase was to turn separate sprite, movement, and NPC config facts into a
portable object layer that a future editor, installer, or native port can consume
without hard-coding scattered SNES bank addresses.

## Durable Artifacts

- `notes/map-sprite-usage-contract.json`
- `notes/map-movement-usage-contract.json`
- `notes/map-object-bundles.json`
- `tools/build_map_sprite_usage_contract.py`
- `tools/build_map_movement_usage_contract.py`
- `tools/build_map_object_bundle_contract.py`

The Markdown companions summarize those JSON contracts:

- `notes/map-sprite-usage-contract.md`
- `notes/map-movement-usage-contract.md`
- `notes/map-object-bundles.md`

## What Is Covered

- `1584` NPC config rows are joined to visual metadata.
- `1582` map placements are exposed as stable `map_object.NNNN` rows.
- `627` of the `1280` map sectors contain placed objects.
- `297` unique NPC sprite IDs are covered.
- `163` unique sprite IDs have full animation-role contracts.
- `133` unique sprite IDs decode direct EF runtime slot records from the ROM.
- Only sprite `0` (`OVERWORLD_SPRITE::NONE`) remains metadata-only.
- `136` unique NPC movement IDs are used by NPC configs.
- All `895` C4 event pointer-table targets are decoded to concrete addresses.
- `115` used movement IDs resolve to present ebsrc script files.
- `21` used movement IDs point at expected but missing late ebsrc script files.

## Object Bundle Shape

`notes/map-object-bundles.json` is the practical consumption layer. Each placed
object row has:

- stable `object_id` such as `map_object.0000`
- NPC config ID
- sector and world-pixel position
- NPC type, visibility rule, and initial direction
- sprite ID, sprite label, palette ID, runtime slot count, and role model
- movement ID, ebsrc event label, decoded C4 pointer-table target address, and
  behavior source status
- event flag and text pointer fields

That means a consumer can ask one joined question:

> What is placed here, what does it look like, what behavior entrypoint does it
> use, and what interaction fields are attached?

Before this pass, those answers lived across map placement YAML, NPC config YAML,
overworld sprite metadata, EF sprite grouping pointers, C4 event pointer bytes,
and C3 event/actionscript refs.

## Late Movement Script Family

The remaining `21` placed objects without present ref script files are no longer
address-unknown. They are movement IDs `870-873` and `875-891`, with C3 targets
from `C3:9623` through `C3:9A28`.

The first script, `EVENT_870` at `C3:9623`, decodes as:

```text
EVENT_SHORTCALL $C3:9AC7
EVENT_PAUSE $01
EVENT_CALLROUTINE $C0:A84C, $E7, $01
EVENT_SHORTCALL_CONDITIONAL local_wait
EVENT_SET_VAR $00, $1684
EVENT_SET_VAR $01, $20C0
EVENT_SET_VAR $02, $001C
EVENT_SET_VAR $03, $0008
EVENT_CALLROUTINE $C4:6E74
EVENT_SHORTCALL_CONDITIONAL local_wait
EVENT_SHORTCALL $C3:9E01
EVENT_CALLROUTINE $C0:A88D, $C6, $00, $58, $88
EVENT_HALT
```

The sampled late scripts follow the same 0x31-byte template:

1. run common setup at `C3:9AC7`
2. wait until a `C0:A84C` read/check succeeds
3. load four coordinate/size-style vars
4. call `C4:6E74`
5. run common setup at `C3:9E01`
6. queue a text pointer through `C0:A88D`
7. halt

So the remaining gap is not a broad unknown behavior class. It is a compact,
repetitive late script family whose source files are absent from the local ebsrc
checkout. A later event-script phase can emit or reconstruct these as generated
script assets directly from the ROM.

## What This Enables

For romhacking:

- Find all placed uses of a sprite label or movement ID.
- See object visibility/event flag rules without manually joining tables.
- Locate which sectors contain dense object clusters.
- Identify text-bearing objects and script-bearing objects.
- Trace an object from map position to visual payload and behavior entrypoint.

For a future port or editor:

- Build a first object-placement database without distributing ROM-derived
  graphics or script payloads.
- Use stable object IDs instead of raw map-list offsets.
- Load visual assets through generated asset manifests and sprite contracts.
- Route behavior through script IDs and pointer target addresses until the event
  VM layer is lifted into higher-level semantics.

## Explicit Deferrals

This phase does not fully decompile event/actionscript semantics. It identifies
behavior entrypoints, macro profiles, source-file coverage, pointer targets, and
object usage. Full event VM semantics remain a later phase.

This phase also does not yet bundle the map substrate under the objects:

- map sector tile graphics
- map sector arrangements
- palettes
- collision
- doors and warp triggers
- area metadata

Those are the next natural world-layer targets.

## Recommended Next Frontier

The next frontier has started with `notes/map-sector-bundles.json`, a first-pass
map-sector bundle contract that joins:

1. sector IDs from the same 40x32 world grid used by object placements
2. placed `map_object.NNNN` IDs from `notes/map-object-bundles.json`
3. sector metadata from `map_sectors.yml`
4. door, rope, ladder, stairway, escalator, switch, person, and object trigger
   refs from `map_doors.yml`
5. enemy-map groups, music options, hotspots, map-change group counts, and
   `map_tiles.map` sector hashes

`notes/map-tileset-bundles.json` now adds the first tileset dependency layer:
all sector rows point at stable `map_tileset.NN` IDs, `18` used tileset IDs have
direct `.fts` exports in refs, and `10` used IDs currently have palette settings
only.

The remaining refinements are to attach true decoder outputs:

1. tileset graphics
2. arrangements
3. palettes
4. collision
5. door/warp destination bundles

That will turn the current sector inventory into scene bundles: not just "what
objects exist," but "what world surface are they standing on?"
