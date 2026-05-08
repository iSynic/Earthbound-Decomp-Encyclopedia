# Text Command `0x04` as Set-Event-Flag Opcode

This note captures the current best local read of script byte `0x04`.

See also [text-command-05-clear-event-flag.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-05-clear-event-flag.md).
See also [text-command-06-jump-if-flag-set.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-06-jump-if-flag-set.md).
See also [text-command-07-check-event-flag.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-07-check-event-flag.md).

## Main result

`0x04` is the plain two-byte set-event-flag opcode in the lower bank-`01` text-command strip.

The safest current local read is:

- `0x04` = `SET_EVENT_FLAG`
- the next two bytes form an event-flag id
- the opcode builds that 16-bit flag id and calls shared flag-write helper `C2:165E`
- it does not branch and does not stage a boolean result

So this is the set-side mirror of plain clear-event-flag `0x05`.

## Local parser proof

The ordinary top-level parser at `C1:890E` dispatches:

- `0x04 -> C1:8A29`

The `0x04` leaf is tiny:

- `C1:8A29`: `LDY #$4265 ; STY $1E ; JMP C1:8754`

So `0x04` installs callback root `C1:4265`.

## Callback-root behavior at `C1:4265`

`C1:4265` is a two-byte flag-id builder plus direct flag-set helper.

The strongest local flow is:

- if no bytes are currently queued in `$97BA`, the current byte in `X` is appended there and the callback returns itself (`#$4265`) for continued parsing
- on the second byte, the routine:
  - zero-extends and shifts the current byte through `C0:923E` with `Y = #$08`
  - ORs that shifted high byte with queued low byte `$97BA`
  - sets `X` to `1`
  - calls `C2:165E` with the resulting 16-bit event-flag id
- the helper then returns `0`

So the local structure is the same as `0x05`, just with the write mode flipped from clear to set.

## Shared helper at `C2:165E`

`C2:165E` is the shared flag-write helper used by both `0x04` and `0x05`.

The local split is now very clean:

- `0x04`: call `C2:165E` with `X = 1` to set the flag
- `0x05`: call `C2:165E` with `X = 0` to clear the flag

That makes the parser-side `SET_EVENT_FLAG 0xNNNN` outputs locally well supported.

## Script-side usage pattern

The exposed script hits fit that model directly.

Representative outputs include:

- `SET_EVENT_FLAG 0x0300`
- `SET_EVENT_FLAG 0x0004`
- `SET_EVENT_FLAG 0x0113`
- `SET_EVENT_FLAG 0x0027`

And the local neighborhoods read exactly the way a plain state-write command should:

- set a flag
- then continue immediately into ordinary control flow, text, or the next event-side action

## Relationship to nearby lower-strip commands

`0x04..0x07` now form a clean lower-strip flag cluster:

- `0x04` = set event flag
- `0x05` = clear event flag
- `0x06` = branch if flag is set
- `0x07` = plain check event flag

That gives this lower range a much nicer structure than the earlier parser-driven ?lots of subcommands? impression.

## Confidence boundaries

### Locally proved

- `0x04` dispatches through `C1:8A29`
- `C1:8A29` installs callback root `C1:4265`
- `C1:4265` queues one low byte in `$97BA`
- on the second byte, `C1:4265` assembles a 16-bit flag id
- `C1:4265` calls `C2:165E` with `X = 1`

### Locally supported and strong

- `0x04` is best named `SET_EVENT_FLAG`
- the two following bytes are a 16-bit event-flag id

### Still open

- the nicest exact project-wide wording for `C2:165E`'s complete mode interface beyond the locally pinned `X = 1` set-side and `X = 0` clear-side uses

## Practical conclusion

Treat `0x04` as the lower-strip plain set-event-flag opcode. Together with `0x05`, `0x06`, and `0x07`, it closes out a coherent little bank-`01` flag-control cluster: set, clear, branch, and predicate.
