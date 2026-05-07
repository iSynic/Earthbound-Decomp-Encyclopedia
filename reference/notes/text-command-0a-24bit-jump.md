# Text Command `0x0A` as 24-bit Jump Opcode

This note captures the current best local read of script byte `0x0A`.

See also [text-command-0b-parameterized-test-if-workmem-true.md](notes/text-command-0b-parameterized-test-if-workmem-true.md).
See also [jeff-repair-item-name-bridge.md](notes/jeff-repair-item-name-bridge.md).

## Main result

`0x0A` is the direct 24-bit jump opcode in the lower bank-`01` text-command strip.

Unlike `0x0B..0x10`, it is not just a one-byte parameterized memory or pause helper. Its callback root at `C1:4103` is a three-byte target builder that assembles a full destination pointer and writes it back into the current parser state.

So the safest current read is:

- `0x0A` = direct jump opcode
- the three following bytes form a 24-bit destination
- parser-side displays like `JUMP C7:FD06` or `JUMP C5:8000` are directionally correct much more often than the fake lower-strip subcommand maps were

## Working Names

- `C1:4103` = `BuildTextCommand24BitJumpTarget`

## Local parser proof

The ordinary top-level parser at `C1:890E` dispatches:

- `0x0A -> C1:8A59`

The `0x0A` leaf is tiny:

- `C1:8A59`: `LDY #$4103 ; STY $1E ; JMP C1:8754`

So `0x0A` installs callback root `C1:4103`.

## Callback-root behavior at `C1:4103`

`C1:4103` is the same three-byte queue builder already seen in the earlier conditional-jump work.

The strongest local flow is:

- if fewer than 3 bytes are queued in `$97BA/$97BB/$97BC`, the current byte in `X` is appended to that queue and the callback returns itself (`#$4103`) for continued parsing
- once all 3 bytes are available, the routine combines:
  - current byte in `X`
  - `$97BC`
  - `$97BB`
  - `$97BA`
- then writes the resulting destination back through the pointer in `$0E`

So the safest current read is that `0x0A` is a 24-bit branch target installer using the same queue-and-assemble machinery that the conditional jump helpers reuse.

Source polish follow-up (2026-05-06): `src/c1/c1_4103_build_text_command24_bit_jump_target.asm`
now names the three queued argument bytes, queue count, self-return callback
low word, shift counts, scratch dword, and parser-pointer writeback slot used
by this builder.

## Script-side usage pattern

The exposed script hits fit that model well.

Common parser outputs look like:

- `JUMP C7:FD06`
- `JUMP C5:8000`
- `JUMP C9:1905`
- `JUMP EF:7221`

Those are exactly the kind of ordinary intra-bank or cross-bank script transfers we would expect from a 24-bit jump command.

I am still keeping one caution explicit: malformed or desynced script neighborhoods can make some parser-rendered jump targets look odd, especially where compressed-bank or other control bytes nearby confuse the dump.

## Relationship to earlier conditional-jump work

This result strengthens an earlier structural read rather than replacing it.

The same helper at `C1:4103` was already the best local fit for the branch-payload builder used by the `0x1B 02 / 03` conditional-jump side. `0x0A` now gives the clean direct version of that mechanism: an unconditional 24-bit jump target built by the same queue-and-assemble routine.

## Confidence boundaries

### Locally proved

- `0x0A` dispatches through `C1:8A59`
- `C1:8A59` installs callback root `C1:4103`
- `C1:4103` is a three-byte queue-and-assemble helper over `$97BA/$97BB/$97BC`
- the resulting assembled destination is written back into current parser state through `$0E`

### Still open

- the nicest exact phrasing for the destination word layout as seen by the callback mechanism, since the helper is written in terms of queued bytes and OR-combined partial results rather than a simple explicit long-pointer comment
- whether there are any rare non-ordinary contexts where the same helper is reused for something other than text-script control transfer

## Practical conclusion

Treat `0x0A` as the lower-strip direct 24-bit jump opcode. This is the point where the bank-`01` lower command strip stops being just parameterized memory/pause helpers and starts exposing fuller control-flow machinery.
