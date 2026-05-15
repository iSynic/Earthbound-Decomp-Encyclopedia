# C-Port Feedback Intake

This note folds port-side feedback from
`F:\Earthbound C Port - Codex\docs\decomp-feedback-diary.md` back into this
decomp workspace. It is an intake layer, not a replacement for local proof:
the diary entries are valuable implementation pressure from the C-port lane,
but source labels and behavior claims in this repo should still be backed by
local ASM, byte-equivalence, trace, or manifest evidence before promotion.

Intake snapshot: 2026-05-13.

Entries folded: 36 actionable diary entries, mostly around C2 battle runtime
contracts plus C1 target/item selection bridges and EF battle-text payloads.

## How To Use This Note

- Treat `confirmed` diary entries as strong candidates for comments, tests, and
  port-facing contracts.
- Treat `decomp note candidate` entries as next-note or note-refresh seeds.
- Treat `test oracle` entries as harness work: useful enough to prioritize, but
  not enough to rename source behavior by themselves.
- Keep local source labels primary unless a diary claim is locally verified
  against the checked-in source and validation reports.

## Main Intake Lanes

### C1/C2 Target And Item Staging

The diary reinforces the existing model that C1 owns target/menu selection while
C2 consumes staged battle-action records and target masks:

- `C1:ADB4` remains the shared battle targetting resolver for PSI, item, and
  action-row flows.
- `C1:CE85` and `C1:CFC6` should stay separated: `C1:CFC6` owns the battle
  inventory selection loop, while `C1:CE85` resolves the selected item into the
  item-action/targetting path.
- The useful trace metadata is the candidate row field layout around
  `+0x07`, `+0x08`, and `+0x0A`, especially the selected target/action byte
  before C2 consumes it.
- The target byte shapes from the C-port diary should be checked against local
  traces before being turned into stable names:
  - `0x11` / `0x01`: single/ranked target shapes.
  - `0x12`: row selector shape, with target `1` mapping to row `0` and target
    `2` mapping to row `1` in the observed port harness.

Primary local notes:

- `notes/battle-targetting-resolver-c1adb4-af50.md`
- `notes/battle-item-action-selection-c1ce85-c1cfc6.md`
- `notes/c1-battle-front-end-runtime-polish.md`
- `notes/c2-target-selection-runtime-polish.md`
- `notes/c2-battle-contract-workahead.md`

### Current-Action Payload Bridge

The strongest repeated diary theme is that many apparent action leaves are
better read as payloads over the current selected target:

- `C2:40A4` is still the right central name for applying the second pointer /
  payload side of a `D5:7B68` action entry.
- Direct curatives, target-loss leaves, food/condiment effects, item-side
  status leaves, HP/PP recovery, and several late status/numeric leaves all
  reuse selected-row or current-action staging.
- Damage/collapse should stay separated in the model: the diary explicitly
  supports collapse finalization after HP roller settlement rather than at the
  moment damage is staged.

Primary local notes:

- `notes/class2-second-pointer-consumer-40a4.md`
- `notes/c2-action-dispatch-runtime-polish.md`
- `notes/c2-late-selected-row-runtime-polish.md`
- `notes/c2-lifeup-healing-runtime-polish.md`
- `notes/c2-hit-resolution-status-runtime-polish.md`

### Affliction Writer Matrix

The diary provides useful pressure for treating `C2:724A` as a small reusable
affliction/subgroup writer, with chance and resistance gates modeled separately:

- Solidification, late status payloads, PSI status leaves, Flash body numbness
  (called paralysis in ebsrc/internal status vocabulary),
  item-side statuses, and concentration-seal paths all converge on the same
  family shape.
- The writer contract should stay parameterized by selected row plus subgroup
  slot/value; separate notes can own individual chance gates.
- Future trace work should build a caller matrix for the `X` / `Y` pairs rather
  than giving every caller a one-off semantic model.

Primary local notes:

- `notes/class2-affliction-apply-helper-724a.md`
- `notes/class2-battler-affliction-crosswalk.md`
- `notes/c2-late-status-runtime-polish.md`
- `notes/c2-psi-flash-runtime-polish.md`
- `notes/c2-concentration-seal-runtime-polish.md`
- `notes/c2-hit-resolution-status-runtime-polish.md`

### Damage Spine And Result Text

The diary strongly supports `C2:8125` as the shared selected-target damage
spine or ABI boundary:

- Random-damage item leaves, bottle rockets, bombs, HP-Sucker, PSI damage
  commons, and Final Prayer-style damage paths are best described by how they
  prepare an amount and then cross the `C2:8125` boundary.
- `C2:8125` should not be overloaded with all downstream meaning. Keep amount
  calculation, guts/survival/collapse, HP roller settlement, and EF result text
  as separate contracts.
- Bombs also tie damage gates to battle sprite geometry; that detail belongs in
  both the C2 bomb note and future presentation/asset-facing contracts.

Primary local notes:

- `notes/c2-hit-resolution-status-runtime-polish.md`
- `notes/c2-bottle-rocket-runtime-polish.md`
- `notes/c2-item-bomb-runtime-polish.md`
- `notes/c2-psi-common-runtime-polish.md`
- `notes/class2-bomb-common-family-c2a658-c2a821.md`
- `notes/c2-ef-battle-text-contract-workahead.md`

### Healing, Resource, And Numeric Payloads

The C-port diary gives a coherent work queue for amount-bearing effects:

- PSI Magnet is a transfer: it has a drained PP amount and a recovery side.
- PP reduction is the loss-only sibling and should not inherit recovery wording.
- Fixed HP and fixed PP recovery mirror each other structurally, but the target
  resource and text contracts should remain explicit.
- Late numeric reducers and stat-up/down leaves have small 16-bit edge behavior
  that deserves local tests before a C port relies on normalized integer widths.
- Healing Gamma and Healing Omega should stay distinct in notes: Gamma is a
  broad recovery gate; Omega is a hard-state full-HP revival wrapper.

Primary local notes:

- `notes/psi-magnet-drain-amount.md`
- `notes/c2-late-stat-resource-runtime-polish.md`
- `notes/c2-offense-defense-stat-actions-runtime-polish.md`
- `notes/c2-lifeup-healing-runtime-polish.md`
- `notes/battle-affliction-recovery-family-c29aea-a39d.md`

### PSI Status And Flash Gates

The diary backs the existing split between compact gate families and shared
writers:

- PSI Flash is a trace-gate family over several result/status possibilities.
- The resist-checked PSI status trio should be modeled as one host gate shape
  with distinct payload outcomes.
- Flash body numbness is small enough to be an early local trace oracle for the
  broader `C2:724A` affliction writer model.

Primary local notes:

- `notes/c2-psi-flash-runtime-polish.md`
- `notes/class2-psi-flash-common-local-flow.md`
- `notes/c2-psi-common-runtime-polish.md`
- `notes/class2-affliction-apply-helper-724a.md`

## Suggested Trace-Oracles

These are the highest-value local tests or harness probes implied by the C-port
feedback:

The concrete execution queue for these probes now lives in
`notes/c2-battle-trace-oracle-plan.md`.

