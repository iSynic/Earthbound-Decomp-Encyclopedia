# Text Command `0x06` as Conditional Event-Flag Branch Opcode

This note captures the current best local read of script byte `0x06`.

See also [text-command-07-check-event-flag.md](notes/text-command-07-check-event-flag.md).
See also [text-command-0a-24bit-jump.md](notes/text-command-0a-24bit-jump.md).

## Main result

`0x06` is the conditional event-flag branch opcode in the lower bank-`01` text-command strip.

The safest current local read is:

- `0x06` = `JUMP_IF_FLAG_SET`
- the next two bytes form an event-flag id
- if the flag is set, the opcode hands control to shared jump-target builder `C1:4103`
- if the flag is clear, it advances the live parser pointer past the embedded branch payload instead

## Working Names

- `C1:42F5` = `HandleTextCommand06JumpIfFlagSet`

So `0x06` is not a family and not a parser artifact. It is the branch-form partner to plain event-flag predicate `0x07`.

## Local parser proof

The ordinary top-level parser at `C1:890E` dispatches:

- `0x06 -> C1:8A39`

The `0x06` leaf is tiny:

- `C1:8A39`: `LDY #$42F5 ; STY $1E ; JMP C1:8754`

So `0x06` installs callback root `C1:42F5`.

## Callback-root behavior at `C1:42F5`

`C1:42F5` is a two-byte flag-id builder plus conditional branch helper.

The strongest local flow is:

- if no bytes are currently queued in `$97BA`, the current byte in `X` is appended there and the callback returns itself (`#$42F5`) for continued parsing
- on the second byte, the routine:
  - zero-extends and shifts the current byte through `C0:923E` with `Y = #$08`
  - ORs that shifted high byte with queued low byte `$97BA`
  - calls `C2:1628` with the resulting 16-bit event-flag id
- if the flag test succeeds, the helper clears `$97CA` and returns callback root `#$4103`
- `#$4103` is the already-mapped direct 24-bit jump-target builder from [text-command-0a-24bit-jump.md](notes/text-command-0a-24bit-jump.md)
- if the flag test fails, the helper advances the live parser pointer forward past the embedded branch payload and returns `0`

So the local structure is very clean: build flag id, test it, then either branch through `C1:4103` or skip the branch payload.

Source polish follow-up (2026-05-06): `src/c1/c1_42f5_handle_text_command06_jump_if_flag_set.asm`
now names the queued flag low byte, queue count, callback self-return low word,
branch-target callback handoff, low-byte mask, and four-byte branch-payload skip.

## Relationship to `0x07`

`0x06` and `0x07` now form a very tidy pair.

- `0x07` uses the same two-byte flag-id build pattern, but stages the result through `C1:045D`
- `0x06` uses the same two-byte flag-id build pattern, but dispatches into branch-target helper `C1:4103` on success

So `0x06` is the direct branch-form event-flag command, while `0x07` is the plain predicate-form event-flag command.

## Script-side usage pattern

The exposed parser hits fit that model unusually well.

Representative outputs include:

- `JUMP_IF_FLAG_SET flag=0x0200 dest=C6:77CC`
- `JUMP_IF_FLAG_SET flag=0x0301 dest=C7:6357`
- `JUMP_IF_FLAG_SET flag=0x0005 dest=C9:8571`
- `JUMP_IF_FLAG_SET flag=0x0113 dest=C6:B99F`

And the local neighborhoods read exactly like ordinary conditional branches: if the condition is met, execution jumps to the embedded destination; otherwise the surrounding text flow continues normally.

## Confidence boundaries

### Locally proved

- `0x06` dispatches through `C1:8A39`
- `C1:8A39` installs callback root `C1:42F5`
- `C1:42F5` queues one low byte in `$97BA`
- on the second byte, `C1:42F5` assembles a 16-bit flag id and calls `C2:1628`
- on success, `C1:42F5` returns callback root `#$4103`
- `#$4103` is the direct 24-bit jump-target builder already mapped for `0x0A`
- on failure, `C1:42F5` advances the live parser pointer instead of taking the branch

### Locally supported and strong

- `0x06` is best named `JUMP_IF_FLAG_SET`
- the two following bytes are a 16-bit event-flag id
- the embedded branch target is a 24-bit destination handled through the same machinery as direct jump `0x0A`

### Still open

- the nicest exact phrasing for the failure-side pointer advance, since the helper is written in terms of current live parser-state fields rather than a plain literal ?skip 3-byte destination? comment
- whether there are any rare malformed or parser-desynced neighborhoods where the rendered target looks stranger than the ordinary local behavior really is

## Practical conclusion

Treat `0x06` as the lower-strip conditional event-flag branch opcode. Together with [text-command-07-check-event-flag.md](notes/text-command-07-check-event-flag.md), it gives the lower bank-`01` range a clean flag-control pair: predicate and branch.
