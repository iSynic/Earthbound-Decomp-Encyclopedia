# Bank CA Source Scaffold Handoff

## Status

Bank `CA` is byte-complete for the current source-scaffold phase.

- durable scaffold: `src/ca/bank_ca_helpers_asar.asm`
- manifest: `build/ca-build-candidate-ranges.json`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `27`
- source bytes: `0`
- preserved data-gap bytes: `65536`
- byte-equivalence: `OK`, `0` mismatches

CA is protected as a battle-background asset/data bank: 20 compressed binary
asset corridors, 6 table corridors, and 1 byte of tail padding.

## Regenerate And Validate

Use these commands from the repository root:

```powershell
python tools\build_asset_bank_manifest.py CA --json-out build\asset-bank-ca.json --markdown-out notes\bank-ca-asset-data-map.md
python tools\promote_asset_bank_to_source_scaffold.py CA
python tools\build_source_bank_scaffold.py --bank CA
python tools\validate_source_bank_byte_equivalence.py --bank CA --module all --combined --scaffold src\ca\bank_ca_helpers_asar.asm --strict
python tools\build_source_bank_candidate_ranges_doc.py --bank CA
python tools\build_source_bank_residual_map.py --bank CA
```

Expected validation:

- `CA byte-equivalence: OK, 27 module(s), 0 mismatch(es).`
- `notes/ca-source-residual-map.md` reports `0` residual bytes and `0`
  residual ranges.

## Protected Range Groups

| Group | Range | Bytes | Notes |
| --- | --- | ---: | --- |
| compressed battle-background assets | `CA:0000..CA:D7A1` | `55201` | 15 graphics payloads, 5 arrangement payloads |
| battle-background pointer tables | `CA:D7A1..CA:DCA1` | `1280` | graphics, arrangement, and palette pointer tables |
| battle-background config table | `CA:DCA1..CA:F258` | `5559` | 327 17-byte layer config records |
| battle-background scrolling table | `CA:F258..CA:F708` | `1200` | 600 word values |
| battle-background distortion table | `CA:F708..CA:FFFF` | `2295` | mixed byte/word distortion records |
| tail padding | `CA:FFFF..CA:10000` | `1` | explicit bank-end slack |

## Remaining Semantic Work

The CA scaffold is byte-complete, but it is still an asset scaffold. Future
polish should focus on richer table emitters:

- split pointer tables into typed long-pointer rows
- emit the 17-byte config table as named layer records
- map the distortion table to the friendlier YAML interpretation in
  `refs/eb-decompile-4ef92/bg_distortion_table.yml`
- optionally decompress/render sampled battle backgrounds as a visual regression
  check

