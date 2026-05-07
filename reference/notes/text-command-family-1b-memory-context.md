# Text Command Family `1B`: Memory / Context Manipulation

This note is the top-level overview for bank-`01` text command family `0x1B`.

See also [jeff-repair-item-name-bridge.md](notes/jeff-repair-item-name-bridge.md).

## Main result

The safest current local read is that `0x1B` is the bank-`01` text memory / context manipulation family.

In the live parser path, top-level command byte `0x1B` dispatches through `C1:8ADC`, which installs callback low word `C1:7C36`. The body at `C1:7C36` then dispatches on the one-byte `0x1B` subselector in `X`.

That puts `0x1B` in a stable family-level slot:

- `0x1A` -> `C1:7B56`
- `0x1B` -> `C1:7C36`
- `0x1C` -> `C1:7D94`
- `0x1D` -> `C1:7F11`
- `0x1E` -> `C1:811F`
- `0x1F` -> `C1:81BB`

## Best current subcommand map

The strongest currently pinned `0x1B` leaves are:

- `1B 00` -> backup live `+0x17/+0x1B/+0x1F` into saved `+0x21/+0x25/+0x29`
- `1B 01` -> restore saved `+0x21/+0x25/+0x29` into live `+0x17/+0x1B/+0x1F`
- `1B 02` -> zero-test branch helper, best current fit `JUMP_IF_FALSE`
- `1B 03` -> nonzero-test branch helper, best current fit `JUMP_IF_TRUE`
- `1B 04` -> swap live `+0x17` and `+0x1B`, best current fit `SWAP_WORKING_AND_ARG_MEMORY`
- `1B 05` -> copy live context into scratch `97CC..97D4`, best current fit `COPY_ACTIVE_MEMORY_TO_WORKING_MEMORY`
- `1B 06` -> restore scratch `97CC..97D4` into live context, best current fit `COPY_WORKING_MEMORY_TO_ACTIVE_MEMORY`

The branch pair `1B 02/03` is tied to the same three-byte destination builder at `C1:4103` that the lower control-flow strip uses for direct `JUMP`.

The decoded source now carries this contract directly in the `C1:7C36` body.
The dispatcher names the `1B 01..06` subselector ids, the zero-primary-context
branch tests, the four-byte jump-target skip, the saved `$16` argument pointer,
the primary and secondary context staging pairs at `$06/$08` and `$0A/$0C`,
the temporary swap pair at `$12/$14`, and the scratch context snapshot slots at
`$97CC..$97D4`.

Source polish follow-up (2026-05-06): the `C1:7C36` body now also names its
larger caller-frame offset and uses the common `$0E/$10` text-context source
pointer aliases when reinstalling the swapped or restored primary and secondary
contexts. That makes the `1B` contract line up with the adjacent `1A` menu and
`1C` display handoff vocabulary.

## Why this family matters

`0x1B` is the memory/context side that partners with the print/display family at `0x1C`.

The clearest local example is Jeff repair:

- `{swap}` enters `0x1B`
- `[1C 05 00]` enters `0x1C`
- the paired live slots at `+0x17` and `+0x1B`, plus their saved shadows at `+0x21/+0x25/+0x29`, explain how the same visible item-name selector can print different values before and after `{swap}`

So the best current system-level read is:

- `0x1B` manipulates live and saved text-memory / context slots
- `0x1C` reads and displays data from those slots

## Best current interpretation

The safest current interpretation is that `0x1B` is the bank-`01` text memory / context family, responsible for backing up, restoring, swapping, testing, and branching on the current paired text-context state.
