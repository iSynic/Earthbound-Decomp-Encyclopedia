# Bank DA Source Scaffold Handoff

## Status

Bank `DA` is byte-complete for the current source-scaffold phase.

- durable scaffold: `src/da/bank_da_helpers_asar.asm`
- manifest: `build/da-build-candidate-ranges.json`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `38`
- source bytes: `0`
- preserved data-gap bytes: `65536`
- byte-equivalence: `OK`, `0` mismatches

DA is protected as exact compressed map arrangement, palette table, audio payload, and tail-padding corridors.

## Regenerate And Validate

Use these commands from the repository root:

```powershell
python tools\promote_asset_bank_to_source_scaffold.py DA
python tools\build_source_bank_scaffold.py --bank DA
python tools\validate_source_bank_byte_equivalence.py --bank DA --module all --combined --scaffold src\da\bank_da_helpers_asar.asm --strict
python tools\build_source_bank_candidate_ranges_doc.py --bank DA
python tools\build_source_bank_residual_map.py --bank DA
```

Expected validation:

- `DA byte-equivalence: OK, 38 module(s), 0 mismatch(es).`
- `notes/da-source-residual-map.md` reports `0` residual bytes and `0` residual ranges.

## Remaining Semantic Work

- promote the palette pointer/table span into a richer typed contract
- optional map arrangement/palette render fixtures
- leave audio packs opaque unless audio-pack decoding becomes a separate target
