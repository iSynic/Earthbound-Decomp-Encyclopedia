# C2 Hit-Resolution And Status-Action Runtime Polish

Primary queue context: `notes/c2-runtime-semantic-polish-plan.md`,
`notes/c2-ef-battle-text-contract-workahead.md`,
`notes/source-readiness-triage.md`, and `notes/project-status.md`.

## Scope

This pass covers the large `C2:7EAF..8BBE` hit-resolution and late
status-action cluster in
`src/c2/c2_7eaf_run_hit_resolution_and_status_action_cluster.asm`.
The edit is semantic source polish only: it promotes local aliases and
message constants without changing runtime bytes.

## Promoted Contracts

- C1 battle-text ABIs:
  - `C1:DC1C` as direct `$0E/$10` battle-text pointer display.
  - `C1:DC66` as substitution-payload display for damage/stat amount text.
  - `C1:DD7C` as the byte-substitution bridge used by the Spy present script.
- C2 helper ABIs:
  - `C2:3D05` target text-context rebuild.
  - `C2:69F8`, `C2:698B`, `C2:69BE`, `C2:6AFD`, `C2:6BB8`, and
    `C2:6BDB` as shared math/probability/helper joins. `C2:69BE` is now called
    by its counted-frame wait role, `WaitFrames`. `C2:6AFD` is now
    called by its amount-shaping role:
    `ApplyTwentyFivePercentVariance`. `C2:6BB8` is now called by its generic
    action chance-gate role: `RollActionChanceGate`.
  - `C2:6EF8` as the mask-set first-match finder used when the reflected or
    retargeted hit path needs to select a surviving target from the current
    working mask.
  - `C2:7126`, `C2:71F0`, `C2:724A`, `C2:7550`, `C2:7C96`,
    `C2:7CFD`, and `C2:7E8A` as HP/status/default-text/reflection helpers.
    `C2:7126` is now called as `SetBattlerHpTarget`, `C2:71F0` as
    `ReduceBattlerHpTarget`, and `C2:7550` as
    `StartSelectedBattlerCollapseAfflictionPath`.
    `C2:7CFD` is called as `CheckSelectedBattlerDefaultTextBlocker`, and
    `C2:7C96` is called as `RollSelectedRowThresholdGate`.
    `C2:724A` is now called by its selected-row slot writer role:
    `ApplySelectedRowAfflictionSlotValue`.
  - `C2:8125` as the selected-target damage ABI now called by its
    `ApplyDamageToSelectedTarget` role. A is the staged damage amount, while X
    is the damage/resistance selector (`0xFF` for default damage callers).
- EF battle-text scripts for damage, miss/dodge, SMAAAASH, Spy readouts,
  Time Stop return, no-effect fallback, and late primary-status success text.
- The shield/timed-substate join now uses the EF payload names from the
  `EF:7099..70B1` split: `EF:70B1` is the power-shield physical reflection
  text and `EF:7099` is the shared shield-expired text.

## Spy Readout Payloads

The `BTLACT_SPY` readout now names the target battler fields it samples:

- `+0x26/+0x28` are offense and defense words. Spy stages each current value
  through `C1:DC66`, so the EF scripts at `EF:69EA` and `EF:69FF` consume the
  value as a `1C 0F` amount payload.
- `+0x3A/+0x38/+0x39/+0x37` are fire, freeze, flash, and paralysis
  resistance bytes. The readout emits the matching vulnerability text only
  when the byte is `0xFF`.
- `+0x3C/+0x3B` are hypnosis and brainshock resistance bytes. These drive the
  two Brainshock/Sleep-friendly readout scripts at `EF:6A6C` and `EF:6A7F`.
- The final Check Present branch then reuses `BattlePresentItemByte` as
  described below.

## Shield Reflection Tail

The physical-hit shield branch reads selected row `+0x23` as the active timed
substate id:

- `3` = power shield; reflect the physical hit, emit `EF:70B1`, swap
  attacker/target text contexts through `C2:7E8A`, and apply reflected damage.
