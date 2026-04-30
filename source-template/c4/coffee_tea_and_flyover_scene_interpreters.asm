; EarthBound C4 coffee/tea and flyover scene interpreter prototype.
;
; Source-emission status:
; - Prototype level: build-candidate
; - C4 source-bank scaffold slice.
; - Derived from notes/landing-and-coffee-tea-visual-helpers-c492d2-c49d1e.md,
;   refs/ebsrc-main bank04 include order, and legacy Routine_Macros_EB.
; - ROM byte range, SHA-1, and source signature are tracked by
;   build/c4-build-candidate-ranges.json.
;
; Source units covered:
; - C4:9D6A..C4:9EA4 named coffee/tea scene script interpreter.
; - C4:9EA4..C4:9EC4 preserved flyover text pointer table.
; - C4:9EC4..C4:9FE1 flyover intro text scene interpreter.

; ---------------------------------------------------------------------------
; External contracts used by this module

C018F3_RestoreOrRefreshDisplayState          = $C018F3
C08726_BlankWaitAndDisableHdma               = $C08726
C08744_CloseDisplayTransitionBracket         = $C08744
C08756_WaitOneFrameAndPollInput              = $C08756
C087CE_ApplyDisplayStateOrLayerPreset        = $C087CE
C08814_OpenDisplayTransitionBracket          = $C08814
C0886C_SetDisplayTransitionState             = $C0886C
C0887A_ClearDisplayTransitionState           = $C0887A
C088B1_WaitOneFrameAndUpdateDisplayState     = $C088B1
C2DB3F_UpdateBattleBgVisualState             = $C2DB3F
C47370_DisplayTextTokenOrPrompt              = $C47370
C4800B_RestoreC4VisualState                  = $C4800B

C49A4B_WaitFrameAndUpdateBattleBgVisualState_Near = $9A4B
C49A56_InitCoffeeTeaTileBufferAndTransferState_Ext = $C49A56
C49B6E_UploadCoffeeTeaTileBufferWindow_Ext   = $C49B6E
C49C56_AdvanceCoffeeTeaTileScrollState_Ext   = $C49C56
C49CA8_AdvanceCoffeeTeaRowRevealCursor_Ext   = $C49CA8
C49CC3_RenderCoffeeTeaTokenString_Ext        = $C49CC3
C49D16_RenderSingleCoffeeTeaTileToken_Ext    = $C49D16
C49D1E_AdvanceCoffeeTeaVramOffsetByTileRow_Ext = $C49D1E

; ---------------------------------------------------------------------------
; WRAM / data contracts

COFFEE_SCENE_TEXT_BASE_LOW                   = $0000
TEA_SCENE_TEXT_BASE_LOW                      = $0652
COFFEE_TEA_SCENE_TEXT_BANK                   = $00E1
FLYOVER_TEXT_POINTER_TABLE                   = $C49EA4
FLYOVER_TEXT_POINTER_TABLE_BANK              = $00C4

COFFEE_TEA_TILE_WINDOW_INDEX                 = $9F2D
COFFEE_TEA_ROW_TILE_LIMIT                    = $2000
COFFEE_TEA_FRAME_STEP                        = $0018
COFFEE_TEA_TOKEN_WIDTH                       = $000C
COFFEE_TEA_SCRIPT_TERMINATOR                 = $0000
COFFEE_TEA_CMD_SCROLL_PAGE                   = $0009
COFFEE_TEA_CMD_ADVANCE_ROW                   = $0001
COFFEE_TEA_CMD_TOKEN_STRING                  = $0008
FLYOVER_CMD_SET_WINDOW_INDEX                 = $0002
FLYOVER_END_WAIT_FRAMES                      = $00B4
SCENE_CLEAR_WORDS                            = $0380
SCENE_CLEAR_BASE                             = $7DFE
DISPLAY_SHADOW_1A                            = $001A
COFFEE_TEA_DISPLAY_MODE_04                   = $04
FLYOVER_DISPLAY_MODE_17                      = $17
SCENE_BUSY_FLAG_5E6E                         = $5E6E
FLYOVER_STATE_WORD_10E4                      = $10E4
FLYOVER_STATE_MASK_C000                      = $C000
INPUT_STATE_28                               = $0028

; ---------------------------------------------------------------------------
; C4:9D6A

