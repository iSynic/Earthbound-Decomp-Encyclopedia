# Audio Nonzero Control Coverage Report

Status: nonzero control coverage is mapped; probe outputs are still pending and current export behavior is preserved.

## Summary

- blocker tracks: `155`
- blocker export classes: `{'finite_or_transition_review_candidate': 12, 'finite_trim_candidate': 15, 'loop_or_held_candidate': 56, 'unknown_active_preview': 72}`
- probe jobs: `7`
- command jobs: `{'0xEF': 3, '0xFD': 1, '0xFE': 2, '0xFF': 1}`
- reader PC jobs: `{'0x0847': 2, '0x0957': 3, '0x0B8A': 1, '0x0D12': 1}`
- affected kinds: `{'return_stack_context': 3, 'static_walk_blocker': 1, 'timing_toggle_context': 3}`
- source candidate records: `56`
- unique source candidate tracks: `10`
- blocker source candidate tracks: `9`
- blocker tracks without source candidate: `146`
- sequence promotion allowed: `False`

## Probe Jobs

| Job | Command | Reader PC | Affected kind | Source candidates | Blocker candidates | Promotion allowed |
| --- | --- | --- | --- | ---: | ---: | --- |
| `nonzero-probe-fd-pc-0847` | `0xFD` | `0x0847` | `timing_toggle_context` | 8 | 8 | `False` |
| `nonzero-probe-fe-pc-0847` | `0xFE` | `0x0847` | `timing_toggle_context` | 8 | 8 | `False` |
| `nonzero-probe-ef-pc-0b8a` | `0xEF` | `0x0B8A` | `return_stack_context` | 8 | 7 | `False` |
| `nonzero-probe-ef-pc-0d12` | `0xEF` | `0x0D12` | `return_stack_context` | 8 | 8 | `False` |
| `nonzero-probe-ef-pc-0957` | `0xEF` | `0x0957` | `return_stack_context` | 8 | 8 | `False` |
| `nonzero-probe-fe-pc-0957` | `0xFE` | `0x0957` | `timing_toggle_context` | 8 | 8 | `False` |
| `nonzero-probe-ff-pc-0957` | `0xFF` | `0x0957` | `static_walk_blocker` | 8 | 8 | `False` |

## Source Candidate Reuse

| Track | Name | Probe job count | Primary nonzero blocker |
| ---: | --- | ---: | --- |
| 001 | `GAS_STATION` | 1 | `False` |
| 017 | `MONOTOLI_BUILDING` | 7 | `True` |
| 083 | `SKY_RUNNER` | 7 | `True` |
| 084 | `SKY_RUNNER_FALLING` | 7 | `True` |
| 109 | `EXPLOSION` | 6 | `True` |
| 110 | `SKY_RUNNER_CRASH` | 6 | `True` |
| 133 | `HIDDEN_SONG` | 1 | `True` |
| 137 | `ELEVATOR_DOWN` | 7 | `True` |
| 138 | `ELEVATOR_UP` | 7 | `True` |
| 139 | `ELEVATOR_STOP` | 7 | `True` |

## Coverage Policy

- This report maps current nonzero-control blockers to the existing probe jobs; it does not run the harness.
- Source candidates are representative evidence anchors, not complete coverage of all blocked tracks.
- Promotion stays blocked until imported probe outputs classify command effects and refresh the duration uncertainty register.
- Independent external-emulator oracle evidence remains a separate release-quality gate.

## Remaining Uncertainty

- The 7 probe jobs are representative anchors for 155 blocked tracks, not full track coverage.
- 146 primary nonzero-control blocker tracks do not appear as source candidates in the current probe plan.
- Probe output import and duration-register refresh remain required before any exact-duration promotion.
