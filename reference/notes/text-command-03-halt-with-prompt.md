# Text Command `0x03` as Halt-With-Prompt Opcode

This note captures the current best local read of script byte `0x03`.

See also [text-commands-13-and-14-halt-control.md](notes/text-commands-13-and-14-halt-control.md).

## Main result

`0x03` is the ordinary halt-with-prompt opcode used all over the bank-`01` text engine.

It is not a family. The apparent spread of many parser-side `0x03 NN` combinations is just a side effect of scanning a standalone one-byte control opcode as if it had subcommands.

The safest current local read is simply:

- `0x03` = `HALT_WITH_PROMPT`

## Local parser proof

The ordinary top-level parser at `C1:890E` dispatches:

- `0x03 -> C1:8A1D`

The `0x03` leaf is tiny:

- `C1:8A1D`: `LDX #$0000 ; LDA #$0001 ; JSR C1:0166 ; JMP C1:8754`

So `0x03` is a one-byte direct control opcode, not a callback-root family and not a parameterized immediate helper.

## Worker behavior

The important local fact here is structural, not exotic:

- `0x03` routes straight into shared halt/control worker `C1:0166`
- it does so with a fixed baked-in mode pair (`X = 0`, `A = 1`)
- there is no extra immediate payload and no subdispatch under the opcode itself

That matches the parser-side `HALT_WITH_PROMPT` output extremely well.

## Script-side usage pattern

The exposed script hits are exactly what we would expect from a normal prompt-wait control byte:

- ordinary conversation text
- `HALT_WITH_PROMPT`
- then resume with more text, line breaks, menus, or event-side actions afterward

This is one of the most common control opcodes in the script corpus, which is why parser-side pseudo-subcommand scans produce huge noisy counts. But the runtime structure itself is simple.

## Relationship to other halt/control opcodes

This result fits neatly with the earlier lower-strip cleanup:

- `0x03` = ordinary halt-with-prompt opcode
- `0x13` and `0x14` = the separate later halt/control pair that also route through `C1:0166`, but with different baked-in modes

So there is a small family resemblance at the worker level, but `0x03` itself is still just one standalone opcode.

## Confidence boundaries

### Locally proved

- `0x03` dispatches through `C1:8A1D`
- `C1:8A1D` directly calls `C1:0166` with fixed immediate setup
- `0x03` has no subcommand family structure of its own

### Locally supported and strong

- `0x03` is best named `HALT_WITH_PROMPT`

### Still open

- the nicest exact modal wording for the fixed `X = 0, A = 1` call into `C1:0166` relative to the other halt/control variants, if we eventually want a fully cross-compared map of every prompt/advance mode

## Practical conclusion

Treat `0x03` as the ordinary one-byte halt-with-prompt opcode. The huge parser hit count reflects how common it is, not hidden family structure.
