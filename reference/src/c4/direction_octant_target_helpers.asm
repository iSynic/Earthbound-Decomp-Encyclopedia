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
PlayerDirectionFacing                             = $987F
CurrentSlotIndex                                  = $1A42
PlayerWorldX                                      = $9877
PlayerWorldY                                      = $987B
LiveEntityWorldXTable                             = $0B8E
LiveEntityWorldYTable                             = $0BCA
CurrentSlotTargetXTable                           = $0FC6
CurrentSlotTargetYTable                           = $1002
CurrentSlotRoundedOctantCacheTable                = $1A86
NewEntityStagedX                                  = $9E2D
NewEntityStagedY                                  = $9E2F
RegistryActiveCount                               = $98A3
RegistrySlotList                                  = $9897
RegistryRecentSlotCode                            = $00FE
AngleOctantUnit                                   = $2000
AngleOctantBias                                   = $1000
OctantMask                                        = $0007

; ---------------------------------------------------------------------------
; C4:6A6E


; ---------------------------------------------------------------------------
; C4:6A5E

C46A5E_PlayerDirection987fTurnBiasTable:
    ; data bytes: C4:6A5E..C4:6A6E
    db $01,$00,$01,$00,$01,$00,$05,$00,$05,$00,$05,$00,$05,$00,$01,$00

C46A6E_MapPlayerDirection987fToTurnBias:
    rep #$31
    lda PlayerDirectionFacing
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
    ; Compute direction from the current slot's live anchor to its cached
    ; target pair using the sign/delta helper.
    rep #$31
    phd
    tdc
    adc.w #$FFEC
    tcd
    lda CurrentSlotIndex
    asl A
    sta $12
    tax
    lda CurrentSlotTargetYTable,X
    sta $0E
    lda $12
    tax
    ldy CurrentSlotTargetXTable,X
    tax
    lda LiveEntityWorldYTable,X
    tax
    stx $10
    lda $12
    tax
    lda LiveEntityWorldXTable,X
    ldx $10
    jsl GET_DIRECTION_TO
    pld
    rtl
C46ADB_ComputeCurrentSlotTargetDirectionOctant:
    ; Angle-based sibling of C46AAC, keeping the same current-slot live-anchor
    ; and cached-target source fields.
    rep #$31
    phd
    tdc
    adc.w #$FFEC
    tcd
    lda CurrentSlotIndex
    asl A
    sta $12
    tax
    lda CurrentSlotTargetYTable,X
    sta $0E
    lda $12
    tax
    ldy CurrentSlotTargetXTable,X
    tax
    lda LiveEntityWorldYTable,X
    tax
    stx $10
    lda $12
    tax
    lda LiveEntityWorldXTable,X
    ldx $10
    jsl C41EFF_CalculateAngleBetweenPoints
    pld
    rtl
C46B0A_RoundAngleToOctantAndCacheCurrentSlot:
    ; Round a 16-bit angle to an octant and cache it for the current slot.
    rep #$31
    phd
    pha
    tdc
    adc.w #$FFF0
    tcd
    pla
    ldy.w #AngleOctantUnit
    clc
    adc.w #AngleOctantBias
    jsl C0915B_DivideUnsignedWordByY
    sta $0E
    lda CurrentSlotIndex
    asl A
    tax
    lda $0E
    sta CurrentSlotRoundedOctantCacheTable,X
    pld
    rtl
C46B2D_FloorAngleToDirectionOctant:
    rep #$31
    ldy.w #AngleOctantUnit
    jsl C09032_DivideUnsignedWordByIndex
    rtl
C46B37_RotateDirectionOctantHalfTurn:
    rep #$31
    ; Four INCs preserve the original half-turn add without changing bytes.
    inc A
    inc A
    inc A
    inc A
    and.w #OctantMask
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
    ldy.w #AngleOctantUnit
    clc
    adc.w #AngleOctantBias
    jsl C0915B_DivideUnsignedWordByY
    asl A
    tax
    lda C46B41_RoundedAngleToWalkDirectionTable,X
    rtl
C46B65_SetCurrentSlotTargetToPlayerPosition:
    ; Exact current-slot target setter from the live player position.
    rep #$31
    lda CurrentSlotIndex
    asl A
    tax
    lda PlayerWorldX
    sta CurrentSlotTargetXTable,X
    lda PlayerWorldY
    sta CurrentSlotTargetYTable,X
    rtl
C46B79_SetCurrentSlotTargetTo9e2dPosition:
    ; Exact current-slot target setter from the staged new-entity position
    ; words shared with nearby entity-preparation helpers.
    rep #$31
    lda CurrentSlotIndex
    asl A
    tax
    lda NewEntityStagedX
    sta CurrentSlotTargetXTable,X
    lda NewEntityStagedY
    sta CurrentSlotTargetYTable,X
    rtl
C46B8D_SetCurrentSlotTargetToVisualTypeSlotPosition:
    ; Resolve a visual-type keyed slot and copy its live anchor into the
    ; current slot's cached target pair.
    rep #$31
    phd
    pha
    tdc
    adc.w #$FFEE
    tcd
    pla
    tax
    ldy CurrentSlotIndex
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
    lda LiveEntityWorldXTable,X
    sta CurrentSlotTargetXTable,Y
    lda LiveEntityWorldYTable,X
    sta CurrentSlotTargetYTable,Y
    pld
    rtl
C46BBB_SetCurrentSlotTargetToPoseDescriptorSlotPosition:
    ; Cached pose-descriptor keyed sibling of C46B8D.
    rep #$31
    phd
    pha
    tdc
    adc.w #$FFEE
    tcd
    pla
    tax
    ldy CurrentSlotIndex
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
    lda LiveEntityWorldXTable,X
    sta CurrentSlotTargetXTable,Y
    lda LiveEntityWorldYTable,X
    sta CurrentSlotTargetYTable,Y
    pld
    rtl
GET_POSITION_OF_PARTY_MEMBER:
C46BE9_SetCurrentSlotTargetToRegistrySlotPosition = GET_POSITION_OF_PARTY_MEMBER
    ; Registry-code target setter. The $00FE path picks the most recent live
    ; registry slot, falling back one entry when its X anchor is zero.
    rep #$31
    phd
    pha
    tdc
    adc.w #$FFEC
    tcd
    pla
    tax
    ldy CurrentSlotIndex
    sty $12
    cpx.w #RegistryRecentSlotCode
    bne C46C25_SetCurrentSlotTargetToRegistrySlotPosition_ResolveExplicitCode
    lda RegistryActiveCount
    and.w #$00FF
    tax
    stx $10
    txa
    dec A
    asl A
    tax
    lda RegistrySlotList,X
    sta $0E
    asl A
    tax
    lda LiveEntityWorldXTable,X
    bne C46C2E_SetCurrentSlotTargetToRegistrySlotPosition_CopyPosition
    ldx $10
    txa
    dec A
    dec A
    asl A
    tax
    lda RegistrySlotList,X
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
    lda LiveEntityWorldXTable,X
    sta CurrentSlotTargetXTable,Y
    lda LiveEntityWorldYTable,X
    sta CurrentSlotTargetYTable,Y
    pld
    rtl
