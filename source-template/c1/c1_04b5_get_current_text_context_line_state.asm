; EarthBound C1 active-window cursor field accessors.
;
; Source-emission status:
; - Prototype level: build-candidate with preserved tail data gap
; - Hand-polished from tools/emit_linear_source_module.py output, then
;   intended for byte-equivalence validation.
;
; Source unit covered:
; - C1:04B5..C1:078D GetCurrentTextContextLineState

; ---------------------------------------------------------------------------
; External contracts used by this module

C08FF7_ResolveIndexedPointerOffset = $C08FF7
C09032_MultiplyWords               = $C09032
C11383_ClearActiveTextEntryChain   = $1383
C3E4EF_AllocateWindowDescriptor    = $C3E4EF
C44E4D_ReleaseNonBlankTextTileWord = $C44E4D
C45E96_ResetGlyphScratchAndAdvanceUploadCursor = $C45E96
C07C5B_RefreshWindowStateAfterDescriptorBind   = $C07C5B

ActiveWindowDescriptorHead = $88E0
ActiveWindowDescriptorTail = $88E2
ActiveWindowFocus          = $8958
WindowDescriptorIndexTable = $88E4
WindowDescriptorSize       = $0052
WindowDescriptorTable      = $8650
WindowCursorColumnField    = $865E
WindowCursorLineField      = $8660
WindowDefinitionTableLo    = $E250
WindowDefinitionTableBank  = $00C3
WindowAssociatedIndexTable = $894E
WindowNeedsRedrawFlag      = $9623
BlankTileWord              = $0040

NoActiveWindow = $FFFF

; ---------------------------------------------------------------------------
; C1:04B5

C104B5_GetCurrentTextContextLineState:
    rep #$31
    lda ActiveWindowFocus
    cmp.w #NoActiveWindow
    bne C104C4_ReadActiveWindowCursorColumn

    lda.w #$0000
    bra C104D7_ReturnActiveWindowCursorColumn

C104C4_ReadActiveWindowCursorColumn:
    lda ActiveWindowFocus
    asl A
    tax
    lda WindowDescriptorIndexTable,X
    ldy.w #WindowDescriptorSize
    jsl C08FF7_ResolveIndexedPointerOffset
    tax
    lda WindowCursorColumnField,X

C104D7_ReturnActiveWindowCursorColumn:
    rts

; ---------------------------------------------------------------------------
; C1:04D8

C104D8_GetCurrentTextContextRowState:
    rep #$31
    lda ActiveWindowFocus
    asl A
    tax
    lda WindowDescriptorIndexTable,X
    ldy.w #WindowDescriptorSize
    jsl C08FF7_ResolveIndexedPointerOffset
    tax
    lda WindowCursorLineField,X
    rts

; ---------------------------------------------------------------------------
; C1:04EE

C104EE_CreateOrBindWindowDescriptorAndContext:
    rep #$31
    phd
    pha
    tdc
    adc.w #$FFEA
    tcd
    pla
    tay
    sty $14
    tya
    asl A
    clc
    adc.w #WindowDescriptorIndexTable
    tax
    stx $12
    lda $0000,X
    cmp.w #NoActiveWindow
    beq C10528_AllocateWindowDescriptorForBinding

    sty ActiveWindowFocus
    jsr C11383_ClearActiveTextEntryChain
    ldx $12
    lda $0000,X
    ldy.w #WindowDescriptorSize
    jsl C08FF7_ResolveIndexedPointerOffset
    clc
    adc.w #WindowDescriptorTable
    tax
    stx $10
    jmp.w C10644_InitializeBoundWindowDescriptorState

C10528_AllocateWindowDescriptorForBinding:
    jsl C3E4EF_AllocateWindowDescriptor
    sta $0E
    cmp.w #NoActiveWindow
    bne C10536_ResolveAllocatedWindowDescriptor

    jmp.w C1078B_ReturnCreateOrBindWindowDescriptor

C10536_ResolveAllocatedWindowDescriptor:
    ldy.w #WindowDescriptorSize
    jsl C08FF7_ResolveIndexedPointerOffset
    clc
    adc.w #WindowDescriptorTable
    tax
    stx $10
    ldy $14
    cpy.w #$000A
    bne C10585_LinkRegularWindowDescriptor

    lda ActiveWindowDescriptorHead
    cmp.w #NoActiveWindow
    bne C10560_LinkSpecialWindowAfterHead

    lda.w #NoActiveWindow
    sta $0002,X
    lda $0E
    sta ActiveWindowDescriptorTail
    bra C10578_InstallSpecialWindowAsHead

C10560_LinkSpecialWindowAfterHead:
    lda ActiveWindowDescriptorHead
    ldy.w #WindowDescriptorSize
    jsl C08FF7_ResolveIndexedPointerOffset
    tax
    lda $0E
    sta WindowDescriptorTable,X
    lda ActiveWindowDescriptorHead
    ldx $10
    sta $0002,X

C10578_InstallSpecialWindowAsHead:
    lda.w #NoActiveWindow
    sta $0000,X
    lda $0E
    sta ActiveWindowDescriptorHead
    bra C105BB_RecordWindowLogicalSlotAndMapping

C10585_LinkRegularWindowDescriptor:
    lda ActiveWindowDescriptorHead
    cmp.w #NoActiveWindow
    bne C1059A_LinkRegularWindowAfterTail

    lda.w #NoActiveWindow
    sta $0000,X
    lda $0E
    sta ActiveWindowDescriptorHead
    bra C105B0_InstallRegularWindowAsTail

