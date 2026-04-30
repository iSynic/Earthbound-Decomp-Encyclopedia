; EarthBound C4 coffee/tea tile-buffer helper prototype.
;
; Source-emission status:
; - Prototype level: build-candidate
; - C4 source-bank scaffold slice.
; - Derived from notes/landing-and-coffee-tea-visual-helpers-c492d2-c49d1e.md
;   and the legacy Routine_Macros_EB reference.
; - ROM byte range, SHA-1, and source signature are tracked by
;   build/c4-build-candidate-ranges.json.
;
; Source units covered:
; - C4:9841..C4:9D6A coffee/tea and flyover tile-buffer preparation,
;   token rendering, scroll/window upload, and VRAM offset advancement helpers.

; ---------------------------------------------------------------------------
; External contracts used by this module

C08726_BlankWaitAndDisableHdma               = $C08726
C08744_CloseDisplayTransitionBracket         = $C08744
C08756_WaitOneFrameAndPollInput              = $C08756
C088B1_WaitOneFrameAndUpdateDisplayState     = $C088B1
C08B26_ApplyBgScrollOrTilemapUpdate          = $C08B26
C08616_QueueVramTransfer_FromDpSource        = $C08616
C08E1C_UpdateBg3ScreenBaseRegistersFromQueue = $C08E1C
C08ED2_QueueOrTransferDynamicTileBlock       = $C08ED2
C08EFC_CommitTileBufferToStaging             = $C08EFC
C08F8B_PrepareTileBufferCommit               = $C08F8B
C08FF7_MultiplyAByYAlt                       = $C08FF7
C09032_MultiplyAByY                          = $C09032
C09231_ShiftRightByYPreserveWidth            = $C09231
C0923E_ShiftRightByY                         = $C0923E
C09251_ShiftRightByYAlt                      = $C09251
C2DB3F_UpdateBattleBgVisualState             = $C2DB3F
C2EA15_BeginBattleBgVisualState              = $C2EA15

; ---------------------------------------------------------------------------
; WRAM / data contracts

COFFEE_TEA_TOKEN_METADATA                    = $C3F054
COFFEE_TEA_TOKEN_METADATA_BANK               = $00C3
COFFEE_TEA_VISUAL_SOURCE                     = $E02188
COFFEE_TEA_TILE_BUFFER                       = $3492
COFFEE_TEA_TILE_BUFFER_WORDS                 = $0340
COFFEE_TEA_TILE_COMMIT_SIZE                  = $0680
COFFEE_TEA_TILE_SOURCE_LOW                   = $7DFE
COFFEE_TEA_STATIC_VISUAL_SOURCE              = $7C00
COFFEE_TEA_VISUAL_TRANSFER_SIZE              = $0800
COFFEE_TEA_TILEMAP_VRAM_BASE                 = $6000
COFFEE_TEA_TILEMAP_VRAM_SIZE                 = $3800
COFFEE_TEA_WINDOW_STEP_BYTES                 = $01A0
COFFEE_TEA_WINDOW_VISIBLE_BYTES              = $04E0
COFFEE_TEA_WINDOW_BOUNDARY                   = $3400
COFFEE_TEA_WINDOW_VRAM_BASE                  = $6150
COFFEE_TEA_WINDOW_VRAM_WRAP_SOURCE           = $6892
COFFEE_TEA_ROW_STRIDE                        = $00D0
COFFEE_TEA_TILE_ID_BASE                      = $2000
COFFEE_TEA_TILE_COLUMNS                      = $0020
COFFEE_TEA_INITIAL_TILE_ID                   = $0010
COFFEE_TEA_TILE_COLUMN_FIRST                 = $0003
COFFEE_TEA_TILE_COLUMN_LIMIT                 = $001D
COFFEE_TEA_COMPACT_TOKEN_BASE                = $99CE
COFFEE_TEA_COMPACT_TOKEN_STRIDE              = $005F
COFFEE_TEA_MAX_TOKEN_STRING_BYTES            = $0005
COFFEE_TEA_TOKEN_DRAW_THRESHOLD_MINUS_ONE    = $004F
COFFEE_TEA_TOKEN_BASE                        = $0050
COFFEE_TEA_TOKEN_INDEX_MASK                  = $007F
COFFEE_TEA_TILE_ROW_ADVANCE                  = $0040
COFFEE_TEA_TILE_ROW_CROSSING_SHIFT           = $08
COFFEE_TEA_SCROLL_WRAP_ROWS                  = $0020
COFFEE_TEA_UPLOAD_SELECTOR_03                = $03
COFFEE_TEA_UPLOAD_SELECTOR_00                = $00
COFFEE_TEA_DISPLAY_SHADOW_30_VALUE           = $18
COFFEE_TEA_DISPLAY_STATE_3C18_VALUE          = $001A

