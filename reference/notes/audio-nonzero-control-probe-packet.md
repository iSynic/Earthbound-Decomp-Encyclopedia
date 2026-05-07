# Audio Nonzero Control Probe Packet

Status: nonzero-control probe jobs are packaged for external harness evidence; current playback/export behavior is preserved.

## Summary

- packet jobs: `7`
- blocker tracks: `155`
- source candidate records: `56`
- unique source candidate tracks: `10`
- blocker tracks without source candidate: `146`
- command jobs: `{'0xEF': 3, '0xFD': 1, '0xFE': 2, '0xFF': 1}`
- reader PC jobs: `{'0x0847': 2, '0x0957': 3, '0x0B8A': 1, '0x0D12': 1}`
- result files found: `0`
- valid results: `0`
- remaining blockers: `{'earthbound_variant_ff_effect': 1, 'ef_call_return_effect': 3, 'non_zero_control_semantics_pending': 7, 'timing_toggle_effect': 3}`
- accepted classifications: `['ef_call_return', 'timing_toggle', 'earthbound_variant_ff', 'unreachable', 'unresolved']`

## Phase Batches

| Phase | Jobs | Job IDs |
| --- | ---: | --- |
| `nonzero-0957-command-mix` | 3 | `['nonzero-probe-ff-pc-0957', 'nonzero-probe-ef-pc-0957', 'nonzero-probe-fe-pc-0957']` |
| `nonzero-reader-coverage` | 4 | `['nonzero-probe-ef-pc-0b8a', 'nonzero-probe-ef-pc-0d12', 'nonzero-probe-fd-pc-0847', 'nonzero-probe-fe-pc-0847']` |

## Probe Jobs

| Order | Job | Phase | Command | Reader PC | Kind | Source candidates | Result output |
| ---: | --- | --- | --- | --- | --- | ---: | --- |
| 1 | `nonzero-probe-ff-pc-0957` | `nonzero-0957-command-mix` | `0xFF` | `0x0957` | `static_walk_blocker` | 8 | `build/audio/nonzero-control-probe/nonzero-probe-ff-pc-0957/nonzero-control-proof-result.json` |
| 2 | `nonzero-probe-ef-pc-0957` | `nonzero-0957-command-mix` | `0xEF` | `0x0957` | `return_stack_context` | 8 | `build/audio/nonzero-control-probe/nonzero-probe-ef-pc-0957/nonzero-control-proof-result.json` |
| 3 | `nonzero-probe-fe-pc-0957` | `nonzero-0957-command-mix` | `0xFE` | `0x0957` | `timing_toggle_context` | 8 | `build/audio/nonzero-control-probe/nonzero-probe-fe-pc-0957/nonzero-control-proof-result.json` |
| 4 | `nonzero-probe-ef-pc-0b8a` | `nonzero-reader-coverage` | `0xEF` | `0x0B8A` | `return_stack_context` | 8 | `build/audio/nonzero-control-probe/nonzero-probe-ef-pc-0b8a/nonzero-control-proof-result.json` |
| 5 | `nonzero-probe-ef-pc-0d12` | `nonzero-reader-coverage` | `0xEF` | `0x0D12` | `return_stack_context` | 8 | `build/audio/nonzero-control-probe/nonzero-probe-ef-pc-0d12/nonzero-control-proof-result.json` |
| 6 | `nonzero-probe-fd-pc-0847` | `nonzero-reader-coverage` | `0xFD` | `0x0847` | `timing_toggle_context` | 8 | `build/audio/nonzero-control-probe/nonzero-probe-fd-pc-0847/nonzero-control-proof-result.json` |
| 7 | `nonzero-probe-fe-pc-0847` | `nonzero-reader-coverage` | `0xFE` | `0x0847` | `timing_toggle_context` | 8 | `build/audio/nonzero-control-probe/nonzero-probe-fe-pc-0847/nonzero-control-proof-result.json` |

## Validation After External Results

- `python tools/validate_audio_nonzero_control_probe_packet.py`
- `python tools/run_audio_probe_campaign.py --lane nonzero --mode dry-run-stub --force`
- `python tools/validate_audio_probe_campaign_run_summary.py`
- `python tools/run_audio_probe_campaign.py --lane nonzero --mode stub-shape --force`
- `python tools/validate_audio_probe_campaign_run_summary.py`
- `python tools/collect_audio_nonzero_control_probe_results.py`
- `python tools/validate_audio_nonzero_control_probe_results_summary.py`
- `python tools/build_audio_sequence_semantics_intake_plan.py`
- `python tools/validate_audio_sequence_semantics_intake_plan.py`
- `python tools/validate_audio_duration_uncertainty_register.py`
- `python tools/validate_audio_nonzero_control_coverage_report.py`
- `python tools/build_audio_duration_readiness_rollup.py`
- `python tools/validate_audio_duration_readiness_rollup.py`

## Probe Packet Policy

- This packet is an operator checklist for external nonzero-control harness evidence; it does not run a real harness.
- Generated traces, results, SPCs, WAVs, and evidence markdown must stay under ignored build/audio paths.
- Dry-run and stub-shape commands prove runner/result schema only; they do not resolve sequence semantics.
- Only validated external results with accepted control-effect classifications may feed sequence semantics intake.
- This packet cannot directly promote sequence commands, public exact durations, or release-quality playback claims.

## Remaining Uncertainty

- All seven nonzero-control probe jobs still need external harness results before sequence semantics can change.
- The representative source-candidate set covers ten tracks, while 146 primary nonzero blockers still lack a direct source candidate.
- Sequence promotion and public exact-duration promotion remain blocked after packet generation.
