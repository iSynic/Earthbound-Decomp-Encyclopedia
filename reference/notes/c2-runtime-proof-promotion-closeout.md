# C2 Runtime Proof Promotion Closeout

This note is the compact Phase 2 index for C2 runtime evidence that is strong
enough to guide source-facing comments and C-port contracts. It does not add
new behavior claims; it consolidates existing natural traces, controlled
fixtures, local ASM review, and byte-equivalence-protected source comments.

## Promoted Natural Vanilla Evidence

| Contract | Evidence | Current source-facing state |
| --- | --- | --- |
| Damage ABI and amount text | Physical, PSI Freeze, Healing, and Large Pizza save-state captures reach `C2:8125`, selected-row HP word changes, and C1 amount-text joins. | Treat `C2:8125` as the amount-bearing HP mutation boundary; keep collapse tails split from damage timing unless the trace includes them. |
| HP collapse entry | Rolling-HP/collapse traces reach `C2:7550 -> C2:77CA` and hard/collapsed row-state installation. | Collapse entry is proof-grade; optional descriptor text and cleanup tails remain controlled-helper or timing follow-up evidence. |
| PSI Magnet PP transfer | Stonehenge Mook/Paula capture reaches `C2:9F5E -> C2:721D -> C2:7191`, carries amount `6`, reduces target PP, and routes caster recovery through `SET_PP` with cap behavior. | Initial proof complete. A non-full caster trace would only broaden visible positive recovery, not prove the transfer path. |
| Mad Duck PP loss | Desert Gold Mine Mad Duck capture reaches `C2:8E42 -> C2:721D -> C2:7191`, rolls amount `4`, reduces party PP target, and has no caster-side recovery call. | Initial proof complete; keep this lane loss-only and do not inherit PSI Magnet transfer wording. |
| Fresh Egg snapshot export | Overworld Goods Use Fresh Egg targeting Poo reaches natural `C1:B3DB -> C2:B930` with source row `$99CE`, destination row `$9FAC`, item id `$5C`, and post-return snapshot capture. | Initial natural route proof complete. Additional item/target families are optional broadening only. |
| Flash numb and crying | Mighty Bear Seven Flash reaches `C2:98A1 -> C2:9917 -> C2:724A` and writes selected-row `+0x1D = 3`; Mook Senior Flash reaches the crying writer path. | Numb and crying writers are proven as Flash-family paths; avoid broad status-enum promotion beyond observed slots. |
| Poison writer | Dread Scorpion poison reaches `C2:724A` with selected-row `+0x1D` write evidence. | Poison writer is family-specific proof; keep generic writer comments parameterized. |
| Item healing | Large Pizza and Healing captures join item/action resolution, HP amount, row snapshots, and text payloads. | Good enough for HP recovery/comment polish; do not infer unrelated item families. |
| HP-Sucker item drain | Jeff HP-Sucker save-state capture reaches `C2:A46B`, stages `EF:8E5E`, mutates target HP through `C2:8125`, and displays the drained amount through `C1:DC66` with `EF:75AB`. | Treat as natural item-drain coverage for HP amount/text joins; keep self-drain and no-effect branches separate until captured. |

## Controlled Or Neighbor Evidence

- `adb4-force-b930-snapshot-export` proves `C2:B930` row-copy mechanics under
  fixture steering. The Fresh Egg natural route now supplies the first
  unpatched C1 callsite proof, so this controlled run is mechanics
  corroboration rather than the only evidence.
- Fixture ROMs for `C2:40A4`, direct collapse helpers, and resource steering
  remain navigation/mechanics evidence. They should not be worded as vanilla
  action behavior unless a natural save-state trace corroborates the claim.
- Battle Goods target-select saves that reach `C1:CE85 -> C1:ADB4 -> C2:BAC5`
  are neighbor-route evidence for target counting and selection, not
  `C2:B930` export proof.

## Remaining C2 Runtime Backlog

- Source polish and final wording for PP transfer/loss-only, snapshot export,
  and status writer comments.
- Optional broader `C2:B930` coverage with a second overworld item or target
  family.
- Review/promotion wording for paired `C2:724A`/`C2:9917` status-gate captures
  without broadening unobserved status enums.
- C1/EF battle-text joins for amount/name substitutions that sit around the C2
  behavior contracts.
- Optional natural timing for collapse tails such as `C2:7680` and `C2:BC5C`.

## Policy

- Natural vanilla traces can promote behavior contracts when local ASM agrees.
- Controlled fixtures can promote mechanics, not vanilla gameplay timing.
- Neighbor routes explain nearby control flow but do not satisfy proof for a
  missing callsite.
- Optional broadening must not re-open completed initial-proof lanes.
