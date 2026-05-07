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
;   one-shot color math presets, and WH0/WH2 HDMA setup/teardown helpers.

; ---------------------------------------------------------------------------
; Hardware and WRAM contracts
;
; These helpers write the PPU registers directly and maintain only the local
; HDMA enable shadow at $001F. They do not queue through the C0 renderer layer,
; so call sites must already be inside an appropriate display/effect bracket.

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

DMA4_HDMA_MODE                       = $004340
DMA4_BBUS_TARGET                     = $004341
DMA4_HDMA_TABLE_ADDR                 = $004342
DMA4_HDMA_TABLE_BANK                 = $004344
DMA4_INDIRECT_BANK                   = $004347
DMA5_HDMA_MODE                       = $004350
DMA5_BBUS_TARGET                     = $004351
DMA5_HDMA_TABLE_ADDR                 = $004352
DMA5_HDMA_TABLE_BANK                 = $004354
DMA5_INDIRECT_BANK                   = $004357

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
WOBJSEL_NO_WINDOW                    = $00
CGADSUB_COLOR_MATH_33                = $33
CGADSUB_SUBTRACT_HALF_B3             = $B3
FIXED_COLOR_FULL_WHITE               = $FF
FIXED_COLOR_CENTERED_SUBTRACT        = $EF
FIXED_COLOR_SELECTOR_MASK            = $E0
COLDATA_RED_SELECTOR                 = $80
COLDATA_GREEN_SELECTOR               = $40
COLDATA_BLUE_SELECTOR                = $20

; ---------------------------------------------------------------------------
; C4:23DC

; SetCenteredColorWindowRangePreset
;
; Side effects: writes WH0/WH2 = $80, WH1/WH3 = $7F, CGWSEL/TMW, and clears
; WBGLOG/WOBJLOG. This is a color-window preset, not a general window API.
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
;
; Side effects: writes full WH0/WH2 and WH1/WH3 ranges, CGWSEL/TMW, and clears
; WBGLOG/WOBJLOG.
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
    ora.b #COLDATA_RED_SELECTOR
    sta.l REGISTER_COLDATA
    lda FIXED_COLOR_GREEN_COMPONENT
    ora.b #COLDATA_GREEN_SELECTOR
    sta.l REGISTER_COLDATA
    lda FIXED_COLOR_BLUE_COMPONENT
    ora.b #COLDATA_BLUE_SELECTOR
    sta.l REGISTER_COLDATA
    rep #$30
    rtl

; ---------------------------------------------------------------------------
; C4:245D

