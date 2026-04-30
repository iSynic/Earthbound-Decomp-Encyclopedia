; EarthBound C3 window and battle text helper prototype.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Assembler contract: pilot-ready
; - Assembler-ready pilot; not yet linked into a full assembler ROM build.
; - Derived from notes/c3-source-emission-plan.md and the source contracts linked
;   below.
; - Build-candidate conventions are documented in
;   notes/c3-build-candidate-source-conventions.md.
; - Original instruction flow is preserved with stable public/internal labels,
;   local symbolic state names, and width-sensitive control-flow paths covered
;   by source signature validation.
; - ROM byte range, SHA-1, width-sensitive labels, and source signature are
;   tracked by build/c3-build-candidate-ranges.json and
;   build/c3-source-signature-validation.json.
;
; Source units covered:
; - C3:E450..C3:E4EF WindowTickTransferDynamicTileBlock
; - C3:E4EF..C3:E6F8 FindFirstFreeWindowSlot
; - C3:E6F8..C3:E75D ClearFocusedPartyHpPpActorAndBlankRow
; - C3:E75D..C3:E7E3 ResolveReflectedHitSideArticleTokens
; - C3:E7E3..C3:E84E ClearWindowRegisteredCopyChain
;
; Evidence:
; - notes/c3-window-text-source-helper-corridor-e450-e7e3.md
; - notes/c3-window-lifecycle-source-contract-e4ef-e6f7.md
; - notes/c3-focused-party-hppp-actor-clear-e6f8.md
; - notes/class2-reflected-hit-side-token-consumers.md
; - notes/c3-window-and-battle-visual-unknown-tail-e7e3-f981.md

; ---------------------------------------------------------------------------
; External contracts used by this module

C08756_WaitOneFrame                         = $C08756
C08ED2_QueueOrTransferDynamicTileBlock      = $C08ED2
C08FF7_Multiply16                           = $C08FF7
C09032_MultiplyOrDimensionHelper            = $C09032
C12DD5_TickWindowTextSystem                 = $C12DD5
C447FB_DispatchTextControlFragment          = $C447FB
C44AF7_ReleaseTileOrGlyphResource           = $C44AF7
C45E96_RefreshOrReleaseWindowPresentationMapping = $C45E96

; C0:8756 WaitOneFrame
; C0:8ED2 QueueOrTransferDynamicTileBlock
; C0:8FF7 Multiply16
; C0:9032 MultiplyOrDimensionHelper
; C1:2DD5 TickWindowTextSystem
; C4:47FB DispatchTextControlFragment
; C4:4AF7 ReleaseTileOrGlyphResource
; C4:5E96 RefreshOrReleaseWindowPresentationMapping

; ---------------------------------------------------------------------------
; Local data contracts and WRAM fields

WINDOW_RECORD_BASE              = $8650
WINDOW_RECORD_STRIDE            = $0052
WINDOW_RECORD_PREV              = $00
WINDOW_RECORD_NEXT              = $02
WINDOW_RECORD_ALLOC_MARKER      = $04
WINDOW_RECORD_TILE_X            = $06
WINDOW_RECORD_TILE_Y            = $08
WINDOW_RECORD_WIDTH_INDEX       = $0A
WINDOW_RECORD_TILE_PTR          = $35
WINDOW_RECORD_COPY_CHAIN_HEAD   = $2B
WINDOW_RECORD_COPY_CHAIN_MID    = $2D
WINDOW_RECORD_COPY_CHAIN_TAIL   = $2F
WINDOW_RECORD_COPY_READY_A      = $31
WINDOW_RECORD_COPY_READY_B      = $33

WINDOW_RECORD_PREV_ABS          = $8650
WINDOW_RECORD_NEXT_ABS          = $8652
WINDOW_RECORD_ALLOC_MARKER_ABS  = $8654
WINDOW_RECORD_TILE_X_ABS        = $8656
WINDOW_RECORD_TILE_Y_ABS        = $8658
WINDOW_RECORD_WIDTH_INDEX_ABS   = $865A
WINDOW_RECORD_HEIGHT_OR_ROWS_ABS = $865C
WINDOW_RECORD_TILE_PTR_ABS      = $8685
WINDOW_RECORD_PRESENTATION_MAP  = $868B

OPEN_WINDOW_HEAD                = $88E0
OPEN_WINDOW_TAIL                = $88E2
LOGICAL_WINDOW_RECORD_MAP       = $88E4
FOCUSED_WINDOW_ID               = $8958
WINDOW_RELATED_MAPPING_BASE     = $894E
WINDOW_RECORD_COPY_CHAIN_BASE   = $89D4
WINDOW_RECORD_COPY_CHAIN_STRIDE = $002D

INSTANT_PRINTING_FLAG           = $9622
PRESENTATION_DIRTY_FLAG         = $9623
TEXT_DISPLAY_MODE               = $89C9
FOCUSED_PARTY_HP_PP_ACTOR       = $89CA
ACTIVE_PARTY_COUNT              = $98A4

WINDOW_ACTIVE_CLOSE_TARGET      = $5E7A
WINDOW_CLOSE_DRAIN_LATCH        = $5E70
WINDOW_CLOSE_BUSY_FLAG          = $5E75

WINDOW_DYNAMIC_TILE_FLAG_WORD   = $0002
WINDOW_DYNAMIC_TILE_SOURCE_LOW  = $1FC8
WINDOW_DYNAMIC_TILE_SOURCE_BANK = $00E0
WINDOW_DYNAMIC_TILE_ROW_TABLE   = $E01FB9
ACTIVE_CHARACTER_TABLE_INDEX    = $99CD
WINDOW_DYNAMIC_TILE_DEST        = $0228
WINDOW_DYNAMIC_TILE_WIDTH       = $0008
WINDOW_DYNAMIC_TILE_READY_BYTE  = $0030

WINDOW_TILEMAP_CLEAR_BASE       = $7DFE
FOCUSED_HP_PP_CLEAR_BASE        = $827E

REFLECT_FIRST_SIDE_ID           = $9658
REFLECT_SECOND_SIDE_ID          = $965A
REFLECT_TEXT_VARIANT            = $5E76
REFLECT_FIRST_SIDE_FLAG         = $5E77
REFLECT_SECOND_SIDE_FLAG        = $5E78
ENEMY_DESCRIPTOR_TABLE          = $D59589
ENEMY_DESCRIPTOR_STRIDE         = $005E
REFLECT_ARTICLE_FRAGMENT_A_LOW  = $0998
REFLECT_ARTICLE_FRAGMENT_B_LOW  = $099C
REFLECT_ARTICLE_FRAGMENT_BANK   = $00C2
REFLECT_ARTICLE_FRAGMENT_COUNT  = $0004

NO_INDEX                        = $FFFF
BLANK_TILE_WORD                 = $0040

; ---------------------------------------------------------------------------
; C3:E450..C3:E4EF WindowTickTransferDynamicTileBlock

; WindowTickTransferDynamicTileBlock
;
; Entry:
;   Called by the frame/window tick path when text display mode is active.
;
; Behavior:
;   Chooses one of two E0:1FC8 dynamic tile rows from flag bit $0002.2 and the
;   active character/table index, then queues an 8-word transfer to destination
;   $0228. Marks byte $0030 with $18 after the transfer.
C3E450_WindowTickTransferDynamicTileBlock:
    rep #$31
    phd
    tdc
    adc #$FFEE
    tcd

    lda WINDOW_DYNAMIC_TILE_FLAG_WORD
    and #$00FF
    and #$0004
    beq C3E489_WindowDynamicTile_UseLaterRowBias

    lda #WINDOW_DYNAMIC_TILE_SOURCE_LOW
    sta $06
    lda #WINDOW_DYNAMIC_TILE_SOURCE_BANK
    sta $08
    lda ACTIVE_CHARACTER_TABLE_INDEX
    and #$00FF
    dec A
    sta $04
    asl A
    adc $04
    tax
    lda WINDOW_DYNAMIC_TILE_ROW_TABLE,X
    clc
    adc #$0008
    clc
    adc $06
    sta $06
    bra C3E4AD_WindowDynamicTile_Transfer

C3E489_WindowDynamicTile_UseLaterRowBias:
    lda #WINDOW_DYNAMIC_TILE_SOURCE_LOW
    sta $06
    lda #WINDOW_DYNAMIC_TILE_SOURCE_BANK
    sta $08
    lda ACTIVE_CHARACTER_TABLE_INDEX
    and #$00FF
    dec A
    sta $04
    asl A
    adc $04
    tax
    lda WINDOW_DYNAMIC_TILE_ROW_TABLE,X
    clc
    adc #$0028
    clc
    adc $06
    sta $06

C3E4AD_WindowDynamicTile_Transfer:
    lda $06
    sta $0E
    lda $08
    sta $10
    ldx #WINDOW_DYNAMIC_TILE_WIDTH
    lda #WINDOW_DYNAMIC_TILE_DEST
    jsl C08ED2_QueueOrTransferDynamicTileBlock
    sep #$20
    lda #$18
    sta WINDOW_DYNAMIC_TILE_READY_BYTE
    rep #$20
    pld
    rtl

; ClearInstantPrinting
C3E4CA_ClearInstantPrinting:
    rep #$31
    sep #$20
    stz INSTANT_PRINTING_FLAG
    rep #$20
    rtl

; SetInstantPrinting
C3E4D4_SetInstantPrinting:
    rep #$31
    sep #$20
    lda #$01
    sta INSTANT_PRINTING_FLAG
    rep #$20
    rtl

; TickWindowWithoutInstantPrinting
C3E4E0_TickWindowWithoutInstantPrinting:
    rep #$31
    jsl C3E4CA_ClearInstantPrinting
    jsl C12DD5_TickWindowTextSystem
    jsl C3E4D4_SetInstantPrinting
    rtl

; ---------------------------------------------------------------------------
; C3:E4EF..C3:E6F8 FindFirstFreeWindowSlot

; FindFirstFreeWindowSlot
;
; Entry:
;   No meaningful caller input.
;
; Return:
;   A = first logical slot 0..7 whose window-record allocation marker is FFFF,
;       or FFFF when all eight slots are occupied.
C3E4EF_FindFirstFreeWindowSlot:
    rep #$31
    phd
    tdc
    adc #$FFF0
    tcd
    lda #$0000
    sta $0E
    bra C3E517_FindFirstFreeWindowSlot_TestLimit

C3E4FE_FindFirstFreeWindowSlot_TestSlot:
    ldy #WINDOW_RECORD_STRIDE
    jsl C08FF7_Multiply16
    tax
    lda WINDOW_RECORD_ALLOC_MARKER_ABS,X
    cmp #NO_INDEX
    bne C3E512_FindFirstFreeWindowSlot_NextSlot
    lda $0E
    bra C3E51F_FindFirstFreeWindowSlot_Return

C3E512_FindFirstFreeWindowSlot_NextSlot:
    lda $0E
    inc A
    sta $0E

C3E517_FindFirstFreeWindowSlot_TestLimit:
    cmp #$0008
    bne C3E4FE_FindFirstFreeWindowSlot_TestSlot
    lda #NO_INDEX

C3E51F_FindFirstFreeWindowSlot_Return:
    pld
    rtl

; CloseWindowAndReleaseTileState
;
; Entry:
;   A = logical window id, or FFFF for no-op.
;
; Behavior:
;   Unmaps and unlinks one open window, releases registered copy/text state,
;   clears its visible/backing tile state, and marks presentation dirty.
C3E521_CloseWindowAndReleaseTileState:
    rep #$31
    phd
    pha
    tdc
    adc #$FFE8
    tcd
    pla
    sta $16
    cmp #NO_INDEX
    bne C3E535_CloseWindow_MapLogicalId
    jmp C3E6F4_CloseWindowAndReleaseTileState_Return

