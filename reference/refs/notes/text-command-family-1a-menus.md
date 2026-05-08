# Text Command Family 1A Menus

This note captures the current best local map for bank-`01` text command family `0x1A`.

See also [text-command-family-1d-inventory-money.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-family-1d-inventory-money.md).
See also [text-command-family-1e-stat-recovery.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-family-1e-stat-recovery.md).
See also [jeff-repair-item-name-bridge.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/jeff-repair-item-name-bridge.md).

## Main result

`0x1A` now reads as the bank-`01` menu and selection-command family.

The ordinary script parser routes it through:

- top-level text parser `C1:890E`
- `0x1A -> C1:8AD4`
- callback family root `C1:7B56`

The live ordinary-script case map at `C1:7B56` currently covers:

- `0x00`
- `0x01`
- `0x04`
- `0x05`
- `0x06`
- `0x07`
- `0x08`
- `0x09`
- `0x0A`
- `0x0B`

So the safest current read is that `0x1A` is the family for current-party selection menus, inventory/shop menus, the Escargo item list, the phone menu, and the teleport menu.

## Local dispatcher proof

The ordinary parser side is straightforward:

- `C1:890E` dispatches top-level text families
- `0x1A` jumps to `C1:8AD4`
- `C1:8AD4` installs callback low word `C1:7B56`

Then `C1:7B56` dispatches on the family subopcode in `X`.

The live local `C1:7B56` case map is:

- `0x00 -> C1:463B`
- `0x01 -> C1:467D`
- `0x04 -> C1:7BA5 -> C1:196A(0) + C1:1383`
- `0x05 -> C1:549E`
- `0x06 -> C1:4EB5`
- `0x07 -> C1:7BC9 -> C1:9A43`
- `0x08 -> C1:7BDD -> C1:196A(0)`
- `0x09 -> C1:7BF4 -> C1:196A(1)`
- `0x0A -> C1:AC00`
- `0x0B -> C1:AAFA`
- default -> `0`

## Best current case map

### `0x1A 00`

Best current read:

- current party member selection menu, no cancel

Confidence:

- reference-backed and locally consistent

Why:

- the ordinary runtime dispatcher does have a real `0x00` case
- the paired `0x01` scripts do show a real false branch after menu return, which makes the `0x00 = no-cancel` reading healthier than the current parser/YAML labels alone
- community docs describe `0x1A 00` as the no-cancel current-party member selection menu

Caution:

- the only currently exposed parsed hit in `EEVENT0` sits inside a dense teleport or story-event neighborhood and is not especially illuminating on its own
- the immediate leaf is the generic queue builder `C1:463B`, so the user-facing menu identity here still rests more on family pairing and docs than on a directly named local menu routine

### `0x1A 01`

Best current read:

- current party member selection menu

Confidence:

- strong script-context fit; reference-backed and locally consistent

Why:

- exact parsed hits in `EDEBUG` and `ESHOP1`
- those scripts immediately branch on success/failure and then follow up with character-inventory and character-specific logic
- community docs describe `0x1A 01` as the cancellable sibling of `0x1A 00`
- the current parser/YAML label names `0x1A 01` as the uncancellable variant, but the local script behavior looks more like the docs than the inherited label

Caution:

- like `0x00`, the immediate leaf is a generic queue builder (`C1:467D`), so the menu identity is stronger at the script/use level than at the leaf-name level

### `0x1A 04`

Best current read:

- selection menu, no cancelling

Confidence:

- reference-backed and locally consistent

Why:

- live case exists
- it goes through `C1:196A(0)` plus the same staging path used by other selection-oriented cases
- community docs describe `0x1A 04` that way

Caution:

- no exact currently exposed parsed hits

### `0x1A 05`

Best current read:

- show character inventory

Confidence:

- locally strong

Why:

- exact parsed hits in `E09DSRT` and `ESHOP1`
- script arguments behave like `window, character`
- community docs explicitly match the observed usage
- local handler `C1:549E` manages a queued character byte, interacts with the current active object/context family, and then dispatches through `C1:98DE`

### `0x1A 06`

Best current read:

- display shop menu

Confidence:

- locally strong

Why:

- many exact parsed hits
- scripts use it in obvious shop/menu flows
- local handler `C1:4EB5` snapshots/restores menu context, uses the active interaction object, and stages a result through `C1:9DB5`

