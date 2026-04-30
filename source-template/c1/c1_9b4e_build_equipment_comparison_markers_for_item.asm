; EarthBound C1 equipment comparison marker builder entry.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Hand-polished from tools/emit_linear_source_module.py output, then
;   intended for byte-equivalence validation.
;
; Source unit covered:
; - C1:9B4E..C1:9B79 BuildEquipmentComparisonMarkersForItem

C19CB6_ContinueEquipmentComparisonMarkerBuild = $9CB6
C19CCB_RunEquipmentComparisonMarkerLoop       = $9CCB
C3EE14_TestEquipmentCompatibilityForCharacter = $C3EE14

ItemId = $04
ComparisonMarkerAccumulator = $10
ComparisonLoopIndex = $12
ComparisonMarkerForCannotEquip = $0C00

; ---------------------------------------------------------------------------
; C1:9B4E

C19B4E_BuildEquipmentComparisonMarkersForItem:
    rep #$31
    phd
    pha
    tdc
    adc.w #$FFEC
    tcd
    pla
    sta ItemId
    ldy.w #$0000
    sty ComparisonLoopIndex
    jmp C19CCB_RunEquipmentComparisonMarkerLoop

C19B61_TestNextEquipmentComparisonCandidate:
    ldx ItemId
    tya
    inc A
    jsl C3EE14_TestEquipmentCompatibilityForCharacter
    cmp.w #$0000
    bne C19B77_ReturnItemIdForEquipmentComparisonMarker

    lda.w #ComparisonMarkerForCannotEquip
    sta ComparisonMarkerAccumulator
    jmp C19CB6_ContinueEquipmentComparisonMarkerBuild

C19B77_ReturnItemIdForEquipmentComparisonMarker:
    lda ItemId
