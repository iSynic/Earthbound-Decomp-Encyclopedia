# Text Command Family `0x1D` (Inventory / Money / Checks)

This note captures the current local picture of the bank-`01` `0x1D` text-command family.

## Main result

`0x1D` is still best read as the inventory / money / possession-check family of the text engine.

The parser-backed summary is now much closer to a finished local map:

- `0x00` = `GIVE_ITEM_TO_CHARACTER` (2 hits)
- `0x01` = `TAKE_ITEM_FROM_CHARACTER` (22 hits)
- `0x02` = `CHECK_ITEM_BROAD_CLASS` (6 hits; old parser label was wrong)
- `0x03` = `GET_PLAYER_HAS_INVENTORY_ROOM` (94 hits; now locally supported)
- `0x04` = `CHECK_IF_CHARACTER_DOESNT_HAVE_ITEM` (1 hit)
- `0x05` = `CHECK_IF_CHARACTER_HAS_ITEM` (23 hits)
- `0x06` = `ADD_TO_ATM` (11 hits)
- `0x07` = `TAKE_FROM_ATM` (5 hits)
- `0x08` = `ADD_TO_WALLET` (18 hits)
- `0x09` = `TAKE_FROM_WALLET` (53 hits)
- `0x0A` = `GET_BUY_PRICE_OF_ITEM` (5 hits)
- `0x0B` = `GET_SELL_PRICE_OF_ITEM` (9 hits)
- `0x0C` = best current read: Escargo storage status check (10 hits)
- `0x0D` = `CHARACTER_HAS_AILMENT` (38 hits)
- `0x0E` = `GIVE_ITEM_TO_CHARACTER_B` (174 hits)
- `0x0F` = best current read: remove inventory item by slot and stage results (32 hits)
- `0x10` = best current read: test whether an item is currently equipped (0 exposed parsed hits)
- `0x11` = best current read: test whether the selected character can use/equip the selected inventory item (1 hit)
- `0x12` = best current read: store selected inventory item with Escargo (1 hit)
- `0x13` = best current read: withdraw stored item from Escargo (1 hit)
- `0x14` = `HAVE_ENOUGH_MONEY` (57 hits)
- `0x15` = `PUT_VAL_IN_ARGMEM` (30 hits)
- `0x17` = `HAVE_ENOUGH_MONEY_IN_ATM` (11 hits)
- `0x18` = best current read: add item id directly to Escargo storage (7 hits)
- `0x19` = `HAVE_X_PARTY_MEMBERS` (18 hits)
- `0x20` = `TEST_IS_USER_TARGETTING_SELF` (5 hits)
- `0x21` = `GENERATE_RANDOM_NUMBER` (17 hits)
- `0x22` = `TEST_IF_EXIT_MOUSE_USABLE` (1 hit)
- `0x23` = best current read: offensive-vs-nonoffensive equipment classifier (1 hit)
- `0x24` = best current read: fetch staged bank deposited-cash total (0 exposed parsed hits)

That distribution still looks exactly like an item/economy/status family: heavy shop and system use, lots of inventory-room and money checks, plus a smaller shop/storage adjunct tail and a very small battle-side tail.

## Important correction

An earlier revision of this note accidentally borrowed a large leaf block from the neighboring `0x1E` family. That has now been corrected.

The current top-level split is:

- `0x1D` routes through `C1:8AEC -> C1:7F11`
- `0x1E` routes through `C1:8AF4 -> C1:811F`
- `0x1F` routes through `C1:8AFC -> C1:81BB`

So the old `C1:49B6..76A7` leaf map was not `0x1D`; it was `0x1E`.

## Live parser anchor

The real local dispatcher for `0x1D` is `C1:7F11`.

Its current case map is:

