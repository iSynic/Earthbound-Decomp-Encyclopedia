# Text Commands `0x11` and `0x12` as Single Menu/Line Control Opcodes

This note captures the current best local read of script bytes `0x11` and `0x12`.

See also [text-commands-13-and-14-halt-control.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-commands-13-and-14-halt-control.md).
See also [text-command-family-1a-menus.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-family-1a-menus.md).

## Main result

`0x11` and `0x12` are not ordinary bank-`01` subcommand families.

The safest current local read is:

- `0x11` is a single selection-menu setup opcode routed through `C1:8A8F`
- `0x12` is a single line-clear or display-reset opcode routed through `C1:8AAA`
- the parser-side `0x11 xx` and `0x12 xx` spreads are mostly the next byte being misread as if these were family roots

So these should currently sit next to `0x13/0x14` as single control-style commands, not as the next ordinary families below `0x1A`.

## Local parser proof

The ordinary top-level parser at `C1:890E` dispatches:

- `0x11 -> C1:8A8F`
- `0x12 -> C1:8AAA`

Neither command installs a family callback low word in `$1E`.

That is the key structural difference from ordinary families like `0x18`, `0x19`, `0x1A`, `0x1D`, `0x1E`, or `0x1F`.

## `0x11` local behavior

The `0x11` leaf at `C1:8A8F` does:

- `LDA #$0001`
- `JSR C1:196A`
- stages the returned pointer pair into `$0E/$10` through `$06/$08`
- `JSR C1:045D`
- `JSR C1:1383`
- returns through the normal parser exit path

So the safest current local read is that `0x11` is a single selection-menu setup helper that builds or installs one prepared menu-side text context.

This is directionally consistent with the inherited parser name `CREATE_SELECTION_MENU`, but the local proof is stronger on "single menu-setup opcode" than on any broader subcommand-family interpretation.

## `0x12` local behavior

The `0x12` leaf at `C1:8AAA` is even smaller:

- `JSR C1:0BD3`
- return through the normal parser exit path

`C1:0BD3` then:

- resolves the live text context through `$8958 -> $88E4 -> C08FF7 -> $8650`
- calls `C4:3739`
- resolves the current context-specific display object through `$8660`
- calls `C4:38A5` with `A = 0`

So the safest current local read is that `0x12` is a single line-clear or display-reset opcode affecting the current active text display line or display object, not a family root.

That remains nicely compatible with the inherited parser name `CLEAR_TEXT_LINE`, but the local structural conclusion is the important part: it is one command, not a subcommand family.

## Why parser-backed family summaries are misleading here

Tools that summarize `0x11 xx` or `0x12 xx` as if they were ordinary families produce fake subcommand spreads.

That happens because:

- `0x11` and `0x12` are single opcodes, not family roots
- the parser summaries are reading the following byte as if it were a family subopcode
- those following bytes vary naturally across event and battle text payloads

So the visible `0x11 xx` and `0x12 xx` spreads should not be promoted into runtime family maps.

## Confidence boundaries

### Locally proved

- `0x11` dispatches directly to `C1:8A8F`
- `0x12` dispatches directly to `C1:8AAA`
- neither command installs a family callback root in `$1E`
- `0x11` uses `C1:196A`, `C1:045D`, and `C1:1383` in one fixed helper path
- `0x12` uses `C1:0BD3` in one fixed helper path

### Still open

- the exact user-facing phrasing for `0x11` beyond "selection-menu setup"
- whether `C4:3739` and `C4:38A5` are best named as current-line clear, text-window clear, or a slightly broader display-object reset pair

## Practical conclusion

Treat `0x11` and `0x12` as single menu/line control opcodes, not as the next adjacent bank-`01` text-command families to map.
