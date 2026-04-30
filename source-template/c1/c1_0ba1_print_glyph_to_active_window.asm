; EarthBound C1 active-window glyph and row helper bridge.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Hand-polished from tools/emit_linear_source_module.py output, then
;   intended for byte-equivalence validation.
;
; Source unit covered:
; - C1:0BA1..C1:0BFE PrintGlyphToActiveWindow

; ---------------------------------------------------------------------------
; External contracts used by this module

C1008E_CloseAndDrainAllWindows               = $008E
C10A85_WriteGlyphToWindowDescriptorBuffer    = $0A85
C08FF7_ResolveIndexedPointerOffset           = $C08FF7
C43739_ClearTextWindowRowAndDisplayObjects   = $C43739
C438A5_SetActiveWindowDescriptorCursorFields = $C438A5

ActiveWindowFocus          = $8958
WindowDescriptorIndexTable = $88E4
WindowDescriptorSize       = $0052
WindowLineStateField       = $8660
WindowGlyphAuxField        = $8663

NoActiveWindow = $FFFF
InputGlyphCode = $0E

; ---------------------------------------------------------------------------
; C1:0BA1

C10BA1_PrintGlyphToActiveWindow:
    rep #$31
    phd
    pha
    tdc
    adc.w #$FFF0
    tcd
    pla
    tax
    stx InputGlyphCode
    lda ActiveWindowFocus
    cmp.w #NoActiveWindow
    beq C10BD1_ReturnPrintGlyphToActiveWindow

    lda ActiveWindowFocus
    asl A
    tax
    lda WindowDescriptorIndexTable,X
    ldy.w #WindowDescriptorSize
    jsl C08FF7_ResolveIndexedPointerOffset
    tax
    ldy WindowGlyphAuxField,X
    ldx InputGlyphCode
    lda ActiveWindowFocus
    jsr C10A85_WriteGlyphToWindowDescriptorBuffer

C10BD1_ReturnPrintGlyphToActiveWindow:
    pld
    rts

; ---------------------------------------------------------------------------
; C1:0BD2

C10BD2_ClearActiveWindowRowAndResetCursor:
    rep #$31
    lda ActiveWindowFocus
    jsl C43739_ClearTextWindowRowAndDisplayObjects
    lda ActiveWindowFocus
    asl A
    tax
    lda WindowDescriptorIndexTable,X
    ldy.w #WindowDescriptorSize
    jsl C08FF7_ResolveIndexedPointerOffset
    tax
    lda WindowLineStateField,X
    tax
    lda.w #$0000
    jsl C438A5_SetActiveWindowDescriptorCursorFields
    rts

; ---------------------------------------------------------------------------
; C1:0BF8

C10BF8_CloseAndDrainAllWindowsRedirect:
    rep #$31
    jsr C1008E_CloseAndDrainAllWindows
    rtl
