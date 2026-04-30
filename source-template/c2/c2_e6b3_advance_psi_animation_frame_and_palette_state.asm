; EarthBound C2 PSI animation state prefix bytes.
;
; Source-emission status:
; - Prototype level: source-locked data prefix.
; - The callable body starts at C2:E6B6.
;
; Source unit covered:
; - C2:E6B3..C2:E6B6 AdvancePsiAnimationFrameAndPaletteState

; ---------------------------------------------------------------------------
; C2:E6B3

C2E6B3_AdvancePsiAnimationFrameAndPaletteState:
    db $30,$00,$00

; ---------------------------------------------------------------------------
; C2:E6B6

C2E6B6_AdvancePsiAnimationFrameAndPaletteState_End:
