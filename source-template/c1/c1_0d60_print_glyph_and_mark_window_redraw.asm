; EarthBound C1 print glyph and mark window redraw helper.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Hand-shaped from ROM decode because the redraw flag is written in 8-bit
;   accumulator mode before returning to 16-bit mode.
;
; Source units covered:
; - C1:0D60..C1:0D7C PrintGlyphAndMarkWindowRedraw

; ---------------------------------------------------------------------------
; External contracts used by this module

C10BA1_PrintGlyphToActiveWindow = $0BA1
ActiveWindowFocus               = $8958
WindowDescriptorIndexTable      = $88E4
QueuedRedrawWindowIndex         = $88E2
WindowNeedsRedrawFlag           = $9623

; ---------------------------------------------------------------------------
; C1:0D60

C10D60_PrintGlyphAndMarkWindowRedraw:
    rep #$31
    jsr C10BA1_PrintGlyphToActiveWindow
    lda ActiveWindowFocus
    asl A
    tax
    lda WindowDescriptorIndexTable,X
    cmp QueuedRedrawWindowIndex
    beq C10D79_Return
    sep #$20
    lda.b #$01
    sta WindowNeedsRedrawFlag

C10D79_Return:
    rep #$20
    rts
