; EarthBound C4 staged movement and tracked-item pulse helper prototype.
;
; Source-emission status:
; - Prototype level: build-candidate
; - C4 source-bank scaffold pilot slice.
; - Derived from notes/staged-movement-pulse-and-tracked-item-registry-c48c59-c48f98.md
;   plus byte-level corroboration from the original ROM and legacy disassembly.
; - ROM byte range, SHA-1, and source signature are tracked by
;   build/c4-build-candidate-ranges.json.
;
; Source units covered:
; - C4:8C59..C4:90ED movement pulse run accumulation, staged movement path
;   pulse generation, tracked item pulse slot arm/clear, and periodic slot tick.

; ---------------------------------------------------------------------------
; External contracts used by this module

C0402B_InstallGeneratedMovementPulseScript = $C0402B
C0915B_ScaleOrDivideAngleMagnitude         = $C0915B
C0ABE0_PlayMovementPulseSelector           = $C0ABE0
C18BC6_ApplyTrackedItemPulsePair           = $C18BC6
C18EAD_PrepareTrackedItemPulseValue        = $C18EAD
C41EFF_ComputeDirectionOctantFromDelta     = $C41EFF
C45F7B_GetRandomLessThanA                  = $C45F7B

MOVEMENT_OCTANT_TO_PULSE_SELECTOR_TABLE    = $C48C59
TRACKED_ITEM_PULSE_SOURCE_TABLE            = $F4BB
TRACKED_ITEM_PULSE_SOURCE_BANK             = $00D5

; ---------------------------------------------------------------------------
; WRAM contracts

MOVEMENT_PULSE_RUN_FLAG_BASE               = $9E58
MOVEMENT_PULSE_RUN_WORD_BASE               = $9E59
MOVEMENT_PULSE_RUN_COUNT                   = $9F18

PARTY_TICK_TABLE_BASE_POSITIVE_A           = $4DD6
PARTY_TICK_TABLE_BASE_NEG_A                = $4F96

OVERWORLD_MOVEMENT_LOCK_A                  = $4DBA
OVERWORLD_MOVEMENT_LOCK_B                  = $5D60
OVERWORLD_FREEZE_FLAG                      = $B4B6
OVERWORLD_STATE                            = $98A5

TRACKED_ITEM_PULSE_SLOT_BASE               = $9F1A
TRACKED_ITEM_PULSE_SLOT_DELAY_BASE         = $9F1B
TRACKED_ITEM_PULSE_SLOT_TIMER_BASE         = $9F1D
TRACKED_ITEM_PULSE_ACTIVE_COUNT            = $9F2A
TRACKED_ITEM_PULSE_GLOBAL_TIMER            = $9F2C
TRACKED_ITEM_PULSE_SLOT_BASE_LOW           = $9F1A

MOVEMENT_PULSE_RUN_LIMIT                   = $0040
TRACKED_ITEM_SLOT_COUNT                    = $0004
TRACKED_ITEM_SLOT_REFRESH_TIMER            = $3C
TRACKED_ITEM_RANDOM_WINDOW                 = $0002

; Direct-page locals:
;   C4:8C97 uses $02/$04/$0E/$10 as run-list base/current value scratch.
;   C4:8D58 uses $02..$1E as staged movement vector/current-target scratch.
;   C4:8EEB/C4:8FC4 use $06/$08 and $0A/$0C as D5:F4BB long pointers.

; ---------------------------------------------------------------------------
; C4:8C69

; ClearMovementPulseAccumulator

; ---------------------------------------------------------------------------
; C4:8C59

C48C59_MovementOctantToPulseSelectorTable:
    ; data bytes: C4:8C59..C4:8C69
    db $00,$08,$00,$09,$00,$01,$00,$05,$00,$04,$00,$06,$00,$02,$00,$0A

C48C69_ClearMovementPulseAccumulator:
    rep #$31
    phd
    tdc
    adc #$FFF0
    tcd
    stz MOVEMENT_PULSE_RUN_COUNT
    lda #$0000
    sta $0E
    bra C48C90_ClearMovementPulseAccumulator_CheckLoop

