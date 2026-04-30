; EarthBound C4 visual frame copy and HDMA helper prototype.
;
; Source-emission status:
; - Prototype level: build-candidate
; - C4 source-bank scaffold pilot slice with one explicit source-adjacent data block.
; - Derived from notes/c4-visual-frame-copy-and-footprint-tables-283f-2b0d.md.
; - ROM byte range, SHA-1, and source signature are tracked by
;   build/c4-build-candidate-ranges.json.
;
; Source units covered:
; - C4:283F..C4:2955 frame copy / masked row merge helpers
; - C4:2965..C4:2A1F masked pair merge / render strip / HDMA helpers
;
; Data block emitted by the scaffold:
; - C4:2955..C4:2965 TileColumnWordPairMaskTable

; ---------------------------------------------------------------------------
; External contracts used by this module

C0A623_VisualProfileSecondaryOffsetTable = $C0A623
C0A60B_VisualProfileDirectionOffsetTable = $C0A60B
C0A56E_GenerateRenderDmaStripDescriptor  = $C0A56E
C0AE16_HdmaChannelEnableBitTable         = $C0AE16

; ---------------------------------------------------------------------------
; ROM/WRAM contracts

VISUAL_FRAME_LIST_POINTER_TABLE       = $29CA
VISUAL_FRAME_DATA_BANK_TABLE          = $2A42
VISUAL_FRAME_RECORD_STRIDE_TABLE      = $2A7E
VISUAL_FRAME_PIECE_COUNT_TABLE        = $2ABA
VISUAL_FRAME_DIRECTION_SELECTOR_TABLE = $2AF6
VISUAL_FRAME_SOURCE_BANK_TABLE        = $2A06
VISUAL_FRAME_RUNTIME_OFFSET_TABLE     = $10F2

TILE_COLUMN_WORD_PAIR_MASK_TABLE      = $C42955
RENDER_STRIP_TARGET_TABLE             = $298E

LONG_POINTER_LOW                      = $00
LONG_POINTER_BANK                     = $02
LONG_POINTER_2_LOW                    = $04
LONG_POINTER_2_BANK                   = $06
MASK_WORD                             = $08
MASK_COMPLEMENT                       = $0A
MASKED_SOURCE_WORD                    = $0C
ROW_COUNT                             = $0E

MERGE_MASK_INDEX                      = $1C
MERGE_HEIGHT_PIXELS                   = $1E
MERGE_DEST_ROW_STRIDE                 = $20
COPY_COUNT                            = $16

WRAM_BANK_7F                          = $007F
FRAME_POINTER_LOW_MASK                = $FFF0
TILE_ROW_WORDS                        = $0010
TILE_COLUMN_PAIR_OFFSET               = $0010

DMA_SOURCE_BANK_7E                    = $7E
DMA_MAIN_SCREEN_SOURCE_LOW            = $ADB8
DMA_MAIN_SCREEN_TARGET_REGISTER       = $2C
DMA_MODE_INDIRECT_2REG                = $01
HDMA_ENABLE_SHADOW                    = $001F

DMA_CHANNEL_DMAP                      = $004300
DMA_CHANNEL_BBAD                      = $004301
DMA_CHANNEL_A1T                       = $004302
DMA_CHANNEL_A1B                       = $004304
DMA_CHANNEL_DASB                      = $004307

DMA_SOURCE_OFFSET_HIGH                = $0091
DMA_TRANSFER_SIZE_OR_STRIDE           = $0092
DMA_SOURCE_OFFSET_LOW                 = $0094
DMA_SOURCE_BANK                       = $0096
DMA_TARGET_LOW                        = $0097

; Direct-page locals:
;   $00/$02 and $04/$06 = long source/destination pointers.
;   $08/$0A/$0C/$0E = mask, complement, temp word, row count.

; ---------------------------------------------------------------------------
; C4:283F

; CopySecondaryVisualProfileFrameWords
C4283F_CopySecondaryVisualProfileFrameWords:
    rep #$20
    phd
    pha
    tdc
    sec
    sbc #$0008
    tcd
    pla
    phy
    stx LONG_POINTER_2_LOW
    asl
    tay
    lda #WRAM_BANK_7F
    sta LONG_POINTER_2_BANK
    lda VISUAL_FRAME_SOURCE_BANK_TABLE,Y
    sta LONG_POINTER_BANK
    lda VISUAL_FRAME_DIRECTION_SELECTOR_TABLE,Y
    asl
    tax
    lda.l C0A623_VisualProfileSecondaryOffsetTable,X
    asl
    asl
    clc
    adc VISUAL_FRAME_LIST_POINTER_TABLE,Y
    adc VISUAL_FRAME_RUNTIME_OFFSET_TABLE,Y
    sta LONG_POINTER_LOW
    lda [LONG_POINTER_LOW]
    and #FRAME_POINTER_LOW_MASK
    sta LONG_POINTER_LOW
    lda VISUAL_FRAME_DATA_BANK_TABLE,Y
    sta LONG_POINTER_BANK
    ply
