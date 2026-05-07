# Audio Exact-Duration Triage

Status: exact-duration release promotion is still pending, but sequence work is now sorted into actionable lanes.

## Summary

- sequence packs triaged: `119`
- category pack counts: `{'blocked_by_unpromoted_control': 108, 'candidate_for_zero_terminator_review': 10, 'no_sequence_semantics_needed': 1}`
- category track counts: `{'blocked_by_unpromoted_control': 155, 'candidate_for_zero_terminator_review': 19, 'no_sequence_semantics_needed': 1}`
- command semantics status: `runtime_command_semantics_promotion_blocked`
- sequence promotion allowed: `False`
- release status: `exact_duration_not_promoted_sequence_triage_ready`

## Lane Diagnostics

| Lane | Packs | Tracks | Export classes | Terminators | EF edges | Blockers | Next step |
| --- | ---: | ---: | --- | ---: | ---: | --- | --- |
| `blocked_by_unpromoted_control` | 108 | 155 | `{'finite_trim_candidate': 15, 'finite_or_transition_review_candidate': 12, 'unknown_active_preview': 72, 'loop_or_held_candidate': 56}` | 854 | 994 | `{'0xFF': 149}` | decode FD/FE/FF command behavior through SPC700 driver dispatch before exact duration promotion |
| `candidate_for_zero_terminator_review` | 10 | 19 | `{'finite_or_transition_review_candidate': 10, 'unknown_active_preview': 7, 'loop_or_held_candidate': 2}` | 62 | 98 | `{}` | build focused pack report and confirm whether 0x00 marks sequence end or EF subroutine return |
| `no_sequence_semantics_needed` | 1 | 1 | `{'finite_trim_candidate': 1}` | 6 | 0 | `{'0xFF': 1}` | no sequence-duration action required |

## candidate_for_zero_terminator_review

| Pack | ROM range | Tracks | Export classes | EF edges | Terminators | Terminator commands | Blockers | Semantic evidence |
| ---: | --- | --- | --- | ---: | ---: | --- | --- | --- |
| `25` | `EC:E101..EC:EB51` | `[32, 33, 34, 35, 36, 37, 38, 39]` | `{'finite_or_transition_review_candidate': 8}` | 44 | 32 | `{'0x00': 32}` | `{}` | `pending_earthbound_zero_control_effect_proof` |
| `136` | `EE:0000..EE:0554` | `[120, 173]` | `{'unknown_active_preview': 1, 'loop_or_held_candidate': 1}` | 0 | 5 | `{'0x00': 5}` | `{}` | `pending_earthbound_zero_control_effect_proof` |
| `1` | `E6:0000..E6:45D8` | `[1, 174]` | `{'unknown_active_preview': 1, 'finite_or_transition_review_candidate': 1}` | 9 | 2 | `{'0x00': 2}` | `{}` | `pending_earthbound_zero_control_effect_proof` |
| `148` | `EE:3A7D..EE:3E9C` | `[143]` | `{'unknown_active_preview': 1}` | 12 | 5 | `{'0x00': 5}` | `{}` | `pending_earthbound_zero_control_effect_proof` |
| `160` | `EE:4ADF..EE:4EEA` | `[171]` | `{'loop_or_held_candidate': 1}` | 20 | 4 | `{'0x00': 4}` | `{}` | `pending_earthbound_zero_control_effect_proof` |
| `154` | `EB:E9E4..EB:FE22` | `[157]` | `{'unknown_active_preview': 1}` | 6 | 4 | `{'0x00': 4}` | `{}` | `pending_earthbound_zero_control_effect_proof` |
| `107` | `EC:4592..EC:6700` | `[94]` | `{'unknown_active_preview': 1}` | 3 | 4 | `{'0x00': 4}` | `{}` | `pending_earthbound_zero_control_effect_proof` |
| `18` | `E2:FC88..E2:FFFD` | `[25]` | `{'unknown_active_preview': 1}` | 0 | 3 | `{'0x00': 3}` | `{}` | `pending_earthbound_zero_control_effect_proof` |
| `163` | `EE:0A8B..EE:0FB2` | `[175]` | `{'finite_or_transition_review_candidate': 1}` | 4 | 2 | `{'0x00': 2}` | `{}` | `pending_earthbound_zero_control_effect_proof` |
| `96` | `CF:FF38..CF:FFF9` | `[85]` | `{'unknown_active_preview': 1}` | 0 | 1 | `{'0x00': 1}` | `{}` | `pending_earthbound_zero_control_effect_proof` |