COFFEE_TEA_TILE_WINDOW_INDEX                 = $9F2D
COFFEE_TEA_ROW_PIXEL_CURSOR                  = $9F2F
COFFEE_TEA_ROW_BASE_CURSOR                   = $9F31
COFFEE_TEA_SCROLL_PIXEL_ACCUM                = $3C16
COFFEE_TEA_SCROLL_FRAME_ACCUM                = $3C14
COFFEE_TEA_DISPLAY_STATE_3C18                = $3C18
COFFEE_TEA_DISPLAY_STATE_3C1C                = $3C1C
COFFEE_TEA_DIRTY_MIN                         = $3C1E
COFFEE_TEA_DIRTY_MAX                         = $3C20
BG_SCROLL_SHADOW_3B                          = $003B
DISPLAY_SHADOW_30                            = $0030

; Direct-page locals:
;   $06/$08/$09 and $0E/$10 carry long source/destination pointers for C0
;   transfer helpers. $9F2D/$9F2F/$9F31 hold the tile-window and row cursors.

; ---------------------------------------------------------------------------
; C4:9841

; BeginCoffeeTeaBattleBgVisualState
C49841_BeginCoffeeTeaBattleBgVisualState:
    rep #$31
    lda #$0001
    jsl C2EA15_BeginBattleBgVisualState
    rtl

; ---------------------------------------------------------------------------
; C4:984B

; InvertCoffeeTeaTileBufferWords
C4984B_InvertCoffeeTeaTileBufferWords:
    rep #$31
    phd
    tdc
    adc #$FFF0
    tcd
    lda #COFFEE_TEA_TILE_BUFFER
    sta $0E
    ldy #COFFEE_TEA_TILE_BUFFER_WORDS
    bra C4986E_InvertCoffeeTeaTileBufferWords_Check

C4985D_InvertCoffeeTeaTileBufferWords_Loop:
    tax
    lda.w $0000,x
    eor #$FFFF
    sta.w $0000,x
    dey
    lda $0E
    inc
    inc
    sta $0E
C4986E_InvertCoffeeTeaTileBufferWords_Check:
    cpy #$0000
    bne C4985D_InvertCoffeeTeaTileBufferWords_Loop
    pld
    rts

; ---------------------------------------------------------------------------
; C4:9875

; ApplyCoffeeTeaTileRowMask
C49875_ApplyCoffeeTeaTileRowMask:
    rep #$31
    phd
    pha
    tdc
    adc #$FFE6
    tcd
    pla
    sty $18
    sta $16
    lda $28
    sta $0A
    lda $2A
    sta $0C
    ldy #$0008
    lda.w COFFEE_TEA_ROW_PIXEL_CURSOR
    jsl C09231_ShiftRightByYPreserveWidth
    sta $14
    lda.w COFFEE_TEA_ROW_BASE_CURSOR
    clc
    adc $18
    sta $02
    lda $0A
    sta $06
    lda $0C
    sta $08
    lda $02
    sta $12
    lda #$0000
    sta $04
    bra C498F9_ApplyCoffeeTeaTileRowMask_FirstPassCheck

C498B2_ApplyCoffeeTeaTileRowMask_FirstPassRow:
    ldy #$0000
    sty $10
    bra C498EA_ApplyCoffeeTeaTileRowMask_FirstPassByteCheck

C498B9_ApplyCoffeeTeaTileRowMask_FirstPassByte:
    sep #$20
    lda [$06]
    eor.b #$FF
    ldy $14
    sep #$10
    jsl C09251_ShiftRightByYAlt
    eor.b #$FF
    rep #$10
    ldx $02
    inx
    sta $00
    lda.w $0000,x
    and $00
    sta.w $0000,x
    ldx $02
    sta.w $0000,x
    rep #$20
    inc $02
    inc $02
    ldy $10
    iny
    sty $10
    inc $06
