# Text Command Family `0x1E` (Recovery / Experience / Stat Boosts)

This note captures the current local picture of the bank-`01` `0x1E` text-command family.

## Main result

`0x1E` is now pinned as the recovery / experience / stat-boost family of the text engine.

The earlier `0x1D` note accidentally absorbed this family because both sit in the same bank-`01` parser neighborhood. The top-level routing is now clear:

- `0x1D` -> `C1:8AEC` -> `C1:7F11`
- `0x1E` -> `C1:8AF4` -> `C1:811F`
- `0x1F` -> `C1:8AFC` -> `C1:81BB`

So `C1:811F` is the real live parser anchor for `0x1E`.

## Parser-backed family summary

Across the exposed `text_data` segments, the parser-backed hits are already unusually coherent:

- `0x00` = `RECOVER_HP_PERCENT` (11 hits)
- `0x01` = `DEPLETE_HP_PERCENT` (4 hits)
- `0x02` = `RECOVER_HP_AMOUNT` (3 hits)
- `0x04` = `RECOVER_PP_PERCENT` (8 hits)
- `0x05` = `DEPLETE_PP_PERCENT` (3 hits)
- `0x08` = `SET_CHARACTER_LEVEL` (10 hits)
- `0x09` = `GIVE_EXPERIENCE` (2 hits)
- `0x0A` = `BOOST_IQ` (3 hits)
- `0x0B` = `BOOST_GUTS` (3 hits)
- `0x0C` = `BOOST_SPEED` (4 hits)
- `0x0D` = `BOOST_VITALITY` (2 hits)
- `0x0E` = `BOOST_LUCK` (4 hits)

The side reference macro table also shows the full early block:

- `0x00` = `RECOVER_HP_PERCENT`
- `0x01` = `DEPLETE_HP_PERCENT`
- `0x02` = `RECOVER_HP_AMOUNT`
- `0x03` = `DEPLETE_HP_AMOUNT`
- `0x04` = `RECOVER_PP_PERCENT`
- `0x05` = `DEPLETE_PP_PERCENT`
- `0x06` = `RECOVER_PP_AMOUNT`
- `0x07` = `DEPLETE_PP_AMOUNT`

So even where the current exposed script set does not show every one of `0x03/06/07`, the family shape is already strongly constrained.

## Live dispatcher map

The real local dispatcher is `C1:811F`, and its case map is now direct:

- `0x1E 00` -> `C1:49B6`
- `0x1E 01` -> `C1:4A03`
- `0x1E 02` -> `C1:4A50`
- `0x1E 03` -> `C1:4A9D`
- `0x1E 04` -> `C1:4AEA`
- `0x1E 05` -> `C1:4B37`
- `0x1E 06` -> `C1:4B84`
- `0x1E 07` -> `C1:4BD1`
- `0x1E 08` -> `C1:6A01`
- `0x1E 09` -> `C1:744B`
- `0x1E 0A` -> `C1:7523`
- `0x1E 0B` -> `C1:7584`
- `0x1E 0C` -> `C1:75E5`
- `0x1E 0D` -> `C1:7646`
- `0x1E 0E` -> `C1:76A7`

So the family has a stable local execution map instead of being just a macro list.

## High-confidence subfamilies

### Early HP / PP recover-deplete block

The eight early leaves form a very clean structured block:

- `C1:49B6`
- `C1:4A03`
- `C1:4A50`
- `C1:4A9D`
- `C1:4AEA`
- `C1:4B37`
- `C1:4B84`
- `C1:4BD1`

The strongest local pattern is that they come in four shared helper families, with `Y` selecting percent versus amount inside each family:

- `C1:49B6` and `C1:4A50` both call `C1:8F64` = HP recovery, with `Y=0` versus `Y=1`
- `C1:4A03` and `C1:4A9D` both call `C1:8F0E` = HP depletion, with `Y=0` versus `Y=1`
- `C1:4AEA` and `C1:4B84` both call `C1:9010` = PP recovery, with `Y=0` versus `Y=1`
- `C1:4B37` and `C1:4BD1` both call `C1:8FBA` = PP depletion, with `Y=0` versus `Y=1`

Those helper bodies are stronger than they first looked:

- all four support either a direct target id or the wildcard `0x00FF`
- on wildcard input, they loop the active-party family through `$986F` up to boundary `$98A4`
- `Y = 0` computes `max * percent / 100` through `C0:9086` and `C0:90FF`
- `Y = 1` uses the direct queued amount
- the HP-side workers operate on `$99D8` / `$9A15`
- the PP-side workers operate on `$99DA` / `$9A1B`
- recovery workers cap at the corresponding max and also set paired nonzero markers at `$9A13` or `$9A19` if clear
- depletion workers subtract down to `0`

The shared-worker split is now:

- `C1:8F0E` -> `C3:EC1F` = HP depletion
- `C1:8F64` -> `C3:EC8B` = HP recovery
- `C1:8FBA` -> `C3:ED2C` = PP depletion
- `C1:9010` -> `C3:ED98` = PP recovery

So this whole `0x00..0x07` block is now locally coherent rather than only parser-backed. HP versus PP is determined by the helper family, percent versus amount is determined by `Y`, and recover versus deplete is determined by the bank-`03` worker body; see [hp-pp-adjust-helper-quartet-c18f0e-c19010.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/hp-pp-adjust-helper-quartet-c18f0e-c19010.md).

### `0x1E 08 = SET_CHARACTER_LEVEL`

