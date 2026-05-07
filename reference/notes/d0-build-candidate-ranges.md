# D0 build-candidate byte ranges

This manifest records source slices promoted into the reusable source-bank scaffold pipeline.

## Summary

- ranges: `11`
- total bytes: `65536`
- source bytes: `0`
- data gap bytes: `65536`

## Ranges

| Level | Source Path | Range | Span Bytes | Source Bytes | Data Gap Bytes | SHA-1 |
| --- | --- | --- | ---: | ---: | ---: | --- |
| `build-candidate` | `src/d0/table_door_pointer_table.asm` | `D0:0000..D0:1400` | 5120 | 0 | 5120 | `98894a101cccf358992ca5ac629645ec499d2b1d` |
| `build-candidate` | `src/d0/table_screen_transition_config_table.asm` | `D0:1400..D0:1598` | 408 | 0 | 408 | `67a3160c6fd873570a1498e80e288c9f712c55db` |
| `build-candidate` | `src/d0/table_event_control_ptr_table.asm` | `D0:1598..D0:15C0` | 40 | 0 | 40 | `0b1163a6213cb495e185320d6e5d456871f04f62` |
| `build-candidate` | `src/d0/table_map_tile_event_control_table.asm` | `D0:15C0..D0:1880` | 704 | 0 | 704 | `d30b6eee12c680e300448ae233890f2302535186` |
| `build-candidate` | `src/d0/table_map_enemy_placement.asm` | `D0:1880..D0:B880` | 40960 | 0 | 40960 | `4d4df55dc1c3eacaf258f4d5dc1a9bdcadaef644` |
| `build-candidate` | `src/d0/table_enemy_placement_groups_ptr_table.asm` | `D0:B880..D0:BBAC` | 812 | 0 | 812 | `21f51e1de1a05ad3a8bd66658bb6982d16a3b439` |
| `build-candidate` | `src/d0/table_enemy_placement_groups_table.asm` | `D0:BBAC..D0:C60D` | 2657 | 0 | 2657 | `6c2d227f1a84e0bcff2f628672cd3e77a5389a37` |
| `build-candidate` | `src/d0/table_btl_entry_ptr_table.asm` | `D0:C60D..D0:D52D` | 3872 | 0 | 3872 | `95a6cc0eb36c958a4cd69eaf43cdbfe4eade8484` |
| `build-candidate` | `src/d0/table_enemy_battle_groups_table.asm` | `D0:D52D..D0:DFB4` | 2695 | 0 | 2695 | `e5e2871d05b0ae9b3ee0583228398320af0d0d0a` |
| `build-candidate` | `src/d0/asset_audio_pack_139.asm` | `D0:DFB4..D0:FFA8` | 8180 | 0 | 8180 | `c20cf02e14338f7b9bfb19aad161e7c701141a3b` |
| `build-candidate` | `src/d0/padding_d0_tail_slack.asm` | `D0:FFA8..D0:10000` | 88 | 0 | 88 | `5c0a9085206c2dafcf9c1cb2c0a8dabdc387c895` |

## Source Segments

### `src/d0/table_door_pointer_table.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `D0:0000..D0:1400` (`5120` bytes, SHA-1 `98894a101cccf358992ca5ac629645ec499d2b1d`) `DoorPointerTable`

Labels:

- `D0:0000 DoorPointerTable`

Evidence:

- `build/d0-table-splits.json`
- `notes/d0-table-splits.md`

### `src/d0/table_screen_transition_config_table.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `D0:1400..D0:1598` (`408` bytes, SHA-1 `67a3160c6fd873570a1498e80e288c9f712c55db`) `ScreenTransitionConfigTable`

Labels:

- `D0:1400 ScreenTransitionConfigTable`

Evidence:

- `build/d0-table-splits.json`
- `notes/d0-table-splits.md`

### `src/d0/table_event_control_ptr_table.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `D0:1598..D0:15C0` (`40` bytes, SHA-1 `0b1163a6213cb495e185320d6e5d456871f04f62`) `EventControlPtrTable`

Labels:

- `D0:1598 EventControlPtrTable`

Evidence:

- `build/d0-table-splits.json`
- `notes/d0-table-splits.md`

### `src/d0/table_map_tile_event_control_table.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `D0:15C0..D0:1880` (`704` bytes, SHA-1 `d30b6eee12c680e300448ae233890f2302535186`) `MapTileEventControlTable`

Labels:

- `D0:15C0 MapTileEventControlTable`

Evidence:

- `build/d0-table-splits.json`
- `notes/d0-table-splits.md`

### `src/d0/table_map_enemy_placement.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `D0:1880..D0:B880` (`40960` bytes, SHA-1 `4d4df55dc1c3eacaf258f4d5dc1a9bdcadaef644`) `MapEnemyPlacement`

Labels:

- `D0:1880 MapEnemyPlacement`

Evidence:

- `build/d0-table-splits.json`
- `notes/d0-table-splits.md`

### `src/d0/table_enemy_placement_groups_ptr_table.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `D0:B880..D0:BBAC` (`812` bytes, SHA-1 `21f51e1de1a05ad3a8bd66658bb6982d16a3b439`) `EnemyPlacementGroupsPtrTable`

Labels:

- `D0:B880 EnemyPlacementGroupsPtrTable`

Evidence:

- `build/d0-table-splits.json`
- `notes/d0-table-splits.md`

### `src/d0/table_enemy_placement_groups_table.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `D0:BBAC..D0:C60D` (`2657` bytes, SHA-1 `6c2d227f1a84e0bcff2f628672cd3e77a5389a37`) `EnemyPlacementGroupsTable`

Labels:

- `D0:BBAC EnemyPlacementGroupsTable`

Evidence:

- `build/d0-table-splits.json`
- `notes/d0-table-splits.md`

### `src/d0/table_btl_entry_ptr_table.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `D0:C60D..D0:D52D` (`3872` bytes, SHA-1 `95a6cc0eb36c958a4cd69eaf43cdbfe4eade8484`) `BtlEntryPtrTable`

Labels:

- `D0:C60D BtlEntryPtrTable`

Evidence:

- `build/d0-table-splits.json`
- `notes/d0-table-splits.md`

### `src/d0/table_enemy_battle_groups_table.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `D0:D52D..D0:DFB4` (`2695` bytes, SHA-1 `e5e2871d05b0ae9b3ee0583228398320af0d0d0a`) `EnemyBattleGroupsTable`

Labels:

- `D0:D52D EnemyBattleGroupsTable`

Evidence:

- `build/d0-table-splits.json`
- `notes/d0-table-splits.md`

### `src/d0/asset_audio_pack_139.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `D0:DFB4..D0:FFA8` (`8180` bytes, SHA-1 `c20cf02e14338f7b9bfb19aad161e7c701141a3b`) `AudioPack139`

Labels:

- `D0:DFB4 AudioPack139`

Evidence:

- `build/d0-table-splits.json`
- `notes/d0-table-splits.md`

### `src/d0/padding_d0_tail_slack.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `D0:FFA8..D0:10000` (`88` bytes, SHA-1 `5c0a9085206c2dafcf9c1cb2c0a8dabdc387c895`) `D0TailSlack`

Labels:

- `D0:FFA8 D0TailSlack`

Evidence:

- `build/d0-table-splits.json`
- `notes/d0-table-splits.md`

## Notes

The scaffold preserves intentional source-adjacent data gaps from the manifest and validates each protected span against the original ROM bytes.