- `0x1D 00` -> `C1:4C1E`
- `0x1D 01` -> `C1:4C86`
- `0x1D 02` -> `C1:48AC`
- `0x1D 03` -> `C1:4CEE`
- `0x1D 04` -> `C1:4D24`
- `0x1D 05` -> `C1:4D93`
- `0x1D 06` -> `C1:5C85`
- `0x1D 07` -> `C1:5D6B`
- `0x1D 08` -> `C1:48E9`
- `0x1D 09` -> `C1:494A`
- `0x1D 0A` -> `C1:4EF8`
- `0x1D 0B` -> `C1:4F33`
- `0x1D 0C` -> `C1:7058`
- `0x1D 0D` -> `C1:50E4`
- `0x1D 0E` -> `C1:5659`
- `0x1D 0F` -> `C1:56DB`
- `0x1D 10` -> `C1:575D`
- `0x1D 11` -> `C1:57CD`
- `0x1D 12` -> `C1:58A5`
- `0x1D 13` -> `C1:58FE`
- `0x1D 14` -> `C1:59F9`
- `0x1D 15` -> `C1:5BCA`
- `0x1D 17` -> `C1:5E5C`
- `0x1D 18` -> `C1:6124`
- `0x1D 19` -> `C1:6172`
- `0x1D 20` -> direct body at `C1:80A2`
- `0x1D 21` -> `C1:61F0`
- `0x1D 22` -> direct body at `C1:80DC`
- `0x1D 23` -> `C1:7708`
- `0x1D 24` -> `C1:7274`

Two negative results matter too:

- `0x1D 16` is not a live case in this dispatcher.
- `0x1D 1C` is not a live case in this dispatcher either, even though the script parser reports one exposed `EBATTLE8` hit.

That `0x1D 1C` hit now looks even less trustworthy than before. A direct sequence scan turns it into four raw `1D 1C` byte hits, three of them in the same dense `EBATTLE8` neighborhood, and the surrounding disassembly shows that two of those are simply the bytes spanning `COMPRESSED_BANK_1 0x1D` followed by `PRINT_SPECIAL_GFX 0x02`. So `0x1D 1C` should currently be treated the same way we treated the out-of-range `0x1E` hits: parser-side artifact or incidental raw bytes in a dense script block, not a proved runtime leaf.

## High-confidence subfamilies

### Item give/take and possession checks

The front half of the family is now split by confidence.

High-confidence locally anchored leaves:

- `0x00 GIVE_ITEM_TO_CHARACTER`
- `0x01 TAKE_ITEM_FROM_CHARACTER`
- `0x03 GET_PLAYER_HAS_INVENTORY_ROOM`
- `0x04 CHECK_IF_CHARACTER_DOESNT_HAVE_ITEM`
- `0x05 CHECK_IF_CHARACTER_HAS_ITEM`

Corrected front-half leaf:

- `0x02 CHECK_ITEM_BROAD_CLASS`

The important correction is that `0x02` is no longer just a local mismatch candidate. Its live leaf at `C1:48AC` resolves the current item through `C1:03DC`, passes that item id into [item-category-classifier-c19ee6.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/item-category-classifier-c19ee6.md), and compares the returned compact class code against the command argument. The shared field work in [item-byte-19-packed-class-and-slot.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/item-byte-19-packed-class-and-slot.md) now makes the intended behavior pretty clean: `0x1D 02` is testing the broad class encoded in item byte `+0x19`, not checking inventory capacity. The community control-code docs also agree with the ROM here by describing `[1D 02 XX]` as an item-type check over four broad classes, so the old parser label `GET_PLAYER_HAS_INVENTORY_FULL` should now be treated as incorrect rather than merely suspicious.

`0x03` no longer needs that level of caution. Its real leaf is `C1:4CEE`, and that body routes straight into [party-inventory-room-search-c456e4-c4572b.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/party-inventory-room-search-c456e4-c4572b.md), which is the first-empty-slot mirror of the `0x05` possession search family. So the parser label `GET_PLAYER_HAS_INVENTORY_ROOM` is now locally supported instead of only script-backed.

Two script anchors still make this cluster feel solid at the family level:

- In `C9:CD39`, `GIVE_ITEM_TO_CHARACTER 0xFF, 0x64` is immediately followed by character-number setup and a printed reward line.
- In `C7:616F`, `GET_PLAYER_HAS_INVENTORY_ROOM 0xFF` gates `GIVE_ITEM_TO_CHARACTER_B 0x00, 0x58`, which is a very clean "check room, then award item" pattern and now matches the local wildcard room-search helper exactly.