; RunCoffeeTeaScene
C49D6A_RunCoffeeTeaScene:
    rep #$31
    phd
    pha
    tdc
    adc #$FFF0
    tcd
    pla
    sta $02
    ldy #$0000
    ldx #$0001
    txa
    jsl C08814_OpenDisplayTransitionBracket
    jsl C49A56_InitCoffeeTeaTileBufferAndTransferState_Ext
    jsl C088B1_WaitOneFrameAndUpdateDisplayState
    lda $02
    bne C49D92_RunCoffeeTeaScene_TeaPrompt
    ldx #$00E8
    bra C49D95_RunCoffeeTeaScene_DisplayPrompt

C49D92_RunCoffeeTeaScene_TeaPrompt:
    ldx #$00EA
C49D95_RunCoffeeTeaScene_DisplayPrompt:
    lda $02
    bne C49D9E_RunCoffeeTeaScene_TeaResponsePrompt
    ldy #$00E7
    bra C49DA1_RunCoffeeTeaScene_DisplayResponsePrompt

C49D9E_RunCoffeeTeaScene_TeaResponsePrompt:
    ldy #$00E9
C49DA1_RunCoffeeTeaScene_DisplayResponsePrompt:
    tya
    jsl C47370_DisplayTextTokenOrPrompt
    ldx #$0001
    txa
    jsl C0886C_SetDisplayTransitionState
    lda #$001C
    sta.w COFFEE_TEA_TILE_WINDOW_INDEX
    lda #$0000
    sta $04
    lda $02
    bne C49DC9_RunCoffeeTeaScene_UseTeaScript
    lda #COFFEE_SCENE_TEXT_BASE_LOW
    sta $06
    lda #COFFEE_TEA_SCENE_TEXT_BANK
    sta $08
    bra C49DD3_RunCoffeeTeaScene_StartScript

C49DC9_RunCoffeeTeaScene_UseTeaScript:
    lda #TEA_SCENE_TEXT_BASE_LOW
    sta $06
    lda #COFFEE_TEA_SCENE_TEXT_BANK
    sta $08
C49DD3_RunCoffeeTeaScene_StartScript:
    stz.w SCENE_BUSY_FLAG_5E6E
C49DD6_RunCoffeeTeaScene_ReadCommand:
    lda [$06]
    and #$00FF
    inc $06
    cmp #COFFEE_TEA_SCRIPT_TERMINATOR
    beq C49E58_RunCoffeeTeaScene_EndScript
    cmp #COFFEE_TEA_CMD_SCROLL_PAGE
    beq C49DF3_RunCoffeeTeaScene_ScrollPage
    cmp #COFFEE_TEA_CMD_ADVANCE_ROW
    beq C49E2B_RunCoffeeTeaScene_AdvanceRow
    cmp #COFFEE_TEA_CMD_TOKEN_STRING
    beq C49E39_RunCoffeeTeaScene_TokenString
    bra C49E4B_RunCoffeeTeaScene_SingleToken

C49DF3_RunCoffeeTeaScene_ScrollPage:
    lda $04
    jsl C49D1E_AdvanceCoffeeTeaVramOffsetByTileRow_Ext
    tax
    stx $0E
    lda #COFFEE_TEA_FRAME_STEP
    jsl C49B6E_UploadCoffeeTeaTileBufferWindow_Ext
    jsl C2DB3F_UpdateBattleBgVisualState
    bra C49E14_RunCoffeeTeaScene_ContinueTileAdvanceCheck

C49E09_RunCoffeeTeaScene_AdvanceTileRow:
    txa
    jsl C49D1E_AdvanceCoffeeTeaVramOffsetByTileRow_Ext
    tax
    stx $0E
    jsr C49A4B_WaitFrameAndUpdateBattleBgVisualState_Near
C49E14_RunCoffeeTeaScene_ContinueTileAdvanceCheck:
    ldx $0E
    cpx #COFFEE_TEA_ROW_TILE_LIMIT
    bcc C49E09_RunCoffeeTeaScene_AdvanceTileRow
    txa
    sec
    sbc #COFFEE_TEA_ROW_TILE_LIMIT
    sta $04
    lda #COFFEE_TEA_FRAME_STEP
    jsl C49C56_AdvanceCoffeeTeaTileScrollState_Ext
    bra C49DD6_RunCoffeeTeaScene_ReadCommand

