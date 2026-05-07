# Audio Nonzero Control Probe Plan

Status: targeted EF/FD/FE/FF reader-PC probe jobs are planned; runtime effect proof is still pending.

## Summary

- jobs: `7`
- command jobs: `{'0xEF': 3, '0xFD': 1, '0xFE': 2, '0xFF': 1}`
- reader PC jobs: `{'0x0847': 2, '0x0957': 3, '0x0B8A': 1, '0x0D12': 1}`
- affected kinds: `{'return_stack_context': 3, 'static_walk_blocker': 1, 'timing_toggle_context': 3}`
- source candidates: `56`
- source candidates joined to oracle jobs: `56`
- frontier tracks: `155`
- sequence promotion allowed: `False`

## Probe Contract

- harness target: `future zero/nonzero-capable ares audio harness external mode`
- behavior change allowed: `False`
- public exact promotion allowed: `False`
- required capture fields: `['sequence_read_trace', 'track_id', 'track_name', 'command', 'reader_pc', 'sequence_address', 'instruction', 'registers.ya', 'registers.x', 'registers.s', 'registers.p', 'command_pointer_registers.dp_10_11', 'command_pointer_registers.dp_12_13', 'post_read_pc', 'post_read_branch_or_effect', 'voice_slot_state', 'phrase_or_subroutine_stack_state', 'timing_counter_state', 'tempo_or_fast_forward_state', 'control_effect_classification', 'classification_evidence']`
- accepted classifications: `['ef_call_return', 'timing_toggle', 'earthbound_variant_ff', 'unreachable', 'unresolved']`

## Jobs

| Job | Command | Reader PC | Reads | Affected kind | Source candidates | Output root |
| --- | --- | --- | ---: | --- | ---: | --- |
| `nonzero-probe-ff-pc-0957` | `0xFF` | `0x0957` | 10 | `static_walk_blocker` | 8 | `build/audio/nonzero-control-probe/nonzero-probe-ff-pc-0957` |
| `nonzero-probe-ef-pc-0957` | `0xEF` | `0x0957` | 23 | `return_stack_context` | 8 | `build/audio/nonzero-control-probe/nonzero-probe-ef-pc-0957` |
| `nonzero-probe-fe-pc-0957` | `0xFE` | `0x0957` | 4 | `timing_toggle_context` | 8 | `build/audio/nonzero-control-probe/nonzero-probe-fe-pc-0957` |
| `nonzero-probe-ef-pc-0b8a` | `0xEF` | `0x0B8A` | 95 | `return_stack_context` | 8 | `build/audio/nonzero-control-probe/nonzero-probe-ef-pc-0b8a` |
| `nonzero-probe-ef-pc-0d12` | `0xEF` | `0x0D12` | 1 | `return_stack_context` | 8 | `build/audio/nonzero-control-probe/nonzero-probe-ef-pc-0d12` |
| `nonzero-probe-fd-pc-0847` | `0xFD` | `0x0847` | 1 | `timing_toggle_context` | 8 | `build/audio/nonzero-control-probe/nonzero-probe-fd-pc-0847` |
| `nonzero-probe-fe-pc-0847` | `0xFE` | `0x0847` | 1 | `timing_toggle_context` | 8 | `build/audio/nonzero-control-probe/nonzero-probe-fe-pc-0847` |

## Promotion Policy

- This plan creates diagnostic jobs only and cannot promote sequence-derived public exact-duration exports.
- 0xFF remains a static-walk blocker until EarthBound reader-path effect is locally classified.
- EF evidence must describe call/return state, not just command reads.
- FD/FE evidence must describe source-backed fast_forward_flag and helper reset state before exact duration math can depend on it.

## Next Work

- run the 0x0957 FF/FE/EF jobs first because that reader PC spans the highest-value command mix
- add a nonzero control result validator/collector after the harness writes real effect classifications
- feed only validated command effects back into audio-sequence-command-semantics
