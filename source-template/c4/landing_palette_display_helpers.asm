; EarthBound C4 landing palette/display helper prototype.
;
; Source-emission status:
; - Prototype level: build-candidate
; - C4 source-bank scaffold pilot slice.
; - Derived from notes/landing-and-coffee-tea-visual-helpers-c492d2-c49d1e.md
;   and notes/landing-palette-interpolation-export-c4958e-c426ed.md.
; - ROM byte range, SHA-1, and source signature are tracked by
;   build/c4-build-candidate-ranges.json.
;
; Source units covered:
; - C4:9496..C4:9841 packed RGB555 scaling, landing palette plane build/export,
;   landing palette fade driver, and static visual block copy to VRAM source RAM.

; ---------------------------------------------------------------------------
; External contracts used by this module

C0856B_WriteAtoDisplaySelector30              = $C0856B
C08756_WaitOneFrameAndPollInput               = $C08756
C08616_QueueVramTransfer_FromDpSource         = $C08616
C08EED_CopyBlockFromDpSourceToDpDest          = $C08EED
C08ED2_QueueOrTransferDynamicTileBlock        = $C08ED2
C08F15_FillLongBlockWithByte                  = $C08F15
C09032_MultiplyAByY                           = $C09032
C0915B_ScaleOrDivideAngleMagnitude            = $C0915B
C0923E_ShiftRightByY                          = $C0923E
C09251_ShiftRightByYAlt                       = $C09251
C426ED_StepPaletteComponentInterpolation      = $C426ED
C491EE_ComputeSignedComponentStep             = $91EE

; ---------------------------------------------------------------------------
; WRAM / data contracts

CGRAM_SHADOW_BUFFER                           = $0200
SAVED_CGRAM_SHADOW_BUFFER                     = $4476
LANDING_PALETTE_WORK_BASE                     = $0000
LANDING_PALETTE_WORK_BANK                     = $007F
LANDING_COMPONENT_DELTA_LOW_PLANE             = $7F0200
LANDING_COMPONENT_DELTA_MID_PLANE             = $7F0400
LANDING_COMPONENT_DELTA_HIGH_PLANE            = $7F0600
LANDING_COMPONENT_BASE_LOW_PLANE              = $7F0800
LANDING_COMPONENT_BASE_MID_PLANE              = $7F0A00
LANDING_COMPONENT_BASE_HIGH_PLANE             = $7F0C00
LANDING_COMPONENT_PLANE_CLEAR_BYTES           = $1000
LANDING_PALETTE_WORD_COUNT                    = $0100
LANDING_COMPONENT_BLOCK_SIZE                  = $0010
RGB555_COMPONENT_MASK                         = $001F
RGB555_MID_COMPONENT_MASK                     = $03E0
RGB555_HIGH_COMPONENT_MASK                    = $7C00
RGB555_SCALE_CLAMP_THRESHOLD                  = $1E45
RGB555_SCALE_CLAMP_VALUE                      = $1F00
RGB555_GREEN_SHIFT                            = $000A
LANDING_CGRAM_UPLOAD_SELECTOR                 = $0018
STATIC_VISUAL_CLEAR_SOURCE                    = $0BE8
STATIC_VISUAL_CLEAR_SOURCE_BANK               = $00C4
STATIC_VISUAL_VRAM_SOURCE_DEST                = $7C00
STATIC_VISUAL_COPY_SIZE                       = $0800
STATIC_VISUAL_TRANSFER_SELECTOR               = $03

; Direct-page locals:
;   C4:9496 uses $02/$04/$0E/$10/$12 as RGB component scratch.
;   C4:954C uses $06/$08 and $0A/$0C as destination/source long pointers.
;   C4:958E uses $06/$08 and $0E/$10 as 7F plane pointers, $1C/$1E/$20 as
;   frame count/source selector/template pointer inputs, and $1A/$18/$16 as
;   row-window counters.

; ---------------------------------------------------------------------------
; C4:9496

