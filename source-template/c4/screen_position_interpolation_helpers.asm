; EarthBound C4 screen-position interpolation helper prototype.
;
; Source-emission status:
; - Prototype level: build-candidate
; - C4 source-bank scaffold pilot slice.
; - Derived from notes/c4-window-color-math-and-palette-helpers-23dc-26ed.md.
; - ROM byte range, SHA-1, and source signature are tracked by
;   build/c4-build-candidate-ranges.json.
;
; Source units covered:
; - C4:2631..C4:26ED screen-position interpolation and live-entity rebase.

; ---------------------------------------------------------------------------
; External contracts used by this module

C0B40B_CosineOrSineProjectionHelper = $C0B40B
C0B400_SineOrCosineProjectionHelper = $C0B400
C01731_RefreshMapPositionFromScreenOrigin = $C01731

; ---------------------------------------------------------------------------
; WRAM contracts

SCREEN_ORIGIN_X_CURRENT              = $0031
SCREEN_ORIGIN_Y_CURRENT              = $0033
SCREEN_ORIGIN_X_APPLIED              = $0035
SCREEN_ORIGIN_Y_APPLIED              = $0037

SCREEN_STEP_X_FRAC_DELTA             = $3C22
SCREEN_STEP_X_SIGN_DELTA             = $3C24
SCREEN_STEP_Y_FRAC_DELTA             = $3C26
SCREEN_STEP_Y_SIGN_DELTA             = $3C28
SCREEN_STEP_X_FRAC_ACCUM             = $3C2A
SCREEN_STEP_X_CURRENT                = $3C2C
SCREEN_STEP_Y_FRAC_ACCUM             = $3C2E
SCREEN_STEP_Y_CURRENT                = $3C30

LIVE_ENTITY_STATUS_TABLE             = $0A62
LIVE_ENTITY_WORLD_X_TABLE            = $0B8E
LIVE_ENTITY_WORLD_Y_TABLE            = $0BCA
LIVE_ENTITY_SCREEN_X_TABLE           = $0B16
LIVE_ENTITY_SCREEN_Y_TABLE           = $0B52
LIVE_ENTITY_SLOT_BYTES_END           = $003C

ANGLE_HALF_TURN_OFFSET               = $0080
ANGLE_BYTE_MASK                      = $00FF
SIGN_EXTENSION_HIGH_BYTE             = $FF00

; ---------------------------------------------------------------------------
; C4:2631

; InitScreenPositionInterpolationFromAngle
;
; Entry:
;   A = speed or magnitude input.
;   X = angle byte.
C42631_InitScreenPositionInterpolationFromAngle:
    rep #$30
    stz SCREEN_STEP_X_FRAC_DELTA
    stz SCREEN_STEP_X_SIGN_DELTA
    stz SCREEN_STEP_Y_FRAC_DELTA
    stz SCREEN_STEP_Y_SIGN_DELTA
    tay
    txa
    clc
    adc #ANGLE_HALF_TURN_OFFSET
    and #ANGLE_BYTE_MASK
    tax
    phx
    tya
    jsl C0B40B_CosineOrSineProjectionHelper
    sta SCREEN_STEP_X_FRAC_DELTA+1
    lda SCREEN_STEP_X_FRAC_DELTA+1
    bpl C42660_InitScreenPositionInterpolationFromAngle_XPositive
    lda #SIGN_EXTENSION_HIGH_BYTE
    ora SCREEN_STEP_X_SIGN_DELTA
    sta SCREEN_STEP_X_SIGN_DELTA
C42660_InitScreenPositionInterpolationFromAngle_XPositive:
    plx
    tya
    jsl C0B400_SineOrCosineProjectionHelper
    sta SCREEN_STEP_Y_FRAC_DELTA+1
    lda SCREEN_STEP_Y_FRAC_DELTA+1
    bpl C42677_InitScreenPositionInterpolationFromAngle_YPositive
    lda #SIGN_EXTENSION_HIGH_BYTE
    ora SCREEN_STEP_Y_SIGN_DELTA
    sta SCREEN_STEP_Y_SIGN_DELTA
C42677_InitScreenPositionInterpolationFromAngle_YPositive:
    lda SCREEN_ORIGIN_X_CURRENT
    sta SCREEN_STEP_X_CURRENT
    lda SCREEN_ORIGIN_Y_CURRENT
    sta SCREEN_STEP_Y_CURRENT
    stz SCREEN_STEP_X_FRAC_ACCUM
    stz SCREEN_STEP_Y_FRAC_ACCUM
    rtl

; ---------------------------------------------------------------------------
; C4:268A

; StepScreenPositionInterpolationAndApply
C4268A_StepScreenPositionInterpolationAndApply:
    lda SCREEN_STEP_X_FRAC_DELTA
    clc
    adc SCREEN_STEP_X_FRAC_ACCUM
    sta SCREEN_STEP_X_FRAC_ACCUM
    lda SCREEN_STEP_X_SIGN_DELTA
    adc SCREEN_STEP_X_CURRENT
    sta SCREEN_STEP_X_CURRENT
    sta SCREEN_ORIGIN_X_CURRENT
    sta SCREEN_ORIGIN_X_APPLIED
    lda SCREEN_STEP_Y_FRAC_DELTA
    clc
    adc SCREEN_STEP_Y_FRAC_ACCUM
    sta SCREEN_STEP_Y_FRAC_ACCUM
    lda SCREEN_STEP_Y_SIGN_DELTA
    adc SCREEN_STEP_Y_CURRENT
    sta SCREEN_STEP_Y_CURRENT
    sta SCREEN_ORIGIN_Y_CURRENT
    sta SCREEN_ORIGIN_Y_APPLIED
    lda SCREEN_ORIGIN_X_CURRENT
    ldx SCREEN_ORIGIN_Y_CURRENT
    jsl C01731_RefreshMapPositionFromScreenOrigin
    rtl

; ---------------------------------------------------------------------------
; C4:26C7

; RebaseLiveEntityPositionsToScreenOrigin
C426C7_RebaseLiveEntityPositionsToScreenOrigin:
    rep #$30
    ldx #$0000
C426CC_RebaseLiveEntityPositionsToScreenOrigin_Loop:
    lda LIVE_ENTITY_STATUS_TABLE,X
    bmi C426E5_RebaseLiveEntityPositionsToScreenOrigin_Next
    lda LIVE_ENTITY_WORLD_X_TABLE,X
    sec
    sbc SCREEN_ORIGIN_X_CURRENT
    sta LIVE_ENTITY_SCREEN_X_TABLE,X
    lda LIVE_ENTITY_WORLD_Y_TABLE,X
    sec
    sbc SCREEN_ORIGIN_Y_CURRENT
    sta LIVE_ENTITY_SCREEN_Y_TABLE,X
C426E5_RebaseLiveEntityPositionsToScreenOrigin_Next:
    inx
    inx
    cpx #LIVE_ENTITY_SLOT_BYTES_END
    bne C426CC_RebaseLiveEntityPositionsToScreenOrigin_Loop
    rtl
