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

C10301_GetActiveInteractionContextRecord:
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

C10324_SnapshotActiveInteractionContextSlots:
    rep #$31
    phd
    tdc
    adc.w #$FFF0
    tcd
    jsr C10301_GetActiveInteractionContextRecord
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

C10380_RestoreActiveInteractionContextSlots:
    rep #$31
    phd
    tdc
    adc.w #$FFF0
    tcd
    jsr C10301_GetActiveInteractionContextRecord
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

C103DC_LoadSecondaryInteractionContextPointer:
    rep #$31
    phd
    tdc
    adc.w #$FFF2
    tcd
    jsr C10301_GetActiveInteractionContextRecord
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

C10400_GetCurrentTextContextWorkmem:
    rep #$31
    jsr C10301_GetActiveInteractionContextRecord
    tax
    lda ContextWorkmemOffset,X
    rts

; ---------------------------------------------------------------------------
; C1:040A

C1040A_LoadPrimaryInteractionContextPointer:
    rep #$31
    phd
    tdc
    adc.w #$FFF2
    tcd
    jsr C10301_GetActiveInteractionContextRecord
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
