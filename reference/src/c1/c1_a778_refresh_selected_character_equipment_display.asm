; EarthBound C1 selected-character equipment display refresher.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Hand-polished from tools/emit_linear_source_module.py output, then
;   intended for byte-equivalence validation.
;
; Source unit covered:
; - C1:A778..C1:A795 RefreshSelectedCharacterEquipmentDisplay
;
; Runtime contract:
; - A = 1-based selected character id.
; - Clears the preview-ready latch `$9CD4`, renders the live equipment list,
;   then renders the status/preview panel for the same character.
; - This is the character-selection callback used by the top-level party
;   equipment menu.

; ---------------------------------------------------------------------------
; External contracts used by this module

C19F29_RenderSelectedCharacterEquipmentList = $9F29
C1A1D8_RenderEquipmentPreviewStatus         = $C1A1D8

SavedCharacterIndex          = $0E
EquipmentPreviewScratchLatch = $9CD4

; ---------------------------------------------------------------------------
; C1:A778

C1A778_RefreshSelectedCharacterEquipmentDisplay:
    rep #$31
    phd
    pha
    tdc
    adc.w #$FFF0
    tcd
    pla
    tax
    stx SavedCharacterIndex
    stz EquipmentPreviewScratchLatch
    txa
    jsr C19F29_RenderSelectedCharacterEquipmentList
    ldx SavedCharacterIndex
    txa
    jsl C1A1D8_RenderEquipmentPreviewStatus
    pld
    rtl
