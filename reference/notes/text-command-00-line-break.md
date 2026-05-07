# Text Command `0x00` as Line-Break Opcode

This note captures the current best local read of script byte `0x00`.

See also [text-command-01-start-new-line.md](notes/text-command-01-start-new-line.md).
See also [text-command-02-end-block.md](notes/text-command-02-end-block.md).

## Main result

`0x00` is the ordinary one-byte `LINE_BREAK` opcode in the bank-`01` text engine.

It is not a family. The parser-side spread of apparent `0x00 NN` combinations is just noise from scanning a standalone one-byte control opcode as if it had subcommands.

The safest current local read is simply:

- `0x00` = `LINE_BREAK`

## Local parser proof

The ordinary top-level parser at `C1:890E` dispatches:

- `0x00 -> C1:8A00`

The `0x00` leaf is tiny:

- `C1:8A00`: `TXA ; JMP C1:8754`

So `0x00` is a direct one-byte control opcode with no callback-root family and no immediate payload.

## Runtime behavior

The local implementation is even simpler than `0x01`.

- `0x00` does not call the conditional gating helper at `C1:04B5`
- it does not call the explicit new-line worker `C4:38B1`
- it simply feeds the current byte straight back into the main parser/executor path through `C1:8754`

That fits a plain line-break control byte much better than any more elaborate family interpretation.

The exact low-level distinction between this and `START_NEW_LINE` is still worth keeping explicit:

- `0x00` is the plain inline line-break control
- `0x01` is the more stateful start-new-line helper that checks active display context and then calls `C4:38B1`

So these two are related, but not redundant.

## Script-side usage pattern

The exposed hits fit the simple `LINE_BREAK` model directly.

Typical neighborhoods look like:

- text
- `LINE_BREAK`
- more text immediately after

And some ordinary scripts use repeated consecutive `LINE_BREAK` bytes exactly where we would expect manual vertical spacing or empty displayed lines.

## Relationship to nearby standalone control opcodes

The bottom of the ordinary control strip now reads cleanly:

- `0x00` = line break
- `0x01` = start new line
- `0x02` = end block
- `0x03` = halt with prompt

Then `0x04..0x07` form the lower flag-control cluster, and `0x08..0x0A` form the lower call/jump cluster.

## Confidence boundaries

### Locally proved

- `0x00` dispatches through `C1:8A00`
- `C1:8A00` is a direct one-byte control path with no family structure and no extra immediate payload

### Locally supported and strong

- `0x00` is best named `LINE_BREAK`
- it is the plain inline line-break opcode, distinct from the more stateful `0x01` helper

### Still open

- the nicest exact wording for the low-level internal distinction between `LINE_BREAK` and `START_NEW_LINE`, beyond the current practical split of plain inline break vs stateful line-advance helper

## Practical conclusion

Treat `0x00` as the ordinary one-byte `LINE_BREAK` opcode. Together with `0x01`, `0x02`, and `0x03`, it closes out a clean standalone control layer at the bottom of the bank-`01` text-command range.
