# Bank DC Source Scaffold Handoff

## Status

Bank `DC` is byte-complete for the current source-scaffold phase.

- durable scaffold: `src/dc/bank_dc_helpers_asar.asm`
- manifest: `build/dc-build-candidate-ranges.json`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `11`
- source bytes: `0`
- preserved data-gap bytes: `65536`
- byte-equivalence: `OK`, `0` mismatches

DC is protected as exact map arrangement, per-sector music table, audio payload, and tail-padding corridors. The first per-sector music byte plane is now joined to the CF event-music context selector contract in `notes/cf-event-music-context-contracts.md`.

## Regenerate And Validate

Use these commands from the repository root:

```powershell
python tools\promote_asset_bank_to_source_scaffold.py DC
python tools\build_source_bank_scaffold.py --bank DC
python tools\validate_source_bank_byte_equivalence.py --bank DC --module all --combined --scaffold src\dc\bank_dc_helpers_asar.asm --strict
python tools\build_source_bank_candidate_ranges_doc.py --bank DC
python tools\build_source_bank_residual_map.py --bank DC
```

Expected validation:

- `DC byte-equivalence: OK, 11 module(s), 0 mismatch(es).`
- `notes/dc-source-residual-map.md` reports `0` residual bytes and `0` residual ranges.

## Remaining Semantic Work

- keep the CF/DC current-position music selector contract regression-tested
- name the second per-sector music byte plane only if a consumer/tool join supports it
- optional arrangement/music cross-reference fixtures
- leave audio packs opaque unless audio-pack decoding becomes a separate target
