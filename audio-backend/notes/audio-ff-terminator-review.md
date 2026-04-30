# Audio FF Terminator Review

Status: FF terminator candidates grouped; SPC700 dispatch corroboration still pending.

## Summary

- candidate packs: `92`
- candidate tracks: `123`
- promotion classes: `{'ff_can_confirm_existing_pcm_trim_candidate': 2, 'ff_can_promote_after_dispatch': 47, 'ff_can_promote_after_dispatch_and_track_review': 7, 'ff_present_but_loop_metadata_still_needed': 34, 'ff_present_with_fallthrough_roots': 2}`
- promotion-class tracks: `{'ff_can_confirm_existing_pcm_trim_candidate': 7, 'ff_can_promote_after_dispatch': 48, 'ff_can_promote_after_dispatch_and_track_review': 13, 'ff_present_but_loop_metadata_still_needed': 51, 'ff_present_with_fallthrough_roots': 4}`
- semantic status: `static_ff_candidates_ready_for_spc700_dispatch_corroboration`

## Promotion Rules

- No record in this review has FD/FE blockers; those stay in the separate blocked lane.
- FF can only be promoted to a true end/return command after SPC700 dispatch confirms its effect.
- Finite/transition review tracks still need track-context review even when FF is confirmed.
- Loop/held candidates with FF still require loop-point or hold/fade interpretation before release exactness.

## Candidates

