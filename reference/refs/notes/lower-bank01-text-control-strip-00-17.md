# Lower Bank-`01` Text Control Strip (`0x00..0x17`)

This note consolidates the current best local read of the lower bank-`01` text-command range from `0x00` through `0x17`.

See also:
- [text-command-00-line-break.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-00-line-break.md)
- [text-command-01-start-new-line.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-01-start-new-line.md)
- [text-command-02-end-block.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-02-end-block.md)
- [text-command-03-halt-with-prompt.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-03-halt-with-prompt.md)
- [text-command-04-set-event-flag.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-04-set-event-flag.md)
- [text-command-05-clear-event-flag.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-05-clear-event-flag.md)
- [text-command-06-jump-if-flag-set.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-06-jump-if-flag-set.md)
- [text-command-07-check-event-flag.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-07-check-event-flag.md)
- [text-command-08-call-text.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-08-call-text.md)
- [text-command-09-jump-multi.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-09-jump-multi.md)
- [text-command-0a-24bit-jump.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-0a-24bit-jump.md)
- [text-command-0b-parameterized-test-if-workmem-true.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-0b-parameterized-test-if-workmem-true.md)
- [text-command-0c-parameterized-test-if-workmem-false.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-0c-parameterized-test-if-workmem-false.md)
- [text-command-0d-parameterized-copy-to-argmem.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-0d-parameterized-copy-to-argmem.md)
- [text-command-0e-parameterized-store-to-argmem.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-0e-parameterized-store-to-argmem.md)
- [text-command-0f-parameterized-workmem-increment.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-0f-parameterized-workmem-increment.md)
- [text-command-10-parameterized-pause.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-10-parameterized-pause.md)
- [text-commands-11-and-12-menu-and-line-control.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-commands-11-and-12-menu-and-line-control.md)
- [text-commands-13-and-14-halt-control.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-commands-13-and-14-halt-control.md)
- [text-command-15-compressed-bank-1-pseudo-opcode.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-15-compressed-bank-1-pseudo-opcode.md)
- [text-command-16-compressed-bank-2-pseudo-opcode.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-16-compressed-bank-2-pseudo-opcode.md)
- [text-command-17-compressed-bank-3-pseudo-opcode.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-17-compressed-bank-3-pseudo-opcode.md)

## Main result

The lower bank-`01` strip is much cleaner than the parser-noise view first suggested.

It is not a stack of hidden subcommand families. Instead, it is mostly:

- a small standalone control layer
- a compact flag-control cluster
- a compact lower control-flow cluster
- a short run of parameterized memory/test/control helpers
- then a few later one-off control bytes and compressed-bank parser pseudo-opcodes

## Current best local map

### Standalone control layer

- `0x00` = `LINE_BREAK`
- `0x01` = `START_NEW_LINE`
- `0x02` = `END_BLOCK`
- `0x03` = `HALT_WITH_PROMPT`

### Flag-control cluster

- `0x04` = `SET_EVENT_FLAG`
- `0x05` = `CLEAR_EVENT_FLAG`
- `0x06` = `JUMP_IF_FLAG_SET`
- `0x07` = `CHECK_EVENT_FLAG`

### Lower control-flow cluster

- `0x08` = `CALL_TEXT`
- `0x09` = `JUMP_MULTI`
- `0x0A` = direct 24-bit `JUMP`

### Parameterized memory/test/control strip

- `0x0B` = parameterized `TEST_IF_WORKMEM_TRUE`
- `0x0C` = parameterized `TEST_IF_WORKMEM_FALSE`
- `0x0D` = parameterized `COPY_TO_ARGMEM`
- `0x0E` = parameterized `STORE_TO_ARGMEM`
- `0x0F` = parameterized `INCREMENT_WORKMEM`
- `0x10` = parameterized `PAUSE`

### Later one-off control bytes

- `0x11` = single selection-menu setup opcode
- `0x12` = single line-clear / display-reset opcode
- `0x13` = halt/control opcode through `C1:0166`
- `0x14` = sibling halt/control opcode through `C1:0166`

### Parser-side compressed-bank pseudo-opcodes

- `0x15` = compressed-bank-1 pseudo-opcode
- `0x16` = compressed-bank-2 pseudo-opcode
- `0x17` = compressed-bank-3 pseudo-opcode

## Structural takeaways

### 1. The lower strip is mostly not family-shaped

Below the richer family-heavy range higher up, most of these bytes are just direct opcodes.

That matters because parser-side scans made this area look much noisier than it really is. The local runtime map is cleaner: most bytes here either dispatch directly to one worker or install one tiny callback root.

### 2. `0x04..0x07` are a real little flag subsystem

These four bytes now read as a very tidy local cluster:

- set flag
- clear flag
- branch on flag
- test flag

And they all share the same 2-byte flag-id build pattern through `$97BA` and the `C0:923E` high-byte helper.

### 3. `0x08..0x0A` are the lower control-flow core

These three bytes are the first place the lower strip exposes real nontrivial control transfer:

- far text call
- counted multi-way branch
- direct 24-bit jump

That gives the lower range a nice compact control-flow nucleus.

### 4. `0x0B..0x10` are mostly immediate helper opcodes

This run is now much better understood as a strip of one-byte opcodes with one-byte immediate payloads, not hidden subcommand families.

### 5. `0x15..0x17` should be kept out of ordinary runtime family maps

Those three bytes are best treated as parser-side compressed-bank pseudo-opcodes. Leaving them inside the ordinary runtime family map only creates false structure.

## Confidence boundaries

### Strong locally pinned area

The whole `0x00..0x17` strip is now in good shape structurally.

The main remaining softness is not opcode identity. It is finer wording around:

- the exact runtime distinction between `LINE_BREAK` and `START_NEW_LINE`
- the exact mode split inside shared halt worker `C1:0166`
- a few exact human-facing names for later one-off control bytes like `0x11` and `0x12`

### What no longer looks like a real problem

- fake lower-strip subcommand families
- treating `0x15..0x17` as ordinary runtime command families
- treating `0x0B..0x10` as family dispatch ranges instead of immediate helper opcodes

## Practical conclusion

The lower bank-`01` text-command strip is now mostly solved at the structural level. It should be read as a compact control-and-helper layer beneath the richer higher command families, not as another broad forest of subdispatch families.
