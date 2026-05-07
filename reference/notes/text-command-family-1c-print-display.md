# Text Command Family `1C`: Print / Display

This note is the top-level overview for bank-`01` text command family `0x1C`.

See also [jeff-repair-item-name-bridge.md](notes/jeff-repair-item-name-bridge.md).

## Main result

The safest current local read is that `0x1C` is the broad bank-`01` print / display family.

In the live parser path, top-level command byte `0x1C` dispatches through `C1:8AE4`, which installs callback low word `C1:7D94`. The body at `C1:7D94` then dispatches on the one-byte `0x1C` subselector in `X`.

## Best current family shape

The currently strongest pinned `0x1C` leaves are:

- `0x1C 01` -> best current fit `PRINT_STAT`
- `0x1C 02` -> best current fit `PRINT_CHAR_NAME`
- `0x1C 03` -> best current fit `PRINT_CHAR`
- `0x1C 05` -> `PRINT_ITEM_NAME`
- `0x1C 06` -> best current fit town / teleport-destination name printer
- `0x1C 07` -> best current fit horizontal text-string printer
- `0x1C 08` -> battle-only special-graphics print branch
- `0x1C 0A` -> best current fit `PRINT_NUMBER`
- `0x1C 0C` -> best current fit vertical text-string printer
- `0x1C 0D` -> strong local fit `PRINT_ACTION_USER_NAME`
- `0x1C 0E` -> strong local fit `PRINT_ACTION_TARGET_NAME`
- `0x1C 0F` -> strong local fit `PRINT_ACTION_AMOUNT`
- `0x1C 12` -> strong local fit `PRINT_PSI_NAME`
- `0x1C 13` -> strong local fit `DISPLAY_PSI_ANIMATION`
- `0x1C 14/15` -> special selector loaders used before `JUMP_MULTI`

Some edge leaves remain narrower or more cautious:

- `0x1C 09` is now named `SET_ACTIVE_WINDOW_TEXT_MODE`; it is runtime-only in the exposed `text_data` corpus, but its live write to `$8662` is pinned
- `0x1C 00` and `0x1C 0B` are real live-context setters or printers, but their exact player-facing names are still weaker than the central print paths
- `0x1C 11` is still a narrow special-selector loader without a clean final name

## Why this family matters

`0x1C` is the display side of the paired `0x1B / 0x1C` text-engine model.

The clearest local example is Jeff repair:

- `0x1B` changes live text-memory / context slots
- `0x1C 05` reads from those slots through the item-name printer
- `{swap}` plus repeated `[1C 05 00]` prints broken-item first, then repaired-item, without changing the visible item-name selector

So the best current system-level read is that `0x1C` is not a grab-bag of unrelated helpers. It is the main print/data-display family that consumes the current bank-`01` text context.

Source polish update: the `0x1C 0F` branch inside
`src/c1/c1_7b56_dispatch_display_text_dynamic_source_selector.asm` now names
the getter through `C1:AD26`, the `$9D12/$9D14` staged action-amount payload,
the handoff into `$0E/$10`, and the final `C1:0DF6` number printer. This
matches the `C1:DC66` display wrapper contract used by C2 amount-result
callers.

Follow-up source polish also names the adjacent battle-name display pair. The
`0x1C 0D/0E` leaves now show the `C3:E75D` reflected-hit side article-token
setup, `C1:AC9B/C1:ACF2` attacker/target name-buffer base reads, and the
`C4:47FB` fixed-string preflight printer by contract names.

The decoded `C1:7D94` dispatcher now carries the front `0x1C` contract
directly too. Its jump ladder names the stable `0x1C 01..0F` and `0x1C 11..15`
subselector ids, while the battle-name pair names the user/target side
selector values, the `$06/$08/$09` staged name-buffer pointer, the `$0E/$10`
text-context handoff, the fixed-string preflight length, and the no-follow-up
return value.

Follow-up source polish now covers the front display leaves in
`src/c1/c1_4eab_handle_text_command10_parameterized_pause.asm` as well. The
`0x1C 02`, `0x1C 0A`, `0x1C 0B`, and `0x1C 14/15` paths name the character
label printer, decimal and right-aligned money printers, special-selector
context installers, party-count checks, and text-event snapshot helper edges,
leaving that corridor byte-equivalent and free of raw helper calls.

The adjacent `C1:575D..621F` source unit now names the `0x1C 0C` vertical text
layout helper and the `0x1C 12` PSI-name printer edge directly. This keeps the
front display-family source readable while the broader `0x1D/0x19` inventory
and queue helpers continue to carry most of the module's behavior.

Follow-up source polish now names the deferred-byte ABI inside the
`0x1C 0A/0B` numeric display leaves themselves. `PRINT_NUMBER` and
`PRINT_MONEY_AMOUNT` both assemble queued bytes from `$97BA..$97BC` plus the
caller byte before falling back to the next text argument when that assembled
value is zero; their callback low words are now source aliases rather than raw
`C1:53AF` / `C1:5573` literals.

Follow-up source polish now carries that display contract into the caller-frame
scratch slots as well. In `C1:4EAB..575D`, `PRINT_NUMBER` and
`PRINT_MONEY_AMOUNT` hand their assembled or fallback values to the decimal
printers through named `$0E/$10` decimal-source aliases, while the adjacent
`0x1C 14/15` special-selector loaders and `0x18 08/09` selection helpers
install their results through named text-context source aliases.

Follow-up source polish now names the `0x1C 13` battle visual-effect staging
leaf in `src/c1/c1_7274_stage_bank_deposit_accumulator_text_value.asm`. The
source exposes the queued visual token, actor selector, blinking-prompt gate,
`C3:FAC9` dispatch, and signed `$06/$08 -> $0E/$10` result installation.

## Best current interpretation

The safest current interpretation is that `0x1C` is the bank-`01` print / display family, covering ordinary text substitution, item and character naming, numeric/stat printing, and a narrower battle-facing action / PSI display tail.
