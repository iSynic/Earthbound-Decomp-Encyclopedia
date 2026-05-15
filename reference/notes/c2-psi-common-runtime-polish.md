# C2 PSI Common Runtime Polish

This note records the byte-neutral C2 PSI common-helper polish slice. It promotes
the local runtime contracts for the shared early PSI helpers, the common
timed-substate blocker/cleanup pair, and the Thunder reflection tail.

Primary source modules:

- `src/c2/c2_941d_check_selected_battler_timed_substate_blocker.asm`
- `src/c2/c2_94ce_tick_selected_battler_timed_substate_cleanup.asm`
- `src/c2/c2_9516_run_psi_rockin_common.asm`
- `src/c2/c2_957a_run_psi_fire_common.asm`
- `src/c2/c2_95cf_run_psi_freeze_common.asm`
- `src/c2/c2_966b_run_psi_thunder_common.asm`
- `src/c2/c2_97a5_handle_psi_thunder_franklin_badge_reflection.asm`
- `src/c2/c2_9a80_run_psi_starstorm_common.asm`

Related evidence notes:

- `notes/class2-psi-action-wrapper-local-verification.md`
- `notes/class2-psi-common-helper-candidates.md`
- `notes/class2-psi-thunder-common-local-flow.md`
- `notes/class2-psi-thunder-reflection-branch.md`
- `notes/class2-psi-shield-post-hit-aa96.md`
- `notes/class2-d57b68-battle-action-table-match.md`

## Shared PSI Blocker And Cleanup

`C2:941D` and `C2:94CE` form the shared pre-hit and post-hit pair used by the
early PSI common helpers.

`C2:941D`:

- sets `PendingTimedSubstateMessageFlag` (`$AA94`) to `1`
- stages the selected action argument byte (`+0x08`) through `C1:DD7C` for EF
  scripts that consume the byte-substitution slot
- reads the active `D5:7B68` action descriptor type byte at row `+0x02`
- only `BattleActionTypePsi` (`3`) enters timed-substate handling
- target-row `TimedSubstatePsychicPowerShield` (`+0x23 == 1`) emits `EF:70D2`
  (`MsgBtlPsychicPowerShieldReflectsPsiName`), sets `$AA96 = 1`, and swaps
  attacker/target text contexts
- target-row `TimedSubstatePsychicShield` (`+0x23 == 2`) emits `EF:70FA`
  (`MsgBtlPsychicShieldNullifiesPsiName`), decrements row `+0x25`, and when
  the counter expires clears `+0x23` and emits `EF:7099`
  (`MsgBtlShieldExpired`)

`EF:70D2` and `EF:70FA` both consume the pending byte substitution as a PSI
name before printing the shield reflection/nullification text.

`C2:94CE`:

- clears `$AA94`
- if `$AA96` is set, swaps attacker/target text contexts back
- decrements selected-row `+0x25`
- clears selected-row `+0x23` and emits `EF:7099`
  (`MsgBtlShieldExpired`) when the counter expires
- clears `$AA96`

The promoted model is that `$AA96` is the reflected-hit or delayed cleanup
marker shared by PSI shield/timed-substate handling and Thunder reflection.

Implementation update: `src/c2/c2_941d_check_selected_battler_timed_substate_blocker.asm`
now names the selected/target row pointers, `D5:7B68` table root, action row
type offset, PSI action type constant, timed-substate byte, timed-substate turn
byte, and `$AA94/$AA96` transient flags directly in source.

The physical-hit path in
`src/c2/c2_7eaf_run_hit_resolution_and_status_action_cluster.asm` uses the
parallel row `+0x23 == 3/4` shield family: substate `3` emits `EF:70B1`
(`MsgBtlPowerShieldReflectsAttack`) and reflects damage through the same
attacker/target context swap helper, while both `3` and `4` share row `+0x25`
countdown and `EF:7099` shield-expired cleanup.

## One-Parameter PSI Helpers

Rockin, Fire, Freeze, and Starstorm each have wrapper families that pass a
single damage-like value in A to a shared helper.

| Helper | Wrapper family | Core local behavior |
| --- | --- | --- |
| `C2:9516` | Rockin | blocker, random amount via `C2:6A44` / `RollRandomAmount`, physical avoidance via `C2:84AD`, `EF:766E` on avoidance, type `0xFF` damage |
| `C2:957A` | Fire | blocker, amount via `C2:6AFD` / `ApplyTwentyFivePercentVariance`, selected-row `+0x3A` damage selector, damage apply |
| `C2:95CF` | Freeze | default-target/NPC blocker, PSI blocker, amount via `C2:6AFD` / `ApplyTwentyFivePercentVariance`, selected-row `+0x38` damage selector, chance-based subgroup status side effect, `EF:6BEF` on side-effect success |
| `C2:9A80` | Starstorm | blocker, amount via `C2:6AFD` / `ApplyTwentyFivePercentVariance`, type `0xFF` damage |

