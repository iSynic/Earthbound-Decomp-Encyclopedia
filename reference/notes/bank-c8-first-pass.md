# Bank C8 First Pass

## Main result

Bank `C8` is still a text/data bank, not an ordinary code frontier. It differs
from `C5` through `C7` because the bank config mixes locale text segments with
the shared compressed-text dictionary data/pointer includes.

Follow-up source-scaffold status:

- durable scaffold: `src/c8/bank_c8_helpers_asar.asm`
- manifest: `build/c8-build-candidate-ranges.json`
- handoff: `notes/bank-c8-source-scaffold-handoff.md`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `11`
- byte-equivalence: `OK`, `0` mismatches

The US ebsrc bank config has support includes, eight locale text segments, and
two compressed-text includes:

| Order | Include | Bank segment | Role |
| ---: | --- | --- | --- |
| 0 | `E02TWSN0` | `BANK08` | Twoson text block |
| 1 | `E10FOUR1` | `BANK08` | Fourside text block |
| 2 | `ENEWS` | `BANK08` | newspaper text/pointer-list block |
| 3 | `EBGMESS` | `BANK08` | background/event message text block |
| 4 | `EEVENT2` | `BANK08B` | event/message text block |
| 5 | `E11SUMS` | `BANK08B` | Summers text block |
| 6 | `data/text/compressed_text_data.asm` | `BANK08B` | shared compressed text dictionary data |
| 7 | `data/text/compressed_text_pointers.asm` | `BANK08B` | shared compressed text dictionary pointers |
| 8 | `E05THRK` | `BANK08B` | Threed text block |
| 9 | `EBATTLE6` | `BANK08B` | battle text block |

Generated map:

- `notes/bank-c8-text-data-map.md`
- `build/text-bank-c8.json`

The generated map currently reports:

- locale text segments: `8`
- locale text bytes: `57686`
- non-locale/gap bytes: `7850` across `3` gaps
- labels: `858`
- parsed control commands: `18053`
- unknown parsed commands: `3`

The normal bank audit and frontier scorer now also cover C8:

- `notes/bank-c8-progress-audit.md`
- `notes/bank-c8-cluster-map.md`

Both agree that C8 has no address-bearing unknown include frontier.

## Coverage gaps

`tools/build_text_bank_manifest.py` now records text-bank coverage gaps. For C8
that matters because the middle gap is intentional data, not missing work:

| CPU span | Bytes | Current read |
| --- | ---: | --- |
| `C8:7F23..C8:7FFF` | `221` | segment-boundary padding/slack before `BANK08B` |
| `C8:BC2D..C8:D9EC` | `7616` | compressed-text dictionary data plus pointer table |
| `C8:FFF3..C8:FFFF` | `13` | tail slack after `EBATTLE6` |

The exact split between `compressed_text_data.asm` and
`compressed_text_pointers.asm` is not pinned locally yet because the ebsrc
reference tree exposes those includes in the bank config and symbol file, but
not as checked-in source files in this refs snapshot.

## Tooling and decoder fixes from this pass

C8 exposed one real missing text command name:

- `0x1F 62` = set blinking triangle flag

This is corroborated by `refs/community-earthbound-docs/Control_codes.txt` and
by the EBATTLE6 contexts around `C8:FB23`, `C8:FC34`, `C8:FD18`, and
`C8:FF38`. Promoting the name reduced C8's unknown parsed command count from
`7` to `3`.

The remaining three unknowns are all in `ENEWS`:

- `C8:435D` = `UNKNOWN_1A_48`
- `C8:4A59` = `UNKNOWN_1F_4E`
- `C8:4A61` = `UNKNOWN_19_4F`

The surrounding bytes are pointer-list-shaped values ending in bank byte `C8`,
followed by ordinary newspaper text. These should be treated as linear parser
artifacts, not promoted as text command semantics.

## Current C8 confidence boundary

Locally strong:

- C8's bank-level shape is text/data, not code.
- The eight locale text segments line up with `earthbound.yml` offsets/sizes and
  `renameLabels`.
- The only substantial non-locale span is exactly where the bank config inserts
  compressed-text data and pointers.
- C8 has no address-bearing unknown include frontier.
- All non-ENEWS parser unknowns were eliminated by the `0x1F 62` name promotion.

Still cautious:

- The compressed text island is classified by include order and gap geometry,
  but the local refs snapshot does not provide the generated include contents,
  so its internal data/pointer boundary is not byte-pinned here.
- This pass classifies the bank and validates parser coverage. It does not
  semantically interpret every Twoson, Fourside, newspaper, Summers, Threed, or
  battle text branch.
- `ENEWS` contains pointer-list-shaped bytes that a linear text parser can
  misread as commands. Future semantic work should start from label boundaries,
  not arbitrary command-hit addresses inside that table region.

## Recommended next move

Treat C8 as structurally complete for the current bank-coverage phase.

C8 is also byte-protected by the durable source scaffold. The next C8-specific
semantic improvement is splitting the `C8:BC2D..C8:D9ED` compressed-text island
into dictionary data and pointer-table subranges once that generated include
boundary is pinned.
