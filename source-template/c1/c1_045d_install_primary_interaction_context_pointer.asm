; EarthBound C1 primary interaction/text context pointer installer.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Hand-polished from tools/emit_linear_source_module.py output, then
;   intended for byte-equivalence validation.
;
; Source unit covered:
; - C1:045D..C1:0489 InstallPrimaryInteractionContextPointer

; ---------------------------------------------------------------------------
; External contracts used by this module

C10301_GetActiveInteractionContextRecord = $0301

ContextPrimaryPointerOffset = $0017
ScratchPointerLo            = $06
ScratchPointerHi            = $08
CurrentTextPointerLo        = $14
CurrentTextPointerHi        = $16
StagedTextPointerLo         = $1C
StagedTextPointerHi         = $1E

; ---------------------------------------------------------------------------
; C1:045D

C1045D_InstallPrimaryInteractionContextPointer:
    rep #$31
    phd
    tdc
    adc.w #$FFF2
    tcd
    lda StagedTextPointerLo
    sta ScratchPointerLo
    lda StagedTextPointerHi
    sta ScratchPointerHi
    jsr C10301_GetActiveInteractionContextRecord
    clc
    adc.w #ContextPrimaryPointerOffset
    tay
    lda ScratchPointerLo
    sta $0000,Y
    lda ScratchPointerHi
    sta $0002,Y
    lda ScratchPointerLo
    sta CurrentTextPointerLo
    lda ScratchPointerHi
    sta CurrentTextPointerHi
    pld
    rts
