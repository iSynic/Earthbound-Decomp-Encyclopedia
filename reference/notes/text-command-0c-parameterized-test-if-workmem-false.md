# Text Command `0x0C` as Parameterized Test-If-Workmem-False Opcode

This note captures the current best local read of script byte `0x0C`.

See also [text-command-0d-parameterized-copy-to-argmem.md](notes/text-command-0d-parameterized-copy-to-argmem.md).
See also [text-command-0f-parameterized-workmem-increment.md](notes/text-command-0f-parameterized-workmem-increment.md).

## Main result

`0x0C` is not best read as an ordinary subcommand family.

The safest current local read is:

- `0x0C` is a single parameterized test opcode over the live working-memory field
- the following byte is the comparison value, not a family subcommand
- parser-side `0x0C xx` summaries are therefore mostly exposing immediate test values

## Working Names

- `C1:4591` = `HandleTextCommand0CTestWorkmemFalse`

## Local parser proof

The ordinary top-level parser at `C1:890E` dispatches:

- `0x0C -> C1:8A69`

The `0x0C` leaf is tiny:

- `C1:8A69`: `LDY #$4591 ; STY $1E ; JMP C1:8754`

So `0x0C` enters one callback root, but that root is not a case ladder.

## Root behavior at `C1:4591`

`C1:4591` does:

- stores the incoming immediate value from `X`
- reads the current live working-memory side through `C1:040A`
- compares the live value against the incoming immediate
- produces `0` when they are equal and `1` when they differ
- stages that boolean result through `C1:045D`

So the safest current local read is: `0x0C` tests whether the current live working-memory value is false with respect to the provided immediate comparison value, then stages a boolean result into the text pipeline.

That is strongly compatible with the inherited parser label `TEST_IF_WORKMEM_FALSE`, especially for the common `0x0C 00` form.

## Script-side usage pattern

The exposed script neighborhoods fit that model well.

For example:

- `0x0C 00` often appears right before movement or event continuations, matching a "working memory is zero / false" check
- `0x0C 01` appears in places that branch on a one-bit or one-step working-memory state being absent

So the common visible forms are best read as immediate-value tests, not as separate family cases.

## Why parser-backed family summaries are misleading here

Tools that summarize `0x0C xx` as if they were ordinary family cases produce a fake case map.

That happens because:

- `0x0C` is one opcode with an immediate comparison byte
- the second byte is data, not a runtime branch selector
- ordinary scripts naturally use several common comparison values like `0x00` and `0x01`

So visible forms like `0x0C 00`, `0x0C 01`, or `0x0C 10` should be read as immediate test values, not as subcommands.

## Confidence boundaries

### Locally proved

- `0x0C` dispatches through `C1:8A69`
- `C1:8A69` installs callback root `C1:4591`
- `C1:4591` compares the immediate value in `X` against the live working-memory side from `C1:040A`
- `C1:4591` stages a boolean result through `C1:045D`

### Still open

- the nicest universal user-facing phrasing for the `C1:040A` live field across all text contexts
- whether any unusual non-ordinary parser path uses signed or wider interpretations of the compared value

## Practical conclusion

Treat `0x0C` as a parameterized working-memory false-test opcode, not as the next adjacent bank-`01` family.
