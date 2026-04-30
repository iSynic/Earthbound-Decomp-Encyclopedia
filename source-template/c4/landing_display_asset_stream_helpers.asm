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
	CPY.w #$00FF
	BNE.b C4B1D0_TransferLandingDisplayAssetSubpiecePair_LoadDescriptor
	LDA.b $04
	JMP.w C4B269_TransferLandingDisplayAssetSubpiecePair_Return

C4B1D0_TransferLandingDisplayAssetSubpiecePair_LoadDescriptor:
	LDA.w #DATA_EF133F
	STA.b $0A
	LDA.w #DATA_EF133F>>16
	STA.b $0C
	TXA
	ASL
	ASL
	CLC
	ADC.b $0A
	STA.b $0A
	LDY.w #$0002
	LDA.b [$0A],Y
	TAY
	LDA.b [$0A]
	STA.b $06
	STY.b $08
	SEP.b #$20
	LDY.w #$0001
	LDA.b [$06],Y
	REP.b #$20
	AND.w #$00FF
	ASL
	STA.b $02
	SEP.b #$20
	LDY.w #$0008
	LDA.b [$06],Y
	REP.b #$20
	AND.w #$00FF
	STA.b $14
	LDY.b $16
	TYA
	ASL
	CLC
	ADC.w #$0009
	CLC
	ADC.b $06
	STA.b $06
	LDA.b [$06]
	AND.w #$FFFE
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
	LDA.b #$00
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
	ADC.w #$0100
	TAY
	LDX.b $02
	SEP.b #$20
	LDA.b #$00
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
C4B26B_InitializeLandingDisplayStreamsAndChildAnchors:
	REP.b #$31
	PHD
	TDC
	ADC.w #$FFEC
	TCD
	LDA.w #$5600
	STA.b $12
	LDA.w #DATA_C40E32
	STA.b $0A
	LDA.w #DATA_C40E32>>16
	STA.b $0C
	LDA.w #$0000
	STA.b $02
	BRA.b C4B2C9_InitializeLandingDisplayStreamsAndChildAnchors_CheckDescriptorLoop

C4B289_InitializeLandingDisplayStreamsAndChildAnchors_DescriptorLoop:
	LDA.b $0A
	STA.b $06
	LDA.b $0C
	STA.b $08
	SEP.b #$20
	LDY.w #$0002
	LDA.b [$0A],Y
	REP.b #$20
	AND.w #$00FF
	TAY
	LDA.b [$06]
	TAX
	LDA.b $12
	JSR.w C4B1B8_TransferLandingDisplayAssetSubpiecePair
	STA.b $10
	SEP.b #$20
	LDY.w #$0003
	LDA.b [$0A],Y
	REP.b #$20
	AND.w #$00FF
	TAY
	LDA.b [$06]
	TAX
	LDA.b $10
	JSR.w C4B1B8_TransferLandingDisplayAssetSubpiecePair
	STA.b $12
	LDA.w #$0004
	CLC
	ADC.b $0A
	STA.b $0A
	INC.b $02
C4B2C9_InitializeLandingDisplayStreamsAndChildAnchors_CheckDescriptorLoop:
	LDA.l DATA_C40E31
	AND.w #$00FF
	STA.b $04
	LDA.b $02
	CMP.b $04
	BCC.b C4B289_InitializeLandingDisplayStreamsAndChildAnchors_DescriptorLoop
	LDA.w #$0000
	STA.b $0E
	BRA.b C4B322_InitializeLandingDisplayStreamsAndChildAnchors_CheckStreamLoop

C4B2DF_InitializeLandingDisplayStreamsAndChildAnchors_StreamLoop:
	ASL
	TAX
	LDA.w #DATA_C40EE4
	STA.b $06
	LDA.w #DATA_C40EE4>>16
	STA.b $08
	LDA.b $06
	STA.w $2EB6,X
	LDA.w #DATA_C40EB0
	STA.b $06
	LDA.w #DATA_C40EB0>>16
	STA.b $08
	LDA.b $06
	STA.w $2F6A,X
	LDA.w #DATA_C40EF0
	STA.b $06
	LDA.w #DATA_C40EF0>>16
	STA.b $08
	LDA.b $06
	STA.w $301E,X
	LDA.w #DATA_C40F04
	STA.b $06
	LDA.w #DATA_C40F04>>16
	STA.b $08
	LDA.b $06
	STA.w $30D2,X
	LDA.b $0E
	INC
	STA.b $0E
C4B322_InitializeLandingDisplayStreamsAndChildAnchors_CheckStreamLoop:
	CMP.w #$001E
	BCC.b C4B2DF_InitializeLandingDisplayStreamsAndChildAnchors_StreamLoop
	PLD
	RTL

