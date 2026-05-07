# Bank D7 Source Scaffold Handoff

## Status

Bank `D7` is byte-complete for the current source-scaffold phase.

- durable scaffold: `src/d7/bank_d7_helpers_asar.asm`
- manifest: `build/d7-build-candidate-ranges.json`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `7`
- source bytes: `0`
- preserved data-gap bytes: `65536`
- byte-equivalence: `OK`, `0` mismatches

D7 is protected as exact map tile chunk, generated palette/sector-attribute table, arrangement asset, audio payload, and tail-padding corridors.

## Regenerate And Validate

Use these commands from the repository root:

```powershell
python tools\promote_asset_bank_to_source_scaffold.py D7
python tools\build_source_bank_scaffold.py --bank D7
python tools\validate_source_bank_byte_equivalence.py --bank D7 --module all --combined --scaffold src\d7\bank_d7_helpers_asar.asm --strict
python tools\build_source_bank_candidate_ranges_doc.py --bank D7
python tools\build_source_bank_residual_map.py --bank D7
```

Expected validation:

- `D7 byte-equivalence: OK, 7 module(s), 0 mismatch(es).`
- `notes/d7-source-residual-map.md` reports `0` residual bytes and `0` residual ranges.

## Remaining Semantic Work

- promote palette and sector-attribute rows into richer typed contracts
- link map tile chunks to arrangement/palette consumers for render fixtures
- leave audio packs opaque unless audio-pack decoding becomes a separate target
