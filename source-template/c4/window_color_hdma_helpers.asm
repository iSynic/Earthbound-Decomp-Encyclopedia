; EarthBound C4 window/color HDMA helper prototype.
;
; Source-emission status:
; - Prototype level: build-candidate
; - C4 source-bank scaffold pilot slice.
; - Derived from notes/c4-window-color-math-and-palette-helpers-23dc-26ed.md.
; - Original instruction flow is preserved in address order with explicit
;   accumulator/index-width suffixes where byte-equivalence depends on them.
; - ROM byte range, SHA-1, and source signature are tracked by
;   build/c4-build-candidate-ranges.json.
;
; Source units covered:
; - C4:23DC..C4:249A centered/fullscreen color-window presets, fixed color,
;   and the first WH0 HDMA channel-4 setup/teardown pair.

; ---------------------------------------------------------------------------
; Hardware and WRAM contracts

REGISTER_WH0                         = $002126
REGISTER_WH1                         = $002127
REGISTER_WH2                         = $002128
REGISTER_WH3                         = $002129
REGISTER_WBGLOG                      = $00212A
REGISTER_WOBJLOG                     = $00212B
REGISTER_TMW                         = $00212E
REGISTER_CGWSEL                      = $002130
REGISTER_CGADSUB                     = $002131
REGISTER_COLDATA                     = $002132
REGISTER_WOBJSEL                     = $002125

DMA4_DMAP                            = $004340
DMA4_BBAD                            = $004341
DMA4_A1T                             = $004342
DMA4_A1B                             = $004344
DMA4_DASB                            = $004347
DMA5_DMAP                            = $004350
DMA5_BBAD                            = $004351
DMA5_A1T                             = $004352
DMA5_A1B                             = $004354
DMA5_DASB                            = $004357

HDMA_ENABLE_SHADOW                   = $001F
HDMA_CHANNEL4_ENABLE_BIT             = $10
HDMA_CHANNEL4_DISABLE_MASK           = $EF
HDMA_CHANNEL5_ENABLE_BIT             = $20
HDMA_CHANNEL5_DISABLE_MASK           = $DF

FIXED_COLOR_RED_COMPONENT            = $9E37
FIXED_COLOR_GREEN_COMPONENT          = $9E38
FIXED_COLOR_BLUE_COMPONENT           = $9E39

COLOR_WINDOW_CENTER_LEFT             = $80
COLOR_WINDOW_CENTER_RIGHT            = $7F
COLOR_WINDOW_FULLSCREEN_LEFT         = $00
COLOR_WINDOW_FULLSCREEN_RIGHT        = $FF
COLOR_WINDOW_CENTER_CGWSEL           = $10
COLOR_WINDOW_FULLSCREEN_CGWSEL       = $20
COLOR_WINDOW_LAYER_MASK              = $13
COLOR_WINDOW_LOGIC_CLEAR             = $00

HDMA_MODE_INDIRECT_2REG              = $01
HDMA_TARGET_WH0                      = $26
HDMA_TARGET_WH2                      = $28
WOBJSEL_DUAL_WINDOW                  = $A0
WOBJSEL_OBJECT_WINDOW                = $20
CGADSUB_COLOR_MATH_33                = $33
CGADSUB_SUBTRACT_HALF_B3             = $B3
FIXED_COLOR_FULL_WHITE               = $FF
FIXED_COLOR_CENTERED_SUBTRACT        = $EF
FIXED_COLOR_SELECTOR_MASK            = $E0

; ---------------------------------------------------------------------------
; C4:23DC

; SetCenteredColorWindowRangePreset
C423DC_SetCenteredColorWindowRangePreset:
    sep #$20
    lda.b #COLOR_WINDOW_CENTER_LEFT
    sta.l REGISTER_WH0
    sta.l REGISTER_WH2
    dec A
    sta.l REGISTER_WH1
    sta.l REGISTER_WH3
    lda.b #COLOR_WINDOW_CENTER_CGWSEL
    sta.l REGISTER_CGWSEL
    lda.b #COLOR_WINDOW_LAYER_MASK
    sta.l REGISTER_TMW
    lda.b #COLOR_WINDOW_LOGIC_CLEAR
    sta.l REGISTER_WBGLOG
    sta.l REGISTER_WOBJLOG
    rep #$20
    rtl