C48C7B_ClearMovementPulseAccumulator_ClearEntry:
    sta $04
    asl
    adc $04
    tax
    stz MOVEMENT_PULSE_RUN_WORD_BASE,X
    sep #$20
    stz MOVEMENT_PULSE_RUN_FLAG_BASE,X
    rep #$20
    lda $0E
    inc A
    sta $0E
C48C90_ClearMovementPulseAccumulator_CheckLoop:
    cmp #MOVEMENT_PULSE_RUN_LIMIT
    bcc C48C7B_ClearMovementPulseAccumulator_ClearEntry
    pld
    rtl

; ---------------------------------------------------------------------------
; C4:8C97

; AppendMovementPulseSelectorRun
C48C97_AppendMovementPulseSelectorRun:
    rep #$31
    phd
    pha
    tdc
    adc #$FFEE
    tcd
    pla
    sta $04
    sta $10
    lda MOVEMENT_PULSE_RUN_COUNT
    bne C48CD4_AppendMovementPulseSelectorRun_SearchExisting
    ldx #MOVEMENT_PULSE_RUN_WORD_BASE
    stx $0E
    stx $02
    lda MOVEMENT_PULSE_RUN_COUNT
    sta $04
    asl
    adc $04
    clc
    adc $02
    tax
    lda $0000,X
    bne C48CD4_AppendMovementPulseSelectorRun_SearchExisting
    lda $10
    sta $04
    ldx $0E
    sta $0000,X
    sep #$20
    lda.b #$01
    sta MOVEMENT_PULSE_RUN_FLAG_BASE
    bra C48D34_AppendMovementPulseSelectorRun_Return

C48CD4_AppendMovementPulseSelectorRun_SearchExisting:
    lda MOVEMENT_PULSE_RUN_COUNT
    sta $04
    asl
    adc $04
    sta $0E
    lda #MOVEMENT_PULSE_RUN_WORD_BASE
    sta $02
    lda $10
    sta $04
    lda $0E
    clc
    adc $02
    tax
    lda $0000,X
    cmp $04
    bne C48D06_AppendMovementPulseSelectorRun_AllocateNew
    lda $0E
    clc
    adc #MOVEMENT_PULSE_RUN_FLAG_BASE
    tax
    sep #$20
    lda $0000,X
    inc A
    sta $0000,X
    bra C48D34_AppendMovementPulseSelectorRun_Return

C48D06_AppendMovementPulseSelectorRun_AllocateNew:
    lda MOVEMENT_PULSE_RUN_COUNT
    inc A
    sta MOVEMENT_PULSE_RUN_COUNT
    cmp #MOVEMENT_PULSE_RUN_LIMIT
    bne C48D14_AppendMovementPulseSelectorRun_StoreNew
C48D12_AppendMovementPulseSelectorRun_OverflowLock:
    bra C48D12_AppendMovementPulseSelectorRun_OverflowLock

C48D14_AppendMovementPulseSelectorRun_StoreNew:
    sta $04
    asl
    adc $04
    clc
    adc $02
    tax
    lda $10
    sta $04
    sta $0000,X
    lda MOVEMENT_PULSE_RUN_COUNT
    sta $04
    asl
    adc $04
    tax
    sep #$20
    lda.b #$01
    sta MOVEMENT_PULSE_RUN_FLAG_BASE,X
C48D34_AppendMovementPulseSelectorRun_Return:
    rep #$20
    pld
    rtl

; ---------------------------------------------------------------------------
; C4:8D58

; BuildStagedMovementPulsesAndReturnDelay

; ---------------------------------------------------------------------------
; C4:8D38

C48D38_MovementOctantSignedUnitDeltaTable:
    ; data bytes: C4:8D38..C4:8D58
    db $00,$00,$01,$00,$01,$00,$01,$00,$00,$00,$FF,$FF,$FF,$FF,$FF,$FF
    db $FF,$FF,$FF,$FF,$00,$00,$01,$00,$01,$00,$01,$00,$00,$00,$FF,$FF

