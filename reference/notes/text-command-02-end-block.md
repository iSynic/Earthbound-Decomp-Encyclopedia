# Text Command `0x02` as End-Block Opcode

This note captures the current best local read of script byte `0x02`.

See also [text-command-03-halt-with-prompt.md](notes/text-command-03-halt-with-prompt.md).

## Main result

`0x02` is the ordinary one-byte `END_BLOCK` opcode in the bank-`01` text engine.

It is not a family. The many parser-side `0x02 NN` combinations are just noise from scanning a standalone one-byte control opcode as if it had subcommands.

The safest current local read is simply:

- `0x02` = `END_BLOCK`

## Local parser proof

The ordinary top-level parser at `C1:890E` dispatches:

- `0x02 -> C1:8A04`

The `0x02` leaf is tiny:

- `C1:8A04`: `JSL C4:38B1 ; JMP C1:8754`

So `0x02` is a one-byte direct block-termination opcode, not a callback-root family and not a parameterized immediate helper.

## Worker behavior

The important local fact here is structural:

- `0x02` always routes directly into shared helper `C4:38B1`
- there is no extra immediate payload and no subdispatch under the opcode itself
- the surrounding script neighborhoods match ordinary block termination much better than any multi-byte-family interpretation

So the parser-side `END_BLOCK` label is locally well supported.

## Script-side usage pattern

The exposed hits fit that model directly.

Typical neighborhoods look like:

- text or event-side setup
- `END_BLOCK`
- then later separate control flow resumes through another text entry, branch target, or externally triggered script path

This is exactly the kind of use we would expect from a hard block terminator.

## Relationship to nearby lower-strip commands

The lower strip is now reading much more cleanly than the old parser-noise picture suggested:

- `0x02` = end block
- `0x03` = halt with prompt
- `0x04..0x07` = the flag-control cluster
- `0x08..0x0A` = call/jump control-flow trio

So `0x02` is part of the small standalone control-opcode layer beneath the richer family-heavy range higher up.

## Confidence boundaries

### Locally proved

- `0x02` dispatches through `C1:8A04`
- `C1:8A04` directly calls `C4:38B1`
- `0x02` has no subcommand family structure of its own

### Locally supported and strong

- `0x02` is best named `END_BLOCK`

### Still open

- the cleanest exact role description for `C4:38B1` relative to other block/window/display termination helpers, if we later want a fully cross-compared control-opcode map

## Practical conclusion

Treat `0x02` as the ordinary one-byte `END_BLOCK` opcode. The huge parser-side subopcode spread is just an artifact of scanning a standalone control byte out of context.
