; EarthBound C3 inventory, equipment, and tracked-item helper prototype.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Assembler contract: pilot-ready
; - Assembler-ready pilot; not yet linked into a full assembler ROM build.
; - Derived from notes/c3-source-emission-plan.md and the source contracts linked
;   below.
; - Build-candidate conventions are documented in
;   notes/c3-build-candidate-source-conventions.md.
; - Original instruction flow is preserved in address order with symbolic
;   comments for local direct-page variables, mixed-row slices, and tracked-item
;   table contracts.
; - ROM byte range, SHA-1, mixed-row slice labels, and source signature are
;   tracked by build/c3-build-candidate-ranges.json and
;   build/c3-source-signature-validation.json.
;
; Source units covered:
; - C3:E977..C3:E9A0 ReadCharacterInventorySlotByte
; - C3:E9A0..C3:E9F7 CheckEquippedInventorySlotReference
; - C3:E9F7..C3:EAD0 CheckEquippedInventoryItemPresence
; - C3:EAD0..C3:EB1C RefreshEggFamilyLifecycleOnInsert
; - C3:EB1C..C3:EBCA RefreshEggFamilyLifecycleOnRemove
; - C3:EBCA..C3:EC1F SyncPartyOverlayTrackedItemFamilyState
;
; Evidence:
; - notes/c3-inventory-equipped-slot-and-egg-refresh-helpers-e977-ebca.md
; - notes/c3-mixed-source-split-plan.md
; - notes/c3-tracked-item-sync-source-contract-ebca.md
; - notes/data-contracts-c0-c4.md, TIMED_ITEM_TRANSFORMATION_TABLE

; ---------------------------------------------------------------------------
; External contracts used by this module

C08FF7_Multiply16                     = $C08FF7
C45683_CheckActiveInventoryForItem    = $C45683
C48ECE_IsTrackedItemPulseActive       = $C48ECE
C48EEB_ArmTrackedItemPulse            = $C48EEB
C48F98_ClearTrackedItemPulse          = $C48F98

; C0:8FF7 Multiply16
;   Input:  A = multiplicand, Y = multiplier
;   Output: A = product

; C4:5683 CheckActiveInventoryForItem
;   Input:  A = character selector, X = item id
;   If A == 00FF, scans active party/entity inventory state.
;   Output: 0 when absent, nonzero when present.

; C4:8ECE IsTrackedItemPulseActive
;   Input:  A = timed-item row index
;   Output: 1 if matching $9F1A record has active bytes, else 0.

; C4:8EEB ArmTrackedItemPulse
;   Input:  A = timed-item row index
;   Arms/refreshed the $9F1A record from D5:F4BB row metadata.

; C4:8F98 ClearTrackedItemPulse
;   Input:  A = timed-item row index
;   Clears/decrements the matching $9F1A record if active.

; ---------------------------------------------------------------------------
; Local data contracts and WRAM fields

CHARACTER_RECORD_STRIDE        = $005F
CHARACTER_INVENTORY_BASE       = $99F1
EQUIPPED_SLOT_REFERENCE_BASE   = $99FF
ACTIVE_PARTY_TYPE_ARRAY        = $986F
ACTIVE_PARTY_TYPE_COUNT        = $98A4

TIMED_ITEM_TRANSFORMATION_TABLE = $D5F4BB
TIMED_ITEM_TABLE_LOW           = $F4BB
TIMED_ITEM_TABLE_BANK          = $00D5
TIMED_ITEM_ROW_SIZE            = $0005

NO_ACTIVE_INVENTORY_SELECTOR   = $00FF
ACTIVE_INVENTORY_SLOT_COUNT    = $000E

; Shared locals:
;   $00 = low-byte item id being inserted/removed/synced
;   $02/$04 = scratch counters and computed offsets
;   $06/$08 = long pointer to timed-item table row
;   $0E = row index or matched inventory item id
;   $10/$12/$14 = nested scan counters / row index scratch

; ---------------------------------------------------------------------------
; C3:E977

; ReadCharacterInventorySlotByte
;
; Entry:
;   A = 1-based character id
;   X = 1-based inventory slot
;
; Return:
;   A = inventory byte at $99F1 + (character - 1) * 0x5F + (slot - 1)
;
; Source note:
;   This routine is embedded in the original C3:E84E mixed data/source row.
;   The split plan carves it as C3:E977..E9A0.
C3E977_ReadCharacterInventorySlotByte:
    rep #$31
    phd
    pha
    tdc
    adc #$FFF2
    tcd
    pla
    txy                              ; slot id from X
    tax                              ; character id from A
    tya
    dec A
    sta $02                          ; zero-based slot index
    txa
    dec A                            ; zero-based character index
    ldy #CHARACTER_RECORD_STRIDE
    jsl C08FF7_Multiply16
    clc
    adc #CHARACTER_INVENTORY_BASE
    clc
    adc $02
    tax
    lda $0000,X
    and #$00FF
    pld
    rtl