; ---------------------------------------------------------------------------
; C4:240A

; SetFullscreenColorWindowRangePreset
C4240A_SetFullscreenColorWindowRangePreset:
    sep #$20
    lda.b #COLOR_WINDOW_FULLSCREEN_LEFT
    sta.l REGISTER_WH0
    sta.l REGISTER_WH2
    lda.b #COLOR_WINDOW_FULLSCREEN_RIGHT
    sta.l REGISTER_WH1
    sta.l REGISTER_WH3
    lda.b #COLOR_WINDOW_FULLSCREEN_CGWSEL
    sta.l REGISTER_CGWSEL
    lda.b #COLOR_WINDOW_LAYER_MASK
    sta.l REGISTER_TMW
    lda.b #COLOR_WINDOW_LOGIC_CLEAR
    sta.l REGISTER_WBGLOG
    sta.l REGISTER_WOBJLOG
    rep #$20
    rtl

; ---------------------------------------------------------------------------
; C4:2439

; ApplyColorMathAndFixedColorFrom9e37
;
; Entry:
;   A = CGADSUB value.
; Fixed color bytes come from $9E37-$9E39 and are written with their
; red/green/blue COLDATA selector bits.
C42439_ApplyColorMathAndFixedColorFrom9e37:
    sep #$30
    sta.l REGISTER_CGADSUB
    lda FIXED_COLOR_RED_COMPONENT
    ora.b #$80
    sta.l REGISTER_COLDATA
    lda FIXED_COLOR_GREEN_COMPONENT
    ora.b #$40
    sta.l REGISTER_COLDATA
    lda FIXED_COLOR_BLUE_COMPONENT
    ora.b #$20
    sta.l REGISTER_COLDATA
    rep #$30
    rtl

; ---------------------------------------------------------------------------
; C4:245D

; StartWh0HdmaChannel4AndWhselA0
;
; Entry:
;   A = HDMA source bank / indirect bank.
;   X = HDMA table source address.
C4245D_StartWh0HdmaChannel4AndWhselA0:
    sep #$20
    sta.l DMA4_A1B
    sta.l DMA4_DASB
    lda.b #HDMA_MODE_INDIRECT_2REG
    sta.l DMA4_DMAP
    lda.b #HDMA_TARGET_WH0
    sta.l DMA4_BBAD
    rep #$20
    txa
    sta.l DMA4_A1T
    sep #$20
    lda.b #WOBJSEL_DUAL_WINDOW
    sta.l REGISTER_WOBJSEL
    lda.b #HDMA_CHANNEL4_ENABLE_BIT
    tsb.w HDMA_ENABLE_SHADOW
    rep #$20
    rtl

; ---------------------------------------------------------------------------
; C4:248A

; StopWh0HdmaChannel4AndClearWhsel
C4248A_StopWh0HdmaChannel4AndClearWhsel:
    sep #$20
    lda.b #HDMA_CHANNEL4_ENABLE_BIT
    trb.w HDMA_ENABLE_SHADOW
    lda.b #$00
    sta.l REGISTER_WOBJSEL
    rep #$20
    rtl

; ---------------------------------------------------------------------------
; C4:249A

