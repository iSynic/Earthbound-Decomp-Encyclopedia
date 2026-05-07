# Bank CB Source Scaffold Handoff

## Status

Bank `CB` is byte-complete for the current source-scaffold phase.

- durable scaffold: `src/cb/bank_cb_helpers_asar.asm`
- manifest: `build/cb-build-candidate-ranges.json`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `304`
- source bytes: `0`
- preserved data-gap bytes: `65536`
- byte-equivalence: `OK`, `0` mismatches

CB is protected as a mixed battle-background asset/audio/table bank: 302 binary
asset corridors, 1 battle-entry background-layer table corridor, and one tail
padding corridor.

## Regenerate And Validate

Use these commands from the repository root:

```powershell
python tools\build_asset_bank_manifest.py CB --json-out build\asset-bank-cb.json --markdown-out notes\bank-cb-asset-data-map.md
python tools\promote_asset_bank_to_source_scaffold.py CB
python tools\build_source_bank_scaffold.py --bank CB
python tools\validate_source_bank_byte_equivalence.py --bank CB --module all --combined --scaffold src\cb\bank_cb_helpers_asar.asm --strict
python tools\build_source_bank_candidate_ranges_doc.py --bank CB
python tools\build_source_bank_residual_map.py --bank CB
```

Expected validation:

- `CB byte-equivalence: OK, 304 module(s), 0 mismatch(es).`
- `notes/cb-source-residual-map.md` reports `0` residual bytes and `0`
  residual ranges.

## Protected Range Groups

| Group | Range | Bytes | Notes |
| --- | --- | ---: | --- |
| battle-background assets | `CB:0000..CB:D89A` | `55450` | arrangements, graphics, and palettes |
| battle-entry background-layer table | `CB:D89A..CB:E02A` | `1936` | `BTL_ENTRY_BG_TABLE`, 968 word values |
| audio pack 66 | `CB:E02A..CB:FEE2` | `7864` | generated audio pack payload |
| audio pack 59 | `CB:FEE2..CB:FFE4` | `258` | generated audio pack payload |
| tail padding | `CB:FFE4..CB:10000` | `28` | explicit bank-end slack |

## Remaining Semantic Work

CB is byte-complete, but the asset semantics are still intentionally raw:

- row-name the battle-entry background-layer table against battle entry IDs
- keep CA's pointer/config tables and CB's layer table linked in documentation
- optionally render/decompress sampled battle background arrangements, graphics,
  and palettes as a visual regression
- leave audio packs as binary assets unless the audio-pack format becomes a
  separate decompilation target

