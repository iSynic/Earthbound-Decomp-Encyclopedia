# Bank EA Source Scaffold Handoff

## Status

Bank `EA` is byte-complete for the current source-scaffold phase.

- durable scaffold: `src/ea/bank_ea_helpers_asar.asm`
- manifest: `build/ea-build-candidate-ranges.json`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `8`
- source bytes: `0`
- preserved data-gap bytes: `65536`
- byte-equivalence: `OK`, `0` mismatches

EA is protected as exact audio-pack/data payload corridors plus any explicit padding or inline table corridors from the asset manifest.

## Regenerate And Validate

Use these commands from the repository root:

```powershell
python tools\promote_asset_bank_to_source_scaffold.py EA
python tools\build_source_bank_scaffold.py --bank EA
python tools\validate_source_bank_byte_equivalence.py --bank EA --module all --combined --scaffold src\ea\bank_ea_helpers_asar.asm --strict
python tools\build_source_bank_candidate_ranges_doc.py --bank EA
python tools\build_source_bank_residual_map.py --bank EA
```

Expected validation:

- `EA byte-equivalence: OK, 8 module(s), 0 mismatch(es).`
- `notes/ea-source-residual-map.md` reports `0` residual bytes and `0` residual ranges.

## Remaining Semantic Work

- leave audio packs opaque unless audio-pack decoding becomes a separate target
- optional audio-pack inventory/render fixtures for playback or extraction tooling
