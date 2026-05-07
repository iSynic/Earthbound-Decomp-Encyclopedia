# Audio Sequence Semantics Intake Plan

Status: probe results are mapped to candidate semantics evidence only; no export behavior changes.

## Summary

- current confirmed commands: `0`
- intake records: `26`
- zero intake records: `19`
- nonzero intake records: `7`
- accepted candidates: `0`
- command record counts: `{'0x00': 19, '0xEF': 3, '0xFD': 1, '0xFE': 2, '0xFF': 1}`
- statuses: `{'pending': 26}`
- classifications: `{'pending': 26}`
- sequence promotion allowed by intake: `False`

## Intake Policy

- Probe results can create candidate sequence-command evidence only after their individual result validators pass.
- A zero result is candidate evidence only for true_end, ef_return, or loop_or_hold_continues classifications.
- A nonzero result is candidate evidence only for ef_call_return, timing_toggle, earthbound_variant_ff, or unreachable classifications that match the command family validator.
- This intake plan cannot directly promote public exact-duration exports or edit audio-sequence-command-semantics.
- Candidate evidence must still be reviewed in a later semantics-promotion pass and then re-run export triage.

## Command State

| Command | Current semantic status | Records | Accepted | Intake state | Next action |
| --- | --- | ---: | ---: | --- | --- |
| `0x00` | `pending_earthbound_zero_control_effect_proof` | 19 | 0 | `probe_results_pending` | run and collect the relevant runtime probe jobs |
| `0xEF` | `runtime_interpreter_read_observed_dispatch_decode_pending` | 3 | 0 | `probe_results_pending` | run and collect the relevant runtime probe jobs |
| `0xFD` | `runtime_interpreter_read_observed_dispatch_decode_pending` | 1 | 0 | `probe_results_pending` | run and collect the relevant runtime probe jobs |
| `0xFE` | `runtime_interpreter_read_observed_dispatch_decode_pending` | 2 | 0 | `probe_results_pending` | run and collect the relevant runtime probe jobs |
| `0xFF` | `contradicted_by_stock_n_spc_pending_earthbound_variant_proof` | 1 | 0 | `probe_results_pending` | run and collect the relevant runtime probe jobs |

## Intake Records

| Command | Job | Status | Valid | Classification | Accepted | Remaining blockers |
| --- | --- | --- | --- | --- | --- | --- |
| `0x00` | `zero-probe-track-001-gas_station` | `pending` | `False` | `pending` | `False` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'active_preview_classification']` |
| `0x00` | `zero-probe-track-174-gas_station_2` | `pending` | `False` | `pending` | `False` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'finite_transition_review']` |
| `0x00` | `zero-probe-track-025-chaos_theatre` | `pending` | `False` | `pending` | `False` | `['zero_runtime_effect_proof', 'active_preview_classification']` |
| `0x00` | `zero-probe-track-032-giant_step` | `pending` | `False` | `pending` | `False` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'finite_transition_review']` |
| `0x00` | `zero-probe-track-033-lilliput_steps` | `pending` | `False` | `pending` | `False` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'finite_transition_review']` |
| `0x00` | `zero-probe-track-034-milky_well` | `pending` | `False` | `pending` | `False` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'finite_transition_review']` |
| `0x00` | `zero-probe-track-035-rainy_circle` | `pending` | `False` | `pending` | `False` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'finite_transition_review']` |
| `0x00` | `zero-probe-track-036-magnet_hill` | `pending` | `False` | `pending` | `False` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'finite_transition_review']` |
| `0x00` | `zero-probe-track-037-pink_cloud` | `pending` | `False` | `pending` | `False` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'finite_transition_review']` |
| `0x00` | `zero-probe-track-038-lumine_hall` | `pending` | `False` | `pending` | `False` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'finite_transition_review']` |
| `0x00` | `zero-probe-track-039-fire_spring` | `pending` | `False` | `pending` | `False` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'finite_transition_review']` |
| `0x00` | `zero-probe-track-085-bulldozer` | `pending` | `False` | `pending` | `False` | `['zero_runtime_effect_proof', 'active_preview_classification']` |
| `0x00` | `zero-probe-track-094-good_friends_bad_friends` | `pending` | `False` | `pending` | `False` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'active_preview_classification']` |
| `0x00` | `zero-probe-track-120-hotel_of_the_living_dead` | `pending` | `False` | `pending` | `False` | `['zero_runtime_effect_proof', 'active_preview_classification']` |
| `0x00` | `zero-probe-track-173-good_morning_moonside` | `pending` | `False` | `pending` | `False` | `['zero_runtime_effect_proof', 'loop_point_metadata']` |
| `0x00` | `zero-probe-track-143-leaving_magicant` | `pending` | `False` | `pending` | `False` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'active_preview_classification']` |
| `0x00` | `zero-probe-track-157-attract_mode` | `pending` | `False` | `pending` | `False` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'active_preview_classification']` |
| `0x00` | `zero-probe-track-171-winters_intro` | `pending` | `False` | `pending` | `False` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'loop_point_metadata']` |
| `0x00` | `zero-probe-track-175-title_screen` | `pending` | `False` | `pending` | `False` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'finite_transition_review']` |
| `0xFF` | `nonzero-probe-ff-pc-0957` | `pending` | `False` | `pending` | `False` | `['non_zero_control_semantics_pending', 'earthbound_variant_ff_effect']` |
| `0xEF` | `nonzero-probe-ef-pc-0957` | `pending` | `False` | `pending` | `False` | `['non_zero_control_semantics_pending', 'ef_call_return_effect']` |
| `0xFE` | `nonzero-probe-fe-pc-0957` | `pending` | `False` | `pending` | `False` | `['non_zero_control_semantics_pending', 'timing_toggle_effect']` |
| `0xEF` | `nonzero-probe-ef-pc-0b8a` | `pending` | `False` | `pending` | `False` | `['non_zero_control_semantics_pending', 'ef_call_return_effect']` |
| `0xEF` | `nonzero-probe-ef-pc-0d12` | `pending` | `False` | `pending` | `False` | `['non_zero_control_semantics_pending', 'ef_call_return_effect']` |
| `0xFD` | `nonzero-probe-fd-pc-0847` | `pending` | `False` | `pending` | `False` | `['non_zero_control_semantics_pending', 'timing_toggle_effect']` |
| `0xFE` | `nonzero-probe-fe-pc-0847` | `pending` | `False` | `pending` | `False` | `['non_zero_control_semantics_pending', 'timing_toggle_effect']` |

## Next Work

- run the 0x0957 FF/FE/EF nonzero jobs first, then re-collect nonzero control probe results
- run the highest-priority 0x00 finite/loop/active-preview jobs, then re-collect zero runtime probe results
- promote only validator-clean candidate evidence through a separate audio-sequence-command-semantics update