C498EA_ApplyCoffeeTeaTileRowMask_FirstPassByteCheck:
    cpy #$0008
    bcc C498B9_ApplyCoffeeTeaTileRowMask_FirstPassByte
    lda $12
    clc
    adc #COFFEE_TEA_WINDOW_STEP_BYTES
    sta $02
    inc $04
C498F9_ApplyCoffeeTeaTileRowMask_FirstPassCheck:
    lda #$0002
    clc
    sbc $04
    bvs C49905_ApplyCoffeeTeaTileRowMask_FirstPassOverflow
    bpl C498B2_ApplyCoffeeTeaTileRowMask_FirstPassRow
    bra C49907_ApplyCoffeeTeaTileRowMask_NextCursor

C49905_ApplyCoffeeTeaTileRowMask_FirstPassOverflow:
    bmi C498B2_ApplyCoffeeTeaTileRowMask_FirstPassRow
C49907_ApplyCoffeeTeaTileRowMask_NextCursor:
    lda.w COFFEE_TEA_ROW_PIXEL_CURSOR
    clc
    adc $16
    sta.w COFFEE_TEA_ROW_PIXEL_CURSOR
    lsr
    lsr
    lsr
    cmp.w COFFEE_TEA_ROW_BASE_CURSOR
    bne C4991B_ApplyCoffeeTeaTileRowMask_CrossedRow
    jmp C49999_ApplyCoffeeTeaTileRowMask_Return

C4991B_ApplyCoffeeTeaTileRowMask_CrossedRow:
    asl
    asl
    asl
    asl
    sta $16
    sta.w COFFEE_TEA_ROW_BASE_CURSOR
    lda #$0008
    sec
    sbc $14
    sta $12
    lda $16
    clc
    adc $18
    ldx $0A
    stx $06
    ldx $0C
    stx $08
    sta $14
    sta $02
    lda #$0000
    sta $04
    bra C4998B_ApplyCoffeeTeaTileRowMask_SecondPassCheck

C49944_ApplyCoffeeTeaTileRowMask_SecondPassRow:
    ldy #$0000
    sty $0E
    bra C4997C_ApplyCoffeeTeaTileRowMask_SecondPassByteCheck

C4994B_ApplyCoffeeTeaTileRowMask_SecondPassByte:
    sep #$20
    lda [$06]
    eor.b #$FF
    ldy $12
    sep #$10
    jsl C0923E_ShiftRightByY
    eor.b #$FF
    rep #$10
    ldx $02
    inx
    sta $00
    lda.w $0000,x
    and $00
    sta.w $0000,x
    ldx $02
    sta.w $0000,x
    rep #$20
    inc $02
    inc $02
    ldy $0E
    iny
    sty $0E
    inc $06
C4997C_ApplyCoffeeTeaTileRowMask_SecondPassByteCheck:
    cpy #$0008
    bcc C4994B_ApplyCoffeeTeaTileRowMask_SecondPassByte
    lda $14
    clc
    adc #COFFEE_TEA_WINDOW_STEP_BYTES
    sta $02
    inc $04
C4998B_ApplyCoffeeTeaTileRowMask_SecondPassCheck:
    lda #$0002
    clc
    sbc $04
    bvs C49997_ApplyCoffeeTeaTileRowMask_SecondPassOverflow
    bpl C49944_ApplyCoffeeTeaTileRowMask_SecondPassRow
    bra C49999_ApplyCoffeeTeaTileRowMask_Return

C49997_ApplyCoffeeTeaTileRowMask_SecondPassOverflow:
    bmi C49944_ApplyCoffeeTeaTileRowMask_SecondPassRow
C49999_ApplyCoffeeTeaTileRowMask_Return:
    pld
    rtl

; ---------------------------------------------------------------------------
; C4:999B

