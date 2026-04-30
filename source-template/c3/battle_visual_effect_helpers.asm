; EarthBound C3 battle visual effect helper prototype.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Assembler contract: pilot-ready
; - Assembler-ready pilot with segmented source/data coverage; not yet linked
;   into a full assembler ROM build.
; - Derived from notes/c3-source-emission-plan.md and the source contracts linked
;   below.
; - Build-candidate conventions are documented in
;   notes/c3-build-candidate-source-conventions.md.
; - Original instruction flow is preserved for the helper code while adjacent
;   C3 visual tables remain explicit data dependencies outside this source unit.
; - The C3:F67D row-wrap helper's return-state dependency on C0:8616 is covered
;   by source signature validation.
; - ROM byte ranges, source segments, the internal data gap, SHA-1 values, and
;   source signature are tracked by build/c3-build-candidate-ranges.json and
;   build/c3-source-signature-validation.json.
;
; Source units covered:
; - C3:F5F9..C3:F67D QueueVisualTileRowsLinear
; - C3:F67D..C3:F705 QueueVisualTileRowsWrapped
; - C3:F705..C3:F7FB QueueVisualTileBlockFromStream
; - C3:F7FB..C3:F819 QueueFixedEfEb3dVisualTileBlock
; - C3:F981..C3:FAC9 DispatchBattleVisualEffectToken
; - C3:FAC9..C3:FB09 DispatchBattleActorVisualEffectToken
; - C3:FB09..C3:FB1F CheckCurrentBattleActorVisualFlag
;
; Evidence:
; - notes/c3-window-and-battle-visual-unknown-tail-e7e3-f981.md
; - notes/c3-battle-visual-effect-dispatch-source-contract-f981.md
; - notes/c3-source-emission-plan.md

; ---------------------------------------------------------------------------
; External contracts used by this module

C08616_QueueVramTransfer_FromDpSource      = $C08616
C0B01A_SetFixedColourRgbComponents        = $C0B01A
C0B039_SetColourAddSubModeRegisters       = $C0B039
C2E116_DispatchBaseBattleVisualEffectToken = $C2E116
C2DE0F_DimLoadedBattleBgPalettesAndUpload = $C2DE0F
C4A67E_StartBattleOverlayScriptState      = $C4A67E

; C0:8616 QueueVramTransfer_FromDpSource
; C0:B01A ApplyFixedColourComponents
; C0:B039 ApplyFixedColourWindowOrMask
; C2:E116 DispatchBaseBattleVisualEffectToken
; C2:DE0F PrepareBattleVisualColourEffect
; C4:A67E ApplyBattleVisualEffectDuration

; ---------------------------------------------------------------------------
; Local data contracts and WRAM fields

VISUAL_TRANSFER_COLUMN          = $9F7A
VISUAL_TRANSFER_ROW             = $9F7C
VISUAL_TRANSFER_ROWS            = $9F7E
VISUAL_TRANSFER_COLUMNS         = $9F80
VISUAL_TRANSFER_SOURCE_STRIDE   = $9F82
VISUAL_TRANSFER_VRAM_BASE       = $9F84
VISUAL_TRANSFER_SOURCE_LOW      = $9F86
VISUAL_TRANSFER_SOURCE_BANK     = $9F88

BATTLE_VISUAL_TOKEN_23_TABLE_LOW = $F951
BATTLE_VISUAL_TOKEN_31_TABLE_LOW = $F972
BATTLE_VISUAL_TOKEN_TABLE_BANK   = $00C3
BATTLE_VISUAL_TOKEN_ROW_SIZE     = $0003

BATTLE_VISUAL_WOBBLE_TIMER      = $AD92
BATTLE_VISUAL_SHAKE_TIMER       = $AD94
CURRENT_BATTLE_ACTOR_RECORD     = $A972
CURRENT_BATTLE_ACTOR_RECORD_ALT = $A970

FIXED_EF_EB3D_VISUAL_LOW        = $EB3D
FIXED_EF_EB3D_VISUAL_BANK       = $00EF

; Adjacent data that should stay explicit when this module becomes real source:
; - C3:F819 BattleSwirlOverlayMode2Script
; - C3:F951 BattleVisualToken23To2dColourTriples, 11 rows of 3 bytes
; - C3:F972 BattleVisualToken31To35ColourTriples, 5 rows of 3 bytes

