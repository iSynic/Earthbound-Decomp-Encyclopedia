; EarthBound C1 decimal and fixed-string active-window helpers.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Hand-polished from tools/emit_linear_source_module.py output, then
;   intended for byte-equivalence validation.
;
; Source unit covered:
; - C1:0D7C..C1:0F40 FormatDecimalDigitsTo8960

; ---------------------------------------------------------------------------
; External contracts used by this module

C10CB6_PrintGlyphWithSoundAndDelay           = $0CB6
C08FF7_ResolveIndexedPointerOffset           = $C08FF7
C091A6_Divide32By16                          = $C091A6
C09237_PrepareDivide32By16                   = $C09237
C12BF3_PrintDebugMenuTitleWordsWithTicks     = $C12BF3
C12C36_PrintDebugMenuFixedWordGroups         = $C12C36
C43D95_StageActiveCursorGlyphVariantState    = $C43D95
C43EF8_StageCenteredStringGlyphVariantState  = $C43EF8

ActiveWindowFocus          = $8958
WindowDescriptorIndexTable = $88E4
WindowDescriptorTable      = $8650
WindowDescriptorSize       = $0052
ActiveWindowTextModeByte   = $8662
WindowDigitLayoutByte      = $0012
CenterFixedStringFlag      = $5E74

DecimalDigitBufferStart    = $8960
DecimalDigitPrintBase      = $895A
MaxPrintableDecimalLo      = $967F
MaxPrintableDecimalHi      = $FFFF
GlyphDigitBase             = $0060
NoActiveWindow             = $FFFF

ValueLo                    = $06
ValueHi                    = $08
DivisorLo                  = $0A
DivisorHi                  = $0C
DivideArgLo                = $0E
DivideArgHi                = $10
DigitCount                 = $12
WorkingValueLo             = $14
WorkingValueHi             = $16
ActiveWindowRecord         = $16
DigitReadPointer           = $12
TempValue                  = $02
GlyphVariantOffset         = $04
FixedStringPointerLo       = $06
FixedStringPointerBank     = $08
FixedStringLength          = $12

; ---------------------------------------------------------------------------
; C1:0D7C

C10D7C_FormatDecimalDigitsTo8960:
    rep #$31
    phd
    tdc
    adc.w #$FFE8
    tcd
    lda $26
    sta ValueLo
    lda $28
    sta ValueHi
    lda ValueLo
    sta WorkingValueLo
    lda ValueHi
    sta WorkingValueHi
    ldx.w #DecimalDigitBufferStart
    lda.w #$0001
    sta DigitCount
    bra C10DCD_TestDecimalDivideLoop

C10D9E_StoreNextDecimalRemainderDigit:
    jsl C09237_PrepareDivide32By16
    sep #$20
    lda ValueLo
    sta $0000,X
    dex
    rep #$20
    lda DivideArgLo
    sta DivisorLo
    lda DivideArgHi
    sta DivisorHi
    lda WorkingValueLo
    sta ValueLo
    lda WorkingValueHi
    sta ValueHi
    jsl C091A6_Divide32By16
    lda ValueLo
    sta WorkingValueLo
    lda ValueHi
    sta WorkingValueHi
    lda DigitCount
    inc A
    sta DigitCount

C10DCD_TestDecimalDivideLoop:
    lda.w #$000A
    sta DivisorLo
    lda.w #$0000
    sta DivisorHi
    lda DivisorLo
    sta DivideArgLo
    lda DivisorHi
    sta DivideArgHi
    lda ValueLo
    cmp DivisorLo
    lda ValueHi
    sbc DivisorHi
    bcs C10D9E_StoreNextDecimalRemainderDigit

    sep #$20
    lda ValueLo
    sta $0000,X
    rep #$20
    lda DigitCount
    pld
    rts

; ---------------------------------------------------------------------------
; C1:0DF6

C10DF6_PrintDecimalValueFromCallerPointer:
    rep #$31
    phd
    tdc
    adc.w #$FFE8
    tcd
    lda $26
    sta DivisorLo
    lda $28
    sta DivisorHi
    lda ActiveWindowFocus
    cmp.w #NoActiveWindow
    bne C10E11_PrintDecimalWithActiveWindow

    jmp.w C10EB2_ReturnPrintDecimalValueFromCallerPointer

C10E11_PrintDecimalWithActiveWindow:
    lda.w #MaxPrintableDecimalLo
    sta ValueLo
    lda.w #MaxPrintableDecimalHi
    sta ValueHi
    lda ValueLo
    cmp DivisorLo
    lda ValueHi
    sbc DivisorHi
    bcs C10E2D_ResolveDecimalPrintWindow

    lda ValueLo
    sta DivisorLo
    lda ValueHi
    sta DivisorHi

