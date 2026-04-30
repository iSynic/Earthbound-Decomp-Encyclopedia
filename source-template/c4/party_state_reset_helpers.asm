; EarthBound C4 party-state reset and callback table helper prototype.
;
; Source-emission status:
; - Prototype level: build-candidate
; - C4 source-bank scaffold pilot slice.
; - Derived from notes/c4-party-state-reset-and-callback-tables-30ec-3317.md.
; - ROM byte range, SHA-1, and source signature are tracked by
;   build/c4-build-candidate-ranges.json.
;
; Source units covered:
; - C4:30EC..C4:334A party callback table initialization, visual/status reset,
;   party record pointer rebuild, and special-event restriction latch setter.

; ---------------------------------------------------------------------------
; External contracts used by this module

C08FF7_MultiplyAByY                  = $C08FF7
C3E0BC_PartyTickVectorTableA         = $C3E0BC
C3E0F4_PartyTickVectorTableB         = $C3E0F4
C3_PARTY_TICK_VECTOR_BANK            = $00C3

; ---------------------------------------------------------------------------
; WRAM contracts

PARTY_TICK_TABLE_BASE_POSITIVE_A     = $4DD6
PARTY_TICK_TABLE_BASE_POSITIVE_B     = $4DDA
PARTY_TICK_TABLE_BASE_VECTOR_A       = $4DDE
PARTY_TICK_TABLE_BASE_VECTOR_B       = $4DE2
PARTY_TICK_TABLE_BASE_ZERO_A         = $4DE6
PARTY_TICK_TABLE_BASE_NEGATIVE_B     = $4DEA
PARTY_TICK_TABLE_BASE_NEGATIVE_A     = $4DEE
PARTY_TICK_TABLE_BASE_NEGATIVE_B_ALT = $4DF2

PARTY_TICK_TABLE_BASE_NEG_A          = $4F96
PARTY_TICK_TABLE_BASE_NEG_B          = $4F9A
PARTY_TICK_TABLE_BASE_ZERO_B         = $4F9E
PARTY_TICK_TABLE_BASE_VECTOR_B_ALT   = $4FA2
PARTY_TICK_TABLE_BASE_VECTOR_A_ALT   = $4FA6
PARTY_TICK_TABLE_BASE_VECTOR_B_COPY  = $4FAA
PARTY_TICK_TABLE_BASE_ZERO_A_ALT     = $4FAE
PARTY_TICK_TABLE_BASE_NEG_B_COPY     = $4FB2

PARTY_VISUAL_MASK_TABLE              = $2BAA
PARTY_CHARACTER_STATUS_BYTES_BASE    = $99DC
PARTY_CHARACTER_RECORD_BASE          = $99CE
PARTY_CHARACTER_RECORD_POINTER_TABLE = $4DC8
GLOBAL_9840_GATE                     = $9840
SPECIAL_EVENT_RESTRICTION_LATCH      = $5D98

PARTY_TICK_VECTOR_ENTRY_COUNT        = $000E
PARTY_TICK_VECTOR_STRIDE             = $0020
PARTY_VISUAL_MASK_SLOT_COUNT         = $001E
PARTY_CHARACTER_COUNT                = $0006
PARTY_STATUS_BYTE_COUNT              = $0007
PARTY_CHARACTER_RECORD_STRIDE        = $005F

; Direct-page locals:
;   $06/$08 = long/vector temp value.
;   $0A/$0C = long source pointer.
;   $0E/$10 = original vector temp value.
;   $12 = per-entry 32-byte table stride.
;   $14 = outer callback/vector entry index.

; ---------------------------------------------------------------------------
; C4:30EC

; InitializePartyTickCallbackTables
C430EC_InitializePartyTickCallbackTables:
    rep #$31
    phd
    tdc
    adc #$FFEA
    tcd
    ldy #$0000
    sty $14
    jmp C432A5_InitializePartyTickCallbackTables_CheckLoop