- `4` = shield; skip reflection but share the `+0x25` countdown path.
- when row `+0x25` expires, clear row `+0x23` and emit `EF:7099`.

The SMAAAASH path refreshes row `+0x25 = 1` for substates `3` and `4` before
entering the `ApplyDamageToSelectedTarget` path.

## Status Tails

The late action labels now match the action bodies and EF evidence:

- `BTLACT_DIAMONDIZE` / `C289CE_RunDiamondizeStatusAction`
- `BTLACT_PARALYZE` / `C28A92_RunParalyzeStatusAction`
- `BTLACT_NAUSEATE` / `C28AEB_RunNauseateStatusAction`
- `BTLACT_POISON` / `C28B2C_RunPoisonStatusAction`
- `BTLACT_COLD` / `C28B6D_RunColdStatusAction`

These bodies all feed `C2:724A` with primary status-group constants and then
emit the corresponding EF success script or `EF:766E` no-effect fallback.
The source now calls the named selected-row slot writer directly at each tail.

## Check Present Byte Slot

The `C2:8881` Check Present / Spy tail now names the same
`BattlePresentItemByte` (`$AA10`) slot used by the battle-start present path:

- if the selected target exposes a present byte and the fixed Check Present
  recipient id `3` has inventory room through `C4:572B`, C2 stages the item
  byte through `C1:DD7C` into `$9D11`;
- `EF:7DD5` (`MSG_BTL_CHECK_PRESENT_GET`) consumes it through `0x19 0x1F`
  before printing the item name;
- C2 clears `BattlePresentItemByte` after the preview text displays.

This keeps the Check Present branch tied to the C1/EF byte-substitution
contract and the C4 inventory-room predicate rather than treating `$AA10` as a
generic battle-start scratch byte.

## Follow-Up Mask Join

The retargeting tail now calls the named `C2:6EF8`
`MaskSet_FindFirstMatchInRange` helper instead of a raw long address. That
keeps the hit-resolution cluster aligned with the standalone class-`2` mask
helper note and the A89D item/status payload lane.

Result-corridor follow-up: the Time Stop/retarget status tail now also names
the adjacent `C2:416F` / `FilterBattleActionTargetMaskByRowState` prune and
`C2:7029` / `MaskSet_TestBit` scan helpers. The local flow is now explicit:
prune the current target mask, pick the first surviving mask range, scan for
the selected bit, rebuild target text context, and invoke the bash payload.

Second result-corridor follow-up: the same Time Stop tail now brackets the
retarget loop with the EF audio flag helpers by name: `EF:0256` /
`PauseMusic` before the repeated bash applications and `EF:026E` /
`ResumeMusic` before the `EF:7843` return text. The physical-hit damage path
also names the shared `C0:925B` resistance-bit shifter at the defending and
shield/power-shield reduction sites, while the target-switch cue calls
`C0:ABE0` as the queued sound/effect dispatcher.

Special-event follow-up: `C2:92EE` now calls this cluster by its
`RunHitResolutionAndStatusActionCluster` contract when the Poo/Starstorm event
applies the scripted `0x0168` damage pass to each selected enemy row.

## Phase 2 Trace-Oracles

Damage/resource-lane closure should keep `C2:8125` as the selected-target
damage ABI boundary, not as a catch-all name for everything that happens after
damage is staged. Local source already supports the call ABI: A carries the
amount and X carries the damage/resistance selector, with `0xFF` used by
default-damage callers. Phase 2 traces should sample that boundary across plain
hit resolution, reflected hits, random-damage item leaves, bottle rockets,
bombs, HP-Sucker, and PSI common helpers.

The C-port feedback also makes collapse-after-HP-roller behavior a high-value
oracle. Until this workspace pins the timing locally, keep the diary wording as
a trace candidate: damage application, HP roller settlement, guts/survival
handling, collapse finalization, and EF result text should remain separate
contracts in notes and tests.