The local leaves are stronger now too:

- `0x00 -> C1:4C1E` is the simple insertion wrapper. It resolves the character and item arguments from the live text context, calls [inventory-slot-insertion-helper-c18bc6.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/inventory-slot-insertion-helper-c18bc6.md), and stages the resulting recipient character id through `C1:045D`.
- `0x01 -> C1:4C86` is the take-side search/removal wrapper. It resolves the character and item arguments, calls [inventory-slot-search-removal-helper-c18e5b-c18ead.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/inventory-slot-search-removal-helper-c18e5b-c18ead.md), and stages the resulting source character id through `C1:045D`.
- `0x03 -> C1:4CEE` is the positive inventory-room search path. It resolves an explicit or wildcard holder selector, routes through [party-inventory-room-search-c456e4-c4572b.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/party-inventory-room-search-c456e4-c4572b.md), and stages the resulting character id with room through `C1:045D`.
- `0x04 -> C1:4D24` now looks like the negative form of an item-possession/equipment predicate. It resolves a character/item pair and routes through `C3:E9F7`, then stages the resulting boolean through `C1:045D`.
- `0x05 -> C1:4D93` is the positive item-possession search path. It resolves an explicit or wildcard holder selector, routes through [party-item-possession-search-c45637-c45683.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/party-item-possession-search-c45637-c45683.md), and stages the resulting holder character id through `C1:045D`. At script level `CHECK_IF_CHARACTER_HAS_ITEM` is still a good label, but the low-level return value is the first matching holder id rather than a pure boolean.
- `0x0E -> C1:5659` is the richer award variant. It also inserts through `C1:8BC6`, but then immediately calls `C2:2351` to resolve the first empty slot in the recipient inventory and stages both the slot index and recipient id through the paired `C1:0489` / `C1:045D` text-context installers.

So the parser names `GIVE_ITEM_TO_CHARACTER`, `TAKE_ITEM_FROM_CHARACTER`, `GET_PLAYER_HAS_INVENTORY_ROOM`, `CHECK_IF_CHARACTER_HAS_ITEM`, and `GIVE_ITEM_TO_CHARACTER_B` are now locally supported as real insertion/search-removal wrappers rather than just script-side labels, and `0x02` is best promoted under a corrected local name like `CHECK_ITEM_BROAD_CLASS`.

A useful supporting cross-check from the community documentation now lines up with the local ROM behavior too: the documented `0x1D 02` classes match the broad `+0x19 & 0x30` split unusually well, with class `2` as equippable gear and the other classes dividing general items, edible items, and other usable items. That is still reference-backed rather than fully local semantic proof, but it makes the low-level correction much safer.

### Money / ATM / wallet checks

The middle cluster still holds together naturally:

- `0x06 ADD_TO_ATM`
- `0x07 TAKE_FROM_ATM`
- `0x08 ADD_TO_WALLET`
- `0x09 TAKE_FROM_WALLET`
- `0x0A GET_BUY_PRICE_OF_ITEM`
- `0x0B GET_SELL_PRICE_OF_ITEM`
- `0x14 HAVE_ENOUGH_MONEY`
- `0x17 HAVE_ENOUGH_MONEY_IN_ATM`

One especially clean script bridge is still `C6:5DA6`:

- `HAVE_ENOUGH_MONEY 00:1D4C`
- `JUMP_IF_TRUE ...`
- `TAKE_FROM_WALLET 0x1D4C`
- `SHOW_WALLET_WINDOW`

The local money leaves are now better pinned too:

- `0x14 -> C1:59F9` is a real three-byte amount comparator over queued `$97BA/$97BB/$97BC` data, ending in a compare against live wallet-side state at `$9831/$9833` and staging a boolean result through `C1:045D`.
- `0x17 -> C1:5E5C` is the parallel ATM-side comparator, using the same queued amount shape but comparing against `$9835/$9837` before staging the result.

So `HAVE_ENOUGH_MONEY` and `HAVE_ENOUGH_MONEY_IN_ATM` are now locally stronger than before, not just parser-backed labels.

### Status / party-count / battle-adjunct checks

