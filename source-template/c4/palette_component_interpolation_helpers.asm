; EarthBound C4 palette component interpolation helper prototype.
;
; Source-emission status:
; - Prototype level: build-candidate
; - C4 source-bank scaffold pilot slice.
; - Derived from notes/landing-palette-interpolation-export-c4958e-c426ed.md
;   and notes/c4-window-color-math-and-palette-helpers-23dc-26ed.md.
; - ROM byte range, SHA-1, and source signature are tracked by
;   build/c4-build-candidate-ranges.json.
;
; Source units covered:
; - C4:26ED..C4:279F palette component stepper/repacker.

; ---------------------------------------------------------------------------
; WRAM and work-plane contracts

PALETTE_PACK_TEMP                    = $00

PALETTE_LOW_DELTA_PLANE              = $7F0200
PALETTE_MID_DELTA_PLANE              = $7F0400
PALETTE_HIGH_DELTA_PLANE             = $7F0600
PALETTE_LOW_CURRENT_PLANE            = $7F0800
PALETTE_MID_CURRENT_PLANE            = $7F0A00
PALETTE_HIGH_CURRENT_PLANE           = $7F0C00
PALETTE_CGRAM_SHADOW                 = $0200

PALETTE_COMPONENT_UPPER_MASK         = $1F00
FULL_CGRAM_UPLOAD_SELECTOR           = $18
DISPLAY_UPLOAD_SELECTOR              = $0030
PALETTE_EXPORT_BYTE_SIZE             = $0200

; Direct-page locals:
;   $00 = partially packed SNES 15-bit color word.

; ---------------------------------------------------------------------------
; C4:26ED

; StepPaletteComponentInterpolationToCgramShadow
;
; Steps the three component delta/current plane pairs, saturates each channel
; to the 5-bit range, repacks the result into the low WRAM CGRAM shadow, and
; requests a full CGRAM upload through display selector $18.
C426ED_StepPaletteComponentInterpolationToCgramShadow:
    rep #$20
    phd
    pha
    tdc
    sec
    sbc #$0002
    tcd
    pla
    ldx #$0000

C426FB_StepPaletteComponentInterpolationToCgramShadow_Loop:
    lda.l PALETTE_LOW_DELTA_PLANE,X
    clc
    adc.l PALETTE_LOW_CURRENT_PLANE,X
    sta.l PALETTE_LOW_CURRENT_PLANE,X
    bpl C42713_StepPaletteComponentInterpolationToCgramShadow_LowNonnegative
    lda #$0000
    sta.l PALETTE_LOW_DELTA_PLANE,X
    bra C42725_StepPaletteComponentInterpolationToCgramShadow_LowReady

C42713_StepPaletteComponentInterpolationToCgramShadow_LowNonnegative:
    and #PALETTE_COMPONENT_UPPER_MASK
    cmp #PALETTE_COMPONENT_UPPER_MASK
    bne C42725_StepPaletteComponentInterpolationToCgramShadow_LowReady
    lda #$0000
    sta.l PALETTE_LOW_DELTA_PLANE,X
    lda #PALETTE_COMPONENT_UPPER_MASK
C42725_StepPaletteComponentInterpolationToCgramShadow_LowReady:
    xba
    sta PALETTE_PACK_TEMP

    lda.l PALETTE_MID_DELTA_PLANE,X
    clc
    adc.l PALETTE_MID_CURRENT_PLANE,X
    sta.l PALETTE_MID_CURRENT_PLANE,X
    bpl C42740_StepPaletteComponentInterpolationToCgramShadow_MidNonnegative
    lda #$0000
    sta.l PALETTE_MID_DELTA_PLANE,X
    bra C42752_StepPaletteComponentInterpolationToCgramShadow_MidReady

C42740_StepPaletteComponentInterpolationToCgramShadow_MidNonnegative:
    and #PALETTE_COMPONENT_UPPER_MASK
    cmp #PALETTE_COMPONENT_UPPER_MASK
    bne C42752_StepPaletteComponentInterpolationToCgramShadow_MidReady
    lda #$0000
    sta.l PALETTE_MID_DELTA_PLANE,X
    lda #PALETTE_COMPONENT_UPPER_MASK
C42752_StepPaletteComponentInterpolationToCgramShadow_MidReady:
    lsr
    lsr
    lsr
    ora PALETTE_PACK_TEMP
    sta PALETTE_PACK_TEMP

    lda.l PALETTE_HIGH_DELTA_PLANE,X
    clc
    adc.l PALETTE_HIGH_CURRENT_PLANE,X
    sta.l PALETTE_HIGH_CURRENT_PLANE,X
    bpl C42771_StepPaletteComponentInterpolationToCgramShadow_HighNonnegative
    lda #$0000
    ; Original code clears the middle delta plane on this negative high-channel
    ; clamp. Preserve byte-equivalence until a later semantic pass proves intent.
    sta.l PALETTE_MID_DELTA_PLANE,X
    bra C42783_StepPaletteComponentInterpolationToCgramShadow_HighReady

C42771_StepPaletteComponentInterpolationToCgramShadow_HighNonnegative:
    and #PALETTE_COMPONENT_UPPER_MASK
    cmp #PALETTE_COMPONENT_UPPER_MASK
    bne C42783_StepPaletteComponentInterpolationToCgramShadow_HighReady
    lda #$0000
    sta.l PALETTE_HIGH_DELTA_PLANE,X
    lda #PALETTE_COMPONENT_UPPER_MASK
C42783_StepPaletteComponentInterpolationToCgramShadow_HighReady:
    asl
    asl
    ora PALETTE_PACK_TEMP
    sta PALETTE_CGRAM_SHADOW,X
    inx
    inx
    cpx #PALETTE_EXPORT_BYTE_SIZE
    beq C42794_StepPaletteComponentInterpolationToCgramShadow_Done
    jmp C426FB_StepPaletteComponentInterpolationToCgramShadow_Loop

C42794_StepPaletteComponentInterpolationToCgramShadow_Done:
    sep #$20
    lda.b #FULL_CGRAM_UPLOAD_SELECTOR
    sta.w DISPLAY_UPLOAD_SELECTOR
    rep #$20
    pld
    rtl
