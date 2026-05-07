# C2 Steal Runtime Polish

This note records the byte-neutral C2 STEAL helper polish slice. It promotes
the transient stealable-item candidate buffer, random candidate selector,
pending-item validation guard, and battle-end application fallback.

Primary source modules:

- `src/c2/c2_41dc_build_stealable_item_candidate_list.asm`
- `src/c2/c2_4316_select_stealable_item_candidate.asm`
- `src/c2/c2_4348_is_pending_steal_item_still_stealable.asm`
- `src/c2/c2_437e_apply_pending_stolen_item_slot_if_still_valid.asm`

Related evidence notes:

- `notes/c2-steal-and-target-selection-helpers-c241dc-c24434.md`
- `notes/c2-action-dispatch-runtime-polish.md`
- `notes/c2-target-selection-runtime-polish.md`
- `notes/class2-d57b68-battle-action-table-match.md`

## Candidate Buffer

`C2:41DC` builds the transient candidate buffer at `$A9D4`.

The builder scans active playable party character ids `1..4`, finds the
matching battler row, excludes the battler's current action item slot, then
walks the character's 14 inventory slots.

An item slot is accepted only when:

- the slot is nonempty
- the item price is nonzero and below `0x0122`
- item type bits `#$0030` equal `#$0020`
- the slot is not one of the character's equipped slots at `$99FF..$9A02`

Accepted item ids are written to `$A9D4[count]`; A returns the count.

## Selection And Guards

`C2:4316` is the candidate selector for STEAL. It rebuilds `$A9D4`, returns
`0` if no candidates exist, applies a 50 percent random failure gate with
`RAND & #$0080`, and otherwise returns one candidate chosen with
`C2:6A2D` / `GetRandomBelow(count)`.

`C2:4348` validates a pending stolen item id by rebuilding `$A9D4` and checking
whether the item still appears in the current candidate list. This prevents a
stale STEAL action argument from naming an item that is no longer stealable.

## Pending Slot Application

`C2:437E` is a fallback/application helper for an active battler row at `$A970`.
It requires:

- row `+0x0E/+0x0F` blocker bytes are zero
- row `+0x07` has a nonzero source inventory slot
- row `+0x08` item id still matches that character inventory slot
- D5 item config flag `#$80` is set
- `C3:EE14` says the source character can still use the item

If all gates pass, it calls `C1:DDC6` with the battler id and inventory slot.

## Decomp Value

This slice separates the STEAL action into durable runtime contracts:

- `$A9D4` is the transient stealable-item candidate buffer
- candidate ids are item ids, not inventory slot ids
- row `+0x07` carries the source inventory slot
- row `+0x08` carries the pending stolen item id
- the selector's zero return covers both "no item" and random steal failure

## Remaining Soft Spots

- exact user-facing text path for failed versus no-candidate steal
- whether `C2:437E` should be named for battle-end cleanup or a broader
  pending-item fallout role after more callers are reviewed
