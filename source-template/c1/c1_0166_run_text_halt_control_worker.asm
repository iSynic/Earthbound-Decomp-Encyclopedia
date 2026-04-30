; EarthBound C1 shared text halt/control worker.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Hand-polished from tools/emit_linear_source_module.py output, then
;   intended for byte-equivalence validation.
;
; Source unit covered:
; - C1:0166..C1:02D0 RunTextHaltControlWorker

; ---------------------------------------------------------------------------
; External contracts used by this module

C100FE_WaitForTextPromptOrInputGate  = $00FE
C08616_QueueVramTransfer             = $C08616
C08FF7_ResolveIndexedPointerOffset   = $C08FF7
C12DD5_TickWindowTextSystem          = $C12DD5
C12E42_TickPromptWaitFrame           = $C12E42
C3E4CA_ClearInstantPrinting          = $C3E4CA
EF0256_UpdateBattleTextWaitState     = $EF0256
EF026E_FinalizeTextHaltControlWorker = $EF026E

DebugControlModeFlag      = $436C
ControllerButtonsPressed  = $006D
ActiveWindowFocus         = $8958
WindowDescriptorIndexTable = $88E4
WindowDescriptorTable     = $8650
WindowDescriptorSize      = $0052

TextInputLockFlag         = $9645
TextPromptWaitTicks       = $964B
BattleTextDisplayMode     = $964D

PromptAcceptMask          = $A0A0
DebugUnlockChordMask      = $8010
NoPromptMode              = $0000
PromptTileUploadBytes     = $0002

PromptTilePointDownBig    = $E416
PromptTilePointDownSmall  = $E418
PromptTileWaitPair        = $E41A
PromptTileBank            = $00C3
TextWindowVramBase        = $7C20

SavedMode                 = $12
SavedCallerX              = $14
ActiveWindowRecord        = $02
PromptRowOffset           = $04
PromptTilePointerLo       = $0E
PromptTilePointerBank     = $10

; ---------------------------------------------------------------------------
; C1:0166

C10166_RunTextHaltControlWorker:
    rep #$31
    phd
    pha
    tdc
    adc.w #$FFEA
    tcd
    pla
    stx SavedCallerX
    tay
    sty SavedMode
    bra C1018C_TestTextInputLock

C10177_CheckDebugUnlockChord:
    lda DebugControlModeFlag
    beq C1018C_TestTextInputLock

    lda ControllerButtonsPressed
    and.w #DebugUnlockChordMask
    cmp.w #DebugUnlockChordMask
    bne C1018C_TestTextInputLock

    stz TextInputLockFlag
    bra C10191_ServiceWindowTextState

C1018C_TestTextInputLock:
    lda TextInputLockFlag
    bne C10177_CheckDebugUnlockChord

C10191_ServiceWindowTextState:
    jsl C3E4CA_ClearInstantPrinting
    jsl C12DD5_TickWindowTextSystem
    ldx SavedCallerX
    bne C101B0_ServiceBattleTextWaitState

    lda BattleTextDisplayMode
    beq C101B0_ServiceBattleTextWaitState

    lda TextPromptWaitTicks
    beq C101B0_ServiceBattleTextWaitState

    lda.w #NoPromptMode
    jsr C100FE_WaitForTextPromptOrInputGate
    jmp.w C102CE_ReturnTextHaltControlWorker

C101B0_ServiceBattleTextWaitState:
    lda BattleTextDisplayMode
    beq C101B9_ResolveActiveWindowRecord

    jsl EF0256_UpdateBattleTextWaitState

C101B9_ResolveActiveWindowRecord:
    lda ActiveWindowFocus
    asl A
    tax
    lda WindowDescriptorIndexTable,X
    ldy.w #WindowDescriptorSize
    jsl C08FF7_ResolveIndexedPointerOffset
    clc
    adc.w #WindowDescriptorTable
    sta ActiveWindowRecord
    ldy SavedMode
    bne C101E3_ShowPromptPointDownBig

    bra C101D8_WaitForPromptAcceptNoTile