; DrawCoffeeTeaTileTokenRun
C4999B_DrawCoffeeTeaTileTokenRun:
    rep #$31
    phd
    pha
    tdc
    adc #$FFEC
    tcd
    pla
    sec
    sbc #COFFEE_TEA_TOKEN_BASE
    and #COFFEE_TEA_TOKEN_INDEX_MASK
    sta $12
    lda #COFFEE_TEA_TOKEN_METADATA
    sta $0A
    lda #COFFEE_TEA_TOKEN_METADATA_BANK
    sta $0C
    ldy #$0038
    lda [$0A],y
    tax
    ldy #$0034
    lda [$0A],y
    pha
    iny
    iny
    lda [$0A],y
    sta $08
    pla
    sta $06
    lda $12
    tay
    txa
    jsl C09032_MultiplyAByY
    clc
    adc $06
    sta $06
    ldy #$003A
    lda [$0A],y
    sta $04
    ldy #$0030
    lda [$0A],y
    pha
    iny
    iny
    lda [$0A],y
    sta $0C
    pla
    sta $0A
    lda $12
    clc
    adc $0A
    sta $0A
    lda [$0A]
    and #$00FF
    tax
    stx $02
    inc $02
    lda $02
    cmp #$0008
    bcc C49A36_DrawCoffeeTeaTileTokenRun_FinalChunk
    beq C49A36_DrawCoffeeTeaTileTokenRun_FinalChunk
C49A0A_DrawCoffeeTeaTileTokenRun_FullChunk:
    lda $06
    sta $0E
    lda $08
    sta $10
    ldy #COFFEE_TEA_TILE_BUFFER
    ldx $04
    lda #$0008
    jsl C49875_ApplyCoffeeTeaTileRowMask
    lda $02
    sec
    sbc #$0008
    sta $02
    lda $04
    clc
    adc $06
    sta $06
    lda $02
    cmp #$0008
    beq C49A36_DrawCoffeeTeaTileTokenRun_FinalChunk
    bcs C49A0A_DrawCoffeeTeaTileTokenRun_FullChunk
C49A36_DrawCoffeeTeaTileTokenRun_FinalChunk:
    lda $06
    sta $0E
    lda $08
    sta $10
    ldy #COFFEE_TEA_TILE_BUFFER
    ldx $04
    lda $02
    jsl C49875_ApplyCoffeeTeaTileRowMask
    pld
    rtl

; ---------------------------------------------------------------------------
; C4:9A4B

; WaitFrameAndUpdateBattleBgVisualState
C49A4B_WaitFrameAndUpdateBattleBgVisualState:
    rep #$31
    jsl C08756_WaitOneFrameAndPollInput
    jsl C2DB3F_UpdateBattleBgVisualState
    rts

; ---------------------------------------------------------------------------
; C4:9A56

; InitCoffeeTeaTileBufferAndTransferState
C49A56_InitCoffeeTeaTileBufferAndTransferState:
    rep #$31
    phd
    tdc
    adc #$FFEA
    tcd
    lda #$0000
    sta $06
    lda #$007F
    sta $08
    jsl C08726_BlankWaitAndDisableHdma
    ldy #COFFEE_TEA_TILEMAP_VRAM_BASE
    ldx #COFFEE_TEA_STATIC_VISUAL_SOURCE
    lda #$0000
    jsl C08E1C_UpdateBg3ScreenBaseRegistersFromQueue
    lda #$0000
    sta [$06]
    lda $06
    sta $0E
    lda $08
    sta $10
    ldy #COFFEE_TEA_TILEMAP_VRAM_BASE
    ldx #COFFEE_TEA_TILEMAP_VRAM_SIZE
    sep #$20
    lda.b #COFFEE_TEA_UPLOAD_SELECTOR_03
    jsl C08616_QueueVramTransfer_FromDpSource
    lda.w #COFFEE_TEA_VISUAL_SOURCE
    sta $0E
    lda.w #COFFEE_TEA_VISUAL_SOURCE>>16
    sta $10
    ldx #$0008
    lda.w #$0200
    jsl C08ED2_QueueOrTransferDynamicTileBlock
    sep #$20
    lda.b #COFFEE_TEA_DISPLAY_SHADOW_30_VALUE
    sta.w DISPLAY_SHADOW_30
    lda.b #$FF
    sta $0E
    ldx #COFFEE_TEA_TILE_COMMIT_SIZE
    rep #$20
    lda #COFFEE_TEA_TILE_BUFFER
    jsl C08EFC_CommitTileBufferToStaging
    ldy #COFFEE_TEA_INITIAL_TILE_ID
    ldx #$0000
    stx $14
    bra C49B20_InitCoffeeTeaTileBufferAndTransferState_ColumnCheck

