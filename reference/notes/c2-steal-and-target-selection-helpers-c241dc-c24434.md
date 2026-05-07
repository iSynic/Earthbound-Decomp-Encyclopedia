# C2 Steal and Target Selection Helpers `C241DC..C24434`

This note covers the next C2 audit gap immediately before `CHOOSE_TARGET` in the `ebsrc-main` include map. The three address-bearing unknowns at `C2:4348`, `C2:437E`, and `C2:4434` sit in a coherent battle-targeting strip:

- `C2:41DC` builds the stealable-item candidate buffer at `$A9D4`.
- `C2:4316` is the named reference `SELECT_STEALABLE_ITEM`.
- `C2:4348` checks whether a previously selected steal item is still present in the current candidate buffer.
- `C2:437E` is a battle-end fallback that applies a stolen item to a matching character inventory slot.
- `C2:4434` chooses a random target from the current front/back target rows and is only called from `CHOOSE_TARGET`.

## Reference anchors

`refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank02.asm` corroborates the ordering:

- `battle/find_stealable_items.asm`
- `battle/select_stealable_item.asm`
- `unknown/C2/C24348.asm`
- `unknown/C2/C2437E.asm`
- `unknown/C2/C24434.asm`
- `battle/choose_target.asm`

The unknown files are not present in the local `refs/ebsrc-main` checkout, but the named neighbors are present and line up cleanly with the local ROM bytes. The local direct callers are also narrow:

- `C2:4348`: one caller at `C2:5AD1`
- `C2:437E`: callers at `C2:5D62`, `C2:5D82`, and `C2:5DB4`
- `C2:4434`: callers at `C2:462D` and `C2:465A`, both inside `CHOOSE_TARGET`

## Stealable candidate buffer

`C2:41DC` matches the reference `FIND_STEALABLE_ITEMS` body. It scans active party members from `$986F`, restricts source codes to the playable range `1..4`, finds each matching battler in `$9FAC`, and records the battler's `action_item_slot` byte. It then walks each character's 14 inventory slots at `$99F1 + character * 0x5F`, rejects empty slots, rejects item prices of zero or `>= 290`, requires item type bits `#$0030 == #$0020`, and skips slots that are currently equipped through `$99FF..$9A02`.

Accepted item ids are written one byte at a time into `$A9D4`, and the helper returns the count. That makes `$A9D4` a transient stealable-item candidate list.

`C2:4316`, the reference `SELECT_STEALABLE_ITEM`, calls `C2:41DC`, returns zero if the candidate count is zero, otherwise gives the steal a 50 percent failure gate via `RAND & #$0080`; if that gate passes, it selects one candidate with `C2:6A2D` / `GetRandomBelow(count)` and returns `$A9D4[index]`.

Working names used below are collected again in the final section for the generated proposal table.

Source follow-up (2026-05-06): the battle-start front controller now calls
`C2:4316` by the `SelectStealableItemCandidate` contract at both STEAL action
argument setup sites. This makes row `0x42`'s selected-row `+8` byte read as a
pending stolen item id instead of an opaque action argument.

## `C2:4348`: validate a pending steal item

`C2:4348` takes an item id in `A`, rebuilds the `$A9D4` stealable candidate list through `C2:41DC`, then linearly scans the returned candidate count. It returns `1` if any candidate equals the input item id and `0` otherwise.

The only direct caller is the STEAL action cleanup path at `C2:5AD1`. That caller checks the active battler's `current_action == #$0042`, loads `current_action_argument` from offset `+8`, calls `C2:4348`, and clears `current_action_argument` if the helper returns zero.

The source callsite now uses `IsPendingStealItemStillStealable`, matching this
guard role at the point where battle-start is about to stage the selected-row
`+8` byte for text/payload consumption.

`inspect_battle_action.py 66` corroborates table row `0x42` as the STEAL action:

- target `one`
- type `other`
- message `EF:9ABB`, whose preview prints a stole-item message
- action pointer `C2:889E`, matching the reference `BTLACT_STEAL`

So `C2:4348` is not a general inventory search. It is the guard that prevents a stale STEAL action argument from naming an item that is no longer stealable.

Working name used below: `IsPendingStealItemStillStealable`.

## `C2:437E`: battle-end stolen item application fallback

`C2:437E` is called only from the late main battle routine, around defeat/end-of-turn fallout. The three direct call sites are all in the `C2:5D40..5DB4` region after `COUNT_CHARS`/`SPECIAL_DEFEAT` checks and before the routine resumes the broader end-state cleanup.