Some of the later checks are now locally stronger too:

- `0x0D CHARACTER_HAS_AILMENT` remains a good fit from parser use and its real leaf `C1:50E4`.
- `0x19 HAVE_X_PARTY_MEMBERS` is now a strong local fit: `C1:6172` compares the requested count against `$98A4` and stages a boolean result.
- `0x20 TEST_IS_USER_TARGETTING_SELF` still looks right from parser use, and the direct body at `C1:80A2` resolves two battle-side helpers through `C1:ACF2`, `C1:AC9B`, and `C1:4070` before staging a boolean.
- `0x21 GENERATE_RANDOM_NUMBER` now has a real local leaf at `C1:61F0`, which feeds the selected bound through `C4:5F7B` and stages the result.
- `0x22 TEST_IF_EXIT_MOUSE_USABLE` now has a direct local body at `C1:80DC`: it reads the current tile/context class from `C0:0AA1`, checks for class `2`, and stages a boolean result.

### `0x15 = PUT_VAL_IN_ARGMEM`

This one still has a nice local script anchor that does not depend on the earlier dispatcher mistake. In `C8:21B2`, `PUT_VAL_IN_ARGMEM 0x0005` is followed by `SWAP_WORKING_AND_ARG_MEMORY` and then `PRINT_NUMBER 00:0000`. That is a strong behavioral fit for the macro name.

Its real leaf is now pinned too:

- `0x15 -> C1:5BCA`

That body is no longer just abstract. It stages one queued byte, combines it with converted numeric payload bytes, then routes through `C2:26F0` and `C0:9086` before installing the result into the active text context. So the parser name still fits the script-level behavior, even though the exact low-level install shape is richer than a trivial setter.

## Revalidated edge cases

### `0x1D 0C`

`0x1D 0C` now has a real live leaf at `C1:7058`, and it looks much more specifically like an Escargo storage eligibility classifier than a generic shop predicate.

The local body:

- resolves a current/argument character and inventory-slot pair through the usual `C1:040A` / `C1:03DC` slot family
- calls `C1:90F1` and turns its result into either `0` or `2`
- fetches the selected inventory item through the character inventory record and then reads item-table byte `+0x1C`
- tests item bit `0x40` and turns that into either `0` or `1`
- ORs those two components together and stages the final value through `C1:045D`

That makes the return-value structure much clearer than before:

- `0` = item is storable and storage has room
- `1` = item is not storable but storage has room
- `2` = item is storable but storage is full
- `3` = item is not storable and storage is full

`C1:90F1` itself now reads cleanly as the storage-capacity side of that split. It starts from `#$0024`, subtracts one for each nonzero byte in `$98AB[0..2]`, then scans `$984B` until it reaches either the first zero slot or the remaining capacity limit. It returns `1` only when no free queue entry exists within that remaining capacity, which is exactly the shape we would expect for a "storage full" bit.

The script distribution lines up with that unusually well. This command is almost entirely confined to `ESHOP3`, and the hits cluster around Escargo-style request, refusal, and follow-up branches, including the path that sets `flag 0x0285` and triggers timed event row `0x03`. The community control-code docs also match the local return structure closely by describing `0x1D 0C` as "Check If Item Can Be Stored By Escargo Express."

So the safest current read is no longer just "small service/item classifier." `0x1D 0C` is a compact Escargo storage result code composed from one live storage-capacity bit and one per-item storable/not-storable bit from item byte `+0x1C` bit `0x40`.

### `0x1D 23`

`0x1D 23` now has a good local read from its live leaf at `C1:7708`.

That body:

- resolves an explicit or active-context item id
- reads item byte `+0x19` from `D5:5000`
- masks it with `0x0C`
- returns `1` for subtype `0x00`
- returns `2` for subtypes `0x04`, `0x08`, or `0x0C`
- returns `0` otherwise

So the safest current model is [offensive-defensive-item-check-c17708.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/offensive-defensive-item-check-c17708.md): this is a compact equipment-subtype collapse, not a generic item predicate. The only exposed script hit is in `ESHOP1`, and the community control-code description matches the local split unusually well by describing it as an offensive-versus-defensive equipment check. That wording should still stay reference-backed, but it is now much safer than the older `UNKNOWN_1D_23` placeholder.

