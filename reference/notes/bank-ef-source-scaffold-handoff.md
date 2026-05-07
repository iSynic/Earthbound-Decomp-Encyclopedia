# Bank EF Source Scaffold Handoff

## Status

Bank `EF` is byte-complete for the current source-scaffold phase.

- durable scaffold: `src/ef/bank_ef_helpers_asar.asm`
- manifest: `build/ef-build-candidate-ranges.json`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `5`
- source bytes: `65536`
- preserved data-gap bytes: `0`
- byte-equivalence: `OK`, `0` mismatches

EF is source-backed as coarse exact corridors for the mixed save/map/text/debug bank: one large inferred front/middle source-order span, debug font assets, a small debug palette/unknown span, debug cursor graphics, and the named late tail. These are explicit `db` source blocks, not decoded 65816 routines.

## Regenerate And Validate

Use these commands from the repository root:

```powershell
python tools\promote_asset_bank_to_source_scaffold.py EF
python tools\build_source_bank_scaffold.py --bank EF
python tools\validate_source_bank_byte_equivalence.py --bank EF --module all --combined --scaffold src\ef\bank_ef_helpers_asar.asm --strict
python tools\build_source_bank_candidate_ranges_doc.py --bank EF
python tools\build_source_bank_residual_map.py --bank EF
```

Expected validation:

- `EF byte-equivalence: OK, 5 module(s), 0 mismatch(es).`
- `notes/ef-source-residual-map.md` reports `0` residual bytes and `0` residual ranges.

## Remaining Semantic Work

- split the coarse EF:0000..EF:EB5F span into save/SRAM helpers, map tileset/sprite grouping tables, Sound Stone data, text runs, glyph tables, and debug routines
- split EF:F0D7..EF:10000 into the named late tail includes from bank2F.asm
- promote true EF source helpers separately where consumers prove they are executable code instead of opaque asset/data corridors
- decode EF text-script families using D5/C1 consumers
