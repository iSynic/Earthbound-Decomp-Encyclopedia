# Audio Sequence Walk Frontier

Status: provisional static walk built; EF edges are explicit, FD/FE/FF still need driver corroboration before exact duration promotion.

## Summary

- sequence packs walked: `119`
- walk statuses: `{'blocked': 51, 'falls_through_segment': 2568, 'terminates': 158}`
- EF call edges: `2007`
- EF edges outside block: `15` (`0.0075`)
- FF terminator candidates reached: `159`
- blocker counts: `{'0xFD': 8, '0xFE': 34}`
- semantic status: `provisional_static_walk_ef_edges_known_fd_fe_blockers_unpromoted`

## Commands Seen By Walker

| Command | Count | Current hypothesis |
| --- | ---: | --- |
| `0xE0` | 2335 | set_instrument_candidate |
| `0xE1` | 5785 | set_pan_candidate |
| `0xE2` | 921 | pan_fade_candidate |
| `0xE3` | 993 | vibrato_on_candidate |
| `0xE4` | 189 | vibrato_off_candidate |
| `0xE5` | 85 | master_volume_or_channel_state_candidate |
| `0xE6` | 57 | volume_or_master_fade_candidate |
| `0xE7` | 221 | tempo_or_tuning_candidate |
| `0xE8` | 27 | tempo_fade_candidate |
| `0xE9` | 15 | global_transpose_candidate |
| `0xEA` | 133 | channel_transpose_candidate |
| `0xEB` | 110 | tremolo_or_modulation_on_candidate |
| `0xEC` | 66 | tremolo_or_modulation_off_candidate |
| `0xED` | 2695 | set_channel_volume_candidate |
| `0xEE` | 743 | channel_volume_fade_candidate |
| `0xEF` | 2007 | subroutine_call_candidate |
| `0xF0` | 137 | modulation_fade_candidate |
| `0xF1` | 701 | pitch_envelope_or_portamento_candidate |
| `0xF2` | 448 | pitch_envelope_off_candidate |
| `0xF3` | 498 | tuning_or_detune_candidate |
| `0xF4` | 1282 | driver_toggle_or_extended_control_candidate |
| `0xF5` | 249 | echo_or_voice_param_candidate |
| `0xF6` | 18 | echo_off_or_effect_disable_candidate |
| `0xF7` | 217 | echo_or_effect_setup_candidate |
| `0xF8` | 22 | echo_or_effect_fade_candidate |
| `0xF9` | 344 | pitch_slide_candidate |
| `0xFA` | 198 | earthbound_extended_command_candidate |
| `0xFB` | 18 | loop_start_or_control_candidate |
| `0xFC` | 18 | loop_end_or_control_candidate |
| `0xFD` | 8 | loop_or_jump_control_candidate |
| `0xFE` | 34 | jump_or_long_control_candidate |
| `0xFF` | 159 | end_or_sentinel_candidate |

## Priority Packs

| Pack | ROM range | Tracks | Walk statuses | EF edges | Terminators | Blockers |
| ---: | --- | ---: | --- | ---: | ---: | --- |
| `25` | `EC:E101..EC:EB51` | 8 | `{'blocked': 17, 'falls_through_segment': 95}` | 43 | 0 | `{'0xFE': 17}` |
| `133` | `EC:B38A..EC:BF28` | 4 | `{'falls_through_segment': 40, 'terminates': 4}` | 20 | 4 | `{}` |
| `4` | `DF:EC46..DF:FFEE` | 3 | `{'falls_through_segment': 47, 'terminates': 2}` | 103 | 2 | `{}` |
| `132` | `ED:1406..ED:1DFF` | 3 | `{'falls_through_segment': 57, 'terminates': 3}` | 31 | 3 | `{}` |
| `79` | `DC:F8BF..DC:FF92` | 3 | `{'falls_through_segment': 22, 'terminates': 2}` | 17 | 2 | `{}` |
| `103` | `EE:52E6..EE:56DF` | 3 | `{'falls_through_segment': 47, 'terminates': 3}` | 2 | 3 | `{}` |
| `83` | `EE:6D36..EE:6FDD` | 3 | `{'falls_through_segment': 44, 'terminates': 3}` | 0 | 3 | `{}` |
| `157` | `EC:F578..EC:FF94` | 10 | `{'blocked': 2, 'falls_through_segment': 78, 'terminates': 1}` | 0 | 1 | `{'0xFE': 2}` |
| `94` | `CF:F2B5..CF:FF38` | 4 | `{'blocked': 1, 'falls_through_segment': 68, 'terminates': 4}` | 42 | 4 | `{'0xFE': 1}` |
| `115` | `EE:0FB2..EE:14D4` | 2 | `{'blocked': 1, 'falls_through_segment': 19, 'terminates': 1}` | 25 | 1 | `{'0xFE': 1}` |
| `38` | `ED:6409..ED:6C06` | 2 | `{'blocked': 1, 'falls_through_segment': 28, 'terminates': 2}` | 19 | 2 | `{'0xFD': 1}` |
| `87` | `ED:0A07..ED:1406` | 2 | `{'blocked': 1, 'falls_through_segment': 34, 'terminates': 2}` | 19 | 2 | `{'0xFD': 1}` |
| `28` | `ED:B753..ED:BD60` | 2 | `{'blocked': 1, 'falls_through_segment': 32, 'terminates': 2}` | 13 | 2 | `{'0xFE': 1}` |
| `77` | `ED:C96E..ED:CF55` | 2 | `{'blocked': 1, 'falls_through_segment': 34, 'terminates': 2}` | 0 | 2 | `{'0xFE': 1}` |
| `97` | `EC:BF28..EC:CAA1` | 2 | `{'falls_through_segment': 42, 'terminates': 2}` | 43 | 2 | `{}` |
| `102` | `CE:F8C6..CE:FFAA` | 2 | `{'blocked': 1, 'falls_through_segment': 37, 'terminates': 1}` | 31 | 1 | `{}` |
| `150` | `ED:53DF..ED:5C01` | 2 | `{'falls_through_segment': 36, 'terminates': 2}` | 26 | 2 | `{}` |
| `55` | `EC:CAA1..EC:D5D8` | 2 | `{'falls_through_segment': 39, 'terminates': 3}` | 22 | 3 | `{}` |
| `149` | `E9:F8C8..E9:FF65` | 3 | `{'falls_through_segment': 52, 'terminates': 4}` | 20 | 4 | `{}` |
| `23` | `EE:3E9C..EE:42BB` | 2 | `{'falls_through_segment': 36, 'terminates': 2}` | 16 | 2 | `{}` |

## Findings

- EF call edges are now represented as explicit same-block target edges in a static walk frontier.
- A small number of EF-like bytes are tracked as out-of-block under the provisional width table, which marks operand-width or data/noise uncertainty rather than promoted call semantics.
- FD and FE remain blockers because their control-flow effect is not promoted from driver dispatch yet.
- FF is treated as a terminator candidate when encountered by the provisional walker, but exact end/return meaning still needs dispatch corroboration.
- The walker records offsets, hashes, counts, and edge metadata only; it does not embed ROM-derived sequence payload byte strings.

## Next Work

- tie FD/FE/FF behavior to the SPC700 driver dispatch path
- turn EF call edges into a checked sequence subroutine stack model
- use walker status to narrow exact-duration work to packs without unpromoted blockers first
