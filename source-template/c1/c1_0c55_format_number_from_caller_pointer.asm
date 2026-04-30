; EarthBound C1 packed active-window text/number bridge helpers.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Hand-polished from tools/emit_linear_source_module.py output, then
;   intended for byte-equivalence validation.
;
; Source unit covered:
; - C1:0C55..C1:0D60 FormatNumberFromCallerPointer

; ---------------------------------------------------------------------------
; External contracts used by this module

C10BA1_PrintGlyphToActiveWindow              = $0BA1
C10CB6_PrintGlyphWithSoundAndDelay           = $0CB6
C10D7C_FormatDecimalDigitsTo8960             = $0D7C
C10EFC_PrintFixedString                      = $0EFC
C08FF7_ResolveIndexedPointerOffset           = $C08FF7
C0ABE0_PlaySoundEffect                       = $C0ABE0
C12DD5_TickWindowTextSystem                  = $C12DD5
C437B8_ScrollTextWindowBufferUpOneLine       = $C437B8
C438A5_SetActiveWindowDescriptorCursorFields = $C438A5
C438B1_AdvanceActiveWindowLineOrScroll       = $C438B1
C44E61_StageTextTokenGlyphRunForActiveWindow = $C44E61

CallerPointerLo       = $20
CallerPointerBank     = $22
CallerFixedStringBank = $24
StagedPointerLo       = $06
StagedPointerBank     = $08
InstallPointerLo      = $0E
InstallPointerBank    = $10
InputLengthOrGlyph    = $12
InputGlyph            = $10
DelayCounter          = $0E

ActiveWindowFocus          = $8958
ActiveRedrawWindowIndex    = $88E2
WindowDescriptorIndexTable = $88E4
WindowDescriptorSize       = $0052
WindowGlyphModeField       = $8665

InstantPrintingFlag    = $9622
WindowNeedsRedrawFlag  = $9623
TextPrintDelay         = $9625
BattleTextDisplayMode  = $964D
TextSoundMode          = $964F
NoActiveWindow         = $FFFF
SoundEffectTextBlip    = $0007
GlyphSpace             = $0020
GlyphNewlineOrControl  = $0050

; ---------------------------------------------------------------------------
; C1:0C55

C10C55_FormatNumberFromCallerPointer:
    rep #$31
    phd
    tdc
    adc.w #$FFEE
    tcd
    lda CallerPointerLo
    sta StagedPointerLo
    lda CallerPointerBank
    sta StagedPointerBank
    lda StagedPointerLo
    sta InstallPointerLo
    lda StagedPointerBank
    sta InstallPointerBank
    jsr C10D7C_FormatDecimalDigitsTo8960
    pld
    rtl

; ---------------------------------------------------------------------------
; C1:0C72

C10C72_SetActiveWindowDescriptorCursorFields:
    rep #$31
    jsl C438A5_SetActiveWindowDescriptorCursorFields
    rtl

; ---------------------------------------------------------------------------
; C1:0C79

C10C79_AdvanceActiveWindowLineOrScroll:
    rep #$31
    jsl C438B1_AdvanceActiveWindowLineOrScroll
    rtl

; ---------------------------------------------------------------------------
; C1:0C80

C10C80_PrintGlyphToActiveWindowRedirect:
    rep #$31
    jsr C10BA1_PrintGlyphToActiveWindow
    rtl

; ---------------------------------------------------------------------------
; C1:0C86

C10C86_PrintGlyphWithSoundAndDelayRedirect:
    rep #$31
    jsr C10CB6_PrintGlyphWithSoundAndDelay
    rtl

; ---------------------------------------------------------------------------
; C1:0C8C

C10C8C_PrintFixedStringFromCallerPointer:
    rep #$31
    phd
    pha
    tdc
    adc.w #$FFEC
    tcd
    pla
    sta InputLengthOrGlyph
    lda CallerPointerBank
    sta StagedPointerLo
    lda CallerFixedStringBank
    sta StagedPointerBank
    lda StagedPointerLo
    sta InstallPointerLo
    lda StagedPointerBank
    sta InstallPointerBank
    lda InputLengthOrGlyph
    jsr C10EFC_PrintFixedString
    pld
    rtl

; ---------------------------------------------------------------------------
; C1:0CAF

C10CAF_ScrollTextWindowBufferUpOneLineRedirect:
    rep #$31
    jsl C437B8_ScrollTextWindowBufferUpOneLine
    rtl

; ---------------------------------------------------------------------------
; C1:0CB6

C10CB6_PrintGlyphWithSoundAndDelay:
    rep #$31
    phd
    pha
    tdc
    adc.w #$FFEE
    tcd
    pla
    tay
    sty InputGlyph
    lda ActiveWindowFocus
    cmp.w #NoActiveWindow
    bne C10CCE_PrintGlyphWithSoundAndDelayActiveWindow

    jmp.w C10D5E_ReturnPrintGlyphWithSoundAndDelay

C10CCE_PrintGlyphWithSoundAndDelayActiveWindow:
    lda ActiveWindowFocus
    asl A
    tax
    lda WindowDescriptorIndexTable,X
    ldy.w #WindowDescriptorSize
    jsl C08FF7_ResolveIndexedPointerOffset
    tax
    lda WindowGlyphModeField,X
    ldy InputGlyph
    tyx
    jsl C44E61_StageTextTokenGlyphRunForActiveWindow
    lda ActiveWindowFocus
    asl A
    tax
    lda WindowDescriptorIndexTable,X
    cmp ActiveRedrawWindowIndex
    beq C10CFC_CheckTextSoundMode

    sep #$20
    lda.b #$01
    sta WindowNeedsRedrawFlag

C10CFC_CheckTextSoundMode:
    rep #$20
    lda TextSoundMode
    cmp.w #$0002
    bne C10D0B_CheckMutedTextSoundMode

    ldx.w #$0001
    bra C10D23_CheckWhetherToPlayTextSound

C10D0B_CheckMutedTextSoundMode:
    lda TextSoundMode
    cmp.w #$0003
    bne C10D18_CheckBattleTextSoundGate

    ldx.w #$0000
    bra C10D23_CheckWhetherToPlayTextSound

C10D18_CheckBattleTextSoundGate:
    ldx.w #$0000
    lda BattleTextDisplayMode
    bne C10D23_CheckWhetherToPlayTextSound

    ldx.w #$0001

C10D23_CheckWhetherToPlayTextSound:
    cpx.w #$0000
    beq C10D43_CheckTextPrintDelay

    lda InstantPrintingFlag
    and.w #$00FF
    bne C10D43_CheckTextPrintDelay

    ldy InputGlyph
    cpy.w #GlyphSpace
    beq C10D43_CheckTextPrintDelay

    cpy.w #GlyphNewlineOrControl
    beq C10D43_CheckTextPrintDelay

    lda.w #SoundEffectTextBlip
    jsl C0ABE0_PlaySoundEffect

C10D43_CheckTextPrintDelay:
    lda InstantPrintingFlag
    and.w #$00FF
    bne C10D5E_ReturnPrintGlyphWithSoundAndDelay

    ldx TextPrintDelay
    inx
    stx DelayCounter
    bra C10D5C_TestPrintDelayCounter

C10D53_TickPrintDelay:
    jsl C12DD5_TickWindowTextSystem
    ldx DelayCounter
    dex
    stx DelayCounter

C10D5C_TestPrintDelayCounter:
    bne C10D53_TickPrintDelay

C10D5E_ReturnPrintGlyphWithSoundAndDelay:
    pld
    rts