C48D58_BuildStagedMovementPulsesAndReturnDelay:
    rep #$31
    phd
    pha
    tdc
    adc #$FFE0
    tcd
    pla
    sty $1E
    stx $02
    tax
    ldy $2E
    sty $1C
    lda #$0000
    sta $04
    stx $12
    lda $02
    sta $16
C48D76_BuildStagedMovementPulsesAndReturnDelay_Loop:
    lda $12
    sec
    sbc $1E
    sta $1A
    lda $16
    sec
    sbc $1C
    sta $02
    sta $18
    lda $1A
    sta $02
    lda #$0000
    clc
    sbc $02
    bvc C48D96_BuildStagedMovementPulsesAndReturnDelay_CheckAbsXSign
    bpl C48DA0_BuildStagedMovementPulsesAndReturnDelay_KeepAbsX
    bra C48D98_BuildStagedMovementPulsesAndReturnDelay_NegateAbsX

C48D96_BuildStagedMovementPulsesAndReturnDelay_CheckAbsXSign:
    bmi C48DA0_BuildStagedMovementPulsesAndReturnDelay_KeepAbsX
C48D98_BuildStagedMovementPulsesAndReturnDelay_NegateAbsX:
    lda $1A
    eor #$FFFF
    inc A
    bra C48DA2_BuildStagedMovementPulsesAndReturnDelay_CheckXDelta

C48DA0_BuildStagedMovementPulsesAndReturnDelay_KeepAbsX:
    lda $1A
C48DA2_BuildStagedMovementPulsesAndReturnDelay_CheckXDelta:
    clc
    sbc #$0001
    bvs C48DAC_BuildStagedMovementPulsesAndReturnDelay_CheckXDeltaSign
    bpl C48DDA_BuildStagedMovementPulsesAndReturnDelay_EmitStep
    bra C48DAE_BuildStagedMovementPulsesAndReturnDelay_CheckYDelta

C48DAC_BuildStagedMovementPulsesAndReturnDelay_CheckXDeltaSign:
    bmi C48DDA_BuildStagedMovementPulsesAndReturnDelay_EmitStep
C48DAE_BuildStagedMovementPulsesAndReturnDelay_CheckYDelta:
    lda $18
    sta $02
    lda #$0000
    clc
    sbc $02
    bvc C48DBE_BuildStagedMovementPulsesAndReturnDelay_CheckAbsYSign
    bpl C48DC8_BuildStagedMovementPulsesAndReturnDelay_KeepAbsY
    bra C48DC0_BuildStagedMovementPulsesAndReturnDelay_NegateAbsY

C48DBE_BuildStagedMovementPulsesAndReturnDelay_CheckAbsYSign:
    bmi C48DC8_BuildStagedMovementPulsesAndReturnDelay_KeepAbsY
C48DC0_BuildStagedMovementPulsesAndReturnDelay_NegateAbsY:
    lda $02
    eor #$FFFF
    inc A
    bra C48DCA_BuildStagedMovementPulsesAndReturnDelay_CheckYDelta

C48DC8_BuildStagedMovementPulsesAndReturnDelay_KeepAbsY:
    lda $02
C48DCA_BuildStagedMovementPulsesAndReturnDelay_CheckYDelta:
    clc
    sbc #$0001
    bvc C48DD5_BuildStagedMovementPulsesAndReturnDelay_CheckYDeltaSign
    bmi C48DDA_BuildStagedMovementPulsesAndReturnDelay_EmitStep
    jmp C48E67_BuildStagedMovementPulsesAndReturnDelay_Done

C48DD5_BuildStagedMovementPulsesAndReturnDelay_CheckYDeltaSign:
    bpl C48DDA_BuildStagedMovementPulsesAndReturnDelay_EmitStep
    jmp C48E67_BuildStagedMovementPulsesAndReturnDelay_Done

