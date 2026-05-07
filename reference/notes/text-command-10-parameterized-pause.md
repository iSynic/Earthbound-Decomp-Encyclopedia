# Text Command `0x10` as Parameterized Pause Opcode

This note captures the current best local read of script byte `0x10`.

See also [text-commands-11-and-12-menu-and-line-control.md](notes/text-commands-11-and-12-menu-and-line-control.md).
See also [text-commands-13-and-14-halt-control.md](notes/text-commands-13-and-14-halt-control.md).

## Main result

`0x10` is not best read as an ordinary subcommand family.

The safest current local read is:

- `0x10` is a single parameterized pause opcode
- its following byte is a countdown value or duration parameter, not a family subcommand
- parser-side `0x10 xx` summaries are therefore mostly describing pause lengths, not a runtime case map

## Working Names

- `C1:00D6` = `WaitTextTicks`
- `C1:4EAB` = `HandleTextCommand10ParameterizedPause`

## Local parser proof

The ordinary top-level parser at `C1:890E` dispatches:

- `0x10 -> C1:8A87`

The `0x10` leaf is tiny:

- `C1:8A87`: `LDY #$4EAB ; STY $1E ; JMP C1:8754`

That means `0x10` does enter one callback root, but the root itself is not a subcommand ladder.

## Root behavior at `C1:4EAB`

`C1:4EAB` does:

- `TXA`
- `JSR C1:00D6`
- returns `0`

So whatever byte follows `0x10` in the script becomes the numeric argument passed straight into the shared worker at `C1:00D6`.

This is the key reason not to treat the second byte as a family subopcode.

This leaf is now source-backed in `src/c1/c1_4eab_handle_text_command10_parameterized_pause.asm`; the wider `C1:4EAB..575D` helper corridor validates byte-for-byte in the C1 scaffold.

Source polish follow-up (2026-05-06): the same source module now names the
`C1:00D6` wait worker and the rest of the corridor's menu, print, status,
inventory, and context helper calls directly. The parameterized-pause leaf
itself remains intentionally tiny: it forwards the numeric argument to the
wait worker and returns zero.

## Shared worker at `C1:00D6`

`C1:00D6` is a countdown-style wait helper.

The strongest local behavior is:

- it stores the incoming argument in `$0E`
- synchronizes through the usual text-side state helpers `C3:E4CA` and `C1:2DD5`
- then loops through `C1:2E42` once per count while decrementing `$0E`
- exits when the count reaches zero

So the safest current local read is: `0x10` is a parameterized pause or wait command whose argument is the number of loop ticks or update steps to wait.

## Why parser-backed family summaries are misleading here

Tools that summarize `0x10 xx` as if they were ordinary subcommands produce huge fake case spreads.

That happens because:

- `0x10` is one opcode with a numeric argument
- the second byte is a duration value, not a branch selector
- ordinary script content naturally uses many different pause values

So heavy values like `0x0F` or `0x14` should currently be read as common pause durations, not as meaningful family cases.

## Confidence boundaries

### Locally proved

- `0x10` dispatches through `C1:8A87`
- `C1:8A87` installs callback root `C1:4EAB`
- `C1:4EAB` forwards the incoming argument directly to `C1:00D6`
- `C1:00D6` behaves like a countdown wait loop over `C1:2E42`

### Still open

- the best exact user-facing unit for the countdown: frames, text ticks, or some slightly higher-level update step
- whether any special contexts reinterpret the count differently

## Practical conclusion

Treat `0x10` as a parameterized pause opcode, not as the next adjacent bank-`01` subcommand family.
