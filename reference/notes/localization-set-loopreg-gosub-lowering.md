# Localization `@SET_LOOPREG` / `@GOSUB` Lowering Hypothesis

This note captures the second focused lowering hypothesis for recovered `.MSG`
control macros. It uses generated command-only and argument-category evidence;
recovered dialogue, raw argument values, labels, and full source records remain
ignored.

## Inputs

- `notes/localization-control-macro-context.md`
- `notes/localization-control-macro-patterns.md`
- `notes/localization-control-macro-lowering-profiles.md`
- `notes/localization-cmp-ongosub-lowering.md`
- bank-`01` Text VM notes for `CALL_TEXT`, parameterized memory commands, and
  family `0x1B` memory/context commands

## Evidence

The generated reports isolate `@SET_LOOPREG > @GOSUB` as the strongest
cross-file control-macro motif:

- `@SET_LOOPREG`: `325` hits, always `1` argument
- `@GOSUB`: `2095` one-argument hits in the recovered authoring source
- `@SET_LOOPREG > @GOSUB`: `191` adjacent hits across `31` files
- `@SET_LOOPREG > @SET_LOOPREG`: `77` adjacent hits, showing list-style or
  repeated staging is common
- common triple: `@SET_LOOPREG > @GOSUB > @TRUE_GOTO` with `74` hits
- focus-pair argument profiles:
  - `@SET_LOOPREG(symbol) > @GOSUB(message_label)`: `95`
  - `@SET_LOOPREG(decimal) > @GOSUB(message_label)`: `76`
  - `@SET_LOOPREG(decimal) > @GOSUB(symbol)`: `16`
  - `@SET_LOOPREG(symbol) > @GOSUB(symbol)`: `4`

Unlike `@CMP > @ONGOSUB`, this motif is not concentrated in one file. It is a
broad authoring pattern across ordinary script areas, shop scripts, and debug
source.

## Working Read

The safest current read is:

```text
@SET_LOOPREG(value)
@GOSUB(label)
```

means:

```text
stage source-local loop/register value
CALL_TEXT label
called text reads or tests the staged value
fall through after the call returns
```

This is source-level call-with-staged-argument syntax over existing Text VM
state, not a standalone runtime opcode.

## Why "Loop Register" Is The Right Source-Level Phrase

The source macro name itself says `LOOPREG`, and the generated pattern evidence
matches that name:

- repeated `@SET_LOOPREG` chains appear before related control work
- staged values can be decimal literals or symbols
- the staged value usually feeds a `@GOSUB`, which is already mapped to
  `0x08` `CALL_TEXT`
- the common `@SET_LOOPREG > @GOSUB > @TRUE_GOTO` triple implies the called
  text or surrounding source often stages a predicate immediately after the
  call

So the best public-facing source term is currently "source-local loop/register
argument" rather than a raw VM field name. That keeps the source readable while
we continue pinning the exact byte-level storage slot.

## Likely Lower-Level Ingredients

The exact byte template is still open, but the likely primitive set is already
documented:

- `0x08` `CALL_TEXT`: far text call for `@GOSUB(label)`
- `0x0D` / `0x0E`: copy/store into the arg-memory side for staged source
  values
- `0x1B 00` / `0x1B 01`: backup/restore live text memory slots around nested
  calls when needed
- `0x1B 04..06`: swap/copy active and scratch memory when source-local state
  has to survive helper calls
- `0x1B 02` / `0x1B 03`: follow-up false/true branches over a staged predicate

The strongest plausible lowering shape is therefore:

```text
store or copy source-local value into the active text context
CALL_TEXT label
optionally test or branch on the value/predicate produced by that call
continue after the call site
```

As with `@CMP > @ONGOSUB`, this is a control/data-flow shape, not a final byte
template. The generated profiles prove the source pattern; they do not by
themselves prove whether `@SET_LOOPREG` stores into the work-memory side, the
arg-memory side, or a source-tool local that later compiles through one of
those VM slots.

## Relationship To `@SET_REG`

`@SET_REG` and `@SET_LOOPREG` are related but should not be collapsed yet.

The context report shows:

- `@SET_REG`: `120` hits, usually near name/display/query commands
- `@SET_LOOPREG`: `325` hits, usually near `@GOSUB`, repeated
  `@SET_LOOPREG`, and branch controls

That suggests `@SET_REG` is a general source-register assignment, while
`@SET_LOOPREG` is the authoring shorthand used for repeated call/list contexts.
The two may share a lower-level storage primitive, but they are different
source-level affordances.

## Confidence

High confidence:

- `@SET_LOOPREG` is a one-argument source macro.
- The dominant `@SET_LOOPREG > @GOSUB` motif is stage-then-call syntax.
- `@GOSUB` in this motif lowers through existing `0x08` `CALL_TEXT` semantics.
- The motif is broad enough to matter for ordinary script editing, not just
  debug-source reconstruction.

Medium confidence:

- `@SET_LOOPREG(value)` stages a source-local loop/register argument that the
  called text reads, tests, or displays.
- The common `@SET_LOOPREG > @GOSUB > @TRUE_GOTO` triple represents a call that
  leaves a predicate for a following branch.

Still open:

- exact byte sequence emitted for `@SET_LOOPREG`
- whether decimal and symbolic arguments use the same lowering path
- whether the staged value is stored in the work-memory side, arg-memory side,
  scratch memory, or a compiler-local that maps to different VM slots by
  context
- whether repeated `@SET_LOOPREG` chains compile to repeated stores, compact
  generated loops, or source-tool unrolling

## Port-Friendly Source Form

A future reassembly-friendly text source can preserve this as readable syntax:

```text
with_loopreg <value>:
    call_text <label>
```

or:

```text
set_loopreg <value>
call_text <label>
```

The second form is closer to the recovered source. The first form may be nicer
for a higher-level port or text-editing DSL once exact lowering is available.

## Next Proof

The next focused proof should target the selection branch family:
`@DSP_ITEM > @SELGOTO`, `@GOSUB > @SELGOTO`, and `@SELGOTO > @GOTO`.
That cluster appears across many files and should explain how menu/item
selection authoring syntax maps onto `CREATE_SELECTION_MENU`, `JUMP_MULTI`,
and direct `JUMP`/prompt continuations.