C49AC9_InitCoffeeTeaTileBufferAndTransferState_Column:
    txa
    asl
    asl
    asl
    asl
    asl
    asl
    tax
    stz.w COFFEE_TEA_TILE_SOURCE_LOW,x
    tax
    stz.w COFFEE_TEA_TILE_SOURCE_LOW+$0002,x
    tax
    stz.w COFFEE_TEA_TILE_SOURCE_LOW+$0004,x
    lda #COFFEE_TEA_TILE_COLUMN_FIRST
    sta $12
    bra C49B01_InitCoffeeTeaTileBufferAndTransferState_RowCheck

C49AE3_InitCoffeeTeaTileBufferAndTransferState_Row:
    asl
    sta $02
    ldx $14
    txa
    asl
    asl
    asl
    asl
    asl
    asl
    clc
    adc $02
    tax
    tya
    clc
    adc #COFFEE_TEA_TILE_ID_BASE
    sta.w COFFEE_TEA_TILE_SOURCE_LOW,x
    iny
    lda $12
    inc
    sta $12
C49B01_InitCoffeeTeaTileBufferAndTransferState_RowCheck:
    cmp #COFFEE_TEA_TILE_COLUMN_LIMIT
    bcc C49AE3_InitCoffeeTeaTileBufferAndTransferState_Row
    ldx $14
    txa
    asl
    asl
    asl
    asl
    asl
    asl
    tax
    stz.w COFFEE_TEA_TILE_SOURCE_LOW+$003A,x
    tax
    stz.w COFFEE_TEA_TILE_SOURCE_LOW+$003C,x
    tax
    stz.w COFFEE_TEA_TILE_SOURCE_LOW+$003E,x
    ldx $14
    inx
    stx $14
C49B20_InitCoffeeTeaTileBufferAndTransferState_ColumnCheck:
    cpx #COFFEE_TEA_TILE_COLUMNS
    bcc C49AC9_InitCoffeeTeaTileBufferAndTransferState_Column
    lda #COFFEE_TEA_TILE_SOURCE_LOW
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
    ldy #COFFEE_TEA_STATIC_VISUAL_SOURCE
    ldx #COFFEE_TEA_VISUAL_TRANSFER_SIZE
    sep #$20
    lda.b #COFFEE_TEA_UPLOAD_SELECTOR_00
    jsl C08616_QueueVramTransfer_FromDpSource
    lda.w #COFFEE_TEA_DISPLAY_STATE_3C18_VALUE
    sta.w COFFEE_TEA_DISPLAY_STATE_3C18
    stz.w COFFEE_TEA_DISPLAY_STATE_3C1C
    lda.w #$FFFF
    sta.w COFFEE_TEA_DIRTY_MIN
    stz.w COFFEE_TEA_DIRTY_MAX
    stz.w COFFEE_TEA_SCROLL_FRAME_ACCUM
    stz.w COFFEE_TEA_SCROLL_PIXEL_ACCUM
    stz.w COFFEE_TEA_ROW_PIXEL_CURSOR
    stz.w COFFEE_TEA_ROW_BASE_CURSOR
    jsl C08744_CloseDisplayTransitionBracket
    pld
    rtl

; ---------------------------------------------------------------------------
; C4:9B6E

; UploadCoffeeTeaTileBufferWindow
C49B6E_UploadCoffeeTeaTileBufferWindow:
    rep #$31
    phd
    pha
    tdc
    adc #$FFEA
    tcd
    pla
    jsr C4984B_InvertCoffeeTeaTileBufferWords
    ldy #COFFEE_TEA_WINDOW_STEP_BYTES
    lda.w COFFEE_TEA_TILE_WINDOW_INDEX
    jsl C09032_MultiplyAByY
    sta $14
    clc
    adc #COFFEE_TEA_WINDOW_VISIBLE_BYTES
    cmp #COFFEE_TEA_WINDOW_BOUNDARY
    beq C49B92_UploadCoffeeTeaTileBufferWindow_NoWrap
    bcs C49B95_UploadCoffeeTeaTileBufferWindow_SplitAtBoundary
C49B92_UploadCoffeeTeaTileBufferWindow_NoWrap:
    jmp C49C16_UploadCoffeeTeaTileBufferWindow_Contiguous

