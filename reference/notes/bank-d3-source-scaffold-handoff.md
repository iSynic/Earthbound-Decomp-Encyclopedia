# Bank D3 Source Scaffold Handoff

## Status

Bank `D3` is byte-complete for the current source-scaffold phase.

- durable scaffold: `src/d3/bank_d3_helpers_asar.asm`
- manifest: `build/d3-build-candidate-ranges.json`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `339`
- source bytes: `0`
- preserved data-gap bytes: `65536`
- byte-equivalence: `OK`, `0` mismatches

D3 is protected as exact overworld sprite graphics payload corridors.

## Regenerate And Validate

Use these commands from the repository root:

```powershell
python tools\promote_asset_bank_to_source_scaffold.py D3
python tools\build_source_bank_scaffold.py --bank D3
python tools\validate_source_bank_byte_equivalence.py --bank D3 --module all --combined --scaffold src\d3\bank_d3_helpers_asar.asm --strict
python tools\build_source_bank_candidate_ranges_doc.py --bank D3
python tools\build_source_bank_residual_map.py --bank D3
```

Expected validation:

- `D3 byte-equivalence: OK, 339 module(s), 0 mismatch(es).`
- `notes/d3-source-residual-map.md` reports `0` residual bytes and `0` residual ranges.

## Remaining Semantic Work

- optional render fixtures for the sprite graphics payloads
- consumer-side grouping against sprite-group metadata if a later graphics tool needs friendlier labels