C48DDA_BuildStagedMovementPulsesAndReturnDelay_EmitStep:
    lda $1C
    sta $0E
    ldy $1E
    ldx $16
    lda $12
    jsl C41EFF_ComputeDirectionOctantFromDelta
    ldy #$2000
    clc
    adc #$1000
    jsl C0915B_ScaleOrDivideAngleMagnitude
    tax
    stx $18
    txa
    asl
    tax
    lda.l MOVEMENT_OCTANT_TO_PULSE_SELECTOR_TABLE,X
    jsl C48C97_AppendMovementPulseSelectorRun
    ldx $18
    txa
    asl
    asl
    sta $1A
    clc
    adc #PARTY_TICK_TABLE_BASE_POSITIVE_A
    tay
    lda $0000,Y
    sta $0A
    lda $0002,Y
    sta $0C
    lda $10
    sta $06
    lda $12
    sta $08
    clc
    lda $06
    adc $0A
    sta $06
    lda $08
    adc $0C
    sta $08
    lda $06
    sta $10
    lda $08
    sta $12
    lda $1A
    clc
    adc #PARTY_TICK_TABLE_BASE_NEG_A
    tay
    lda $0000,Y
    sta $0A
    lda $0002,Y
    sta $0C
    lda $14
    sta $06
    lda $16
    sta $08
    clc
    lda $06
    adc $0A
    sta $06
    lda $08
    adc $0C
    sta $08
    lda $06
    sta $14
    lda $08
    sta $16
    inc $04
    jmp C48D76_BuildStagedMovementPulsesAndReturnDelay_Loop

C48E67_BuildStagedMovementPulsesAndReturnDelay_Done:
    lda $04
    pld
    rtl

; ---------------------------------------------------------------------------
; C4:8E6B

; AppendRepeatedMovementPulseSelector
C48E6B_AppendRepeatedMovementPulseSelector:
    rep #$31
    phd
    pha
    tdc
    adc #$FFEE
    tcd
    pla
    stx $10
    tay
    sty $0E
    bra C48E8E_AppendRepeatedMovementPulseSelector_CheckLoop

C48E7C_AppendRepeatedMovementPulseSelector_Entry:
    ldy $0E
    tya
    asl
    tax
    lda.l MOVEMENT_OCTANT_TO_PULSE_SELECTOR_TABLE,X
    jsl C48C97_AppendMovementPulseSelectorRun
    ldx $10
    dex
    stx $10
C48E8E_AppendRepeatedMovementPulseSelector_CheckLoop:
    cpx #$0000
    bne C48E7C_AppendRepeatedMovementPulseSelector_Entry
    pld
    rtl

; ---------------------------------------------------------------------------
; C4:8E95

; InstallGeneratedMovementPulseScript
C48E95_InstallGeneratedMovementPulseScript:
    rep #$31
    phd
    tdc
    adc #$FFEE
    tcd
    lda MOVEMENT_PULSE_RUN_COUNT
    inc A
    sta MOVEMENT_PULSE_RUN_COUNT
    sta $04
    asl
    adc $04
    tax
    sep #$20
    stz MOVEMENT_PULSE_RUN_FLAG_BASE,X
    rep #$20
    lda #MOVEMENT_PULSE_RUN_FLAG_BASE
    sta $06
    phb
    sep #$20
    pla
    sta $08
    stz $09
    rep #$20
    lda $06
    sta $0E
    lda $08
    sta $10
    jsl C0402B_InstallGeneratedMovementPulseScript
    pld
    rtl

; ---------------------------------------------------------------------------
; C4:8ECE

; CheckTrackedItemPulseSlotActive
C48ECE_CheckTrackedItemPulseSlotActive:
    rep #$31
    ldy #$0000
    asl
    asl
    tax
    lda TRACKED_ITEM_PULSE_SLOT_TIMER_BASE,X
    and #$00FF
    bne C48EE6_CheckTrackedItemPulseSlotActive_Active
    lda TRACKED_ITEM_PULSE_SLOT_DELAY_BASE,X
    and #$00FF
    beq C48EE9_CheckTrackedItemPulseSlotActive_Return
C48EE6_CheckTrackedItemPulseSlotActive_Active:
    ldy #$0001
C48EE9_CheckTrackedItemPulseSlotActive_Return:
    tya
    rtl

; ---------------------------------------------------------------------------
; C4:8EEB

