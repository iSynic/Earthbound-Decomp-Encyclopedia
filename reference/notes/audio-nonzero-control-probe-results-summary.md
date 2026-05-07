# Audio Nonzero Control Probe Results Summary

Status: no public export behavior changes; probe outputs are collected only when local ignored result files exist.

## Summary

- probe jobs: `7`
- result files found: `0`
- valid results: `0`
- statuses: `{'pending': 7}`
- validation: `{'invalid_or_pending': 7}`
- classifications: `{'pending': 7}`
- command jobs: `{'0xEF': 3, '0xFD': 1, '0xFE': 2, '0xFF': 1}`
- remaining blockers: `{'earthbound_variant_ff_effect': 1, 'ef_call_return_effect': 3, 'non_zero_control_semantics_pending': 7, 'timing_toggle_effect': 3}`
- resolved control-effect jobs: `[]`
- sequence promotion allowed: `False`

## Acceptance Policy

- A result can resolve one command/reader-PC job only when it validates and classifies the effect as ef_call_return, timing_toggle, earthbound_variant_ff, or unreachable.
- EF, FD/FE, and FF classifications are command-family specific; a valid result cannot use a classification from the wrong family.
- This summary cannot directly promote public exact-duration exports.
- Validated command effects must be consumed by audio-sequence-command-semantics before exact-duration policy can change.

## Results

| Job | Command | Reader PC | Status | Valid | Classification | Remaining blockers | Result path |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nonzero-probe-ff-pc-0957` | `0xFF` | `0x0957` | `pending` | `False` | `pending` | `['non_zero_control_semantics_pending', 'earthbound_variant_ff_effect']` | `build/audio/nonzero-control-probe/nonzero-probe-ff-pc-0957/nonzero-control-proof-result.json` |
| `nonzero-probe-ef-pc-0957` | `0xEF` | `0x0957` | `pending` | `False` | `pending` | `['non_zero_control_semantics_pending', 'ef_call_return_effect']` | `build/audio/nonzero-control-probe/nonzero-probe-ef-pc-0957/nonzero-control-proof-result.json` |
| `nonzero-probe-fe-pc-0957` | `0xFE` | `0x0957` | `pending` | `False` | `pending` | `['non_zero_control_semantics_pending', 'timing_toggle_effect']` | `build/audio/nonzero-control-probe/nonzero-probe-fe-pc-0957/nonzero-control-proof-result.json` |
| `nonzero-probe-ef-pc-0b8a` | `0xEF` | `0x0B8A` | `pending` | `False` | `pending` | `['non_zero_control_semantics_pending', 'ef_call_return_effect']` | `build/audio/nonzero-control-probe/nonzero-probe-ef-pc-0b8a/nonzero-control-proof-result.json` |
| `nonzero-probe-ef-pc-0d12` | `0xEF` | `0x0D12` | `pending` | `False` | `pending` | `['non_zero_control_semantics_pending', 'ef_call_return_effect']` | `build/audio/nonzero-control-probe/nonzero-probe-ef-pc-0d12/nonzero-control-proof-result.json` |
| `nonzero-probe-fd-pc-0847` | `0xFD` | `0x0847` | `pending` | `False` | `pending` | `['non_zero_control_semantics_pending', 'timing_toggle_effect']` | `build/audio/nonzero-control-probe/nonzero-probe-fd-pc-0847/nonzero-control-proof-result.json` |
| `nonzero-probe-fe-pc-0847` | `0xFE` | `0x0847` | `pending` | `False` | `pending` | `['non_zero_control_semantics_pending', 'timing_toggle_effect']` | `build/audio/nonzero-control-probe/nonzero-probe-fe-pc-0847/nonzero-control-proof-result.json` |

## Next Work

- run the 0x0957 FF/FE/EF jobs first because that reader PC covers the highest-value command mix
- review invalid or unresolved probe outputs before changing sequence command semantics
- feed only validated control-effect classifications back into audio-sequence-command-semantics
