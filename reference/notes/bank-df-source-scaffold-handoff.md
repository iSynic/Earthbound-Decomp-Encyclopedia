# Bank DF Source Scaffold Handoff

## Status

Bank `DF` is byte-complete for the current source-scaffold phase.

- durable scaffold: `src/df/bank_df_helpers_asar.asm`
- manifest: `build/df-build-candidate-ranges.json`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `24`
- source bytes: `0`
- preserved data-gap bytes: `65536`
- byte-equivalence: `OK`, `0` mismatches

DF is protected as exact map graphics, palette animation/table, audio payload, and tail-padding corridors.

## Regenerate And Validate

Use these commands from the repository root:

```powershell
python tools\promote_asset_bank_to_source_scaffold.py DF
python tools\build_source_bank_scaffold.py --bank DF
python tools\validate_source_bank_byte_equivalence.py --bank DF --module all --combined --scaffold src\df\bank_df_helpers_asar.asm --strict
python tools\build_source_bank_candidate_ranges_doc.py --bank DF
python tools\build_source_bank_residual_map.py --bank DF
```

Expected validation:

- `DF byte-equivalence: OK, 24 module(s), 0 mismatch(es).`
- `notes/df-source-residual-map.md` reports `0` residual bytes and `0` residual ranges.

## Remaining Semantic Work

- promote the palette-animation table family into richer typed contracts
- optional map graphics/palette animation render fixtures
- leave audio packs opaque unless audio-pack decoding becomes a separate target