; ScalePackedRgb555ColorByStep
C49496_ScalePackedRgb555ColorByStep:
    rep #$31
    phd
    pha
    tdc
    adc #$FFEC
    tcd
    pla
    sta $12
    cpx #$0032
    bcs C49515_ScalePackedRgb555ColorByStep_HandleLargeStep
    txa
    sta $04
    asl
    asl
    adc $04
    tay
    sty $10
    lda $12
    and #RGB555_COMPONENT_MASK
    jsl C09032_MultiplyAByY
    sta $02
    ldy $10
    lda $12
    lsr
    lsr
    lsr
    lsr
    lsr
    and #RGB555_COMPONENT_MASK
    jsl C09032_MultiplyAByY
    tax
    stx $0E
    sep #$20
    lda.b #RGB555_GREEN_SHIFT
    sep #$10
    tay
    rep #$20
    lda $12
    jsl C09251_ShiftRightByYAlt
    and #RGB555_COMPONENT_MASK
    rep #$10
    ldy $10
    jsl C09032_MultiplyAByY
    sta $12
    lda $02
    cmp #RGB555_SCALE_CLAMP_THRESHOLD
    bcc C494F9_ScalePackedRgb555ColorByStep_CheckGreen
    beq C494F9_ScalePackedRgb555ColorByStep_CheckGreen
    lda #RGB555_SCALE_CLAMP_VALUE
    sta $02
C494F9_ScalePackedRgb555ColorByStep_CheckGreen:
    ldx $0E
    cpx #RGB555_SCALE_CLAMP_THRESHOLD
    bcc C49505_ScalePackedRgb555ColorByStep_CheckBlue
    beq C49505_ScalePackedRgb555ColorByStep_CheckBlue
    ldx #RGB555_SCALE_CLAMP_VALUE
C49505_ScalePackedRgb555ColorByStep_CheckBlue:
    lda $12
    cmp #RGB555_SCALE_CLAMP_THRESHOLD
    bcc C49522_ScalePackedRgb555ColorByStep_Repack
    beq C49522_ScalePackedRgb555ColorByStep_Repack
    lda #RGB555_SCALE_CLAMP_VALUE
    sta $12
    bra C49522_ScalePackedRgb555ColorByStep_Repack

C49515_ScalePackedRgb555ColorByStep_HandleLargeStep:
    cpx #$0032
    beq C49548_ScalePackedRgb555ColorByStep_ReturnOriginal
    lda #RGB555_SCALE_CLAMP_VALUE
    sta $12
    tax
    stx $02
C49522_ScalePackedRgb555ColorByStep_Repack:
    lda $02
    xba
    and #$00FF
    sta $02
    txa
    xba
    and #$00FF
    asl
    asl
    asl
    asl
    asl
    sta $04
    sep #$10
    ldy.b #RGB555_GREEN_SHIFT
    lda $12
    xba
    and #$00FF
    jsl C0923E_ShiftRightByY
    ora $04
    ora $02
C49548_ScalePackedRgb555ColorByStep_ReturnOriginal:
    rep #$10
    pld
    rts

; ---------------------------------------------------------------------------
; C4:954C

; BuildScaledPaletteBlockTo7f0000
C4954C_BuildScaledPaletteBlockTo7f0000:
    rep #$31
    phd
    pha
    tdc
    adc #$FFF0
    tcd
    pla
    sta $02
    lda $1E
    sta $0A
    lda $20
    sta $0C
    lda #LANDING_PALETTE_WORK_BASE
    sta $06
    lda #LANDING_PALETTE_WORK_BANK
    sta $08
    ldy #$0000
    sty $0E
    bra C49587_BuildScaledPaletteBlockTo7f0000_CheckLoop

C49571_BuildScaledPaletteBlockTo7f0000_Entry:
    lda [$0A]
    inc $0A
    inc $0A
    ldx $02
    jsr C49496_ScalePackedRgb555ColorByStep
    sta [$06]
    inc $06
    inc $06
    ldy $0E
    iny
    sty $0E
