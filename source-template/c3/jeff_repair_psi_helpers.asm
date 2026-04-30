; EarthBound C3 Jeff repair helper prototype.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Assembler contract: pilot-ready
; - Assembler-ready pilot; not yet linked into a full assembler ROM build.
; - Derived from notes/c3-source-emission-plan.md and
;   notes/c3-jeff-repair-source-contract-f1ec.md.
; - Build-candidate conventions are documented in
;   notes/c3-build-candidate-source-conventions.md.
; - Original instruction flow is preserved in address order with symbolic
;   comments for local direct-page variables, item-table fields, and mutation
;   points.
; - ROM byte range, SHA-1, and source signature are tracked by
;   build/c3-build-candidate-ranges.json and
;   build/c3-source-signature-validation.json.
;
; Source units covered:
; - C3:F1EC..C3:F2B1 TryRepairJeffBrokenInventoryItem
;
; Evidence:
; - notes/c3-jeff-repair-source-contract-f1ec.md
; - notes/try-fix-item-callback-d0.md
; - notes/jeff-repair-item-name-bridge.md
; - notes/item-byte-19-packed-class-and-slot.md

; ---------------------------------------------------------------------------
; External contracts used by this module

C2239D_CheckPartyOverlayEntryPresent = $C2239D
C08FF7_Multiply16                   = $C08FF7
C45F7B_RollOrBoundedRandomValue     = $C45F7B

; C2:239D CheckPartyOverlayEntryPresent
;   Input:  A = party/overlay entry id
;   Output: nonzero when the entry is present.

; C0:8FF7 Multiply16
;   Input:  A = multiplicand, Y = multiplier
;   Output: A = product

; C4:5F7B RollOrBoundedRandomValue
;   Input:  A = upper bound / roll selector used here as #$0063
;   Output: value compared against the repair success threshold.

; C1:D038 MapBrokenItemToRepairedItem
;   Sister mapper used by the caller after this helper returns a nonzero
;   original broken item id.

; ---------------------------------------------------------------------------
; Local data contracts and WRAM fields

JEFF_PARTY_OVERLAY_ENTRY        = $0003

JEFF_REPAIR_THRESHOLD_ARGUMENT  = $12
JEFF_REPAIR_INVENTORY_INDEX     = $02
JEFF_REPAIR_SLOT_ADDRESS        = $04
JEFF_REPAIR_ITEM_ROW_OFFSET     = $10
JEFF_REPAIR_ORIGINAL_ITEM_ID    = $0E

ITEM_TABLE_LOW                  = $5000
ITEM_TABLE_BANK                 = $00D5
ITEM_CONFIGURATION_STRIDE       = $0027
ITEM_TYPE_OFFSET                = $0019
ITEM_REPAIR_IQ_REQUIREMENT      = $0020
ITEM_REPAIRED_ITEM_ID_OFFSET    = $0021
ITEM_TYPE_BROKEN                = $0008

JEFF_INVENTORY_BASE             = $9AAF
JEFF_INVENTORY_SLOT_COUNT       = $000E
JEFF_REPAIR_IQ_OR_STAT          = $9AA7
REPAIR_RANDOM_BOUND             = $0063

; Direct-page locals:
;   $02 = inventory index
;   $04 = address of current Jeff inventory slot
;   $06/$08 = item table long pointer or repaired-item byte pointer
;   $0A/$0C = computed long pointer for item fields
;   $0E = original broken item id
;   $10 = item row offset
;   $12 = repair success threshold from callback argument

; ---------------------------------------------------------------------------
; C3:F1EC

; TryRepairJeffBrokenInventoryItem
;
; Entry:
;   A = repair success threshold from the 1F D0 callback argument
;
; Return:
;   A = 0 if Jeff is absent or no repair succeeds
;   A = original broken item id on success
;
; Mutation:
;   On success, replaces the matched Jeff inventory slot with the repaired item
;   id from the same D5:5000 item row.
C3F1EC_TryRepairJeffBrokenInventoryItem:
    rep #$31
    phd
    pha
    tdc
    adc #$FFEC
    tcd
    pla
    sta JEFF_REPAIR_THRESHOLD_ARGUMENT

    lda #JEFF_PARTY_OVERLAY_ENTRY
    jsl C2239D_CheckPartyOverlayEntryPresent
    cmp #$0000
    bne C3F20A_TryRepairJeffBrokenInventoryItem_JeffPresent
    lda #$0000
    jmp C3F2AF_TryRepairJeffBrokenInventoryItem_Return

