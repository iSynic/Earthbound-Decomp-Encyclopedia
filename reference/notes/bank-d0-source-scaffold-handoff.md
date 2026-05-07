# Bank D0 Source Scaffold Handoff

## Status

Bank `D0` is byte-complete for the current source-scaffold phase.

- durable scaffold: `src/d0/bank_d0_helpers_asar.asm`
- manifest: `build/d0-build-candidate-ranges.json`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `11`
- source bytes: `0`
- preserved data-gap bytes: `65536`
- byte-equivalence: `OK`, `0` mismatches

D0 is protected as exact generated map/battle-data table splits plus one audio
pack payload and an 88-byte tail padding corridor.

## Regenerate And Validate

Use these commands from the repository root:

```powershell
python tools\build_d0_table_splits.py
python tools\promote_table_splits_to_source_scaffold.py D0
python tools\build_source_bank_scaffold.py --bank D0
python tools\validate_source_bank_byte_equivalence.py --bank D0 --module all --combined --scaffold src\d0\bank_d0_helpers_asar.asm --strict
python tools\build_source_bank_candidate_ranges_doc.py --bank D0
python tools\build_source_bank_residual_map.py --bank D0
```

Expected validation:

- `D0 byte-equivalence: OK, 11 module(s), 0 mismatch(es).`
- `notes/d0-source-residual-map.md` reports `0` residual bytes and `0`
  residual ranges.

## Protected Range Groups

| Group | Range | Bytes | Notes |
| --- | --- | ---: | --- |
| door pointer table | `D0:0000..D0:1400` | `5120` | 1280 long pointers into CF |
| screen transition config table | `D0:1400..D0:1598` | `408` | 34 rows, stride `0x0C` |
| event control pointer table | `D0:1598..D0:15C0` | `40` | 20 word pointers into decoded tile-event chains |
| map tile event control table | `D0:15C0..D0:1880` | `704` | 20 variable chains; decoded in `notes/d0-tile-event-contracts.md` |
| map enemy placement | `D0:1880..D0:B880` | `40960` | 20480 word entries |
| enemy placement group pointer table | `D0:B880..D0:BBAC` | `812` | 203 long pointers |
| enemy placement groups table | `D0:BBAC..D0:C60D` | `2657` | 203 variable lists |
| battle entry pointer table | `D0:C60D..D0:D52D` | `3872` | 484 rows, stride `0x08` |
| enemy battle groups table | `D0:D52D..D0:DFB4` | `2695` | variable battle groups |
| audio pack 139 | `D0:DFB4..D0:FFA8` | `8180` | generated audio pack payload |
| tail padding | `D0:FFA8..D0:10000` | `88` | explicit bank-end slack |

## Remaining Semantic Work

D0 is byte-complete and its highest-risk variable rows now have row contracts:

- use `notes/d0-tile-event-contracts.json` for tile-event source emission
- use `notes/d0-variable-list-contracts.json` for placement/battle source emission
- connect `BTL_ENTRY_PTR_TABLE` rows to higher-level enemy/battle metadata names
- keep D0's door pointer table linked to CF's door config table contract
