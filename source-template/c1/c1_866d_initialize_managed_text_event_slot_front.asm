; EarthBound C1 managed text-event slot initializer.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Hand-polished from tools/emit_linear_source_module.py output, then
;   intended for byte-equivalence validation.
;
; Source unit covered:
; - C1:866D..C1:869D InitializeManagedTextEventSlotFront

ManagedTextEventSlot   = $0E
StagedEventPointerLo   = $06
StagedEventPointerHi   = $08
CallerEventPointerLo   = $1E
CallerEventPointerHi   = $20

; ---------------------------------------------------------------------------
; C1:866D

C1866D_InitializeManagedTextEventSlotFront:
    rep #$31
    phd
    pha
    tdc
    adc.w #$FFF0
    tcd
    pla
    sta ManagedTextEventSlot
    lda CallerEventPointerLo
    sta StagedEventPointerLo
    lda CallerEventPointerHi
    sta StagedEventPointerHi
    lda ManagedTextEventSlot
    bne C1868A_InitializeManagedTextEventSlot

    lda.w #$0000
    bra C1869B_ReturnManagedTextEventSlot

C1868A_InitializeManagedTextEventSlot:
    tax
    stz $0004,X
    tay
    lda StagedEventPointerLo
    sta $0000,Y
    lda StagedEventPointerHi
    sta $0002,Y
    lda ManagedTextEventSlot

C1869B_ReturnManagedTextEventSlot:
    pld
    rts
