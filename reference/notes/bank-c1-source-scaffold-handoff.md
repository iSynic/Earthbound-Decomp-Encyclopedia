# Bank C1 Source Scaffold Handoff

## Status

Bank `C1` is byte-complete for the current source-scaffold phase.

- durable scaffold: `src/c1/bank_c1_helpers_asar.asm`
- manifest: `build/c1-build-candidate-ranges.json`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `172`
- source bytes: `65536`
- preserved data-gap bytes: `0`
- byte-equivalence: `OK`, `0` mismatches

C1 is structurally closed as a working-name anchored source scaffold, and it is now source-complete for this phase. All C1 byte ranges assemble from checked-in source. The terminal checksum constant/padding bytes at `C1:FFEF..10000` are modeled explicitly as data inside the mixed bank-end module rather than as a preserved manifest gap.

Current notable byte-preserved targets:

- No remaining preserved C1 data gaps.
- `C1:FFEF..10000` terminal bank-end constant/padding is now explicit source data under `src/c1/c1_ff99_compute_centered_text_layout_metric.asm`.
- No remaining C1 code corridors are byte-preserved in the current source-bank manifest.

## Regenerate And Validate

Use these commands from the repository root:

```powershell
# Do not re-run promote_working_names_to_source_scaffold.py here: it overwrites
# build/c1-build-candidate-ranges.json and the per-range stubs, discarding
# in-progress source promotion decisions.
python tools\build_source_bank_scaffold.py --bank C1
python tools\validate_source_bank_byte_equivalence.py --bank C1 --module all --combined --scaffold src\c1\bank_c1_helpers_asar.asm --strict
python tools\build_source_bank_candidate_ranges_doc.py --bank C1
python tools\build_source_bank_residual_map.py --bank C1
```

Expected validation:

- `C1 byte-equivalence: OK, 172 module(s), 0 mismatch(es).`
- `notes/c1-source-residual-map.md` reports `0` residual bytes and `0` residual ranges.

## Remaining Semantic Work

- Tighten cross-bank contracts with C2 battle runtime, C4 renderer/window helpers, D5 tables, and EF text/debug payloads.
- Keep byte-equivalence validation running after naming, label, or contract edits to source modules.
