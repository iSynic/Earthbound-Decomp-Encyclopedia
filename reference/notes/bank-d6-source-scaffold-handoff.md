# Bank D6 Source Scaffold Handoff

## Status

Bank `D6` is byte-complete for the current source-scaffold phase.

- durable scaffold: `src/d6/bank_d6_helpers_asar.asm`
- manifest: `build/d6-build-candidate-ranges.json`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `6`
- source bytes: `0`
- preserved data-gap bytes: `65536`
- byte-equivalence: `OK`, `0` mismatches

D6 is protected as exact map tile graphics payload corridors.

## Regenerate And Validate

Use these commands from the repository root:

```powershell
python tools\promote_asset_bank_to_source_scaffold.py D6
python tools\build_source_bank_scaffold.py --bank D6
python tools\validate_source_bank_byte_equivalence.py --bank D6 --module all --combined --scaffold src\d6\bank_d6_helpers_asar.asm --strict
python tools\build_source_bank_candidate_ranges_doc.py --bank D6
python tools\build_source_bank_residual_map.py --bank D6
```

Expected validation:

- `D6 byte-equivalence: OK, 6 module(s), 0 mismatch(es).`
- `notes/d6-source-residual-map.md` reports `0` residual bytes and `0` residual ranges.

## Remaining Semantic Work

- optional decompression/render fixtures for the map tile graphics payloads
- cross-bank linkage to D7/DA/DB/DD/DE arrangement and palette banks when typed map assets are emitted
