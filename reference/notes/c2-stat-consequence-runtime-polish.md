# C2 Stat Consequence Runtime Polish

This note records the byte-neutral C2 battle consequence polish slice. It
promotes the selector map around `C2:B2E0`, where action payloads turn into
HP/PP feedback, direct stat increases, and affliction-recovery tails.

Primary source modules:

- `src/c2/c2_b2e0_dispatch_battle_stat_change_consequence.asm`
- `src/c2/c2_b342_apply_battle_hp_recovery_consequence.asm`
- `src/c2/c2_b360_apply_battle_pp_recovery_consequence.asm`
- `src/c2/c2_b3d8_apply_battle_iq_increase_consequence.asm`
- `src/c2/c2_b43f_apply_battle_guts_increase_consequence.asm`
- `src/c2/c2_b4a6_apply_battle_speed_increase_consequence.asm`
- `src/c2/c2_b50d_apply_battle_vitality_increase_consequence.asm`
- `src/c2/c2_b573_apply_battle_luck_increase_consequence.asm`

Related evidence notes:

- `notes/battle-action-stat-change-family-c2b2e0-b5d7.md`
- `notes/class2-post-selection-controller-phases.md`
- `notes/battle-affliction-recovery-family-c29aea-a39d.md`
- `notes/equipped-item-derived-cache-family-c21857-c21e03.md`

## Dispatcher Contract

`C2:B2E0` treats caller direct-page `$06/$08` as a pointer to a small
consequence record. Byte `+0` is the selector. Incoming A is copied to Y and
stored in `$16` as the amount or selector payload used by the case handlers.

Current promoted selector map:

| Selector | Runtime behavior |
| --- | --- |
| `0` | HP-side bounded feedback through `C2:7294` |
| `1` | PP-side bounded feedback through `C2:7318` |
| `2` | chained `C2:7294` then `C2:7318` |
| `3` | random choice among direct stat increases |
| `4` | IQ increase |
| `5` | guts increase |
| `6` | speed increase |
| `7` | vitality increase |
| `8` | luck increase |
| `9` | narrow affliction recovery through `C2:9AEA` |
| `0x0A` | poison-only item-side recovery through `C2:A39D` |

The common epilogue restores the caller pointer and may dispatch a trailing
control byte at record offset `+3` through `C0:76C8`.

Source follow-up: the `C2:B573..B6EB` source now names selector `9` as
`TryRecoverSelectedBattlerNarrowAffliction`, selector `0x0A` as
`TryRecoverSelectedBattlerPoisonOnly`, and the epilogue's optional `+3` byte
handoff as `DispatchBattleConsequenceControlByte`. The C0 helper name remains
local to this consequence-record contract until its wider bank-C0 role is
promoted from its own callers.

Return-tail follow-up: `C2:B606` is now exposed as
`ReturnFromBattleStatChangeConsequence`. The late condiment/odor no-effect
route jumps there when it wants the shared `pld/rtl` return without entering
the optional `C2:B5E3` control-byte epilogue.

Selector-dispatch follow-up: `C2:B2E0` now jumps to each explicit jump selector
leaf by behavioral contract instead of raw local addresses. Selector `2` is
`ApplyBattleHpPpRecoveryConsequence`, selector `3` is
`PickRandomBattleStatIncreaseConsequence`, selectors `4..8` target the named
direct stat leaves, selectors `9/0x0A` target the named affliction-recovery
consequence tails, and the default case lands on the shared
`RunBattleStatChangeConsequenceEpilogue`.

## HP/PP Feedback Selectors

Selectors `0` and `1` reuse the selected-row feedback helpers documented in the
post-selection controller notes.

- selector `0` maps the incoming amount to the X payload expected by `C2:7294`
  and applies it to active row `$A972`
- selector `1` maps the incoming amount to the X payload expected by `C2:7318`
  and applies it to active row `$A972`
- selector `2` applies both helpers in order