; ApplyFullscreenColorMathWithFixedColorX
;
; Entry:
;   A = CGADSUB value.
;   X = fixed-color low component value, ORed with the COLDATA selector mask.
C4249A_ApplyFullscreenColorMathWithFixedColorX:
    sep #$30
    sta.l REGISTER_CGADSUB
    lda.b #WOBJSEL_OBJECT_WINDOW
    sta.l REGISTER_WOBJSEL
    lda.b #COLOR_WINDOW_FULLSCREEN_LEFT
    sta.l REGISTER_WH0
    lda.b #COLOR_WINDOW_FULLSCREEN_RIGHT
    sta.l REGISTER_WH1
    lda.b #COLOR_WINDOW_LAYER_MASK
    sta.w REGISTER_TMW
    lda.b #COLOR_WINDOW_LOGIC_CLEAR
    sta.l REGISTER_WBGLOG
    sta.l REGISTER_WOBJLOG
    lda.b #COLOR_WINDOW_CENTER_CGWSEL
    sta.l REGISTER_CGWSEL
    txa
    ora.b #FIXED_COLOR_SELECTOR_MASK
    sta.l REGISTER_COLDATA
    rep #$30
    rtl

; ---------------------------------------------------------------------------
; C4:24D1

; ApplyCenteredColorSubtractHalfPreset
C424D1_ApplyCenteredColorSubtractHalfPreset:
    sep #$20
    lda.b #WOBJSEL_OBJECT_WINDOW
    sta.l REGISTER_WOBJSEL
    lda.b #COLOR_WINDOW_CENTER_LEFT
    sta.l REGISTER_WH0
    dec A
    sta.l REGISTER_WH1
    lda.b #COLOR_WINDOW_LAYER_MASK
    sta.l REGISTER_TMW
    lda.b #COLOR_WINDOW_LOGIC_CLEAR
    sta.l REGISTER_WBGLOG
    sta.l REGISTER_WOBJLOG
    lda.b #COLOR_WINDOW_FULLSCREEN_CGWSEL
    sta.l REGISTER_CGWSEL
    lda.b #CGADSUB_SUBTRACT_HALF_B3
    sta.l REGISTER_CGADSUB
    lda.b #FIXED_COLOR_CENTERED_SUBTRACT
    sta.l REGISTER_COLDATA
    rep #$20
    rtl

; ---------------------------------------------------------------------------
; C4:2509

; ApplyFullscreenColorSubtractHalfPreset
C42509_ApplyFullscreenColorSubtractHalfPreset:
    sep #$20
    lda.b #WOBJSEL_OBJECT_WINDOW
    sta.l REGISTER_WOBJSEL
    lda.b #COLOR_WINDOW_FULLSCREEN_LEFT
    sta.l REGISTER_WH0
    lda.b #COLOR_WINDOW_FULLSCREEN_RIGHT
    sta.l REGISTER_WH1
    lda.b #COLOR_WINDOW_LAYER_MASK
    sta.l REGISTER_TMW
    lda.b #COLOR_WINDOW_LOGIC_CLEAR
    sta.l REGISTER_WBGLOG
    sta.l REGISTER_WOBJLOG
    lda.b #COLOR_WINDOW_FULLSCREEN_CGWSEL
    sta.l REGISTER_CGWSEL
    lda.b #CGADSUB_SUBTRACT_HALF_B3
    sta.l REGISTER_CGADSUB
    lda.b #FIXED_COLOR_FULL_WHITE
    sta.l REGISTER_COLDATA
    rep #$20
    rtl

; ---------------------------------------------------------------------------
; C4:2542

; StartWh0HdmaChannel4
C42542_StartWh0HdmaChannel4:
    sep #$20
    sta.l DMA4_A1B
    sta.l DMA4_DASB
    lda.b #HDMA_MODE_INDIRECT_2REG
    sta.l DMA4_DMAP
    lda.b #HDMA_TARGET_WH0
    sta.l DMA4_BBAD
    rep #$20
    txa
    sta.l DMA4_A1T
    sep #$20
    lda.b #HDMA_CHANNEL4_ENABLE_BIT
    tsb.w HDMA_ENABLE_SHADOW
    rep #$20
    rtl

; ---------------------------------------------------------------------------
; C4:2569 / C4:2574 / C4:257F