C3E535_CloseWindow_MapLogicalId:
    lda $16
    asl A
    tax
    lda LOGICAL_WINDOW_RECORD_MAP,X
    sta $04
    cmp #NO_INDEX
    bne C3E546_CloseWindow_ClearFocusedIfNeeded
    jmp C3E6F4_CloseWindowAndReleaseTileState_Return

C3E546_CloseWindow_ClearFocusedIfNeeded:
    lda FOCUSED_WINDOW_ID
    cmp $16
    bne C3E553_CloseWindow_ClearCopyChain
    lda #NO_INDEX
    sta FOCUSED_WINDOW_ID

C3E553_CloseWindow_ClearCopyChain:
    lda $16
    jsl C3E7E3_ClearWindowRegisteredCopyChain

    lda $04
    ldy #WINDOW_RECORD_STRIDE
    jsl C08FF7_Multiply16
    tax
    ldy WINDOW_RECORD_NEXT_ABS,X
    sty $14
    lda WINDOW_RECORD_PREV_ABS,X
    sta $12
    cpy #NO_INDEX
    bne C3E577_CloseWindow_UpdateNextPrev
    sta OPEN_WINDOW_TAIL
    bra C3E585_CloseWindow_UpdatePrevNextOrHead

C3E577_CloseWindow_UpdateNextPrev:
    tya
    ldy #WINDOW_RECORD_STRIDE
    jsl C08FF7_Multiply16
    tax
    lda $12
    sta WINDOW_RECORD_PREV_ABS,X

C3E585_CloseWindow_UpdatePrevNextOrHead:
    cmp #NO_INDEX
    bne C3E591_CloseWindow_UpdatePrevNext
    ldy $14
    sty OPEN_WINDOW_HEAD
    bra C3E59F_CloseWindow_MarkFree

C3E591_CloseWindow_UpdatePrevNext:
    ldy #WINDOW_RECORD_STRIDE
    jsl C08FF7_Multiply16
    tax
    ldy $14
    tya
    sta WINDOW_RECORD_NEXT_ABS,X

C3E59F_CloseWindow_MarkFree:
    lda $04
    ldy #WINDOW_RECORD_STRIDE
    jsl C08FF7_Multiply16
    tax
    stx $10
    lda #NO_INDEX
    sta WINDOW_RECORD_ALLOC_MARKER_ABS,X
    lda $16
    asl A
    tax
    lda #NO_INDEX
    sta LOGICAL_WINDOW_RECORD_MAP,X

    ldx $10
    lda WINDOW_RECORD_TILE_X_ABS,X
    asl A
    sta $02
    lda WINDOW_RECORD_TILE_Y_ABS,X
    asl A
    asl A
    asl A
    asl A
    asl A
    asl A
    clc
    adc $02
    clc
    adc #WINDOW_TILEMAP_CLEAR_BASE
    sta $02
    sta $0E
    ldy WINDOW_RECORD_TILE_PTR_ABS,X
    sty $14
    ldx #$0000
    stx $10
    bra C3E60A_CloseWindow_TestVisibleTileLoop

C3E5E3_CloseWindow_ClearVisibleTile:
    ldy $14
    lda $0000,Y
    cmp #BLANK_TILE_WORD
    bne C3E5F2_CloseWindow_ReleaseVisibleTile
    cmp #$0000
    beq C3E5F9_CloseWindow_StoreBlankVisibleTile

C3E5F2_CloseWindow_ReleaseVisibleTile:
    lda $0000,Y
    jsl C44AF7_ReleaseTileOrGlyphResource

C3E5F9_CloseWindow_StoreBlankVisibleTile:
    lda #BLANK_TILE_WORD
    ldy $14
    sta $0000,Y
    iny
    iny
    sty $14
    ldx $10
    inx
    stx $10

