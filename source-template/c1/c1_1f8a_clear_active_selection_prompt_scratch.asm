; EarthBound C1 active selection-prompt scratch clearer.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Hand-polished from tools/emit_linear_source_module.py output, then
;   intended for byte-equivalence validation.
;
; Source unit covered:
; - C1:1F8A..C1:1FBC ClearActiveSelectionPromptScratch

C08FF7_ResolveIndexedPointerOffset = $C08FF7

ActiveWindowFocus          = $8958
WindowDescriptorIndexTable = $88E4
WindowDescriptorSize       = $0052
SelectionPromptScratchSlot = $8687

ScratchPointerLo = $06
ScratchPointerHi = $08

; ---------------------------------------------------------------------------
; C1:1F8A

C11F8A_ClearActiveSelectionPromptScratch:
    rep #$31
    phd
    tdc
    adc.w #$FFF2
    tcd
    lda.w #$0000
    sta ScratchPointerLo
    lda.w #$0000
    sta ScratchPointerHi
    lda ActiveWindowFocus
    asl A
    tax
    lda WindowDescriptorIndexTable,X
    ldy.w #WindowDescriptorSize
    jsl C08FF7_ResolveIndexedPointerOffset
    clc
    adc.w #SelectionPromptScratchSlot
    tay
    lda ScratchPointerLo
    sta $0000,Y
    lda ScratchPointerHi
    sta $0002,Y
    pld
    rts
