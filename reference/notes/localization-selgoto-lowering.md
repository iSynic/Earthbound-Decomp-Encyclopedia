# Localization `@SELGOTO` Lowering Hypothesis

This note captures the third focused lowering hypothesis for recovered `.MSG`
control macros. It uses generated command-only and argument-category evidence;
recovered dialogue, raw argument values, labels, and full source records remain
ignored.

## Inputs

- `notes/localization-control-macro-context.md`
- `notes/localization-control-macro-patterns.md`
- `notes/localization-control-macro-lowering-profiles.md`
- `notes/localization-set-loopreg-gosub-lowering.md`
- bank-`01` Text VM notes for menu setup, `JUMP_MULTI`, direct `JUMP`,
  `CALL_TEXT`, print/display, and menu/selection family `0x1A`

## Evidence

The generated reports isolate `@SELGOTO` as the main recovered source macro for
selection-result branching:

- `@SELGOTO`: `250` context hits, nearly always `2` arguments
- argument profile: `@SELGOTO(symbol,symbol)` for `235` of the profiled hits
- `@DSP_ITEM > @SELGOTO`: `188` adjacent hits across `35` files
- `@GOSUB > @SELGOTO`: `57` adjacent hits across `8` files
- `@SELGOTO > @KEY`: `68` adjacent hits across `26` files
- `@SELGOTO > @GOTO`: `53` adjacent hits across `20` files
- `@SELGOTO > @KEYNP`: `46` adjacent hits across `24` files

The strongest argument-category forms are:

- `@DSP_ITEM(decimal) > @SELGOTO(symbol,symbol)`: `175`
- `@GOSUB(message_label) > @SELGOTO(symbol,symbol)`: `49`
- `@SELGOTO(symbol,symbol) > @KEY(empty)`: `67`
- `@SELGOTO(symbol,symbol) > @GOTO(symbol)`: `44`
- `@SELGOTO(symbol,symbol) > @KEYNP(empty)`: `45`

That shape is broad and ordinary-script-heavy. Unlike the debug-heavy
`@CMP > @ONGOSUB` proof, `@SELGOTO` appears across many files and sits directly
on item-display, helper-call, prompt, and jump neighborhoods.

## Working Read

The safest current read is:

```text
@DSP_ITEM(item_slot_or_selector)
@SELGOTO(choice_1_target, choice_2_target)
```

or:

```text
@GOSUB(selection_setup_text)
@SELGOTO(choice_1_target, choice_2_target)
```

means:

```text
prepare visible selection text or selection-side state
run or consume the active selection result
branch to one of the source targets
continue through prompt, no-prompt, or direct jump syntax
```

This is source-level selection branch syntax. It should not be treated as a new
runtime opcode.

## Likely Lower-Level Ingredients

The exact byte template is still open, but the likely primitive set is already
documented:

- `0x11` `CREATE_SELECTION_MENU`: single menu setup helper
- `0x09` `JUMP_MULTI`: counted branch over the live 1-based working-memory
  selector
- `0x0A` `JUMP`: direct 24-bit jump for explicit source `@GOTO` continuations
- `0x08` `CALL_TEXT`: helper text or source subroutine call for `@GOSUB`
  setup paths
- `0x1A`: menu/selection family for party, inventory, shop, Escargo, phone,
  and teleport menu flows
- `0x1C 05`: item-name display for `@DSP_ITEM`-style setup
- `0x03` / `0x13`: prompt and no-prompt halts for `@KEY` and `@KEYNP`

The strongest plausible lowering shape is therefore:

```text
prepare option text, item text, or helper-call selection state
create or consume the current selection menu/result
JUMP_MULTI over the two source targets
each selected branch resumes through prompt, no-prompt, direct jump, or
ordinary fallthrough text
```

This is deliberately a source-to-VM shape rather than a final byte template.
The generated profiles prove the authoring motif and argument categories; they
do not prove whether every `@SELGOTO(a,b)` emits a literal `JUMP_MULTI count=2`
at the call site, or whether some surrounding macros lower the menu setup and
branch table as a larger fused source-tool expansion.

## Why `@SELGOTO` Is Not Just `JUMP_MULTI`

`0x09` `JUMP_MULTI` is the lower-level counted branch primitive. `@SELGOTO` is
the recovered source syntax that sits above it.

The difference matters:

- `JUMP_MULTI` consumes a live selector and a table of 24-bit branch entries.
- `@SELGOTO` carries source labels and appears next to display/setup macros.
- `@SELGOTO` continuations are often prompt commands (`@KEY`, `@KEYNP`) or
  source-level direct jumps (`@GOTO`), which means the branch target bodies are
  part of the authoring structure, not simply a raw table.

So a future reassembler should be allowed to preserve `@SELGOTO` as readable
source syntax and lower it into `JUMP_MULTI` plus surrounding prompt/jump
machinery only when emitting bytes.

## Confidence

High confidence:

- `@SELGOTO` is a source-level selection-result branch macro.
- The dominant form is two-argument branch syntax.
- `@DSP_ITEM > @SELGOTO` is item-display or item-selection setup followed by
  selection branching.
- `@GOSUB > @SELGOTO` is helper-call setup followed by selection branching.
- The macro lowers onto existing bank-`01` menu/display/branch primitives, not
  a new runtime VM.

Medium confidence:

- The common two-target form usually lowers to `JUMP_MULTI count=2` or an
  equivalent two-way branch over the active selector.
- `@SELGOTO > @KEY`, `@SELGOTO > @KEYNP`, and `@SELGOTO > @GOTO` represent
  ordinary branch-body continuations rather than separate variants of the
  branch macro itself.

Still open:

- exact byte sequence emitted for `@SELGOTO`
- whether all two-argument forms use the same lowering path
- how the rare empty, three-argument, and mixed message-label forms lower
- whether item-display setup and helper-call setup share one backend or two
  source-tool templates

## Port-Friendly Source Form

A future reassembly-friendly text source can preserve this as readable syntax:

```text
select_goto <choice_1_target>, <choice_2_target>
```

or, when paired with display/setup:

```text
display_item <selector>
select_goto <choice_1_target>, <choice_2_target>
```

For a higher-level port, this may become a structured choice block:

```text
choice:
    option 1 -> <choice_1_target>
    option 2 -> <choice_2_target>
```

The important constraint is that it remains selection-branch source syntax
until the exact byte lowering is proven.

## Next Proof

The next focused proof should leave the control-macro lane and move to
display/inventory alias consolidation. The obvious target is a compact note
that ties high-count recovered aliases such as `@DSP_ITEM`, `@DSP_NAME`,
`@DSP_STS`, `@GOODSIN_PLAYER`, and related shop/item commands to the already
documented `0x1C` and `0x1D` Text VM families.