## candidate_for_ff_variant_review

| Pack | ROM range | Tracks | Export classes | EF edges | Terminators | Terminator commands | Blockers | Semantic evidence |
| ---: | --- | --- | --- | ---: | ---: | --- | --- | --- |

## blocked_by_unpromoted_control

| Pack | ROM range | Tracks | Export classes | EF edges | Terminators | Terminator commands | Blockers | Semantic evidence |
| ---: | --- | --- | --- | ---: | ---: | --- | --- | --- |
| `157` | `EC:F578..EC:FF94` | `[160, 161, 162, 163, 164, 165, 166, 167, 168, 189]` | `{'finite_trim_candidate': 8, 'finite_or_transition_review_candidate': 2}` | 0 | 20 | `{'0x00': 20}` | `{'0xFF': 1}` | `blocked_by_control_semantics` |
| `94` | `CF:F2B5..CF:FF38` | `[83, 84, 109, 110]` | `{'unknown_active_preview': 1, 'finite_or_transition_review_candidate': 1, 'finite_trim_candidate': 2}` | 25 | 20 | `{'0x00': 20}` | `{'0xFF': 4}` | `blocked_by_control_semantics` |
| `10` | `ED:BD60..ED:C36C` | `[17, 137, 138, 139]` | `{'unknown_active_preview': 1, 'finite_trim_candidate': 3}` | 37 | 19 | `{'0x00': 19}` | `{'0xFF': 4}` | `blocked_by_control_semantics` |
| `133` | `EC:B38A..EC:BF28` | `[116, 150, 153, 177]` | `{'loop_or_held_candidate': 2, 'unknown_active_preview': 1, 'finite_or_transition_review_candidate': 1}` | 18 | 16 | `{'0x00': 16}` | `{'0xFF': 3}` | `blocked_by_control_semantics` |
| `14` | `ED:DAFD..ED:E0AE` | `[21, 112, 113]` | `{'unknown_active_preview': 2, 'finite_trim_candidate': 1}` | 8 | 19 | `{'0x00': 19}` | `{'0xFF': 2}` | `blocked_by_control_semantics` |
| `4` | `DF:EC46..DF:FFEE` | `[2, 3, 158]` | `{'unknown_active_preview': 2, 'finite_or_transition_review_candidate': 1}` | 44 | 18 | `{'0x00': 18}` | `{'0xFF': 2}` | `blocked_by_control_semantics` |
| `132` | `ED:1406..ED:1DFF` | `[114, 118, 121]` | `{'loop_or_held_candidate': 3}` | 18 | 17 | `{'0x00': 17}` | `{'0xFF': 3}` | `blocked_by_control_semantics` |
| `103` | `EE:52E6..EE:56DF` | `[91, 126, 127]` | `{'finite_or_transition_review_candidate': 3}` | 2 | 17 | `{'0x00': 17}` | `{'0xFF': 3}` | `blocked_by_control_semantics` |
| `149` | `E9:F8C8..E9:FF65` | `[147, 152, 156]` | `{'finite_trim_candidate': 1, 'loop_or_held_candidate': 2}` | 20 | 16 | `{'0x00': 16}` | `{'0xFF': 3}` | `blocked_by_control_semantics` |
| `83` | `EE:6D36..EE:6FDD` | `[75, 182, 190]` | `{'loop_or_held_candidate': 3}` | 0 | 14 | `{'0x00': 14}` | `{'0xFF': 3}` | `blocked_by_control_semantics` |
| `79` | `DC:F8BF..DC:FF92` | `[73, 185, 187]` | `{'loop_or_held_candidate': 2, 'unknown_active_preview': 1}` | 10 | 10 | `{'0x00': 10}` | `{'0xFF': 2}` | `blocked_by_control_semantics` |
| `19` | `ED:CF55..ED:D539` | `[26, 27]` | `{'unknown_active_preview': 2}` | 15 | 15 | `{'0x00': 15}` | `{'0xFF': 2}` | `blocked_by_control_semantics` |
| `38` | `ED:6409..ED:6C06` | `[48, 136]` | `{'loop_or_held_candidate': 2}` | 16 | 14 | `{'0x00': 14}` | `{'0xFF': 2}` | `blocked_by_control_semantics` |
| `87` | `ED:0A07..ED:1406` | `[78, 130]` | `{'loop_or_held_candidate': 2}` | 17 | 13 | `{'0x00': 13}` | `{'0xFF': 2}` | `blocked_by_control_semantics` |
| `28` | `ED:B753..ED:BD60` | `[41, 145]` | `{'unknown_active_preview': 2}` | 10 | 12 | `{'0x00': 12}` | `{'0xFF': 2}` | `blocked_by_control_semantics` |
| `150` | `ED:53DF..ED:5C01` | `[148, 149]` | `{'loop_or_held_candidate': 2}` | 10 | 12 | `{'0x00': 12}` | `{'0xFF': 2}` | `blocked_by_control_semantics` |
| `162` | `ED:A4D7..ED:AB12` | `[172, 180]` | `{'unknown_active_preview': 1, 'finite_or_transition_review_candidate': 1}` | 9 | 11 | `{'0x00': 11}` | `{'0xFF': 2}` | `blocked_by_control_semantics` |
| `97` | `EC:BF28..EC:CAA1` | `[86, 146]` | `{'unknown_active_preview': 2}` | 25 | 10 | `{'0x00': 10}` | `{'0xFF': 2}` | `blocked_by_control_semantics` |
| `55` | `EC:CAA1..EC:D5D8` | `[58, 144]` | `{'loop_or_held_candidate': 1, 'unknown_active_preview': 1}` | 15 | 10 | `{'0x00': 10}` | `{'0xFF': 3}` | `blocked_by_control_semantics` |
| `34` | `ED:27F7..ED:3195` | `[46, 122]` | `{'loop_or_held_candidate': 2}` | 10 | 9 | `{'0x00': 9}` | `{'0xFF': 1}` | `blocked_by_control_semantics` |

