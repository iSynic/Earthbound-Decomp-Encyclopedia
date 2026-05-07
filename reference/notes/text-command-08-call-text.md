# Text Command `0x08` as Far Text-Call Opcode

This note captures the current best local read of script byte `0x08`.

See also [text-command-09-jump-multi.md](notes/text-command-09-jump-multi.md).
See also [text-command-0a-24bit-jump.md](notes/text-command-0a-24bit-jump.md).

## Main result

`0x08` is the far text-call opcode in the lower bank-`01` text-command strip.

Unlike `0x0B..0x10`, it is not just a one-byte parameterized memory or pause helper. And unlike `0x0A`, it does not simply rewrite the current parser pointer directly. Its callback root at `C1:43D6` queues three bytes, assembles a 24-bit far text pointer, and then hands that pointer to shared nested text-execution helper `C1:86B1`.

So the safest current read is:

- `0x08` = `CALL_TEXT`
- the three following bytes form a 24-bit text destination
- parser-side outputs like `CALL_TEXT C9:0000`, `CALL_TEXT C6:8500`, or `CALL_TEXT EF:790B` are directionally correct
- the target is executed through a shared nested text helper rather than a raw direct jump installer

## Working Names

- `C1:43D6` = `BuildCallTextFarPointerAndDispatch`
- `C1:86B1` = `ExecuteNestedTextPointer`

## Local parser proof

The ordinary top-level parser at `C1:890E` dispatches:

- `0x08 -> C1:8A49`

The `0x08` leaf is tiny:

- `C1:8A49`: `LDY #$43D6 ; STY $1E ; JMP C1:8754`

So `0x08` installs callback root `C1:43D6`.

## Callback-root behavior at `C1:43D6`

`C1:43D6` is a three-byte far-pointer builder.

The strongest local flow is:

- if fewer than 3 bytes are queued in `$97BA/$97BB/$97BC`, the current byte in `X` is appended to that queue and the callback returns itself (`#$43D6`) for continued parsing
- once all 3 bytes are available, the routine combines:
  - current byte in `X`
  - `$97BC`
  - `$97BB`
  - `$97BA`
- the combined value is assembled into a far pointer in `$0E/$10`
- the routine then `JSL`s shared helper `C1:86B1`

The exact arithmetic is written in terms of partial zero-extended values and OR-combined shifted pieces rather than a simple literal long-pointer comment, but the resulting structure is clearly a 24-bit far destination.

Source polish follow-up (2026-05-06): `src/c1/c1_43d6_build_call_text_far_pointer_and_dispatch.asm`
now names the queued argument bytes, queue count, self-return callback low word,
scratch dword, staged text-context source pointer, and the adjacent `0x18 05`
forced-alignment one-byte queue that shares the same source unit.

## Shared helper at `C1:86B1`

`C1:86B1` is not specific to `0x08`; it is a broadly reused nested text-execution helper with many direct `JSL` callers.

The strongest local anchors are:

- it snapshots current parser state from `$32/$34` into temporary locals and `$20/$22`
- it installs shared callback root `C4:550E`
- it stages the newly assembled far pointer into `$20/$22` and onward into live parser state
- it routes execution through the ordinary text-engine dispatcher at `C1:890E` and the shared executor path around `C1:8B2A`

So the best current local phrasing is: `0x08` calls another text stream through the shared nested text-execution machinery, instead of just replacing the current parser pointer the way direct jump `0x0A` does.

I am still keeping one caution explicit: I have not yet pinned the final return/restore path byte-for-byte through the whole helper, even though the state-save shape and script neighborhoods both strongly support call-style rather than pure jump-style behavior.

## Script-side usage pattern

The exposed hits fit a text-subroutine model unusually well.

Representative parser outputs include:

- `CALL_TEXT C9:0000`
- `CALL_TEXT C6:8500`
- `CALL_TEXT C5:1700`
- `CALL_TEXT C8:8000`
- `CALL_TEXT EF:790B`

And the local script neighborhoods often look like:

- print or prompt text
- `CALL_TEXT ...`
- then resume ordinary script flow with line breaks, tests, flags, or more text commands afterward

That is much more consistent with a nested text-call helper than with an unconditional branch.

## Relationship to `0x09` and `0x0A`

This result makes the lower control-flow cluster much cleaner:

- `0x08` = far text call through shared nested executor `C1:86B1`
- `0x09` = counted multi-way jump through `C1:41D0`
- `0x0A` = direct 24-bit jump through `C1:4103`

So the lower bank-`01` strip now has a compact control-flow trio beneath the parameterized memory/test helpers.

## Confidence boundaries

### Locally proved

- `0x08` dispatches through `C1:8A49`
- `C1:8A49` installs callback root `C1:43D6`
- `C1:43D6` is a three-byte far-pointer builder over `$97BA/$97BB/$97BC`
- once all bytes are available, `C1:43D6` assembles a far destination in `$0E/$10`
- `C1:43D6` then calls shared helper `C1:86B1`
- `C1:86B1` is a nested text-execution helper, not a `0x08`-specific one-off leaf

### Locally supported but still slightly cautious

- `0x08` is best named `CALL_TEXT`
- the helper behavior is call-style rather than jump-style, with the called text returning to the caller stream afterward

### Still open

- the cleanest byte-for-byte description of the final restore path inside `C1:86B1`
- whether any rare caller contexts use the same helper for something slightly broader than ordinary text-subroutine execution

## Practical conclusion

Treat `0x08` as the lower-strip far text-call opcode. Together, `0x08`, `0x09`, and `0x0A` give the bank-`01` lower command range a clean local control-flow core: call, counted branch, and direct jump.
