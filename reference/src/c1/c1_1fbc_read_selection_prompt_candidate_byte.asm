; EarthBound C1 selection-prompt candidate table reader.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Hand-polished from tools/emit_linear_source_module.py output, then
;   intended for byte-equivalence validation.
;
; Source unit covered:
; - C1:1FBC..C1:1FD4 ReadSelectionPromptCandidateByte

; ---------------------------------------------------------------------------
; External contracts used by this module
; - Input A selects candidate list 0/1 and Y selects candidate index.
; - Returns a zero-extended byte from $AD5A or $AD6A.

PrimarySelectionPromptCandidateTable   = $AD5A
SecondarySelectionPromptCandidateTable = $AD6A

; ---------------------------------------------------------------------------
; C1:1FBC

C11FBC_ReadSelectionPromptCandidateByte:
    rep #$31
    txy
    tax
    bne C11FC9_ReadSecondarySelectionPromptCandidateByte

    sep #$20
    lda PrimarySelectionPromptCandidateTable,Y
    bra C11FCE_ReturnSelectionPromptCandidateByte

C11FC9_ReadSecondarySelectionPromptCandidateByte:
    sep #$20
    lda SecondarySelectionPromptCandidateTable,Y

C11FCE_ReturnSelectionPromptCandidateByte:
    rep #$20
    and.w #$00FF
    rts
