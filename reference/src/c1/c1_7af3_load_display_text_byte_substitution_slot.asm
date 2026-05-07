; EarthBound C1 display-text byte substitution source loader.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Hand-polished from tools/emit_linear_source_module.py output, then
;   intended for byte-equivalence validation.
;
; Source unit covered:
; - C1:7AF3..C1:7B0D LoadDisplayTextByteSubstitutionSlot

; ---------------------------------------------------------------------------
; External contracts used by this module

C1045D_InstallPrimaryInteractionContextPointer = $045D
C1AD02_ReadBattleTextSubstitutionByte          = $AD02

TextContextSourcePointerLo     = $0E
TextContextSourcePointerHi     = $10
LoadedSubstitutionValueLo      = $06
LoadedSubstitutionValueByte1   = $07
LoadedSubstitutionValueHi      = $08
LoadedSubstitutionValueByte3   = $09
AccumulatorWidthFlag           = $20

; ---------------------------------------------------------------------------
; C1:7AF3

C17AF3_LoadDisplayTextByteSubstitutionSlot:
    jsr C1AD02_ReadBattleTextSubstitutionByte
    sta LoadedSubstitutionValueLo
    stz LoadedSubstitutionValueByte1
    stz LoadedSubstitutionValueHi
    stz LoadedSubstitutionValueByte3
    rep #AccumulatorWidthFlag
    lda LoadedSubstitutionValueLo
    sta TextContextSourcePointerLo
    lda LoadedSubstitutionValueHi
    sta TextContextSourcePointerHi
    jsr SET_WORKING_MEMORY
    bra C17B51_DisplayTextSubstitutionSharedContinuation
