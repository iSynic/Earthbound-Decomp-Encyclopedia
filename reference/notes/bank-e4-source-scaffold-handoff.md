# Bank E4 Source Scaffold Handoff

## Status

Bank `E4` is byte-complete for the current source-scaffold phase.

- durable scaffold: `src/e4/bank_e4_helpers_asar.asm`
- manifest: `build/e4-build-candidate-ranges.json`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `6`
- source bytes: `0`
- preserved data-gap bytes: `65536`
- byte-equivalence: `OK`, `0` mismatches

E4 is protected as exact audio-pack/data payload corridors plus any explicit padding or inline table corridors from the asset manifest.

## Regenerate And Validate

Use these commands from the repository root:

```powershell
python tools\promote_asset_bank_to_source_scaffold.py E4
python tools\build_source_bank_scaffold.py --bank E4
python tools\validate_source_bank_byte_equivalence.py --bank E4 --module all --combined --scaffold src\e4\bank_e4_helpers_asar.asm --strict
python tools\build_source_bank_candidate_ranges_doc.py --bank E4
python tools\build_source_bank_residual_map.py --bank E4
```

Expected validation:

- `E4 byte-equivalence: OK, 6 module(s), 0 mismatch(es).`
- `notes/e4-source-residual-map.md` reports `0` residual bytes and `0` residual ranges.

## Remaining Semantic Work

- leave audio packs opaque unless audio-pack decoding becomes a separate target
- optional audio-pack inventory/render fixtures for playback or extraction tooling
