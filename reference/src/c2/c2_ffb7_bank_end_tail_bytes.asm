; EarthBound C2 bank-end tail bytes.
;
; Source-emission status:
; - Prototype level: source-locked data tail.
; - This follows the final callable C2:FF9A..FFB7 helper.
;
; Source unit covered:
; - C2:FFB7..C2:10000 BankEndTailBytes

; ---------------------------------------------------------------------------
; C2:FFB7

C2FFB7_BankEndTailBytes:
    db $1C,$BB,$F5,$EF,$23,$BB,$A0,$22
    db $FA,$A0,$3B,$00,$06,$05,$42,$56
    db $E5,$EF,$19,$C3,$FF
    db $00,$00,$00,$00,$00,$00,$00,$00
    db $00,$00,$00,$00,$00,$00,$00,$00
    db $00,$00,$00,$00,$00,$00,$00,$00
    db $00,$00,$00,$00,$00,$00,$00,$00
    db $00,$00,$00,$00,$00,$00,$00,$00
    db $00,$00,$00,$00,$00,$00,$00,$00
    db $00,$00,$00,$00

; ---------------------------------------------------------------------------
; C2:10000

C30000_BankEndTailBytes_End:
