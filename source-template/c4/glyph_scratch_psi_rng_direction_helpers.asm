; EarthBound C4 glyph scratch, PSI, RNG, and direction helper bridge.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Generated from state-aware linear ROM decodes, then tightened into a
;   mixed source/data module for byte-equivalence validation.
;
; Source units covered:
; - C4:5E96..C4:5ECE ResetGlyphScratchAndAdvanceUploadCursor
; - C4:5ECE..C4:5F7B CheckPartyMemberPsiKnown
; - C4:5F7B..C4:5F96 GetRandomModuloInclusive
; - C4:5F96..C4:5FA8 DirectionMatrix data
; - C4:5FA8..C4:6028 GetDirectionToCoordinateDelta

; ---------------------------------------------------------------------------
; External contracts used by this module

C08E9A_GetRandom16                 = $C08E9A
C08FF7_ResolveIndexedPointerOffset = $C08FF7
C09231_ModUnsignedWordByIndex      = $C09231
C44E44_ResetActiveTextGlyphRun     = $C44E44
PsiLearnTableD58A50                = $D58A50

; ---------------------------------------------------------------------------
; C4:5E96

C45E96_ResetGlyphScratchAndAdvanceUploadCursor:
    rep #$31
C45E98_ResetGlyphScratchAndAdvanceUploadCursor_WaitForGlyphUploadIdle:
    lda $9E2B
    bne C45E98_ResetGlyphScratchAndAdvanceUploadCursor_WaitForGlyphUploadIdle
    ldx.w #$0000
    bra C45EAA_ResetGlyphScratchAndAdvanceUploadCursor_CheckClearLoop
C45EA2_ResetGlyphScratchAndAdvanceUploadCursor_ClearScratchByte:
    sep #$20
    lda.b #$FF
    sta $9D23,X
    inx
C45EAA_ResetGlyphScratchAndAdvanceUploadCursor_CheckClearLoop:
    cpx.w #$0020
    bcc C45EA2_ResetGlyphScratchAndAdvanceUploadCursor_ClearScratchByte
    rep #$20
    stz $9E25
    stz $9E23
    ldx $9E27
    inx
    stx $9E27
    cpx.w #$0030
    bcc C45EC6_ResetGlyphScratchAndAdvanceUploadCursor_FinishReset
    stz $9E27
C45EC6_ResetGlyphScratchAndAdvanceUploadCursor_FinishReset:
    stz $9E29
    jsl C44E44_ResetActiveTextGlyphRun
    rtl

; ---------------------------------------------------------------------------
; C4:5ECE

C45ECE_CheckPartyMemberPsiKnown:
    rep #$31
    phd
    pha
    tdc
    adc.w #$FFED
    tcd
    pla
    sta $11
    cmp.w #$0001
    beq C45EEB_CheckPartyMemberPsiKnown_CheckLevel1PsiId
    cmp.w #$0002
    beq C45F08_CheckPartyMemberPsiKnown_CheckLevel2PsiId
    cmp.w #$0004
    beq C45F25_CheckPartyMemberPsiKnown_CheckLevel4PsiId
    bra C45F40_CheckPartyMemberPsiKnown_CompareKnownPsiThreshold
C45EEB_CheckPartyMemberPsiKnown_CheckLevel1PsiId:
    txa
    sta $04
    asl A
    adc $04
    asl A
    adc $04
    asl A
    adc $04
    clc
    adc.w #$0006
    tax
    sep #$20
    lda PsiLearnTableD58A50,X
    sta $00
    sta $10
    bra C45F40_CheckPartyMemberPsiKnown_CompareKnownPsiThreshold
C45F08_CheckPartyMemberPsiKnown_CheckLevel2PsiId:
    txa
    sta $04
    asl A
    adc $04
    asl A
    adc $04
    asl A
    adc $04
    clc
    adc.w #$0007
    tax
    sep #$20
    lda PsiLearnTableD58A50,X
    sta $00
    sta $10
    bra C45F40_CheckPartyMemberPsiKnown_CompareKnownPsiThreshold
C45F25_CheckPartyMemberPsiKnown_CheckLevel4PsiId:
    txa
    sta $04
    asl A
    adc $04
    asl A
    adc $04
    asl A
    adc $04
    clc
    adc.w #$0008
    tax
    sep #$20
    lda PsiLearnTableD58A50,X
    sta $00
    sta $10
C45F40_CheckPartyMemberPsiKnown_CompareKnownPsiThreshold:
    sep #$20
    lda $10
    sta $00
    rep #$20
    lda $00
    and.w #$00FF
    beq C45F76_CheckPartyMemberPsiKnown_ReturnNotKnown
    ldx.w #$0000
    stx $0E
    lda $11
    dec A
    ldy.w #$005F
    jsl C08FF7_ResolveIndexedPointerOffset
    tax
    sep #$20
    lda $00
    cmp $99D3,X
    beq C45F6A_CheckPartyMemberPsiKnown_MarkKnown
    bcs C45F6F_CheckPartyMemberPsiKnown_ReturnFlag
