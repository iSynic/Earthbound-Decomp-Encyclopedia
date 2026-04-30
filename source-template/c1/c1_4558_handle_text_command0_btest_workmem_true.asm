; EarthBound C1 text command 0B workmem equality predicate.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Hand-polished from tools/emit_linear_source_module.py output, then
;   intended for byte-equivalence validation.
;
; Source unit covered:
; - C1:4558..C1:4591 HandleTextCommand0BTestWorkmemTrue

C1040A_LoadPrimaryInteractionContextPointer   = $040A
C1045D_InstallPrimaryInteractionContextPointer = $045D

ExpectedWorkmemValue = $02
PredicateResultLo    = $06
PredicateResultHi    = $08
PredicateResult      = $12
StagedPointerLo      = $0E
StagedPointerHi      = $10

; ---------------------------------------------------------------------------
; C1:4558

C14558_HandleTextCommand0BTestWorkmemTrue:
    rep #$31
    phd
    pha
    tdc
    adc.w #$FFEC
    tcd
    pla
    stx ExpectedWorkmemValue
    lda.w #$0000
    sta PredicateResult
    jsr C1040A_LoadPrimaryInteractionContextPointer
    lda PredicateResultLo
    cmp ExpectedWorkmemValue
    bne C14577_StageTextCommand0BPredicateResult

    lda.w #$0001
    sta PredicateResult

C14577_StageTextCommand0BPredicateResult:
    lda PredicateResult
    sta PredicateResultLo
    stz PredicateResultHi
    bpl C14581_InstallTextCommand0BPredicateResult

    dec PredicateResultHi

C14581_InstallTextCommand0BPredicateResult:
    lda PredicateResultLo
    sta StagedPointerLo
    lda PredicateResultHi
    sta StagedPointerHi
    jsr C1045D_InstallPrimaryInteractionContextPointer
    lda.w #$0000
    pld
    rts