C101D4_TickNoTilePromptWait:
    jsl C12E42_TickPromptWaitFrame

C101D8_WaitForPromptAcceptNoTile:
    lda ControllerButtonsPressed
    and.w #PromptAcceptMask
    beq C101D4_TickNoTilePromptWait

    jmp.w C102CA_FinalizeTextHaltControlWorker

C101E3_ShowPromptPointDownBig:
    lda.w #PromptTilePointDownBig
    sta PromptTilePointerLo
    lda.w #PromptTileBank
    sta PromptTilePointerBank
    ldx ActiveWindowRecord
    lda $0008,X
    ldx ActiveWindowRecord
    clc
    adc $000C,X
    asl A
    asl A
    asl A
    asl A
    asl A
    sta PromptRowOffset
    ldx ActiveWindowRecord
    lda $0006,X
    ldx ActiveWindowRecord
    clc
    adc $000A,X
    clc
    adc PromptRowOffset
    clc
    adc.w #TextWindowVramBase
    tay
    ldx.w #PromptTileUploadBytes
    sep #$20
    lda.b #$00
    jsl C08616_QueueVramTransfer
    ldx.w #$000F
    stx SavedMode
    bra C10235_TestPointDownBigWaitCount

C10224_WaitPointDownBigOrAccept:
    lda ControllerButtonsPressed
    and.w #PromptAcceptMask
    bne C1028E_ShowPromptWaitPair

    jsl C12E42_TickPromptWaitFrame
    ldx SavedMode
    dex
    stx SavedMode

C10235_TestPointDownBigWaitCount:
    bne C10224_WaitPointDownBigOrAccept

    lda.w #PromptTilePointDownSmall
    sta PromptTilePointerLo
    lda.w #PromptTileBank
    sta PromptTilePointerBank
    ldx ActiveWindowRecord
    lda $0008,X
    ldx ActiveWindowRecord
    clc
    adc $000C,X
    asl A
    asl A
    asl A
    asl A
    asl A
    sta PromptRowOffset
    ldx ActiveWindowRecord
    lda $0006,X
    ldx ActiveWindowRecord
    clc
    adc $000A,X
    clc
    adc PromptRowOffset
    clc
    adc.w #TextWindowVramBase
    tay
    ldx.w #PromptTileUploadBytes
    sep #$20
    lda.b #$00
    jsl C08616_QueueVramTransfer
    ldx.w #$000A
    stx SavedMode
    bra C10289_TestPointDownSmallWaitCount

C10278_WaitPointDownSmallOrAccept:
    lda ControllerButtonsPressed
    and.w #PromptAcceptMask
    bne C102CA_FinalizeTextHaltControlWorker

    jsl C12E42_TickPromptWaitFrame
    ldx SavedMode
    dex
    stx SavedMode

C10289_TestPointDownSmallWaitCount:
    bne C10278_WaitPointDownSmallOrAccept

    jmp.w C101E3_ShowPromptPointDownBig

C1028E_ShowPromptWaitPair:
    lda.w #PromptTileWaitPair
    sta PromptTilePointerLo
    lda.w #PromptTileBank
    sta PromptTilePointerBank
    ldx ActiveWindowRecord
    lda $0008,X
    ldx ActiveWindowRecord
    clc
    adc $000C,X
    asl A
    asl A
    asl A
    asl A
    asl A
    pha
    ldx ActiveWindowRecord
    lda $0006,X
    ldx ActiveWindowRecord
    clc
    adc $000A,X
    ply
    sty ActiveWindowRecord
    clc
    adc ActiveWindowRecord
    clc
    adc.w #TextWindowVramBase
    tay
    ldx.w #PromptTileUploadBytes
    sep #$20
    lda.b #$00
    jsl C08616_QueueVramTransfer

C102CA_FinalizeTextHaltControlWorker:
    jsl EF026E_FinalizeTextHaltControlWorker

C102CE_ReturnTextHaltControlWorker:
    pld
    rts