C49E2B_RunCoffeeTeaScene_AdvanceRow:
    sep #$20
    lda [$06]
    rep #$20
    inc $06
    jsl C49CA8_AdvanceCoffeeTeaRowRevealCursor_Ext
    bra C49DD6_RunCoffeeTeaScene_ReadCommand

C49E39_RunCoffeeTeaScene_TokenString:
    lda [$06]
    and #$00FF
    tay
    inc $06
    ldx #COFFEE_TEA_TOKEN_WIDTH
    tya
    jsl C49CC3_RenderCoffeeTeaTokenString_Ext
    bra C49DD6_RunCoffeeTeaScene_ReadCommand

C49E4B_RunCoffeeTeaScene_SingleToken:
    ldy #COFFEE_TEA_TOKEN_WIDTH
    ldx #$0000
    jsl C49D16_RenderSingleCoffeeTeaTileToken_Ext
    jmp C49DD6_RunCoffeeTeaScene_ReadCommand

C49E58_RunCoffeeTeaScene_EndScript:
    ldx #$0001
    txa
    jsl C0887A_ClearDisplayTransitionState
    bra C49E65_RunCoffeeTeaScene_WaitForInputReleaseCheck

C49E62_RunCoffeeTeaScene_WaitForInputRelease:
    jsr C49A4B_WaitFrameAndUpdateBattleBgVisualState_Near
C49E65_RunCoffeeTeaScene_WaitForInputReleaseCheck:
    lda.w INPUT_STATE_28
    and #$00FF
    bne C49E62_RunCoffeeTeaScene_WaitForInputRelease
    jsl C08726_BlankWaitAndDisableHdma
    jsl C018F3_RestoreOrRefreshDisplayState
    ldy #SCENE_CLEAR_BASE
    ldx #SCENE_CLEAR_WORDS
    bra C49E86_RunCoffeeTeaScene_ClearTileBufferCheck

C49E7D_RunCoffeeTeaScene_ClearTileBuffer:
    lda #$0000
    sta.w $0000,y
    iny
    iny
    dex
C49E86_RunCoffeeTeaScene_ClearTileBufferCheck:
    bne C49E7D_RunCoffeeTeaScene_ClearTileBuffer
    lda #$00FF
    sta.w SCENE_BUSY_FLAG_5E6E
    jsl C08726_BlankWaitAndDisableHdma
    jsl C4800B_RestoreC4VisualState
    jsl C08744_CloseDisplayTransitionBracket
    ldx #$0001
    txa
    jsl C0886C_SetDisplayTransitionState
    pld
    rtl

; ---------------------------------------------------------------------------
; C4:9EA4..C4:9EC4 is FlyoverIntroTextPointerTable data.

; ---------------------------------------------------------------------------
; C4:9EC4

; RunFlyoverIntroTextSceneByIndex

; ---------------------------------------------------------------------------
; C4:9EA4

C49EA4_FlyoverIntroTextPointerTable:
    ; data bytes: C4:9EA4..C4:9EC4
    db $86,$0B,$E1,$00,$9C,$0B,$E1,$00,$C2,$0B,$E1,$00,$D2,$0B,$E1,$00
    db $FD,$0B,$E1,$00,$1B,$0C,$E1,$00,$38,$0C,$E1,$00,$61,$0C,$E1,$00

C49EC4_RunFlyoverIntroTextSceneByIndex:
    rep #$31
    phd
    pha
    tdc
    adc #$FFF0
    tcd
    pla
    sta $0E
    ldx #FLYOVER_STATE_WORD_10E4
    lda.w $0000,x
    sta $02
    ora #FLYOVER_STATE_MASK_C000
    sta.w $0000,x
    jsl C49A56_InitCoffeeTeaTileBufferAndTransferState_Ext
    lda #FLYOVER_TEXT_POINTER_TABLE
    sta $0A
    lda #FLYOVER_TEXT_POINTER_TABLE_BANK
    sta $0C
    lda $0E
    asl
    asl
    clc
    adc $0A
    sta $0A
    ldy #$0002
    lda [$0A],y
    tay
    lda [$0A]
    sta $06
    sty $08
    stz.w SCENE_BUSY_FLAG_5E6E
