; EarthBound C1 item-name printer from the item configuration table.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Hand-polished from tools/emit_linear_source_module.py output, then
;   intended for byte-equivalence validation.
;
; Source unit covered:
; - C1:9216..C1:9249 PrintItemNameFromConfigurationTable

C08FF7_ResolveIndexedPointerOffset          = $C08FF7
C4487C_PrintSegmentedStringBufferWithWrapPreflight = $C4487C

ItemConfigurationTableLo   = $5000
ItemConfigurationTableBank = $00D5
ItemConfigurationRecordSize = $0027
ItemNameByteCount = $0019

ItemId = $12
SourcePointerLo = $06
SourcePointerBank = $08
PrintPointerLo = $0E
PrintPointerBank = $10

; ---------------------------------------------------------------------------
; C1:9216

C19216_PrintItemNameFromConfigurationTable:
    rep #$31
    phd
    pha
    tdc
    adc.w #$FFEC
    tcd
    pla
    sta ItemId
    lda.w #ItemConfigurationTableLo
    sta SourcePointerLo
    lda.w #ItemConfigurationTableBank
    sta SourcePointerBank
    lda ItemId
    ldy.w #ItemConfigurationRecordSize
    jsl C08FF7_ResolveIndexedPointerOffset
    clc
    adc SourcePointerLo
    sta SourcePointerLo
    sta PrintPointerLo
    lda SourcePointerBank
    sta PrintPointerBank
    lda.w #ItemNameByteCount
    jsl C4487C_PrintSegmentedStringBufferWithWrapPreflight
    pld
    rts