### `0x1D 0F`

`0x1D 0F` now has its real leaf at `C1:56DB`, and it no longer reads best as a vague follow-up resolver. The safest current read is: remove the selected inventory item by slot, stage the removed item id in arg memory, and stage the source character id in working memory.

The local body now lines up unusually well with that reading:

- it resolves a character selector through `C1:040A` / working memory and an inventory-slot selector through `C1:03DC` / arg memory
- it calls `C3:E977`, which fetches the item id currently stored in that character's selected inventory slot
- it stages that fetched item id through `C1:0489`
- it then calls `C1:8C27`, the live inventory-slot removal helper, which removes that slot from the character inventory and returns the source character id
- it stages that returned character id through `C1:045D`

This is also one of the nicer local-plus-reference matches in the family. The community control-code docs describe `[1D 0F XX YY]` as removing character `XX`'s `YY`th inventory item, then setting working memory to the source character id and arg memory to the removed item id. That is exactly the shape the ROM now shows.

The script distribution also makes better sense under that model. This command appears across `E09DSRT`, `ESHOP1`, `ESHOP3`, `EGOODS2`, and `ESYSTEM`, and many of those hits sit in exactly the sort of "take the selected item out, then talk about what happened to it" neighborhoods where a staged removed-item id plus source character id is the useful pair.

So `0x1D 0F` is now best treated as the slot-based removal counterpart to `0x1D 0E`, not as another soft service-side helper.


### `0x1D 10`

`0x1D 10` now has a much better local role than before. Its real leaf is `C1:575D`, and that body resolves a character/item pair, supports the same explicit-versus-wildcard target split as the other inventory helpers, and forwards the actual test to [equipped-item-presence-predicate-c3e9a0.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/equipped-item-presence-predicate-c3e9a0.md).

That bank-`03` helper, `C3:E9A0`, is no longer vague. It checks the selected character's four adjacent bytes at `$99FF..$9A02` and returns `1` if any one of them matches the requested item id, otherwise `0`. Combined with the already-mapped four-slot equipment compatibility helper `C3:EE14`, the safest current read is that those four bytes are the equipped item-id slots for the character record.

So the safest command-level reading is: test whether the selected character, or anyone in the active wildcard family, currently has the requested item equipped.

### `0x1D 11`

`0x11 -> C1:57CD` now reads much more directly than it used to. It is no longer best treated as a vague post-award follow-up helper. The safest current read is: direct inventory-item usability/equipability check.

The local body:

- resolves one selector through `C1:040A` / working memory and one through `C1:03DC` / arg memory
- uses `C3:E977` to fetch the item id currently stored in the selected character's selected inventory slot
- passes that fetched item id into `C3:EE14` together with the selected character/slot side
- stages the boolean result through `C1:045D`

That fits the helper pair unusually well now that both halves are pinned:

- `C3:E977` is a compact character inventory-slot byte accessor
- `C3:EE14` is a four-slot equipment-compatibility predicate over item byte `+0x1C`

The script-side picture matches too. Its only exposed hit is still the `ESHOP1` one-off immediately after `GIVE_ITEM_TO_CHARACTER_B`, and the following script block is clearly the equip/stat follow-up narration. The community control-code docs also line up closely here by describing `0x1D 11` as checking whether character `XX` can use the `YY`th item in their inventory.

So the safest current command-level wording is: check whether the selected character can use or equip the selected inventory item. In this shop context, that is exactly the prelude the narration would need before choosing the later equipment/stat-change text.

### `0x1D 12/13`

These now read like a real Escargo storage transfer pair rather than a vague service-side subfamily.

- `0x12 -> C1:58A5`
- `0x13 -> C1:58FE`

The strongest shared local anchor is the packed pending-item queue rooted at `$984B`; see [pending-item-queue-984b.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/pending-item-queue-984b.md). The community control-code docs also line up unusually well here: `[1D 12 XX YY]` is described as immediately storing character `XX`'s `YY`th item with Escargo Express, and `[1D 13 XX YY]` as immediately withdrawing stored item `YY` and giving it to character `XX`.

