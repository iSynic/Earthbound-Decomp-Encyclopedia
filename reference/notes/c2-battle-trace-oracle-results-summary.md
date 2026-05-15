# C2 Battle Trace Oracle Results Summary

Status: no source or behavior promotion. Local results are collected
only when ignored `build/c2/battle-trace-oracles/` result files exist.

## Summary

- jobs: `10`
- result files found: `10`
- valid results: `10`
- trace-observed results: `6`
- proof-grade results: `2`
- stub results: `4`
- proof-capable results: `6`
- statuses: `{'ok': 6, 'unsupported': 4}`
- validation: `{'valid': 10}`
- classifications: `{'needs_followup': 4, 'refined_contract': 2, 'unresolved': 4}`
- remaining blockers: `{'followup_review': 4, 'not_first_trace_pass': 4, 'oracle_contract_unresolved': 4, 'runtime_trace_proof': 4}`
- source promotion allowed: `False`
- behavior change allowed: `False`

## Acceptance Policy

- Stub unsupported/unresolved results validate runner plumbing only and never count as trace-observed evidence.
- A result counts as trace-observed only when it validates, is non-stub, is status ok, has a non-empty trace, matches packet job/trace paths, includes every packet capture field, and classifies the contract as confirmed_contract, refined_contract, contradicted_plan, or needs_followup.
- A result counts as proof-grade only when it satisfies the trace-observed gate and classifies the contract as confirmed_contract, refined_contract, or contradicted_plan.
- Contradicted results require manual review before any source-facing promotion.
- This summary cannot directly promote source names, source comments, C-port helper contracts, or behavior changes.

## Results

| Oracle | Priority | First pass | Status | Valid | Stub | Proof capable | Classification | Remaining blockers | Result path |
| --- | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| `c1_c2_target_action_staging` | `1` | `True` | `ok` | `True` | `False` | `True` | `needs_followup` | `['followup_review']` | `build/c2/battle-trace-oracles/c1_c2_target_action_staging/result.json` |
| `c2_40a4_current_action_payload` | `1` | `True` | `ok` | `True` | `False` | `True` | `needs_followup` | `['followup_review']` | `build/c2/battle-trace-oracles/c2_40a4_current_action_payload/result.json` |
| `c2_724a_affliction_writer_matrix` | `1` | `True` | `ok` | `True` | `False` | `True` | `needs_followup` | `['followup_review']` | `build/c2/battle-trace-oracles/c2_724a_affliction_writer_matrix/result.json` |
| `c2_8125_damage_abi_boundary` | `1` | `True` | `ok` | `True` | `False` | `True` | `refined_contract` | `[]` | `build/c2/battle-trace-oracles/c2_8125_damage_abi_boundary/result.json` |
| `hp_roller_collapse_boundary` | `2` | `True` | `ok` | `True` | `False` | `True` | `refined_contract` | `[]` | `build/c2/battle-trace-oracles/hp_roller_collapse_boundary/result.json` |
| `resource_amount_pair_magnet_vs_pp_loss` | `2` | `True` | `ok` | `True` | `False` | `True` | `needs_followup` | `['followup_review']` | `build/c2/battle-trace-oracles/resource_amount_pair_magnet_vs_pp_loss/result.json` |
| `battle_text_payload_join` | `2` | `False` | `unsupported` | `True` | `True` | `False` | `unresolved` | `['runtime_trace_proof', 'oracle_contract_unresolved', 'not_first_trace_pass']` | `build/c2/battle-trace-oracles/battle_text_payload_join/result.json` |
| `healing_ladder_gamma_omega` | `2` | `False` | `unsupported` | `True` | `True` | `False` | `unresolved` | `['runtime_trace_proof', 'oracle_contract_unresolved', 'not_first_trace_pass']` | `build/c2/battle-trace-oracles/healing_ladder_gamma_omega/result.json` |
| `psi_flash_and_status_gate_family` | `2` | `False` | `unsupported` | `True` | `True` | `False` | `unresolved` | `['runtime_trace_proof', 'oracle_contract_unresolved', 'not_first_trace_pass']` | `build/c2/battle-trace-oracles/psi_flash_and_status_gate_family/result.json` |
| `numeric_stat_edge_behavior` | `3` | `False` | `unsupported` | `True` | `True` | `False` | `unresolved` | `['runtime_trace_proof', 'oracle_contract_unresolved', 'not_first_trace_pass']` | `build/c2/battle-trace-oracles/numeric_stat_edge_behavior/result.json` |

## Next Work

- replace remaining stub results with real emulator or trace harness captures for the first-pass jobs
- review trace-observed needs_followup results in the owning C2 subsystem notes before touching source comments
- promote a result to proof-grade only after downstream text/collapse/status effects are decoded from trace evidence
- keep non-first-pass oracle jobs queued until the first-pass contracts stop moving
