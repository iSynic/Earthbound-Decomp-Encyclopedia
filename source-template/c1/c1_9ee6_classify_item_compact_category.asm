; EarthBound C1 compact item category classifier.
;
; Source units covered:
; - C1:9EE6..C1:9F29 ClassifyItemCompactCategory

C08FF7_ResolveIndexedPointerOffset = $C08FF7

ItemConfigurationTable = $D55000
ItemRecordStride = $0027
ItemPackedClassAndSlotOffset = $0019

; ---------------------------------------------------------------------------
; C1:9EE6

C19EE6_ClassifyItemCompactCategory:
    rep #$31
    ldy.w #ItemRecordStride
    jsl C08FF7_ResolveIndexedPointerOffset
    clc
    adc.w #ItemPackedClassAndSlotOffset
    tax
    lda ItemConfigurationTable,X
    and.w #$00FF
    and.w #$0030
    beq C19F11_ReturnGeneralItemClass
    cmp.w #$0010
    beq C19F16_ReturnEquipmentItemClass
    cmp.w #$0020
    beq C19F1B_ReturnFoodItemClass
    cmp.w #$0030
    beq C19F20_ReturnOtherUsableItemClass
    bra C19F25_ReturnUnknownItemClass

C19F11_ReturnGeneralItemClass:
    lda.w #$0001
    bra C19F28_ReturnCompactItemClass

C19F16_ReturnEquipmentItemClass:
    lda.w #$0002
    bra C19F28_ReturnCompactItemClass

C19F1B_ReturnFoodItemClass:
    lda.w #$0003
    bra C19F28_ReturnCompactItemClass

C19F20_ReturnOtherUsableItemClass:
    lda.w #$0004
    bra C19F28_ReturnCompactItemClass

C19F25_ReturnUnknownItemClass:
    lda.w #$0000

C19F28_ReturnCompactItemClass:
    rts
