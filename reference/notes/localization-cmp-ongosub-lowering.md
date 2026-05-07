# Localization `@CMP` / `@ONGOSUB` Lowering Hypothesis

This note captures the first focused lowering hypothesis for recovered `.MSG`
control macros. It uses generated command-only and argument-category evidence;
recovered dialogue, raw argument values, labels, and full source records remain
ignored.

## Inputs

- `notes/localization-control-macro-context.md`
- `notes/localization-control-macro-patterns.md`
- `notes/localization-control-macro-lowering-profiles.md`
- bank-`01` Text VM notes for `CALL_TEXT`, `JUMP_MULTI`, `JUMP`,
  parameterized work-memory tests, and family `0x1B` memory/context branches

## Evidence

The generated reports isolate a strong source-level motif:

- `@CMP`: `312` hits, always `2` arguments
- `@ONGOSUB`: `280` hits, usually `1` argument in the dominant motif
- `@CMP > @ONGOSUB`: `254` adjacent hits
- `@ONGOSUB > @CMP`: `254` adjacent hits
- `@CMP > @ONGOSUB > @CMP`: `254` triples
- focus-pair argument profile:
  `@CMP(decimal,decimal) > @ONGOSUB(message_label)` for all `254` hits

That shape is important: the high-frequency form is not a many-label
source-level table. It is a repeated two-argument compare followed by a
one-label subroutine call.

## Working Read

The safest current read is:

```text
@CMP(a, b)
@ONGOSUB(label)
```

means:

```text
stage predicate = compare(a, b)
if predicate is true:
    CALL_TEXT label
fall through to the next source command
```

This should be treated as source-level conditional-call syntax over existing
Text VM primitives, not as a new runtime opcode.

## Likely Lower-Level Ingredients

The exact byte template is still open, but the likely primitive set is already
documented:

- `0x08` `CALL_TEXT`: far text call to the one-label target
- `0x0B` / `0x0C`: parameterized tests over live work memory
- `0x0D` / `0x0E`: copy/store into the arg-memory side
- `0x1B 02` / `0x1B 03`: false/true branches over the current staged context
- `0x1B 04..06`: swap/copy active/scratch memory when source-local staging is
  needed

The strongest plausible lowering shape is therefore:

```text
stage or restore the compare subject
test subject against the compare value
branch over the call when false
CALL_TEXT label
continue after the call site
```

This is deliberately phrased as a control-flow shape, not as a final byte
template. The generated profiles prove the source pattern; they do not by
themselves prove which of the two decimal `@CMP` arguments is the subject,
which is the compared value, or whether one of them is a source-local register
slot.

## Relationship To `JUMP_MULTI`

The dominant `@CMP > @ONGOSUB` motif should not be forced onto `0x09`
`JUMP_MULTI`.

`JUMP_MULTI` is a counted branch table over a live 1-based selector. The common
`@CMP > @ONGOSUB` form is a chain of single-label conditional calls. Larger
`@ONGOSUB(...)` arities still exist and may lower to a table-like form, but
they are not the common compare/call motif.

## Confidence

High confidence:

- `@CMP` is a source-level two-argument compare macro.
- The dominant `@CMP > @ONGOSUB` motif is a compare followed by a one-label
  source call.
- The motif lowers onto existing bank-`01` Text VM call/test/branch machinery,
  not a new runtime VM.

Medium confidence:

- `@ONGOSUB(label)` in this motif is best read as a conditional `CALL_TEXT`
  controlled by the immediately preceding compare.
- The repeated alternating pattern represents source-authored case checks over
  one active selector or local register.

Still open:

- exact byte sequence emitted for `@CMP`
- exact role of the two numeric `@CMP` operands
- whether source-local register state is always required, or only in records
  that use `@LOAD_REG`, `@SAVE_REG`, `@SET_REG`, or global register helpers
- whether multi-argument `@ONGOSUB` forms lower to `CALL_TEXT` chains,
  `JUMP_MULTI`-like tables, or another source-tool expansion

## Port-Friendly Source Form

A future reassembly-friendly text source can preserve this as readable syntax:

```text
cmp_case <subject>, <value>, call <label>
```

or:

```text
if_cmp <subject>, <value>:
    call_text <label>
```

The important constraint is that it should remain a source macro until the
exact lowering is proven. Treating it as a native bytecode opcode would make
the source less honest and harder to round-trip.

## Next Proof

The next focused proof should target `@SET_LOOPREG > @GOSUB`, because it is
the highest-frequency cross-file motif and likely explains how source-local
register/loop state feeds repeated calls outside the debug-heavy
`@CMP > @ONGOSUB` cluster.