C49B95_UploadCoffeeTeaTileBufferWindow_SplitAtBoundary:
    lda $14
    sta $02
    lda #COFFEE_TEA_WINDOW_BOUNDARY
    sec
    sbc $02
    sta $12
    beq C49BD4_UploadCoffeeTeaTileBufferWindow_SecondSegment
    lda #COFFEE_TEA_TILE_BUFFER
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
    lda.w COFFEE_TEA_TILE_WINDOW_INDEX
    ldy #COFFEE_TEA_ROW_STRIDE
    jsl C08FF7_MultiplyAByYAlt
    clc
    adc #COFFEE_TEA_WINDOW_VRAM_BASE
    tay
    lda $12
    tax
    sep #$20
    lda.b #COFFEE_TEA_UPLOAD_SELECTOR_00
    jsl C08616_QueueVramTransfer_FromDpSource
C49BD4_UploadCoffeeTeaTileBufferWindow_SecondSegment:
    ldy #COFFEE_TEA_WINDOW_STEP_BYTES
    lda.w COFFEE_TEA_TILE_WINDOW_INDEX
    jsl C09032_MultiplyAByY
    sta $14
    clc
    adc #COFFEE_TEA_WINDOW_VISIBLE_BYTES
    sec
    sbc #COFFEE_TEA_WINDOW_BOUNDARY
    tax
    beq C49C47_UploadCoffeeTeaTileBufferWindow_Done
    lda $14
    sta $02
    lda #COFFEE_TEA_WINDOW_VRAM_WRAP_SOURCE
    sec
    sbc $02
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
    ldy #COFFEE_TEA_WINDOW_VRAM_BASE
    sep #$20
    lda.b #COFFEE_TEA_UPLOAD_SELECTOR_00
    jsl C08616_QueueVramTransfer_FromDpSource
    bra C49C47_UploadCoffeeTeaTileBufferWindow_Done

C49C16_UploadCoffeeTeaTileBufferWindow_Contiguous:
    lda #COFFEE_TEA_TILE_BUFFER
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
    lda.w COFFEE_TEA_TILE_WINDOW_INDEX
    ldy #COFFEE_TEA_ROW_STRIDE
    jsl C08FF7_MultiplyAByYAlt
    clc
    adc #COFFEE_TEA_WINDOW_VRAM_BASE
    tay
    ldx #COFFEE_TEA_WINDOW_VISIBLE_BYTES
    sep #$20
    lda.b #COFFEE_TEA_UPLOAD_SELECTOR_00
    jsl C08616_QueueVramTransfer_FromDpSource
C49C47_UploadCoffeeTeaTileBufferWindow_Done:
    lda.w #$FFFF
    sta.w COFFEE_TEA_DIRTY_MIN
    stz.w COFFEE_TEA_DIRTY_MAX
    jsl C08756_WaitOneFrameAndPollInput
    pld
    rtl

; ---------------------------------------------------------------------------
; C4:9C56

; AdvanceCoffeeTeaTileScrollState
C49C56_AdvanceCoffeeTeaTileScrollState:
    rep #$31
    phd
    pha
    tdc
    adc #$FFF1
    tcd
    pla
    clc
    adc.w COFFEE_TEA_SCROLL_PIXEL_ACCUM
    sta.w COFFEE_TEA_SCROLL_PIXEL_ACCUM
    stz.w COFFEE_TEA_SCROLL_FRAME_ACCUM
    lsr
    lsr
    lsr
    inc
    clc
    adc.w COFFEE_TEA_TILE_WINDOW_INDEX
    sta.w COFFEE_TEA_TILE_WINDOW_INDEX
    cmp #COFFEE_TEA_SCROLL_WRAP_ROWS
    bcc C49C81_AdvanceCoffeeTeaTileScrollState_InRange
    sec
    sbc #COFFEE_TEA_SCROLL_WRAP_ROWS
    sta.w COFFEE_TEA_TILE_WINDOW_INDEX
C49C81_AdvanceCoffeeTeaTileScrollState_InRange:
    jsl C08F8B_PrepareTileBufferCommit
    sep #$20
    lda.b #$FF
    sta $0E
    ldx #COFFEE_TEA_TILE_COMMIT_SIZE
    rep #$20
    lda #COFFEE_TEA_TILE_BUFFER
    jsl C08EFC_CommitTileBufferToStaging
    lda.w COFFEE_TEA_SCROLL_PIXEL_ACCUM
    and #$0007
    sta.w COFFEE_TEA_SCROLL_PIXEL_ACCUM
    stz.w COFFEE_TEA_ROW_PIXEL_CURSOR
    stz.w COFFEE_TEA_ROW_BASE_CURSOR
    pld
    rtl

