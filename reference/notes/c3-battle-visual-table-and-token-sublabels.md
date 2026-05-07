# C3 battle visual table and token sublabels

## Purpose

This note promotes source-useful sublabels inside the C3 battle visual tail. The earlier notes named the public consumers; this pass names table rows and token branch bodies that are now structurally pinned well enough for source splitting. The source-emission contract for the dispatcher is now captured in [c3-battle-visual-effect-dispatch-source-contract-f981.md](notes/c3-battle-visual-effect-dispatch-source-contract-f981.md).

References:

- `notes/c3-battle-visual-offset-tables-f871-f8f1.md`
- `notes/c3-window-and-battle-visual-unknown-tail-e7e3-f981.md`
- `notes/c2-battle-sprite-render-and-palette-tail-c2eee7-c2ff9a.md`
- `notes/c2-battlebg-load-and-palette-effect-corridor-c2cfe5-c2e0e7.md`
- `notes/c2-psi-swirl-overlay-tail-c2e6b3-c2ea74.md`
- `notes/ppu-colour-window-bg-offset-frontier-c0afcd-c0b3ff.md`

## Battle-swirl overlay script payload

`C2:EA15` selects `C3:F819` only for mode `2`, storing it into the active effect-script pointer pair `$AECC/$AECE` and setting `$AEC8 = #$13`. That makes `C3:F819` a pointer-driven battle-swirl overlay script payload, not 65816 code.

The payload occupies the gap before `C3:F871`. Its exact per-record format belongs to the `AECC/AECE` effect-script interpreter, but the source boundary is clear enough to name the top-level C3 payload.

## Battle visual graphics offset rows

`C3:F871` is an eight-page table of four 0x80-byte source-strip offsets. The row starts are useful source labels because the consumer selects `C3:F871 + page * 8` and then copies the four strips with a `0x0200` stride in the `$7F:0000` work buffer.

The row starts are:

- `C3:F871`: page 0, offsets `0000, 0080, 0100, 0180`
- `C3:F879`: page 1, offsets `0800, 0880, 0900, 0980`
- `C3:F881`: page 2, offsets `1000, 1080, 1100, 1180`
- `C3:F889`: page 3, offsets `1800, 1880, 1900, 1980`
- `C3:F891`: page 4, offsets `2000, 2080, 2100, 2180`
- `C3:F899`: page 5, offsets `2800, 2880, 2900, 2980`
- `C3:F8A1`: page 6, offsets `3000, 3080, 3100, 3180`
- `C3:F8A9`: page 7, offsets `3800, 3880, 3900, 3980`

## OAM tile-index grid rows

`C3:F8B1` is a four-row OAM tile-index grid. Each row contains eight words with a `+4` horizontal step and a `+0x40` row step.

The row starts are:

- `C3:F8B1`: row 0, `0000..004C`
- `C3:F8C1`: row 1, `0080..00CC`
- `C3:F8D1`: row 2, `0100..014C`
- `C3:F8E1`: row 3, `0180..01CC`

## Battle palette rows

`C2:FEF9` treats input `A = 1, 2, 3` as palette-set rows `0, 1, 2` at `C3:F8F1 + (A - 1) * 0x20`. It then copies the selected 0x20-byte row to all four battle palette buffers `$0380`, `$03A0`, `$03C0`, and `$03E0`.

So the table has three confirmed 0x20-byte palette rows before the effect-token table begins at `C3:F951`:

- `C3:F8F1`: palette row 0
- `C3:F911`: palette row 1
- `C3:F931`: palette row 2

Earlier wording that suggested four distinct source rows was too broad: the routine copies one selected source row into four destination palette buffers.

## Visual effect token colour triples

`C3:F981` dispatches token ranges into two 3-byte tables. The byte order is now pinned by the branch bodies:

1. table byte `2` -> `A` for `C0:B01A`
2. table byte `1` -> `X` for `C0:B01A`
3. table byte `0` -> `Y` for `C0:B01A`

So each record is best read as a fixed-colour RGB component triple in source order `B, G, R` as consumed by `SetFixedColourRgbComponents`, while the table's byte order is `R, G, B`.

The first table at `C3:F951` covers tokens `#$0023..#$002D`. Its branch body at `C3:F9A2` darkens loaded battle-background palettes through `C2:DE0F`, applies the selected fixed colour, writes colour add/sub mode registers with `A = #$0010`, `X = #$003F`, then calls `C4:A67E(5, 7)`.

The second table at `C3:F972` covers tokens `#$0031..#$0035`. Its branch body at `C3:FA4A` is the same fixed-colour path, but its final `C4:A67E` parameters split by token:

- tokens `< #$0035`: `C4:A67E(4, 5)`
- tokens `>= #$0035`: `C4:A67E(2, 4)`

The middle token range `#$002E..#$0030` does not use a table. It either sets `WOBBLE_DURATION` (`$AD92`) to `#$0090`, sets `SHAKE_DURATION` (`$AD94`) to `#$012C`, or no-ops.

## Working Names

- `C3:F819` = `BattleSwirlOverlayMode2Script`
- `C3:F879` = `BattleVisualGraphicsSourceStripOffsetsPage1`
- `C3:F881` = `BattleVisualGraphicsSourceStripOffsetsPage2`
- `C3:F889` = `BattleVisualGraphicsSourceStripOffsetsPage3`
- `C3:F891` = `BattleVisualGraphicsSourceStripOffsetsPage4`
- `C3:F899` = `BattleVisualGraphicsSourceStripOffsetsPage5`
- `C3:F8A1` = `BattleVisualGraphicsSourceStripOffsetsPage6`
- `C3:F8A9` = `BattleVisualGraphicsSourceStripOffsetsPage7`
- `C3:F8C1` = `BattleVisualOamTileIndexGridRow1`
- `C3:F8D1` = `BattleVisualOamTileIndexGridRow2`
- `C3:F8E1` = `BattleVisualOamTileIndexGridRow3`
- `C3:F911` = `BattlePaletteSetRow1`
- `C3:F931` = `BattlePaletteSetRow2`
- `C3:F951` = `BattleVisualToken23To2dColourTriples`
- `C3:F972` = `BattleVisualToken31To35ColourTriples`
- `C3:F9A2` = `ApplyBattleVisualToken23To2dColourEffect`
- `C3:FA4A` = `ApplyBattleVisualToken31To35ColourEffect`
- `C3:FAC7` = `ReturnFromBattleVisualEffectTokenDispatch`

## Remaining questions

- `C3:F819` still needs the `AECC/AECE` effect-script interpreter format before its internal records should get field names.
- The effect-token tables are byte-order pinned, but the gameplay-facing meaning of each individual token still belongs to the battle action/effect caller pass.