| Oracle | Purpose | Diary pressure |
| --- | --- | --- |
| C1/C2 target bridge | Capture `C1:ADB4` output shape, candidate row fields, and selected target/action byte before C2 dispatch. | Entries 02, 03, 05, 10, 11 |
| Item slot removal | Distinguish the `C1:DDC6` and guarded `C2:437E` item-removal shapes. | Entry 12 |
| Current-action payload bridge | Confirm selected-target staging through direct curatives, target-loss, food, and item leaves. | Entries 06, 07, 10, 13, 25, 26, 31 |
| Collapse after HP roller | Prove collapse finalization occurs after HP roller settlement. | Entry 08 |
| Affliction writer matrix | Record `C2:724A` caller `X` / `Y` pairs and separate chance/resistance gates. | Entries 14, 15, 29, 30, 31, 36, 37 |
| Resource amount pair | Compare PSI Magnet transfer, PP loss-only, fixed HP, and fixed PP recovery amount paths. | Entries 16, 18, 25, 26 |
| Late 16-bit numeric edges | Check stat reducers/stat-up helpers for width, clamp, and text amount behavior. | Entries 19, 20, 27, 28 |
| Damage spine boundary | Verify amount preparation into `C2:8125` across random items, rockets, bombs, HP-Sucker, and PSI commons. | Entries 21, 22, 23, 24, 34, 35 |
| Healing ladder reset | Separate Gamma broad recovery from Omega full-HP revival and the heavy reset helper. | Entries 32, 33 |
| Status gate families | Trace Flash and resist-checked PSI status families through host gates and shared writers. | Entries 36, 37 |

## Per-Entry Intake

| Entry | Diary status | Decomp action |
| --- | --- | --- |
| 02 Battle Target Staging Feeds Derived Action Byte | confirmed | Add trace evidence around `C1:ADB4` staged target/action bytes before treating target-byte values as stable contracts. |
| 03 Staged Target Inputs Are Useful Trace Metadata | decomp note candidate | Refresh target-selection notes with which staged bytes are diagnostic metadata versus semantic output. |
| 04 Battle Affliction Recovery Selectors Are Small Trace Gates | decomp note candidate | Keep recovery selectors as small gates feeding known recovery leaves; add trace labels before source renames. |
| 05 Enemy Single-Target Choice Reaches Mixed-Round Harness | confirmed | Use enemy single-target choice as an oracle for mixed player/enemy target domains. |
| 06 Direct Curative Payloads Share The Consequence Bridge | confirmed | Group direct curatives under current-action selected-target payload handling. |
| 07 Direct Target-Loss Payloads Fit The Same Staged Target Bridge | confirmed | Tie target-loss payloads to the selected-target bridge and keep text/result handling separate. |
| 08 Collapse Finalization Belongs After HP Roller Settlement | confirmed | Document collapse as post-roller settlement, not immediate damage application. |
| 09 Random Stat-Up Selector Wants An Explicit RNG Trace | test oracle | Add an RNG trace before naming random stat-up selector outcomes too strongly. |
| 10 Food/Condiment Payload Fits The Staged Target Bridge | confirmed | Treat food/condiment as another selected-target payload lane. |
| 11 Battle Item Selection Is A Clean C1-To-C2 Bridge | confirmed | Keep the `C1:CFC6` / `C1:CE85` to C2 contract visible in C1 and C2 notes. |
| 12 Item Source-Slot Removal Has Two Useful Runtime Shapes | confirmed | Split item source-slot removal into `C1:DDC6` and guarded `C2:437E` shapes. |
| 13 Item-Side Concentration Seal Fits The Current-Action Payload Bridge | confirmed | Keep concentration-seal effect payloads tied to current-action selection. |
| 14 Solidification Shares A Reusable Affliction-Slot Primitive | confirmed | Use solidification as a clear `C2:724A` caller in the affliction writer matrix. |
| 15 Late Status Payloads Collapse Onto One Affliction Writer | confirmed | Continue grouping late status leaves by shared writer instead of isolated behavior names. |
| 16 PSI Magnet PP Drain Is An Amount-Bearing Resource Payload | confirmed | Preserve transfer semantics and amount evidence for PSI Magnet. |
| 17 Timed Shield Actions Feed The Thunder Blocker Fields Directly | confirmed | Add a shield/Thunder-blocker field trace lane before collapsing shield names into generic status wording. |
| 18 PP Reduction Is The Loss-Only Sibling Of PSI Magnet | confirmed | Keep PP reduction separate from transfer/recovery wording. |
| 19 Late Numeric Reducers Have Small But Real 16-Bit Edge Semantics | confirmed | Add width/clamp tests for late numeric reducers. |
| 20 Offense-Up And Defense-Down Share The Late Numeric Helper Spine | confirmed | Group offense/defense amount helpers while preserving direction-specific names. |
| 21 Random-Damage Item Leaves Are Good C2:8125 Boundary Probes | confirmed | Use these leaves as low-noise `C2:8125` amount-boundary tests. |
| 22 Bottle Rockets Are A Counted Trace-Gate Damage Family | confirmed | Keep rocket count/gate separate from shared damage application. |
| 23 Bombs Tie Damage Gates To Battle Sprite Geometry | confirmed | Preserve the visual geometry dependency in bomb/presentation contracts. |
| 24 HP-Sucker Crosses Damage, Recovery, And Amount Text | confirmed | Model HP-Sucker as a multi-contract lane: damage, recovery, and text amount. |
| 25 Lifeup And Fixed HP Recovery Share One Selected-Row Core | confirmed | Group fixed HP recovery with selected-row healing core. |
| 26 Fixed PP Recovery Mirrors The HP Recovery Wrapper Shape | confirmed | Mirror fixed PP recovery structurally while keeping PP resource wording. |
| 27 Direct 1d4 Stat-Up Items Share B2E0 Stat Leaves | confirmed | Use direct stat-up items to test the B2E0 stat leaf family. |
| 28 Odor Offense Reduction Is The Offense Half Of 8F21 | confirmed | Record odor as offense-reduction evidence for the 8F21/late numeric family. |
| 29 Flash Body-Numb Leaf Is A Small Affliction Writer | confirmed | Use Flash body numbness as a compact writer-gate oracle; keep ebsrc `FLASH_INFLICT_PARALYSIS` as an alias. |
| 30 Enemy-Side Concentration Seal Shares The Item-Side Post-Gate Effect | confirmed | Pair enemy-side and item-side concentration seal effects after their gates. |
| 31 Item-Side Status Leaves Split Cleanly From A89D Cluster | confirmed | Keep item-side status leaves grouped but split from the broader A89D cluster. |
| 32 Healing Gamma Broad Recovery Has A Small Trace Gate | confirmed | Add a Gamma-specific trace around the broad recovery gate. |
| 33 Healing Omega Hard-State Wrapper Is Full-HP Revival | confirmed | Treat Omega as hard-state full-HP revival around the heavy reset path. |
| 34 C2:8125 Is The Right Shared Damage Spine | confirmed | Continue using `C2:8125` as the shared selected-target damage ABI. |
| 35 PSI Damage Commons Share One Traceable Spine | confirmed | Group PSI damage commons by shared damage spine plus distinct element gates. |
| 36 PSI Flash Is A Compact Trace-Gate Family | confirmed | Keep Flash as a compact gate family with separate result writers. |
| 37 Resist-Checked PSI Status Trio Shares One Host Gate Shape | confirmed | Model the resist-checked PSI status trio as one host-gate shape with distinct payloads. |

## Documentation Follow-Up

The first follow-up should not be more broad inventory. The most useful next
pass is to update a small set of focused notes with diary-backed trace targets:

0. `notes/c2-battle-trace-oracle-plan.md`
1. `notes/battle-targetting-resolver-c1adb4-af50.md`
2. `notes/battle-item-action-selection-c1ce85-c1cfc6.md`
3. `notes/class2-second-pointer-consumer-40a4.md`
4. `notes/class2-affliction-apply-helper-724a.md`
5. `notes/c2-hit-resolution-status-runtime-polish.md`
6. `notes/c2-psi-common-runtime-polish.md`
7. `notes/c2-psi-flash-runtime-polish.md`
8. `notes/c2-lifeup-healing-runtime-polish.md`
9. `notes/c2-late-stat-resource-runtime-polish.md`
10. `notes/c2-ef-battle-text-contract-workahead.md`

For source work, the safest rule is: diary claim -> local note/trace oracle ->
source comment/name only after the local evidence is pinned.
