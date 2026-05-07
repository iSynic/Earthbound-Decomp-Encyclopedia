# Text Command `0x09` as Counted Multi-Way Jump Opcode

This note captures the current best local read of script byte `0x09`.

See also [text-command-0a-24bit-jump.md](notes/text-command-0a-24bit-jump.md).
See also [text-command-0b-parameterized-test-if-workmem-true.md](notes/text-command-0b-parameterized-test-if-workmem-true.md).

## Main result

`0x09` is the counted multi-way branch opcode in the lower bank-`01` text-command strip.

The safest current local read is:

- `0x09` = `JUMP_MULTI`
- the following byte is the branch-count or number of cases
- the opcode selects one destination from a table of 24-bit branch entries
- parser-side outputs like `JUMP_MULTI count=2` and `JUMP_MULTI count=3` are directionally correct

## Working Names

- `C1:41D0` = `HandleTextCommand09JumpMulti`

## Local parser proof

The ordinary top-level parser at `C1:890E` dispatches:

- `0x09 -> C1:8A51`

The `0x09` leaf is tiny:

- `C1:8A51`: `LDY #$41D0 ; STY $1E ; JMP C1:8754`

So `0x09` installs callback root `C1:41D0`.

## Callback-root behavior at `C1:41D0`

`C1:41D0` is a real multi-way branch helper.

The strongest local flow is:

- it captures the incoming immediate count parameter from `X/Y`
- it reads the current live working-memory side through `C1:040A`
- if the live selection value is in range, it indexes into a table of 4-byte branch entries rooted at the current parser pointer
- if the live selection value is out of range, it falls back to the final branch entry block instead of indexing past the table
- it then rewrites the current parser pointer to the selected branch destination

A key structural detail is the `value - 1` adjustment before the 4-byte indexing step. So the live selector behaves like a 1-based choice number rather than a 0-based array index.

## Relationship to `0x0A`

`0x09` is the natural partner to direct jump `0x0A`.

- `0x0A` uses `C1:4103` to assemble one direct 24-bit jump target
- `0x09` uses `C1:41D0` to choose one destination from multiple 24-bit branch entries

So this is the point where the lower strip clearly exposes structured control-flow machinery, not just memory/predicate helpers.

## Script-side usage pattern

The exposed hits fit that model well.

Common `count=2` uses appear right after:

- `LOAD_STRING_TO_MEMORY "Yes"`
- `LOAD_STRING_TO_MEMORY "No"`
- `PRINT_HORIZONTAL_TEXT_STRING 0x02`
- `CREATE_SELECTION_MENU`
- `CLEAR_TEXT_LINE`
- `JUMP_MULTI count=2`

That is exactly the shape expected for a yes/no menu branch.

Likewise, `count=3` appears after battle-side producers like `GENERATE_RANDOM_NUMBER 0x03`, then fans out into three alternative text branches.

## Confidence boundaries

### Locally proved

- `0x09` dispatches through `C1:8A51`
- `C1:8A51` installs callback root `C1:41D0`
- `C1:41D0` is a counted multi-way branch helper over a table of branch entries
- the helper uses a 1-based live selector value from the working-memory side
- parser-side `count=2` and `count=3` outputs match the local structure unusually well

### Still open

- the nicest exact phrasing for the out-of-range fallback case, beyond "fall back to the final branch entry block"
- whether every script-side `count` value is always the exact visible branch count, or whether a few special contexts reserve one extra fallback entry implicitly

## Practical conclusion

Treat `0x09` as the lower-strip counted multi-way jump opcode. Together, `0x09` and `0x0A` give us the clean first pair of explicit lower-level control-flow commands below the parameterized memory/test strip.