C4287A_CopySecondaryVisualProfileFrameWords_Loop:
    lda [LONG_POINTER_LOW],Y
    sta [LONG_POINTER_2_LOW],Y
    dey
    dey
    bpl C4287A_CopySecondaryVisualProfileFrameWords_Loop
    pld
    rtl

; ---------------------------------------------------------------------------
; C4:2884

; CopyDirectionalVisualProfileFrameWords
C42884_CopyDirectionalVisualProfileFrameWords:
    rep #$20
    phd
    pha
    tdc
    sec
    sbc #$0008
    tcd
    pla
    phy
    stx LONG_POINTER_2_LOW
    asl
    tay
    lda #WRAM_BANK_7F
    sta LONG_POINTER_2_BANK
    lda VISUAL_FRAME_SOURCE_BANK_TABLE,Y
    sta LONG_POINTER_BANK
    lda VISUAL_FRAME_LIST_POINTER_TABLE,Y
    sta LONG_POINTER_LOW
    lda VISUAL_FRAME_DIRECTION_SELECTOR_TABLE,Y
    asl
    tax
    lda.l C0A60B_VisualProfileDirectionOffsetTable,X
    beq C428BA_CopyDirectionalVisualProfileFrameWords_UsePointer
    tax
    lda LONG_POINTER_LOW
    clc
C428B2_CopyDirectionalVisualProfileFrameWords_AdvancePointer:
    adc #$0004
    dex
    bne C428B2_CopyDirectionalVisualProfileFrameWords_AdvancePointer
    sta LONG_POINTER_LOW
C428BA_CopyDirectionalVisualProfileFrameWords_UsePointer:
    lda [LONG_POINTER_LOW]
    and #FRAME_POINTER_LOW_MASK
    sta LONG_POINTER_LOW
    lda VISUAL_FRAME_DATA_BANK_TABLE,Y
    sta LONG_POINTER_BANK
    ply
C428C7_CopyDirectionalVisualProfileFrameWords_Loop:
    lda [LONG_POINTER_LOW],Y
    sta [LONG_POINTER_2_LOW],Y
    dey
    dey
    bpl C428C7_CopyDirectionalVisualProfileFrameWords_Loop
    pld
    rtl

; ---------------------------------------------------------------------------
; C4:28D1

; Copy7fWordsEvery16ByCount
C428D1_Copy7fWordsEvery16ByCount:
    rep #$30
    rep #$20
    phd
    pha
    tdc
    sec
    sbc #$0008
    tcd
    pla
    sta LONG_POINTER_LOW
    stx LONG_POINTER_2_LOW
    lda #WRAM_BANK_7F
    sta LONG_POINTER_BANK
    sta LONG_POINTER_2_BANK
    lda COPY_COUNT
    asl
    tax
C428ED_Copy7fWordsEvery16ByCount_Loop:
    lda [LONG_POINTER_2_LOW],Y
    sta [LONG_POINTER_LOW],Y
    tya
    clc
    adc #TILE_COLUMN_PAIR_OFFSET
    tay
    dex
    bne C428ED_Copy7fWordsEvery16ByCount_Loop
    pld
    rtl

; ---------------------------------------------------------------------------
; C4:28FC

; MergeMasked7fTileColumnRows
C428FC_MergeMasked7fTileColumnRows:
    rep #$30
    rep #$20
    phd
    pha
    tdc
    sec
    sbc #$0010
    tcd
    pla
    sta LONG_POINTER_LOW
    stx LONG_POINTER_2_LOW
    lda #WRAM_BANK_7F
    sta LONG_POINTER_BANK
    sta LONG_POINTER_2_BANK
    tya
    and #$0007
    asl
    tax
    lda.l TILE_COLUMN_WORD_PAIR_MASK_TABLE,X
    sta MASK_WORD
    eor #$FFFF
    sta MASK_COMPLEMENT
    tya
    and #$FFF8
    asl
    asl
    tay
    lda MERGE_HEIGHT_PIXELS
    lsr
    lsr
    lsr
    sta ROW_COUNT
C42933_MergeMasked7fTileColumnRows_RowLoop:
    ldx #TILE_ROW_WORDS
    phy
