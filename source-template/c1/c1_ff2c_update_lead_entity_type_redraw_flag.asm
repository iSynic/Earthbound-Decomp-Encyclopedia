; EarthBound C1 file-select lead entity redraw predicate.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Hand-polished from tools/emit_linear_source_module.py output, then
;   intended for byte-equivalence validation.
;
; Source unit covered:
; - C1:FF2C..C1:FF6B UpdateLeadEntityTypeRedrawFlag

ActivePartyMemberCountOrIndex = $98A4
PartyMemberSlotOrder          = $9891
EntityPointerTable            = $4DC8
FileSelectTransientState      = $B4A2

EntityTypeOffset = $000E

; ---------------------------------------------------------------------------
; C1:FF2C

C1FF2C_UpdateLeadEntityTypeRedrawFlag:
    rep #$31
    lda ActivePartyMemberCountOrIndex
    and.w #$00FF
    tax
    dex
    lda PartyMemberSlotOrder,X
    and.w #$00FF
    asl A
    tax
    lda EntityPointerTable,X
    tax
    sep #$20
    lda EntityTypeOffset,X
    ldx.w #$0000
    rep #$20
    and.w #$00FF
    cmp.w #$0001
    beq C1FF59_SetFileSelectLeadEntityRedrawFlag

    cmp.w #$0002
    bne C1FF5C_CompareFileSelectLeadEntityRedrawFlag

C1FF59_SetFileSelectLeadEntityRedrawFlag:
    ldx.w #$0001

C1FF5C_CompareFileSelectLeadEntityRedrawFlag:
    lda.w #$0000
    cpx FileSelectTransientState
    beq C1FF67_StoreFileSelectLeadEntityRedrawFlag

    lda.w #$0001

C1FF67_StoreFileSelectLeadEntityRedrawFlag:
    stx FileSelectTransientState
    rts
