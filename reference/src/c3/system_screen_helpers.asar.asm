; EarthBound C3 system screen helper source pilot.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Assembler contract: source-pilot
; - Included by the C3 event/actionscript source-pilot scaffold as a
;   supplemental native-helper span inside the C3:0000..0295 prefix.
; - The surrounding C3:0000..0100 palette data and C3:0184..0195 data/script
;   prelude remain preserved as non-source payload bytes.
;
; Source units covered:
; - C3:0100..C3:0142 DisplayAntiPiracyScreen
; - C3:0142..C3:0184 DisplayFaultyGamePakScreen
;
; Evidence:
; - notes/c4-system-error-screen-render-0b51-0b75.md
; - refs/EB-M2-Listing-v1/US/bank03.txt

; ---------------------------------------------------------------------------
; External contracts used by this module

C40B51_SetupSystemErrorScreenDisplay = $C40B51
C40B75_RenderSystemErrorScreenAndHalt = $C40B75
C41A9E_DecompressAssetToLongDest = $C41A9E

; ---------------------------------------------------------------------------
; Asset pointer contracts

ASSET_BANK_D8_WORD = $00D8
SYSTEM_SCREEN_WORK_BUFFER_BANK = $007F
SYSTEM_SCREEN_GRAPHICS_DEST_LOW = $0000
SYSTEM_SCREEN_TILEMAP_DEST_LOW = $4000

ANTI_PIRACY_NOTICE_GRAPHICS = $F20D
ANTI_PIRACY_NOTICE_ARRANGEMENT = $F05E
FAULTY_GAME_PAK_GRAPHICS = $F5C4
FAULTY_GAME_PAK_ARRANGEMENT = $F3C6

; ---------------------------------------------------------------------------
; Stack-frame local pointer slots

LOCAL_SOURCE_PTR_LOW = $0E
LOCAL_SOURCE_PTR_BANK = $10
LOCAL_DEST_PTR_LOW = $12
LOCAL_DEST_PTR_BANK = $14

; ---------------------------------------------------------------------------
; C3:0100

; DisplayAntiPiracyScreen
;
; Builds the copyright-protection warning screen, then joins the shared C4
; system-screen render/halt path.
org $C30100
C30100_DisplayAntiPiracyScreen:
    rep #$31
    phd
    tdc
    adc.w #$FFEA
    tcd
    jsl C40B51_SetupSystemErrorScreenDisplay
    lda.w #ANTI_PIRACY_NOTICE_GRAPHICS
    sta.b LOCAL_SOURCE_PTR_LOW
    lda.w #ASSET_BANK_D8_WORD
    sta.b LOCAL_SOURCE_PTR_BANK
    lda.w #SYSTEM_SCREEN_GRAPHICS_DEST_LOW
    sta.b LOCAL_DEST_PTR_LOW
    lda.w #SYSTEM_SCREEN_WORK_BUFFER_BANK
    sta.b LOCAL_DEST_PTR_BANK
    jsl C41A9E_DecompressAssetToLongDest
    lda.w #ANTI_PIRACY_NOTICE_ARRANGEMENT
    sta.b LOCAL_SOURCE_PTR_LOW
    lda.w #ASSET_BANK_D8_WORD
    sta.b LOCAL_SOURCE_PTR_BANK
    lda.w #SYSTEM_SCREEN_TILEMAP_DEST_LOW
    sta.b LOCAL_DEST_PTR_LOW
    lda.w #SYSTEM_SCREEN_WORK_BUFFER_BANK
    sta.b LOCAL_DEST_PTR_BANK
    jsl C41A9E_DecompressAssetToLongDest
    jsl C40B75_RenderSystemErrorScreenAndHalt
    pld
    rtl

; ---------------------------------------------------------------------------
; C3:0142

; DisplayFaultyGamePakScreen
;
; Builds the incorrect-region/faulty Game Pak warning screen, then joins the
; shared C4 system-screen render/halt path.
org $C30142
C30142_DisplayFaultyGamePakScreen:
    rep #$31
    phd
    tdc
    adc.w #$FFEA
    tcd
    jsl C40B51_SetupSystemErrorScreenDisplay
    lda.w #FAULTY_GAME_PAK_GRAPHICS
    sta.b LOCAL_SOURCE_PTR_LOW
    lda.w #ASSET_BANK_D8_WORD
    sta.b LOCAL_SOURCE_PTR_BANK
    lda.w #SYSTEM_SCREEN_GRAPHICS_DEST_LOW
    sta.b LOCAL_DEST_PTR_LOW
    lda.w #SYSTEM_SCREEN_WORK_BUFFER_BANK
    sta.b LOCAL_DEST_PTR_BANK
    jsl C41A9E_DecompressAssetToLongDest
    lda.w #FAULTY_GAME_PAK_ARRANGEMENT
    sta.b LOCAL_SOURCE_PTR_LOW
    lda.w #ASSET_BANK_D8_WORD
    sta.b LOCAL_SOURCE_PTR_BANK
    lda.w #SYSTEM_SCREEN_TILEMAP_DEST_LOW
    sta.b LOCAL_DEST_PTR_LOW
    lda.w #SYSTEM_SCREEN_WORK_BUFFER_BANK
    sta.b LOCAL_DEST_PTR_BANK
    jsl C41A9E_DecompressAssetToLongDest
    jsl C40B75_RenderSystemErrorScreenAndHalt
    pld
    rtl
