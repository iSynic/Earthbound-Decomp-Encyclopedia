# Text Command `0x0E` as Parameterized Store-To-Argmem Opcode

This note captures the current best local read of script byte `0x0E`.

See also [text-command-0f-parameterized-workmem-increment.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-0f-parameterized-workmem-increment.md).
See also [text-commands-11-and-12-menu-and-line-control.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-commands-11-and-12-menu-and-line-control.md).

## Main result

`0x0E` is not best read as an ordinary subcommand family.

The safest current local read is:

- `0x0E` is a single parameterized store-to-argmem opcode
- the following byte is the value being staged, not a family subcommand
- parser-side `0x0E xx` summaries are therefore mostly exposing immediate argument values

## Local parser proof

The ordinary top-level parser at `C1:890E` dispatches:

- `0x0E -> C1:8A79`

The `0x0E` leaf is tiny:

- `C1:8A79`: `LDY #$461A ; STY $1E ; JMP C1:8754`

So `0x0E` does enter one callback root, but that root is not a case ladder.

## Root behavior at `C1:461A`

`C1:461A` does:

- if `X == 0`, it falls back to the live arg-side selector byte through `C1:03DC`
- otherwise it uses `X` directly as the numeric argument
- then it calls `C1:0443`
- and returns `0`

`C1:0443` is the paired helper that writes the value in `A` to the current live text-context field at offset `+0x1F`.

So the safest current local read is: `0x0E` stores an immediate value into the current arg-memory selector or slot field.

That is strongly compatible with the inherited parser name `STORE_TO_ARGMEM`, and the local evidence is now good enough to promote that as the best current behavior label.

## Why parser-backed family summaries are misleading here

Tools that summarize `0x0E xx` as if they were ordinary family cases produce a fake case map.

That happens because:

- `0x0E` is one opcode with a following argument byte
- the second byte is the value being stored, not a branch selector
- ordinary scripts naturally use many different values here, especially in story, shop, and debug text

So visible forms like `0x0E 01`, `0x0E 02`, `0x0E 10`, or `0x0E 23` should currently be read as immediate stored values, not as runtime family subcommands.

## Script-side usage pattern

The exposed script neighborhoods fit that model well.

For example, common `0x0E 01` / `0x0E 02` uses appear immediately before:

- `CALL_TEXT C7:DC7F`
- `JUMP_IF_TRUE ...`

which is exactly the kind of pattern you would expect if the command is installing a small arg-memory selector or input value that the following helper text consults.

## Confidence boundaries

### Locally proved

- `0x0E` dispatches through `C1:8A79`
- `C1:8A79` installs callback root `C1:461A`
- `C1:461A` does not dispatch on subcommands; it forwards one numeric value into `C1:0443`
- `C1:0443` writes that value to the current live text-context field at offset `+0x1F`

### Still open

- the nicest user-facing phrasing for the `+0x1F` field itself across all text-engine contexts
- whether any special non-ordinary parser path reuses `0x0E` differently

## Practical conclusion

Treat `0x0E` as a parameterized store-to-argmem opcode, not as the next adjacent bank-`01` family.