C430FC_InitializePartyTickCallbackTables_Entry:
    tya
    asl
    asl
    tax
    lda #C3E0BC_PartyTickVectorTableA
    sta $0A
    lda #C3_PARTY_TICK_VECTOR_BANK
    sta $0C
    txa
    clc
    adc $0A
    sta $0A
    ldy #$0002
    lda [$0A],Y
    tay
    lda [$0A]
    sta $06
    sty $08
    lda $06
    sta $0E
    lda $08
    sta $10
    lda #$0000
    sta $06
    lda #$0000
    sta $08
    ldy $14
    tya
    asl
    asl
    asl
    asl
    asl
    sta $12
    clc
    adc #PARTY_TICK_TABLE_BASE_ZERO_A
    tay
    lda $06
    sta $0000,Y
    lda $08
    sta $0002,Y
    lda $12
    clc
    adc #PARTY_TICK_TABLE_BASE_POSITIVE_A
    tay
    lda $06
    sta $0000,Y
    lda $08
    sta $0002,Y
    lda $12
    clc
    adc #PARTY_TICK_TABLE_BASE_ZERO_A_ALT
    tay
    lda $06
    sta $0000,Y
    lda $08
    sta $0002,Y
    lda $12
    clc
    adc #PARTY_TICK_TABLE_BASE_ZERO_B
    tay
    lda $06
    sta $0000,Y
    lda $08
    sta $0002,Y
    lda $0E
    sta $06
    lda $10
    sta $08
    lda $12
    clc
    adc #PARTY_TICK_TABLE_BASE_VECTOR_A_ALT
    tay
    lda $06
    sta $0000,Y
    lda $08
    sta $0002,Y
    lda $12
    clc
    adc #PARTY_TICK_TABLE_BASE_VECTOR_A
    tay
    lda $06
    sta $0000,Y
    lda $08
    sta $0002,Y
    lda $0E
    sta $06
    lda $10
    sta $08
    sec
    lda #$0000
    sbc $06
    sta $06
    lda #$0000
    sbc $08
    sta $08
    lda $12
    clc
    adc #PARTY_TICK_TABLE_BASE_NEG_A
    tay
    lda $06
    sta $0000,Y
    lda $08
    sta $0002,Y
    lda $12
    clc
    adc #PARTY_TICK_TABLE_BASE_NEGATIVE_A
    tay
    lda $06
    sta $0000,Y
    lda $08
    sta $0002,Y
    lda #C3E0F4_PartyTickVectorTableB
    sta $0A
    lda #C3_PARTY_TICK_VECTOR_BANK
    sta $0C
    txa
    clc
    adc $0A
    sta $0A
    ldy #$0002
    lda [$0A],Y
    tay
    lda [$0A]
    sta $06
    sty $08
    lda $06
    sta $0E
    lda $08
    sta $10
    lda $12
    clc
    adc #PARTY_TICK_TABLE_BASE_VECTOR_B_COPY
    tay
    lda $06
    sta $0000,Y
    lda $08
    sta $0002,Y
    lda $12
    clc
    adc #PARTY_TICK_TABLE_BASE_VECTOR_B_ALT
    tay
    lda $06
    sta $0000,Y
    lda $08
    sta $0002,Y
    lda $12
    clc
    adc #PARTY_TICK_TABLE_BASE_VECTOR_B
    tay
    lda $06
    sta $0000,Y
    lda $08
    sta $0002,Y
    lda $12
    clc
    adc #PARTY_TICK_TABLE_BASE_POSITIVE_B
    tay
    lda $06
    sta $0000,Y
    lda $08
    sta $0002,Y
    lda $0E
    sta $06
    lda $10
    sta $08
    sec
    lda #$0000
    sbc $06
    sta $06
    lda #$0000
    sbc $08
    sta $08
    lda $12
    clc
    adc #PARTY_TICK_TABLE_BASE_NEG_B_COPY
    tay
    lda $06
    sta $0000,Y
    lda $08
    sta $0002,Y
    lda $12
    clc
    adc #PARTY_TICK_TABLE_BASE_NEG_B
    tay
    lda $06
    sta $0000,Y
    lda $08
    sta $0002,Y
    lda $12
    clc
    adc #PARTY_TICK_TABLE_BASE_NEGATIVE_B
    tay
    lda $06
    sta $0000,Y
    lda $08
    sta $0002,Y
    lda $12
    clc
    adc #PARTY_TICK_TABLE_BASE_NEGATIVE_B_ALT
    tay
    lda $06
    sta $0000,Y
    lda $08
    sta $0002,Y
    ldy $14
    iny
    sty $14
