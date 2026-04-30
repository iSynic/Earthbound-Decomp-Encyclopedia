; EarthBound C3 equipment and battle selector helper prototype.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Assembler contract: pilot-ready
; - Assembler-ready pilot; not yet linked into a full assembler ROM build.
; - Derived from notes/c3-source-emission-plan.md and
;   notes/c3-equipment-selector-source-contract-ee14-ef22.md.
; - Build-candidate conventions are documented in
;   notes/c3-build-candidate-source-conventions.md.
; - Original instruction flow is preserved in address order with symbolic
;   comments for local direct-page variables, WRAM fields, and selector kinds.
; - ROM byte range, SHA-1, and source signature are tracked by
;   build/c3-build-candidate-ranges.json and
;   build/c3-source-signature-validation.json.
;
; Source units covered:
; - C3:EE14..C3:EE4D CheckItemEquipmentSlotCompatibility
; - C3:EE4D..C3:EE7A RefreshWorldAndReleaseActiveVisualHandle
; - C3:EE7A..C3:EF23 ResolveStatisticSelectorValue
;
; Evidence:
; - notes/c3-equipment-selector-source-contract-ee14-ef22.md
; - notes/item-slot-helper-pair-c3e977-c3ee14.md
; - notes/statistic-selector-family-c4550f-c3ee7a.md
; - notes/equipment-comparison-markers-9a1d.md

; ---------------------------------------------------------------------------
; External contracts used by this module

C08FF7_Multiply16                              = $C08FF7
C034D6_SortAndExport_MushroomizedWalkingEntries = $C034D6
C07B52_RefreshVisibleEntityScreenPositions    = $C07B52
C1004E_PumpTextWaitFrame                      = $C1004E
C0943C_MarkWorldObjectChainForSetup           = $C0943C

; C0:8FF7 Multiply16
;   Input:  A = multiplicand, Y = multiplier
;   Output: A = product

; C0:34D6 SortAndExport_MushroomizedWalkingEntries
; C0:7B52 Refresh_VisibleEntityScreenPositions
; C1:004E PumpTextWaitFrame
; C0:943C MarkWorldObjectChainForSetup

; ---------------------------------------------------------------------------
; Local data contracts and WRAM fields

ITEM_CONFIGURATION_TABLE        = $D55000
ITEM_CONFIGURATION_STRIDE       = $0027
ITEM_EQUIPMENT_MASK_OFFSET      = $001C

EQUIPMENT_SLOT_MASK_TABLE       = $C458AB
STATISTIC_SELECTOR_TABLE_LOW    = $550F
STATISTIC_SELECTOR_TABLE_BANK   = $00C4
STATISTIC_SELECTOR_RECORD_SIZE  = $0003

ACTIVE_VISUAL_HANDLE            = $B4A8
WORLD_OBJECT_FLAGS_BASE         = $10B6
WORLD_OBJECT_SETUP_BITS_MASK    = $3FFF
NO_ACTIVE_VISUAL_HANDLE         = $FFFF

STAT_SELECTOR_KIND_HIGH_BIT     = $0080
STAT_SELECTOR_KIND_BYTE_SCALAR  = $0001
STAT_SELECTOR_KIND_WORD_SCALAR  = $0002

; Shared statistic-selector locals:
;   $04 = selector index scratch
;   $06/$08 = table pointer or resolved result pair
;   $0A/$0C = computed long pointer to table row
;   $0E = selector kind byte
;   $16/$18 = final stores that become caller $06/$08 after PLD

; ---------------------------------------------------------------------------
; C3:EE14

; CheckItemEquipmentSlotCompatibility
;
; Entry:
;   A = 1-based equipment-slot selector
;   X = 1-based item id
;
; Return:
;   A = 1 if item byte +$1C intersects the selected equipment-slot mask,
;       otherwise 0
C3EE14_CheckItemEquipmentSlotCompatibility:
    rep #$31
    phd
    pha
    tdc
    adc #$FFF0
    tcd
    pla
    txy                              ; preserve item id from X into Y
    tax                              ; slot selector from A
    stx $0E
    tya                              ; item id
    ldy #ITEM_CONFIGURATION_STRIDE
    jsl C08FF7_Multiply16
    clc
    adc #ITEM_EQUIPMENT_MASK_OFFSET
    tax
    sep #$20
    lda ITEM_CONFIGURATION_TABLE,X
    ldx $0E
    dex
    and EQUIPMENT_SLOT_MASK_TABLE,X
    rep #$20
    and #$00FF
    beq C3EE48_CheckItemEquipmentSlotCompatibility_False
    lda #$0001
    bra C3EE4B_CheckItemEquipmentSlotCompatibility_Return

