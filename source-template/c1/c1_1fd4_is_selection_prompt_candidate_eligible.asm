; EarthBound C1 selection-prompt candidate eligibility predicate.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Hand-polished from tools/emit_linear_source_module.py output, then
;   intended for byte-equivalence validation.
;
; Source unit covered:
; - C1:1FD4..C1:2012 IsSelectionPromptCandidateEligible

C2FAD2_CheckSelectionCandidateState = $C2FAD2

SavedCandidateIndex = $02
SavedRowIndex       = $04
CharacterDataBase   = $D57B68

; ---------------------------------------------------------------------------
; C1:1FD4

C11FD4_IsSelectionPromptCandidateEligible:
    rep #$31
    phd
    pha
    tdc
    adc.w #$FFF2
    tcd
    pla
    stx SavedCandidateIndex
    tax
    cpx.w #$0001
    bne C1200D_ReturnSelectionPromptCandidateEligible

    tya
    sta SavedRowIndex
    asl A
    adc SavedRowIndex
    asl A
    asl A
    tax
    inx
    inx
    lda CharacterDataBase,X
    and.w #$00FF
    cmp.w #$0001
    bne C1200D_ReturnSelectionPromptCandidateEligible

    lda SavedCandidateIndex
    jsl C2FAD2_CheckSelectionCandidateState
    cmp.w #$0000
    bne C1200D_ReturnSelectionPromptCandidateEligible

    lda.w #$0000
    bra C12010_ReturnSelectionPromptCandidateEligibility

C1200D_ReturnSelectionPromptCandidateEligible:
    lda.w #$0001

C12010_ReturnSelectionPromptCandidateEligibility:
    pld
    rts