C49F04_RunFlyoverIntroTextScene_ReadCommand:
    lda [$06]
    and #$00FF
    inc $06
    cmp #COFFEE_TEA_SCRIPT_TERMINATOR
    beq C49F72_RunFlyoverIntroTextScene_EndScript
    cmp #FLYOVER_CMD_SET_WINDOW_INDEX
    beq C49F26_RunFlyoverIntroTextScene_SetWindowIndex
    cmp #COFFEE_TEA_CMD_SCROLL_PAGE
    beq C49F32_RunFlyoverIntroTextScene_ScrollPage
    cmp #COFFEE_TEA_CMD_ADVANCE_ROW
    beq C49F46_RunFlyoverIntroTextScene_AdvanceRow
    cmp #COFFEE_TEA_CMD_TOKEN_STRING
    beq C49F54_RunFlyoverIntroTextScene_TokenString
    bra C49F66_RunFlyoverIntroTextScene_SingleToken

C49F26_RunFlyoverIntroTextScene_SetWindowIndex:
    lda [$06]
    and #$00FF
    sta.w COFFEE_TEA_TILE_WINDOW_INDEX
    inc $06
    bra C49F04_RunFlyoverIntroTextScene_ReadCommand

C49F32_RunFlyoverIntroTextScene_ScrollPage:
    lda #COFFEE_TEA_FRAME_STEP
    jsl C49B6E_UploadCoffeeTeaTileBufferWindow_Ext
    jsl C08756_WaitOneFrameAndPollInput
    lda #COFFEE_TEA_FRAME_STEP
    jsl C49C56_AdvanceCoffeeTeaTileScrollState_Ext
    bra C49F04_RunFlyoverIntroTextScene_ReadCommand

C49F46_RunFlyoverIntroTextScene_AdvanceRow:
    sep #$20
    lda [$06]
    rep #$20
    inc $06
    jsl C49CA8_AdvanceCoffeeTeaRowRevealCursor_Ext
    bra C49F04_RunFlyoverIntroTextScene_ReadCommand

C49F54_RunFlyoverIntroTextScene_TokenString:
    lda [$06]
    and #$00FF
    tay
    inc $06
    ldx #COFFEE_TEA_TOKEN_WIDTH
    tya
    jsl C49CC3_RenderCoffeeTeaTokenString_Ext
    bra C49F04_RunFlyoverIntroTextScene_ReadCommand

C49F66_RunFlyoverIntroTextScene_SingleToken:
    ldy #COFFEE_TEA_TOKEN_WIDTH
    ldx #$0000
    jsl C49D16_RenderSingleCoffeeTeaTileToken_Ext
    bra C49F04_RunFlyoverIntroTextScene_ReadCommand

C49F72_RunFlyoverIntroTextScene_EndScript:
    sep #$20
    lda.b #COFFEE_TEA_DISPLAY_MODE_04
    sta.w DISPLAY_SHADOW_1A
    ldy #$0000
    ldx #$0003
    rep #$20
    lda #$0001
    jsl C087CE_ApplyDisplayStateOrLayerPreset
    ldx #$0000
    stx $0E
    bra C49F98_RunFlyoverIntroTextScene_WaitCheck

C49F8F_RunFlyoverIntroTextScene_WaitFrame:
    jsl C08756_WaitOneFrameAndPollInput
    ldx $0E
    inx
    stx $0E
C49F98_RunFlyoverIntroTextScene_WaitCheck:
    cpx #FLYOVER_END_WAIT_FRAMES
    bcc C49F8F_RunFlyoverIntroTextScene_WaitFrame
    ldy #$0000
    ldx #$0003
    lda #$0001
    jsl C08814_OpenDisplayTransitionBracket
    sep #$20
    lda.b #FLYOVER_DISPLAY_MODE_17
    sta.w DISPLAY_SHADOW_1A
    ldy #SCENE_CLEAR_BASE
    ldx #SCENE_CLEAR_WORDS
    bra C49FC4_RunFlyoverIntroTextScene_ClearTileBufferCheck

C49FB9_RunFlyoverIntroTextScene_ClearTileBuffer:
    rep #$20
    lda #$0000
    sta.w $0000,y
    iny
    iny
    dex
C49FC4_RunFlyoverIntroTextScene_ClearTileBufferCheck:
    bne C49FB9_RunFlyoverIntroTextScene_ClearTileBuffer
    rep #$20
    lda #$00FF
    sta.w SCENE_BUSY_FLAG_5E6E
    jsl C08726_BlankWaitAndDisableHdma
    jsl C4800B_RestoreC4VisualState
    lda $02
    sta.w FLYOVER_STATE_WORD_10E4
    jsl C08744_CloseDisplayTransitionBracket
    pld
    rtl
