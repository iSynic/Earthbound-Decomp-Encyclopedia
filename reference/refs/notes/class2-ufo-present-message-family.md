# Class2 UFO Present Message Family

This note captures the current best local model for the `$AA10`-driven UFO present message path in bank `C2`.

See also [class2-battle-start-extra-message-state-4dbc-aa10.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-battle-start-extra-message-state-4dbc-aa10.md).
See also [class2-c1-display-text-substitution-handler-7af3.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-c1-display-text-substitution-handler-7af3.md).
See also [class2-c1acf8-substitution-byte-family.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-c1acf8-substitution-byte-family.md).
See also [class2-cc19-1f-display-text-bridge.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-cc19-1f-display-text-bridge.md).

## Main result

The `$AA10` path is no longer best read as an enemy-id-like selector.

The stronger current interpretation is:

- the fallback table at `C2:3109` matches specific UFO enemy ids
- the table's follow-up bytes are item ids
- `$AA10` is very likely a present/drop item selector for those UFO cases
- the two concrete text scripts fed by `$AA10` are the `EBATTLE8` present-message family

That is a materially better fit than the older "linked enemy id" reading.

## The local text scripts are now identified

Using the `earthbound.yml` text bank map from `ebsrc`:

- `EBATTLE8` begins at ROM offset `0x2F77FD`, which is CPU `EF:77FD`
- `EF:7BDF - EF:77FD = 0x03E2` -> `MSG_BTL_PRESENT`
- `EF:7DD5 - EF:77FD = 0x05D8` -> `MSG_BTL_CHECK_PRESENT_GET`

So the two concrete local readers are now identified:

- `C2:6003` -> `EF:7BDF` -> `MSG_BTL_PRESENT`
- `C2:8881` -> `EF:7DD5` -> `MSG_BTL_CHECK_PRESENT_GET`

That is a much stronger anchor than just calling them "hardcoded `EF` battle-text scripts."

## The scripts themselves fit the present family

The local bytes reinforce the same interpretation.

The `EF:7DD5` script contains:

- `1C 0D` -> `PRINT_ACTION_USER_NAME`
- `1F 02 10` -> play sound effect `16`, which `ebsrc` names `PRESENT_OPENED`
- `1C 05 00` -> `PRINT_ITEM_NAME 0`

That is exactly the shape we would expect for a battle message about opening a present and obtaining an item.

So the local message behavior now agrees with the symbol map.

## The fallback table at `C2:3109` is mixed-domain

The earlier "all enemy ids" interpretation for the `C2:3109` records was too broad.

The first byte of each record still behaves like an enemy id key:

- `84` -> `CUTE_LIL_UFO`
- `85` -> `BEAUTIFUL_UFO`

But the eight candidate bytes that follow now line up much better with the item table:

- record 0 candidates: `58 59 5A 5B 5C 5D 5F 00`
- record 1 candidates: `6A 6B 6C 6D 6E 6F 70 00`

Using the `ebsrc` item constants:

- `58` -> `COOKIE`
- `59` -> `BAG_OF_FRIES`
- `5A` -> `HAMBURGER`
- `5B` -> `BOILED_EGG`
- `5C` -> `FRESH_EGG`
- `5D` -> `PICNIC_LUNCH`
- `5F` -> `PIZZA`
- `6A` -> `CAN_OF_FRUIT_JUICE`
- `6B` -> `ROYAL_ICED_TEA`
- `6C` -> `PROTEIN_DRINK`
- `6D` -> `KRAKEN_SOUP`
- `6E` -> `BOTTLE_OF_WATER`
- `6F` -> `COLD_REMEDY`
- `70` -> `VIAL_OF_SERUM`

That makes the local table read naturally as:

- if a live `Cute Li'l UFO` is found, choose one item from a food/present set
- if a live `Beautiful UFO` is found, choose one item from a drink/medicine set

So the table is best understood as UFO-specific present contents, not as a linked enemy list.

## What this changes about `$AA10`

The downstream battle-text path already showed:

- `C2:6003` and `C2:8881` load `$AA10`
- `JSL C1:DD7C`
- then dispatch `MSG_BTL_PRESENT` or `MSG_BTL_CHECK_PRESENT_GET`

Since `C1:DD7C` is just the far wrapper around `C1:ACF8`, that means `$AA10` is copied into `$9D11` immediately before those present-family messages display.

The safest current interpretation is now:

