# C3 map movement parameter table E1D8-E240

## Reference context

This pass covers the remaining unnoted C3 unknown include starts in the movement-data cluster:

- `C3:E1D8` `data/unknown/C3E1D8.asm`
- `C3:E1E0` `data/unknown/C3E1E0.asm`

In `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank03.asm`, the cluster appears immediately after named map movement data:

- `data/map/character_initial_entity_data.asm`
- `data/map/character_sizes.asm`
- `data/map/movement_speeds.asm`
- `data/map/allowed_input_directions.asm`
- `data/map/mushroomization_direction_remap_tables.asm`

The legacy disassembly labels the whole block as `DATA_C3E1D8`.

## Consumer evidence

`tools/find_xrefs.py C3E1D8` finds two long pointer users at `C0:6D29` and `C0:6D93`. Both are inside the same C0 placement/update path:

```text
C0:6D27  AA               tax
C0:6D28  BF D8 E1 C3      lda $C3E1D8,X
C0:6D2C  C9 02 00         cmp #$0002
...
C0:6D91  AA               tax
C0:6D92  BF D8 E1 C3      lda $C3E1D8,X
C0:6D96  A8               tay
C0:6D97  A6 04            ldx $04
C0:6D99  A5 02            lda $02
C0:6D9B  22 A9 3F C0      jsl $C03FA9
```

The index is derived by normalizing a packed field from the current entity/object record through `C0:9251`, then doubling it. The value is used first as a special-case test against `#$0002`, then as the `Y` argument into `C0:3FA9` (`Refresh_PostTransitionEntityPlacement` in the local working-name manifest). That makes `C3:E1D8` part of the map entity placement/direction parameter family rather than free-form unknown data.

## Table shape

The exact table bytes in the verified ROM are:

```text
C3:E1D8: 0004 0000 0002 0006
C3:E1E0: 0000 0000 0004 0000
C3:E1E8: 0000 0000 FFFC 0000
C3:E1F0: FFFC 0000 0000 0000
C3:E1F8: 0004 0000 0000 0000
C3:E200: 0007 0001 0005 0003
C3:E208: 0002 0006 0002 0006
C3:E210: 0000 0008 0000 0008
C3:E218: 0000 0000 0008 0008
C3:E220: 0008 0000 0008 0000
C3:E228: 0008 0008 0000 0000
C3:E230: 0000 0001 0001 0001
C3:E240: FFFF FFFF 0000 0001
         0001 0001 0000 FFFF
```

Existing movement notes already establish the later sub-blocks:

- `C3:E200/E208` are direction-like parameters consumed by the staged movement wrapper through `C4:8E6B`.
- `C3:E210/E218` and `C3:E220/E228` are 8-pixel sub-tile offset sets used by staged movement setup.
- `C3:E230/E240` are direction-dependent coarse-cell offset tables used by the type-6 door candidate probe.

The newly covered `C3:E1D8-E1FF` prefix belongs to that same map movement parameter family, but its values are consumed by C0 entity placement rather than the C4 staged-movement helper.

## Working Names

- `C3:E1D8` = `MapEntityPlacementDirectionParamTable`
- `C3:E1E0` = `MapEntityPlacementDirectionParamTable_Page1`
- `C3:E200` = `StagedMovementPrimaryDirectionParamTable`
- `C3:E208` = `StagedMovementAlternateDirectionParamTable`
- `C3:E210` = `StagedMovementSubtileOffsetSetA_X`
- `C3:E218` = `StagedMovementSubtileOffsetSetA_Y`
- `C3:E220` = `StagedMovementSubtileOffsetSetB_X`
- `C3:E228` = `StagedMovementSubtileOffsetSetB_Y`
- `C3:E230` = `DoorCandidateDirectionOffsetX`
- `C3:E240` = `DoorCandidateDirectionOffsetY`

## Remaining questions

- `C0:6D00` has no direct-call hits, so its entry mechanism is probably a dispatch/jump-table path. That should be pinned before making the `E1D8-E1FF` subtable name more specific.
- The exact semantic split inside `C3:E1D8-E1FF` still needs C0-side struct field names for the packed entity/object word read from `[$0A]+6`.
