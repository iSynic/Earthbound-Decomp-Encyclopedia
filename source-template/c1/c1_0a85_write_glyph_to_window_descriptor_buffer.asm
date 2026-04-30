; EarthBound C1 descriptor-backed active-window glyph writer.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Hand-polished from tools/emit_linear_source_module.py output, then
;   intended for byte-equivalence validation.
;
; Source unit covered:
; - C1:0A85..C1:0BA1 WriteGlyphToWindowDescriptorBuffer

; ---------------------------------------------------------------------------
; External contracts used by this module

C08FF7_ResolveIndexedPointerOffset     = $C08FF7
C09032_DivideUnsignedWordByIndex       = $C09032
C437B8_ScrollTextWindowBufferUpOneLine = $C437B8

WindowDescriptorIndexTable = $88E4
WindowDescriptorSize       = $0052
WindowWidthField           = $865A
WindowHeightField          = $865C
WindowCursorXField         = $865E
WindowCursorYField         = $8660
WindowTileBufferPointer    = $8685
BattleTextDisplayMode      = $964D
NoWindowDescriptor         = $FFFF

GlyphWord                  = $16
WindowFocus                = $14
DescriptorIndex            = $12
CursorX                    = $10
CursorY                    = $04
TileWritePointer           = $0E
AuxiliaryGlyphBits         = $18
Scratch                    = $02

; ---------------------------------------------------------------------------
; C1:0A85

C10A85_WriteGlyphToWindowDescriptorBuffer:
    rep #$31
    phd
    pha
    tdc
    adc.w #$FFE6
    tcd
    pla
    sty AuxiliaryGlyphBits
    stx Scratch
    stx GlyphWord
    sta WindowFocus
    asl A
    tax
    lda WindowDescriptorIndexTable,X
    sta DescriptorIndex
    cmp.w #NoWindowDescriptor
    bne C10AA6_ResolveDescriptorForGlyphWrite

    jmp.w C10B9F_ReturnWriteGlyphToWindowDescriptorBuffer

C10AA6_ResolveDescriptorForGlyphWrite:
    lda DescriptorIndex
    ldy.w #WindowDescriptorSize
    jsl C08FF7_ResolveIndexedPointerOffset
    tax
    ldy WindowCursorXField,X
    sty CursorX
    lda WindowCursorYField,X
    sta CursorY
    tya
    cmp WindowWidthField,X
    bne C10ADC_CheckDisplayModeShortcuts

    lda WindowHeightField,X
    lsr A
    dec A
    sta Scratch
    lda CursorY
    cmp Scratch
    beq C10AD1_ScrollWindowBeforeGlyphWrite

    inc CursorY
    bra C10AD7_ResetCursorXForNextLine

C10AD1_ScrollWindowBeforeGlyphWrite:
    lda WindowFocus
    jsl C437B8_ScrollTextWindowBufferUpOneLine

C10AD7_ResetCursorXForNextLine:
    ldy.w #$0000
    sty CursorX

C10ADC_CheckDisplayModeShortcuts:
    lda BattleTextDisplayMode
    beq C10B0D_ComputeGlyphTilePointer
    cpy.w #$0000
    bne C10B0D_ComputeGlyphTilePointer
    lda GlyphWord
    sta Scratch
    cmp.w #$0020
    beq C10AF6_HandleModeShortcutGlyph
    lda Scratch
    cmp.w #$0040
    bne C10B0D_ComputeGlyphTilePointer

C10AF6_HandleModeShortcutGlyph:
    lda BattleTextDisplayMode
    cmp.w #$0001
    bne C10B01_CheckModeTwoShortcutGlyph

    jmp.w C10B8A_UpdateDescriptorCursorAfterGlyphWrite

C10B01_CheckModeTwoShortcutGlyph:
    cmp.w #$0002
    bne C10B0D_ComputeGlyphTilePointer
    lda.w #$0020
    sta Scratch
    sta GlyphWord

C10B0D_ComputeGlyphTilePointer:
    lda DescriptorIndex
    ldy.w #WindowDescriptorSize
    jsl C08FF7_ResolveIndexedPointerOffset
    tax
    ldy CursorX
    tya
    asl A
    sta Scratch
    ldy WindowWidthField,X
    lda CursorY
    jsl C09032_DivideUnsignedWordByIndex
    asl A
    asl A
    clc
    adc WindowTileBufferPointer,X
    clc
    adc Scratch
    sta TileWritePointer
    lda GlyphWord
    sta Scratch
    cmp.w #$0022
    bne C10B3F_UseCallerAuxiliaryGlyphBits

    ldx.w #$0C00
    bra C10B41_ComposeGlyphTileWord

C10B3F_UseCallerAuxiliaryGlyphBits:
    ldx AuxiliaryGlyphBits

C10B41_ComposeGlyphTileWord:
    lda Scratch
    and.w #$000F
    pha
    lda Scratch
    and.w #$FFF0
    asl A
    ply
    sty Scratch
    clc
    adc Scratch
    stx Scratch
    clc
    adc Scratch
    sta Scratch
    sta AuxiliaryGlyphBits
    lda TileWritePointer
    tax
    lda Scratch
    sta $0000,X
    lda DescriptorIndex
    ldy.w #WindowDescriptorSize
    jsl C08FF7_ResolveIndexedPointerOffset
    tax
    lda WindowWidthField,X
    asl A
    sta Scratch
    lda TileWritePointer
    clc
    adc Scratch
    tax
    lda AuxiliaryGlyphBits
    sta Scratch
    clc
    adc.w #$0010
    sta $0000,X
    ldy CursorX
    iny
    sty CursorX

C10B8A_UpdateDescriptorCursorAfterGlyphWrite:
    lda DescriptorIndex
    ldy.w #WindowDescriptorSize
    jsl C08FF7_ResolveIndexedPointerOffset
    tax
    ldy CursorX
    tya
    sta WindowCursorXField,X
    lda CursorY
    sta WindowCursorYField,X

C10B9F_ReturnWriteGlyphToWindowDescriptorBuffer:
    pld
    rts

; ---------------------------------------------------------------------------
; C1:0BA1

C10BA1_WriteGlyphToWindowDescriptorBuffer_End:
