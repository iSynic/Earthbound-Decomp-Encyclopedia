# CF build-candidate byte ranges

This manifest records source slices promoted into the reusable source-bank scaffold pipeline.

## Summary

- ranges: `11`
- total bytes: `65536`
- source bytes: `0`
- data gap bytes: `65536`

## Ranges

| Level | Source Path | Range | Span Bytes | Source Bytes | Data Gap Bytes | SHA-1 |
| --- | --- | --- | ---: | ---: | ---: | --- |
| `build-candidate` | `src/cf/table_door_data.asm` | `CF:0000..CF:264F` | 9807 | 0 | 9807 | `d1148a10239fdfad56593366e5fe18be707d719a` |
| `build-candidate` | `src/cf/table_door_config_table.asm` | `CF:264F..CF:58EF` | 12960 | 0 | 12960 | `b18e72efdccb51e290c8261b757638b9885456a9` |
| `build-candidate` | `src/cf/table_overworld_event_music_pointer_table.asm` | `CF:58EF..CF:5A39` | 330 | 0 | 330 | `76d96bef963a70bc9923fd2b6acd8e979381430d` |
| `build-candidate` | `src/cf/table_overworld_event_music_table.asm` | `CF:5A39..CF:61DD` | 1956 | 0 | 1956 | `69fb88a79649e5f81be910222d7670c9d6592d23` |
| `build-candidate` | `src/cf/table_cf_inline_event_music_trailer.asm` | `CF:61DD..CF:61E7` | 10 | 0 | 10 | `b71d8fc8273978311382a6eb6af3c8b97944ffd3` |
| `build-candidate` | `src/cf/table_sprite_placement_pointer_table.asm` | `CF:61E7..CF:6BE7` | 2560 | 0 | 2560 | `8c92631ca7288709ee5b3940025d5e504cb7e2df` |
| `build-candidate` | `src/cf/table_sprite_placement_table.asm` | `CF:6BE7..CF:8985` | 7582 | 0 | 7582 | `f00f6788a6440deb34f7ba6c4d528f8df120dd52` |
| `build-candidate` | `src/cf/table_npc_config_table.asm` | `CF:8985..CF:F2B5` | 26928 | 0 | 26928 | `ad26b2e5cde28ccee528ae81978f7c46dedb6e1a` |
| `build-candidate` | `src/cf/asset_audio_pack_94.asm` | `CF:F2B5..CF:FF38` | 3203 | 0 | 3203 | `b624f1f05e30efc3f6588b9076291f87ef0e618c` |
| `build-candidate` | `src/cf/asset_audio_pack_96.asm` | `CF:FF38..CF:FFF9` | 193 | 0 | 193 | `757fc75c398c7340fd6ea8f811001b181337f2c4` |
| `build-candidate` | `src/cf/padding_cf_tail_slack.asm` | `CF:FFF9..CF:10000` | 7 | 0 | 7 | `77ce0377defbd11b77b1f4ad54ca40ea5ef28490` |

## Source Segments

### `src/cf/table_door_data.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `CF:0000..CF:264F` (`9807` bytes, SHA-1 `d1148a10239fdfad56593366e5fe18be707d719a`) `DoorData`

Labels:

- `CF:0000 DoorData`

Evidence:

- `build/cf-table-splits.json`
- `notes/cf-table-splits.md`

### `src/cf/table_door_config_table.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `CF:264F..CF:58EF` (`12960` bytes, SHA-1 `b18e72efdccb51e290c8261b757638b9885456a9`) `DoorConfigTable`

Labels:

- `CF:264F DoorConfigTable`

Evidence:

- `build/cf-table-splits.json`
- `notes/cf-table-splits.md`

### `src/cf/table_overworld_event_music_pointer_table.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `CF:58EF..CF:5A39` (`330` bytes, SHA-1 `76d96bef963a70bc9923fd2b6acd8e979381430d`) `OverworldEventMusicPointerTable`

Labels:

- `CF:58EF OverworldEventMusicPointerTable`

Evidence:

- `build/cf-table-splits.json`
- `notes/cf-table-splits.md`

### `src/cf/table_overworld_event_music_table.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `CF:5A39..CF:61DD` (`1956` bytes, SHA-1 `69fb88a79649e5f81be910222d7670c9d6592d23`) `OverworldEventMusicTable`

Labels:

- `CF:5A39 OverworldEventMusicTable`

Evidence:

- `build/cf-table-splits.json`
- `notes/cf-table-splits.md`

### `src/cf/table_cf_inline_event_music_trailer.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `CF:61DD..CF:61E7` (`10` bytes, SHA-1 `b71d8fc8273978311382a6eb6af3c8b97944ffd3`) `CfInlineEventMusicTrailer`

Labels:

- `CF:61DD CfInlineEventMusicTrailer`

Evidence:

- `build/cf-table-splits.json`
- `notes/cf-table-splits.md`

### `src/cf/table_sprite_placement_pointer_table.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `CF:61E7..CF:6BE7` (`2560` bytes, SHA-1 `8c92631ca7288709ee5b3940025d5e504cb7e2df`) `SpritePlacementPointerTable`

Labels:

- `CF:61E7 SpritePlacementPointerTable`

Evidence:

- `build/cf-table-splits.json`
- `notes/cf-table-splits.md`

### `src/cf/table_sprite_placement_table.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `CF:6BE7..CF:8985` (`7582` bytes, SHA-1 `f00f6788a6440deb34f7ba6c4d528f8df120dd52`) `SpritePlacementTable`

Labels:

- `CF:6BE7 SpritePlacementTable`

Evidence:

- `build/cf-table-splits.json`
- `notes/cf-table-splits.md`

### `src/cf/table_npc_config_table.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `CF:8985..CF:F2B5` (`26928` bytes, SHA-1 `ad26b2e5cde28ccee528ae81978f7c46dedb6e1a`) `NpcConfigTable`

Labels:

- `CF:8985 NpcConfigTable`

Evidence:

- `build/cf-table-splits.json`
- `notes/cf-table-splits.md`

### `src/cf/asset_audio_pack_94.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `CF:F2B5..CF:FF38` (`3203` bytes, SHA-1 `b624f1f05e30efc3f6588b9076291f87ef0e618c`) `AudioPack94`

Labels:

- `CF:F2B5 AudioPack94`

Evidence:

- `build/cf-table-splits.json`
- `notes/cf-table-splits.md`

### `src/cf/asset_audio_pack_96.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `CF:FF38..CF:FFF9` (`193` bytes, SHA-1 `757fc75c398c7340fd6ea8f811001b181337f2c4`) `AudioPack96`

Labels:

- `CF:FF38 AudioPack96`

Evidence:

- `build/cf-table-splits.json`
- `notes/cf-table-splits.md`

### `src/cf/padding_cf_tail_slack.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `CF:FFF9..CF:10000` (`7` bytes, SHA-1 `77ce0377defbd11b77b1f4ad54ca40ea5ef28490`) `CfTailSlack`

Labels:

- `CF:FFF9 CfTailSlack`

Evidence:

- `build/cf-table-splits.json`
- `notes/cf-table-splits.md`

## Notes

The scaffold preserves intentional source-adjacent data gaps from the manifest and validates each protected span against the original ROM bytes.