C3F20A_TryRepairJeffBrokenInventoryItem_JeffPresent:
    lda #$0000
    sta JEFF_REPAIR_INVENTORY_INDEX
    jmp C3F28D_TryRepairJeffBrokenInventoryItem_NextSlotCheck

C3F212_TryRepairJeffBrokenInventoryItem_CheckCandidate:
    lda #ITEM_TABLE_LOW
    sta $06
    lda #ITEM_TABLE_BANK
    sta $08
    tya                              ; original item id
    ldy #ITEM_CONFIGURATION_STRIDE
    jsl C08FF7_Multiply16
    tax
    stx JEFF_REPAIR_ITEM_ROW_OFFSET

    txa
    clc
    adc #ITEM_TYPE_OFFSET
    ldy $06
    sty $0A
    ldy $08
    sty $0C
    clc
    adc $0A
    sta $0A
    lda [$0A]
    and #$00FF
    cmp #ITEM_TYPE_BROKEN
    bne C3F289_TryRepairJeffBrokenInventoryItem_RejectCandidate

    txa
    clc
    adc #ITEM_REPAIR_IQ_REQUIREMENT
    ldx $06
    stx $0A
    ldx $08
    stx $0C
    clc
    adc $0A
    sta $0A
    sep #$20
    lda [$0A]
    cmp JEFF_REPAIR_IQ_OR_STAT
    beq C3F260_TryRepairJeffBrokenInventoryItem_IqPassed
    bcs C3F289_TryRepairJeffBrokenInventoryItem_RejectCandidate

C3F260_TryRepairJeffBrokenInventoryItem_IqPassed:
    rep #$20
    lda #REPAIR_RANDOM_BOUND
    jsl C45F7B_RollOrBoundedRandomValue
    cmp JEFF_REPAIR_THRESHOLD_ARGUMENT
    bcs C3F289_TryRepairJeffBrokenInventoryItem_RejectCandidate

    ldx JEFF_REPAIR_ITEM_ROW_OFFSET
    txa
    clc
    adc #ITEM_REPAIRED_ITEM_ID_OFFSET
    clc
    adc $06
    sta $06
    sep #$20
    lda [$06]
    ldx JEFF_REPAIR_SLOT_ADDRESS
    sta $0000,X                       ; replace broken item with repaired item
    ldy JEFF_REPAIR_ORIGINAL_ITEM_ID
    rep #$20
    tya
    bra C3F2AF_TryRepairJeffBrokenInventoryItem_Return

C3F289_TryRepairJeffBrokenInventoryItem_RejectCandidate:
    rep #$20
    inc JEFF_REPAIR_INVENTORY_INDEX

C3F28D_TryRepairJeffBrokenInventoryItem_NextSlotCheck:
    lda JEFF_REPAIR_INVENTORY_INDEX
    cmp #JEFF_INVENTORY_SLOT_COUNT
    bcs C3F2AC_TryRepairJeffBrokenInventoryItem_Fail
    lda JEFF_REPAIR_INVENTORY_INDEX
    clc
    adc #JEFF_INVENTORY_BASE
    sta JEFF_REPAIR_SLOT_ADDRESS
    ldx JEFF_REPAIR_SLOT_ADDRESS
    lda $0000,X
    and #$00FF
    tay
    sty JEFF_REPAIR_ORIGINAL_ITEM_ID
    beq C3F2AC_TryRepairJeffBrokenInventoryItem_Fail
    jmp C3F212_TryRepairJeffBrokenInventoryItem_CheckCandidate

C3F2AC_TryRepairJeffBrokenInventoryItem_Fail:
    lda #$0000

C3F2AF_TryRepairJeffBrokenInventoryItem_Return:
    pld
    rtl