; ---------------------------------------------------------------------------
; C3:E9A0

; CheckEquippedInventorySlotReference
;
; Entry:
;   A = 1-based character id
;   X = equipped inventory-slot reference byte to search for
;
; Return:
;   A = 1 if any of $99FF..$9A02 in the character record equals X, else 0
C3E9A0_CheckEquippedInventorySlotReference:
    rep #$31
    phd
    pha
    tdc
    adc #$FFF2
    tcd
    pla
    stx $02                          ; requested slot reference
    tax
    dec A
    ldy #CHARACTER_RECORD_STRIDE
    jsl C08FF7_Multiply16
    tax
    lda EQUIPPED_SLOT_REFERENCE_BASE,X
    and #$00FF
    cmp $02
    bne C3E9C5_CheckEquippedInventorySlotReference_CheckSlot1
    lda #$0001
    bra C3E9F5_CheckEquippedInventorySlotReference_Return

C3E9C5_CheckEquippedInventorySlotReference_CheckSlot1:
    lda EQUIPPED_SLOT_REFERENCE_BASE + 1,X
    and #$00FF
    cmp $02
    bne C3E9D4_CheckEquippedInventorySlotReference_CheckSlot2
    lda #$0001
    bra C3E9F5_CheckEquippedInventorySlotReference_Return

C3E9D4_CheckEquippedInventorySlotReference_CheckSlot2:
    lda EQUIPPED_SLOT_REFERENCE_BASE + 2,X
    and #$00FF
    cmp $02
    bne C3E9E3_CheckEquippedInventorySlotReference_CheckSlot3
    lda #$0001
    bra C3E9F5_CheckEquippedInventorySlotReference_Return

C3E9E3_CheckEquippedInventorySlotReference_CheckSlot3:
    lda EQUIPPED_SLOT_REFERENCE_BASE + 3,X
    and #$00FF
    cmp $02
    bne C3E9F2_CheckEquippedInventorySlotReference_False
    lda #$0001
    bra C3E9F5_CheckEquippedInventorySlotReference_Return

C3E9F2_CheckEquippedInventorySlotReference_False:
    lda #$0000

C3E9F5_CheckEquippedInventorySlotReference_Return:
    pld
    rtl

; ---------------------------------------------------------------------------
; C3:E9F7

; CheckEquippedInventoryItemPresence
;
; Entry:
;   A = 1-based character id
;   X = concrete item id to search for
;
; Return:
;   A = 1 if any nonzero equipped slot reference dereferences to the requested
;       item id in that character's inventory, else 0
C3E9F7_CheckEquippedInventoryItemPresence:
    rep #$31
    phd
    pha
    tdc
    adc #$FFF0
    tcd
    pla
    stx $02                          ; requested item id
    tax
    txy
    dey
    sty $0E                          ; zero-based character index
    tya
    ldy #CHARACTER_RECORD_STRIDE
    jsl C08FF7_Multiply16
    tax
    lda EQUIPPED_SLOT_REFERENCE_BASE,X
    and #$00FF
    beq C3EA38_CheckEquippedInventoryItemPresence_CheckEquip1
    and #$00FF
    dec A
    sta $04
    txa
    clc
    adc #CHARACTER_INVENTORY_BASE
    clc
    adc $04
    tax
    lda $0000,X
    and #$00FF
    cmp $02
    bne C3EA38_CheckEquippedInventoryItemPresence_CheckEquip1
    lda #$0001
    jmp C3EACE_CheckEquippedInventoryItemPresence_Return

C3EA38_CheckEquippedInventoryItemPresence_CheckEquip1:
    ldy $0E
    tya
    ldy #CHARACTER_RECORD_STRIDE
    jsl C08FF7_Multiply16
    tax
    lda EQUIPPED_SLOT_REFERENCE_BASE + 1,X
    and #$00FF
    beq C3EA69_CheckEquippedInventoryItemPresence_CheckEquip2
    and #$00FF
    dec A
    sta $04
    txa
    clc
    adc #CHARACTER_INVENTORY_BASE
    clc
    adc $04
    tax
    lda $0000,X
    and #$00FF
    cmp $02
    bne C3EA69_CheckEquippedInventoryItemPresence_CheckEquip2
    lda #$0001
    bra C3EACE_CheckEquippedInventoryItemPresence_Return