C3E60A_CloseWindow_TestVisibleTileLoop:
    lda $04
    ldy #WINDOW_RECORD_STRIDE
    jsl C08FF7_Multiply16
    tax
    ldy WINDOW_RECORD_WIDTH_INDEX_ABS,X
    tax
    lda WINDOW_RECORD_HEIGHT_OR_ROWS_ABS,X
    jsl C09032_MultiplyOrDimensionHelper
    sta $02
    ldx $10
    txa
    cmp $02
    bcc C3E5E3_CloseWindow_ClearVisibleTile

    ldy #$0000
    sty $10
    bra C3E686_CloseWindow_TestBackingRowLoop

C3E62F_CloseWindow_StartBackingRow:
    lda #$0000
    sta $12
    bra C3E64D_CloseWindow_TestBackingColumnLoop

C3E636_CloseWindow_ClearBackingWord:
    lda #$0000
    ldx $0E
    stx $02
    sta $0000,X
    inc $02
    inc $02
    lda $02
    sta $0E
    lda $12
    inc A
    sta $12

C3E64D_CloseWindow_TestBackingColumnLoop:
    lda $04
    ldy #WINDOW_RECORD_STRIDE
    jsl C08FF7_Multiply16
    tax
    lda WINDOW_RECORD_WIDTH_INDEX_ABS,X
    tax
    stx $02
    inc $02
    inc $02
    lda $12
    cmp $02
    bne C3E636_CloseWindow_ClearBackingWord

    stx $02
    lda #$0020
    sec
    sbc $02
    dec A
    dec A
    asl A
    pha
    lda $0E
    sta $02
    ply
    sty $02
    clc
    adc $02
    sta $02
    sta $0E
    ldy $10
    iny
    sty $10

C3E686_CloseWindow_TestBackingRowLoop:
    lda $04
    ldy #WINDOW_RECORD_STRIDE
    jsl C08FF7_Multiply16
    tax
    stx $12
    lda WINDOW_RECORD_HEIGHT_OR_ROWS_ABS,X
    sta $02
    inc $02
    inc $02
    ldy $10
    tya
    cmp $02
    bne C3E62F_CloseWindow_StartBackingRow

    jsl C45E96_RefreshOrReleaseWindowPresentationMapping
    ldx $12
    lda WINDOW_RECORD_PRESENTATION_MAP,X
    and #$00FF
    beq C3E6BC_CloseWindow_ClearPresentationByte
    and #$00FF
    dec A
    asl A
    tax
    lda #NO_INDEX
    sta WINDOW_RELATED_MAPPING_BASE,X

C3E6BC_CloseWindow_ClearPresentationByte:
    lda $04
    ldy #WINDOW_RECORD_STRIDE
    jsl C08FF7_Multiply16
    tax
    sep #$20
    stz WINDOW_RECORD_PRESENTATION_MAP,X
    lda #$01
    sta PRESENTATION_DIRTY_FLAG
    rep #$20

    lda WINDOW_ACTIVE_CLOSE_TARGET
    cmp $16
    bne C3E6DF_CloseWindow_MaybeTickText
    lda #NO_INDEX
    sta WINDOW_ACTIVE_CLOSE_TARGET

C3E6DF_CloseWindow_MaybeTickText:
    lda WINDOW_CLOSE_DRAIN_LATCH
    and #$00FF
    bne C3E6EF_CloseWindow_ClearBusyFlag
    jsl C3E4E0_TickWindowWithoutInstantPrinting
    jsl C3E4CA_ClearInstantPrinting

C3E6EF_CloseWindow_ClearBusyFlag:
    sep #$20
    stz WINDOW_CLOSE_BUSY_FLAG

C3E6F4_CloseWindowAndReleaseTileState_Return:
    rep #$20
    pld
    rtl

; ---------------------------------------------------------------------------
; C3:E6F8..C3:E75D ClearFocusedPartyHpPpActorAndBlankRow

