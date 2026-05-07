# C3 menu cursor tile data E3F8-E450

## Reference context

This pass covers the remaining unnoted C3 unknown include starts in the menu/text tile cluster:

- `C3:E3F8` `data/unknown/C3E3F8.asm`
- `C3:E41C` `data/unknown/C3E41C.asm`
- `C3:E44C` `data/unknown/C3E44C.asm`

The surrounding `ebsrc` bankconfig entries are useful:

- `data/text/window_configuration_table.asm`
- `data/unknown/C3E3F8.asm`
- `data/unknown/C3E40E.asm`
- `data/text/blinking_triangle_tiles.asm`
- `data/unknown/C3E41C.asm`
- `data/unknown/C3E41C_pointer_table.asm`
- `data/unknown/C3E44C.asm`
- `unknown/C3/C3E450.asm`
- text/window tick helpers

The legacy disassembly names `C3:E406` as `AnimatedMenuCursorTiles`, with `.PointRight` and `.PointDown` sublabels.

## Tile words

The verified ROM data from `C3:E3F8` through the pointer table is:

```text
C3:E3F8: 0908 1918 090A 191A 2415 2416 6415
C3:E406: 2441 268D 2451 269D
C3:E40E: 3A69 3A6A 3A6B 3A6C
C3:E416: 3C14 3C15 BC11
C3:E41C: 3C16 2E6D 2E6E 7C16
C3:E424: 3C16 2E7D 2E7E 7C16
C3:E42C: 3C16 2E6D 2C40 7C16
C3:E434: 3C16 2C40 2E6E 7C16
C3:E43C: C3:E41C C3:E424 C3:E42C C3:E434
```

The whole `C3:E3F8-E44B` cursor/triangle tile corridor is now split into small ROM-table contracts:

- `C3:E3F8-E405` = `MENU_CURSOR_TILE_PREFIX_TABLE`
- `C3:E406-E40D` = `ANIMATED_MENU_CURSOR_POINT_RIGHT_TILES`
- `C3:E40E-E415` = `TITLE_NAME_BUFFER_CURSOR_TILE_RUN`
- `C3:E416-E41B` = `BLINKING_TRIANGLE_BASE_TILES`
- `C3:E41C-E43B` = `BLINKING_TRIANGLE_WAIT_FRAME_TILES`
- `C3:E43C-E44B` = `BLINKING_TRIANGLE_WAIT_FRAME_POINTER_TABLE`

`C3:E406-E40D` matches the legacy right-pointing cursor tiles:

```text
PointRight.Top:    2441 268D
PointRight.Bottom: 2451 269D
```

`C3:E416-E43B` is the blinking/down cursor family. `C3:E416-E41B` is the three-word base tile run; `C3:E41C`, `C3:E424`, `C3:E42C`, and `C3:E434` are four 4-word frames selected by the long pointer table at `C3:E43C`; the latter two replace one interior tile with `$2C40`, so they are partial-blank blink frames rather than separate structures.

`C3:E40E` is already tied to the C2 title/name buffer helper: `C2:0266` copies the four words `$3A69,$3A6A,$3A6B,$3A6C` into `$8272`.

## `C3:E44C` boundary

`C3:E44C` is a four-byte data island immediately before the routine at `C3:E450`:

```text
C3:E44C: A4 A8 66 00
C3:E450: REP #$31 ; routine body
```

Decoding `C3:E44C` as code gives only two implausible direct-page operations before the real routine prologue, and direct caller scanning finds the routine entry at `C3:E450` from `C1:0058`. For now, `C3:E44C` should remain a named data boundary, not a code label.

`C3:E450` itself runs from the C1 window tick path when `$89C9` is nonzero. It computes a source pointer in bank `E0` from `$99CD`, chooses one of two row offsets (`#$0008` or `#$0028`) depending on bit `#$04` of `$0002`, and calls `C0:8ED2` to transfer `#$0228` bytes with `X = #$0008`. This is adjacent UI/window rendering code, but it is not the same data object as the cursor tile tables.

## Working Names

- `C3:E3F8` = `MenuCursorTilePrefixTable`
- `C3:E406` = `AnimatedMenuCursorPointRightTiles`
- `C3:E40E` = `TitleNameBufferCursorTileRun`
- `C3:E416` = `BlinkingTriangleBaseTiles`
- `C3:E41C` = `BlinkingTriangleWaitFrame0Tiles`
- `C3:E424` = `BlinkingTriangleWaitFrame1Tiles`
- `C3:E42C` = `BlinkingTriangleWaitFrame2Tiles`
- `C3:E434` = `BlinkingTriangleWaitFrame3Tiles`
- `C3:E43C` = `BlinkingTriangleWaitFramePointerTable`
- `C3:E44C` = `WindowTickTransferPreludeData`
- `C3:E450` = `WindowTickTransferDynamicTileBlock`

## Remaining questions

- `C3:E3F8-E405` is structurally contracted as tile/attribute words, but still needs a consumer-side proof before upgrading beyond `proposed`.
- The `C3:E44C` two-word payload needs its actual consumer before the name can be promoted beyond boundary documentation.