; ArmTrackedItemPulseSlotFromD5f4bb
C48EEB_ArmTrackedItemPulseSlotFromD5f4bb:
    rep #$31
    phd
    pha
    tdc
    adc #$FFEE
    tcd
    pla
    tax
    stx $10
    txa
    jsl C48ECE_CheckTrackedItemPulseSlotActive
    cmp #$0000
    bne C48F0E_ArmTrackedItemPulseSlotFromD5f4bb_AlreadyActive
    sep #$20
    lda.b #TRACKED_ITEM_SLOT_REFRESH_TIMER
    sta TRACKED_ITEM_PULSE_GLOBAL_TIMER
    rep #$20
    inc TRACKED_ITEM_PULSE_ACTIVE_COUNT
C48F0E_ArmTrackedItemPulseSlotFromD5f4bb_AlreadyActive:
    ldx $10
    txa
    asl
    asl
    clc
    adc #TRACKED_ITEM_PULSE_SLOT_BASE
    tay
    sty $0E
    lda #TRACKED_ITEM_PULSE_SOURCE_TABLE
    sta $06
    lda #TRACKED_ITEM_PULSE_SOURCE_BANK
    sta $08
    txa
    sta $04
    asl
    asl
    adc $04
    tax
    stx $10
    txa
    inc A
    pha
    lda $06
    sta $0A
    lda $08
    sta $0C
    pla
    clc
    adc $0A
    sta $0A
    sep #$20
    lda [$0A]
    sta $0000,Y
    rep #$20
    txa
    inc A
    inc A
    ldx $06
    stx $0A
    ldx $08
    stx $0C
    clc
    adc $0A
    sta $0A
    sep #$20
    lda [$0A]
    sta $00
    sta $0001,Y
    rep #$20
    lda #TRACKED_ITEM_RANDOM_WINDOW
    jsl C45F7B_GetRandomLessThanA
    sep #$20
    pha
    lda $00
    sep #$10
    plx
    stx $00
    clc
    adc $00
    dec A
    rep #$10
    ldy $0E
    sta $0002,Y
    ldx $10
    rep #$20
    txa
    inc A
    inc A
    inc A
    inc A
    clc
    adc $06
    sta $06
    sep #$20
    lda [$06]
    sta $0003,Y
    rep #$20
    pld
    rtl

; ---------------------------------------------------------------------------
; C4:8F98

; ClearTrackedItemPulseSlot
C48F98_ClearTrackedItemPulseSlot:
    rep #$31
    phd
    pha
    tdc
    adc #$FFF0
    tcd
    pla
    tax
    stx $0E
    txa
    jsl C48ECE_CheckTrackedItemPulseSlotActive
    cmp #$0000
    beq C48FC0_ClearTrackedItemPulseSlot_Return
    dec TRACKED_ITEM_PULSE_ACTIVE_COUNT
    ldx $0E
    txa
    asl
    asl
    tax
    sep #$20
    stz TRACKED_ITEM_PULSE_SLOT_DELAY_BASE,X
    stz TRACKED_ITEM_PULSE_SLOT_TIMER_BASE,X
C48FC0_ClearTrackedItemPulseSlot_Return:
    rep #$20
    pld
    rtl

; ---------------------------------------------------------------------------
; C4:8FC4

; StepTrackedItemPulseSlots
C48FC4_StepTrackedItemPulseSlots:
    rep #$31
    phd
    tdc
    adc #$FFEA
    tcd
    lda OVERWORLD_MOVEMENT_LOCK_A
    clc
    adc OVERWORLD_MOVEMENT_LOCK_B
    beq C48FD8_StepTrackedItemPulseSlots_CheckFreeze
    jmp C490EC_StepTrackedItemPulseSlots_Return

C48FD8_StepTrackedItemPulseSlots_CheckFreeze:
    lda OVERWORLD_FREEZE_FLAG
    beq C48FE0_StepTrackedItemPulseSlots_CheckState
    jmp C490EC_StepTrackedItemPulseSlots_Return

