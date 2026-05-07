# Bank EC Source Scaffold Handoff

## Status

Bank `EC` is byte-complete for the current source-scaffold phase.

- durable scaffold: `src/ec/bank_ec_helpers_asar.asm`
- manifest: `build/ec-build-candidate-ranges.json`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `15`
- source bytes: `0`
- preserved data-gap bytes: `65536`
- byte-equivalence: `OK`, `0` mismatches

EC is protected as exact audio-pack/data payload corridors plus any explicit padding or inline table corridors from the asset manifest.

## Regenerate And Validate

Use these commands from the repository root:

```powershell
python tools\promote_asset_bank_to_source_scaffold.py EC
python tools\build_source_bank_scaffold.py --bank EC
python tools\validate_source_bank_byte_equivalence.py --bank EC --module all --combined --scaffold src\ec\bank_ec_helpers_asar.asm --strict
python tools\build_source_bank_candidate_ranges_doc.py --bank EC
python tools\build_source_bank_residual_map.py --bank EC
```

Expected validation:

- `EC byte-equivalence: OK, 15 module(s), 0 mismatch(es).`
- `notes/ec-source-residual-map.md` reports `0` residual bytes and `0` residual ranges.

## Remaining Semantic Work

- leave audio packs opaque unless audio-pack decoding becomes a separate target
- optional audio-pack inventory/render fixtures for playback or extraction tooling
