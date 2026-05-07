# Bank C6 Source Scaffold Handoff

## Status

Bank `C6` is byte-complete for the current source-scaffold phase.

- durable scaffold: `src/c6/bank_c6_helpers_asar.asm`
- manifest: `build/c6-build-candidate-ranges.json`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `9`
- source bytes: `0`
- preserved data-gap bytes: `65536`
- byte-equivalence: `OK`, `0` mismatches

C6 is a text/data scaffold, not executable source. The bank is protected as
seven locale text corridors plus two explicit padding/alignment ranges.

## Regenerate And Validate

Use these commands from the repository root:

```powershell
python tools\build_text_bank_manifest.py C6 --json-out build\text-bank-c6.json --markdown-out notes\bank-c6-text-data-map.md
python tools\promote_text_bank_to_source_scaffold.py C6
python tools\build_source_bank_scaffold.py --bank C6
python tools\validate_source_bank_byte_equivalence.py --bank C6 --module all --combined --scaffold src\c6\bank_c6_helpers_asar.asm --strict
python tools\build_source_bank_candidate_ranges_doc.py --bank C6
python tools\build_source_bank_residual_map.py --bank C6
```

Expected validation:

- `C6 byte-equivalence: OK, 9 module(s), 0 mismatch(es).`
- `notes/c6-source-residual-map.md` reports `0` residual bytes and `0`
  residual ranges.

## Protected Ranges

| Range | Stub | Purpose |
| --- | --- | --- |
| `C6:0000..C6:2D30` | `src/c6/text_e09dsrt.asm` | `E09DSRT` locale text segment |
| `C6:2D30..C6:59C9` | `src/c6/text_eshop3.asm` | `ESHOP3` locale text segment |
| `C6:59C9..C6:7EEC` | `src/c6/text_e01onet2.asm` | `E01ONET2` locale text segment |
| `C6:7EEC..C6:8000` | `src/c6/text_bank_c6_gap_1_alignmentgap.asm` | bank-segment alignment gap |
| `C6:8000..C6:A9F9` | `src/c6/text_eglobal.asm` | `EGLOBAL` locale text segment |
| `C6:A9F9..C6:D19C` | `src/c6/text_e06wins.asm` | `E06WINS` locale text segment |
| `C6:D19C..C6:F8D9` | `src/c6/text_e10four0.asm` | `E10FOUR0` locale text segment |
| `C6:F8D9..C6:FFE3` | `src/c6/text_egoods3.asm` | `EGOODS3` locale text segment |
| `C6:FFE3..C6:10000` | `src/c6/text_bank_c6_gap_2_tailpadding.asm` | zero-filled bank-end padding |

## Remaining Semantic Work

The C6 text manifest has zero unknown parser starts, so there is no immediate
decoder fire to chase here. Future work is text VM polish and richer text-script
asset emission after C7-C9 have gone through the same scaffold path.

