# C3 late interaction table contracts

This note promotes four small table families inside the late C3 preserved corridor from cautious raw data to explicit ROM-table contracts.

## Pathfinding tile-context gate

`C3:DFE8..DFF0` is now `PATHFINDING_TILE_CONTEXT_GATE_TABLE`.

Consumer evidence:

```text
C0:C0CB  JSL C0:0AA1
C0:C0CF  AND #$0007
C0:C0D2  TAX
C0:C0D3  LDA $C3DFE8,X
C0:C0D7  AND #$00FF
C0:C0DA  BNE continue_path_consumer

C0:C1B2  JSL C0:0AA1
C0:C1B6  AND #$0007
C0:C1B9  TAX
C0:C1BA  LDA $C3DFE8,X
C0:C1BE  AND #$00FF
C0:C1C1  BNE continue_path_consumer
```

`C0:0AA1` returns the current player tile context from the D7:B200 map-tile table and caches it in `$438E`. These two path consumers mask the context to `0..7`, index the C3 byte table, and abort if the gate byte is zero.

## Interaction result facing remap

`C3:E168..E178` is now `INTERACTION_RESULT_FACING_REMAP_TABLE`.

Consumer evidence:

```text
C0:42D2  LDA $987F
C0:42D5  ASL
C0:42D6  TAX
C0:42D7  LDA $C3E168,X
C0:42DB  LDX $98AB
C0:42DD  STA $2AF6,X
C0:42E0  JSL C0:9907
C0:42E4  JSL C0:A48F
```

This is the class-1 interaction result path documented in `notes/interaction-result-classes.md` and `notes/interaction-result-consumers.md`. It remaps the player/current facing value in `$987F` into the target slot's `$2AF6` facing/state field before the target refresh calls.

## Door candidate direction offsets

`C3:E230..E240` is now `DOOR_CANDIDATE_DIRECTION_OFFSET_X`, and `C3:E240..E250` is now `DOOR_CANDIDATE_DIRECTION_OFFSET_Y`.

Consumer evidence:

```text
C4:335F  ADC $C3E230,X
C4:3374  ADC $C3E240,X
...
C4:33AB  ADC $C3E230,X
C4:33B7  ADC $C3E240,X
```

`X` is the input/facing direction index doubled. The C4 door probe adds these signed coarse-cell offsets to the player tile coordinate, checks tile flags, and may store a cached door fallback candidate in `$5DDC/$5DDE/$5DE0` while setting `$5D62` to `#$FFFE`.

## Still cautious

The remaining late-C3 cautious spans stay raw for now:

- `C3:DFF0..E12C`: broader pathfinding-context table family with legacy sublabels but no final field split.
- `C3:E178..E1D8`: additional interaction/facing/result data adjacent to the promoted class-1 remap.
- `C3:E250..E3F8`: file-select or name-entry sprite/OAM-like data.
- `C3:E3F8..E40E`: menu cursor tile prefix words before the promoted cursor-frame contracts.
- `C3:E44C..E450`: four-byte data island immediately before the C3:E450 helper.
