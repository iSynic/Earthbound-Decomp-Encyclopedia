# Audio Sequence Control-Flow Frontier

Status: static control-flow operand shapes known; SPC700 driver dispatch still needs naming.

## Summary

- sequence packs with control candidates: `102`
- control commands inspected: `['0xEF', '0xFD', '0xFE', '0xFF']`
- total control candidates: `2281`
- semantic status: `control_flow_operand_shapes_known_driver_dispatch_pending`

## Command Summaries

| Command | Count | Current hypothesis | Next-word pointers | Tail occurrences | Remaining-byte shapes |
| --- | ---: | --- | ---: | ---: | --- |
| `0xEF` | 2057 | subroutine_call_candidate | 2045 (0.9942) | 0 (0.0) | `[{'remaining': '3', 'count': 219}, {'remaining': '4', 'count': 82}, {'remaining': '5', 'count': 58}, {'remaining': '7', 'count': 56}, {'remaining': '11', 'count': 50}]` |
| `0xFD` | 19 | loop_or_jump_control_candidate | 1 (0.0526) | 0 (0.0) | `[{'remaining': '33', 'count': 1}, {'remaining': '7', 'count': 1}, {'remaining': '2', 'count': 1}, {'remaining': '19', 'count': 1}, {'remaining': '107', 'count': 1}]` |
| `0xFE` | 49 | jump_or_long_control_candidate | 0 (0.0) | 0 (0.0) | `[{'remaining': '29', 'count': 2}, {'remaining': '35', 'count': 2}, {'remaining': '656', 'count': 1}, {'remaining': '16', 'count': 1}, {'remaining': '34', 'count': 1}]` |
| `0xFF` | 156 | end_or_sentinel_candidate | 2 (0.0128) | 0 (0.0) | `[{'remaining': '11', 'count': 8}, {'remaining': '10', 'count': 5}, {'remaining': '35', 'count': 5}, {'remaining': '12', 'count': 5}, {'remaining': '3', 'count': 3}]` |

## Priority Packs

| Pack | ROM range | Tracks | Control counts | Pointer-shaped operands |
| ---: | --- | ---: | --- | --- |
| `25` | `EC:E101..EC:EB51` | 8 | `{'0xEF': 43, '0xFD': 1, '0xFE': 16, '0xFF': 8}` | `{'0xEF': 43}` |
| `133` | `EC:B38A..EC:BF28` | 4 | `{'0xEF': 21, '0xFF': 1}` | `{'0xEF': 21}` |
| `4` | `DF:EC46..DF:FFEE` | 3 | `{'0xEF': 105, '0xFF': 3}` | `{'0xEF': 103}` |
| `132` | `ED:1406..ED:1DFF` | 3 | `{'0xEF': 31, '0xFE': 2, '0xFF': 1}` | `{'0xEF': 31}` |
| `79` | `DC:F8BF..DC:FF92` | 3 | `{'0xEF': 17, '0xFE': 3}` | `{'0xEF': 17}` |
| `103` | `EE:52E6..EE:56DF` | 3 | `{'0xEF': 2, '0xFF': 2}` | `{'0xEF': 2}` |
| `94` | `CF:F2B5..CF:FF38` | 4 | `{'0xEF': 41, '0xFD': 3, '0xFF': 20}` | `{'0xEF': 41}` |
| `97` | `EC:BF28..EC:CAA1` | 2 | `{'0xEF': 42, '0xFF': 2}` | `{'0xEF': 42}` |
| `102` | `CE:F8C6..CE:FFAA` | 2 | `{'0xEF': 31, '0xFF': 2}` | `{'0xEF': 31}` |
| `115` | `EE:0FB2..EE:14D4` | 2 | `{'0xEF': 24, '0xFF': 6}` | `{'0xEF': 24}` |
| `150` | `ED:53DF..ED:5C01` | 2 | `{'0xEF': 27, '0xFD': 1}` | `{'0xEF': 27}` |
| `149` | `E9:F8C8..E9:FF65` | 3 | `{'0xEF': 20, '0xFF': 1}` | `{'0xEF': 20}` |
| `55` | `EC:CAA1..EC:D5D8` | 2 | `{'0xEF': 21}` | `{'0xEF': 21}` |
| `136` | `EE:0000..EE:0554` | 2 | `{'0xEF': 12, '0xFD': 2, '0xFE': 4, '0xFF': 2}` | `{'0xEF': 12}` |
| `1` | `E6:0000..E6:45D8` | 2 | `{'0xEF': 15, '0xFD': 1, '0xFF': 3}` | `{'0xEF': 14}` |
| `38` | `ED:6409..ED:6C06` | 2 | `{'0xEF': 19}` | `{'0xEF': 19}` |
| `87` | `ED:0A07..ED:1406` | 2 | `{'0xEF': 19}` | `{'0xEF': 19}` |
| `162` | `ED:A4D7..ED:AB12` | 2 | `{'0xEF': 14, '0xFD': 2, '0xFF': 1}` | `{'0xEF': 14}` |
| `19` | `ED:CF55..ED:D539` | 2 | `{'0xEF': 15}` | `{'0xEF': 15}` |
| `23` | `EE:3E9C..EE:42BB` | 2 | `{'0xEF': 15}` | `{'0xEF': 15}` |

## Findings

- EF/FD/FE/FF occurrences are now isolated from pointer-table bytes and grouped by likely sequence segment.
- The next-word pointer ratio is the main static evidence for call/jump-like commands before SPC700 driver dispatch is named.
- FF tail ratio separates likely end sentinels from FF bytes that appear as operands or data inside longer phrases.
- This frontier stores offsets, counts, hashes, and operand-shape evidence only; it does not embed song payload byte strings.

## Next Work

- tie the static EF/FD/FE/FF operand shapes to the SPC700 driver's command dispatch table
- promote commands with pointer-shaped operands into a checked sequence-walker used by exact-duration export planning
- feed high-confidence end and jump behavior back into audio-export-plan exact finite/loop classifications
