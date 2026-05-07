; EarthBound C4 landing display asset stream helper prototype.
;
; Source-emission status:
; - Prototype level: build-candidate
; - C4 source-bank scaffold slice.
; - Derived from notes/landing-display-assembly-cluster-c007b6-c4b26b.md and
;   the legacy routine macro disassembly.
; - ROM byte range, SHA-1, and source signature are tracked by
;   build/c4-build-candidate-ranges.json.
;
; Source units covered:
; - C4:B1B8..C4:B26B landing-display asset subpiece transfer helper.
; - C4:B26B..C4:B329 landing-display stream/child-anchor initializer.

; ---------------------------------------------------------------------------
; External contracts used by this module

DATA_EF133F                                   = $EF133F
DATA_C40E31                                   = $C40E31
DATA_C40E32                                   = $C40E32
DATA_C40EB0                                   = $C40EB0
DATA_C40EE4                                   = $C40EE4
DATA_C40EF0                                   = $C40EF0
DATA_C40F04                                   = $C40F04
C08616_TransferBlockToVramOrBuffer           = $C08616

; ---------------------------------------------------------------------------
; Landing-display asset stream contracts

LandingSubpieceDescriptorPointerTable        = $EF133F
LandingStreamDescriptorCountByte             = $C40E31
LandingStreamDescriptorTable                 = $C40E32
LandingStreamGroup2f6aSource                 = $C40EB0
LandingStreamGroup2eb6Source                 = $C40EE4
LandingStreamGroup301eSource                 = $C40EF0
LandingStreamGroup30d2Source                 = $C40F04
LandingNoSubpieceSentinel                    = $00FF
LandingDescriptorBankOffset                  = $0002
LandingSubpieceLengthOffset                  = $0001
LandingSubpieceSourceBankOffset              = $0008
LandingSubpieceEntryListOffset               = $0009
LandingSubpiecePointerAlignmentMask          = $FFFE
LandingSubpieceSecondPlaneVramOffset         = $0100
LandingVramTransferFlagsNone                 = $00
LandingStreamInitialVramDestination          = $5600
LandingStreamDescriptorFirstIndex            = $0000
LandingStreamDescriptorBytes                 = $0004
LandingStreamFirstSubpieceOffset             = $0002
LandingStreamSecondSubpieceOffset            = $0003
LandingStreamPointerSlotCount                = $001E
LandingStreamGroup2eb6Table                  = $2EB6
LandingStreamGroup2f6aTable                  = $2F6A
LandingStreamGroup301eTable                  = $301E
LandingStreamGroup30d2Table                  = $30D2
LowByteMask                                  = $00FF

; ---------------------------------------------------------------------------
; C4:B1B8

; TransferLandingDisplayAssetSubpiecePair
C4B1B8_TransferLandingDisplayAssetSubpiecePair:
	REP.b #$31
	PHD
	PHA
	TDC
	ADC.w #$FFE8
	TCD
	PLA
	STY.b $16
	STA.b $04
	CPY.w #LandingNoSubpieceSentinel
	BNE.b C4B1D0_TransferLandingDisplayAssetSubpiecePair_LoadDescriptor
	LDA.b $04
	JMP.w C4B269_TransferLandingDisplayAssetSubpiecePair_Return

C4B1D0_TransferLandingDisplayAssetSubpiecePair_LoadDescriptor:
	LDA.w #LandingSubpieceDescriptorPointerTable
	STA.b $0A
	LDA.w #LandingSubpieceDescriptorPointerTable>>16
	STA.b $0C
	TXA
	ASL
	ASL
	CLC
	ADC.b $0A
	STA.b $0A
	LDY.w #LandingDescriptorBankOffset
	LDA.b [$0A],Y
	TAY
	LDA.b [$0A]
	STA.b $06
	STY.b $08
	SEP.b #$20
	LDY.w #LandingSubpieceLengthOffset
	LDA.b [$06],Y
	REP.b #$20
	AND.w #LowByteMask
	ASL
	STA.b $02
	SEP.b #$20
	LDY.w #LandingSubpieceSourceBankOffset
	LDA.b [$06],Y
	REP.b #$20
	AND.w #LowByteMask
	STA.b $14
	LDY.b $16
	TYA
	ASL
	CLC
	ADC.w #LandingSubpieceEntryListOffset
	CLC
	ADC.b $06
	STA.b $06
	LDA.b [$06]
	AND.w #LandingSubpiecePointerAlignmentMask
	STA.b $12
	STA.b $06
	LDA.b $14
	STA.b $08
	LDA.b $06
	STA.b $0E
	LDA.b $08
	STA.b $10
	LDY.b $04
	LDX.b $02
	SEP.b #$20
	LDA.b #LandingVramTransferFlagsNone
	JSL.l C08616_TransferBlockToVramOrBuffer
	LDA.b $02
	CLC
	ADC.b $12
	STA.b $12
	STA.b $06
	LDA.b $14
	STA.b $08
	LDA.b $06
	STA.b $0E
	LDA.b $08
	STA.b $10
	LDA.b $04
	CLC
	ADC.w #LandingSubpieceSecondPlaneVramOffset
	TAY
	LDX.b $02
	SEP.b #$20
	LDA.b #LandingVramTransferFlagsNone
	JSL.l C08616_TransferBlockToVramOrBuffer
	LDA.b $02
	LSR
	STA.b $02
	LDA.b $04
	CLC
	ADC.b $02
