; EarthBound C1 bounded byte-string length helper.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Hand-polished from tools/emit_linear_source_module.py output, then
;   intended for byte-equivalence validation.
;
; Source unit covered:
; - C1:17E2..C1:180D MeasureBoundedStringLength

MeasuredLength = $0E

; ---------------------------------------------------------------------------
; C1:17E2

C117E2_MeasureBoundedStringLength:
    rep #$31
    phd
    pha
    tdc
    adc.w #$FFF0
    tcd
    pla
    txy
    tax
    lda.w #$0000
    sta MeasuredLength
    bra C117FC_TestBoundedStringByte

C117F5_CountBoundedStringByte:
    lda MeasuredLength
    inc A
    sta MeasuredLength
    dey
    inx

C117FC_TestBoundedStringByte:
    lda $0000,X
    and.w #$00FF
    beq C11809_ReturnBoundedStringLength

    cpy.w #$0000
    bne C117F5_CountBoundedStringByte

C11809_ReturnBoundedStringLength:
    lda MeasuredLength
    pld
    rts
