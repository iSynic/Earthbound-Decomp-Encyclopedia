; EarthBound C1 front-interaction result class reader.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Hand-shaped from the ROM decode because the terminal no-result branch
;   switches to 8-bit accumulator mode before loading the zero return value.
;
; Source units covered:
; - C1:AD42..C1:AD7D GetFrontInteractionResultClass

; ---------------------------------------------------------------------------
; External contracts used by this module

C04279_ResolveInteractableAlongFacingTarget = $C04279
FrontInteractionResult = $5D62
LocalResult = $04
NpcConfigTable = $CF8985

; ---------------------------------------------------------------------------
; C1:AD42

C1AD42_GetFrontInteractionResultClass:
    rep #$31
    phd
    tdc
    adc.w #$FFF2
    tcd
    jsl C04279_ResolveInteractableAlongFacingTarget
    lda FrontInteractionResult
    beq C1AD63_NoInteractionResult
    lda FrontInteractionResult
    cmp.w #$FFFF
    beq C1AD63_NoInteractionResult
    lda FrontInteractionResult
    cmp.w #$FFFE
    bne C1AD69_LoadInteractionResultClass

C1AD63_NoInteractionResult:
    sep #$20
    lda.b #$00
    bra C1AD7B_Return

C1AD69_LoadInteractionResultClass:
    lda FrontInteractionResult
    sta LocalResult
    asl A
    asl A
    asl A
    asl A
    adc LocalResult
    tax
    sep #$20
    lda.l NpcConfigTable,X

C1AD7B_Return:
    pld
    rts
