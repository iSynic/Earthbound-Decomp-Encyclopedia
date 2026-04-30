; EarthBound C1 managed text-event slot snapshot applier.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Hand-polished from tools/emit_linear_source_module.py output, then
;   intended for byte-equivalence validation.
;
; Source unit covered:
; - C1:869D..C1:86B1 ApplyActiveManagedTextEventSlotSnapshot

; ---------------------------------------------------------------------------
; External contracts used by this module

C20ABC_ApplyManagedTextEventSnapshot = $C20ABC

ManagedTextEventSnapshotOffset = $0006

; ---------------------------------------------------------------------------
; C1:869D

C1869D_ApplyActiveManagedTextEventSlotSnapshot:
    rep #$31
    tax
    beq C186B0_ReturnFromManagedTextEventSnapshot

    lda $0004,X
    beq C186B0_ReturnFromManagedTextEventSnapshot

    txa
    clc
    adc.w #ManagedTextEventSnapshotOffset
    jsl C20ABC_ApplyManagedTextEventSnapshot

C186B0_ReturnFromManagedTextEventSnapshot:
    rts
