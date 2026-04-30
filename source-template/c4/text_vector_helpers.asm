; EarthBound C4 text tile staging and direction/vector helper prototype.
;
; Source-emission status:
; - Prototype level: build-candidate
; - C4 source-bank scaffold slice with explicit source-adjacent data blocks.
; - Derived from notes/c4-text-tile-staging-and-vector-helpers-1db6-213f.md.
; - ROM byte range, SHA-1, and source signature are tracked by
;   build/c4-build-candidate-ranges.json.
;
; Source units covered:
; - C4:1DB6..C4:1EB9 masked glyph/text-tile staging renderer
; - C4:1EE9..C4:1EFF dirty-range trackers
; - C4:1EFF..C4:1FC5 direction/octant-from-delta helper
; - C4:1FFF..C4:205D direction projection helper
; - C4:213F..C4:2172 fractional multiply helper
;
; Data blocks emitted by the scaffold:
; - C4:1EB9..C4:1EE9 glyph tile staging masks
; - C4:1FC5..C4:1FFF direction/octant threshold tables
; - C4:205D..C4:213F projection scale tables

; ---------------------------------------------------------------------------
; External contracts used by this module

C41BCA_RenderGlyphScratchRows          = $1BCA

; ---------------------------------------------------------------------------
; ROM/WRAM contracts

GLYPH_TILE_STAGING_MASK_TABLE_0        = $C41EB9
GLYPH_TILE_STAGING_MASK_TABLE_1        = $C41EC9
GLYPH_TILE_STAGING_MASK_TABLE_2        = $C41ED9
DIRECTION_OCTANT_BASE_ANGLE_TABLE      = $C41FC5
DIRECTION_SLOPE_THRESHOLD_TABLE        = $C41FDF
DIRECTION_PROJECTION_X_SCALE_TABLE     = $C4205D
DIRECTION_PROJECTION_Y_SCALE_TABLE     = $C420BD

PPU_MULTIPLICAND_A                     = $004202
PPU_MULTIPLICAND_B                     = $004203
PPU_MULTIPLICAND_WORD                  = $004202
PPU_PRODUCT_LOW                        = $004216
PPU_DIVIDEND_LOW                       = $004204
PPU_DIVISOR                            = $004206
PPU_QUOTIENT_LOW                       = $004214

TEXT_TILE_SOURCE_X                     = $3C14
TEXT_TILE_SOURCE_Y                     = $3C16
TEXT_TILE_ROW_STRIDE                   = $3C18
TEXT_TILE_BASE_OFFSET                  = $3C1C
TEXT_TILE_MIN_DIRTY_OFFSET             = $3C1E
TEXT_TILE_MAX_DIRTY_OFFSET             = $3C20

TEXT_TILE_STAGING_ROW0                 = $3492
TEXT_TILE_STAGING_ROW1                 = $34A2
TEXT_TILE_STAGING_ROW2                 = $34B2
GLYPH_RENDER_SCRATCH_ROW               = $3B12

GLYPH_TILE_LOW_MASK                    = $0007
GLYPH_RENDER_BASE_BIAS                 = $8000
GLYPH_RENDER_BYTE_COUNT                = $0024
TEXT_TILE_ROW_ADVANCE                  = $0010
DIRECTION_DELTA_NORMALIZE_LIMIT        = $0100
DIRECTION_THRESHOLD_TABLE_END          = $0020
PROJECTION_TABLE_INDEX_MASK            = $00FC

; Direct-page locals:
;   $00 = input tile/glyph id or projection scratch.
;   $02/$04 = coarse tile coordinates or projection scratch.
;   $06/$08 = fine tile coordinates or vector input pair.
;   $0A = staging buffer byte offset or direction slope numerator.
;   $0C = direction slope denominator.
;   $0E/$10/$12 = staging mask words or direction quadrant state.
;   $14/$16 = caller-visible projected vector components.

; ---------------------------------------------------------------------------
; C4:1DB6

