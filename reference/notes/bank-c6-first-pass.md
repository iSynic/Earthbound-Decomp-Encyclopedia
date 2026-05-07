# Bank C6 First Pass

## Main result

Bank `C6` is another text-data bank. Like `C5`, it has no ordinary
address-bearing unknown code/data include frontier.

Follow-up source-scaffold status:

- durable scaffold: `src/c6/bank_c6_helpers_asar.asm`
- manifest: `build/c6-build-candidate-ranges.json`
- handoff: `notes/bank-c6-source-scaffold-handoff.md`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `9`
- byte-equivalence: `OK`, `0` mismatches

The US ebsrc bank config has support includes plus seven locale text segments:

| Order | Segment | Bank segment | Role |
| ---: | --- | --- | --- |
| 0 | `E09DSRT` | `BANK06` | Dusty Dunes / desert text block |
| 1 | `ESHOP3` | `BANK06` | shop/service text block |
| 2 | `E01ONET2` | `BANK06` | Onett text block |
| 3 | `EGLOBAL` | `BANK06B` | global/common text block |
| 4 | `E06WINS` | `BANK06B` | Winters text block |
| 5 | `E10FOUR0` | `BANK06B` | Fourside text block |
| 6 | `EGOODS3` | `BANK06B` | goods/item text block |

Generated map:

- `notes/bank-c6-text-data-map.md`
- `build/text-bank-c6.json`

The generated map currently reports:

- text segments: `7`
- total bytes: `65231`
- labels: `1024`
- parsed control commands: `21184`
- unknown parsed commands: `0`

The normal bank audit and frontier scorer now also cover C6:

- `notes/bank-c6-progress-audit.md`
- `notes/bank-c6-cluster-map.md`

Both agree that C6 has no address-bearing unknown include frontier.

## Tooling and decoder fixes from this pass

The first C6 run exposed a few text-command names that were already understood
elsewhere but missing from the decoder:

- `0x19 14` = Escargo storage item enumeration / return item from storage
- `0x19 26` = transition landing-target snapshot helper
- `0x1F E8` = unfreeze character movement

Promoting those names dropped C6's unknown parsed command count from `13` to
`2`.

The remaining two hits were both `0x1E 18`, but they appeared immediately after
`0x1F 16` commands. Cross-checking the community control-code docs showed that
`0x1F 16` takes a TPT-entry word plus a one-byte direction, not two words. The
local parser was over-consuming one byte, which created the false `0x1E 18`
starts.

The decoder now treats:

- `0x1F 15` as `word, word, byte`
- `0x1F 16` as `word, byte`
- `0x1F 17` as `word, word, byte`
- `0x1F 18/19` as seven-argument no-op commands

After that correction, C6 had zero unknown parsed command starts. A later C7
width pass corrected several more `0x1F` movement/sprite argument sizes; C6
still has zero unknown parsed command starts under the tightened decoder.

## Current C6 confidence boundary

Locally strong:

- C6's bank-level shape is text-only.
- The seven text segments line up contiguously through the bank.
- The segment byte spans and CPU spans are pinned from `earthbound.yml` and ROM
  offsets.
- The label counts and first-label anchors are pinned from `renameLabels`.
- The C6 text-command usage now fully parses with the locally documented command
  vocabulary.

Still cautious:

- This pass classifies the bank and validates parser coverage. It does not
  interpret every Dusty Dunes, Onett, Winters, Fourside, shop, or global script
  branch semantically.
- Some segment roles are inferred from ebsrc names and label prefixes, not from
  player-facing script walkthroughs.

## Recommended next move

Treat C6 as structurally complete for the current bank-coverage phase.

The next high-value step is `C7` with the same text-bank scaffold promotion
workflow. A preview run already showed that C7 is also text-data-shaped, but it
still has more parser unknowns than C6 after the current decoder improvements,
so it may produce the next useful text-command decoder corrections.
