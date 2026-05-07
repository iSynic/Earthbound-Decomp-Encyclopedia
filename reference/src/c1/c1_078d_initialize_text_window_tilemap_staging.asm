; EarthBound C1 text window tilemap staging initializer.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Hand-shaped from ROM decode because the fill value is loaded in 8-bit
;   accumulator mode immediately before the long fill/copy helper.
;
; Source units covered:
; - C1:078D..C1:07AF InitializeTextWindowTilemapStaging

; ---------------------------------------------------------------------------
; External contracts used by this module

C0862E_FillTextWindowTilemapStaging = $C0862E
TilemapStagingPointerLo            = $0E
TilemapStagingPointerBank          = $10
TilemapStagingBank                 = $007E
TilemapStagingBase                 = $7E40
TilemapStagingEnd                  = $827E
TilemapStagingByteCount            = $0240
BlankTileByte                      = $00

; ---------------------------------------------------------------------------
; C1:078D

C1078D_InitializeTextWindowTilemapStaging:
    rep #$31
    phd
    tdc
    adc.w #$FFEE
    tcd
    lda.w #TilemapStagingBank
    sta TilemapStagingPointerLo
    lda.w #TilemapStagingBase
    sta TilemapStagingPointerBank
    ldy.w #TilemapStagingEnd
    ldx.w #TilemapStagingByteCount
    sep #$20
    lda.b #BlankTileByte
    jsl C0862E_FillTextWindowTilemapStaging
    pld
    rts
