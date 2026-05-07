# C2 PSI Flash Runtime Polish

This note records the byte-neutral C2 PSI Flash polish slice. It promotes the
Flash gate, the parameterized affliction writer, the three concrete status
branches, and the tier-specific random branch maps.

Primary source modules:

- `src/c2/c2_724a_apply_battler_affliction_subgroup_value.asm`
- `src/c2/c2_98a1_gate_selected_battler_for_random_status_action.asm`
- `src/c2/c2_98de_try_apply_strange_status_to_selected_battler.asm`
- `src/c2/c2_9917_try_apply_numb_status_to_selected_battler.asm`
- `src/c2/c2_9950_try_apply_crying_status_to_selected_battler.asm`
- `src/c2/c2_9987_run_psi_flash_alpha_action.asm`
- `src/c2/c2_99ae_run_psi_flash_beta_action.asm`
- `src/c2/c2_99ef_run_psi_flash_gamma_action.asm`
- `src/c2/c2_9a35_run_psi_flash_omega_action.asm`

Related evidence notes:

- `notes/class2-psi-flash-common-local-flow.md`
- `notes/class2-affliction-apply-helper-724a.md`
- `notes/class2-battler-affliction-crosswalk.md`
- `notes/c2-selected-row-controller-runtime-polish.md`
- `notes/c2-affliction-recovery-runtime-polish.md`

## Generic Affliction Writer

`C2:724A` is the small parameterized writer behind Flash status branches and the
Freeze side effect.

Source-vocabulary update: the helper is now exposed as
`ApplySelectedRowAfflictionSlotValue`, with the older
`ApplyBattlerAfflictionSubgroupValue` alias preserved for compatibility. The
Flash and Freeze callers now use the selected-row slot-writer name directly.

Runtime contract:

- A = selected-row base
- X = row-field offset relative to `+0x1D`
- Y = new affliction or subgroup value
- selected-row `+0x0F != 0` blocks the write
- target byte is `row + X + 0x1D`
- write succeeds only when the current byte is clear or lower/weaker than Y
- return value is `1` on write and `0` on blocked/no-upgrade

That contract explains the parameter pairs used by Flash:

| Helper | Y | X | Target byte | Outcome |
| --- | --- | --- | --- | --- |
| `C2:98DE` | `1` | `3` | `+0x20` | strange-style subgroup |
| `C2:9917` | `3` | `0` | `+0x1D` | numb/paralysis main affliction |
| `C2:9950` | `2` | `2` | `+0x1F` | crying subgroup |

Each branch emits its success text on a successful write and shared no-effect
text `EF:766E` on failure.

## Flash Gate

`C2:98A1` is the shared Flash-family gate:

- first runs the shared PSI blocker `C2:941D`
- if that blocker returns nonzero, returns `0`
- otherwise tests selected-row byte `+0x39` through `C2:6BB8` /
  `RollActionChanceGate`
- returns `1` on pass
- emits `EF:766E` and returns `0` on failure

The Flash tier wrappers therefore only enter their random branch maps after both
the default target/NPC gate and this selected-row gate pass.

## Tier Branch Maps

All four Flash tiers sample `C0:8E9A & 7`.

| Tier | Random values | Outcome |
| --- | --- | --- |
| Alpha `C2:9987` | `0` | strange |
| Alpha `C2:9987` | `1..7` | crying |
| Beta `C2:99AE` | `0` | collapse startup through `C2:7550` |
| Beta `C2:99AE` | `1` | numb/paralysis |
| Beta `C2:99AE` | `2` | strange |
| Beta `C2:99AE` | `3..7` | crying |
| Gamma `C2:99EF` | `0..1` | collapse startup through `C2:7550` |
| Gamma `C2:99EF` | `2` | numb/paralysis |
| Gamma `C2:99EF` | `3` | strange |
| Gamma `C2:99EF` | `4..7` | crying |
| Omega `C2:9A35` | `0..2` | collapse startup through `C2:7550` |
| Omega `C2:9A35` | `3` | numb/paralysis |
| Omega `C2:9A35` | `4` | strange |
| Omega `C2:9A35` | `5..7` | crying |

Every tier finishes through the shared PSI cleanup helper `C2:94CE`.

## Decomp Value

This slice ties Flash into the selected-row contracts established by the
previous C2 passes:

- Flash collapse outcomes now point directly at the documented `C2:7550`
  startup path
- the strange, numb, and crying branches are all exact parameterizations of
  `C2:724A`
- status branch success/failure text is explicit at the helper boundary
- tier differences are represented as branch maps rather than vague difficulty
  labels

## Remaining Soft Spots

- final user-facing wording for the `C2:7550` collapse outcome should stay broad
  until more non-Flash callers are joined
- selected-row `+0x39` is still best described as the Flash-family gate byte
  rather than a final resistance/immunity field name
- global enum promotion for `+0x1F/+0x20` subgroup bytes should wait for a wider
  reader pass