C42937_MergeMasked7fTileColumnRows_WordLoop:
    lda [LONG_POINTER_2_LOW],Y
    and MASK_WORD
    sta MASKED_SOURCE_WORD
    lda [LONG_POINTER_LOW],Y
    and MASK_COMPLEMENT
    ora MASKED_SOURCE_WORD
    sta [LONG_POINTER_LOW],Y
    iny
    iny
    dex
    bne C42937_MergeMasked7fTileColumnRows_WordLoop
    pla
    clc
    adc MERGE_DEST_ROW_STRIDE
    tay
    dec ROW_COUNT
    bne C42933_MergeMasked7fTileColumnRows_RowLoop
    pld
    rtl

; ---------------------------------------------------------------------------
; C4:2965

; MergeMasked7fTileColumnPair

; ---------------------------------------------------------------------------
; C4:2955

C42955_TileColumnWordPairMaskTable:
    ; data bytes: C4:2955..C4:2965
    db $80,$80,$40,$40,$20,$20,$10,$10,$08,$08,$04,$04,$02,$02,$01,$01

C42965_MergeMasked7fTileColumnPair:
    rep #$20
    phd
    pha
    tdc
    sec
    sbc #$000E
    tcd
    pla
    sta LONG_POINTER_LOW
    stx LONG_POINTER_2_LOW
    lda #WRAM_BANK_7F
    sta LONG_POINTER_BANK
    sta LONG_POINTER_2_BANK
    lda MERGE_MASK_INDEX
    asl
    tax
    lda.l TILE_COLUMN_WORD_PAIR_MASK_TABLE,X
    sta MASK_WORD
    eor #$FFFF
    sta MASK_COMPLEMENT
    lda [LONG_POINTER_2_LOW],Y
    and MASK_WORD
    sta MASKED_SOURCE_WORD
    lda [LONG_POINTER_LOW],Y
    and MASK_COMPLEMENT
    ora MASKED_SOURCE_WORD
    sta [LONG_POINTER_LOW],Y
    tya
    clc
    adc #TILE_COLUMN_PAIR_OFFSET
    tay
    lda [LONG_POINTER_2_LOW],Y
    and MASK_WORD
    sta MASKED_SOURCE_WORD
    lda [LONG_POINTER_LOW],Y
    and MASK_COMPLEMENT
    ora MASKED_SOURCE_WORD
    sta [LONG_POINTER_LOW],Y
    pld
    rtl

; ---------------------------------------------------------------------------
; C4:29AE

; GenerateVisualProfileRenderDmaStrips
C429AE_GenerateVisualProfileRenderDmaStrips:
    pha
    txa
    asl
    tax
    lda VISUAL_FRAME_PIECE_COUNT_TABLE,X
    sta LONG_POINTER_LOW
    lda #$0000
    sta DMA_SOURCE_OFFSET_HIGH
    lda VISUAL_FRAME_RECORD_STRIDE_TABLE,X
    sta DMA_TRANSFER_SIZE_OR_STRIDE
    lda #WRAM_BANK_7F
    sta DMA_SOURCE_BANK
    pla
    sta DMA_SOURCE_OFFSET_LOW
    lda RENDER_STRIP_TARGET_TABLE,X
    sta DMA_TARGET_LOW
C429D3_GenerateVisualProfileRenderDmaStrips_Loop:
    jsl C0A56E_GenerateRenderDmaStripDescriptor
    dec LONG_POINTER_LOW
    beq C429E7_GenerateVisualProfileRenderDmaStrips_Return
    lda DMA_SOURCE_OFFSET_LOW
    clc
    adc DMA_TRANSFER_SIZE_OR_STRIDE
    sta DMA_SOURCE_OFFSET_LOW
    bra C429D3_GenerateVisualProfileRenderDmaStrips_Loop
C429E7_GenerateVisualProfileRenderDmaStrips_Return:
    rtl

; ---------------------------------------------------------------------------
; C4:29E8

; StartMainScreenLayerHdmaFromAdb8
C429E8_StartMainScreenLayerHdmaFromAdb8:
    tay
    asl
    asl
    asl
    asl
    tax
    sep #$20
    lda.b #DMA_SOURCE_BANK_7E
    sta.l DMA_CHANNEL_A1B,X
    sta.l DMA_CHANNEL_DASB,X
    lda.b #DMA_MAIN_SCREEN_TARGET_REGISTER
    sta.l DMA_CHANNEL_BBAD,X
    lda.b #DMA_MODE_INDIRECT_2REG
    sta.l DMA_CHANNEL_DMAP,X
    rep #$20
    lda #DMA_MAIN_SCREEN_SOURCE_LOW
    sta.l DMA_CHANNEL_A1T,X
    sep #$20
    tyx
    lda HDMA_ENABLE_SHADOW
    ora.l C0AE16_HdmaChannelEnableBitTable,X
    sta HDMA_ENABLE_SHADOW
    rep #$20
    rtl