The helper exits unless the active attacker has:

- `ally_or_enemy == 0`
- `npc_id == 0`
- nonzero `action_item_slot` at `+7`

It then verifies the current `current_action_argument` at `+8` still matches the item in that character's inventory slot:

- character index comes from battler id at `+0`
- item slot comes from `action_item_slot - 1`
- character inventory address is `$99F1 + (id - 1) * 0x5F + (action_item_slot - 1)`
- the item byte must equal `current_action_argument`

The item configuration table at `D5:5000` is then checked at item record field `+0x1C`; bit `#$80` must be set. The helper also calls `C3:EE14(id, item)` and requires a nonzero result, matching the same compatibility/equipment-style predicate seen in weapon/armor switch paths.

If all gates pass, `C2:437E` calls `C1:DDC6` with the battler id and slot number. Given the context, this looks like a battle-end or special-fallout path that applies the pending stolen item to the original character slot only if the inventory still agrees with the action record.

Working name used below: `ApplyPendingStolenItemSlotIfStillValid`.

Source follow-up (2026-05-06): the battle-start back half now calls
`ApplyPendingStolenItemSlotIfStillValid` by name at the three end-state cleanup
edges. That keeps the helper tied to committing a pending STEAL action fallout
rather than reading like a generic inventory updater.

## `C2:4434`: random front/back target-row picker

`C2:4434` takes a battler pointer in `A`, stores a one-based target code to battler offset `+0x0A` (`current_target`), and returns the selected battler code converted through the front/back row arrays.

The local byte flow is:

- read `NUM_BATTLERS_IN_FRONT_ROW` at `$AD56`
- read `NUM_BATTLERS_IN_BACK_ROW` at `$AD58`
- choose a random value in `0..front+back-1` with `C2:6A2D` / `GetRandomBelow`
- store `random + 1` into `battler::current_target`
- if the value falls in the front-row count, return `FRONT_ROW_BATTLERS[index]` from `$AD7A`
- otherwise subtract the front-row count and return `BACK_ROW_BATTLERS[index]` from `$AD82`

The direct callers are `C2:462D` and `C2:465A`, both inside `CHOOSE_TARGET` loops for one-target actions whose battle-action table row says to avoid purely random targeting. The caller immediately validates the returned code with `CHECK_IF_VALID_TARGET` (`C4:A1F5` in local address form) and repeats until it finds a valid target.

Working name used below: `PickRandomBattlerFromFrontBackRows`.

Source follow-up (2026-05-06): the `CHOOSE_TARGET` source now calls
`C2:4434` by this name at both front/back-row picker sites. The surrounding
loop still validates the returned battler code through `C4:A1F5`, so the
helper remains a row-list picker rather than a complete target-validity guard.

## Relation to `CHOOSE_TARGET`

The reference `CHOOSE_TARGET` source names the active battler fields touched by this strip:

- `+4`: `current_action`
- `+7`: `action_item_slot`
- `+8`: `current_action_argument`
- `+9`: `action_targetting`
- `+10`: `current_target`
- `+14`: `ally_or_enemy`
- `+15`: `npc_id`

`CHOOSE_TARGET` first ensures at least one front- or back-row target is valid, then derives target flags from `D5:7B68[current_action]`:

- row byte `+0`: action direction
- row byte `+1`: action target
- row byte `+2`: action type
- row byte `+3`: cost

For target modes `one` and `random`, the routine chooses between NPC targettable helpers, true random target ids, and the `C2:4434` row-picker above depending on the action direction and the table row's front byte. For row/all/no-target cases it writes the appropriate `action_targetting` bits and target codes directly.

This ties the unknown trio into the same action table model documented in `notes/class2-d57b68-battle-action-table-match.md`: the code is not generic menu selection, it is the live battle target-selection bridge over `D5:7B68` rows.

## Remaining caution

The reference labels still leave these helpers as unknown, and the exact meaning of the item config bit at `D5:5000 + item * 0x27 + 0x1C & #$80` is not named locally. The behavior-level claim is strong enough for working names, but the item-bit name should stay provisional until an item-table field note corroborates it.

## Working Names

- `C2:41DC` = `BuildStealableItemCandidateList`
- `C2:4316` = `SelectStealableItemCandidate`
- `C2:4348` = `IsPendingStealItemStillStealable`
- `C2:437E` = `ApplyPendingStolenItemSlotIfStillValid`
- `C2:4434` = `PickRandomBattlerFromFrontBackRows`