C432A5_InitializePartyTickCallbackTables_CheckLoop:
    cpy #PARTY_TICK_VECTOR_ENTRY_COUNT
    bcs C432AF_InitializePartyTickCallbackTables_Done
    beq C432AF_InitializePartyTickCallbackTables_Done
    jmp C430FC_InitializePartyTickCallbackTables_Entry
C432AF_InitializePartyTickCallbackTables_Done:
    pld
    rtl

; ---------------------------------------------------------------------------
; C4:32B1

; ResetPartyVisualMasksAndStatusBytes
C432B1_ResetPartyVisualMasksAndStatusBytes:
    rep #$31
    phd
    tdc
    adc #$FFEE
    tcd
    lda #$0000
    sta $10
    bra C432CA_ResetPartyVisualMasksAndStatusBytes_CheckVisualMaskLoop
C432C0_ResetPartyVisualMasksAndStatusBytes_ClearVisualMask:
    asl
    tax
    stz PARTY_VISUAL_MASK_TABLE,X
    lda $10
    inc
    sta $10
C432CA_ResetPartyVisualMasksAndStatusBytes_CheckVisualMaskLoop:
    cmp #PARTY_VISUAL_MASK_SLOT_COUNT
    bcc C432C0_ResetPartyVisualMasksAndStatusBytes_ClearVisualMask
    ldx #$0000
    stx $0E
    bra C43309_ResetPartyVisualMasksAndStatusBytes_CheckPartyLoop
C432D6_ResetPartyVisualMasksAndStatusBytes_PartySlot:
    lda #$0000
    sta $10
    bra C432FF_ResetPartyVisualMasksAndStatusBytes_CheckStatusByteLoop
C432DD_ResetPartyVisualMasksAndStatusBytes_ClearStatusByte:
    sta $02
    ldx $0E
    txa
    ldy #PARTY_CHARACTER_RECORD_STRIDE
    jsl C08FF7_MultiplyAByY
    clc
    adc #PARTY_CHARACTER_STATUS_BYTES_BASE
    clc
    adc $02
    tax
    sep #$20
    lda #$00
    sta $0000,X
    rep #$20
    lda $10
    inc
    sta $10
C432FF_ResetPartyVisualMasksAndStatusBytes_CheckStatusByteLoop:
    cmp #PARTY_STATUS_BYTE_COUNT
    bcc C432DD_ResetPartyVisualMasksAndStatusBytes_ClearStatusByte
    ldx $0E
    inx
    stx $0E
C43309_ResetPartyVisualMasksAndStatusBytes_CheckPartyLoop:
    cpx #PARTY_CHARACTER_COUNT
    bcc C432D6_ResetPartyVisualMasksAndStatusBytes_PartySlot
    sep #$20
    stz GLOBAL_9840_GATE
    rep #$20
    pld
    rtl

; ---------------------------------------------------------------------------
; C4:3317

; RebuildPartyCharacterRecordPointerTable4dc8
C43317_RebuildPartyCharacterRecordPointerTable4dc8:
    rep #$31
    phd
    tdc
    adc #$FFF0
    tcd
    lda #$0000
    sta $0E
    bra C4333D_RebuildPartyCharacterRecordPointerTable4dc8_CheckLoop
C43326_RebuildPartyCharacterRecordPointerTable4dc8_Entry:
    asl
    tax
    lda $0E
    ldy #PARTY_CHARACTER_RECORD_STRIDE
    jsl C08FF7_MultiplyAByY
    clc
    adc #PARTY_CHARACTER_RECORD_BASE
    sta PARTY_CHARACTER_RECORD_POINTER_TABLE,X
    lda $0E
    inc
    sta $0E
C4333D_RebuildPartyCharacterRecordPointerTable4dc8_CheckLoop:
    cmp #PARTY_CHARACTER_COUNT
    bcc C43326_RebuildPartyCharacterRecordPointerTable4dc8_Entry
    pld
    rtl

; ---------------------------------------------------------------------------
; C4:3344

; SetSpecialEventRestrictionLatch5d98
C43344_SetSpecialEventRestrictionLatch5d98:
    rep #$31
    sta SPECIAL_EVENT_RESTRICTION_LATCH
    rtl
