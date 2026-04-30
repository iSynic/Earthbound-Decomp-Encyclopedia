; EarthBound C4 direction octant and target-position helpers.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Generated from state-aware linear ROM decodes, then tightened into a
;   mixed source/data module for byte-equivalence validation.
;
; Source units covered:
; - C4:6A5E..C4:6A6E PlayerDirection987fTurnBiasTable data
; - C4:6A6E..C4:6A7A MapPlayerDirection987fToTurnBias
; - C4:6A7A..C4:6A9A direction octant table data
; - C4:6A9A..C4:6B41 DirectionOctantNormalizerHelpers
; - C4:6B41..C4:6B51 RoundedAngleToWalkDirectionTable data
; - C4:6B51..C4:6C45 DirectionTargetSetterHelpers

; ---------------------------------------------------------------------------
; External contracts used by this module

C09032_DivideUnsignedWordByIndex                  = $C09032
C0915B_DivideUnsignedWordByY                      = $C0915B
C41EFF_CalculateAngleBetweenPoints                = $C41EFF
C45FA8_GetDirectionToCoordinateDelta              = $C45FA8
C46028_FindEntitySlotByCachedPoseDescriptorId     = $C46028
C4605A_FindEntitySlotByVisualTypeId               = $C4605A
C4608C_ResolveEntitySlotFromOverworldTypeRegistryCode = $C4608C
C46A5E_PlayerDirection987fTurnBiasTable           = $C46A5E
C46A7A_DirectionOctantToAltFacingQuadrantTable    = $C46A7A
C46A8A_DirectionOctantToSpriteFacingQuadrantTable = $C46A8A
C46B41_RoundedAngleToWalkDirectionTable           = $C46B41

; ---------------------------------------------------------------------------
; C4:6A6E


; ---------------------------------------------------------------------------
; C4:6A5E

C46A5E_PlayerDirection987fTurnBiasTable:
    ; data bytes: C4:6A5E..C4:6A6E
    db $01,$00,$01,$00,$01,$00,$05,$00,$05,$00,$05,$00,$05,$00,$01,$00

C46A6E_MapPlayerDirection987fToTurnBias:
    rep #$31
    lda $987F
    asl A
    tax
    lda C46A5E_PlayerDirection987fTurnBiasTable,X
    rtl

; ---------------------------------------------------------------------------
; C4:6A9A


; ---------------------------------------------------------------------------
; C4:6A7A

C46A7A_DirectionOctantToAltFacingQuadrantTable:
    ; data bytes: C4:6A7A..C4:6A8A
    db $00,$00,$02,$00,$02,$00,$02,$00,$04,$00,$06,$00,$06,$00,$06,$00

C46A8A_DirectionOctantToSpriteFacingQuadrantTable:
    ; data bytes: C4:6A8A..C4:6A9A
    db $00,$00,$00,$00,$02,$00,$04,$00,$04,$00,$04,$00,$06,$00,$00,$00

C46A9A_MapOctantToAltFacingQuadrant:
    rep #$31
    asl A
    tax
    lda C46A7A_DirectionOctantToAltFacingQuadrantTable,X
    rtl
C46AA3_MapOctantToSpriteFacingQuadrant:
    rep #$31
    asl A
    tax
    lda C46A8A_DirectionOctantToSpriteFacingQuadrantTable,X
    rtl
C46AAC_ComputeCurrentSlotSignDeltaTargetDirection:
    rep #$31
    phd
    tdc
    adc.w #$FFEC
    tcd
    lda $1A42
    asl A
    sta $12
    tax
    lda $1002,X
    sta $0E
    lda $12
    tax
    ldy $0FC6,X
    tax
    lda $0BCA,X
    tax
    stx $10
    lda $12
    tax
    lda $0B8E,X
    ldx $10
    jsl C45FA8_GetDirectionToCoordinateDelta
    pld
    rtl
C46ADB_ComputeCurrentSlotTargetDirectionOctant:
    rep #$31
    phd
    tdc
    adc.w #$FFEC
    tcd
    lda $1A42
    asl A
    sta $12
    tax
    lda $1002,X
    sta $0E
    lda $12
    tax
    ldy $0FC6,X
    tax
    lda $0BCA,X
    tax
    stx $10
    lda $12
    tax
    lda $0B8E,X
    ldx $10
    jsl C41EFF_CalculateAngleBetweenPoints
    pld
    rtl