| Pack | ROM range | Tracks | Export classes | FF candidates | EF edges | Promotion class |
| ---: | --- | --- | --- | ---: | ---: | --- |
| `97` | `EC:BF28..EC:CAA1` | `[86, 146]` | `{'unknown_active_preview': 2}` | `2` | `43` | `ff_present_with_fallthrough_roots` |
| `102` | `CE:F8C6..CE:FFAA` | `[90, 181]` | `{'unknown_active_preview': 2}` | `1` | `31` | `ff_present_with_fallthrough_roots` |
| `133` | `EC:B38A..EC:BF28` | `[116, 150, 153, 177]` | `{'loop_or_held_candidate': 2, 'unknown_active_preview': 1, 'finite_or_transition_review_candidate': 1}` | `4` | `20` | `ff_present_but_loop_metadata_still_needed` |
| `149` | `E9:F8C8..E9:FF65` | `[147, 152, 156]` | `{'finite_trim_candidate': 1, 'loop_or_held_candidate': 2}` | `4` | `20` | `ff_present_but_loop_metadata_still_needed` |
| `132` | `ED:1406..ED:1DFF` | `[114, 118, 121]` | `{'loop_or_held_candidate': 3}` | `3` | `31` | `ff_present_but_loop_metadata_still_needed` |
| `83` | `EE:6D36..EE:6FDD` | `[75, 182, 190]` | `{'loop_or_held_candidate': 3}` | `3` | `0` | `ff_present_but_loop_metadata_still_needed` |
| `79` | `DC:F8BF..DC:FF92` | `[73, 185, 187]` | `{'loop_or_held_candidate': 2, 'unknown_active_preview': 1}` | `2` | `17` | `ff_present_but_loop_metadata_still_needed` |
| `55` | `EC:CAA1..EC:D5D8` | `[58, 144]` | `{'loop_or_held_candidate': 1, 'unknown_active_preview': 1}` | `3` | `22` | `ff_present_but_loop_metadata_still_needed` |
| `150` | `ED:53DF..ED:5C01` | `[148, 149]` | `{'loop_or_held_candidate': 2}` | `2` | `26` | `ff_present_but_loop_metadata_still_needed` |
| `23` | `EE:3E9C..EE:42BB` | `[30, 31]` | `{'loop_or_held_candidate': 2}` | `2` | `16` | `ff_present_but_loop_metadata_still_needed` |
| `81` | `EE:7E29..EE:804D` | `[74, 191]` | `{'loop_or_held_candidate': 2}` | `2` | `0` | `ff_present_but_loop_metadata_still_needed` |
| `34` | `ED:27F7..ED:3195` | `[46, 122]` | `{'loop_or_held_candidate': 2}` | `1` | `13` | `ff_present_but_loop_metadata_still_needed` |
| `145` | `EA:FE8B..EA:FFE2` | `[134, 155]` | `{'loop_or_held_candidate': 2}` | `1` | `0` | `ff_present_but_loop_metadata_still_needed` |
| `85` | `ED:AB12..ED:B136` | `[76]` | `{'loop_or_held_candidate': 1}` | `3` | `25` | `ff_present_but_loop_metadata_still_needed` |
| `36` | `E2:ED2C..E2:FC88` | `[47]` | `{'loop_or_held_candidate': 1}` | `2` | `49` | `ff_present_but_loop_metadata_still_needed` |
| `112` | `EE:0554..EE:0A8B` | `[97]` | `{'loop_or_held_candidate': 1}` | `2` | `14` | `ff_present_but_loop_metadata_still_needed` |
| `111` | `DA:FB07..DA:FFEE` | `[96]` | `{'loop_or_held_candidate': 1}` | `2` | `13` | `ff_present_but_loop_metadata_still_needed` |
| `62` | `EC:9B76..EC:A7D8` | `[62]` | `{'loop_or_held_candidate': 1}` | `2` | `0` | `ff_present_but_loop_metadata_still_needed` |
| `57` | `ED:D539..ED:DAFD` | `[59]` | `{'loop_or_held_candidate': 1}` | `1` | `32` | `ff_present_but_loop_metadata_still_needed` |
| `123` | `E1:F581..E1:FFF2` | `[104]` | `{'loop_or_held_candidate': 1}` | `1` | `27` | `ff_present_but_loop_metadata_still_needed` |
| `119` | `ED:3195..ED:3A9C` | `[101]` | `{'loop_or_held_candidate': 1}` | `1` | `25` | `ff_present_but_loop_metadata_still_needed` |
| `67` | `EE:19EE..EE:1EFE` | `[65]` | `{'loop_or_held_candidate': 1}` | `1` | `22` | `ff_present_but_loop_metadata_still_needed` |
| `117` | `ED:C36C..ED:C96E` | `[100]` | `{'loop_or_held_candidate': 1}` | `1` | `21` | `ff_present_but_loop_metadata_still_needed` |
| `120` | `ED:5C01..ED:6409` | `[102]` | `{'loop_or_held_candidate': 1}` | `1` | `20` | `ff_present_but_loop_metadata_still_needed` |
| `48` | `ED:436B..ED:4BA7` | `[54]` | `{'loop_or_held_candidate': 1}` | `1` | `16` | `ff_present_but_loop_metadata_still_needed` |
| `121` | `ED:0000..ED:0A07` | `[103]` | `{'loop_or_held_candidate': 1}` | `1` | `16` | `ff_present_but_loop_metadata_still_needed` |
| `151` | `EE:648C..EE:67B7` | `[151]` | `{'loop_or_held_candidate': 1}` | `1` | `16` | `ff_present_but_loop_metadata_still_needed` |
| `6` | `E0:FCE1..E0:FFB3` | `[7]` | `{'loop_or_held_candidate': 1}` | `1` | `10` | `ff_present_but_loop_metadata_still_needed` |
| `113` | `ED:F183..ED:F710` | `[98]` | `{'loop_or_held_candidate': 1}` | `1` | `10` | `ff_present_but_loop_metadata_still_needed` |
| `143` | `DE:FCDD..DE:FFD4` | `[132]` | `{'loop_or_held_candidate': 1}` | `1` | `9` | `ff_present_but_loop_metadata_still_needed` |
| `159` | `EE:8638..EE:87CB` | `[170]` | `{'loop_or_held_candidate': 1}` | `1` | `8` | `ff_present_but_loop_metadata_still_needed` |
| `152` | `EE:826C..EE:8466` | `[154]` | `{'loop_or_held_candidate': 1}` | `1` | `3` | `ff_present_but_loop_metadata_still_needed` |
| `65` | `DB:F2EB..DB:FF64` | `[64]` | `{'loop_or_held_candidate': 1}` | `1` | `1` | `ff_present_but_loop_metadata_still_needed` |
| `41` | `EE:90FF..EE:9201` | `[50]` | `{'loop_or_held_candidate': 1}` | `1` | `0` | `ff_present_but_loop_metadata_still_needed` |
| `164` | `EE:614C..EE:648C` | `[178]` | `{'loop_or_held_candidate': 1}` | `1` | `0` | `ff_present_but_loop_metadata_still_needed` |
| `167` | `EE:8C1E..EE:8D65` | `[186]` | `{'loop_or_held_candidate': 1}` | `1` | `0` | `ff_present_but_loop_metadata_still_needed` |
| `103` | `EE:52E6..EE:56DF` | `[91, 126, 127]` | `{'finite_or_transition_review_candidate': 3}` | `3` | `2` | `ff_can_promote_after_dispatch_and_track_review` |
| `4` | `DF:EC46..DF:FFEE` | `[2, 3, 158]` | `{'unknown_active_preview': 2, 'finite_or_transition_review_candidate': 1}` | `2` | `103` | `ff_can_promote_after_dispatch_and_track_review` |
| `162` | `ED:A4D7..ED:AB12` | `[172, 180]` | `{'unknown_active_preview': 1, 'finite_or_transition_review_candidate': 1}` | `3` | `11` | `ff_can_promote_after_dispatch_and_track_review` |
| `1` | `E6:0000..E6:45D8` | `[1, 174]` | `{'unknown_active_preview': 1, 'finite_or_transition_review_candidate': 1}` | `1` | `9` | `ff_can_promote_after_dispatch_and_track_review` |
| `137` | `EE:8FD6..EE:90FF` | `[124]` | `{'finite_or_transition_review_candidate': 1}` | `1` | `6` | `ff_can_promote_after_dispatch_and_track_review` |
| `147` | `EE:804D..EE:826C` | `[142]` | `{'finite_or_transition_review_candidate': 1}` | `1` | `1` | `ff_can_promote_after_dispatch_and_track_review` |
| `130` | `EE:8D65..EE:8EA2` | `[111]` | `{'finite_or_transition_review_candidate': 1}` | `1` | `0` | `ff_can_promote_after_dispatch_and_track_review` |
| `19` | `ED:CF55..ED:D539` | `[26, 27]` | `{'unknown_active_preview': 2}` | `2` | `15` | `ff_can_promote_after_dispatch` |
| `68` | `ED:73E2..ED:7BB6` | `[66]` | `{'unknown_active_preview': 1}` | `2` | `60` | `ff_can_promote_after_dispatch` |
| `146` | `ED:F710..ED:FC9C` | `[140]` | `{'unknown_active_preview': 1}` | `2` | `36` | `ff_can_promote_after_dispatch` |
| `104` | `ED:7BB6..ED:8389` | `[92]` | `{'unknown_active_preview': 1}` | `2` | `2` | `ff_can_promote_after_dispatch` |
| `61` | `D8:F6B7..D8:FFE9` | `[61]` | `{'unknown_active_preview': 1}` | `2` | `1` | `ff_can_promote_after_dispatch` |
| `15` | `EC:EB51..EC:F578` | `[22]` | `{'unknown_active_preview': 1}` | `1` | `64` | `ff_can_promote_after_dispatch` |
| `43` | `ED:9E93..ED:A4D7` | `[51]` | `{'unknown_active_preview': 1}` | `1` | `34` | `ff_can_promote_after_dispatch` |
| `141` | `ED:3A9C..ED:436B` | `[129]` | `{'unknown_active_preview': 1}` | `1` | `34` | `ff_can_promote_after_dispatch` |
| `99` | `ED:B136..ED:B753` | `[87]` | `{'unknown_active_preview': 1}` | `1` | `32` | `ff_can_promote_after_dispatch` |
| `138` | `EE:2DCD..EE:3236` | `[125]` | `{'unknown_active_preview': 1}` | `1` | `28` | `ff_can_promote_after_dispatch` |
| `127` | `EE:3236..EE:365D` | `[106]` | `{'unknown_active_preview': 1}` | `1` | `22` | `ff_can_promote_after_dispatch` |
| `26` | `ED:9824..ED:9E93` | `[40]` | `{'unknown_active_preview': 1}` | `1` | `21` | `ff_can_promote_after_dispatch` |
| `53` | `EE:14D4..EE:19EE` | `[57]` | `{'unknown_active_preview': 1}` | `1` | `21` | `ff_can_promote_after_dispatch` |
| `30` | `ED:E65C..ED:EBF4` | `[43]` | `{'unknown_active_preview': 1}` | `1` | `20` | `ff_can_promote_after_dispatch` |
| `93` | `EE:5A99..EE:5DFA` | `[82]` | `{'unknown_active_preview': 1}` | `1` | `20` | `ff_can_promote_after_dispatch` |
| `39` | `ED:4BA7..ED:53DF` | `[49]` | `{'unknown_active_preview': 1}` | `1` | `19` | `ff_can_promote_after_dispatch` |
| `20` | `EE:1EFE..EE:2401` | `[28]` | `{'unknown_active_preview': 1}` | `1` | `18` | `ff_can_promote_after_dispatch` |
| `158` | `ED:E0AE..ED:E65C` | `[169]` | `{'unknown_active_preview': 1}` | `1` | `18` | `ff_can_promote_after_dispatch` |
| `142` | `EE:46CE..EE:4ADF` | `[131]` | `{'unknown_active_preview': 1}` | `1` | `15` | `ff_can_promote_after_dispatch` |
| `46` | `E8:F872..E8:FF1B` | `[53]` | `{'unknown_active_preview': 1}` | `1` | `14` | `ff_can_promote_after_dispatch` |
| `88` | `EE:6FDD..EE:7274` | `[79]` | `{'unknown_active_preview': 1}` | `1` | `14` | `ff_can_promote_after_dispatch` |
| `134` | `ED:EBF4..ED:F183` | `[117]` | `{'unknown_active_preview': 1}` | `1` | `14` | `ff_can_promote_after_dispatch` |
| `106` | `EC:D5D8..EC:E101` | `[93]` | `{'unknown_active_preview': 1}` | `1` | `13` | `ff_can_promote_after_dispatch` |
| `11` | `EE:42BB..EE:46CE` | `[18]` | `{'unknown_active_preview': 1}` | `1` | `12` | `ff_can_promote_after_dispatch` |
| `49` | `EE:87CB..EE:894F` | `[55]` | `{'unknown_active_preview': 1}` | `1` | `12` | `ff_can_promote_after_dispatch` |
| `135` | `EE:6A85..EE:6D36` | `[119]` | `{'unknown_active_preview': 1}` | `1` | `11` | `ff_can_promote_after_dispatch` |
| `9` | `EE:894F..EE:8ACA` | `[16]` | `{'unknown_active_preview': 1}` | `1` | `10` | `ff_can_promote_after_dispatch` |
| `32` | `E3:FDCC..E3:FFF2` | `[45]` | `{'unknown_active_preview': 1}` | `1` | `9` | `ff_can_promote_after_dispatch` |
| `91` | `EE:7BDF..EE:7E29` | `[81]` | `{'unknown_active_preview': 1}` | `1` | `8` | `ff_can_promote_after_dispatch` |
| `101` | `EE:4EEA..EE:52E6` | `[89]` | `{'unknown_active_preview': 1}` | `1` | `7` | `ff_can_promote_after_dispatch` |
| `29` | `ED:FC9C..ED:FFFE` | `[42]` | `{'unknown_active_preview': 1}` | `1` | `6` | `ff_can_promote_after_dispatch` |
| `12` | `EE:67B7..EE:6A85` | `[19]` | `{'unknown_active_preview': 1}` | `1` | `5` | `ff_can_promote_after_dispatch` |
| `45` | `D9:FC18..D9:FFE1` | `[52]` | `{'unknown_active_preview': 1}` | `1` | `4` | `ff_can_promote_after_dispatch` |
| `128` | `EE:8466..EE:8638` | `[107]` | `{'unknown_active_preview': 1}` | `1` | `4` | `ff_can_promote_after_dispatch` |
| `31` | `EE:7274..EE:74D7` | `[44]` | `{'unknown_active_preview': 1}` | `1` | `2` | `ff_can_promote_after_dispatch` |
| `100` | `ED:91AF..ED:9824` | `[88]` | `{'unknown_active_preview': 1}` | `1` | `2` | `ff_can_promote_after_dispatch` |
| `129` | `EE:74D7..EE:7737` | `[108]` | `{'unknown_active_preview': 1}` | `1` | `2` | `ff_can_promote_after_dispatch` |
| `168` | `EE:8EA2..EE:8FD6` | `[188]` | `{'unknown_active_preview': 1}` | `1` | `2` | `ff_can_promote_after_dispatch` |
| `17` | `EE:798E..EE:7BDF` | `[24]` | `{'unknown_active_preview': 1}` | `1` | `1` | `ff_can_promote_after_dispatch` |
| `63` | `EE:28FE..EE:2DCD` | `[63]` | `{'unknown_active_preview': 1}` | `1` | `1` | `ff_can_promote_after_dispatch` |
| `155` | `E4:FD92..E4:FFF9` | `[159]` | `{'unknown_active_preview': 1}` | `1` | `1` | `ff_can_promote_after_dispatch` |
| `13` | `EB:FE22..EB:FFFF` | `[20]` | `{'unknown_active_preview': 1}` | `1` | `0` | `ff_can_promote_after_dispatch` |
| `59` | `CB:FEE2..CB:FFE4` | `[60]` | `{'unknown_active_preview': 1}` | `1` | `0` | `ff_can_promote_after_dispatch` |
| `69` | `EE:8ACA..EE:8C1E` | `[67]` | `{'unknown_active_preview': 1}` | `1` | `0` | `ff_can_promote_after_dispatch` |
| `73` | `E6:FF18..E6:FFF5` | `[69]` | `{'unknown_active_preview': 1}` | `1` | `0` | `ff_can_promote_after_dispatch` |
| `75` | `DD:FECE..DD:FFF8` | `[70]` | `{'unknown_active_preview': 1}` | `1` | `0` | `ff_can_promote_after_dispatch` |
| `166` | `E5:FF38..E5:FFDE` | `[179]` | `{'unknown_active_preview': 1}` | `1` | `0` | `ff_can_promote_after_dispatch` |
| `10` | `ED:BD60..ED:C36C` | `[17, 137, 138, 139]` | `{'unknown_active_preview': 1, 'finite_trim_candidate': 3}` | `4` | `37` | `ff_can_confirm_existing_pcm_trim_candidate` |
| `14` | `ED:DAFD..ED:E0AE` | `[21, 112, 113]` | `{'unknown_active_preview': 2, 'finite_trim_candidate': 1}` | `2` | `8` | `ff_can_confirm_existing_pcm_trim_candidate` |

## Findings

- The no-FD/FE FF lane covers packs that are structurally ready for dispatch corroboration.
- Candidate packs mix finite trims, finite/transition reviews, unknown active previews, and loop/held tracks, so FF confirmation alone is necessary but not sufficient for public exact exports.
- Tracks whose export class is finite_trim_candidate can use FF as sequence corroboration for existing PCM silence evidence once the driver dispatch is named.
- Loop/held packs with FF likely need intro/body loop modeling rather than simple finite-end promotion.

## Next Work

- inspect the SPC700 high-command dispatch path for FF and record whether it stops a channel, returns from EF, or ends a sequence
- after FF dispatch is confirmed, promote finite_trim_candidate records to sequence-corroborated finite metadata
- keep loop_or_held_candidate records in the loop-point lane even if FF is confirmed as a local terminator
