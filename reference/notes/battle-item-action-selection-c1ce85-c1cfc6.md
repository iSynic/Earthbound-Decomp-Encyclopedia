# Battle Item Action Selection `C1:CE85` and `C1:CFC6`

This note covers the unknown includes at `C1:CE85` and `C1:CFC6`.

See also [battle-targetting-resolver-c1adb4-af50.md](notes/battle-targetting-resolver-c1adb4-af50.md).
See also [battle-choice-text-family-c1b2ec-b997.md](notes/battle-choice-text-family-c1b2ec-b997.md).
See also [item-slot-helper-pair-c3e977-c3ee14.md](notes/item-slot-helper-pair-c3e977-c3ee14.md).
See also [item-psi-name-display-and-target-prompt-c19216-c19437.md](notes/item-psi-name-display-and-target-prompt-c19216-c19437.md).

## Main Result

`C1:CFC6` is the battle item-inventory selection loop, and `C1:CE85` is the selected-item action/target resolver underneath it.
Both corridors are now source-backed in `src/c1/c1_cfc6_open_battle_item_selection_loop.asm` and `src/c1/c1_ce85_resolve_selected_battle_item_action.asm`.

The only direct caller of `C1:CFC6` is currently:

- `C1:DE33 -> C1:CFC6`

The only direct caller of `C1:CE85` is:

- `C1:D022 -> C1:CE85`

That caller is inside `C1:CFC6`, after the player has selected an inventory slot.

## `C1:CFC6`: Inventory Selection Loop

`C1:CFC6` takes a pointer to a small selection record in `A`.

The record's first byte is the acting character id. The helper:

- converts that character id to the 0x5F-byte party record offset
- checks `$99F1 + offset`, the first inventory slot for that character
- returns `0` immediately if the inventory is empty
- opens window/context `0x02`
- calls `C1:98DE`, now source-backed as `RenderCharacterInventoryOrEquipmentRows`, to build the character's item list
- runs the generic selection loop through `C1:196A`
- closes/updates text state through `C3:E4D4` and `C1:0084`
- stores the chosen inventory slot into record byte `+1`
- calls `C1:CE85` to resolve the selected item into action and target state
- closes temporary window `0x26`
- if `C1:CE85` returned `0`, loops and asks for a different item
- otherwise returns the nonzero result

So this is the battle-side "choose an item and validate what it can do" loop.

## `C1:CE85`: Selected Item Action And Target Resolver

`C1:CE85` also takes the same record pointer in `A`.

It:

- reads record byte `+0` as character id and byte `+1` as selected slot
- resolves the actual item id through `C3:E977`
- indexes `ITEM_CONFIGURATION_TABLE` at `D5:5000` with stride `0x27`
- writes record word `+2 = 2` as the default action class
- writes record byte `+4 = 1`
- writes record byte `+5 = character id`
- reads item config byte `+0x19`

The item config byte `+0x19` controls how far the helper proceeds:

- config bits `0x10` or `0x20` take the ordinary target-resolution path
- config bits `0x30` take an additional usability/equipability-style mask check using item byte `+0x1C` and `C4:58AB[character-1]`
- other values fall through and return the current local result, usually `0x00FF`

On the ordinary target-resolution path:

- it reads the item action word at config offset `+0x1D`
- calls the shared battle targetting resolver `C1:ADB4`
- if `ADB4` returns `0`, the item choice is rejected
- otherwise it writes the action word into record word `+2`
- it stores target bytes derived through `C0:9251`
- and returns the target/result byte

If the `0x30` path fails the item mask check, the helper writes record word `+2 = 3`, marking a different fallback or failure action class.

## Interpretation

This pair is the missing battle-item counterpart to the PSI menu targeting path:

- PSI selection resolves through `D5:8A50` and then targetting
- item selection resolves through `D5:5000`, chooses an item action word, and then targetting

The item action word at `D5:5000 + 0x1D` is especially important, because it is passed directly to `C1:ADB4`, the same shared targetting resolver already documented for PSI and action rows.

## Adjacent Use-Item Text Bridge

The adjacent `C1:AF73..B5B6` body is now source-polished enough to connect this
resolver to the text/export side of item use.

Current safest read:

- item config byte `+0x19` chooses the coarse battle/field use lane
- item config byte `+0x1C` supplies the per-character usability mask
- item config word `+0x1D` selects the associated `D5:7B68` action row
- action row `+0x04` supplies ordinary choice text
- action row `+0x08` supplies the later target-choice/payload text pointer
- fixed `C7` pointers cover wrong-user and other item-use rejection branches
- successful targetting continues into the `$9FAC -> C2:B930 -> $9FFA`
  battle selection snapshot/export path

So `C1:CE85` decides whether the chosen inventory slot can become an action
selection record, while the adjacent `AF73/B2EC/B450` lane owns the action-row
text and snapshot side effects that follow from that choice.