First local Mesen pass: the numbered multi-enemy fixture save
`EarthBound (USA)_5.mss` now produces a reviewed `refined_contract` result for
`c2_8125_damage_abi_boundary`. The trace reaches `C2:8125` five times and
corroborates the entry ABI: A carries the staged damage amount, X carries the
damage/resistance selector, entry Y is overwritten by `TXY`, caller DP is only
used to allocate the local frame, and `$A972` supplies the selected battler row.
The decoded row snapshots also show the source gates used by this helper:
`+0x0C` active/consciousness is `1`, primary affliction `+0x1D` is clear, timed
substate `+0x23` is clear, shield countdown `+0x25` is clear, and later selected
row samples show HP live/target mutation after the damage helper. The expanded
runner also captures the downstream C1/EF amount-text lane: damage entries reach
`C1:DC66`, stage EF scripts such as `EF:75C2`, `EF:75D9`, and `EF:7607` in
caller `$0E/$10`, commit the amount payload through `C1:AD0A` into
`$9D12/$9D14`, consume it through the `C1:7EED` `1C 0F` action-amount command,
read it with `C1:AD26`, and enter the C1 number printer at `C1:0DF6`. Direct
result text through `C1:DC1C` is also observed for adjacent miss/SMAAAASH
branches such as `EF:7630` and `EF:7655`. This promotes the ABI, selected-row
HP mutation, and C1/EF amount-result join as proof-grade subcontracts; broader
caller subfamily coverage remains a follow-up lane.

Second local Mesen pass: the numbered multi-enemy fixture save
`EarthBound (USA)_7.mss` now produces a reviewed `refined_contract` result for
`hp_roller_collapse_boundary`. The neutral trace observes the collapse boundary
that save 5 did not: first `C2:8125` at frame 41, then `C2:7550` at frame 117,
the adjacent `C2:77CA` collapse-presentation tail, C1 direct/substitution
battle-text entries, and later repeated `C2:BB18` promotion-controller samples.
The decoded row snapshots show the selected row moving from live HP
`+0x11 = 0x00B2` at damage entry to `+0x11 = 0x0000` at the collapse-start
call, with `+0x1D = 0x01` visible in the later promotion-controller sample.
This promotes the HP-to-zero collapse boundary, `C2:7550 -> C2:77CA` order, and
hard/collapsed row-state installation. It is still not proof-grade for every
collapse contract: the neutral run does not observe `C2:7680` enemy-death
descriptor text or `C2:BC5C` inactive-slot cleanup, and it does not by itself
prove HP-roller visual timing.

## Evidence Inputs

- `refs/EB-M2-Listing-v1/US/bank02.txt` for helper names such as
  `SUCCESS_500`, `SUCCESS_255`, `SUCCESS_LUCK80`,
  `FAIL_ATTACK_ON_NPCS`, `INFLICT_STATUS_BATTLE`, and
  `SWAP_ATTACKER_WITH_TARGET`.
- `refs/EB-M2-Listing-v1/US/bank2F.txt` for EF scripts such as
  `MSG_BTL_DAMAGE`, `MSG_BTL_SMASH_PLAYER`, `MSG_BTL_KIKANAI`,
  `MSG_BTL_DAIYA_ON`, `MSG_BTL_SHIBIRE_ON`, `MSG_BTL_KIMOCHI_ON`,
  `MSG_BTL_MODOKU_ON`, `MSG_BTL_KAZE_ON`, and `MSG_BTL_TIMESTOP_RET`.
- `notes/c2-ef-battle-text-contract-workahead.md` for the C1/C2/EF battle
  text contract vocabulary.

## Validation

Future implementation gates remain the normal C2 scaffold and byte-equivalence
checks:

```powershell
python tools\build_source_bank_scaffold.py --bank C2
python tools\validate_source_bank_byte_equivalence.py --bank C2 --module all --combined --scaffold src\c2\bank_c2_helpers_asar.asm --strict
```