C3EA69_CheckEquippedInventoryItemPresence_CheckEquip2:
    ldy $0E
    tya
    ldy #CHARACTER_RECORD_STRIDE
    jsl C08FF7_Multiply16
    tax
    lda EQUIPPED_SLOT_REFERENCE_BASE + 2,X
    and #$00FF
    beq C3EA9A_CheckEquippedInventoryItemPresence_CheckEquip3
    and #$00FF
    dec A
    sta $04
    txa
    clc
    adc #CHARACTER_INVENTORY_BASE
    clc
    adc $04
    tax
    lda $0000,X
    and #$00FF
    cmp $02
    bne C3EA9A_CheckEquippedInventoryItemPresence_CheckEquip3
    lda #$0001
    bra C3EACE_CheckEquippedInventoryItemPresence_Return

C3EA9A_CheckEquippedInventoryItemPresence_CheckEquip3:
    ldy $0E
    tya
    ldy #CHARACTER_RECORD_STRIDE
    jsl C08FF7_Multiply16
    tax
    lda EQUIPPED_SLOT_REFERENCE_BASE + 3,X
    and #$00FF
    beq C3EACB_CheckEquippedInventoryItemPresence_False
    and #$00FF
    dec A
    sta $04
    txa
    clc
    adc #CHARACTER_INVENTORY_BASE
    clc
    adc $04
    tax
    lda $0000,X
    and #$00FF
    cmp $02
    bne C3EACB_CheckEquippedInventoryItemPresence_False
    lda #$0001
    bra C3EACE_CheckEquippedInventoryItemPresence_Return

C3EACB_CheckEquippedInventoryItemPresence_False:
    lda #$0000

C3EACE_CheckEquippedInventoryItemPresence_Return:
    pld
    rtl

; ---------------------------------------------------------------------------
; C3:EAD0

; RefreshEggFamilyLifecycleOnInsert
;
; Entry:
;   A = inserted item id, low byte significant
C3EAD0_RefreshEggFamilyLifecycleOnInsert:
    rep #$31
    phd
    pha
    tdc
    adc #$FFF0
    tcd
    pla
    sep #$20
    sta $00                          ; inserted item id
    ldx #$0000
    stx $0E                          ; timed-item row index
    bra C3EB07_RefreshEggFamilyLifecycleOnInsert_LoadRow

C3EAE5_RefreshEggFamilyLifecycleOnInsert_CheckRow:
    sep #$20
    cmp $00
    bne C3EB02_RefreshEggFamilyLifecycleOnInsert_NextRow
    ldx $0E
    rep #$20
    txa
    jsl C48ECE_IsTrackedItemPulseActive
    cmp #$0000
    bne C3EB1A_RefreshEggFamilyLifecycleOnInsert_Return
    ldx $0E
    txa
    jsl C48EEB_ArmTrackedItemPulse
    bra C3EB1A_RefreshEggFamilyLifecycleOnInsert_Return

C3EB02_RefreshEggFamilyLifecycleOnInsert_NextRow:
    ldx $0E
    inx
    stx $0E

C3EB07_RefreshEggFamilyLifecycleOnInsert_LoadRow:
    rep #$20
    txa
    sta $04
    asl A
    asl A
    adc $04                          ; row_index * 5
    tax
    lda TIMED_ITEM_TRANSFORMATION_TABLE,X
    and #$00FF
    bne C3EAE5_RefreshEggFamilyLifecycleOnInsert_CheckRow

C3EB1A_RefreshEggFamilyLifecycleOnInsert_Return:
    pld
    rtl

; ---------------------------------------------------------------------------
; C3:EB1C

; RefreshEggFamilyLifecycleOnRemove
;
; Entry:
;   A = removed item id, low byte significant
C3EB1C_RefreshEggFamilyLifecycleOnRemove:
    rep #$31
    phd
    pha
    tdc
    adc #$FFEA
    tcd
    pla
    sep #$20
    sta $00                          ; removed item id
    ldy #$0000
    sty $14                          ; matched timed-item row index
    bra C3EB34_RefreshEggFamilyLifecycleOnRemove_LoadTimedRow

C3EB31_RefreshEggFamilyLifecycleOnRemove_NextTimedRow:
    iny
    sty $14

C3EB34_RefreshEggFamilyLifecycleOnRemove_LoadTimedRow:
    rep #$20
    tya
    sta $04
    asl A
    asl A
    adc $04                          ; row_index * 5
    tax
    lda TIMED_ITEM_TRANSFORMATION_TABLE,X
    and #$00FF
    beq C3EB4D_RefreshEggFamilyLifecycleOnRemove_ClearPulse
    sep #$20
    cmp $00
    bne C3EB31_RefreshEggFamilyLifecycleOnRemove_NextTimedRow

C3EB4D_RefreshEggFamilyLifecycleOnRemove_ClearPulse:
    rep #$20
    tya
    jsl C48F98_ClearTrackedItemPulse
    ldx #$0000
    stx $12                          ; active party index
    bra C3EBBB_RefreshEggFamilyLifecycleOnRemove_CheckPartyBounds

