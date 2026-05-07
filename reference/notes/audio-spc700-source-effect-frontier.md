# Audio SPC700 Source Effect Frontier

Status: source-backed effect landmarks are recorded for runtime proof, with exact-duration promotion still blocked.

## Summary

- commands: `5`
- source-backed VCMDs: `3`
- zero-control pending: `1`
- outside-VCMD-table: `1`
- exact-duration promotion allowed: `False`
- semantic status: `source_navigation_proven_runtime_effects_not_promoted`

## Landmarks

- get_next_byte: `0x0955`
- skip_byte: `0x0957`
- voice_zero_reader: `0x0882`
- pattern_zero_reader: `0x081A`
- ef_subroutine_handler: `0x0AAC`
- ef_target_loader: `0x0AC4`
- fd_handler: `0x0B7E`
- fe_handler: `0x0B7F`
- fd_fe_post_write_helper: `0x0787`
- music_effect_fastforward_tick: `0x2DAB`
- music_effect_fastforward_start: `0x2DC6`

## Effects

| Command | Source role | Source label | Source target | Source effect status | Runtime capture requirements |
| --- | --- | --- | ---: | --- | ---: |
| `0x00` | `zero_control_pending` | `None` | `None` | `source_backed_zero_reader_paths_effect_pending_runtime_context` | 7 |
| `0xEF` | `source_backed_vcmd` | `VCMD_Subroutine` | `0x0AAC` | `source_backed_call_return_slots_runtime_effect_pending` | 4 |
| `0xFD` | `source_backed_vcmd` | `VCMD_FastForward` | `0x0B7E` | `source_backed_fast_forward_flag_write_runtime_timing_pending` | 4 |
| `0xFE` | `source_backed_vcmd` | `VCMD_FastForwardOff` | `0x0B7F` | `source_backed_fast_forward_flag_write_runtime_timing_pending` | 4 |
| `0xFF` | `outside_vcmd_table` | `None` | `None` | `outside_vcmd_table_no_source_handler` | 2 |

## Promotion Policy

- Source labels and state slots identify proof targets, but do not promote exact-duration exports.
- 0x00 proof must distinguish voice-stream loop/return behavior from pattern-level StopMusic and fast-forward control pairs.
- EF proof must join the call target, loop count, saved return pointer, and later 0x00 behavior.
- FD/FE proof must capture fast_forward_flag and timing counters before duration math can model affected regions.
- 0xFF remains outside the VCMD table unless an EarthBound reader path proves otherwise.

## Next Work

- feed these source-effect requirements into zero and nonzero probe plans
- capture EF/0x00 state transitions at runtime before unblocking finite end candidates
- capture FD/FE fast-forward flag and helper reset effects before timing promotion
