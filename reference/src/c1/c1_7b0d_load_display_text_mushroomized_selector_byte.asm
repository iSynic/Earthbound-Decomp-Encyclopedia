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

TextContextSourcePointerLo                  = $0E
TextContextSourcePointerHi                  = $10
LoadedMushroomizedSelectorValueLo           = $06
LoadedMushroomizedSelectorValueByte1        = $07
LoadedMushroomizedSelectorValueHi           = $08
LoadedMushroomizedSelectorValueByte3        = $09
MushroomizedSelectorByte                    = $98A4
AccumulatorWidthFlag                        = $20
DisplayTextFoodCategoryHelper               = $6143
DisplayTextCharacterToObjectDirectionHelper = $68A0
DisplayTextNpcToObjectDirectionHelper       = $6947
DisplayTextGeneratedSpriteDirectionHelper   = $6A7B
DisplayTextFoodCondimentHelper              = $6F9F
DisplayTextTransitionLandingSnapshotHelper  = $7037
DisplayTextStatisticSelectorValueHelper     = $776A
DisplayTextStatisticSelectorCharacterHelper = $4819
ZeroWord                                    = $0000

; ---------------------------------------------------------------------------
; C1:7B0D

C17B0D_LoadDisplayTextMushroomizedSelectorByte:
    sep #AccumulatorWidthFlag
    lda MushroomizedSelectorByte
    sta LoadedMushroomizedSelectorValueLo
    stz LoadedMushroomizedSelectorValueByte1
    stz LoadedMushroomizedSelectorValueHi
    stz LoadedMushroomizedSelectorValueByte3
    rep #AccumulatorWidthFlag
    lda LoadedMushroomizedSelectorValueLo
    sta TextContextSourcePointerLo
    lda LoadedMushroomizedSelectorValueHi
    sta TextContextSourcePointerHi
    jsr SET_WORKING_MEMORY
    bra C17B51_DisplayTextSubstitutionSharedContinuation

C17B29_LoadDisplayTextFoodCategoryHelperPointer:
    lda.w #DisplayTextFoodCategoryHelper
    bra C17B54_ReturnDisplayTextStaticPointer

C17B2E_LoadDisplayTextCharacterToObjectDirectionHelperPointer:
    lda.w #DisplayTextCharacterToObjectDirectionHelper
    bra C17B54_ReturnDisplayTextStaticPointer

C17B33_LoadDisplayTextNpcToObjectDirectionHelperPointer:
    lda.w #DisplayTextNpcToObjectDirectionHelper
    bra C17B54_ReturnDisplayTextStaticPointer

C17B38_LoadDisplayTextGeneratedSpriteDirectionHelperPointer:
    lda.w #DisplayTextGeneratedSpriteDirectionHelper
    bra C17B54_ReturnDisplayTextStaticPointer

C17B3D_LoadDisplayTextFoodCondimentHelperPointer:
    lda.w #DisplayTextFoodCondimentHelper
    bra C17B54_ReturnDisplayTextStaticPointer

C17B42_LoadDisplayTextTransitionLandingSnapshotHelperPointer:
    lda.w #DisplayTextTransitionLandingSnapshotHelper
    bra C17B54_ReturnDisplayTextStaticPointer

C17B47_LoadDisplayTextStatisticSelectorValueHelperPointer:
    lda.w #DisplayTextStatisticSelectorValueHelper
    bra C17B54_ReturnDisplayTextStaticPointer

C17B4C_LoadDisplayTextStatisticSelectorCharacterHelperPointer:
    lda.w #DisplayTextStatisticSelectorCharacterHelper
    bra C17B54_ReturnDisplayTextStaticPointer

C17B51_DisplayTextSubstitutionSharedContinuation:
    lda.w #ZeroWord

C17B54_ReturnDisplayTextStaticPointer:
    pld
    rts
