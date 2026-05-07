# Bank D9 Source Scaffold Handoff

## Status

Bank `D9` is byte-complete for the current source-scaffold phase.

- durable scaffold: `src/d9/bank_d9_helpers_asar.asm`
- manifest: `build/d9-build-candidate-ranges.json`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `7`
- source bytes: `0`
- preserved data-gap bytes: `65536`
- byte-equivalence: `OK`, `0` mismatches

D9 is protected as exact compressed map graphics/arrangement, audio payload, and tail-padding corridors.

## Regenerate And Validate

Use these commands from the repository root:

```powershell
python tools\promote_asset_bank_to_source_scaffold.py D9
python tools\build_source_bank_scaffold.py --bank D9
python tools\validate_source_bank_byte_equivalence.py --bank D9 --module all --combined --scaffold src\d9\bank_d9_helpers_asar.asm --strict
python tools\build_source_bank_candidate_ranges_doc.py --bank D9
python tools\build_source_bank_residual_map.py --bank D9
```

Expected validation:

- `D9 byte-equivalence: OK, 7 module(s), 0 mismatch(es).`
- `notes/d9-source-residual-map.md` reports `0` residual bytes and `0` residual ranges.

## Remaining Semantic Work

- optional decompression/render fixtures for map graphics and arrangements
- leave audio packs opaque unless audio-pack decoding becomes a separate target
