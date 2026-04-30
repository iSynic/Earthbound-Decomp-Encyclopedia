; EarthBound C1 window tilemap and HP/PP window display helpers.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Hand-polished from tools/emit_linear_source_module.py output, then
;   intended for byte-equivalence validation.
;
; Source unit covered:
; - C1:07AF..C1:0A85 BuildWindowTilemapFromDescriptor

; ---------------------------------------------------------------------------
; External contracts used by this module

C08FF7_ResolveIndexedPointerOffset       = $C08FF7
C08F22_ScanDelimitedByteRun              = $C08F22
C207E1_ClearPartyMemberHpppWindow        = $C207E1
C3E6F8_ClearFocusedPartyHpPpActorAndBlankRow = $C3E6F8

WindowDescriptorSize     = $0052
WindowDescriptorTable    = $8650
WindowTileBufferPointer  = $8685
WindowOptionalRunCount   = $868B
WindowOptionalRunData    = $868C
WindowDescriptorIdField  = $8654
WindowXField             = $8656
WindowYField             = $8658
WindowWidthField         = $865A
WindowHeightField        = $865C
PartyWindowActorTable    = $986F
PartyWindowRecordTable   = $99CE
PartyCountByte           = $98A4
TextDisplayModeFlag      = $89C9
TextWindowDirtyFlag      = $9623
BattleWindowModeFlag     = $9643
PartyWindowDirtyMask     = $9647
HighlightedWindowId      = $5E7A
HighlightedWindowTileSet = $5E7C
HighlightedTileSetTableLo = $E43C
HighlightedTileSetTableBank = $00C3

DescriptorId             = $20
TileCursor               = $18
TileSourcePointer        = $1E
WindowWidth              = $1C
WindowHeight             = $1A
DescriptorOffset         = $16
OptionalRunPointer       = $14
OptionalRunRemaining     = $14
OptionalRunWidth         = $12
TileWord                 = $02
LongPointerLo            = $06
LongPointerBank          = $08
HighlightTablePointerLo  = $0A
HighlightTablePointerBank = $0C
ScanPointerLo            = $0E
ScanPointerBank          = $10
PartyIndex               = $0E

; ---------------------------------------------------------------------------
; C1:07AF

C107AF_BuildWindowTilemapFromDescriptor:
    rep #$31
    phd
    pha
    tdc
    adc.w #$FFDE
    tcd
    pla
    sta DescriptorId
    ldy.w #WindowDescriptorSize
    jsl C08FF7_ResolveIndexedPointerOffset
    tay
    lda WindowTileBufferPointer,Y
    sta TileSourcePointer
    lda WindowXField,Y
    asl A
    sta TileWord
    lda WindowYField,Y
    asl A
    asl A
    asl A
    asl A
    asl A
    asl A
    clc
    adc TileWord
    clc
    adc.w #$7DFE
    tax
    lda WindowWidthField,Y
    sta $04
    sta WindowWidth
    lda WindowHeightField,Y
    sta WindowHeight
    lda $0000,X
    beq C107F5_WritePlainTopLeftCorner
    cmp.w #$3C10
    bne C10802_WriteJoinedTopLeftCorner

C107F5_WritePlainTopLeftCorner:
    lda.w #$3C10
    sta $0000,X
    txy
    iny
    iny
    sty TileCursor
    bra C1080D_CheckOptionalTopBorderRun

C10802_WriteJoinedTopLeftCorner:
    lda.w #$3C13
    sta $0000,X
    txy
    iny
    iny

C1080B_StoreTopBorderCursor:
    sty TileCursor

C1080D_CheckOptionalTopBorderRun:
    lda DescriptorId
    ldy.w #WindowDescriptorSize
    jsl C08FF7_ResolveIndexedPointerOffset
    sta DescriptorOffset
    tax
    sep #$20
    lda WindowOptionalRunCount,X
    sta $00
    rep #$20
    lda $00
    and.w #$00FF
    bne C1082C_DrawOptionalTopBorderRun
    jmp.w C108B8_DrawTopBorderFill

C1082C_DrawOptionalTopBorderRun:
    lda DescriptorOffset
    clc
    adc.w #WindowOptionalRunData
    sta OptionalRunPointer
    lda $00
    and.w #$00FF
    dec A

