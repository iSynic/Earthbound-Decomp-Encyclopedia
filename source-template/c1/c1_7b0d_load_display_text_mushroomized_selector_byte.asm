; EarthBound C1 display-text dynamic source loaders.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Hand-polished from tools/emit_linear_source_module.py output, then
;   intended for byte-equivalence validation.
;
; Source unit covered:
; - C1:7B0D..C1:7B56 LoadDisplayTextMushroomizedSelectorByte

; ---------------------------------------------------------------------------
; External contracts used by this module

C1045D_InstallPrimaryInteractionContextPointer = $045D

TextContextSourcePointerLo = $0E
TextContextSourcePointerHi = $10
ScratchValueLo             = $06
ScratchValueByte1          = $07
ScratchValueHi             = $08
ScratchValueByte3          = $09
MushroomizedSelectorByte   = $98A4

; ---------------------------------------------------------------------------
; C1:7B0D

C17B0D_LoadDisplayTextMushroomizedSelectorByte:
    sep #$20
    lda MushroomizedSelectorByte
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

C17B29_LoadDisplayTextStaticPointer6143:
    lda.w #$6143
    bra C17B54_ReturnDisplayTextStaticPointer

C17B2E_LoadDisplayTextStaticPointer68A0:
    lda.w #$68A0
    bra C17B54_ReturnDisplayTextStaticPointer

C17B33_LoadDisplayTextStaticPointer6947:
    lda.w #$6947
    bra C17B54_ReturnDisplayTextStaticPointer

C17B38_LoadDisplayTextStaticPointer6A7B:
    lda.w #$6A7B
    bra C17B54_ReturnDisplayTextStaticPointer

C17B3D_LoadDisplayTextStaticPointer6F9F:
    lda.w #$6F9F
    bra C17B54_ReturnDisplayTextStaticPointer

C17B42_LoadDisplayTextStaticPointer7037:
    lda.w #$7037
    bra C17B54_ReturnDisplayTextStaticPointer

C17B47_LoadDisplayTextStaticPointer776A:
    lda.w #$776A
    bra C17B54_ReturnDisplayTextStaticPointer

C17B4C_LoadDisplayTextStaticPointer4819:
    lda.w #$4819
    bra C17B54_ReturnDisplayTextStaticPointer

C17B51_DisplayTextSubstitutionSharedContinuation:
    lda.w #$0000

C17B54_ReturnDisplayTextStaticPointer:
    pld
    rts
