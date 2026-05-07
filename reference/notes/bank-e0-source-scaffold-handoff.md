# Bank E0 Source Scaffold Handoff

## Status

Bank `E0` is byte-complete for the current source-scaffold phase.

- durable scaffold: `src/e0/bank_e0_helpers_asar.asm`
- manifest: `build/e0-build-candidate-ranges.json`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `16`
- source bytes: `0`
- preserved data-gap bytes: `65536`
- byte-equivalence: `OK`, `0` mismatches

E0 is protected as exact UI/font/town-map/audio payload corridors, including
the inferred `COMPRESSED_SRAM` span and generated text-window/town-map table
span. Their semantic contracts now live in `notes/sram-template-contracts.md`
and `notes/text-window-skin-bundle-contracts.md`.

## Regenerate And Validate

Use these commands from the repository root:

```powershell
python tools\promote_asset_bank_to_source_scaffold.py E0
python tools\build_source_bank_scaffold.py --bank E0
python tools\validate_source_bank_byte_equivalence.py --bank E0 --module all --combined --scaffold src\e0\bank_e0_helpers_asar.asm --strict
python tools\build_source_bank_candidate_ranges_doc.py --bank E0
python tools\build_source_bank_residual_map.py --bank E0
```

Expected validation:

- `E0 byte-equivalence: OK, 16 module(s), 0 mismatch(es).`
- `notes/e0-source-residual-map.md` reports `0` residual bytes and `0` residual ranges.

## Remaining Semantic Work

- preserve the missing-yml `mystery_sram.bin.lzhal` provenance note if asset-level extraction needs a named source file
- use the existing SRAM save-template and text-window/town-map table contracts for source emission
- optionally name reserve SRAM template block provenance and remaining palette-row presentation roles when stronger caller evidence appears
- optional render fixtures for text-window graphics, fonts, and town maps
- leave audio packs opaque unless audio-pack decoding becomes a separate target