C1083A_DrawOptionalTopBorderRun:
    asl A
    asl A
    asl A
    asl A
    clc
    adc.w #$02E0
    sta TileWord
    lda.w #$3C16
    ldy TileCursor
    sta $0000,Y
    tyx
    inx
    inx
    stx TileCursor
    lda $04
    dec A
    sta $04
    sta OptionalRunWidth
    lda OptionalRunPointer
    sta LongPointerLo
    phb
    sep #$20
    pla
    sta LongPointerBank
    stz LongPointerBank + 1
    rep #$20
    lda LongPointerLo
    sta ScanPointerLo
    lda LongPointerBank
    sta ScanPointerBank
    jsl C08F22_ScanDelimitedByteRun
    sta $04
    asl A
    adc $04
    asl A
    clc
    adc.w #$0007
    lsr A
    lsr A
    lsr A
    sta OptionalRunRemaining
    bra C108A2_TestOptionalRunTilesRemaining

C10883_WriteOptionalRunTile:
    lda TileWord
    clc
    adc.w #$2000

C10889_StoreOptionalRunTile:
    ldx TileCursor
    sta $0000,X
    inc TileWord
    inx
    inx
    stx TileCursor
    lda OptionalRunWidth
    sta $04
    dec A
    sta $04
    sta OptionalRunWidth
    lda OptionalRunRemaining
    dec A
    sta OptionalRunRemaining

C108A2_TestOptionalRunTilesRemaining:
    bne C10883_WriteOptionalRunTile
    lda.w #$7C16
    ldx TileCursor
    sta $0000,X
    txy
    iny
    iny
    sty TileCursor
    lda OptionalRunWidth
    sta $04
    dec A
    sta $04

C108B8_DrawTopBorderFill:
    lda DescriptorId
    ldy.w #WindowDescriptorSize
    jsl C08FF7_ResolveIndexedPointerOffset
    tax
    lda WindowDescriptorIdField,X
    cmp HighlightedWindowId
    bne C108DA_TopBorderWidthReady
    lda HighlightedWindowTileSet
    cmp.w #$FFFF
    beq C108DA_TopBorderWidthReady
    lda $04
    sec
    sbc.w #$0004
    sta $04

C108DA_TopBorderWidthReady:
    ldx $04
    bra C108EB_TestTopBorderFillRemaining

C108DE_DrawTopBorderFillTile:
    lda.w #$3C11
    ldy TileCursor
    sta $0000,Y
    iny
    iny
    sty TileCursor
    dex

C108EB_TestTopBorderFillRemaining:
    bne C108DE_DrawTopBorderFillTile
    lda DescriptorId
    ldy.w #WindowDescriptorSize
    jsl C08FF7_ResolveIndexedPointerOffset
    tax
    lda WindowDescriptorIdField,X
    cmp HighlightedWindowId
    bne C10941_WriteTopRightCorner
    lda HighlightedWindowTileSet
    cmp.w #$FFFF
    beq C10941_WriteTopRightCorner
    lda.w #HighlightedTileSetTableLo
    sta HighlightTablePointerLo
    lda.w #HighlightedTileSetTableBank
    sta HighlightTablePointerBank
    lda HighlightedWindowTileSet
    asl A
    asl A
    clc
    adc HighlightTablePointerLo
    sta HighlightTablePointerLo
    ldy.w #$0002
    lda [HighlightTablePointerLo],Y
    tay
    lda [HighlightTablePointerLo]
    sta LongPointerLo
    sty LongPointerBank
    ldx.w #$0000
    bra C1093C_TestHighlightedTilesRemaining

C1092C_CopyHighlightedTopBorderTile:
    lda [LongPointerLo]
    ldy TileCursor
    sta $0000,Y
    inc LongPointerLo
    inc LongPointerLo
    iny
    iny
    sty TileCursor
    inx

C1093C_TestHighlightedTilesRemaining:
    cpx.w #$0004
    bcc C1092C_CopyHighlightedTopBorderTile

C10941_WriteTopRightCorner:
    ldy TileCursor
    lda $0000,Y
    beq C1094D_WritePlainTopRightCorner
    cmp.w #$7C10
    bne C1095A_WriteJoinedTopRightCorner

C1094D_WritePlainTopRightCorner:
    lda.w #$7C10
    sta $0000,Y
    tya
    inc A
    inc A
    sta DescriptorId
    bra C10965_DrawInteriorAndBottomRows

C1095A_WriteJoinedTopRightCorner:
    lda.w #$7C13
    sta $0000,Y
    tya
    inc A
    inc A
    sta DescriptorId

C10965_DrawInteriorAndBottomRows:
    lda.w #$0020
    sec
    sbc WindowWidth
    dec A
    dec A
    asl A
    sta TileWord
    lda DescriptorId
    clc
    adc TileWord
    tax
    ldy WindowHeight
    bra C109BB_TestInteriorRowsRemaining