; SetColorMathMode33
C42569_SetColorMathMode33:
    sep #$20
    lda.b #CGADSUB_COLOR_MATH_33
    sta.l REGISTER_CGADSUB
    rep #$20
    rtl

; SetColorMathModeB3
C42574_SetColorMathModeB3:
    sep #$20
    lda.b #CGADSUB_SUBTRACT_HALF_B3
    sta.l REGISTER_CGADSUB
    rep #$20
    rtl

; ClearWh0HdmaChannel4Enable
C4257F_ClearWh0HdmaChannel4Enable:
    sep #$20
    lda HDMA_ENABLE_SHADOW
    and.b #HDMA_CHANNEL4_DISABLE_MASK
    sta HDMA_ENABLE_SHADOW
    rep #$20
    rtl

; ---------------------------------------------------------------------------
; C4:258C

; ApplyDualCenteredColorSubtractHalfPreset
C4258C_ApplyDualCenteredColorSubtractHalfPreset:
    sep #$20
    lda.b #WOBJSEL_DUAL_WINDOW
    sta.l REGISTER_WOBJSEL
    lda.b #COLOR_WINDOW_CENTER_LEFT
    sta.l REGISTER_WH0
    sta.l REGISTER_WH2
    dec A
    sta.l REGISTER_WH1
    sta.l REGISTER_WH3
    lda.b #COLOR_WINDOW_LAYER_MASK
    sta.l REGISTER_TMW
    lda.b #COLOR_WINDOW_LOGIC_CLEAR
    sta.l REGISTER_WBGLOG
    sta.l REGISTER_WOBJLOG
    lda.b #COLOR_WINDOW_FULLSCREEN_CGWSEL
    sta.l REGISTER_CGWSEL
    lda.b #CGADSUB_SUBTRACT_HALF_B3
    sta.l REGISTER_CGADSUB
    lda.b #FIXED_COLOR_CENTERED_SUBTRACT
    sta.l REGISTER_COLDATA
    rep #$20
    rtl

; ---------------------------------------------------------------------------
; C4:25CC / C4:25F3

; StartWh0HdmaChannel4AltEntry
C425CC_StartWh0HdmaChannel4AltEntry:
    sep #$20
    sta.l DMA4_A1B
    sta.l DMA4_DASB
    lda.b #HDMA_MODE_INDIRECT_2REG
    sta.l DMA4_DMAP
    lda.b #HDMA_TARGET_WH0
    sta.l DMA4_BBAD
    rep #$20
    txa
    sta.l DMA4_A1T
    sep #$20
    lda.b #HDMA_CHANNEL4_ENABLE_BIT
    tsb.w HDMA_ENABLE_SHADOW
    rep #$20
    rtl

; ClearWh0HdmaChannel4EnableViaTrb
C425F3_ClearWh0HdmaChannel4EnableViaTrb:
    sep #$20
    lda.b #HDMA_CHANNEL4_ENABLE_BIT
    trb.w HDMA_ENABLE_SHADOW
    rep #$20
    rtl

; ---------------------------------------------------------------------------
; C4:25FD / C4:2624

; StartWh2HdmaChannel5
C425FD_StartWh2HdmaChannel5:
    sep #$20
    sta.l DMA5_A1B
    sta.l DMA5_DASB
    lda.b #HDMA_MODE_INDIRECT_2REG
    sta.l DMA5_DMAP
    lda.b #HDMA_TARGET_WH2
    sta.l DMA5_BBAD
    rep #$20
    txa
    sta.l DMA5_A1T
    sep #$20
    lda.b #HDMA_CHANNEL5_ENABLE_BIT
    tsb.w HDMA_ENABLE_SHADOW
    rep #$20
    rtl

; ClearWh2HdmaChannel5Enable
C42624_ClearWh2HdmaChannel5Enable:
    sep #$20
    lda HDMA_ENABLE_SHADOW
    and.b #HDMA_CHANNEL5_DISABLE_MASK
    sta HDMA_ENABLE_SHADOW
    rep #$20
    rtl