C3EB5B_RefreshEggFamilyLifecycleOnRemove_ScanPartyMember:
    lda ACTIVE_PARTY_TYPE_ARRAY,X
    and #$00FF
    dec A
    ldy #CHARACTER_RECORD_STRIDE
    jsl C08FF7_Multiply16
    clc
    adc #$99CE                       ; inventory base minus $23 slot offset
    sta $04
    lda #$0000
    sta $02
    sta $10                          ; inventory slot index
    bra C3EB98_RefreshEggFamilyLifecycleOnRemove_CheckSlotBounds

C3EB78_RefreshEggFamilyLifecycleOnRemove_CheckFoundItem:
    lda $00
    and #$00FF
    sta $02
    lda $0E
    cmp $02
    bne C3EB8E_RefreshEggFamilyLifecycleOnRemove_NextSlot
    ldy $14
    tya
    jsl C48EEB_ArmTrackedItemPulse
    bra C3EBC8_RefreshEggFamilyLifecycleOnRemove_Return

C3EB8E_RefreshEggFamilyLifecycleOnRemove_NextSlot:
    lda $10
    sta $02
    inc $02
    lda $02
    sta $10

C3EB98_RefreshEggFamilyLifecycleOnRemove_CheckSlotBounds:
    lda #ACTIVE_INVENTORY_SLOT_COUNT
    clc
    sbc $02                          ; original signed/overflow loop test
    bvc C3EBA4_RefreshEggFamilyLifecycleOnRemove_NoOverflow
    bpl C3EBB6_RefreshEggFamilyLifecycleOnRemove_NextPartyMember
    bra C3EBA6_RefreshEggFamilyLifecycleOnRemove_LoadSlot

C3EBA4_RefreshEggFamilyLifecycleOnRemove_NoOverflow:
    bmi C3EBB6_RefreshEggFamilyLifecycleOnRemove_NextPartyMember

C3EBA6_RefreshEggFamilyLifecycleOnRemove_LoadSlot:
    lda $04
    clc
    adc $02
    tax
    lda $0023,X
    and #$00FF
    sta $0E
    bne C3EB78_RefreshEggFamilyLifecycleOnRemove_CheckFoundItem

C3EBB6_RefreshEggFamilyLifecycleOnRemove_NextPartyMember:
    ldx $12
    inx
    stx $12

C3EBBB_RefreshEggFamilyLifecycleOnRemove_CheckPartyBounds:
    lda ACTIVE_PARTY_TYPE_COUNT
    and #$00FF
    sta $02
    txa
    cmp $02
    bcc C3EB5B_RefreshEggFamilyLifecycleOnRemove_ScanPartyMember

C3EBC8_RefreshEggFamilyLifecycleOnRemove_Return:
    pld
    rtl

; ---------------------------------------------------------------------------
; C3:EBCA

; SyncPartyOverlayTrackedItemFamilyState
;
; Entry:
;   No meaningful caller input.
;
; Width note:
;   The pointer rebuild at C3:EC00 is M16 in the real flow. The immediately
;   preceding branch calls C3:EAD0 or C3:EB1C, and both callees return with
;   M16 before execution reaches C3:EBFB/C3:EC00.
C3EBCA_SyncPartyOverlayTrackedItemFamilyState:
    rep #$31
    phd
    tdc
    adc #$FFF0
    tcd
    ldy #$0000
    sty $0E                          ; timed-item row index
    bra C3EC00_SyncPartyOverlayTrackedItemFamilyState_LoadRow

C3EBD9_SyncPartyOverlayTrackedItemFamilyState_CheckPresence:
    and #$00FF
    tax
    lda #NO_ACTIVE_INVENTORY_SELECTOR
    jsl C45683_CheckActiveInventoryForItem
    cmp #$0000
    beq C3EBF3_SyncPartyOverlayTrackedItemFamilyState_HandleAbsent
    sep #$20
    lda [$06]
    jsl C3EAD0_RefreshEggFamilyLifecycleOnInsert
    bra C3EBFB_SyncPartyOverlayTrackedItemFamilyState_NextRow

C3EBF3_SyncPartyOverlayTrackedItemFamilyState_HandleAbsent:
    sep #$20
    lda [$06]
    jsl C3EB1C_RefreshEggFamilyLifecycleOnRemove

C3EBFB_SyncPartyOverlayTrackedItemFamilyState_NextRow:
    ldy $0E
    iny
    sty $0E

C3EC00_SyncPartyOverlayTrackedItemFamilyState_LoadRow:
    lda #TIMED_ITEM_TABLE_LOW
    sta $06
    lda #TIMED_ITEM_TABLE_BANK
    sta $08
    tya
    sta $04
    asl A
    asl A
    adc $04                          ; row_index * 5
    clc
    adc $06
    sta $06
    lda [$06]
    and #$00FF
    bne C3EBD9_SyncPartyOverlayTrackedItemFamilyState_CheckPresence
    pld
    rtl
