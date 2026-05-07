# Text Command `0x0F` as Parameterized Working-Memory Increment Opcode

This note captures the current best local read of script byte `0x0F`.

See also [text-command-10-parameterized-pause.md](notes/text-command-10-parameterized-pause.md).
See also [text-commands-11-and-12-menu-and-line-control.md](notes/text-commands-11-and-12-menu-and-line-control.md).

## Main result

`0x0F` is not best read as an ordinary subcommand family.

The safest current local read is:

- `0x0F` is a single parameterized working-memory increment opcode
- the following byte is a numeric increment target or selector, not a family subcommand
- parser-side `0x0F xx` summaries are therefore mostly describing argument values, not runtime cases

## Working Names

- `C1:042E` = `IncrementCurrentTextContextWorkmem`

## Local parser proof

The ordinary top-level parser at `C1:890E` dispatches:

- `0x0F -> C1:8A81`

The `0x0F` leaf is tiny:

- `C1:8A81`: `JSR C1:042E ; JMP C1:8754`

So `0x0F` is a single command opcode with one fixed worker path, not a family root.

## Worker behavior at `C1:042E`

`C1:042E` does:

- resolves the current live text context through `C1:0301`
- adds `0x001F` to that context base
- reads the current word at that field
- increments it by one
- writes it back

So the safest current local read is: `0x0F` increments the current context's working-memory word at offset `+0x1F`.

This is strongly compatible with the inherited parser label `INCREMENT_WORKMEM`, and the local evidence is now good enough to promote that as the best current behavior label.

## Why parser-backed family summaries are misleading here

Tools that summarize `0x0F xx` as if they were ordinary family cases produce fake subcommand spreads.

That happens because:

- `0x0F` is one opcode with a following argument byte
- the second byte is not used as a runtime branch selector at the parser root
- ordinary scripts naturally use many different following bytes after the opcode

So the visible `0x0F 0A`, `0x0F 10`, and similar combinations should not be promoted into a case map.

## Confidence boundaries

### Locally proved

- `0x0F` dispatches directly to `C1:8A81`
- `C1:8A81` always calls `C1:042E`
- `C1:042E` increments the current live-context word at offset `+0x1F`

### Still open

- whether any script-side following byte after `0x0F` has separate meaning outside the ordinary parser path
- the nicest user-facing phrasing for the live-context field at `+0x1F`, which elsewhere behaves like a working-memory selector byte or slot word depending on context family

## Practical conclusion

Treat `0x0F` as a single parameterized working-memory increment opcode, not as the next adjacent bank-`01` family.
