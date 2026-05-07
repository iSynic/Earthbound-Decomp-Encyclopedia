# Bank C5 Source Scaffold Handoff

## Status

Bank `C5` is byte-complete for the current source-scaffold phase.

- durable scaffold: `src/c5/bank_c5_helpers_asar.asm`
- manifest: `build/c5-build-candidate-ranges.json`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `9`
- source bytes: `0`
- preserved data-gap bytes: `65536`
- byte-equivalence: `OK`, `0` mismatches

This scaffold deliberately treats C5 as a text/data bank, not as source code.
The claim is byte protection and reproducible packaging: every byte is now
represented by a checked-in scaffold input and can be regenerated and validated
against the original ROM.

## Regenerate And Validate

Use these commands from the repository root:

```powershell
python tools\build_text_bank_manifest.py C5 --json-out build\text-bank-c5.json --markdown-out notes\bank-c5-text-data-map.md
python tools\promote_text_bank_to_source_scaffold.py C5
python tools\build_source_bank_scaffold.py --bank C5
python tools\validate_source_bank_byte_equivalence.py --bank C5 --module all --combined --scaffold src\c5\bank_c5_helpers_asar.asm --strict
python tools\build_source_bank_candidate_ranges_doc.py --bank C5
python tools\build_source_bank_residual_map.py --bank C5
```

Expected validation:

- `C5 byte-equivalence: OK, 9 module(s), 0 mismatch(es).`
- `notes/c5-source-residual-map.md` reports `0` residual bytes and `0`
  residual ranges.

## Reference-Led Closure

C5 was promoted from the text-bank manifest, which combines:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank05.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/text-bank-c5.json`
- `notes/bank-c5-text-data-map.md`

The durable scaffold covers the seven locale text segments plus the two small
non-locale gaps:

| Range | Stub | Purpose |
| --- | --- | --- |
| `C5:0000..C5:3711` | `src/c5/text_eshop0.asm` | `ESHOP0` locale text segment |
| `C5:3711..C5:6DF3` | `src/c5/text_eexplgds.asm` | `EEXPLGDS` locale text segment |
| `C5:6DF3..C5:7E1C` | `src/c5/text_e13skrb.asm` | `E13SKRB` locale text segment |
| `C5:7E1C..C5:7FC1` | `src/c5/text_e17past.asm` | `E17PAST` locale text segment |
| `C5:7FC1..C5:8000` | `src/c5/text_bank_c5_gap_1_alignmentgap.asm` | bank-segment alignment gap |
| `C5:8000..C5:B3BA` | `src/c5/text_edebug.asm` | `EDEBUG` text/debug script segment |
| `C5:B3BA..C5:E5BC` | `src/c5/text_eshop1.asm` | `ESHOP1` locale text segment |
| `C5:E5BC..C5:FFEC` | `src/c5/text_eevent0.asm` | `EEVENT0` locale text segment |
| `C5:FFEC..C5:10000` | `src/c5/text_bank_c5_gap_2_tailpadding.asm` | zero-filled bank-end padding |

## Remaining Semantic Work

The remaining C5 work is text VM and asset semantics, not bank closure:

- keep C5 as a regression fixture for the text-command decoder
- inspect the two remaining EDEBUG unknown parser hits before promoting command
  semantics
- eventually emit the locale text segments as richer text-script assets rather
  than raw byte corridors
- apply the same promotion flow to C6-C9, then compare command coverage across
  all text banks

