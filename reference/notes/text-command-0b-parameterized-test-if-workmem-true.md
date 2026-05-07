# Text Command `0x0B` as Parameterized Test-If-Workmem-True Opcode

This note captures the current best local read of script byte `0x0B`.

See also [text-command-0c-parameterized-test-if-workmem-false.md](notes/text-command-0c-parameterized-test-if-workmem-false.md).
See also [text-command-0d-parameterized-copy-to-argmem.md](notes/text-command-0d-parameterized-copy-to-argmem.md).

## Main result

`0x0B` is not best read as an ordinary subcommand family.

The safest current local read is:

- `0x0B` is a single parameterized test opcode over the live working-memory field
- the following byte is the comparison value, not a family subcommand
- parser-side `0x0B xx` summaries are therefore mostly exposing immediate test values

## Working Names

- `C1:4558` = `HandleTextCommand0BTestWorkmemTrue`

## Local parser proof

The ordinary top-level parser at `C1:890E` dispatches:

- `0x0B -> C1:8A61`

The `0x0B` leaf is tiny:

- `C1:8A61`: `LDY #$4558 ; STY $1E ; JMP C1:8754`

So `0x0B` enters one callback root, but that root is not a case ladder.

## Root behavior at `C1:4558`

`C1:4558` does:

- stores the incoming immediate value from `X`
- reads the current live working-memory side through `C1:040A`
- compares the live value against the incoming immediate
- produces `1` when they are equal and `0` when they differ
- stages that boolean result through `C1:045D`

So the safest current local read is: `0x0B` tests whether the current live working-memory value is true with respect to the provided immediate comparison value, then stages a boolean result into the text pipeline.

That is strongly compatible with the inherited parser label `TEST_IF_WORKMEM_TRUE`.

## Script-side usage pattern

The exposed script neighborhoods fit that model well.

For example:

- `0x0B 01` commonly appears right after a producer like `GET_CHARACTER_NUMBER` or `COPY_TO_ARGMEM`, then before `JUMP_IF_TRUE` or `JUMP_IF_FALSE`
- that is exactly the sort of layout expected for a staged boolean comparison result over a current working-memory value

So the visible forms are best read as immediate-value tests, not as separate family cases.

## Why parser-backed family summaries are misleading here

Tools that summarize `0x0B xx` as if they were ordinary family cases produce a fake case map.

That happens because:

- `0x0B` is one opcode with an immediate comparison byte
- the second byte is data, not a runtime branch selector
- ordinary scripts naturally use several common comparison values like `0x00`, `0x01`, and `0x02`

So visible forms like `0x0B 01`, `0x0B 02`, or `0x0B 10` should be read as immediate test values, not as subcommands.

## Confidence boundaries

### Locally proved

- `0x0B` dispatches through `C1:8A61`
- `C1:8A61` installs callback root `C1:4558`
- `C1:4558` compares the immediate value in `X` against the live working-memory side from `C1:040A`
- `C1:4558` stages a boolean result through `C1:045D`
- `C1:4558` is the true-result mirror of the false-result helper at `C1:4591`

### Still open

- the nicest universal user-facing phrasing for the `C1:040A` live field across all text contexts
- whether any unusual non-ordinary parser path uses signed or wider interpretations of the compared value

## Practical conclusion

Treat `0x0B` as a parameterized working-memory true-test opcode, not as the next adjacent bank-`01` family.
