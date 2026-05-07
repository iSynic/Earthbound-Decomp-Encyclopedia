# Bank D2 Source Scaffold Handoff

## Status

Bank `D2` is byte-complete for the current source-scaffold phase.

- durable scaffold: `src/d2/bank_d2_helpers_asar.asm`
- manifest: `build/d2-build-candidate-ranges.json`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `231`
- source bytes: `0`
- preserved data-gap bytes: `65536`
- byte-equivalence: `OK`, `0` mismatches

D2 is protected as exact overworld sprite graphics payload corridors.

## Regenerate And Validate

Use these commands from the repository root:

```powershell
python tools\promote_asset_bank_to_source_scaffold.py D2
python tools\build_source_bank_scaffold.py --bank D2
python tools\validate_source_bank_byte_equivalence.py --bank D2 --module all --combined --scaffold src\d2\bank_d2_helpers_asar.asm --strict
python tools\build_source_bank_candidate_ranges_doc.py --bank D2
python tools\build_source_bank_residual_map.py --bank D2
```

Expected validation:

- `D2 byte-equivalence: OK, 231 module(s), 0 mismatch(es).`
- `notes/d2-source-residual-map.md` reports `0` residual bytes and `0` residual ranges.

## Remaining Semantic Work

- optional render fixtures for the sprite graphics payloads
- consumer-side grouping against sprite-group metadata if a later graphics tool needs friendlier labels
