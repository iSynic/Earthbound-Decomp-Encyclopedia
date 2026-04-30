; EarthBound C1 current text-context workmem helpers.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Hand-polished from tools/emit_linear_source_module.py output, then
;   intended for byte-equivalence validation.
;
; Source unit covered:
; - C1:042E..C1:045D IncrementCurrentTextContextWorkmem

; ---------------------------------------------------------------------------
; External contracts used by this module

C10301_GetActiveInteractionContextRecord = $0301

ContextWorkmemOffset = $001F
SavedWorkmemValue    = $0E

; ---------------------------------------------------------------------------
; C1:042E

C1042E_IncrementCurrentTextContextWorkmem:
    rep #$31
    jsr C10301_GetActiveInteractionContextRecord
    clc
    adc.w #ContextWorkmemOffset
    tax
    lda $0000,X
    lda $0000,X
    inc A
    sta $0000,X
    rts

; ---------------------------------------------------------------------------
; C1:0450

C10450_SetCurrentTextContextWorkmem:
    rep #$31
    phd
    pha
    tdc
    adc.w #$FFF0
    tcd
    pla
    tay
    sty SavedWorkmemValue
    jsr C10301_GetActiveInteractionContextRecord
    tax
    ldy SavedWorkmemValue
    tya
    sta ContextWorkmemOffset,X
    tya
    pld
    rts
