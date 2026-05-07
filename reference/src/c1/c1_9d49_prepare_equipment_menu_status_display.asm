; EarthBound C1 equipment/shop menu display preparation.
;
; Source units covered:
; - C1:9D49..C1:9DB5 PrepareEquipmentMenuStatusDisplay
; - C1:9DB5..C1:9EE6 RunShopItemSelectionMenu
;
; Runtime contract:
; - `C1:9D49` is the shop/equipment status panel reset used after shop
;   selection. It restores the four comparison lanes to 0x0400 and copies the
;   selected-character E0 status tilemap row into `$0218`.
; - `C1:9DB5` builds the shop item list from `D5:76B2`, stages item names from
;   `D5:5000`, prints the item cost from item-row byte pair `+0x1A`, and
;   installs `C1:9B4E` as the candidate comparison callback before the menu
;   selection loop.

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
ShopMenuComparisonCallbackLo = $0E
ShopMenuComparisonCallbackBank = $10
ShopStatusComparisonCharacterIndex = $12
ShopStatusRowIndexScratch = $04
ShopStatusTileBlockSourcePointerLo = $0E
ShopStatusTileBlockSourcePointerBank = $10
ShopMenuTableSelector = $1E
ShopMenuRowIndex = $1C
ShopMenuRowScratch = $04
ShopMenuItemId = $1A
ShopMenuSelectionResult = $1A
ShopMenuItemRecordOffset = $02
ShopMenuItemRowPointerLo = $16
ShopMenuItemRowPointerBank = $18
ShopMenuTileBlockSourcePointerLo = $0E
ShopMenuTileBlockSourcePointerBank = $10
ShopMenuTextEntrySourcePointerLo = $0E
ShopMenuTextEntrySourcePointerBank = $10
ShopMenuTextEntryMetadataLo = $12
ShopMenuTextEntryMetadataHi = $14
ShopMenuPriceSourcePointerLo = $0E
ShopMenuPriceSourcePointerHi = $10

; ---------------------------------------------------------------------------
; C1:9D49

C19D49_PrepareEquipmentMenuStatusDisplay:
    rep #$31
    phd
    tdc
    adc.w #$FFEC
    tcd
    lda.w #$0000
    sta ShopStatusComparisonCharacterIndex
    bra C19D6B_CheckNextCharacterMarker

C19D58_ResetCharacterMarker:
    ldy.w #CharacterRecordStride
    jsl C08FF7_ResolveIndexedPointerOffset
    tax
    lda.w #DefaultEquipmentComparisonMarker
    sta EquipmentComparisonMarkers,X
    lda ShopStatusComparisonCharacterIndex
    inc A
    sta ShopStatusComparisonCharacterIndex

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
    sta ShopStatusRowIndexScratch
    asl A
    adc ShopStatusRowIndexScratch
    tax
    lda ShopStatusRowOffsetTable,X
    clc
    adc.w #$0018
    clc
    adc $06
    sta $06
    sta ShopStatusTileBlockSourcePointerLo
    lda $08
    sta ShopStatusTileBlockSourcePointerBank
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
    sta ShopMenuTableSelector
    jsr C1AA18_RefreshWalletOrStatusDisplay
    jsl C3E4D4_PrepareMenuDisplayContext
    lda.w #MenuContextSnapshotBuffer
    jsl C20A20_SnapshotManagedTextEventSlotState
    lda.w #$000C
    jsr CREATE_WINDOW
    lda.w #$0005
    jsr C10EB4_ClearOrPrepareWindowContent
    lda.w #$0000
    sta ShopMenuRowScratch
    sta ShopMenuRowIndex
    jmp.w C19E99_CheckNextShopItemRow

C19DE5_BuildShopItemTextEntry:
    lda ShopMenuTableSelector
    sta ShopMenuRowScratch
    asl A
    adc ShopMenuRowScratch
    asl A
    adc ShopMenuRowScratch
    ldx ShopMenuRowIndex
    stx ShopMenuRowScratch
    clc
    adc ShopMenuRowScratch
    tax
    lda ShopItemTable,X
    and.w #$00FF
    tay
    sty ShopMenuItemId
    bne C19E06_CopyShopItemName
    jmp.w C19E93_AdvanceShopItemRow

C19E06_CopyShopItemName:
    lda.w #ItemConfigurationTable
    sta $06
    lda.w #$00D5
    sta $08
    lda $06
    sta ShopMenuItemRowPointerLo
    lda $08
    sta ShopMenuItemRowPointerBank
    tya
    ldy.w #ItemRecordStride
    jsl C08FF7_ResolveIndexedPointerOffset
    sta ShopMenuItemRecordOffset
    clc
    adc $06
    sta $06
    sta ShopMenuTileBlockSourcePointerLo
    lda $08
    sta ShopMenuTileBlockSourcePointerBank
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
    sta ShopMenuTextEntrySourcePointerLo
    lda $08
    sta ShopMenuTextEntrySourcePointerBank
    lda.w #$0000
    sta ShopMenuTextEntryMetadataLo
    lda.w #$0000
    sta ShopMenuTextEntryMetadataHi
    ldy ShopMenuItemId
    tya
    jsr C115F4_CreateTypedTextEntryRecordDirect
    ldx ShopMenuRowScratch
    lda.w #$0000
    jsl C438A5_ConfigureTextEntryRowPosition
    lda ShopMenuItemRecordOffset
    clc
    adc.w #$001A
    ldx ShopMenuItemRowPointerLo
    stx $06
    ldx ShopMenuItemRowPointerBank
    stx $08
    clc
    adc $06
    sta $06
    lda [$06]
    sta $06
    stz $08
    lda $06
    sta ShopMenuPriceSourcePointerLo
    lda $08
    sta ShopMenuPriceSourcePointerHi
    jsl C4507A_PrintActiveWindowRightAlignedDecimal

C19E93_AdvanceShopItemRow:
    inc ShopMenuRowScratch
    lda ShopMenuRowScratch
    sta ShopMenuRowIndex

C19E99_CheckNextShopItemRow:
    lda ShopMenuRowScratch
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
    sta ShopMenuComparisonCallbackLo
    lda.w #$00C1
    sta ShopMenuComparisonCallbackBank
    jsr C11F5A_InstallSelectionPromptCallback
    jsr C19CDD_InitializeEquipmentComparisonMarkersDefault
    lda.w #$0001
    jsr C1196A_RunActiveTextEntrySelectionMenu
    tax
    stx ShopMenuSelectionResult
    jsr.w C19D49_PrepareEquipmentMenuStatusDisplay
    jsr C10084_CloseCurrentFocusWindowOrContext
    lda.w #MenuContextSnapshotBuffer
    jsl C20ABC_RestoreManagedTextEventSlotState
    jsl C3E4CA_FinalizeOrRefreshMenuDisplay
    ldx ShopMenuSelectionResult
    txa
    pld
    rts