### `0x1A 07`

Best current read:

- display Escargo Express items

Confidence:

- strong script-context fit; reference-backed and locally consistent

Why:

- only exposed exact hits are in `ESHOP3`
- those scripts immediately move into stored-item selection, item-name printing, and Escargo-specific follow-up
- local handler `C1:9A43` snapshots menu context, iterates the packed stored-item queue at `$984B`, stages per-item strings into the text context, and then returns through `C1:196A(1)` into the shared current-party selection infrastructure
- the strongest current local fit is therefore narrower than generic 'display items': this is the Escargo stored-item selection menu

### `0x1A 08`

Best current read:

- selection menu with persistent strings, no cancelling

Confidence:

- reference-backed and locally consistent

Why:

- live case exists
- it reuses the `C1:196A(0)` selection-side entry without the extra `C1:1383` side call from `0x04`
- community docs describe it as the persistent-strings no-cancel variant

Caution:

- no exact currently exposed parsed hits

### `0x1A 09`

Best current read:

- selection menu with persistent strings

Confidence:

- reference-backed and locally consistent

Why:

- live case exists
- it is the `C1:196A(1)` sibling of `0x08`
- community docs describe it as the cancellable persistent-strings variant

Caution:

- no exact currently exposed parsed hits

### `0x1A 0A`

Best current read:

- open phone menu / make phone call

Confidence:

- locally strong

Why:

- exact parsed hits appear in `ESHOP3`
- local handler `C1:AC00` calls `C1:9441`, resolves a contact-table entry under `D5:7A8F`, stages the selected result into text memory, and invokes `C1:86B1`
- community docs describe the returned working-memory value as the called contact id, or `0` if none was called

### `0x1A 0B`

Best current read:

- display teleport menu

Confidence:

- locally strong

Why:

- live case routes directly to `C1:AAFA`
- `C1:AAFA` snapshots/restores menu context, builds visible strings from teleport-destination data at `D5:7880`, and runs the same selection-side infrastructure as other menu families
- `C1:AAFA` is also reused by non-text code at `C1:B76E`, which reinforces that it is a standalone teleport-menu helper rather than a tiny script-only adapter

## Sparse out-of-range parser hits

The parser still exposes a few rare `0x1A` subcodes outside the live ordinary dispatcher:

- `0x02`
- `0x0E`
- `0x15`
- `0x16`
- `0x17`

The ordinary runtime dispatcher at `C1:7B56` has no cases for them.

These are now best split into two softer buckets instead of one generic unresolved tail.

More plausible alternate-path or interpreter-oddity candidates:

- `0x02` appears in `EDEBUG` immediately before a real horizontal-string print plus `CREATE_SELECTION_MENU` flow
- `0x0E` appears in `E11SUMS` inside a structured story-event or movement block, immediately after `CHANGE_TPT_ENTRY_DIRECTION`

Stronger parser-desync or non-ordinary-flow candidates:

- `0x15` appears in `ESHOP2` immediately after `TELEPORT_TO 16:022B` and before a prompt block, which is less healthy as an ordinary menu-family use
- `0x16/0x17` appear in `E05THRK` as a paired story-event sequence tightly interleaved with `CHANGE_TPT_ENTRY_DIRECTION`, `END_BLOCK`, prompt pauses, and floating-sprite deletion or appearance commands

So the safest current treatment is:

- do not promote any of these to ordinary `0x1A` runtime commands yet
- keep `0x02/0x0E` as possible alternate-path or non-ordinary interpreter cases
- treat `0x15/0x16/0x17` more skeptically as likely parser-desync or other non-ordinary-flow artifacts until a real local consumer is found

## Current safest interpretation

The safest current interpretation is:

- `0x1A` is the bank-`01` text-command family for menu-opening and selection flows
- the stable live center of the family is:
  - current-party selection
  - inventory display
  - shop menu display
  - Escargo item display
  - phone menu
  - teleport menu
- the no-hit `0x04/0x08/0x09` cases are still worth keeping, but only as reference-backed and locally consistent labels

## Best next target

The best next move is to decide whether the sparse parser-only `0x1A 02/0E/15/16/17` cases are genuine alternate-path commands or just another class of parser artifacts.