C46B0A_RoundAngleToOctantAndCacheCurrentSlot:
    rep #$31
    phd
    pha
    tdc
    adc.w #$FFF0
    tcd
    pla
    ldy.w #$2000
    clc
    adc.w #$1000
    jsl C0915B_DivideUnsignedWordByY
    sta $0E
    lda $1A42
    asl A
    tax
    lda $0E
    sta $1A86,X
    pld
    rtl
C46B2D_FloorAngleToDirectionOctant:
    rep #$31
    ldy.w #$2000
    jsl C09032_DivideUnsignedWordByIndex
    rtl
C46B37_RotateDirectionOctantHalfTurn:
    rep #$31
    inc A
    inc A
    inc A
    inc A
    and.w #$0007
    rtl

; ---------------------------------------------------------------------------
; C4:6B51


; ---------------------------------------------------------------------------
; C4:6B41

C46B41_RoundedAngleToWalkDirectionTable:
    ; data bytes: C4:6B41..C4:6B51
    db $02,$00,$03,$00,$04,$00,$05,$00,$06,$00,$07,$00,$07,$00,$01,$00

C46B51_RoundAngleToWalkDirectionStep:
    rep #$31
    ldy.w #$2000
    clc
    adc.w #$1000
    jsl C0915B_DivideUnsignedWordByY
    asl A
    tax
    lda C46B41_RoundedAngleToWalkDirectionTable,X
    rtl
C46B65_SetCurrentSlotTargetToPlayerPosition:
    rep #$31
    lda $1A42
    asl A
    tax
    lda $9877
    sta $0FC6,X
    lda $987B
    sta $1002,X
    rtl
C46B79_SetCurrentSlotTargetTo9e2dPosition:
    rep #$31
    lda $1A42
    asl A
    tax
    lda $9E2D
    sta $0FC6,X
    lda $9E2F
    sta $1002,X
    rtl
C46B8D_SetCurrentSlotTargetToVisualTypeSlotPosition:
    rep #$31
    phd
    pha
    tdc
    adc.w #$FFEE
    tcd
    pla
    tax
    ldy $1A42
    sty $10
    txa
    jsl C4605A_FindEntitySlotByVisualTypeId
    sta $0E
    ldy $10
    tya
    asl A
    tay
    lda $0E
    asl A
    tax
    lda $0B8E,X
    sta $0FC6,Y
    lda $0BCA,X
    sta $1002,Y
    pld
    rtl
C46BBB_SetCurrentSlotTargetToPoseDescriptorSlotPosition:
    rep #$31
    phd
    pha
    tdc
    adc.w #$FFEE
    tcd
    pla
    tax
    ldy $1A42
    sty $10
    txa
    jsl C46028_FindEntitySlotByCachedPoseDescriptorId
    sta $0E
    ldy $10
    tya
    asl A
    tay
    lda $0E
    asl A
    tax
    lda $0B8E,X
    sta $0FC6,Y
    lda $0BCA,X
    sta $1002,Y
    pld
    rtl
C46BE9_SetCurrentSlotTargetToRegistrySlotPosition:
    rep #$31
    phd
    pha
    tdc
    adc.w #$FFEC
    tcd
    pla
    tax
    ldy $1A42
    sty $12
    cpx.w #$00FE
    bne C46C25_SetCurrentSlotTargetToRegistrySlotPosition_ResolveExplicitCode
    lda $98A3
    and.w #$00FF
    tax
    stx $10
    txa
    dec A
    asl A
    tax
    lda $9897,X
    sta $0E
    asl A
    tax
    lda $0B8E,X
    bne C46C2E_SetCurrentSlotTargetToRegistrySlotPosition_CopyPosition
    ldx $10
    txa
    dec A
    dec A
    asl A
    tax
    lda $9897,X
    sta $0E
    bra C46C2E_SetCurrentSlotTargetToRegistrySlotPosition_CopyPosition
C46C25_SetCurrentSlotTargetToRegistrySlotPosition_ResolveExplicitCode:
    txa
    sep #$20
    jsl C4608C_ResolveEntitySlotFromOverworldTypeRegistryCode
    sta $0E
C46C2E_SetCurrentSlotTargetToRegistrySlotPosition_CopyPosition:
    ldy $12
    tya
    asl A
    tay
    lda $0E
    asl A
    tax
    lda $0B8E,X
    sta $0FC6,Y
    lda $0BCA,X
    sta $1002,Y
    pld
    rtl
