# C2 Target Selection Runtime Polish

This note records the byte-neutral C2 target-selection polish slice. It promotes
the runtime contracts that C1's battle target resolver depends on: snapshot row
export, second-stage battler-row counting, selected-row source-entry promotion,
and transient cleanup.

Primary source modules:

- `src/c2/c2_b930_export_battle_selection_snapshot.asm`
- `src/c2/c2_bac5_count_filtered_second_stage_rows.asm`
- `src/c2/c2_bb18_promote_candidate_to_collapse_affliction_controller.asm`
- `src/c2/c2_bc5c_clear_inactive_candidate_live_slot_transient_fields.asm`

Related evidence notes:

- `notes/c2-battle-contract-workahead.md`
- `notes/battle-selection-snapshot-export-c2b930.md`
- `notes/class2-second-stage-selector-a970.md`
- `notes/class2-post-selection-controller-phases.md`
- `notes/class2-candidate-population-and-ranking.md`

## Snapshot Export

`C2:B930` exports one live battler or party slot into a 0x4E-byte battle
selection snapshot row.

Inputs:

- A = 1-based battler or party slot id
- X/Y = destination base

The helper clears the destination row, writes a small selection header, then
copies and derives fields from `$99CE + (A - 1) * 0x5F`.

Important row fields promoted in source comments:

| Offset | Meaning |
| --- | --- |
| `+0x00` | selected 1-based battler/party id |
| `+0x02` | cleared word |
| `+0x0C` | active marker set to `1` |
| `+0x0E` | filter/group byte, cleared by exporter |
| `+0x0F` | subtype/gate byte, cleared by exporter |
| `+0x10` | selected battler index, zero-based |

When the destination is `$9FFA`, the first bytes overlap the formal
`battle_menu_selection` header. The important C2-local constraint is that
`C2:B930` writes past that header into the wider adjacent snapshot block. C1 can
therefore use it as a target/choice prompt export without reducing the routine
to a six-byte menu-struct writer.

## Filtered Row Count

`C2:BAC5` scans the 32 battler rows rooted at `$9FAC`, with stride `0x4E`.
It returns a count in A. The source now exposes the newer role alias
`CountFilteredSecondStageBattlerRows`, while preserving the older
`CountFilteredSecondStageRows` alias for compatibility.

Input:

- A = requested row state or group value

Counted rows must satisfy all of these predicates:

- row `+0x0C != 0`
- row `+0x0E == input A`
- row `+0x0F == 0`
- row primary affliction/state byte `+0x1D` is neither `1` nor `2`

This is the C2 side of the C1 random-target lane: `C1:ADB4` uses the count
before choosing a random second-stage row.

## Source-Entry Promotion

`C2:BB18` scans six selected-row source entries in the `$9FB8..9FCF` battler-
field family. For enabled entries that are not blocked by the phase/gate bytes,
it mirrors live battler fields from `$99CE + slot * 0x5F` into the source entry
and linked live battler row.

The source now exposes the role alias
`PromoteSourceEntryToCollapseAfflictionController`, while preserving the older
candidate-promotion alias as a compatibility clue.

The strongest promoted behavior is the newly selected collapse/affliction path:

- write selected row pointer to `$A972`
- set row `+0x1D = 1`
- clear row `+0x1E..+0x23`
- build target text context
- emit hardcoded battle text `EF:6C6B`
- wait for the battle text when needed

After that, the routine copies seven source-entry status bytes into linked live
battler transient/status fields and refreshes presentation state. The source
comment keeps the wording conservative: `+0x1D = 1` is strongly associated with
collapse/unconscious handling, but the wider selected-row state family still
needs more C2-local pass coverage before every value gets a final enum name.

## Transient Cleanup

`C2:BC5C` is a separate callable cleanup helper, not just an internal tail of
`C2:BB18`. It scans the same six selected-row source entries and, for enabled
unblocked entries, resolves the linked live battler row from `9FBC`.

The source now exposes the role alias
`ClearInactiveSourceEntryLiveSlotTransientFields`, while preserving the older
candidate-cleanup alias for inherited callers and notes.

It clears live row bytes:

- `+0x10`
- `+0x11`
- `+0x12`
- `+0x14`

This should be read as inactive/transient-field cleanup, not a full
target/candidate-pool reset.

## C-Port Feedback Trace-Oracles

`notes/c-port-feedback-intake.md` frames the C2 side of this work as the
consumer of C1-staged battle-action and target bytes. The diary observations
are useful oracle candidates, but they should stay below contract status until
local C2 traces pin the same fields.

Useful trace probes for this note:

- capture the staged target/action bytes produced through `C1:ADB4` at the
  handoff into C2 target-selection and selected-row consumers
- record candidate/source-entry bytes `+0x07`, `+0x08`, and `+0x0A` where they
  are visible during candidate promotion, row counting, or selected-row
  dispatch; treat them as diagnostic metadata until their C2-local meaning is
  proven
- use target byte shapes `0x11`, `0x01`, and `0x12` as observed C-port diary
  probes, not promoted enum names; the `0x12` row-selector shape is a good
  trace target for checking row `0` / row `1` behavior
- keep item-originated actions tied back to the C1 separation: `C1:CFC6`
  selects an inventory slot, while `C1:CE85` resolves the item into the
  action/target path that C2 later consumes

## Decomp Value

This slice closes the strongest C1-to-C2 target-selection dependency:

- C1's target prompts can now point to a source-commented C2 snapshot export
  contract.
- C1's random second-stage target lane can rely on a documented C2 battler-row
  count contract.
- C2's selected-row promotion now has a clear bridge from source entries into
  `$A972`, target text context, and the `EF:6C6B` collapse/affliction message.

## Remaining Soft Spots

- exact enum names for row bytes `+0x0E`, `+0x0F`, `+0x1D`, and `+0x1E..+0x23`
- the precise difference between `$A970` and `$A972`
- wider controller behavior after `C2:7550` and the late `C2:77CA` path