; RenderMaskedGlyphIntoTextTileStaging
C41DB6_RenderMaskedGlyphIntoTextTileStaging:
    rep #$20
    phd
    pha
    tdc
    sec
    sbc #$0014
    tcd
    pla
    sta $00
    lda TEXT_TILE_SOURCE_X
    and #GLYPH_TILE_LOW_MASK
    sta $06
    lda TEXT_TILE_SOURCE_Y
    and #GLYPH_TILE_LOW_MASK
    sta $08
    lda TEXT_TILE_SOURCE_X
    lsr
    lsr
    lsr
    sta $02
    lda TEXT_TILE_SOURCE_Y
    lsr
    lsr
    lsr
    sta $04
    sep #$20
    xba
    lda TEXT_TILE_ROW_STRIDE
    rep #$20
    sta.l PPU_MULTIPLICAND_WORD
    nop
    nop
    lda.l PPU_PRODUCT_LOW
    clc
    adc $02
    clc
    adc TEXT_TILE_BASE_OFFSET
    asl
    asl
    asl
    clc
    adc $08
    asl
    sta $0A
    jsr C41EE9_TrackTextTileStagingMinDirtyOffset
    lda $06
    asl
    tax
    lda.l GLYPH_TILE_STAGING_MASK_TABLE_0,X
    sta $0E
    lda.l GLYPH_TILE_STAGING_MASK_TABLE_1,X
    sta $10
    lda.l GLYPH_TILE_STAGING_MASK_TABLE_2,X
    sta $12
    lda $00
    sec
    sbc #GLYPH_RENDER_BASE_BIAS
    rep #$30
    ldx #GLYPH_RENDER_SCRATCH_ROW
    ldy $06
    jsr C41BCA_RenderGlyphScratchRows
    ldy #$0000
C41E31_RenderMaskedGlyphIntoTextTileStaging_Loop:
    sep #$20
    lda GLYPH_RENDER_SCRATCH_ROW,Y
    xba
    lda GLYPH_RENDER_SCRATCH_ROW,Y
    rep #$20
    ldx $0A
    eor TEXT_TILE_STAGING_ROW0,X
    and $0E
    eor TEXT_TILE_STAGING_ROW0,X
    sta TEXT_TILE_STAGING_ROW0,X
    iny
    sep #$20
    lda GLYPH_RENDER_SCRATCH_ROW,Y
    xba
    lda GLYPH_RENDER_SCRATCH_ROW,Y
    rep #$20
    ldx $0A
    eor TEXT_TILE_STAGING_ROW1,X
    and $10
    eor TEXT_TILE_STAGING_ROW1,X
    sta TEXT_TILE_STAGING_ROW1,X
    iny
    lda $12
    beq C41E7F_RenderMaskedGlyphIntoTextTileStaging_SkipRow2
    sep #$20
    lda GLYPH_RENDER_SCRATCH_ROW,Y
    xba
    lda GLYPH_RENDER_SCRATCH_ROW,Y
    rep #$20
    ldx $0A
    eor TEXT_TILE_STAGING_ROW2,X
    and $12
    eor TEXT_TILE_STAGING_ROW2,X
    sta TEXT_TILE_STAGING_ROW2,X
C41E7F_RenderMaskedGlyphIntoTextTileStaging_SkipRow2:
    iny
    inc $0A
    inc $0A
    cpy #GLYPH_RENDER_BYTE_COUNT
    bcs C41EA3_RenderMaskedGlyphIntoTextTileStaging_FinishDirtyRange
    lda $08
    inc
    and #GLYPH_TILE_LOW_MASK
    sta $08
    bne C41EA0_RenderMaskedGlyphIntoTextTileStaging_NextColumn
    lda TEXT_TILE_ROW_STRIDE
    dec
    asl
    asl
    asl
    asl
    clc
    adc $0A
    sta $0A
C41EA0_RenderMaskedGlyphIntoTextTileStaging_NextColumn:
    jmp C41E31_RenderMaskedGlyphIntoTextTileStaging_Loop
C41EA3_RenderMaskedGlyphIntoTextTileStaging_FinishDirtyRange:
    lda $0A
    clc
    adc #TEXT_TILE_ROW_ADVANCE
    ldx $12
    beq C41EB0_RenderMaskedGlyphIntoTextTileStaging_StoreMax
    adc #TEXT_TILE_ROW_ADVANCE
