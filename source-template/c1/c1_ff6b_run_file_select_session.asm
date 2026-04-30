; EarthBound C1 file-select session runner.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Hand-polished from tools/emit_linear_source_module.py output, then
;   intended for byte-equivalence validation.
;
; Source unit covered:
; - C1:FF6B..C1:FF99 RunFileSelectSession

C1F805_RunFileSelectLoop       = $F805
C3E4CA_ClearInstantPrinting    = $C3E4CA
C12DD5_TickWindowTextSystem    = $C12DD5

AutoWrapPreflightGate          = $5E6E
FileSelectSessionActiveFlag    = $B49D
FileSelectPendingAction        = $B4B6
FileSelectTransientState       = $B4A2

; ---------------------------------------------------------------------------
; C1:FF6B

C1FF6B_RunFileSelectSession:
    rep #$31
    stz AutoWrapPreflightGate
    sep #$20
    lda.b #$01
    sta FileSelectSessionActiveFlag
    jsr C1F805_RunFileSelectLoop
    jsl C3E4CA_ClearInstantPrinting
    jsl C12DD5_TickWindowTextSystem
    stz FileSelectPendingAction
    stz FileSelectTransientState
    lda.w #$00FF
    sta AutoWrapPreflightGate
    sep #$20
    stz FileSelectSessionActiveFlag
    rep #$20
    lda.w #$0000
    rtl
