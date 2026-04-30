# Audio Exact-Duration Triage

Status: exact-duration release promotion is still pending, but sequence work is now sorted into actionable lanes.

## Summary

- sequence packs triaged: `119`
- category pack counts: `{'blocked_by_unpromoted_fd_fe_control': 22, 'candidate_for_ff_terminator_review': 92, 'needs_loop_or_fallthrough_semantics': 4, 'no_sequence_semantics_needed': 1}`
- category track counts: `{'blocked_by_unpromoted_fd_fe_control': 46, 'candidate_for_ff_terminator_review': 123, 'needs_loop_or_fallthrough_semantics': 5, 'no_sequence_semantics_needed': 1}`
- release status: `exact_duration_not_promoted_sequence_triage_ready`

## candidate_for_ff_terminator_review

| Pack | ROM range | Tracks | Export classes | EF edges | Terminators | Blockers |
| ---: | --- | --- | --- | ---: | ---: | --- |
| `10` | `ED:BD60..ED:C36C` | `[17, 137, 138, 139]` | `{'unknown_active_preview': 1, 'finite_trim_candidate': 3}` | 37 | 4 | `{}` |
| `133` | `EC:B38A..EC:BF28` | `[116, 150, 153, 177]` | `{'loop_or_held_candidate': 2, 'unknown_active_preview': 1, 'finite_or_transition_review_candidate': 1}` | 20 | 4 | `{}` |
| `149` | `E9:F8C8..E9:FF65` | `[147, 152, 156]` | `{'finite_trim_candidate': 1, 'loop_or_held_candidate': 2}` | 20 | 4 | `{}` |
| `132` | `ED:1406..ED:1DFF` | `[114, 118, 121]` | `{'loop_or_held_candidate': 3}` | 31 | 3 | `{}` |
| `103` | `EE:52E6..EE:56DF` | `[91, 126, 127]` | `{'finite_or_transition_review_candidate': 3}` | 2 | 3 | `{}` |
| `83` | `EE:6D36..EE:6FDD` | `[75, 182, 190]` | `{'loop_or_held_candidate': 3}` | 0 | 3 | `{}` |
| `4` | `DF:EC46..DF:FFEE` | `[2, 3, 158]` | `{'unknown_active_preview': 2, 'finite_or_transition_review_candidate': 1}` | 103 | 2 | `{}` |
| `79` | `DC:F8BF..DC:FF92` | `[73, 185, 187]` | `{'loop_or_held_candidate': 2, 'unknown_active_preview': 1}` | 17 | 2 | `{}` |
| `14` | `ED:DAFD..ED:E0AE` | `[21, 112, 113]` | `{'unknown_active_preview': 2, 'finite_trim_candidate': 1}` | 8 | 2 | `{}` |
| `55` | `EC:CAA1..EC:D5D8` | `[58, 144]` | `{'loop_or_held_candidate': 1, 'unknown_active_preview': 1}` | 22 | 3 | `{}` |
| `162` | `ED:A4D7..ED:AB12` | `[172, 180]` | `{'unknown_active_preview': 1, 'finite_or_transition_review_candidate': 1}` | 11 | 3 | `{}` |
| `97` | `EC:BF28..EC:CAA1` | `[86, 146]` | `{'unknown_active_preview': 2}` | 43 | 2 | `{}` |
| `150` | `ED:53DF..ED:5C01` | `[148, 149]` | `{'loop_or_held_candidate': 2}` | 26 | 2 | `{}` |
| `23` | `EE:3E9C..EE:42BB` | `[30, 31]` | `{'loop_or_held_candidate': 2}` | 16 | 2 | `{}` |
| `19` | `ED:CF55..ED:D539` | `[26, 27]` | `{'unknown_active_preview': 2}` | 15 | 2 | `{}` |
| `81` | `EE:7E29..EE:804D` | `[74, 191]` | `{'loop_or_held_candidate': 2}` | 0 | 2 | `{}` |
| `102` | `CE:F8C6..CE:FFAA` | `[90, 181]` | `{'unknown_active_preview': 2}` | 31 | 1 | `{}` |
| `34` | `ED:27F7..ED:3195` | `[46, 122]` | `{'loop_or_held_candidate': 2}` | 13 | 1 | `{}` |
| `1` | `E6:0000..E6:45D8` | `[1, 174]` | `{'unknown_active_preview': 1, 'finite_or_transition_review_candidate': 1}` | 9 | 1 | `{}` |
| `145` | `EA:FE8B..EA:FFE2` | `[134, 155]` | `{'loop_or_held_candidate': 2}` | 0 | 1 | `{}` |

## blocked_by_unpromoted_fd_fe_control

| Pack | ROM range | Tracks | Export classes | EF edges | Terminators | Blockers |
| ---: | --- | --- | --- | ---: | ---: | --- |
| `157` | `EC:F578..EC:FF94` | `[160, 161, 162, 163, 164, 165, 166, 167, 168, 189]` | `{'finite_trim_candidate': 8, 'finite_or_transition_review_candidate': 2}` | 0 | 1 | `{'0xFE': 2}` |
| `25` | `EC:E101..EC:EB51` | `[32, 33, 34, 35, 36, 37, 38, 39]` | `{'finite_or_transition_review_candidate': 8}` | 43 | 0 | `{'0xFE': 17}` |
| `94` | `CF:F2B5..CF:FF38` | `[83, 84, 109, 110]` | `{'unknown_active_preview': 1, 'finite_or_transition_review_candidate': 1, 'finite_trim_candidate': 2}` | 42 | 4 | `{'0xFE': 1}` |
| `38` | `ED:6409..ED:6C06` | `[48, 136]` | `{'loop_or_held_candidate': 2}` | 19 | 2 | `{'0xFD': 1}` |
| `87` | `ED:0A07..ED:1406` | `[78, 130]` | `{'loop_or_held_candidate': 2}` | 19 | 2 | `{'0xFD': 1}` |
| `28` | `ED:B753..ED:BD60` | `[41, 145]` | `{'unknown_active_preview': 2}` | 13 | 2 | `{'0xFE': 1}` |
| `77` | `ED:C96E..ED:CF55` | `[71, 72]` | `{'unknown_active_preview': 1, 'loop_or_held_candidate': 1}` | 0 | 2 | `{'0xFE': 1}` |
| `115` | `EE:0FB2..EE:14D4` | `[99, 141]` | `{'loop_or_held_candidate': 2}` | 25 | 1 | `{'0xFE': 1}` |
| `109` | `EC:23EC..EC:4592` | `[95]` | `{'unknown_active_preview': 1}` | 58 | 4 | `{'0xFD': 1}` |
| `140` | `EA:F124..EA:FE8B` | `[128]` | `{'unknown_active_preview': 1}` | 26 | 2 | `{'0xFD': 1}` |
| `71` | `CC:F617..CC:FFDB` | `[68]` | `{'unknown_active_preview': 1}` | 46 | 1 | `{'0xFE': 1}` |
| `125` | `E4:EED0..E4:FD92` | `[105]` | `{'unknown_active_preview': 1}` | 46 | 1 | `{'0xFD': 1}` |
| `90` | `ED:8389..ED:8B21` | `[80]` | `{'unknown_active_preview': 1}` | 43 | 1 | `{'0xFE': 1}` |
| `86` | `ED:8B21..ED:91AF` | `[77]` | `{'loop_or_held_candidate': 1}` | 21 | 1 | `{'0xFE': 1}` |
| `51` | `EE:56DF..EE:5A99` | `[56]` | `{'loop_or_held_candidate': 1}` | 19 | 1 | `{'0xFD': 1}` |
| `144` | `EE:2401..EE:28FE` | `[133]` | `{'unknown_active_preview': 1}` | 14 | 1 | `{'0xFE': 1}` |
| `16` | `EE:365D..EE:3A7D` | `[23]` | `{'unknown_active_preview': 1}` | 6 | 1 | `{'0xFD': 1}` |
| `18` | `E2:FC88..E2:FFFD` | `[25]` | `{'unknown_active_preview': 1}` | 3 | 1 | `{'0xFE': 1}` |
| `22` | `EE:7737..EE:798E` | `[29]` | `{'loop_or_held_candidate': 1}` | 3 | 1 | `{'0xFE': 1}` |
| `107` | `EC:4592..EC:6700` | `[94]` | `{'unknown_active_preview': 1}` | 81 | 0 | `{'0xFD': 1, '0xFE': 3}` |

## needs_loop_or_fallthrough_semantics

| Pack | ROM range | Tracks | Export classes | EF edges | Terminators | Blockers |
| ---: | --- | --- | --- | ---: | ---: | --- |
| `136` | `EE:0000..EE:0554` | `[120, 173]` | `{'unknown_active_preview': 1, 'loop_or_held_candidate': 1}` | 12 | 0 | `{}` |
| `160` | `EE:4ADF..EE:4EEA` | `[171]` | `{'loop_or_held_candidate': 1}` | 20 | 0 | `{}` |
| `163` | `EE:0A8B..EE:0FB2` | `[175]` | `{'finite_or_transition_review_candidate': 1}` | 4 | 0 | `{}` |
| `96` | `CF:FF38..CF:FFF9` | `[85]` | `{'unknown_active_preview': 1}` | 0 | 0 | `{}` |

## no_sequence_semantics_needed

| Pack | ROM range | Tracks | Export classes | EF edges | Terminators | Blockers |
| ---: | --- | --- | --- | ---: | ---: | --- |
| `7` | `E8:FF1B..E8:FFED` | `[15]` | `{'finite_trim_candidate': 1}` | 0 | 1 | `{}` |

## Findings

- Exact-duration work now splits into packs with FF terminator candidates, packs blocked by FD/FE, and packs needing loop/fallthrough semantics.
- Pack 25 remains blocked by FE behavior despite clean eb-decompile payload corroboration and strong EF call-edge evidence.
- Packs without FD/FE blockers and with FF terminator candidates are the fastest next candidates for exact finite review.
- Loop/held preview tracks still need explicit loop-point or fade policy even when playback/export is already near-oracle accurate.

## Next Work

- promote candidate_for_ff_terminator_review packs into focused reports before tackling FD/FE dispatch
- decode FE behavior because it blocks pack 25 and several finite/review families
- feed resolved exact finite or loop outcomes back into audio-export-plan
