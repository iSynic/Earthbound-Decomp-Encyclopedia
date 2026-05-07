# Text VM / Localization Script Semantics Closeout

This note closes the current Text VM / Localization Script Semantics milestone
for this phase. It does not claim finished text reassembly or a finished
localization compiler. It records why the remaining gaps are now bounded and
non-blocking.

## Phase Result

Milestone 3 is phase-good-enough.

The project now has a durable, public-safe model for the bank-`01` Text VM,
decoded text-bank command usage, and recovered localization authoring syntax:

- `notes/text-command-semantics-manifest.md` covers the top-level runtime
  command map and structured command families.
- `notes/text-script-assets-frontier.md` separates live runtime leaves,
  parser-only pseudo-opcodes, parser artifacts, and recovered authoring syntax.
- `notes/localization-authoring-command-frontier.md` profiles `202` recovered
  source commands without checking in dialogue or full source records.
- `notes/localization-macro-expansion-frontier.md` splits authoring syntax into
  direct runtime hints and macro/markup expansion lanes.
- `notes/localization-control-macro-expansion-model.md` records the source
  control-macro model.
- `notes/localization-cmp-ongosub-lowering.md`,
  `notes/localization-set-loopreg-gosub-lowering.md`, and
  `notes/localization-selgoto-lowering.md` give focused lowering hypotheses for
  the highest-value control-flow motifs.
- `notes/localization-display-inventory-aliases.md` splits display/inventory
  authoring syntax into direct VM aliases and higher-level source macros.

## Good-Enough Criteria

This milestone is good enough because:

- top-level runtime text commands are accounted for as `29 / 32`, with the
  remaining `0x15..0x17` explicitly classified as parser-only compressed-bank
  pseudo-opcodes
- family subcommands are classified as covered, runtime-only, or parser
  artifacts instead of being treated as one undifferentiated unknown pile
- runtime-only leaves are live C1 dispatcher cases with names and addresses,
  but lack observed hits in the current decoded text-bank corpus
- parser artifact candidates are fenced off with segment/context notes and
  should not receive new runtime names without stronger proof
- recovered localization source commands are all bucketed; `0` commands remain
  unclassified in the generated authoring frontier
- the high-value control macro lane now has generated context, pattern, and
  argument-category reports plus three focused lowering hypotheses
- display and inventory aliases are split into direct `0x1C` / `0x1D` source
  aliases versus higher-level source macros

That is enough for romhackers and future source tooling to avoid guessing
whether an unmatched authoring command is a new bytecode opcode, source-only
metadata, a macro over existing VM commands, or an artifact of parser overlap.

## What Remains

Remaining work is intentionally deferred, not forgotten.

### Runtime-only leaves

`notes/text-script-assets-frontier.md` still lists `25` runtime-only family
leaves. They are real dispatcher surface area, but they are not blockers for
this milestone because they already have live addresses and names. Most are
rare menu/system helpers, no-op argument shims, or special UI/service leaves.

Future work should add deeper notes only when one of these leaves becomes
important for a concrete source-editing or porting task.

### Parser artifacts

The `9` parsed artifact candidates should stay visible but out of naming work.
They are current evidence of table, pointer, compressed-data, or dense-script
overlap, not proved runtime commands.

Future parser work can improve boundaries around `EDEBUG`, `ENEWS`, `EHINT`,
and `EBATTLE8`, but this is not required to close the semantics phase.

### Authoring format markup

Source markers such as `@WI`, `@A`, `@M`, `@H`, `@P`, `@F`, `@G`, and `@C`
still need a dedicated source-format pass if the goal is exact recovered-source
round-tripping. For this phase, they are safely classified as authoring-format
markup rather than runtime VM opcodes.

### Higher-level macro lanes

The following lanes remain useful future work:

- movement/camera/visibility macros, which should join C3/map-object
  event-actionscript semantics
- shop/Escargo/display helpers, which likely lower through multiple `0x1A`,
  `0x19`, `0x1C`, and `0x1D` operations
- status and battle-text macros, which should be handled when C2/EF and battle
  text payloads are the active focus
- rare multi-argument `@ONGOSUB` / `@ONGOTO` forms, which are not blocking the
  common control-flow source model

## Source / Porting Contract

For future reassembly-friendly text source, use this contract:

- preserve readable aliases such as `@GOSUB`, `@GOTO`, `@KEY`, `@KEYNP`,
  `@DSP_NAME`, `@DSP_GOODS`, `@GOODSIN_PLAYER`, and `@Q_MONEY`
- preserve source macros such as `@CMP > @ONGOSUB`, `@SET_LOOPREG > @GOSUB`,
  and `@SELGOTO` until exact byte templates are proven
- do not invent new runtime opcodes for recovered authoring conveniences
- treat parser-only pseudo-opcodes and artifact candidates as parser/tooling
  concerns, not game VM features
- keep recovered dialogue/source payloads ignored unless a future public-safe
  extraction workflow is explicitly designed

The structured follow-up model is now generated by
`tools/build_localization_macro_expansion_model.py`, documented in
`notes/localization-macro-expansion-model.md`, and checked by
`tools/validate_localization_macro_expansion_model.py`. It currently records
`15` proven control/register/branch source macro shapes, `23` direct
display/inventory VM aliases, and `38` unresolved display/inventory source
macros.

## Next Recommended Phase

The next highest-value work should move out of milestone 3 and into subsystem
semantics or asset extraction planning:

1. C0/C2/C4 subsystem side-effect contracts for overworld, battle, and
   rendering flows.
2. Asset/decode fixture planning for map, graphics, UI/font, and audio banks.
3. Targeted text follow-up only when needed by a concrete source-editing,
   reinsertion, or porting task; the next such pass should start with operand
   syntax for direct aliases such as `@DSP_GOODS`, `@DSP_ITEM`, `@DSP_NAME`,
   `@Q_MONEY`, `@GOODSIN_PLAYER`, and `@Q_GOODSFULL`.

This keeps the project moving toward practical romhacking and eventual porting
without polishing text macros indefinitely.
