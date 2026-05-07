# Bank CF Source Scaffold Handoff

## Status

Bank `CF` is byte-complete for the current source-scaffold phase.

- durable scaffold: `src/cf/bank_cf_helpers_asar.asm`
- manifest: `build/cf-build-candidate-ranges.json`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `11`
- source bytes: `0`
- preserved data-gap bytes: `65536`
- byte-equivalence: `OK`, `0` mismatches

CF is protected as exact generated map-data table splits plus two audio pack
payloads and a seven-byte tail padding corridor.

## Regenerate And Validate

Use these commands from the repository root:

```powershell
python tools\build_cf_table_splits.py
python tools\promote_table_splits_to_source_scaffold.py CF
python tools\build_source_bank_scaffold.py --bank CF
python tools\validate_source_bank_byte_equivalence.py --bank CF --module all --combined --scaffold src\cf\bank_cf_helpers_asar.asm --strict
python tools\build_source_bank_candidate_ranges_doc.py --bank CF
python tools\build_source_bank_residual_map.py --bank CF
```

Expected validation:

- `CF byte-equivalence: OK, 11 module(s), 0 mismatch(es).`
- `notes/cf-source-residual-map.md` reports `0` residual bytes and `0`
  residual ranges.

## Protected Range Groups

| Group | Range | Bytes | Notes |
| --- | --- | ---: | --- |
| door data | `CF:0000..CF:264F` | `9807` | variable door payload block; type 0/2/6 variants decoded in `notes/cf-door-data-contracts.md` |
| door config table | `CF:264F..CF:58EF` | `12960` | 1280 counted sector lists; trigger payload meanings decoded in `notes/cf-movement-trigger-contracts.md` |
| overworld event music pointer table | `CF:58EF..CF:5A39` | `330` | 165 word pointers |
| overworld event music table | `CF:5A39..CF:61DD` | `1956` | 164 selector-addressed event-music context chains; see `notes/cf-event-music-context-contracts.md` |
| inline event music trailer | `CF:61DD..CF:61E7` | `10` | inline bank-config bytes |
| sprite placement pointer table | `CF:61E7..CF:6BE7` | `2560` | 1280 word pointers |
| sprite placement table | `CF:6BE7..CF:8985` | `7582` | 627 counted sector lists |
| NPC config table | `CF:8985..CF:F2B5` | `26928` | 1584 rows, stride `0x11` |
| audio pack 94 | `CF:F2B5..CF:FF38` | `3203` | generated audio pack payload |
| audio pack 96 | `CF:FF38..CF:FFF9` | `193` | generated audio pack payload |
| tail padding | `CF:FFF9..CF:10000` | `7` | explicit bank-end slack |

## Remaining Semantic Work

CF is byte-complete, but useful semantic work remains:

- keep the CF door-data type 0/2/6 payload contract regression-tested
- keep the CF movement-trigger parameter contract regression-tested
- keep the CF/DC event-music context contract regression-tested
- row-name NPC config entries against map/sprite placement consumers
- keep the D0 door pointer table tied to the CF door config contract
- leave audio packs opaque unless audio-pack decoding becomes a separate target
