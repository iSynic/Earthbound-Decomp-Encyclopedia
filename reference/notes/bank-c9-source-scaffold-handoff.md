# Bank C9 Source Scaffold Handoff

## Status

Bank `C9` is byte-complete for the current source-scaffold phase.

- durable scaffold: `src/c9/bank_c9_helpers_asar.asm`
- manifest: `build/c9-build-candidate-ranges.json`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `16`
- source bytes: `0`
- preserved data-gap bytes: `65536`
- byte-equivalence: `OK`, `0` mismatches

C9 is protected as fourteen locale text corridors plus two explicit
padding/alignment ranges.

## Regenerate And Validate

Use these commands from the repository root:

```powershell
python tools\build_text_bank_manifest.py C9 --json-out build\text-bank-c9.json --markdown-out notes\bank-c9-text-data-map.md
python tools\promote_text_bank_to_source_scaffold.py C9
python tools\build_source_bank_scaffold.py --bank C9
python tools\validate_source_bank_byte_equivalence.py --bank C9 --module all --combined --scaffold src\c9\bank_c9_helpers_asar.asm --strict
python tools\build_source_bank_candidate_ranges_doc.py --bank C9
python tools\build_source_bank_residual_map.py --bank C9
```

Expected validation:

- `C9 byte-equivalence: OK, 16 module(s), 0 mismatch(es).`
- `notes/c9-source-residual-map.md` reports `0` residual bytes and `0`
  residual ranges.

## Protected Ranges

| Range | Stub | Purpose |
| --- | --- | --- |
| `C9:0000..C9:1C3A` | `src/c9/text_eshop2.asm` | `ESHOP2` locale text segment |
| `C9:1C3A..C9:3853` | `src/c9/text_eevent3.asm` | `EEVENT3` locale text segment |
| `C9:3853..C9:53BF` | `src/c9/text_e02twsn2.asm` | `E02TWSN2` locale text segment |
| `C9:53BF..C9:6D10` | `src/c9/text_e02twsn1.asm` | `E02TWSN1` locale text segment |
| `C9:6D10..C9:7B6B` | `src/c9/text_e19moon.asm` | `E19MOON` locale text segment |
| `C9:7B6B..C9:7FB3` | `src/c9/text_egoods0.asm` | `EGOODS0` locale text segment |
| `C9:7FB3..C9:8000` | `src/c9/text_bank_c9_gap_1_alignmentgap.asm` | bank-segment alignment gap |
| `C9:8000..C9:992F` | `src/c9/text_e03happy.asm` | `E03HAPPY` locale text segment |
| `C9:992F..C9:B226` | `src/c9/text_unknown_c9992f.asm` | `UNKNOWN_C9992F` locale text segment |
| `C9:B226..C9:C991` | `src/c9/text_eevent5.asm` | `EEVENT5` locale text segment |
| `C9:C991..C9:D6F8` | `src/c9/text_e12rama.asm` | `E12RAMA` locale text segment |
| `C9:D6F8..C9:E37E` | `src/c9/text_e15gumi.asm` | `E15GUMI` locale text segment |
| `C9:E37E..C9:EE2F` | `src/c9/text_e14makyo.asm` | `E14MAKYO` locale text segment |
| `C9:EE2F..C9:F897` | `src/c9/text_ebattle7.asm` | `EBATTLE7` locale text segment |
| `C9:F897..C9:FF2F` | `src/c9/text_egoods1.asm` | `EGOODS1` locale text segment |
| `C9:FF2F..C9:10000` | `src/c9/text_bank_c9_gap_2_tailpadding.asm` | bank-end padding |

## Remaining Semantic Work

C9 is the cleanest text-bank regression case in this group: the current text
decoder reports zero parser unknowns. The one naming follow-up is
`UNKNOWN_C9992F`, which appears structurally text/door/event-heavy and should
be renamed from script context rather than bank geometry alone.

