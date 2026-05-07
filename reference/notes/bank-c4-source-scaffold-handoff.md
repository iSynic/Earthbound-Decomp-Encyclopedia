# Bank C4 Source Scaffold Handoff

## Status

Bank `C4` is byte-complete for the current source-scaffold phase.

- durable scaffold: `src/c4/bank_c4_helpers_asar.asm`
- manifest: `build/c4-build-candidate-ranges.json`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `142`
- source bytes: `65536`
- preserved data-gap bytes: `0`
- byte-equivalence: `OK`, `0` mismatches

The source scaffold is not claiming final semantic names for every helper or
asset. It is claiming that every byte in bank `C4` is now represented by a
checked-in scaffold input and can be regenerated and validated byte-for-byte
against the original ROM.

## Regenerate And Validate

Use these commands from the repository root:

```powershell
python tools\build_source_bank_scaffold.py --bank C4
python tools\validate_source_bank_byte_equivalence.py --bank C4 --module all --combined --scaffold src\c4\bank_c4_helpers_asar.asm --strict
python tools\build_source_bank_candidate_ranges_doc.py --bank C4
python tools\build_ebsrc_bank_map.py --bank C4
python tools\build_source_bank_residual_map.py --bank C4
python tools\build_working_name_manifest.py --banks C0 C1 C2 C3 C4 --output build\working-names-c0-c4.json
python tools\validate_data_contracts.py
```

Expected validation:

- `C4 byte-equivalence: OK, 142 module(s), 0 mismatch(es).`
- `notes/c4-source-residual-map.md` reports `0` residual bytes and `0`
  residual ranges.
- data contracts remain `OK`.

## Reference-Led Closure

The final closure pass leaned on existing references instead of hand-decoding
every residual byte. The most useful references were:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank04.asm`
- `notes/ebsrc-bank-c4-map.md`
- `refs/earthbound-disasm-legacy/Earthbound Decomp/EB/Routine_Macros_EB.asm`
- ebsrc event fragments under `refs/ebsrc-main/ebsrc-main/src/data/events/`

The last residual ranges were promoted as explicit source data blocks:

| Range | Stub | Purpose |
| --- | --- | --- |
| `C4:00D4..C4:0B51` | `src/c4/event_script_pointer_table.asm` | event script pointer table |
| `C4:0BD4..C4:1DB6` | `src/c4/early_event_overlay_data_payloads.asm` | early event, overlay, and map-adjacent payloads |
| `C4:2172..C4:23DC` | `src/c4/event_script_payloads_2172_23dc.asm` | event script payloads and adjacent fragments |
| `C4:279F..C4:283F` | `src/c4/event_script_payloads_279f_283f.asm` | event script payloads and adjacent fragments |
| `C4:2A1F..C4:30EC` | `src/c4/entity_footprint_visual_profile_tables.asm` | entity footprint and visual profile tables |
| `C4:FD4B..C4:10000` | `src/c4/bank_end_padding.asm` | zero-filled bank-end padding |

## Source/Data Boundary

C4 is now fully source-backed. The scaffold still distinguishes decoded
executable helpers from explicit `db` assets/tables:

- checked-in scaffold source: `65536` bytes
- preserved manifest data gaps: `0` bytes

The explicit data source includes text fragments, event scripts, pointer
tables, visual/entity profile tables, Sound Stone and music tables, file-select
text, Lumine Hall/Event 353 text payloads, and bank-end padding. These are
valid source-scaffold inputs, but many are still intentionally coarse asset
stubs.

## Remaining Semantic Work

The remaining C4 work is no longer byte closure. It is semantic asset polish:

- split coarse data stubs into richer typed manifests where useful
- decode event/actionscript payloads as portable script assets
- attach stable names to table rows and fields when consumers prove them
- promote only the names that are strong enough for upstream-facing source
- keep byte-equivalence as the backstop after every refinement

Good next C4-specific targets, if revisiting C4, are:

1. event script pointer table structure at `C4:00D4..C4:0B51`
2. event script payload islands at `C4:2172..C4:23DC` and `C4:279F..C4:283F`
3. entity footprint and visual profile tables at `C4:2A1F..C4:30EC`
4. early event/overlay data payloads at `C4:0BD4..C4:1DB6`

For bank-wide progress, C4 is now a stable reference point: new tools or source
pipeline changes should continue to validate this bank cleanly.
