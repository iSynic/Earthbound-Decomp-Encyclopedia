; EarthBound C1 pointer-backed text entry record bridge.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Hand-polished from tools/emit_linear_source_module.py output, then
;   intended for byte-equivalence validation.
;
; Source unit covered:
; - C1:0BFE..C1:0C49 CreatePointerBackedTextEntryRecord

; ---------------------------------------------------------------------------
; External contracts used by this module

C1153B_CreateTypedTextEntryRecord = $153B

CallerPrimaryPointerLo   = $2A
CallerPrimaryPointerBank = $2C
CallerExtraPointerLo     = $2E
CallerExtraPointerBank   = $30

InputTypeOrMode          = $1A
PrimaryPointerLo         = $0A
PrimaryPointerBank       = $0C
InstallPrimaryPointerLo  = $0E
InstallPrimaryPointerBank = $10
ExtraPointerLo           = $16
ExtraPointerBank         = $18
InstallExtraPointerLo    = $12
InstallExtraPointerBank  = $14
ScratchPointerLo         = $06
ScratchPointerBank       = $08

; ---------------------------------------------------------------------------
; C1:0BFE

C10BFE_CreatePointerBackedTextEntryRecord:
    rep #$31
    phd
    pha
    tdc
    adc.w #$FFE4
    tcd
    pla
    sta InputTypeOrMode
    lda CallerExtraPointerLo
    sta ScratchPointerLo
    lda CallerExtraPointerBank
    sta ScratchPointerBank
    lda ScratchPointerLo
    sta ExtraPointerLo
    lda ScratchPointerBank
    sta ExtraPointerBank
    lda CallerPrimaryPointerLo
    sta PrimaryPointerLo
    lda CallerPrimaryPointerBank
    sta PrimaryPointerBank
    lda PrimaryPointerLo
    sta ScratchPointerLo
    lda PrimaryPointerBank
    sta ScratchPointerBank
    lda ScratchPointerLo
    sta InstallPrimaryPointerLo
    lda ScratchPointerBank
    sta InstallPrimaryPointerBank
    lda ExtraPointerLo
    sta ScratchPointerLo
    lda ExtraPointerBank
    sta ScratchPointerBank
    lda ScratchPointerLo
    sta InstallExtraPointerLo
    lda ScratchPointerBank
    sta InstallExtraPointerBank
    lda InputTypeOrMode
    jsr C1153B_CreateTypedTextEntryRecord
    pld
    rtl