C48FE0_StepTrackedItemPulseSlots_CheckState:
    lda OVERWORLD_STATE
    cmp #$0002
    bne C48FEB_StepTrackedItemPulseSlots_TickGlobalTimer
    jmp C490EC_StepTrackedItemPulseSlots_Return

C48FEB_StepTrackedItemPulseSlots_TickGlobalTimer:
    sep #$20
    lda TRACKED_ITEM_PULSE_GLOBAL_TIMER
    dec A
    sta TRACKED_ITEM_PULSE_GLOBAL_TIMER
    rep #$20
    and #$00FF
    beq C48FFE_StepTrackedItemPulseSlots_ResetGlobalTimer
    jmp C490EC_StepTrackedItemPulseSlots_Return

C48FFE_StepTrackedItemPulseSlots_ResetGlobalTimer:
    sep #$20
    lda.b #TRACKED_ITEM_SLOT_REFRESH_TIMER
    sta TRACKED_ITEM_PULSE_GLOBAL_TIMER
    rep #$20
    lda #TRACKED_ITEM_PULSE_SLOT_BASE_LOW
    sta $02
    lda #$0001
    sta $14
    lda #$0000
    sta $04
    sta $12
    jmp C490E0_StepTrackedItemPulseSlots_CheckLoop

C4901B_StepTrackedItemPulseSlots_SlotLoop:
    lda $14
    beq C4906B_StepTrackedItemPulseSlots_TickPairTimer
    ldy $02
    iny
    sty $10
    lda $0000,Y
    and #$00FF
    beq C4906B_StepTrackedItemPulseSlots_TickPairTimer
    ldx $02
    inx
    inx
    stx $0E
    sep #$20
    lda $0000,X
    dec A
    sta $0000,X
    rep #$20
    and #$00FF
    bne C4906B_StepTrackedItemPulseSlots_TickPairTimer
    lda #TRACKED_ITEM_RANDOM_WINDOW
    jsl C45F7B_GetRandomLessThanA
    sep #$20
    sta $00
    ldy $10
    lda $0000,Y
    clc
    adc $00
    dec A
    ldx $0E
    sta $0000,X
    ldx $02
    rep #$20
    lda $0000,X
    and #$00FF
    jsl C0ABE0_PlayMovementPulseSelector
    stz $14
C4906B_StepTrackedItemPulseSlots_TickPairTimer:
    ldx $02
    inx
    inx
    inx
    lda $0000,X
    and #$00FF
    beq C490CE_StepTrackedItemPulseSlots_AdvanceSlot
    sep #$20
    dec A
    sta $0000,X
    rep #$20
    and #$00FF
    bne C490CE_StepTrackedItemPulseSlots_AdvanceSlot
    lda #TRACKED_ITEM_PULSE_SOURCE_TABLE
    sta $06
    lda #TRACKED_ITEM_PULSE_SOURCE_BANK
    sta $08
    lda $04
    sta $04
    asl
    asl
    adc $04
    tay
    sty $0E
    tya
    ldx $06
    stx $0A
    ldx $08
    stx $0C
    clc
    adc $0A
    sta $0A
    lda [$0A]
    and #$00FF
    tax
    lda #$00FF
    jsl C18EAD_PrepareTrackedItemPulseValue
    sta $10
    ldy $0E
    tya
    inc A
    inc A
    inc A
    clc
    adc $06
    sta $06
    lda [$06]
    and #$00FF
    tax
    lda $10
    jsl C18BC6_ApplyTrackedItemPulsePair
C490CE_StepTrackedItemPulseSlots_AdvanceSlot:
    inc $02
    inc $02
    inc $02
    inc $02
    lda $12
    sta $04
    inc $04
    lda $04
    sta $12
C490E0_StepTrackedItemPulseSlots_CheckLoop:
    lda $04
    cmp #TRACKED_ITEM_SLOT_COUNT
    bcs C490EC_StepTrackedItemPulseSlots_Return
    beq C490EC_StepTrackedItemPulseSlots_Return
    jmp C4901B_StepTrackedItemPulseSlots_SlotLoop

C490EC_StepTrackedItemPulseSlots_Return:
    pld
    rtl