`0x1E 08` routes to `C1:6A01`, which takes one queued byte and one 16-bit signed value, uses `C1:D8D0`, and stages the result through `C1:045D`.

That is a good local fit for `SET_CHARACTER_LEVEL`, and it matches the parser-backed hit pattern:

- 10 hits total
- 9 in `EDEBUG`
- 1 in `EEVENT4`

This is still slightly more parser-backed than behaviorally named, but it now sits in exactly the right local neighborhood.

### `0x1E 09 = GIVE_EXPERIENCE`

`0x1E 09` routes to `C1:744B`, and the local body is now clearer than before:

- it expects four queued bytes total
- `$97BA` is the character selector
- `$97BB/$97BC/$97BD` are assembled into a 24-bit-or-wider amount through repeated `C0:9246` conversion/or steps
- the final payload is handed to `C1:D9E9`

That lines up very well with the parser-backed command:

- `GIVE_EXPERIENCE 0x04, 00:1770` in `E12RAMA`
- `GIVE_EXPERIENCE 0x01, 03:0D40` in `ESYSTEM`

So `C1:744B` is now a strong local fit for the experience-award leaf rather than just an address in the right order.

### `0x1E 0A..0E = stat boosts`

The final five leaves form a clean ordered block:

- `0x1E 0A` -> `C1:7523`
- `0x1E 0B` -> `C1:7584`
- `0x1E 0C` -> `C1:75E5`
- `0x1E 0D` -> `C1:7646`
- `0x1E 0E` -> `C1:76A7`

The parser-backed order is:

- `BOOST_IQ`
- `BOOST_GUTS`
- `BOOST_SPEED`
- `BOOST_VITALITY`
- `BOOST_LUCK`

These bodies are now locally stronger too. Each one:

- queues one byte when staged
- resolves the target character through the same `0x5F`-stride character table mapper
- adds the queued byte into one byte-sized field in the `9A25..9A29` region
- calls a distinct bank-`C2` follow-up helper

Current per-leaf local mapping:

- `C1:7523` adds to `9A28` and calls `C2:1D7D`
- `C1:7584` adds to `9A26` and calls `C2:1BA4`
- `C1:75E5` adds to `9A25` and calls `C2:1AEB`
- `C1:7646` adds to `9A27` and calls `C2:1D65`
- `C1:76A7` adds to `9A29` and calls `C2:1C5D`

So the safest current semantic mapping is still:

- `C1:7523` = `BOOST_IQ`
- `C1:7584` = `BOOST_GUTS`
- `C1:75E5` = `BOOST_SPEED`
- `C1:7646` = `BOOST_VITALITY`
- `C1:76A7` = `BOOST_LUCK`

That mapping is still parser-order-backed more than field-named locally, but the bodies now clearly behave like one-byte stat adders over a shared character-record family.

## Confidence boundaries

### Locally proved

- `0x1E` routes through `C1:8AF4 -> C1:811F`
- `C1:811F` has 15 cases `0x00..0x0E`
- the exact leaf low words listed above
- the early `0x00..0x07` block forms four consistent paired helper families
- those early helpers support explicit target ids and wildcard `0x00FF` active-party loops
- `C1:6A01`, `C1:744B`, and `C1:7523..76A7` belong to `0x1E`, not `0x1D`
- the stat-boost block really does add one-byte values into the `9A25..9A29` character-record region before handing off to bank `C2`; see [equipped-item-derived-cache-family-c21857-c21e03.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/equipped-item-derived-cache-family-c21857-c21e03.md) for the current structural map of that refresh layer
- the five late leaves are now cross-validated better than before:
  - `0x0A -> C1:7523` updates `$9A28` and calls `C2:1D7D`, consistent with `BOOST_IQ`
  - `0x0B -> C1:7584` updates `$9A26` and calls `C2:1BA4`, consistent with `BOOST_GUTS`
  - `0x0C -> C1:75E5` updates `$9A25` and calls `C2:1AEB`, consistent with `BOOST_SPEED`
  - `0x0D -> C1:7646` updates `$9A27` and calls `C2:1D65`, consistent with `BOOST_VITALITY`
  - `0x0E -> C1:76A7` updates `$9A29` and calls `C2:1C5D`, consistent with `BOOST_LUCK`

### Parser-backed or order-backed

- the exact command names for `0x00..0x0E`

### Still open

- the exact player-facing meaning of the nonzero marker writes at `9A13` and `9A19`
- whether the hidden `0x03/06/07` leaves behave exactly like the macro names suggest in the current ROM, even though the macro order strongly implies that they do
- the final status of the rare parser-side `0x1E 10/14/18/19/1F` hits

Current best read on that last point:

- the live runtime dispatcher `C1:811F` explicitly stops at `0x0E` and falls through to `0x0000` for anything else
- the reference macro set also stops at `0x0E`
- the exposed `0x1E 10/14/18/19/1F` hits all sit in event-heavy blocks that already look parser-fragile or partially desynced when disassembled raw

So the safest current interpretation is that those extra subcommands are parser-side artifacts or dead/raw bytes inside dense event-script data, not live supported `0x1E` leaves. I am keeping that as a strong inference rather than a fully proved local fact.

## Best current interpretation

The safest current local read is that `0x1E` is the text engine's recovery / experience / stat-boost family. The dispatcher is now pinned, the HP/PP block is structurally grouped, the level and experience leaves have good local fits, and the five trailing leaves form a clean stat-boost block with real local add-to-field behavior plus a cross-validated IQ/Guts/Speed/Vitality/Luck assignment instead of only macro-order support.