; ---------------------------------------------------------------------------
; C3:F5F9..C3:F67D QueueVisualTileRowsLinear

; QueueVisualTileRowsLinear
;
; Entry:
;   Uses VISUAL_TRANSFER_* state initialized by QueueVisualTileBlockFromStream.
;
; Behavior:
;   Queues each row linearly through C0:8616, advancing source by
;   VISUAL_TRANSFER_SOURCE_STRIDE and wrapping row index at 32.
C3F5F9_QueueVisualTileRowsLinear:
    rep #$31
    phd
    tdc
    adc #$FFE8
    tcd
    lda #$0000
    sta $04
    lda VISUAL_TRANSFER_ROWS
    asl A
    sta $16
    lda #$0000
    sta $02
    sta $14
    bra C3F674_QueueVisualTileRowsLinear_TestLoop

C3F615_QueueVisualTileRowsLinear_QueueRow:
    lda VISUAL_TRANSFER_COLUMN
    and #$001F
    sta $02
    lda VISUAL_TRANSFER_ROW
    asl A
    asl A
    asl A
    asl A
    asl A
    clc
    adc VISUAL_TRANSFER_VRAM_BASE
    clc
    adc $02
    sta $12

    lda VISUAL_TRANSFER_SOURCE_LOW
    sta $06
    lda VISUAL_TRANSFER_SOURCE_BANK
    sta $08
    lda $04
    asl A
    clc
    adc $06
    sta $06
    sta $0E
    lda $08
    sta $10

    lda $12
    tay
    ldx $16
    sep #$20
    lda #$00
    jsl C08616_QueueVramTransfer_FromDpSource

    lda $04
    clc
    adc VISUAL_TRANSFER_SOURCE_STRIDE
    sta $04
    ldx VISUAL_TRANSFER_ROW
    inx
    stx VISUAL_TRANSFER_ROW
    cpx #$0020
    bne C3F66A_QueueVisualTileRowsLinear_CountRow
    stz VISUAL_TRANSFER_ROW

C3F66A_QueueVisualTileRowsLinear_CountRow:
    lda $14
    sta $02
    inc $02
    lda $02
    sta $14

C3F674_QueueVisualTileRowsLinear_TestLoop:
    lda $02
    cmp VISUAL_TRANSFER_COLUMNS
    bcc C3F615_QueueVisualTileRowsLinear_QueueRow
    pld
    rts

; ---------------------------------------------------------------------------
; C3:F67D..C3:F705 QueueVisualTileRowsWrapped

; QueueVisualTileRowsWrapped
;
; Entry:
;   Uses VISUAL_TRANSFER_* state initialized by QueueVisualTileBlockFromStream.
;
; Behavior:
;   Queues rows while advancing the source pointer and toggling the destination
;   $0400 page bit when column/page wrapping crosses a boundary.
C3F67D_QueueVisualTileRowsWrapped:
    rep #$31
    phd
    tdc
    adc #$FFEC
    tcd
    lda VISUAL_TRANSFER_COLUMNS
    asl A
    sta $04
    lda #$0000
    sta $02
    bra C3F6FC_QueueVisualTileRowsWrapped_TestLoop

C3F692_QueueVisualTileRowsWrapped_QueueRow:
    lda VISUAL_TRANSFER_ROW
    asl A
    asl A
    asl A
    asl A
    asl A
    clc
    adc VISUAL_TRANSFER_VRAM_BASE
    clc
    adc VISUAL_TRANSFER_COLUMN
    sta $12
    inc VISUAL_TRANSFER_COLUMN

    lda VISUAL_TRANSFER_SOURCE_LOW
    sta $06
    lda VISUAL_TRANSFER_SOURCE_BANK
    sta $08
    lda $06
    sta $0E
    lda $08
    sta $10
    lda $12
    tay
    ldx $04
    sep #$20
    lda #$00
    jsl C08616_QueueVramTransfer_FromDpSource

    ; C0:8616 returns in the 16-bit accumulator state expected below.
    lda VISUAL_TRANSFER_SOURCE_LOW
    sta $06
    lda VISUAL_TRANSFER_SOURCE_BANK
    sta $08
    lda VISUAL_TRANSFER_SOURCE_STRIDE
    asl A
    clc
    adc $06
    sta $06
    sta VISUAL_TRANSFER_SOURCE_LOW
    lda $08
    sta VISUAL_TRANSFER_SOURCE_BANK

    lda VISUAL_TRANSFER_COLUMN
    cmp #$0020
    beq C3F6F1_QueueVisualTileRowsWrapped_TogglePage
    lda VISUAL_TRANSFER_COLUMN
    cmp #$0040
    bne C3F6FA_QueueVisualTileRowsWrapped_NextRow

