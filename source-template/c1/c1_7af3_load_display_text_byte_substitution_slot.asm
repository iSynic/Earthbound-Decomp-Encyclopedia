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

TextContextSourcePointerLo = $0E
TextContextSourcePointerHi = $10
ScratchValueLo             = $06
ScratchValueByte1          = $07
ScratchValueHi             = $08
ScratchValueByte3          = $09

; ---------------------------------------------------------------------------
; C1:7AF3

C17AF3_LoadDisplayTextByteSubstitutionSlot:
    jsr C1AD02_ReadBattleTextSubstitutionByte
    sta ScratchValueLo
    stz ScratchValueByte1
    stz ScratchValueHi
    stz ScratchValueByte3
    rep #$20
    lda ScratchValueLo
    sta TextContextSourcePointerLo
    lda ScratchValueHi
    sta TextContextSourcePointerHi
    jsr C1045D_InstallPrimaryInteractionContextPointer
    bra C17B51_DisplayTextSubstitutionSharedContinuation
