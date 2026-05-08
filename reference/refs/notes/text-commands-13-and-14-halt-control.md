# Text Commands `0x13` and `0x14` as Halt/Control Opcodes

This note captures the current best local read of script bytes `0x13` and `0x14`.

See also [text-command-15-compressed-bank-1-pseudo-opcode.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-15-compressed-bank-1-pseudo-opcode.md).
See also [text-command-16-compressed-bank-2-pseudo-opcode.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-16-compressed-bank-2-pseudo-opcode.md).
See also [text-command-17-compressed-bank-3-pseudo-opcode.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-17-compressed-bank-3-pseudo-opcode.md).

## Main result

`0x13` and `0x14` are not ordinary bank-`01` subcommand families.

The safest current local read is:

- `0x13` is a single halt/control opcode routed through `C1:8AB0`
- `0x14` is a sibling halt/control opcode routed through `C1:8ABA`
- the large parser-side `0x13 xx` and `0x14 xx` "subcommand" spreads are mostly just ordinary payload or following bytes being misread as family subopcodes

That means they should sit in the roadmap as single special commands, not as the next adjacent families after `0x1A` or `0x19`.

## Local parser proof

The ordinary top-level parser at `C1:890E` dispatches:

- `0x13 -> C1:8AB0`
- `0x14 -> C1:8ABA`

Unlike `0x18`, `0x19`, `0x1A`, `0x1B`, `0x1C`, `0x1D`, `0x1E`, and `0x1F`, neither command installs a family callback low word in `$1E`.

Instead, both are tiny direct leaves:

- `C1:8AB0`: `LDX #0 ; TXA ; JSR C1:0166 ; JMP C1:8754`
- `C1:8ABA`: `LDX #1 ; TXA ; JSR C1:0166 ; JMP C1:8754`

So locally they behave like one-off command opcodes with mode arguments baked into the leaf, not ordinary subcommand-family roots.

## Shared worker at `C1:0166`

`C1:0166` is the shared worker for these halt/control opcodes.

The strongest local features are:

- it stores both incoming mode values into direct-page work bytes `$12/$14`
- it loops on text/input state including `$9645`, `$964B`, `$964D`, and `$006D`
- it calls `C3:E4CA`, `C1:2DD5`, and later `EF:0256` depending on state
- it resolves the current live text context through `$8958 -> $88E4 -> C08FF7 -> $8650`
- it can trigger VRAM-side work through `C08616`

So the safest current umbrella read is that `C1:0166` is a shared halt/control routine for textbox progression or display gating, with `0x13` and `0x14` selecting two closely related modes.

## Best current interpretation

The best current interpretation is still close to the inherited labels:

- `0x13` behaves like a halt without prompt or the quieter halt mode
- `0x14` behaves like a halt with prompt or the more explicit prompt-for-advance mode

I am still keeping that last user-facing distinction slightly cautious, because the local proof is stronger on "shared halt/control worker with two baked-in modes" than on the exact wording of the prompt behavior.

## Why parser-backed family summaries are misleading here

Tools that summarize `0x13 xx` or `0x14 xx` as if they were ordinary families produce wide fake subcommand spreads.

That happens because:

- `0x13` and `0x14` are single opcodes, not family roots
- the parser summaries are reading the next byte as if it were a family subopcode
- those following bytes vary naturally across ordinary text content, battle text, and event payloads

So the heavy apparent subcommand diversity under `0x13` and `0x14` should not be promoted into a runtime family map.

## Confidence boundaries

### Locally proved

- `0x13` dispatches directly to `C1:8AB0`
- `0x14` dispatches directly to `C1:8ABA`
- both leaves call the same worker `C1:0166`
- neither command installs an ordinary family callback root in `$1E`
- parser-side `0x13 xx` / `0x14 xx` subcommand spreads are therefore not ordinary family evidence

### Still open

- the exact user-facing difference between the two `C1:0166` modes
- how best to phrase the prompt distinction without overclaiming from the inherited labels

## Practical conclusion

Treat `0x13` and `0x14` as single halt/control opcodes with a shared modal worker, not as the next adjacent bank-`01` text-command families to map.
