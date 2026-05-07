# Audio FD/FE Timing Frontier

Status: FD/FE are source-backed VCMDs, but fast-forward timing effects remain unproven.

## Summary

- commands: `2`
- source-backed VCMDs: `2`
- runtime reads: `6`
- reader PC links: `3`
- exact-duration promotion allowed: `False`
- semantic status: `fd_fe_timing_effects_unproven`

## Commands

| Command | Source label | Source target | Arg bytes | Effect proof | Runtime reads | Reader PCs |
| --- | --- | ---: | ---: | --- | ---: | ---: |
| `0xFD` | `VCMD_FastForward` | `0x0B7E` | `0` | `runtime_effect_pending` | 1 | 1 |
| `0xFE` | `VCMD_FastForwardOff` | `0x0B7F` | `0` | `runtime_effect_pending` | 5 | 2 |

## Promotion Policy

- FD and FE have source-backed VCMD labels and zero argument bytes.
- FD/FE source-effect facts prove the fast_forward_flag write and L_0787 helper path, but not the duration impact.
- Source labels identify the timing lane, but do not prove export duration math.
- Exact-duration export remains blocked until local runtime timing effects are captured.

## Next Work

- trace reader PCs 0x0847 and 0x0957 for FD/FE observations
- join traces to fast_forward_flag, mfx_fastforward_timer, and tempo restore state
- feed confirmed timing effects back into sequence-command semantics before duration promotion
