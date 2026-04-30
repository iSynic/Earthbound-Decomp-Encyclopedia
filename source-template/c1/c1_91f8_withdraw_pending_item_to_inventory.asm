; EarthBound C1 pending-item inventory withdrawal wrapper.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Hand-polished from tools/emit_linear_source_module.py output, then
;   intended for byte-equivalence validation.
;
; Source unit covered:
; - C1:91F8..C1:9216 WithdrawPendingItemToInventory

; ---------------------------------------------------------------------------
; External contracts used by this module

C191B0_RemovePendingItemIdAtIndex       = $91B0
C18BC6_InsertItemIntoCharacterInventory = $C18BC6

SavedCharacterIndex = $0E

; ---------------------------------------------------------------------------
; C1:91F8

C191F8_WithdrawPendingItemToInventory:
    rep #$31
    phd
    pha
    tdc
    adc.w #$FFF0
    tcd
    pla
    tay
    sty SavedCharacterIndex
    txa
    jsr C191B0_RemovePendingItemIdAtIndex
    tax
    ldy SavedCharacterIndex
    tya
    jsl C18BC6_InsertItemIntoCharacterInventory
    ldy SavedCharacterIndex
    tya
    pld
    rts