; ---------------------------------------------------------------------------
; C4:9CA8

; AdvanceCoffeeTeaRowRevealCursor
C49CA8_AdvanceCoffeeTeaRowRevealCursor:
    rep #$31
    and #$00FF
    clc
    adc #$0008
    clc
    adc.w COFFEE_TEA_ROW_PIXEL_CURSOR
    sta.w COFFEE_TEA_ROW_PIXEL_CURSOR
    lsr
    lsr
    lsr
    asl
    asl
    asl
    asl
    sta.w COFFEE_TEA_ROW_BASE_CURSOR
    rtl

; ---------------------------------------------------------------------------
; C4:9CC3

; RenderCoffeeTeaTokenString
C49CC3_RenderCoffeeTeaTokenString:
    rep #$31
    phd
    pha
    tdc
    adc #$FFEE
    tcd
    pla
    tax
    dec
    ldy #COFFEE_TEA_COMPACT_TOKEN_STRIDE
    jsl C08FF7_MultiplyAByYAlt
    clc
    adc #COFFEE_TEA_COMPACT_TOKEN_BASE
    sta $06
    phb
    sep #$20
    pla
    sta $08
    stz $09
    ldx #$0000
    stx $10
    bra C49CF8_RenderCoffeeTeaTokenString_Check

C49CEB_RenderCoffeeTeaTokenString_DrawToken:
    inc $06
    lda $0E
    jsl C4999B_DrawCoffeeTeaTileTokenRun
    ldx $10
    inx
    stx $10
C49CF8_RenderCoffeeTeaTokenString_Check:
    cpx #COFFEE_TEA_MAX_TOKEN_STRING_BYTES
    bcs C49D12_RenderCoffeeTeaTokenString_Return
    rep #$20
    lda [$06]
    and #$00FF
    sta $0E
    clc
    sbc #COFFEE_TEA_TOKEN_DRAW_THRESHOLD_MINUS_ONE
    bvs C49D10_RenderCoffeeTeaTokenString_ThresholdOverflow
    bpl C49CEB_RenderCoffeeTeaTokenString_DrawToken
    bra C49D12_RenderCoffeeTeaTokenString_Return

C49D10_RenderCoffeeTeaTokenString_ThresholdOverflow:
    bmi C49CEB_RenderCoffeeTeaTokenString_DrawToken
C49D12_RenderCoffeeTeaTokenString_Return:
    rep #$20
    pld
    rtl

; ---------------------------------------------------------------------------
; C4:9D16

; RenderSingleCoffeeTeaTileToken
C49D16_RenderSingleCoffeeTeaTileToken:
    rep #$31
    tax
    jsl C4999B_DrawCoffeeTeaTileTokenRun
    rtl

; ---------------------------------------------------------------------------
; C4:9D1E

; AdvanceCoffeeTeaVramOffsetByTileRow
C49D1E_AdvanceCoffeeTeaVramOffsetByTileRow:
    rep #$31
    phd
    pha
    tdc
    adc #$FFEE
    tcd
    pla
    sta $10
    jsl C088B1_WaitOneFrameAndUpdateDisplayState
    lda $10
    and #$FF00
    sta $02
    lda $10
    clc
    adc #COFFEE_TEA_TILE_ROW_ADVANCE
    tax
    stx $0E
    txa
    and #$FF00
    sta $10
    cmp $02
    beq C49D65_AdvanceCoffeeTeaVramOffsetByTileRow_Return
    sep #$20
    lda.b #COFFEE_TEA_TILE_ROW_CROSSING_SHIFT
    sep #$10
    tay
    rep #$20
    lda $10
    sec
    sbc $02
    jsl C09251_ShiftRightByYAlt
    clc
    adc.w BG_SCROLL_SHADOW_3B
    sta.w BG_SCROLL_SHADOW_3B
    jsl C08B26_ApplyBgScrollOrTilemapUpdate
C49D65_AdvanceCoffeeTeaVramOffsetByTileRow_Return:
    ldx $0E
    txa
    pld
    rtl
