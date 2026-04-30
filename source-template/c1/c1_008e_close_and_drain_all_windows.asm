; EarthBound C1 close and drain all windows helper.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Hand-shaped from ROM decode because this routine uses 8-bit accumulator
;   mode for the window-drain guard byte before returning to 16-bit work.
;
; Source units covered:
; - C1:008E..C1:00D6 CloseAndDrainAllWindows

; ---------------------------------------------------------------------------
; External contracts used by this module

C08FF7_ResolveIndexedPointerOffset = $C08FF7
C3E521_CloseWindowById             = $C3E521
C3E4CA_RefreshWindowTextState      = $C3E4CA
C12DD5_TickWindowTextSystem        = $C12DD5
C43F53_ClearWindowDrainSideEffects = $C43F53
WindowDrainGuard                   = $5E70
QueuedWindowIndex                  = $88E2
WindowDescriptorStride             = $0052
WindowDescriptorIdOffset           = $8654
NoQueuedWindow                     = $FFFF
InputLockFlag                      = $9645

; ---------------------------------------------------------------------------
; C1:008E

C1008E_CloseAndDrainAllWindows:
    rep #$31
    sep #$20
    lda.b #$01
    sta WindowDrainGuard
    bra C100AB_CheckQueuedWindow

C10099_CloseQueuedWindow:
    lda QueuedWindowIndex
    ldy.w #WindowDescriptorStride
    jsl C08FF7_ResolveIndexedPointerOffset
    tax
    lda WindowDescriptorIdOffset,X
    jsl C3E521_CloseWindowById

C100AB_CheckQueuedWindow:
    rep #$20
    lda QueuedWindowIndex
    cmp.w #NoQueuedWindow
    bne C10099_CloseQueuedWindow
    jsl C3E4CA_RefreshWindowTextState
    jsl C12DD5_TickWindowTextSystem
    sep #$20
    stz WindowDrainGuard
    jsl C43F53_ClearWindowDrainSideEffects
    rts

C100C7_LockTextInput:
    rep #$31
    lda.w #$0001
    sta InputLockFlag
    rts

C100D0_UnlockTextInput:
    rep #$31
    stz InputLockFlag
    rts