C10E2D_ResolveDecimalPrintWindow:
    lda ActiveWindowFocus
    asl A
    tax
    lda WindowDescriptorIndexTable,X
    ldy.w #WindowDescriptorSize
    jsl C08FF7_ResolveIndexedPointerOffset
    clc
    adc.w #WindowDescriptorTable
    sta ActiveWindowRecord
    lda DivisorLo
    sta ValueLo
    lda DivisorHi
    sta ValueHi
    lda ValueLo
    sta DivideArgLo
    lda ValueHi
    sta DivideArgHi
    jsr.w C10D7C_FormatDecimalDigitsTo8960
    tax
    stx WorkingValueLo
    stx TempValue
    lda.w #$0007
    sec
    sbc TempValue
    clc
    adc.w #DecimalDigitPrintBase
    tay
    sty DigitReadPointer
    lda ActiveWindowRecord
    tax
    lda WindowDigitLayoutByte,X
    and.w #$00FF
    sta ActiveWindowRecord
    and.w #$0080
    bne C10EAE_TestDecimalDigitsRemaining

    lda ActiveWindowRecord
    and.w #$000F
    inc A
    ldx WorkingValueLo
    stx TempValue
    cmp TempValue
    bcs C10E86_UseComputedDecimalGlyphVariantOffset

    txa

C10E86_UseComputedDecimalGlyphVariantOffset:
    stx TempValue
    sec
    sbc TempValue
    sta GlyphVariantOffset
    asl A
    adc GlyphVariantOffset
    asl A
    jsl C43D95_StageActiveCursorGlyphVariantState
    bra C10EAE_TestDecimalDigitsRemaining

C10E97_PrintNextDecimalDigit:
    ldy DigitReadPointer
    lda $0000,Y
    and.w #$00FF
    clc
    adc.w #GlyphDigitBase
    iny
    sty DigitReadPointer
    jsr C10CB6_PrintGlyphWithSoundAndDelay
    ldx WorkingValueLo
    dex
    stx WorkingValueLo

C10EAE_TestDecimalDigitsRemaining:
    ldx WorkingValueLo
    bne C10E97_PrintNextDecimalDigit

C10EB2_ReturnPrintDecimalValueFromCallerPointer:
    pld
    rts

; ---------------------------------------------------------------------------
; C1:0EB4

C10EB4_SetActiveWindowTextModeByte:
    rep #$31
    phd
    pha
    tdc
    adc.w #$FFF0
    tcd
    pla
    sta DivideArgLo
    lda ActiveWindowFocus
    cmp.w #NoActiveWindow
    beq C10EDF_ReturnSetActiveWindowTextModeByte

    lda ActiveWindowFocus
    asl A
    tax
    lda WindowDescriptorIndexTable,X
    ldy.w #WindowDescriptorSize
    jsl C08FF7_ResolveIndexedPointerOffset
    tax
    lda DivideArgLo
    sep #$20
    sta ActiveWindowTextModeByte,X

C10EDF_ReturnSetActiveWindowTextModeByte:
    rep #$20
    pld
    rts

; ---------------------------------------------------------------------------
; C1:0EE3

C10EE3_DispatchDebugMenuPrintMode:
    rep #$31
    cmp.w #$0001
    beq C10EF1_PrintDebugMenuTitleWords

    cmp.w #$0002
    beq C10EF7_PrintDebugMenuFixedWordGroups

    bra C10EFB_ReturnDebugMenuPrintMode

C10EF1_PrintDebugMenuTitleWords:
    jsl C12BF3_PrintDebugMenuTitleWordsWithTicks
    bra C10EFB_ReturnDebugMenuPrintMode

C10EF7_PrintDebugMenuFixedWordGroups:
    jsl C12C36_PrintDebugMenuFixedWordGroups

C10EFB_ReturnDebugMenuPrintMode:
    rts

; ---------------------------------------------------------------------------
; C1:0EFC

C10EFC_PrintFixedString:
    rep #$31
    phd
    pha
    tdc
    adc.w #$FFEC
    tcd
    pla
    tax
    stx FixedStringLength
    lda $22
    sta FixedStringPointerLo
    lda $24
    sta FixedStringPointerBank
    lda CenterFixedStringFlag
    and.w #$00FF
    beq C10F33_TestFixedStringSourceByte

    lda FixedStringPointerLo
    sta DivideArgLo
    lda FixedStringPointerBank
    sta DivideArgHi
    txa
    jsl C43EF8_StageCenteredStringGlyphVariantState
    bra C10F33_TestFixedStringSourceByte

C10F28_PrintNextFixedStringGlyph:
    dex
    stx FixedStringLength
    and.w #$00FF
    inc FixedStringPointerLo
    jsr C10CB6_PrintGlyphWithSoundAndDelay

C10F33_TestFixedStringSourceByte:
    lda [FixedStringPointerLo]
    and.w #$00FF
    beq C10F3E_ReturnPrintFixedString

    ldx FixedStringLength
    bne C10F28_PrintNextFixedStringGlyph

C10F3E_ReturnPrintFixedString:
    pld
    rts
