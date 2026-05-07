# C2 Action Dispatch Runtime Polish

This note records the byte-neutral C2 action-dispatch polish slice. It promotes
the local contract between the `D5:7B68` battle-action descriptor table, battler
action/target bytes, target-mask construction, battle text-context
refresh, and second-pointer payload application.

Primary source modules:

- `src/c2/c2_40a4_apply_battle_action_second_pointer_payload.asm`
- `src/c2/c2_3bcf_build_battle_attacker_text_context.asm`
- `src/c2/c2_3d05_build_battle_target_text_context.asm`
- `src/c2/c2_4477_build_class2_derived_action_code.asm`
- `src/c2/c2_4703_dispatch_class2_derived_action.asm`

Related evidence notes:

- `notes/class2-handoff-4477-4703.md`
- `notes/class2-second-pointer-consumer-40a4.md`
- `notes/class2-mask-helper-family.md`
- `notes/class2-descriptor-field-4e-and-d57b68.md`
- `notes/class2-d57b68-battle-action-table-match.md`
- `notes/class2-battlers-table-layout-9f8a-9fac.md`
- `notes/class2-concrete-battle-text-call-paths.md`

## Derived Action Bytes

`C2:4477` accepts a battler row base in A, usually from the
`$9FAC + 0x4E * n` row domain. It consults:

- ranked candidate lists `$AD7A/$AD82`
- battler `current_action` at `+0x04`
- the `D5:7B68` battle-action descriptor table

The routine writes:

| Battler byte | Role |
| --- | --- |
| `+0x09 action_targeting` | compact derived action code |
| `+0x0A current_target` | action parameter, target index, or ranked-list index |

The source comment deliberately keeps this mechanical. The current local proof
is strongest for the fact that `C2:4703` consumes these bytes as action code and
parameter; exact enum names for every `+0x09` value still need more end-to-end
action-table coverage.

## Descriptor Table Join

The `D5:7B68` layout used by this slice is:

| Offset | Current best role |
| --- | --- |
| `+0x00` | action direction/class selector |
| `+0x01` | target-shape selector |
| `+0x02` | action type |
| `+0x03` | cost byte |
| `+0x04` | message/presentation pointer |
| `+0x08` | action/behavior pointer |

The `+0x00` and `+0x01` bytes directly influence `C2:4477`'s derived
`+0x09/+0x0A` writes. The `+0x08` pointer is consumed by `C2:40A4` through the
second-pointer path.

Implementation update: `src/c2/c2_4477_build_class2_derived_action_code.asm`
now carries the same local `D5:7B68` row root/bank constants, `0x0C` row-size
constant, and battler `current_action` / `action_targeting` / `current_target`
names used by the battle-start and late selected-row action-table text passes.
This keeps the action-row producer aligned with the C1/C2 text and payload
consumers.

## Target-Mask Dispatch

`C2:4703` accepts a battler row base in A, clears `$A96C/$A96E`, then
dispatches on battler byte `+0x09`. Several branches consume battler byte
`+0x0A`.

Implementation update: `src/c2/c2_4703_dispatch_class2_derived_action.asm`
now names `$A96C/$A96E` as the current target mask, battler
`current_action/action_targeting/current_target/ally_or_enemy` offsets, and the
observed derived-action code lanes:
single parameter battler (`1`), allied target sets (`2/4`), ranked-list member
(`0x11`), direct metadata-matched battlers (`0x12`), and all enemies (`0x14`).

The dispatch branches build, prune, or target bits through the class-2 mask
helper family:

- `C2:6BFB`
- `C2:6C82`
- `C2:6D04`
- `C2:6E77`
- `C2:6FDC`
- `C2:7029`
- `C2:7089`
- `C2:416F`

The important promoted contract is that `$A96C/$A96E` is the current 32-bit
target mask for the derived action, not a generic scratch pair.

Implementation update: the mask helper source family now mirrors that contract
directly by naming `C4:A279` as the one-hot bit table, `$A96C/$A96E` as the
current target mask, `$9FAC` as the battler-table domain, and `0x4E` as the row
stride in the core add/test/clear and build/remove passes.

Follow-up update: the remaining `6EF8` first-match finder and `70E4`
flagged-battler pruner now share the same one-hot table and bit-index
vocabulary, with `70E4` explicitly calling the named `C2:7029` test and
`C2:7089` clear helpers.

Source-vocabulary update: the action builder/dispatcher, second-pointer
applicator, and mask-helper sources now reserve candidate wording for the
ranked `$AD7A/$AD82` lists. Their `$9FAC` constants and local field offsets use
`BattlersTableBase`, `BattlerRowSize`, and named battler fields such as
`current_action`, `action_targeting`, `current_target`, `consciousness`,
`ally_or_enemy`, `npc_id`, `row`, and `afflictions`.

## Second-Pointer Application

`C2:40A4` is the consumer for the second pointer from a `D5:7B68` action
descriptor. The caller stages that pointer in direct-page `$1E/$20`; the routine
copies it to local `$06/$08`.

Runtime shape:

1. wait for `C2:EACF` to report that the battle effect step is ready
2. iterate targeted bits in the `$A21C` domain
3. iterate targeted bits in the `$9FAC` battler-row domain
4. for each targeted bit, rebuild target text context through `C2:3D05`
5. dispatch the same fixed payload pointer through `C0:9279`

That makes `C2:40A4` an action-payload applicator over the current target mask.
It is not just a passive animation or data-stream routine.

`C2:416F` is the sibling mask-pruning helper in the same source module. It
removes currently targeted rows from `$A96C/$A96E` when their battler row is
inactive or in blocked affliction/state bytes.

Implementation update: `src/c2/c2_40a4_apply_battle_action_second_pointer_payload.asm`
now names the caller-frame second-payload pointer, the local payload pointer,
the `$A21C` actor-target domain, the `$9FAC` battler-target domain, the
shared `0x4E` battler-row stride, and the bit ranges used by the two payload
passes.

Follow-up update: the same source now names `$00BC/$00BE` as the current
action-payload dispatch pointer and names the `C4:A08D` special-case table used
by the sibling target-mask pruning helper. This keeps the second-pointer
consumer aligned with the C1 DD9F tail's distinction between current payload
slots and ordinary battle-text dispatch staging.

Second follow-up: `src/c2/c2_a89d_run_random_damage_and_status_item_action_cluster.asm`
now calls the same named `C2:40A4` applicator for its local payload tail, and
`src/c2/c2_654c_run_magic_butterfly_pp_restore_animation.asm` names its
embedded `D5:7B68` action-type helper. These are small edges, but they keep
non-table-looking helper modules from drifting back to raw action-payload
vocabulary.

Third follow-up: the mask-helper source now labels embedded `C2:6E00` as the
all-active battler target-mask builder, and the A89D item/status tail now uses
named calls for the `6BFB/6C82/6E00/6E77/6EF8/70E4` mask-helper family before
handing the selected payload pointer to `C2:40A4`.

Fourth follow-up: dispatch and payload-side consumers now prefer the battler
domain helper aliases directly. `C2:4703`, `C2:3D05`, `C2:966B`, `C2:90C6`,
and `C2:A89D` call the mask family as active typed battlers, enemy-side
battlers, target-parameter matched battlers, active battlers, active NPC
battler removal, affliction-flagged pruning, and row-state filtering. The old
`TARGET_*`, `REMOVE_*`, and candidate-style labels remain as compatibility
anchors where they clarify inherited call names, but the action contract now
reads as target-mask construction over battler rows.

Battle-start controller follow-up: the front half now names its
`BuildClass2DerivedActionCode`, `DispatchClass2DerivedAction`, and
`FilterBattleActionTargetMaskByRowState` joins directly. This makes the
fallback retargeting loop read as: build derived action bytes, build the
current target mask, prune blocked row states, and retry when the mask is empty.

Hit-resolution follow-up: the Time Stop/retarget tail now uses the same named
`FilterBattleActionTargetMaskByRowState` and `MaskSet_TestBit` contracts before
refreshing the target text context and applying the selected hit payload.

Target-picker follow-up: `src/c2/c2_4477_build_class2_derived_action_code.asm`
now calls the documented `C2:4434` helper as
`PickRandomBattlerFromFrontBackRows` in the two `CHOOSE_TARGET` loops that
need a front/back-row candidate before validating it through `C4:A1F5`. The
nearby `C2:3F6C` call now reads as
`TryPickAiFlaggedNpcBattlerTargetOrdinal`: it may return a one-based
`current_target` ordinal for an active battler whose `npc_id` matches a party
slot carrying enemy-AI flag `0x02`, otherwise it returns zero and the existing
random valid-target fallback remains in charge.

Battle-start target-mask follow-up: the target text-context source now exposes
two formerly hidden helper entries inside `C2:3D05..40A4`. `C2:3E32` rebuilds
the first target text context from the current target mask, and `C2:4009`
builds the current target mask from the active attacker's action-targeting
byte before row-state pruning. The battle-start front controller now calls both
entries by those roles instead of raw local addresses.

Battle-start tail follow-up: the adjacent `C2:4703..4958` source now exposes
`C2:48E0` as the shared battle-start visual-state and candidate-buffer reset
entry used by variable source rebuilds, action cancellation, and battle-end
cleanup paths. This keeps the action dispatcher source aligned with the
battle-start controller tails that jump back into the setup lane.

## Battle Text Context Join

The nearby `C2:3BCF` and `C2:3D05` context builders are the strongest local
bridge between the current action/targeting state and the C1 battle-text
substitution buffers.

Implementation update: `src/c2/c2_3bcf_build_battle_attacker_text_context.asm`
now names `$A970` as the active attacker battler pointer, its `D5:9589`
enemy-data lookup, the attacker name buffer at `$A983`, the `$5E77` article
flag, the party-record fallback path through `$99CE + row * 0x5F`, and the
`battler` fields used by the source body:

| Battler field | Local role in `C2:3BCF` |
| --- | --- |
| `+0x00 id` | enemy-data row and final attacker text id |
| `+0x0B the_flag` | article/name-format token source |
| `+0x0E ally_or_enemy` | enemy-side versus party-side name path |
| `+0x0F npc_id` | non-party/non-enemy name-path override |
| `+0x10 row` | party-record fallback selector |
| `+0x4C` | companion input to `C2:B66A` before article insertion |

Implementation update: `src/c2/c2_3d05_build_battle_target_text_context.asm`
now carries the same vocabulary for `$A972` as the active target battler
pointer, the target name buffer at `$A99E`, and the `$5E78` target article flag.
Its helper tails also name the `$A96C/$A96E` current target mask, the
`C2:7029` bit test, the `9FAC + 0x4E * n` battler pointer rebuild, the
`$AD56/$AD7A/$AD82` front/back battler order lists, and the mask builders used
by action-targeting modes.

Small target-picker tail: the same source now exposes `C2:3F6C` as the
AI-flagged NPC battler target ordinal probe used by `C2:4477`. The helper keeps
its zero-result ABI explicit so callers can distinguish "no special NPC target"
from a real one-based target ordinal.

This is the first source-backed spot where the newer `$9FAC == BATTLERS_TABLE`
correction is carried directly through the battle-text context builders instead
of only appearing in notes.

Battle-start controller follow-up: the front and back controller halves now
call `BuildBattleAttackerTextContext` and `BuildBattleTargetTextContext` by
name when they refresh `$A970/$A972` before damage/status feedback, target-mask
payload dispatch, and selected-row result text.

Battler-row resistance follow-up: the C2 enemy initializer and player snapshot
exporter now call `C2:B608` as `ConvertElementalResistanceByte` and `C2:B639`
as `ConvertStatusResistanceByte`, matching the C1 current-action text consumer.
That ties the same resistance-byte normalization lane through enemy-data import,
party-row snapshot export, and selected-row equipment text refresh.

Enemy initializer shield follow-up: the same `C2:B6EB` source now calls
`C2:9CDC` as `ApplyTimedSubstateOrRefreshShieldCounter` when enemy-data byte
`+0x59` seeds initial timed shield/substate ids `1..4`. That connects enemy
row initialization to the selected-row shield action leaves through the same
row `+0x23/+0x25` contract.

## Decomp Value

This slice makes the selected-row controller more actionable:

- `D5:7B68` is now tied to source-commented consumers for metadata bytes and the
  second action pointer.
- battler bytes `+0x09/+0x0A` are documented as the handoff between action
  derivation and target-mask construction.
- `$A96C/$A96E` is explicitly documented as the current target mask.
- `C2:40A4` is documented as a per-target action-payload applicator, which is a
  useful bridge for later table-entry naming.
- `C2:3BCF` and `C2:3D05` now show how active battler pointers feed the
  attacker/target text buffers used by the C1 battle-text stack.
- battle-start front/back controller callsites now use the same action-dispatch,
  target-mask, bit-test, payload-dispatch, and text-context vocabulary as the
  helper source bodies.
- the hit-resolution retarget/status tail now shares that target-mask filter
  and bit-test vocabulary as well.
- resistance mirrors in initialized/exported battler rows now share the same
  elemental/status conversion helper names used by the C1 action-text lane.
- initial timed shield/substate seeds in initialized enemy rows now share the
  same `ApplyTimedSubstateOrRefreshShieldCounter` contract as shield action
  leaves.
- the last raw `C2:4477` target-picker helper now has an explicit zero-result
  or one-based target ordinal contract for AI-flagged NPC battlers.

## Remaining Soft Spots

- final enum names for `+0x09` action codes and `+0x0A` parameter meanings
- the exact payload ABI behind `C0:9279`
- full local naming of all `D5:7B68` action entries beyond the currently strong
  early PSI and late anchor families
