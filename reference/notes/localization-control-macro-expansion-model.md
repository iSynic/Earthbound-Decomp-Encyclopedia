# Localization Control Macro Expansion Model

This note captures the first practical expansion model for recovered `.MSG`
control macros. It uses structural command context only; recovered dialogue and
full source records remain ignored.

## Main Result

The recovered control macros are best treated as source-level conveniences over
the existing bank-`01` text VM control and memory commands, not as a separate
runtime VM.

The current strongest split is:

- direct text VM controls already mapped: `@GOSUB`, `@GOTO`, `@TRUE_GOTO`,
  `@FALSE_GOTO`, `@CHKFGOTO`
- register/memory helper macros needing expansion models: `@SET_LOOPREG`,
  `@LOAD_REG`, `@SAVE_REG`, `@SET_REG`, `@LOAD_GLOBAL_REG`,
  `@SAVE_GLOBAL_REG`, `@CMP`, `@EQ`, `@INC`, `@SUB`, `@NOT`
- multi-way source branch macros needing expansion models: `@ONGOSUB`,
  `@ONGOTO`, `@SELGOTO`, `@SEL_TEL_GOSUB`

The generated context report is
`notes/localization-control-macro-context.md`.
The generated pattern report is
`notes/localization-control-macro-patterns.md`.
The first focused lowering hypothesis is
`notes/localization-cmp-ongosub-lowering.md`.
The second focused lowering hypothesis is
`notes/localization-set-loopreg-gosub-lowering.md`.
The third focused lowering hypothesis is
`notes/localization-selgoto-lowering.md`.

## Local VM Anchors

The runtime-side anchors are already documented in the text-command notes:

- `0x08` `CALL_TEXT`: far text call through nested text execution
- `0x09` `JUMP_MULTI`: counted branch over a 1-based working-memory selector
- `0x0A` `JUMP`: direct 24-bit jump
- `0x0B` / `0x0C`: parameterized working-memory true/false tests
- `0x0D` / `0x0E`: copy/store into the arg-memory side
- `0x0F`: increment the working-memory side
- `0x1B 02` / `0x1B 03`: false/true branches over current context state
- `0x1B 04`: swap working and arg memory
- `0x1B 05` / `0x1B 06`: copy active context to/from scratch memory

That means the authoring control macros can probably be modeled as structured
source syntax over a small VM core: staged memory, comparisons, direct jumps,
calls, and counted branch tables.

## Structural Evidence

The generated context shows the center of gravity:

- `@SET_LOOPREG`: `325` hits, commonly followed by `@GOSUB` or another
  `@SET_LOOPREG`
- `@CMP`: `312` hits, commonly adjacent to `@ONGOSUB`,
  `@FALSE_GOTO`, and `@TRUE_GOTO`
- `@ONGOSUB`: `280` hits, overwhelmingly paired with `@CMP`
- `@SELGOTO`: `250` hits, usually following item/text display setup and then
  branching to `@GOTO`, prompt, or terminal text commands
- `@LOAD_REG` / `@SAVE_REG` / `@SET_REG`: frequent context-staging helpers
  adjacent to `@EQ`, `@XCHG`, display commands, inventory commands, and
  branches

The generated pattern report sharpens that into command-sequence evidence:

- `@CMP > @ONGOSUB` and `@ONGOSUB > @CMP`: `254` adjacent hits each, all in
  `EDEBUG.MSG`, making this the clearest compare/table-call proof case.
- `@SET_LOOPREG > @GOSUB`: `191` adjacent hits across `31` files, with a
  second `@SET_LOOPREG > @SET_LOOPREG` motif at `77` hits. This supports a
  source-level staging/loop initializer read rather than a new runtime opcode.
- `@DSP_ITEM > @SELGOTO`: `188` adjacent hits across `35` files, followed by
  prompt/jump-style continuations such as `@KEY`, `@GOTO`, and `@KEYNP`.
  This supports treating `@SELGOTO` as selection-result branch syntax.
- The sanitized lowering profile shows the dominant `@CMP > @ONGOSUB` form is
  always `@CMP(decimal,decimal) > @ONGOSUB(message_label)`. That makes it a
  repeated compare plus one-label conditional-call motif, not the common shape
  of a many-label source table.
- The expanded lowering profile shows `@SELGOTO` is overwhelmingly a
  two-argument source branch form: `@SELGOTO(symbol,symbol)` accounts for
  `235` profiled hits, and the strongest setup motifs are
  `@DSP_ITEM > @SELGOTO` and `@GOSUB > @SELGOTO`.

This strongly suggests a compiler-like authoring layer: the source macros stage
or compare small values, then expand into existing text VM branch/call helpers.

## First Expansion Hypotheses

These are intentionally phrased as expansion hypotheses, not final byte
templates.

| Source macro | Current expansion read | Confidence |
| --- | --- | --- |
| `@SET_LOOPREG(x)` before `@GOSUB` | Stage source-local loop/register value before a text subroutine call. | high |
| `@SET_LOOPREG(x)` elsewhere | Stage loop/register value used by nearby repeated calls or comparisons. | medium |
| `@CMP(a,b)` | Compare staged values before a branch/multi-way call macro. | medium |
| `@EQ(x)` | Test equality against the current staged/register value. | medium |
| `@LOAD_REG()` | Restore local source register into the active text context. | medium |
| `@SAVE_REG()` | Save active text context into a local source register. | medium |
| `@SET_REG(x)` | Set local source register to an immediate or symbolic value. | medium |
| `@INC()` | Increment the current staged working-memory/register value. | medium |
| `@NOT(x)` | Invert or negate a staged predicate before branch use. | low |
| `@ONGOSUB(label)` after `@CMP` | Source-level conditional call controlled by the immediately preceding compare. | high |
| `@ONGOSUB(...)` multi-arg forms | Source-level multi-way call table or call-chain syntax; still separate from the dominant one-label motif. | medium |
| `@ONGOTO(...)` | Source-level multi-way jump table, probably over current comparison/selector state. | medium |
| `@SELGOTO(a,b)` | Two-way selection-result branch over the most recent menu/selection value. | high |
| `@SELGOTO(...)` rare forms | Selection-result branch syntax with less common arity/label shapes. | medium |
| `@SEL_TEL_GOSUB()` | Teleport-selection call helper; likely a narrow wrapper over selection and call semantics. | low |

## What This Gets Us

For romhacking and eventual source-level text editing, this model means we do
not need to expose only raw bytecode. A future source form can preserve useful
authoring syntax like:

- set or save a local text-script register
- compare that register
- branch or call based on selection/comparison results
- display text/data using readable aliases

Then a compiler or reassembler can lower that syntax into the smaller bank-`01`
text VM primitives.

## Next Manual Proof

The `@CMP > @ONGOSUB`, `@SET_LOOPREG > @GOSUB`, and `@SELGOTO` lowering
hypotheses are now documented. Display/inventory aliases are split in
`notes/localization-display-inventory-aliases.md`.

The next best proof should be a cleanup/closeout pass:

1. mark the control-flow macro lane as phase-good-enough
2. mark display/inventory aliases as direct VM aliases versus source macros
3. decide whether remaining runtime-only leaves and parser artifacts need any
   new notes before milestone 3 closes

The goal is not to recover dialogue. The goal is to prove the source macro's
lowering shape against already-documented text VM commands.
