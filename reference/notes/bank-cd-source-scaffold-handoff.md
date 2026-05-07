# Bank CD Source Scaffold Handoff

## Status

Bank `CD` is byte-complete for the current source-scaffold phase.

- durable scaffold: `src/cd/bank_cd_helpers_asar.asm`
- manifest: `build/cd-build-candidate-ranges.json`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `55`
- source bytes: `0`
- preserved data-gap bytes: `65536`
- byte-equivalence: `OK`, `0` mismatches

CD is protected as a pure battle-sprite graphics payload bank. The `55`
compressed sprite assets fill the entire bank with no tables and no slack.

## Regenerate And Validate

Use these commands from the repository root:

```powershell
python tools\build_asset_bank_manifest.py CD --json-out build\asset-bank-cd.json --markdown-out notes\bank-cd-asset-data-map.md
python tools\promote_asset_bank_to_source_scaffold.py CD
python tools\build_source_bank_scaffold.py --bank CD
python tools\validate_source_bank_byte_equivalence.py --bank CD --module all --combined --scaffold src\cd\bank_cd_helpers_asar.asm --strict
python tools\build_source_bank_candidate_ranges_doc.py --bank CD
python tools\build_source_bank_residual_map.py --bank CD
```

Expected validation:

- `CD byte-equivalence: OK, 55 module(s), 0 mismatch(es).`
- `notes/cd-source-residual-map.md` reports `0` residual bytes and `0`
  residual ranges.

## Protected Range Groups

| Group | Range | Bytes | Notes |
| --- | --- | ---: | --- |
| battle sprite graphics payloads | `CD:0000..CD:10000` | `65536` | 55 compressed `.gfx.lzhal` assets |

## Remaining Semantic Work

CD has no bank-local table semantics to decode. Useful follow-up work belongs
to the consumer side:

- link each sprite payload to `BATTLE_SPRITES_POINTERS` entries
- preserve US locale-resolved sprite payloads `BATTLE_SPRITE_62` and
  `BATTLE_SPRITE_23`
- optionally decompress/render sampled sprites as visual regression fixtures

