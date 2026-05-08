# Bank `01` Text Command Map `00..1F`

This note is the current top-level map of the ordinary bank-`01` text command range `0x00..0x1F`.

See also [lower-bank01-text-control-strip-00-17.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/lower-bank01-text-control-strip-00-17.md).
See also [text-command-family-18-windows-and-selection.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-family-18-windows-and-selection.md).
See also [text-command-family-19-data-and-substitution.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-family-19-data-and-substitution.md).
See also [text-command-family-1a-menus.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-family-1a-menus.md).
See also [text-command-family-1b-memory-context.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-family-1b-memory-context.md).
See also [text-command-family-1c-print-display.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-family-1c-print-display.md).
See also [text-command-family-1d-inventory-money.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-family-1d-inventory-money.md).
See also [text-command-family-1e-stat-recovery.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-family-1e-stat-recovery.md).
See also [text-command-family-1f-deferred-callbacks.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-family-1f-deferred-callbacks.md).

## Main result

The ordinary bank-`01` text command range now reads as a coherent layered command map rather than a flat list of parser macros.

The strongest current high-level split is:

- `0x00..0x17` = low-level control, flag, branch, memory, and parser-side helper strip
- `0x18..0x1F` = structured higher families for windows, substitution/data, menus, memory/context, print/display, inventory/status, stat recovery, and deferred callbacks

A useful caution also survives at the top level: `0x15..0x17` are best treated as compressed-bank parser pseudo-opcodes, not ordinary runtime families.

## Lower control strip `00..17`

The current safest map for the lower strip is:

- `0x00` = `LINE_BREAK`
- `0x01` = `START_NEW_LINE`
- `0x02` = `END_BLOCK`
- `0x03` = `HALT_WITH_PROMPT`
- `0x04` = `SET_EVENT_FLAG`
- `0x05` = `CLEAR_EVENT_FLAG`
- `0x06` = `JUMP_IF_FLAG_SET`
- `0x07` = `CHECK_EVENT_FLAG`
- `0x08` = `CALL_TEXT`
- `0x09` = `JUMP_MULTI`
- `0x0A` = direct 24-bit `JUMP`
- `0x0B` = parameterized `TEST_IF_WORKMEM_TRUE`
- `0x0C` = parameterized `TEST_IF_WORKMEM_FALSE`
- `0x0D` = parameterized `COPY_TO_ARGMEM`
- `0x0E` = parameterized `STORE_TO_ARGMEM`
- `0x0F` = parameterized `INCREMENT_WORKMEM`
- `0x10` = parameterized `PAUSE`
- `0x11` = selection-menu setup helper
- `0x12` = line/menu display control helper
- `0x13` and `0x14` = the later halt/control pair through `C1:0166`
- `0x15..0x17` = compressed-bank parser pseudo-opcodes

So the lower strip is now much cleaner than the inherited parser view suggested: it is mostly a compact control and state-manipulation layer, not a set of mini-families.

## Structured family strip `18..1F`

The structured upper families now read as:

- `0x18` = windows and selection helpers
- `0x19` = data loading, substitution, fixed-width buffer selectors, and statistic selectors
- `0x1A` = menu and menu-display family
- `0x1B` = memory / context manipulation family
- `0x1C` = print / display family
- `0x1D` = inventory / money / storage / equipment helper family
- `0x1E` = HP/PP/stat recovery and stat-add family
- `0x1F` = deferred callback and event-helper family

The live family roots in the ordinary parser path are:

- `0x18` -> `C1:790B`
- `0x19` -> `C1:79AA`
- `0x1A` -> `C1:7B56`
- `0x1B` -> `C1:7C36`
- `0x1C` -> `C1:7D94`
- `0x1D` -> `C1:7F11`
- `0x1E` -> `C1:811F`
- `0x1F` -> `C1:81BB`

## Pairings and system shape

A few family pairings are now important enough to state at the top level:

- `0x1B` and `0x1C` are the core memory/display pair.
  `0x1B` manipulates live and saved text-context slots, while `0x1C` reads and displays from those slots.
- `0x09` and `0x0A` are the lower control-flow core.
  `0x09` is multi-way branch, and `0x0A` is direct 24-bit jump.
- `0x1D` and `0x1E` sit on top of the character/item/stat record families rather than acting like generic text helpers.
- `0x1F` is broader than timed delivery alone.
  It is the deferred-callback / event-helper family that also covers Jeff repair, magic-truffle direction, and wandering-photographer behavior.

## Best current interpretation

The safest current interpretation is that bank `01` text commands are now mapped well enough to be treated as a real runtime architecture:

- a low control strip at `0x00..0x17`
- a structured family strip at `0x18..0x1F`
- parser-only compressed-bank pseudo-opcodes at `0x15..0x17`

That gives the project a stable command-map backbone for future subsystem work instead of forcing every new text-engine question to start from raw opcode lists.
