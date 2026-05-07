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

INCREMENT_SECONDARY_MEMORY:
C1042E_IncrementCurrentTextContextWorkmem = INCREMENT_SECONDARY_MEMORY
    rep #$31
    jsr GET_ACTIVE_WINDOW_ADDRESS
    clc
    adc.w #ContextWorkmemOffset
    tax
    lda $0000,X
    lda $0000,X
    inc A
    sta $0000,X
    rts

; ---------------------------------------------------------------------------
; C1:0443

C10443_SetCurrentTextContextWorkmem:
    rep #$31
    phd
    pha
    tdc
    adc.w #$FFF0
    tcd
    pla
    tay
    sty SavedWorkmemValue
    jsr GET_ACTIVE_WINDOW_ADDRESS
    tax
    ldy SavedWorkmemValue
    tya
    sta ContextWorkmemOffset,X
    tya
    pld
    rts
