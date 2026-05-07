# C3 battle visual offset tables F871-F8F1

## Reference context

This pass covers the remaining unnoted C3 unknown include starts in the battle visual tail:

- `C3:F871` `data/unknown/C3F871.asm`
- `C3:F8B1` `data/unknown/C3F8B1.asm`

The local C2 notes establish the neighbor at `C3:F8F1`: `C2:FEF9` selects one `0x20`-byte palette row from `C3:F8F1 + index * 0x20`, copies that same row into palette buffers `$0380`, `$03A0`, `$03C0`, and `$03E0`, then uploads the palette range.

## `C3:F871` graphics source offsets

`tools/find_xrefs.py C3F871` finds a long pointer hit at `C2:EE70`. The consumer constructs a source pointer in bank `$7F`, adds a word from `C3:F871 + $AAB2 * 2`, then copies four `0x80`-byte strips with a `0x0200` stride:

```text
C2:EE60  lda #$0000
C2:EE63  sta $0A
C2:EE65  lda #$007F
C2:EE68  sta $0C
C2:EE6A  lda $AAB2
C2:EE6D  asl A
C2:EE6E  tax
C2:EE6F  lda $C3F871,X
C2:EE73  adc $0A
...
C2:EEC4  cpx #$0080
C2:EEC9  lda #$0200
C2:EECD  adc $0A
C2:EED6  cmp #$0004
```

The table is 32 words, laid out as 8 groups of four strip offsets:

```text
C3:F871: 0000 0080 0100 0180
C3:F879: 0800 0880 0900 0980
C3:F881: 1000 1080 1100 1180
C3:F889: 1800 1880 1900 1980
C3:F891: 2000 2080 2100 2180
C3:F899: 2800 2880 2900 2980
C3:F8A1: 3000 3080 3100 3180
C3:F8A9: 3800 3880 3900 3980
```

This is best read as battle visual graphics-source offsets into the `$7F:0000` work buffer, with four `0x80` strips per visual frame or page.

## `C3:F8B1` OAM tile index offsets

`tools/find_xrefs.py C3F8B1` finds the direct consumer at `C2:EB44`. That routine builds OAM-style entries in a five-byte stride, seeds Y with `x * 5`, writes a fixed screen Y value `$E0`, reads `C3:F8B1 + (x + $AAB2) * 2`, stores the low byte as the tile index, then derives another attribute component through `C0:9251` selector `#$08`:

```text
C2:EB31  txa
C2:EB34  asl A
C2:EB35  asl A
C2:EB36  adc $04
C2:EB38  sta $1E
...
C2:EB43  lda #$F8B1
C2:EB46  sta $06
C2:EB48  lda #$00C3
C2:EB4B  sta $08
...
C2:EB53  adc $AAB2
C2:EB56  asl A
C2:EB62  adc $0A
C2:EB68  lda [$0A]
C2:EB6A  sta ($26),Y
```

The table shape is a regular tile-index grid:

```text
C3:F8B1: 0000 0004 0008 000C 0040 0044 0048 004C
C3:F8C1: 0080 0084 0088 008C 00C0 00C4 00C8 00CC
C3:F8D1: 0100 0104 0108 010C 0140 0144 0148 014C
C3:F8E1: 0180 0184 0188 018C 01C0 01C4 01C8 01CC
```

The `+4` horizontal step and `+0x40` row step match a 4-tile-wide OAM tile-index grid.

## Working Names

- `C3:F871` = `BattleVisualGraphicsSourceStripOffsets`
- `C3:F8B1` = `BattleVisualOamTileIndexGrid`
- `C3:F8F1` = `BattlePaletteSetRows`

## Remaining questions

- The upstream meaning of `$AAB2/$AAB4` in the C2 battle visual path is still bank-C2 local state. These C3 names describe the consumed data contracts rather than the whole effect scheduler.
- `C3:F819` remains the neighboring PSI/battle swirl overlay script table; this note only covers the visual offset and palette-table tail.