## needs_loop_or_fallthrough_semantics

| Pack | ROM range | Tracks | Export classes | EF edges | Terminators | Terminator commands | Blockers | Semantic evidence |
| ---: | --- | --- | --- | ---: | ---: | --- | --- | --- |

## no_sequence_semantics_needed

| Pack | ROM range | Tracks | Export classes | EF edges | Terminators | Terminator commands | Blockers | Semantic evidence |
| ---: | --- | --- | --- | ---: | ---: | --- | --- | --- |
| `7` | `E8:FF1B..E8:FFED` | `[15]` | `{'finite_trim_candidate': 1}` | 0 | 6 | `{'0x00': 6}` | `{'0xFF': 1}` | `not_promoted_by_command_semantics` |

## Findings

- Exact-duration work now splits into packs with N-SPC 0x00 terminator candidates, packs blocked by unpromoted control, and packs needing loop/fallthrough semantics.
- The PK Hack/N-SPC confirmation moves finite-end review away from static FF terminator assumptions.
- Packs with 0x00 terminator candidates are the fastest next candidates for exact finite review, but EF return context still matters.
- Loop/held preview tracks still need explicit loop-point or fade policy even when playback/export is already near-oracle accurate.

## Next Work

- promote candidate_for_zero_terminator_review packs into focused reports that distinguish song end from EF subroutine return
- decode FD/FE fast-forward timing behavior because it can skip or resume audible playback
- keep FF in a variant/unreachable review lane unless EarthBound driver proof contradicts stock N-SPC
- feed resolved exact finite or loop outcomes back into audio-export-plan