C3F6F1_QueueVisualTileRowsWrapped_TogglePage:
    lda VISUAL_TRANSFER_VRAM_BASE
    eor #$0400
    sta VISUAL_TRANSFER_VRAM_BASE

C3F6FA_QueueVisualTileRowsWrapped_NextRow:
    inc $02

C3F6FC_QueueVisualTileRowsWrapped_TestLoop:
    lda $02
    cmp VISUAL_TRANSFER_ROWS
    bcc C3F692_QueueVisualTileRowsWrapped_QueueRow
    pld
    rts

; ---------------------------------------------------------------------------
; C3:F705..C3:F7FB QueueVisualTileBlockFromStream

; QueueVisualTileBlockFromStream
;
; Entry:
;   caller DP $28/$2A = long source pointer
;   A = destination/control low word
;   X = input column/offset
;
; Behavior:
;   Reads the two-byte stream header, initializes VISUAL_TRANSFER_* state, and
;   chooses the linear or wrapped row queue path.
C3F705_QueueVisualTileBlockFromStream:
    rep #$31
    phd
    pha
    tdc
    adc #$FFE6
    tcd
    pla
    sta $18
    lda $28
    sta $06
    lda $2A
    sta $08
    lda $06
    sta $14
    lda $08
    sta $16
    inc $06
    inc $06
    lda $06
    sta VISUAL_TRANSFER_SOURCE_LOW
    lda $08
    sta VISUAL_TRANSFER_SOURCE_BANK

    lda $18
    and #$003F
    tay
    sty $12
    sty VISUAL_TRANSFER_COLUMN
    txa
    and #$001F
    sta $02
    sta $10
    lda $02
    sta VISUAL_TRANSFER_ROW
    tya
    and #$001F
    beq C3F752_QueueVisualTileBlockFromStream_UseLowVramPage
    ldx #$3C00
    bra C3F755_QueueVisualTileBlockFromStream_StoreVramPage

C3F752_QueueVisualTileBlockFromStream_UseLowVramPage:
    ldx #$3800

C3F755_QueueVisualTileBlockFromStream_StoreVramPage:
    stx VISUAL_TRANSFER_VRAM_BASE
    lda $14
    sta $06
    lda $16
    sta $08
    lda [$06]
    xba
    and #$00FF
    sta $18
    tax
    stx $0E
    stx VISUAL_TRANSFER_ROWS
    lda [$06]
    and #$00FF
    sta $04
    sta VISUAL_TRANSFER_COLUMNS

    lda $18
    sta $02
    tya
    clc
    adc $02
    and #$FFE0
    sta $04
    tya
    and #$FFE0
    cmp $04
    bne C3F797_QueueVisualTileBlockFromStream_SplitAtPage

    lda $18
    sta VISUAL_TRANSFER_SOURCE_STRIDE
    jsr C3F5F9_QueueVisualTileRowsLinear
    bra C3F7F9_QueueVisualTileBlockFromStream_Return

C3F797_QueueVisualTileBlockFromStream_SplitAtPage:
    lda $18
    sta $04
    ldy $12
    tya
    clc
    adc $04
    and #$FFE0
    sec
    sbc VISUAL_TRANSFER_COLUMN
    sta VISUAL_TRANSFER_ROWS
    lda $18
    sta VISUAL_TRANSFER_SOURCE_STRIDE
    jsr C3F5F9_QueueVisualTileRowsLinear

    lda VISUAL_TRANSFER_VRAM_BASE
    eor #$0400
    sta VISUAL_TRANSFER_VRAM_BASE
    lda VISUAL_TRANSFER_SOURCE_LOW
    sta $06
    lda VISUAL_TRANSFER_SOURCE_BANK
    sta $08
    lda VISUAL_TRANSFER_ROWS
    asl A
    clc
    adc $06
    sta $06
    sta VISUAL_TRANSFER_SOURCE_LOW
    lda $08
    sta VISUAL_TRANSFER_SOURCE_BANK
    stz VISUAL_TRANSFER_COLUMN
    lda $10
    sta $02
    sta VISUAL_TRANSFER_ROW
    lda $18
    sec
    sbc VISUAL_TRANSFER_ROWS
    sta $18
    cmp #$0020
    bcs C3F797_QueueVisualTileBlockFromStream_SplitAtPage
    sta VISUAL_TRANSFER_ROWS
    ldx $0E
    stx VISUAL_TRANSFER_SOURCE_STRIDE
    jsr C3F5F9_QueueVisualTileRowsLinear

C3F7F9_QueueVisualTileBlockFromStream_Return:
    pld
    rtl

; ---------------------------------------------------------------------------
; C3:F7FB..C3:F819 QueueFixedEfEb3dVisualTileBlock

; QueueFixedEfEb3dVisualTileBlock
;
; Entry:
;   No meaningful caller input.
;
; Behavior:
;   Queues the fixed EF:EB3D visual tile block using C3:F705 with X=$001F and
;   A=$039E.
C3F7FB_QueueFixedEfEb3dVisualTileBlock:
    rep #$31
    phd
    tdc
    adc #$FFEE
    tcd
    lda #FIXED_EF_EB3D_VISUAL_LOW
    sta $0E
    lda #FIXED_EF_EB3D_VISUAL_BANK
    sta $10
    ldx #$001F
    lda #$039E
    jsl C3F705_QueueVisualTileBlockFromStream
    pld
    rtl

; ---------------------------------------------------------------------------
; C3:F981..C3:FAC9 DispatchBattleVisualEffectToken

; DispatchBattleVisualEffectToken
;
; Entry:
;   A = battle visual/effect token.
;
; Return:
;   No meaningful numeric result; caller-facing result belongs to C3:FAC9.

; ---------------------------------------------------------------------------
; C3:F819

C3F819_BattleVisualScriptAndOffsetTableBlock:
    ; data bytes: C3:F819..C3:F981
    db $3C,$00,$80,$00,$70,$00,$00,$98,$00,$7F,$00,$00,$00,$00,$20,$FF
    db $49,$FF,$FC,$FF,$FD,$FF,$3C,$00,$80,$00,$70,$00,$00,$80,$00,$80
    db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$3C,$00,$80,$00
    db $70,$00,$00,$80,$00,$80,$00,$00,$00,$00,$38,$FF,$50,$FF,$FC,$FF
    db $FD,$FF,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00
    db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$80,$00,$00,$01,$80,$01
    db $00,$08,$80,$08,$00,$09,$80,$09,$00,$10,$80,$10,$00,$11,$80,$11
    db $00,$18,$80,$18,$00,$19,$80,$19,$00,$20,$80,$20,$00,$21,$80,$21
    db $00,$28,$80,$28,$00,$29,$80,$29,$00,$30,$80,$30,$00,$31,$80,$31
    db $00,$38,$80,$38,$00,$39,$80,$39,$00,$00,$04,$00,$08,$00,$0C,$00
    db $40,$00,$44,$00,$48,$00,$4C,$00,$80,$00,$84,$00,$88,$00,$8C,$00
    db $C0,$00,$C4,$00,$C8,$00,$CC,$00,$00,$01,$04,$01,$08,$01,$0C,$01
    db $40,$01,$44,$01,$48,$01,$4C,$01,$80,$01,$84,$01,$88,$01,$8C,$01
    db $C0,$01,$C4,$01,$C8,$01,$CC,$01,$00,$00,$9B,$77,$9B,$77,$9B,$77
    db $9B,$77,$9B,$77,$9B,$77,$9B,$77,$9B,$77,$9B,$77,$9B,$77,$9B,$77
    db $9B,$77,$9B,$77,$9B,$77,$AF,$35,$00,$00,$BF,$0B,$BF,$0B,$BF,$0B
    db $BF,$0B,$BF,$0B,$BF,$0B,$BF,$0B,$BF,$0B,$BF,$0B,$BF,$0B,$BF,$0B
    db $BF,$0B,$BF,$0B,$BF,$0B,$7F,$2C,$00,$00,$00,$00,$00,$00,$00,$00
    db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00
    db $00,$00,$00,$00,$00,$00,$AF,$35,$1F,$00,$00,$12,$06,$00,$10,$06
    db $00,$00,$00,$0A,$1D,$1D,$1D,$00,$00,$1F,$1A,$0E,$0E,$00,$0A,$04
    db $12,$12,$12,$12,$12,$1F,$1F,$1F,$0B,$0F,$0F,$0F,$0F,$0F,$00,$0F
    db $07,$0F,$00,$00,$0F,$1F,$00,$0C

