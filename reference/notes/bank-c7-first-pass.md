# Bank C7 First Pass

## Main result

Bank `C7` is another text-data bank. Like `C5` and `C6`, it has no ordinary
address-bearing unknown code/data include frontier.

Follow-up source-scaffold status:

- durable scaffold: `src/c7/bank_c7_helpers_asar.asm`
- manifest: `build/c7-build-candidate-ranges.json`
- handoff: `notes/bank-c7-source-scaffold-handoff.md`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `11`
- byte-equivalence: `OK`, `0` mismatches

The US ebsrc bank config has support includes plus nine locale text segments:

| Order | Segment | Bank segment | Role |
| ---: | --- | --- | --- |
| 0 | `EHINT` | `BANK07` | hint/debug hint text and pointer-style hint table |
| 1 | `E01ONET1` | `BANK07` | Onett text block |
| 2 | `E01ONET0` | `BANK07` | Onett text block |
| 3 | `E18MGKT` | `BANK07` | Magicant text block |
| 4 | `EGOODS4` | `BANK07` | goods/item text block |
| 5 | `EEVENT1` | `BANK07B` | event/message text block |
| 6 | `EEVENT4` | `BANK07B` | event/message text block |
| 7 | `ESYSTEM` | `BANK07B` | system/prayer/naming text block |
| 8 | `E08DOSEI` | `BANK07B` | Saturn Valley / Mr. Saturn text block |

Generated map:

- `notes/bank-c7-text-data-map.md`
- `build/text-bank-c7.json`

The generated map currently reports:

- text segments: `9`
- total bytes: `65088`
- labels: `914`
- parsed control commands: `21026`
- unknown parsed commands: `6`

The normal bank audit and frontier scorer now also cover C7:

- `notes/bank-c7-progress-audit.md`
- `notes/bank-c7-cluster-map.md`

Both agree that C7 has no address-bearing unknown include frontier.

## Tooling and decoder fixes from this pass

The first C7 text-bank run exposed three real text-command names that were
already corroborated by reference docs or earlier notes, plus the paired
statistic selector name from the same local family:

- `0x19 28` = statistic-letter selector
- `0x1C 11` = make room to display a text character
- `0x1F A2` = check TPT entry flag
- `0x19 27` = statistic value selector, promoted alongside `0x19 28`

More importantly, C7 exposed stale argument widths in the local `0x1F`
movement/sprite decoder. Cross-checking `refs/community-earthbound-docs`
against raw C7 bytes tightened these command sizes:

- `0x1F 13` is byte, byte: change character direction
- `0x1F 1B` is one word: delete floating sprite near TPT entry
- `0x1F 1D` is one byte: delete floating sprite near character
- `0x1F 21` is one byte: teleport to preset coordinates
- `0x1F 63` is two words: screen-reload pointer
- `0x1F E7/E9/EA/EE/EF/F4` are one word
- `0x1F E8` is one byte
- `0x1F EB/EC` are byte, byte

That width pass changed real C7 snippets from desynced output like
`UNKNOWN_1E_1F` into clean movement choreography:

- `C7:9C91` / `C7:9C95` now decode as two character direction changes.
- `C7:9CA2` / `C7:9CA8` now decode as delete/unfreeze generated sprite flow.
- `C7:BD05..BD0D` now decode as three TPT floating-sprite deletes.

The text-bank manifest tool now also stores sample addresses for unknown parser
hits, so future banks do not need a second command-search pass just to locate
the evidence.

## Current C7 confidence boundary

Locally strong:

- C7's bank-level shape is text-only.
- The nine text segments line up contiguously through the bank.
- The segment byte spans and CPU spans are pinned from `earthbound.yml` and ROM
  offsets.
- The label counts and first-label anchors are pinned from `renameLabels`.
- C7 has no address-bearing unknown include frontier.
- All non-EHINT parser unknowns were eliminated by corroborated command names
  or argument-width fixes.

Still cautious:

- The six remaining unknown parsed hits are all in early `EHINT`:
  `C7:00F3`, `C7:00F7`, `C7:00FB`, `C7:00FF`, `C7:0103`, and `C7:0107`.
  The surrounding bytes are pointer-table-shaped values ending in bank byte
  `C7`, not normal text-script flow.
- This pass classifies the bank and validates parser coverage. It does not
  interpret every Onett, Magicant, event, system, or Saturn Valley branch
  semantically.
- Segment roles are mostly inferred from ebsrc names, label prefixes, and
  nearby known notes, not from a complete script walkthrough.

## Recommended next move

Treat C7 as structurally complete for the current bank-coverage phase.

C7 is also byte-protected by the durable source scaffold. Future C7 work should
focus on text VM semantics or richer text-script asset emission, especially
around the early `EHINT` pointer-table-shaped bytes.
