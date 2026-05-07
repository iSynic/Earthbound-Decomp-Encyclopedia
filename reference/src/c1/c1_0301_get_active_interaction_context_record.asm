; EarthBound C1 active interaction/text context helper family.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Hand-polished from tools/emit_linear_source_module.py output, then
;   intended for byte-equivalence validation.
;
; Source unit covered:
; - C1:0301..C1:042E GetActiveInteractionContextRecord

; ---------------------------------------------------------------------------
; External contracts used by this module
; - Resolves the active text/interaction context descriptor from $8958 through
;   the $88E4 index table and $8650 descriptor table, or returns fallback
;   descriptor $85FE when $88E0 is FFFF.
; - The neighbor helpers snapshot/restore primary pointer, secondary pointer,
;   and workmem slots inside that descriptor.

C08FF7_ResolveIndexedPointerOffset = $C08FF7

ActiveWindowDescriptorState = $88E0
ActiveWindowFocus           = $8958
WindowDescriptorIndexTable  = $88E4

FallbackInteractionContextRecord = $85FE
InteractionContextRecordTable    = $8650
InteractionContextRecordSize     = $0052

ContextPrimaryPointerOffset        = $0017
ContextSecondaryPointerOffset      = $001B
ContextWorkmemOffset               = $001F
ContextSavedPrimaryPointerOffset   = $0021
ContextSavedSecondaryPointerOffset = $0025
ContextSavedWorkmemOffset          = $0029

ScratchPointerLo        = $06
ScratchPointerHi        = $08
ContextRecordBase       = $0E
CurrentTextPointerLo    = $14
CurrentTextPointerHi    = $16

; ---------------------------------------------------------------------------
; C1:0301

GET_ACTIVE_WINDOW_ADDRESS:
C10301_GetActiveInteractionContextRecord = GET_ACTIVE_WINDOW_ADDRESS
    rep #$31
    lda ActiveWindowDescriptorState
    cmp.w #$FFFF
    bne C10310_ResolveFocusedInteractionContextRecord

    lda.w #FallbackInteractionContextRecord
    bra C10323_ReturnInteractionContextRecord

C10310_ResolveFocusedInteractionContextRecord:
    lda ActiveWindowFocus
    asl A
    tax
    lda WindowDescriptorIndexTable,X
    ldy.w #InteractionContextRecordSize
    jsl C08FF7_ResolveIndexedPointerOffset
    clc
    adc.w #InteractionContextRecordTable

C10323_ReturnInteractionContextRecord:
    rts

; ---------------------------------------------------------------------------
; C1:0324

TRANSFER_ACTIVE_MEM_STORAGE:
C10324_SnapshotActiveInteractionContextSlots = TRANSFER_ACTIVE_MEM_STORAGE
    rep #$31
    phd
    tdc
    adc.w #$FFF0
    tcd
    jsr GET_ACTIVE_WINDOW_ADDRESS
    sta ContextRecordBase

    clc
    adc.w #ContextPrimaryPointerOffset
    tay
    lda $0000,Y
    sta ScratchPointerLo
    lda $0002,Y
    sta ScratchPointerHi

    lda ContextRecordBase
    clc
    adc.w #ContextSavedPrimaryPointerOffset
    tay
    lda ScratchPointerLo
    sta $0000,Y
    lda ScratchPointerHi
    sta $0002,Y

    lda ContextRecordBase
    clc
    adc.w #ContextSecondaryPointerOffset
    tay
    lda $0000,Y
    sta ScratchPointerLo
    lda $0002,Y
    sta ScratchPointerHi

    lda ContextRecordBase
    clc
    adc.w #ContextSavedSecondaryPointerOffset
    tay
    lda ScratchPointerLo
    sta $0000,Y
    lda ScratchPointerHi
    sta $0002,Y

    lda ContextRecordBase
    pha
    tax
    lda ContextWorkmemOffset,X
    plx
    sta ContextSavedWorkmemOffset,X
    pld
    rts

; ---------------------------------------------------------------------------
; C1:0380

TRANSFER_STORAGE_MEM_ACTIVE:
C10380_RestoreActiveInteractionContextSlots = TRANSFER_STORAGE_MEM_ACTIVE
    rep #$31
    phd
    tdc
    adc.w #$FFF0
    tcd
    jsr GET_ACTIVE_WINDOW_ADDRESS
    sta ContextRecordBase

    clc
    adc.w #ContextSavedPrimaryPointerOffset
    tay
    lda $0000,Y
    sta ScratchPointerLo
    lda $0002,Y
    sta ScratchPointerHi

    lda ContextRecordBase
    clc
    adc.w #ContextPrimaryPointerOffset
    tay
    lda ScratchPointerLo
    sta $0000,Y
    lda ScratchPointerHi
    sta $0002,Y

    lda ContextRecordBase
    clc
    adc.w #ContextSavedSecondaryPointerOffset
    tay
    lda $0000,Y
    sta ScratchPointerLo
    lda $0002,Y
    sta ScratchPointerHi

    lda ContextRecordBase
    clc
    adc.w #ContextSecondaryPointerOffset
    tay
    lda ScratchPointerLo
    sta $0000,Y
    lda ScratchPointerHi
    sta $0002,Y

    lda ContextRecordBase
    pha
    tax
    lda ContextSavedWorkmemOffset,X
    plx
    sta ContextWorkmemOffset,X
    pld
    rts

; ---------------------------------------------------------------------------
; C1:03DC

GET_ARGUMENT_MEMORY:
C103DC_LoadSecondaryInteractionContextPointer = GET_ARGUMENT_MEMORY
    rep #$31
    phd
    tdc
    adc.w #$FFF2
    tcd
    jsr GET_ACTIVE_WINDOW_ADDRESS
    clc
    adc.w #ContextSecondaryPointerOffset
    tay
    lda $0000,Y
    sta ScratchPointerLo
    lda $0002,Y
    sta ScratchPointerHi
    lda ScratchPointerLo
    sta CurrentTextPointerLo
    lda ScratchPointerHi
    sta CurrentTextPointerHi
    pld
    rts

; ---------------------------------------------------------------------------
; C1:0400

GET_SECONDARY_MEMORY:
C10400_GetCurrentTextContextWorkmem = GET_SECONDARY_MEMORY
    rep #$31
    jsr GET_ACTIVE_WINDOW_ADDRESS
    tax
    lda ContextWorkmemOffset,X
    rts

; ---------------------------------------------------------------------------
; C1:040A

GET_WORKING_MEMORY:
C1040A_LoadPrimaryInteractionContextPointer = GET_WORKING_MEMORY
    rep #$31
    phd
    tdc
    adc.w #$FFF2
    tcd
    jsr GET_ACTIVE_WINDOW_ADDRESS
    clc
    adc.w #ContextPrimaryPointerOffset
    tay
    lda $0000,Y
    sta ScratchPointerLo
    lda $0002,Y
    sta ScratchPointerHi
    lda ScratchPointerLo
    sta CurrentTextPointerLo
    lda ScratchPointerHi
    sta CurrentTextPointerHi
    pld
    rts
