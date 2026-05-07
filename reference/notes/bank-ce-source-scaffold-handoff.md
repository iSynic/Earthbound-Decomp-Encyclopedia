# Bank CE Source Scaffold Handoff

## Status

Bank `CE` is byte-complete for the current source-scaffold phase.

- durable scaffold: `src/ce/bank_ce_helpers_asar.asm`
- manifest: `build/ce-build-candidate-ranges.json`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `220`
- source bytes: `0`
- preserved data-gap bytes: `65536`
- byte-equivalence: `OK`, `0` mismatches

CE is protected as a mixed battle/swirls/Sound Stone asset-data bank: 216 binary
asset corridors, 3 table corridors, and one tail padding corridor.

## Regenerate And Validate

Use these commands from the repository root:

```powershell
python tools\build_asset_bank_manifest.py CE --json-out build\asset-bank-ce.json --markdown-out notes\bank-ce-asset-data-map.md
python tools\promote_asset_bank_to_source_scaffold.py CE
python tools\build_source_bank_scaffold.py --bank CE
python tools\validate_source_bank_byte_equivalence.py --bank CE --module all --combined --scaffold src\ce\bank_ce_helpers_asar.asm --strict
python tools\build_source_bank_candidate_ranges_doc.py --bank CE
python tools\build_source_bank_residual_map.py --bank CE
```

Expected validation:

- `CE byte-equivalence: OK, 220 module(s), 0 mismatch(es).`
- `notes/ce-source-residual-map.md` reports `0` residual bytes and `0`
  residual ranges.

## Protected Range Groups

| Group | Range | Bytes | Notes |
| --- | --- | ---: | --- |
| battle sprite graphics payloads | `CE:0000..CE:62EE` | `25326` | remaining 55 compressed battle sprite graphics |
| battle sprite pointer table | `CE:62EE..CE:6514` | `550` | 110 five-byte pointer/shape records |
| battle sprite palettes | `CE:6514..CE:6914` | `1024` | 32 SNES palettes |
| swirl data payloads | `CE:6914..CE:DC45` | `29489` | 126 swirl payloads |
| swirl pointer table | `CE:DC45..CE:DD41` | `252` | 126 local word pointers |
| swirl primary table | `CE:DD41..CE:DD5D` | `28` | inline bank-config table |
| Sound Stone graphics | `CE:DD5D..CE:F806` | `6825` | compressed locale graphics |
| Sound Stone palette | `CE:F806..CE:F8C6` | `192` | root-level palette payload |
| audio pack 102 | `CE:F8C6..CE:FFAA` | `1764` | US retail audio pack payload |
| tail padding | `CE:FFAA..CE:10000` | `86` | explicit bank-end slack |

## Remaining Semantic Work

CE is byte-complete, but useful typed work remains:

- emit `BATTLE_SPRITES_POINTERS` as five-byte pointer/shape records
- link CE sprite payloads and palettes to enemy/battle sprite IDs
- decode or at least row-name swirl payload families against transition users
- preserve the inline `SWIRL_PRIMARY_TABLE` as a named table, not anonymous gap
- optionally render battle sprites, swirls, and the Sound Stone graphic as visual
  regression fixtures