C3F981_DispatchBattleVisualEffectToken:
    rep #$31
    phd
    pha
    tdc
    adc #$FFEE
    tcd
    pla
    sta $02
    cmp #$0023
    bcs C3F99B_DispatchBattleVisualEffectToken_TestColour23Upper
    lda $02
    jsl C2E116_DispatchBaseBattleVisualEffectToken
    jmp C3FAC7_ReturnFromBattleVisualEffectTokenDispatch

C3F99B_DispatchBattleVisualEffectToken_TestColour23Upper:
    lda $02
    cmp #$002E
    bcs C3FA0F_DispatchBattleVisualEffectToken_TestTimedTokens

; ApplyBattleVisualToken23To2dColourEffect
;
; Token range:
;   $23..$2D, indexing C3:F951 3-byte colour triples.
C3F9A2_ApplyBattleVisualToken23To2dColourEffect:
    jsl C2DE0F_DimLoadedBattleBgPalettesAndUpload
    lda #BATTLE_VISUAL_TOKEN_23_TABLE_LOW
    sta $06
    lda #BATTLE_VISUAL_TOKEN_TABLE_BANK
    sta $08
    lda $02
    sec
    sbc #$0023
    sta $04
    asl A
    adc $04
    sta $10
    inc A
    inc A
    ldx $06
    stx $0A
    ldx $08
    stx $0C
    clc
    adc $0A
    sta $0A
    lda [$0A]
    and #$00FF
    tay
    lda $10
    inc A
    ldx $06
    stx $0A
    ldx $08
    stx $0C
    clc
    adc $0A
    sta $0A
    lda [$0A]
    and #$00FF
    tax
    lda $10
    clc
    adc $06
    sta $06
    lda [$06]
    and #$00FF
    jsl C0B01A_SetFixedColourRgbComponents
    ldx #$003F
    lda #$0010
    jsl C0B039_SetColourAddSubModeRegisters
    ldx #$0007
    lda #$0005
    jsl C4A67E_StartBattleOverlayScriptState
    jmp C3FAC7_ReturnFromBattleVisualEffectTokenDispatch

C3FA0F_DispatchBattleVisualEffectToken_TestTimedTokens:
    lda $02
    cmp #$0031
    bcs C3FA40_DispatchBattleVisualEffectToken_TestColour31Upper
    lda $02
    inc A
    cmp #$002F
    beq C3FA2E_DispatchBattleVisualEffectToken_SetWobbleTimer
    cmp #$0030
    beq C3FA37_DispatchBattleVisualEffectToken_SetShakeTimer
    cmp #$0031
    bne C3FA2B_DispatchBattleVisualEffectToken_NoOpToken
    jmp C3FAC7_ReturnFromBattleVisualEffectTokenDispatch

C3FA2B_DispatchBattleVisualEffectToken_NoOpToken:
    jmp C3FAC7_ReturnFromBattleVisualEffectTokenDispatch

C3FA2E_DispatchBattleVisualEffectToken_SetWobbleTimer:
    lda #$0090
    sta BATTLE_VISUAL_WOBBLE_TIMER
    jmp C3FAC7_ReturnFromBattleVisualEffectTokenDispatch

C3FA37_DispatchBattleVisualEffectToken_SetShakeTimer:
    lda #$012C
    sta BATTLE_VISUAL_SHAKE_TIMER
    jmp C3FAC7_ReturnFromBattleVisualEffectTokenDispatch

C3FA40_DispatchBattleVisualEffectToken_TestColour31Upper:
    lda $02
    cmp #$0036
    bcc C3FA4A_ApplyBattleVisualToken31To35ColourEffect
    jmp C3FAC7_ReturnFromBattleVisualEffectTokenDispatch