C3EE48_CheckItemEquipmentSlotCompatibility_False:
    lda #$0000

C3EE4B_CheckItemEquipmentSlotCompatibility_Return:
    pld
    rtl

; ---------------------------------------------------------------------------
; C3:EE4D

; RefreshWorldAndReleaseActiveVisualHandle
;
; Entry:
;   No meaningful caller input.
;
; Behavior:
;   Runs a shared world/text refresh chain, then clears the high setup bits on
;   the active visual/presentation handle when one exists.
C3EE4D_RefreshWorldAndReleaseActiveVisualHandle:
    rep #$31
    jsl C034D6_SortAndExport_MushroomizedWalkingEntries
    jsl C07B52_RefreshVisibleEntityScreenPositions
    jsl C1004E_PumpTextWaitFrame
    jsl C0943C_MarkWorldObjectChainForSetup
    lda ACTIVE_VISUAL_HANDLE
    cmp #NO_ACTIVE_VISUAL_HANDLE
    beq C3EE79_RefreshWorldAndReleaseActiveVisualHandle_Return
    lda ACTIVE_VISUAL_HANDLE
    asl A
    clc
    adc #WORLD_OBJECT_FLAGS_BASE
    tax
    lda $0000,X
    and #WORLD_OBJECT_SETUP_BITS_MASK
    sta $0000,X

C3EE79_RefreshWorldAndReleaseActiveVisualHandle_Return:
    rtl

; ---------------------------------------------------------------------------
; C3:EE7A

; ResolveStatisticSelectorValue
;
; Entry:
;   A = statistic selector index
;
; Return:
;   caller $06 = low word or pointer low word
;   caller $08 = high word, pointer bank/high word, or zero
;
; Direct-page note:
;   The routine lowers D by $10. Final writes to local $16/$18 therefore land
;   in the caller's $06/$08 after PLD restores the caller's direct page.
C3EE7A_ResolveStatisticSelectorValue:
    rep #$31
    phd
    pha
    tdc
    adc #$FFF0
    tcd
    pla
    sta $0E                         ; selector index
    lda #STATISTIC_SELECTOR_TABLE_LOW
    sta $06
    lda #STATISTIC_SELECTOR_TABLE_BANK
    sta $08
    lda $0E
    sta $04
    asl A
    adc $04                         ; selector * 3
    tax
    ldy $06
    sty $0A
    ldy $08
    sty $0C
    clc
    adc $0A
    sta $0A                         ; $0A/$0C -> selector record
    lda [$0A]
    and #$00FF
    sta $0E                         ; kind byte
    and #STAT_SELECTOR_KIND_HIGH_BIT
    beq C3EF04_ResolveStatisticSelectorValue_InlinePointer

    lda $0E
    and #$007F
    cmp #STAT_SELECTOR_KIND_BYTE_SCALAR
    beq C3EEC2_ResolveStatisticSelectorValue_IndirectByte
    cmp #STAT_SELECTOR_KIND_WORD_SCALAR
    beq C3EEDB_ResolveStatisticSelectorValue_IndirectWord
    bra C3EEEE_ResolveStatisticSelectorValue_IndirectPointer

C3EEC2_ResolveStatisticSelectorValue_IndirectByte:
    txa
    inc A
    clc
    adc $06
    sta $06
    lda [$06]                       ; payload word address
    tax
    sep #$20
    lda $0000,X
    sta $06
    stz $07
    stz $08
    stz $09
    bra C3EF17_ResolveStatisticSelectorValue_StoreResult

C3EEDB_ResolveStatisticSelectorValue_IndirectWord:
    txa
    inc A
    clc
    adc $06
    sta $06
    lda [$06]                       ; payload word address
    tax
    lda $0000,X
    sta $06
    stz $08
    bra C3EF17_ResolveStatisticSelectorValue_StoreResult

C3EEEE_ResolveStatisticSelectorValue_IndirectPointer:
    txa
    inc A
    clc
    adc $06
    sta $06
    lda [$06]                       ; payload word points at pointer pair
    tay
    lda $0000,Y
    sta $06
    lda $0002,Y
    sta $08
    bra C3EF17_ResolveStatisticSelectorValue_StoreResult

C3EF04_ResolveStatisticSelectorValue_InlinePointer:
    txa
    inc A
    clc
    adc $06
    sta $06
    lda [$06]                       ; inline payload word
    sta $06
    phb
    sep #$20
    pla
    sta $08                         ; current data bank
    stz $09

C3EF17_ResolveStatisticSelectorValue_StoreResult:
    rep #$20
    lda $06
    sta $16                         ; caller $06 after PLD
    lda $08
    sta $18                         ; caller $08 after PLD
    pld
    rtl