; ClearFocusedPartyHpPpActorAndBlankRow
;
; Entry:
;   No meaningful caller input.
;
; Behavior:
;   If a focused party HP/PP actor is latched, waits one frame, blanks that
;   actor's seven-word row in the $827E tile region, clears the latch, and marks
;   presentation dirty.
C3E6F8_ClearFocusedPartyHpPpActorAndBlankRow:
    rep #$31
    phd
    tdc
    adc #$FFF2
    tcd
    lda FOCUSED_PARTY_HP_PP_ACTOR
    cmp #NO_INDEX
    beq C3E759_ClearFocusedPartyHpPpActorAndBlankRow_Return

    jsl C08756_WaitOneFrame
    lda FOCUSED_PARTY_HP_PP_ACTOR
    sta $04
    asl A
    adc $04
    asl A
    adc $04
    sta $02
    lda ACTIVE_PARTY_COUNT
    and #$00FF
    sta $04
    asl A
    adc $04
    asl A
    adc $04
    pha
    asl A
    pla
    ror A
    sta $04
    lda #$0010
    sec
    sbc $04
    clc
    adc $02
    asl A
    clc
    adc #FOCUSED_HP_PP_CLEAR_BASE
    tay
    ldx #$0007
    bra C3E74A_ClearFocusedPartyHpPpActorAndBlankRow_TestLoop

C3E741_ClearFocusedPartyHpPpActorAndBlankRow_ClearWord:
    lda #$0000
    sta $0000,Y
    iny
    iny
    dex

C3E74A_ClearFocusedPartyHpPpActorAndBlankRow_TestLoop:
    bne C3E741_ClearFocusedPartyHpPpActorAndBlankRow_ClearWord
    lda #NO_INDEX
    sta FOCUSED_PARTY_HP_PP_ACTOR
    sep #$20
    lda #$01
    sta PRESENTATION_DIRTY_FLAG

C3E759_ClearFocusedPartyHpPpActorAndBlankRow_Return:
    rep #$20
    pld
    rtl

; ---------------------------------------------------------------------------
; C3:E75D..C3:E7E3 ResolveReflectedHitSideArticleTokens

; ResolveReflectedHitSideArticleTokens
;
; Entry:
;   A = 0 for first reflected-hit side, nonzero for second side.
;
; Behavior:
;   Resolves side-specific article text fragments for reflected-hit narration.
;   Branches that skip the `sep #$20` flag-clear path keep M=16; the byte stream
;   at E778/E794/E7A7 therefore must be decoded along the taken control-flow
;   path, not linearly from the previous flag-clear branch.
C3E75D_ResolveReflectedHitSideArticleTokens:
    rep #$31
    phd
    pha
    tdc
    adc #$FFEE
    tcd
    pla
    bne C3E785_ResolveReflectedHitSideArticleTokens_SecondSide

    lda REFLECT_FIRST_SIDE_ID
    cmp #NO_INDEX
    bne C3E778_ResolveReflectedHitSideArticleTokens_FirstSidePresent
    sep #$20

; ClearFirstReflectedHitSideArticleTokenFlag
C3E773_ClearFirstReflectedHitSideArticleTokenFlag:
    stz REFLECT_FIRST_SIDE_FLAG
    bra C3E7DF_ResolveReflectedHitSideArticleTokens_Return

C3E778_ResolveReflectedHitSideArticleTokens_FirstSidePresent:
    lda REFLECT_FIRST_SIDE_FLAG
    and #$00FF
    bne C3E7DF_ResolveReflectedHitSideArticleTokens_Return
    lda REFLECT_FIRST_SIDE_ID
    bra C3E79F_ResolveReflectedHitSideArticleTokens_LoadEnemyArticle

C3E785_ResolveReflectedHitSideArticleTokens_SecondSide:
    lda REFLECT_SECOND_SIDE_ID
    cmp #NO_INDEX
    bne C3E794_ResolveReflectedHitSideArticleTokens_SecondSidePresent
    sep #$20

; ClearSecondReflectedHitSideArticleTokenFlag
C3E78F_ClearSecondReflectedHitSideArticleTokenFlag:
    stz REFLECT_SECOND_SIDE_FLAG
    bra C3E7DF_ResolveReflectedHitSideArticleTokens_Return

C3E794_ResolveReflectedHitSideArticleTokens_SecondSidePresent:
    lda REFLECT_SECOND_SIDE_FLAG
    and #$00FF
    bne C3E7DF_ResolveReflectedHitSideArticleTokens_Return
    lda REFLECT_SECOND_SIDE_ID

C3E79F_ResolveReflectedHitSideArticleTokens_LoadEnemyArticle:
    ldy #ENEMY_DESCRIPTOR_STRIDE
    jsl C08FF7_Multiply16
    tax
    lda ENEMY_DESCRIPTOR_TABLE,X
    and #$00FF
    beq C3E7DF_ResolveReflectedHitSideArticleTokens_Return

    lda REFLECT_TEXT_VARIANT
    and #$00FF
    cmp #$0070
    bne C3E7CE_ResolveReflectedHitSideArticleTokens_UseFallbackFragment

    lda #REFLECT_ARTICLE_FRAGMENT_A_LOW
    sta $0E
    lda #REFLECT_ARTICLE_FRAGMENT_BANK
    sta $10
    lda #REFLECT_ARTICLE_FRAGMENT_COUNT
    jsl C447FB_DispatchTextControlFragment
    bra C3E7DF_ResolveReflectedHitSideArticleTokens_Return

C3E7CE_ResolveReflectedHitSideArticleTokens_UseFallbackFragment:
    lda #REFLECT_ARTICLE_FRAGMENT_B_LOW
    sta $0E
    lda #REFLECT_ARTICLE_FRAGMENT_BANK
    sta $10
    lda #REFLECT_ARTICLE_FRAGMENT_COUNT
    jsl C447FB_DispatchTextControlFragment

C3E7DF_ResolveReflectedHitSideArticleTokens_Return:
    rep #$20
    pld
    rtl

; ---------------------------------------------------------------------------
; C3:E7E3..C3:E84E ClearWindowRegisteredCopyChain

; ClearWindowRegisteredCopyChain
;
; Entry:
;   A = logical window id, or FFFF for no-op.
;
; Behavior:
;   Clears the registered text-entry/copy chain attached to one window record
;   and resets the record's copy-chain fields.
C3E7E3_ClearWindowRegisteredCopyChain:
    rep #$31
    phd
    pha
    tdc
    adc #$FFF0
    tcd
    pla
    cmp #NO_INDEX
    beq C3E84C_ClearWindowRegisteredCopyChain_Return

    asl A
    tax
    lda LOGICAL_WINDOW_RECORD_MAP,X
    ldy #WINDOW_RECORD_STRIDE
    jsl C08FF7_Multiply16
    clc
    adc #WINDOW_RECORD_BASE
    tay
    sty $0E
    lda WINDOW_RECORD_COPY_CHAIN_HEAD,Y
    cmp #NO_INDEX
    beq C3E84C_ClearWindowRegisteredCopyChain_Return

    ldy #WINDOW_RECORD_COPY_CHAIN_STRIDE
    jsl C08FF7_Multiply16
    clc
    adc #WINDOW_RECORD_COPY_CHAIN_BASE
    tax

C3E819_ClearWindowRegisteredCopyChain_ClearEntry:
    lda #$0000
    sta $0000,X
    lda $0002,X
    cmp #NO_INDEX
    beq C3E835_ClearWindowRegisteredCopyChain_ResetRecordFields
    ldy #WINDOW_RECORD_COPY_CHAIN_STRIDE
    jsl C08FF7_Multiply16
    clc
    adc #WINDOW_RECORD_COPY_CHAIN_BASE
    tax
    bra C3E819_ClearWindowRegisteredCopyChain_ClearEntry

C3E835_ClearWindowRegisteredCopyChain_ResetRecordFields:
    lda #NO_INDEX
    ldy $0E
    sta WINDOW_RECORD_COPY_CHAIN_TAIL,Y
    sta WINDOW_RECORD_COPY_CHAIN_MID,Y
    sta WINDOW_RECORD_COPY_CHAIN_HEAD,Y
    lda #$0001
    sta WINDOW_RECORD_COPY_READY_A,Y
    sta WINDOW_RECORD_COPY_READY_B,Y

C3E84C_ClearWindowRegisteredCopyChain_Return:
    pld
    rtl
