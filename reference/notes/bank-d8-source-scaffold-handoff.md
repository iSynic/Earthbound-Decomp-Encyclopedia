# Bank D8 Source Scaffold Handoff

## Status

Bank `D8` is byte-complete for the current source-scaffold phase.

- durable scaffold: `src/d8/bank_d8_helpers_asar.asm`
- manifest: `build/d8-build-candidate-ranges.json`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `28`
- source bytes: `0`
- preserved data-gap bytes: `65536`
- byte-equivalence: `OK`, `0` mismatches

D8 is protected as exact generated tile-collision data/pointer splits plus the
warning-screen asset tail, one audio pack payload, and a 23-byte tail padding
corridor.

## Regenerate And Validate

Use these commands from the repository root:

```powershell
python tools\build_d8_table_splits.py
python tools\promote_table_splits_to_source_scaffold.py D8
python tools\build_source_bank_scaffold.py --bank D8
python tools\validate_source_bank_byte_equivalence.py --bank D8 --module all --combined --scaffold src\d8\bank_d8_helpers_asar.asm --strict
python tools\build_source_bank_candidate_ranges_doc.py --bank D8
python tools\build_source_bank_residual_map.py --bank D8
```

Expected validation:

- `D8 byte-equivalence: OK, 28 module(s), 0 mismatch(es).`
- `notes/d8-source-residual-map.md` reports `0` residual bytes and `0`
  residual ranges.

## Protected Range Groups

| Group | Range | Bytes | Notes |
| --- | --- | ---: | --- |
| map tile collision data | `D8:0000..D8:8F50` | `36688` | raw collision data block |
| tile collision pointer tables | `D8:8F50..D8:F05E` | `24846` | 20 exact word-offset tables |
| anti-piracy warning arrangement | `D8:F05E..D8:F20D` | `431` | compressed warning asset |
| anti-piracy warning graphics | `D8:F20D..D8:F3BE` | `433` | compressed warning asset |
| warning palette | `D8:F3BE..D8:F3C6` | `8` | shared warning palette |
| faulty game pak arrangement | `D8:F3C6..D8:F5C4` | `510` | compressed warning asset |
| faulty game pak graphics | `D8:F5C4..D8:F6B7` | `243` | compressed warning asset |
| audio pack 61 | `D8:F6B7..D8:FFE9` | `2354` | generated audio pack payload |
| tail padding | `D8:FFE9..D8:10000` | `23` | explicit bank-end slack |

## Remaining Semantic Work

D8 is byte-complete, but collision semantics remain:

- decode pointed collision row formats under `MAP_TILE_COLLISION_DATA`
- tie the 20 pointer tables back to EF tileset-collision entries
- optionally render/decompress the warning-screen assets as visual fixtures
- leave audio packs opaque unless audio-pack decoding becomes a separate target

