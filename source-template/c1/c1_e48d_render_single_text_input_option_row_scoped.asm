; EarthBound C1 scoped text-input option row renderer.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Hand-polished from tools/emit_linear_source_module.py output, then
;   intended for byte-equivalence validation.
;
; Source unit covered:
; - C1:E48D..C1:E4BE RenderSingleTextInputOptionRowScoped

C1007E_SetWindowFocus                    = $007E
C3E4D4_SetInstantPrinting                = $C3E4D4
C442AC_RenderSingleTextInputOptionRow    = $C442AC

SavedRowIndex = $0E
SavedColumn   = $10
OptionIndex   = $02
TextInputOptionWindowFocus = $001C

; ---------------------------------------------------------------------------
; C1:E48D

C1E48D_RenderSingleTextInputOptionRowScoped:
    rep #$31
    phd
    pha
    tdc
    adc.w #$FFEE
    tcd
    pla
    sty SavedColumn
    stx SavedRowIndex
    sta OptionIndex
    jsl C3E4D4_SetInstantPrinting
    lda OptionIndex
    jsr C1007E_SetWindowFocus
    ldy SavedColumn
    ldx SavedRowIndex
    lda OptionIndex
    jsl C442AC_RenderSingleTextInputOptionRow
    tax
    stx SavedRowIndex
    lda.w #TextInputOptionWindowFocus
    jsr C1007E_SetWindowFocus
    ldx SavedRowIndex
    txa
    pld
    rts