C41EB0_RenderMaskedGlyphIntoTextTileStaging_StoreMax:
    sta $0A
    jsr C41EF4_TrackTextTileStagingMaxDirtyOffset
    pld
    rep #$30
    rtl

; ---------------------------------------------------------------------------
; C4:1EE9

; TrackTextTileStagingMinDirtyOffset

; ---------------------------------------------------------------------------
; C4:1EB9

C41EB9_GlyphTileStagingMaskTables:
    ; data bytes: C4:1EB9..C4:1EE9
    db $FF,$FF,$7F,$7F,$3F,$3F,$1F,$1F,$0F,$0F,$07,$07,$03,$03,$01,$01
    db $F0,$F0,$F8,$F8,$FC,$FC,$FE,$FE,$FF,$FF,$FF,$FF,$FF,$FF,$FF,$FF
    db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$80,$80,$C0,$C0,$E0,$E0

C41EE9_TrackTextTileStagingMinDirtyOffset:
    lda $0A
    cmp TEXT_TILE_MIN_DIRTY_OFFSET
    bcs C41EF3_TrackTextTileStagingMinDirtyOffset_Done
    sta TEXT_TILE_MIN_DIRTY_OFFSET
C41EF3_TrackTextTileStagingMinDirtyOffset_Done:
    rts

; ---------------------------------------------------------------------------
; C4:1EF4

; TrackTextTileStagingMaxDirtyOffset
C41EF4_TrackTextTileStagingMaxDirtyOffset:
    lda $0A
    cmp TEXT_TILE_MAX_DIRTY_OFFSET
    bcc C41EFE_TrackTextTileStagingMaxDirtyOffset_Done
    sta TEXT_TILE_MAX_DIRTY_OFFSET
C41EFE_TrackTextTileStagingMaxDirtyOffset_Done:
    rts

; ---------------------------------------------------------------------------
; C4:1EFF

; ComputeDirectionOctantFromDelta
C41EFF_ComputeDirectionOctantFromDelta:
    rep #$20
    phd
    pha
    tdc
    sec
    sbc #$0010
    tcd
    pla
    sta $00
    stx $02
    sty $04
    lda $1E
    sta $06
    lda $00
    sec
    sbc $04
    pha
    bpl C41F20_ComputeDirectionOctantFromDelta_XPositive
    eor #$FFFF
    inc
C41F20_ComputeDirectionOctantFromDelta_XPositive:
    tay
    lda $02
    sec
    sbc $06
    pha
    bpl C41F2D_ComputeDirectionOctantFromDelta_YPositive
    eor #$FFFF
    inc
C41F2D_ComputeDirectionOctantFromDelta_YPositive:
    sta $0C
    tya
C41F30_ComputeDirectionOctantFromDelta_NormalizeLoop:
    cmp #DIRECTION_DELTA_NORMALIZE_LIMIT
    bcc C41F3A_ComputeDirectionOctantFromDelta_Normalized
    lsr
    lsr $0C
    bra C41F30_ComputeDirectionOctantFromDelta_NormalizeLoop
C41F3A_ComputeDirectionOctantFromDelta_Normalized:
    sta $0A
    pla
    beq C41F46_ComputeDirectionOctantFromDelta_ZeroY
    bpl C41F4B_ComputeDirectionOctantFromDelta_PositiveY
    lda #$0000
    bra C41F4E_ComputeDirectionOctantFromDelta_CheckX
C41F46_ComputeDirectionOctantFromDelta_ZeroY:
    lda #$0008
    bra C41F4E_ComputeDirectionOctantFromDelta_CheckX
C41F4B_ComputeDirectionOctantFromDelta_PositiveY:
    lda #$0002
C41F4E_ComputeDirectionOctantFromDelta_CheckX:
    plx
    beq C41F55_ComputeDirectionOctantFromDelta_ZeroX
    bpl C41F5A_ComputeDirectionOctantFromDelta_PositiveX
    bra C41F5D_ComputeDirectionOctantFromDelta_QuadrantCheck
C41F55_ComputeDirectionOctantFromDelta_ZeroX:
    ora #$0004
    bra C41F6D_ComputeDirectionOctantFromDelta_DivideSlope
C41F5A_ComputeDirectionOctantFromDelta_PositiveX:
    ora #$0001
C41F5D_ComputeDirectionOctantFromDelta_QuadrantCheck:
    bit #$000C
    beq C41F6D_ComputeDirectionOctantFromDelta_DivideSlope
    asl
    tax
    lda.l DIRECTION_OCTANT_BASE_ANGLE_TABLE,X
    sta $0E
    jmp C41FC1_ComputeDirectionOctantFromDelta_Done
C41F6D_ComputeDirectionOctantFromDelta_DivideSlope:
    sta $0E
    asl
    sta $08
    lda $0C
    xba
    bit #$00FF
    beq C41F7D_ComputeDirectionOctantFromDelta_DividendReady
    lda #$FFFF
C41F7D_ComputeDirectionOctantFromDelta_DividendReady:
    sta.l PPU_DIVIDEND_LOW
    lda $0A
    sep #$20
    sta.l PPU_DIVISOR
    rep #$20
    nop
    nop
    nop
    nop
    nop
    lda.l PPU_QUOTIENT_LOW
    ldx #$0000
C41F97_ComputeDirectionOctantFromDelta_ThresholdLoop:
    cmp.l DIRECTION_SLOPE_THRESHOLD_TABLE,X
    bcc C41FA4_ComputeDirectionOctantFromDelta_ThresholdFound
    inx
    inx
    cpx #DIRECTION_THRESHOLD_TABLE_END
    bcc C41F97_ComputeDirectionOctantFromDelta_ThresholdLoop
C41FA4_ComputeDirectionOctantFromDelta_ThresholdFound:
    lda $0E
    beq C41FB7_ComputeDirectionOctantFromDelta_UseThreshold
    eor #$0003
    beq C41FB7_ComputeDirectionOctantFromDelta_UseThreshold
    stx $0E
    lda #DIRECTION_THRESHOLD_TABLE_END
    sec
    sbc $0E
    bra C41FB8_ComputeDirectionOctantFromDelta_ToAngle
C41FB7_ComputeDirectionOctantFromDelta_UseThreshold:
    txa
C41FB8_ComputeDirectionOctantFromDelta_ToAngle:
    asl
    xba
    ldx $08
    clc
    adc.l DIRECTION_OCTANT_BASE_ANGLE_TABLE,X
C41FC1_ComputeDirectionOctantFromDelta_Done:
    pld
    rep #$30
    rtl

; ---------------------------------------------------------------------------
; C4:1FFF

; ProjectMagnitudeByDirectionAngle

; ---------------------------------------------------------------------------
; C4:1FC5

C41FC5_DirectionOctantThresholdTables:
    ; data bytes: C4:1FC5..C4:1FFF
    db $00,$40,$00,$80,$00,$00,$00,$C0,$00,$80,$FF,$FF,$00,$00,$FF,$FF
    db $00,$40,$00,$C0,$FF,$FF,$FF,$FF,$00,$00,$0D,$00,$26,$00,$40,$00
    db $5C,$00,$79,$00,$99,$00,$BE,$00,$E8,$00,$1A,$01,$59,$01,$AB,$01
    db $1D,$02,$CB,$02,$FD,$03,$BB,$06,$3D,$14

C41FFF_ProjectMagnitudeByDirectionAngle:
    rep #$20
    phd
    pha
    tdc
    sec
    sbc #$000E
    tcd
    pla
    txy
    phy
    xba
    and #PROJECTION_TABLE_INDEX_MASK
    lsr
    pha
    tax
    lda.l DIRECTION_PROJECTION_X_SCALE_TABLE,X
    cmp #$0100
    bne C4201F_ProjectMagnitudeByDirectionAngle_ScaleX
    tya
    bra C42022_ProjectMagnitudeByDirectionAngle_XReady
C4201F_ProjectMagnitudeByDirectionAngle_ScaleX:
    jsr C4213F_ScaleU16ByU8Fraction
