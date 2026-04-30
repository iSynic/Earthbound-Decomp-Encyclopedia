# Audio Sequence Semantics Frontier

Status: first-pass sequence-pack frontier inventory; payload-level opcode decoding is the next active work.

EarthBound's music sequence data is loaded by `CHANGE_MUSIC` as the third pack role, after primary and secondary sample packs. The current audio renderer can play/export all snapshot-backed tracks, but exact endings and loop points still need sequence bytecode semantics.

## Summary

- music tracks represented: `192`
- unique sequence packs used by tracks: `119`
- sequence payload blocks inventoried: `170`
- destination counts: `{'0x4800': 59, '0x5000': 6, '0x6000': 7, '0x5800': 60, '0x5C00': 4, '0x6400': 2, '0x5200': 8, '0x4A00': 1, '0x4C00': 2, '0x4E00': 1, '0x5400': 3, '0x5600': 1, '0x6200': 3, '0x4B00': 1, '0x5300': 1, '0x4F80': 1, '0x5100': 1, '0x6700': 1, '0x4900': 1, '0x4AE0': 1, '0x4CC0': 1, '0x4EA0': 1, '0x5080': 1, '0x5260': 1, '0x5440': 1, '0x5620': 1}`
- export-pressure classes: `{'unknown_active_preview': 79, 'finite_or_transition_review_candidate': 22, 'loop_or_held_candidate': 58, 'finite_trim_candidate': 16}`
- observed high-command candidates: `{'0xE0': 2354, '0xE1': 5925, '0xE2': 925, '0xE3': 998, '0xE4': 242, '0xE5': 208, '0xE6': 121, '0xE7': 322, '0xE8': 57, '0xE9': 8, '0xEA': 133, '0xEB': 108, '0xEC': 54, '0xED': 2769, '0xEE': 755, '0xEF': 2058, '0xF0': 284, '0xF1': 711, '0xF2': 450, '0xF3': 496, '0xF4': 1379, '0xF5': 243, '0xF6': 20, '0xF7': 281, '0xF8': 35, '0xF9': 344, '0xFA': 328, '0xFB': 34, '0xFC': 45, '0xFD': 19, '0xFE': 49, '0xFF': 156}`
- opcode status: `payload_histograms_built_command_meanings_still_hypotheses`

## Current Boundary

- This frontier is contract-backed and safe to check in.
- It does not embed ROM-derived sequence payload bytes; it stores structural statistics, pointer candidates, hashes, and command histograms.
- It separates track/export pressure from opcode semantics so exact-duration work can focus on the tracks that still need it.

## First-Pass Command Hypotheses

These names are hypotheses to guide driver work, not final source names. They are intentionally marked as candidates until tied to SPC700 dispatch evidence.

| Byte | Candidate meaning | Confidence |
| --- | --- | --- |
| `0xE0` | set_instrument_candidate | medium |
| `0xE1` | set_pan_candidate | medium |
| `0xE2` | pan_fade_candidate | low |
| `0xE3` | vibrato_on_candidate | low |
| `0xE4` | vibrato_off_candidate | low |
| `0xE5` | master_volume_or_channel_state_candidate | low |
| `0xE6` | volume_or_master_fade_candidate | low |
| `0xE7` | tempo_or_tuning_candidate | low |
| `0xE8` | tempo_fade_candidate | low |
| `0xE9` | global_transpose_candidate | low |
| `0xEA` | channel_transpose_candidate | low |
| `0xEB` | tremolo_or_modulation_on_candidate | low |
| `0xEC` | tremolo_or_modulation_off_candidate | low |
| `0xED` | set_channel_volume_candidate | medium |
| `0xEE` | channel_volume_fade_candidate | low |
| `0xEF` | subroutine_call_candidate | medium |
| `0xF0` | modulation_fade_candidate | low |
| `0xF1` | pitch_envelope_or_portamento_candidate | low |
| `0xF2` | pitch_envelope_off_candidate | low |
| `0xF3` | tuning_or_detune_candidate | low |
| `0xF4` | driver_toggle_or_extended_control_candidate | low |
| `0xF5` | echo_or_voice_param_candidate | low |
| `0xF6` | echo_off_or_effect_disable_candidate | low |
| `0xF7` | echo_or_effect_setup_candidate | low |
| `0xF8` | echo_or_effect_fade_candidate | low |
| `0xF9` | pitch_slide_candidate | low |
| `0xFA` | earthbound_extended_command_candidate | medium |
| `0xFB` | loop_start_or_control_candidate | low |
| `0xFC` | loop_end_or_control_candidate | low |
| `0xFD` | loop_or_jump_control_candidate | low |
| `0xFE` | jump_or_long_control_candidate | low |
| `0xFF` | end_or_sentinel_candidate | medium |

## Command Contexts

Top next-byte profiles are statistical evidence for operand widths and control-flow commands. They still need SPC700 driver-dispatch corroboration before promotion to final names.

| Byte | Count | Candidate meaning | Top following bytes |
| --- | ---: | --- | --- |
| `0xE0` | 2354 | set_instrument_candidate | `[{'byte': '0xCB', 'count': 254}, {'byte': '0x08', 'count': 245}, {'byte': '0xCE', 'count': 172}, {'byte': '0xCD', 'count': 167}, {'byte': '0xD0', 'count': 128}, {'byte': '0x09', 'count': 126}]` |
| `0xE1` | 5925 | set_pan_candidate | `[{'byte': '0x0A', 'count': 929}, {'byte': '0x05', 'count': 641}, {'byte': '0x12', 'count': 578}, {'byte': '0x0F', 'count': 562}, {'byte': '0x08', 'count': 463}, {'byte': '0x02', 'count': 431}]` |
| `0xE2` | 925 | pan_fade_candidate | `[{'byte': '0x60', 'count': 483}, {'byte': '0x5A', 'count': 163}, {'byte': '0xB4', 'count': 73}, {'byte': '0x28', 'count': 72}, {'byte': '0x30', 'count': 60}, {'byte': '0x48', 'count': 15}]` |
| `0xE3` | 998 | vibrato_on_candidate | `[{'byte': '0x00', 'count': 269}, {'byte': '0x01', 'count': 119}, {'byte': '0x02', 'count': 108}, {'byte': '0x03', 'count': 58}, {'byte': '0x0C', 'count': 51}, {'byte': '0x14', 'count': 45}]` |
| `0xE4` | 242 | vibrato_off_candidate | `[{'byte': '0xF3', 'count': 38}, {'byte': '0x18', 'count': 32}, {'byte': '0xEF', 'count': 30}, {'byte': '0xE1', 'count': 26}, {'byte': '0xF4', 'count': 19}, {'byte': '0x0C', 'count': 12}]` |
| `0xE5` | 208 | master_volume_or_channel_state_candidate | `[{'byte': '0xF0', 'count': 176}, {'byte': '0x96', 'count': 4}, {'byte': '0xB4', 'count': 3}, {'byte': '0x78', 'count': 3}, {'byte': '0xE6', 'count': 2}, {'byte': '0x5D', 'count': 2}]` |
| `0xE6` | 121 | volume_or_master_fade_candidate | `[{'byte': '0xB4', 'count': 14}, {'byte': '0x5A', 'count': 12}, {'byte': '0xE1', 'count': 10}, {'byte': '0xF4', 'count': 8}, {'byte': '0x01', 'count': 8}, {'byte': '0x0C', 'count': 8}]` |
| `0xE7` | 322 | tempo_or_tuning_candidate | `[{'byte': '0x0E', 'count': 38}, {'byte': '0x10', 'count': 29}, {'byte': '0x15', 'count': 28}, {'byte': '0x19', 'count': 20}, {'byte': '0x14', 'count': 17}, {'byte': '0x1B', 'count': 16}]` |
| `0xE8` | 57 | tempo_fade_candidate | `[{'byte': '0x60', 'count': 8}, {'byte': '0x0C', 'count': 7}, {'byte': '0x18', 'count': 6}, {'byte': '0xE2', 'count': 5}, {'byte': '0x5B', 'count': 4}, {'byte': '0xE1', 'count': 3}]` |
| `0xE9` | 8 | global_transpose_candidate | `[{'byte': '0x60', 'count': 2}, {'byte': '0x49', 'count': 2}, {'byte': '0x4C', 'count': 2}, {'byte': '0x5B', 'count': 2}]` |
| `0xEA` | 133 | channel_transpose_candidate | `[{'byte': '0xFF', 'count': 43}, {'byte': '0x00', 'count': 36}, {'byte': '0xFC', 'count': 21}, {'byte': '0xFA', 'count': 8}, {'byte': '0x50', 'count': 4}, {'byte': '0x0E', 'count': 3}]` |
| `0xEB` | 108 | tremolo_or_modulation_on_candidate | `[{'byte': '0x00', 'count': 71}, {'byte': '0x06', 'count': 8}, {'byte': '0x0A', 'count': 5}, {'byte': '0x01', 'count': 4}, {'byte': '0x4A', 'count': 3}, {'byte': '0x49', 'count': 2}]` |
| `0xEC` | 54 | tremolo_or_modulation_off_candidate | `[{'byte': '0xF4', 'count': 17}, {'byte': '0x08', 'count': 8}, {'byte': '0x02', 'count': 4}, {'byte': '0x03', 'count': 4}, {'byte': '0x04', 'count': 4}, {'byte': '0x60', 'count': 3}]` |
| `0xED` | 2769 | set_channel_volume_candidate | `[{'byte': '0x64', 'count': 202}, {'byte': '0x78', 'count': 196}, {'byte': '0x5A', 'count': 190}, {'byte': '0x50', 'count': 182}, {'byte': '0x3C', 'count': 178}, {'byte': '0x82', 'count': 176}]` |
| `0xEE` | 755 | channel_volume_fade_candidate | `[{'byte': '0x5A', 'count': 122}, {'byte': '0xB4', 'count': 83}, {'byte': '0x60', 'count': 68}, {'byte': '0xC8', 'count': 55}, {'byte': '0xFA', 'count': 52}, {'byte': '0x50', 'count': 32}]` |
| `0xEF` | 2058 | subroutine_call_candidate | `[{'byte': '0x4F', 'count': 22}, {'byte': '0x52', 'count': 20}, {'byte': '0x00', 'count': 19}, {'byte': '0x66', 'count': 19}, {'byte': '0x20', 'count': 18}, {'byte': '0x2A', 'count': 17}]` |
| `0xF0` | 284 | modulation_fade_candidate | `[{'byte': '0xE7', 'count': 82}, {'byte': '0xED', 'count': 68}, {'byte': '0xE1', 'count': 16}, {'byte': '0xF5', 'count': 13}, {'byte': '0xE0', 'count': 13}, {'byte': '0x01', 'count': 9}]` |
| `0xF1` | 711 | pitch_envelope_or_portamento_candidate | `[{'byte': '0x00', 'count': 348}, {'byte': '0x01', 'count': 216}, {'byte': '0x0C', 'count': 31}, {'byte': '0x06', 'count': 17}, {'byte': '0x03', 'count': 14}, {'byte': '0x02', 'count': 12}]` |
| `0xF2` | 450 | pitch_envelope_off_candidate | `[{'byte': '0x00', 'count': 224}, {'byte': '0x01', 'count': 218}, {'byte': '0x0C', 'count': 2}, {'byte': '0x4E', 'count': 2}, {'byte': '0x68', 'count': 2}, {'byte': '0x4A', 'count': 1}]` |
| `0xF3` | 496 | tuning_or_detune_candidate | `[{'byte': '0x0C', 'count': 99}, {'byte': '0xE4', 'count': 55}, {'byte': '0xE1', 'count': 36}, {'byte': '0x18', 'count': 32}, {'byte': '0x06', 'count': 31}, {'byte': '0xEF', 'count': 31}]` |
| `0xF4` | 1379 | driver_toggle_or_extended_control_candidate | `[{'byte': '0x0A', 'count': 411}, {'byte': '0x00', 'count': 285}, {'byte': '0x05', 'count': 101}, {'byte': '0x23', 'count': 74}, {'byte': '0x24', 'count': 65}, {'byte': '0x14', 'count': 62}]` |
| `0xF5` | 243 | echo_or_voice_param_candidate | `[{'byte': '0x7F', 'count': 97}, {'byte': '0xFF', 'count': 27}, {'byte': '0x7E', 'count': 14}, {'byte': '0x03', 'count': 13}, {'byte': '0x70', 'count': 10}, {'byte': '0x78', 'count': 6}]` |
| `0xF6` | 20 | echo_off_or_effect_disable_candidate | `[{'byte': '0x4C', 'count': 4}, {'byte': '0x5A', 'count': 3}, {'byte': '0xE3', 'count': 2}, {'byte': '0x87', 'count': 2}, {'byte': '0x8C', 'count': 2}, {'byte': '0x51', 'count': 2}]` |
| `0xF7` | 281 | echo_or_effect_setup_candidate | `[{'byte': '0x03', 'count': 171}, {'byte': '0x18', 'count': 51}, {'byte': '0x02', 'count': 17}, {'byte': '0x01', 'count': 15}, {'byte': '0x60', 'count': 10}, {'byte': '0x24', 'count': 5}]` |
| `0xF8` | 35 | echo_or_effect_fade_candidate | `[{'byte': '0x24', 'count': 7}, {'byte': '0xE1', 'count': 7}, {'byte': '0x57', 'count': 4}, {'byte': '0x60', 'count': 4}, {'byte': '0x55', 'count': 2}, {'byte': '0x4C', 'count': 2}]` |
| `0xF9` | 344 | pitch_slide_candidate | `[{'byte': '0x00', 'count': 314}, {'byte': '0x30', 'count': 8}, {'byte': '0x0C', 'count': 7}, {'byte': '0x18', 'count': 3}, {'byte': '0x10', 'count': 2}, {'byte': '0xC8', 'count': 2}]` |
| `0xFA` | 328 | earthbound_extended_command_candidate | `[{'byte': '0x1A', 'count': 163}, {'byte': '0xF4', 'count': 13}, {'byte': '0x60', 'count': 12}, {'byte': '0x5A', 'count': 11}, {'byte': '0x46', 'count': 11}, {'byte': '0xF1', 'count': 9}]` |
| `0xFB` | 34 | loop_start_or_control_candidate | `[{'byte': '0x0C', 'count': 9}, {'byte': '0x01', 'count': 4}, {'byte': '0x60', 'count': 3}, {'byte': '0x51', 'count': 3}, {'byte': '0x58', 'count': 2}, {'byte': '0x8E', 'count': 2}]` |
| `0xFC` | 45 | loop_end_or_control_candidate | `[{'byte': '0xF3', 'count': 12}, {'byte': '0x0C', 'count': 5}, {'byte': '0x18', 'count': 4}, {'byte': '0xEF', 'count': 4}, {'byte': '0x30', 'count': 4}, {'byte': '0x60', 'count': 2}]` |
| `0xFD` | 19 | loop_or_jump_control_candidate | `[{'byte': '0x18', 'count': 4}, {'byte': '0x0C', 'count': 3}, {'byte': '0x60', 'count': 2}, {'byte': '0x32', 'count': 2}, {'byte': '0x30', 'count': 1}, {'byte': '0x56', 'count': 1}]` |
| `0xFE` | 49 | jump_or_long_control_candidate | `[{'byte': '0x60', 'count': 11}, {'byte': '0x08', 'count': 9}, {'byte': '0x18', 'count': 5}, {'byte': '0x59', 'count': 4}, {'byte': '0xC8', 'count': 3}, {'byte': '0x5A', 'count': 2}]` |
| `0xFF` | 156 | end_or_sentinel_candidate | `[{'byte': '0xF4', 'count': 43}, {'byte': '0xEE', 'count': 21}, {'byte': '0x32', 'count': 9}, {'byte': '0x60', 'count': 9}, {'byte': '0x18', 'count': 9}, {'byte': '0x0C', 'count': 7}]` |

## Exact-Duration Priority Packs

These packs have the most tracks still needing sequence semantics for exact export behavior.

| Pack | ROM range | Needs semantics | Tracks | Export classes | Block shapes |
| ---: | --- | ---: | ---: | --- | --- |
| `25` | `EC:E101..EC:EB51` | 8 | 8 | `{'finite_or_transition_review_candidate': 8}` | `[{'destination': '0x4800', 'bytes': 325, 'pointer_prefix_words': 19, 'scan_bytes': 287}, {'destination': '0x4A00', 'bytes': 327, 'pointer_prefix_words': 19, 'scan_bytes': 289}, {'destination': '0x4C00', 'bytes': 343, 'pointer_prefix_words': 19, 'scan_bytes': 305}, {'destination': '0x4E00', 'bytes': 335, 'pointer_prefix_words': 19, 'scan_bytes': 297}, {'destination': '0x5000', 'bytes': 320, 'pointer_prefix_words': 19, 'scan_bytes': 282}, {'destination': '0x5200', 'bytes': 339, 'pointer_prefix_words': 19, 'scan_bytes': 301}, {'destination': '0x5400', 'bytes': 337, 'pointer_prefix_words': 19, 'scan_bytes': 299}, {'destination': '0x5600', 'bytes': 280, 'pointer_prefix_words': 19, 'scan_bytes': 242}]` |
| `133` | `EC:B38A..EC:BF28` | 4 | 4 | `{'loop_or_held_candidate': 2, 'unknown_active_preview': 1, 'finite_or_transition_review_candidate': 1}` | `[{'destination': '0x5800', 'bytes': 702, 'pointer_prefix_words': 12, 'scan_bytes': 678}, {'destination': '0x5C00', 'bytes': 438, 'pointer_prefix_words': 12, 'scan_bytes': 414}, {'destination': '0x6000', 'bytes': 1293, 'pointer_prefix_words': 39, 'scan_bytes': 1215}, {'destination': '0x6700', 'bytes': 523, 'pointer_prefix_words': 10, 'scan_bytes': 503}]` |
| `103` | `EE:52E6..EE:56DF` | 3 | 3 | `{'finite_or_transition_review_candidate': 3}` | `[{'destination': '0x4800', 'bytes': 422, 'pointer_prefix_words': 21, 'scan_bytes': 380}, {'destination': '0x4C00', 'bytes': 251, 'pointer_prefix_words': 21, 'scan_bytes': 209}, {'destination': '0x5200', 'bytes': 330, 'pointer_prefix_words': 21, 'scan_bytes': 288}]` |
| `4` | `DF:EC46..DF:FFEE` | 3 | 3 | `{'unknown_active_preview': 2, 'finite_or_transition_review_candidate': 1}` | `[{'destination': '0x4800', 'bytes': 1314, 'pointer_prefix_words': 39, 'scan_bytes': 1236}, {'destination': '0x5000', 'bytes': 3355, 'pointer_prefix_words': 76, 'scan_bytes': 3203}, {'destination': '0x6000', 'bytes': 349, 'pointer_prefix_words': 10, 'scan_bytes': 329}]` |
| `83` | `EE:6D36..EE:6FDD` | 3 | 3 | `{'loop_or_held_candidate': 3}` | `[{'destination': '0x4800', 'bytes': 247, 'pointer_prefix_words': 21, 'scan_bytes': 205}, {'destination': '0x5200', 'bytes': 111, 'pointer_prefix_words': 21, 'scan_bytes': 69}, {'destination': '0x5300', 'bytes': 307, 'pointer_prefix_words': 21, 'scan_bytes': 265}]` |
| `132` | `ED:1406..ED:1DFF` | 3 | 3 | `{'loop_or_held_candidate': 3}` | `[{'destination': '0x5800', 'bytes': 745, 'pointer_prefix_words': 30, 'scan_bytes': 685}, {'destination': '0x5C00', 'bytes': 1313, 'pointer_prefix_words': 49, 'scan_bytes': 1215}, {'destination': '0x6200', 'bytes': 481, 'pointer_prefix_words': 21, 'scan_bytes': 439}]` |
| `79` | `DC:F8BF..DC:FF92` | 3 | 3 | `{'loop_or_held_candidate': 2, 'unknown_active_preview': 1}` | `[{'destination': '0x4800', 'bytes': 270, 'pointer_prefix_words': 21, 'scan_bytes': 228}, {'destination': '0x4B00', 'bytes': 1034, 'pointer_prefix_words': 2, 'scan_bytes': 1030}, {'destination': '0x5400', 'bytes': 429, 'pointer_prefix_words': 21, 'scan_bytes': 387}]` |
| `157` | `EC:F578..EC:FF94` | 2 | 10 | `{'finite_trim_candidate': 8, 'finite_or_transition_review_candidate': 2}` | `[{'destination': '0x4800', 'bytes': 211, 'pointer_prefix_words': 10, 'scan_bytes': 191}, {'destination': '0x4900', 'bytes': 322, 'pointer_prefix_words': 10, 'scan_bytes': 302}, {'destination': '0x4AE0', 'bytes': 289, 'pointer_prefix_words': 10, 'scan_bytes': 269}, {'destination': '0x4CC0', 'bytes': 296, 'pointer_prefix_words': 10, 'scan_bytes': 276}, {'destination': '0x4EA0', 'bytes': 288, 'pointer_prefix_words': 10, 'scan_bytes': 268}, {'destination': '0x5080', 'bytes': 307, 'pointer_prefix_words': 10, 'scan_bytes': 287}, {'destination': '0x5260', 'bytes': 261, 'pointer_prefix_words': 10, 'scan_bytes': 241}, {'destination': '0x5440', 'bytes': 326, 'pointer_prefix_words': 10, 'scan_bytes': 306}, {'destination': '0x5620', 'bytes': 250, 'pointer_prefix_words': 10, 'scan_bytes': 230}]` |
| `94` | `CF:F2B5..CF:FF38` | 2 | 4 | `{'unknown_active_preview': 1, 'finite_or_transition_review_candidate': 1, 'finite_trim_candidate': 2}` | `[{'destination': '0x4800', 'bytes': 1891, 'pointer_prefix_words': 50, 'scan_bytes': 1791}, {'destination': '0x4F80', 'bytes': 299, 'pointer_prefix_words': 21, 'scan_bytes': 257}, {'destination': '0x5100', 'bytes': 401, 'pointer_prefix_words': 21, 'scan_bytes': 359}, {'destination': '0x5400', 'bytes': 594, 'pointer_prefix_words': 21, 'scan_bytes': 552}]` |
| `1` | `E6:0000..E6:45D8` | 2 | 2 | `{'unknown_active_preview': 1, 'finite_or_transition_review_candidate': 1}` | `[{'destination': '0x4800', 'bytes': 1029, 'pointer_prefix_words': 10, 'scan_bytes': 1009}]` |
| `162` | `ED:A4D7..ED:AB12` | 2 | 2 | `{'unknown_active_preview': 1, 'finite_or_transition_review_candidate': 1}` | `[{'destination': '0x4800', 'bytes': 1172, 'pointer_prefix_words': 47, 'scan_bytes': 1078}, {'destination': '0x5000', 'bytes': 413, 'pointer_prefix_words': 21, 'scan_bytes': 371}]` |
| `149` | `E9:F8C8..E9:FF65` | 2 | 3 | `{'finite_trim_candidate': 1, 'loop_or_held_candidate': 2}` | `[{'destination': '0x5800', 'bytes': 446, 'pointer_prefix_words': 21, 'scan_bytes': 404}, {'destination': '0x5C00', 'bytes': 820, 'pointer_prefix_words': 30, 'scan_bytes': 760}, {'destination': '0x6200', 'bytes': 413, 'pointer_prefix_words': 21, 'scan_bytes': 371}]` |
| `23` | `EE:3E9C..EE:42BB` | 2 | 2 | `{'loop_or_held_candidate': 2}` | `[{'destination': '0x5800', 'bytes': 352, 'pointer_prefix_words': 22, 'scan_bytes': 308}, {'destination': '0x6000', 'bytes': 693, 'pointer_prefix_words': 21, 'scan_bytes': 651}]` |
| `34` | `ED:27F7..ED:3195` | 2 | 2 | `{'loop_or_held_candidate': 2}` | `[{'destination': '0x5800', 'bytes': 2456, 'pointer_prefix_words': 59, 'scan_bytes': 2338}]` |
| `38` | `ED:6409..ED:6C06` | 2 | 2 | `{'loop_or_held_candidate': 2}` | `[{'destination': '0x5800', 'bytes': 1227, 'pointer_prefix_words': 39, 'scan_bytes': 1149}, {'destination': '0x6200', 'bytes': 808, 'pointer_prefix_words': 21, 'scan_bytes': 766}]` |
| `81` | `EE:7E29..EE:804D` | 2 | 2 | `{'loop_or_held_candidate': 2}` | `[{'destination': '0x4800', 'bytes': 269, 'pointer_prefix_words': 21, 'scan_bytes': 227}, {'destination': '0x5200', 'bytes': 269, 'pointer_prefix_words': 21, 'scan_bytes': 227}]` |
| `87` | `ED:0A07..ED:1406` | 2 | 2 | `{'loop_or_held_candidate': 2}` | `[{'destination': '0x4800', 'bytes': 1649, 'pointer_prefix_words': 77, 'scan_bytes': 1495}, {'destination': '0x5000', 'bytes': 900, 'pointer_prefix_words': 32, 'scan_bytes': 836}]` |
| `115` | `EE:0FB2..EE:14D4` | 2 | 2 | `{'loop_or_held_candidate': 2}` | `[{'destination': '0x4800', 'bytes': 1308, 'pointer_prefix_words': 47, 'scan_bytes': 1214}]` |
| `145` | `EA:FE8B..EA:FFE2` | 2 | 2 | `{'loop_or_held_candidate': 2}` | `[{'destination': '0x4800', 'bytes': 337, 'pointer_prefix_words': 12, 'scan_bytes': 313}]` |
| `150` | `ED:53DF..ED:5C01` | 2 | 2 | `{'loop_or_held_candidate': 2}` | `[{'destination': '0x4800', 'bytes': 1550, 'pointer_prefix_words': 58, 'scan_bytes': 1434}, {'destination': '0x5000', 'bytes': 522, 'pointer_prefix_words': 21, 'scan_bytes': 480}]` |

## Focused Pack Reports

| Pack | Status | Manifest | Claim |
| ---: | --- | --- | --- |
| `25` | structure_known_opcode_dispatch_pending | `manifests/audio-sequence-pack-025-semantics.json` | Sanctuary melody family tracks 32..39 map to eight sequence blocks with a stable 3-word top-level table, two pointer groups, and repeated channel/phrase segment shapes. |

## Sequence Packs

First 40 sequence packs by id:

| Pack | ROM range | Track count | Export classes |
| ---: | --- | ---: | --- |
| `1` | `E6:0000..E6:45D8` | 2 | `{'unknown_active_preview': 1, 'finite_or_transition_review_candidate': 1}` |
| `4` | `DF:EC46..DF:FFEE` | 3 | `{'unknown_active_preview': 2, 'finite_or_transition_review_candidate': 1}` |
| `6` | `E0:FCE1..E0:FFB3` | 1 | `{'loop_or_held_candidate': 1}` |
| `7` | `E8:FF1B..E8:FFED` | 1 | `{'finite_trim_candidate': 1}` |
| `9` | `EE:894F..EE:8ACA` | 1 | `{'unknown_active_preview': 1}` |
| `10` | `ED:BD60..ED:C36C` | 4 | `{'unknown_active_preview': 1, 'finite_trim_candidate': 3}` |
| `11` | `EE:42BB..EE:46CE` | 1 | `{'unknown_active_preview': 1}` |
| `12` | `EE:67B7..EE:6A85` | 1 | `{'unknown_active_preview': 1}` |
| `13` | `EB:FE22..EB:FFFF` | 1 | `{'unknown_active_preview': 1}` |
| `14` | `ED:DAFD..ED:E0AE` | 3 | `{'unknown_active_preview': 2, 'finite_trim_candidate': 1}` |
| `15` | `EC:EB51..EC:F578` | 1 | `{'unknown_active_preview': 1}` |
| `16` | `EE:365D..EE:3A7D` | 1 | `{'unknown_active_preview': 1}` |
| `17` | `EE:798E..EE:7BDF` | 1 | `{'unknown_active_preview': 1}` |
| `18` | `E2:FC88..E2:FFFD` | 1 | `{'unknown_active_preview': 1}` |
| `19` | `ED:CF55..ED:D539` | 2 | `{'unknown_active_preview': 2}` |
| `20` | `EE:1EFE..EE:2401` | 1 | `{'unknown_active_preview': 1}` |
| `22` | `EE:7737..EE:798E` | 1 | `{'loop_or_held_candidate': 1}` |
| `23` | `EE:3E9C..EE:42BB` | 2 | `{'loop_or_held_candidate': 2}` |
| `25` | `EC:E101..EC:EB51` | 8 | `{'finite_or_transition_review_candidate': 8}` |
| `26` | `ED:9824..ED:9E93` | 1 | `{'unknown_active_preview': 1}` |
| `28` | `ED:B753..ED:BD60` | 2 | `{'unknown_active_preview': 2}` |
| `29` | `ED:FC9C..ED:FFFE` | 1 | `{'unknown_active_preview': 1}` |
| `30` | `ED:E65C..ED:EBF4` | 1 | `{'unknown_active_preview': 1}` |
| `31` | `EE:7274..EE:74D7` | 1 | `{'unknown_active_preview': 1}` |
| `32` | `E3:FDCC..E3:FFF2` | 1 | `{'unknown_active_preview': 1}` |
| `34` | `ED:27F7..ED:3195` | 2 | `{'loop_or_held_candidate': 2}` |
| `36` | `E2:ED2C..E2:FC88` | 1 | `{'loop_or_held_candidate': 1}` |
| `38` | `ED:6409..ED:6C06` | 2 | `{'loop_or_held_candidate': 2}` |
| `39` | `ED:4BA7..ED:53DF` | 1 | `{'unknown_active_preview': 1}` |
| `41` | `EE:90FF..EE:9201` | 1 | `{'loop_or_held_candidate': 1}` |
| `43` | `ED:9E93..ED:A4D7` | 1 | `{'unknown_active_preview': 1}` |
| `45` | `D9:FC18..D9:FFE1` | 1 | `{'unknown_active_preview': 1}` |
| `46` | `E8:F872..E8:FF1B` | 1 | `{'unknown_active_preview': 1}` |
| `48` | `ED:436B..ED:4BA7` | 1 | `{'loop_or_held_candidate': 1}` |
| `49` | `EE:87CB..EE:894F` | 1 | `{'unknown_active_preview': 1}` |
| `51` | `EE:56DF..EE:5A99` | 1 | `{'loop_or_held_candidate': 1}` |
| `53` | `EE:14D4..EE:19EE` | 1 | `{'unknown_active_preview': 1}` |
| `55` | `EC:CAA1..EC:D5D8` | 2 | `{'loop_or_held_candidate': 1, 'unknown_active_preview': 1}` |
| `57` | `ED:D539..ED:DAFD` | 1 | `{'loop_or_held_candidate': 1}` |
| `59` | `CB:FEE2..CB:FFE4` | 1 | `{'unknown_active_preview': 1}` |

## Next Work

- identify the sequence entry table shape that maps the APU track command to channel/subsequence pointers
- map high-byte command candidates to the SPC700 driver dispatch paths
- use command semantics to promote exact finite endings and loop/fade export policy
