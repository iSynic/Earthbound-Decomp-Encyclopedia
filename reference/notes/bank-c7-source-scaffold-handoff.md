# Bank C7 Source Scaffold Handoff

## Status

Bank `C7` is byte-complete for the current source-scaffold phase.

- durable scaffold: `src/c7/bank_c7_helpers_asar.asm`
- manifest: `build/c7-build-candidate-ranges.json`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `11`
- source bytes: `0`
- preserved data-gap bytes: `65536`
- byte-equivalence: `OK`, `0` mismatches

C7 is protected as nine locale text corridors plus two explicit
padding/alignment ranges.

## Regenerate And Validate

Use these commands from the repository root:

```powershell
python tools\build_text_bank_manifest.py C7 --json-out build\text-bank-c7.json --markdown-out notes\bank-c7-text-data-map.md
python tools\promote_text_bank_to_source_scaffold.py C7
python tools\build_source_bank_scaffold.py --bank C7
python tools\validate_source_bank_byte_equivalence.py --bank C7 --module all --combined --scaffold src\c7\bank_c7_helpers_asar.asm --strict
python tools\build_source_bank_candidate_ranges_doc.py --bank C7
python tools\build_source_bank_residual_map.py --bank C7
```

Expected validation:

- `C7 byte-equivalence: OK, 11 module(s), 0 mismatch(es).`
- `notes/c7-source-residual-map.md` reports `0` residual bytes and `0`
  residual ranges.

## Protected Ranges

| Range | Stub | Purpose |
| --- | --- | --- |
| `C7:0000..C7:2709` | `src/c7/text_ehint.asm` | `EHINT` locale text segment |
| `C7:2709..C7:4BA9` | `src/c7/text_e01onet1.asm` | `E01ONET1` locale text segment |
| `C7:4BA9..C7:6F20` | `src/c7/text_e01onet0.asm` | `E01ONET0` locale text segment |
| `C7:6F20..C7:7DCE` | `src/c7/text_e18mgkt.asm` | `E18MGKT` locale text segment |
| `C7:7DCE..C7:7F00` | `src/c7/text_egoods4.asm` | `EGOODS4` locale text segment |
| `C7:7F00..C7:8000` | `src/c7/text_bank_c7_gap_1_alignmentgap.asm` | bank-segment alignment gap |
| `C7:8000..C7:A2F7` | `src/c7/text_eevent1.asm` | `EEVENT1` locale text segment |
| `C7:A2F7..C7:C588` | `src/c7/text_eevent4.asm` | `EEVENT4` locale text segment |
| `C7:C588..C7:E797` | `src/c7/text_esystem.asm` | `ESYSTEM` locale text segment |
| `C7:E797..C7:FF40` | `src/c7/text_e08dosei.asm` | `E08DOSEI` locale text segment |
| `C7:FF40..C7:10000` | `src/c7/text_bank_c7_gap_2_tailpadding.asm` | bank-end padding |

## Remaining Semantic Work

The remaining C7 parser unknowns are still confined to early `EHINT`
pointer-table-shaped bytes. Treat C7 as structurally closed; revisit it for
text VM semantics or richer script asset emission after C8/C9 are in the same
regression set.

