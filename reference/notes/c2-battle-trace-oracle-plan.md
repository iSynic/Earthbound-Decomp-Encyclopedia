# C2 Battle Trace Oracle Plan

This note turns the C-port feedback intake into concrete Phase 2 proof lanes for
the C1/C2/EF battle runtime. It is intentionally proof-oriented: entries here
are not new behavior claims until they are backed by local source review,
trace/emulator captures, or generated manifest evidence.

Primary inputs:

- `notes/phase-2-semantic-closure-plan.md`
- `notes/c-port-feedback-intake.md`
- `notes/c2-battle-contract-workahead.md`
- `notes/c2-ef-battle-text-contract-workahead.md`
- focused C1/C2/class2 notes linked below

Generated companions:

- `manifests/c2-battle-trace-oracle-plan.json`
- `manifests/c2-battle-trace-oracle-packet.json`
- `manifests/c2-battle-trace-oracle-emulator-handoff.json`
- `manifests/c2-battle-trace-oracle-results-summary.json`
- `notes/c2-battle-trace-oracle-index.md`
- `notes/c2-battle-trace-oracle-packet.md`
- `notes/c2-battle-trace-oracle-emulator-handoff.md`
- `notes/c2-battle-trace-oracle-mesen-runner.md`
- `notes/c2-battle-trace-oracle-results-summary.md`
- `tools/build_c2_battle_trace_oracle_manifest.py`
- `tools/validate_c2_battle_trace_oracle_manifest.py`
- `tools/build_c2_battle_trace_oracle_packet.py`
- `tools/validate_c2_battle_trace_oracle_packet.py`
- `tools/build_c2_battle_trace_oracle_emulator_handoff.py`
- `tools/validate_c2_battle_trace_oracle_emulator_handoff.py`
- `tools/build_c2_battle_trace_oracle_runner_assets.py`
- `tools/validate_c2_battle_trace_oracle_runner_assets.py`
- `tools/build_c2_battle_trace_oracle_result_from_evidence.py`
- `tools/run_c2_battle_trace_oracle_mesen.py`
- `tools/validate_c2_battle_trace_local_fixtures.py`
- `tools/validate_c2_battle_trace_oracle_mesen_run_summary.py`
- `tools/summarize_c2_battle_trace_oracle_raw_trace.py`
- `tools/validate_c2_battle_trace_oracle_raw_trace_summary.py`
- `tools/probe_c2_battle_trace_save_states.py`
- `tools/validate_c2_battle_trace_save_state_probes.py`
- `tools/probe_c2_battle_fixture_scout.py`
- `tools/validate_c2_battle_fixture_scout.py`
- `tools/run_c2_battle_trace_oracle_batch.py`
- `tools/collect_c2_battle_trace_oracle_results.py`

## Proof Rules

- Treat C-port diary findings as high-value leads, not as source-facing proof.
- Promote a source comment/name only after the local checked-in ASM or a trace
  confirms the contract.
- Accept an `ok` result only when the validator sees non-stub harness
  provenance, exact packet job/trace paths, a non-empty trace, required proof
  capture fields, every packet job capture field, and observed addresses from
  the oracle address set.
- Keep gate, payload, writer, text, and presentation effects separated unless a
  single local routine truly owns all of them.
- Preserve numeric fields where the role is bounded but the user-facing label is
  not proven.

## Oracle Queue