; ApplyBattleVisualToken31To35ColourEffect
;
; Token range:
;   $31..$35, indexing C3:F972 3-byte colour triples.
C3FA4A_ApplyBattleVisualToken31To35ColourEffect:
    jsl C2DE0F_DimLoadedBattleBgPalettesAndUpload
    lda #BATTLE_VISUAL_TOKEN_31_TABLE_LOW
    sta $06
    lda #BATTLE_VISUAL_TOKEN_TABLE_BANK
    sta $08
    lda $02
    sec
    sbc #$0031
    sta $04
    asl A
    adc $04
    sta $0E
    inc A
    inc A
    ldx $06
    stx $0A
    ldx $08
    stx $0C
    clc
    adc $0A
    sta $0A
    lda [$0A]
    and #$00FF
    tay
    lda $0E
    inc A
    ldx $06
    stx $0A
    ldx $08
    stx $0C
    clc
    adc $0A
    sta $0A
    lda [$0A]
    and #$00FF
    tax
    lda $0E
    clc
    adc $06
    sta $06
    lda [$06]
    and #$00FF
    jsl C0B01A_SetFixedColourRgbComponents
    ldx #$003F
    lda #$0010
    jsl C0B039_SetColourAddSubModeRegisters
    lda $02
    cmp #$0035
    bcs C3FABD_ApplyBattleVisualToken31To35ColourEffect_LongDuration
    ldx #$0005
    lda #$0004
    jsl C4A67E_StartBattleOverlayScriptState
    bra C3FAC7_ReturnFromBattleVisualEffectTokenDispatch

C3FABD_ApplyBattleVisualToken31To35ColourEffect_LongDuration:
    ldx #$0004
    lda #$0002
    jsl C4A67E_StartBattleOverlayScriptState

; ReturnFromBattleVisualEffectTokenDispatch
C3FAC7_ReturnFromBattleVisualEffectTokenDispatch:
    pld
    rts

; ---------------------------------------------------------------------------
; C3:FAC9..C3:FB09 DispatchBattleActorVisualEffectToken

; DispatchBattleActorVisualEffectToken
;
; Entry:
;   A/X/Y carry the caller's explicit and secondary battle visual tokens.
;
; Return:
;   A = 1 when actor state chooses the secondary/suppressed path.
;   A = 0 when actor byte +$0E is clear and the explicit token was dispatched.
C3FAC9_DispatchBattleActorVisualEffectToken:
    rep #$31
    phd
    pha
    tdc
    adc #$FFF0
    tcd
    pla
    txy
    tax
    stx $0E
    ldx CURRENT_BATTLE_ACTOR_RECORD
    lda $000F,X
    and #$00FF
    cmp #$00D5
    bne C3FAEA_DispatchBattleActorVisualEffectToken_TestActorVisualFlag
    lda #$0001
    bra C3FB07_DispatchBattleActorVisualEffectToken_Return

C3FAEA_DispatchBattleActorVisualEffectToken_TestActorVisualFlag:
    ldx CURRENT_BATTLE_ACTOR_RECORD
    lda $000E,X
    and #$00FF
    bne C3FB00_DispatchBattleActorVisualEffectToken_DispatchSecondary
    ldx $0E
    txa
    jsr C3F981_DispatchBattleVisualEffectToken
    lda #$0000
    bra C3FB07_DispatchBattleActorVisualEffectToken_Return

C3FB00_DispatchBattleActorVisualEffectToken_DispatchSecondary:
    tya
    jsr C3F981_DispatchBattleVisualEffectToken
    lda #$0001

C3FB07_DispatchBattleActorVisualEffectToken_Return:
    pld
    rtl

; ---------------------------------------------------------------------------
; C3:FB09..C3:FB1F CheckCurrentBattleActorVisualFlag

; CheckCurrentBattleActorVisualFlag
;
; Entry:
;   No meaningful caller input.
;
; Return:
;   A = 1 if current alternate battle actor record byte +$0E is nonzero, else 0.
;
; Boundary note:
;   The legacy reference labels C3:FB1F as DATA_C3FB1F immediately after this
;   helper's RTL, so the source-emission plan treats C3:FB09..C3:FB1F as the
;   final battle-visual source slice and keeps following bytes as data/frontier
;   material.
C3FB09_CheckCurrentBattleActorVisualFlag:
    rep #$31
    ldx CURRENT_BATTLE_ACTOR_RECORD_ALT
    lda $000E,X
    and #$00FF
    bne C3FB1B_CheckCurrentBattleActorVisualFlag_ReturnTrue
    lda #$0000
    bra C3FB1E_CheckCurrentBattleActorVisualFlag_Return

C3FB1B_CheckCurrentBattleActorVisualFlag_ReturnTrue:
    lda #$0001

C3FB1E_CheckCurrentBattleActorVisualFlag_Return:
    rtl