`0x12 -> C1:58A5` is now strong. It resolves the same item pair, then calls `C1:9183`. That helper uses `C1:913D` to insert the resolved item id into the first free entry of the `0x24`-entry `$984B..$986E` queue, and on success routes through `C1:8C27`, which removes the corresponding entry from the source character inventory while maintaining the four live equipment-slot indices; see [inventory-slot-removal-helper-c18c27.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/inventory-slot-removal-helper-c18c27.md). Combined with its lone `ESHOP3` hit right after `COPY_STORAGE_MEMORY_TO_ACTIVE`, the safest current read is: immediately store one source inventory item with Escargo Express.

`0x13 -> C1:58FE` now has the cleanest player-visible bridge. It resolves the selected pair, then calls `C1:91F8` and `C2:2351`. `C1:91F8` removes one 1-based entry from the same packed `$984B` item-id queue, compacts the remaining bytes left, then forwards the removed item id into `C1:8BC6`, the insertion-side mirror of `C1:8C27`; see [inventory-slot-insertion-helper-c18bc6.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/inventory-slot-insertion-helper-c18bc6.md). `C2:2351` scans the selected recipient's item area for the first empty slot. The leaf stages one result through `C1:0489` and the other through `C1:045D`, and its only exposed `ESHOP3` use is followed immediately by `ADD_ITEM_ID_TO_WORK_MEMORY 0x00, 0x00` and `PRINT_ITEM_NAME 0x00`. So the safest current read is: immediately withdraw one stored item and give it to the destination inventory.

### `0x1D 18`

`0x18` now has a much cleaner local role than before. Its real leaf is `C1:6124`, and that body either takes the explicit command argument or falls back to arg memory, then passes that item id straight to `C1:913D`.

`C1:913D` is now a firm queue-insertion helper over the packed `0x24`-entry `$984B..$986E` item-id block; see [pending-item-queue-984b.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/pending-item-queue-984b.md). It stores the selected item id into the first free slot and returns success only when a free entry exists. That matches both the `ESHOP3` script neighborhoods and the community control-code wording unusually well: `[1D 18 XX]` is described as adding item `XX` to Escargo Express inventory.

So the safest current read is: `0x18` is the queue-add side of the same service-side pending-item family as `0x12/0x13`, not a generic customer predicate.

### `0x1D 24`

`0x1D 24` is now in much better shape. Its live leaf is `C1:7274`, and the best current model is [bank-deposit-accumulator-98b9-98bb.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/bank-deposit-accumulator-98b9-98bb.md): it stages the cached 32-bit value at `$98B9/$98BB` through `C1:045D`, and command argument `2` clears that accumulator after staging it.

The local writer side is what corrected the old model. Bank-`C2` code at `C2:5F3D..5F7D` and `C2:6279..62B9` is doing real arithmetic on `$98B9/$98BB`, adding converted 16-bit amounts into it as a dword total. That is a much better fit for the `ESHOP3` script neighborhood too:

- `0x24 01` gates the `deposited $... to your bank account` line
- `0x24 02` then fetches and clears the same value for the following narration branch

So the safest current read is no longer a pointer-loader guess. `0x1D 24` now looks like a bank deposited-cash total fetcher with optional clear-on-consume behavior. The community control-code description is strongly consistent with that local model, even though the exact player-facing wording should still be treated as reference-backed.

## What is still tentative

The biggest remaining open group is now much smaller.

The remaining uncertainty is now very small:

- `0x1D 1C` stays explicitly excluded rather than open: the real runtime dispatcher has no such case, and the exposed parser hit now looks like an incidental raw-byte artifact in dense battle text


## Best current interpretation

The safest current read is still that `0x1D` is the text engine's inventory / money / possession-check family, with shop/storage and battle-adjunct tails. The difference now is that most of the family is locally anchored to the true `C1:7F11` dispatcher: the money checks, give/take helpers, possession and room searches, equipped-item tests, storage classifier, bank-deposit fetch, party-count check, exit-mouse predicate, random-number helper, and the small service-side pending-item subfamily all sit on real bank-`01` leaves instead of inherited guesses from neighboring families.


