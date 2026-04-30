; EarthBound C4 battle overlay script state helper prototype.
;
; Source-emission status:
; - Prototype level: build-candidate
; - C4 source-bank scaffold slice.
; - Derived from notes/bank-c4-cluster-map.md and direct ROM decode.
; - ROM byte range, SHA-1, and source signature are tracked by
;   build/c4-build-candidate-ranges.json.
;
; Source units covered:
; - C4:A67E..C4:A7B0 battle overlay script state initializer.

; ---------------------------------------------------------------------------
; External contracts used by this module

C0B0AA_ResetOrPrimeBattleOverlayRenderer      = $C0B0AA

; ---------------------------------------------------------------------------
; WRAM / data contracts

BATTLE_OVERLAY_SCRIPT_TABLE_BASE              = $CEDD41
BATTLE_OVERLAY_SCRIPT_TABLE_BANK              = $00CE
BATTLE_OVERLAY_OPEN_MODE0_SCRIPT              = $A5CE
BATTLE_OVERLAY_SCRIPT_ACTIVE                  = $AEC2
BATTLE_OVERLAY_SCRIPT_FRAME_COUNT             = $AEC3
BATTLE_OVERLAY_SCRIPT_REPEAT_COUNT            = $AEC4
BATTLE_OVERLAY_SCRIPT_FRAME_INDEX             = $AEC5
BATTLE_OVERLAY_LAYER_SELECT                   = $AEC6
BATTLE_OVERLAY_REVERSE_FLAG                   = $AEC7
BATTLE_OVERLAY_TILE_COUNT                     = $AEC8
BATTLE_OVERLAY_ANIMATION_PARITY               = $AEC9
BATTLE_OVERLAY_WORK_BYTE_AECA                 = $AECA
BATTLE_OVERLAY_WORK_BYTE_AECB                 = $AECB
BATTLE_OVERLAY_SCRIPT_PTR                     = $AECC
BATTLE_OVERLAY_SPECIAL_MODE                   = $AEE4
BATTLE_OVERLAY_SPECIAL_STEP                   = $AEE5
BATTLE_OVERLAY_SPECIAL_DELAY                  = $AEE6

; ---------------------------------------------------------------------------
; C4:A67E

; StartBattleOverlayScriptState
C4A67E_StartBattleOverlayScriptState:
    rep #$31
    phd
    pha
    tdc
    adc #$FFEF
    tcd
    pla
    stx $02
    sta $04

    lda $02
    and #$0002
    beq C4A69C_StartBattleOverlayScriptState_ClearLayerSelect
    sep #$20
    lda.b #$01
    sta.w BATTLE_OVERLAY_LAYER_SELECT
    bra C4A6A1_StartBattleOverlayScriptState_LayerSelectDone

C4A69C_StartBattleOverlayScriptState_ClearLayerSelect:
    sep #$20
    stz.w BATTLE_OVERLAY_LAYER_SELECT
C4A6A1_StartBattleOverlayScriptState_LayerSelectDone:
    rep #$20
    lda $02
    and #$0001
    beq C4A6B3_StartBattleOverlayScriptState_ClearReverseFlag
    sep #$20
    lda.b #$01
    sta.w BATTLE_OVERLAY_REVERSE_FLAG
    bra C4A6B8_StartBattleOverlayScriptState_ReverseDone

C4A6B3_StartBattleOverlayScriptState_ClearReverseFlag:
    sep #$20
    stz.w BATTLE_OVERLAY_REVERSE_FLAG
C4A6B8_StartBattleOverlayScriptState_ReverseDone:
    rep #$20
    lda $02
    and #$0004
    beq C4A6CA_StartBattleOverlayScriptState_DefaultTileCount
    sep #$20
    lda.b #$20
    sta.w BATTLE_OVERLAY_TILE_COUNT
    bra C4A6D1_StartBattleOverlayScriptState_TileCountDone

C4A6CA_StartBattleOverlayScriptState_DefaultTileCount:
    sep #$20
    lda.b #$1F
    sta.w BATTLE_OVERLAY_TILE_COUNT
C4A6D1_StartBattleOverlayScriptState_TileCountDone:
    lda.b #$01
    sta.w BATTLE_OVERLAY_SCRIPT_ACTIVE
    rep #$20
    lda #BATTLE_OVERLAY_SCRIPT_TABLE_BASE
    sta $06
    lda #BATTLE_OVERLAY_SCRIPT_TABLE_BANK
    sta $08
    lda $04
    asl
    asl
    sta $0F
    ldx $06
    stx $0A
    ldx $08
    stx $0C
    clc
    adc $0A
    sta $0A
    sep #$20
    lda [$0A]
    sta.w BATTLE_OVERLAY_SCRIPT_FRAME_COUNT
    ldy #BATTLE_OVERLAY_SCRIPT_REPEAT_COUNT
    rep #$20
    lda $0F
    inc
    inc
    ldx $06
    stx $0A
    ldx $08
    stx $0C
    clc
    adc $0A
    sta $0A
    sep #$20
    lda [$0A]
    sta.w $0000,y
    ldx #BATTLE_OVERLAY_SCRIPT_FRAME_INDEX
    rep #$20
    lda $0F
    inc
    clc
    adc $06
    sta $06
    sep #$20
    lda [$06]
    sta $0E
    sta.w $0000,x
    rep #$20
    lda.w BATTLE_OVERLAY_REVERSE_FLAG
    and #$00FF
    beq C4A748_StartBattleOverlayScriptState_FrameIndexReady
    sep #$20
    lda.w $0000,y
    sta $00
    lda $0E
    clc
    adc $00
    sta.w $0000,x

C4A748_StartBattleOverlayScriptState_FrameIndexReady:
    ldy #BATTLE_OVERLAY_SCRIPT_PTR
    rep #$20
    lda #$0000
    sta $06
    lda #$0000
    sta $08
    lda $06
    sta.w $0000,y
    lda $08
    sta.w $0002,y
    lda $04
    bne C4A779_StartBattleOverlayScriptState_NoDefaultOpenScript
    lda #BATTLE_OVERLAY_OPEN_MODE0_SCRIPT
    sta $06
    lda #$00C4
    sta $08
    lda $06
    sta.w $0000,y
    lda $08
    sta.w $0002,y

C4A779_StartBattleOverlayScriptState_NoDefaultOpenScript:
    sep #$20
    stz.w BATTLE_OVERLAY_ANIMATION_PARITY
    stz.w BATTLE_OVERLAY_WORK_BYTE_AECA
    lda.b #$01
    sta.w BATTLE_OVERLAY_WORK_BYTE_AECB
    rep #$20
    lda $02
    and #$0080
    beq C4A7A5_StartBattleOverlayScriptState_ClearSpecialMode
    lda $04
    sep #$20
    sta.w BATTLE_OVERLAY_SPECIAL_MODE
    lda.b #$04
    sta.w BATTLE_OVERLAY_SCRIPT_FRAME_COUNT
    stz.w BATTLE_OVERLAY_SPECIAL_STEP
    lda.b #$08
    sta.w BATTLE_OVERLAY_SPECIAL_DELAY
    bra C4A7AA_StartBattleOverlayScriptState_ResetRenderer

C4A7A5_StartBattleOverlayScriptState_ClearSpecialMode:
    sep #$20
    stz.w BATTLE_OVERLAY_SPECIAL_MODE
C4A7AA_StartBattleOverlayScriptState_ResetRenderer:
    jsl C0B0AA_ResetOrPrimeBattleOverlayRenderer
    pld
    rtl