C42022_ProjectMagnitudeByDirectionAngle_XReady:
    plx
    ply
    pha
    lda.l DIRECTION_PROJECTION_Y_SCALE_TABLE,X
    phx
    cmp #$0100
    bne C42032_ProjectMagnitudeByDirectionAngle_ScaleY
    tya
    bra C42035_ProjectMagnitudeByDirectionAngle_YReady
C42032_ProjectMagnitudeByDirectionAngle_ScaleY:
    jsr C4213F_ScaleU16ByU8Fraction
C42035_ProjectMagnitudeByDirectionAngle_YReady:
    plx
    cpx #$0020
    bcc C42040_ProjectMagnitudeByDirectionAngle_NegateY
    cpx #$0062
    bcc C42044_ProjectMagnitudeByDirectionAngle_StoreY
C42040_ProjectMagnitudeByDirectionAngle_NegateY:
    eor #$FFFF
    inc
C42044_ProjectMagnitudeByDirectionAngle_StoreY:
    tay
    pla
    cpx #$0042
    bcc C42054_ProjectMagnitudeByDirectionAngle_StoreX
    cpx #$0080
    bcs C42054_ProjectMagnitudeByDirectionAngle_StoreX
    eor #$FFFF
    inc
C42054_ProjectMagnitudeByDirectionAngle_StoreX:
    tax
    stx $16
    sty $14
    pld
    rep #$30
    rtl

; ---------------------------------------------------------------------------
; C4:213F

; ScaleU16ByU8Fraction

; ---------------------------------------------------------------------------
; C4:205D

C4205D_DirectionProjectionScaleTables:
    ; data bytes: C4:205D..C4:213F
    db $00,$00,$19,$00,$32,$00,$4A,$00,$62,$00,$79,$00,$8E,$00,$A2,$00
    db $B5,$00,$C6,$00,$D5,$00,$E2,$00,$EC,$00,$F5,$00,$FB,$00,$FE,$00
    db $00,$01,$FE,$00,$FB,$00,$F5,$00,$ED,$00,$E2,$00,$D5,$00,$C6,$00
    db $B5,$00,$A2,$00,$8E,$00,$79,$00,$62,$00,$4A,$00,$32,$00,$19,$00
    db $00,$00,$19,$00,$32,$00,$4A,$00,$62,$00,$79,$00,$8E,$00,$A2,$00
    db $B5,$00,$C6,$00,$D5,$00,$E2,$00,$EC,$00,$F5,$00,$FB,$00,$FE,$00
    db $00,$01,$FE,$00,$FB,$00,$F5,$00,$EC,$00,$E2,$00,$D5,$00,$C6,$00
    db $B5,$00,$A3,$00,$8E,$00,$79,$00,$62,$00,$4B,$00,$32,$00,$19,$00
    db $00,$00,$19,$00,$32,$00,$4A,$00,$62,$00,$79,$00,$8E,$00,$A2,$00
    db $B5,$00,$C6,$00,$D5,$00,$E2,$00,$EC,$00,$F5,$00,$FB,$00,$FE,$00
    db $00,$01,$FE,$00,$FB,$00,$F5,$00,$ED,$00,$E2,$00,$D5,$00,$C6,$00
    db $B5,$00,$A2,$00,$8E,$00,$79,$00,$62,$00,$4A,$00,$32,$00,$19,$00
    db $00,$00,$19,$00,$32,$00,$4A,$00,$62,$00,$79,$00,$8E,$00,$A2,$00
    db $B5,$00,$C6,$00,$D5,$00,$E2,$00,$EC,$00,$F5,$00,$FB,$00,$FE,$00
    db $00,$01

C4213F_ScaleU16ByU8Fraction:
    sty $00
    sta $02
    tya
    sep #$20
    lda $02
    rep #$20
    sta.l PPU_MULTIPLICAND_WORD
    nop
    clc
    lda.l PPU_PRODUCT_LOW
    sta $04
    sep #$20
    lda $00
    sta.l PPU_MULTIPLICAND_B
    nop
    nop
    rep #$20
    lda.l PPU_PRODUCT_LOW
    xba
    sep #$20
    sta $02
    rep #$20
    lda $02
    adc $04
    rts