C49587_BuildScaledPaletteBlockTo7f0000_CheckLoop:
    cpy #LANDING_PALETTE_WORD_COUNT
    bcc C49571_BuildScaledPaletteBlockTo7f0000_Entry
    pld
    rtl

; ---------------------------------------------------------------------------
; C4:958E

; BuildLandingPaletteInterpolationPlanes
C4958E_BuildLandingPaletteInterpolationPlanes:
    rep #$31
    phd
    pha
    tdc
    adc #$FFDE
    tcd
    pla
    sty $20
    stx $1E
    sta $1C
    lda #LANDING_PALETTE_WORK_BASE
    sta $06
    lda #LANDING_PALETTE_WORK_BANK
    sta $08
    lda #CGRAM_SHADOW_BUFFER
    sta $0E
    lda #LANDING_PALETTE_WORK_BANK
    sta $10
    ldx #LANDING_COMPONENT_PLANE_CLEAR_BYTES
    sep #$20
    lda.b #$00
    jsl C08F15_FillLongBlockWithByte
    stz $1A
    jmp C496D9_BuildLandingPaletteInterpolationPlanes_CheckOuterLoop

C495C2_BuildLandingPaletteInterpolationPlanes_StartRow:
    lda $1A
    sta $18
    jmp C4966E_BuildLandingPaletteInterpolationPlanes_CheckCurrentBlock

C495C9_BuildLandingPaletteInterpolationPlanes_UseExistingWorkWord:
    lda $1E
    and #$0001
    beq C495E6_BuildLandingPaletteInterpolationPlanes_LoadTemplateWord
    lda $18
    asl
    ldx $06
    stx $0A
    ldx $08
    stx $0C
    clc
    adc $0A
    sta $0A
    lda [$0A]
    sta $02
    bra C49603_BuildLandingPaletteInterpolationPlanes_BuildDeltas

C495E6_BuildLandingPaletteInterpolationPlanes_LoadTemplateWord:
    lda $18
    asl
    sta $16
    tay
    lda ($20),Y
    sta $02
    lda $16
    ldx $06
    stx $0A
    ldx $08
    stx $0C
    clc
    adc $0A
    sta $0A
    lda $02
    sta [$0A]
C49603_BuildLandingPaletteInterpolationPlanes_BuildDeltas:
    lda $18
    asl
    sta $04
    ldy $04
    lda ($20),Y
    sta $14
    ldy $1C
    lda $02
    and #RGB555_COMPONENT_MASK
    tax
    lda $14
    and #RGB555_COMPONENT_MASK
    jsr C491EE_ComputeSignedComponentStep
    ldx $04
    sta.l LANDING_COMPONENT_DELTA_LOW_PLANE,X
    ldy $1C
    lda $02
    and #RGB555_MID_COMPONENT_MASK
    lsr
    lsr
    lsr
    lsr
    lsr
    tax
    lda $14
    and #RGB555_MID_COMPONENT_MASK
    lsr
    lsr
    lsr
    lsr
    lsr
    jsr C491EE_ComputeSignedComponentStep
    ldx $04
    sta.l LANDING_COMPONENT_DELTA_MID_PLANE,X
    ldy $1C
    sty $12
    ldy #$0400
    lda $02
    and #RGB555_HIGH_COMPONENT_MASK
    jsl C0915B_ScaleOrDivideAngleMagnitude
    tax
    ldy #$0400
    lda $14
    and #RGB555_HIGH_COMPONENT_MASK
    jsl C0915B_ScaleOrDivideAngleMagnitude
    ldy $12
    jsr C491EE_ComputeSignedComponentStep
    ldx $04
    sta.l LANDING_COMPONENT_DELTA_HIGH_PLANE,X
    inc $18
C4966E_BuildLandingPaletteInterpolationPlanes_CheckCurrentBlock:
    lda $1A
    clc
    adc #LANDING_COMPONENT_BLOCK_SIZE
    cmp $18
    beq C4967D_BuildLandingPaletteInterpolationPlanes_CopyBaseRows
    bcc C4967D_BuildLandingPaletteInterpolationPlanes_CopyBaseRows
    jmp C495C9_BuildLandingPaletteInterpolationPlanes_UseExistingWorkWord

C4967D_BuildLandingPaletteInterpolationPlanes_CopyBaseRows:
    lda $1A
    sta $16
    bra C496C2_BuildLandingPaletteInterpolationPlanes_CheckBaseRows

C49683_BuildLandingPaletteInterpolationPlanes_CopyBaseRow:
    asl
    sta $02
    clc
    adc $20
    tax
    stx $14
    lda $0000,X
    and #RGB555_COMPONENT_MASK
    xba
    and #$FF00
    ldx $02
    sta.l LANDING_COMPONENT_BASE_LOW_PLANE,X
    ldx $14
    lda $0000,X
    and #RGB555_MID_COMPONENT_MASK
    asl
    asl
    asl
    ldx $02
    sta.l LANDING_COMPONENT_BASE_MID_PLANE,X
    ldx $14
    lda $0000,X
    and #RGB555_HIGH_COMPONENT_MASK
    lsr
    lsr
    ldx $02
    sta.l LANDING_COMPONENT_BASE_HIGH_PLANE,X
    lda $16
    inc A
    sta $16
C496C2_BuildLandingPaletteInterpolationPlanes_CheckBaseRows:
    lda $1A
    clc
    adc #LANDING_COMPONENT_BLOCK_SIZE
    sta $02
    lda $16
    cmp $02
    bcc C49683_BuildLandingPaletteInterpolationPlanes_CopyBaseRow
    lda $1E
    lsr
    sta $1E
    lda $02
    sta $1A
C496D9_BuildLandingPaletteInterpolationPlanes_CheckOuterLoop:
    lda $1A
    cmp #LANDING_PALETTE_WORD_COUNT
    bcs C496E5_BuildLandingPaletteInterpolationPlanes_Return
    beq C496E5_BuildLandingPaletteInterpolationPlanes_Return
    jmp C495C2_BuildLandingPaletteInterpolationPlanes_StartRow

C496E5_BuildLandingPaletteInterpolationPlanes_Return:
    pld
    rts

; ---------------------------------------------------------------------------
; C4:96E7

; InitLandingPalettePlanesFrom0200
C496E7_InitLandingPalettePlanesFrom0200:
    rep #$31
    ldy #CGRAM_SHADOW_BUFFER
    jsr C4958E_BuildLandingPaletteInterpolationPlanes
    rtl

; ---------------------------------------------------------------------------
; C4:96F0

; InitLandingPalettePlanesFrom4476
C496F0_InitLandingPalettePlanesFrom4476:
    rep #$31
    ldy #SAVED_CGRAM_SHADOW_BUFFER
    jsr C4958E_BuildLandingPaletteInterpolationPlanes
    rtl

; ---------------------------------------------------------------------------
; C4:96F9

; MirrorCgramShadow0200To7f0000
C496F9_MirrorCgramShadow0200To7f0000:
    rep #$31
    phd
    tdc
    adc #$FFE6
    tcd
    lda #CGRAM_SHADOW_BUFFER
    sta $06
    phb
    sep #$20
    pla
    sta $08
    stz $09
    rep #$20
    lda $06
    sta $16
    lda $08
    sta $18
    lda #$007E
    sta $18
    lda #LANDING_PALETTE_WORK_BASE
    sta $0E
    lda #LANDING_PALETTE_WORK_BANK
    sta $10
    lda $16
    sta $06
    lda $18
    sta $08
    lda $06
    sta $12
    lda $08
    sta $14
    lda #CGRAM_SHADOW_BUFFER
    jsl C08EED_CopyBlockFromDpSourceToDpDest
    pld
    rtl

; ---------------------------------------------------------------------------
; C4:9740