All four finish successful action bodies through `C2:94CE`.

The Fire and Freeze row-byte selectors are intentionally documented as
damage-selector fields rather than final resistance names until more non-PSI
readers are joined.

Source-vocabulary update: all one-parameter PSI damage helpers now call
`C2:8125` by its selected-target damage role,
`ApplyDamageToSelectedTarget`. A is the staged damage amount; X carries the
damage/resistance selector, with `0xFF` used by default-damage callers.
The adjacent amount-shaping helpers are now split by observed ABI:
`C2:6A44` is `RollRandomAmount`, while the Fire/Freeze/Starstorm variance path
uses `C2:6AFD` / `ApplyTwentyFivePercentVariance`.

## Thunder Common

`C2:966B` is the two-parameter PSI helper. Its wrappers pass:

| Rank wrapper | X | A |
| --- | --- | --- |
| `C2:9871` | `1` | `0x0078` |
| `C2:987D` | `2` | `0x0078` |
| `C2:9889` | `3` | `0x00C8` |
| `C2:9895` | `4` | `0x00C8` |

Source follow-up: the wrapper bodies are now labeled as
`RunPsiThunderAlpha/Beta/Gamma/Omega` and call `C2:966B` by the shared
`RunPsiThunderCommon` contract. The cross-module loop edges are also named:
`C2:96CB` is the next-strike entry, `C2:9821` is the miss presentation tail,
`C2:985A` is the requested-hit-count continuation gate, and `C2:9863` clears
the target mask before returning.

Promoted local flow:

- count active bits in the current 32-entry target mask
- derive `min(active_count * 64, 255)`
- preserve the original target mask for each strike
- restore and filter the mask before each strike
- choose one surviving target and map it into selected row `$A972`
- rebuild target text context
- use the clamped active-count value as the strike success threshold through
  `C2:6BB8` / `RollActionChanceGate`
- emit `EF:8814` for the small Thunder presentation or `EF:8823` for the large
  Thunder presentation
- wait on `C2:EACF` until the presentation is no longer busy
- continue into the post-strike tail at `C2:97A5`

That makes Thunder the strongest local PSI common helper because its wrapper
signature and multi-hit target-mask loop are both locally visible.

## Thunder Reflection Tail

`C2:97A5` completes Thunder's per-strike resolution.

Promoted local flow:

- clear selected-row marker `+0x4B`
- if selected-row `+0x0E == 0`, check `C4:5683` for row `+0x10 + 1` using
  search slot `X = 1`
- on success, emit `EF:7160` (`MsgBtlFranklinBadgeReflectsThunder`), set
  `$AA96 = 1`, and swap attacker/target contexts
- timed substates `+0x23 == 1/2` refresh row `+0x25 = 1`
- run the shared PSI blocker/damage/cleanup path
- miss path emits `EF:8837` and `C8:FAF6`
- loop while both side counts remain nonzero and the requested hit count has not
  been reached
- clear `$A96C/$A96E` before returning

The reflection wording remains reference-backed, but the local structure is now
strong enough to keep the helper name and source comments: possession check,
reflection text, `$AA96`, and context swap all line up.

## Decomp Value

This slice turns the early PSI families from wrapper-name candidates into
runtime-helpful action helpers:

- wrapper parameters are source-commented at the shared helper boundary
- shared blocker/cleanup effects are tied to `$AA94`, `$AA96`, `+0x23`, and
  `+0x25`
- Fire and Freeze now identify their selected-row damage selector bytes
- Thunder has a documented target-mask loop, per-strike selection, presentation
  branch, reflection tail, and loop termination shape
- Thunder wrapper and loop-tail labels now keep the common helper, miss path,
  continuation gate, and cleanup return readable without raw local jumps

## Phase 2 Trace-Oracles

The PSI damage commons are Phase 2 damage-spine probes. Rockin, Fire, Freeze,
Starstorm, and Thunder should be traced at the point they prepare an amount,
choose the selector byte or default `0xFF`, and cross `C2:8125` /
`ApplyDamageToSelectedTarget`. The trace should not collapse element gates,
shield/timed-substate blockers, Franklin Badge reflection, amount shaping, and
post-hit cleanup into the damage ABI itself.

Diary-backed PSI status and Flash comparisons belong in the adjacent status
gate lane until locally proven. For this note, the useful closure target is the
common damage spine: the one-parameter helpers and Thunder's per-strike tail
should all expose the same selected-target damage boundary while preserving
their distinct target-mask and presentation behavior.

## Remaining Soft Spots

- final names for selected-row `+0x38/+0x3A` beyond damage-selector wording
- exact symbolic name for descriptor type `3` in `D5:7B68`
- deeper helper-body promotion for the damage/resistance helper stack beneath
  the now-named `C2:8125` selected-target damage ABI
- global promotion of the reflection item identity should wait until item table
  evidence is joined locally