| Oracle | Contract to prove | First observations | Promotion target |
| --- | --- | --- | --- |
| Target/action staging bridge | `C1:ADB4`, `C1:CE85`, and `C1:CFC6` produce stable selected action/target bytes for C2. | Capture C1 selection record fields, `C2:B930` candidate exports, target bytes `0x11`, `0x01`, and `0x12` as observed values. | Target/item notes, then cautious record-field aliases. |
| Current-action payload bridge | `C2:40A4` applies second-pointer/current-action payloads over the selected target domain. | Capture `$A96C/$A96E`, payload pointer, selected row pointer, and per-target loop state for curative, target-loss, food, and item-status leaves. | `class2-second-pointer-consumer-40a4.md` and action-dispatch comments. |
| Affliction writer matrix | `C2:724A` is a parameterized selected-row affliction/subgroup writer, while adjacent status writers such as concentration seal should stay separate when they do not call it. | For each caller, record selected row source, `X` subgroup slot, `Y` value, chance/resistance gate, and EF text pointer; for adjacent direct writers, record the target field/value instead. | Affliction crosswalk, status notes, and source-side caller comments. |
| Damage ABI boundary | `C2:8125` is the shared selected-target damage boundary, not the whole damage/result system. | Record amount input, target row, caller family, post-call HP roller/collapse path, and result text side effects. | Damage/status notes and C2 damage caller comments. |
| HP roller collapse boundary | Collapse finalization happens after HP roller settlement. | Capture damage staging, HP roller update, `C2:BB18`/`C2:BC5C` candidate cleanup, and collapse text/action timing. | Hit-resolution status note and collapse/affliction controller comments. |
| Resource amount pair | PSI Magnet transfers PP while PP reduction is loss-only. | Capture source PP, target PP, amount payload, result text payload, and recovery side effects. | PSI Magnet and late stat/resource notes. |
| Healing ladder | Gamma broad recovery and Omega full-HP revival are distinct wrappers around selected-row recovery/reset. | Capture recovery selector, selected row, HP/PP result, hard-state reset fields, and text branch. | Lifeup/healing and affliction-recovery notes. |
| Numeric/stat edge behavior | Late reducers and stat-up/down leaves have width/clamp details that matter for a C port. | Capture 16-bit amount math, clamp limits, random selector seed/output, and text payload. | Late stat/resource and offense/defense notes. |
| PSI Flash/status gates | Flash and resist-checked PSI status trio share compact host-gate shapes but distinct payload outcomes. | Capture gate result, resistance byte, `C2:724A` parameters, and selected EF result text. | PSI Flash/common notes and affliction writer matrix. |
| Battle-text payload join | C2 result routines feed EF/C1 text payloads with stable pointer and number-substitution contracts. | Capture `$0E/$10` text pointer, `$12/$14` payload pointer, `C1:DC1C`, `C1:DC66`, and EF row pointer. | `c2-ef-battle-text-contract-workahead.md`. |

## First Trace Pass

The first trace pass should stay narrow and reusable:

1. Run a target-selection case that exercises `C1:ADB4 -> C2:B930/BAC5`.
2. Run one `C2:40A4` payload case with a direct curative or item-side status.
3. Run one `C2:724A` status case, preferably Flash body numbness or
   solidification.
4. Run one `C2:8125` amount case, preferably a random-damage item or PSI common
   damage helper.
5. Run one resource case comparing PSI Magnet with PP reduction.

Each capture should record address, routine name, input fields, output fields,
and whether the observation confirms, refines, or contradicts the C-port diary
entry.

## Note Update Targets

Trace-confirmed findings should flow into these notes before source comments:

- `notes/battle-targetting-resolver-c1adb4-af50.md`
- `notes/battle-item-action-selection-c1ce85-c1cfc6.md`
- `notes/c2-target-selection-runtime-polish.md`
- `notes/class2-second-pointer-consumer-40a4.md`
- `notes/class2-affliction-apply-helper-724a.md`
- `notes/class2-battler-affliction-crosswalk.md`
- `notes/c2-hit-resolution-status-runtime-polish.md`
- `notes/c2-psi-common-runtime-polish.md`
- `notes/c2-psi-flash-runtime-polish.md`
- `notes/c2-lifeup-healing-runtime-polish.md`
- `notes/c2-late-stat-resource-runtime-polish.md`
- `notes/c2-ef-battle-text-contract-workahead.md`

## Ghidra Role

Ghidra-SNES may be used to visually inspect local control-flow shape around
these routines, but any observation should be recorded as a `ghidra_hint` until
local source or trace evidence confirms it. The trace-oracle queue should not
depend on Ghidra labels or inferred function boundaries.

## Refresh Commands

```powershell
python tools\build_c2_battle_trace_oracle_manifest.py
python tools\validate_c2_battle_trace_oracle_manifest.py
python tools\build_c2_battle_trace_oracle_packet.py
python tools\validate_c2_battle_trace_oracle_packet.py
python tools\build_c2_battle_trace_oracle_emulator_handoff.py
python tools\validate_c2_battle_trace_oracle_emulator_handoff.py
python tools\build_c2_battle_trace_oracle_runner_assets.py
python tools\validate_c2_battle_trace_oracle_runner_assets.py
python tools\run_c2_battle_trace_oracle_mesen.py --oracle-id c1_c2_target_action_staging --dry-run
python tools\probe_c2_battle_trace_save_states.py
python tools\validate_c2_battle_trace_save_state_probes.py
python tools\probe_c2_battle_fixture_scout.py
python tools\validate_c2_battle_fixture_scout.py
python tools\run_c2_battle_trace_oracle_batch.py --mode dry-run-stub --force
python tools\validate_c2_battle_trace_oracle_batch_summary.py
python tools\collect_c2_battle_trace_oracle_results.py
python tools\validate_c2_battle_trace_oracle_results_summary.py
```