C1097A_DrawInteriorRow:
    lda.w #$3C12
    sta $0000,X
    inx
    inx
    lda WindowWidth
    sta TileCursor
    bra C1099C_TestInteriorFillRemaining

C10988_CopyInteriorTile:
    lda (TileSourcePointer)
    clc
    adc.w #$2000
    sta $0000,X
    inc TileSourcePointer
    inc TileSourcePointer
    inx
    inx
    lda TileCursor
    dec A
    sta TileCursor

C1099C_TestInteriorFillRemaining:
    bne C10988_CopyInteriorTile
    lda.w #$7C12
    sta $0000,X
    txa
    inc A
    inc A
    sta DescriptorOffset
    lda.w #$0020
    sec
    sbc WindowWidth
    dec A
    dec A
    asl A
    sta TileWord
    lda DescriptorOffset
    clc
    adc TileWord
    tax
    dey

C109BB_TestInteriorRowsRemaining:
    bne C1097A_DrawInteriorRow
    lda $0000,X
    beq C109C7_WritePlainBottomLeftCorner
    cmp.w #$BC10
    bne C109D2_WriteJoinedBottomLeftCorner

C109C7_WritePlainBottomLeftCorner:
    lda.w #$BC10
    sta $0000,X
    txy
    iny
    iny
    bra C109DB_DrawBottomBorderFill

C109D2_WriteJoinedBottomLeftCorner:
    lda.w #$BC13
    sta $0000,X
    txy
    iny
    iny

C109DB_DrawBottomBorderFill:
    ldx WindowWidth
    bra C109E8_TestBottomBorderFillRemaining

C109DF_DrawBottomBorderFillTile:
    lda.w #$BC11
    sta $0000,Y
    iny
    iny
    dex

C109E8_TestBottomBorderFillRemaining:
    bne C109DF_DrawBottomBorderFillTile
    lda $0000,Y
    beq C109F4_WritePlainBottomRightCorner
    cmp.w #$FC10
    bne C109FC_WriteJoinedBottomRightCorner

C109F4_WritePlainBottomRightCorner:
    lda.w #$FC10
    sta $0000,Y
    bra C10A02_ReturnBuildWindowTilemapFromDescriptor

C109FC_WriteJoinedBottomRightCorner:
    lda.w #$FC13
    sta $0000,Y

C10A02_ReturnBuildWindowTilemapFromDescriptor:
    pld
    rtl

; ---------------------------------------------------------------------------
; C1:0A04

C10A04_ShowHpppWindows_Internal:
    rep #$31
    jsl C3E6F8_ClearFocusedPartyHpPpActorAndBlankRow
    sep #$20
    lda.b #$01
    sta TextDisplayModeFlag
    sta TextWindowDirtyFlag
    rep #$20
    lda.w #$FFFF
    sta PartyWindowDirtyMask
    rts

; ---------------------------------------------------------------------------
; C1:0A1D

C10A1D_HideHpppWindows_Internal:
    rep #$31
    phd
    tdc
    adc.w #$FFF0
    tcd
    jsl C3E6F8_ClearFocusedPartyHpPpActorAndBlankRow
    sep #$20
    stz TextDisplayModeFlag
    rep #$20
    lda BattleWindowModeFlag
    bne C10A7A_MarkTextWindowDirty
    ldy.w #$0000
    sty PartyIndex
    bra C10A6D_TestPartyWindowsRemaining

C10A3C_RedrawNextPartyWindow:
    tya
    jsl C207E1_ClearPartyMemberHpppWindow
    ldy PartyIndex
    lda PartyWindowActorTable,Y
    and.w #$00FF
    dec A
    ldy.w #$005F
    jsl C08FF7_ResolveIndexedPointerOffset
    clc
    adc.w #PartyWindowRecordTable
    tax
    lda $0047,X
    sta $0045,X
    lda $004D,X
    sta $004B,X
    stz $0049,X
    stz $0043,X
    ldy PartyIndex
    iny
    sty PartyIndex

C10A6D_TestPartyWindowsRemaining:
    lda PartyCountByte
    and.w #$00FF
    sta TileWord
    tya
    cmp TileWord
    bne C10A3C_RedrawNextPartyWindow

C10A7A_MarkTextWindowDirty:
    sep #$20
    lda.b #$01
    sta TextWindowDirtyFlag
    rep #$20
    pld
    rts

; ---------------------------------------------------------------------------
; C1:0A85

C10A85_BuildWindowTilemapFromDescriptor_End:
