; EarthBound C4 system error screen helper prototype.
;
; Source-emission status:
; - Prototype level: build-candidate
; - First C4 pilot for the reusable source-bank scaffold pipeline.
; - Derived from notes/c4-system-error-screen-render-0b51-0b75.md.
; - Original instruction flow is preserved in address order with symbolic
;   comments for the display setup, VRAM transfer, and terminal halt path.
; - ROM byte range, SHA-1, and source signature are tracked by
;   build/c4-build-candidate-ranges.json.
;
; Source units covered:
; - C4:0B51..C4:0B75 SetupSystemErrorScreenDisplay
; - C4:0B75..C4:0BD4 RenderSystemErrorScreenAndHalt
;
; Evidence:
; - notes/c4-system-error-screen-render-0b51-0b75.md
; - refs/earthbound-disasm-legacy/Earthbound Decomp/EB/Routine_Macros_EB.asm

; ---------------------------------------------------------------------------
; External contracts used by this module

C0ABC6_StopMusicAndLatchNoTrack              = $C0ABC6
C08D79_UpdateBgModeRegisterFromQueue         = $C08D79
C08E1C_UpdateBg3ScreenBaseRegistersFromQueue = $C08E1C
C08726_BlankWaitAndDisableHdma               = $C08726
C08616_QueueVramTransfer_FromDpSource        = $C08616
C08ED2_QueueOrTransferDynamicTileBlock       = $C08ED2
C0856B_WriteAtoDisplaySelector30             = $C0856B
C087CE_ApplyDisplayStateOrLayerPreset        = $C087CE

; C0:8616 QueueVramTransfer_FromDpSource
;   Inputs used here:
;     DP+$0E/$10 = source pointer
;     A = VRAM target, X = transfer size, Y = source offset
;   Contract note:
;     The original caller expects this helper to return with 16-bit A.

; C0:8ED2 QueueOrTransferDynamicTileBlock
;   Inputs used here:
;     DP+$0E/$10 = source pointer
;     A = WRAM destination, X = transfer size
;   Contract note:
;     The original caller expects this helper to return with 16-bit A.

; ---------------------------------------------------------------------------
; Local data contracts and WRAM fields

VRAM_TRANSFER_SOURCE_LOW      = $0E
VRAM_TRANSFER_SOURCE_BANK     = $10

SYSTEM_SCREEN_WRAM_BLOCK_A    = $0000
SYSTEM_SCREEN_WRAM_BLOCK_B    = $4000
SYSTEM_SCREEN_WRAM_BANK       = $007F
SYSTEM_SCREEN_VRAM_TARGET_A   = $0000
SYSTEM_SCREEN_VRAM_TARGET_B   = $4000
SYSTEM_SCREEN_VRAM_SIZE_A     = $0A00
SYSTEM_SCREEN_VRAM_SIZE_B     = $0800

SPECIAL_STARTUP_SCREEN_PALETTE = $F3BE
SPECIAL_STARTUP_SCREEN_BANK    = $00D8
SPECIAL_STARTUP_PALETTE_DEST   = $0200
SPECIAL_STARTUP_PALETTE_SIZE   = $0010

BG_MODE_1                     = $0001
BG3_SCREEN_BASE_TARGET        = $4000
DISPLAY_CONTROL_SHADOW_1A     = $001A
DISPLAY_CONTROL_VALUE_04      = $04
FULL_CGRAM_UPLOAD_SELECTOR    = $0018

; Direct-page locals:
;   $0E/$10 = long source pointer used by C0:8616 and C0:8ED2

; ---------------------------------------------------------------------------
; C4:0B51

; SetupSystemErrorScreenDisplay
;
; Stops music, queues a BG mode/screen-base state for the terminal system
; warning screens, writes the display-control shadow used by the caller, then
; blanks/waits/disables HDMA through the C0 display helper.
C40B51_SetupSystemErrorScreenDisplay:
    rep #$31
    jsl C0ABC6_StopMusicAndLatchNoTrack
    lda #BG_MODE_1
C40B59_SetupSystemErrorScreenDisplay_QueueBgMode:
    jsl C08D79_UpdateBgModeRegisterFromQueue
    ldy #$0000
    ldx #BG3_SCREEN_BASE_TARGET
    tya
    jsl C08E1C_UpdateBg3ScreenBaseRegistersFromQueue
    sep #$20
    lda.b #DISPLAY_CONTROL_VALUE_04
    sta.w DISPLAY_CONTROL_SHADOW_1A
    jsl C08726_BlankWaitAndDisableHdma
    rtl

; ---------------------------------------------------------------------------
; C4:0B75

; RenderSystemErrorScreenAndHalt
;
; Uploads the two caller-decompressed WRAM blocks into VRAM, copies the shared
; system warning palette/control block, applies the final display selector, and
; falls into the permanent halt loop.
C40B75_RenderSystemErrorScreenAndHalt:
    rep #$31
    phd
    tdc
    adc #$FFEE
    tcd

    lda #SYSTEM_SCREEN_WRAM_BLOCK_A
    sta VRAM_TRANSFER_SOURCE_LOW
    lda #SYSTEM_SCREEN_WRAM_BANK
    sta VRAM_TRANSFER_SOURCE_BANK
    ldy #$0000
    ldx #SYSTEM_SCREEN_VRAM_SIZE_A
    sep #$20
    tya
    jsl C08616_QueueVramTransfer_FromDpSource

    lda.w #SYSTEM_SCREEN_WRAM_BLOCK_B
    sta VRAM_TRANSFER_SOURCE_LOW
    lda.w #SYSTEM_SCREEN_WRAM_BANK
    sta VRAM_TRANSFER_SOURCE_BANK
    ldy #SYSTEM_SCREEN_VRAM_TARGET_B
    ldx #SYSTEM_SCREEN_VRAM_SIZE_B
    sep #$20
    lda.b #SYSTEM_SCREEN_VRAM_TARGET_A
    jsl C08616_QueueVramTransfer_FromDpSource

    lda.w #SPECIAL_STARTUP_SCREEN_PALETTE
    sta VRAM_TRANSFER_SOURCE_LOW
    lda.w #SPECIAL_STARTUP_SCREEN_BANK
    sta VRAM_TRANSFER_SOURCE_BANK
    ldx #SPECIAL_STARTUP_PALETTE_SIZE
    lda.w #SPECIAL_STARTUP_PALETTE_DEST
    jsl C08ED2_QueueOrTransferDynamicTileBlock

    lda.w #FULL_CGRAM_UPLOAD_SELECTOR
    jsl C0856B_WriteAtoDisplaySelector30
    ldy #$0000
    ldx #$0001
    txa
    jsl C087CE_ApplyDisplayStateOrLayerPreset
C40BD2_SystemErrorScreenHaltLoop:
    bra C40BD2_SystemErrorScreenHaltLoop
