# Text Command `0x0D` as Parameterized Copy-To-Argmem Opcode

This note captures the current best local read of script byte `0x0D`.

See also [text-command-0e-parameterized-store-to-argmem.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-0e-parameterized-store-to-argmem.md).
See also [text-command-0f-parameterized-workmem-increment.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-0f-parameterized-workmem-increment.md).

## Main result

`0x0D` is not best read as an ordinary subcommand family.

The safest current local read is:

- `0x0D` is a single parameterized copy-to-argmem opcode
- the following byte chooses which live memory side is copied, not a family subcommand
- parser-side `0x0D xx` summaries are therefore mostly exposing immediate mode values

## Local parser proof

The ordinary top-level parser at `C1:890E` dispatches:

- `0x0D -> C1:8A71`

The `0x0D` leaf is tiny:

- `C1:8A71`: `LDY #$45EF ; STY $1E ; JMP C1:8754`

So `0x0D` enters one callback root, but that root is not a case ladder.

## Root behavior at `C1:45EF`

`C1:45EF` does:

- if `X != 0`, it reads the current live working-memory side through `C1:0400`
- if `X == 0`, it reads the current live arg-memory side through `C1:040A`
- stages that pointer pair into `$0E/$10`
- calls `C1:0489`
- returns `0`

`C1:0489` is the paired helper that installs a pointer pair into the current context's arg-memory slot family.

So the safest current local read is: `0x0D` copies either the current arg-memory side or the current working-memory side into the arg-memory slot, depending on the immediate byte.

That is strongly compatible with the inherited parser name `COPY_TO_ARGMEM`.

## Script-side usage pattern

The exposed script neighborhoods fit that model well.

For example:

- `0x0D 00` often appears right after a producer like `GET_CHARACTER_NUMBER`, then before tests against arg-side state
- `0x0D 01` appears in loops that walk party members or items, copying the current working-side result into arg memory before later text/tests consult it

So the current best behavioral split is:

- `0x0D 00` = copy current arg-side value back into the arg-memory slot context
- `0x0D 01` = copy current working-side value into arg-memory slot context

I am still keeping the wording slightly cautious because the underlying helpers are pointer-pair based, not just simple scalar byte moves.

## Why parser-backed family summaries are misleading here

Tools that summarize `0x0D xx` as if they were ordinary family cases produce a fake case map.

That happens because:

- `0x0D` is one opcode with an immediate mode byte
- the second byte selects which live side is copied, not a runtime branch family
- ordinary scripts naturally use a handful of common mode values like `0x00` and `0x01`

So visible forms like `0x0D 00` and `0x0D 01` should be read as immediate copy modes, not as separate family leaves.

## Confidence boundaries

### Locally proved

- `0x0D` dispatches through `C1:8A71`
- `C1:8A71` installs callback root `C1:45EF`
- `C1:45EF` does not branch into a family map; it chooses between `C1:0400` and `C1:040A` based on whether `X` is zero
- `C1:45EF` then installs the resulting pointer pair through `C1:0489`

### Still open

- the cleanest universal user-facing phrasing for the live working-memory side versus arg-memory side in every text-engine context
- whether any unusual non-ordinary parser path gives meaning to rarer immediate values beyond the simple zero/nonzero split

## Practical conclusion

Treat `0x0D` as a parameterized copy-to-argmem opcode, not as the next adjacent bank-`01` family.
