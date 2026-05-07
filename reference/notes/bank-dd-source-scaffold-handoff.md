# Bank DD Source Scaffold Handoff

## Status

Bank `DD` is byte-complete for the current source-scaffold phase.

- durable scaffold: `src/dd/bank_dd_helpers_asar.asm`
- manifest: `build/dd-build-candidate-ranges.json`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `8`
- source bytes: `0`
- preserved data-gap bytes: `65536`
- byte-equivalence: `OK`, `0` mismatches

DD is protected as exact compressed map graphics/arrangement, audio payload, and tail-padding corridors.

## Regenerate And Validate

Use these commands from the repository root:

```powershell
python tools\promote_asset_bank_to_source_scaffold.py DD
python tools\build_source_bank_scaffold.py --bank DD
python tools\validate_source_bank_byte_equivalence.py --bank DD --module all --combined --scaffold src\dd\bank_dd_helpers_asar.asm --strict
python tools\build_source_bank_candidate_ranges_doc.py --bank DD
python tools\build_source_bank_residual_map.py --bank DD
```

Expected validation:

- `DD byte-equivalence: OK, 8 module(s), 0 mismatch(es).`
- `notes/dd-source-residual-map.md` reports `0` residual bytes and `0` residual ranges.

## Remaining Semantic Work

- optional decompression/render fixtures for map graphics and arrangements
- leave audio packs opaque unless audio-pack decoding becomes a separate target
