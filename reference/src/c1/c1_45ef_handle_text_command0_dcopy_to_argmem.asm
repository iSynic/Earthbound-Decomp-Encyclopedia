; EarthBound C1 text command 0D pointer copy helper.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Hand-polished from tools/emit_linear_source_module.py output, then
;   intended for byte-equivalence validation.
;
; Source unit covered:
; - C1:45EF..C1:461A HandleTextCommand0DCopyToArgmem

C10400_GetCurrentTextContextWorkmem           = $0400
C1040A_LoadPrimaryInteractionContextPointer   = $040A
C10489_InstallSecondaryInteractionContextPointer = $0489

StagedPointerLo = $06
StagedPointerHi = $08
InstallPointerLo = $0E
InstallPointerHi = $10

; ---------------------------------------------------------------------------
; C1:45EF

CC_0D:
C145EF_HandleTextCommand0DCopyToArgmem = CC_0D
    rep #$31
    phd
    pha
    tdc
    adc.w #$FFEE
    tcd
    pla
    cpx.w #$0000
    beq C14607_LoadPrimaryPointerForTextCommand0D

    jsr GET_SECONDARY_MEMORY
    sta StagedPointerLo
    stz StagedPointerHi
    bra C1460A_InstallTextCommand0DSecondaryPointer

C14607_LoadPrimaryPointerForTextCommand0D:
    jsr GET_WORKING_MEMORY

C1460A_InstallTextCommand0DSecondaryPointer:
    lda StagedPointerLo
    sta InstallPointerLo
    lda StagedPointerHi
    sta InstallPointerHi
    jsr SET_ARGUMENT_MEMORY
    lda.w #$0000
    pld
    rts
