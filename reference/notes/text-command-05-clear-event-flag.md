# Text Command `0x05` as Clear-Event-Flag Opcode

This note captures the current best local read of script byte `0x05`.

See also [text-command-06-jump-if-flag-set.md](notes/text-command-06-jump-if-flag-set.md).
See also [text-command-07-check-event-flag.md](notes/text-command-07-check-event-flag.md).

## Main result

`0x05` is the plain two-byte clear-event-flag opcode in the lower bank-`01` text-command strip.

The safest current local read is:

- `0x05` = `CLEAR_EVENT_FLAG`
- the next two bytes form an event-flag id
- the opcode builds that 16-bit flag id and calls shared clear helper `C2:165E`
- it does not branch and does not stage a boolean result

## Working Names

- `C1:42AD` = `HandleTextCommand05ClearEventFlag`
- `C2:165E` = `SetOrClearEventFlag`

So this is a real ordinary opcode, not a family and not parser noise.

## Local parser proof

The ordinary top-level parser at `C1:890E` dispatches:

- `0x05 -> C1:8A31`

The `0x05` leaf is tiny:

- `C1:8A31`: `LDY #$42AD ; STY $1E ; JMP C1:8754`

So `0x05` installs callback root `C1:42AD`.

## Callback-root behavior at `C1:42AD`

`C1:42AD` is a two-byte flag-id builder plus direct flag-clear helper.

The strongest local flow is:

- if no bytes are currently queued in `$97BA`, the current byte in `X` is appended there and the callback returns itself (`#$42AD`) for continued parsing
- on the second byte, the routine:
  - zero-extends and shifts the current byte through `C0:923E` with `Y = #$08`
  - ORs that shifted high byte with queued low byte `$97BA`
  - clears `X` to `0`
  - calls `C2:165E` with the resulting 16-bit event-flag id
- the helper then returns `0`

So the local structure is very straightforward: queue low byte, combine with high byte, clear one event flag.

Source polish follow-up (2026-05-06): `src/c1/c1_42ad_handle_text_command05_clear_event_flag.asm`
now names the queued flag low byte, queue count, callback self-return low word,
low-byte mask, and clear-mode value used for the `C2:165E` call.

## Shared helper at `C2:165E`

`C2:165E` is the live flag-write helper already visible elsewhere in the project.

Here the local calling pattern is especially clear:

- `A` holds the assembled 16-bit flag id
- `X = 0`
- the result is a direct flag clear, with no predicate staging and no control-flow side effect inside the opcode itself

That matches the parser-side `CLEAR_EVENT_FLAG 0xNNNN` outputs unusually well.

## Script-side usage pattern

The exposed script hits fit that model directly.

Representative outputs include:

- `CLEAR_EVENT_FLAG 0x0200`
- `CLEAR_EVENT_FLAG 0x0100`
- `CLEAR_EVENT_FLAG 0x000B`
- `CLEAR_EVENT_FLAG 0x0216`

And the local neighborhoods often show the expected simple state-change role:

- clear a flag
- then proceed immediately into ordinary text, event setup, or the next control opcode

That is exactly the shape expected for a plain flag-clear command.

## Relationship to nearby flag commands

`0x05..0x07` are now reading as a coherent lower-strip flag cluster:

- `0x05` = clear event flag
- `0x06` = branch if flag is set
- `0x07` = plain check event flag

So the remaining likely mirror to close is the set-flag side just below this cluster.

## Confidence boundaries

### Locally proved

- `0x05` dispatches through `C1:8A31`
- `C1:8A31` installs callback root `C1:42AD`
- `C1:42AD` queues one low byte in `$97BA`
- on the second byte, `C1:42AD` assembles a 16-bit flag id
- `C1:42AD` calls `C2:165E` with `X = 0`

### Locally supported and strong

- `0x05` is best named `CLEAR_EVENT_FLAG`
- the two following bytes are a 16-bit event-flag id

### Still open

- the nicest exact project-wide phrasing for `C2:165E`'s mode split, since the helper is shared and this note only pins the clear-side `X = 0` call pattern locally

## Practical conclusion

Treat `0x05` as the lower-strip plain clear-event-flag opcode. It is the direct state-write companion to the predicate and branch helpers immediately above it.
