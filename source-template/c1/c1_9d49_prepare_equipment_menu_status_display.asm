; EarthBound C1 equipment/shop menu display preparation.
;
; Source units covered:
; - C1:9D49..C1:9DB5 PrepareEquipmentMenuStatusDisplay
; - C1:9DB5..C1:9EE6 RunShopItemSelectionMenu

C104EE_CreateOrBindWindowDescriptorAndContext = $04EE
C10EB4_ClearOrPrepareWindowContent = $0EB4
C115F4_CreateTypedTextEntryRecordDirect = $15F4
C1180D_LayoutActiveTextEntriesAndRefresh = $180D
C1196A_RunActiveTextEntrySelectionMenu = $196A
C11F5A_InstallSelectionPromptCallback = $1F5A
C10084_CloseCurrentFocusWindowOrContext = $0084
C19CDD_InitializeEquipmentComparisonMarkersDefault = $9CDD
C1AA18_RefreshWalletOrStatusDisplay = $AA18
C08ED2_QueueOrTransferDynamicTileBlock = $C08ED2
C08FF7_ResolveIndexedPointerOffset = $C08FF7
C20A20_SnapshotManagedTextEventSlotState = $C20A20
C20ABC_RestoreManagedTextEventSlotState = $C20ABC
C3E4CA_FinalizeOrRefreshMenuDisplay = $C3E4CA
C3E4D4_PrepareMenuDisplayContext = $C3E4D4
C438A5_ConfigureTextEntryRowPosition = $C438A5
C4507A_PrintActiveWindowRightAlignedDecimal = $C4507A

CharacterRecordStride = $005F
DefaultEquipmentComparisonMarker = $0400
EquipmentComparisonMarkers = $9A1D
ItemConfigurationTable = $D55000
ItemRecordStride = $0027
ItemNameStagingBuffer = $9C9F
MenuContextSnapshotBuffer = $9C8A
ShopItemTable = $D576B2
ShopStatusRowOffsetTable = $E01FB9
ShopStatusTilemapRows = $E01FC8

; ---------------------------------------------------------------------------
; C1:9D49

C19D49_PrepareEquipmentMenuStatusDisplay:
    rep #$31
    phd
    tdc
    adc.w #$FFEC
    tcd
    lda.w #$0000
    sta $12
    bra C19D6B_CheckNextCharacterMarker

C19D58_ResetCharacterMarker:
    ldy.w #CharacterRecordStride
    jsl C08FF7_ResolveIndexedPointerOffset
    tax
    lda.w #DefaultEquipmentComparisonMarker
    sta EquipmentComparisonMarkers,X
    lda $12
    inc A
    sta $12

C19D6B_CheckNextCharacterMarker:
    cmp.w #$0004
    bcc C19D58_ResetCharacterMarker
    lda.w #ShopStatusTilemapRows
    sta $06
    lda.w #$00E0
    sta $08
    lda $99CD
    and.w #$00FF
    dec A
    sta $04
    asl A
    adc $04
    tax
    lda ShopStatusRowOffsetTable,X
    clc
    adc.w #$0018
    clc
    adc $06
    sta $06
    sta $0E
    lda $08
    sta $10
    ldx.w #$0008
    lda.w #$0218
    jsl C08ED2_QueueOrTransferDynamicTileBlock
    sep #$20
    lda.b #$18
    sta $0030
    rep #$20
    lda.w #$0001
    sta $9623
    pld
    rts

; ---------------------------------------------------------------------------
; C1:9DB5

C19DB5_RunShopItemSelectionMenu:
    rep #$31
    phd
    pha
    tdc
    adc.w #$FFE0
    tcd
    pla
    sta $1E
    jsr C1AA18_RefreshWalletOrStatusDisplay
    jsl C3E4D4_PrepareMenuDisplayContext
    lda.w #MenuContextSnapshotBuffer
    jsl C20A20_SnapshotManagedTextEventSlotState
    lda.w #$000C
    jsr C104EE_CreateOrBindWindowDescriptorAndContext
    lda.w #$0005
    jsr C10EB4_ClearOrPrepareWindowContent
    lda.w #$0000
    sta $04
    sta $1C
    jmp.w C19E99_CheckNextShopItemRow

C19DE5_BuildShopItemTextEntry:
    lda $1E
    sta $04
    asl A
    adc $04
    asl A
    adc $04
    ldx $1C
    stx $04
    clc
    adc $04
    tax
    lda ShopItemTable,X
    and.w #$00FF
    tay
    sty $1A
    bne C19E06_CopyShopItemName
    jmp.w C19E93_AdvanceShopItemRow

C19E06_CopyShopItemName:
    lda.w #ItemConfigurationTable
    sta $06
    lda.w #$00D5
    sta $08
    lda $06
    sta $16
    lda $08
    sta $18
    tya
    ldy.w #ItemRecordStride
    jsl C08FF7_ResolveIndexedPointerOffset
    sta $02
    clc
    adc $06
    sta $06
    sta $0E
    lda $08
    sta $10
    ldx.w #$0019
    lda.w #ItemNameStagingBuffer
    jsl C08ED2_QueueOrTransferDynamicTileBlock
    sep #$20
    stz $9CB8
    rep #$20
    lda.w #ItemNameStagingBuffer
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
    lda.w #$0000
    sta $12
    lda.w #$0000
    sta $14
    ldy $1A
    tya
    jsr C115F4_CreateTypedTextEntryRecordDirect
    ldx $04
    lda.w #$0000
    jsl C438A5_ConfigureTextEntryRowPosition
    lda $02
    clc
    adc.w #$001A
    ldx $16
    stx $06
    ldx $18
    stx $08
    clc
    adc $06
    sta $06
    lda [$06]
    sta $06
    stz $08
    lda $06
    sta $0E
    lda $08
    sta $10
    jsl C4507A_PrintActiveWindowRightAlignedDecimal

C19E93_AdvanceShopItemRow:
    inc $04
    lda $04
    sta $1C

C19E99_CheckNextShopItemRow:
    lda $04
    cmp.w #$0007
    bcs C19EA5_RunShopMenuSelection
    beq C19EA5_RunShopMenuSelection
    jmp.w C19DE5_BuildShopItemTextEntry

C19EA5_RunShopMenuSelection:
    ldx.w #$0000
    txa
    jsl C438A5_ConfigureTextEntryRowPosition
    ldy.w #$0000
    tyx
    lda.w #$0001
    jsr C1180D_LayoutActiveTextEntriesAndRefresh
    lda.w #$9B4E
    sta $0E
    lda.w #$00C1
    sta $10
    jsr C11F5A_InstallSelectionPromptCallback
    jsr C19CDD_InitializeEquipmentComparisonMarkersDefault
    lda.w #$0001
    jsr C1196A_RunActiveTextEntrySelectionMenu
    tax
    stx $1A
    jsr.w C19D49_PrepareEquipmentMenuStatusDisplay
    jsr C10084_CloseCurrentFocusWindowOrContext
    lda.w #MenuContextSnapshotBuffer
    jsl C20ABC_RestoreManagedTextEventSlotState
    jsl C3E4CA_FinalizeOrRefreshMenuDisplay
    ldx $1A
    txa
    pld
    rts
