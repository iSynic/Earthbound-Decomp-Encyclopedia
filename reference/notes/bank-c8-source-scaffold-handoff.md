# Bank C8 Source Scaffold Handoff

## Status

Bank `C8` is byte-complete for the current source-scaffold phase.

- durable scaffold: `src/c8/bank_c8_helpers_asar.asm`
- manifest: `build/c8-build-candidate-ranges.json`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `11`
- source bytes: `0`
- preserved data-gap bytes: `65536`
- byte-equivalence: `OK`, `0` mismatches

C8 is protected as eight locale text corridors, two padding ranges, and one
non-locale data island for the compressed-text dictionary region.

## Regenerate And Validate

Use these commands from the repository root:

```powershell
python tools\build_text_bank_manifest.py C8 --json-out build\text-bank-c8.json --markdown-out notes\bank-c8-text-data-map.md
python tools\promote_text_bank_to_source_scaffold.py C8
python tools\build_source_bank_scaffold.py --bank C8
python tools\validate_source_bank_byte_equivalence.py --bank C8 --module all --combined --scaffold src\c8\bank_c8_helpers_asar.asm --strict
python tools\build_source_bank_candidate_ranges_doc.py --bank C8
python tools\build_source_bank_residual_map.py --bank C8
```

Expected validation:

- `C8 byte-equivalence: OK, 11 module(s), 0 mismatch(es).`
- `notes/c8-source-residual-map.md` reports `0` residual bytes and `0`
  residual ranges.

## Protected Ranges

| Range | Stub | Purpose |
| --- | --- | --- |
| `C8:0000..C8:2105` | `src/c8/text_e02twsn0.asm` | `E02TWSN0` locale text segment |
| `C8:2105..C8:41DE` | `src/c8/text_e10four1.asm` | `E10FOUR1` locale text segment |
| `C8:41DE..C8:6279` | `src/c8/text_enews.asm` | `ENEWS` locale text segment |
| `C8:6279..C8:7F23` | `src/c8/text_ebgmess.asm` | `EBGMESS` locale text segment |
| `C8:7F23..C8:8000` | `src/c8/text_bank_c8_gap_1_alignmentgap.asm` | bank-segment alignment gap |
| `C8:8000..C8:9E1B` | `src/c8/text_eevent2.asm` | `EEVENT2` locale text segment |
| `C8:9E1B..C8:BC2D` | `src/c8/text_e11sums.asm` | `E11SUMS` locale text segment |
| `C8:BC2D..C8:D9ED` | `src/c8/text_bank_c8_gap_2_nonlocaledataisland.asm` | compressed-text dictionary data/pointer island |
| `C8:D9ED..C8:F77D` | `src/c8/text_e05thrk.asm` | `E05THRK` locale text segment |
| `C8:F77D..C8:FFF3` | `src/c8/text_ebattle6.asm` | `EBATTLE6` locale text segment |
| `C8:FFF3..C8:10000` | `src/c8/text_bank_c8_gap_3_tailpadding.asm` | bank-end padding |

## Remaining Semantic Work

The main C8 follow-up is to split the `C8:BC2D..C8:D9ED` compressed-text island
into dictionary data and pointer-table subranges once the generated include
boundary is pinned. The remaining ENEWS parser unknowns still look like linear
parser artifacts inside pointer-list-shaped bytes.

