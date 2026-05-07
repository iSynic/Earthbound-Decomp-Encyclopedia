# Bank E6 Source Scaffold Handoff

## Status

Bank `E6` is byte-complete for the current source-scaffold phase.

- durable scaffold: `src/e6/bank_e6_helpers_asar.asm`
- manifest: `build/e6-build-candidate-ranges.json`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `14`
- source bytes: `0`
- preserved data-gap bytes: `65536`
- byte-equivalence: `OK`, `0` mismatches

E6 is protected as exact audio-pack/data payload corridors plus explicit inline table, SPC700 binary, and padding corridors from the asset manifest.

## Regenerate And Validate

Use these commands from the repository root:

```powershell
python tools\promote_asset_bank_to_source_scaffold.py E6
python tools\build_source_bank_scaffold.py --bank E6
python tools\validate_source_bank_byte_equivalence.py --bank E6 --module all --combined --scaffold src\e6\bank_e6_helpers_asar.asm --strict
python tools\build_source_bank_candidate_ranges_doc.py --bank E6
python tools\build_source_bank_residual_map.py --bank E6
```

Expected validation:

- `E6 byte-equivalence: OK, 14 module(s), 0 mismatch(es).`
- `notes/e6-source-residual-map.md` reports `0` residual bytes and `0` residual ranges.

## Remaining Semantic Work

- leave audio packs opaque unless audio-pack decoding becomes a separate target
- optional audio-pack inventory/render fixtures for playback or extraction tooling