; StartWh0HdmaChannel4AndWhselA0
;
; Entry:
;   A = HDMA table bank, also written as the indirect data bank.
;   X = HDMA table address.
; Side effects: programs DMA channel 4 for indirect HDMA to WH0/WH1, sets
; WOBJSEL to $A0, and sets bit $10 in the $001F HDMA enable shadow.
C4245D_StartWh0HdmaChannel4AndWhselA0:
    sep #$20
    sta.l DMA4_HDMA_TABLE_BANK
    sta.l DMA4_INDIRECT_BANK
    lda.b #HDMA_MODE_INDIRECT_2REG
    sta.l DMA4_HDMA_MODE
    lda.b #HDMA_TARGET_WH0
    sta.l DMA4_BBUS_TARGET
    rep #$20
    txa
    sta.l DMA4_HDMA_TABLE_ADDR
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
;
; Side effects: clears bit $10 in the $001F HDMA enable shadow and clears
; WOBJSEL. It does not clear the DMA4 descriptor fields.
C4248A_StopWh0HdmaChannel4AndClearWhsel:
    sep #$20
    lda.b #HDMA_CHANNEL4_ENABLE_BIT
    trb.w HDMA_ENABLE_SHADOW
    lda.b #WOBJSEL_NO_WINDOW
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
; Side effects: writes CGADSUB, WOBJSEL, WH0/WH1, TMW, WBGLOG/WOBJLOG,
; CGWSEL, and one COLDATA byte.
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
;
; Entry:
;   A = HDMA table bank, also written as the indirect data bank.
;   X = HDMA table address.
; Side effects: programs DMA channel 4 for indirect HDMA to WH0/WH1 and sets
; bit $10 in the $001F HDMA enable shadow. WOBJSEL is left unchanged.
C42542_StartWh0HdmaChannel4:
    sep #$20
    sta.l DMA4_HDMA_TABLE_BANK
    sta.l DMA4_INDIRECT_BANK
    lda.b #HDMA_MODE_INDIRECT_2REG
    sta.l DMA4_HDMA_MODE
    lda.b #HDMA_TARGET_WH0
    sta.l DMA4_BBUS_TARGET
    rep #$20
    txa
    sta.l DMA4_HDMA_TABLE_ADDR
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
;
; Side effects: clears bit $10 in the $001F HDMA enable shadow through an
; AND/store sequence. WOBJSEL and the DMA4 descriptor fields are left unchanged.
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
;
; Entry:
;   A = HDMA table bank, also written as the indirect data bank.
;   X = HDMA table address.
; Side effects match C4:2542: programs DMA channel 4 for WH0/WH1 HDMA and
; sets bit $10 in the $001F HDMA enable shadow. The distinct entry name is kept
; until call-site ownership proves whether it is semantically separate.
C425CC_StartWh0HdmaChannel4AltEntry:
    sep #$20
    sta.l DMA4_HDMA_TABLE_BANK
    sta.l DMA4_INDIRECT_BANK
    lda.b #HDMA_MODE_INDIRECT_2REG
    sta.l DMA4_HDMA_MODE
    lda.b #HDMA_TARGET_WH0
    sta.l DMA4_BBUS_TARGET
    rep #$20
    txa
    sta.l DMA4_HDMA_TABLE_ADDR
    sep #$20
    lda.b #HDMA_CHANNEL4_ENABLE_BIT
    tsb.w HDMA_ENABLE_SHADOW
    rep #$20
    rtl

; ClearWh0HdmaChannel4EnableViaTrb
;
; Side effects: clears bit $10 in the $001F HDMA enable shadow through TRB.
C425F3_ClearWh0HdmaChannel4EnableViaTrb:
    sep #$20
    lda.b #HDMA_CHANNEL4_ENABLE_BIT
    trb.w HDMA_ENABLE_SHADOW
    rep #$20
    rtl

; ---------------------------------------------------------------------------
; C4:25FD / C4:2624

; StartWh2HdmaChannel5
;
; Entry:
;   A = HDMA table bank, also written as the indirect data bank.
;   X = HDMA table address.
; Side effects: programs DMA channel 5 for indirect HDMA to WH2/WH3 and sets
; bit $20 in the $001F HDMA enable shadow.
C425FD_StartWh2HdmaChannel5:
    sep #$20
    sta.l DMA5_HDMA_TABLE_BANK
    sta.l DMA5_INDIRECT_BANK
    lda.b #HDMA_MODE_INDIRECT_2REG
    sta.l DMA5_HDMA_MODE
    lda.b #HDMA_TARGET_WH2
    sta.l DMA5_BBUS_TARGET
    rep #$20
    txa
    sta.l DMA5_HDMA_TABLE_ADDR
    sep #$20
    lda.b #HDMA_CHANNEL5_ENABLE_BIT
    tsb.w HDMA_ENABLE_SHADOW
    rep #$20
    rtl

; ClearWh2HdmaChannel5Enable
;
; Side effects: clears bit $20 in the $001F HDMA enable shadow. DMA5
; descriptor fields are left unchanged.
C42624_ClearWh2HdmaChannel5Enable:
    sep #$20
    lda HDMA_ENABLE_SHADOW
    and.b #HDMA_CHANNEL5_DISABLE_MASK
    sta HDMA_ENABLE_SHADOW
    rep #$20
    rtl