C1059A_LinkRegularWindowAfterTail:
    lda ActiveWindowDescriptorTail
    sta $0000,X
    lda ActiveWindowDescriptorTail
    ldy.w #WindowDescriptorSize
    jsl C08FF7_ResolveIndexedPointerOffset
    tax
    lda $0E
    sta WindowDescriptorTable + 2,X

C105B0_InstallRegularWindowAsTail:
    sta ActiveWindowDescriptorTail
    lda.w #NoActiveWindow
    ldx $10
    sta $0002,X

C105BB_RecordWindowLogicalSlotAndMapping:
    ldy $14
    tya
    sta $0004,X
    tya
    asl A
    tax
    lda $0E
    sta WindowDescriptorIndexTable,X
    lda.w #WindowDefinitionTableLo
    sta $06
    lda.w #WindowDefinitionTableBank
    sta $08
    tya
    asl A
    asl A
    asl A
    sta $02
    ldx $06
    stx $0A
    ldx $08
    stx $0C
    clc
    adc $0A
    sta $0A
    lda [$0A]
    ldx $10
    sta $0006,X
    lda $02
    inc A
    inc A
    ldy $06
    sty $0A
    ldy $08
    sty $0C
    clc
    adc $0A
    sta $0A
    lda [$0A]
    sta $0008,X
    lda $02
    inc A
    inc A
    inc A
    inc A
    ldy $06
    sty $0A
    ldy $08
    sty $0C
    clc
    adc $0A
    sta $0A
    lda [$0A]
    dec A
    dec A
    sta $000A,X
    lda $02
    clc
    adc.w #$0006
    clc
    adc $06
    sta $06
    lda [$06]
    dec A
    dec A
    sta $000C,X
    ldy.w #$03F0
    lda $0E
    jsl C09032_MultiplyWords
    clc
    adc.w #$5E7E
    sta $0035,X
    ldy $14
    sty ActiveWindowFocus

C10644_InitializeBoundWindowDescriptorState:
    jsr $0301
    sta $12
    ldx $10
    stz $0010,X
    stz $000E,X
    sep #$20
    lda.b #$80
    sta $0012,X
    rep #$20
    stz $0013,X
    stz $0015,X
    lda $12
    clc
    adc.w #$0017
    tay
    lda $0000,Y
    sta $06
    lda $0002,Y
    sta $08
    txa
    clc
    adc.w #$0017
    tay
    lda $06
    sta $0000,Y
    lda $08
    sta $0002,Y
    lda $12
    clc
    adc.w #$001B
    tay
    lda $0000,Y
    sta $06
    lda $0002,Y
    sta $08
    txa
    clc
    adc.w #$001B
    tay
    lda $06
    sta $0000,Y
    lda $08
    sta $0002,Y
    lda $12
    clc
    adc.w #$0021
    tay
    lda $0000,Y
    sta $06
    lda $0002,Y
    sta $08
    txa
    clc
    adc.w #$0021
    tay
    lda $06
    sta $0000,Y
    lda $08
    sta $0002,Y
    lda $12
    clc
    adc.w #$0025
    tay
    lda $0000,Y
    sta $06
    lda $0002,Y
    sta $08
    txa
    clc
    adc.w #$0025
    tay
    lda $06
    sta $0000,Y
    lda $08
    sta $0002,Y
    lda $12
    tax
    lda $001F,X
    ldx $10
    sta $001F,X
    lda $12
    tax
    lda $0029,X
    ldx $10
    sta $0029,X
    lda.w #NoActiveWindow
    sta $002F,X
    sta $002D,X
    sta $002B,X
    lda.w #$0001
    sta $0031,X
    sta $0033,X
    lda.w #$0000
    sta $06
    lda.w #$0000
    sta $08
    txa
    clc
    adc.w #$0037
    tay
    lda $06
    sta $0000,Y
    lda $08
    sta $0002,Y
    ldy $0035,X
    sty $0E
    ldy $000C,X
    lda $000A,X
    jsl C09032_MultiplyWords
    sta $02
    bra C10758_TestWindowTileClearCount

C1073C_ClearNextWindowTileWord:
    ldy $0E
    lda $0000,Y
    beq C10747_WriteBlankWindowTileWord

    jsl C44E4D_ReleaseNonBlankTextTileWord

C10747_WriteBlankWindowTileWord:
    lda.w #BlankTileWord
    ldy $0E
    sta $0000,Y
    iny
    iny
    sty $0E
    lda $02
    dec A
    sta $02

C10758_TestWindowTileClearCount:
    lda $02
    bne C1073C_ClearNextWindowTileWord

    ldx $10
    lda $003B,X
    and.w #$00FF
    beq C10772_ClearWindowAssociationBytes

    and.w #$00FF
    dec A
    asl A
    tax
    lda.w #NoActiveWindow
    sta WindowAssociatedIndexTable,X

C10772_ClearWindowAssociationBytes:
    ldx $10
    sep #$20
    stz $003C,X
    stz $003B,X
    jsl C45E96_ResetGlyphScratchAndAdvanceUploadCursor
    sep #$20
    lda.b #$01
    sta WindowNeedsRedrawFlag
    jsl C07C5B_RefreshWindowStateAfterDescriptorBind

C1078B_ReturnCreateOrBindWindowDescriptor:
    pld
    rts

; ---------------------------------------------------------------------------
; C1:078D

C1078D_GetCurrentTextContextLineState_End:
