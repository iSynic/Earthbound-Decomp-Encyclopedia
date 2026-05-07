; EarthBound C4 gas-station intro visual loader prototype.
;
; Source-emission status:
; - Prototype level: build-candidate
; - C4 source-bank scaffold slice.
; - Derived from notes/bank-c4-cluster-map.md and legacy Routine_Macros_EB.
; - ROM byte range, SHA-1, and source signature are tracked by
;   build/c4-build-candidate-ranges.json.
;
; Source units covered:
; - C4:A377..C4:A591 graphics/tilemap/palette loader for the gas-station
;   intro or "War on Giygas" presentation screen.

; ---------------------------------------------------------------------------
; External contracts used by this module

C08616_QueueVramTransfer_FromDpSource        = $C08616
C08D79_UpdateBgModeRegisterFromQueue         = $C08D79
C08D9E_UpdateBg1ScreenBaseRegistersFromQueue = $C08D9E
C08DDE_UpdateBg3ScreenBaseRegistersFromQueue = $C08DDE
C08ED2_QueueOrTransferDynamicTileBlock       = $C08ED2
C2C92D_QueueOrApplyBattleVisualScript        = $C2C92D
C2CFE5_DecompressOrCopyBattleVisualAsset     = $C2CFE5
C41A9E_GraphicsDecompressionRoutines_Main    = $C41A9E

; ---------------------------------------------------------------------------
; ROM / WRAM contracts

GAS_STATION_GRAPHICS_SELECTOR_SOURCE         = $CAF038
GAS_STATION_GRAPHICS_SELECTOR_SOURCE_BANK    = $00CA
GAS_STATION_GRAPHICS_POINTER_TABLE_A         = $CAD7A1
GAS_STATION_GRAPHICS_POINTER_TABLE_A_BANK    = $00CA
GAS_STATION_GRAPHICS_POINTER_TABLE_B         = $CAD93D
GAS_STATION_GRAPHICS_POINTER_TABLE_B_BANK    = $00CA
GAS_STATION_GRAPHICS_POINTER_TABLE_C         = $CADCA1
GAS_STATION_GRAPHICS_POINTER_TABLE_C_BANK    = $00CA
GAS_STATION_GRAPHICS_POINTER_TABLE_D         = $CADAD9
GAS_STATION_GRAPHICS_POINTER_TABLE_D_BANK    = $00CA

GAS_STATION_WORK_BASE                        = $0000
GAS_STATION_WORK_BANK                        = $007F
GAS_STATION_VRAM_SOURCE_BASE                 = $7C00
GAS_STATION_BG1_SCREEN_BASE                  = $7800
GAS_STATION_BG3_SCREEN_BASE                  = $7C00
GAS_STATION_BG3_VRAM_TARGET                  = $6000
GAS_STATION_BG3_UPLOAD_SIZE                  = $2000
GAS_STATION_TILE_UPLOAD_SIZE                 = $0800
GAS_STATION_TILE_ATTR_BYTES                  = $0800
GAS_STATION_TILE_ATTR_HIGH_BYTE_OFFSET       = $0001
GAS_STATION_BG_MODE_3                        = $0003
GAS_STATION_CLEAR_SELECTOR                   = $0000
GAS_STATION_UPLOAD_SELECTOR_00               = $00
GAS_STATION_POINTER_BANK_OFFSET              = $0002
GAS_STATION_SELECTOR_OFFSET_C                = $1397
GAS_STATION_SELECTOR_OFFSET_D                = $1398
GAS_STATION_BATTLE_VISUAL_SCRIPT             = $ADD4
GAS_STATION_BATTLE_VISUAL_STATE              = $AE20
GAS_STATION_BATTLE_VISUAL_ENABLE             = $AE4B
GAS_STATION_BATTLE_VISUAL_TILE_STATE         = $0240
GAS_STATION_BATTLE_VISUAL_CHUNK_A_DEST       = $ADE0
GAS_STATION_BATTLE_VISUAL_CHUNK_B_DEST       = $AE00
GAS_STATION_BATTLE_VISUAL_CHUNK_SIZE         = $0020
GAS_STATION_BATTLE_VISUAL_SCRIPT_START       = $02
GAS_STATION_TILE_ATTR_MASK                   = $DF
GAS_STATION_TILE_ATTR_SET_BITS               = $08
LowByteMask                                  = $00FF
ZeroWord                                     = $0000

; ---------------------------------------------------------------------------
; C4:A377

; Loads the gas-station / War-on-Giygas intro visual package. C4 owns the CA
; selector/pointer-table walk, $7F:0000 decompression staging, tilemap attribute
; rewrite, VRAM queue arguments, and small battle-visual tail seeds; C0/C2 own
; the display queue, decompressed battle-visual asset format, and script runner.
C4A377_LoadGasStationIntroGraphicsAndTilemap:
    rep #$31
    phd
    tdc
    adc #$FFE0
    tcd
    ; Queue BG mode/base setup for the intro screen and clear the BG3 tile area.
    lda #GAS_STATION_BG_MODE_3
    jsl C08D79_UpdateBgModeRegisterFromQueue
    ldy #ZeroWord
    ldx #GAS_STATION_BG1_SCREEN_BASE
    tya
    jsl C08D9E_UpdateBg1ScreenBaseRegistersFromQueue
    ldy #GAS_STATION_BG3_VRAM_TARGET
    ldx #GAS_STATION_BG3_SCREEN_BASE
    lda #GAS_STATION_CLEAR_SELECTOR
    jsl C08DDE_UpdateBg3ScreenBaseRegistersFromQueue

    ; First selector byte at CA:F038 chooses a CA:D7A1 graphics pointer.
    ; Decompress that asset to $7F:0000 and queue $2000 bytes to VRAM $6000.
    lda #GAS_STATION_GRAPHICS_SELECTOR_SOURCE
    sta $0A
    lda #GAS_STATION_GRAPHICS_SELECTOR_SOURCE_BANK
    sta $0C
    lda #GAS_STATION_WORK_BASE
    sta $06
    lda #GAS_STATION_WORK_BANK
    sta $08
    lda $06
    sta $1C
    lda $08
    sta $1E
    lda #GAS_STATION_GRAPHICS_POINTER_TABLE_A
    sta $06
    lda #GAS_STATION_GRAPHICS_POINTER_TABLE_A_BANK
    sta $08
    lda [$0A]
    and #LowByteMask
    asl
    asl
    clc
    adc $06
    sta $06
    ldy #GAS_STATION_POINTER_BANK_OFFSET
    lda [$06],y
    tay
    lda [$06]
    sta $06
    sty $08
    lda $06
    sta $0E
    lda $08
    sta $10
    lda $1C
    sta $06
    lda $1E
    sta $08
    lda $06
    sta $12
    lda $08
    sta $14
    jsl C41A9E_GraphicsDecompressionRoutines_Main

    lda $06
    sta $0E
    lda $08
    sta $10
    ldy #GAS_STATION_BG3_VRAM_TARGET
    ldx #GAS_STATION_BG3_UPLOAD_SIZE
    sep #$20
    lda.b #GAS_STATION_UPLOAD_SELECTOR_00
    jsl C08616_QueueVramTransfer_FromDpSource
    ; Reuse the same selector for the CA:D93D tilemap pointer table, then
    ; decompress the tilemap to the same $7F:0000 staging buffer.
    lda [$0A]
    and.w #LowByteMask
    asl
    asl
    pha
    lda.w #GAS_STATION_GRAPHICS_POINTER_TABLE_B
    sta $0A
    lda.w #GAS_STATION_GRAPHICS_POINTER_TABLE_B_BANK
    sta $0C
    pla
    clc
    adc $0A
    sta $0A
    ldy #GAS_STATION_POINTER_BANK_OFFSET
    lda [$0A],y
    tay
    lda [$0A]
    sta $06
    sty $08
    lda $06
    sta $0E
    lda $08
    sta $10
    lda $1C
    sta $06
    lda $1E
    sta $08
    lda $06
    sta $12
    lda $08
    sta $14
    jsl C41A9E_GraphicsDecompressionRoutines_Main

    lda #ZeroWord
    sta $1A
    bra C4A47A_LoadGasStationIntroGraphicsAndTilemap_AttrLoopCheck

; Rewrites the high byte of each tilemap word in $7F:0000..07FF, clearing bit
; $20 and setting bit $08 before the tilemap is queued to VRAM-source $7C00.
C4A455_LoadGasStationIntroGraphicsAndTilemap_AttrLoop:
    sta $06
    stz $08
    clc
    lda $06
    adc #GAS_STATION_TILE_ATTR_HIGH_BYTE_OFFSET
    sta $06
    lda $08
    adc #GAS_STATION_WORK_BANK
    sta $08
    sep #$20
    lda [$06]
    and.b #GAS_STATION_TILE_ATTR_MASK
    ora.b #GAS_STATION_TILE_ATTR_SET_BITS
    sta [$06]
    rep #$20
    lda $1A
    inc
    inc
    sta $1A
C4A47A_LoadGasStationIntroGraphicsAndTilemap_AttrLoopCheck:
    cmp #GAS_STATION_TILE_ATTR_BYTES
    bcc C4A455_LoadGasStationIntroGraphicsAndTilemap_AttrLoop

    lda #GAS_STATION_WORK_BASE
    sta $0E
    lda #GAS_STATION_WORK_BANK
    sta $10
    ldy #GAS_STATION_VRAM_SOURCE_BASE
    ldx #GAS_STATION_TILE_UPLOAD_SIZE
    sep #$20
    lda.b #GAS_STATION_UPLOAD_SELECTOR_00
    jsl C08616_QueueVramTransfer_FromDpSource
    ; Tail setup: feed the C2 battle-visual asset/script side with CA:DCA1 and
    ; CA:DAD9 table selections, plus the local $ADD4/$AE20/$AE4B state seeds.
    lda.w #GAS_STATION_GRAPHICS_POINTER_TABLE_C
    sta $0A
    lda.w #GAS_STATION_GRAPHICS_POINTER_TABLE_C_BANK
    sta $0C
    lda.w #GAS_STATION_SELECTOR_OFFSET_C
    ldx $0A
    stx $06
    ldx $0C
    stx $08
    clc
    adc $06
    sta $06
    sta $0E
    lda $08
    sta $10
    lda #GAS_STATION_BATTLE_VISUAL_SCRIPT
    jsl C2CFE5_DecompressOrCopyBattleVisualAsset
    lda #GAS_STATION_BATTLE_VISUAL_STATE
    sta $02
    lda #GAS_STATION_BATTLE_VISUAL_TILE_STATE
    ldx $02
    sta.w $0000,x
    ldy #GAS_STATION_BATTLE_VISUAL_CHUNK_A_DEST
    sty $18

    lda #GAS_STATION_GRAPHICS_POINTER_TABLE_D
    sta $06
    lda #GAS_STATION_GRAPHICS_POINTER_TABLE_D_BANK
    sta $08
    lda $06
    sta $1C
    lda $08
    sta $1E
    lda #GAS_STATION_SELECTOR_OFFSET_D
    clc
    adc $0A
    sta $0A
    lda [$0A]
    and #LowByteMask
    asl
    asl
    clc
    adc $06
    sta $06
    ldy #GAS_STATION_POINTER_BANK_OFFSET
    lda [$06],y
    tay
    lda [$06]
    sta $06
    sty $08
    lda $06
    sta $0E
    lda $08
    sta $10
    ldx #GAS_STATION_BATTLE_VISUAL_CHUNK_SIZE
    ldy $18
    tya
    jsl C08ED2_QueueOrTransferDynamicTileBlock
    lda [$0A]
    and #LowByteMask
    asl
    asl
    ldx $1C
    stx $06
    ldx $1E
    stx $08
    ldx $06
    stx $0A
    ldx $08
    stx $0C
    clc
    adc $0A
    sta $0A
    ldy #GAS_STATION_POINTER_BANK_OFFSET
    lda [$0A],y
    tay
    lda [$0A]
    sta $06
    sty $08
    lda $06
    sta $0E
    lda $08
    sta $10
    ldx #GAS_STATION_BATTLE_VISUAL_CHUNK_SIZE
    lda #GAS_STATION_BATTLE_VISUAL_CHUNK_B_DEST
    jsl C08ED2_QueueOrTransferDynamicTileBlock
    ldy $18
    tya
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
    ldx #GAS_STATION_BATTLE_VISUAL_CHUNK_SIZE
    stx $16
    ldx $02
    lda.w $0000,x
    ldx $16
    jsl C08ED2_QueueOrTransferDynamicTileBlock
    sep #$20
    lda.b #GAS_STATION_BATTLE_VISUAL_SCRIPT_START
    sta.w GAS_STATION_BATTLE_VISUAL_SCRIPT
    ldx #ZeroWord
    rep #$20
    lda #GAS_STATION_BATTLE_VISUAL_SCRIPT
    jsl C2C92D_QueueOrApplyBattleVisualScript
    sep #$20
    stz.w GAS_STATION_BATTLE_VISUAL_ENABLE
    rep #$20
    pld
    rtl