- `$AA10` is very likely an item id or item-like present-content selector for this message family
- the `$9D11` substitution slot is then used by the display-text engine to expand a placeholder inside those messages

That is a better fit than "enemy-id-like substitution value."

## Current safest interpretation

The safest interpretation is:

- `C2:3109` keys off UFO enemy ids
- the candidate bytes in those records are item ids
- `$AA10` stores the selected UFO present item
- `C2:6003` and `C2:8881` feed that value into `$9D11` through `C1:DD7C`
- the resulting battle text is the `EBATTLE8` present-message family, especially `MSG_BTL_PRESENT` and `MSG_BTL_CHECK_PRESENT_GET`

## Best next target

The best next move is to pin the exact display-text placeholder case that reads `$9D11` in these present scripts, or to decode enough of `MSG_BTL_PRESENT` / `MSG_BTL_CHECK_PRESENT_GET` to say exactly where that item-like substitution appears in the player-visible line.

## Update: script control-flow map

A later local pass added a script dumper in [disasm_ebtext_script.py](/F:/Earthbound%20Decomp%20-%20Codex/tools/disasm_ebtext_script.py), which makes the structure of these present messages much clearer.

### `MSG_BTL_PRESENT`

The main script at `EF:7BDF` now reads like a real present-open flow:

- open with a short line, then halt
- `PLAY_SOUND 0x10`, which matches `PRESENT_OPENED`
- emit the central present line beginning with `@Insid...`
- `PRINT_ITEM_NAME 0x00`
- test inventory room with `GET_PLAYER_HAS_INVENTORY_ROOM 0xFF`
- if false, jump to `EF:7C73`, which matches `_BTL_PRESENT_FULL`
- otherwise continue into the normal give-item path
- the give-item path also has a conditional jump to `EF:7C42`, which matches `_BTL_PRESENT_DEAD`
- on the ordinary success branch, the script reaches `GIVE_ITEM_TO_CHARACTER_B 0x00, 0x00` and later prints the added-to-inventory line

So the message structure now lines up well with the `EBATTLE8` labels:

- main present line
- dead-target branch
- inventory-full branch
- give-item success line

### `MSG_BTL_CHECK_PRESENT_GET`

The `spy.asm` path uses `MSG_BTL_CHECK_PRESENT_GET`, and the local dump at `EF:7DD5` now shows it is the inspection/preview companion to `MSG_BTL_PRESENT`.

It contains:

- a lead line using `PRINT_ACTION_USER_NAME`
- `PLAY_SOUND 0x10` for the present-opening moment
- the same `@Insid...` core line
- `PRINT_ITEM_NAME 0x00`
- several short follow-up branches that each start with `PRINT_ACTION_USER_NAME` and end in their own `END_BLOCK`

So the safest current read is that `MSG_BTL_CHECK_PRESENT_GET` is not a duplicate of the ordinary open-present flow. It is a separate preview/check family used by Spy and related inspection logic.

## Update: exact `$9D11` bridge is now pinned

The remaining open point about the exact bridge is now resolved locally.

The present scripts use:

- `0x19 0x1F`
- `0x1B 0x04` -> `SWAP_WORKING_AND_ARG_MEMORY`
- `0x1C 0x05 0x00` -> `PRINT_ITEM_NAME 0`

A later local pass pinned the dispatcher around `C1:79F5..7A3A`, which shows:

- `0x1F -> C1:7AF3`

and `C1:7AF3` is already known to read `$9D11` through `C1:AD02`.

So the bridge is now concrete:

- `$AA10 -> C1:DD7C -> $9D11`
- `0x19 0x1F -> C1:7AF3`
- `0x1B 0x04` moves the loaded value into argument memory
- `PRINT_ITEM_NAME 0` prints the selected present item

That is the cleanest local end-to-end bridge we have so far for this battle-text substitution path.

## Update: the present path uses a generic byte-substitution loader

A later cross-segment scan showed that the present scripts are only one consumer of the `0x19 0x1F` loader.

That matters because it sharpens the wording here:

- `$AA10` is still best read as the UFO present item selector in this path
- but the downstream `$9D11 -> 0x19 0x1F` bridge is generic one-byte text substitution machinery, not a present-specific item printer hook

So the present family is now best described as a specific caller of a more general byte-substitution text pipeline.

See also [class2-cc19-1f-cross-segment-reuse.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-cc19-1f-cross-segment-reuse.md).
