# C3 battle visual data and file-select transition split

This note splits the old raw `C3:F2B1..F5F9` row into two data contracts and one ordinary source helper.

## Data prefix

`C3:F2B1..F2B5` is `LEVEL_UP_STAT_GROWTH_VARIANCE_TABLE`.

`C1:D08B` computes level-up stat growth deltas. After a `C4:5F7B(3)` random result, it calls `C0:91F4`, indexes `C3:F2B1` as bytes, and adds the selected byte into the delta calculation:

```text
C1:D0D8  LDA #$0003
C1:D0DB  JSL C4:5F7B
C1:D0E1  LDY $11
C1:D0E4  INC A
C1:D0E5  LDY #$0004
C1:D0E8  JSL C0:91F4
C1:D0EC  TAX
C1:D0ED  LDA $C3F2B1,X
C1:D0F1  AND #$00FF
```

`C3:F2B5..F3C5` is `VISUAL_SELECTOR_POSE_ROW_TABLE`.

This is the table already documented by the visual-selector notes. `C0:780F`/`C0:79EC` index it as 16-byte rows of eight word pose values:

```text
C0:79E3  ADC $02
C0:79E5  TAX
C0:79E6  LDA $C3F2B5,X

C0:7A1F  CLC
C0:7A20  ADC $02
C0:7A22  TAX
C0:7A23  LDA $C3F2B5,X
```

The current best name remains visual-selector pose row table: it maps higher-level row/context selectors to concrete pose indices.

## Source helper

`C3:F3C5..F5F9` is real callable 65816 source, not data.

Direct control-flow callers:

- `C1:BFE8`
- `C4:DBB3`
- `C4:DC19`
- `C4:DC37`

The helper is reached by text command `1F 41` special event `0A` and by file-select/intro transition paths. It sets up a file-select-like visual transition, queues display/VRAM work through C0/C4 helpers, waits through C1 tick calls, handles input/exit state, and returns a status in `A`.

## Working Names

- `C3:F2B1` = `LevelUpStatGrowthVarianceTable`
- `C3:F2B5` = `VisualSelectorPoseRowTable`
- `C3:F3C5` = `RunFileSelectVisualTransition`

## Remaining softness

The exact user-facing name of `C3:F3C5` is still a little cautious because it is reachable both from file-select/intro state and from a special text command. The important source/data split is no longer soft: `F2B1..F3C5` is table data, and `F3C5..F5F9` is callable source.