C4B269_TransferLandingDisplayAssetSubpiecePair_Return:
	PLD
	RTS

; ---------------------------------------------------------------------------
; C4:B26B

; InitializeLandingDisplayStreamsAndChildAnchors
LOAD_OVERLAY_SPRITES:
C4B26B_InitializeLandingDisplayStreamsAndChildAnchors = LOAD_OVERLAY_SPRITES
	REP.b #$31
	PHD
	TDC
	ADC.w #$FFEC
	TCD
	LDA.w #LandingStreamInitialVramDestination
	STA.b $12
	LDA.w #LandingStreamDescriptorTable
	STA.b $0A
	LDA.w #LandingStreamDescriptorTable>>16
	STA.b $0C
	LDA.w #LandingStreamDescriptorFirstIndex
	STA.b $02
	BRA.b C4B2C9_InitializeLandingDisplayStreamsAndChildAnchors_CheckDescriptorLoop

C4B289_InitializeLandingDisplayStreamsAndChildAnchors_DescriptorLoop:
	LDA.b $0A
	STA.b $06
	LDA.b $0C
	STA.b $08
	SEP.b #$20
	LDY.w #LandingStreamFirstSubpieceOffset
	LDA.b [$0A],Y
	REP.b #$20
	AND.w #LowByteMask
	TAY
	LDA.b [$06]
	TAX
	LDA.b $12
	JSR.w C4B1B8_TransferLandingDisplayAssetSubpiecePair
	STA.b $10
	SEP.b #$20
	LDY.w #LandingStreamSecondSubpieceOffset
	LDA.b [$0A],Y
	REP.b #$20
	AND.w #LowByteMask
	TAY
	LDA.b [$06]
	TAX
	LDA.b $10
	JSR.w C4B1B8_TransferLandingDisplayAssetSubpiecePair
	STA.b $12
	LDA.w #LandingStreamDescriptorBytes
	CLC
	ADC.b $0A
	STA.b $0A
	INC.b $02
C4B2C9_InitializeLandingDisplayStreamsAndChildAnchors_CheckDescriptorLoop:
	LDA.l LandingStreamDescriptorCountByte
	AND.w #LowByteMask
	STA.b $04
	LDA.b $02
	CMP.b $04
	BCC.b C4B289_InitializeLandingDisplayStreamsAndChildAnchors_DescriptorLoop
	LDA.w #LandingStreamDescriptorFirstIndex
	STA.b $0E
	BRA.b C4B322_InitializeLandingDisplayStreamsAndChildAnchors_CheckStreamLoop

C4B2DF_InitializeLandingDisplayStreamsAndChildAnchors_StreamLoop:
	ASL
	TAX
	LDA.w #LandingStreamGroup2eb6Source
	STA.b $06
	LDA.w #LandingStreamGroup2eb6Source>>16
	STA.b $08
	LDA.b $06
	STA.w LandingStreamGroup2eb6Table,X
	LDA.w #LandingStreamGroup2f6aSource
	STA.b $06
	LDA.w #LandingStreamGroup2f6aSource>>16
	STA.b $08
	LDA.b $06
	STA.w LandingStreamGroup2f6aTable,X
	LDA.w #LandingStreamGroup301eSource
	STA.b $06
	LDA.w #LandingStreamGroup301eSource>>16
	STA.b $08
	LDA.b $06
	STA.w LandingStreamGroup301eTable,X
	LDA.w #LandingStreamGroup30d2Source
	STA.b $06
	LDA.w #LandingStreamGroup30d2Source>>16
	STA.b $08
	LDA.b $06
	STA.w LandingStreamGroup30d2Table,X
	LDA.b $0E
	INC
	STA.b $0E
C4B322_InitializeLandingDisplayStreamsAndChildAnchors_CheckStreamLoop:
	CMP.w #LandingStreamPointerSlotCount
	BCC.b C4B2DF_InitializeLandingDisplayStreamsAndChildAnchors_StreamLoop
	PLD
	RTL

