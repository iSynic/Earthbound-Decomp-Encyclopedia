# Audio Nonzero Control Semantics Frontier

Status: the 155-track non-0x00 duration lane is grouped by command family and remains effect-proof pending.

## Summary

- tracks: `155`
- packs: `108`
- export classes: `{'finite_or_transition_review_candidate': 12, 'finite_trim_candidate': 15, 'loop_or_held_candidate': 56, 'unknown_active_preview': 72}`
- FF static blockers: `149`
- EF call edges: `994`
- command runtime reads: `{'0xEF': 475, '0xFD': 1, '0xFE': 5, '0xFF': 12}`
- command reader PCs: `{'0xEF': 3, '0xFD': 1, '0xFE': 2, '0xFF': 1}`
- sequence promotion allowed: `False`

## Command Frontier

| Command | Status | Static target | Runtime reads | Reader PCs | Affected kind | Affected observations |
| --- | --- | --- | ---: | ---: | --- | ---: |
| `0xEF` | `runtime_interpreter_read_observed_dispatch_decode_pending` | `0x0AAC` | 475 | 3 | `return_stack_context` | 994 |
| `0xFD` | `runtime_interpreter_read_observed_dispatch_decode_pending` | `0x0B7E` | 1 | 1 | `timing_toggle_context` | 1 |
| `0xFE` | `runtime_interpreter_read_observed_dispatch_decode_pending` | `0x0B7F` | 5 | 2 | `timing_toggle_context` | 5 |
| `0xFF` | `contradicted_by_stock_n_spc_pending_earthbound_variant_proof` | `None` | 12 | 1 | `static_walk_blocker` | 149 |

## Priority Packs

| Pack | Tracks | Export classes | FF blockers | EF edges |
| ---: | --- | --- | ---: | ---: |
| `10` | `[17, 137, 138, 139]` | `{'unknown_active_preview': 1, 'finite_trim_candidate': 3}` | 4 | 37 |
| `94` | `[83, 84, 109, 110]` | `{'unknown_active_preview': 1, 'finite_or_transition_review_candidate': 1, 'finite_trim_candidate': 2}` | 4 | 25 |
| `109` | `[95]` | `{'unknown_active_preview': 1}` | 4 | 9 |
| `149` | `[147, 152, 156]` | `{'finite_trim_candidate': 1, 'loop_or_held_candidate': 2}` | 3 | 20 |
| `133` | `[116, 150, 153, 177]` | `{'loop_or_held_candidate': 2, 'unknown_active_preview': 1, 'finite_or_transition_review_candidate': 1}` | 3 | 18 |
| `132` | `[114, 118, 121]` | `{'loop_or_held_candidate': 3}` | 3 | 18 |
| `85` | `[76]` | `{'loop_or_held_candidate': 1}` | 3 | 16 |
| `55` | `[58, 144]` | `{'loop_or_held_candidate': 1, 'unknown_active_preview': 1}` | 3 | 15 |
| `103` | `[91, 126, 127]` | `{'finite_or_transition_review_candidate': 3}` | 3 | 2 |
| `83` | `[75, 182, 190]` | `{'loop_or_held_candidate': 3}` | 3 | 0 |
| `4` | `[2, 3, 158]` | `{'unknown_active_preview': 2, 'finite_or_transition_review_candidate': 1}` | 2 | 44 |
| `97` | `[86, 146]` | `{'unknown_active_preview': 2}` | 2 | 25 |
| `68` | `[66]` | `{'unknown_active_preview': 1}` | 2 | 21 |
| `36` | `[47]` | `{'loop_or_held_candidate': 1}` | 2 | 20 |
| `87` | `[78, 130]` | `{'loop_or_held_candidate': 2}` | 2 | 17 |
| `38` | `[48, 136]` | `{'loop_or_held_candidate': 2}` | 2 | 16 |

## Promotion Policy

- This frontier is diagnostic only and cannot promote sequence-derived exact duration.
- 0xFF remains an EarthBound variant/unreachable blocker until local reader-path effect is decoded.
- 0xEF call/return behavior is required context for exact end-vs-return decisions.
- FD/FE timing toggles require local timing-effect proof before exact duration math can depend on them.

## Next Work

- decode reader PC 0x0957 first because it observes FF, FE, and EF in the current control-reader frontier
- join FF observations to post-read branch/effect state and classify EarthBound-specific behavior
- capture FD/FE timing counter or tempo mutations for the rare observed reads
- feed validated effects back into audio-sequence-command-semantics before changing export policy