; ExportLandingPaletteAndQueueCgramUpload
C49740_ExportLandingPaletteAndQueueCgramUpload:
    rep #$31
    phd
    tdc
    adc #$FFE6
    tcd
    lda #CGRAM_SHADOW_BUFFER
    sta $06
    phb
    sep #$20
    pla
    sta $08
    stz $09
    rep #$20
    lda $06
    sta $16
    lda $08
    sta $18
    lda #$007E
    sta $18
    lda $16
    sta $06
    lda $18
    sta $08
    lda $06
    sta $0E
    lda $08
    sta $10
    lda #LANDING_PALETTE_WORK_BASE
    sta $12
    lda #LANDING_PALETTE_WORK_BANK
    sta $14
    lda #CGRAM_SHADOW_BUFFER
    jsl C08EED_CopyBlockFromDpSourceToDpDest
    lda #LANDING_CGRAM_UPLOAD_SELECTOR
    jsl C0856B_WriteAtoDisplaySelector30
    pld
    rtl

; ---------------------------------------------------------------------------
; C4:978E

; CopyCgramShadow0200To4476
C4978E_CopyCgramShadow0200To4476:
    rep #$31
    phd
    tdc
    adc #$FFEE
    tcd
    lda #CGRAM_SHADOW_BUFFER
    sta $06
    stz $08
    clc
    lda $06
    adc #$0000
    sta $06
    lda $08
    adc #$007E
    sta $08
    lda $06
    sta $0E
    lda $08
    sta $10
    ldx #CGRAM_SHADOW_BUFFER
    lda #SAVED_CGRAM_SHADOW_BUFFER
    jsl C08ED2_QueueOrTransferDynamicTileBlock
    pld
    rtl

; ---------------------------------------------------------------------------
; C4:97C0

; RunLandingPaletteFadeToScaledBlock
C497C0_RunLandingPaletteFadeToScaledBlock:
    rep #$31
    phd
    pha
    tdc
    adc #$FFEA
    tcd
    pla
    sty $14
    sta $02
    lda #SAVED_CGRAM_SHADOW_BUFFER
    sta $06
    phb
    sep #$20
    pla
    sta $08
    stz $09
    rep #$20
    lda $06
    sta $0E
    lda $08
    sta $10
    txa
    jsl C4954C_BuildScaledPaletteBlockTo7f0000
    ldy $14
    tyx
    lda $02
    jsl C496E7_InitLandingPalettePlanesFrom0200
    lda $02
    cmp #$0001
    beq C49812_RunLandingPaletteFadeToScaledBlock_Export
    lda #$0000
    sta $12
    bra C4980E_RunLandingPaletteFadeToScaledBlock_CheckLoop

C49801_RunLandingPaletteFadeToScaledBlock_Frame:
    jsl C426ED_StepPaletteComponentInterpolation
    jsl C08756_WaitOneFrameAndPollInput
    lda $12
    inc A
    sta $12
C4980E_RunLandingPaletteFadeToScaledBlock_CheckLoop:
    cmp $02
    bcc C49801_RunLandingPaletteFadeToScaledBlock_Frame
C49812_RunLandingPaletteFadeToScaledBlock_Export:
    jsl C49740_ExportLandingPaletteAndQueueCgramUpload
    lda #LANDING_CGRAM_UPLOAD_SELECTOR
    jsl C0856B_WriteAtoDisplaySelector30
    pld
    rtl

; ---------------------------------------------------------------------------
; C4:981F

; CopyStaticVisualBlock0be8To7c00
C4981F_CopyStaticVisualBlock0be8To7c00:
    rep #$31
    phd
    tdc
    adc #$FFEE
    tcd
    lda #STATIC_VISUAL_CLEAR_SOURCE
    sta $0E
    lda #STATIC_VISUAL_CLEAR_SOURCE_BANK
    sta $10
    ldy #STATIC_VISUAL_VRAM_SOURCE_DEST
    ldx #STATIC_VISUAL_COPY_SIZE
    sep #$20
    lda.b #STATIC_VISUAL_TRANSFER_SELECTOR
    jsl C08616_QueueVramTransfer_FromDpSource
    pld
    rtl