When the amount is zero, the wrapper passes fixed fallback payload `0x7530`.
Otherwise it maps the incoming amount through `C2:6AFD` /
`ApplyTwentyFivePercentVariance` before handing X to the HP/PP feedback helper.

The source leaves now name those joins directly: selector `0` calls
`ApplyBattlerHpRecoveryFeedback`, selector `1` calls
`ApplyBattlerPpRecoveryFeedback`, and selector `2` chains both after the same
variance-shaped amount setup.

The selector `2` continuation inside `C2:B360` is now locally labeled as
`ApplyBattleHpPpRecoveryConsequence`, matching the dispatcher map and making
the HP-then-PP pairing explicit at both entry points.

## Direct Stat Increase Selectors

Selectors `4..8` share a strong row-local plus live-character mirror pattern:

1. add amount `$16` into one active selected-row byte at `$A972`
2. add the same amount into a live character stat-byte in the `0x5F`-stride
   character row
3. run the corresponding derived-stat refresh helper
4. emit an amount-bearing C8 battle text through `C1:DC66`

| Selector | Stat | Active row byte | Live byte | Refresh helper | Text |
| --- | --- | --- | --- | --- | --- |
| `4` | IQ | `+0x31` | `$9A28` | `C2:1D7D` | `C8:F7B8` |
| `5` | guts | `+0x2C` | `$9A26` | `C2:1BA4` | `C8:F7D2` |
| `6` | speed | `+0x2A` | `$9A25` | `C2:1AEB` | `C8:F82F` |
| `7` | vitality | `+0x30` | `$9A27` | `C2:1D65` | `C8:F84C` |
| `8` | luck | `+0x2E` | `$9A29` | `C2:1C5D` | `C8:F86B` |

This is a concrete runtime bridge between battle action consequences and the
same live derived-stat family used by equipment and level-up paths.

Selector `3` is now labeled as `PickRandomBattleStatIncreaseConsequence`; its
random branches jump to the named guts, speed, vitality, and luck leaves, while
the zero branch continues to the adjacent IQ leaf.

Source-promotion status:

- `src/c2/c2_b3d8_apply_battle_iq_increase_consequence.asm`,
  `src/c2/c2_b43f_apply_battle_guts_increase_consequence.asm`,
  `src/c2/c2_b4a6_apply_battle_speed_increase_consequence.asm`,
  `src/c2/c2_b50d_apply_battle_vitality_increase_consequence.asm`, and
  `src/c2/c2_b573_apply_battle_luck_increase_consequence.asm` now carry local
  aliases for the selected-row stat byte, live character mirror byte, `0x5F`
  character stride, derived-stat refresh helper, C8 amount script, C8 script
  bank, and `C1:DC66` substitution-payload call.
- `src/c2/c2_a056_run_resist_checked_strange_status_action.asm` now uses the
  same C8 amount-script and selected-row stat-byte names for the 1d4 stat-up
  actions and random stat-up offense/defense branches.
- The direct stat leaves and the HP/PP wrapper leaves now target the shared
  `C2:B5E3` tail as `RunBattleStatChangeConsequenceEpilogue`.

## Affliction-Recovery Tails

Selectors `9` and `0x0A` are now documented as tails into the affliction
recovery family:

- `9 -> C2:9AEA`: narrow recovery for cold, sunstroke, and asleep-style status
- `0x0A -> C2:A39D`: poison-only item-side cure

Those helpers should keep their behavior-first names until the wider healing
action-table entries are promoted end to end.

## Decomp Value

This slice makes one more C2 action-payload surface useful:

- action payload selector bytes now have a source-commented dispatch contract
- selector-to-leaf jumps now use behavior names rather than raw addresses
- stat increases are tied to exact active-row fields, live character bytes,
  derived-stat refresh helpers, and amount-bearing battle text
- the affliction-recovery ladder is linked back to the consequence dispatcher

## Remaining Soft Spots

- final gameplay names for selectors `0..2`
- exact ABI and field names for the caller-provided consequence record
- whether selector `9` should eventually be named as a specific Healing-tier
  action once the full `D5:7B68` action-table crosswalk is promoted