C45F6A_CheckPartyMemberPsiKnown_MarkKnown:
    ldx.w #$0001
    stx $0E
C45F6F_CheckPartyMemberPsiKnown_ReturnFlag:
    ldx $0E
    rep #$20
    txa
    bra C45F79_CheckPartyMemberPsiKnown_Done
C45F76_CheckPartyMemberPsiKnown_ReturnNotKnown:
    lda.w #$0000
C45F79_CheckPartyMemberPsiKnown_Done:
    pld
    rtl

; ---------------------------------------------------------------------------
; C4:5F7B

C45F7B_GetRandomModuloInclusive:
    rep #$31
    phd
    pha
    tdc
    adc.w #$FFF0
    tcd
    pla
    tax
    stx $0E
    jsl C08E9A_GetRandom16
    ldx $0E
    txy
    iny
    jsl C09231_ModUnsignedWordByIndex
    pld
    rtl

; ---------------------------------------------------------------------------
; C4:5FA8


; ---------------------------------------------------------------------------
; C4:5F96

C45F96_DirectionMatrix:
    ; data bytes: C4:5F96..C4:5FA8
    db $07,$00,$00,$00,$01,$00,$06,$00,$00,$00,$02,$00,$05,$00,$04,$00
    db $03,$00

C45FA8_GetDirectionToCoordinateDelta:
    rep #$31
    phd
    pha
    tdc
    adc.w #$FFEE
    tcd
    pla
    stx $04
    sta $02
    ldx $20
    txa
    sta $10
    tya
    sec
    sbc $02
    tax
    lda $10
    sec
    sbc $04
    sta $0E
    stx $02
    lda.w #$0000
    clc
    sbc $02
    bvc C45FD5_GetDirectionToCoordinateDelta_CheckHorizontalSign
    bpl C45FDC_GetDirectionToCoordinateDelta_ResolveHorizontalNonnegativeColumn
    bra C45FD7_GetDirectionToCoordinateDelta_UseHorizontalNegativeColumn
C45FD5_GetDirectionToCoordinateDelta_CheckHorizontalSign:
    bmi C45FDC_GetDirectionToCoordinateDelta_ResolveHorizontalNonnegativeColumn
C45FD7_GetDirectionToCoordinateDelta_UseHorizontalNegativeColumn:
    ldx.w #$0000
    bra C45FE9_GetDirectionToCoordinateDelta_ResolveVerticalRow
C45FDC_GetDirectionToCoordinateDelta_ResolveHorizontalNonnegativeColumn:
    cpx.w #$0000
    bne C45FE6_GetDirectionToCoordinateDelta_UseHorizontalPositiveColumn
    ldx.w #$0001
    bra C45FE9_GetDirectionToCoordinateDelta_ResolveVerticalRow
C45FE6_GetDirectionToCoordinateDelta_UseHorizontalPositiveColumn:
    ldx.w #$0002
C45FE9_GetDirectionToCoordinateDelta_ResolveVerticalRow:
    lda $0E
    sta $02
    lda.w #$0000
    clc
    sbc $02
    bvc C45FF9_GetDirectionToCoordinateDelta_CheckVerticalNonnegative
    bpl C46002_GetDirectionToCoordinateDelta_ResolveVerticalNonnegativeRow
    bra C45FFB_GetDirectionToCoordinateDelta_UseVerticalNegativeRow
C45FF9_GetDirectionToCoordinateDelta_CheckVerticalNonnegative:
    bmi C46002_GetDirectionToCoordinateDelta_ResolveVerticalNonnegativeRow
C45FFB_GetDirectionToCoordinateDelta_UseVerticalNegativeRow:
    lda.w #$0000
    sta $10
    bra C46012_GetDirectionToCoordinateDelta_FetchDirection
C46002_GetDirectionToCoordinateDelta_ResolveVerticalNonnegativeRow:
    lda $0E
    bne C4600D_GetDirectionToCoordinateDelta_UseVerticalPositiveRow
    lda.w #$0001
    sta $10
    bra C46012_GetDirectionToCoordinateDelta_FetchDirection
C4600D_GetDirectionToCoordinateDelta_UseVerticalPositiveRow:
    lda.w #$0002
    sta $10
C46012_GetDirectionToCoordinateDelta_FetchDirection:
    txa
    asl A
    sta $02
    lda $10
    sta $04
    asl A
    adc $04
    asl A
    clc
    adc $02
    tax
    lda.l $C45F96,X
    pld
    rtl
