# Text Command `0x07` as Event-Flag Predicate Opcode

This note captures the current best local read of script byte `0x07`.

See also [text-command-08-call-text.md](notes/text-command-08-call-text.md).
See also [text-command-0b-parameterized-test-if-workmem-true.md](notes/text-command-0b-parameterized-test-if-workmem-true.md).

## Main result

`0x07` is the plain two-byte event-flag predicate opcode in the lower bank-`01` text-command strip.

The safest current local read is:

- `0x07` = `CHECK_EVENT_FLAG`
- the next two bytes form an event-flag id
- the opcode calls shared flag-test helper `C2:1628`
- the result is staged as a signed boolean-like value through `C1:045D`

## Working Names

- `C1:435F` = `HandleTextCommand07CheckEventFlag`
- `C2:1628` = `TestEventFlag`

So this is not a family and not a fake parser artifact. It is a real immediate event-flag test command.

## Local parser proof

The ordinary top-level parser at `C1:890E` dispatches:

- `0x07 -> C1:8A41`

The `0x07` leaf is tiny:

- `C1:8A41`: `LDY #$435F ; STY $1E ; JMP C1:8754`

So `0x07` installs callback root `C1:435F`.

## Callback-root behavior at `C1:435F`

`C1:435F` is a two-byte immediate flag predicate.

The strongest local flow is:

- if no bytes are currently queued in `$97BA`, the current byte in `X` is appended there and the callback returns itself (`#$435F`) for continued parsing
- on the second byte, the routine:
  - zero-extends and shifts the current byte through `C0:923E` with `Y = #$08`
  - ORs that shifted high byte with queued low byte `$97BA`
  - calls `C2:1628` with the resulting 16-bit flag id
- the result from `C2:1628` is sign-extended into `$0E/$10`
- that value is then staged through `C1:045D`

So the plain local shape is: queue low byte, combine with high byte, test one event flag, stage the result.

Source polish follow-up (2026-05-06): `src/c1/c1_435f_handle_text_command07_check_event_flag.asm`
now names the queued flag low byte, queue count, callback self-return low word,
and low-byte mask before staging the predicate result through `C1:045D`.

## Shared helper at `C2:1628`

`C2:1628` is the live event-flag test helper already seen elsewhere in the bank-`01` command families.

`0x07` is the clean immediate version of that path: it does not branch by itself and does not directly rewrite the parser pointer. It simply turns a two-byte event-flag id into a staged result that later conditional commands can consume.

## Script-side usage pattern

The exposed script hits fit that model unusually well.

Representative parser outputs include:

- `CHECK_EVENT_FLAG 0x0115`
- `CHECK_EVENT_FLAG 0x0116`
- `CHECK_EVENT_FLAG 0x0215`
- `CHECK_EVENT_FLAG 0x1002`

And the local neighborhoods typically look like:

- `CHECK_EVENT_FLAG ...`
- immediately followed by `JUMP_IF_FALSE ...`
- or followed by another flag test in a chain of AND-like gating checks

That is exactly the shape expected for a plain predicate opcode that stages a boolean-like result rather than branching on its own.

## Relationship to nearby lower-strip commands

`0x07` now fits neatly into the lower control strip:

- `0x07` = immediate event-flag predicate
- `0x08` = far text call
- `0x09` = counted multi-way jump
- `0x0A` = direct 24-bit jump
- `0x0B/0x0C` = immediate workmem true/false tests

So `0x07` is the event-flag analogue of the immediate memory-test commands just above it.

## Confidence boundaries

### Locally proved

- `0x07` dispatches through `C1:8A41`
- `C1:8A41` installs callback root `C1:435F`
- `C1:435F` queues one low byte in `$97BA`
- on the second byte, `C1:435F` assembles a 16-bit flag id and calls `C2:1628`
- the result is sign-extended and staged through `C1:045D`

### Locally supported and strong

- `0x07` is best named `CHECK_EVENT_FLAG`
- the two following bytes are a 16-bit event-flag id

### Still open

- the nicest exact user-facing wording for the staged result, beyond ?signed boolean-like value,? since the helper stores a sign-extended `0` or nonzero outcome rather than a tiny explicit `0/1` write
- whether there are any rare special callers that interpret the staged result differently from the ordinary `JUMP_IF_FALSE` / `JUMP_IF_TRUE` paths

## Practical conclusion

Treat `0x07` as the lower-strip immediate event-flag predicate opcode. It is the clean flag-test counterpart to the immediate workmem-test commands nearby, and its parser-side `CHECK_EVENT_FLAG 0xNNNN` outputs are locally well supported.
