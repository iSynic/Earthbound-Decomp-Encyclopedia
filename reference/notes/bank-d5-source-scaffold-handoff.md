# Bank D5 Source Scaffold Handoff

## Status

Bank `D5` is byte-complete for the current source-scaffold phase.

- durable scaffold: `src/d5/bank_d5_helpers_asar.asm`
- manifest: `build/d5-build-candidate-ranges.json`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `139`
- source bytes: `0`
- preserved data-gap bytes: `65536`
- byte-equivalence: `OK`, `0` mismatches

D5 is protected as the final overworld sprite graphics tail, an explicit
zero-filled pad, exact gameplay/battle/map table splits, and bank-end zero
padding.

## Regenerate And Validate

Use these commands from the repository root:

```powershell
python tools\build_asset_bank_manifest.py D5 --json-out build\asset-bank-d5.json --markdown-out notes\bank-d5-asset-data-map.md
python tools\build_d5_table_splits.py
python tools\promote_mixed_asset_table_bank_to_source_scaffold.py D5
python tools\build_source_bank_scaffold.py --bank D5
python tools\validate_source_bank_byte_equivalence.py --bank D5 --module all --combined --scaffold src\d5\bank_d5_helpers_asar.asm --strict
python tools\build_source_bank_candidate_ranges_doc.py --bank D5
python tools\build_source_bank_residual_map.py --bank D5
```

Expected validation:

- `D5 byte-equivalence: OK, 139 module(s), 0 mismatch(es).`
- `notes/d5-source-residual-map.md` reports `0` residual bytes and `0`
  residual ranges.

## Protected Range Groups

| Group | Range | Bytes | Notes |
| --- | --- | ---: | --- |
| overworld sprite graphics tail | `D5:0000..D5:45C0` | `17856` | 118 raw sprite graphics payloads, `SPRITE_1028` through `SPRITE_1145` |
| explicit zero pad | `D5:45C0..D5:5000` | `2624` | US retail `.REPEAT` pad from bank config |
| item/store/teleport/contact tables | `D5:5000..D5:7B68` | `11112` | corrected `ITEM_CONFIGURATION_TABLE` has 254 rows |
| battle/PSI/EXP/enemy/stat tables | `D5:7B68..D5:EBAA` | `28739` | battle action, PSI, enemy, growth, and condiment tables |
| map/timed/naming/initial tables | `D5:EBAA..D5:F711` | `2919` | teleport destinations, hotspots, timed item/delivery, default names, initial stats |
| tail padding | `D5:F711..D5:10000` | `2287` | zero-filled bank-end tail |

## Remaining Semantic Work

D5 is byte-complete, but useful semantic work remains:

- promote the exact split rows into richer typed data contracts where callers
  need field-level meaning
- keep the corrected 254-row item table count visible in all downstream tools
- decode `TIMED_DELIVERY_TABLE` subfields against the C3/C4 timed-delivery
  scripts before treating those rows as semantically final
- optionally render the `SPRITE_1028..SPRITE_1145` graphics payloads as fixtures
