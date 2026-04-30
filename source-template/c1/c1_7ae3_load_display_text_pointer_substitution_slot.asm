; EarthBound C1 display-text pointer substitution source loader.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Hand-polished from tools/emit_linear_source_module.py output, then
;   intended for byte-equivalence validation.
;
; Source unit covered:
; - C1:7AE3..C1:7AF3 LoadDisplayTextPointerSubstitutionSlot

; ---------------------------------------------------------------------------
; External contracts used by this module

C1045D_InstallPrimaryInteractionContextPointer = $045D
C1AD26_LoadBattleTextSubstitutionPointer       = $AD26

TextContextSourcePointerLo = $0E
TextContextSourcePointerHi = $10
ScratchPointerLo           = $06
ScratchPointerHi           = $08

; ---------------------------------------------------------------------------
; C1:7AE3

C17AE3_LoadDisplayTextPointerSubstitutionSlot:
    jsr C1AD26_LoadBattleTextSubstitutionPointer
    lda ScratchPointerLo
    sta TextContextSourcePointerLo
    lda ScratchPointerHi
    sta TextContextSourcePointerHi
    jsr C1045D_InstallPrimaryInteractionContextPointer
    bra C17B51_DisplayTextSubstitutionSharedContinuation
