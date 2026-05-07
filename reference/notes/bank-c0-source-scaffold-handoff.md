# Bank C0 Source Scaffold Handoff

## Status

Bank `C0` is byte-complete for the current source-scaffold phase.

- durable scaffold: `src/c0/bank_c0_helpers_asar.asm`
- manifest: `build/c0-build-candidate-ranges.json`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `504`
- source bytes: `0`
- preserved data-gap bytes: `65536`
- byte-equivalence: `OK`, `0` mismatches

C0 is structurally closed as a working-name anchored source scaffold. The current modules preserve each interval between known C0 working-name anchors as exact ROM bytes, giving us a byte-equivalent replacement surface for the overworld/runtime bank without claiming those corridors are semantically decoded source yet.

## Regenerate And Validate

Use these commands from the repository root:

```powershell
python tools\promote_working_names_to_source_scaffold.py --bank C0 --force
# run the bank-specific promoter for C0
python tools\build_source_bank_scaffold.py --bank C0
python tools\validate_source_bank_byte_equivalence.py --bank C0 --module all --combined --scaffold src\c0\bank_c0_helpers_asar.asm --strict
python tools\build_source_bank_candidate_ranges_doc.py --bank C0
python tools\build_source_bank_residual_map.py --bank C0
```

Expected validation:

- `C0 byte-equivalence: OK, 504 module(s), 0 mismatch(es).`
- `notes/c0-source-residual-map.md` reports `0` residual bytes and `0` residual ranges.

## Remaining Semantic Work

- Replace byte corridors with decoded source modules subsystem by subsystem, starting with the existing movement, entity, collision, teleport, presentation, and task notes.
- Promote high-confidence working names into stable labels and add typed WRAM/ROM contracts at call boundaries.
- Keep byte-equivalence validation running after each corridor is converted from preserved bytes into real source.
