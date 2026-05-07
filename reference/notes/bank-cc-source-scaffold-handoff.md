# Bank CC Source Scaffold Handoff

## Status

Bank `CC` is byte-complete for the current source-scaffold phase.

- durable scaffold: `src/cc/bank_cc_helpers_asar.asm`
- manifest: `build/cc-build-candidate-ranges.json`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `83`
- source bytes: `0`
- preserved data-gap bytes: `65536`
- byte-equivalence: `OK`, `0` mismatches

CC is protected as an animation/PSI asset bank: 79 binary asset corridors, 3
generated table corridors, and one tail padding corridor.

## Regenerate And Validate

Use these commands from the repository root:

```powershell
python tools\build_asset_bank_manifest.py CC --json-out build\asset-bank-cc.json --markdown-out notes\bank-cc-asset-data-map.md
python tools\promote_asset_bank_to_source_scaffold.py CC
python tools\build_source_bank_scaffold.py --bank CC
python tools\validate_source_bank_byte_equivalence.py --bank CC --module all --combined --scaffold src\cc\bank_cc_helpers_asar.asm --strict
python tools\build_source_bank_candidate_ranges_doc.py --bank CC
python tools\build_source_bank_residual_map.py --bank CC
```

Expected validation:

- `CC byte-equivalence: OK, 83 module(s), 0 mismatch(es).`
- `notes/cc-source-residual-map.md` reports `0` residual bytes and `0`
  residual ranges.

## Protected Range Groups

| Group | Range | Bytes | Notes |
| --- | --- | ---: | --- |
| compressed animation payloads | `CC:0000..CC:2DE1` | `11745` | six animation payloads |
| animation sequence pointer table | `CC:2DE1..CC:2E19` | `56` | retail table branch |
| PSI arrangements/graphics | `CC:2E19..CC:F04D` | `49716` | compressed PSI arrangement and graphics payloads |
| PSI animation config table | `CC:F04D..CC:F1E5` | `408` | inferred generated table span |
| PSI palettes | `CC:F1E5..CC:F58F` | `938` | remaining arrangements plus 34 eight-byte palettes |
| PSI animation pointer table | `CC:F58F..CC:F617` | `136` | inferred generated table span |
| audio pack 71 | `CC:F617..CC:FFDB` | `2500` | US retail audio pack payload |
| tail padding | `CC:FFDB..CC:10000` | `37` | explicit bank-end slack |

## Remaining Semantic Work

CC is byte-complete, but the useful next work is typed asset/table emission:

- field-name `data/psi_anim_cfg.asm` from `show_psi_animation.asm` consumers
- row-name `data/psi_anim_pointers.asm` against PSI animation IDs
- preserve the US retail conditional branch behavior in any future source
  emitter
- optionally render/decompress sampled animation and PSI payloads as visual
  regression fixtures

